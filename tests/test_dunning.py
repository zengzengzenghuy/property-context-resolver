"""Unit tests for DunningReconciler.

Run:
    python -m unittest tests.test_dunning -v
"""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from extractor.engine import DunningReconciler, FactStore
from extractor.identity import IdentityResolver
from extractor.models import Fact, PROPERTY_ID


# A minimal stammdaten.json that gives the resolver enough to map the Mahnung
# recipient name "Carsten Austermühle" → MIE-002. The test tenant MIE-001 is
# Julius Nette, EH-025 — same shape as the real corpus.
_STAMM = {
    "liegenschaft": {
        "id": "LIE-001", "name": "WEG Test", "strasse": "Teststr. 1",
        "plz": "10405", "ort": "Berlin",
    },
    "einheiten": [
        {"id": "EH-025", "einheit_nr": "WE 25", "lage": "1.OG"},
        {"id": "EH-009", "einheit_nr": "WE 9", "lage": "EG"},
    ],
    "eigentuemer": [],
    "mieter": [
        {"id": "MIE-001", "vorname": "Julius", "nachname": "Nette",
         "email": "julius@example.com", "iban": "DE00000000000000001"},
        {"id": "MIE-002", "vorname": "Carsten", "nachname": "Austermühle",
         "email": "carsten@example.com", "iban": "DE00000000000000002"},
    ],
    "dienstleister": [],
}


def _resolver_with(stamm: dict) -> IdentityResolver:
    """Build an IdentityResolver from an in-memory stammdaten dict."""
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "stammdaten").mkdir()
        import json
        (root / "stammdaten" / "stammdaten.json").write_text(
            json.dumps(stamm), encoding="utf-8",
        )
        return IdentityResolver(root)


def fact(*, fact_id: str, entity_type: str | None, entity_id: str, key: str,
         value, source_ref: str = "https://x/raw/bank/k.csv#TX-1",
         source_event_id: str = "ev1",
         observed_at: str | None = None, confidence: float = 1.0) -> Fact:
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


def seed_lease(store: FactStore, tenant_id: str = "MIE-001",
               einheit_id: str = "EH-025",
               kaltmiete: float = 1403.0, nk: float = 273.0,
               mietbeginn: str = "2024-01-01") -> None:
    """Lease parameters that the reconciler reads as the 'expected' side."""
    src = "https://x/raw/stammdaten/x.json"
    store.add(fact(fact_id=f"{tenant_id}-kalt", entity_type="mieter",
                   entity_id=tenant_id, key="kaltmiete", value=kaltmiete,
                   source_ref=src))
    store.add(fact(fact_id=f"{tenant_id}-nk", entity_type="mieter",
                   entity_id=tenant_id, key="nk_vorauszahlung", value=nk,
                   source_ref=src))
    store.add(fact(fact_id=f"{tenant_id}-beg", entity_type="mieter",
                   entity_id=tenant_id, key="mietbeginn", value=mietbeginn,
                   source_ref=src))
    store.add(fact(fact_id=f"{tenant_id}-unit", entity_type="mieter",
                   entity_id=tenant_id, key="einheit_id", value=einheit_id,
                   source_ref=src))


def seed_payment(store: FactStore, einheit_id: str, period: str,
                 amount: float, observed_at: str, ev_id: str) -> None:
    """One bank-row's worth of facts: amount + period + kind + direction.
    Group-by source_event_id is how the reconciler correlates them."""
    ref = f"https://x/raw/bank/k.csv#{ev_id}"
    for k, v in (("payment.amount_eur", amount),
                 ("payment.miete_period", period),
                 ("payment.kind", "miete"),
                 ("payment.direction", "credit")):
        store.add(fact(
            fact_id=f"{ev_id}-{k}",
            entity_type="einheit", entity_id=einheit_id,
            key=k, value=v, source_ref=ref, source_event_id=ev_id,
            observed_at=observed_at,
        ))


def seed_mahnung(store: FactStore, letter_id: str, recipient_name: str,
                 stufe: int, offen: float, date_iso: str) -> None:
    """A Mahnung letter's worth of facts on the letter entity. The
    DunningReconciler resolves recipient_name → tenant_id and projects."""
    ref = f"https://x/raw/briefe/{letter_id}.pdf"
    for k, v in (
        ("letter.kind", "mahnung"),
        ("letter.recipient_name", recipient_name),
        ("letter.date", date_iso),
        ("mahnung.stufe", stufe),
        ("mahnung.offener_betrag_eur", offen),
        ("mahnung.date", date_iso),
    ):
        store.add(fact(
            fact_id=f"{letter_id}-{k}",
            entity_type="letter", entity_id=letter_id,
            key=k, value=v, source_ref=ref,
            source_event_id=f"ev-{letter_id}",
            observed_at=date_iso,
        ))


