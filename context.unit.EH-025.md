# context.unit.<!-- auto:unit_id -->EH-025<!-- /auto:unit_id -->.md

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
- owner_ref: `EIG-003`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit -->
- unit_id: `EH-025`
- label: WE 25
- haus_id: `HAUS-14`
- floor: 3. OG
- position: links
- typ: Wohnung
- area_sqm: 109.0
- rooms: 4.0
- mea_‰: 253
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
- lease_id: `LEASE-MIE-001`
- unit_ref: `EH-025`
- start_date: 2022-07-11 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-001)
- end_date: _(no data in source yet)_
- term_type: `unbefristet`
- cancellation_status: `by_tenant` (notice_date: 2025-11-03, move_out_date: —)
- rent_components: { kaltmiete: 1403.0, betriebskosten_vorauszahlung: 273.0, total_warmmiete: 1676.00 }
- payment_mode: Überweisung
- iban_payer: DE94120300004034471349 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-001)
- kaution: { amount: 4209.0 }
- usage: `residential`
- subletting: { current_status: `requested` }
- special_agreements: _(no data in source yet)_
<!-- /auto:lease -->

### 2.1 Tenants on this Lease
<!-- auto:tenants -->
| tenant_id | name | role | contact_email | contact_phone | comms_pref | gesamtschuldner |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-001` | Herr Julius Nette | haupt | julius.nette@outlook.com | 05886753396 | email | — |
<!-- /auto:tenants -->

---

## 3. Operations (this unit / this tenant)

### 3.1 Open Tickets — Critical (overdue or due ≤7 days)
<!-- auto:tickets.critical -->
| ticket_id | type | title | deadline | status | assignee |
| --- | --- | --- | --- | --- | --- |
| `TKT-7fc724d9` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-640bf0c5` | wasserschaden | Re: Wasserschaden Bad | — | open | — |
| `TKT-ceca4f9f` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-c9da00e6` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-b3f37dc0` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-84525b23` | wasserschaden | Re: Water damage in bathroom | — | open | — |
| `TKT-be9d9e89` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-ca82883d` | schimmel | Re: Schimmel im Schlafzimmer | — | open | — |
| `TKT-41bb8a54` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-406ce4aa` | wasserschaden | Re: Water damage in bathroom | — | open | — |
| `TKT-428b042b` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-1904a63d` | wasserschaden | Wasserschaden Bad | — | open | — |
<!-- /auto:tickets.critical -->

### 3.2 Open Tickets — Aggregate
<!-- auto:tickets.aggregate -->
- total_open: `21`
- by_type: { abfluss: `3`, fenster: `2`, schimmel: `4`, schluessel: `4`, wasserschaden: `8` }
- live source: `db.tickets WHERE unit_id=EH-025 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren (per claim)
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-001` | — | 1 | 6704.00 EUR | 2025-12-01 | — | — |
- live balance pointer: `db.tenant_balance.tenant_id=MIE-001`
<!-- /auto:dunning -->

