# Buena Context Engine — backend handoff

I built a Python engine that produces a per-property `context.md` and writes
it to Supabase. The Lovable scaffold needs the changes below so the engine
and the demo Q&A flow line up. Apply each section as written.

---

## 1. Replace the existing migration

The current migration in `supabase/migrations/` has a schema mismatch with the
engine and Edge Functions: missing `property_id text` on `properties`, missing
`mode / input_tokens / output_tokens` on `queries`, FKs reference uuid instead
of text, wrong storage bucket name, and a generic seed row. Replace its
contents with the SQL below (keep the same filename so the migration hasn't
been applied yet — this is a clean rewrite, not an alter).

```sql
-- Schema for the property-context-resolver demo.
-- The Python engine and both Edge Functions look up by the text identifier
-- `property_id` (e.g. "LIE-001"), not by uuid — so every FK below references
-- properties.property_id, not properties.id.

-- properties --------------------------------------------------------------

CREATE TABLE public.properties (
  id           UUID NOT NULL DEFAULT gen_random_uuid() PRIMARY KEY,
  property_id  TEXT NOT NULL UNIQUE,                  -- e.g. 'LIE-001'
  name         TEXT,
  address      TEXT,
  context_md   TEXT,
  last_run_at  TIMESTAMPTZ
);

-- context_updates ---------------------------------------------------------

CREATE TABLE public.context_updates (
  id              UUID NOT NULL DEFAULT gen_random_uuid() PRIMARY KEY,
  property_id     TEXT NOT NULL REFERENCES public.properties(property_id) ON DELETE CASCADE,
  source_filename TEXT,
  diff_summary    TEXT,
  created_at      TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- queries -----------------------------------------------------------------

CREATE TABLE public.queries (
  id            UUID NOT NULL DEFAULT gen_random_uuid() PRIMARY KEY,
  property_id   TEXT NOT NULL REFERENCES public.properties(property_id) ON DELETE CASCADE,
  question      TEXT NOT NULL,
  answer        TEXT,
  mode          TEXT,                                  -- 'context_md' | 'raw_data'
  latency_ms    INT,
  input_tokens  INT,
  output_tokens INT,
  created_at    TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- RLS — no-auth demo: public read on all three tables. Writes go through
-- service-role (engine + Edge Functions), which bypasses RLS.

ALTER TABLE public.properties      ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.context_updates ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.queries         ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Public can read properties"      ON public.properties      FOR SELECT USING (true);
CREATE POLICY "Public can read context_updates" ON public.context_updates FOR SELECT USING (true);
CREATE POLICY "Public can read queries"         ON public.queries         FOR SELECT USING (true);

-- Storage bucket consumed by `answer_question_raw` (the benchmark function).
-- A Python script uploads the bundle to: raw-uploads/<property_id>/raw_bundle.txt
INSERT INTO storage.buckets (id, name, public)
VALUES ('raw-uploads', 'raw-uploads', false)
ON CONFLICT (id) DO NOTHING;

-- Seed: LIE-001 row so the engine can upsert into it on first run and the UI
-- has something to render before the engine ever fires.
INSERT INTO public.properties (property_id, name, address, context_md, last_run_at)
VALUES (
  'LIE-001',
  'WEG Immanuelkirchstraße 26',
  'Immanuelkirchstraße 26, 10405 Berlin',
  E'# Property Context — LIE-001\n\n_Populated by engine on first run._',
  now()
)
ON CONFLICT (property_id) DO NOTHING;
```

---

## 2. Replace `supabase/functions/answer_question/index.ts`

The current stub returns `"Stub. LLM wiring pending."`. Replace it with the
real Claude-calling implementation below.

```ts
// supabase/functions/answer_question/index.ts
//
// Answers a property-management question using ONLY the rendered context.md
// for that property, then logs the Q&A to `queries` with mode=context_md.
//
// Required env (Supabase project secrets):
//   SUPABASE_URL              auto-injected
//   SUPABASE_SERVICE_ROLE_KEY service-role key — never ship to UI
//   ANTHROPIC_API_KEY         Anthropic console key

import { createClient } from "npm:@supabase/supabase-js@2";
import Anthropic from "npm:@anthropic-ai/sdk@0.30.1";

const corsHeaders = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers":
    "authorization, x-client-info, apikey, content-type, x-supabase-client-platform, x-supabase-client-platform-version, x-supabase-client-runtime, x-supabase-client-runtime-version",
};

const ANTHROPIC_MODEL = "claude-sonnet-4-6";

const SYSTEM_PROMPT = `You answer property-management questions using ONLY the
provided context.md. The file uses <!-- auto:section --> blocks with inline
citations of the form [(source)](url). When you cite, copy those exact source
links into your answer so the user can click through to the underlying PDF /
email / bank row.

