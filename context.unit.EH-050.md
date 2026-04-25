# context.unit.<!-- auto:unit_id -->EH-050<!-- /auto:unit_id -->.md

> Per-unit dossier (one file per Einheit). Holds everything specific to this unit:
> the unit itself, the active lease, the tenant(s), and all unit/tenant-specific operations.
> **Property-wide data lives in `context.property.md`** — see `parent_property_ref` below.

<!-- auto:meta -->
- last_built_at: `2026-04-25T20:53:16+00:00`
- build_hash: `engine-v2`
- engine_version: `0.2.0`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `unit`
- unit_id: `EH-050`
- property_id: `LIE-001`
- parent_property_ref: `context.property.LIE-001.md`
- owner_ref: `EIG-010`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit -->
- unit_id: `EH-050`
- label: WE 50
- haus_id: `HAUS-16`
- floor: 4. OG
- position: rechts
- typ: Wohnung
- area_sqm: 59.0
- rooms: 2.0
- mea_‰: 137
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
- lease_id: `LEASE-MIE-019`
- unit_ref: `EH-050`
- start_date: 2020-07-18 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-019)
- end_date: _(no data in source yet)_
- term_type: `unbefristet`
- cancellation_status: `by_tenant` (notice_date: 2025-05-11, move_out_date: —)
- rent_components: { kaltmiete: 827.0, betriebskosten_vorauszahlung: 179.0, total_warmmiete: 1006.00 }
- payment_mode: Überweisung
- iban_payer: DE72100700002675869261 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-019)
- kaution: { amount: 2481.0 }
- usage: `residential`
- subletting: { current_status: `requested` }
- special_agreements: _(no data in source yet)_
<!-- /auto:lease -->

### 2.1 Tenants on this Lease
<!-- auto:tenants -->
| tenant_id | name | role | contact_email | contact_phone | comms_pref | gesamtschuldner |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-019` | Herr Jörgen Seidel | haupt | joergen.seidel@gmx.de | 00643171390 | email | — |
<!-- /auto:tenants -->

---

## 3. Operations (this unit / this tenant)

### 3.1 Open Tickets — Critical (overdue or due ≤7 days)
<!-- auto:tickets.critical -->
| ticket_id | type | title | deadline | status | assignee |
| --- | --- | --- | --- | --- | --- |
| `TKT-da660243` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-134a699e` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-68743749` | schimmel | Re: Schimmel im Schlafzimmer | — | open | — |
| `TKT-0ce18596` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-0ef6407e` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-3ebe5a2a` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-6e81f8e8` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-6c9cc913` | wasserschaden | Wasserschaden Bad | — | open | — |
<!-- /auto:tickets.critical -->

### 3.2 Open Tickets — Aggregate
<!-- auto:tickets.aggregate -->
- total_open: `28`
- by_type: { abfluss: `7`, fenster: `4`, schimmel: `5`, schluessel: `9`, wasserschaden: `3` }
- live source: `db.tickets WHERE unit_id=EH-050 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren

