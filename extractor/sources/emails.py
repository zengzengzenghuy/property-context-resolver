"""Email connector.

Parses RFC822 .eml files into events. Subject + body are run through a small
rule-based classifier that produces facts for the recurring intents in this
corpus (Mahnung, Verkaufsabsicht, Sonderumlage, Rechnung, etc.).

Schema-aware emission:
- ticket-like intents (Wasserschaden, Schimmel, Heizung, Fenster, Schluessel,
  Reparatur) emit `ticket.*` facts on the unit (resolved via einheit_nr)
- `vendor_dunning` (subject `Mahnung Rechnung RE-...`) emits `vendor_dunning.*`
  on the dienstleister
- `kuendigung_mietvertrag` emits `lease.cancellation_status=by_tenant` on the
  sender tenant
- `untervermietung` emits `subletting.current_status=requested` on the tenant
- `mietminderung_ankuendigung` emits `reductions.*` on the unit
- `wohnungsuebergabe` emits `handover.next_scheduled_*` on the unit

A second pass at the end of `extract()` clusters emails by normalized subject
and emits `sticky_thread.*` facts for any cluster of ≥ 3 messages — this is
what feeds the §4.3 "Sticky Communication Threads" block in the unit MD.
"""

from __future__ import annotations

import email
import email.policy
import re
import unicodedata
from collections import defaultdict
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any, Iterator, Optional

from ..identity import IdentityResolver
from ..models import Event, Fact, PROPERTY_ID
from ..source_ref import for_path


_UNIT_NUM_RX = re.compile(r"\b(?:WE|TG|GE)\s*\d{1,3}\b", re.IGNORECASE)
_UNIT_RX = re.compile(r"\bEH-\d{3}\b")
_TENANT_RX = re.compile(r"\bMIE-\d{3}\b")
_OWNER_RX = re.compile(r"\bEIG-\d{3}\b")
_VENDOR_RX = re.compile(r"\bDL-\d{3}\b")
_INVOICE_RX = re.compile(r"\b(?:RE|INV)-\d{4}-\d{3,5}\b")
_AMOUNT_RX = re.compile(r"(\d{1,3}(?:\.\d{3})*(?:,\d{2})?)\s*EUR", re.IGNORECASE)
_REPLY_PREFIX_RX = re.compile(r"^\s*(re|fw|fwd|aw|wg)\s*:\s*", re.IGNORECASE)


# Subject pattern → intent. First match wins. Order matters: more specific
# patterns must come before more generic catch-alls (e.g. ticket subjects
# beat the generic `\bschaden\b`).
_INTENT_PATTERNS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"\bmahnung\s+rechnung\b", re.IGNORECASE), "vendor_dunning"),
    (re.compile(r"\bmahnung\b", re.IGNORECASE), "mahnung"),
    (re.compile(r"\bwasserschaden\b|\bwater\s+damage\b", re.IGNORECASE), "ticket_wasserschaden"),
    (re.compile(r"\bschimmel\b", re.IGNORECASE), "ticket_schimmel"),
    (re.compile(r"\bheizung\s+f[aä]llt|heating\s+(?:broken|not\s+working)", re.IGNORECASE), "ticket_heizung"),
    (re.compile(r"\bdefektes?\s+fenster\b", re.IGNORECASE), "ticket_fenster"),
    (re.compile(r"\bverstopfter?\s+abfluss\b", re.IGNORECASE), "ticket_abfluss"),
    (re.compile(r"\bhaust(?:ü|ue)r\b.*\b(?:schlie[sß]t|kaputt)\b|\bhaust(?:ü|ue)r\s+schlie[sß]t\s+nicht\b", re.IGNORECASE), "ticket_haustuer"),
    (re.compile(r"\bschl(?:ü|ue)sselverlust\b|\bkey\s+replacement\b|\blost\s+key\b", re.IGNORECASE), "ticket_schluessel"),
    (re.compile(r"\bnachtrag\s+reparatur\b", re.IGNORECASE), "ticket_reparatur"),
    (re.compile(r"\bk(?:ü|ue)ndigung\s+mietvertrag\b", re.IGNORECASE), "kuendigung_mietvertrag"),
    (re.compile(r"\bwohnung\s+untervermieten\b|\bsublet\b", re.IGNORECASE), "untervermietung"),
    (re.compile(r"\bmietminderung\b", re.IGNORECASE), "mietminderung_ankuendigung"),
    (re.compile(r"\bwohnungs?[uü]bergabe\b|\b(?:move[\s-]?(?:in|out))\b", re.IGNORECASE), "wohnungsuebergabe"),
    (re.compile(r"\brechnung\b", re.IGNORECASE), "rechnung_eingang"),
    (re.compile(r"\bverkaufsabsicht\b", re.IGNORECASE), "verkaufsabsicht"),
    (re.compile(r"\bsonderumlage\b", re.IGNORECASE), "sonderumlage"),
    (re.compile(r"\bhausgeld(?:abrechnung)?\b", re.IGNORECASE), "hausgeld"),
    (re.compile(r"\bnebenkosten", re.IGNORECASE), "nebenkostenabrechnung"),
    (re.compile(r"\beinzug\b|\bauszug\b", re.IGNORECASE), "ein_auszug"),
    (re.compile(r"\bruhest(?:ö|oe)rung\b|\bnoise\s+complaint\b|\blaerm\b", re.IGNORECASE), "ruhestoerung"),
    (re.compile(r"\bschaden\b|\bdefekt\b|\breparatur\b", re.IGNORECASE), "schaden_general"),
    (re.compile(r"\beinladung\b|\bETV\b", re.IGNORECASE), "etv_einladung"),
    (re.compile(r"\bprotokoll\b", re.IGNORECASE), "etv_protokoll"),
    (re.compile(r"\bfrage\b|\brueckfrage\b|\brückfrage\b", re.IGNORECASE), "anfrage"),
]