Rules:
- Never invent facts. If a fact is not in context.md, reply "Not in current
  context.md" and name the section it would belong in (e.g. "Node:
  Maintenance"). Do not extrapolate from related facts.
- The "Status" line in "Node: Legal / Disputes" is the canonical answer for
  any "ist X im Verzug" question. Cite it verbatim.
- When you mention a number (Mahnstufe, offener Betrag, Verzugszinsen, Monate
  im Verzug, Kaltmiete, etc.), include the matching [(source)](url) link from
  context.md on the same line.
- Answer in the same language the question was asked in (de or en). Match
  the user's tone — terse questions get terse answers.
- Keep answers under 6 sentences unless the user asks for detail.`;

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") {
    return new Response("ok", { headers: corsHeaders });
  }

  try {
    const { property_id, question } = await req.json();

    if (!property_id || !question || typeof question !== "string") {
      return new Response(
        JSON.stringify({ error: "property_id and question are required" }),
        { status: 400, headers: { ...corsHeaders, "Content-Type": "application/json" } }
      );
    }

    const supabase = createClient(
      Deno.env.get("SUPABASE_URL")!,
      Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!
    );

    const anthropicKey = Deno.env.get("ANTHROPIC_API_KEY");
    if (!anthropicKey) {
      return new Response(
        JSON.stringify({ error: "ANTHROPIC_API_KEY is not configured" }),
        { status: 500, headers: { ...corsHeaders, "Content-Type": "application/json" } }
      );
    }
    const anthropic = new Anthropic({ apiKey: anthropicKey });

    const { data: row, error: rowErr } = await supabase
      .from("properties")
      .select("context_md")
      .eq("property_id", property_id)
      .maybeSingle();

    if (rowErr) {
      return new Response(
        JSON.stringify({ error: `Supabase read failed: ${rowErr.message}` }),
        { status: 500, headers: { ...corsHeaders, "Content-Type": "application/json" } }
      );
    }
    if (!row || !row.context_md) {
      return new Response(
        JSON.stringify({ error: `No context_md found for property_id=${property_id}` }),
        { status: 404, headers: { ...corsHeaders, "Content-Type": "application/json" } }
      );
    }

    const t0 = Date.now();
    const msg = await anthropic.messages.create({
      model: ANTHROPIC_MODEL,
      max_tokens: 1024,
      system: [
        {
          type: "text",
          text: SYSTEM_PROMPT,
          cache_control: { type: "ephemeral" },
        },
      ],
      messages: [
        {
          role: "user",
          content: `# context.md\n\n${row.context_md}\n\n# Question\n\n${question}`,
        },
      ],
    });
    const latency_ms = Date.now() - t0;

    const answer = msg.content
      .map((c) => (c.type === "text" ? c.text : ""))
      .join("")
      .trim();

    const { error: insertErr } = await supabase.from("queries").insert({
      property_id,
      question,
      answer,
      mode: "context_md",
      latency_ms,
      input_tokens: msg.usage.input_tokens,
      output_tokens: msg.usage.output_tokens,
    });

    if (insertErr) {
      console.error("Insert query failed:", insertErr);
    }

    return new Response(
      JSON.stringify({
        answer,
        latency_ms,
        input_tokens: msg.usage.input_tokens,
        output_tokens: msg.usage.output_tokens,
      }),
      {
        headers: { ...corsHeaders, "Content-Type": "application/json" },
        status: 200,
      }
    );
  } catch (err) {
    console.error("answer_question error:", err);
    return new Response(
      JSON.stringify({ error: (err as Error).message }),
      { status: 500, headers: { ...corsHeaders, "Content-Type": "application/json" } }
    );
  }
});
```

---

## 3. Add a new Edge Function: `supabase/functions/answer_question_raw/index.ts`

Powers the benchmark slide that compares engine-rendered context.md against
the raw corpus. Reads a pre-built bundle from Supabase Storage at
`raw-uploads/<property_id>/raw_bundle.txt` (uploaded out-of-band by a Python
script) and asks Claude the same question.

```ts
// supabase/functions/answer_question_raw/index.ts
//
// Benchmark companion to `answer_question`. Same prompt, same model, but the
// LLM gets the *raw* corpus instead of the engine-rendered context.md.

