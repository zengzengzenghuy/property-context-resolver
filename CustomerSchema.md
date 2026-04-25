# Customer Schema

Reference doc for the **Customer** entity in `property-context-resolver`.
"Customer" here = **Mieter** (tenant) — the human paying rent on a unit
inside `LIE-001` (WEG Immanuelkirchstraße 26, Berlin). Owners
(Eigentümer) and service providers (Dienstleister) are separate entities
and are NOT customers.

This file has two sections:
1. **Required customer fields** — the canonical columns that need to live
   in the database to support the queries the property manager runs.
2. **Raw data fields** — what each folder under `raw/` carries and how
   those fields feed (or don't) the customer record above.

---

## 1. Required Customer Fields (DB-facing)

These are the fields that must be queryable per customer. Each row models a
single tenant. `customer_id` (= `mieter_id`) is the primary key. Anything not
in this list is either derivable, time-series (kept in a child table), or
unstructured context that lives in `context.md` rather than the DB.

### 1.1 Identity

| Field | Type | Source(s) | Notes |
|---|---|---|---|
| `customer_id` | string PK | stammdaten/mieter.csv `id` | Format `MIE-###`. Stable canonical id; used by `IdentityResolver`. |
| `property_id` | string FK | hard-coded `LIE-001` | Single property in v1. |
| `unit_id` | string FK | mieter.csv `einheit_id` | `EH-###`. Joins to `einheiten`. |
| `salutation` | enum(`Herr`,`Frau`) | mieter.csv `anrede` | Used in correspondence. |
| `first_name` | string | mieter.csv `vorname` | |
| `last_name` | string | mieter.csv `nachname` | Fuzzy match key — `IdentityResolver` uses 0.86 threshold (umlaut variants exist). |
| `language` | ISO-639-1 | mieter.csv `sprache` | Default `de`. Drives template choice for letters. |

### 1.2 Contact (strong identity signals — used by IdentityResolver)

| Field | Type | Source(s) | Notes |
|---|---|---|---|
| `email` | string | mieter.csv `email`; email `From:` headers | Lowercased + stripped on dedup. Strong identity signal. |
| `phone` | string | mieter.csv `telefon` | Free-text format in source; normalize on ingest. |

### 1.3 Lease / contract (scalar — render in context.md)

| Field | Type | Source(s) | Notes |
|---|---|---|---|
| `lease_start` | date | mieter.csv `mietbeginn` | ISO `YYYY-MM-DD`. |
| `lease_end` | date \| null | mieter.csv `mietende` | Null = open-ended. |
| `kaltmiete_eur` | decimal(10,2) | mieter.csv `kaltmiete` | Base rent. Conflict-detected as scalar. |
| `nk_vorauszahlung_eur` | decimal(10,2) | mieter.csv `nk_vorauszahlung` | Operating-cost prepayment. |
| `kaution_eur` | decimal(10,2) | mieter.csv `kaution` | Security deposit. |
| `owner_id` | string FK | mieter.csv `eigentuemer_id` | `EIG-###`. Links to landlord side. |

### 1.4 Banking (strong identity signal)

| Field | Type | Source(s) | Notes |
|---|---|---|---|
| `iban` | string | mieter.csv `iban`; bank CSV `Kontonummer/IBAN` for incoming credits | Strong identity signal. Resolves payments → tenant when name match is ambiguous. |
| `bic` | string | mieter.csv `bic` | |

### 1.5 Time-series (separate child tables — DO NOT collapse into customer row)

These belong in joined tables keyed by `(customer_id, period)`. They legitimately
change every month and would trigger false `<!-- conflict -->` markers if stored
as scalars. The engine's `SCALAR_KEYS` allowlist explicitly excludes these.

| Table | Key fields | Source | Notes |
|---|---|---|---|
| `payments` | `tx_id`, `customer_id`, `amount_eur`, `direction`, `period`, `verwendungszweck`, `counterparty_iban` | bank CSV + bank_index.csv | One row per Sparkasse line. `period` parsed from "Miete MM/YYYY" pattern. |
| `dunning` | `customer_id`, `letter_id`, `invoice_ref`, `offener_betrag_eur`, `letter_date` | briefe/*.pdf (Mahnung) | Surfaces overdue balances. |
| `communications` | `customer_id`, `event_id`, `from`, `subject`, `intent`, `received_at` | emails/*.eml | Intent comes from `_INTENT_PATTERNS` classifier. |

### 1.6 Provenance (required on every fact, mirrored on every table row)

| Field | Type | Notes |
|---|---|---|
| `source_event_id` | string | Hash id of the originating Event. |
| `source_ref` | URL | GitHub blob URL with optional fragment. |
| `confidence` | float [0,1] | Stammdaten/bank = 1.0; subject regex = 0.85; body sniffing = 0.6–0.7. |
| `observed_at` | timestamp \| null | When the fact happened (e.g. email date). Null for stammdaten. |
| `extracted_at` | timestamp | When the engine wrote the row. |

### 1.7 Query patterns this schema needs to support

- "Show all overdue tenants" → join `customers` × `payments` × `dunning`.
- "Who lives in EH-025?" → `customers WHERE unit_id = ?`.
- "Resolve sender `julius.nette@outlook.com` to a customer" → `customers WHERE email = ?` (then fall back to IBAN, einheit_nr, phone, fuzzy name — see `IdentityResolver`).
- "Last 12 months of payments for MIE-001" → `payments WHERE customer_id = ? AND period BETWEEN ?`.
- "Tenants with kaltmiete > 1500 EUR" → scalar lookup on `customers`.
- "All correspondence with a tenant in 2024" → `communications WHERE customer_id = ?`.

---

## 2. Raw Data Fields (engineer-facing)

This section maps the on-disk corpus under `raw/` to the fields they
contribute. Use it when wiring a new connector or debugging why a field
didn't land. **Source priority** for conflicts: `stammdaten=4 >
letter/invoice/bank=3 > email=1`.

### 2.1 `raw/stammdaten/` — canonical master data (priority 4)

Authoritative baseline. Loaded first, gives every customer row its initial
values. JSON is the source of truth; CSVs are projections.

#### `mieter.csv` — **the customer table**
Columns: `id, anrede, vorname, nachname, email, telefon, einheit_id,
eigentuemer_id, mietbeginn, mietende, kaltmiete, nk_vorauszahlung, kaution,
iban, bic, sprache`
→ feeds **all** of section 1.1–1.4 directly. 1:1 mapping.

#### `einheiten.csv` — units (joined via `customer.unit_id`)
Columns: `id, haus_id, einheit_nr, lage, typ, wohnflaeche_qm, zimmer,
miteigentumsanteil`
→ adds physical context (sqm, floor, room count) to a customer record.
Not stored on the customer row itself; query via join.

#### `eigentuemer.csv` — owners (joined via `customer.owner_id`)
Columns: `id, anrede, vorname, nachname, firma, strasse, plz, ort, land,
email, telefon, iban, bic, einheit_ids, selbstnutzer, sev_mandat, beirat,
sprache`
→ landlord side. Note `selbstnutzer=True` means owner-occupied — those
units have no Mieter record.

#### `dienstleister.csv` — service providers (NOT customers)
Columns: `id, firma, branche, ansprechpartner, email, telefon, strasse,
plz, ort, land, iban, bic, ust_id, steuernummer, stil, sprache,
vertrag_monatlich, stundensatz`
→ vendors (Hausmeister, elevator, etc.). Used to resolve invoice
counterparties; never produces a customer row.

#### `stammdaten.json` — superset
Holds `liegenschaft` (the property itself: address, verwalter info, WEG
bank accounts, Rücklage IBAN) and `gebaeude` (building-level: hausnr,
einheiten count, floors, fahrstuhl, baujahr). Customer rows reference
`property_id` only; the rest is metadata for context.md.

### 2.2 `raw/bank/` — Sparkasse export (priority 3)

#### `kontoauszug_2024_2025.csv` (semicolon-delimited)
Columns: `Auftragskonto, Buchungstag, Valutadatum, Buchungstext,
Verwendungszweck, Glaeubiger-ID, Mandatsreferenz, Kundenreferenz
(End-to-End), Sammlerreferenz, Lastschrift Ursprungsbetrag,
Auslagenersatz Ruecklastschrift, Beguenstigter/Zahlungspflichtiger,
Kontonummer/IBAN, BIC (SWIFT-Code), Betrag, Waehrung, Info`

Maps to **time-series `payments` table**, NOT the customer row. Resolution:
- `Kontonummer/IBAN` → matched against `customers.iban` (strong signal).
- `Beguenstigter/Zahlungspflichtiger` → fuzzy name match if IBAN miss.
- `Verwendungszweck` parsed for `Miete MM/YYYY EH-###` → confirms `unit_id`.
- `Betrag` (German `1.234,56`) → `payment.amount_eur` (float).
- `Buchungstag` (`DD.MM.YYYY`) → `observed_at`.

`bank_index.csv` is a curated companion with pre-resolved `referenz_id`
(MIE-### or EIG-### or DL-###) and `error_types` flags.
`kontoauszug_2024_2025.camt053.xml` is the same data in CAMT.053 format —
keep as alternate ingest path.

### 2.3 `raw/emails/YYYY-MM/*.eml` — correspondence (priority 1)

Standard RFC-822 headers used for the customer record:
- `From:` → resolves to a customer via email lookup. Strong signal.
- `Date:` → `communication.received_at` / `observed_at`.
- `Subject:` → fed to `_INTENT_PATTERNS` regex classifier
  (Mahnung, ETV-Einladung, Rechnung, Betriebskostenabrechnung, etc.) →
  `communication.intent`.
- Body → optional rule-based amount/IBAN sniffing at confidence 0.6–0.7.
  Watch out: `quoted-printable` encoding leaks (`R=C3=B6hricht` ↔
  `Röhricht`) — extractors must handle both.

Output: rows in the **`communications` table**, never updates the customer
scalar fields (priority too low to overwrite stammdaten).

### 2.4 `raw/briefe/YYYY-MM/*.pdf` — outgoing letters (priority 3)

Two letter types so far:
- **Mahnung** (dunning notice): `mahnung.invoice_ref`,
  `mahnung.offener_betrag_eur` → `dunning` table.
- **ETV-Einladung** (annual owner meeting invite): not customer-bound;
  binds to property/owner.

PDFs are pre-OCR'd via `scripts/preocr.py`; the engine reads
`<file>.pdf.txt` siblings. Filename pattern
`YYYYMMDD_<type>_LTR-####.pdf` carries date and letter id.

### 2.5 `raw/rechnungen/YYYY-MM/*.pdf` — vendor invoices (priority 3)

Filename: `YYYYMMDD_DL-###_INV-####.pdf` — the `DL-###` segment is the
vendor (Dienstleister) id. **Invoices target Dienstleister/Liegenschaft,
not customers.** Extracted fields: `rechnung.netto_eur`, `rechnung.ust_eur`,
`rechnung.brutto_eur`, `rechnung.invoice_ref`. Two PDF layouts (inline
vs. tabular column-flatten); use `_extract_totals()` — don't write
per-label regexes.

### 2.6 `raw/lease/*.txt` — lease contracts (priority 3, authoritative on lease terms)

Free-form German lease document. Filename `mietvertrag_MIE-###_<name>.txt`
gives the customer id. Fields the extractor should pull:
- Tenant name, DOB, unit address & einheit_nr → cross-check against
  stammdaten.
- `mietbeginn` (§ 2) → `customer.lease_start`.
- `kaltmiete`, `nk_vorauszahlung`, `heizkosten_vorauszahlung`,
  `stellplatzmiete` (§ 3) → reconcile against `mieter.csv`. Lease wins
  if they diverge on the day the lease was signed.
- Bank account of Vermieter (§ 3) → cross-check `eigentuemer.iban`.

Currently only `MIE-001` has a lease file. Others are stammdaten-only.

### 2.7 `raw/incremental/day-XX/` — delta drops (EXCLUDED by default)

Mirrors the structure of `raw/{bank,emails,rechnungen}` but only the
files that arrived on day `XX`. `incremental_manifest.json` lists the new
files. Loaded only when `run.py --include-incremental` is passed; this is
the fixture for demonstrating surgical updates to `context.md` on a
second run. **Do not include in v1 default ingestion.**

### 2.8 What the raw corpus does NOT carry (and the customer row therefore can't have)

- No date of birth in `mieter.csv` (only in lease text → optional enrichment).
- No previous-address / move-in history.
- No occupancy count / household size.
- No emergency contact / next-of-kin.
- No payment-method preference (everything is SEPA inbound).

If product later wants any of these, plan a manual stammdaten extension
or a lease-text extractor — they will not appear from emails/bank alone.

---

## Cross-reference

- Engine details, conventions, gotchas: `CLAUDE.md`.
- Why this shape (vs. Postgres/vector DB): `Tech Stack.md`.
- Component-by-component build status: `Technical Component.md`.
- Ownership / sprint cadence: `Sprint.md`.
- Output schema (`Event`, `Fact`): `extractor/models.py`.
