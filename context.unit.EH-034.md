# context.unit.<!-- auto:unit_id -->EH-034<!-- /auto:unit_id -->.md

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
- owner_ref: `EIG-016`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit -->
- unit_id: `EH-034`
- label: WE 34
- haus_id: `HAUS-14`
- floor: 5. OG
- position: links
- typ: Wohnung
- area_sqm: 118.0
- rooms: 4.5
- mea_‰: 274
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
- lease_id: `LEASE-MIE-015`
- unit_ref: `EH-034`
- start_date: 2024-09-01 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-015)
- end_date: _(no data in source yet)_
- term_type: `unbefristet`
- cancellation_status: `by_tenant` (notice_date: 2025-08-02, move_out_date: —)
- rent_components: { kaltmiete: 2012.0, betriebskosten_vorauszahlung: 392.0, total_warmmiete: 2404.00 }
- payment_mode: Überweisung
- iban_payer: DE49370400443953394210 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-015)
- kaution: { amount: 6036.0 }
- usage: `residential`
- subletting: { current_status: `requested` }
- special_agreements: _(no data in source yet)_
<!-- /auto:lease -->

### 2.1 Tenants on this Lease
<!-- auto:tenants -->
| tenant_id | name | role | contact_email | contact_phone | comms_pref | gesamtschuldner |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-015` | Frau Hanna Schweitzer | haupt | hanna.schweitzer@gmx.de | 01370985931 | email | — |
<!-- /auto:tenants -->

---

## 3. Operations (this unit / this tenant)

### 3.1 Open Tickets — Critical (overdue or due ≤7 days)
<!-- auto:tickets.critical -->
| ticket_id | type | title | deadline | status | assignee |
| --- | --- | --- | --- | --- | --- |
| `TKT-758e6d03` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-8db041f7` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-3251bce9` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-f78e411a` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-d3165adf` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-51229d40` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-1ca2f0f0` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-5aee5437` | schimmel | Re: Schimmel im Schlafzimmer | — | open | — |
| `TKT-25ebd2d0` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-c4557698` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-1fb9eea6` | wasserschaden | Wasserschaden Bad | — | open | — |
<!-- /auto:tickets.critical -->

### 3.2 Open Tickets — Aggregate
<!-- auto:tickets.aggregate -->
- total_open: `33`
- by_type: { abfluss: `8`, fenster: `8`, schimmel: `5`, schluessel: `6`, wasserschaden: `6` }
- live source: `db.tickets WHERE unit_id=EH-034 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren (per claim)
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-015` | — | 1 | 9616.00 EUR | 2025-12-01 | — | — |
- live balance pointer: `db.tenant_balance.tenant_id=MIE-015`
<!-- /auto:dunning -->

### 3.4 Active Reductions / Deferrals (§ 536 BGB)
<!-- auto:reductions -->_(no data in source yet)_<!-- /auto:reductions -->

### 3.5 Latest Übergabeprotokoll
<!-- auto:handover -->_(no data in source yet)_<!-- /auto:handover -->

