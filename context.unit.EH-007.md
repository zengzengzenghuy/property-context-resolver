# context.unit.<!-- auto:unit_id -->EH-007<!-- /auto:unit_id -->.md

> Per-unit dossier (one file per Einheit). Holds everything specific to this unit:
> the unit itself, the active lease, the tenant(s), and all unit/tenant-specific operations.
> **Property-wide data lives in `context.property.md`** — see `parent_property_ref` below.

<!-- auto:meta -->
- last_built_at: `2026-04-25T20:52:26+00:00`
- build_hash: `engine-v2`
- engine_version: `0.2.0`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `unit`
- unit_id: `EH-007`
- property_id: `LIE-001`
- parent_property_ref: `context.property.LIE-001.md`
- owner_ref: `EIG-005`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit -->
- unit_id: `EH-007`
- label: WE 07
- haus_id: `HAUS-12`
- floor: 3. OG
- position: links
- typ: Wohnung
- area_sqm: 45.0
- rooms: 1.5
- mea_‰: 104
- equipment: _(no data in source yet)_
- media_supply: _(no data in source yet)_
- key_inventory: _(no data in source yet)_
- meters: _(no data in source yet)_
- occupancy_status: `own-use`
- nk_keys: _(no data in source yet)_
<!-- /auto:unit -->

---

## 2. Lease (Mietverhältnis, voll)
<!-- auto:lease -->_(no data in source yet)_<!-- /auto:lease -->

### 2.1 Tenants on this Lease
<!-- auto:tenants -->
| tenant_id | name | role | contact_email | contact_phone | comms_pref | gesamtschuldner |
| --- | --- | --- | --- | --- | --- | --- |
_(no data in source yet)_
<!-- /auto:tenants -->

---

## 3. Operations (this unit / this tenant)

### 3.1 Open Tickets — Critical (overdue or due ≤7 days)
<!-- auto:tickets.critical -->
| ticket_id | type | title | deadline | status | assignee |
| --- | --- | --- | --- | --- | --- |
_(no data in source yet)_
<!-- /auto:tickets.critical -->

### 3.2 Open Tickets — Aggregate
<!-- auto:tickets.aggregate -->
- total_open: `1`
- by_type: { schluessel: `1` }
- live source: `db.tickets WHERE unit_id=EH-007 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren

<!-- auto:dunning.summary -->_no issue_<!-- /auto:dunning.summary -->

#### Per claim
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
_(no data in source yet)_
- live balance pointer: `db.tenant_balance.tenant_id=EH-007`
<!-- /auto:dunning -->

### 3.4 Active Reductions / Deferrals (§ 536 BGB)
<!-- auto:reductions -->_(no data in source yet)_<!-- /auto:reductions -->

### 3.5 Latest Übergabeprotokoll
<!-- auto:handover -->_(no data in source yet)_<!-- /auto:handover -->

### 3.6 Recurring Process State (this unit, in-flight)
<!-- auto:recurring -->
| process_type | started | current_step | owner | eta | blockers |
| --- | --- | --- | --- | --- | --- |
_(no data in source yet)_
<!-- /auto:recurring -->

### 3.7 Vermietungs-Pipeline *(if vacant)*
<!-- auto:vermietung -->_Not yet activated. Triggers when occupancy_status flips to vacant after move-out._<!-- /auto:vermietung -->

---

## 4. Decisions & History (this unit / this tenant)

### 4.1 Tenant Special Agreements
<!-- auto:tenant-agreements -->
| date | type | one-line | doc_ref |
| --- | --- | --- | --- |
_(no data in source yet)_
<!-- /auto:tenant-agreements -->

### 4.2 Modernisierungs-Maßnahmen (this unit)
<!-- auto:modernization-unit -->
| date_completed | scope | umlage_per_year | rent_increase_per_month | tenant_opted_out |
| --- | --- | --- | --- | --- |
_(no data in source yet)_
<!-- /auto:modernization-unit -->

### 4.3 Sticky Communication Threads (this tenant)
<!-- auto:sticky-threads -->
| thread_id | subject | last_msg_date | parties | status | one-line outcome | pointer |
| --- | --- | --- | --- | --- | --- | --- |
| `TH-3f79c8` | Verkaufsabsicht WE 07 | 2025-12-12 | `EH-007` | active | 6 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251212_144300_EMAIL-06366.eml) |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `kontoauszug_2024_2025-csv` | bank | [bank/kontoauszug_2024_2025.csv](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv) | 2025-12-05 |
| `20241105_053900_EMAIL-02819-eml` | email | [emails/2024-11/20241105_053900_EMAIL-02819.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241105_053900_EMAIL-02819.eml) | 2024-11-05T05:39:00+00:00 |
| `20250614_024300_EMAIL-04769-eml` | email | [emails/2025-06/20250614_024300_EMAIL-04769.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250614_024300_EMAIL-04769.eml) | 2025-06-14T02:43:00+00:00 |
| `20251122_112300_EMAIL-06188-eml` | email | [emails/2025-11/20251122_112300_EMAIL-06188.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251122_112300_EMAIL-06188.eml) | 2025-11-22T11:23:00+00:00 |
| `20251212_144300_EMAIL-06366-eml` | email | [emails/2025-12/20251212_144300_EMAIL-06366.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251212_144300_EMAIL-06366.eml) | 2025-12-12 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-25T20:52:09+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
