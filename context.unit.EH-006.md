# context.unit.<!-- auto:unit_id -->EH-006<!-- /auto:unit_id -->.md

> Per-unit dossier (one file per Einheit). Holds everything specific to this unit:
> the unit itself, the active lease, the tenant(s), and all unit/tenant-specific operations.
> **Property-wide data lives in `context.property.md`** — see `parent_property_ref` below.

<!-- auto:meta -->
- last_built_at: `2026-04-25T20:52:23+00:00`
- build_hash: `engine-v2`
- engine_version: `0.2.0`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `unit`
- unit_id: `EH-006`
- property_id: `LIE-001`
- parent_property_ref: `context.property.LIE-001.md`
- owner_ref: `EIG-035`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit -->
- unit_id: `EH-006`
- label: WE 06
- haus_id: `HAUS-12`
- floor: 2. OG
- position: rechts
- typ: Wohnung
- area_sqm: 51.0
- rooms: 1.5
- mea_‰: 118
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
- lease_id: `LEASE-MIE-026`
- unit_ref: `EH-006`
- start_date: 2020-07-16 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-026)
- end_date: _(no data in source yet)_
- term_type: `unbefristet`
- cancellation_status: `by_tenant` (notice_date: 2025-05-05, move_out_date: —)
- rent_components: { kaltmiete: 850.0, betriebskosten_vorauszahlung: 133.0, total_warmmiete: 983.00 }
- payment_mode: Überweisung
- iban_payer: DE95370400442809885165 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-026)
- kaution: { amount: 2550.0 }
- usage: `residential`
- subletting: { current_status: `requested` }
- special_agreements: _(no data in source yet)_
<!-- /auto:lease -->

### 2.1 Tenants on this Lease
<!-- auto:tenants -->
| tenant_id | name | role | contact_email | contact_phone | comms_pref | gesamtschuldner |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-026` | Herr Kamil Trub | haupt | kamil.trub@gmx.de | 06984789611 | email | — |
<!-- /auto:tenants -->

---

## 3. Operations (this unit / this tenant)

### 3.1 Open Tickets — Critical (overdue or due ≤7 days)
<!-- auto:tickets.critical -->
| ticket_id | type | title | deadline | status | assignee |
| --- | --- | --- | --- | --- | --- |
| `TKT-ba95f37d` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-ef4a1b82` | wasserschaden | Re: Wasserschaden Bad | — | open | — |
| `TKT-01d7239f` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-d60b9f88` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-ae677a23` | wasserschaden | Wasserschaden Bad | — | open | — |
<!-- /auto:tickets.critical -->

### 3.2 Open Tickets — Aggregate
<!-- auto:tickets.aggregate -->
- total_open: `14`
- by_type: { abfluss: `3`, fenster: `2`, schimmel: `1`, schluessel: `4`, wasserschaden: `4` }
- live source: `db.tickets WHERE unit_id=EH-006 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren

<!-- auto:dunning.summary -->[Routine] Mieter MIE-026 ist seit vier Monaten im Verzug; offener Betrag 3.932,00 EUR zzgl. 50,36 EUR Verzugszinsen, letzte Zahlung 2025-12-02 [(bank)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv#TX-01567). Vertraglich geschuldet sind monatlich 983,00 EUR (Kaltmiete 850,00 EUR + NK 133,00 EUR) [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-026). Verzug nach § 286 BGB festgestellt, Verzugszinsen § 288 I BGB (Basiszins + 5pp); Mahnstufe 1, nächster Schritt: 2. Mahnung nach 14 Tagen.<!-- /auto:dunning.summary -->

#### Per claim
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-026` | — | 1 | 3932.00 EUR | 2025-12-02 | — | — |
- live balance pointer: `db.tenant_balance.tenant_id=MIE-026`
<!-- /auto:dunning -->

