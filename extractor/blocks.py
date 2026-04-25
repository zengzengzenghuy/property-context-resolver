"""Block render registry.

One render function per `<!-- auto:NAME -->` block defined in
`context.property.template.md` and `context.unit.template.md`. The Merger
walks the registry; each fn takes `(store, ctx)` and returns the markdown
body that goes inside the auto-block markers.

Empty blocks render `_(no data in source yet)_` rather than disappearing,
so the schema is always present and surgical updates remain stable.
"""

from __future__ import annotations

import re
from datetime import date as _date
from datetime import datetime, timezone
from typing import Any, Callable, Iterable, Optional

from .engine import FactStore, _source_from_ref, format_value
from .models import Fact


# ---------- helpers ----------

EMPTY = "_(no data in source yet)_"


def _md_escape(s: Any) -> str:
    """Cell-safe — collapse newlines and escape pipes so tables don't shatter."""
    return str(s).replace("|", "\\|").replace("\n", " ").strip()


def _latest_value(store: FactStore, eid: str, key: str, default: Any = None) -> Any:
    f = store.latest(eid, key)
    return f.value if f else default


def _cited(store: FactStore, eid: str, key: str, fallback: str = EMPTY) -> str:
    """Wrap format_value with a fallback for missing keys."""
    out = format_value(store, eid, key)
    return out if out else fallback


def _entity_ids_by_type(store: FactStore, etype: str) -> list[str]:
    seen: set[str] = set()
    for fact in store.all_facts():
        if fact.entity_type == etype and fact.entity_id:
            seen.add(fact.entity_id)
    return sorted(seen)


def _group_facts_by_event(
    store: FactStore, eid: str, key_prefix: str,
) -> list[dict[str, Fact]]:
    by_event: dict[str, dict[str, Fact]] = {}
    for fact in store.all_facts():
        if fact.entity_id != eid:
            continue
        if not fact.key.startswith(key_prefix):
            continue
        by_event.setdefault(fact.source_event_id, {})[fact.key] = fact
    return list(by_event.values())


def _bullets(rows: list[tuple[str, str]]) -> str:
    """List of `(label, rendered)` pairs → bullet markdown."""
    out: list[str] = []
    for label, rendered in rows:
        if rendered.startswith("<!-- conflict"):
            out.append(f"- {label}:\n{rendered}")
        else:
            out.append(f"- {label}: {rendered}")
    return "\n".join(out) if out else EMPTY


def _empty_table(headers: list[str]) -> str:
    sep = ["---"] * len(headers)
    return (
        "| " + " | ".join(headers) + " |\n"
        + "| " + " | ".join(sep) + " |\n"
        + EMPTY
    )


def _table(headers: list[str], rows: list[list[str]]) -> str:
    if not rows:
        return _empty_table(headers)
    sep = ["---"] * len(headers)
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(sep) + " |",
    ]
    for r in rows:
        lines.append("| " + " | ".join(_md_escape(c) for c in r) + " |")
    return "\n".join(lines)


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


# ---------- shared blocks ----------

def render_property_meta(store: FactStore, ctx: dict[str, Any]) -> str:
    return _bullets([
        ("last_built_at", f"`{_now_iso()}`"),
        ("build_hash", f"`{ctx.get('build_hash', 'engine-v2')}`"),
        ("engine_version", f"`{ctx.get('engine_version', '0.2.0')}`"),
        ("schema_version", "`spine-v2-split` (2026-04-25)"),
        ("file_role", "`property`"),
    ])


def render_unit_meta(store: FactStore, ctx: dict[str, Any]) -> str:
    unit_id = ctx["unit_id"]
    # owner_ref: walk eigentuemer, find one whose einheit_ids includes this unit
    owner_ref = "—"
    for eig in _entity_ids_by_type(store, "eigentuemer"):
        f = store.latest(eig, "einheit_ids")
        if f and isinstance(f.value, list) and unit_id in f.value:
            owner_ref = f"`{eig}`"
            break
    parent = "`context.property.LIE-001.md`"
    return _bullets([
        ("last_built_at", f"`{_now_iso()}`"),
        ("build_hash", f"`{ctx.get('build_hash', 'engine-v2')}`"),
        ("engine_version", f"`{ctx.get('engine_version', '0.2.0')}`"),
        ("schema_version", "`spine-v2-split` (2026-04-25)"),
        ("file_role", "`unit`"),
        ("parent_property_ref", parent),
        ("owner_ref", owner_ref),
    ])


