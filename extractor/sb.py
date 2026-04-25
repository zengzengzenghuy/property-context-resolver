"""Supabase client wrapper for the engine.

Mirrors the rendered context files into Supabase under the spine-v2-split
schema (one row per property in `properties`, one row per unit in `units`).
A one-line audit row is appended to `context_updates` for each write —
property-scoped or unit-scoped (with `unit_id` set).

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

    def upsert_unit(self, unit_id: str, property_id: str, context_md: str,
                    label: Optional[str] = None,
                    occupancy: Optional[str] = None) -> bool:
        """Mirror one unit's rendered `context.unit.<EH-XX>.md`.

        Returns True on success, False if the call was a no-op or skipped
        (e.g. because the `units` table doesn't exist yet — migration 0002).

        Requires the `units` table from migration 0002. Older deployments
        without it get a 404 from PostgREST; we swallow the failure with a
        warning so a missing migration doesn't tank the whole pipeline."""
        if not self.enabled:
            return False
        row: dict = {
            "unit_id": unit_id,
            "property_id": property_id,
            "context_md": context_md,
            "last_run_at": datetime.now(timezone.utc).isoformat(),
        }
        if label is not None:
            row["label"] = label
        if occupancy is not None:
            row["occupancy"] = occupancy
        try:
            self.client.table("units").upsert(row, on_conflict="unit_id").execute()
            return True
        except Exception as e:
            print(f"  [sb] upsert_unit({unit_id}) skipped: {e}")
            return False

    def log_update(self, property_id: str, source_filename: str,
                   diff_summary: str, *, unit_id: Optional[str] = None) -> None:
        if not self.enabled:
            return
        row: dict = {
            "property_id": property_id,
            "source_filename": source_filename,
            "diff_summary": diff_summary,
        }
        if unit_id is not None:
            row["unit_id"] = unit_id
        try:
            self.client.table("context_updates").insert(row).execute()
        except Exception as e:
            # `unit_id` column requires migration 0002. Retry without it so
            # property-scoped logs still land on older deployments.
            if unit_id is not None and "unit_id" in str(e):
                row.pop("unit_id", None)
                self.client.table("context_updates").insert(row).execute()
            else:
                raise

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

    def read_unit(self, unit_id: str) -> Optional[str]:
        if not self.enabled:
            return None
        resp = (
            self.client.table("units")
            .select("context_md")
            .eq("unit_id", unit_id)
            .single()
            .execute()
        )
        return (resp.data or {}).get("context_md")
