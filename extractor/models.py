"""Normalized event + fact records.

Events are the common envelope produced by source connectors:
    (id, source, source_ref, timestamp, property_id, content, metadata)

Facts are structured `(property_id, entity_type, entity_id, key, value, source_ref, ...)`
records produced by extractors, each citing the originating event.
"""

from __future__ import annotations

import dataclasses
import hashlib
import json
import os
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Iterable, Optional


PROPERTY_ID = "LIE-001"


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def stable_id(*parts: str) -> str:
    h = hashlib.sha1("|".join(parts).encode("utf-8")).hexdigest()
    return h[:16]


@dataclass
class Event:
    id: str
    source: str               # "stammdaten" | "bank" | "email" | "invoice" | "letter"
    source_ref: str           # path or stable URI back to the raw artifact
    timestamp: Optional[str]  # ISO-8601 UTC if known
    property_id: str
    content: str              # human-readable raw content (may be truncated)
    metadata: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def make(
        cls,
        source: str,
        source_ref: str,
        content: str,
        timestamp: Optional[str] = None,
        property_id: str = PROPERTY_ID,
        metadata: Optional[dict[str, Any]] = None,
    ) -> "Event":
        return cls(
            id=stable_id(source, source_ref, content[:64]),
            source=source,
            source_ref=source_ref,
            timestamp=timestamp,
            property_id=property_id,
            content=content,
            metadata=metadata or {},
        )

    def to_json(self) -> dict[str, Any]:
        return dataclasses.asdict(self)


@dataclass
class Fact:
    id: str
    property_id: str
    entity_type: Optional[str]    # "einheit" | "eigentuemer" | "mieter" | "dienstleister" | "rechnung" | "letter" | None
    entity_id: Optional[str]      # e.g. "EH-014", "MIE-022", "DL-010", "RE-2024-0097"
    key: str
    value: Any
    source_event_id: str
    source_ref: str
    confidence: float = 1.0
    observed_at: Optional[str] = None
    extracted_at: str = field(default_factory=_now_iso)

    @classmethod
    def make(
        cls,
        property_id: str,
        key: str,
        value: Any,
        source_event_id: str,
        source_ref: str,
        entity_type: Optional[str] = None,
        entity_id: Optional[str] = None,
        confidence: float = 1.0,
        observed_at: Optional[str] = None,
    ) -> "Fact":
        return cls(
            id=stable_id(property_id, entity_type or "", entity_id or "", key,
                         json.dumps(value, sort_keys=True, default=str), source_event_id),
            property_id=property_id,
            entity_type=entity_type,
            entity_id=entity_id,
            key=key,
            value=value,
            source_event_id=source_event_id,
            source_ref=source_ref,
            confidence=confidence,
            observed_at=observed_at,
        )

    def to_json(self) -> dict[str, Any]:
        return dataclasses.asdict(self)


class JsonlWriter:
    """Append-once JSONL writer that truncates on first open."""

    def __init__(self, path: str):
        self.path = path
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        self._fh = open(path, "w", encoding="utf-8")
        self.count = 0

    def write(self, obj: Any) -> None:
        if hasattr(obj, "to_json"):
            obj = obj.to_json()
        self._fh.write(json.dumps(obj, ensure_ascii=False, default=str))
        self._fh.write("\n")
        self.count += 1

    def write_many(self, objs: Iterable[Any]) -> None:
        for o in objs:
            self.write(o)

    def close(self) -> None:
        self._fh.close()

    def __enter__(self) -> "JsonlWriter":
        return self

    def __exit__(self, *exc: Any) -> None:
        self.close()
