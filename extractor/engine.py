"""Engine skeleton from Sprint.md.

Typed classes that the `run.py` driver instantiates in order:
    SourceLoader -> IdentityResolver -> NoiseFilter -> FactExtractor
                 -> FactStore -> Merger
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Hashable, Iterable, Iterator, Optional

from .extract import extract_all
from .identity import Identity, IdentityResolver
from .models import Event, Fact


# ---------- 1. SourceLoader ----------

@dataclass
class SourceLoader:
    """Walks `raw/` and emits normalized Events from every connector."""
    root: Path
    include_incremental: bool = False

    def load(self) -> Iterator[tuple[str, Event, list[Fact]]]:
        yield from extract_all(self.root, include_incremental=self.include_incremental)


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
