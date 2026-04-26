# property-context-resolver

Turn the chaos of property-management artifacts — emails, scanned letters,
vendor invoices, bank statements, master-data CSVs — into one auditable
`context.md` per property and per unit, with surgical updates that preserve
human edits across runs.

The demo property is `LIE-001` (WEG Immanuelkirchstraße 26, Berlin) with one
flagship tenant in dunning (`MIE-001`).

## What it does

The pipeline ingests a `raw/` directory, resolves identities across sources,
deduplicates and conflict-detects facts, reconciles a tenant's payment ledger
against its lease, and renders a per-property + per-unit Markdown dossier in
the `spine-v2-split` schema. Every fact carries a citation back to its source
file (a GitHub blob URL by default, autodetected from `git remote`), so each
line in `context.md` is auditable to the byte.

A second pass — the LLM **Summarizer** — consumes deterministically pre-
filtered "signal" payloads (anomalies, conflicts, items with deadlines) and
emits 3-sentence German summaries inside dedicated `<!-- auto:*.summary -->`
blocks. Summaries follow the **Signal-First Property Management Philosophy**:
every non-empty summary contains exactly four elements (issue, lease clause,
legal obligation, timeline) and is prefixed with a triage tag
(`[Emergency]` / `[Routine]` / `[Administrative]`).

## Architecture

```
raw/                            extractor/                            out/
─────                           ──────────                            ─────
stammdaten/  ─┐                                                       events.jsonl
emails/      ─┤   SourceLoader → NoiseFilter → FactExtractor          facts.jsonl
briefe/      ─┼─►        │             │             │           ┌──► llm_cache/
rechnungen/  ─┤          ▼             ▼             ▼           │    summary.json
bank/        ─┘   (Event, [Fact])  (filter rules) (identity-     │
                                                    enrich)      │
                                       │                         │
                                       ▼                         │
                                   FactStore                     │
                                   (append-only,                 │
                                    JSONL audit log,             │  context.property.LIE-001.md
                                    conflict detection)          │  context.unit.EH-XXX.md
                                       │                         │     ▲
                                       ▼                         │     │
                              DunningReconciler ─► ┐             │     │
                              PropertyAggregator ─►├─► dunning.* │     │
                                                   │   operations.*    │
                                       │           │   facts           │
                                       ▼                                │
                                PropertyMerger / UnitMerger ────────────┘
                                     │       (block registry: blocks.py)
                                     ▼
                                Summarizer ◄── ANTHROPIC_API_KEY
                                (Signal-First, cached, or GEMINI_API_KEY)
                                     │
                                     ▼

                                  Supabase (optional mirror, no-op without keys)
```

### Components

| # | Module                              | Role                                                                          |
|---|-------------------------------------|-------------------------------------------------------------------------------|
| 1 | `extractor/sources/*`               | One connector per source kind (stammdaten / emails / briefe / rechnungen / bank). Yields `(Event, [Fact])`. |
| 2 | `extractor/identity.py`             | `IdentityResolver` — exact match on email/IBAN/einheit_nr/phone, then fuzzy name (`difflib`, threshold 0.86). |
| 3 | `extractor/engine.py::NoiseFilter`  | Drops auto-acks and other non-signal events. Stub for now; expand with quoted-reply / signature stripping. |
| 4 | `extractor/engine.py::FactExtractor`| Identity-enriches each fact. Hooks for LLM-based enrichment (currently empty). |
| 5 | `extractor/engine.py::FactStore`    | Bucketed `(entity_id, key)` index, append-only dedup, conflict detection at confidence floor 0.7, tie-break on confidence > observed_at > source priority > extracted_at. JSONL round-trip. |
| 6 | `extractor/engine.py::DunningReconciler` | Per-tenant payment-ledger reconciliation against `kaltmiete + nk_vorauszahlung`. Emits `dunning.*` facts (mahnstufe, months_overdue, offener_betrag, verzugszinsen) anchored on § 286 / § 288 BGB. |
| 7 | `extractor/aggregator.py`           | `PropertyAggregator` — emits `operations.*` facts on `LIE-001` from unit-scoped state (rented/vacant/own-use counts, active dunning, pending handovers). See `engine.aggregation-rules.md` §5.1. |
| 8 | `extractor/merger.py` + `blocks.py` | `PropertyMerger` / `UnitMerger` — surgical update of `<!-- auto:NAME -->` blocks. Each block is a `(store, ctx) -> str` render fn registered in `PROPERTY_BLOCKS` / `UNIT_BLOCKS`. Anything outside auto-blocks is preserved across runs. |
| 9 | `extractor/summarizer.py`           | Anthropic-backed LLM summary for `<!-- auto:*.summary -->` blocks. Signal-First philosophy in the system prompt; pre-filtered signal payloads built deterministically in `blocks.py`. File-cached at `out/llm_cache/summary.json`. No-ops gracefully without `ANTHROPIC_API_KEY`. |
| 10| `extractor/sb.py`                   | `SupabaseSink` — mirrors rendered Markdown into Supabase under `spine-v2-split`. No-op when keys are unset. |

