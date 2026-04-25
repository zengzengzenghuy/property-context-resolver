# context.unit.<!-- auto:unit_id -->EH-046<!-- /auto:unit_id -->.md

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
- owner_ref: `EIG-030`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit -->
- unit_id: `EH-046`
- label: WE 46
- haus_id: `HAUS-16`
- floor: 3. OG
- position: mitte
- typ: Wohnung
- area_sqm: 85.0
- rooms: 3.0
- mea_‰: 197
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
- lease_id: `LEASE-MIE-010`
- unit_ref: `EH-046`
- start_date: 2022-06-20 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-010)
- end_date: _(no data in source yet)_
- term_type: `unbefristet`
- cancellation_status: `by_tenant` (notice_date: 2025-07-29, move_out_date: —)
- rent_components: { kaltmiete: 1432.0, betriebskosten_vorauszahlung: 294.0, total_warmmiete: 1726.00 }
- payment_mode: Überweisung
- iban_payer: DE93120300000262174596 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-010)
- kaution: { amount: 4296.0 }
- usage: `residential`
- subletting: { current_status: `requested` }
- special_agreements: _(no data in source yet)_
<!-- /auto:lease -->

### 2.1 Tenants on this Lease
<!-- auto:tenants -->
| tenant_id | name | role | contact_email | contact_phone | comms_pref | gesamtschuldner |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-010` | Frau Ewa Thies | haupt | ewa.thies@gmail.com | +49(0)0640 90974 | email | — |
<!-- /auto:tenants -->

---

## 3. Operations (this unit / this tenant)

### 3.1 Open Tickets — Critical (overdue or due ≤7 days)
<!-- auto:tickets.critical -->
| ticket_id | type | title | deadline | status | assignee |
| --- | --- | --- | --- | --- | --- |
| `TKT-da67518e` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-848af94c` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-e1a490e8` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-1303f1b5` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-e7041e4d` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-2233b516` | wasserschaden | Wasserschaden Bad | — | open | — |
<!-- /auto:tickets.critical -->

### 3.2 Open Tickets — Aggregate
<!-- auto:tickets.aggregate -->
- total_open: `21`
- by_type: { abfluss: `3`, fenster: `7`, schimmel: `1`, schluessel: `5`, wasserschaden: `5` }
- live source: `db.tickets WHERE unit_id=EH-046 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren (per claim)
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-010` | — | 1 | 6904.00 EUR | 2025-12-03 | — | — |
- live balance pointer: `db.tenant_balance.tenant_id=MIE-010`
<!-- /auto:dunning -->

