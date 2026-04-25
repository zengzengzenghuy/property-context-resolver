"""Engine skeleton from Sprint.md.

Typed classes that the `run.py` driver instantiates in order:
    SourceLoader -> IdentityResolver -> NoiseFilter -> FactExtractor
                 -> FactStore -> Merger
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from datetime import date, timedelta
from pathlib import Path
from typing import Any, Hashable, Iterable, Iterator, Optional

from .extract import extract_all
from .identity import Identity, IdentityResolver
from .models import Event, Fact, PROPERTY_ID, stable_id


# ---------- 1. SourceLoader ----------

@dataclass
class SourceLoader:
    """Walks `raw/` and emits normalized Events from every connector."""
    root: Path
    include_incremental: bool = False
    resolver: Optional["IdentityResolver"] = None

    def load(self) -> Iterator[tuple[str, Event, list[Fact]]]:
        yield from extract_all(
            self.root,
            include_incremental=self.include_incremental,
            resolver=self.resolver,
        )


# ---------- 2. IdentityResolver — re-export for symmetry ----------

__all_identity__ = (IdentityResolver, Identity)


# ---------- 3. NoiseFilter ----------

@dataclass
class NoiseFilter:
    """Drop or downweight events that aren't worth extracting from.

    TODO:
    - filter quoted-reply tails / signature blocks
    - drop bank rows that are just internal Saldo-Übertraege
    """
    drop_auto_acks: bool = True

    def is_noise(self, event: Event) -> bool:
        if event.source == "email":
            subj = (event.metadata.get("subject") or "").lower()
            body = event.content.lower()
            if self.drop_auto_acks and "wir pruefen die angelegenheit" in body and subj.startswith("re:"):
                return True
        return False

    def filter(self, stream: Iterator[tuple[str, Event, list[Fact]]]) -> Iterator[tuple[str, Event, list[Fact]]]:
        for src, ev, facts in stream:
            if self.is_noise(ev):
                continue
            yield src, ev, facts


# ---------- 4. FactExtractor — identity-enrichment wrapper ----------

@dataclass
class FactExtractor:
    """Apply identity resolution to events whose facts came in unresolved."""
    resolver: IdentityResolver

    def enrich(self, event: Event, facts: list[Fact]) -> list[Fact]:
        if all(f.entity_id for f in facts):
            return facts
        ident = self._resolve_event(event)
        if ident is None:
            return facts
        out: list[Fact] = []
        for f in facts:
            if f.entity_id is None:
                out.append(Fact(
                    id=f.id,
                    property_id=f.property_id,
                    entity_type=ident.entity_type,
                    entity_id=ident.canonical_id,
                    key=f.key,
                    value=f.value,
                    source_event_id=f.source_event_id,
                    source_ref=f.source_ref,
                    confidence=min(f.confidence, ident.confidence),
                    observed_at=f.observed_at,
                    extracted_at=f.extracted_at,
                ))
            else:
                out.append(f)
        return out

    def _resolve_event(self, event: Event) -> Optional[Identity]:
        md = event.metadata or {}
        if event.source == "email":
            return self.resolver.resolve(
                email=md.get("from"),
                einheit_nr=(md.get("refs") or {}).get("einheit_nr", [None])[0],
            )
        if event.source == "bank":
            return self.resolver.resolve(
                iban=md.get("iban"),
                name=md.get("counterparty"),
            )
        return None


# ---------- 5. FactStore ----------

# Source priority for tie-breaking when multiple sources speak to the same key.
# Higher number wins. Globally applied — for v1 demo good enough; bank is the
# financial ground-truth, stammdaten is the contractual ground-truth, formal
# letters/invoices are next, emails are noisiest.
# TODO: per-key overrides (bank > stammdaten for payment keys, etc.)
SOURCE_PRIORITY: dict[str, int] = {
    "stammdaten": 4,
    "letter": 3,
    "invoice": 3,
    "bank": 3,
    "email": 1,
}

CONFIDENCE_FLOOR = 0.7  # facts below this never participate in conflict detection


_RAW_RE = re.compile(r"/raw/([^/]+)/")


def _source_from_ref(source_ref: str) -> str:
    """Recover the source name (`stammdaten`/`bank`/`email`/`invoice`/`letter`)
    from a fact's source_ref URL or local path. Used only for priority tie-break."""
    m = _RAW_RE.search(source_ref or "")
    if not m:
        return ""
    kind = m.group(1)
    return {
        "emails": "email",
        "rechnungen": "invoice",
        "briefe": "letter",
        # bank, stammdaten, incremental keep their bare names below
    }.get(kind, kind)