def _bucket_provenance(
    store: FactStore,
    predicate: Callable[[Fact], bool],
    *,
    aggregate: bool = True,
) -> list[list[str]]:
    """Group facts by (source_kind, parent-directory) and emit one row each.

    `aggregate=True` (property scale) collapses thousands of emails into one
    `email | emails/2025-07 | 234 files` row.
    `aggregate=False` (unit scale) keeps one row per file — unit-scoped
    provenance is small enough to enumerate.
    """
    if aggregate:
        buckets: dict[tuple[str, str], dict[str, Any]] = {}
        for fact in store.all_facts():
            if not predicate(fact):
                continue
            ref = (fact.source_ref or "").split("#", 1)[0]
            if not ref:
                continue
            kind = _source_from_ref(ref) or "external"
            path = ref.split("/raw/", 1)[-1] if "/raw/" in ref else ref
            parent = path.rsplit("/", 1)[0] if "/" in path else path
            key = (kind, parent)
            b = buckets.setdefault(key, {"files": set(), "last": "", "ref": ref})
            b["files"].add(ref)
            obs = fact.observed_at or fact.extracted_at or ""
            if obs > b["last"]:
                b["last"] = obs
                b["ref"] = ref
        rows: list[list[str]] = []
        for (kind, parent), b in sorted(buckets.items()):
            n = len(b["files"])
            label = f"{parent}/" if n > 1 else parent
            rows.append([
                f"`{kind}-{re.sub(r'[^A-Za-z0-9]+', '-', parent)[:30] or 'src'}`",
                kind,
                f"[{label} ({n} files)]({b['ref']})" if n > 1 else f"[{parent}]({b['ref']})",
                b["last"] or "—",
            ])
        return rows

    by_ref: dict[str, tuple[str, str]] = {}
    last_seen: dict[str, str] = {}
    for fact in store.all_facts():
        if not predicate(fact):
            continue
        ref = (fact.source_ref or "").split("#", 1)[0]
        if not ref:
            continue
        kind = _source_from_ref(ref) or "external"
        sid = re.sub(r"[^A-Za-z0-9_\-]+", "-", ref.rsplit("/", 1)[-1])[:40]
        by_ref[ref] = (sid or "src", kind)
        observed = fact.observed_at or fact.extracted_at or ""
        if observed > last_seen.get(ref, ""):
            last_seen[ref] = observed
    rows = []
    for ref, (sid, kind) in sorted(by_ref.items()):
        path = ref.split("/raw/", 1)[-1] if "/raw/" in ref else ref
        rows.append([f"`{sid}`", kind, f"[{path}]({ref})", last_seen.get(ref, "—")])
    return rows


def render_property_provenance(store: FactStore, ctx: dict[str, Any]) -> str:
    # Aggregated: ~6k email files collapse to one row per (kind, directory).
    rows = _bucket_provenance(store, lambda f: True, aggregate=True)
    return _table(["source-id", "type", "path", "last_seen"], rows)


def render_unit_provenance(store: FactStore, ctx: dict[str, Any]) -> str:
    unit_id = ctx["unit_id"]
    tenant_ids = ctx.get("tenant_ids") or []
    relevant_entities = {unit_id, *tenant_ids}

    def _scope(f: Fact) -> bool:
        if f.entity_id in relevant_entities:
            return True
        if f.entity_type == "letter":
            ref = (f.source_ref or "")
            if any(t in ref for t in tenant_ids):
                return True
        return False

    rows = _bucket_provenance(store, _scope, aggregate=False)
    return _table(["source-id", "type", "path", "last_seen"], rows)


# ---------- property § 1 ----------

def render_property_display_name(store: FactStore, ctx: dict[str, Any]) -> str:
    name = _latest_value(store, ctx["property_id"], "name", default="(unbenannt)")
    return str(name)


def render_property(store: FactStore, ctx: dict[str, Any]) -> str:
    pid = ctx["property_id"]
    strasse = _latest_value(store, pid, "strasse", "")
    plz = _latest_value(store, pid, "plz", "")
    ort = _latest_value(store, pid, "ort", "")
    addr = ", ".join(p for p in [strasse, f"{plz} {ort}".strip()] if p) or EMPTY
    haus_ids = _entity_ids_by_type(store, "gebaeude")
    total_units = len(_entity_ids_by_type(store, "einheit"))
    bank_iban = _cited(store, pid, "weg_bankkonto_iban")
    bank_bank = _cited(store, pid, "weg_bankkonto_bank")
    ruecklage_iban = _cited(store, pid, "ruecklage_iban")
    return _bullets([
        ("property_id", f"`{pid}`"),
        ("address", addr),
        ("property_type", "`residential`"),
        ("legal_form", "`WEG`"),
        ("year_built", _cited(store, pid, "baujahr")),
        ("year_renovated", _cited(store, pid, "sanierung")),
        ("total_units", str(total_units) if total_units else EMPTY),
        ("houses", ", ".join(f"`{h}`" for h in haus_ids) if haus_ids else EMPTY),
        ("bank_accounts.hausgeld",
         f"{{ iban: {bank_iban}, bank: {bank_bank} }}"),
        ("bank_accounts.ruecklage",
         f"{{ iban: {ruecklage_iban} }}"),
        ("documents", EMPTY),
    ])