<!-- auto:dunning.summary -->[Routine] Mieter MIE-019 ist seit vier Monaten im Verzug; offener Betrag 4.024,00 EUR zzgl. 51,54 EUR Verzugszinsen, letzte Zahlung 2025-12-03 [(bank)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv#TX-01586). Vertraglich geschuldet sind monatlich 1.006,00 EUR (Kaltmiete 827,00 EUR + NK 179,00 EUR) [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-019). Verzug nach § 286 BGB, Verzugszinsen § 288 I BGB; Mahnstufe 1 aktiv, 2. Mahnung nach 14 Tagen fällig.<!-- /auto:dunning.summary -->

#### Per claim
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-019` | — | 1 | 4024.00 EUR | 2025-12-03 | — | — |
- live balance pointer: `db.tenant_balance.tenant_id=MIE-019`
<!-- /auto:dunning -->

### 3.4 Active Reductions / Deferrals (§ 536 BGB)
<!-- auto:reductions -->
- date_raised: 2024-01-20
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-03-13
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-09-26
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
| Mieterwechsel | 2025-05-11 | Kündigung erhalten | Verwaltung | TBD | Übergabe-Termin offen |
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
| `TH-a5e111` | Heizung faellt aus | 2025-12-12 | `MIE-019` | active | 140 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251212_160400_EMAIL-06370.eml) |
| `TH-853401` | Verkaufsabsicht WE 50 | 2025-07-20 | `EH-050` | active | 8 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250720_133000_EMAIL-05096.eml) |
| `TH-05414a` | Mieterwechsel in WE 50 | 2024-12-15 | `EH-050` | active | 3 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241215_053900_EMAIL-03178.eml) |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `kontoauszug_2024_2025-csv` | bank | [bank/kontoauszug_2024_2025.csv](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv) | 2026-04-25 |
| `20240108_163400_EMAIL-00059-eml` | email | [emails/2024-01/20240108_163400_EMAIL-00059.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240108_163400_EMAIL-00059.eml) | 2024-01-08T16:34:00+00:00 |
| `20240110_092000_EMAIL-00078-eml` | email | [emails/2024-01/20240110_092000_EMAIL-00078.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240110_092000_EMAIL-00078.eml) | 2024-01-10T09:20:00+00:00 |
| `20240113_155800_EMAIL-00112-eml` | email | [emails/2024-01/20240113_155800_EMAIL-00112.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240113_155800_EMAIL-00112.eml) | 2024-01-13T15:58:00+00:00 |
| `20240115_173500_EMAIL-00128-eml` | email | [emails/2024-01/20240115_173500_EMAIL-00128.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240115_173500_EMAIL-00128.eml) | 2024-01-15T17:35:00+00:00 |
| `20240120_162300_EMAIL-00164-eml` | email | [emails/2024-01/20240120_162300_EMAIL-00164.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240120_162300_EMAIL-00164.eml) | 2024-01-20T16:23:00+00:00 |
| `20240129_102800_EMAIL-00230-eml` | email | [emails/2024-01/20240129_102800_EMAIL-00230.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240129_102800_EMAIL-00230.eml) | 2024-01-29T10:28:00+00:00 |
| `20240130_212800_EMAIL-00247-eml` | email | [emails/2024-01/20240130_212800_EMAIL-00247.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240130_212800_EMAIL-00247.eml) | 2024-01-30T21:28:00+00:00 |
| `20240206_123700_EMAIL-00315-eml` | email | [emails/2024-02/20240206_123700_EMAIL-00315.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240206_123700_EMAIL-00315.eml) | 2024-02-06T12:37:00+00:00 |
| `20240206_223700_EMAIL-00320-eml` | email | [emails/2024-02/20240206_223700_EMAIL-00320.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240206_223700_EMAIL-00320.eml) | 2024-02-06T22:37:00+00:00 |
| `20240212_091000_EMAIL-00358-eml` | email | [emails/2024-02/20240212_091000_EMAIL-00358.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240212_091000_EMAIL-00358.eml) | 2024-02-12T09:10:00+00:00 |
| `20240219_111000_EMAIL-00412-eml` | email | [emails/2024-02/20240219_111000_EMAIL-00412.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240219_111000_EMAIL-00412.eml) | 2024-02-19T11:10:00+00:00 |
| `20240220_171000_EMAIL-00429-eml` | email | [emails/2024-02/20240220_171000_EMAIL-00429.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240220_171000_EMAIL-00429.eml) | 2024-02-20T17:10:00+00:00 |
| `20240224_105700_EMAIL-00459-eml` | email | [emails/2024-02/20240224_105700_EMAIL-00459.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240224_105700_EMAIL-00459.eml) | 2024-02-24T10:57:00+00:00 |
| `20240310_122200_EMAIL-00603-eml` | email | [emails/2024-03/20240310_122200_EMAIL-00603.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240310_122200_EMAIL-00603.eml) | 2024-03-10T12:22:00+00:00 |
| `20240316_130200_EMAIL-00661-eml` | email | [emails/2024-03/20240316_130200_EMAIL-00661.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240316_130200_EMAIL-00661.eml) | 2024-03-16T13:02:00+00:00 |
| `20240327_143500_EMAIL-00745-eml` | email | [emails/2024-03/20240327_143500_EMAIL-00745.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240327_143500_EMAIL-00745.eml) | 2024-03-27T14:35:00+00:00 |
| `20240402_194200_EMAIL-00808-eml` | email | [emails/2024-04/20240402_194200_EMAIL-00808.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240402_194200_EMAIL-00808.eml) | 2024-04-02T19:42:00+00:00 |
| `20240410_100600_EMAIL-00881-eml` | email | [emails/2024-04/20240410_100600_EMAIL-00881.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240410_100600_EMAIL-00881.eml) | 2024-04-10T10:06:00+00:00 |
| `20240416_134400_EMAIL-00957-eml` | email | [emails/2024-04/20240416_134400_EMAIL-00957.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240416_134400_EMAIL-00957.eml) | 2024-04-16T13:44:00+00:00 |
| `20240419_092700_EMAIL-00982-eml` | email | [emails/2024-04/20240419_092700_EMAIL-00982.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240419_092700_EMAIL-00982.eml) | 2024-04-19T09:27:00+00:00 |
| `20240423_152900_EMAIL-01026-eml` | email | [emails/2024-04/20240423_152900_EMAIL-01026.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240423_152900_EMAIL-01026.eml) | 2024-04-23T15:29:00+00:00 |
| `20240423_192900_EMAIL-01030-eml` | email | [emails/2024-04/20240423_192900_EMAIL-01030.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240423_192900_EMAIL-01030.eml) | 2024-04-23T19:29:00+00:00 |
| `20240518_113200_EMAIL-01247-eml` | email | [emails/2024-05/20240518_113200_EMAIL-01247.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240518_113200_EMAIL-01247.eml) | 2024-05-18T11:32:00+00:00 |
| `20240524_224800_EMAIL-01296-eml` | email | [emails/2024-05/20240524_224800_EMAIL-01296.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240524_224800_EMAIL-01296.eml) | 2024-05-24T22:48:00+00:00 |
| `20240526_154800_EMAIL-01310-eml` | email | [emails/2024-05/20240526_154800_EMAIL-01310.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240526_154800_EMAIL-01310.eml) | 2024-05-26T15:48:00+00:00 |
| `20240529_125000_EMAIL-01340-eml` | email | [emails/2024-05/20240529_125000_EMAIL-01340.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240529_125000_EMAIL-01340.eml) | 2024-05-29T12:50:00+00:00 |
| `20240601_154800_EMAIL-01377-eml` | email | [emails/2024-06/20240601_154800_EMAIL-01377.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240601_154800_EMAIL-01377.eml) | 2024-06-01T15:48:00+00:00 |
| `20240618_161800_EMAIL-01531-eml` | email | [emails/2024-06/20240618_161800_EMAIL-01531.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240618_161800_EMAIL-01531.eml) | 2024-06-18T16:18:00+00:00 |
| `20240621_145400_EMAIL-01558-eml` | email | [emails/2024-06/20240621_145400_EMAIL-01558.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240621_145400_EMAIL-01558.eml) | 2024-06-21T14:54:00+00:00 |
| `20240627_120000_EMAIL-01600-eml` | email | [emails/2024-06/20240627_120000_EMAIL-01600.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240627_120000_EMAIL-01600.eml) | 2024-06-27T12:00:00+00:00 |
| `20240704_102300_EMAIL-01648-eml` | email | [emails/2024-07/20240704_102300_EMAIL-01648.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240704_102300_EMAIL-01648.eml) | 2024-07-04T10:23:00+00:00 |
| `20240716_161000_EMAIL-01784-eml` | email | [emails/2024-07/20240716_161000_EMAIL-01784.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240716_161000_EMAIL-01784.eml) | 2024-07-16T16:10:00+00:00 |
| `20240718_061000_EMAIL-01797-eml` | email | [emails/2024-07/20240718_061000_EMAIL-01797.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240718_061000_EMAIL-01797.eml) | 2024-07-18T06:10:00+00:00 |
| `20240806_110200_EMAIL-01979-eml` | email | [emails/2024-08/20240806_110200_EMAIL-01979.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240806_110200_EMAIL-01979.eml) | 2024-08-06T11:02:00+00:00 |
| `20240822_180200_EMAIL-02125-eml` | email | [emails/2024-08/20240822_180200_EMAIL-02125.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240822_180200_EMAIL-02125.eml) | 2024-08-22T18:02:00+00:00 |
| `20240827_110800_EMAIL-02168-eml` | email | [emails/2024-08/20240827_110800_EMAIL-02168.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240827_110800_EMAIL-02168.eml) | 2024-08-27T11:08:00+00:00 |
| `20240831_174400_EMAIL-02207-eml` | email | [emails/2024-08/20240831_174400_EMAIL-02207.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240831_174400_EMAIL-02207.eml) | 2024-08-31T17:44:00+00:00 |
| `20240908_135100_EMAIL-02290-eml` | email | [emails/2024-09/20240908_135100_EMAIL-02290.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240908_135100_EMAIL-02290.eml) | 2024-09-08T13:51:00+00:00 |
| `20240912_104300_EMAIL-02323-eml` | email | [emails/2024-09/20240912_104300_EMAIL-02323.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240912_104300_EMAIL-02323.eml) | 2024-09-12T10:43:00+00:00 |
| `20240912_160400_EMAIL-02333-eml` | email | [emails/2024-09/20240912_160400_EMAIL-02333.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240912_160400_EMAIL-02333.eml) | 2024-09-12T16:04:00+00:00 |
| `20240920_200400_EMAIL-02393-eml` | email | [emails/2024-09/20240920_200400_EMAIL-02393.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240920_200400_EMAIL-02393.eml) | 2024-09-20T20:04:00+00:00 |
| `20240921_131000_EMAIL-02399-eml` | email | [emails/2024-09/20240921_131000_EMAIL-02399.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240921_131000_EMAIL-02399.eml) | 2024-09-21T13:10:00+00:00 |
| `20241004_112400_EMAIL-02512-eml` | email | [emails/2024-10/20241004_112400_EMAIL-02512.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241004_112400_EMAIL-02512.eml) | 2024-10-04T11:24:00+00:00 |
| `20241004_174400_EMAIL-02521-eml` | email | [emails/2024-10/20241004_174400_EMAIL-02521.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241004_174400_EMAIL-02521.eml) | 2024-10-04T17:44:00+00:00 |
| `20241023_153500_EMAIL-02701-eml` | email | [emails/2024-10/20241023_153500_EMAIL-02701.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241023_153500_EMAIL-02701.eml) | 2024-10-23T15:35:00+00:00 |
| `20241025_114100_EMAIL-02718-eml` | email | [emails/2024-10/20241025_114100_EMAIL-02718.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241025_114100_EMAIL-02718.eml) | 2024-10-25T11:41:00+00:00 |
| `20241215_053900_EMAIL-03178-eml` | email | [emails/2024-12/20241215_053900_EMAIL-03178.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241215_053900_EMAIL-03178.eml) | 2024-12-15T05:39:00+00:00 |
| `20241224_141300_EMAIL-03262-eml` | email | [emails/2024-12/20241224_141300_EMAIL-03262.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241224_141300_EMAIL-03262.eml) | 2024-12-24T14:13:00+00:00 |
| `20241225_161700_EMAIL-03275-eml` | email | [emails/2024-12/20241225_161700_EMAIL-03275.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241225_161700_EMAIL-03275.eml) | 2024-12-25T16:17:00+00:00 |
| `20250205_163800_EMAIL-03657-eml` | email | [emails/2025-02/20250205_163800_EMAIL-03657.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250205_163800_EMAIL-03657.eml) | 2025-02-05T16:38:00+00:00 |
| `20250213_152800_EMAIL-03723-eml` | email | [emails/2025-02/20250213_152800_EMAIL-03723.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250213_152800_EMAIL-03723.eml) | 2025-02-13T15:28:00+00:00 |
| `20250225_102600_EMAIL-03846-eml` | email | [emails/2025-02/20250225_102600_EMAIL-03846.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250225_102600_EMAIL-03846.eml) | 2025-02-25T10:26:00+00:00 |
| `20250306_121800_EMAIL-03933-eml` | email | [emails/2025-03/20250306_121800_EMAIL-03933.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250306_121800_EMAIL-03933.eml) | 2025-03-06T12:18:00+00:00 |
| `20250313_104500_EMAIL-04000-eml` | email | [emails/2025-03/20250313_104500_EMAIL-04000.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250313_104500_EMAIL-04000.eml) | 2025-03-13T10:45:00+00:00 |
| `20250314_201800_EMAIL-04014-eml` | email | [emails/2025-03/20250314_201800_EMAIL-04014.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250314_201800_EMAIL-04014.eml) | 2025-03-14T20:18:00+00:00 |
| `20250323_130900_EMAIL-04105-eml` | email | [emails/2025-03/20250323_130900_EMAIL-04105.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250323_130900_EMAIL-04105.eml) | 2025-03-23T13:09:00+00:00 |
| `20250405_141400_EMAIL-04211-eml` | email | [emails/2025-04/20250405_141400_EMAIL-04211.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250405_141400_EMAIL-04211.eml) | 2025-04-05T14:14:00+00:00 |
| `20250406_121400_EMAIL-04219-eml` | email | [emails/2025-04/20250406_121400_EMAIL-04219.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250406_121400_EMAIL-04219.eml) | 2025-04-06T12:14:00+00:00 |
| `20250417_182600_EMAIL-04317-eml` | email | [emails/2025-04/20250417_182600_EMAIL-04317.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250417_182600_EMAIL-04317.eml) | 2025-04-17T18:26:00+00:00 |
| `20250427_121500_EMAIL-04380-eml` | email | [emails/2025-04/20250427_121500_EMAIL-04380.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250427_121500_EMAIL-04380.eml) | 2025-04-27T12:15:00+00:00 |
| `20250511_101700_EMAIL-04484-eml` | email | [emails/2025-05/20250511_101700_EMAIL-04484.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250511_101700_EMAIL-04484.eml) | 2025-05-11T10:17:00+00:00 |
| `20250511_131700_EMAIL-04487-eml` | email | [emails/2025-05/20250511_131700_EMAIL-04487.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250511_131700_EMAIL-04487.eml) | 2025-05-11T13:17:00+00:00 |
| `20250527_115700_EMAIL-04634-eml` | email | [emails/2025-05/20250527_115700_EMAIL-04634.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250527_115700_EMAIL-04634.eml) | 2025-05-27T11:57:00+00:00 |
| `20250602_164700_EMAIL-04693-eml` | email | [emails/2025-06/20250602_164700_EMAIL-04693.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250602_164700_EMAIL-04693.eml) | 2025-06-02T16:47:00+00:00 |
| `20250701_150600_EMAIL-04922-eml` | email | [emails/2025-07/20250701_150600_EMAIL-04922.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250701_150600_EMAIL-04922.eml) | 2025-07-01T15:06:00+00:00 |
| `20250702_000600_EMAIL-04927-eml` | email | [emails/2025-07/20250702_000600_EMAIL-04927.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250702_000600_EMAIL-04927.eml) | 2025-07-02T00:06:00+00:00 |
| `20250705_000600_EMAIL-04949-eml` | email | [emails/2025-07/20250705_000600_EMAIL-04949.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250705_000600_EMAIL-04949.eml) | 2025-07-05T00:06:00+00:00 |
| `20250714_184000_EMAIL-05037-eml` | email | [emails/2025-07/20250714_184000_EMAIL-05037.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250714_184000_EMAIL-05037.eml) | 2025-07-14T18:40:00+00:00 |
| `20250720_133000_EMAIL-05096-eml` | email | [emails/2025-07/20250720_133000_EMAIL-05096.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250720_133000_EMAIL-05096.eml) | 2025-07-20 |
| `20250824_105200_EMAIL-05392-eml` | email | [emails/2025-08/20250824_105200_EMAIL-05392.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250824_105200_EMAIL-05392.eml) | 2025-08-24T10:52:00+00:00 |
| `20250830_153200_EMAIL-05457-eml` | email | [emails/2025-08/20250830_153200_EMAIL-05457.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250830_153200_EMAIL-05457.eml) | 2025-08-30T15:32:00+00:00 |
| `20250920_145000_EMAIL-05668-eml` | email | [emails/2025-09/20250920_145000_EMAIL-05668.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250920_145000_EMAIL-05668.eml) | 2025-09-20T14:50:00+00:00 |
| `20250921_152100_EMAIL-05679-eml` | email | [emails/2025-09/20250921_152100_EMAIL-05679.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250921_152100_EMAIL-05679.eml) | 2025-09-21T15:21:00+00:00 |
| `20250924_114600_EMAIL-05698-eml` | email | [emails/2025-09/20250924_114600_EMAIL-05698.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250924_114600_EMAIL-05698.eml) | 2025-09-24T11:46:00+00:00 |
| `20250926_160700_EMAIL-05724-eml` | email | [emails/2025-09/20250926_160700_EMAIL-05724.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250926_160700_EMAIL-05724.eml) | 2025-09-26T16:07:00+00:00 |
| `20250928_114500_EMAIL-05733-eml` | email | [emails/2025-09/20250928_114500_EMAIL-05733.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250928_114500_EMAIL-05733.eml) | 2025-09-28T11:45:00+00:00 |
| `20251013_090200_EMAIL-05856-eml` | email | [emails/2025-10/20251013_090200_EMAIL-05856.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251013_090200_EMAIL-05856.eml) | 2025-10-13T09:02:00+00:00 |
| `20251017_133100_EMAIL-05895-eml` | email | [emails/2025-10/20251017_133100_EMAIL-05895.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251017_133100_EMAIL-05895.eml) | 2025-10-17T13:31:00+00:00 |
| `20251019_023100_EMAIL-05910-eml` | email | [emails/2025-10/20251019_023100_EMAIL-05910.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251019_023100_EMAIL-05910.eml) | 2025-10-19T02:31:00+00:00 |
| `20251023_152600_EMAIL-05951-eml` | email | [emails/2025-10/20251023_152600_EMAIL-05951.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251023_152600_EMAIL-05951.eml) | 2025-10-23T15:26:00+00:00 |
| `20251105_153900_EMAIL-06053-eml` | email | [emails/2025-11/20251105_153900_EMAIL-06053.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251105_153900_EMAIL-06053.eml) | 2025-11-05T15:39:00+00:00 |
| `20251106_233900_EMAIL-06070-eml` | email | [emails/2025-11/20251106_233900_EMAIL-06070.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251106_233900_EMAIL-06070.eml) | 2025-11-06T23:39:00+00:00 |
| `20251201_113100_EMAIL-06272-eml` | email | [emails/2025-12/20251201_113100_EMAIL-06272.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251201_113100_EMAIL-06272.eml) | 2025-12-01T11:31:00+00:00 |
| `20251212_160400_EMAIL-06370-eml` | email | [emails/2025-12/20251212_160400_EMAIL-06370.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251212_160400_EMAIL-06370.eml) | 2025-12-12 |
| `20251231_164200_EMAIL-06544-eml` | email | [emails/2025-12/20251231_164200_EMAIL-06544.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251231_164200_EMAIL-06544.eml) | 2025-12-31T16:42:00+00:00 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-25T20:52:09+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