import { createClient } from "npm:@supabase/supabase-js@2";
import Anthropic from "npm:@anthropic-ai/sdk@0.30.1";

const corsHeaders = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers":
    "authorization, x-client-info, apikey, content-type, x-supabase-client-platform, x-supabase-client-platform-version, x-supabase-client-runtime, x-supabase-client-runtime-version",
};

const ANTHROPIC_MODEL = "claude-sonnet-4-6";
const RAW_BUCKET = "raw-uploads";
const RAW_BUNDLE_KEY = (property_id: string) => `${property_id}/raw_bundle.txt`;

const SYSTEM_PROMPT = `You answer property-management questions using ONLY the
provided raw corpus (stammdaten JSON, bank CSV rows, scanned letters,
invoices, emails). Never invent facts. If the answer is not in the corpus,
reply "Not in raw corpus" and name the source you'd expect it in.

When you cite a number, point to the source file and a row/line/section so a
human can verify (e.g. "kontoauszug_2024_2025.csv row TX-01552",
"briefe/.../20250717_mahnung_LTR-0132.pdf"). Answer in the same language as
the question (de or en). Keep answers under 6 sentences unless asked for
detail.`;

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") {
    return new Response("ok", { headers: corsHeaders });
  }

  try {
    const { property_id, question } = await req.json();

    if (!property_id || !question || typeof question !== "string") {
      return new Response(
        JSON.stringify({ error: "property_id and question are required" }),
        { status: 400, headers: { ...corsHeaders, "Content-Type": "application/json" } }
      );
    }

    const supabase = createClient(
      Deno.env.get("SUPABASE_URL")!,
      Deno.env.get("SUPABASE_SERVICE_ROLE_KEY")!
    );

    const anthropicKey = Deno.env.get("ANTHROPIC_API_KEY");
    if (!anthropicKey) {
      return new Response(
        JSON.stringify({ error: "ANTHROPIC_API_KEY is not configured" }),
        { status: 500, headers: { ...corsHeaders, "Content-Type": "application/json" } }
      );
    }
    const anthropic = new Anthropic({ apiKey: anthropicKey });

    const { data: blob, error: downloadErr } = await supabase.storage
      .from(RAW_BUCKET)
      .download(RAW_BUNDLE_KEY(property_id));

    if (downloadErr || !blob) {
      const msg = downloadErr?.message ?? "bundle missing";
      return new Response(
        JSON.stringify({
          error: `Raw bundle not found at ${RAW_BUCKET}/${RAW_BUNDLE_KEY(property_id)}: ${msg}.`,
        }),
        { status: 404, headers: { ...corsHeaders, "Content-Type": "application/json" } }
      );
    }
    const bundle = await blob.text();

    const t0 = Date.now();
    const msg = await anthropic.messages.create({
      model: ANTHROPIC_MODEL,
      max_tokens: 1024,
      system: [
        {
          type: "text",
          text: SYSTEM_PROMPT,
          cache_control: { type: "ephemeral" },
        },
      ],
      messages: [
        {
          role: "user",
          content: [
            {
              type: "text",
              text: `# Raw corpus for ${property_id}\n\n${bundle}`,
              cache_control: { type: "ephemeral" },
            },
            {
              type: "text",
              text: `# Question\n\n${question}`,
            },
          ],
        },
      ],
    });
    const latency_ms = Date.now() - t0;

    const answer = msg.content
      .map((c) => (c.type === "text" ? c.text : ""))
      .join("")
      .trim();

    const usage = msg.usage as {
      input_tokens: number;
      output_tokens: number;
      cache_creation_input_tokens?: number;
      cache_read_input_tokens?: number;
    };

    const { error: insertErr } = await supabase.from("queries").insert({
      property_id,
      question,
      answer,
      mode: "raw_data",
      latency_ms,
      input_tokens:
        usage.input_tokens +
        (usage.cache_creation_input_tokens ?? 0) +
        (usage.cache_read_input_tokens ?? 0),
      output_tokens: usage.output_tokens,
    });

    if (insertErr) {
      console.error("Insert query failed:", insertErr);
    }

    return new Response(
      JSON.stringify({
        answer,
        latency_ms,
        input_tokens: usage.input_tokens,
        output_tokens: usage.output_tokens,
        cache_creation_input_tokens: usage.cache_creation_input_tokens ?? 0,
        cache_read_input_tokens: usage.cache_read_input_tokens ?? 0,
        bundle_chars: bundle.length,
      }),
      {
        headers: { ...corsHeaders, "Content-Type": "application/json" },
        status: 200,
      }
    );
  } catch (err) {
    console.error("answer_question_raw error:", err);
    return new Response(
      JSON.stringify({ error: (err as Error).message }),
      { status: 500, headers: { ...corsHeaders, "Content-Type": "application/json" } }
    );
  }
});
```

---

## 4. Frontend: pass `property_id` (text) to the Edge Function, not the row UUID

The Edge Function looks up by the text `property_id` ("LIE-001"). Right now
`PropertyDetail.tsx` passes the row's UUID `id`, which after the migration
won't match anything.

### `src/pages/PropertyDetail.tsx` — change

Update the `Property` type, the SELECT, and the `AskModal` prop:

```ts
type Property = {
  id: string;
  property_id: string;          // NEW
  name: string;
  address: string;
  last_run_at: string | null;
};