def render_owners(store: FactStore, ctx: dict[str, Any]) -> str:
    headers = ["owner_id", "name", "share_‰ (MEA)", "unit_refs", "contact",
               "reporting_pref", "sale_intent", "beirat"]
    rows: list[list[str]] = []
    for eid in _entity_ids_by_type(store, "eigentuemer"):
        firma = _latest_value(store, eid, "firma")
        if firma:
            name = firma
        else:
            v = _latest_value(store, eid, "vorname", "")
            n = _latest_value(store, eid, "nachname", "")
            name = f"{v} {n}".strip() or eid
        unit_refs = _latest_value(store, eid, "einheit_ids", []) or []
        unit_str = ", ".join(unit_refs) if isinstance(unit_refs, list) else str(unit_refs)
        email = _latest_value(store, eid, "email", "")
        beirat = _latest_value(store, eid, "beirat", False)
        # share_‰: sum miteigentumsanteil for each owned einheit
        share = 0
        if isinstance(unit_refs, list):
            for u in unit_refs:
                f = store.latest(u, "miteigentumsanteil")
                if f and f.value is not None:
                    try:
                        share += int(f.value)
                    except (TypeError, ValueError):
                        pass
        rows.append([
            f"`{eid}`",
            name,
            str(share) if share else "—",
            unit_str or "—",
            email or "—",
            "—",
            "none",
            "True" if beirat else "—",
        ])
    return _table(headers, rows)


def render_mandate(store: FactStore, ctx: dict[str, Any]) -> str:
    pid = ctx["property_id"]
    return _bullets([
        ("manager", _cited(store, pid, "verwalter")),
        ("contact_email", _cited(store, pid, "verwalter_email")),
        ("contact_phone", _cited(store, pid, "verwalter_telefon")),
        ("iban", _cited(store, pid, "verwalter_iban")),
        ("bank", _cited(store, pid, "verwalter_bank")),
        ("steuernummer", _cited(store, pid, "verwalter_steuernummer")),
        ("scope", "WEG"),
    ])


# ---------- property § 2 ----------

def render_units_index(store: FactStore, ctx: dict[str, Any]) -> str:
    headers = ["unit_id", "label", "haus_id", "floor", "sqm", "rooms",
               "typ", "mea_‰", "occupancy", "owner_ref", "unit_md_ref"]
    rows: list[list[str]] = []
    # Build owner_ref index from eigentuemer.einheit_ids
    owner_for: dict[str, str] = {}
    for eig in _entity_ids_by_type(store, "eigentuemer"):
        units = _latest_value(store, eig, "einheit_ids", []) or []
        if isinstance(units, list):
            for u in units:
                owner_for[u] = eig
    for eid in _entity_ids_by_type(store, "einheit"):
        nr = _latest_value(store, eid, "einheit_nr", "")
        haus = _latest_value(store, eid, "haus_id", "")
        lage = _latest_value(store, eid, "lage", "") or ""
        # "1. OG links" → floor "1. OG"; "EG mitte" → "EG"
        pos_match = re.search(r"\b(links|mitte|rechts)\b\s*$", lage, re.IGNORECASE)
        floor = lage[:pos_match.start()].strip() if pos_match else lage
        sqm = _latest_value(store, eid, "wohnflaeche_qm", "")
        rooms = _latest_value(store, eid, "zimmer", "")
        typ = _latest_value(store, eid, "typ", "")
        mea = _latest_value(store, eid, "miteigentumsanteil", "")
        occ = _latest_value(store, eid, "occupancy_status") or _occupancy_inferred(store, eid)
        owner = owner_for.get(eid, "—")
        rows.append([
            f"`{eid}`", nr or "—", haus or "—", floor or "—",
            str(sqm) if sqm else "—", str(rooms) if rooms else "—",
            typ or "—", str(mea) if mea else "—",
            occ, f"`{owner}`" if owner != "—" else "—",
            f"`context.unit.{eid}.md`",
        ])
    return _table(headers, rows)


def _occupancy_inferred(store: FactStore, unit_id: str) -> str:
    """If a mieter is bound to this einheit and has no mietende → rented.
    Else if owner is selbstnutzer → own-use. Else vacant."""
    for mid in _entity_ids_by_type(store, "mieter"):
        eh = _latest_value(store, mid, "einheit_id")
        if eh != unit_id:
            continue
        ende = _latest_value(store, mid, "mietende")
        if not ende:
            return "rented"
    # check selbstnutzer
    for eig in _entity_ids_by_type(store, "eigentuemer"):
        units = _latest_value(store, eig, "einheit_ids", []) or []
        if isinstance(units, list) and unit_id in units:
            if _latest_value(store, eig, "selbstnutzer"):
                return "own-use"
    return "vacant"


# ---------- property § 3 / § 4 / § 8 (mostly empty stubs) ----------

def render_compliance(store: FactStore, ctx: dict[str, Any]) -> str:
    headers = ["obligation", "last_done", "next_due", "vendor_ref",
               "status", "evidence_doc_ref"]
    return _empty_table(headers)


def render_vendor_quotes(store: FactStore, ctx: dict[str, Any]) -> str:
    headers = ["vendor_ref", "scope", "amount", "valid_until", "decision", "doc_ref"]
    return _empty_table(headers)