class DunningReconcilerTests(unittest.TestCase):

    def setUp(self) -> None:
        self.resolver = _resolver_with(_STAMM)

    # --- on-time tenant -----------------------------------------------------

    def test_on_time_tenant_emits_zero_overdue(self):
        store = FactStore()
        seed_lease(store)
        # 12 months 2024-01 .. 2024-12, all paid in full.
        for i, month in enumerate(range(1, 13)):
            seed_payment(
                store, "EH-025", f"{month:02d}/2024",
                amount=1676.0,
                observed_at=f"2024-{month:02d}-02",
                ev_id=f"e{i}",
            )

        # today inside 2025-01's grace period (due 2025-01-01 + 14d = 2025-01-15)
        # so 2025-01 isn't counted as overdue yet — the only window we've scoped
        # is 2024-01..2024-12, all paid.
        rec = DunningReconciler(
            store=store, resolver=self.resolver, today="2025-01-10",
            bank_csv_ref="https://x/raw/bank/k.csv",
        )
        n = rec.reconcile("MIE-001")
        self.assertGreater(n, 0)

        self.assertEqual(store.latest("MIE-001", "dunning.mahnstufe").value, 0)
        self.assertEqual(store.latest("MIE-001", "dunning.months_overdue_count").value, 0)
        self.assertEqual(store.latest("MIE-001", "dunning.offener_betrag_eur").value, 0.0)
        self.assertEqual(store.latest("MIE-001", "dunning.verzugszinsen_eur").value, 0.0)
        self.assertEqual(store.latest("MIE-001", "dunning.expected_eur").value, 1676.0)
        self.assertEqual(store.latest("MIE-001", "dunning.last_payment_date").value, "2024-12-02")
        # Summary sentence in German is what the LLM cites.
        summary = store.latest("MIE-001", "dunning.summary_text").value
        self.assertIn("MIE-001", summary)
        self.assertIn("nicht im Verzug", summary)
        self.assertIn("Mahnstufe 0", summary)

    # --- overdue tenant, no Mahnung yet -------------------------------------

    def test_overdue_with_no_mahnung_assigns_stufe_one(self):
        """Sprint.md framework: 14d overdue with no Mahnung = stufe 1."""
        store = FactStore()
        seed_lease(store)  # mietbeginn 2024-01-01
        # 2024-01 paid, 2024-02 missed, 2024-03 paid.
        seed_payment(store, "EH-025", "01/2024", 1676.0, "2024-01-02", "e1")
        seed_payment(store, "EH-025", "03/2024", 1676.0, "2024-03-02", "e2")

        rec = DunningReconciler(
            store=store, resolver=self.resolver, today="2024-04-01",
            bank_csv_ref="https://x/raw/bank/k.csv",
        )
        rec.reconcile("MIE-001")

        self.assertEqual(store.latest("MIE-001", "dunning.mahnstufe").value, 1)
        # 02/2024 missed → 1 month overdue.
        self.assertEqual(store.latest("MIE-001", "dunning.months_overdue_count").value, 1)
        self.assertAlmostEqual(
            store.latest("MIE-001", "dunning.offener_betrag_eur").value,
            1676.0, places=2,
        )
        # Verzugszinsen > 0 (some days past grace).
        self.assertGreater(
            store.latest("MIE-001", "dunning.verzugszinsen_eur").value, 0.0,
        )

    # --- Mahnung links via recipient name -----------------------------------

    def test_mahnung_recipient_name_resolves_and_projects(self):
        store = FactStore()
        seed_lease(store, tenant_id="MIE-002", einheit_id="EH-009")
        # No payments → 03/2024 missed.
        # Add a Mahnung for "Carsten Austermühle" — exact stammdaten name.
        seed_mahnung(
            store, "LTR-0035", recipient_name="Carsten Austermühle",
            stufe=2, offen=1676.0, date_iso="2024-04-20",
        )

        rec = DunningReconciler(
            store=store, resolver=self.resolver, today="2024-04-25",
            bank_csv_ref="https://x/raw/bank/k.csv",
        )
        rec.reconcile("MIE-002")

        # Tenant-side projection landed: mahnung.* now exists under MIE-002.
        proj = store.latest("MIE-002", "mahnung.stufe")
        self.assertIsNotNone(proj)
        self.assertEqual(proj.value, 2)
        # The roll-up takes the max stufe from linked Mahnungen.
        self.assertEqual(store.latest("MIE-002", "dunning.mahnstufe").value, 2)
        # Citation chain preserved — source_ref still points to the letter PDF.
        self.assertIn("/raw/briefe/", proj.source_ref)

    def test_unrelated_mahnung_does_not_leak(self):
        """A Mahnung for tenant A must not affect tenant B's roll-up."""
        store = FactStore()
        seed_lease(store, tenant_id="MIE-001", einheit_id="EH-025")
        seed_payment(store, "EH-025", "01/2024", 1676.0, "2024-01-02", "e1")
        # Mahnung for Carsten (MIE-002), not Julius (MIE-001).
        seed_mahnung(
            store, "LTR-0035", recipient_name="Carsten Austermühle",
            stufe=3, offen=2000.0, date_iso="2024-04-20",
        )

        # today inside 2024-01's grace+1 window: 2024-01 paid, 2024-02 not yet
        # past grace. Net = on-time.
        rec = DunningReconciler(
            store=store, resolver=self.resolver, today="2024-01-30",
            bank_csv_ref="https://x/raw/bank/k.csv",
        )
        rec.reconcile("MIE-001")

        # Carsten's Mahnung must NOT have projected onto MIE-001.
        self.assertIsNone(store.latest("MIE-001", "mahnung.stufe"))
        self.assertEqual(store.latest("MIE-001", "dunning.mahnstufe").value, 0)


if __name__ == "__main__":
    unittest.main()
