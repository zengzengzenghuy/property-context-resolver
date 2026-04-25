# context.unit.<!-- auto:unit_id -->EH-049<!-- /auto:unit_id -->.md

> Per-unit dossier (one file per Einheit). Holds everything specific to this unit:
> the unit itself, the active lease, the tenant(s), and all unit/tenant-specific operations.
> **Property-wide data lives in `context.property.md`** — see `parent_property_ref` below.

<!-- auto:meta -->
- last_built_at: `2026-04-25T20:04:23+00:00`
- build_hash: `engine-v2`
- engine_version: `0.2.0`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `unit`
- parent_property_ref: `context.property.LIE-001.md`
- owner_ref: `EIG-003`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit -->
- unit_id: `EH-049`
- label: WE 49
- haus_id: `HAUS-16`
- floor: 4. OG
- position: mitte
- typ: Wohnung
- area_sqm: 115.0
- rooms: 4.5
- mea_‰: 267
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
- lease_id: `LEASE-MIE-003`
- unit_ref: `EH-049`
- start_date: 2020-03-22 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-003)
- end_date: _(no data in source yet)_
- term_type: `unbefristet`
- cancellation_status: `by_tenant` (notice_date: 2024-04-19, move_out_date: —)
- rent_components: { kaltmiete: 1721.0, betriebskosten_vorauszahlung: 298.0, total_warmmiete: 2019.00 }
- payment_mode: Überweisung
- iban_payer: DE83100701245940139904 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-003)
- kaution: { amount: 5163.0 }
- usage: `residential`
- subletting: { current_status: `requested` }
- special_agreements: _(no data in source yet)_
<!-- /auto:lease -->

