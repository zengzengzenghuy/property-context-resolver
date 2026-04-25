"""Unit tests for FactStore + format_value.

Run:
    python -m unittest tests.test_factstore -v
"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from extractor.engine import (
    CONFIDENCE_FLOOR,
    FactStore,
    SOURCE_PRIORITY,
    _normalize_value,
    _source_from_ref,
    format_value,
)
from extractor.models import Fact, PROPERTY_ID


def make_fact(
    *,
    fact_id: str,
    entity_id: str | None = "MIE-022",
    entity_type: str | None = "mieter",
    key: str = "telefon",
    value=None,
    source_ref: str = "https://github.com/o/r/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-022",
    confidence: float = 1.0,
    observed_at: str | None = "2024-04-20",
    extracted_at: str = "2026-04-25T10:00:00+00:00",
) -> Fact:
    return Fact(
        id=fact_id,
        property_id=PROPERTY_ID,
        entity_type=entity_type,
        entity_id=entity_id,
        key=key,
        value=value,
        source_event_id="evt-" + fact_id,
        source_ref=source_ref,
        confidence=confidence,
        observed_at=observed_at,
        extracted_at=extracted_at,
    )


class TestNormalizeValue(unittest.TestCase):
    def test_strings_are_lowercased_and_stripped(self):
        self.assertEqual(_normalize_value("  Hello "), _normalize_value("hello"))

    def test_floats_round_to_two_dp(self):
        self.assertEqual(_normalize_value(249.9), _normalize_value(249.90))
        self.assertNotEqual(_normalize_value(249.9), _normalize_value(250.0))

    def test_lists_are_order_invariant(self):
        self.assertEqual(_normalize_value(["EH-001", "EH-002"]),
                         _normalize_value(["EH-002", "EH-001"]))


class TestSourceFromRef(unittest.TestCase):
    def test_recognized_kinds(self):
        cases = {
            "https://github.com/o/r/blob/main/raw/stammdaten/x.json": "stammdaten",
            "https://github.com/o/r/blob/main/raw/bank/x.csv": "bank",
            "https://github.com/o/r/blob/main/raw/emails/2024-01/x.eml": "email",
            "https://github.com/o/r/blob/main/raw/rechnungen/2024-01/x.pdf": "invoice",
            "https://github.com/o/r/blob/main/raw/briefe/2024-04/x.pdf": "letter",
        }
        for ref, expected in cases.items():
            self.assertEqual(_source_from_ref(ref), expected, ref)

    def test_unknown_returns_empty(self):
        self.assertEqual(_source_from_ref("/some/random/path"), "")


class TestFactStoreDedup(unittest.TestCase):
    def test_same_id_dropped(self):
        s = FactStore()
        f1 = make_fact(fact_id="a", value="0123456789")
        f2 = make_fact(fact_id="a", value="0123456789")
        self.assertTrue(s.add(f1))
        self.assertFalse(s.add(f2))
        self.assertEqual(s.count(), 1)

    def test_same_value_no_progress_drops(self):
        """Two facts with the same value, same observed_at, same confidence:
        the second is redundant — drop it."""
        s = FactStore()
        f1 = make_fact(fact_id="a", value="0123456789", observed_at="2024-04-20", confidence=0.9)
        f2 = make_fact(fact_id="b", value="0123456789", observed_at="2024-04-20", confidence=0.9)
        s.add(f1)
        self.assertFalse(s.add(f2))
        self.assertEqual(s.count(), 1)

    def test_same_value_newer_observed_appends(self):
        """`We saw this again` — append a new audit row."""
        s = FactStore()
        s.add(make_fact(fact_id="a", value="0123456789", observed_at="2024-04-20"))
        self.assertTrue(s.add(make_fact(fact_id="b", value="0123456789", observed_at="2025-01-01")))
        self.assertEqual(s.count(), 2)

    def test_different_value_always_appends(self):
        s = FactStore()
        s.add(make_fact(fact_id="a", value="0123456789"))
        s.add(make_fact(fact_id="b", value="0987654321"))
        self.assertEqual(s.count(), 2)

    def test_unresolved_facts_persist_but_skip_index(self):
        s = FactStore()
        s.add(make_fact(fact_id="a", entity_id=None, entity_type=None,
                        key="communication.intent", value="anfrage"))
        self.assertEqual(s.count(), 1)
        self.assertIsNone(s.latest("MIE-022", "communication.intent"))
        # And it should still serialize.
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "facts.jsonl"
            self.assertEqual(s.write_jsonl(p), 1)


class TestFactStoreConflicts(unittest.TestCase):
    STAMM_REF = "https://github.com/o/r/blob/main/raw/stammdaten/stammdaten.json"
    EMAIL_REF = "https://github.com/o/r/blob/main/raw/emails/2024-04/x.eml"
    BANK_REF = "https://github.com/o/r/blob/main/raw/bank/x.csv"

    def test_two_distinct_values_above_floor_conflict(self):
        s = FactStore()
        s.add(make_fact(fact_id="a", value="0111", source_ref=self.STAMM_REF, confidence=1.0))
        s.add(make_fact(fact_id="b", value="0222", source_ref=self.EMAIL_REF, confidence=0.85))
        self.assertTrue(s.is_conflicted("MIE-022", "telefon"))
        sides = s.conflicts("MIE-022", "telefon")
        self.assertEqual(len(sides), 2)
        # Sorted strongest-first → stammdaten should lead.
        self.assertEqual(sides[0].value, "0111")

    def test_low_confidence_side_does_not_conflict(self):
        """An email with conf 0.6 should not flag a conflict against stammdaten."""
        s = FactStore()
        s.add(make_fact(fact_id="a", value="0111", source_ref=self.STAMM_REF, confidence=1.0))
        s.add(make_fact(fact_id="b", value="0222", source_ref=self.EMAIL_REF, confidence=0.6))
        self.assertFalse(s.is_conflicted("MIE-022", "telefon"))
        latest = s.latest("MIE-022", "telefon")
        self.assertEqual(latest.value, "0111")

    def test_same_value_two_sources_is_not_conflict(self):
        """Reinforcement, not disagreement."""
        s = FactStore()
        s.add(make_fact(fact_id="a", value="0111", source_ref=self.STAMM_REF, confidence=1.0))
        s.add(make_fact(fact_id="b", value="0111", source_ref=self.EMAIL_REF, confidence=0.9))
        self.assertFalse(s.is_conflicted("MIE-022", "telefon"))


class TestFactStoreLatestTieBreak(unittest.TestCase):
    def test_higher_confidence_wins(self):
        s = FactStore()
        s.add(make_fact(fact_id="a", value="0111", confidence=0.85, observed_at="2025-01-01"))
        s.add(make_fact(fact_id="b", value="0222", confidence=1.0, observed_at="2024-01-01"))
        self.assertEqual(s.latest("MIE-022", "telefon").value, "0222")

    def test_observed_at_breaks_confidence_tie(self):
        s = FactStore()
        s.add(make_fact(fact_id="a", value="0111", confidence=1.0, observed_at="2024-01-01"))
        s.add(make_fact(fact_id="b", value="0222", confidence=1.0, observed_at="2025-01-01"))
        self.assertEqual(s.latest("MIE-022", "telefon").value, "0222")

    def test_source_priority_breaks_remaining_ties(self):
        s = FactStore()
        # Same confidence, same observed_at — stammdaten priority > email.
        stamm = "https://github.com/o/r/blob/main/raw/stammdaten/x.json"
        email = "https://github.com/o/r/blob/main/raw/emails/2024-04/x.eml"
        s.add(make_fact(fact_id="a", value="0111", confidence=1.0, observed_at="2024-01-01",
                        source_ref=email))
        s.add(make_fact(fact_id="b", value="0222", confidence=1.0, observed_at="2024-01-01",
                        source_ref=stamm))
        self.assertEqual(s.latest("MIE-022", "telefon").value, "0222")


class TestFormatValue(unittest.TestCase):
    def test_resolved_renders_inline_citation(self):
        s = FactStore()
        s.add(make_fact(fact_id="a", value="0111",
                        source_ref="https://github.com/o/r/blob/main/raw/stammdaten/x.json"))
        out = format_value(s, "MIE-022", "telefon")
        self.assertIn("0111", out)
        self.assertIn("[(source)](https://github.com/o/r/blob/main/raw/stammdaten/x.json)", out)
        self.assertNotIn("conflict", out)

    def test_conflict_renders_block(self):
        s = FactStore()
        stamm = "https://github.com/o/r/blob/main/raw/stammdaten/x.json"
        email = "https://github.com/o/r/blob/main/raw/emails/2024-04/x.eml"
        s.add(make_fact(fact_id="a", value="0111", source_ref=stamm, confidence=1.0))
        s.add(make_fact(fact_id="b", value="0222", source_ref=email, confidence=0.85))
        out = format_value(s, "MIE-022", "telefon")
        self.assertTrue(out.startswith("<!-- conflict -->"))
        self.assertTrue(out.endswith("<!-- /conflict -->"))
        self.assertIn("0111", out)
        self.assertIn("0222", out)
        self.assertIn("(stammdaten,", out)
        self.assertIn("(email,", out)

    def test_missing_returns_none(self):
        s = FactStore()
        self.assertIsNone(format_value(s, "MIE-022", "telefon"))


class TestJsonlRoundTrip(unittest.TestCase):
    def test_load_dedupes_by_fact_id(self):
        """Re-loading the same JSONL must be a no-op."""
        s1 = FactStore()
        s1.add(make_fact(fact_id="a", value="0111"))
        s1.add(make_fact(fact_id="b", value="0222"))
        s1.add(make_fact(fact_id="c", entity_id=None, entity_type=None,
                         key="communication.intent", value="anfrage"))

        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "facts.jsonl"
            self.assertEqual(s1.write_jsonl(p), 3)

            s2 = FactStore()
            self.assertEqual(s2.load_jsonl(p), 3)
            # Reloading is a no-op.
            self.assertEqual(s2.load_jsonl(p), 0)
            self.assertEqual(s2.count(), 3)

    def test_loaded_store_resolves_latest(self):
        s1 = FactStore()
        s1.add(make_fact(fact_id="a", value="0111", confidence=1.0))
        s1.add(make_fact(fact_id="b", value="0222", confidence=0.85))
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "facts.jsonl"
            s1.write_jsonl(p)
            s2 = FactStore()
            s2.load_jsonl(p)
            self.assertEqual(s2.latest("MIE-022", "telefon").value, "0111")
            self.assertTrue(s2.is_conflicted("MIE-022", "telefon"))


class TestSanityChecks(unittest.TestCase):
    def test_confidence_floor_is_set(self):
        self.assertGreater(CONFIDENCE_FLOOR, 0.0)
        self.assertLess(CONFIDENCE_FLOOR, 1.0)

    def test_source_priority_has_known_kinds(self):
        for k in ("stammdaten", "letter", "invoice", "bank", "email"):
            self.assertIn(k, SOURCE_PRIORITY)


if __name__ == "__main__":
    unittest.main()
