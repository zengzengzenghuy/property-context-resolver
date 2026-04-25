"""Unit tests for the surgical Merger.

Run:
    python -m unittest tests.test_merger -v
"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from extractor.engine import FactStore
from extractor.merger import (
    FLAGSHIP_TENANT,
    PROPERTY_ID,
    SurgicalMerger,
    _BLOCK_RE_TMPL,
    _replace_blocks,
    _wrap,
)
from extractor.models import Fact


def fact(*, fact_id: str, entity_id: str, key: str, value, source_ref: str,
         observed_at: str | None = None, source_event_id: str = "ev1",
         confidence: float = 1.0) -> Fact:
    return Fact(
        id=fact_id,
        property_id=PROPERTY_ID,
        entity_type=None,
        entity_id=entity_id,
        key=key,
        value=value,
        source_event_id=source_event_id,
        source_ref=source_ref,
        confidence=confidence,
        observed_at=observed_at,
        extracted_at="2026-04-25T10:00:00+00:00",
    )


class AutoBlockRoundTripTests(unittest.TestCase):
    """The block primitives are the load-bearing piece of surgical update."""

    def test_replace_blocks_replaces_only_named_blocks(self):
        before = (
            "Header\n"
            "<!-- auto:meta -->\nold meta\n<!-- /auto:meta -->\n"
            "human paragraph\n"
            "<!-- auto:other -->\nother body\n<!-- /auto:other -->\n"
            "footer\n"
        )
        rendered = {"meta": "new meta body", "other": "new other body"}
        new_text, replaced = _replace_blocks(before, rendered)
        self.assertEqual(replaced, {"meta", "other"})
        # Human paragraph survives.
        self.assertIn("human paragraph", new_text)
        # New bodies present, old gone.
        self.assertIn("new meta body", new_text)
        self.assertIn("new other body", new_text)
        self.assertNotIn("old meta", new_text)
        # Header + footer survive.
        self.assertTrue(new_text.startswith("Header\n"))
        self.assertTrue(new_text.rstrip().endswith("footer"))

    def test_replace_blocks_skips_unknown_block_names(self):
        """Blocks the Merger doesn't render must pass through verbatim."""
        before = (
            "<!-- auto:owned -->\nowned body\n<!-- /auto:owned -->\n"
            "<!-- auto:third_party -->\nthird-party body\n<!-- /auto:third_party -->\n"
        )
        rendered = {"owned": "new owned"}
        new_text, replaced = _replace_blocks(before, rendered)
        self.assertEqual(replaced, {"owned"})
        self.assertIn("third-party body", new_text)
        self.assertIn("new owned", new_text)

    def test_wrap_round_trip(self):
        body = "line1\nline2"
        wrapped = _wrap("section_a", body)
        m = _BLOCK_RE_TMPL.search(wrapped)
        self.assertIsNotNone(m)
        self.assertEqual(m.group("name"), "section_a")
        self.assertIn("line1", m.group("body"))