_CRITICAL_TICKET_INTENTS = {
    "ticket_wasserschaden",
    "ticket_schimmel",
    "ticket_heizung",
}


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


def _normalize_subject(subject: str) -> str:
    """For sticky-thread clustering: strip Re:/Fwd: prefixes, lowercase, fold accents."""
    s = subject
    for _ in range(5):
        new = _REPLY_PREFIX_RX.sub("", s)
        if new == s:
            break
        s = new
    s = unicodedata.normalize("NFD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[^\w\s]+", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()


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
        hits = list(dict.fromkeys(rx.findall(text)))
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


def _resolve_unit(refs: dict[str, list[str]], resolver: Optional[IdentityResolver]) -> Optional[str]:
    """Pick a unit canonical id from the available signals."""
    if refs.get("einheit"):
        return refs["einheit"][0]
    if refs.get("einheit_nr") and resolver:
        ident = resolver.by_einheit_nr(refs["einheit_nr"][0])
        if ident:
            return ident.canonical_id
    return None


def _resolve_sender_tenant(sender: str, resolver: Optional[IdentityResolver]) -> Optional[str]:
    if not resolver or not sender:
        return None
    ident = resolver.by_email(sender)
    if ident and ident.entity_type == "mieter":
        return ident.canonical_id
    return None


def _resolve_vendor_from_invoice(invoice_ref: str, store_lookup: Optional[Any]) -> Optional[str]:
    """Vendor lookup by invoice ref deferred to a later projection — at email
    extraction time we may not yet have the rechnung→vendor mapping. Return
    None and let the renderer fall back."""
    return None


def _emit_eml(
    path: Path,
    resolver: Optional[IdentityResolver] = None,
) -> tuple[Event, list[Fact]]:
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
    observed_date = ts.split("T", 1)[0] if ts else None

    body_part = msg.get_body(preferencelist=("plain", "html"))
    body = body_part.get_content() if body_part is not None else ""

    text = f"{subject}\n{body}"
    refs = _entity_refs(text)
    intent = _classify(subject)
    primary_etype, primary_eid = _primary_entity(refs)
    unit_id = _resolve_unit(refs, resolver)
    tenant_id = _resolve_sender_tenant(sender, resolver)

    event = Event.make(
        source="email",
        source_ref=for_path(path),
        content=f"Subject: {subject}\nFrom: {sender}\nTo: {recipient}\n\n{body}",
        timestamp=ts,
        metadata={
            "subject": subject,
            "subject_normalized": _normalize_subject(subject),
            "from": sender,
            "to": recipient,
            "message_id": msg["Message-ID"],
            "in_reply_to": msg["In-Reply-To"],
            "intent": intent,
            "refs": refs,
            "is_reply": bool(_REPLY_PREFIX_RX.match(subject)),
            "resolved_unit_id": unit_id,
            "resolved_tenant_id": tenant_id,
        },
    )

    facts: list[Fact] = []

    def add(key: str, value: Any, *, etype: Optional[str] = primary_etype,
            eid: Optional[str] = primary_eid, confidence: float = 0.9) -> None:
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

    # Base communication facts on the primary entity (legacy behavior).
    add("communication.subject", subject, confidence=1.0)
    add("communication.from", sender, confidence=1.0)
    if intent:
        add("communication.intent", intent, confidence=0.85)

    # Intent-driven, schema-aware emissions.
    if intent and intent.startswith("ticket_") and unit_id:
        severity = "critical" if intent in _CRITICAL_TICKET_INTENTS else "normal"
        ticket_type = intent.replace("ticket_", "")
        add("ticket.type", ticket_type, etype="einheit", eid=unit_id, confidence=0.85)
        add("ticket.severity", severity, etype="einheit", eid=unit_id, confidence=0.85)
        add("ticket.title", subject, etype="einheit", eid=unit_id, confidence=0.9)
        if observed_date:
            add("ticket.opened_at", observed_date, etype="einheit", eid=unit_id, confidence=0.9)
    elif intent == "vendor_dunning":
        # Subject: "Mahnung Rechnung RE-2024-8659"
        invoice_id = None
        if mr := _INVOICE_RX.search(subject):
            invoice_id = mr.group(0)
        elif refs.get("rechnung"):
            invoice_id = refs["rechnung"][0]
        # Vendor entity: prefer DL-XXX in body, else attach to the invoice id
        # so a later projection step can move it to the right vendor.
        dl_id = (refs.get("dienstleister") or [None])[0]
        eid = dl_id or invoice_id
        etype = "dienstleister" if dl_id else "rechnung"
        if eid:
            if invoice_id:
                add("vendor_dunning.invoice_no", invoice_id, etype=etype, eid=eid, confidence=0.95)
            add("vendor_dunning.stage", 1, etype=etype, eid=eid, confidence=0.9)
            if observed_date:
                add("vendor_dunning.since", observed_date, etype=etype, eid=eid, confidence=0.9)
            amounts = [_parse_amount(a) for a in _AMOUNT_RX.findall(text)]
            amounts = [a for a in amounts if a is not None]
            if amounts:
                add("vendor_dunning.amount_eur", max(amounts), etype=etype, eid=eid, confidence=0.7)
    elif intent == "kuendigung_mietvertrag" and tenant_id:
        add("lease.cancellation_status", "by_tenant",
            etype="mieter", eid=tenant_id, confidence=0.9)
        if observed_date:
            add("lease.cancellation_notice_date", observed_date,
                etype="mieter", eid=tenant_id, confidence=0.9)
        # Project to unit too, so the unit MD's recurring + lease blocks see it.
        unit = unit_id or _ensure_unit_for_tenant(resolver, tenant_id)
        if unit:
            add("lease.cancellation_status", "by_tenant",
                etype="einheit", eid=unit, confidence=0.85)
            if observed_date:
                add("lease.cancellation_notice_date", observed_date,
                    etype="einheit", eid=unit, confidence=0.85)
    elif intent == "untervermietung":
        target = tenant_id or unit_id
        target_etype = "mieter" if tenant_id else "einheit"
        if target:
            add("subletting.current_status", "requested",
                etype=target_etype, eid=target, confidence=0.85)
    elif intent == "mietminderung_ankuendigung":
        unit = unit_id or _ensure_unit_for_tenant(resolver, tenant_id)
        if unit:
            if observed_date:
                add("reductions.date_raised", observed_date,
                    etype="einheit", eid=unit, confidence=0.85)
            add("reductions.status", "unilateral",
                etype="einheit", eid=unit, confidence=0.8)
            add("reductions.reason", "ungelöste Reparaturen (auto-detected)",
                etype="einheit", eid=unit, confidence=0.6)
    elif intent == "wohnungsuebergabe":
        unit = unit_id or _ensure_unit_for_tenant(resolver, tenant_id)
        if unit and observed_date:
            add("handover.next_scheduled_date", observed_date,
                etype="einheit", eid=unit, confidence=0.7)
            add("handover.next_scheduled_type", "Auszug",
                etype="einheit", eid=unit, confidence=0.7)

    # Legacy mahnung-against-tenant rule (inbound mahnung email — not the
    # vendor dunning case which we've already handled).
    if intent == "mahnung":
        amounts = [_parse_amount(a) for a in _AMOUNT_RX.findall(body)]
        amounts = [a for a in amounts if a is not None]
        if amounts:
            add("mahnung.offener_betrag_eur", max(amounts), confidence=0.7)
        if invoices := refs.get("rechnung"):
            add("mahnung.invoice_ref", invoices[0], confidence=0.95)
    if intent == "verkaufsabsicht" and refs.get("einheit_nr"):
        add("verkauf.einheit_nr", refs["einheit_nr"][0], confidence=0.9)
    if intent == "sonderumlage":
        amounts = [_parse_amount(a) for a in _AMOUNT_RX.findall(text)]
        if amounts:
            add("sonderumlage.betrag_eur", max(amounts), confidence=0.6)

    return event, facts


def _ensure_unit_for_tenant(
    resolver: Optional[IdentityResolver], tenant_id: Optional[str],
) -> Optional[str]:
    """Look up the einheit_id for a tenant via the IdentityResolver's loaded
    stammdaten. The resolver caches `mieter` records as Identity rows but not
    the einheit_id link — so we re-walk its `_stamm` payload."""
    if not resolver or not tenant_id:
        return None
    for t in resolver._stamm.get("mieter", []):
        if t.get("id") == tenant_id:
            return t.get("einheit_id")
    return None


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


# ---------- sticky-thread clustering ----------

# After all individual email events are yielded, group by normalized subject
# and emit one synthetic "sticky_thread" event per cluster of ≥ STICKY_MIN
# messages. Facts are attached to the most-frequent tenant (by sender), or
# to the most-frequent unit when there's no clear tenant.
STICKY_MIN = 3


def _cluster_thread_facts(
    events_by_subject: dict[str, list[dict[str, Any]]],
    resolver: Optional[IdentityResolver],
) -> Iterator[tuple[Event, list[Fact]]]:
    for subject_norm, items in events_by_subject.items():
        if len(items) < STICKY_MIN:
            continue
        items_sorted = sorted(items, key=lambda i: i.get("timestamp") or "")
        first = items_sorted[0]
        last = items_sorted[-1]

        # Pick the most frequent tenant or unit signal.
        from collections import Counter
        tenant_counts = Counter(i["tenant_id"] for i in items if i.get("tenant_id"))
        unit_counts = Counter(i["unit_id"] for i in items if i.get("unit_id"))
        tenant_id = tenant_counts.most_common(1)[0][0] if tenant_counts else None
        unit_id = unit_counts.most_common(1)[0][0] if unit_counts else None

        eid = tenant_id or unit_id
        etype = "mieter" if tenant_id else ("einheit" if unit_id else None)
        if eid is None:
            continue

        # Synthetic event: cite the latest message in the cluster.
        cluster_event = Event.make(
            source="email",
            source_ref=last["source_ref"],
            content=f"[sticky-thread] {first['subject']} — {len(items)} msgs",
            timestamp=last.get("timestamp"),
            metadata={
                "cluster": True,
                "subject_normalized": subject_norm,
                "msg_count": len(items),
                "first_msg_date": first.get("timestamp"),
                "last_msg_date": last.get("timestamp"),
            },
        )
        observed = (last.get("timestamp") or "").split("T", 1)[0] or None

        def _f(key: str, value: Any, conf: float = 0.85) -> Fact:
            return Fact.make(
                property_id=PROPERTY_ID,
                entity_type=etype,
                entity_id=eid,
                key=key,
                value=value,
                source_event_id=cluster_event.id,
                source_ref=cluster_event.source_ref,
                observed_at=observed,
                confidence=conf,
            )

        facts = [
            _f("sticky_thread.subject", first["subject"]),
            _f("sticky_thread.subject_normalized", subject_norm),
            _f("sticky_thread.msg_count", len(items), conf=1.0),
            _f("sticky_thread.first_msg_date", (first.get("timestamp") or "").split("T", 1)[0] or None),
            _f("sticky_thread.last_msg_date", observed),
            _f("sticky_thread.status", "active"),
        ]
        yield cluster_event, [f for f in facts if f.value not in (None, "", [])]


def extract(
    root: Path,
    *,
    include_incremental: bool = False,
    resolver: Optional[IdentityResolver] = None,
) -> Iterator[tuple[Event, list[Fact]]]:
    threads: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for emails_root in _email_roots(root, include_incremental):
        for path in sorted(emails_root.rglob("*.eml")):
            try:
                event, facts = _emit_eml(path, resolver=resolver)
                yield event, facts
                # Track for clustering.
                md = event.metadata or {}
                if md.get("subject") and not md.get("is_reply"):
                    # Group reply chains under the parent's normalized subject.
                    pass
                subj_norm = md.get("subject_normalized") or _normalize_subject(md.get("subject", ""))
                if subj_norm:
                    threads[subj_norm].append({
                        "subject": md.get("subject", ""),
                        "timestamp": event.timestamp,
                        "source_ref": event.source_ref,
                        "tenant_id": md.get("resolved_tenant_id"),
                        "unit_id": md.get("resolved_unit_id"),
                    })
            except Exception as e:
                err_event = Event.make(
                    source="email",
                    source_ref=for_path(path),
                    content=f"<unparseable: {e}>",
                    metadata={"error": str(e)},
                )
                yield err_event, []
    # Sticky-thread cluster pass.
    yield from _cluster_thread_facts(threads, resolver)
