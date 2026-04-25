# final_execution.md — 10-hour hackathon plan (source of truth)

Supersedes ExecutionPlan1, ExecutionPlan2, ExecutionPlan3, and the prior
`final_execution_optional.md`. Combines the **engine depth** (surgical merger,
dunning, Mahnstufe, Verzugszinsen, provenance) with the **UI depth** (Lovable
+ Supabase Edge Function for `answer_question`, benchmark harness).

## What we ship

A working `property-context-resolver` demo with two halves working off the
same Supabase row:

1. **Engine (Zeng's repo).** Raw property data → JSONL fact store →
   surgically-updated `context.md` per tenant, written to disk (git-backed)
   AND mirrored to Supabase. Every fact carries an inline citation back to
   its source. Includes the **Overdue Tenant Reminder** flagship: dunning
   roll-up with Mahnstufe state and Verzugszinsen (§ 288 BGB).
2. **UI (Karl's Lovable project).** Minimal property dashboard with one
   primary feature: "Ask About This Property" → Supabase Edge Function calls
   Claude with the live `context.md` → returns a cited answer + latency.
   Plus a benchmark slide: same question against (a) `context.md` vs
   (b) raw-data corpus, side-by-side latency + cost.

**Demo flow:** run engine → `context.md` v1 lands in Supabase, renders in
Lovable. Karl asks "Is MIE-001 overdue?" → answer cites the dunning section.
Karl makes a human edit. Drop in incremental email + bank row + Mahnung PDF.
Re-run. UI updates live. `git diff` shows human edit preserved + new facts
merged + every line cited. Close on the benchmark slide: 10× faster, ~50×
cheaper than the same question against raw data.

## Why this is feasible in 10 hours

We start substantially built. From `CLAUDE.md`:

| # | Component         | State    | Hackathon work |
|---|-------------------|----------|----------------|
| 1 | SourceLoader      | done     | none |
| 2 | IdentityResolver  | done     | none |
| 3 | NoiseFilter       | stub     | minimal — keep auto-ack rule |
| 4 | FactExtractor     | partial  | optional LLM enrichment behind a flag |
| 5 | FactStore         | done     | none |
| 6 | Merger            | stub     | **the main backend build** — 3-4h |

`format_value()` (in `extractor/engine.py`) is built and tested — returns
either `value [(source)](source_ref)` or a `<!-- conflict -->` block. The
Merger only has to decide *which keys go where*. That single helper is why
3 hours of Merger work is enough.

UI is light because Lovable + Supabase Edge Function is roughly 2 hours of
glue — not a full app build.

## Architecture

```
Zeng's repo (Python engine)              Karl's Lovable project
├── extractor/                           ├── Lovable UI (markdown viewer
│   ├── sources/      ✓                  │   + Ask About This Property)
│   ├── identity.py   ✓                  │
│   ├── engine.py     +dunning           │
│   ├── merger.py     NEW                │
│   └── models.py     ✓                  └── supabase/functions/
├── run.py            +supabase write          answer_question/  NEW
├── out/                                       (TS, calls Claude)
│   ├── events.jsonl                                  │
│   ├── facts.jsonl                                   │
│   └── context.LIE-001.md  ──────────┐               │
└── tests/                            │               │
                                      ▼               ▼
                        ┌─────────────────────────────────────┐
                        │      Supabase (shared data layer)   │
                        │  properties.context_md  (the file)  │
                        │  context_updates        (audit log) │
                        │  queries                (Q&A log    │
                        │                          + bench)   │
                        │  storage: raw-uploads               │
                        └─────────────────────────────────────┘
```

**Two repos, never share code.** They share **Supabase** as the data layer.
The Python engine writes to `properties.context_md` via `supabase-py`; the
Lovable UI reads from the same column via Realtime. The Edge Function
`answer_question` is the only Supabase-side code with logic.

## Tech stack — what we use, what we drop

Use:
- Existing Python engine (`extractor/`, `run.py`, `tests/`) — system of record.
- Git-backed `context.md` in Zeng's repo — canonical artifact, full history,
  free diffs (this IS the demo's surgical-update story).
- Claude (Anthropic SDK) at two call sites only:
  - Optional email-body enrichment in `extractor/sources/emails.py` (flagged).
  - The Edge Function `answer_question` (single Q&A pass).
- **Supabase** as shared data layer:
  - `properties` table (mirror of the rendered `context.md`).
  - `context_updates` table (audit log of engine runs).
  - `queries` table (Q&A log + benchmark numbers).
  - `raw-uploads` Storage bucket (Lovable upload zone, optional).
  - One Edge Function: `answer_question`.
- Lovable for the frontend (auto-generated from the prompt below).

Drop, and do not be tempted back in:
- Supabase as the **fact store**. The JSONL log under `out/` is append-only
  with 23 unit tests — recreating that in Postgres in 10 hours buys nothing.
- Edge Functions running the extraction pipeline. The engine runs locally;
  Supabase only sees the rendered output + Q&A traffic.
- Multi-property infra — `PROPERTY_ID = "LIE-001"` is hardcoded in
  `extractor/models.py` and stays hardcoded.
- Custom LLM gateway (Langdock), vector DB, fine-tuning, auth, mobile app.
- Replicating `customers` / `facts` schemas in Supabase. Three small tables
  is the entire contract.

## Supabase schema (final)

```sql
properties (
  id          uuid pk default gen_random_uuid(),
  property_id text unique not null,    -- 'LIE-001'
  name        text,                    -- 'WEG Immanuelkirchstraße 26'
  address     text,
  context_md  text,                    -- mirror of out/context.LIE-001.md
  last_run_at timestamptz
);

context_updates (
  id              uuid pk default gen_random_uuid(),
  property_id     text references properties(property_id),
  source_filename text,
  diff_summary    text,                -- short delta, e.g. "+2 facts, 0 conflicts"
  created_at      timestamptz default now()
);

queries (
  id           uuid pk default gen_random_uuid(),
  property_id  text references properties(property_id),
  question     text,
  answer       text,
  mode         text,                   -- 'context_md' | 'raw_data' (for benchmark)
  latency_ms   int,
  input_tokens int,
  output_tokens int,
  created_at   timestamptz default now()
);

-- Storage bucket: raw-uploads (private; for live upload demo, optional)
```

## Hour-by-hour

### Hour 0 — Scope lock, Supabase project, two repos online

**Together (15 min):** read this doc, lock flagship = Overdue Tenant
Reminder for MIE-001 only.

**Karl (parallel, 30 min):**
- Create Lovable project, paste the prompt at the bottom of this doc.
- Lovable auto-provisions Supabase + GitHub repo + applies schema + seeds
  one row.
- Verify: `properties` row exists, schema matches above, Lovable home page
  renders the seed `context_md`.
- Share `SUPABASE_URL` + `SUPABASE_SERVICE_KEY` with Zeng (1Password / private
  Notion). Service-role key, not anon — the engine writes.

**Zeng (parallel, 30 min):**
- `git checkout -b final-demo` in `property-context-resolver`.
- Confirm `python run.py raw/` runs green.
- Confirm `python -m unittest discover tests` passes.
- `pip install supabase` and add `supabase-py` import + env-var loading to
  `run.py`. Smoke-test by reading the seed row.

### Hour 1 — Karl: gold-standard `context.md` for MIE-001 (Zeng works in parallel below)

Deliverable: `out/context.LIE-001.md.goldstandard` — hand-written by Karl
from the Buena corpus, using the schema in `CustomerSchema.md` §1 and the
context.template referenced in `Sprint.md`.

- YAML frontmatter with all 1.1–1.4 scalars filled in.
- Sections: `## Node: Lease & Contract`, `## Node: Payments & Banking`,
  `## Node: Communications`, `## Node: Maintenance`,
  `## Node: Legal / Disputes`, `## Node: Notes`.
- Each fact carries an inline `[(source)](source_ref)` citation.
- Paste this content into Supabase `properties.context_md` (via Lovable's
  table editor) as the seed — so the UI demos render meaningful content
  even before Zeng's engine writes.

This file is the target the engine must converge to.

### Hours 1-3 — Zeng: build the Merger

Deliverable: `extractor/merger.py` + `run.py` integration. Replaces the
current stub.

1. `SECTION_SCHEMA` — list of `(section_title, [keys...])` derived from
   Karl's gold-standard. Each section ↔ one `<!-- auto:section -->...
   <!-- /auto -->` block.
2. For each scalar key call `format_value(store, "MIE-001", key)`. The
   helper already returns `value [(source)](source_ref)` or
   `<!-- conflict -->`. Do not re-implement.
3. Time-series sections (Communications, Payments) render as markdown
   tables sorted by `observed_at` desc, last N rows. Iterate facts where
   `key.startswith("payment.")` or `key.startswith("communication.")`.
   These keys are NOT in `SCALAR_KEYS` and must NOT pass through
   `format_value` (CLAUDE.md is explicit).
4. Surgical-update rule: read existing `context.md`; replace only the
   contents of each auto-block; never touch anything outside. YAML
   frontmatter is fully auto-managed (regenerated each run).
5. Atomic writes: `out/context.LIE-001.md.tmp` → rename. So git diffs are
   meaningful even mid-run.
6. After write: `sb.table("properties").update({"context_md": new_md,
   "last_run_at": "now()"}).eq("property_id", "LIE-001").execute()`.
   Insert a row in `context_updates` with a one-line diff summary.

Exit criteria: `python run.py raw/` produces a `context.md` whose section
headers and key list match the gold-standard exactly; Lovable UI shows the
new content within ~1s via Realtime.

### Hours 3-4 — Zeng: dunning / overdue logic (the flagship)

Deliverable: dunning roll-up rendered in `## Node: Legal / Disputes`.

1. `payment.expected_eur` baseline = `kaltmiete + nk_vorauszahlung`
   (already in stammdaten facts).
2. Reconciler in `engine.py`: per month in 2024-2025, sum
   `payment.amount_eur` rows for MIE-001 where `direction=in` and the
   verwendungszweck matches the month. Compare to expected. If short,
   emit `dunning.month_short_eur` at confidence 1.0.
3. Cross-reference `briefe/*Mahnung*.pdf` facts (already extracted) for
   `mahnung.invoice_ref` and `mahnung.offener_betrag_eur`.
4. Mahnstufe 0/1/2/3 per Sprint.md framework: 0 = on time, 1 = 14d
   overdue, 2 = first Mahnung sent, 3 = second Mahnung + Verzugszinsen.
5. Verzugszinsen per § 288 BGB: `5pp + ECB base rate` × overdue principal.
   Hardcode `ECB_BASE = 3.5` for the demo.

Exit criteria: `## Node: Legal / Disputes` reads "Mieter MIE-001 ist N
Monate im Verzug, offener Betrag X EUR, Mahnstufe M, Verzugszinsen Y EUR"
with all four numbers cited.

### Hours 4-5 — Karl: implement `answer_question` Edge Function

Deliverable: working Edge Function called from the Lovable Ask button.

```ts
// supabase/functions/answer_question/index.ts
import { serve } from "https://deno.land/std/http/server.ts";
import { createClient } from "https://esm.sh/@supabase/supabase-js@2";
import Anthropic from "https://esm.sh/@anthropic-ai/sdk@0";

serve(async (req) => {
  const { property_id, question } = await req.json();
  const sb = createClient(
    Deno.env.get("SUPABASE_URL")!,
    Deno.env.get("SUPABASE_SERVICE_KEY")!,
  );
  const anthropic = new Anthropic({
    apiKey: Deno.env.get("ANTHROPIC_API_KEY")!,
  });

  const { data: row } = await sb
    .from("properties").select("context_md")
    .eq("property_id", property_id).single();

  const t0 = Date.now();
  const msg = await anthropic.messages.create({
    model: "claude-sonnet-4-6",
    max_tokens: 1024,
    system: `You answer property-management questions using ONLY the
provided context.md. The file uses <!-- auto:section --> blocks with
inline citations [(source)](url). Cite the same source links in your
answer. If a fact is not in context.md, say "Not in current context.md"
and name the section it would belong in. Never invent facts. Answer in
the same language the question was asked in (de or en).`,
    messages: [{
      role: "user",
      content: `# context.md\n\n${row.context_md}\n\n# Question\n\n${question}`,
    }],
  });
  const latency_ms = Date.now() - t0;
  const answer = msg.content
    .map((c) => (c.type === "text" ? c.text : "")).join("");

  await sb.from("queries").insert({
    property_id, question, answer, mode: "context_md",
    latency_ms,
    input_tokens: msg.usage.input_tokens,
    output_tokens: msg.usage.output_tokens,
  });
  return new Response(JSON.stringify({ answer, latency_ms }), {
    headers: { "Content-Type": "application/json" },
  });
});
```

Set Supabase secrets: `SUPABASE_URL`, `SUPABASE_SERVICE_KEY`,
`ANTHROPIC_API_KEY`. Wire Lovable's Ask button to invoke this function.

Exit criteria: Karl asks "Ist MIE-001 im Verzug?" via Lovable; answer cites
the dunning section; row in `queries` shows latency + token counts.

### Hour 5 — Pair: end-to-end smoke test

Both: confirm the loop works.
1. `python run.py raw/` writes context to Supabase.
2. Lovable viewer shows the live content.
3. Karl asks 3 questions: "Wer wohnt in EH-025?", "Ist MIE-001 im Verzug?",
   "Welche Mahnungen wurden bereits versendet?"
4. All three return cited answers in <2s.
5. `queries` table has 3 rows.

Any breakage stops other work until fixed.

### Hours 5-6 — Zeng: optional LLM email enrichment (drop if behind)

Deliverable: one new code path in `extractor/sources/emails.py`.

1. Karl writes the system prompt — single Claude call per relevant email:
   - Input: subject + body (max 2k tokens) + already-known customer facts.
   - Output: strict JSON `[{key, value, confidence, reasoning}]`.
   - Allowed keys (locked): `dunning.acknowledgement`,
     `payment.deferral_request`, `complaint.maintenance_issue`,
     `lease.cancellation_intent`. Anything else rejected at parse.
2. Behind `ENABLE_LLM_ENRICHMENT` env flag.
3. Per-email cache `out/llm_cache/<event_id>.json` — re-runs don't re-pay.
4. Confidence floor 0.7 stays. Below = dropped pre-store.

Exit criteria: at least 3 emails produce structured facts that visibly
change `context.md` (deferral request → Legal/Disputes; maintenance
complaint → Maintenance). **Skip this hour entirely if Hour 5 smoke test
revealed any P0 issues.**

### Hours 6-7 — Surgical-update demo (the headline)

Deliverable: a `git diff` + a live UI update we will show on stage.

1. Commit v1 of `out/context.LIE-001.md` to `final-demo`.
2. Karl makes one human edit OUTSIDE the auto-blocks (e.g., `## Notes`
   line: "Mieter ist konfliktfreudig, behutsam vorgehen"). Commit.
