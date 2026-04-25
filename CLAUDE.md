# CLAUDE.md

Operational notes for working on **property-context-resolver**. The why-and-what
lives in `Tech Stack.md`, `Technical Component.md`, and `Sprint.md` — read those
first if you don't have context. This file captures the how — repo layout,
commands, conventions, gotchas — and the current state of each component.

## What this is

A pipeline that turns scattered property-management artifacts (emails, scanned
letters, vendor invoices, bank statements, master-data CSVs) into a single
`context.md` per property, stored in git. The engine surgically updates lines
inside `<!-- auto:section -->` blocks and never touches anything outside them,
so human edits are preserved across runs. Single demo property = `LIE-001`
(WEG Immanuelkirchstraße 26, Berlin).

The demo flow: run engine → produces `context.md` v1 → human edits something →
drop in a new email/invoice → re-run → diff shows human edit preserved + new
facts merged + sources cited.

## Run it

```bash
# install deps (pdfminer.six is the only required one; rest are optional)
pip install -r requirements.txt

# pre-OCR pass — caches <pdf>.pdf.txt next to every PDF in raw/
python scripts/preocr.py raw/

# end-to-end pipeline (v1: archive only)
python run.py raw/

# second run with incremental delta drops (the surgical-update fixture)
# Loads existing out/facts.jsonl first so prior history feeds conflict detection.
python run.py raw/ --include-incremental

# unit tests
python -m unittest tests.test_factstore -v
```

Outputs land in `out/`: `events.jsonl`, `facts.jsonl`, `context.LIE-001.md`.

## Repo layout

```
raw/                         immutable input corpus
  stammdaten/                JSON (canonical) + per-table CSVs
  emails/YYYY-MM/*.eml       ~6.5k emails
  briefe/YYYY-MM/*.pdf       letters (Mahnung, ETV-Einladung)
  rechnungen/YYYY-MM/*.pdf   vendor invoices
  bank/kontoauszug_*.csv     semicolon-delimited Sparkasse export
  incremental/day-XX/        delta drops — EXCLUDED from default run

extractor/                   the engine
  models.py                  Event + Fact dataclasses, JsonlWriter
  identity.py                IdentityResolver — name/email/IBAN/phone/einheit_nr → canonical_id
  source_ref.py              local Path → GitHub blob URL (autodetects from git remote)
  extract.py                 fan-out across source connectors
  engine.py                  typed pipeline classes (Sprint.md skeleton)
  cli.py                     `python -m extractor.cli ingest` (alt entrypoint)
  sources/
    stammdaten.py            JSON/CSV master data → baseline facts
    bank.py                  CSV rows → payment events
    emails.py                .eml + subject-pattern classifier
    pdfs.py                  invoices + letters; reads .pdf.txt cache first

scripts/preocr.py            one-shot PDF text cache builder
run.py                       end-to-end driver
tests/test_factstore.py      stdlib unittest — FactStore + format_value
out/                         pipeline outputs (gitignored or versioned by you)
```

## Component status

| # | Component         | State    | Notes |
|---|-------------------|----------|-------|
| 1 | SourceLoader      | ✅ done  | All 5 connectors wired |
| 2 | IdentityResolver  | ✅ done  | Exact + fuzzy (difflib), stdlib only |
| 3 | NoiseFilter       | 🟡 stub  | One auto-ack rule wired; needs quoted-reply / signature stripping |
| 4 | FactExtractor     | 🟢 partial | Rule-based for all sources; LLM enrichment slot empty |
| 5 | FactStore         | ✅ done  | Bucketed `(entity_id, key)` index, append-only dedup, conflict detection at confidence floor 0.7, `latest()` with full priority tie-break, JSONL round-trip with id-based dedup. 23 unit tests. |
| 6 | Merger            | ❌ stub  | One-line placeholder. **`format_value()` helper is built and tested**; rendering plumbing waits on Karl's section schema. |
| 7 | Summarizer        | 🟢 partial | `extractor/summarizer.py` — Claude wrapper for `<!-- auto:*.summary -->` blocks. Signal-First philosophy in the system prompt, file-cached at `out/llm_cache/summary.json`, no-ops gracefully without `ANTHROPIC_API_KEY`. Wired for unit `dunning.summary`; other blocks pending. |

## Conventions and gotchas

**`/incremental` is OFF by default.** Per `Sprint.md`, `raw/incremental/` is the
fixture for the second engine run that demonstrates surgical updates. Keep it
out of the v1 run unless `--include-incremental` is passed.

**Single property.** `PROPERTY_ID = "LIE-001"` is hard-coded in `extractor/models.py`.
Don't add multi-tenancy plumbing — the spec explicitly excludes it.

**`source_ref` is a GitHub URL, not a local path.** `extractor/source_ref.py`
autodetects the base from `git remote get-url origin` + current branch. Override
via `--source-ref-base` or `SOURCE_REF_BASE`. Outside a git repo it falls back
to the absolute local path so the pipeline never breaks. **Every Fact must
carry `source_ref` + `source_event_id`** — the merger uses these for the inline
citations the spec requires.