### Key design choices

- **JSONL audit log instead of Postgres.** The fact store is append-only;
  re-observation appends a new row. `latest()` and `conflicts()` work on the
  in-memory index built from the log. Reproducible without a DB.
- **GitHub blob URLs as `source_ref`.** Autodetected from `git remote` +
  current branch; fall back to absolute local path outside a git repo so
  the pipeline never breaks. Override via `--source-ref-base` or
  `SOURCE_REF_BASE`.
- **Surgical Markdown updates.** The merger only writes inside
  `<!-- auto:NAME -->` ... `<!-- /auto:NAME -->` blocks. Free-form prose,
  human notes, and `## Human Notes` sections are preserved across runs.
- **PDFs go through a pre-OCR cache.** `scripts/preocr.py` writes
  `<file>.pdf.txt` siblings; the engine reads those first and falls back to
  live `pdfminer.six` only when needed. The cache is checked into git so
  the engine is reproducible without `pdfminer.six` installed.
- **LLM does prose, not filtering.** The Summarizer never sees raw data —
  salience extractors in `blocks.py` (e.g. `_dunning_signal()`) pre-filter
  by confidence floor, key allowlist, recency, and anomaly status. The LLM
  produces ≤3 German sentences with the four Trifecta elements (issue /
  contract / law / timeline) and preserved `[(label)](url)` citations.
- **Single-property scope.** `PROPERTY_ID = "LIE-001"` is hard-coded in
  `extractor/models.py`. No multi-tenancy, no auth, no vector DB.

## Tavily Integration Plan

To treat Tavily as a "Legal & Temporal Oracle" and ensure the assistant's advice doesn't rely on stale laws or hardcoded financial constants, the integration is planned as follows:

