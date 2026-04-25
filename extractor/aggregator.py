"""PropertyAggregator — implements `engine.aggregation-rules.md`.

Takes the FactStore after all extractors + DunningReconciler have run, walks
every unit + every active lease, and emits property-scoped facts capturing
the §5.1 operations summary:

- units_status (rented / vacant / own-use / total)
- active_dunning (count, by_stage, units list)
- active_reductions (count, units)
- pending_handovers_next_30d
- active_mieterwechsel_in_flight
- critical_tickets_total
- vendor_open_balance_against_us_total

Each derived value is emitted as a Fact on `LIE-001` with key
`operations.<field>` so the merger picks it up via `format_value`. The
aggregator is a single deterministic pass — equivalent to "replay every
unit-event from scratch" — and is idempotent: running it twice on the same
store yields the same facts.

§8.5 cross-unit-patterns (LLM pattern detection) is NOT implemented here —
the spec calls for a nightly batch that we'll wire in a follow-up. The block
in the merger renders empty + a stub line referencing this file.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime, timedelta
from typing import Any, Iterable, Optional

from .engine import FactStore
from .models import Fact, PROPERTY_ID, stable_id


HANDOVER_WINDOW_DAYS = 30


@dataclass
class PropertyAggregator:
    store: FactStore
    today: str  # YYYY-MM-DD
    property_id: str = PROPERTY_ID

    def aggregate(self) -> int:
        """Walk facts and emit `operations.*` summary facts. Returns count."""
        emitted = 0
        unit_ids = self._entity_ids("einheit")
        eig_ids = self._entity_ids("eigentuemer")
        mie_ids = self._entity_ids("mieter")

        # 1. units_status
        rented, vacant, own_use = 0, 0, 0
        selbstnutzer_units: set[str] = set()
        for eig in eig_ids:
            if self._latest_value(eig, "selbstnutzer"):
                units = self._latest_value(eig, "einheit_ids", []) or []
                if isinstance(units, list):
                    selbstnutzer_units.update(units)
        rented_set: set[str] = set()
        for mie in mie_ids:
            unit = self._latest_value(mie, "einheit_id")
            ende = self._latest_value(mie, "mietende")
            if unit and not ende:
                rented_set.add(unit)
        for eid in unit_ids:
            if eid in rented_set:
                rented += 1
            elif eid in selbstnutzer_units:
                own_use += 1
            else:
                vacant += 1

        emitted += self._emit("operations.units_rented", rented)
        emitted += self._emit("operations.units_vacant", vacant)
        emitted += self._emit("operations.units_own_use", own_use)
        emitted += self._emit("operations.units_total", len(unit_ids))

        # 2. active_dunning — per-tenant dunning roll-up facts
        dunning_units: list[str] = []
        by_stage = {1: 0, 2: 0, 3: 0}
        dunning_count = 0
        for mie in mie_ids:
            stufe = self._latest_value(mie, "dunning.mahnstufe")
            offen = self._latest_value(mie, "dunning.offener_betrag_eur")
            if not stufe or not offen:
                continue
            try:
                stufe_i = int(stufe)
                offen_f = float(offen)
            except (TypeError, ValueError):
                continue
            if stufe_i < 1 or offen_f <= 0:
                continue
            dunning_count += 1
            by_stage[min(stufe_i, 3)] = by_stage.get(min(stufe_i, 3), 0) + 1
            unit = self._latest_value(mie, "einheit_id")
            if unit and unit not in dunning_units:
                dunning_units.append(unit)
        emitted += self._emit("operations.active_dunning_count", dunning_count)
        emitted += self._emit("operations.active_dunning_stage_1", by_stage.get(1, 0))
        emitted += self._emit("operations.active_dunning_stage_2", by_stage.get(2, 0))
        emitted += self._emit("operations.active_dunning_stage_3", by_stage.get(3, 0))
        emitted += self._emit("operations.active_dunning_units", sorted(dunning_units))

        # 3. active_reductions — units with any reductions.* facts
        reduction_units = self._units_with_prefix("reductions.")
        emitted += self._emit("operations.active_reductions_count", len(reduction_units))
        emitted += self._emit("operations.active_reductions_units", sorted(reduction_units))

        # 4. pending_handovers_next_30d — units with handover.next_scheduled_date
        # in the [today, today+30d] window.
        today_d = self._parse_date(self.today)
        handover_units: list[str] = []
        if today_d is not None:
            cutoff = today_d + timedelta(days=HANDOVER_WINDOW_DAYS)
            for eid in unit_ids:
                d = self._latest_value(eid, "handover.next_scheduled_date")
                pd = self._parse_date(d) if d else None
                if pd is None:
                    continue
                if today_d <= pd <= cutoff:
                    handover_units.append(eid)
        emitted += self._emit("operations.pending_handovers_30d", len(handover_units))

        # 5. active_mieterwechsel_in_flight
        mw_units: list[str] = []
        for eid in unit_ids:
            cancel = self._latest_value(eid, "lease.cancellation_status")
            if cancel and cancel != "none":
                mw_units.append(eid)
        # Also: tenants with cancellation status set
        for mie in mie_ids:
            cancel = self._latest_value(mie, "lease.cancellation_status")
            if cancel and cancel != "none":
                unit = self._latest_value(mie, "einheit_id")
                if unit and unit not in mw_units:
                    mw_units.append(unit)
        emitted += self._emit("operations.active_mieterwechsel_count", len(mw_units))
        emitted += self._emit("operations.active_mieterwechsel_units", sorted(mw_units))

        # 6. critical_tickets_total
        crit = 0
        for eid in unit_ids:
            for g in self._group_by_event(eid, "ticket."):
                sev = g.get("ticket.severity")
                if sev and sev.value == "critical":
                    crit += 1
        emitted += self._emit("operations.critical_tickets_total", crit)

        # 7. vendor_open_balance — sum of vendor_dunning.amount_eur across all DLs
        open_eur = 0.0
        for dl in self._entity_ids("dienstleister"):
            for g in self._group_by_event(dl, "vendor_dunning."):
                amt = g.get("vendor_dunning.amount_eur")
                if amt is None or amt.value is None:
                    continue
                try:
                    open_eur += float(amt.value)
                except (TypeError, ValueError):
                    pass
        emitted += self._emit("operations.vendor_open_balance_eur", round(open_eur, 2))

        return emitted

    # --- helpers ---

    def _emit(self, key: str, value: Any) -> int:
        fact = Fact.make(
            property_id=self.property_id,
            entity_type="liegenschaft",
            entity_id=self.property_id,
            key=key,
            value=value,
            source_event_id=stable_id("aggregator", self.property_id, key, self.today),
            source_ref=f"engine://aggregator/{self.today}",
            observed_at=self.today,
            confidence=1.0,
        )
        return 1 if self.store.add(fact) else 0

    def _entity_ids(self, etype: str) -> list[str]:
        seen: set[str] = set()
        for fact in self.store.all_facts():
            if fact.entity_type == etype and fact.entity_id:
                seen.add(fact.entity_id)
        return sorted(seen)

    def _latest_value(self, eid: str, key: str, default: Any = None) -> Any:
        f = self.store.latest(eid, key)
        return f.value if f else default

    def _units_with_prefix(self, prefix: str) -> list[str]:
        out: set[str] = set()
        for eid in self._entity_ids("einheit"):
            for fact in self.store.all_facts():
                if fact.entity_id == eid and fact.key.startswith(prefix):
                    out.add(eid)
                    break
        return sorted(out)

    def _group_by_event(self, eid: str, prefix: str) -> list[dict[str, Fact]]:
        by_event: dict[str, dict[str, Fact]] = {}
        for fact in self.store.all_facts():
            if fact.entity_id != eid or not fact.key.startswith(prefix):
                continue
            by_event.setdefault(fact.source_event_id, {})[fact.key] = fact
        return list(by_event.values())

    @staticmethod
    def _parse_date(s: Optional[str]) -> Optional[date]:
        if not s:
            return None
        try:
            return datetime.fromisoformat(s.split("T", 1)[0]).date()
        except ValueError:
            return None


__all__ = ["PropertyAggregator"]
