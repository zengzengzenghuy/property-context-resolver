"""Build and upload the raw-corpus bundle that `answer_question_raw` reads.

Concatenates the canonical sources (stammdaten JSON, bank CSV, every Mahnung
+ invoice .pdf.txt, and recent emails) into a single text bundle, caps it
near a token budget so it fits comfortably inside Claude Sonnet 4.6's 200k
window, and uploads to Supabase Storage at:

    raw-uploads/<PROPERTY_ID>/raw_bundle.txt

Run after `python run.py raw/` and before the benchmark harness:

    python scripts/upload_raw_bundle.py raw/ --property-id LIE-001

Requires SUPABASE_URL + SUPABASE_SERVICE_KEY (or SERVICE_ROLE_KEY) in the env
or .env file. Without them the script writes the bundle locally to
`out/raw_bundle.txt` and skips the upload (useful for inspection).
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

try:
    from supabase import create_client
except ImportError:
    create_client = None  # type: ignore[assignment]


# ~3.5 chars/token (German-leaning) → 600k chars ≈ 170k tokens — leaves
# headroom under the 200k context for the question + system + response.
DEFAULT_CHAR_BUDGET = 600_000

BUCKET = "raw-uploads"


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except Exception as exc:
        return f"<read-error: {exc}>"


def _section(title: str, body: str) -> str:
    return f"\n\n===== {title} =====\n\n{body.rstrip()}\n"


def collect_sources(raw: Path) -> list[tuple[str, Path, str]]:
    """Return (label, path, body) tuples in priority order. Earlier items get
    in first when we hit the budget — Stammdaten + bank rows are non-negotiable
    for any property-management Q&A; emails are the fattest tail and go last."""
    items: list[tuple[str, Path, str]] = []

    stamm_json = raw / "stammdaten" / "stammdaten.json"
    if stamm_json.exists():
        items.append(("stammdaten/stammdaten.json", stamm_json, _read_text(stamm_json)))

    bank_dir = raw / "bank"
    if bank_dir.exists():
        for csv in sorted(bank_dir.glob("kontoauszug*.csv")):
            items.append((f"bank/{csv.name}", csv, _read_text(csv)))

    # Letters: Mahnungen first, then everything else (ETV-Einladungen etc.).
    briefe_dir = raw / "briefe"
    if briefe_dir.exists():
        letters = sorted(briefe_dir.rglob("*.pdf.txt"))
        mahnungen = [p for p in letters if "mahnung" in p.name.lower()]
        rest = [p for p in letters if p not in mahnungen]
        for p in mahnungen + rest:
            rel = p.relative_to(raw)
            items.append((f"briefe/{rel.parent.name}/{p.name}", p, _read_text(p)))

    rechn_dir = raw / "rechnungen"
    if rechn_dir.exists():
        for p in sorted(rechn_dir.rglob("*.pdf.txt")):
            rel = p.relative_to(raw)
            items.append((f"rechnungen/{rel.parent.name}/{p.name}", p, _read_text(p)))

    # Emails: newest first, capped by budget below. Mailbox is 6500+ emails so
    # we lean on the budget enforcer to truncate gracefully.
    emails_dir = raw / "emails"
    if emails_dir.exists():
        eml_paths = sorted(emails_dir.rglob("*.eml"), reverse=True)
        for p in eml_paths:
            rel = p.relative_to(raw)
            items.append((f"emails/{rel.parent.name}/{p.name}", p, _read_text(p)))

    return items


def build_bundle(items: list[tuple[str, Path, str]],
                 char_budget: int) -> tuple[str, dict]:
    """Concatenate sections in priority order until char_budget is hit.
    Returns (bundle_text, stats)."""
    chunks: list[str] = []
    used = 0
    counts: dict[str, int] = {}
    truncated_at: str | None = None

    for label, _path, body in items:
        section = _section(label, body)
        if used + len(section) > char_budget:
            truncated_at = label
            chunks.append(_section(
                "TRUNCATED",
                f"raw bundle hit the {char_budget:,} char budget before "
                f"reaching {label} — earlier sources fit, later ones omitted.",
            ))
            break
        chunks.append(section)
        used += len(section)
        kind = label.split("/", 1)[0]
        counts[kind] = counts.get(kind, 0) + 1

    text = "".join(chunks)
    stats = {
        "chars": len(text),
        "approx_tokens": len(text) // 4,
        "sections": counts,
        "truncated_at": truncated_at,
    }
    return text, stats


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="upload_raw_bundle",
                                description="Build + upload raw_bundle.txt")
    p.add_argument("raw", help="path to raw/ directory")
    p.add_argument("--property-id", default="LIE-001",
                   help="property_id used as the Storage path prefix")
    p.add_argument("--char-budget", type=int, default=DEFAULT_CHAR_BUDGET,
                   help="char ceiling for the bundle (default 600k ≈ 170k tokens)")
    p.add_argument("--out", default="out/raw_bundle.txt",
                   help="local path for the bundle (always written; uploaded if env is set)")
    args = p.parse_args(argv)

    raw_root = Path(args.raw).resolve()
    if not raw_root.is_dir():
        print(f"raw root does not exist: {raw_root}", file=sys.stderr)
        return 2

    items = collect_sources(raw_root)
    text, stats = build_bundle(items, args.char_budget)

    out_path = Path(args.out).resolve()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")
    print(f"bundle:        {out_path}")
    print(f"chars:         {stats['chars']:>10,}  (~{stats['approx_tokens']:,} tokens)")
    print(f"sections:      {stats['sections']}")
    if stats["truncated_at"]:
        print(f"truncated at:  {stats['truncated_at']}")

    url = os.environ.get("SUPABASE_URL")
    key = (os.environ.get("SUPABASE_SERVICE_KEY")
           or os.environ.get("SUPABASE_SERVICE_ROLE_KEY"))
    if not url or not key or create_client is None:
        print("supabase:      skipped (no SUPABASE_URL / SERVICE_KEY)")
        return 0

    sb = create_client(url, key)
    storage_path = f"{args.property_id}/raw_bundle.txt"
    try:
        sb.storage.create_bucket(BUCKET, options={"public": False})
    except Exception:
        pass  # already exists
    sb.storage.from_(BUCKET).upload(
        path=storage_path,
        file=text.encode("utf-8"),
        file_options={"content-type": "text/plain", "upsert": "true"},
    )
    print(f"supabase:      uploaded -> {BUCKET}/{storage_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