def render_vendor_dunning(store: FactStore, ctx: dict[str, Any]) -> str:
    headers = ["vendor_ref", "invoice_no", "amount", "stage", "since",
               "deadline", "reason"]
    rows: list[list[str]] = []
    for dl in _entity_ids_by_type(store, "dienstleister"):
        groups = _group_facts_by_event(store, dl, "vendor_dunning.")
        for g in groups:
            inv = (g.get("vendor_dunning.invoice_no") or g.get("vendor_dunning.invoice_ref"))
            amt = g.get("vendor_dunning.amount_eur")
            stage = g.get("vendor_dunning.stage")
            since = g.get("vendor_dunning.since")
            reason = g.get("vendor_dunning.reason")
            rows.append([
                f"`{dl}`",
                inv.value if inv else "—",
                f"{amt.value:.2f}" if amt and amt.value is not None else "—",
                str(stage.value) if stage else "1",
                since.value if since else (next(iter(g.values())).observed_at or "—"),
                "—",
                reason.value if reason else "—",
            ])
    return _table(headers, rows)


def render_recurring_property(store: FactStore, ctx: dict[str, Any]) -> str:
    headers = ["process_type", "started", "current_step", "owner", "eta", "blockers"]
    rows: list[list[str]] = []
    # mieterwechsel-in-flight aggregated from units
    for eid in _entity_ids_by_type(store, "einheit"):
        if _latest_value(store, eid, "lease.cancellation_status") not in (None, "none"):
            started = _latest_value(store, eid, "lease.cancellation_notice_date") or "—"
            rows.append([
                f"Mieterwechsel {eid}", started, "Kündigung erhalten",
                "Verwaltung", "TBD", "—",
            ])
    return _table(headers, rows)


def render_financials(store: FactStore, ctx: dict[str, Any]) -> str:
    pid = ctx["property_id"]
    return _bullets([
        ("last_nk_abrechnung", EMPTY),
        ("last_hausgeld_abrechnung", EMPTY),
        ("last_owner_payouts", EMPTY),
        ("ytd_aggregates", EMPTY),
        ("ruecklage_balance", EMPTY),
        ("live balances pointer",
         f"`db.account_balance WHERE property_id={pid}`"),
    ])


def render_operations_summary(store: FactStore, ctx: dict[str, Any]) -> str:
    pid = ctx["property_id"]
    rented = _latest_value(store, pid, "operations.units_rented", 0) or 0
    vacant = _latest_value(store, pid, "operations.units_vacant", 0) or 0
    own = _latest_value(store, pid, "operations.units_own_use", 0) or 0
    total = _latest_value(store, pid, "operations.units_total", 0) or 0
    dunning_count = _latest_value(store, pid, "operations.active_dunning_count", 0) or 0
    dunning_s1 = _latest_value(store, pid, "operations.active_dunning_stage_1", 0) or 0
    dunning_s2 = _latest_value(store, pid, "operations.active_dunning_stage_2", 0) or 0
    dunning_s3 = _latest_value(store, pid, "operations.active_dunning_stage_3", 0) or 0
    dunning_units = _latest_value(store, pid, "operations.active_dunning_units", []) or []
    red_count = _latest_value(store, pid, "operations.active_reductions_count", 0) or 0
    red_units = _latest_value(store, pid, "operations.active_reductions_units", []) or []
    handovers = _latest_value(store, pid, "operations.pending_handovers_30d", 0) or 0
    mw_count = _latest_value(store, pid, "operations.active_mieterwechsel_count", 0) or 0
    mw_units = _latest_value(store, pid, "operations.active_mieterwechsel_units", []) or []
    crit = _latest_value(store, pid, "operations.critical_tickets_total", 0) or 0
    vendor_open = _latest_value(store, pid, "operations.vendor_open_balance_eur", 0.0) or 0.0
    return _bullets([
        ("units_status",
         f"{{ rented: `{rented}`, vacant: `{vacant}`, own-use: `{own}`, total: `{total}` }}"),
        ("active_dunning",
         f"{{ count: `{dunning_count}`, by_stage: {{ 1: `{dunning_s1}`, 2: `{dunning_s2}`, 3: `{dunning_s3}` }}, units: {dunning_units} }}"),
        ("active_reductions",
         f"{{ count: `{red_count}`, units: {red_units} }}"),
        ("pending_handovers_next_30d", f"`{handovers}`"),
        ("active_mieterwechsel_in_flight",
         f"{{ count: `{mw_count}`, units: {mw_units} }}"),
        ("critical_tickets_total", f"`{crit}`"),
        ("vendor_open_balance_against_us_total", f"`{vendor_open:.2f} EUR`"),
        ("last_aggregated_at", f"`{_now_iso()}`"),
    ])


# ---------- property § 6 ----------