**PDFs go through the pre-OCR cache.** `extractor/sources/pdfs.py` reads
`<file>.pdf.txt` siblings first, falls back to live `pdfminer.six`, then
`pypdf`. If you change the PDF set, run `scripts/preocr.py raw/` to refresh the
cache. The cache is checked in to git so the engine is reproducible without
pdfminer.

**Invoice totals: two PDF layouts in this corpus.** Some invoices are inline
(`Gesamtbetrag: 1.088,85 EUR`); others are tabular and pdfminer flattens them
column-wise (labels first, then amounts). `_extract_totals()` in `pdfs.py`
handles both — it pulls the totals block and uses positional ordering (first
amount = netto, last = brutto). Don't add per-label regexes; that breaks on
the column layout.

**Stammdaten resolves last in the resolver.** `IdentityResolver.resolve()` tries
strong signals (email → IBAN → einheit_nr → phone → address) before fuzzy name
match. Names are noisy in this corpus ("Frau Gertraud Holsten" vs
"Holsten, Gertraud"), so name match is gated on `threshold=0.86`.

**Confidence levels.** Structured sources (stammdaten, bank rows) → 1.0.
Rule-based email classification (subject regex) → 0.85. Body amount sniffing
(e.g. mahnung body) → 0.6–0.7. Facts below `CONFIDENCE_FLOOR = 0.7`
(in `extractor/engine.py`) never participate in conflict detection — they're
weak signals, not contradictions.

**FactStore is append-only.** Dedup never mutates; if a fact is re-observed
with newer `observed_at` or higher `confidence`, a new audit row is appended.
The on-disk JSONL is the full history; `latest()` and `conflicts()` work on
the in-memory index built from that log. `load_jsonl()` dedupes by `fact.id`,
so re-running on the same input is a no-op.

**Conflict detection is by `(entity_id, key)`.** A bucket is conflicted iff
≥2 distinct normalized values exist in it, both at confidence ≥ 0.7. Tie-break
for `latest()`: confidence > observed_at > source priority > extracted_at.
`SOURCE_PRIORITY` (in `engine.py`) is global: `stammdaten=4, letter/invoice/bank=3,
email=1`. **TODO** marker for per-key overrides — bank should beat stammdaten
on payment keys, etc. Acceptable for the demo.

**Time-series keys vs scalar keys.** The conflict detector treats every key
the same — but `payment.amount_eur` for a tenant legitimately differs every
month and should not surface as a `<!-- conflict -->` marker. Run.py reports
two counts: `conflicts (raw)` (all buckets, inflated by time-series) and
`conflicts (merge)` (restricted to the `SCALAR_KEYS` set: `email`, `telefon`,
`iban`, `kaltmiete`, etc.). Only the merge count is meaningful for context.md.
**The Merger should call `format_value(store, entity_id, key)` only for keys
it intends to render as scalars.** That helper is in `engine.py` and returns
either `value [(source)](source_ref)` or a `<!-- conflict -->` block.

**Value normalization for dedup.** Strings → lowercased + stripped. Floats →
rounded to 2dp (so `249.9 == 249.90`). Lists → tuples sorted by `repr` (order-
invariant). When adding a new fact value type, extend `_normalize_value()` in
`engine.py` so dedup compares apples to apples.

