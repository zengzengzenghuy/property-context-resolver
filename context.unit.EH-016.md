# context.unit.<!-- auto:unit_id -->EH-016<!-- /auto:unit_id -->.md

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
- owner_ref: `EIG-013`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit -->
- unit_id: `EH-016`
- label: WE 16
- haus_id: `HAUS-12`
- floor: 5. OG
- position: links
- typ: Wohnung
- area_sqm: 108.0
- rooms: 4.0
- mea_‰: 251
- equipment: _(no data in source yet)_
- media_supply: _(no data in source yet)_
- key_inventory: _(no data in source yet)_
- meters: _(no data in source yet)_
- occupancy_status: `rented`
- nk_keys: _(no data in source yet)_
<!-- /auto:unit -->

---

## 2. Lease (Mietverhältnis, voll)
<!-- auto:lease -->
- lease_id: `LEASE-MIE-011`
- unit_ref: `EH-016`
- start_date: 2024-01-11 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-011)
- end_date: _(no data in source yet)_
- term_type: `unbefristet`
- cancellation_status: `by_tenant` (notice_date: 2025-10-28, move_out_date: —)
- rent_components: { kaltmiete: 1555.0, betriebskosten_vorauszahlung: 308.0, total_warmmiete: 1863.00 }
- payment_mode: Überweisung
- iban_payer: DE91120300008091343161 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-011)
- kaution: { amount: 4665.0 }
- usage: `residential`
- subletting: { current_status: `requested` }
- special_agreements: _(no data in source yet)_
<!-- /auto:lease -->

### 2.1 Tenants on this Lease
<!-- auto:tenants -->
| tenant_id | name | role | contact_email | contact_phone | comms_pref | gesamtschuldner |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-011` | Frau Peggy Hein | haupt | peggy.hein@outlook.com | (05339) 421047 | email | — |
<!-- /auto:tenants -->

---

## 3. Operations (this unit / this tenant)

### 3.1 Open Tickets — Critical (overdue or due ≤7 days)
<!-- auto:tickets.critical -->
| ticket_id | type | title | deadline | status | assignee |
| --- | --- | --- | --- | --- | --- |
| `TKT-de4ca582` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-1f9a0ba8` | wasserschaden | Re: Wasserschaden Bad | — | open | — |
| `TKT-8deb974e` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-5c4b096e` | schimmel | Re: Schimmel im Schlafzimmer | — | open | — |
| `TKT-43217446` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-f9d0409c` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-58109197` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-42c72d93` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-b2e5bc74` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-2e2b3eba` | wasserschaden | Re: Wasserschaden Bad | — | open | — |
| `TKT-2f5c4961` | wasserschaden | Wasserschaden Bad | — | open | — |
<!-- /auto:tickets.critical -->

### 3.2 Open Tickets — Aggregate
<!-- auto:tickets.aggregate -->
- total_open: `23`
- by_type: { abfluss: `7`, fenster: `3`, schimmel: `5`, schluessel: `2`, wasserschaden: `6` }
- live source: `db.tickets WHERE unit_id=EH-016 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren (per claim)
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-011` | — | 1 | 7452.00 EUR | 2025-12-01 | — | — |
- live balance pointer: `db.tenant_balance.tenant_id=MIE-011`
<!-- /auto:dunning -->