// inside useEffect:
supabase
  .from("properties")
  .select("id, property_id, name, address, last_run_at")   // add property_id
  .eq("id", id)
  .maybeSingle()

// in the JSX:
<AskModal
  open={open}
  onOpenChange={setOpen}
  propertyId={property.property_id}    // was: property.id
/>
```

`AskModal.tsx` and `Index.tsx` need no changes.

---

## 5. Regenerate Supabase TypeScript types

After the migration applies, regenerate `src/integrations/supabase/types.ts`
so it picks up the new `property_id` column on `properties` and the new
`mode / input_tokens / output_tokens` columns on `queries`.

If your tooling doesn't auto-regenerate, the relevant blocks should be:

```ts
properties: {
  Row: {
    address: string | null
    context_md: string | null
    id: string
    last_run_at: string | null
    name: string | null
    property_id: string
  }
  // Insert + Update follow the same shape, with property_id required on Insert.
  // Relationships: []
}

queries: {
  Row: {
    answer: string | null
    created_at: string
    id: string
    input_tokens: number | null
    latency_ms: number | null
    mode: string | null
    output_tokens: number | null
    property_id: string
    question: string
  }
  // FK: queries_property_id_fkey → properties.property_id
}

context_updates: {
  // FK: context_updates_property_id_fkey → properties.property_id
}
```

All FKs should reference `properties.property_id` (text), not `properties.id`
(uuid).

---

## 6. Required Supabase secrets

Set on the Supabase project (Settings → Edge Functions → Secrets):

| Secret | Value |
|---|---|
| `ANTHROPIC_API_KEY` | Anthropic console key (sk-ant-...) |

`SUPABASE_URL` and `SUPABASE_SERVICE_ROLE_KEY` are auto-injected by Supabase
into Edge Functions — don't set them manually.

---

## 7. After deploy — what to expect

- The seed row `LIE-001` is visible in `properties` with placeholder `context_md`.
- The Python engine (`python run.py raw/`, separate repo) will overwrite that
  row with the real rendered `context.md` once the engineer runs it locally
  with the service-role key in their `.env`.
- `answer_question` works as soon as `context_md` is populated.
- `answer_question_raw` requires a one-time Python upload of `raw_bundle.txt`
  to Storage; will return 404 with a helpful message until then.

---

## Summary of files touched

```
supabase/migrations/20260425150935_*.sql                    REPLACED
supabase/functions/answer_question/index.ts                 REPLACED
supabase/functions/answer_question_raw/index.ts             NEW
src/pages/PropertyDetail.tsx                                MODIFIED
src/integrations/supabase/types.ts                          REGENERATE (auto)
```

Storage bucket `raw-uploads` is created by the migration (private).

No changes to: `Index.tsx`, `AskModal.tsx`, routing, Tailwind config,
`package.json`. Bun lockfile may update if Lovable bumps deps — that's fine.
