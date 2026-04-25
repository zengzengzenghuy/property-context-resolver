"""CLI: `python -m extractor.cli ingest <raw_dir> [--out out/]`."""

from __future__ import annotations

import argparse
import sys
from collections import Counter
from pathlib import Path

from .extract import extract_all
from .models import JsonlWriter
from .source_ref import configure as configure_source_ref


def cmd_ingest(args: argparse.Namespace) -> int:
    if args.source_ref_base:
        configure_source_ref(args.source_ref_base)
    root = Path(args.raw).resolve()
    out_dir = Path(args.out).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    include_incr = bool(args.include_incremental)

    events_path = out_dir / "events.jsonl"
    facts_path = out_dir / "facts.jsonl"

    by_source: Counter[str] = Counter()
    fact_keys: Counter[str] = Counter()

    with JsonlWriter(str(events_path)) as ew, JsonlWriter(str(facts_path)) as fw:
        for source_name, event, facts in extract_all(root, include_incremental=include_incr):
            ew.write(event)
            for f in facts:
                fw.write(f)
                fact_keys[f.key] += 1
            by_source[source_name] += 1

    print(f"events: {ew.count}  -> {events_path}")
    print(f"facts:  {fw.count}  -> {facts_path}")
    print("\nevents by source:")
    for src, n in by_source.most_common():
        print(f"  {src:<12} {n:>6}")
    print("\ntop fact keys:")
    for k, n in fact_keys.most_common(15):
        print(f"  {k:<35} {n:>6}")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="extractor")
    sub = p.add_subparsers(dest="cmd", required=True)

    ing = sub.add_parser("ingest", help="run all source connectors over a raw/ tree")
    ing.add_argument("raw", help="path to raw/ directory")
    ing.add_argument("--out", default="out", help="output dir for events.jsonl + facts.jsonl")
    ing.add_argument(
        "--include-incremental",
        action="store_true",
        help="Include raw/incremental/* delta drops. Off by default per Sprint.md "
             "(incremental is the surgical-update fixture for the second run).",
    )
    ing.add_argument(
        "--source-ref-base",
        default=None,
        help="GitHub blob base for source_ref citations "
             "(e.g. https://github.com/owner/repo/blob/main). "
             "Defaults to autodetect from git remote/branch, or $SOURCE_REF_BASE.",
    )
    ing.set_defaults(fn=cmd_ingest)

    args = p.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