### 3.6 Recurring Process State (this unit, in-flight)
<!-- auto:recurring -->
| process_type | started | current_step | owner | eta | blockers |
| --- | --- | --- | --- | --- | --- |
| Mieterwechsel | 2025-08-02 | Kündigung erhalten | Verwaltung | TBD | Übergabe-Termin offen |
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
| `TH-52cf07` | Wohnung untervermieten | 2025-11-29 | `MIE-015` | active | 111 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251129_160600_EMAIL-06259.eml) |
| `TH-c1703b` | Verkaufsabsicht WE 34 | 2025-04-11 | `EH-034` | active | 6 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250411_103500_EMAIL-04265.eml) |
| `TH-e155be` | Mieterwechsel in WE 34 | 2025-05-28 | `EH-034` | active | 5 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250528_055500_EMAIL-04640.eml) |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `kontoauszug_2024_2025-csv` | bank | [bank/kontoauszug_2024_2025.csv](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv) | 2026-04-25 |
| `20240109_091300_EMAIL-00064-eml` | email | [emails/2024-01/20240109_091300_EMAIL-00064.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240109_091300_EMAIL-00064.eml) | 2024-01-09T09:13:00+00:00 |
| `20240109_121300_EMAIL-00069-eml` | email | [emails/2024-01/20240109_121300_EMAIL-00069.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240109_121300_EMAIL-00069.eml) | 2024-01-09T12:13:00+00:00 |
| `20240110_140400_EMAIL-00082-eml` | email | [emails/2024-01/20240110_140400_EMAIL-00082.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240110_140400_EMAIL-00082.eml) | 2024-01-10T14:04:00+00:00 |
| `20240127_172300_EMAIL-00218-eml` | email | [emails/2024-01/20240127_172300_EMAIL-00218.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240127_172300_EMAIL-00218.eml) | 2024-01-27T17:23:00+00:00 |
| `20240216_080600_EMAIL-00395-eml` | email | [emails/2024-02/20240216_080600_EMAIL-00395.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240216_080600_EMAIL-00395.eml) | 2024-02-16T08:06:00+00:00 |
| `20240223_135500_EMAIL-00454-eml` | email | [emails/2024-02/20240223_135500_EMAIL-00454.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240223_135500_EMAIL-00454.eml) | 2024-02-23T13:55:00+00:00 |
| `20240303_182300_EMAIL-00539-eml` | email | [emails/2024-03/20240303_182300_EMAIL-00539.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240303_182300_EMAIL-00539.eml) | 2024-03-03T18:23:00+00:00 |
| `20240304_100700_EMAIL-00543-eml` | email | [emails/2024-03/20240304_100700_EMAIL-00543.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240304_100700_EMAIL-00543.eml) | 2024-03-04T10:07:00+00:00 |
| `20240305_182300_EMAIL-00558-eml` | email | [emails/2024-03/20240305_182300_EMAIL-00558.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240305_182300_EMAIL-00558.eml) | 2024-03-05T18:23:00+00:00 |
| `20240305_230700_EMAIL-00559-eml` | email | [emails/2024-03/20240305_230700_EMAIL-00559.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240305_230700_EMAIL-00559.eml) | 2024-03-05T23:07:00+00:00 |
| `20240310_230700_EMAIL-00610-eml` | email | [emails/2024-03/20240310_230700_EMAIL-00610.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240310_230700_EMAIL-00610.eml) | 2024-03-10T23:07:00+00:00 |
| `20240322_124900_EMAIL-00708-eml` | email | [emails/2024-03/20240322_124900_EMAIL-00708.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240322_124900_EMAIL-00708.eml) | 2024-03-22T12:49:00+00:00 |
| `20240407_101600_EMAIL-00853-eml` | email | [emails/2024-04/20240407_101600_EMAIL-00853.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240407_101600_EMAIL-00853.eml) | 2024-04-07T10:16:00+00:00 |
| `20240411_161900_EMAIL-00904-eml` | email | [emails/2024-04/20240411_161900_EMAIL-00904.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240411_161900_EMAIL-00904.eml) | 2024-04-11T16:19:00+00:00 |
| `20240412_031900_EMAIL-00907-eml` | email | [emails/2024-04/20240412_031900_EMAIL-00907.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240412_031900_EMAIL-00907.eml) | 2024-04-12T03:19:00+00:00 |
| `20240412_164000_EMAIL-00920-eml` | email | [emails/2024-04/20240412_164000_EMAIL-00920.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240412_164000_EMAIL-00920.eml) | 2024-04-12T16:40:00+00:00 |
| `20240419_082700_EMAIL-00981-eml` | email | [emails/2024-04/20240419_082700_EMAIL-00981.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240419_082700_EMAIL-00981.eml) | 2024-04-19T08:27:00+00:00 |
| `20240419_140400_EMAIL-00988-eml` | email | [emails/2024-04/20240419_140400_EMAIL-00988.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240419_140400_EMAIL-00988.eml) | 2024-04-19T14:04:00+00:00 |
| `20240420_144100_EMAIL-01000-eml` | email | [emails/2024-04/20240420_144100_EMAIL-01000.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240420_144100_EMAIL-01000.eml) | 2024-04-20T14:41:00+00:00 |
| `20240427_165300_EMAIL-01057-eml` | email | [emails/2024-04/20240427_165300_EMAIL-01057.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240427_165300_EMAIL-01057.eml) | 2024-04-27T16:53:00+00:00 |
| `20240527_145000_EMAIL-01317-eml` | email | [emails/2024-05/20240527_145000_EMAIL-01317.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240527_145000_EMAIL-01317.eml) | 2024-05-27T14:50:00+00:00 |
| `20240601_121500_EMAIL-01373-eml` | email | [emails/2024-06/20240601_121500_EMAIL-01373.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240601_121500_EMAIL-01373.eml) | 2024-06-01T12:15:00+00:00 |
| `20240605_165800_EMAIL-01413-eml` | email | [emails/2024-06/20240605_165800_EMAIL-01413.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240605_165800_EMAIL-01413.eml) | 2024-06-05T16:58:00+00:00 |
| `20240617_154600_EMAIL-01518-eml` | email | [emails/2024-06/20240617_154600_EMAIL-01518.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240617_154600_EMAIL-01518.eml) | 2024-06-17T15:46:00+00:00 |
| `20240726_142100_EMAIL-01874-eml` | email | [emails/2024-07/20240726_142100_EMAIL-01874.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240726_142100_EMAIL-01874.eml) | 2024-07-26T14:21:00+00:00 |
| `20240816_130800_EMAIL-02058-eml` | email | [emails/2024-08/20240816_130800_EMAIL-02058.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240816_130800_EMAIL-02058.eml) | 2024-08-16T13:08:00+00:00 |
| `20240817_050800_EMAIL-02065-eml` | email | [emails/2024-08/20240817_050800_EMAIL-02065.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240817_050800_EMAIL-02065.eml) | 2024-08-17T05:08:00+00:00 |
| `20240930_164200_EMAIL-02485-eml` | email | [emails/2024-09/20240930_164200_EMAIL-02485.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240930_164200_EMAIL-02485.eml) | 2024-09-30T16:42:00+00:00 |
| `20241006_105200_EMAIL-02534-eml` | email | [emails/2024-10/20241006_105200_EMAIL-02534.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241006_105200_EMAIL-02534.eml) | 2024-10-06T10:52:00+00:00 |
| `20241007_181200_EMAIL-02552-eml` | email | [emails/2024-10/20241007_181200_EMAIL-02552.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241007_181200_EMAIL-02552.eml) | 2024-10-07T18:12:00+00:00 |
| `20241019_094000_EMAIL-02653-eml` | email | [emails/2024-10/20241019_094000_EMAIL-02653.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241019_094000_EMAIL-02653.eml) | 2024-10-19T09:40:00+00:00 |
| `20241024_174700_EMAIL-02709-eml` | email | [emails/2024-10/20241024_174700_EMAIL-02709.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241024_174700_EMAIL-02709.eml) | 2024-10-24T17:47:00+00:00 |
| `20241024_204700_EMAIL-02712-eml` | email | [emails/2024-10/20241024_204700_EMAIL-02712.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241024_204700_EMAIL-02712.eml) | 2024-10-24T20:47:00+00:00 |
| `20241027_081800_EMAIL-02733-eml` | email | [emails/2024-10/20241027_081800_EMAIL-02733.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241027_081800_EMAIL-02733.eml) | 2024-10-27T08:18:00+00:00 |
| `20241107_085900_EMAIL-02838-eml` | email | [emails/2024-11/20241107_085900_EMAIL-02838.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241107_085900_EMAIL-02838.eml) | 2024-11-07T08:59:00+00:00 |
| `20241113_125400_EMAIL-02892-eml` | email | [emails/2024-11/20241113_125400_EMAIL-02892.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241113_125400_EMAIL-02892.eml) | 2024-11-13T12:54:00+00:00 |
| `20241114_215400_EMAIL-02912-eml` | email | [emails/2024-11/20241114_215400_EMAIL-02912.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241114_215400_EMAIL-02912.eml) | 2024-11-14T21:54:00+00:00 |
| `20241122_103100_EMAIL-02973-eml` | email | [emails/2024-11/20241122_103100_EMAIL-02973.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241122_103100_EMAIL-02973.eml) | 2024-11-22T10:31:00+00:00 |
| `20241203_115000_EMAIL-03072-eml` | email | [emails/2024-12/20241203_115000_EMAIL-03072.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241203_115000_EMAIL-03072.eml) | 2024-12-03T11:50:00+00:00 |
| `20241211_134400_EMAIL-03148-eml` | email | [emails/2024-12/20241211_134400_EMAIL-03148.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241211_134400_EMAIL-03148.eml) | 2024-12-11T13:44:00+00:00 |
| `20241213_123700_EMAIL-03166-eml` | email | [emails/2024-12/20241213_123700_EMAIL-03166.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241213_123700_EMAIL-03166.eml) | 2024-12-13T12:37:00+00:00 |
| `20241214_090600_EMAIL-03171-eml` | email | [emails/2024-12/20241214_090600_EMAIL-03171.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241214_090600_EMAIL-03171.eml) | 2024-12-14T09:06:00+00:00 |
| `20241218_103500_EMAIL-03201-eml` | email | [emails/2024-12/20241218_103500_EMAIL-03201.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241218_103500_EMAIL-03201.eml) | 2024-12-18T10:35:00+00:00 |
| `20241219_092500_EMAIL-03212-eml` | email | [emails/2024-12/20241219_092500_EMAIL-03212.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241219_092500_EMAIL-03212.eml) | 2024-12-19T09:25:00+00:00 |
| `20241224_100800_EMAIL-03258-eml` | email | [emails/2024-12/20241224_100800_EMAIL-03258.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241224_100800_EMAIL-03258.eml) | 2024-12-24T10:08:00+00:00 |
| `20241227_142500_EMAIL-03291-eml` | email | [emails/2024-12/20241227_142500_EMAIL-03291.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241227_142500_EMAIL-03291.eml) | 2024-12-27T14:25:00+00:00 |
| `20250102_103700_EMAIL-03356-eml` | email | [emails/2025-01/20250102_103700_EMAIL-03356.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250102_103700_EMAIL-03356.eml) | 2025-01-02T10:37:00+00:00 |
| `20250103_163700_EMAIL-03369-eml` | email | [emails/2025-01/20250103_163700_EMAIL-03369.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250103_163700_EMAIL-03369.eml) | 2025-01-03T16:37:00+00:00 |
| `20250106_145200_EMAIL-03397-eml` | email | [emails/2025-01/20250106_145200_EMAIL-03397.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250106_145200_EMAIL-03397.eml) | 2025-01-06T14:52:00+00:00 |
| `20250107_145000_EMAIL-03405-eml` | email | [emails/2025-01/20250107_145000_EMAIL-03405.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250107_145000_EMAIL-03405.eml) | 2025-01-07T14:50:00+00:00 |
| `20250107_150500_EMAIL-03406-eml` | email | [emails/2025-01/20250107_150500_EMAIL-03406.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250107_150500_EMAIL-03406.eml) | 2025-01-07T15:05:00+00:00 |
| `20250109_050500_EMAIL-03419-eml` | email | [emails/2025-01/20250109_050500_EMAIL-03419.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250109_050500_EMAIL-03419.eml) | 2025-01-09T05:05:00+00:00 |
| `20250109_140900_EMAIL-03424-eml` | email | [emails/2025-01/20250109_140900_EMAIL-03424.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250109_140900_EMAIL-03424.eml) | 2025-01-09T14:09:00+00:00 |
| `20250114_110300_EMAIL-03472-eml` | email | [emails/2025-01/20250114_110300_EMAIL-03472.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250114_110300_EMAIL-03472.eml) | 2025-01-14T11:03:00+00:00 |
| `20250114_124800_EMAIL-03475-eml` | email | [emails/2025-01/20250114_124800_EMAIL-03475.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250114_124800_EMAIL-03475.eml) | 2025-01-14T12:48:00+00:00 |
| `20250118_111200_EMAIL-03503-eml` | email | [emails/2025-01/20250118_111200_EMAIL-03503.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250118_111200_EMAIL-03503.eml) | 2025-01-18T11:12:00+00:00 |
| `20250129_112700_EMAIL-03591-eml` | email | [emails/2025-01/20250129_112700_EMAIL-03591.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250129_112700_EMAIL-03591.eml) | 2025-01-29T11:27:00+00:00 |
| `20250202_114800_EMAIL-03629-eml` | email | [emails/2025-02/20250202_114800_EMAIL-03629.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250202_114800_EMAIL-03629.eml) | 2025-02-02T11:48:00+00:00 |
| `20250212_074800_EMAIL-03701-eml` | email | [emails/2025-02/20250212_074800_EMAIL-03701.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250212_074800_EMAIL-03701.eml) | 2025-02-12T07:48:00+00:00 |
| `20250317_004400_EMAIL-04035-eml` | email | [emails/2025-03/20250317_004400_EMAIL-04035.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250317_004400_EMAIL-04035.eml) | 2025-03-17T00:44:00+00:00 |
| `20250328_155900_EMAIL-04146-eml` | email | [emails/2025-03/20250328_155900_EMAIL-04146.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250328_155900_EMAIL-04146.eml) | 2025-03-28T15:59:00+00:00 |
| `20250329_165900_EMAIL-04152-eml` | email | [emails/2025-03/20250329_165900_EMAIL-04152.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250329_165900_EMAIL-04152.eml) | 2025-03-29T16:59:00+00:00 |
| `20250411_103500_EMAIL-04265-eml` | email | [emails/2025-04/20250411_103500_EMAIL-04265.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250411_103500_EMAIL-04265.eml) | 2025-04-11 |
| `20250503_153500_EMAIL-04427-eml` | email | [emails/2025-05/20250503_153500_EMAIL-04427.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250503_153500_EMAIL-04427.eml) | 2025-05-03T15:35:00+00:00 |
| `20250505_165900_EMAIL-04442-eml` | email | [emails/2025-05/20250505_165900_EMAIL-04442.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250505_165900_EMAIL-04442.eml) | 2025-05-05T16:59:00+00:00 |
| `20250521_165800_EMAIL-04584-eml` | email | [emails/2025-05/20250521_165800_EMAIL-04584.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250521_165800_EMAIL-04584.eml) | 2025-05-21T16:58:00+00:00 |
| `20250528_055500_EMAIL-04640-eml` | email | [emails/2025-05/20250528_055500_EMAIL-04640.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250528_055500_EMAIL-04640.eml) | 2025-05-28T05:55:00+00:00 |
| `20250616_113300_EMAIL-04792-eml` | email | [emails/2025-06/20250616_113300_EMAIL-04792.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250616_113300_EMAIL-04792.eml) | 2025-06-16T11:33:00+00:00 |
| `20250630_121900_EMAIL-04911-eml` | email | [emails/2025-06/20250630_121900_EMAIL-04911.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250630_121900_EMAIL-04911.eml) | 2025-06-30T12:19:00+00:00 |
| `20250703_183700_EMAIL-04939-eml` | email | [emails/2025-07/20250703_183700_EMAIL-04939.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250703_183700_EMAIL-04939.eml) | 2025-07-03T18:37:00+00:00 |
| `20250709_170800_EMAIL-04986-eml` | email | [emails/2025-07/20250709_170800_EMAIL-04986.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250709_170800_EMAIL-04986.eml) | 2025-07-09T17:08:00+00:00 |
| `20250712_160800_EMAIL-05015-eml` | email | [emails/2025-07/20250712_160800_EMAIL-05015.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250712_160800_EMAIL-05015.eml) | 2025-07-12T16:08:00+00:00 |
| `20250713_132300_EMAIL-05021-eml` | email | [emails/2025-07/20250713_132300_EMAIL-05021.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250713_132300_EMAIL-05021.eml) | 2025-07-13T13:23:00+00:00 |
| `20250713_132600_EMAIL-05022-eml` | email | [emails/2025-07/20250713_132600_EMAIL-05022.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250713_132600_EMAIL-05022.eml) | 2025-07-13T13:26:00+00:00 |
| `20250714_232600_EMAIL-05039-eml` | email | [emails/2025-07/20250714_232600_EMAIL-05039.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250714_232600_EMAIL-05039.eml) | 2025-07-14T23:26:00+00:00 |
| `20250721_204000_EMAIL-05107-eml` | email | [emails/2025-07/20250721_204000_EMAIL-05107.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250721_204000_EMAIL-05107.eml) | 2025-07-21T20:40:00+00:00 |
| `20250723_164000_EMAIL-05124-eml` | email | [emails/2025-07/20250723_164000_EMAIL-05124.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250723_164000_EMAIL-05124.eml) | 2025-07-23T16:40:00+00:00 |
| `20250726_120400_EMAIL-05133-eml` | email | [emails/2025-07/20250726_120400_EMAIL-05133.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250726_120400_EMAIL-05133.eml) | 2025-07-26T12:04:00+00:00 |
| `20250802_164000_EMAIL-05188-eml` | email | [emails/2025-08/20250802_164000_EMAIL-05188.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250802_164000_EMAIL-05188.eml) | 2025-08-02T16:40:00+00:00 |
| `20250804_144600_EMAIL-05199-eml` | email | [emails/2025-08/20250804_144600_EMAIL-05199.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250804_144600_EMAIL-05199.eml) | 2025-08-04T14:46:00+00:00 |
| `20250806_153000_EMAIL-05213-eml` | email | [emails/2025-08/20250806_153000_EMAIL-05213.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250806_153000_EMAIL-05213.eml) | 2025-08-06T15:30:00+00:00 |
| `20250821_114000_EMAIL-05363-eml` | email | [emails/2025-08/20250821_114000_EMAIL-05363.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250821_114000_EMAIL-05363.eml) | 2025-08-21T11:40:00+00:00 |
| `20250821_150800_EMAIL-05366-eml` | email | [emails/2025-08/20250821_150800_EMAIL-05366.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250821_150800_EMAIL-05366.eml) | 2025-08-21T15:08:00+00:00 |
| `20250830_101500_EMAIL-05454-eml` | email | [emails/2025-08/20250830_101500_EMAIL-05454.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250830_101500_EMAIL-05454.eml) | 2025-08-30T10:15:00+00:00 |
| `20250901_140200_EMAIL-05479-eml` | email | [emails/2025-09/20250901_140200_EMAIL-05479.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250901_140200_EMAIL-05479.eml) | 2025-09-01T14:02:00+00:00 |
| `20250903_123000_EMAIL-05507-eml` | email | [emails/2025-09/20250903_123000_EMAIL-05507.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250903_123000_EMAIL-05507.eml) | 2025-09-03T12:30:00+00:00 |
| `20250903_223000_EMAIL-05513-eml` | email | [emails/2025-09/20250903_223000_EMAIL-05513.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250903_223000_EMAIL-05513.eml) | 2025-09-03T22:30:00+00:00 |
| `20250909_115000_EMAIL-05579-eml` | email | [emails/2025-09/20250909_115000_EMAIL-05579.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250909_115000_EMAIL-05579.eml) | 2025-09-09T11:50:00+00:00 |
| `20250925_125300_EMAIL-05714-eml` | email | [emails/2025-09/20250925_125300_EMAIL-05714.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250925_125300_EMAIL-05714.eml) | 2025-09-25T12:53:00+00:00 |
| `20251003_225300_EMAIL-05776-eml` | email | [emails/2025-10/20251003_225300_EMAIL-05776.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251003_225300_EMAIL-05776.eml) | 2025-10-03T22:53:00+00:00 |
| `20251106_154700_EMAIL-06066-eml` | email | [emails/2025-11/20251106_154700_EMAIL-06066.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251106_154700_EMAIL-06066.eml) | 2025-11-06T15:47:00+00:00 |
| `20251122_114900_EMAIL-06189-eml` | email | [emails/2025-11/20251122_114900_EMAIL-06189.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251122_114900_EMAIL-06189.eml) | 2025-11-22T11:49:00+00:00 |
| `20251126_111400_EMAIL-06226-eml` | email | [emails/2025-11/20251126_111400_EMAIL-06226.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251126_111400_EMAIL-06226.eml) | 2025-11-26T11:14:00+00:00 |
| `20251127_171400_EMAIL-06245-eml` | email | [emails/2025-11/20251127_171400_EMAIL-06245.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251127_171400_EMAIL-06245.eml) | 2025-11-27T17:14:00+00:00 |
| `20251129_160600_EMAIL-06259-eml` | email | [emails/2025-11/20251129_160600_EMAIL-06259.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251129_160600_EMAIL-06259.eml) | 2025-11-29 |
| `20251208_145800_EMAIL-06326-eml` | email | [emails/2025-12/20251208_145800_EMAIL-06326.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251208_145800_EMAIL-06326.eml) | 2025-12-08T14:58:00+00:00 |
| `20251223_140400_EMAIL-06474-eml` | email | [emails/2025-12/20251223_140400_EMAIL-06474.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251223_140400_EMAIL-06474.eml) | 2025-12-23T14:04:00+00:00 |
| `20251223_150600_EMAIL-06476-eml` | email | [emails/2025-12/20251223_150600_EMAIL-06476.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251223_150600_EMAIL-06476.eml) | 2025-12-23T15:06:00+00:00 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-25T20:04:11+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
