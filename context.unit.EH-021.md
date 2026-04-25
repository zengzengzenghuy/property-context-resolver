# context.unit.<!-- auto:unit_id -->EH-021<!-- /auto:unit_id -->.md

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
- owner_ref: `EIG-031`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit -->
- unit_id: `EH-021`
- label: WE 21
- haus_id: `HAUS-14`
- floor: 1. OG
- position: rechts
- typ: Wohnung
- area_sqm: 82.0
- rooms: 3.0
- mea_‰: 190
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
- lease_id: `LEASE-MIE-002`
- unit_ref: `EH-021`
- start_date: 2021-06-28 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-002)
- end_date: _(no data in source yet)_
- term_type: `unbefristet`
- cancellation_status: `by_tenant` (notice_date: 2025-10-04, move_out_date: —)
- rent_components: { kaltmiete: 1248.0, betriebskosten_vorauszahlung: 263.0, total_warmmiete: 1511.00 }
- payment_mode: Überweisung
- iban_payer: DE99100100100249947174 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-002)
- kaution: { amount: 3744.0 }
- usage: `residential`
- subletting: { current_status: `requested` }
- special_agreements: _(no data in source yet)_
<!-- /auto:lease -->

### 2.1 Tenants on this Lease
<!-- auto:tenants -->
| tenant_id | name | role | contact_email | contact_phone | comms_pref | gesamtschuldner |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-002` | Frau Edelgard Wulf | haupt | edelgard.wulf@gmx.de | 0057662702 | email | — |
<!-- /auto:tenants -->

---

## 3. Operations (this unit / this tenant)

### 3.1 Open Tickets — Critical (overdue or due ≤7 days)
<!-- auto:tickets.critical -->
| ticket_id | type | title | deadline | status | assignee |
| --- | --- | --- | --- | --- | --- |
| `TKT-f9447ce1` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-e4a67f84` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-69074a54` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-3f88252c` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-9b8c16a6` | wasserschaden | Re: Wasserschaden Bad | — | open | — |
| `TKT-f4b7914e` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-dffa9e9e` | schimmel | Re: Schimmel im Schlafzimmer | — | open | — |
| `TKT-e7446c22` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-ee5e2ebd` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-7777afca` | wasserschaden | Wasserschaden Bad | — | open | — |
<!-- /auto:tickets.critical -->

### 3.2 Open Tickets — Aggregate
<!-- auto:tickets.aggregate -->
- total_open: `20`
- by_type: { abfluss: `5`, fenster: `3`, schimmel: `5`, schluessel: `2`, wasserschaden: `5` }
- live source: `db.tickets WHERE unit_id=EH-021 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren (per claim)
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-002` | — | 1 | 6044.00 EUR | 2025-12-01 | — | — |
- live balance pointer: `db.tenant_balance.tenant_id=MIE-002`
<!-- /auto:dunning -->

