"""End-to-end pipeline driver.

    python run.py raw/ [--out out] [--include-incremental]

Wires the engine in the order Sprint.md prescribes:
    SourceLoader -> NoiseFilter -> FactExtractor (identity) -> FactStore -> Merger
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from datetime import date
from pathlib import Path

from extractor.engine import (
    DunningReconciler,
    FactExtractor,
    FactStore,
    NoiseFilter,
    SourceLoader,
)
from extractor.identity import IdentityResolver
from extractor.merger import FLAGSHIP_TENANT, SurgicalMerger
from extractor.models import JsonlWriter
from extractor.sb import SupabaseSink
from extractor.source_ref import configure as configure_source_ref


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="run", description="property-context-resolver pipeline")
    p.add_argument("raw", help="path to raw/ directory")
    p.add_argument("--out", default="out", help="output dir for events.jsonl + facts.jsonl + context.md")
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

    # 1. Load
    loader = SourceLoader(raw_root, include_incremental=args.include_incremental)

    # 2. Identity resolver (built from stammdaten)
    resolver = IdentityResolver(raw_root)

    # 3. Noise filter
    noise = NoiseFilter()

    # 4. Fact extractor with identity enrichment
    extractor = FactExtractor(resolver=resolver)

    # 5. Fact store
    store = FactStore()
    facts_path = out_dir / "facts.jsonl"

    # On an incremental run, rehydrate from the previous run's audit log so the
    # second pass can detect conflicts against history (and the JSONL stays
    # append-only across runs). Dedup is by fact.id, so this is a no-op on
    # facts the engine re-emits identically.
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

    # 5b. Dunning reconciler — derive `dunning.*` roll-up facts on the flagship
    # tenant entity (and project Mahnung facts onto the tenant). These power
    # the legal_disputes block in the merger and the LLM Q&A in Hour 4-5.
    today = args.today or date.today().isoformat()
    bank_csv_ref = ""
    for f in store.all_facts():
        if "/raw/bank/" in (f.source_ref or ""):
            bank_csv_ref = f.source_ref.split("#", 1)[0]
            break
    dunning = DunningReconciler(
        store=store,
        resolver=resolver,
        today=today,
        bank_csv_ref=bank_csv_ref,
    )
    dunning_emitted = dunning.reconcile(FLAGSHIP_TENANT)

    n_facts = store.write_jsonl(facts_path)

    # 6. Merger — surgical render. Replaces only the inside of `<!-- auto:NAME -->`
    # blocks; ## Human Notes and any other human-owned content survives.
    merger = SurgicalMerger(store)
    context_md = out_dir / "context.LIE-001.md"
    new_text, merger_stats = merger.render_to_file(context_md)

    # Conflict tally. Two flavors:
    #   raw_conflicts — every (entity, key) bucket with ≥2 distinct values above
    #     the floor. Inflated by time-series keys (payment.*, communication.*)
    #     where every observation is correctly a different value.
    #   merge_conflicts — restricted to identity/contract scalar keys; these are
    #     the ones the Merger surfaces with <!-- conflict --> markers.
    # Scalar identity/contract keys (bare, no namespace) — these are the ones
    # the Merger surfaces in context.md. Namespaced keys like `payment.iban`
    # or `communication.from` are per-event/per-transaction and aggregated
    # elsewhere, so we don't conflict-flag them.
    SCALAR_KEYS = {
        "email", "telefon", "iban", "bic", "strasse", "plz", "ort",
        "kaltmiete", "nk_vorauszahlung", "kaution", "mietbeginn", "mietende",
        "anrede", "vorname", "nachname", "firma",
    }
    raw_conflicts = 0
    merge_conflicts = 0
    for (eid, key), _ in store._buckets.items():
        if store.is_conflicted(eid, key):
            raw_conflicts += 1
            if key in SCALAR_KEYS:
                merge_conflicts += 1

    # 7. Mirror to Supabase. No-op when SUPABASE_URL/SERVICE_KEY are unset, so
    # this stays a soft dependency — the engine still produces local files in
    # CI / on a fresh clone.
    sb = SupabaseSink.from_env()
    diff_summary = (
        f"facts={n_facts}, conflicts(scalar)={merge_conflicts}, "
        f"payments={merger_stats['payment_rows']}, "
        f"communications={merger_stats['communication_rows']}, "
        f"mahnungen={merger_stats.get('mahnung_rows', 0)}, "
        f"dunning={dunning_emitted}, "
        f"blocks_replaced={merger_stats['blocks_replaced']}, "
        f"wrote_fresh={merger_stats['wrote_fresh']}"
    )
    name = (store.latest("LIE-001", "name").value if store.latest("LIE-001", "name") else None)
    address = None
    s = store.latest("LIE-001", "strasse")
    z = store.latest("LIE-001", "plz")
    o = store.latest("LIE-001", "ort")
    if s and o:
        address = f"{s.value}, {z.value if z else ''} {o.value}".strip()
    if sb.enabled:
        sb.upsert_context("LIE-001", new_text, name=name, address=address)
        sb.log_update("LIE-001", source_filename=str(context_md.name), diff_summary=diff_summary)

    print(f"events:          {sum(by_source.values()):>5}  -> {events_path}")
    print(f"facts:           {n_facts:>5}  -> {facts_path}  (loaded {prior} prior)")
    print(f"conflicts (raw): {raw_conflicts:>5}  (incl. time-series)")
    print(f"conflicts (merge):{merge_conflicts:>4}  (scalar identity/contract keys)")
    print(f"context.md:      {context_md}  ({diff_summary})")
    print(f"supabase:        {'wrote' if sb.enabled else 'skipped (no SUPABASE_URL/SERVICE_KEY)'}")
    print("\nevents by source:")
    for s, n in by_source.most_common():
        print(f"  {s:<12} {n:>6}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