class SurgicalMergerTests(unittest.TestCase):
    """End-to-end render + on-disk surgical update."""

    def setUp(self) -> None:
        self.store = FactStore()
        # Minimal fact set — enough to populate the property + tenant blocks.
        self.store.add(fact(
            fact_id="f1", entity_id="LIE-001", key="name",
            value="WEG Test", source_ref="https://x/raw/stammdaten/x.json",
        ))
        self.store.add(fact(
            fact_id="f2", entity_id="LIE-001", key="strasse",
            value="Teststr. 1", source_ref="https://x/raw/stammdaten/x.json",
        ))
        self.store.add(fact(
            fact_id="f3", entity_id=FLAGSHIP_TENANT, key="vorname",
            value="Julius", source_ref="https://x/raw/stammdaten/x.json",
        ))
        self.store.add(fact(
            fact_id="f4", entity_id=FLAGSHIP_TENANT, key="einheit_id",
            value="EH-025", source_ref="https://x/raw/stammdaten/x.json",
        ))
        # One payment row on the einheit.
        self.store.add(fact(
            fact_id="p1", entity_id="EH-025", key="payment.amount_eur",
            value=1676.0, source_ref="https://x/raw/bank/k.csv#TX-1",
            observed_at="2025-12-01", source_event_id="evp1",
        ))
        self.store.add(fact(
            fact_id="p2", entity_id="EH-025", key="payment.direction",
            value="credit", source_ref="https://x/raw/bank/k.csv#TX-1",
            observed_at="2025-12-01", source_event_id="evp1",
        ))

    def test_render_first_run_writes_full_scaffold(self):
        merger = SurgicalMerger(self.store)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "context.LIE-001.md"
            new_text, stats = merger.render_to_file(path)
        self.assertTrue(stats["wrote_fresh"])
        self.assertEqual(stats["blocks_replaced"], 0)
        # All declared blocks appear in the scaffold.
        for name in ("property_meta", "tenant_lease", "tenant_banking",
                     "payments_history", "communications", "maintenance",
                     "legal_disputes"):
            self.assertIn(f"<!-- auto:{name} -->", new_text)
            self.assertIn(f"<!-- /auto:{name} -->", new_text)
        # Property + tenant facts rendered with citations.
        self.assertIn("WEG Test", new_text)
        self.assertIn("Julius", new_text)
        # Scalar fields go through format_value → "[(source)](url)".
        self.assertIn("[(source)](https://x/raw/stammdaten/x.json)", new_text)
        # Payment table rendered with kind-tagged citation column.
        self.assertIn("Amount EUR", new_text)
        self.assertIn("1676.0", new_text)
        self.assertIn("[(bank)]", new_text)
        # Stats report at least the one payment row.
        self.assertEqual(stats["payment_rows"], 1)

    def test_human_edit_preserved_across_runs(self):
        """The headline demo property: anything outside auto-blocks survives."""
        merger = SurgicalMerger(self.store)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "context.LIE-001.md"
            merger.render_to_file(path)
            v1 = path.read_text(encoding="utf-8")

            # Plant a human edit in two places: the Notes section, and a stray
            # line above the auto-blocks (to prove arbitrary placement works).
            v1 = v1.replace(
                "## Human Notes\n",
                "## Human Notes\n\n- Mieter ist konfliktfreudig.\n",
            )
            v1 = "<!-- HUMAN-OWNED-MARKER -->\n" + v1
            path.write_text(v1, encoding="utf-8")

            # Re-run — auto-blocks updated, human bits preserved.
            merger2 = SurgicalMerger(self.store)
            new_text, stats = merger2.render_to_file(path)

        self.assertFalse(stats["wrote_fresh"])
        self.assertGreater(stats["blocks_replaced"], 0)
        self.assertIn("HUMAN-OWNED-MARKER", new_text)
        self.assertIn("Mieter ist konfliktfreudig", new_text)
        # Engine block content still present.
        self.assertIn("WEG Test", new_text)

    def test_unknown_existing_block_is_passed_through(self):
        """If the file carries an auto-block we don't render, we must not
        delete it — the user might have a downstream tool managing it."""
        merger = SurgicalMerger(self.store)
        seed = (
            "<!-- auto:property_meta -->\nstale\n<!-- /auto:property_meta -->\n"
            "<!-- auto:downstream_tool -->\nkeep me\n<!-- /auto:downstream_tool -->\n"
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "context.LIE-001.md"
            path.write_text(seed, encoding="utf-8")
            new_text, _ = merger.render_to_file(path)
        # Our block was rewritten ...
        self.assertNotIn("stale", new_text)
        self.assertIn("WEG Test", new_text)
        # ... but the downstream block is intact.
        self.assertIn("<!-- auto:downstream_tool -->", new_text)
        self.assertIn("keep me", new_text)

    def test_missing_block_is_appended_on_schema_growth(self):
        """If the schema adds a new block name, the file gets it appended
        rather than silently lost."""
        merger = SurgicalMerger(self.store)
        # Seed a file that only carries the property_meta block — older schema.
        seed = "<!-- auto:property_meta -->\nold\n<!-- /auto:property_meta -->\n"
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "context.LIE-001.md"
            path.write_text(seed, encoding="utf-8")
            new_text, stats = merger.render_to_file(path)
        self.assertEqual(stats["blocks_replaced"], 1)
        self.assertGreaterEqual(stats["blocks_appended"], 1)
        # A block introduced later in the schema must now exist in the file.
        self.assertIn("<!-- auto:tenant_lease -->", new_text)


if __name__ == "__main__":
    unittest.main()