def render_stakeholders(store: FactStore, ctx: dict[str, Any]) -> str:
    headers = ["role", "name", "contact", "vertragstyp", "next_service_due",
               "last_invoice (date/amount)", "open_balance_against_us", "id"]
    rows: list[list[str]] = []
    UTILITY_BRANCHEN = {"Stromversorger", "Gasversorger", "Wasserversorger",
                        "Müllentsorgung"}
    for dl in _entity_ids_by_type(store, "dienstleister"):
        branche = _latest_value(store, dl, "branche", "")
        if branche in UTILITY_BRANCHEN:
            continue  # rendered in utilities block
        firma = _latest_value(store, dl, "firma", "")
        contact = _latest_value(store, dl, "email", "")
        monatlich = _latest_value(store, dl, "vertrag_monatlich")
        stundensatz = _latest_value(store, dl, "stundensatz")
        if monatlich:
            vtyp = f"monatlich €{monatlich}"
        elif stundensatz:
            vtyp = f"stundensatz €{stundensatz}"
        else:
            vtyp = "sporadisch"
        last_inv_id = _latest_value(store, dl, "vendor.last_invoice_id", "")
        last_inv_date = _latest_value(store, dl, "vendor.last_invoice_date", "")
        last_inv = f"{last_inv_date} {last_inv_id}".strip() or "—"
        # open balance: sum of vendor_dunning.amount_eur on this DL
        open_bal = 0.0
        for g in _group_facts_by_event(store, dl, "vendor_dunning."):
            f = g.get("vendor_dunning.amount_eur")
            if f and f.value is not None:
                try:
                    open_bal += float(f.value)
                except (TypeError, ValueError):
                    pass
        rows.append([
            branche or "—",
            firma or "—",
            contact or "—",
            vtyp,
            "—",
            last_inv,
            f"{open_bal:.2f} EUR" if open_bal else "—",
            f"`{dl}`",
        ])
    return _table(headers, rows)


def render_utilities(store: FactStore, ctx: dict[str, Any]) -> str:
    headers = ["type", "provider", "vertrag_no", "meter_ref(s)",
               "current_abschlag (€/Mon)", "last_jahresabrechnung_period",
               "next_jahresabrechnung_due", "id"]
    rows: list[list[str]] = []
    UTILITY_BRANCHEN = {"Stromversorger", "Gasversorger", "Wasserversorger",
                        "Müllentsorgung"}
    for dl in _entity_ids_by_type(store, "dienstleister"):
        branche = _latest_value(store, dl, "branche", "")
        if branche not in UTILITY_BRANCHEN:
            continue
        firma = _latest_value(store, dl, "firma", "")
        rows.append([branche, firma or "—", "—", "—", "—", "—", "—", f"`{dl}`"])
    return _table(headers, rows)


def render_authorities(store: FactStore, ctx: dict[str, Any]) -> str:
    headers = ["behörde", "zuständigkeit", "ansprechpartner", "last_contact",
               "open_request", "compliance_doc_required"]
    return _empty_table(headers)


def render_policies(store: FactStore, ctx: dict[str, Any]) -> str:
    return _bullets([
        ("mahngebuehren", "{ stage_1: €5, stage_2: €10 }"),
        ("verzugszinssatz",
         "basiszinssatz + 5pp (§ 288 I BGB)"),
        ("werktage_definition", "Mo–Fr (Sa exkl. per BGH zu § 556b)"),
        ("nk_default_keys", "`area_sqm | person_count | verbrauch | unit_share`"),
        ("heizkosten_method", "HeizkostenV §7 (default 70/30 Verbrauch/Grundkosten)"),
        ("communication_preference_default", "`email`"),
    ])


def render_weg_decisions(store: FactStore, ctx: dict[str, Any]) -> str:
    return _empty_table(["date", "beschluss-no", "topic", "status",
                          "one-line summary", "protocol_ref"])


def render_weg_agenda_backlog(store: FactStore, ctx: dict[str, Any]) -> str:
    return _empty_table(["proposed_at", "proposed_by (owner_id)", "topic",
                          "status", "doc_ref"])


def render_weg_einsprueche(store: FactStore, ctx: dict[str, Any]) -> str:
    return _empty_table(["beschluss-no", "einspruch_by (owner_id)", "date",
                          "reason (one-line)", "status"])


def render_modernization(store: FactStore, ctx: dict[str, Any]) -> str:
    return _empty_table(["date_completed", "scope", "total_cost",
                          "umlage_per_year", "affected_units", "rent_increase",
                          "opt-outs"])


def render_cross_unit_patterns(store: FactStore, ctx: dict[str, Any]) -> str:
    headers = ["pattern_type", "involved_units", "incident_count",
               "first_seen", "last_seen", "trigger_action_suggested", "confidence"]
    return _empty_table(headers) + "\n\n_(LLM pattern detection — Hour 6+, see `engine.aggregation-rules.md` §8.5.)_"


# ---------- unit blocks ----------

def render_unit_id(store: FactStore, ctx: dict[str, Any]) -> str:
    return ctx["unit_id"]


