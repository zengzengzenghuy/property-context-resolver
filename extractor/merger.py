"""Merger — render `context.md` from the FactStore, surgically.

Replaces the placeholder `Merger.render()` in `engine.py`. The Merger only
writes inside `<!-- auto:NAME -->` ... `<!-- /auto:NAME -->` blocks; everything
outside (incl. ## Notes) is preserved across runs. The first run materializes
a full scaffold from `_SCAFFOLD`; subsequent runs replace only the auto-block
bodies, so a `git diff` highlights exactly what the engine changed.

Scalar fields go through `format_value` (in `engine.py`) which emits either
`value [(source)](source_ref)` or a `<!-- conflict --> ... <!-- /conflict -->`
block. Time-series sections (Payments, Communications) render as Markdown
tables grouped by `source_event_id` — these keys are NOT in `SCALAR_KEYS` per
CLAUDE.md and must not pass through `format_value`.

Hour 3-4 will populate the `legal_disputes` block with the dunning roll-up
(Mahnstufe + § 288 BGB Verzugszinsen). For now it carries a placeholder so
the auto-marker exists and the surgical-update path is exercised.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Optional

from .engine import FactStore, format_value, _source_from_ref
from .models import Fact

PROPERTY_ID = "LIE-001"
FLAGSHIP_TENANT = "MIE-001"

# Resolved at render time: which einheit MIE-001 lives in. Cached on the
# Merger instance so we only ask the store once per render.

# ---------- Section schema ----------
#
# Each entry describes exactly one <!-- auto:NAME --> block. The Merger walks
# this list in order and renders each block's body. Block ordering also
# determines the order they appear in the scaffold on first run.

SCALAR_SECTIONS = [
    # block_name,           heading,                                entity_resolver,        fields
    ("property_meta",       "## Property",                          lambda m: PROPERTY_ID,  [
        ("Name",            "name"),
        ("Strasse",         "strasse"),
        ("PLZ",             "plz"),
        ("Ort",             "ort"),
        ("Baujahr",         "baujahr"),
        ("Sanierung",       "sanierung"),
        ("Verwalter",       "verwalter"),
        ("Verwalter Email", "verwalter_email"),
        ("Verwalter Telefon","verwalter_telefon"),
        ("WEG-Bankkonto IBAN","weg_bankkonto_iban"),
        ("Rücklage IBAN",   "ruecklage_iban"),
    ]),
    ("tenant_lease",        "## Node: Lease & Contract",            lambda m: FLAGSHIP_TENANT, [
        ("Tenant ID",       None),  # rendered as static FLAGSHIP_TENANT label, no fact lookup
        ("Anrede",          "anrede"),
        ("Vorname",         "vorname"),
        ("Nachname",        "nachname"),
        ("Einheit",         "einheit_id"),
        ("Eigentümer",      "eigentuemer_id"),
        ("Sprache",         "sprache"),
        ("Mietbeginn",      "mietbeginn"),
        ("Mietende",        "mietende"),
        ("Kaltmiete (EUR)", "kaltmiete"),
        ("NK-Vorauszahlung (EUR)","nk_vorauszahlung"),
        ("Kaution (EUR)",   "kaution"),
    ]),
    ("tenant_banking",      "## Node: Payments & Banking — Stammdaten", lambda m: FLAGSHIP_TENANT, [
        ("Email",           "email"),
        ("Telefon",         "telefon"),
        ("IBAN",            "iban"),
        ("BIC",             "bic"),
    ]),
]

# Time-series sections: entity_id resolved at render time so we can follow the
# tenant → einheit indirection (payments are bucketed under einheit_id, not
# mieter_id, by `extractor/sources/bank.py`).

TIMESERIES_SECTIONS = [
    {
        "name": "payments_history",
        "heading": "## Node: Payments & Banking — History",
        "entity_resolver": lambda m: m.tenant_unit() or FLAGSHIP_TENANT,
        "key_prefix": "payment.",
        "columns": [
            ("Date",            "_observed_at"),
            ("Amount EUR",      "payment.amount_eur"),
            ("Direction",       "payment.direction"),
            ("Kind",            "payment.kind"),
            ("Period",          "payment.miete_period"),
            ("Verwendungszweck","payment.verwendungszweck"),
            ("Counterparty",    "payment.counterparty"),
        ],
        "limit": 12,
    },
    {
        "name": "communications",
        "heading": "## Node: Communications",
        "entity_resolver": lambda m: FLAGSHIP_TENANT,
        "key_prefix": "communication.",
        "columns": [
            ("Date",        "_observed_at"),
            ("From",        "communication.from"),
            ("Subject",     "communication.subject"),
            ("Intent",      "communication.intent"),
        ],
        "limit": 12,
    },
]

# Static (non-fact) sections — placeholders kept inside auto-blocks so future
# Hours can drop in roll-ups without touching the surgical-update plumbing.

STATIC_SECTIONS = [
    ("maintenance",         "## Node: Maintenance",
        "_(no maintenance facts surfaced in v1 — extend Hour 5+.)_"),
]

# Legal / Disputes is rendered dynamically — the dunning roll-up + per-Mahnung
# table are derived facts from `DunningReconciler`. See `_legal_disputes_block`.
LEGAL_DISPUTES_FIELDS = [
    ("Mahnstufe",                 "dunning.mahnstufe"),
    ("Monate im Verzug",          "dunning.months_overdue_count"),
    ("Offener Betrag (EUR)",      "dunning.offener_betrag_eur"),
    ("Verzugszinsen (EUR)",       "dunning.verzugszinsen_eur"),
    ("Erwartete Monatsmiete (EUR)","dunning.expected_eur"),
    ("Letzte Mietzahlung",        "dunning.last_payment_date"),
]

LEGAL_DISPUTES_HEADING = "## Node: Legal / Disputes"

# Order in which blocks appear when scaffolding the file from scratch.
_BLOCK_ORDER = [
    "property_meta",
    "tenant_lease",
    "tenant_banking",
    "payments_history",
    "communications",
    "maintenance",
    "legal_disputes",
]


# ---------- Auto-block primitives ----------

_BLOCK_RE_TMPL = re.compile(
    r"<!--\s*auto:(?P<name>[A-Za-z0-9_\-]+)\s*-->"
    r"(?P<body>.*?)"
    r"<!--\s*/auto:(?P=name)\s*-->",
    re.DOTALL,
)


def _wrap(name: str, body: str) -> str:
    return f"<!-- auto:{name} -->\n{body.rstrip()}\n<!-- /auto:{name} -->"


def _replace_blocks(existing: str, rendered: dict[str, str]) -> tuple[str, set[str]]:
    """Replace each auto-block body in `existing` with `rendered[name]`.

    Returns (new_text, names_replaced). Names in `rendered` that didn't appear
    in `existing` are returned by the caller for append-handling.
    """
    seen: set[str] = set()

    def sub(m: re.Match[str]) -> str:
        name = m.group("name")
        if name in rendered:
            seen.add(name)
            return _wrap(name, rendered[name])
        return m.group(0)  # untouched — engine doesn't own this block name

    return _BLOCK_RE_TMPL.sub(sub, existing), seen


# ---------- Render helpers ----------

def _scalar_block(store: FactStore, entity_id: str,
                  fields: list[tuple[str, Optional[str]]]) -> str:
    """Markdown bullet list, one row per field. Missing keys render as
    `_(not in store)_` so the section never silently drops fields."""
    lines: list[str] = []
    for label, key in fields:
        if key is None:
            # Static label (e.g., the tenant id row).
            lines.append(f"- **{label}:** {entity_id}")
            continue
        rendered = format_value(store, entity_id, key)
        if rendered is None:
            lines.append(f"- **{label}:** _(not in store)_")
        elif rendered.startswith("<!-- conflict"):
            # Render the conflict block on its own lines so the bullet stays
            # readable; the marker still survives the round-trip.
            lines.append(f"- **{label}:**\n{rendered}")
        else:
            lines.append(f"- **{label}:** {rendered}")
    return "\n".join(lines)


def _group_timeseries(store: FactStore, entity_id: str,
                      key_prefix: str) -> list[dict[str, Fact]]:
    """Group facts under (entity_id, key.startswith(prefix)) by source_event_id."""
    by_event: dict[str, dict[str, Fact]] = {}
    for fact in store.all_facts():
        if fact.entity_id != entity_id:
            continue
        if not fact.key.startswith(key_prefix):
            continue
        by_event.setdefault(fact.source_event_id, {})[fact.key] = fact
    return list(by_event.values())


def _md_escape(s: Any) -> str:
    """Cell-safe — collapse newlines and escape pipes so tables don't shatter."""
    return str(s).replace("|", "\\|").replace("\n", " ").strip()


