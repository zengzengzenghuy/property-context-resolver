"""Bank-statement connector.

Reads the canonical semicolon-delimited Sparkasse-style export
(`kontoauszug_*.csv`) plus any incremental delta files. Each row becomes one
Event; the verwendungszweck is parsed for `EH-NNN`, `MIE-NNN`, `EIG-NNN`,
`DL-NNN`, and invoice/Mahnung references to attach facts to entities.
"""

from __future__ import annotations

import csv
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterator, Optional

from ..models import Event, Fact, PROPERTY_ID
from ..source_ref import for_path


_UNIT_RX = re.compile(r"\bEH-\d{3}\b")
_TENANT_RX = re.compile(r"\bMIE-\d{3}\b")
_OWNER_RX = re.compile(r"\bEIG-\d{3}\b")
_VENDOR_RX = re.compile(r"\bDL-\d{3}\b")
_INVOICE_RX = re.compile(r"\b(?:RE|INV)-\d{4}-\d{3,5}\b")
_MIETE_RX = re.compile(r"\bMiete\s+(\d{2}/\d{4})\b", re.IGNORECASE)
_HAUSGELD_RX = re.compile(r"\bHausgeld\s+(\d{2}/\d{4})\b", re.IGNORECASE)


def _parse_amount(s: str) -> Optional[float]:
    if not s:
        return None
    cleaned = s.replace(".", "").replace(",", ".")
    try:
        return float(cleaned)
    except ValueError:
        return None


def _parse_de_date(s: str) -> Optional[str]:
    if not s:
        return None
    try:
        d = datetime.strptime(s, "%d.%m.%Y").replace(tzinfo=timezone.utc)
        return d.date().isoformat()
    except ValueError:
        return None


def _classify(verwendungszweck: str) -> str:
    z = verwendungszweck.lower()
    if "miete" in z:
        return "miete"
    if "hausgeld" in z:
        return "hausgeld"
    if "ruecklage" in z or "rücklage" in z:
        return "ruecklage"
    if "rechnung" in z or "ueberweisung" in z or "überweisung" in z:
        return "vendor_payment"
    if "mahnung" in z:
        return "mahngebuehr"
    return "other"


def _resolve_entity(verwendungszweck: str, beguenstigter: str) -> tuple[Optional[str], Optional[str]]:
    """Best-effort: pick the strongest entity reference visible in the row."""
    text = f"{verwendungszweck} {beguenstigter}"
    if m := _TENANT_RX.search(text):
        return "mieter", m.group(0)
    if m := _OWNER_RX.search(text):
        return "eigentuemer", m.group(0)
    if m := _VENDOR_RX.search(text):
        return "dienstleister", m.group(0)
    if m := _UNIT_RX.search(text):
        return "einheit", m.group(0)
    return None, None


def _emit_row(source_path: Path, row: dict[str, str]) -> tuple[Event, list[Fact]]:
    verw = row.get("Verwendungszweck", "") or ""
    beg = row.get("Beguenstigter/Zahlungspflichtiger", "") or ""
    amount = _parse_amount(row.get("Betrag", ""))
    booking_date = _parse_de_date(row.get("Buchungstag", ""))
    tx_id = (row.get("Kundenreferenz (End-to-End)") or "").strip() or None
    kind = _classify(verw)
    etype, eid = _resolve_entity(verw, beg)

    summary = f"{row.get('Buchungstext','')} {amount} EUR — {verw} ({beg})"
    fragment = tx_id or row.get("Sammlerreferenz") or beg or ""
    event = Event.make(
        source="bank",
        source_ref=for_path(source_path, fragment=fragment or None),
        content=summary,
        timestamp=booking_date,
        metadata={
            "tx_id": tx_id,
            "amount_eur": amount,
            "direction": "credit" if (amount or 0) >= 0 else "debit",
            "kind": kind,
            "iban": row.get("Kontonummer/IBAN"),
            "counterparty": beg,
            "buchungstag": booking_date,
        },
    )

    facts: list[Fact] = []

    def add(key: str, value: Any) -> None:
        if value in (None, "", []):
            return
        facts.append(
            Fact.make(
                property_id=PROPERTY_ID,
                entity_type=etype,
                entity_id=eid,
                key=key,
                value=value,
                source_event_id=event.id,
                source_ref=event.source_ref,
                observed_at=booking_date,
            )
        )

    add("payment.amount_eur", amount)
    add("payment.direction", "credit" if (amount or 0) >= 0 else "debit")
    add("payment.kind", kind)
    add("payment.counterparty", beg)
    add("payment.iban", row.get("Kontonummer/IBAN"))
    add("payment.tx_id", tx_id)
    add("payment.verwendungszweck", verw)

    if m := _MIETE_RX.search(verw):
        add("payment.miete_period", m.group(1))
    if m := _HAUSGELD_RX.search(verw):
        add("payment.hausgeld_period", m.group(1))
    if m := _INVOICE_RX.search(verw):
        add("payment.invoice_ref", m.group(0))

    return event, facts


def _emit_csv(path: Path) -> Iterator[tuple[Event, list[Fact]]]:
    with path.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            yield _emit_row(path, row)


def extract(root: Path, *, include_incremental: bool = False) -> Iterator[tuple[Event, list[Fact]]]:
    # Main statement
    bank_dir = root / "bank"
    if bank_dir.exists():
        for p in sorted(bank_dir.glob("kontoauszug*.csv")):
            yield from _emit_csv(p)

    if not include_incremental:
        return
    inc_dir = root / "incremental"
    if inc_dir.exists():
        for day_dir in sorted(inc_dir.glob("day-*")):
            bank_sub = day_dir / "bank"
            if not bank_sub.exists():
                continue
            for p in sorted(bank_sub.glob("*.csv")):
                if p.name.endswith("_index.csv"):
                    continue
                yield from _emit_csv(p)