def render_unit(store: FactStore, ctx: dict[str, Any]) -> str:
    eid = ctx["unit_id"]
    nr = _latest_value(store, eid, "einheit_nr", "")
    haus = _latest_value(store, eid, "haus_id", "")
    lage = _latest_value(store, eid, "lage", "") or ""
    # `lage` is shaped like "1. OG links" / "EG mitte" / "DG rechts".
    # Split on the trailing position word (links/mitte/rechts) so the floor
    # keeps its full prefix.
    pos_match = re.search(r"\b(links|mitte|rechts)\b\s*$", lage, re.IGNORECASE)
    if pos_match:
        position = pos_match.group(1)
        floor = lage[:pos_match.start()].strip()
    else:
        floor, position = lage, ""
    typ = _latest_value(store, eid, "typ", "Wohnung")
    sqm = _latest_value(store, eid, "wohnflaeche_qm", "")
    rooms = _latest_value(store, eid, "zimmer", "")
    mea = _latest_value(store, eid, "miteigentumsanteil", "")
    occ = _latest_value(store, eid, "occupancy_status") or _occupancy_inferred(store, eid)
    return _bullets([
        ("unit_id", f"`{eid}`"),
        ("label", nr or EMPTY),
        ("haus_id", f"`{haus}`" if haus else EMPTY),
        ("floor", floor or EMPTY),
        ("position", position or EMPTY),
        ("typ", typ),
        ("area_sqm", str(sqm) if sqm else EMPTY),
        ("rooms", str(rooms) if rooms else EMPTY),
        ("mea_‰", str(mea) if mea else EMPTY),
        ("equipment", EMPTY),
        ("media_supply", EMPTY),
        ("key_inventory", EMPTY),
        ("meters", EMPTY),
        ("occupancy_status", f"`{occ}`"),
        ("nk_keys", EMPTY),
    ])


def _tenants_for_unit(store: FactStore, unit_id: str) -> list[str]:
    out = []
    for mid in _entity_ids_by_type(store, "mieter"):
        if _latest_value(store, mid, "einheit_id") == unit_id:
            out.append(mid)
    return out


def render_lease(store: FactStore, ctx: dict[str, Any]) -> str:
    unit_id = ctx["unit_id"]
    tenants = _tenants_for_unit(store, unit_id)
    if not tenants:
        return EMPTY
    primary = tenants[0]
    kalt = _latest_value(store, primary, "kaltmiete")
    nk = _latest_value(store, primary, "nk_vorauszahlung")
    extras = []
    warm = None
    if kalt is not None and nk is not None:
        try:
            warm = float(kalt) + float(nk)
        except (TypeError, ValueError):
            pass
    cancel = _latest_value(store, primary, "lease.cancellation_status", "none")
    cancel_date = _latest_value(store, primary, "lease.cancellation_notice_date", "")
    move_out = _latest_value(store, primary, "lease.move_out_date", "")
    sublet = _latest_value(store, primary, "subletting.current_status", "none")
    rent_components = (
        f"{{ kaltmiete: {kalt or '—'}, betriebskosten_vorauszahlung: {nk or '—'}, "
        f"total_warmmiete: {f'{warm:.2f}' if warm is not None else '—'} }}"
    )
    cancel_block = (
        f"`{cancel}`" if cancel == "none"
        else f"`{cancel}` (notice_date: {cancel_date or '—'}, move_out_date: {move_out or '—'})"
    )
    return _bullets([
        ("lease_id", f"`LEASE-{primary}`"),
        ("unit_ref", f"`{unit_id}`"),
        ("start_date", _cited(store, primary, "mietbeginn")),
        ("end_date", _cited(store, primary, "mietende")),
        ("term_type", "`unbefristet`" if not _latest_value(store, primary, "mietende") else "`befristet`"),
        ("cancellation_status", cancel_block),
        ("rent_components", rent_components),
        ("payment_mode", _latest_value(store, primary, "lease.payment_mode") or "Überweisung"),
        ("iban_payer", _cited(store, primary, "iban")),
        ("kaution", f"{{ amount: {_latest_value(store, primary, 'kaution', '—')} }}"),
        ("usage", "`residential`"),
        ("subletting", f"{{ current_status: `{sublet}` }}"),
        ("special_agreements", EMPTY),
    ])


def render_tenants(store: FactStore, ctx: dict[str, Any]) -> str:
    headers = ["tenant_id", "name", "role", "contact_email", "contact_phone",
               "comms_pref", "gesamtschuldner"]
    rows: list[list[str]] = []
    tenants = _tenants_for_unit(store, ctx["unit_id"])
    for i, tid in enumerate(tenants):
        anrede = _latest_value(store, tid, "anrede", "")
        v = _latest_value(store, tid, "vorname", "")
        n = _latest_value(store, tid, "nachname", "")
        name = " ".join(p for p in [anrede, v, n] if p) or tid
        email = _latest_value(store, tid, "email", "—")
        phone = _latest_value(store, tid, "telefon", "—")
        rows.append([
            f"`{tid}`", name, "haupt" if i == 0 else "mit",
            email, phone, "email", "—" if len(tenants) == 1 else "ja",
        ])
    return _table(headers, rows)