def _legal_disputes_block(store: FactStore, tenant_id: str) -> str:
    """Render the dunning roll-up + linked Mahnung list for `tenant_id`.

    Layout:
      1. The pre-formatted summary sentence (cited) — high-leverage for LLM.
      2. Bullet list of the four flagship numbers (Mahnstufe, offener Betrag,
         Monate im Verzug, Verzugszinsen) via `format_value` so each cell
         carries a working citation back to the source PDF / bank row.
      3. Markdown table of any Mahnungen tied to this tenant, sorted newest
         first. Empty-state line when there are none.
    """
    parts: list[str] = []

    summary = format_value(store, tenant_id, "dunning.summary_text")
    if summary:
        parts.append(f"**Status:** {summary}")
        parts.append("")

    bullets: list[str] = []
    for label, key in LEGAL_DISPUTES_FIELDS:
        rendered = format_value(store, tenant_id, key)
        if rendered is None:
            bullets.append(f"- **{label}:** _(not in store)_")
        elif rendered.startswith("<!-- conflict"):
            bullets.append(f"- **{label}:**\n{rendered}")
        else:
            bullets.append(f"- **{label}:** {rendered}")
    parts.extend(bullets)

    # Mahnungen list (one row per linked Mahnung event, newest first).
    mahnung_rows = _group_timeseries(store, tenant_id, "mahnung.")
    if not mahnung_rows:
        parts.append("")
        parts.append("_Keine Mahnungen für diesen Mieter im Archiv._")
        return "\n".join(parts)

    parts.append("")
    parts.append("**Mahnungen:**")
    parts.append("")
    parts.append("| Datum | Stufe | Offener Betrag (EUR) | Betrifft | Source |")
    parts.append("| --- | --- | --- | --- | --- |")
    mahnung_rows.sort(
        key=lambda r: (r.get("mahnung.date") or r.get("mahnung.stufe")).observed_at or "",
        reverse=True,
    )
    for row in mahnung_rows:
        any_fact = next(iter(row.values()))
        date_v = (row.get("mahnung.date").value if "mahnung.date" in row else "—")
        stufe_v = (row.get("mahnung.stufe").value if "mahnung.stufe" in row else "—")
        offen_v = (row.get("mahnung.offener_betrag_eur").value
                   if "mahnung.offener_betrag_eur" in row else "—")
        betrifft_v = (row.get("mahnung.betrifft").value
                      if "mahnung.betrifft" in row else "—")
        src = _source_from_ref(any_fact.source_ref) or "?"
        parts.append(
            f"| {_md_escape(date_v)} | {_md_escape(stufe_v)} | "
            f"{_md_escape(offen_v)} | {_md_escape(betrifft_v)} | "
            f"[({src})]({any_fact.source_ref}) |"
        )
    return "\n".join(parts)