### 1. The Tavily "Sentinel" Client
A lightweight `extractor/tavily.py` wrapper will handle search queries with a focus on recent results (using Tavily's `search_depth="advanced"` and `days=365`) to catch the latest legal changes.

### 2. Dynamic Interest Rate Validation (Dunning)
The current `DunningReconciler` uses a hardcoded `ECB_BASE_PP = 3.5`.
*   **Integration**: During the `reconcile()` phase, if the date is "today", a Tavily search is triggered: `"Aktueller Basiszinssatz der EZB"`.
*   **Result**: The live rate overrides the hardcoded 3.5%, ensuring the calculated `verzugszinsen_eur` is legally accurate.

### 3. Legal Fact-Checking in Summaries
The `Summarizer` assumes its knowledge of German law is current.
*   **Integration**: In `Summarizer.summarize()`, after the LLM generates a summary, it is scanned for legal citations (e.g., `§ 288 BGB`).
*   **Result**: A background Tavily search checks for recent amendments. If found, a `[Tavily Legal Alert]` is appended to the summary.

### 4. Context Obsolescence Guard
A "Staleness Check" will be added to the `FactStore` or `Aggregator`.
*   **Integration**: For time-sensitive local facts (like "Mietspiegel Berlin 2024"), Tavily checks if a newer version exists.
*   **Result**: If a newer version exists, a high-priority fact `operations.context_outdated` is emitted to flag the property dashboard.

## Build

Requires Python 3.11+. Optional system dep: `tesseract` (only if you want
OCR fallback for scanned PDFs — not needed for the bundled corpus thanks
to the pre-OCR cache).

```bash
# 1. Install Python deps
pip install -r requirements.txt

# 2. Provide secrets in .env (all entries optional — modules degrade gracefully)
cat > .env <<'EOF'
ANTHROPIC_API_KEY=sk-ant-api03-...      # enables LLM summary blocks
SUPABASE_URL=https://...supabase.co     # enables Supabase mirror
SUPABASE_SERVICE_KEY=eyJhbGc...
EOF

# 3. (Re)build the PDF text cache — only needed if you change the PDF set
python scripts/preocr.py raw/
```

`pdfminer.six` is the only required runtime dep; everything else (`pytesseract`,
`pdf2image`, `pypdf`, `supabase`, `python-dotenv`, `anthropic`) is optional —
modules that depend on them no-op gracefully when imports fail or env vars are
missing.

## Run

End-to-end pipeline:

```bash
# Default v1 run — archive only, no incremental delta drops
python run.py raw/

# Pin a reference date so legal deadlines (§ 288 BGB Verzugszinsen, etc.)
# are computed deterministically — also passed into the LLM summary prompt
python run.py raw/ --today 2026-04-25

# Second run with delta drops to demo surgical updates
# (Loads existing out/facts.jsonl first so prior history feeds conflict detection)
python run.py raw/ --include-incremental --today 2026-04-25
```

Outputs:

```
out/
  events.jsonl                  one row per source event
  facts.jsonl                   the full append-only fact log
  llm_cache/summary.json        deterministic cache of LLM summary outputs
  raw_bundle.txt                concatenation of raw text for inspection
context.property.LIE-001.md     property-level dossier
context.unit.EH-XXX.md          per-unit dossier (one per Einheit)
```

The first run scaffolds the Markdown files from
`context.property.template.md` / `context.unit.template.md`. Subsequent runs
update only the auto-block bodies — anything outside those blocks (incl. a
`## Human Notes` section you maintain by hand) is preserved.

### Adding a new auto-block after the first run

The merger only **scaffolds** new blocks into a fresh file. If you register a
new block in `PROPERTY_BLOCKS` / `UNIT_BLOCKS` after files have already been
rendered, delete the affected files so they re-scaffold from the template:

```bash
rm context.unit.*.md context.property.*.md
python run.py raw/ --today 2026-04-25
```

### Tests

```bash
python -m unittest tests.test_factstore -v       # one module, verbose
python -m unittest discover tests                # everything
```

Stdlib `unittest`, no extra runner. The test file uses a `make_fact()` helper
at the top — copy that pattern when adding new cases.

## Configuration

| Variable                      | Used by                | Effect when unset                            |
|-------------------------------|------------------------|----------------------------------------------|
| `ANTHROPIC_API_KEY`           | `extractor/summarizer.py` | enables Claude summaries; if missing, falls back to `GEMINI_API_KEY`. |
| `GEMINI_API_KEY`              | `extractor/summarizer.py` | enables Gemini summaries; used if `ANTHROPIC_API_KEY` is missing. |
| `SUPABASE_URL` + `SUPABASE_SERVICE_KEY` | `extractor/sb.py` | Supabase mirror is skipped; local Markdown still written. |
| `SOURCE_REF_BASE`             | `extractor/source_ref.py` | Autodetect from `git remote` + current branch; fall back to local absolute path. |

CLI flags on `run.py`:

| Flag                       | Default     | Purpose                                                        |
|----------------------------|-------------|----------------------------------------------------------------|
| `raw`                      | (required)  | Path to the `raw/` corpus.                                     |
| `--out`                    | `out`       | Output dir for `events.jsonl` / `facts.jsonl` / `llm_cache/`.  |
| `--repo-root`              | `cwd`       | Where `context.{property,unit}.*.md` are written.              |
| `--include-incremental`    | off         | Walk `raw/incremental/` (the second-run fixture).              |
| `--source-ref-base`        | (autodetect)| Override the GitHub blob base for citations.                   |
| `--today`                  | system date | Reference date for dunning interest + LLM legal deadlines.     |

## Repo layout

```
raw/                           immutable input corpus
extractor/                     the engine
  models.py                    Event + Fact dataclasses, JsonlWriter
  identity.py                  IdentityResolver
  source_ref.py                local Path → GitHub blob URL
  engine.py                    SourceLoader / NoiseFilter / FactExtractor
                               / FactStore / DunningReconciler / format_value
  aggregator.py                PropertyAggregator (engine.aggregation-rules.md §5.1)
  merger.py                    PropertyMerger + UnitMerger (surgical updates)
  blocks.py                    block render registry (PROPERTY_BLOCKS / UNIT_BLOCKS)
  summarizer.py                Anthropic LLM wrapper, file-cached
  sb.py                        Supabase mirror
  sources/                     one connector per source kind
  cli.py                       `python -m extractor.cli ingest`
context.property.template.md   per-property Markdown skeleton
context.unit.template.md       per-unit Markdown skeleton
scripts/preocr.py              pre-OCR cache builder
run.py                         end-to-end driver
tests/test_factstore.py        stdlib unittest — FactStore + format_value
```

## Further reading

- **`CLAUDE.md`** — operational notes, conventions, and gotchas (the *how*).
- **`Tech Stack.md`** — what's deliberately not built and why (no DB, no
  vectors, no auth).
- **`Sprint.md`** — the build plan and ownership split.
- **`engine.aggregation-rules.md`** — `PropertyAggregator` §5.1 spec.