### 2.1 Tenants on this Lease
<!-- auto:tenants -->
| tenant_id | name | role | contact_email | contact_phone | comms_pref | gesamtschuldner |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-003` | Frau Joanna Schäfer | haupt | joanna.schaefer@outlook.com | 01718702621 | email | — |
<!-- /auto:tenants -->

---

## 3. Operations (this unit / this tenant)

### 3.1 Open Tickets — Critical (overdue or due ≤7 days)
<!-- auto:tickets.critical -->
| ticket_id | type | title | deadline | status | assignee |
| --- | --- | --- | --- | --- | --- |
| `TKT-99565299` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-5e579093` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-897d7fa3` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-172e9eac` | schimmel | Re: Schimmel im Schlafzimmer | — | open | — |
| `TKT-ce84468c` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-84a87a3b` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-ee34d9ff` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-cb3f50e0` | wasserschaden | Wasserschaden Bad | — | open | — |
<!-- /auto:tickets.critical -->

### 3.2 Open Tickets — Aggregate
<!-- auto:tickets.aggregate -->
- total_open: `17`
- by_type: { abfluss: `1`, fenster: `3`, schimmel: `3`, schluessel: `5`, wasserschaden: `5` }
- live source: `db.tickets WHERE unit_id=EH-049 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren (per claim)
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-003` | — | 1 | 8076.00 EUR | 2025-12-03 | — | — |
- live balance pointer: `db.tenant_balance.tenant_id=MIE-003`
<!-- /auto:dunning -->

### 3.4 Active Reductions / Deferrals (§ 536 BGB)
<!-- auto:reductions -->
- date_raised: 2024-06-28
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-09-09
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-09-09
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-11-09
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-03-26
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-03-27
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
| Mieterwechsel | 2024-04-19 | Kündigung erhalten | Verwaltung | TBD | Übergabe-Termin offen |
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
| `TH-c218a8` | Verkaufsabsicht WE 49 | 2025-06-14 | `EH-049` | active | 7 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250614_034800_EMAIL-04770.eml) |
| `TH-8aa526` | Mieterwechsel in WE 49 | 2025-09-01 | `EH-049` | active | 3 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250901_214100_EMAIL-05489.eml) |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `kontoauszug_2024_2025-csv` | bank | [bank/kontoauszug_2024_2025.csv](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv) | 2026-04-25 |
| `20240118_142300_EMAIL-00145-eml` | email | [emails/2024-01/20240118_142300_EMAIL-00145.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240118_142300_EMAIL-00145.eml) | 2024-01-18T14:23:00+00:00 |
| `20240125_164700_EMAIL-00199-eml` | email | [emails/2024-01/20240125_164700_EMAIL-00199.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240125_164700_EMAIL-00199.eml) | 2024-01-25T16:47:00+00:00 |
| `20240223_133800_EMAIL-00453-eml` | email | [emails/2024-02/20240223_133800_EMAIL-00453.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240223_133800_EMAIL-00453.eml) | 2024-02-23T13:38:00+00:00 |
| `20240323_004700_EMAIL-00713-eml` | email | [emails/2024-03/20240323_004700_EMAIL-00713.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240323_004700_EMAIL-00713.eml) | 2024-03-23T00:47:00+00:00 |
| `20240323_123700_EMAIL-00717-eml` | email | [emails/2024-03/20240323_123700_EMAIL-00717.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240323_123700_EMAIL-00717.eml) | 2024-03-23T12:37:00+00:00 |
| `20240327_161000_EMAIL-00747-eml` | email | [emails/2024-03/20240327_161000_EMAIL-00747.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240327_161000_EMAIL-00747.eml) | 2024-03-27T16:10:00+00:00 |
| `20240403_114100_EMAIL-00814-eml` | email | [emails/2024-04/20240403_114100_EMAIL-00814.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240403_114100_EMAIL-00814.eml) | 2024-04-03T11:41:00+00:00 |
| `20240418_115600_EMAIL-00976-eml` | email | [emails/2024-04/20240418_115600_EMAIL-00976.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240418_115600_EMAIL-00976.eml) | 2024-04-18T11:56:00+00:00 |
| `20240419_105600_EMAIL-00985-eml` | email | [emails/2024-04/20240419_105600_EMAIL-00985.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240419_105600_EMAIL-00985.eml) | 2024-04-19T10:56:00+00:00 |
| `20240419_161200_EMAIL-00991-eml` | email | [emails/2024-04/20240419_161200_EMAIL-00991.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240419_161200_EMAIL-00991.eml) | 2024-04-19T16:12:00+00:00 |
| `20240421_071200_EMAIL-01005-eml` | email | [emails/2024-04/20240421_071200_EMAIL-01005.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240421_071200_EMAIL-01005.eml) | 2024-04-21T07:12:00+00:00 |
| `20240601_153000_EMAIL-01376-eml` | email | [emails/2024-06/20240601_153000_EMAIL-01376.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240601_153000_EMAIL-01376.eml) | 2024-06-01T15:30:00+00:00 |
| `20240618_184500_EMAIL-01533-eml` | email | [emails/2024-06/20240618_184500_EMAIL-01533.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240618_184500_EMAIL-01533.eml) | 2024-06-18T18:45:00+00:00 |
| `20240628_150500_EMAIL-01609-eml` | email | [emails/2024-06/20240628_150500_EMAIL-01609.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240628_150500_EMAIL-01609.eml) | 2024-06-28T15:05:00+00:00 |
| `20240709_101600_EMAIL-01704-eml` | email | [emails/2024-07/20240709_101600_EMAIL-01704.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240709_101600_EMAIL-01704.eml) | 2024-07-09T10:16:00+00:00 |
| `20240820_114900_EMAIL-02107-eml` | email | [emails/2024-08/20240820_114900_EMAIL-02107.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240820_114900_EMAIL-02107.eml) | 2024-08-20T11:49:00+00:00 |
| `20240830_162600_EMAIL-02196-eml` | email | [emails/2024-08/20240830_162600_EMAIL-02196.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240830_162600_EMAIL-02196.eml) | 2024-08-30T16:26:00+00:00 |
| `20240831_222600_EMAIL-02208-eml` | email | [emails/2024-08/20240831_222600_EMAIL-02208.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240831_222600_EMAIL-02208.eml) | 2024-08-31T22:26:00+00:00 |
| `20240908_201000_EMAIL-02294-eml` | email | [emails/2024-09/20240908_201000_EMAIL-02294.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240908_201000_EMAIL-02294.eml) | 2024-09-08T20:10:00+00:00 |
| `20240909_011000_EMAIL-02296-eml` | email | [emails/2024-09/20240909_011000_EMAIL-02296.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240909_011000_EMAIL-02296.eml) | 2024-09-09T01:10:00+00:00 |
| `20240909_153100_EMAIL-02302-eml` | email | [emails/2024-09/20240909_153100_EMAIL-02302.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240909_153100_EMAIL-02302.eml) | 2024-09-09T15:31:00+00:00 |
| `20240909_233100_EMAIL-02307-eml` | email | [emails/2024-09/20240909_233100_EMAIL-02307.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240909_233100_EMAIL-02307.eml) | 2024-09-09T23:31:00+00:00 |
| `20240911_163800_EMAIL-02320-eml` | email | [emails/2024-09/20240911_163800_EMAIL-02320.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240911_163800_EMAIL-02320.eml) | 2024-09-11T16:38:00+00:00 |
| `20240921_110000_EMAIL-02395-eml` | email | [emails/2024-09/20240921_110000_EMAIL-02395.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240921_110000_EMAIL-02395.eml) | 2024-09-21T11:00:00+00:00 |
| `20240922_200000_EMAIL-02417-eml` | email | [emails/2024-09/20240922_200000_EMAIL-02417.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240922_200000_EMAIL-02417.eml) | 2024-09-22T20:00:00+00:00 |
| `20240927_140300_EMAIL-02459-eml` | email | [emails/2024-09/20240927_140300_EMAIL-02459.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240927_140300_EMAIL-02459.eml) | 2024-09-27T14:03:00+00:00 |
| `20241003_142100_EMAIL-02504-eml` | email | [emails/2024-10/20241003_142100_EMAIL-02504.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241003_142100_EMAIL-02504.eml) | 2024-10-03T14:21:00+00:00 |
| `20241017_172900_EMAIL-02640-eml` | email | [emails/2024-10/20241017_172900_EMAIL-02640.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241017_172900_EMAIL-02640.eml) | 2024-10-17T17:29:00+00:00 |
| `20241025_110400_EMAIL-02716-eml` | email | [emails/2024-10/20241025_110400_EMAIL-02716.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241025_110400_EMAIL-02716.eml) | 2024-10-25T11:04:00+00:00 |
| `20241109_085500_EMAIL-02856-eml` | email | [emails/2024-11/20241109_085500_EMAIL-02856.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241109_085500_EMAIL-02856.eml) | 2024-11-09T08:55:00+00:00 |
| `20241118_071200_EMAIL-02942-eml` | email | [emails/2024-11/20241118_071200_EMAIL-02942.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241118_071200_EMAIL-02942.eml) | 2024-11-18T07:12:00+00:00 |
| `20241123_093800_EMAIL-02985-eml` | email | [emails/2024-11/20241123_093800_EMAIL-02985.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241123_093800_EMAIL-02985.eml) | 2024-11-23T09:38:00+00:00 |
| `20241123_143800_EMAIL-02990-eml` | email | [emails/2024-11/20241123_143800_EMAIL-02990.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241123_143800_EMAIL-02990.eml) | 2024-11-23T14:38:00+00:00 |
| `20241209_174700_EMAIL-03136-eml` | email | [emails/2024-12/20241209_174700_EMAIL-03136.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241209_174700_EMAIL-03136.eml) | 2024-12-09T17:47:00+00:00 |
| `20241212_122300_EMAIL-03154-eml` | email | [emails/2024-12/20241212_122300_EMAIL-03154.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241212_122300_EMAIL-03154.eml) | 2024-12-12T12:23:00+00:00 |
| `20241214_042300_EMAIL-03169-eml` | email | [emails/2024-12/20241214_042300_EMAIL-03169.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241214_042300_EMAIL-03169.eml) | 2024-12-14T04:23:00+00:00 |
| `20241225_111100_EMAIL-03269-eml` | email | [emails/2024-12/20241225_111100_EMAIL-03269.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241225_111100_EMAIL-03269.eml) | 2024-12-25T11:11:00+00:00 |
| `20241230_163200_EMAIL-03321-eml` | email | [emails/2024-12/20241230_163200_EMAIL-03321.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241230_163200_EMAIL-03321.eml) | 2024-12-30T16:32:00+00:00 |
| `20250102_115100_EMAIL-03358-eml` | email | [emails/2025-01/20250102_115100_EMAIL-03358.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250102_115100_EMAIL-03358.eml) | 2025-01-02T11:51:00+00:00 |
| `20250102_135500_EMAIL-03359-eml` | email | [emails/2025-01/20250102_135500_EMAIL-03359.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250102_135500_EMAIL-03359.eml) | 2025-01-02T13:55:00+00:00 |
| `20250119_084600_EMAIL-03515-eml` | email | [emails/2025-01/20250119_084600_EMAIL-03515.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250119_084600_EMAIL-03515.eml) | 2025-01-19T08:46:00+00:00 |
| `20250219_153500_EMAIL-03786-eml` | email | [emails/2025-02/20250219_153500_EMAIL-03786.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250219_153500_EMAIL-03786.eml) | 2025-02-19T15:35:00+00:00 |
| `20250225_023500_EMAIL-03841-eml` | email | [emails/2025-02/20250225_023500_EMAIL-03841.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250225_023500_EMAIL-03841.eml) | 2025-02-25T02:35:00+00:00 |
| `20250227_145000_EMAIL-03873-eml` | email | [emails/2025-02/20250227_145000_EMAIL-03873.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250227_145000_EMAIL-03873.eml) | 2025-02-27T14:50:00+00:00 |
| `20250312_095600_EMAIL-03991-eml` | email | [emails/2025-03/20250312_095600_EMAIL-03991.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250312_095600_EMAIL-03991.eml) | 2025-03-12T09:56:00+00:00 |
| `20250326_221900_EMAIL-04130-eml` | email | [emails/2025-03/20250326_221900_EMAIL-04130.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250326_221900_EMAIL-04130.eml) | 2025-03-26T22:19:00+00:00 |
| `20250327_101900_EMAIL-04135-eml` | email | [emails/2025-03/20250327_101900_EMAIL-04135.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250327_101900_EMAIL-04135.eml) | 2025-03-27T10:19:00+00:00 |
| `20250412_165000_EMAIL-04278-eml` | email | [emails/2025-04/20250412_165000_EMAIL-04278.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250412_165000_EMAIL-04278.eml) | 2025-04-12T16:50:00+00:00 |
| `20250513_134700_EMAIL-04503-eml` | email | [emails/2025-05/20250513_134700_EMAIL-04503.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250513_134700_EMAIL-04503.eml) | 2025-05-13T13:47:00+00:00 |
| `20250517_131000_EMAIL-04539-eml` | email | [emails/2025-05/20250517_131000_EMAIL-04539.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250517_131000_EMAIL-04539.eml) | 2025-05-17T13:10:00+00:00 |
| `20250521_123100_EMAIL-04579-eml` | email | [emails/2025-05/20250521_123100_EMAIL-04579.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250521_123100_EMAIL-04579.eml) | 2025-05-21T12:31:00+00:00 |
| `20250525_163500_EMAIL-04619-eml` | email | [emails/2025-05/20250525_163500_EMAIL-04619.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250525_163500_EMAIL-04619.eml) | 2025-05-25T16:35:00+00:00 |
| `20250525_165700_EMAIL-04620-eml` | email | [emails/2025-05/20250525_165700_EMAIL-04620.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250525_165700_EMAIL-04620.eml) | 2025-05-25T16:57:00+00:00 |
| `20250527_102200_EMAIL-04633-eml` | email | [emails/2025-05/20250527_102200_EMAIL-04633.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250527_102200_EMAIL-04633.eml) | 2025-05-27T10:22:00+00:00 |
| `20250606_193800_EMAIL-04714-eml` | email | [emails/2025-06/20250606_193800_EMAIL-04714.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250606_193800_EMAIL-04714.eml) | 2025-06-06T19:38:00+00:00 |
| `20250614_034800_EMAIL-04770-eml` | email | [emails/2025-06/20250614_034800_EMAIL-04770.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250614_034800_EMAIL-04770.eml) | 2025-06-14T03:48:00+00:00 |
| `20250623_051300_EMAIL-04852-eml` | email | [emails/2025-06/20250623_051300_EMAIL-04852.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250623_051300_EMAIL-04852.eml) | 2025-06-23T05:13:00+00:00 |
| `20250708_104800_EMAIL-04970-eml` | email | [emails/2025-07/20250708_104800_EMAIL-04970.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250708_104800_EMAIL-04970.eml) | 2025-07-08T10:48:00+00:00 |
| `20250824_175600_EMAIL-05395-eml` | email | [emails/2025-08/20250824_175600_EMAIL-05395.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250824_175600_EMAIL-05395.eml) | 2025-08-24T17:56:00+00:00 |
| `20250831_145100_EMAIL-05468-eml` | email | [emails/2025-08/20250831_145100_EMAIL-05468.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250831_145100_EMAIL-05468.eml) | 2025-08-31T14:51:00+00:00 |
| `20250901_214100_EMAIL-05489-eml` | email | [emails/2025-09/20250901_214100_EMAIL-05489.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250901_214100_EMAIL-05489.eml) | 2025-09-01 |
| `20250902_173100_EMAIL-05501-eml` | email | [emails/2025-09/20250902_173100_EMAIL-05501.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250902_173100_EMAIL-05501.eml) | 2025-09-02T17:31:00+00:00 |
| `20250915_155800_EMAIL-05630-eml` | email | [emails/2025-09/20250915_155800_EMAIL-05630.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250915_155800_EMAIL-05630.eml) | 2025-09-15T15:58:00+00:00 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-25T20:04:11+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