def _timeseries_block(store: FactStore, entity_id: str,
                      key_prefix: str,
                      columns: list[tuple[str, str]],
                      limit: int) -> str:
    rows = _group_timeseries(store, entity_id, key_prefix)
    if not rows:
        return f"_(no `{key_prefix}*` facts for {entity_id})_"

    def row_observed_at(row: dict[str, Fact]) -> str:
        return max((f.observed_at or "" for f in row.values()), default="")

    rows.sort(key=row_observed_at, reverse=True)
    rows = rows[:limit]

    headers = [h for h, _ in columns]
    sep = ["---"] * len(columns)
    lines = ["| " + " | ".join(headers) + " |",
             "| " + " | ".join(sep) + " |"]

    for row in rows:
        cells: list[str] = []
        # Pick one representative source_ref — first non-empty wins so the row
        # carries one citation even though the cells came from N facts.
        any_fact = next(iter(row.values()))
        for _, fkey in columns:
            if fkey == "_observed_at":
                cells.append(_md_escape(row_observed_at(row) or "—"))
                continue
            f = row.get(fkey)
            cells.append(_md_escape(f.value) if f is not None else "—")
        # Citation column appended at end so it doesn't compete with data.
        src = _source_from_ref(any_fact.source_ref) or "?"
        cells.append(f"[({src})]({any_fact.source_ref})")
        lines.append("| " + " | ".join(cells) + " |")

    # Append a citation header at table end so the column count matches.
    lines[0] = lines[0][:-2] + " | Source |"
    lines[1] = lines[1][:-2] + " | --- |"

    return "\n".join(lines)


# ---------- Surgical Merger ----------

