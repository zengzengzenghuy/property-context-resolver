# context.unit.<!-- auto:unit_id -->EH-009<!-- /auto:unit_id -->.md

> Per-unit dossier (one file per Einheit). Holds everything specific to this unit:
> the unit itself, the active lease, the tenant(s), and all unit/tenant-specific operations.
> **Property-wide data lives in `context.property.md`** — see `parent_property_ref` below.

<!-- auto:meta -->
- last_built_at: `2026-04-25T20:04:22+00:00`
- build_hash: `engine-v2`
- engine_version: `0.2.0`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `unit`
- parent_property_ref: `context.property.LIE-001.md`
- owner_ref: `EIG-014`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit -->
- unit_id: `EH-009`
- label: WE 09
- haus_id: `HAUS-12`
- floor: 3. OG
- position: rechts
- typ: Wohnung
- area_sqm: 67.0
- rooms: 2.0
- mea_‰: 156
- equipment: _(no data in source yet)_
- media_supply: _(no data in source yet)_
- key_inventory: _(no data in source yet)_
- meters: _(no data in source yet)_
- occupancy_status: `vacant`
- nk_keys: _(no data in source yet)_
<!-- /auto:unit -->

---

## 2. Lease (Mietverhältnis, voll)
<!-- auto:lease -->
- lease_id: `LEASE-MIE-024`
- unit_ref: `EH-009`
- start_date: 2020-10-30 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-024)
- end_date: 2026-02-27 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-024)
- term_type: `befristet`
- cancellation_status: `by_tenant` (notice_date: 2025-08-27, move_out_date: —)
- rent_components: { kaltmiete: 1139.0, betriebskosten_vorauszahlung: 191.0, total_warmmiete: 1330.00 }
- payment_mode: Überweisung
- iban_payer: DE22100700008569847896 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-024)
- kaution: { amount: 3417.0 }
- usage: `residential`
- subletting: { current_status: `requested` }
- special_agreements: _(no data in source yet)_
<!-- /auto:lease -->

### 2.1 Tenants on this Lease
<!-- auto:tenants -->
| tenant_id | name | role | contact_email | contact_phone | comms_pref | gesamtschuldner |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-024` | Frau Anette Vogt | haupt | anette.vogt@gmx.de | (08470) 07661 | email | — |
<!-- /auto:tenants -->

---

## 3. Operations (this unit / this tenant)

### 3.1 Open Tickets — Critical (overdue or due ≤7 days)
<!-- auto:tickets.critical -->
| ticket_id | type | title | deadline | status | assignee |
| --- | --- | --- | --- | --- | --- |
| `TKT-d15e7414` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-25b4f450` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-9a27d9cc` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-cd31b695` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-5436abe0` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-b77f737c` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-966d950b` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-03f741e3` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-535b07f7` | schimmel | Schimmel im Schlafzimmer | — | open | — |
<!-- /auto:tickets.critical -->

### 3.2 Open Tickets — Aggregate
<!-- auto:tickets.aggregate -->
- total_open: `18`
- by_type: { abfluss: `7`, fenster: `1`, schimmel: `7`, schluessel: `1`, wasserschaden: `2` }
- live source: `db.tickets WHERE unit_id=EH-009 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren (per claim)
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
_(no data in source yet)_
- live balance pointer: `db.tenant_balance.tenant_id=MIE-024`
<!-- /auto:dunning -->

### 3.4 Active Reductions / Deferrals (§ 536 BGB)
<!-- auto:reductions -->
- date_raised: 2025-06-06
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-06-09
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-06-09
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-11-09
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- *trigger: HITL exit if any entry present*
<!-- /auto:reductions -->

### 3.5 Latest Übergabeprotokoll
<!-- auto:handover -->_(no data in source yet)_<!-- /auto:handover -->

### 3.6 Recurring Process State (this unit, in-flight)
<!-- auto:recurring -->
| process_type | started | current_step | owner | eta | blockers |
| --- | --- | --- | --- | --- | --- |
| Mieterwechsel | 2025-08-27 | Kündigung erhalten | Verwaltung | TBD | Übergabe-Termin offen |
<!-- /auto:recurring -->

