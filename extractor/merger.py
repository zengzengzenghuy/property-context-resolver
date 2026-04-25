"""Merger — surgically render `context.property.<id>.md` and `context.unit.<id>.md`.

Two file types per the spine-v2-split schema:
- one `context.property.<LIE>.md` per property
- one `context.unit.<EH-XX>.md` per unit (v1 demo: just the flagship `EH-019`)

The merger only writes inside `<!-- auto:NAME -->` ... `<!-- /auto:NAME -->`
blocks; everything outside (footnotes, headers, prose, manual ## Notes blocks)
is preserved across runs. On first run we copy the schema template from
`context.<file_role>.template.md` and surgical-update each auto-block. On
subsequent runs we only replace block bodies.

Block render functions live in `extractor.blocks` and are dispatched via
`PROPERTY_BLOCKS` / `UNIT_BLOCKS` keyed on the auto-block name.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional

from .blocks import PROPERTY_BLOCKS, UNIT_BLOCKS
from .engine import FactStore


# ---------- auto-block primitives ----------

# Allow dots in block names (e.g. `auto:property.display_name`,
# `auto:tickets.critical`) — the old regex didn't.
_BLOCK_RE = re.compile(
    r"<!--\s*auto:(?P<name>[A-Za-z0-9_\-.]+)\s*-->"
    r"(?P<body>.*?)"
    r"<!--\s*/auto:(?P=name)\s*-->",
    re.DOTALL,
)


def _wrap(name: str, body: str) -> str:
    """Re-wrap rendered content in auto-block markers.

    Inline blocks (no newlines in body) stay on one line so they can sit inside
    a heading without breaking it; multi-line bodies get their own lines.
    """
    if "\n" in body.strip():
        return f"<!-- auto:{name} -->\n{body.rstrip()}\n<!-- /auto:{name} -->"
    return f"<!-- auto:{name} -->{body.strip()}<!-- /auto:{name} -->"


def _replace_blocks(existing: str, rendered: dict[str, str]) -> tuple[str, set[str]]:
    """Replace each known auto-block body with its rendered content.

    Unknown auto-blocks (not in `rendered`) are left untouched — the engine
    only owns the blocks it knows how to render.
    """
    seen: set[str] = set()

    def sub(m: re.Match[str]) -> str:
        name = m.group("name")
        if name in rendered:
            seen.add(name)
            return _wrap(name, rendered[name])
        return m.group(0)

    return _BLOCK_RE.sub(sub, existing), seen


def _has_auto_blocks(text: str) -> bool:
    return bool(_BLOCK_RE.search(text))


# ---------- mergers ----------

@dataclass
class _BaseMerger:
    fact_store: FactStore
    template_path: Path
    output_path: Path
    blocks: dict[str, Any]
    ctx: dict[str, Any] = field(default_factory=dict)

    def _render_blocks(self) -> dict[str, str]:
        return {name: fn(self.fact_store, self.ctx) for name, fn in self.blocks.items()}

    def _scaffold(self) -> str:
        if not self.template_path.exists():
            raise FileNotFoundError(
                f"Template not found at {self.template_path}; cannot scaffold "
                f"{self.output_path.name}."
            )
        return self.template_path.read_text(encoding="utf-8")

    def render_to_file(self) -> tuple[str, dict[str, Any]]:
        rendered = self._render_blocks()
        existing = (
            self.output_path.read_text(encoding="utf-8")
            if self.output_path.exists()
            else ""
        )

        if not existing.strip() or not _has_auto_blocks(existing):
            existing = self._scaffold()

        new_text, replaced = _replace_blocks(existing, rendered)
        missing = [n for n in self.blocks if n not in replaced]

        # Atomic write: tmp → rename so partial state never lands on disk.
        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.output_path.with_suffix(self.output_path.suffix + ".tmp")
        tmp.write_text(new_text, encoding="utf-8")
        tmp.replace(self.output_path)

        return new_text, {
            "blocks_replaced": len(replaced),
            "blocks_missing": missing,
            "wrote_fresh": not _has_auto_blocks(existing) if existing else True,
        }


class PropertyMerger(_BaseMerger):
    """Renders `context.property.<id>.md` from the schema template."""

    @classmethod
    def for_property(
        cls,
        store: FactStore,
        property_id: str,
        repo_root: Path,
        flagship_unit: Optional[str] = None,
    ) -> "PropertyMerger":
        return cls(
            fact_store=store,
            template_path=repo_root / "context.property.template.md",
            output_path=repo_root / f"context.property.{property_id}.md",
            blocks=PROPERTY_BLOCKS,
            ctx={
                "property_id": property_id,
                "flagship_unit": flagship_unit,
            },
        )


class UnitMerger(_BaseMerger):
    """Renders `context.unit.<EH-XX>.md` from the schema template."""

    @classmethod
    def for_unit(
        cls,
        store: FactStore,
        unit_id: str,
        repo_root: Path,
        property_id: str = "LIE-001",
        today: Optional[str] = None,
    ) -> "UnitMerger":
        # Tenants on this unit (resolves once per render).
        tenant_ids: list[str] = []
        for fact in store.all_facts():
            if fact.entity_type != "mieter" or not fact.entity_id:
                continue
            if fact.key == "einheit_id" and fact.value == unit_id:
                if fact.entity_id not in tenant_ids:
                    tenant_ids.append(fact.entity_id)
        return cls(
            fact_store=store,
            template_path=repo_root / "context.unit.template.md",
            output_path=repo_root / f"context.unit.{unit_id}.md",
            blocks=UNIT_BLOCKS,
            ctx={
                "unit_id": unit_id,
                "property_id": property_id,
                "tenant_ids": tenant_ids,
                "today": today,
            },
        )


# Back-compat alias for run.py / tests that import `Merger`.
Merger = PropertyMerger
SurgicalMerger = PropertyMerger
FLAGSHIP_TENANT = "MIE-001"  # legacy export — DunningReconciler still uses it


__all__ = [
    "PropertyMerger",
    "UnitMerger",
    "Merger",
    "SurgicalMerger",
    "FLAGSHIP_TENANT",
]