**`entity_id is None` facts are persisted but not indexed.** Orphan facts (e.g.
an email subject classifier output that didn't resolve to any entity) end up
in `FactStore._unresolved`, written to JSONL, and excluded from `latest()`/
`conflicts()`. The Merger renders by entity, so unresolved facts have nowhere
to land in `context.md` anyway.

**German throughout.** Field names, file content, and regex patterns are mostly
German. When adding patterns, keep both umlaut and non-umlaut forms (the corpus
has `quoted-printable` encoding leaking through, so `R=C3=B6hricht` and
`Röhricht` both occur).

**No Postgres / no vector DB.** Per `Tech Stack.md` we are deliberately not
building those for v1. The fact store is JSONL on disk.

**LLM summaries are signal-only — never filter noise in the prompt.** The
Summarizer (`extractor/summarizer.py`) follows the user's "Signal-First
Property Management Philosophy" / Trifecta of Truth (Contract / Law / Logic).
Salience extraction is **deterministic Python** in `blocks.py` (e.g.
`_dunning_signal()`): it pre-filters by confidence, key allowlist, recency,
and anomaly status before the LLM sees anything. The model's only job is to
render that already-curated payload as ≤3 German sentences with a triage tag,
the four Golden Rule elements (issue / contract / law / timeline), and
preserved `[(label)](url)` citations. **Never put filtering instructions in
the system prompt** — Claude is bad at "ignore the boring stuff" and good at
"summarize this list".

**Summarizer degrades gracefully.** Missing `ANTHROPIC_API_KEY`, missing
`anthropic` package, or any API error (incl. 401) → the `render_*_summary`
fn returns the deterministic `fallback` string the caller built from the
salience payload. The pipeline never breaks because of LLM availability.
Output is cached at `out/llm_cache/summary.json` keyed by SHA256 of (model,
system prompt, payload), so re-runs on unchanged data make zero API calls
and produce byte-identical output. Cache dir is gitignored.

**The merger only scaffolds new auto-blocks into a fresh file.** If
`context.unit.<id>.md` already exists with auto-blocks, `_replace_blocks`
will only update bodies of blocks that already appear in the file — newly
registered blocks (e.g. a freshly added `dunning.summary`) won't be inserted.
After adding a block, delete the affected `context.unit.*.md` /
`context.property.*.md` files and re-run to pick up the new structure.

## Adding a new source connector

1. Create `extractor/sources/<name>.py` with `def extract(root: Path, *, include_incremental: bool = False) -> Iterator[tuple[Event, list[Fact]]]:`.
2. Use `extractor.source_ref.for_path(path, fragment=...)` for the `source_ref`.
3. Register it in `extractor/extract.py` `SOURCES` list with a flag for whether it walks `incremental/`.
4. Run `python run.py raw/` and check `events by source` in the output.

## Adding a new fact extractor for emails or PDFs

For emails, append a `(regex, intent)` pair to `_INTENT_PATTERNS` in
`extractor/sources/emails.py`. The classifier tags the event; if the intent
needs structured fields, add a branch in the `add()` block at the bottom of
`_emit_eml`.

For PDFs, the body text is already cached. Add a regex at the top of
`extractor/sources/pdfs.py` and an `add()` call inside `_invoice_event` or
`_letter_event`. **Use the totals block helper** (`_extract_totals`) instead of
matching individual labels — see the column-layout note above.

## Adding a new summary block

Pattern lives in `extractor/blocks.py` — see `_dunning_signal()` +
`render_dunning_summary()` as the reference implementation.

1. Write a `_<section>_signal(store, ...)` helper that pulls *only* the salient
   facts (anomalies, conflicts, items with deadlines) into a small JSON dict.
   This is the noise filter — confidence floor, key allowlist, recency window
   live here, NOT in the prompt.
2. Build a `references: list[{label, url}]` list from the same facts'
   `source_ref` so the LLM has citation material.
3. Write `render_<section>_summary(store, ctx)` that:
   - returns `"_no issue_"` immediately if the signal is empty,
   - constructs a deterministic `fallback` string (used when LLM unavailable),
   - calls `(ctx.get("summarizer") or get_summarizer()).summarize(...)`.
4. Register in `PROPERTY_BLOCKS` or `UNIT_BLOCKS` with the auto-block name
   (use a dotted name like `<section>.summary`).
5. Add `<!-- auto:<name> -->_no issue_<!-- /auto:<name> -->` to the matching
   template (`context.property.template.md` / `context.unit.template.md`).
6. Delete affected rendered files (see merger gotcha) and re-run
   `python run.py raw/ --today YYYY-MM-DD` so `today` reaches the LLM.

## Adding tests

All tests live under `tests/` and run via stdlib `unittest`:

```bash
python -m unittest tests.test_factstore -v       # one module, verbose
python -m unittest discover tests                # everything
```

When adding behavior to `FactStore` or `format_value`, add the unit case to
`tests/test_factstore.py` first. The test file uses a `make_fact()` helper at
the top — copy that pattern; don't construct `Fact()` by hand in every test.

## Sprint.md ownership

Karl owns the `context.md` schema and the chosen flagship use case. Zeng owns
the engine. The next blocking handoff is the section schema → it determines
which facts the Merger has to render and therefore which extractors are critical.
The `format_value` helper is already wired so the Merger only needs to decide
*which keys go where* — the conflict-marker plumbing is done.

## What NOT to do

- Don't add multi-property support, auth, or a vector DB.
- Don't extract from `raw/incremental/` in the v1 run.
- Don't replace `pdfminer.six` text with on-the-fly extraction in hot paths —
  the `.pdf.txt` cache exists for a reason.
- Don't write facts without `source_ref` + `source_event_id`. Provenance is
  load-bearing for the Merger.
- Don't drop the `confidence` field on facts. It gates merger behavior.
- Don't reformat the German content of `raw/` — it's the input fixture.
- Don't mutate facts in `FactStore`. The store is append-only; re-observation
  appends a new row. Mutating breaks the JSONL audit log.
- Don't run conflict detection on time-series keys (`payment.*`,
  `communication.*`, etc.). Use `format_value` only for scalar identity/
  contract keys — see the SCALAR_KEYS set in `run.py` for the allowlist.
- Don't ask the Summarizer to filter noise. Filter deterministically in the
  `_<section>_signal()` helper before the LLM sees the payload — Claude is bad
  at "ignore the boring stuff" and good at "summarize this list".
- Don't strip URLs from summary output. The audit trail is load-bearing per
  the Signal-First philosophy; the system prompt requires the LLM to preserve
  `[(label)](url)` citations in the rendered summary.
- Don't put the LLM cache anywhere except `out/llm_cache/`. The path is
  gitignored; relocating it risks committing cached responses.