### 3.4 Active Reductions / Deferrals (§ 536 BGB)
<!-- auto:reductions -->
- date_raised: 2024-09-07
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
| Mieterwechsel | 2025-11-03 | Kündigung erhalten | Verwaltung | TBD | Übergabe-Termin offen |
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
| `20240302_103200_EMAIL-00526-eml` | email | [emails/2024-03/20240302_103200_EMAIL-00526.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240302_103200_EMAIL-00526.eml) | 2024-03-02T10:32:00+00:00 |
| `20240315_132300_EMAIL-00650-eml` | email | [emails/2024-03/20240315_132300_EMAIL-00650.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240315_132300_EMAIL-00650.eml) | 2024-03-15T13:23:00+00:00 |
| `20240317_145000_EMAIL-00664-eml` | email | [emails/2024-03/20240317_145000_EMAIL-00664.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240317_145000_EMAIL-00664.eml) | 2024-03-17T14:50:00+00:00 |
| `20240318_065000_EMAIL-00671-eml` | email | [emails/2024-03/20240318_065000_EMAIL-00671.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240318_065000_EMAIL-00671.eml) | 2024-03-18T06:50:00+00:00 |
| `20240328_111700_EMAIL-00752-eml` | email | [emails/2024-03/20240328_111700_EMAIL-00752.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240328_111700_EMAIL-00752.eml) | 2024-03-28T11:17:00+00:00 |
| `20240331_135300_EMAIL-00780-eml` | email | [emails/2024-03/20240331_135300_EMAIL-00780.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240331_135300_EMAIL-00780.eml) | 2024-03-31T13:53:00+00:00 |
| `20240402_110500_EMAIL-00801-eml` | email | [emails/2024-04/20240402_110500_EMAIL-00801.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240402_110500_EMAIL-00801.eml) | 2024-04-02T11:05:00+00:00 |
| `20240407_111900_EMAIL-00854-eml` | email | [emails/2024-04/20240407_111900_EMAIL-00854.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240407_111900_EMAIL-00854.eml) | 2024-04-07T11:19:00+00:00 |
| `20240421_174900_EMAIL-01009-eml` | email | [emails/2024-04/20240421_174900_EMAIL-01009.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240421_174900_EMAIL-01009.eml) | 2024-04-21T17:49:00+00:00 |
| `20240422_154900_EMAIL-01017-eml` | email | [emails/2024-04/20240422_154900_EMAIL-01017.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240422_154900_EMAIL-01017.eml) | 2024-04-22T15:49:00+00:00 |
| `20240513_160100_EMAIL-01201-eml` | email | [emails/2024-05/20240513_160100_EMAIL-01201.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240513_160100_EMAIL-01201.eml) | 2024-05-13T16:01:00+00:00 |
| `20240513_230100_EMAIL-01209-eml` | email | [emails/2024-05/20240513_230100_EMAIL-01209.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240513_230100_EMAIL-01209.eml) | 2024-05-13T23:01:00+00:00 |
| `20240517_114200_EMAIL-01238-eml` | email | [emails/2024-05/20240517_114200_EMAIL-01238.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240517_114200_EMAIL-01238.eml) | 2024-05-17T11:42:00+00:00 |
| `20240522_122600_EMAIL-01279-eml` | email | [emails/2024-05/20240522_122600_EMAIL-01279.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240522_122600_EMAIL-01279.eml) | 2024-05-22T12:26:00+00:00 |
| `20240526_125600_EMAIL-01306-eml` | email | [emails/2024-05/20240526_125600_EMAIL-01306.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240526_125600_EMAIL-01306.eml) | 2024-05-26T12:56:00+00:00 |
| `20240609_095700_EMAIL-01440-eml` | email | [emails/2024-06/20240609_095700_EMAIL-01440.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240609_095700_EMAIL-01440.eml) | 2024-06-09T09:57:00+00:00 |
| `20240621_145600_EMAIL-01559-eml` | email | [emails/2024-06/20240621_145600_EMAIL-01559.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240621_145600_EMAIL-01559.eml) | 2024-06-21T14:56:00+00:00 |
| `20240623_105700_EMAIL-01570-eml` | email | [emails/2024-06/20240623_105700_EMAIL-01570.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240623_105700_EMAIL-01570.eml) | 2024-06-23T10:57:00+00:00 |
| `20240709_225900_EMAIL-01717-eml` | email | [emails/2024-07/20240709_225900_EMAIL-01717.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240709_225900_EMAIL-01717.eml) | 2024-07-09T22:59:00+00:00 |
| `20240711_155900_EMAIL-01733-eml` | email | [emails/2024-07/20240711_155900_EMAIL-01733.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240711_155900_EMAIL-01733.eml) | 2024-07-11T15:59:00+00:00 |
| `20240812_113600_EMAIL-02019-eml` | email | [emails/2024-08/20240812_113600_EMAIL-02019.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240812_113600_EMAIL-02019.eml) | 2024-08-12T11:36:00+00:00 |
| `20240816_100900_EMAIL-02055-eml` | email | [emails/2024-08/20240816_100900_EMAIL-02055.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240816_100900_EMAIL-02055.eml) | 2024-08-16T10:09:00+00:00 |
| `20240830_141600_EMAIL-02192-eml` | email | [emails/2024-08/20240830_141600_EMAIL-02192.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240830_141600_EMAIL-02192.eml) | 2024-08-30T14:16:00+00:00 |
| `20240830_154300_EMAIL-02193-eml` | email | [emails/2024-08/20240830_154300_EMAIL-02193.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240830_154300_EMAIL-02193.eml) | 2024-08-30T15:43:00+00:00 |
| `20240831_011600_EMAIL-02199-eml` | email | [emails/2024-08/20240831_011600_EMAIL-02199.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240831_011600_EMAIL-02199.eml) | 2024-08-31T01:16:00+00:00 |
| `20240904_094000_EMAIL-02236-eml` | email | [emails/2024-09/20240904_094000_EMAIL-02236.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240904_094000_EMAIL-02236.eml) | 2024-09-04T09:40:00+00:00 |
| `20240907_185600_EMAIL-02282-eml` | email | [emails/2024-09/20240907_185600_EMAIL-02282.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240907_185600_EMAIL-02282.eml) | 2024-09-07T18:56:00+00:00 |
| `20240909_175600_EMAIL-02305-eml` | email | [emails/2024-09/20240909_175600_EMAIL-02305.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240909_175600_EMAIL-02305.eml) | 2024-09-09T17:56:00+00:00 |
| `20240922_165300_EMAIL-02415-eml` | email | [emails/2024-09/20240922_165300_EMAIL-02415.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240922_165300_EMAIL-02415.eml) | 2024-09-22T16:53:00+00:00 |
| `20240928_143000_EMAIL-02473-eml` | email | [emails/2024-09/20240928_143000_EMAIL-02473.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240928_143000_EMAIL-02473.eml) | 2024-09-28T14:30:00+00:00 |
| `20241015_163300_EMAIL-02620-eml` | email | [emails/2024-10/20241015_163300_EMAIL-02620.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241015_163300_EMAIL-02620.eml) | 2024-10-15T16:33:00+00:00 |
| `20241018_111000_EMAIL-02645-eml` | email | [emails/2024-10/20241018_111000_EMAIL-02645.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241018_111000_EMAIL-02645.eml) | 2024-10-18T11:10:00+00:00 |
| `20241019_181000_EMAIL-02657-eml` | email | [emails/2024-10/20241019_181000_EMAIL-02657.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241019_181000_EMAIL-02657.eml) | 2024-10-19T18:10:00+00:00 |
| `20241106_140900_EMAIL-02836-eml` | email | [emails/2024-11/20241106_140900_EMAIL-02836.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241106_140900_EMAIL-02836.eml) | 2024-11-06T14:09:00+00:00 |
| `20241109_154000_EMAIL-02858-eml` | email | [emails/2024-11/20241109_154000_EMAIL-02858.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241109_154000_EMAIL-02858.eml) | 2024-11-09T15:40:00+00:00 |
| `20241124_090700_EMAIL-02996-eml` | email | [emails/2024-11/20241124_090700_EMAIL-02996.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241124_090700_EMAIL-02996.eml) | 2024-11-24T09:07:00+00:00 |
| `20241226_095600_EMAIL-03279-eml` | email | [emails/2024-12/20241226_095600_EMAIL-03279.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241226_095600_EMAIL-03279.eml) | 2024-12-26T09:56:00+00:00 |
| `20241227_235600_EMAIL-03296-eml` | email | [emails/2024-12/20241227_235600_EMAIL-03296.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241227_235600_EMAIL-03296.eml) | 2024-12-27T23:56:00+00:00 |
| `20241231_115400_EMAIL-03329-eml` | email | [emails/2024-12/20241231_115400_EMAIL-03329.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241231_115400_EMAIL-03329.eml) | 2024-12-31T11:54:00+00:00 |
| `20250105_175400_EMAIL-03391-eml` | email | [emails/2025-01/20250105_175400_EMAIL-03391.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250105_175400_EMAIL-03391.eml) | 2025-01-05T17:54:00+00:00 |
| `20250113_135100_EMAIL-03456-eml` | email | [emails/2025-01/20250113_135100_EMAIL-03456.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250113_135100_EMAIL-03456.eml) | 2025-01-13T13:51:00+00:00 |
| `20250124_111000_EMAIL-03549-eml` | email | [emails/2025-01/20250124_111000_EMAIL-03549.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250124_111000_EMAIL-03549.eml) | 2025-01-24T11:10:00+00:00 |
| `20250130_132000_EMAIL-03604-eml` | email | [emails/2025-01/20250130_132000_EMAIL-03604.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250130_132000_EMAIL-03604.eml) | 2025-01-30T13:20:00+00:00 |
| `20250205_100300_EMAIL-03648-eml` | email | [emails/2025-02/20250205_100300_EMAIL-03648.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250205_100300_EMAIL-03648.eml) | 2025-02-05T10:03:00+00:00 |
| `20250205_120300_EMAIL-03650-eml` | email | [emails/2025-02/20250205_120300_EMAIL-03650.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250205_120300_EMAIL-03650.eml) | 2025-02-05T12:03:00+00:00 |
| `20250222_105800_EMAIL-03810-eml` | email | [emails/2025-02/20250222_105800_EMAIL-03810.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250222_105800_EMAIL-03810.eml) | 2025-02-22T10:58:00+00:00 |
| `20250309_115200_EMAIL-03965-eml` | email | [emails/2025-03/20250309_115200_EMAIL-03965.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250309_115200_EMAIL-03965.eml) | 2025-03-09T11:52:00+00:00 |
| `20250320_115200_EMAIL-04072-eml` | email | [emails/2025-03/20250320_115200_EMAIL-04072.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250320_115200_EMAIL-04072.eml) | 2025-03-20T11:52:00+00:00 |
| `20250321_195200_EMAIL-04085-eml` | email | [emails/2025-03/20250321_195200_EMAIL-04085.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250321_195200_EMAIL-04085.eml) | 2025-03-21T19:52:00+00:00 |
| `20250408_144100_EMAIL-04240-eml` | email | [emails/2025-04/20250408_144100_EMAIL-04240.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250408_144100_EMAIL-04240.eml) | 2025-04-08T14:41:00+00:00 |
| `20250507_142100_EMAIL-04453-eml` | email | [emails/2025-05/20250507_142100_EMAIL-04453.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250507_142100_EMAIL-04453.eml) | 2025-05-07T14:21:00+00:00 |
| `20250510_154200_EMAIL-04476-eml` | email | [emails/2025-05/20250510_154200_EMAIL-04476.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250510_154200_EMAIL-04476.eml) | 2025-05-10T15:42:00+00:00 |
| `20250604_112100_EMAIL-04701-eml` | email | [emails/2025-06/20250604_112100_EMAIL-04701.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250604_112100_EMAIL-04701.eml) | 2025-06-04T11:21:00+00:00 |
| `20250613_171400_EMAIL-04765-eml` | email | [emails/2025-06/20250613_171400_EMAIL-04765.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250613_171400_EMAIL-04765.eml) | 2025-06-13T17:14:00+00:00 |
| `20250618_124200_EMAIL-04808-eml` | email | [emails/2025-06/20250618_124200_EMAIL-04808.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250618_124200_EMAIL-04808.eml) | 2025-06-18T12:42:00+00:00 |
| `20250618_133900_EMAIL-04809-eml` | email | [emails/2025-06/20250618_133900_EMAIL-04809.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250618_133900_EMAIL-04809.eml) | 2025-06-18T13:39:00+00:00 |
| `20250619_223900_EMAIL-04822-eml` | email | [emails/2025-06/20250619_223900_EMAIL-04822.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250619_223900_EMAIL-04822.eml) | 2025-06-19T22:39:00+00:00 |
| `20250719_142800_EMAIL-05084-eml` | email | [emails/2025-07/20250719_142800_EMAIL-05084.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250719_142800_EMAIL-05084.eml) | 2025-07-19T14:28:00+00:00 |
| `20250722_171500_EMAIL-05116-eml` | email | [emails/2025-07/20250722_171500_EMAIL-05116.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250722_171500_EMAIL-05116.eml) | 2025-07-22T17:15:00+00:00 |
| `20250831_162100_EMAIL-05469-eml` | email | [emails/2025-08/20250831_162100_EMAIL-05469.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250831_162100_EMAIL-05469.eml) | 2025-08-31T16:21:00+00:00 |
| `20250911_155900_EMAIL-05598-eml` | email | [emails/2025-09/20250911_155900_EMAIL-05598.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250911_155900_EMAIL-05598.eml) | 2025-09-11T15:59:00+00:00 |
| `20251003_101500_EMAIL-05762-eml` | email | [emails/2025-10/20251003_101500_EMAIL-05762.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251003_101500_EMAIL-05762.eml) | 2025-10-03T10:15:00+00:00 |
| `20251007_154100_EMAIL-05806-eml` | email | [emails/2025-10/20251007_154100_EMAIL-05806.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251007_154100_EMAIL-05806.eml) | 2025-10-07T15:41:00+00:00 |
| `20251009_124100_EMAIL-05821-eml` | email | [emails/2025-10/20251009_124100_EMAIL-05821.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251009_124100_EMAIL-05821.eml) | 2025-10-09T12:41:00+00:00 |
| `20251103_142500_EMAIL-06035-eml` | email | [emails/2025-11/20251103_142500_EMAIL-06035.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251103_142500_EMAIL-06035.eml) | 2025-11-03T14:25:00+00:00 |
| `20251104_102000_EMAIL-06038-eml` | email | [emails/2025-11/20251104_102000_EMAIL-06038.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251104_102000_EMAIL-06038.eml) | 2025-11-04T10:20:00+00:00 |
| `20251127_124200_EMAIL-06239-eml` | email | [emails/2025-11/20251127_124200_EMAIL-06239.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251127_124200_EMAIL-06239.eml) | 2025-11-27T12:42:00+00:00 |
| `20251208_152900_EMAIL-06328-eml` | email | [emails/2025-12/20251208_152900_EMAIL-06328.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251208_152900_EMAIL-06328.eml) | 2025-12-08T15:29:00+00:00 |
| `20251215_104800_EMAIL-06401-eml` | email | [emails/2025-12/20251215_104800_EMAIL-06401.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251215_104800_EMAIL-06401.eml) | 2025-12-15T10:48:00+00:00 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-25T20:04:11+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