### 3.4 Active Reductions / Deferrals (§ 536 BGB)
<!-- auto:reductions -->
- date_raised: 2024-02-08
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-02-09
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-10-12
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-10-23
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
| Mieterwechsel | 2025-05-05 | Kündigung erhalten | Verwaltung | TBD | Übergabe-Termin offen |
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
| `TH-b8e979` | Mieterwechsel in WE 06 | 2025-06-26 | `EH-006` | active | 12 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250626_152000_EMAIL-04882.eml) |
| `TH-6c404e` | Verkaufsabsicht WE 06 | 2025-04-01 | `EH-006` | active | 10 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250401_061100_EMAIL-04175.eml) |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `kontoauszug_2024_2025-csv` | bank | [bank/kontoauszug_2024_2025.csv](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv) | 2026-04-25 |
| `20240115_103200_EMAIL-00121-eml` | email | [emails/2024-01/20240115_103200_EMAIL-00121.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240115_103200_EMAIL-00121.eml) | 2024-01-15T10:32:00+00:00 |
| `20240119_115000_EMAIL-00151-eml` | email | [emails/2024-01/20240119_115000_EMAIL-00151.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240119_115000_EMAIL-00151.eml) | 2024-01-19T11:50:00+00:00 |
| `20240204_154000_EMAIL-00302-eml` | email | [emails/2024-02/20240204_154000_EMAIL-00302.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240204_154000_EMAIL-00302.eml) | 2024-02-04T15:40:00+00:00 |
| `20240208_165000_EMAIL-00335-eml` | email | [emails/2024-02/20240208_165000_EMAIL-00335.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240208_165000_EMAIL-00335.eml) | 2024-02-08T16:50:00+00:00 |
| `20240209_155000_EMAIL-00345-eml` | email | [emails/2024-02/20240209_155000_EMAIL-00345.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240209_155000_EMAIL-00345.eml) | 2024-02-09T15:50:00+00:00 |
| `20240220_132000_EMAIL-00424-eml` | email | [emails/2024-02/20240220_132000_EMAIL-00424.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240220_132000_EMAIL-00424.eml) | 2024-02-20T13:20:00+00:00 |
| `20240311_161600_EMAIL-00619-eml` | email | [emails/2024-03/20240311_161600_EMAIL-00619.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240311_161600_EMAIL-00619.eml) | 2024-03-11T16:16:00+00:00 |
| `20240311_165800_EMAIL-00620-eml` | email | [emails/2024-03/20240311_165800_EMAIL-00620.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240311_165800_EMAIL-00620.eml) | 2024-03-11T16:58:00+00:00 |
| `20240329_161700_EMAIL-00769-eml` | email | [emails/2024-03/20240329_161700_EMAIL-00769.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240329_161700_EMAIL-00769.eml) | 2024-03-29T16:17:00+00:00 |
| `20240519_161000_EMAIL-01253-eml` | email | [emails/2024-05/20240519_161000_EMAIL-01253.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240519_161000_EMAIL-01253.eml) | 2024-05-19T16:10:00+00:00 |
| `20240521_011000_EMAIL-01265-eml` | email | [emails/2024-05/20240521_011000_EMAIL-01265.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240521_011000_EMAIL-01265.eml) | 2024-05-21T01:10:00+00:00 |
| `20240524_154700_EMAIL-01295-eml` | email | [emails/2024-05/20240524_154700_EMAIL-01295.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240524_154700_EMAIL-01295.eml) | 2024-05-24T15:47:00+00:00 |
| `20240612_115800_EMAIL-01475-eml` | email | [emails/2024-06/20240612_115800_EMAIL-01475.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240612_115800_EMAIL-01475.eml) | 2024-06-12T11:58:00+00:00 |
| `20240706_101500_EMAIL-01671-eml` | email | [emails/2024-07/20240706_101500_EMAIL-01671.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240706_101500_EMAIL-01671.eml) | 2024-07-06T10:15:00+00:00 |
| `20240709_023800_EMAIL-01701-eml` | email | [emails/2024-07/20240709_023800_EMAIL-01701.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240709_023800_EMAIL-01701.eml) | 2024-07-09T02:38:00+00:00 |
| `20240726_121200_EMAIL-01870-eml` | email | [emails/2024-07/20240726_121200_EMAIL-01870.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240726_121200_EMAIL-01870.eml) | 2024-07-26T12:12:00+00:00 |
| `20240907_182400_EMAIL-02281-eml` | email | [emails/2024-09/20240907_182400_EMAIL-02281.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240907_182400_EMAIL-02281.eml) | 2024-09-07T18:24:00+00:00 |
| `20241003_162700_EMAIL-02506-eml` | email | [emails/2024-10/20241003_162700_EMAIL-02506.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241003_162700_EMAIL-02506.eml) | 2024-10-03T16:27:00+00:00 |
| `20241005_072700_EMAIL-02525-eml` | email | [emails/2024-10/20241005_072700_EMAIL-02525.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241005_072700_EMAIL-02525.eml) | 2024-10-05T07:27:00+00:00 |
| `20241007_153400_EMAIL-02544-eml` | email | [emails/2024-10/20241007_153400_EMAIL-02544.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241007_153400_EMAIL-02544.eml) | 2024-10-07T15:34:00+00:00 |
| `20241028_152800_EMAIL-02747-eml` | email | [emails/2024-10/20241028_152800_EMAIL-02747.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241028_152800_EMAIL-02747.eml) | 2024-10-28T15:28:00+00:00 |
| `20241102_094700_EMAIL-02794-eml` | email | [emails/2024-11/20241102_094700_EMAIL-02794.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241102_094700_EMAIL-02794.eml) | 2024-11-02T09:47:00+00:00 |
| `20241121_180200_EMAIL-02968-eml` | email | [emails/2024-11/20241121_180200_EMAIL-02968.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241121_180200_EMAIL-02968.eml) | 2024-11-21T18:02:00+00:00 |
| `20241122_070200_EMAIL-02971-eml` | email | [emails/2024-11/20241122_070200_EMAIL-02971.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241122_070200_EMAIL-02971.eml) | 2024-11-22T07:02:00+00:00 |
| `20241122_230300_EMAIL-02981-eml` | email | [emails/2024-11/20241122_230300_EMAIL-02981.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241122_230300_EMAIL-02981.eml) | 2024-11-22T23:03:00+00:00 |
| `20241201_113000_EMAIL-03056-eml` | email | [emails/2024-12/20241201_113000_EMAIL-03056.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241201_113000_EMAIL-03056.eml) | 2024-12-01T11:30:00+00:00 |
| `20241214_102300_EMAIL-03173-eml` | email | [emails/2024-12/20241214_102300_EMAIL-03173.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241214_102300_EMAIL-03173.eml) | 2024-12-14T10:23:00+00:00 |
| `20241222_152200_EMAIL-03241-eml` | email | [emails/2024-12/20241222_152200_EMAIL-03241.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241222_152200_EMAIL-03241.eml) | 2024-12-22T15:22:00+00:00 |
| `20250116_103300_EMAIL-03485-eml` | email | [emails/2025-01/20250116_103300_EMAIL-03485.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250116_103300_EMAIL-03485.eml) | 2025-01-16T10:33:00+00:00 |
| `20250118_134100_EMAIL-03504-eml` | email | [emails/2025-01/20250118_134100_EMAIL-03504.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250118_134100_EMAIL-03504.eml) | 2025-01-18T13:41:00+00:00 |
| `20250219_110600_EMAIL-03782-eml` | email | [emails/2025-02/20250219_110600_EMAIL-03782.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250219_110600_EMAIL-03782.eml) | 2025-02-19T11:06:00+00:00 |
| `20250330_141100_EMAIL-04160-eml` | email | [emails/2025-03/20250330_141100_EMAIL-04160.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250330_141100_EMAIL-04160.eml) | 2025-03-30T14:11:00+00:00 |
| `20250331_075400_EMAIL-04164-eml` | email | [emails/2025-03/20250331_075400_EMAIL-04164.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250331_075400_EMAIL-04164.eml) | 2025-03-31T07:54:00+00:00 |
| `20250401_061100_EMAIL-04175-eml` | email | [emails/2025-04/20250401_061100_EMAIL-04175.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250401_061100_EMAIL-04175.eml) | 2025-04-01T06:11:00+00:00 |
| `20250416_094100_EMAIL-04303-eml` | email | [emails/2025-04/20250416_094100_EMAIL-04303.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250416_094100_EMAIL-04303.eml) | 2025-04-16T09:41:00+00:00 |
| `20250417_184100_EMAIL-04318-eml` | email | [emails/2025-04/20250417_184100_EMAIL-04318.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250417_184100_EMAIL-04318.eml) | 2025-04-17T18:41:00+00:00 |
| `20250422_104300_EMAIL-04349-eml` | email | [emails/2025-04/20250422_104300_EMAIL-04349.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250422_104300_EMAIL-04349.eml) | 2025-04-22T10:43:00+00:00 |
| `20250423_153300_EMAIL-04360-eml` | email | [emails/2025-04/20250423_153300_EMAIL-04360.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250423_153300_EMAIL-04360.eml) | 2025-04-23T15:33:00+00:00 |
| `20250505_081600_EMAIL-04437-eml` | email | [emails/2025-05/20250505_081600_EMAIL-04437.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250505_081600_EMAIL-04437.eml) | 2025-05-05T08:16:00+00:00 |
| `20250506_091700_EMAIL-04443-eml` | email | [emails/2025-05/20250506_091700_EMAIL-04443.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250506_091700_EMAIL-04443.eml) | 2025-05-06T09:17:00+00:00 |
| `20250516_094900_EMAIL-04533-eml` | email | [emails/2025-05/20250516_094900_EMAIL-04533.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250516_094900_EMAIL-04533.eml) | 2025-05-16T09:49:00+00:00 |
| `20250526_133800_EMAIL-04627-eml` | email | [emails/2025-05/20250526_133800_EMAIL-04627.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250526_133800_EMAIL-04627.eml) | 2025-05-26T13:38:00+00:00 |
| `20250616_032400_EMAIL-04786-eml` | email | [emails/2025-06/20250616_032400_EMAIL-04786.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250616_032400_EMAIL-04786.eml) | 2025-06-16T03:24:00+00:00 |
| `20250626_152000_EMAIL-04882-eml` | email | [emails/2025-06/20250626_152000_EMAIL-04882.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250626_152000_EMAIL-04882.eml) | 2025-06-26 |
| `20250710_141300_EMAIL-04993-eml` | email | [emails/2025-07/20250710_141300_EMAIL-04993.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250710_141300_EMAIL-04993.eml) | 2025-07-10T14:13:00+00:00 |
| `20250720_152900_EMAIL-05097-eml` | email | [emails/2025-07/20250720_152900_EMAIL-05097.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250720_152900_EMAIL-05097.eml) | 2025-07-20T15:29:00+00:00 |
| `20250803_081300_EMAIL-05190-eml` | email | [emails/2025-08/20250803_081300_EMAIL-05190.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250803_081300_EMAIL-05190.eml) | 2025-08-03T08:13:00+00:00 |
| `20250808_152800_EMAIL-05224-eml` | email | [emails/2025-08/20250808_152800_EMAIL-05224.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250808_152800_EMAIL-05224.eml) | 2025-08-08T15:28:00+00:00 |
| `20250823_171700_EMAIL-05387-eml` | email | [emails/2025-08/20250823_171700_EMAIL-05387.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250823_171700_EMAIL-05387.eml) | 2025-08-23T17:17:00+00:00 |
| `20250823_201700_EMAIL-05388-eml` | email | [emails/2025-08/20250823_201700_EMAIL-05388.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250823_201700_EMAIL-05388.eml) | 2025-08-23T20:17:00+00:00 |
| `20250829_104400_EMAIL-05438-eml` | email | [emails/2025-08/20250829_104400_EMAIL-05438.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250829_104400_EMAIL-05438.eml) | 2025-08-29T10:44:00+00:00 |
| `20250831_080200_EMAIL-05462-eml` | email | [emails/2025-08/20250831_080200_EMAIL-05462.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250831_080200_EMAIL-05462.eml) | 2025-08-31T08:02:00+00:00 |
| `20250902_010200_EMAIL-05491-eml` | email | [emails/2025-09/20250902_010200_EMAIL-05491.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250902_010200_EMAIL-05491.eml) | 2025-09-02T01:02:00+00:00 |
| `20250908_010200_EMAIL-05566-eml` | email | [emails/2025-09/20250908_010200_EMAIL-05566.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250908_010200_EMAIL-05566.eml) | 2025-09-08T01:02:00+00:00 |
| `20250920_133000_EMAIL-05666-eml` | email | [emails/2025-09/20250920_133000_EMAIL-05666.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250920_133000_EMAIL-05666.eml) | 2025-09-20T13:30:00+00:00 |
| `20250929_233700_EMAIL-05745-eml` | email | [emails/2025-09/20250929_233700_EMAIL-05745.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250929_233700_EMAIL-05745.eml) | 2025-09-29T23:37:00+00:00 |
| `20251009_141200_EMAIL-05824-eml` | email | [emails/2025-10/20251009_141200_EMAIL-05824.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251009_141200_EMAIL-05824.eml) | 2025-10-09T14:12:00+00:00 |
| `20251009_150400_EMAIL-05825-eml` | email | [emails/2025-10/20251009_150400_EMAIL-05825.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251009_150400_EMAIL-05825.eml) | 2025-10-09T15:04:00+00:00 |
| `20251009_181200_EMAIL-05828-eml` | email | [emails/2025-10/20251009_181200_EMAIL-05828.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251009_181200_EMAIL-05828.eml) | 2025-10-09T18:12:00+00:00 |
| `20251010_150400_EMAIL-05836-eml` | email | [emails/2025-10/20251010_150400_EMAIL-05836.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251010_150400_EMAIL-05836.eml) | 2025-10-10T15:04:00+00:00 |
| `20251012_172900_EMAIL-05855-eml` | email | [emails/2025-10/20251012_172900_EMAIL-05855.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251012_172900_EMAIL-05855.eml) | 2025-10-12T17:29:00+00:00 |
| `20251023_121000_EMAIL-05947-eml` | email | [emails/2025-10/20251023_121000_EMAIL-05947.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251023_121000_EMAIL-05947.eml) | 2025-10-23T12:10:00+00:00 |
| `20251023_143100_EMAIL-05949-eml` | email | [emails/2025-10/20251023_143100_EMAIL-05949.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251023_143100_EMAIL-05949.eml) | 2025-10-23T14:31:00+00:00 |
| `20251026_151900_EMAIL-05973-eml` | email | [emails/2025-10/20251026_151900_EMAIL-05973.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251026_151900_EMAIL-05973.eml) | 2025-10-26T15:19:00+00:00 |
| `20251027_113400_EMAIL-05981-eml` | email | [emails/2025-10/20251027_113400_EMAIL-05981.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251027_113400_EMAIL-05981.eml) | 2025-10-27T11:34:00+00:00 |
| `20251105_093000_EMAIL-06048-eml` | email | [emails/2025-11/20251105_093000_EMAIL-06048.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251105_093000_EMAIL-06048.eml) | 2025-11-05T09:30:00+00:00 |
| `20251127_141800_EMAIL-06240-eml` | email | [emails/2025-11/20251127_141800_EMAIL-06240.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251127_141800_EMAIL-06240.eml) | 2025-11-27T14:18:00+00:00 |
| `20251226_151300_EMAIL-06495-eml` | email | [emails/2025-12/20251226_151300_EMAIL-06495.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251226_151300_EMAIL-06495.eml) | 2025-12-26T15:13:00+00:00 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-25T20:52:09+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