### 3.4 Active Reductions / Deferrals (§ 536 BGB)
<!-- auto:reductions -->
- date_raised: 2025-01-27
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-02-12
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-10-17
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
| Mieterwechsel | 2025-07-29 | Kündigung erhalten | Verwaltung | TBD | Übergabe-Termin offen |
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
| `TH-9c3f17` | Verkaufsabsicht WE 46 | 2025-05-18 | `EH-046` | active | 7 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250518_202600_EMAIL-04554.eml) |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `kontoauszug_2024_2025-csv` | bank | [bank/kontoauszug_2024_2025.csv](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv) | 2026-04-25 |
| `20240111_185200_EMAIL-00091-eml` | email | [emails/2024-01/20240111_185200_EMAIL-00091.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240111_185200_EMAIL-00091.eml) | 2024-01-11T18:52:00+00:00 |
| `20240129_173300_EMAIL-00237-eml` | email | [emails/2024-01/20240129_173300_EMAIL-00237.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240129_173300_EMAIL-00237.eml) | 2024-01-29T17:33:00+00:00 |
| `20240209_161400_EMAIL-00346-eml` | email | [emails/2024-02/20240209_161400_EMAIL-00346.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240209_161400_EMAIL-00346.eml) | 2024-02-09T16:14:00+00:00 |
| `20240222_185800_EMAIL-00443-eml` | email | [emails/2024-02/20240222_185800_EMAIL-00443.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240222_185800_EMAIL-00443.eml) | 2024-02-22T18:58:00+00:00 |
| `20240303_125100_EMAIL-00535-eml` | email | [emails/2024-03/20240303_125100_EMAIL-00535.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240303_125100_EMAIL-00535.eml) | 2024-03-03T12:51:00+00:00 |
| `20240305_235100_EMAIL-00560-eml` | email | [emails/2024-03/20240305_235100_EMAIL-00560.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240305_235100_EMAIL-00560.eml) | 2024-03-05T23:51:00+00:00 |
| `20240312_160400_EMAIL-00625-eml` | email | [emails/2024-03/20240312_160400_EMAIL-00625.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240312_160400_EMAIL-00625.eml) | 2024-03-12T16:04:00+00:00 |
| `20240331_141600_EMAIL-00782-eml` | email | [emails/2024-03/20240331_141600_EMAIL-00782.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240331_141600_EMAIL-00782.eml) | 2024-03-31T14:16:00+00:00 |
| `20240401_152200_EMAIL-00792-eml` | email | [emails/2024-04/20240401_152200_EMAIL-00792.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240401_152200_EMAIL-00792.eml) | 2024-04-01T15:22:00+00:00 |
| `20240410_133000_EMAIL-00886-eml` | email | [emails/2024-04/20240410_133000_EMAIL-00886.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240410_133000_EMAIL-00886.eml) | 2024-04-10T13:30:00+00:00 |
| `20240416_153000_EMAIL-00958-eml` | email | [emails/2024-04/20240416_153000_EMAIL-00958.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240416_153000_EMAIL-00958.eml) | 2024-04-16T15:30:00+00:00 |
| `20240417_133000_EMAIL-00970-eml` | email | [emails/2024-04/20240417_133000_EMAIL-00970.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240417_133000_EMAIL-00970.eml) | 2024-04-17T13:30:00+00:00 |
| `20240428_105400_EMAIL-01059-eml` | email | [emails/2024-04/20240428_105400_EMAIL-01059.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240428_105400_EMAIL-01059.eml) | 2024-04-28T10:54:00+00:00 |
| `20240511_095400_EMAIL-01175-eml` | email | [emails/2024-05/20240511_095400_EMAIL-01175.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240511_095400_EMAIL-01175.eml) | 2024-05-11T09:54:00+00:00 |
| `20240511_103400_EMAIL-01179-eml` | email | [emails/2024-05/20240511_103400_EMAIL-01179.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240511_103400_EMAIL-01179.eml) | 2024-05-11T10:34:00+00:00 |
| `20240601_110500_EMAIL-01372-eml` | email | [emails/2024-06/20240601_110500_EMAIL-01372.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240601_110500_EMAIL-01372.eml) | 2024-06-01T11:05:00+00:00 |
| `20240604_162500_EMAIL-01403-eml` | email | [emails/2024-06/20240604_162500_EMAIL-01403.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240604_162500_EMAIL-01403.eml) | 2024-06-04T16:25:00+00:00 |
| `20240605_002500_EMAIL-01405-eml` | email | [emails/2024-06/20240605_002500_EMAIL-01405.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240605_002500_EMAIL-01405.eml) | 2024-06-05T00:25:00+00:00 |
| `20240711_175700_EMAIL-01736-eml` | email | [emails/2024-07/20240711_175700_EMAIL-01736.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240711_175700_EMAIL-01736.eml) | 2024-07-11T17:57:00+00:00 |
| `20240724_152400_EMAIL-01853-eml` | email | [emails/2024-07/20240724_152400_EMAIL-01853.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240724_152400_EMAIL-01853.eml) | 2024-07-24T15:24:00+00:00 |
| `20240811_123500_EMAIL-02013-eml` | email | [emails/2024-08/20240811_123500_EMAIL-02013.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240811_123500_EMAIL-02013.eml) | 2024-08-11T12:35:00+00:00 |
| `20240912_141500_EMAIL-02329-eml` | email | [emails/2024-09/20240912_141500_EMAIL-02329.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240912_141500_EMAIL-02329.eml) | 2024-09-12T14:15:00+00:00 |
| `20240923_094300_EMAIL-02421-eml` | email | [emails/2024-09/20240923_094300_EMAIL-02421.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240923_094300_EMAIL-02421.eml) | 2024-09-23T09:43:00+00:00 |
| `20241004_102400_EMAIL-02511-eml` | email | [emails/2024-10/20241004_102400_EMAIL-02511.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241004_102400_EMAIL-02511.eml) | 2024-10-04T10:24:00+00:00 |
| `20241008_184200_EMAIL-02564-eml` | email | [emails/2024-10/20241008_184200_EMAIL-02564.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241008_184200_EMAIL-02564.eml) | 2024-10-08T18:42:00+00:00 |
| `20241026_131500_EMAIL-02728-eml` | email | [emails/2024-10/20241026_131500_EMAIL-02728.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241026_131500_EMAIL-02728.eml) | 2024-10-26T13:15:00+00:00 |
| `20241113_110700_EMAIL-02891-eml` | email | [emails/2024-11/20241113_110700_EMAIL-02891.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241113_110700_EMAIL-02891.eml) | 2024-11-13T11:07:00+00:00 |
| `20241118_141200_EMAIL-02946-eml` | email | [emails/2024-11/20241118_141200_EMAIL-02946.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241118_141200_EMAIL-02946.eml) | 2024-11-18T14:12:00+00:00 |
| `20241212_155200_EMAIL-03157-eml` | email | [emails/2024-12/20241212_155200_EMAIL-03157.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241212_155200_EMAIL-03157.eml) | 2024-12-12T15:52:00+00:00 |
| `20241223_140800_EMAIL-03251-eml` | email | [emails/2024-12/20241223_140800_EMAIL-03251.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241223_140800_EMAIL-03251.eml) | 2024-12-23T14:08:00+00:00 |
| `20250105_101400_EMAIL-03383-eml` | email | [emails/2025-01/20250105_101400_EMAIL-03383.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250105_101400_EMAIL-03383.eml) | 2025-01-05T10:14:00+00:00 |
| `20250114_133100_EMAIL-03476-eml` | email | [emails/2025-01/20250114_133100_EMAIL-03476.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250114_133100_EMAIL-03476.eml) | 2025-01-14T13:31:00+00:00 |
| `20250127_151600_EMAIL-03575-eml` | email | [emails/2025-01/20250127_151600_EMAIL-03575.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250127_151600_EMAIL-03575.eml) | 2025-01-27T15:16:00+00:00 |
| `20250212_162700_EMAIL-03712-eml` | email | [emails/2025-02/20250212_162700_EMAIL-03712.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250212_162700_EMAIL-03712.eml) | 2025-02-12T16:27:00+00:00 |
| `20250304_124700_EMAIL-03917-eml` | email | [emails/2025-03/20250304_124700_EMAIL-03917.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250304_124700_EMAIL-03917.eml) | 2025-03-04T12:47:00+00:00 |
| `20250328_205300_EMAIL-04148-eml` | email | [emails/2025-03/20250328_205300_EMAIL-04148.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250328_205300_EMAIL-04148.eml) | 2025-03-28T20:53:00+00:00 |
| `20250406_172100_EMAIL-04227-eml` | email | [emails/2025-04/20250406_172100_EMAIL-04227.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250406_172100_EMAIL-04227.eml) | 2025-04-06T17:21:00+00:00 |
| `20250421_105600_EMAIL-04344-eml` | email | [emails/2025-04/20250421_105600_EMAIL-04344.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250421_105600_EMAIL-04344.eml) | 2025-04-21T10:56:00+00:00 |
| `20250506_153600_EMAIL-04447-eml` | email | [emails/2025-05/20250506_153600_EMAIL-04447.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250506_153600_EMAIL-04447.eml) | 2025-05-06T15:36:00+00:00 |
| `20250511_152900_EMAIL-04488-eml` | email | [emails/2025-05/20250511_152900_EMAIL-04488.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250511_152900_EMAIL-04488.eml) | 2025-05-11T15:29:00+00:00 |
| `20250518_202600_EMAIL-04554-eml` | email | [emails/2025-05/20250518_202600_EMAIL-04554.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250518_202600_EMAIL-04554.eml) | 2025-05-18T20:26:00+00:00 |
| `20250519_143700_EMAIL-04565-eml` | email | [emails/2025-05/20250519_143700_EMAIL-04565.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250519_143700_EMAIL-04565.eml) | 2025-05-19T14:37:00+00:00 |
| `20250526_123700_EMAIL-04626-eml` | email | [emails/2025-05/20250526_123700_EMAIL-04626.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250526_123700_EMAIL-04626.eml) | 2025-05-26T12:37:00+00:00 |
| `20250531_175300_EMAIL-04677-eml` | email | [emails/2025-05/20250531_175300_EMAIL-04677.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250531_175300_EMAIL-04677.eml) | 2025-05-31T17:53:00+00:00 |
| `20250622_160700_EMAIL-04848-eml` | email | [emails/2025-06/20250622_160700_EMAIL-04848.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250622_160700_EMAIL-04848.eml) | 2025-06-22T16:07:00+00:00 |
| `20250624_201200_EMAIL-04867-eml` | email | [emails/2025-06/20250624_201200_EMAIL-04867.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250624_201200_EMAIL-04867.eml) | 2025-06-24T20:12:00+00:00 |
| `20250707_115300_EMAIL-04961-eml` | email | [emails/2025-07/20250707_115300_EMAIL-04961.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250707_115300_EMAIL-04961.eml) | 2025-07-07T11:53:00+00:00 |
| `20250717_141100_EMAIL-05061-eml` | email | [emails/2025-07/20250717_141100_EMAIL-05061.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250717_141100_EMAIL-05061.eml) | 2025-07-17T14:11:00+00:00 |
| `20250729_151700_EMAIL-05157-eml` | email | [emails/2025-07/20250729_151700_EMAIL-05157.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250729_151700_EMAIL-05157.eml) | 2025-07-29T15:17:00+00:00 |
| `20250729_204100_EMAIL-05159-eml` | email | [emails/2025-07/20250729_204100_EMAIL-05159.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250729_204100_EMAIL-05159.eml) | 2025-07-29T20:41:00+00:00 |
| `20250819_103200_EMAIL-05348-eml` | email | [emails/2025-08/20250819_103200_EMAIL-05348.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250819_103200_EMAIL-05348.eml) | 2025-08-19T10:32:00+00:00 |
| `20250823_123800_EMAIL-05384-eml` | email | [emails/2025-08/20250823_123800_EMAIL-05384.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250823_123800_EMAIL-05384.eml) | 2025-08-23T12:38:00+00:00 |
| `20250826_200600_EMAIL-05412-eml` | email | [emails/2025-08/20250826_200600_EMAIL-05412.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250826_200600_EMAIL-05412.eml) | 2025-08-26T20:06:00+00:00 |
| `20250921_154300_EMAIL-05681-eml` | email | [emails/2025-09/20250921_154300_EMAIL-05681.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250921_154300_EMAIL-05681.eml) | 2025-09-21T15:43:00+00:00 |
| `20250923_014300_EMAIL-05693-eml` | email | [emails/2025-09/20250923_014300_EMAIL-05693.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250923_014300_EMAIL-05693.eml) | 2025-09-23T01:43:00+00:00 |
| `20250928_162000_EMAIL-05735-eml` | email | [emails/2025-09/20250928_162000_EMAIL-05735.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250928_162000_EMAIL-05735.eml) | 2025-09-28T16:20:00+00:00 |
| `20250929_103000_EMAIL-05742-eml` | email | [emails/2025-09/20250929_103000_EMAIL-05742.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250929_103000_EMAIL-05742.eml) | 2025-09-29T10:30:00+00:00 |
| `20251005_102900_EMAIL-05784-eml` | email | [emails/2025-10/20251005_102900_EMAIL-05784.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251005_102900_EMAIL-05784.eml) | 2025-10-05T10:29:00+00:00 |
| `20251017_145600_EMAIL-05898-eml` | email | [emails/2025-10/20251017_145600_EMAIL-05898.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251017_145600_EMAIL-05898.eml) | 2025-10-17T14:56:00+00:00 |
| `20251116_110100_EMAIL-06134-eml` | email | [emails/2025-11/20251116_110100_EMAIL-06134.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251116_110100_EMAIL-06134.eml) | 2025-11-16T11:01:00+00:00 |
| `20251116_165700_EMAIL-06140-eml` | email | [emails/2025-11/20251116_165700_EMAIL-06140.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251116_165700_EMAIL-06140.eml) | 2025-11-16T16:57:00+00:00 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-25T20:04:11+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