### 3.4 Active Reductions / Deferrals (§ 536 BGB)
<!-- auto:reductions -->
- date_raised: 2024-03-04
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-03-05
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-04-17
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-02-07
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-07-15
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-07-17
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-12-13
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-12-15
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
| Mieterwechsel | 2025-10-28 | Kündigung erhalten | Verwaltung | TBD | Übergabe-Termin offen |
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
_(no data in source yet)_
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `kontoauszug_2024_2025-csv` | bank | [bank/kontoauszug_2024_2025.csv](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv) | 2026-04-25 |
| `20240626_mahnung_LTR-0038-pdf` | letter | [briefe/2024-06/20240626_mahnung_LTR-0038.pdf](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/briefe/2024-06/20240626_mahnung_LTR-0038.pdf) | 2024-06-26 |
| `20251208_mahnung_LTR-0135-pdf` | letter | [briefe/2025-12/20251208_mahnung_LTR-0135.pdf](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/briefe/2025-12/20251208_mahnung_LTR-0135.pdf) | 2026-04-25 |
| `20240102_112600_EMAIL-00007-eml` | email | [emails/2024-01/20240102_112600_EMAIL-00007.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240102_112600_EMAIL-00007.eml) | 2024-01-02T11:26:00+00:00 |
| `20240109_140400_EMAIL-00070-eml` | email | [emails/2024-01/20240109_140400_EMAIL-00070.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240109_140400_EMAIL-00070.eml) | 2024-01-09T14:04:00+00:00 |
| `20240304_081500_EMAIL-00542-eml` | email | [emails/2024-03/20240304_081500_EMAIL-00542.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240304_081500_EMAIL-00542.eml) | 2024-03-04T08:15:00+00:00 |
| `20240305_151500_EMAIL-00557-eml` | email | [emails/2024-03/20240305_151500_EMAIL-00557.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240305_151500_EMAIL-00557.eml) | 2024-03-05T15:15:00+00:00 |
| `20240417_130800_EMAIL-00969-eml` | email | [emails/2024-04/20240417_130800_EMAIL-00969.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240417_130800_EMAIL-00969.eml) | 2024-04-17T13:08:00+00:00 |
| `20240426_172300_EMAIL-01048-eml` | email | [emails/2024-04/20240426_172300_EMAIL-01048.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240426_172300_EMAIL-01048.eml) | 2024-04-26T17:23:00+00:00 |
| `20240427_032300_EMAIL-01052-eml` | email | [emails/2024-04/20240427_032300_EMAIL-01052.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240427_032300_EMAIL-01052.eml) | 2024-04-27T03:23:00+00:00 |
| `20240508_153700_EMAIL-01156-eml` | email | [emails/2024-05/20240508_153700_EMAIL-01156.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240508_153700_EMAIL-01156.eml) | 2024-05-08T15:37:00+00:00 |
| `20240509_213700_EMAIL-01167-eml` | email | [emails/2024-05/20240509_213700_EMAIL-01167.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240509_213700_EMAIL-01167.eml) | 2024-05-09T21:37:00+00:00 |
| `20240602_133800_EMAIL-01384-eml` | email | [emails/2024-06/20240602_133800_EMAIL-01384.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240602_133800_EMAIL-01384.eml) | 2024-06-02T13:38:00+00:00 |
| `20240603_203800_EMAIL-01399-eml` | email | [emails/2024-06/20240603_203800_EMAIL-01399.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240603_203800_EMAIL-01399.eml) | 2024-06-03T20:38:00+00:00 |
| `20240614_143700_EMAIL-01497-eml` | email | [emails/2024-06/20240614_143700_EMAIL-01497.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240614_143700_EMAIL-01497.eml) | 2024-06-14T14:37:00+00:00 |
| `20240623_021700_EMAIL-01568-eml` | email | [emails/2024-06/20240623_021700_EMAIL-01568.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240623_021700_EMAIL-01568.eml) | 2024-06-23T02:17:00+00:00 |
| `20240704_102300_EMAIL-01649-eml` | email | [emails/2024-07/20240704_102300_EMAIL-01649.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240704_102300_EMAIL-01649.eml) | 2024-07-04T10:23:00+00:00 |
| `20240814_161000_EMAIL-02041-eml` | email | [emails/2024-08/20240814_161000_EMAIL-02041.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240814_161000_EMAIL-02041.eml) | 2024-08-14T16:10:00+00:00 |
| `20240820_093300_EMAIL-02098-eml` | email | [emails/2024-08/20240820_093300_EMAIL-02098.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240820_093300_EMAIL-02098.eml) | 2024-08-20T09:33:00+00:00 |
| `20240825_142400_EMAIL-02150-eml` | email | [emails/2024-08/20240825_142400_EMAIL-02150.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240825_142400_EMAIL-02150.eml) | 2024-08-25T14:24:00+00:00 |
| `20240826_113400_EMAIL-02160-eml` | email | [emails/2024-08/20240826_113400_EMAIL-02160.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240826_113400_EMAIL-02160.eml) | 2024-08-26T11:34:00+00:00 |
| `20240828_073400_EMAIL-02172-eml` | email | [emails/2024-08/20240828_073400_EMAIL-02172.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240828_073400_EMAIL-02172.eml) | 2024-08-28T07:34:00+00:00 |
| `20241002_151600_EMAIL-02497-eml` | email | [emails/2024-10/20241002_151600_EMAIL-02497.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241002_151600_EMAIL-02497.eml) | 2024-10-02T15:16:00+00:00 |
| `20241023_152000_EMAIL-02700-eml` | email | [emails/2024-10/20241023_152000_EMAIL-02700.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241023_152000_EMAIL-02700.eml) | 2024-10-23T15:20:00+00:00 |
| `20241025_185200_EMAIL-02722-eml` | email | [emails/2024-10/20241025_185200_EMAIL-02722.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241025_185200_EMAIL-02722.eml) | 2024-10-25T18:52:00+00:00 |
| `20241105_161300_EMAIL-02825-eml` | email | [emails/2024-11/20241105_161300_EMAIL-02825.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241105_161300_EMAIL-02825.eml) | 2024-11-05T16:13:00+00:00 |
| `20241106_061300_EMAIL-02828-eml` | email | [emails/2024-11/20241106_061300_EMAIL-02828.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241106_061300_EMAIL-02828.eml) | 2024-11-06T06:13:00+00:00 |
| `20241108_132500_EMAIL-02846-eml` | email | [emails/2024-11/20241108_132500_EMAIL-02846.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241108_132500_EMAIL-02846.eml) | 2024-11-08T13:25:00+00:00 |
| `20241207_104300_EMAIL-03109-eml` | email | [emails/2024-12/20241207_104300_EMAIL-03109.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241207_104300_EMAIL-03109.eml) | 2024-12-07T10:43:00+00:00 |
| `20241218_181300_EMAIL-03206-eml` | email | [emails/2024-12/20241218_181300_EMAIL-03206.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241218_181300_EMAIL-03206.eml) | 2024-12-18T18:13:00+00:00 |
| `20250108_145500_EMAIL-03417-eml` | email | [emails/2025-01/20250108_145500_EMAIL-03417.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250108_145500_EMAIL-03417.eml) | 2025-01-08T14:55:00+00:00 |
| `20250129_130200_EMAIL-03594-eml` | email | [emails/2025-01/20250129_130200_EMAIL-03594.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250129_130200_EMAIL-03594.eml) | 2025-01-29T13:02:00+00:00 |
| `20250205_154500_EMAIL-03655-eml` | email | [emails/2025-02/20250205_154500_EMAIL-03655.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250205_154500_EMAIL-03655.eml) | 2025-02-05T15:45:00+00:00 |
| `20250207_142700_EMAIL-03671-eml` | email | [emails/2025-02/20250207_142700_EMAIL-03671.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250207_142700_EMAIL-03671.eml) | 2025-02-07T14:27:00+00:00 |
| `20250217_123700_EMAIL-03765-eml` | email | [emails/2025-02/20250217_123700_EMAIL-03765.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250217_123700_EMAIL-03765.eml) | 2025-02-17T12:37:00+00:00 |
| `20250308_173300_EMAIL-03957-eml` | email | [emails/2025-03/20250308_173300_EMAIL-03957.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250308_173300_EMAIL-03957.eml) | 2025-03-08T17:33:00+00:00 |
| `20250316_221000_EMAIL-04033-eml` | email | [emails/2025-03/20250316_221000_EMAIL-04033.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250316_221000_EMAIL-04033.eml) | 2025-03-16T22:10:00+00:00 |
| `20250317_101000_EMAIL-04038-eml` | email | [emails/2025-03/20250317_101000_EMAIL-04038.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250317_101000_EMAIL-04038.eml) | 2025-03-17T10:10:00+00:00 |
| `20250331_203300_EMAIL-04172-eml` | email | [emails/2025-03/20250331_203300_EMAIL-04172.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250331_203300_EMAIL-04172.eml) | 2025-03-31T20:33:00+00:00 |
| `20250402_161200_EMAIL-04191-eml` | email | [emails/2025-04/20250402_161200_EMAIL-04191.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250402_161200_EMAIL-04191.eml) | 2025-04-02T16:12:00+00:00 |
| `20250410_135200_EMAIL-04256-eml` | email | [emails/2025-04/20250410_135200_EMAIL-04256.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250410_135200_EMAIL-04256.eml) | 2025-04-10T13:52:00+00:00 |
| `20250410_160000_EMAIL-04261-eml` | email | [emails/2025-04/20250410_160000_EMAIL-04261.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250410_160000_EMAIL-04261.eml) | 2025-04-10T16:00:00+00:00 |
| `20250519_093300_EMAIL-04558-eml` | email | [emails/2025-05/20250519_093300_EMAIL-04558.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250519_093300_EMAIL-04558.eml) | 2025-05-19T09:33:00+00:00 |
| `20250528_114200_EMAIL-04644-eml` | email | [emails/2025-05/20250528_114200_EMAIL-04644.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250528_114200_EMAIL-04644.eml) | 2025-05-28T11:42:00+00:00 |
| `20250602_114200_EMAIL-04687-eml` | email | [emails/2025-06/20250602_114200_EMAIL-04687.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250602_114200_EMAIL-04687.eml) | 2025-06-02T11:42:00+00:00 |
| `20250611_182600_EMAIL-04753-eml` | email | [emails/2025-06/20250611_182600_EMAIL-04753.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250611_182600_EMAIL-04753.eml) | 2025-06-11T18:26:00+00:00 |
| `20250617_090100_EMAIL-04800-eml` | email | [emails/2025-06/20250617_090100_EMAIL-04800.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250617_090100_EMAIL-04800.eml) | 2025-06-17T09:01:00+00:00 |
| `20250622_141400_EMAIL-04846-eml` | email | [emails/2025-06/20250622_141400_EMAIL-04846.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250622_141400_EMAIL-04846.eml) | 2025-06-22T14:14:00+00:00 |
| `20250715_123200_EMAIL-05045-eml` | email | [emails/2025-07/20250715_123200_EMAIL-05045.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250715_123200_EMAIL-05045.eml) | 2025-07-15T12:32:00+00:00 |
| `20250717_053200_EMAIL-05059-eml` | email | [emails/2025-07/20250717_053200_EMAIL-05059.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250717_053200_EMAIL-05059.eml) | 2025-07-17T05:32:00+00:00 |
| `20250810_124700_EMAIL-05244-eml` | email | [emails/2025-08/20250810_124700_EMAIL-05244.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250810_124700_EMAIL-05244.eml) | 2025-08-10T12:47:00+00:00 |
| `20250810_174700_EMAIL-05248-eml` | email | [emails/2025-08/20250810_174700_EMAIL-05248.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250810_174700_EMAIL-05248.eml) | 2025-08-10T17:47:00+00:00 |
| `20250824_110200_EMAIL-05393-eml` | email | [emails/2025-08/20250824_110200_EMAIL-05393.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250824_110200_EMAIL-05393.eml) | 2025-08-24T11:02:00+00:00 |
| `20250904_161300_EMAIL-05521-eml` | email | [emails/2025-09/20250904_161300_EMAIL-05521.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250904_161300_EMAIL-05521.eml) | 2025-09-04T16:13:00+00:00 |
| `20250906_101300_EMAIL-05538-eml` | email | [emails/2025-09/20250906_101300_EMAIL-05538.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250906_101300_EMAIL-05538.eml) | 2025-09-06T10:13:00+00:00 |
| `20251008_102400_EMAIL-05809-eml` | email | [emails/2025-10/20251008_102400_EMAIL-05809.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251008_102400_EMAIL-05809.eml) | 2025-10-08T10:24:00+00:00 |
| `20251028_153000_EMAIL-05991-eml` | email | [emails/2025-10/20251028_153000_EMAIL-05991.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251028_153000_EMAIL-05991.eml) | 2025-10-28T15:30:00+00:00 |
| `20251213_141100_EMAIL-06380-eml` | email | [emails/2025-12/20251213_141100_EMAIL-06380.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251213_141100_EMAIL-06380.eml) | 2025-12-13T14:11:00+00:00 |
| `20251215_001100_EMAIL-06398-eml` | email | [emails/2025-12/20251215_001100_EMAIL-06398.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251215_001100_EMAIL-06398.eml) | 2025-12-15T00:11:00+00:00 |
| `20251218_101600_EMAIL-06432-eml` | email | [emails/2025-12/20251218_101600_EMAIL-06432.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251218_101600_EMAIL-06432.eml) | 2025-12-18T10:16:00+00:00 |
| `20251219_103400_EMAIL-06435-eml` | email | [emails/2025-12/20251219_103400_EMAIL-06435.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251219_103400_EMAIL-06435.eml) | 2025-12-19T10:34:00+00:00 |
| `20251228_151200_EMAIL-06508-eml` | email | [emails/2025-12/20251228_151200_EMAIL-06508.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251228_151200_EMAIL-06508.eml) | 2025-12-28T15:12:00+00:00 |
| `20251231_113700_EMAIL-06541-eml` | email | [emails/2025-12/20251231_113700_EMAIL-06541.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251231_113700_EMAIL-06541.eml) | 2025-12-31T11:37:00+00:00 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-25T20:04:11+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
