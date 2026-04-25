"""End-to-end pipeline driver.

    python run.py raw/ [--out out] [--include-incremental]

Wires the engine in the order Sprint.md prescribes:
    SourceLoader -> NoiseFilter -> FactExtractor (identity) -> FactStore
                 -> DunningReconciler (per active lease)
                 -> PropertyAggregator (engine.aggregation-rules.md §5.1)
                 -> PropertyMerger + UnitMerger (per spine-v2-split schema)
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from datetime import date
from pathlib import Path

from extractor.aggregator import PropertyAggregator
from extractor.engine import (
    DunningReconciler,
    FactExtractor,
    FactStore,
    NoiseFilter,
    SourceLoader,
)
from extractor.identity import IdentityResolver
from extractor.merger import PropertyMerger, UnitMerger
from extractor.models import JsonlWriter, PROPERTY_ID
from extractor.sb import SupabaseSink
from extractor.source_ref import configure as configure_source_ref


FLAGSHIP_UNIT_FOR_INDEX = "EH-019"  # marked in §2 units-index `unit_md_ref` col


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="run", description="property-context-resolver pipeline")
    p.add_argument("raw", help="path to raw/ directory")
    p.add_argument("--out", default="out", help="output dir for events.jsonl + facts.jsonl")
    p.add_argument("--repo-root", default=None,
                   help="root for context.property/unit.*.md output (defaults to cwd)")
    p.add_argument("--include-incremental", action="store_true",
                   help="Include raw/incremental/* (off by default per Sprint.md)")
    p.add_argument("--source-ref-base", default=None,
                   help="GitHub blob base for citations (autodetects from git remote/branch)")
    p.add_argument("--today", default=None,
                   help="Reference date for the dunning calc (YYYY-MM-DD); defaults to system today")
    args = p.parse_args(argv)

    if args.source_ref_base:
        configure_source_ref(args.source_ref_base)

    raw_root = Path(args.raw).resolve()
    out_dir = Path(args.out).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    repo_root = Path(args.repo_root).resolve() if args.repo_root else Path.cwd().resolve()

    # 1. Identity resolver (built from stammdaten — needed by emails extractor).
    resolver = IdentityResolver(raw_root)

    # 2. Load
    loader = SourceLoader(
        raw_root,
        include_incremental=args.include_incremental,
        resolver=resolver,
    )

    # 3. Noise filter
    noise = NoiseFilter()

    # 4. Fact extractor with identity enrichment
    extractor = FactExtractor(resolver=resolver)

    # 5. Fact store
    store = FactStore()
    facts_path = out_dir / "facts.jsonl"

    # On an incremental run, rehydrate from the previous run's audit log so the
    # second pass can detect conflicts against history.
    prior = 0
    if args.include_incremental and facts_path.exists():
        prior = store.load_jsonl(facts_path)

    # Drive the pipeline
    by_source: Counter[str] = Counter()
    events_path = out_dir / "events.jsonl"

    with JsonlWriter(str(events_path)) as ew:
        for src, event, facts in noise.filter(loader.load()):
            ew.write(event)
            store.add_many(extractor.enrich(event, facts))
            by_source[src] += 1

    # 5b. DunningReconciler — derive `dunning.*` roll-up facts on every active
    # tenant. An "active" lease is one with a `mietbeginn` and no `mietende`.
    today = args.today or date.today().isoformat()
    bank_csv_ref = ""
    for f in store.all_facts():
        if "/raw/bank/" in (f.source_ref or ""):
            bank_csv_ref = f.source_ref.split("#", 1)[0]
            break

    active_tenants: list[str] = []
    seen_tenants: set[str] = set()
    for fact in store.all_facts():
        if fact.entity_type != "mieter" or not fact.entity_id:
            continue
        if fact.entity_id in seen_tenants:
            continue
        seen_tenants.add(fact.entity_id)
        beg = store.latest(fact.entity_id, "mietbeginn")
        end = store.latest(fact.entity_id, "mietende")
        if beg and (end is None or end.value in (None, "")):
            active_tenants.append(fact.entity_id)

    dunning = DunningReconciler(
        store=store,
        resolver=resolver,
        today=today,
        bank_csv_ref=bank_csv_ref,
    )
    dunning_emitted = 0
    for tid in active_tenants:
        dunning_emitted += dunning.reconcile(tid)

    # 5c. PropertyAggregator — implements engine.aggregation-rules.md §5.1.
    # Emits `operations.*` facts on LIE-001 from the unit-scoped state.
    aggregator = PropertyAggregator(store=store, today=today, property_id=PROPERTY_ID)
    aggregator_emitted = aggregator.aggregate()

    n_facts = store.write_jsonl(facts_path)

    # 6. Merger — surgical render to per-property + per-unit files.
    property_merger = PropertyMerger.for_property(
        store=store,
        property_id=PROPERTY_ID,
        repo_root=repo_root,
        flagship_unit=FLAGSHIP_UNIT_FOR_INDEX,
    )
    property_text, property_stats = property_merger.render_to_file()

    unit_ids = sorted({
        f.entity_id for f in store.all_facts()
        if f.entity_type == "einheit" and f.entity_id
    })
    unit_stats = {"rendered": 0, "fresh": 0, "blocks_replaced": 0}
    for uid in unit_ids:
        unit_merger = UnitMerger.for_unit(store=store, unit_id=uid, repo_root=repo_root)
        _text, stats = unit_merger.render_to_file()
        unit_stats["rendered"] += 1
        unit_stats["fresh"] += 1 if stats["wrote_fresh"] else 0
        unit_stats["blocks_replaced"] += stats["blocks_replaced"]

    # Conflict tally — single combined count over the whole store.
    raw_conflicts = sum(
        1 for (eid, key), _ in store._buckets.items()
        if store.is_conflicted(eid, key)
    )

    # 7. Mirror to Supabase (no-op when SUPABASE_URL/SERVICE_KEY are unset).
    sb = SupabaseSink.from_env()
    diff_summary = (
        f"facts={n_facts}, conflicts={raw_conflicts}, "
        f"dunning_facts={dunning_emitted}, "
        f"aggregator_facts={aggregator_emitted}, "
        f"units_rendered={unit_stats['rendered']}, "
        f"property_blocks={property_stats['blocks_replaced']}"
    )
    name = (store.latest(PROPERTY_ID, "name").value if store.latest(PROPERTY_ID, "name") else None)
    address = None
    s = store.latest(PROPERTY_ID, "strasse")
    z = store.latest(PROPERTY_ID, "plz")
    o = store.latest(PROPERTY_ID, "ort")
    if s and o:
        address = f"{s.value}, {z.value if z else ''} {o.value}".strip()
    if sb.enabled:
        sb.upsert_context(PROPERTY_ID, property_text, name=name, address=address)
        sb.log_update(PROPERTY_ID, source_filename=f"context.property.{PROPERTY_ID}.md",
                      diff_summary=diff_summary)

    print(f"events:           {sum(by_source.values()):>5}  -> {events_path}")
    print(f"facts:            {n_facts:>5}  -> {facts_path}  (loaded {prior} prior)")
    print(f"conflicts:        {raw_conflicts:>5}")
    print(f"dunning facts:    {dunning_emitted:>5}  ({len(active_tenants)} active leases)")
    print(f"aggregator facts: {aggregator_emitted:>5}")
    print(f"property file:    {repo_root / f'context.property.{PROPERTY_ID}.md'}")
    print(f"unit files:       {unit_stats['rendered']:>5} rendered "
          f"({unit_stats['fresh']} fresh, {unit_stats['blocks_replaced']} block replacements)")
    print(f"supabase:         {'wrote' if sb.enabled else 'skipped (no SUPABASE_URL/SERVICE_KEY)'}")
    print("\nevents by source:")
    for src, n in by_source.most_common():
        print(f"  {src:<12} {n:>6}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
