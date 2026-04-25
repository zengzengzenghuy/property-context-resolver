"""Invoice + letter PDF connectors.

The `rechnungen/` and `briefe/` filenames already encode the canonical references
(date, vendor id, invoice id, letter id, type), so we always emit a minimal
event from the filename. If `pypdf` is installed we additionally pull text and
extract richer facts (amounts, IBANs, mahnstufe, etc.).
"""

from __future__ import annotations

import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterator, Optional

from ..models import Event, Fact, PROPERTY_ID
from ..source_ref import for_path


# Filename patterns
_INVOICE_FN = re.compile(
    r"^(?P<date>\d{8})_(?P<vendor>DL-\d{3})_(?P<invoice>INV-\d{5})\.pdf$",
    re.IGNORECASE,
)
_LETTER_FN = re.compile(
    r"^(?P<date>\d{8})_(?P<kind>[a-z_]+)_(?P<letter>LTR-\d{4})\.pdf$",
    re.IGNORECASE,
)

# Body patterns
_AMOUNT_RX = re.compile(r"(\d{1,3}(?:\.\d{3})*(?:,\d{2}))\s*EUR")
_TOTALS_BLOCK_RX = re.compile(r"Summe\s+netto.*?Gesamtbetrag.*?(?:EUR.*?)+?(?=\n\s*\n|\Z)",
                              re.IGNORECASE | re.DOTALL)
_INVOICE_REF_RX = re.compile(r"\b(?:RE|INV)-\d{4}-\d{3,5}\b")
_OFFENER_RX = re.compile(r"Offener\s+Betrag:?\s*([\d.,]+)\s*EUR", re.IGNORECASE)
_MAHNSTUFE_RX = re.compile(r"Mahnstufe:?\s*(\d)", re.IGNORECASE)
_BETRIFFT_RX = re.compile(r"Betrifft:?\s*([^\n]+)", re.IGNORECASE)
_DATUM_RX = re.compile(r"Datum:?\s*(\d{2}\.\d{2}\.\d{4})", re.IGNORECASE)
# Anchored at column 0 so "Sehr geehrte/r Frau X," in the greeting doesn't match.
# Captures only the trailing name (no "Frau/Herr/Firma" prefix) so it feeds the
# resolver clean. Title prefixes are stripped by `norm_name` anyway, but keeping
# the value minimal makes downstream debugging easier.
_RECIPIENT_RX = re.compile(
    r"^(?:Frau|Herr|Firma)\s+([A-ZÄÖÜ][^\n,]+?)\s*$",
    re.MULTILINE,
)


def _extract_totals(text: str) -> dict[str, float]:
    """Pull netto / mwst / brutto from an invoice. Robust across both inline
    layouts (`Gesamtbetrag: 1.088,85 EUR`) and table-column layouts where
    pdfminer emits all labels then all amounts."""
    m = _TOTALS_BLOCK_RX.search(text)
    if not m:
        return {}
    block = m.group(0)
    amounts = [_parse_amount(a) for a in _AMOUNT_RX.findall(block)]
    amounts = [a for a in amounts if a is not None]
    if not amounts:
        return {}
    out: dict[str, float] = {}
    # In every observed layout, amounts within this block are emitted in label
    # order: netto first, optional mwst middle, brutto last.
    out["netto"] = amounts[0]
    out["brutto"] = amounts[-1]
    if len(amounts) >= 3:
        out["mwst"] = amounts[1]
    return out


def _parse_amount(s: str) -> Optional[float]:
    cleaned = s.replace(".", "").replace(",", ".")
    try:
        return float(cleaned)
    except ValueError:
        return None


def _date_from_yyyymmdd(s: str) -> Optional[str]:
    try:
        return datetime.strptime(s, "%Y%m%d").replace(tzinfo=timezone.utc).date().isoformat()
    except ValueError:
        return None


def _extract_pdf_text(path: Path) -> Optional[str]:
    """Prefer pre-cached .txt sibling (built by scripts/preocr.py).

    Order: <pdf>.pdf.txt → pdfminer.six → pypdf → None.
    """
    cached = path.with_suffix(path.suffix + ".txt")
    if cached.exists():
        try:
            return cached.read_text(encoding="utf-8")
        except Exception:
            pass

    try:
        from pdfminer.high_level import extract_text  # type: ignore
        try:
            text = extract_text(str(path))
            if text and text.strip():
                return text
        except Exception:
            pass
    except ImportError:
        pass

    try:
        from pypdf import PdfReader  # type: ignore
        reader = PdfReader(str(path))
        return "\n".join((p.extract_text() or "") for p in reader.pages)
    except (ImportError, Exception):
        return None


