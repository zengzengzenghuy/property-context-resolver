# context.unit.<!-- auto:unit_id -->EH-031<!-- /auto:unit_id -->.md

> Per-unit dossier (one file per Einheit). Holds everything specific to this unit:
> the unit itself, the active lease, the tenant(s), and all unit/tenant-specific operations.
> **Property-wide data lives in `context.property.md`** — see `parent_property_ref` below.

<!-- auto:meta -->
- last_built_at: `2026-04-25T20:52:45+00:00`
- build_hash: `engine-v2`
- engine_version: `0.2.0`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `unit`
- unit_id: `EH-031`
- property_id: `LIE-001`
- parent_property_ref: `context.property.LIE-001.md`
- owner_ref: `EIG-011`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit -->
- unit_id: `EH-031`
- label: WE 31
- haus_id: `HAUS-14`
- floor: 5. OG
- position: links
- typ: Wohnung
- area_sqm: 103.0
- rooms: 4.0
- mea_‰: 239
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
- lease_id: `LEASE-MIE-022`
- unit_ref: `EH-031`
- start_date: 2020-08-13 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-022)
- end_date: _(no data in source yet)_
- term_type: `unbefristet`
- cancellation_status: `by_tenant` (notice_date: 2025-11-26, move_out_date: —)
- rent_components: { kaltmiete: 1566.0, betriebskosten_vorauszahlung: 348.0, total_warmmiete: 1914.00 }
- payment_mode: Überweisung
- iban_payer: DE26100100102053950240 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-022)
- kaution: { amount: 4698.0 }
- usage: `residential`
- subletting: { current_status: `requested` }
- special_agreements: _(no data in source yet)_
<!-- /auto:lease -->

### 2.1 Tenants on this Lease
<!-- auto:tenants -->
| tenant_id | name | role | contact_email | contact_phone | comms_pref | gesamtschuldner |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-022` | Herr Carsten Austermühle | haupt | carsten.austermuehle@web.de | 03950240268 | email | — |
<!-- /auto:tenants -->

---

## 3. Operations (this unit / this tenant)

### 3.1 Open Tickets — Critical (overdue or due ≤7 days)
<!-- auto:tickets.critical -->
| ticket_id | type | title | deadline | status | assignee |
| --- | --- | --- | --- | --- | --- |
| `TKT-be53f787` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-bd50f0ff` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-42b531c8` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-8828dc7e` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-6bdec5d0` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-5f843abd` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-056add79` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-7553c747` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-8c66a8c5` | wasserschaden | Re: Wasserschaden Bad | — | open | — |
<!-- /auto:tickets.critical -->

### 3.2 Open Tickets — Aggregate
<!-- auto:tickets.aggregate -->
- total_open: `24`
- by_type: { fenster: `9`, schimmel: `3`, schluessel: `6`, wasserschaden: `6` }
- live source: `db.tickets WHERE unit_id=EH-031 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren

