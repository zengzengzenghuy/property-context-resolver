"""Load raw source content for LLM summary payloads.

The Signal-First philosophy summarizes facts plus the *actual content* of the
emails / letters / bank rows / stammdaten entries that produced those facts.
This module maps a fact's `source_ref` (a GitHub blob URL or a local absolute
path) back to a local file under `raw/`, reads a bounded excerpt, and returns
it in a shape the summarizer can drop into its JSON payload.

Cache invalidation is content-addressed: the summarizer SHA256s the full
payload (including these excerpts), so re-running with unchanged raw files
hits the cache and re-running with new files misses it. No separate "what's
new" tracker needed.
"""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path
from typing import Any, Iterable, Optional

from .models import Fact


_RAW_PATH_RE = re.compile(r"/raw/(.+)$")


def local_path_from_source_ref(source_ref: str, raw_root: Path) -> Optional[Path]:
    """Strip the GitHub URL prefix + fragment, return the local file under raw_root."""
    if not source_ref:
        return None
    no_frag = source_ref.split("#", 1)[0]
    m = _RAW_PATH_RE.search(no_frag)
    if not m:
        return None
    return raw_root / m.group(1)


def _read_email(path: Path, max_chars: int) -> str:
    """Plain-text body + headers of a .eml. Falls back to raw bytes on errors."""
    try:
        from email import policy
        from email.parser import BytesParser
        with path.open("rb") as f:
            msg = BytesParser(policy=policy.default).parse(f)
        subj = msg.get("Subject", "")
        date = msg.get("Date", "")
        sender = msg.get("From", "")
        body_part = msg.get_body(preferencelist=("plain", "html"))
        body = body_part.get_content() if body_part else ""
        text = f"From: {sender}\nDate: {date}\nSubject: {subj}\n\n{body.strip()}"
        return text[:max_chars]
    except Exception:
        try:
            return path.read_text(encoding="utf-8", errors="ignore")[:max_chars]
        except OSError:
            return ""


def _read_pdf(path: Path, max_chars: int) -> str:
    """Pre-OCR cache (`<file>.pdf.txt`) only. Don't shell out to pdfminer here —
    the `scripts/preocr.py` pass owns that, per CLAUDE.md."""
    cache = path.with_suffix(path.suffix + ".txt")
    if cache.exists():
        try:
            return cache.read_text(encoding="utf-8", errors="ignore")[:max_chars]
        except OSError:
            return ""
    return ""


def _read_bank_row(path: Path, fragment: str, max_chars: int) -> str:
    """Pull the row whose any cell contains the fragment id (e.g. `TX-01557`)."""
    if not path.exists():
        return ""
    try:
        with path.open(encoding="utf-8", errors="ignore") as f:
            reader = csv.reader(f, delimiter=";")
            header = next(reader, None)
            for row in reader:
                if fragment and any(fragment in c for c in row):
                    pairs = list(zip(header or [], row))
                    return "; ".join(f"{k}={v}" for k, v in pairs)[:max_chars]
    except OSError:
        return ""
    return ""


def _read_stammdaten(path: Path, fragment: str, max_chars: int) -> str:
    """For `stammdaten.json#<table>/<id>` — pull just the matching record."""
    if not path.exists() or "/" not in fragment:
        return ""
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return ""
    table, key = fragment.split("/", 1)
    items = data.get(table)
    if not isinstance(items, list):
        return ""
    id_keys = ("id", "mieter_id", "eigentuemer_id", "einheit_id",
               "haus_id", "dienstleister_id", "liegenschaft_id")
    for item in items:
        if not isinstance(item, dict):
            continue
        for k in id_keys:
            if item.get(k) == key:
                return json.dumps(item, ensure_ascii=False)[:max_chars]
    return ""


def load_excerpt(
    source_ref: str, raw_root: Path, *, max_chars: int = 2000,
) -> Optional[dict[str, str]]:
    """Best-effort excerpt for a single source_ref. None if not resolvable."""
    if "#" in source_ref:
        bare, fragment = source_ref.split("#", 1)
    else:
        bare, fragment = source_ref, ""
    path = local_path_from_source_ref(bare, raw_root)
    if path is None or not path.exists():
        return None

    suffix = path.suffix.lower()
    s = str(path)
    if suffix == ".eml":
        text, kind = _read_email(path, max_chars), "email"
    elif suffix == ".pdf":
        text = _read_pdf(path, max_chars)
        kind = "letter" if "/briefe/" in s else "invoice" if "/rechnungen/" in s else "pdf"
    elif suffix == ".csv":
        text = _read_bank_row(path, fragment, max_chars)
        kind = "bank-row"
    elif suffix == ".json":
        text = _read_stammdaten(path, fragment, max_chars)
        kind = "stammdaten"
    else:
        return None
    if not text:
        return None
    return {"kind": kind, "ref": source_ref, "name": path.name, "excerpt": text}


def gather_excerpts(
    facts: Iterable[Fact],
    raw_root: Path,
    *,
    max_files: int = 20,
    per_file_chars: int = 2000,
) -> list[dict[str, Any]]:
    """Walk facts (newest first), dedup by source_ref, load up to `max_files`."""
    seen: set[str] = set()
    out: list[dict[str, Any]] = []
    sorted_facts = sorted(
        facts,
        key=lambda f: (f.observed_at or f.extracted_at or ""),
        reverse=True,
    )
    for f in sorted_facts:
        ref = f.source_ref or ""
        if not ref or ref in seen:
            continue
        seen.add(ref)
        ex = load_excerpt(ref, raw_root, max_chars=per_file_chars)
        if ex:
            out.append(ex)
        if len(out) >= max_files:
            break
    return out


__all__ = ["local_path_from_source_ref", "load_excerpt", "gather_excerpts"]
