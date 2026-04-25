"""Supabase client wrapper for the engine.

The engine writes the rendered `context.md` to `properties.context_md` and
appends a one-line summary row to `context_updates`. That's the entire
contract — see final_execution.md "Supabase schema".

Service-role key, never anon. The engine is backend-only.

If SUPABASE_URL or SUPABASE_SERVICE_KEY is missing the wrapper degrades to a
no-op so `python run.py raw/` still produces local artifacts in environments
without Supabase credentials (CI, fresh clone, demo-prep machines).
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

try:
    from supabase import Client, create_client
except ImportError:
    Client = None  # type: ignore[assignment]
    create_client = None  # type: ignore[assignment]


@dataclass
class SupabaseSink:
    """Mirror engine output into Supabase. No-op when not configured."""
    client: Optional["Client"] = None

    @classmethod
    def from_env(cls) -> "SupabaseSink":
        url = os.environ.get("SUPABASE_URL")
        key = os.environ.get("SUPABASE_SERVICE_KEY")
        if not url or not key or create_client is None:
            return cls(client=None)
        return cls(client=create_client(url, key))

    @property
    def enabled(self) -> bool:
        return self.client is not None

    def upsert_context(self, property_id: str, context_md: str,
                       name: Optional[str] = None,
                       address: Optional[str] = None) -> None:
        if not self.enabled:
            return
        row: dict = {
            "property_id": property_id,
            "context_md": context_md,
            # ISO-8601 UTC string — PostgREST coerces to timestamptz on insert.
            # Don't send "now()" here: PostgREST treats body fields as data,
            # not SQL, so the literal string would fail the timestamptz cast.
            "last_run_at": datetime.now(timezone.utc).isoformat(),
        }
        if name is not None:
            row["name"] = name
        if address is not None:
            row["address"] = address
        self.client.table("properties").upsert(row, on_conflict="property_id").execute()

    def log_update(self, property_id: str, source_filename: str,
                   diff_summary: str) -> None:
        if not self.enabled:
            return
        self.client.table("context_updates").insert({
            "property_id": property_id,
            "source_filename": source_filename,
            "diff_summary": diff_summary,
        }).execute()

    def read_context(self, property_id: str) -> Optional[str]:
        if not self.enabled:
            return None
        resp = (
            self.client.table("properties")
            .select("context_md")
            .eq("property_id", property_id)
            .single()
            .execute()
        )
        return (resp.data or {}).get("context_md")
