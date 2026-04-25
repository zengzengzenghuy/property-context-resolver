"""Unit tests for the surgical Merger primitives + new property/unit pipeline.

Run:
    python -m unittest tests.test_merger -v
"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from extractor.engine import FactStore
from extractor.merger import (
    PropertyMerger,
    UnitMerger,
    _BLOCK_RE,
    _replace_blocks,
    _wrap,
)
from extractor.models import Fact, PROPERTY_ID


def fact(*, fact_id: str, entity_id: str, key: str, value, source_ref: str,
         entity_type: str | None = None,
         observed_at: str | None = None, source_event_id: str = "ev1",
         confidence: float = 1.0) -> Fact:
    return Fact(
        id=fact_id,
        property_id=PROPERTY_ID,
        entity_type=entity_type,
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
        self.assertIn("human paragraph", new_text)
        self.assertIn("new meta body", new_text)
        self.assertIn("new other body", new_text)
        self.assertNotIn("old meta", new_text)
        self.assertTrue(new_text.startswith("Header\n"))
        self.assertTrue(new_text.rstrip().endswith("footer"))

    def test_replace_blocks_skips_unknown_block_names(self):
        before = (
            "<!-- auto:owned -->\nowned body\n<!-- /auto:owned -->\n"
            "<!-- auto:third_party -->\nthird-party body\n<!-- /auto:third_party -->\n"
        )
        rendered = {"owned": "new owned"}
        new_text, replaced = _replace_blocks(before, rendered)
        self.assertEqual(replaced, {"owned"})
        self.assertIn("third-party body", new_text)
        self.assertIn("new owned", new_text)

    def test_block_regex_supports_dotted_names(self):
        """`auto:tickets.critical` and `auto:property.display_name` must round-trip."""
        body = "<!-- auto:tickets.critical -->\nstuff\n<!-- /auto:tickets.critical -->"
        m = _BLOCK_RE.search(body)
        self.assertIsNotNone(m)
        self.assertEqual(m.group("name"), "tickets.critical")

    def test_wrap_round_trip_multiline(self):
        body = "line1\nline2"
        wrapped = _wrap("section_a", body)
        m = _BLOCK_RE.search(wrapped)
        self.assertIsNotNone(m)
        self.assertEqual(m.group("name"), "section_a")
        self.assertIn("line1", m.group("body"))

    def test_wrap_inline_for_short_body(self):
        """Short single-line bodies stay inline so they can sit inside a heading."""
        wrapped = _wrap("unit_id", "EH-019")
        self.assertEqual(wrapped, "<!-- auto:unit_id -->EH-019<!-- /auto:unit_id -->")


class PropertyMergerTests(unittest.TestCase):
    """End-to-end render against the schema templates."""

    def setUp(self) -> None:
        self.store = FactStore()
        # Minimal stammdaten facts for property + one unit + one tenant.
        for entity, key, value in [
            ("LIE-001", "name", "WEG Test"),
            ("LIE-001", "strasse", "Teststr. 1"),
            ("LIE-001", "plz", "12345"),
            ("LIE-001", "ort", "Berlin"),
            ("LIE-001", "verwalter", "Test GmbH"),
        ]:
            self.store.add(fact(
                fact_id=f"{entity}-{key}", entity_id=entity, entity_type="liegenschaft",
                key=key, value=value,
                source_ref="https://x/raw/stammdaten/x.json",
            ))
        self.store.add(fact(
            fact_id="u1", entity_id="EH-001", entity_type="einheit",
            key="einheit_nr", value="WE 01",
            source_ref="https://x/raw/stammdaten/x.json",
        ))
        self.store.add(fact(
            fact_id="t1", entity_id="MIE-001", entity_type="mieter",
            key="vorname", value="Julius",
            source_ref="https://x/raw/stammdaten/x.json",
        ))

    def _seed_templates(self, root: Path) -> None:
        # Copy real templates so the merger has something to scaffold from.
        repo_root = Path(__file__).parent.parent
        for name in ("context.property.template.md", "context.unit.template.md"):
            src = repo_root / name
            (root / name).write_text(src.read_text(encoding="utf-8"), encoding="utf-8")

    def test_property_render_first_run_scaffolds_from_template(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._seed_templates(root)
            merger = PropertyMerger.for_property(self.store, "LIE-001", root)
            new_text, stats = merger.render_to_file()
        # Render produced the expected file with property data.
        self.assertIn("WEG Test", new_text)
        self.assertIn("Teststr. 1", new_text)
        # Auto-blocks named in the schema are present.
        for name in ("meta", "property", "owners", "mandate", "units-index",
                     "operations-summary", "provenance"):
            self.assertIn(f"<!-- auto:{name} -->", new_text)
            self.assertIn(f"<!-- /auto:{name} -->", new_text)
        self.assertGreater(stats["blocks_replaced"], 0)

    def test_human_edits_preserved_across_runs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._seed_templates(root)
            out = root / "context.property.LIE-001.md"

            PropertyMerger.for_property(self.store, "LIE-001", root).render_to_file()
            v1 = out.read_text(encoding="utf-8")

            v1 = "<!-- HUMAN-OWNED-MARKER -->\n" + v1 + "\n## Human Notes\n- Note A\n"
            out.write_text(v1, encoding="utf-8")

            new_text, _ = PropertyMerger.for_property(self.store, "LIE-001", root).render_to_file()

        self.assertIn("HUMAN-OWNED-MARKER", new_text)
        self.assertIn("Note A", new_text)
        # Engine block still rewritten.
        self.assertIn("WEG Test", new_text)

    def test_unknown_existing_block_passes_through(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self._seed_templates(root)
            out = root / "context.property.LIE-001.md"
            out.write_text(
                "<!-- auto:property -->\nstale\n<!-- /auto:property -->\n"
                "<!-- auto:downstream_tool -->\nkeep me\n<!-- /auto:downstream_tool -->\n",
                encoding="utf-8",
            )
            new_text, _ = PropertyMerger.for_property(self.store, "LIE-001", root).render_to_file()
        self.assertNotIn("stale", new_text)
        # `property` block was re-rendered with the address from facts.
        self.assertIn("Teststr. 1", new_text)
        self.assertIn("<!-- auto:downstream_tool -->", new_text)
        self.assertIn("keep me", new_text)


class UnitMergerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.store = FactStore()
        self.store.add(fact(
            fact_id="u1", entity_id="EH-019", entity_type="einheit",
            key="einheit_nr", value="WE 19",
            source_ref="https://x/raw/stammdaten/x.json",
        ))
        self.store.add(fact(
            fact_id="u2", entity_id="EH-019", entity_type="einheit",
            key="haus_id", value="HAUS-14",
            source_ref="https://x/raw/stammdaten/x.json",
        ))
        self.store.add(fact(
            fact_id="t1", entity_id="MIE-025", entity_type="mieter",
            key="einheit_id", value="EH-019",
            source_ref="https://x/raw/stammdaten/x.json",
        ))
        self.store.add(fact(
            fact_id="t2", entity_id="MIE-025", entity_type="mieter",
            key="vorname", value="Jasmin",
            source_ref="https://x/raw/stammdaten/x.json",
        ))

    def test_unit_render_includes_unit_id_in_title(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "context.unit.template.md").write_text(
                (Path(__file__).parent.parent / "context.unit.template.md").read_text(encoding="utf-8"),
                encoding="utf-8",
            )
            new_text, _ = UnitMerger.for_unit(self.store, "EH-019", root).render_to_file()
        self.assertIn("<!-- auto:unit_id -->EH-019<!-- /auto:unit_id -->", new_text)
        self.assertIn("WE 19", new_text)
        # Tenant on this unit is rendered in the tenants table.
        self.assertIn("MIE-025", new_text)


if __name__ == "__main__":
    unittest.main()
