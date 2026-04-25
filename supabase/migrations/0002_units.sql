-- spine-v2-split (2026-04-25): per-unit context files.
-- The engine now produces one `context.unit.<EH-XX>.md` per unit on top of
-- the per-property `context.property.<LIE>.md`. Mirror unit files so the
-- agent / Lovable UI can fetch a single unit without scanning the property.

-- units -------------------------------------------------------------------

CREATE TABLE public.units (
  id            UUID NOT NULL DEFAULT gen_random_uuid() PRIMARY KEY,
  unit_id       TEXT NOT NULL UNIQUE,                                 -- e.g. 'EH-019'
  property_id   TEXT NOT NULL REFERENCES public.properties(property_id) ON DELETE CASCADE,
  label         TEXT,                                                 -- e.g. 'WE 19'
  occupancy     TEXT,                                                 -- 'rented' | 'vacant' | 'own-use'
  context_md    TEXT,
  last_run_at   TIMESTAMPTZ
);

CREATE INDEX units_property_idx ON public.units(property_id);

-- context_updates: capture which file was written ----------------------------

ALTER TABLE public.context_updates
  ADD COLUMN unit_id TEXT REFERENCES public.units(unit_id) ON DELETE CASCADE;

CREATE INDEX context_updates_unit_idx ON public.context_updates(unit_id);

-- RLS — public read; writes go via service role (engine).

ALTER TABLE public.units ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Public can read units" ON public.units FOR SELECT USING (true);