@dataclass
class SurgicalMerger:
    """Renders the per-property `context.md` and writes it surgically.

    Replaces `engine.Merger`. The `render` API is the same so `run.py` keeps
    working; the difference is `render_to_file` — it preserves anything
    outside `<!-- auto:NAME -->` blocks across runs.
    """
    fact_store: FactStore
    _unit_cache: Optional[str] = None

    def tenant_unit(self) -> Optional[str]:
        """Resolve which einheit the flagship tenant lives in. Cached per render."""
        if self._unit_cache is not None:
            return self._unit_cache
        f = self.fact_store.latest(FLAGSHIP_TENANT, "einheit_id")
        self._unit_cache = f.value if f else None
        return self._unit_cache

    # -- block-by-block render --

    def _render_blocks(self) -> dict[str, str]:
        out: dict[str, str] = {}

        for name, _heading, ent_resolver, fields in SCALAR_SECTIONS:
            entity_id = ent_resolver(self)
            out[name] = _scalar_block(self.fact_store, entity_id, fields)

        for spec in TIMESERIES_SECTIONS:
            entity_id = spec["entity_resolver"](self)
            out[spec["name"]] = _timeseries_block(
                self.fact_store,
                entity_id,
                spec["key_prefix"],
                spec["columns"],
                spec["limit"],
            )

        for name, _heading, body in STATIC_SECTIONS:
            out[name] = body

        out["legal_disputes"] = _legal_disputes_block(self.fact_store, FLAGSHIP_TENANT)

        return out

    def _scaffold(self, blocks: dict[str, str]) -> str:
        """Full file body for first run (or when file is absent / blockless)."""
        lines = [
            f"# Property Context — {PROPERTY_ID}",
            "",
            "_Generated by `property-context-resolver`. Anything inside "
            "`<!-- auto:NAME -->` blocks is engine-managed and will be "
            "rewritten on the next run. Everything else (incl. ## Human Notes "
            "below) is preserved._",
            "",
        ]

        # Match name → heading from any of the section lists.
        heading_for: dict[str, str] = {}
        for name, heading, _r, _f in SCALAR_SECTIONS:
            heading_for[name] = heading
        for spec in TIMESERIES_SECTIONS:
            heading_for[spec["name"]] = spec["heading"]
        for name, heading, _b in STATIC_SECTIONS:
            heading_for[name] = heading
        heading_for["legal_disputes"] = LEGAL_DISPUTES_HEADING

        for name in _BLOCK_ORDER:
            lines.append(heading_for[name])
            lines.append("")
            lines.append(_wrap(name, blocks[name]))
            lines.append("")

        lines.extend([
            "---",
            "",
            "## Human Notes",
            "",
            "_(Free-form notes by the property manager. Engine never touches "
            "this section.)_",
            "",
        ])
        return "\n".join(lines)

    # -- public API --

    def render(self, property_id: str) -> str:
        """Render a fresh scaffold (no surgical merge). Used for tests + the
        `Merger` interface compatibility expected by `run.py`."""
        if property_id != PROPERTY_ID:
            return f"# context for {property_id}\n_(no schema configured for this property — only {PROPERTY_ID} supported in v1.)_\n"
        return self._scaffold(self._render_blocks())

    def render_to_file(self, path: Path) -> tuple[str, dict[str, Any]]:
        """Surgically write `path`. Returns `(new_text, stats)`.

        stats keys: blocks_replaced, blocks_appended, blocks_scaffolded,
        wrote_fresh (bool), payment_rows, communication_rows.
        """
        blocks = self._render_blocks()
        existing = path.read_text(encoding="utf-8") if path.exists() else ""
        has_any_block = bool(_BLOCK_RE_TMPL.search(existing))

        if not existing.strip() or not has_any_block:
            new_text = self._scaffold(blocks)
            stats = {
                "wrote_fresh": True,
                "blocks_replaced": 0,
                "blocks_appended": 0,
                "blocks_scaffolded": len(blocks),
            }
        else:
            new_text, replaced = _replace_blocks(existing, blocks)
            missing = [n for n in _BLOCK_ORDER if n not in replaced]
            if missing:
                # Append any blocks that aren't yet in the file (schema grew).
                appended_lines = [new_text.rstrip(), "", "<!-- engine-appended sections (schema extended) -->"]
                for name in missing:
                    appended_lines.append("")
                    appended_lines.append(_wrap(name, blocks[name]))
                new_text = "\n".join(appended_lines) + "\n"
            stats = {
                "wrote_fresh": False,
                "blocks_replaced": len(replaced),
                "blocks_appended": len(missing),
                "blocks_scaffolded": 0,
            }

        # Atomic write: tmp → rename so partial state never lands on disk.
        tmp = path.with_suffix(path.suffix + ".tmp")
        tmp.write_text(new_text, encoding="utf-8")
        tmp.replace(path)

        # One-line stats useful for the `context_updates` audit row.
        unit = self.tenant_unit() or FLAGSHIP_TENANT
        stats["payment_rows"] = len(_group_timeseries(self.fact_store, unit, "payment."))
        stats["communication_rows"] = len(_group_timeseries(self.fact_store, FLAGSHIP_TENANT, "communication."))
        stats["mahnung_rows"] = len(_group_timeseries(self.fact_store, FLAGSHIP_TENANT, "mahnung."))
        return new_text, stats


# Back-compat alias — `run.py` currently imports `Merger` from `extractor.engine`.
# We re-export the surgical implementation under the same name so the swap is
# a one-line import change.
Merger = SurgicalMerger