def render_tickets_critical(store: FactStore, ctx: dict[str, Any]) -> str:
    headers = ["ticket_id", "type", "title", "deadline", "status", "assignee"]
    rows: list[list[str]] = []
    for g in _group_facts_by_event(store, ctx["unit_id"], "ticket."):
        sev = g.get("ticket.severity")
        if not sev or sev.value != "critical":
            continue
        any_f = next(iter(g.values()))
        ticket_id = "TKT-" + (any_f.source_event_id[:8])
        ttype = g.get("ticket.type")
        title = g.get("ticket.title")
        rows.append([
            f"`{ticket_id}`",
            ttype.value if ttype else "Reparatur",
            title.value if title else "—",
            "—",
            "open",
            "—",
        ])
    return _table(headers, rows)


def render_tickets_aggregate(store: FactStore, ctx: dict[str, Any]) -> str:
    by_type: dict[str, int] = {}
    total = 0
    for g in _group_facts_by_event(store, ctx["unit_id"], "ticket."):
        ttype = g.get("ticket.type")
        t = ttype.value if ttype else "other"
        by_type[t] = by_type.get(t, 0) + 1
        total += 1
    breakdown = ", ".join(f"{k}: `{v}`" for k, v in sorted(by_type.items())) or "—"
    return _bullets([
        ("total_open", f"`{total}`"),
        ("by_type", f"{{ {breakdown} }}"),
        ("live source", f"`db.tickets WHERE unit_id={ctx['unit_id']} AND status='open'`"),
    ])


def render_dunning(store: FactStore, ctx: dict[str, Any]) -> str:
    headers = ["tenant_ref", "claim_id", "current_stage", "amount_open",
               "default_since", "deadline_for_stage", "last_letter"]
    rows: list[list[str]] = []
    for tid in ctx.get("tenant_ids") or []:
        stufe = _latest_value(store, tid, "dunning.mahnstufe")
        if not stufe:
            continue
        offen = _latest_value(store, tid, "dunning.offener_betrag_eur")
        last_pay = _latest_value(store, tid, "dunning.last_payment_date")
        rows.append([
            f"`{tid}`",
            "—",
            str(stufe),
            f"{offen:.2f} EUR" if isinstance(offen, (int, float)) else "—",
            last_pay or "—",
            "—",
            "—",
        ])
    body = _table(headers, rows)
    pointer_id = (ctx.get("tenant_ids") or [ctx["unit_id"]])[0]
    body += f"\n- live balance pointer: `db.tenant_balance.tenant_id={pointer_id}`"
    return body


def render_reductions(store: FactStore, ctx: dict[str, Any]) -> str:
    rows = _group_facts_by_event(store, ctx["unit_id"], "reductions.")
    if not rows:
        return EMPTY
    parts: list[str] = []
    for g in rows:
        date_v = g.get("reductions.date_raised")
        amt = g.get("reductions.amount_or_percent")
        reason = g.get("reductions.reason")
        status = g.get("reductions.status")
        parts.append(_bullets([
            ("date_raised", date_v.value if date_v else "—"),
            ("amount_or_percent", amt.value if amt else "—"),
            ("reason", reason.value if reason else "—"),
            ("status", f"**{status.value if status else 'unilateral'}**"),
        ]))
    parts.append("- *trigger: HITL exit if any entry present*")
    return "\n\n".join(parts)


def render_handover(store: FactStore, ctx: dict[str, Any]) -> str:
    eid = ctx["unit_id"]
    next_date = _latest_value(store, eid, "handover.next_scheduled_date")
    next_type = _latest_value(store, eid, "handover.next_scheduled_type")
    last_date = _latest_value(store, eid, "handover.last_completed_date")
    last_type = _latest_value(store, eid, "handover.last_completed_type")
    if not any([next_date, last_date]):
        return EMPTY
    return _bullets([
        ("next_scheduled",
         f"{{ date: {next_date or 'TBD'}, type: {next_type or 'Auszug'} }}"),
        ("last_completed",
         f"{{ date: {last_date or '—'}, type: {last_type or '—'} }}"),
        ("meters_at_handover", EMPTY),
        ("keys_handed_over", EMPTY),
        ("defects", EMPTY),
        ("photos_ref", "n/a"),
    ])


def render_recurring_unit(store: FactStore, ctx: dict[str, Any]) -> str:
    headers = ["process_type", "started", "current_step", "owner", "eta", "blockers"]
    rows: list[list[str]] = []
    eid = ctx["unit_id"]
    cancel = _latest_value(store, eid, "lease.cancellation_status")
    if cancel and cancel != "none":
        started = _latest_value(store, eid, "lease.cancellation_notice_date") or "—"
        rows.append([
            "Mieterwechsel", started, "Kündigung erhalten",
            "Verwaltung", "TBD", "Übergabe-Termin offen",
        ])
    return _table(headers, rows)


