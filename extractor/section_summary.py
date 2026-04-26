"""Generic per-section summary renderer.

Each section in `context.<unit|property>.<id>.md` has a `<!-- auto:<name>.summary -->`
auto-block. This module turns a section spec (which facts are in scope, whether
to load raw content) into a `render(store, ctx) -> str` that follows the
existing dunning summary pattern: deterministic Python builds a salience
payload, the Summarizer renders ≤3 German sentences with triage tag + Trifecta
+ citations, and an empty section emits `_no issue_`.

The cache in `Summarizer._key` SHA256s the full payload, so adding new raw
content invalidates exactly the affected sections. Unchanged raw → cache hit.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Callable, Iterable

from .engine import FactStore, _source_from_ref
from .models import Fact
from .raw_loader import gather_excerpts
from .summarizer import get_summarizer


_NO_ISSUE = "_no issue_"

# Caps so a section payload stays well under the haiku context budget.
_MAX_SIGNAL_FACTS = 60
_MAX_REFERENCES = 8
_DEFAULT_MAX_RAW_FILES = 15
_DEFAULT_PER_FILE_CHARS = 1500


FactFilter = Callable[[Fact, dict[str, Any]], bool]


def _collect(store: FactStore, ctx: dict[str, Any], match: FactFilter) -> list[Fact]:
    return [f for f in store.all_facts() if match(f, ctx)]


def _signal_facts(facts: Iterable[Fact]) -> list[dict[str, Any]]:
    """Compact projection of each fact, newest-first, deduped by (entity, key)."""
    out: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    for f in sorted(facts, key=lambda x: (x.observed_at or x.extracted_at or ""), reverse=True):
        sig = (f.entity_id or "", f.key)
        if sig in seen:
            continue
        seen.add(sig)
        out.append({
            "entity_id": f.entity_id,
            "entity_type": f.entity_type,
            "key": f.key,
            "value": f.value,
            "observed_at": f.observed_at,
        })
        if len(out) >= _MAX_SIGNAL_FACTS:
            break
    return out


def _references(facts: Iterable[Fact]) -> list[dict[str, str]]:
    refs: list[dict[str, str]] = []
    seen: set[str] = set()
    for f in facts:
        ref = f.source_ref or ""
        if not ref or ref in seen:
            continue
        seen.add(ref)
        refs.append({"label": _source_from_ref(ref) or "source", "url": ref})
        if len(refs) >= _MAX_REFERENCES:
            break
    return refs


def _fallback(section: str, signal: dict[str, Any]) -> str:
    """Deterministic when LLM unavailable. No narrative, just a triage tag + counts."""
    facts = signal.get("facts", [])
    if not facts:
        return _NO_ISSUE
    excerpts = signal.get("raw_excerpts") or []
    bits = [f"{len(facts)} Fakten"]
    if excerpts:
        bits.append(f"{len(excerpts)} Quellen")
    return f"[Routine] {section}: " + ", ".join(bits) + " (siehe Tabelle/Liste unten)."


def make_section_summary(
    section: str,
    *,
    fact_filter: FactFilter,
    include_raw: bool = False,
    max_raw_files: int = _DEFAULT_MAX_RAW_FILES,
    per_file_chars: int = _DEFAULT_PER_FILE_CHARS,
) -> Callable[[FactStore, dict[str, Any]], str]:
    """Return a `render(store, ctx)` for the section."""

    def render(store: FactStore, ctx: dict[str, Any]) -> str:
        facts = _collect(store, ctx, fact_filter)
        if not facts:
            return _NO_ISSUE

        signal: dict[str, Any] = {"facts": _signal_facts(facts)}
        refs = _references(facts)

        raw_root = ctx.get("raw_root")
        if include_raw and raw_root:
            excerpts = gather_excerpts(
                facts, Path(raw_root),
                max_files=max_raw_files,
                per_file_chars=per_file_chars,
            )
            if excerpts:
                signal["raw_excerpts"] = excerpts

        fallback = _fallback(section, signal)
        summarizer = ctx.get("summarizer") or get_summarizer()
        return summarizer.summarize(
            signal,
            section=section,
            fallback=fallback,
            references=refs,
            today=ctx.get("today"),
        )

    return render


__all__ = ["make_section_summary", "FactFilter"]