### 3.7 Vermietungs-Pipeline *(if vacant)*
<!-- auto:vermietung -->
- inserate_url: _(no data in source yet)_
- days_on_market: _(no data in source yet)_
- asking_kaltmiete: _(no data in source yet)_
- prospects_count: _(no data in source yet)_
- scheduled_viewings_count: _(no data in source yet)_
- applications_received_count: _(no data in source yet)_
- shortlist: _(no data in source yet)_
<!-- /auto:vermietung -->

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
| `TH-0f8898` | Haustuer schliesst nicht | 2025-12-31 | `MIE-024` | active | 114 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251231_164200_EMAIL-06544.eml) |
| `TH-6c1326` | Schimmel im Schlafzimmer | 2025-12-23 | `MIE-024` | active | 110 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251223_194700_EMAIL-06478.eml) |
| `TH-d0b327` | Wohnungsuebergabe | 2025-12-28 | `MIE-024` | active | 103 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251228_151200_EMAIL-06508.eml) |
| `TH-ffc778` | Verkaufsabsicht WE 09 | 2025-01-19 | `EH-009` | active | 6 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250119_072800_EMAIL-03514.eml) |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `kontoauszug_2024_2025-csv` | bank | [bank/kontoauszug_2024_2025.csv](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv) | 2025-12-03 |
| `20240318_135600_EMAIL-00675-eml` | email | [emails/2024-03/20240318_135600_EMAIL-00675.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240318_135600_EMAIL-00675.eml) | 2024-03-18T13:56:00+00:00 |
| `20240318_205600_EMAIL-00680-eml` | email | [emails/2024-03/20240318_205600_EMAIL-00680.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240318_205600_EMAIL-00680.eml) | 2024-03-18T20:56:00+00:00 |
| `20240320_164900_EMAIL-00692-eml` | email | [emails/2024-03/20240320_164900_EMAIL-00692.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240320_164900_EMAIL-00692.eml) | 2024-03-20T16:49:00+00:00 |
| `20240329_105900_EMAIL-00761-eml` | email | [emails/2024-03/20240329_105900_EMAIL-00761.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240329_105900_EMAIL-00761.eml) | 2024-03-29T10:59:00+00:00 |
| `20240504_103800_EMAIL-01115-eml` | email | [emails/2024-05/20240504_103800_EMAIL-01115.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240504_103800_EMAIL-01115.eml) | 2024-05-04T10:38:00+00:00 |
| `20240516_142300_EMAIL-01235-eml` | email | [emails/2024-05/20240516_142300_EMAIL-01235.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240516_142300_EMAIL-01235.eml) | 2024-05-16T14:23:00+00:00 |
| `20240604_105700_EMAIL-01401-eml` | email | [emails/2024-06/20240604_105700_EMAIL-01401.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240604_105700_EMAIL-01401.eml) | 2024-06-04T10:57:00+00:00 |
| `20240702_123900_EMAIL-01640-eml` | email | [emails/2024-07/20240702_123900_EMAIL-01640.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240702_123900_EMAIL-01640.eml) | 2024-07-02T12:39:00+00:00 |
| `20240821_164300_EMAIL-02115-eml` | email | [emails/2024-08/20240821_164300_EMAIL-02115.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240821_164300_EMAIL-02115.eml) | 2024-08-21T16:43:00+00:00 |
| `20240831_121500_EMAIL-02203-eml` | email | [emails/2024-08/20240831_121500_EMAIL-02203.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240831_121500_EMAIL-02203.eml) | 2024-08-31T12:15:00+00:00 |
| `20241031_151400_EMAIL-02777-eml` | email | [emails/2024-10/20241031_151400_EMAIL-02777.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241031_151400_EMAIL-02777.eml) | 2024-10-31T15:14:00+00:00 |
| `20241108_130000_EMAIL-02845-eml` | email | [emails/2024-11/20241108_130000_EMAIL-02845.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241108_130000_EMAIL-02845.eml) | 2024-11-08T13:00:00+00:00 |
| `20241123_174700_EMAIL-02993-eml` | email | [emails/2024-11/20241123_174700_EMAIL-02993.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241123_174700_EMAIL-02993.eml) | 2024-11-23T17:47:00+00:00 |
| `20241128_142600_EMAIL-03032-eml` | email | [emails/2024-11/20241128_142600_EMAIL-03032.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241128_142600_EMAIL-03032.eml) | 2024-11-28T14:26:00+00:00 |
| `20241201_144900_EMAIL-03059-eml` | email | [emails/2024-12/20241201_144900_EMAIL-03059.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241201_144900_EMAIL-03059.eml) | 2024-12-01T14:49:00+00:00 |
| `20241202_115500_EMAIL-03068-eml` | email | [emails/2024-12/20241202_115500_EMAIL-03068.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241202_115500_EMAIL-03068.eml) | 2024-12-02T11:55:00+00:00 |
| `20241204_143700_EMAIL-03083-eml` | email | [emails/2024-12/20241204_143700_EMAIL-03083.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241204_143700_EMAIL-03083.eml) | 2024-12-04T14:37:00+00:00 |
| `20241206_095400_EMAIL-03101-eml` | email | [emails/2024-12/20241206_095400_EMAIL-03101.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241206_095400_EMAIL-03101.eml) | 2024-12-06T09:54:00+00:00 |
| `20241208_083500_EMAIL-03120-eml` | email | [emails/2024-12/20241208_083500_EMAIL-03120.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241208_083500_EMAIL-03120.eml) | 2024-12-08T08:35:00+00:00 |
| `20241209_164200_EMAIL-03135-eml` | email | [emails/2024-12/20241209_164200_EMAIL-03135.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241209_164200_EMAIL-03135.eml) | 2024-12-09T16:42:00+00:00 |
| `20241211_084200_EMAIL-03145-eml` | email | [emails/2024-12/20241211_084200_EMAIL-03145.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241211_084200_EMAIL-03145.eml) | 2024-12-11T08:42:00+00:00 |
| `20241215_144800_EMAIL-03183-eml` | email | [emails/2024-12/20241215_144800_EMAIL-03183.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241215_144800_EMAIL-03183.eml) | 2024-12-15T14:48:00+00:00 |
| `20241230_113800_EMAIL-03311-eml` | email | [emails/2024-12/20241230_113800_EMAIL-03311.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241230_113800_EMAIL-03311.eml) | 2024-12-30T11:38:00+00:00 |
| `20241231_173800_EMAIL-03337-eml` | email | [emails/2024-12/20241231_173800_EMAIL-03337.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241231_173800_EMAIL-03337.eml) | 2024-12-31T17:38:00+00:00 |
| `20250104_140000_EMAIL-03376-eml` | email | [emails/2025-01/20250104_140000_EMAIL-03376.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250104_140000_EMAIL-03376.eml) | 2025-01-04T14:00:00+00:00 |
| `20250107_173800_EMAIL-03409-eml` | email | [emails/2025-01/20250107_173800_EMAIL-03409.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250107_173800_EMAIL-03409.eml) | 2025-01-07T17:38:00+00:00 |
| `20250119_072800_EMAIL-03514-eml` | email | [emails/2025-01/20250119_072800_EMAIL-03514.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250119_072800_EMAIL-03514.eml) | 2025-01-19T07:28:00+00:00 |
| `20250128_101200_EMAIL-03580-eml` | email | [emails/2025-01/20250128_101200_EMAIL-03580.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250128_101200_EMAIL-03580.eml) | 2025-01-28T10:12:00+00:00 |
| `20250224_124900_EMAIL-03834-eml` | email | [emails/2025-02/20250224_124900_EMAIL-03834.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250224_124900_EMAIL-03834.eml) | 2025-02-24T12:49:00+00:00 |
| `20250227_114700_EMAIL-03868-eml` | email | [emails/2025-02/20250227_114700_EMAIL-03868.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250227_114700_EMAIL-03868.eml) | 2025-02-27T11:47:00+00:00 |
| `20250315_153600_EMAIL-04024-eml` | email | [emails/2025-03/20250315_153600_EMAIL-04024.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250315_153600_EMAIL-04024.eml) | 2025-03-15T15:36:00+00:00 |
| `20250325_151000_EMAIL-04118-eml` | email | [emails/2025-03/20250325_151000_EMAIL-04118.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250325_151000_EMAIL-04118.eml) | 2025-03-25T15:10:00+00:00 |
| `20250401_092100_EMAIL-04176-eml` | email | [emails/2025-04/20250401_092100_EMAIL-04176.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250401_092100_EMAIL-04176.eml) | 2025-04-01T09:21:00+00:00 |
| `20250406_154700_EMAIL-04224-eml` | email | [emails/2025-04/20250406_154700_EMAIL-04224.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250406_154700_EMAIL-04224.eml) | 2025-04-06T15:47:00+00:00 |
| `20250413_105600_EMAIL-04280-eml` | email | [emails/2025-04/20250413_105600_EMAIL-04280.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250413_105600_EMAIL-04280.eml) | 2025-04-13T10:56:00+00:00 |
| `20250413_171500_EMAIL-04283-eml` | email | [emails/2025-04/20250413_171500_EMAIL-04283.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250413_171500_EMAIL-04283.eml) | 2025-04-13T17:15:00+00:00 |
| `20250414_121500_EMAIL-04287-eml` | email | [emails/2025-04/20250414_121500_EMAIL-04287.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250414_121500_EMAIL-04287.eml) | 2025-04-14T12:15:00+00:00 |
| `20250417_142000_EMAIL-04314-eml` | email | [emails/2025-04/20250417_142000_EMAIL-04314.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250417_142000_EMAIL-04314.eml) | 2025-04-17T14:20:00+00:00 |
| `20250505_161300_EMAIL-04441-eml` | email | [emails/2025-05/20250505_161300_EMAIL-04441.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250505_161300_EMAIL-04441.eml) | 2025-05-05T16:13:00+00:00 |
| `20250510_163800_EMAIL-04478-eml` | email | [emails/2025-05/20250510_163800_EMAIL-04478.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250510_163800_EMAIL-04478.eml) | 2025-05-10T16:38:00+00:00 |
| `20250516_175000_EMAIL-04536-eml` | email | [emails/2025-05/20250516_175000_EMAIL-04536.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250516_175000_EMAIL-04536.eml) | 2025-05-16T17:50:00+00:00 |
| `20250528_094200_EMAIL-04641-eml` | email | [emails/2025-05/20250528_094200_EMAIL-04641.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250528_094200_EMAIL-04641.eml) | 2025-05-28T09:42:00+00:00 |
| `20250606_154600_EMAIL-04711-eml` | email | [emails/2025-06/20250606_154600_EMAIL-04711.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250606_154600_EMAIL-04711.eml) | 2025-06-06T15:46:00+00:00 |
| `20250609_112400_EMAIL-04726-eml` | email | [emails/2025-06/20250609_112400_EMAIL-04726.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250609_112400_EMAIL-04726.eml) | 2025-06-09T11:24:00+00:00 |
| `20250609_142400_EMAIL-04729-eml` | email | [emails/2025-06/20250609_142400_EMAIL-04729.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250609_142400_EMAIL-04729.eml) | 2025-06-09T14:24:00+00:00 |
| `20250624_114800_EMAIL-04862-eml` | email | [emails/2025-06/20250624_114800_EMAIL-04862.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250624_114800_EMAIL-04862.eml) | 2025-06-24T11:48:00+00:00 |
| `20250718_141000_EMAIL-05073-eml` | email | [emails/2025-07/20250718_141000_EMAIL-05073.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250718_141000_EMAIL-05073.eml) | 2025-07-18T14:10:00+00:00 |
| `20250803_165900_EMAIL-05196-eml` | email | [emails/2025-08/20250803_165900_EMAIL-05196.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250803_165900_EMAIL-05196.eml) | 2025-08-03T16:59:00+00:00 |
| `20250808_154800_EMAIL-05225-eml` | email | [emails/2025-08/20250808_154800_EMAIL-05225.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250808_154800_EMAIL-05225.eml) | 2025-08-08T15:48:00+00:00 |
| `20250827_173700_EMAIL-05422-eml` | email | [emails/2025-08/20250827_173700_EMAIL-05422.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250827_173700_EMAIL-05422.eml) | 2025-08-27T17:37:00+00:00 |
| `20250829_043700_EMAIL-05435-eml` | email | [emails/2025-08/20250829_043700_EMAIL-05435.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250829_043700_EMAIL-05435.eml) | 2025-08-29T04:37:00+00:00 |
| `20250907_171900_EMAIL-05562-eml` | email | [emails/2025-09/20250907_171900_EMAIL-05562.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250907_171900_EMAIL-05562.eml) | 2025-09-07T17:19:00+00:00 |
| `20250922_104000_EMAIL-05687-eml` | email | [emails/2025-09/20250922_104000_EMAIL-05687.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250922_104000_EMAIL-05687.eml) | 2025-09-22T10:40:00+00:00 |
| `20251014_141600_EMAIL-05880-eml` | email | [emails/2025-10/20251014_141600_EMAIL-05880.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251014_141600_EMAIL-05880.eml) | 2025-10-14T14:16:00+00:00 |
| `20251015_110100_EMAIL-05886-eml` | email | [emails/2025-10/20251015_110100_EMAIL-05886.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251015_110100_EMAIL-05886.eml) | 2025-10-15T11:01:00+00:00 |
| `20251018_110000_EMAIL-05904-eml` | email | [emails/2025-10/20251018_110000_EMAIL-05904.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251018_110000_EMAIL-05904.eml) | 2025-10-18T11:00:00+00:00 |
| `20251021_130400_EMAIL-05926-eml` | email | [emails/2025-10/20251021_130400_EMAIL-05926.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251021_130400_EMAIL-05926.eml) | 2025-10-21T13:04:00+00:00 |
| `20251106_105400_EMAIL-06060-eml` | email | [emails/2025-11/20251106_105400_EMAIL-06060.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251106_105400_EMAIL-06060.eml) | 2025-11-06T10:54:00+00:00 |
| `20251106_124800_EMAIL-06062-eml` | email | [emails/2025-11/20251106_124800_EMAIL-06062.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251106_124800_EMAIL-06062.eml) | 2025-11-06T12:48:00+00:00 |
| `20251106_182900_EMAIL-06068-eml` | email | [emails/2025-11/20251106_182900_EMAIL-06068.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251106_182900_EMAIL-06068.eml) | 2025-11-06T18:29:00+00:00 |
| `20251109_130100_EMAIL-06086-eml` | email | [emails/2025-11/20251109_130100_EMAIL-06086.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251109_130100_EMAIL-06086.eml) | 2025-11-09T13:01:00+00:00 |
| `20251118_114100_EMAIL-06153-eml` | email | [emails/2025-11/20251118_114100_EMAIL-06153.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251118_114100_EMAIL-06153.eml) | 2025-11-18T11:41:00+00:00 |
| `20251122_112300_EMAIL-06188-eml` | email | [emails/2025-11/20251122_112300_EMAIL-06188.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251122_112300_EMAIL-06188.eml) | 2025-11-22T11:23:00+00:00 |
| `20251123_152300_EMAIL-06208-eml` | email | [emails/2025-11/20251123_152300_EMAIL-06208.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251123_152300_EMAIL-06208.eml) | 2025-11-23T15:23:00+00:00 |
| `20251125_151400_EMAIL-06223-eml` | email | [emails/2025-11/20251125_151400_EMAIL-06223.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251125_151400_EMAIL-06223.eml) | 2025-11-25T15:14:00+00:00 |
| `20251130_102900_EMAIL-06266-eml` | email | [emails/2025-11/20251130_102900_EMAIL-06266.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251130_102900_EMAIL-06266.eml) | 2025-11-30T10:29:00+00:00 |
| `20251201_165600_EMAIL-06277-eml` | email | [emails/2025-12/20251201_165600_EMAIL-06277.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251201_165600_EMAIL-06277.eml) | 2025-12-01T16:56:00+00:00 |
| `20251206_124000_EMAIL-06314-eml` | email | [emails/2025-12/20251206_124000_EMAIL-06314.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251206_124000_EMAIL-06314.eml) | 2025-12-06T12:40:00+00:00 |
| `20251223_194700_EMAIL-06478-eml` | email | [emails/2025-12/20251223_194700_EMAIL-06478.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251223_194700_EMAIL-06478.eml) | 2025-12-23 |
| `20251228_151200_EMAIL-06508-eml` | email | [emails/2025-12/20251228_151200_EMAIL-06508.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251228_151200_EMAIL-06508.eml) | 2025-12-28 |
| `20251230_144800_EMAIL-06532-eml` | email | [emails/2025-12/20251230_144800_EMAIL-06532.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251230_144800_EMAIL-06532.eml) | 2025-12-30T14:48:00+00:00 |
| `20251231_164200_EMAIL-06544-eml` | email | [emails/2025-12/20251231_164200_EMAIL-06544.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251231_164200_EMAIL-06544.eml) | 2025-12-31 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-25T20:04:11+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