def _normalize_value(v: Any) -> Hashable:
    """Hashable canonical form of a fact value for dedup/conflict comparison."""
    if isinstance(v, str):
        return v.strip().lower()
    if isinstance(v, float):
        return round(v, 2)
    if isinstance(v, list):
        return tuple(sorted((_normalize_value(x) for x in v), key=repr))
    if isinstance(v, dict):
        return tuple(sorted(((k, _normalize_value(val)) for k, val in v.items()), key=repr))
    return v


def _priority_key(fact: Fact) -> tuple[float, str, int, str]:
    """Sort key for `latest()` and conflict-side selection. Higher = newer/stronger.

    Order: confidence > observed_at > source priority > extracted_at.
    """
    return (
        float(fact.confidence or 0.0),
        fact.observed_at or "",
        SOURCE_PRIORITY.get(_source_from_ref(fact.source_ref), 0),
        fact.extracted_at or "",
    )


class FactStore:
    """Append-only fact store, indexed by `(entity_id, key)`.

    Persistence is full audit log — every accepted fact stays on disk so re-runs
    are reproducible. Dedup never mutates; it appends a new "we saw this again"
    row only when the new fact carries newer observed_at or higher confidence.

    Facts with `entity_id is None` are persisted to JSONL but kept out of the
    bucket index — they're orphans (no resolved entity to render them under)
    and excluded from conflict detection.
    """

    def __init__(self) -> None:
        self._buckets: dict[tuple[str, str], list[Fact]] = {}
        self._unresolved: list[Fact] = []
        self._seen_ids: set[str] = set()

    # --- size / iteration ---

    def count(self) -> int:
        n = sum(len(b) for b in self._buckets.values())
        return n + len(self._unresolved)

    def all_facts(self) -> Iterator[Fact]:
        for bucket in self._buckets.values():
            yield from bucket
        yield from self._unresolved

    # --- writes ---

    def add(self, fact: Fact) -> bool:
        """Append a fact. Returns True if it changed the store, False if dropped.

        Dropped iff (a) we've already loaded a row with this fact.id, OR
        (b) the same normalized value is already in the bucket and the new
        fact has neither newer observed_at nor higher confidence.
        """
        if fact.id in self._seen_ids:
            return False
        self._seen_ids.add(fact.id)

        if fact.entity_id is None:
            self._unresolved.append(fact)
            return True

        key = (fact.entity_id, fact.key)
        bucket = self._buckets.setdefault(key, [])
        nv_new = _normalize_value(fact.value)

        for existing in bucket:
            if _normalize_value(existing.value) != nv_new:
                continue
            # Same value already known. Append the new row only if it's
            # strictly newer or stricter; otherwise drop silently.
            new_obs = fact.observed_at or ""
            old_obs = existing.observed_at or ""
            if new_obs > old_obs or fact.confidence > existing.confidence:
                bucket.append(fact)
                return True
            return False

        bucket.append(fact)
        return True

    def add_many(self, facts: Iterable[Fact]) -> int:
        return sum(1 for f in facts if self.add(f))

    # --- queries ---

    def latest(self, entity_id: str, key: str) -> Optional[Fact]:
        """Best-known fact for a key, by (confidence, observed_at, source priority)."""
        bucket = self._buckets.get((entity_id, key))
        if not bucket:
            return None
        return max(bucket, key=_priority_key)

    def conflicts(self, entity_id: str, key: str) -> list[Fact]:
        """Return one representative Fact per distinct value when ≥2 are above
        the confidence floor and disagree. Returns [] when not conflicted."""
        bucket = self._buckets.get((entity_id, key))
        if not bucket:
            return []
        by_value: dict[Hashable, list[Fact]] = {}
        for f in bucket:
            if f.confidence < CONFIDENCE_FLOOR:
                continue
            by_value.setdefault(_normalize_value(f.value), []).append(f)
        if len(by_value) < 2:
            return []
        # One representative per value (the strongest of that side), sorted strongest-first.
        reps = [max(group, key=_priority_key) for group in by_value.values()]
        reps.sort(key=_priority_key, reverse=True)
        return reps

    def is_conflicted(self, entity_id: str, key: str) -> bool:
        return bool(self.conflicts(entity_id, key))

    # --- persistence ---

    def write_jsonl(self, path: Path) -> int:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as f:
            for fact in self.all_facts():
                f.write(json.dumps(fact.to_json(), ensure_ascii=False, default=str))
                f.write("\n")
        return self.count()

    def load_jsonl(self, path: Path) -> int:
        """Rehydrate from a previous run. Dedupes by `fact.id` so re-running
        on the same input is a no-op."""
        if not path.exists():
            return 0
        added = 0
        with path.open(encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                d = json.loads(line)
                # Filter to fields Fact actually accepts (forward-compat).
                allowed = {
                    "id", "property_id", "entity_type", "entity_id",
                    "key", "value", "source_event_id", "source_ref",
                    "confidence", "observed_at", "extracted_at",
                }
                fact = Fact(**{k: d[k] for k in allowed if k in d})
                if self.add(fact):
                    added += 1
        return added


# ---------- 6. Merger + render helper ----------

def format_value(store: FactStore, entity_id: str, key: str) -> Optional[str]:
    """Render a single (entity, key) cell as Markdown.

    Conflicted → returns the surgical-update spec's `<!-- conflict -->` block,
    one line per competing value with citation + source + observed date.
    Resolved → returns `value [(source)](source_ref)`.
    Missing  → returns None.

    This helper is testable without a full section schema; the Merger calls
    it once Karl finalizes the templates.
    """
    if store.is_conflicted(entity_id, key):
        rows = []
        for f in store.conflicts(entity_id, key):
            src = _source_from_ref(f.source_ref) or "?"
            obs = f.observed_at or "n/a"
            rows.append(f"  - {f.value} [({src}, {obs})]({f.source_ref})")
        return "<!-- conflict -->\n" + "\n".join(rows) + "\n<!-- /conflict -->"
    fact = store.latest(entity_id, key)
    if fact is None:
        return None
    return f"{fact.value} [(source)]({fact.source_ref})"


@dataclass
class Merger:
    """Render the per-property `context.md` from the fact store.

    TODO (blocked on Karl's section schema):
    - section templates (Stammdaten / Eigentümer / Mietverhältnisse / …)
    - <!-- auto:section --> ... <!-- /auto --> blocks
    - surgical replacement of only changed keys; preserve human edits

    For now this just renders a flat dump using `format_value` per key, so the
    conflict-marker plumbing is exercised end-to-end before the schema lands.
    """
    fact_store: FactStore

    def render(self, property_id: str) -> str:
        # Placeholder skeleton — replaced once Karl delivers section templates.
        return f"# context for {property_id}\n"


# ---------- 7. DunningReconciler — flagship ----------

# § 288 (1) BGB: 5pp over the ECB base rate. ECB_BASE is fixed for the demo
# (real value per Bundesbank changes semi-annually; we have no live source).
ECB_BASE_PP = 3.5

# Sprint.md framework: a missed Miete is in Verzug 14 days after the due date,
# at which point Mahnstufe 1 applies. § 286 II Nr. 1 BGB anchors the 30-day
# default but the corpus operates on 14d so we follow the corpus.
DEFAULT_GRACE_DAYS = 14


def _parse_ym(iso: str) -> tuple[int, int]:
    """Return (year, month) from a YYYY-MM[-DD...] string."""
    parts = iso.split("-")
    return int(parts[0]), int(parts[1])


def _months_in(start_ym: tuple[int, int], end_ym: tuple[int, int]) -> Iterator[tuple[int, int]]:
    y, m = start_ym
    while (y, m) <= end_ym:
        yield y, m
        y, m = (y + 1, 1) if m == 12 else (y, m + 1)


@dataclass
class DunningReconciler:
    """Compute the dunning roll-up for the flagship tenant.

    Two-phase:
    1. Project per-Mahnung facts (`mahnung.stufe`, `mahnung.offener_betrag_eur`,
       `mahnung.betrifft`, `mahnung.date`) onto the tenant entity by resolving
       each Mahnung letter's `letter.recipient_name` via the IdentityResolver.
       This way the merger can list a tenant's Mahnungen without re-walking
       the letter side of the store.
    2. Walk months from `max(mietbeginn, bank-coverage-start)` → today, sum
       observed `payment.amount_eur` per period, compare to expected
       (`kaltmiete + nk_vorauszahlung`), and emit `dunning.*` summary facts:
       months_overdue_count, offener_betrag_eur, mahnstufe, verzugszinsen_eur,
       last_payment_date, summary_text.

    All emitted facts cite a real source_ref (a linked Mahnung PDF when one
    exists, else the most recent payment row, else the bank CSV) so the
    merger's `format_value` produces working `[(source)](url)` citations.
    """
    store: "FactStore"
    resolver: IdentityResolver
    today: str  # YYYY-MM-DD; reference date for the calc
    bank_csv_ref: str = ""  # canonical fallback citation
    coverage_start_ym: tuple[int, int] = (2024, 1)  # bank data starts 2024
    ecb_base_pp: float = ECB_BASE_PP
    grace_days: int = DEFAULT_GRACE_DAYS

    def reconcile(self, tenant_id: str) -> int:
        emitted = 0

        # 1. Lease parameters (the "expected" side of the equation).
        f_kalt = self.store.latest(tenant_id, "kaltmiete")
        f_nk = self.store.latest(tenant_id, "nk_vorauszahlung")
        f_beg = self.store.latest(tenant_id, "mietbeginn")
        f_end = self.store.latest(tenant_id, "mietende")
        f_unit = self.store.latest(tenant_id, "einheit_id")
        if not (f_kalt and f_nk and f_beg and f_unit):
            return 0
        try:
            expected_eur = round(float(f_kalt.value) + float(f_nk.value), 2)
        except (TypeError, ValueError):
            return 0
        einheit_id = f_unit.value
        mietbeginn = f_beg.value
        mietende = f_end.value if f_end else None

        # 2. Project Mahnungen onto the tenant. We walk every letter entity
        # whose recipient resolves to this tenant.
        tenant_mahnungen = self._mahnungen_for_tenant(tenant_id)
        for letter_facts in tenant_mahnungen:
            for key in ("mahnung.stufe", "mahnung.offener_betrag_eur",
                        "mahnung.betrifft", "mahnung.date", "mahnung.invoice_ref"):
                src = letter_facts.get(key)
                if src is not None and self._project(src, tenant_id):
                    emitted += 1

        # 3. Walk every month within bank coverage and reconcile.
        beg_ym = max(_parse_ym(mietbeginn), self.coverage_start_ym)
        end_iso = mietende if (mietende and mietende < self.today) else self.today
        end_ym = _parse_ym(end_iso)
        today_d = date.fromisoformat(self.today)

        months_overdue: list[dict[str, Any]] = []
        last_payment_date: Optional[str] = None
        last_payment_ref: Optional[str] = None
        last_payment_event_id: Optional[str] = None

        for ym in _months_in(beg_ym, end_ym):
            period = f"{ym[1]:02d}/{ym[0]:04d}"
            # Walk under the einheit AND the tenant: bank.py files payments
            # against EH-XXX when verwendungszweck encodes it, and falls back
            # to MIE-XXX (via IBAN match) when it doesn't.
            paid, latest_pay = self._sum_miete_for_period(
                [einheit_id, tenant_id], period,
            )
            if latest_pay is not None:
                pay_obs, pay_ref, pay_eid = latest_pay
                if last_payment_date is None or pay_obs > last_payment_date:
                    last_payment_date = pay_obs
                    last_payment_ref = pay_ref
                    last_payment_event_id = pay_eid

            due_d = date(ym[0], ym[1], 1)
            # A month is "in Verzug" only after due_date + grace_days.
            if today_d < due_d + timedelta(days=self.grace_days):
                continue
            short = round(expected_eur - paid, 2)
            if short > 0.005:
                months_overdue.append({
                    "period": period,
                    "expected": expected_eur,
                    "paid": paid,
                    "short": short,
                    "due_date": due_d.isoformat(),
                })

        offener_betrag = round(sum(m["short"] for m in months_overdue), 2)

        # § 288 BGB: 5pp + ECB base rate, applied per-month-short, time-weighted.
        rate = (5.0 + self.ecb_base_pp) / 100.0
        verzugszinsen = 0.0
        for m in months_overdue:
            due_d = date.fromisoformat(m["due_date"])
            days_due = (today_d - due_d).days - self.grace_days
            if days_due <= 0:
                continue
            verzugszinsen += m["short"] * rate * (days_due / 365.0)
        verzugszinsen = round(verzugszinsen, 2)

        # 4. Mahnstufe — max recorded letter stufe; else 1 if shortage exists; else 0.
        stufen: list[int] = []
        for letter_facts in tenant_mahnungen:
            sf = letter_facts.get("mahnung.stufe")
            if sf is None:
                continue
            try:
                stufen.append(int(sf.value))
            except (TypeError, ValueError):
                pass
        if stufen:
            mahnstufe = max(stufen)
        elif months_overdue:
            mahnstufe = 1
        else:
            mahnstufe = 0

        # 5. Pick the strongest source to cite. Prefer the most recent linked
        # Mahnung PDF; else the latest payment row; else the bare bank CSV.
        latest_letter: Optional[Fact] = None
        for letter_facts in tenant_mahnungen:
            ld = letter_facts.get("letter.date")
            if ld is None:
                continue
            if latest_letter is None or (ld.value or "") > (latest_letter.value or ""):
                latest_letter = ld
        primary_ref = (
            (latest_letter.source_ref if latest_letter else None)
            or last_payment_ref
            or self.bank_csv_ref
        )
        primary_event_id = (
            (latest_letter.source_event_id if latest_letter else None)
            or last_payment_event_id
            or stable_id("dunning", tenant_id, self.today)
        )
        bank_ref = last_payment_ref or self.bank_csv_ref or primary_ref
        bank_event_id = last_payment_event_id or stable_id("dunning", tenant_id, self.today, "bank")

        # 6. Emit the roll-up facts.
        def emit(key: str, value: Any, source_ref: str, source_event_id: str) -> None:
            nonlocal emitted
            if value is None:
                return
            f = Fact.make(
                property_id=PROPERTY_ID,
                entity_type="mieter",
                entity_id=tenant_id,
                key=key,
                value=value,
                source_event_id=source_event_id,
                source_ref=source_ref,
                observed_at=self.today,
                confidence=1.0,
            )
            if self.store.add(f):
                emitted += 1

        emit("dunning.mahnstufe", mahnstufe, primary_ref, primary_event_id)
        emit("dunning.months_overdue_count", len(months_overdue), bank_ref, bank_event_id)
        emit("dunning.offener_betrag_eur", offener_betrag, primary_ref, primary_event_id)
        emit("dunning.verzugszinsen_eur", verzugszinsen, bank_ref, bank_event_id)
        if last_payment_date:
            emit("dunning.last_payment_date", last_payment_date, bank_ref, bank_event_id)
        emit("dunning.expected_eur", expected_eur, primary_ref, primary_event_id)

        # 7. Pre-formatted German summary sentence — high-leverage for the LLM
        # answering "Ist X im Verzug?" in the demo.
        if months_overdue:
            verb = f"ist seit {len(months_overdue)} Monaten im Verzug"
        else:
            verb = "ist nicht im Verzug"
        summary = (
            f"Mieter {tenant_id} {verb}, offener Betrag {offener_betrag:.2f} EUR, "
            f"Mahnstufe {mahnstufe}, Verzugszinsen {verzugszinsen:.2f} EUR "
            f"(Berechnungsdatum {self.today}, § 288 BGB Basiszins "
            f"{self.ecb_base_pp:.1f}% + 5pp)."
        )
        emit("dunning.summary_text", summary, primary_ref, primary_event_id)

        return emitted

    # --- helpers ---

    def _project(self, src: Fact, tenant_id: str) -> bool:
        """Re-emit `src` under the tenant entity, preserving citation."""
        new_fact = Fact.make(
            property_id=src.property_id,
            entity_type="mieter",
            entity_id=tenant_id,
            key=src.key,
            value=src.value,
            source_event_id=src.source_event_id,
            source_ref=src.source_ref,
            observed_at=src.observed_at,
            confidence=src.confidence,
        )
        return self.store.add(new_fact)

    def _sum_miete_for_period(
        self, entity_ids, period: str,
    ) -> tuple[float, Optional[tuple[str, str, str]]]:
        """Sum Miete payments observed against any of `entity_ids` for `period`.
        Accepts a list because bank.py files some payments under the einheit
        (when EH-XXX is in verwendungszweck) and others under the tenant (when
        only the IBAN identifies them). Returns
        (total_eur, (latest_observed_at, source_ref, source_event_id) | None)."""
        if isinstance(entity_ids, str):
            entity_ids = [entity_ids]
        wanted = set(entity_ids)
        # Group facts under any of the wanted entities by source_event_id so
        # we can correlate amount/direction/period from a single bank row.
        by_event: dict[str, dict[str, Fact]] = {}
        for f in self.store.all_facts():
            if f.entity_id not in wanted:
                continue
            if not f.key.startswith("payment."):
                continue
            by_event.setdefault(f.source_event_id, {})[f.key] = f

        total = 0.0
        latest: Optional[tuple[str, str, str]] = None
        for ev_id, fmap in by_event.items():
            kind_f = fmap.get("payment.kind")
            if kind_f and kind_f.value != "miete":
                continue
            dir_f = fmap.get("payment.direction")
            if dir_f and dir_f.value != "credit":
                continue
            amt_f = fmap.get("payment.amount_eur")
            if amt_f is None:
                continue

            period_f = fmap.get("payment.miete_period")
            if period_f is not None:
                if period_f.value != period:
                    continue
            else:
                # Fallback: bank rows occasionally show `Miete <name>` without
                # the canonical `MM/YYYY` token. When this happens we trust the
                # booking date as the period — the rent month a payment lands
                # in is the month it was for, and `kind=miete` already guards
                # against hausgeld / vendor payments getting swept in.
                inferred = self._period_from_observed(amt_f.observed_at)
                if inferred != period:
                    continue

            try:
                total += float(amt_f.value)
            except (TypeError, ValueError):
                continue
            obs_at = amt_f.observed_at or ""
            if latest is None or obs_at > latest[0]:
                latest = (obs_at, amt_f.source_ref, amt_f.source_event_id)
        return total, latest

    @staticmethod
    def _period_from_observed(observed_at: Optional[str]) -> str:
        if not observed_at:
            return ""
        try:
            y, m = _parse_ym(observed_at)
            return f"{m:02d}/{y:04d}"
        except (ValueError, IndexError):
            return ""

    def _mahnungen_for_tenant(self, tenant_id: str) -> list[dict[str, Fact]]:
        """Group letter facts by letter id; keep only Mahnungen whose recipient
        name resolves (via IdentityResolver) to `tenant_id`."""
        by_letter: dict[str, dict[str, Fact]] = {}
        for f in self.store.all_facts():
            if f.entity_type != "letter" or not f.entity_id:
                continue
            by_letter.setdefault(f.entity_id, {})[f.key] = f
        out: list[dict[str, Fact]] = []
        for fmap in by_letter.values():
            kind_f = fmap.get("letter.kind")
            if kind_f is None or kind_f.value != "mahnung":
                continue
            rec_f = fmap.get("letter.recipient_name")
            if rec_f is None:
                continue
            ident = self.resolver.by_name(rec_f.value)
            if ident is None or ident.canonical_id != tenant_id:
                continue
            out.append(fmap)
        return out