def _invoice_event(path: Path) -> tuple[Event, list[Fact]]:
    m = _INVOICE_FN.match(path.name)
    if not m:
        return _generic_pdf_event(path, source="invoice"), []
    date_iso = _date_from_yyyymmdd(m.group("date"))
    vendor = m.group("vendor").upper()
    invoice = m.group("invoice").upper()

    text = _extract_pdf_text(path) or ""
    summary = f"Rechnung {invoice} von {vendor} ({date_iso})"
    event = Event.make(
        source="invoice",
        source_ref=for_path(path),
        content=summary + ("\n\n" + text if text else ""),
        timestamp=date_iso,
        metadata={
            "vendor_id": vendor,
            "invoice_filename_id": invoice,
            "has_text": bool(text),
        },
    )

    facts: list[Fact] = []

    def add(key: str, value, entity_type=None, entity_id=None, confidence=1.0) -> None:
        if value in (None, "", []):
            return
        facts.append(
            Fact.make(
                property_id=PROPERTY_ID,
                entity_type=entity_type or "rechnung",
                entity_id=entity_id or invoice,
                key=key,
                value=value,
                source_event_id=event.id,
                source_ref=event.source_ref,
                observed_at=date_iso,
                confidence=confidence,
            )
        )

    add("rechnung.vendor_id", vendor, "rechnung", invoice)
    add("rechnung.date", date_iso, "rechnung", invoice)

    if text:
        totals = _extract_totals(text)
        if "brutto" in totals:
            add("rechnung.gesamt_brutto_eur", totals["brutto"], "rechnung", invoice, 0.95)
        if "netto" in totals:
            add("rechnung.summe_netto_eur", totals["netto"], "rechnung", invoice, 0.95)
        if "mwst" in totals:
            add("rechnung.mwst_eur", totals["mwst"], "rechnung", invoice, 0.95)
        if mr := _INVOICE_REF_RX.search(text):
            add("rechnung.invoice_ref", mr.group(0), "rechnung", invoice, 0.95)
        if mr := _DATUM_RX.search(text):
            add("rechnung.body_date", mr.group(1), "rechnung", invoice, 0.9)
        # Vendor enrichment fact
        add("vendor.last_invoice_id", invoice, "dienstleister", vendor, 0.95)
        add("vendor.last_invoice_date", date_iso, "dienstleister", vendor, 0.95)

    return event, facts


def _letter_event(path: Path) -> tuple[Event, list[Fact]]:
    m = _LETTER_FN.match(path.name)
    if not m:
        return _generic_pdf_event(path, source="letter"), []
    date_iso = _date_from_yyyymmdd(m.group("date"))
    kind = m.group("kind").lower()  # e.g. "etv_einladung", "mahnung"
    letter_id = m.group("letter").upper()
    text = _extract_pdf_text(path) or ""

    summary = f"Brief {letter_id} ({kind}) am {date_iso}"
    event = Event.make(
        source="letter",
        source_ref=for_path(path),
        content=summary + ("\n\n" + text if text else ""),
        timestamp=date_iso,
        metadata={
            "letter_id": letter_id,
            "kind": kind,
            "has_text": bool(text),
        },
    )

    facts: list[Fact] = []

    def add(key: str, value, entity_type="letter", entity_id=None, confidence=1.0) -> None:
        if value in (None, "", []):
            return
        facts.append(
            Fact.make(
                property_id=PROPERTY_ID,
                entity_type=entity_type,
                entity_id=entity_id or letter_id,
                key=key,
                value=value,
                source_event_id=event.id,
                source_ref=event.source_ref,
                observed_at=date_iso,
                confidence=confidence,
            )
        )

    add("letter.kind", kind)
    add("letter.date", date_iso)

    if text:
        if mr := _RECIPIENT_RX.search(text):
            # Recipient name lives on the letter entity; the DunningReconciler
            # post-processes letters of kind=mahnung by resolving this name to
            # a MIE-XXX via IdentityResolver and re-emitting tenant-scoped
            # mahnung.* facts (the source-side has no resolver to do it here).
            add("letter.recipient_name", mr.group(1).strip(), confidence=0.9)

    if kind == "mahnung" and text:
        if mr := _OFFENER_RX.search(text):
            add("mahnung.offener_betrag_eur", _parse_amount(mr.group(1)), confidence=0.95)
        if mr := _MAHNSTUFE_RX.search(text):
            add("mahnung.stufe", int(mr.group(1)), confidence=0.95)
        if mr := _BETRIFFT_RX.search(text):
            add("mahnung.betrifft", mr.group(1).strip(), confidence=0.85)

    return event, facts


def _generic_pdf_event(path: Path, source: str) -> Event:
    return Event.make(
        source=source,
        source_ref=for_path(path),
        content=f"<unparsed pdf: {path.name}>",
        metadata={"unparsed": True},
    )


def _walk(root: Path, *, kind: str, include_incremental: bool) -> Iterator[Path]:
    """Walk archive (`raw/<kind>/YYYY-MM/`) and optionally incremental dirs."""
    primary = root / kind
    if primary.exists():
        yield from sorted(primary.rglob("*.pdf"))
    if not include_incremental:
        return
    inc = root / "incremental"
    if inc.exists():
        for day_dir in sorted(inc.glob("day-*")):
            kind_dir = day_dir / kind
            if kind_dir.exists():
                yield from sorted(kind_dir.rglob("*.pdf"))


def extract_invoices(root: Path, *, include_incremental: bool = False) -> Iterator[tuple[Event, list[Fact]]]:
    for path in _walk(root, kind="rechnungen", include_incremental=include_incremental):
        yield _invoice_event(path)


def extract_letters(root: Path, *, include_incremental: bool = False) -> Iterator[tuple[Event, list[Fact]]]:
    for path in _walk(root, kind="briefe", include_incremental=include_incremental):
        yield _letter_event(path)
