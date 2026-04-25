# Engine Aggregation Rules — Property ← Units

> How `context.property.md` aggregates state from all `context.unit.*.md` files.
> **Cost target:** ~80% deterministic (zero LLM), ~15% nightly-batched LLM (1 call per pattern-class per day), ~5% on-the-fly LLM for high-stakes triggers.
> **Spec for Zeng's engine.** Karl & Claude, 2026-04-25.

## Trigger Architecture

```
Source change (CSV / EML / PDF)
        ↓
[Per-Source Extractor] (LLM, only on new source files)
        ↓
[Fact Store] (versioned, with provenance)
        ↓
[Unit MD Builder] writes context.unit.<id>.md
        ↓
[Event Bus] emits structured event (deterministic from MD diff)
        ↓
[Property Aggregator]
   ├─ deterministic side-effects (immediate, in-process)
   └─ pattern-detection bucket (queued, drained nightly)
        ↓
context.property.md (auto-blocks only)
```

Two cadences:
- **On event:** deterministic side-effects fire immediately when a Unit-MD is written. Counter increments, sums, units-list updates. No LLM calls.
- **Nightly batch:** LLM-based pattern-detection runs once per day. Reads recent events, groups by pattern-class, decides if a `cross-unit-patterns` row should be added/updated.
- **On-demand LLM trigger:** when a deterministic counter crosses a threshold (e.g. `active_reductions.count` jumps from 2 to 3 with same root cause), an immediate LLM call fires to evaluate Insurance-Trigger / WEG-Beschluss-Trigger.

## Event-to-Side-Effect Map

| Unit-Event | Property-Side-Effect | Cost |
|---|---|---|
| ticket opened/closed (non-critical) | none | 0 |
| **critical ticket** (Wasserschaden, Heizung, Schimmel) | §8.5 pattern-detector check next batch (cross-unit cluster?) | 1 LLM (batched) |
| `dunning.current_stage` change | §5.1 `active_dunning.by_stage` increment/decrement; units list update | 0 (det.) |
| `lease.cancellation_status = cancelled` | §5.1 `active_mieterwechsel_in_flight`++; §4.3 add Mieterwechsel-Lauf | 0 (det.) |
| `lease.start_date` reached (new lease) | §2 Units-Index `occupancy = rented`; §5 financials projection update | 0 (det.) |
| `unit.occupancy_status = vacant` | §5.1 `units_status.vacant`++; §3.7 Vermietung activated in unit MD | 0 (det.) |
| `tenant_special_agreements` add | none (intern to unit) | 0 |
| `bauliche_veraenderung` approved + `scope=tragend` | §8.2 WEG-Agenda-Backlog add | 0 (rule-based) |
| `handover.next_scheduled` set within 30d | §5.1 `pending_handovers_next_30d` add | 0 (det.) |
| Vendor invoice received (any unit ticket) | §6.1 vendor `last_invoice` update; §5.1 `vendor_open_balance` recalc | 0 (det.) |
| Vendor dunning received | §4.2 `vendor-dunning` table add | 0 (det.) |
| `reductions` (Mietminderung) add | §5.1 `active_reductions`++; **if cluster of 3+ same-cause units → on-demand LLM Insurance-Trigger** | 0 + bedingt 1 LLM |
| `sticky-thread` classified as conflict | §8.5 `cross-unit-patterns` next batch | 1 LLM (batched) |
| Modernisierung completed (in unit) | §8.4 `modernization` add with `affected_units` link | 0 (det.) |

## Pattern Classes (LLM-detected)

The nightly aggregator groups recent events into pattern-class buckets and decides whether to materialize a row in §8.5:

| Class | Trigger threshold | Example |
|---|---|---|
| **Konflikt** | 2+ noise-complaint sticky-threads same unit-pair | WE 5 ↔ WE 6 chronic noise |
| **Wartung** | 3+ critical tickets same root-cause within property in 90d | 3 Wasserschäden in Säule HAUS-12-A → Rohrproblem |
| **Vendor-Quality** | Vendor X dispatched 4+ times to same unit, or 3+ Nachbesserungen | Sanitär XY repeatedly fixing same issue |
| **Owner-Behaviour** | Same owner files 2+ Einsprüche in 12 months | EIG-014 chronic dissenter — Beirat heads-up |
| **Insurance-Trigger** | 3+ tenants with Mietminderung citing same cause | Building-wide Mietminderung pattern → notify insurer |

**Confidence score** in §8.5 reflects: how strong is the cluster (incident count, time-window tightness, semantic similarity). Default threshold to surface: 0.7.

## Cost Estimation per Property per Day

For LIE-001 (35 units) at typical activity:
- **Deterministic counter updates:** ~50–200 events/day, $0.00 each
- **Nightly pattern-detection batch:** 5 LLM calls (one per pattern-class), Sonnet-tier ≈ $0.03 total
- **On-demand insurance/WEG triggers:** 0–2 calls/day, $0.01 each ≈ $0.02 max

→ **Total LLM cost ~$0.05/day per property**. At 1000 properties: $50/day, $1.5k/month for full aggregation. Vs. naive "re-run extractor on every event" approach which would be 10–100×.

## Read Cost (Property-Agent's perspective)

Aggregated counters in §5.1 mean a Property-Agent answering *"how is the property?"* reads ~20 lines (§5.1 + §5) instead of 35 unit MDs (35 × 200 = 7000 lines). **350× read reduction** vs. naive aggregation at read-time.

## Idempotency & Conflict Handling

- Each side-effect is **idempotent**: re-applying the same event yields the same state. Engine can replay events safely.
- If two events arrive for the same field in same window, last-write-wins with `last_aggregated_at` timestamp.
- LLM-detected patterns get a `confidence` and a `last_evaluated_at`. Patterns below confidence 0.7 stay in a backlog buffer, not in §8.5.
- Conflicting deterministic vs LLM verdicts emit `<!-- conflict -->` marker for human review.

## Open Questions for Zeng

1. **Event Bus implementation:** Postgres LISTEN/NOTIFY, Redis Streams, or simple file-watcher on `context.unit.*.md` git diffs?
2. **Pattern-detection model:** Haiku-tier sufficient or do we need Sonnet for semantic clustering?
3. **Threshold tuning:** start with the defaults above, calibrate after first week of real data.