def render_vermietung(store: FactStore, ctx: dict[str, Any]) -> str:
    occ = _latest_value(store, ctx["unit_id"], "occupancy_status") \
        or _occupancy_inferred(store, ctx["unit_id"])
    if occ != "vacant":
        return "_Not yet activated. Triggers when occupancy_status flips to vacant after move-out._"
    return _bullets([
        ("inserate_url", EMPTY),
        ("days_on_market", EMPTY),
        ("asking_kaltmiete", EMPTY),
        ("prospects_count", EMPTY),
        ("scheduled_viewings_count", EMPTY),
        ("applications_received_count", EMPTY),
        ("shortlist", EMPTY),
    ])


def render_tenant_agreements(store: FactStore, ctx: dict[str, Any]) -> str:
    headers = ["date", "type", "one-line", "doc_ref"]
    rows: list[list[str]] = []
    for tid in ctx.get("tenant_ids") or []:
        for g in _group_facts_by_event(store, tid, "tenant_agreement."):
            d = g.get("tenant_agreement.date")
            t = g.get("tenant_agreement.type")
            note = g.get("tenant_agreement.note")
            any_f = next(iter(g.values()))
            rows.append([
                d.value if d else (any_f.observed_at or "—"),
                t.value if t else "—",
                note.value if note else "—",
                f"[(source)]({any_f.source_ref})",
            ])
    return _table(headers, rows)


def render_modernization_unit(store: FactStore, ctx: dict[str, Any]) -> str:
    return _empty_table(["date_completed", "scope", "umlage_per_year",
                          "rent_increase_per_month", "tenant_opted_out"])


def render_sticky_threads(store: FactStore, ctx: dict[str, Any]) -> str:
    headers = ["thread_id", "subject", "last_msg_date", "parties",
               "status", "one-line outcome", "pointer"]
    rows: list[list[str]] = []
    for tid in ctx.get("tenant_ids") or []:
        groups = _group_facts_by_event(store, tid, "sticky_thread.")
        for g in groups:
            subj = g.get("sticky_thread.subject")
            last = g.get("sticky_thread.last_msg_date")
            count = g.get("sticky_thread.msg_count")
            status = g.get("sticky_thread.status")
            any_f = next(iter(g.values()))
            tid_short = "TH-" + any_f.source_event_id[:6]
            rows.append([
                f"`{tid_short}`",
                subj.value if subj else "—",
                last.value if last else "—",
                f"`{tid}`",
                status.value if status else "active",
                f"{count.value} msgs" if count else "—",
                f"[(emails)]({any_f.source_ref})",
            ])
    # Also pick up unit-scoped sticky threads
    for g in _group_facts_by_event(store, ctx["unit_id"], "sticky_thread."):
        subj = g.get("sticky_thread.subject")
        last = g.get("sticky_thread.last_msg_date")
        count = g.get("sticky_thread.msg_count")
        any_f = next(iter(g.values()))
        tid_short = "TH-" + any_f.source_event_id[:6]
        rows.append([
            f"`{tid_short}`",
            subj.value if subj else "—",
            last.value if last else "—",
            f"`{ctx['unit_id']}`",
            "active",
            f"{count.value} msgs" if count else "—",
            f"[(emails)]({any_f.source_ref})",
        ])
    return _table(headers, rows)


# ---------- registry ----------

PROPERTY_BLOCKS: dict[str, Callable[[FactStore, dict[str, Any]], str]] = {
    "property.display_name": render_property_display_name,
    "meta": render_property_meta,
    "property": render_property,
    "owners": render_owners,
    "mandate": render_mandate,
    "units-index": render_units_index,
    "compliance": render_compliance,
    "vendor-quotes": render_vendor_quotes,
    "vendor-dunning": render_vendor_dunning,
    "recurring-property": render_recurring_property,
    "financials": render_financials,
    "operations-summary": render_operations_summary,
    "stakeholders": render_stakeholders,
    "utilities": render_utilities,
    "authorities": render_authorities,
    "policies": render_policies,
    "weg-decisions": render_weg_decisions,
    "weg-agenda-backlog": render_weg_agenda_backlog,
    "weg-einsprueche": render_weg_einsprueche,
    "modernization": render_modernization,
    "cross-unit-patterns": render_cross_unit_patterns,
    "provenance": render_property_provenance,
}


UNIT_BLOCKS: dict[str, Callable[[FactStore, dict[str, Any]], str]] = {
    "unit_id": render_unit_id,
    "meta": render_unit_meta,
    "unit": render_unit,
    "lease": render_lease,
    "tenants": render_tenants,
    "tickets.critical": render_tickets_critical,
    "tickets.aggregate": render_tickets_aggregate,
    "dunning": render_dunning,
    "reductions": render_reductions,
    "handover": render_handover,
    "recurring": render_recurring_unit,
    "vermietung": render_vermietung,
    "tenant-agreements": render_tenant_agreements,
    "modernization-unit": render_modernization_unit,
    "sticky-threads": render_sticky_threads,
    "provenance": render_unit_provenance,
}


__all__ = ["PROPERTY_BLOCKS", "UNIT_BLOCKS"]