### 3.4 Active Reductions / Deferrals (§ 536 BGB)
<!-- auto:reductions -->
- date_raised: 2024-04-02
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-04-03
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-10-07
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-10-14
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
| Mieterwechsel | 2025-10-04 | Kündigung erhalten | Verwaltung | TBD | Übergabe-Termin offen |
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
| `TH-7b2d10` | Frage zu Kaution | 2025-12-30 | `MIE-002` | active | 108 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251230_105600_EMAIL-06527.eml) |
| `TH-51e8f3` | Modernisierung - Zustimmung | 2025-12-30 | `EH-021` | active | 170 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251230_105500_EMAIL-06526.eml) |
| `TH-aba89e` | Mieterwechsel in WE 21 | 2025-10-13 | `EH-021` | active | 9 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251013_180500_EMAIL-05870.eml) |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `kontoauszug_2024_2025-csv` | bank | [bank/kontoauszug_2024_2025.csv](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv) | 2026-04-25 |
| `20241110_mahnung_LTR-0041-pdf` | letter | [briefe/2024-11/20241110_mahnung_LTR-0041.pdf](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/briefe/2024-11/20241110_mahnung_LTR-0041.pdf) | 2024-11-10 |
| `20250218_mahnung_LTR-0046-pdf` | letter | [briefe/2025-02/20250218_mahnung_LTR-0046.pdf](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/briefe/2025-02/20250218_mahnung_LTR-0046.pdf) | 2026-04-25 |
| `20240112_173000_EMAIL-00100-eml` | email | [emails/2024-01/20240112_173000_EMAIL-00100.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240112_173000_EMAIL-00100.eml) | 2024-01-12T17:30:00+00:00 |
| `20240114_160900_EMAIL-00117-eml` | email | [emails/2024-01/20240114_160900_EMAIL-00117.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240114_160900_EMAIL-00117.eml) | 2024-01-14T16:09:00+00:00 |
| `20240119_103200_EMAIL-00150-eml` | email | [emails/2024-01/20240119_103200_EMAIL-00150.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240119_103200_EMAIL-00150.eml) | 2024-01-19T10:32:00+00:00 |
| `20240121_091900_EMAIL-00168-eml` | email | [emails/2024-01/20240121_091900_EMAIL-00168.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240121_091900_EMAIL-00168.eml) | 2024-01-21T09:19:00+00:00 |
| `20240121_132600_EMAIL-00171-eml` | email | [emails/2024-01/20240121_132600_EMAIL-00171.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240121_132600_EMAIL-00171.eml) | 2024-01-21T13:26:00+00:00 |
| `20240402_164100_EMAIL-00803-eml` | email | [emails/2024-04/20240402_164100_EMAIL-00803.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240402_164100_EMAIL-00803.eml) | 2024-04-02T16:41:00+00:00 |
| `20240403_214100_EMAIL-00822-eml` | email | [emails/2024-04/20240403_214100_EMAIL-00822.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240403_214100_EMAIL-00822.eml) | 2024-04-03T21:41:00+00:00 |
| `20240408_114100_EMAIL-00870-eml` | email | [emails/2024-04/20240408_114100_EMAIL-00870.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240408_114100_EMAIL-00870.eml) | 2024-04-08T11:41:00+00:00 |
| `20240410_140000_EMAIL-00887-eml` | email | [emails/2024-04/20240410_140000_EMAIL-00887.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240410_140000_EMAIL-00887.eml) | 2024-04-10T14:00:00+00:00 |
| `20240502_091300_EMAIL-01096-eml` | email | [emails/2024-05/20240502_091300_EMAIL-01096.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240502_091300_EMAIL-01096.eml) | 2024-05-02T09:13:00+00:00 |
| `20240518_104900_EMAIL-01245-eml` | email | [emails/2024-05/20240518_104900_EMAIL-01245.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240518_104900_EMAIL-01245.eml) | 2024-05-18T10:49:00+00:00 |
| `20240628_144000_EMAIL-01608-eml` | email | [emails/2024-06/20240628_144000_EMAIL-01608.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240628_144000_EMAIL-01608.eml) | 2024-06-28T14:40:00+00:00 |
| `20240705_120200_EMAIL-01664-eml` | email | [emails/2024-07/20240705_120200_EMAIL-01664.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240705_120200_EMAIL-01664.eml) | 2024-07-05T12:02:00+00:00 |
| `20240714_124600_EMAIL-01758-eml` | email | [emails/2024-07/20240714_124600_EMAIL-01758.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240714_124600_EMAIL-01758.eml) | 2024-07-14T12:46:00+00:00 |
| `20240808_150400_EMAIL-01995-eml` | email | [emails/2024-08/20240808_150400_EMAIL-01995.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240808_150400_EMAIL-01995.eml) | 2024-08-08T15:04:00+00:00 |
| `20240814_231000_EMAIL-02045-eml` | email | [emails/2024-08/20240814_231000_EMAIL-02045.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240814_231000_EMAIL-02045.eml) | 2024-08-14T23:10:00+00:00 |
| `20240819_031800_EMAIL-02087-eml` | email | [emails/2024-08/20240819_031800_EMAIL-02087.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240819_031800_EMAIL-02087.eml) | 2024-08-19T03:18:00+00:00 |
| `20240824_093900_EMAIL-02135-eml` | email | [emails/2024-08/20240824_093900_EMAIL-02135.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240824_093900_EMAIL-02135.eml) | 2024-08-24T09:39:00+00:00 |
| `20240826_063900_EMAIL-02159-eml` | email | [emails/2024-08/20240826_063900_EMAIL-02159.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240826_063900_EMAIL-02159.eml) | 2024-08-26T06:39:00+00:00 |
| `20240907_111300_EMAIL-02274-eml` | email | [emails/2024-09/20240907_111300_EMAIL-02274.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240907_111300_EMAIL-02274.eml) | 2024-09-07T11:13:00+00:00 |
| `20240908_101600_EMAIL-02285-eml` | email | [emails/2024-09/20240908_101600_EMAIL-02285.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240908_101600_EMAIL-02285.eml) | 2024-09-08T10:16:00+00:00 |
| `20241007_163900_EMAIL-02548-eml` | email | [emails/2024-10/20241007_163900_EMAIL-02548.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241007_163900_EMAIL-02548.eml) | 2024-10-07T16:39:00+00:00 |
| `20241013_092800_EMAIL-02605-eml` | email | [emails/2024-10/20241013_092800_EMAIL-02605.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241013_092800_EMAIL-02605.eml) | 2024-10-13T09:28:00+00:00 |
| `20241016_205000_EMAIL-02630-eml` | email | [emails/2024-10/20241016_205000_EMAIL-02630.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241016_205000_EMAIL-02630.eml) | 2024-10-16T20:50:00+00:00 |
| `20241111_144900_EMAIL-02872-eml` | email | [emails/2024-11/20241111_144900_EMAIL-02872.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241111_144900_EMAIL-02872.eml) | 2024-11-11T14:49:00+00:00 |
| `20241111_164800_EMAIL-02875-eml` | email | [emails/2024-11/20241111_164800_EMAIL-02875.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241111_164800_EMAIL-02875.eml) | 2024-11-11T16:48:00+00:00 |
| `20241113_161200_EMAIL-02895-eml` | email | [emails/2024-11/20241113_161200_EMAIL-02895.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241113_161200_EMAIL-02895.eml) | 2024-11-13T16:12:00+00:00 |
| `20241122_093000_EMAIL-02972-eml` | email | [emails/2024-11/20241122_093000_EMAIL-02972.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241122_093000_EMAIL-02972.eml) | 2024-11-22T09:30:00+00:00 |
| `20241130_171500_EMAIL-03052-eml` | email | [emails/2024-11/20241130_171500_EMAIL-03052.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241130_171500_EMAIL-03052.eml) | 2024-11-30T17:15:00+00:00 |
| `20241212_134700_EMAIL-03155-eml` | email | [emails/2024-12/20241212_134700_EMAIL-03155.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241212_134700_EMAIL-03155.eml) | 2024-12-12T13:47:00+00:00 |
| `20241223_133800_EMAIL-03250-eml` | email | [emails/2024-12/20241223_133800_EMAIL-03250.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241223_133800_EMAIL-03250.eml) | 2024-12-23T13:38:00+00:00 |
| `20241227_150300_EMAIL-03292-eml` | email | [emails/2024-12/20241227_150300_EMAIL-03292.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241227_150300_EMAIL-03292.eml) | 2024-12-27T15:03:00+00:00 |
| `20250204_162800_EMAIL-03641-eml` | email | [emails/2025-02/20250204_162800_EMAIL-03641.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250204_162800_EMAIL-03641.eml) | 2025-02-04T16:28:00+00:00 |
| `20250205_042800_EMAIL-03645-eml` | email | [emails/2025-02/20250205_042800_EMAIL-03645.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250205_042800_EMAIL-03645.eml) | 2025-02-05T04:28:00+00:00 |
| `20250212_090600_EMAIL-03702-eml` | email | [emails/2025-02/20250212_090600_EMAIL-03702.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250212_090600_EMAIL-03702.eml) | 2025-02-12T09:06:00+00:00 |
| `20250213_190600_EMAIL-03728-eml` | email | [emails/2025-02/20250213_190600_EMAIL-03728.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250213_190600_EMAIL-03728.eml) | 2025-02-13T19:06:00+00:00 |
| `20250214_142400_EMAIL-03733-eml` | email | [emails/2025-02/20250214_142400_EMAIL-03733.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250214_142400_EMAIL-03733.eml) | 2025-02-14T14:24:00+00:00 |
| `20250218_124900_EMAIL-03774-eml` | email | [emails/2025-02/20250218_124900_EMAIL-03774.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250218_124900_EMAIL-03774.eml) | 2025-02-18T12:49:00+00:00 |
| `20250504_171500_EMAIL-04435-eml` | email | [emails/2025-05/20250504_171500_EMAIL-04435.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250504_171500_EMAIL-04435.eml) | 2025-05-04T17:15:00+00:00 |
| `20250514_094500_EMAIL-04511-eml` | email | [emails/2025-05/20250514_094500_EMAIL-04511.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250514_094500_EMAIL-04511.eml) | 2025-05-14T09:45:00+00:00 |
| `20250516_084000_EMAIL-04530-eml` | email | [emails/2025-05/20250516_084000_EMAIL-04530.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250516_084000_EMAIL-04530.eml) | 2025-05-16T08:40:00+00:00 |
| `20250517_141900_EMAIL-04541-eml` | email | [emails/2025-05/20250517_141900_EMAIL-04541.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250517_141900_EMAIL-04541.eml) | 2025-05-17T14:19:00+00:00 |
| `20250519_141900_EMAIL-04563-eml` | email | [emails/2025-05/20250519_141900_EMAIL-04563.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250519_141900_EMAIL-04563.eml) | 2025-05-19T14:19:00+00:00 |
| `20250608_121200_EMAIL-04721-eml` | email | [emails/2025-06/20250608_121200_EMAIL-04721.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250608_121200_EMAIL-04721.eml) | 2025-06-08T12:12:00+00:00 |
| `20250710_095200_EMAIL-04990-eml` | email | [emails/2025-07/20250710_095200_EMAIL-04990.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250710_095200_EMAIL-04990.eml) | 2025-07-10T09:52:00+00:00 |
| `20250710_155200_EMAIL-04996-eml` | email | [emails/2025-07/20250710_155200_EMAIL-04996.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250710_155200_EMAIL-04996.eml) | 2025-07-10T15:52:00+00:00 |
| `20250711_112200_EMAIL-05001-eml` | email | [emails/2025-07/20250711_112200_EMAIL-05001.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250711_112200_EMAIL-05001.eml) | 2025-07-11T11:22:00+00:00 |
| `20250809_110400_EMAIL-05230-eml` | email | [emails/2025-08/20250809_110400_EMAIL-05230.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250809_110400_EMAIL-05230.eml) | 2025-08-09T11:04:00+00:00 |
| `20250809_204500_EMAIL-05240-eml` | email | [emails/2025-08/20250809_204500_EMAIL-05240.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250809_204500_EMAIL-05240.eml) | 2025-08-09T20:45:00+00:00 |
| `20250814_131000_EMAIL-05294-eml` | email | [emails/2025-08/20250814_131000_EMAIL-05294.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250814_131000_EMAIL-05294.eml) | 2025-08-14T13:10:00+00:00 |
| `20250816_041000_EMAIL-05310-eml` | email | [emails/2025-08/20250816_041000_EMAIL-05310.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250816_041000_EMAIL-05310.eml) | 2025-08-16T04:10:00+00:00 |
| `20250816_140300_EMAIL-05314-eml` | email | [emails/2025-08/20250816_140300_EMAIL-05314.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250816_140300_EMAIL-05314.eml) | 2025-08-16T14:03:00+00:00 |
| `20250824_094600_EMAIL-05390-eml` | email | [emails/2025-08/20250824_094600_EMAIL-05390.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250824_094600_EMAIL-05390.eml) | 2025-08-24T09:46:00+00:00 |
| `20250825_204600_EMAIL-05405-eml` | email | [emails/2025-08/20250825_204600_EMAIL-05405.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250825_204600_EMAIL-05405.eml) | 2025-08-25T20:46:00+00:00 |
| `20250902_133500_EMAIL-05499-eml` | email | [emails/2025-09/20250902_133500_EMAIL-05499.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250902_133500_EMAIL-05499.eml) | 2025-09-02T13:35:00+00:00 |
| `20250905_222100_EMAIL-05537-eml` | email | [emails/2025-09/20250905_222100_EMAIL-05537.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250905_222100_EMAIL-05537.eml) | 2025-09-05T22:21:00+00:00 |
| `20250907_172500_EMAIL-05563-eml` | email | [emails/2025-09/20250907_172500_EMAIL-05563.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250907_172500_EMAIL-05563.eml) | 2025-09-07T17:25:00+00:00 |
| `20250914_092900_EMAIL-05620-eml` | email | [emails/2025-09/20250914_092900_EMAIL-05620.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250914_092900_EMAIL-05620.eml) | 2025-09-14T09:29:00+00:00 |
| `20251004_171700_EMAIL-05780-eml` | email | [emails/2025-10/20251004_171700_EMAIL-05780.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251004_171700_EMAIL-05780.eml) | 2025-10-04T17:17:00+00:00 |
| `20251008_171500_EMAIL-05816-eml` | email | [emails/2025-10/20251008_171500_EMAIL-05816.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251008_171500_EMAIL-05816.eml) | 2025-10-08T17:15:00+00:00 |
| `20251009_131500_EMAIL-05822-eml` | email | [emails/2025-10/20251009_131500_EMAIL-05822.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251009_131500_EMAIL-05822.eml) | 2025-10-09T13:15:00+00:00 |
| `20251013_180500_EMAIL-05870-eml` | email | [emails/2025-10/20251013_180500_EMAIL-05870.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251013_180500_EMAIL-05870.eml) | 2025-10-13 |
| `20251014_144400_EMAIL-05881-eml` | email | [emails/2025-10/20251014_144400_EMAIL-05881.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251014_144400_EMAIL-05881.eml) | 2025-10-14T14:44:00+00:00 |
| `20251116_093100_EMAIL-06133-eml` | email | [emails/2025-11/20251116_093100_EMAIL-06133.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251116_093100_EMAIL-06133.eml) | 2025-11-16T09:31:00+00:00 |
| `20251201_145300_EMAIL-06275-eml` | email | [emails/2025-12/20251201_145300_EMAIL-06275.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251201_145300_EMAIL-06275.eml) | 2025-12-01T14:53:00+00:00 |
| `20251211_151500_EMAIL-06356-eml` | email | [emails/2025-12/20251211_151500_EMAIL-06356.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251211_151500_EMAIL-06356.eml) | 2025-12-11T15:15:00+00:00 |
| `20251224_103700_EMAIL-06481-eml` | email | [emails/2025-12/20251224_103700_EMAIL-06481.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251224_103700_EMAIL-06481.eml) | 2025-12-24T10:37:00+00:00 |
| `20251230_105500_EMAIL-06526-eml` | email | [emails/2025-12/20251230_105500_EMAIL-06526.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251230_105500_EMAIL-06526.eml) | 2025-12-30 |
| `20251230_105600_EMAIL-06527-eml` | email | [emails/2025-12/20251230_105600_EMAIL-06527.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251230_105600_EMAIL-06527.eml) | 2025-12-30 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-25T20:04:11+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
