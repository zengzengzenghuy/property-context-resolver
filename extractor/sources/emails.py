"""Email connector.

Parses RFC822 .eml files into events. Subject + body are run through a small
rule-based classifier that produces facts for the recurring intents in this
corpus (Mahnung, Verkaufsabsicht, Sonderumlage, Rechnung, etc.). Anything the
classifier can't tag still produces a base event so the merge layer can
reconsider it later (LLM or human review).
"""

from __future__ import annotations

import email
import email.policy
import re
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any, Iterator, Optional

from ..models import Event, Fact, PROPERTY_ID
from ..source_ref import for_path


_UNIT_NUM_RX = re.compile(r"\b(?:WE|TG|GE)\s*\d{1,3}\b", re.IGNORECASE)
_UNIT_RX = re.compile(r"\bEH-\d{3}\b")
_TENANT_RX = re.compile(r"\bMIE-\d{3}\b")
_OWNER_RX = re.compile(r"\bEIG-\d{3}\b")
_VENDOR_RX = re.compile(r"\bDL-\d{3}\b")
_INVOICE_RX = re.compile(r"\b(?:RE|INV)-\d{4}-\d{3,5}\b")
_AMOUNT_RX = re.compile(r"(\d{1,3}(?:\.\d{3})*(?:,\d{2})?)\s*EUR", re.IGNORECASE)


# Subject pattern → intent. First match wins.
_INTENT_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"\bmahnung\b", re.IGNORECASE), "mahnung"),
    (re.compile(r"\brechnung\b", re.IGNORECASE), "rechnung_eingang"),
    (re.compile(r"\bverkaufsabsicht\b", re.IGNORECASE), "verkaufsabsicht"),
    (re.compile(r"\bsonderumlage\b", re.IGNORECASE), "sonderumlage"),
    (re.compile(r"\bhausgeld(?:abrechnung)?\b", re.IGNORECASE), "hausgeld"),
    (re.compile(r"\bnebenkosten", re.IGNORECASE), "nebenkostenabrechnung"),
    (re.compile(r"\bk(?:ü|ue)ndigung\b", re.IGNORECASE), "kuendigung"),
    (re.compile(r"\beinzug\b|\bauszug\b", re.IGNORECASE), "ein_auszug"),
    (re.compile(r"\bschaden\b|\bdefekt\b|\breparatur\b", re.IGNORECASE), "schaden"),
    (re.compile(r"\beinladung\b|\bETV\b", re.IGNORECASE), "etv_einladung"),
    (re.compile(r"\bprotokoll\b", re.IGNORECASE), "etv_protokoll"),
    (re.compile(r"\bfrage\b|\brueckfrage\b|\brückfrage\b", re.IGNORECASE), "anfrage"),
]


def _parse_amount(s: str) -> Optional[float]:
    cleaned = s.replace(".", "").replace(",", ".")
    try:
        return float(cleaned)
    except ValueError:
        return None


def _to_iso(dt: Optional[datetime]) -> Optional[str]:
    if dt is None:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc).isoformat(timespec="seconds")


def _classify(subject: str) -> Optional[str]:
    for rx, intent in _INTENT_PATTERNS:
        if rx.search(subject):
            return intent
    return None


def _entity_refs(text: str) -> dict[str, list[str]]:
    refs: dict[str, list[str]] = {}
    for label, rx in (
        ("mieter", _TENANT_RX),
        ("eigentuemer", _OWNER_RX),
        ("dienstleister", _VENDOR_RX),
        ("einheit", _UNIT_RX),
        ("einheit_nr", _UNIT_NUM_RX),
        ("rechnung", _INVOICE_RX),
    ):
        hits = list(dict.fromkeys(rx.findall(text)))  # dedupe, preserve order
        if hits:
            refs[label] = hits
    return refs


def _primary_entity(refs: dict[str, list[str]]) -> tuple[Optional[str], Optional[str]]:
    for etype in ("mieter", "eigentuemer", "dienstleister", "einheit"):
        if refs.get(etype):
            return etype, refs[etype][0]
    if refs.get("rechnung"):
        return "rechnung", refs["rechnung"][0]
    return None, None


def _emit_eml(path: Path) -> tuple[Event, list[Fact]]:
    raw = path.read_bytes()
    msg = email.message_from_bytes(raw, policy=email.policy.default)
    subject = (msg["Subject"] or "").strip()
    sender = (msg["From"] or "").strip()
    recipient = (msg["To"] or "").strip()
    date_hdr = msg["Date"]
    try:
        ts = _to_iso(parsedate_to_datetime(date_hdr)) if date_hdr else None
    except (TypeError, ValueError):
        ts = None

    body_part = msg.get_body(preferencelist=("plain", "html"))
    body = body_part.get_content() if body_part is not None else ""

    text = f"{subject}\n{body}"
    refs = _entity_refs(text)
    intent = _classify(subject)
    etype, eid = _primary_entity(refs)

    event = Event.make(
        source="email",
        source_ref=for_path(path),
        content=f"Subject: {subject}\nFrom: {sender}\nTo: {recipient}\n\n{body}",
        timestamp=ts,
        metadata={
            "subject": subject,
            "from": sender,
            "to": recipient,
            "message_id": msg["Message-ID"],
            "in_reply_to": msg["In-Reply-To"],
            "intent": intent,
            "refs": refs,
        },
    )

    facts: list[Fact] = []

    def add(key: str, value: Any, confidence: float = 0.9) -> None:
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
                observed_at=ts,
                confidence=confidence,
            )
        )

    add("communication.subject", subject, 1.0)
    add("communication.from", sender, 1.0)
    add("communication.intent", intent, 0.85 if intent else 0.0) if intent else None
    if intent and intent == "mahnung":
        amounts = [_parse_amount(a) for a in _AMOUNT_RX.findall(body)]
        amounts = [a for a in amounts if a is not None]
        if amounts:
            add("mahnung.offener_betrag_eur", max(amounts), 0.7)
        if invoices := refs.get("rechnung"):
            add("mahnung.invoice_ref", invoices[0], 0.95)
    if intent == "verkaufsabsicht" and refs.get("einheit_nr"):
        add("verkauf.einheit_nr", refs["einheit_nr"][0], 0.9)
    if intent == "sonderumlage":
        amounts = [_parse_amount(a) for a in _AMOUNT_RX.findall(text)]
        if amounts:
            add("sonderumlage.betrag_eur", max(amounts), 0.6)

    return event, facts


def _email_roots(root: Path, include_incremental: bool) -> list[Path]:
    roots: list[Path] = []
    primary = root / "emails"
    if primary.exists():
        roots.append(primary)
    if not include_incremental:
        return roots
    inc = root / "incremental"
    if inc.exists():
        for day_dir in sorted(inc.glob("day-*")):
            ed = day_dir / "emails"
            if ed.exists():
                roots.append(ed)
    return roots


def extract(root: Path, *, include_incremental: bool = False) -> Iterator[tuple[Event, list[Fact]]]:
    for emails_root in _email_roots(root, include_incremental):
        for path in sorted(emails_root.rglob("*.eml")):
            try:
                yield _emit_eml(path)
            except Exception as e:  # corrupted .eml shouldn't kill the run
                err_event = Event.make(
                    source="email",
                    source_ref=for_path(path),
                    content=f"<unparseable: {e}>",
                    metadata={"error": str(e)},
                )
                yield err_event, []