3. Run `python run.py raw/ --include-incremental`. The incremental drop
   carries a new email + bank row + Mahnung PDF (Buena's gift).
4. Verify:
   - Human's `## Notes` line untouched.
   - Auto-blocks updated; new payment row, new communication row, dunning
     roll-up updated; every new line cited.
   - No spurious `<!-- conflict -->` markers on scalars.
   - Lovable UI updates live via Realtime — no refresh.
5. Re-ask "Ist MIE-001 im Verzug?" → answer reflects the new Mahnung.
   Compare in the demo.

Exit criteria: clean, narratable `git diff` + a live UI update showing the
same question now answers differently because the context changed.

### Hour 7-8 — Karl: benchmark harness

Deliverable: a one-shot script + a slide.

1. Pick 5 representative questions (mix of identity, dunning, payments,
   communications):
   - "Wer wohnt in EH-025?"
   - "Ist MIE-001 im Verzug? Wie hoch ist der offene Betrag?"
   - "Wann war die letzte Mietzahlung von MIE-001?"
   - "Welche Mahnungen wurden bereits versendet?"
   - "Gibt es offene Reparaturen?"
2. Run each question twice:
   - Mode `context_md`: existing Edge Function. ~3-5k input tokens.
   - Mode `raw_data`: same prompt but with the entire raw corpus as input
     (or as much as fits in 200k context — bank CSV + key emails + lease).
     Probably 80-150k input tokens. Implement as a second Edge Function
     `answer_question_raw`.
3. Both modes log to `queries` with `mode` set accordingly.
4. Slide: a 5-row table — question, latency_md vs latency_raw,
   tokens_md vs tokens_raw, cost_md vs cost_raw. Expect ~10× faster,
   ~50× cheaper.

This slide is the close.

### Hour 8 — Test pass + reproducibility

Zeng: `python -m unittest discover tests` green; wipe `out/` and re-run
cold to verify reproducibility; spot-check 3 random emails and 3 random
bank rows for correct attribution + working source links in the rendered
`context.md`.

Karl: deploy Lovable to a public URL; verify the Ask flow works from a
fresh browser; record a screencast of the full demo as fallback.

### Hours 8-9 — Pitch prep (Karl)

90s pitch + 4-min demo:
1. Problem (15s): 90% of email is noise; humans can't keep state for 100
   tenants; legally-required Mahnung calculations are slow and error-prone.
2. Architecture (30s): `raw/ → engine → context.md`, git-backed,
   surgically updated, every fact cited.
3. Live demo (2.5min):
   - Show MIE-001's `context.md` in the Lovable viewer.
   - Ask "Ist MIE-001 im Verzug?" → cited answer in ~1s.
   - Click a citation → land on the source PDF in GitHub.
   - Drop in incremental files → engine runs → UI updates live.
   - Re-ask the same question → answer reflects new Mahnung.
4. Benchmark slide (45s): the 5×2 latency/cost table. Close: "Same
   question, 10× faster, 50× cheaper, with citations."

Fallback assets: pre-recorded screencast (hour 8); cached LLM responses;
checked-in before/after `context.md` in git.

### Hours 9-10 — Buffer

Reserved. No new features. Use for log polish, README, dry-running pitch,
fixing any P0 surfaced at hour 8.

## File deltas at end of 10 hours

```
property-context-resolver (Zeng's repo)
├── extractor/
│   ├── merger.py                     NEW
│   ├── engine.py                     MOD — dunning + Mahnstufe
│   └── sources/emails.py             MOD — optional LLM enrichment (flagged)
├── run.py                            MOD — Supabase write
├── scripts/benchmark.py              NEW — feeds queries table
├── out/
│   ├── context.LIE-001.md            NEW — generated, committed
│   ├── context.LIE-001.md.goldstandard  NEW — Karl's hand-built target
│   └── llm_cache/                    NEW — per-email response cache
├── .env.example                      NEW — SUPABASE_URL / SERVICE_KEY / ANTHROPIC_API_KEY
└── final_execution.md                this file

Lovable project (Karl's repo, auto-managed)
└── supabase/functions/
    ├── answer_question/index.ts      NEW
    └── answer_question_raw/index.ts  NEW (benchmark only)
```

## Cuts if behind at hour 5

In priority order — drop from the bottom:

1. **`answer_question_raw` benchmark** → keep the comparison theoretical in
   the slide ("based on token counts: ~10× faster, ~50× cheaper"). Saves
   ~45 min of Edge Function work.
2. **LLM email enrichment** → ship with regex-classifier facts only. The
   dunning logic is fully deterministic and is the flagship.
3. **Lovable diff/upload polish** → static markdown viewer + Ask button is
   enough. Skip live upload.
4. **Mahnstufe state machine** → just compute "X months overdue, Y EUR
   open" without the Mahnstufe grade. Verzugszinsen drops with this.
5. **Surgical-update demo** → run a single non-incremental pass; pitch the
   architecture rather than the live diff. (Last resort — this is the
   strongest part of the story.)
6. **Lovable UI** → demo from terminal + GitHub web UI. The git-backed
   diff alone still tells the story.

Non-negotiable core: a `context.md` for MIE-001 generated end-to-end from
`raw/` with the four flagship facts (overdue months, open balance, last
payment, last communication), each with working citations, mirrored in
Supabase, queryable via the Ask button. If we have that at hour 9 we have
a demo.

## Hard rules (lifted from CLAUDE.md so the agent does not drift)

- No multi-property support, auth, or vector DB.
- No `raw/incremental/` in the default run; only behind `--include-incremental`.
- No on-the-fly PDF extraction in hot paths — the `.pdf.txt` cache is law.
- No facts without `source_ref` + `source_event_id`. Provenance is load-bearing.
- No mutating facts in `FactStore`. Append-only; re-observation appends.
- No reformatting of `raw/` content — it is the input fixture.
- No `format_value()` calls on time-series keys (`payment.*`,
  `communication.*`). Use the `SCALAR_KEYS` allowlist.
- No reformatting of German content. Keep umlaut + non-umlaut variants in
  any new regex (corpus has `quoted-printable` leakage).
- Service-role key for backend only — never ship it to Lovable's frontend.

## Ownership

| Hour | Karl                                     | Zeng                          |
|------|------------------------------------------|-------------------------------|
| 0    | Lovable + Supabase up, share keys        | branch + supabase-py wired    |
| 1    | gold-standard `context.md` + seed row    | start Merger                  |
| 2    | gold-standard polish; review schema      | Merger                        |
| 3    | review Merger output                     | finish Merger; start dunning  |
| 4    | implement `answer_question` Edge Fn      | dunning + Mahnstufe           |
| 5    | UI Ask flow polish                       | wire engine → Supabase write  |
| 5-6  | (smoke test together)                    | optional LLM email enrichment |
| 6    | surgical-update demo (live UI side)      | surgical-update (engine side) |
| 7    | benchmark harness + 5×2 slide            | `answer_question_raw` Edge Fn |
| 8    | deploy + screencast fallback             | full test pass + cold rerun   |
| 9    | pitch + dry run                          | bug fixes from hour 8         |
| 10   | buffer                                   | buffer                        |

---

## Appendix: Lovable creation prompt (paste into a new Lovable project)

```
Build "Buena Context Engine" — minimal property management dashboard demo.

UI: clean, minimal, Linear / Notion aesthetic. Light mode default. English
+ German content. Single user, no auth.

PAGES

1. Home — properties list
   - Cards showing: property name, address, last-updated relative time.
   - Click → property detail.

2. Property detail
   - Header: property name, address, "Last engine run: <relative time>".
   - Main pane: rendered context.md (markdown, with working links).
     Subscribe to Supabase Realtime on properties row so it updates live.
   - Primary button: "Ask About This Property" → modal with textarea +
     Ask button. After submit: render answer + "Answered in <latency_ms> ms".
     Calls Supabase Edge Function answer_question(property_id, question).

SUPABASE BACKEND

Tables:
- properties (id uuid pk default gen_random_uuid(), property_id text unique,
  name text, address text, context_md text, last_run_at timestamptz)
- context_updates (id uuid pk default gen_random_uuid(), property_id text
  references properties(property_id), source_filename text, diff_summary
  text, created_at timestamptz default now())
- queries (id uuid pk default gen_random_uuid(), property_id text references
  properties(property_id), question text, answer text, mode text,
  latency_ms int, input_tokens int, output_tokens int,
  created_at timestamptz default now())

Storage bucket: raw-uploads (private).

Seed properties with one row: property_id "LIE-001",
name "WEG Immanuelkirchstraße 26", address "Immanuelkirchstraße 26, 10405
Berlin", context_md "# Property Context — LIE-001\n\n_Populated by engine_".

Edge Function answer_question(property_id, question):
- Stub for now: returns { answer: "Stub. LLM wiring pending.", latency_ms: 42 }.
- Logs a row in queries with mode='context_md'.
- Will be replaced with the real Claude-calling implementation.

No auth, no analytics. Light mode only. Keep it shippable in one go.
```
