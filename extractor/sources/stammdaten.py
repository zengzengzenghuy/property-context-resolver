"""Stammdaten connector: master data → baseline facts.

Reads `raw/stammdaten/stammdaten.json` (canonical) or falls back to the per-table CSVs.
Produces one Event per record and a fact per non-empty field — these become the
ground-truth baseline for the fact store.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Any, Iterator

from ..models import Event, Fact, PROPERTY_ID
from ..source_ref import for_path


# Field → (entity_type, key) mapping for record types. Keys with `None` are skipped.
_OWNER_KEYS = {
    "anrede", "vorname", "nachname", "firma", "strasse", "plz", "ort", "land",
    "email", "telefon", "iban", "bic", "einheit_ids", "selbstnutzer",
    "sev_mandat", "beirat", "sprache",
}
_TENANT_KEYS = {
    "anrede", "vorname", "nachname", "email", "telefon", "einheit_id",
    "eigentuemer_id", "mietbeginn", "mietende", "kaltmiete",
    "nk_vorauszahlung", "kaution", "iban", "bic", "sprache",
}
_VENDOR_KEYS = {
    "firma", "branche", "ansprechpartner", "email", "telefon", "strasse",
    "plz", "ort", "land", "iban", "bic", "ust_id", "steuernummer", "stil",
    "sprache", "vertrag_monatlich", "stundensatz",
}
_UNIT_KEYS = {
    "haus_id", "einheit_nr", "lage", "typ", "wohnflaeche_qm", "zimmer",
    "miteigentumsanteil",
}
_BUILDING_KEYS = {"hausnr", "einheiten", "etagen", "fahrstuhl", "baujahr"}
_PROPERTY_KEYS = {
    "name", "strasse", "plz", "ort", "baujahr", "sanierung", "verwalter",
    "verwalter_strasse", "verwalter_plz", "verwalter_ort", "verwalter_email",
    "verwalter_telefon", "verwalter_iban", "verwalter_bic", "verwalter_bank",
    "verwalter_steuernummer", "weg_bankkonto_iban", "weg_bankkonto_bic",
    "weg_bankkonto_bank", "ruecklage_iban", "ruecklage_bic",
}


def _emit_record(
    source_path: Path,
    record_type: str,
    record: dict[str, Any],
    keys: set[str],
    summary: str,
) -> tuple[Event, list[Fact]]:
    entity_id = record.get("id")
    event = Event.make(
        source="stammdaten",
        source_ref=for_path(source_path, fragment=f"{record_type}/{entity_id}"),
        content=summary,
        metadata={"record_type": record_type, "entity_id": entity_id},
    )
    facts: list[Fact] = []
    for key in keys:
        if key not in record:
            continue
        value = record[key]
        if value in (None, "", []):
            continue
        facts.append(
            Fact.make(
                property_id=PROPERTY_ID,
                entity_type=record_type,
                entity_id=entity_id,
                key=key,
                value=value,
                source_event_id=event.id,
                source_ref=event.source_ref,
            )
        )
    return event, facts


def _from_json(path: Path) -> Iterator[tuple[Event, list[Fact]]]:
    data = json.loads(path.read_text(encoding="utf-8"))

    lie = data.get("liegenschaft") or {}
    if lie:
        ev = Event.make(
            source="stammdaten",
            source_ref=for_path(path, fragment=f"liegenschaft/{lie.get('id', PROPERTY_ID)}"),
            content=f"Liegenschaft {lie.get('name')} ({lie.get('strasse')}, {lie.get('plz')} {lie.get('ort')})",
            metadata={"record_type": "liegenschaft", "entity_id": lie.get("id")},
        )
        yield ev, [
            Fact.make(
                property_id=PROPERTY_ID,
                entity_type="liegenschaft",
                entity_id=lie.get("id"),
                key=k,
                value=lie[k],
                source_event_id=ev.id,
                source_ref=ev.source_ref,
            )
            for k in _PROPERTY_KEYS
            if lie.get(k) not in (None, "", [])
        ]

    for b in data.get("gebaeude", []):
        yield _emit_record(
            path, "gebaeude", b, _BUILDING_KEYS,
            f"Gebaeude {b.get('id')} Hausnr {b.get('hausnr')}",
        )
    for u in data.get("einheiten", []):
        yield _emit_record(
            path, "einheit", u, _UNIT_KEYS,
            f"Einheit {u.get('id')} {u.get('einheit_nr')} {u.get('lage')}",
        )
    for o in data.get("eigentuemer", []):
        name = o.get("firma") or f"{o.get('vorname','')} {o.get('nachname','')}".strip()
        yield _emit_record(path, "eigentuemer", o, _OWNER_KEYS, f"Eigentuemer {o.get('id')} {name}")
    for t in data.get("mieter", []):
        name = f"{t.get('vorname','')} {t.get('nachname','')}".strip()
        yield _emit_record(path, "mieter", t, _TENANT_KEYS, f"Mieter {t.get('id')} {name} -> {t.get('einheit_id')}")
    for d in data.get("dienstleister", []):
        yield _emit_record(
            path, "dienstleister", d, _VENDOR_KEYS,
            f"Dienstleister {d.get('id')} {d.get('firma')} ({d.get('branche')})",
        )


def _from_csvs(stamm_dir: Path) -> Iterator[tuple[Event, list[Fact]]]:
    """Fallback when stammdaten.json is missing: load the per-table CSVs."""
    table_specs = [
        ("eigentuemer.csv", "eigentuemer", _OWNER_KEYS,
         lambda r: f"Eigentuemer {r['id']} {r.get('firma') or (r.get('vorname','') + ' ' + r.get('nachname','')).strip()}"),
        ("mieter.csv", "mieter", _TENANT_KEYS,
         lambda r: f"Mieter {r['id']} {r.get('vorname','')} {r.get('nachname','')} -> {r.get('einheit_id','')}"),
        ("einheiten.csv", "einheit", _UNIT_KEYS,
         lambda r: f"Einheit {r['id']} {r.get('einheit_nr','')} {r.get('lage','')}"),
        ("dienstleister.csv", "dienstleister", _VENDOR_KEYS,
         lambda r: f"Dienstleister {r['id']} {r.get('firma','')} ({r.get('branche','')})"),
    ]
    for fname, etype, keys, summary_fn in table_specs:
        p = stamm_dir / fname
        if not p.exists():
            continue
        with p.open(encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Coerce list-style "EH-001;EH-002" → list (matches JSON shape)
                if "einheit_ids" in row and isinstance(row["einheit_ids"], str):
                    row["einheit_ids"] = [v for v in row["einheit_ids"].split(";") if v]
                yield _emit_record(p, etype, row, keys, summary_fn(row))


def extract(root: Path) -> Iterator[tuple[Event, list[Fact]]]:
    stamm_dir = root / "stammdaten"
    if not stamm_dir.exists():
        return
    json_path = stamm_dir / "stammdaten.json"
    if json_path.exists():
        yield from _from_json(json_path)
    else:
        yield from _from_csvs(stamm_dir)