<!-- auto:dunning.summary -->[Routine] Mieter MIE-022 ist seit vier Monaten im Verzug; offener Betrag 7.656,00 EUR zzgl. 98,06 EUR Verzugszinsen, letzte Zahlung 2025-12-03 [(bank)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv#TX-01589). Vertraglich geschuldet sind monatlich 1.914,00 EUR (Kaltmiete 1.566,00 EUR + NK 348,00 EUR) [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-022). Verzug nach § 286 BGB, Verzugszinsen § 288 I BGB; Mahnstufe 2 [(letter)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/briefe/2024-06/20240627_mahnung_LTR-0039.pdf) — nächster Schritt: Kündigung nach angemessener Frist (§ 573 II BGB).<!-- /auto:dunning.summary -->

#### Per claim
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-022` | — | 2 | 7656.00 EUR | 2025-12-03 | — | — |
- live balance pointer: `db.tenant_balance.tenant_id=MIE-022`
<!-- /auto:dunning -->

### 3.4 Active Reductions / Deferrals (§ 536 BGB)
<!-- auto:reductions -->
- date_raised: 2024-07-18
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
| Mieterwechsel | 2025-11-26 | Kündigung erhalten | Verwaltung | TBD | Übergabe-Termin offen |
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
| `TH-28ec9e` | Schluesselverlust | 2025-12-29 | `MIE-022` | active | 104 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251229_233900_EMAIL-06521.eml) |
| `TH-8bf580` | Parkplatz-Frage | 2025-12-20 | `MIE-022` | active | 135 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251220_173800_EMAIL-06448.eml) |
| `TH-edbae7` | Mieterwechsel in WE 31 | 2024-12-18 | `EH-031` | active | 3 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241218_100300_EMAIL-03199.eml) |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `kontoauszug_2024_2025-csv` | bank | [bank/kontoauszug_2024_2025.csv](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv) | 2026-04-25 |
| `20240420_mahnung_LTR-0035-pdf` | letter | [briefe/2024-04/20240420_mahnung_LTR-0035.pdf](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/briefe/2024-04/20240420_mahnung_LTR-0035.pdf) | 2024-04-20 |
| `20240627_mahnung_LTR-0039-pdf` | letter | [briefe/2024-06/20240627_mahnung_LTR-0039.pdf](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/briefe/2024-06/20240627_mahnung_LTR-0039.pdf) | 2026-04-25 |
| `20240103_152000_EMAIL-00017-eml` | email | [emails/2024-01/20240103_152000_EMAIL-00017.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240103_152000_EMAIL-00017.eml) | 2024-01-03T15:20:00+00:00 |
| `20240125_093400_EMAIL-00194-eml` | email | [emails/2024-01/20240125_093400_EMAIL-00194.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240125_093400_EMAIL-00194.eml) | 2024-01-25T09:34:00+00:00 |
| `20240204_114900_EMAIL-00297-eml` | email | [emails/2024-02/20240204_114900_EMAIL-00297.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240204_114900_EMAIL-00297.eml) | 2024-02-04T11:49:00+00:00 |
| `20240226_085100_EMAIL-00471-eml` | email | [emails/2024-02/20240226_085100_EMAIL-00471.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240226_085100_EMAIL-00471.eml) | 2024-02-26T08:51:00+00:00 |
| `20240228_205100_EMAIL-00498-eml` | email | [emails/2024-02/20240228_205100_EMAIL-00498.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240228_205100_EMAIL-00498.eml) | 2024-02-28T20:51:00+00:00 |
| `20240316_113100_EMAIL-00658-eml` | email | [emails/2024-03/20240316_113100_EMAIL-00658.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240316_113100_EMAIL-00658.eml) | 2024-03-16T11:31:00+00:00 |
| `20240323_103000_EMAIL-00716-eml` | email | [emails/2024-03/20240323_103000_EMAIL-00716.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240323_103000_EMAIL-00716.eml) | 2024-03-23T10:30:00+00:00 |
| `20240402_095700_EMAIL-00798-eml` | email | [emails/2024-04/20240402_095700_EMAIL-00798.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240402_095700_EMAIL-00798.eml) | 2024-04-02T09:57:00+00:00 |
| `20240404_171200_EMAIL-00831-eml` | email | [emails/2024-04/20240404_171200_EMAIL-00831.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240404_171200_EMAIL-00831.eml) | 2024-04-04T17:12:00+00:00 |
| `20240423_125400_EMAIL-01024-eml` | email | [emails/2024-04/20240423_125400_EMAIL-01024.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240423_125400_EMAIL-01024.eml) | 2024-04-23T12:54:00+00:00 |
| `20240501_173200_EMAIL-01093-eml` | email | [emails/2024-05/20240501_173200_EMAIL-01093.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240501_173200_EMAIL-01093.eml) | 2024-05-01T17:32:00+00:00 |
| `20240502_094600_EMAIL-01098-eml` | email | [emails/2024-05/20240502_094600_EMAIL-01098.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240502_094600_EMAIL-01098.eml) | 2024-05-02T09:46:00+00:00 |
| `20240504_175200_EMAIL-01121-eml` | email | [emails/2024-05/20240504_175200_EMAIL-01121.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240504_175200_EMAIL-01121.eml) | 2024-05-04T17:52:00+00:00 |
| `20240507_163500_EMAIL-01145-eml` | email | [emails/2024-05/20240507_163500_EMAIL-01145.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240507_163500_EMAIL-01145.eml) | 2024-05-07T16:35:00+00:00 |
| `20240509_003500_EMAIL-01159-eml` | email | [emails/2024-05/20240509_003500_EMAIL-01159.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240509_003500_EMAIL-01159.eml) | 2024-05-09T00:35:00+00:00 |
| `20240621_155000_EMAIL-01560-eml` | email | [emails/2024-06/20240621_155000_EMAIL-01560.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240621_155000_EMAIL-01560.eml) | 2024-06-21T15:50:00+00:00 |
| `20240713_165000_EMAIL-01754-eml` | email | [emails/2024-07/20240713_165000_EMAIL-01754.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240713_165000_EMAIL-01754.eml) | 2024-07-13T16:50:00+00:00 |
| `20240715_035000_EMAIL-01767-eml` | email | [emails/2024-07/20240715_035000_EMAIL-01767.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240715_035000_EMAIL-01767.eml) | 2024-07-15T03:50:00+00:00 |
| `20240716_111700_EMAIL-01776-eml` | email | [emails/2024-07/20240716_111700_EMAIL-01776.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240716_111700_EMAIL-01776.eml) | 2024-07-16T11:17:00+00:00 |
| `20240718_113400_EMAIL-01800-eml` | email | [emails/2024-07/20240718_113400_EMAIL-01800.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240718_113400_EMAIL-01800.eml) | 2024-07-18T11:34:00+00:00 |
| `20240722_094500_EMAIL-01828-eml` | email | [emails/2024-07/20240722_094500_EMAIL-01828.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240722_094500_EMAIL-01828.eml) | 2024-07-22T09:45:00+00:00 |
| `20240723_111600_EMAIL-01841-eml` | email | [emails/2024-07/20240723_111600_EMAIL-01841.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240723_111600_EMAIL-01841.eml) | 2024-07-23T11:16:00+00:00 |
| `20240727_175100_EMAIL-01883-eml` | email | [emails/2024-07/20240727_175100_EMAIL-01883.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240727_175100_EMAIL-01883.eml) | 2024-07-27T17:51:00+00:00 |
| `20240728_140900_EMAIL-01890-eml` | email | [emails/2024-07/20240728_140900_EMAIL-01890.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240728_140900_EMAIL-01890.eml) | 2024-07-28T14:09:00+00:00 |
| `20240802_205100_EMAIL-01938-eml` | email | [emails/2024-08/20240802_205100_EMAIL-01938.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240802_205100_EMAIL-01938.eml) | 2024-08-02T20:51:00+00:00 |
| `20240802_235100_EMAIL-01939-eml` | email | [emails/2024-08/20240802_235100_EMAIL-01939.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240802_235100_EMAIL-01939.eml) | 2024-08-02T23:51:00+00:00 |
| `20240819_171200_EMAIL-02095-eml` | email | [emails/2024-08/20240819_171200_EMAIL-02095.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240819_171200_EMAIL-02095.eml) | 2024-08-19T17:12:00+00:00 |
| `20240825_152300_EMAIL-02151-eml` | email | [emails/2024-08/20240825_152300_EMAIL-02151.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240825_152300_EMAIL-02151.eml) | 2024-08-25T15:23:00+00:00 |
| `20240825_154100_EMAIL-02152-eml` | email | [emails/2024-08/20240825_154100_EMAIL-02152.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240825_154100_EMAIL-02152.eml) | 2024-08-25T15:41:00+00:00 |
| `20240901_173200_EMAIL-02219-eml` | email | [emails/2024-09/20240901_173200_EMAIL-02219.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240901_173200_EMAIL-02219.eml) | 2024-09-01T17:32:00+00:00 |
| `20240903_144000_EMAIL-02231-eml` | email | [emails/2024-09/20240903_144000_EMAIL-02231.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240903_144000_EMAIL-02231.eml) | 2024-09-03T14:40:00+00:00 |
| `20240914_042200_EMAIL-02349-eml` | email | [emails/2024-09/20240914_042200_EMAIL-02349.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240914_042200_EMAIL-02349.eml) | 2024-09-14T04:22:00+00:00 |
| `20241031_113800_EMAIL-02770-eml` | email | [emails/2024-10/20241031_113800_EMAIL-02770.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241031_113800_EMAIL-02770.eml) | 2024-10-31T11:38:00+00:00 |
| `20241115_143700_EMAIL-02917-eml` | email | [emails/2024-11/20241115_143700_EMAIL-02917.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241115_143700_EMAIL-02917.eml) | 2024-11-15T14:37:00+00:00 |
| `20241116_133700_EMAIL-02931-eml` | email | [emails/2024-11/20241116_133700_EMAIL-02931.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241116_133700_EMAIL-02931.eml) | 2024-11-16T13:37:00+00:00 |
| `20241217_120600_EMAIL-03195-eml` | email | [emails/2024-12/20241217_120600_EMAIL-03195.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241217_120600_EMAIL-03195.eml) | 2024-12-17T12:06:00+00:00 |
| `20241218_100300_EMAIL-03199-eml` | email | [emails/2024-12/20241218_100300_EMAIL-03199.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241218_100300_EMAIL-03199.eml) | 2024-12-18 |
| `20241220_153900_EMAIL-03219-eml` | email | [emails/2024-12/20241220_153900_EMAIL-03219.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241220_153900_EMAIL-03219.eml) | 2024-12-20T15:39:00+00:00 |
| `20241229_110700_EMAIL-03304-eml` | email | [emails/2024-12/20241229_110700_EMAIL-03304.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241229_110700_EMAIL-03304.eml) | 2024-12-29T11:07:00+00:00 |
| `20250124_155700_EMAIL-03553-eml` | email | [emails/2025-01/20250124_155700_EMAIL-03553.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250124_155700_EMAIL-03553.eml) | 2025-01-24T15:57:00+00:00 |
| `20250213_111200_EMAIL-03716-eml` | email | [emails/2025-02/20250213_111200_EMAIL-03716.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250213_111200_EMAIL-03716.eml) | 2025-02-13T11:12:00+00:00 |
| `20250223_183600_EMAIL-03827-eml` | email | [emails/2025-02/20250223_183600_EMAIL-03827.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250223_183600_EMAIL-03827.eml) | 2025-02-23T18:36:00+00:00 |
| `20250225_183600_EMAIL-03855-eml` | email | [emails/2025-02/20250225_183600_EMAIL-03855.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250225_183600_EMAIL-03855.eml) | 2025-02-25T18:36:00+00:00 |
| `20250227_085700_EMAIL-03865-eml` | email | [emails/2025-02/20250227_085700_EMAIL-03865.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250227_085700_EMAIL-03865.eml) | 2025-02-27T08:57:00+00:00 |
| `20250302_101900_EMAIL-03899-eml` | email | [emails/2025-03/20250302_101900_EMAIL-03899.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250302_101900_EMAIL-03899.eml) | 2025-03-02T10:19:00+00:00 |
| `20250302_123600_EMAIL-03900-eml` | email | [emails/2025-03/20250302_123600_EMAIL-03900.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250302_123600_EMAIL-03900.eml) | 2025-03-02T12:36:00+00:00 |
| `20250308_115700_EMAIL-03953-eml` | email | [emails/2025-03/20250308_115700_EMAIL-03953.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250308_115700_EMAIL-03953.eml) | 2025-03-08T11:57:00+00:00 |
| `20250313_123000_EMAIL-04003-eml` | email | [emails/2025-03/20250313_123000_EMAIL-04003.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250313_123000_EMAIL-04003.eml) | 2025-03-13T12:30:00+00:00 |
| `20250315_033000_EMAIL-04017-eml` | email | [emails/2025-03/20250315_033000_EMAIL-04017.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250315_033000_EMAIL-04017.eml) | 2025-03-15T03:30:00+00:00 |
| `20250325_104800_EMAIL-04115-eml` | email | [emails/2025-03/20250325_104800_EMAIL-04115.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250325_104800_EMAIL-04115.eml) | 2025-03-25T10:48:00+00:00 |
| `20250406_112200_EMAIL-04218-eml` | email | [emails/2025-04/20250406_112200_EMAIL-04218.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250406_112200_EMAIL-04218.eml) | 2025-04-06T11:22:00+00:00 |
| `20250612_125200_EMAIL-04755-eml` | email | [emails/2025-06/20250612_125200_EMAIL-04755.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250612_125200_EMAIL-04755.eml) | 2025-06-12T12:52:00+00:00 |
| `20250731_141700_EMAIL-05171-eml` | email | [emails/2025-07/20250731_141700_EMAIL-05171.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250731_141700_EMAIL-05171.eml) | 2025-07-31T14:17:00+00:00 |
| `20250813_090400_EMAIL-05278-eml` | email | [emails/2025-08/20250813_090400_EMAIL-05278.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250813_090400_EMAIL-05278.eml) | 2025-08-13T09:04:00+00:00 |
| `20250818_183600_EMAIL-05344-eml` | email | [emails/2025-08/20250818_183600_EMAIL-05344.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250818_183600_EMAIL-05344.eml) | 2025-08-18T18:36:00+00:00 |
| `20250819_150400_EMAIL-05350-eml` | email | [emails/2025-08/20250819_150400_EMAIL-05350.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250819_150400_EMAIL-05350.eml) | 2025-08-19T15:04:00+00:00 |
| `20250901_164600_EMAIL-05485-eml` | email | [emails/2025-09/20250901_164600_EMAIL-05485.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250901_164600_EMAIL-05485.eml) | 2025-09-01T16:46:00+00:00 |
| `20250902_064600_EMAIL-05493-eml` | email | [emails/2025-09/20250902_064600_EMAIL-05493.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250902_064600_EMAIL-05493.eml) | 2025-09-02T06:46:00+00:00 |
| `20250905_104200_EMAIL-05524-eml` | email | [emails/2025-09/20250905_104200_EMAIL-05524.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250905_104200_EMAIL-05524.eml) | 2025-09-05T10:42:00+00:00 |
| `20250905_142900_EMAIL-05529-eml` | email | [emails/2025-09/20250905_142900_EMAIL-05529.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250905_142900_EMAIL-05529.eml) | 2025-09-05T14:29:00+00:00 |
| `20250910_064600_EMAIL-05586-eml` | email | [emails/2025-09/20250910_064600_EMAIL-05586.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250910_064600_EMAIL-05586.eml) | 2025-09-10T06:46:00+00:00 |
| `20251104_222900_EMAIL-06046-eml` | email | [emails/2025-11/20251104_222900_EMAIL-06046.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251104_222900_EMAIL-06046.eml) | 2025-11-04T22:29:00+00:00 |
| `20251113_135000_EMAIL-06112-eml` | email | [emails/2025-11/20251113_135000_EMAIL-06112.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251113_135000_EMAIL-06112.eml) | 2025-11-13T13:50:00+00:00 |
| `20251116_172900_EMAIL-06141-eml` | email | [emails/2025-11/20251116_172900_EMAIL-06141.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251116_172900_EMAIL-06141.eml) | 2025-11-16T17:29:00+00:00 |
| `20251121_092200_EMAIL-06176-eml` | email | [emails/2025-11/20251121_092200_EMAIL-06176.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251121_092200_EMAIL-06176.eml) | 2025-11-21T09:22:00+00:00 |
| `20251122_202200_EMAIL-06196-eml` | email | [emails/2025-11/20251122_202200_EMAIL-06196.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251122_202200_EMAIL-06196.eml) | 2025-11-22T20:22:00+00:00 |
| `20251123_113000_EMAIL-06201-eml` | email | [emails/2025-11/20251123_113000_EMAIL-06201.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251123_113000_EMAIL-06201.eml) | 2025-11-23T11:30:00+00:00 |
| `20251125_035000_EMAIL-06216-eml` | email | [emails/2025-11/20251125_035000_EMAIL-06216.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251125_035000_EMAIL-06216.eml) | 2025-11-25T03:50:00+00:00 |
| `20251126_150000_EMAIL-06231-eml` | email | [emails/2025-11/20251126_150000_EMAIL-06231.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251126_150000_EMAIL-06231.eml) | 2025-11-26T15:00:00+00:00 |
| `20251129_160600_EMAIL-06259-eml` | email | [emails/2025-11/20251129_160600_EMAIL-06259.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251129_160600_EMAIL-06259.eml) | 2025-11-29T16:06:00+00:00 |
| `20251211_110400_EMAIL-06351-eml` | email | [emails/2025-12/20251211_110400_EMAIL-06351.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251211_110400_EMAIL-06351.eml) | 2025-12-11T11:04:00+00:00 |
| `20251212_160400_EMAIL-06370-eml` | email | [emails/2025-12/20251212_160400_EMAIL-06370.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251212_160400_EMAIL-06370.eml) | 2025-12-12T16:04:00+00:00 |
| `20251214_184000_EMAIL-06396-eml` | email | [emails/2025-12/20251214_184000_EMAIL-06396.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251214_184000_EMAIL-06396.eml) | 2025-12-14T18:40:00+00:00 |
| `20251220_173800_EMAIL-06448-eml` | email | [emails/2025-12/20251220_173800_EMAIL-06448.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251220_173800_EMAIL-06448.eml) | 2025-12-20T17:38:00+00:00 |
| `20251229_113900_EMAIL-06515-eml` | email | [emails/2025-12/20251229_113900_EMAIL-06515.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251229_113900_EMAIL-06515.eml) | 2025-12-29T11:39:00+00:00 |
| `20251229_233900_EMAIL-06521-eml` | email | [emails/2025-12/20251229_233900_EMAIL-06521.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251229_233900_EMAIL-06521.eml) | 2025-12-29 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-25T20:52:09+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
