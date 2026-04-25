# context.unit.<!-- auto:unit_id -->EH-022<!-- /auto:unit_id -->.md

> Per-unit dossier (one file per Einheit). Holds everything specific to this unit:
> the unit itself, the active lease, the tenant(s), and all unit/tenant-specific operations.
> **Property-wide data lives in `context.property.md`** — see `parent_property_ref` below.

<!-- auto:meta -->
- last_built_at: `2026-04-25T20:52:37+00:00`
- build_hash: `engine-v2`
- engine_version: `0.2.0`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `unit`
- unit_id: `EH-022`
- property_id: `LIE-001`
- parent_property_ref: `context.property.LIE-001.md`
- owner_ref: `EIG-028`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit -->
- unit_id: `EH-022`
- label: WE 22
- haus_id: `HAUS-14`
- floor: 2. OG
- position: links
- typ: Wohnung
- area_sqm: 75.0
- rooms: 2.5
- mea_‰: 174
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
- lease_id: `LEASE-MIE-012`
- unit_ref: `EH-022`
- start_date: 2020-04-04 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-012)
- end_date: _(no data in source yet)_
- term_type: `unbefristet`
- cancellation_status: `by_tenant` (notice_date: 2025-07-30, move_out_date: —)
- rent_components: { kaltmiete: 1198.0, betriebskosten_vorauszahlung: 262.0, total_warmmiete: 1460.00 }
- payment_mode: Überweisung
- iban_payer: DE31100100104556238692 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-012)
- kaution: { amount: 3594.0 }
- usage: `residential`
- subletting: { current_status: `requested` }
- special_agreements: _(no data in source yet)_
<!-- /auto:lease -->

### 2.1 Tenants on this Lease
<!-- auto:tenants -->
| tenant_id | name | role | contact_email | contact_phone | comms_pref | gesamtschuldner |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-012` | Frau Alwine Sager | haupt | alwine.sager@web.de | 02145623285 | email | — |
<!-- /auto:tenants -->

---

## 3. Operations (this unit / this tenant)

### 3.1 Open Tickets — Critical (overdue or due ≤7 days)
<!-- auto:tickets.critical -->
| ticket_id | type | title | deadline | status | assignee |
| --- | --- | --- | --- | --- | --- |
| `TKT-30e552bd` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-496860b2` | wasserschaden | Re: Wasserschaden Bad | — | open | — |
| `TKT-da179451` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-bb3c45f9` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-b936649b` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-91bbc891` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-2de58115` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-99286b27` | schimmel | Schimmel im Schlafzimmer | — | open | — |
<!-- /auto:tickets.critical -->

### 3.2 Open Tickets — Aggregate
<!-- auto:tickets.aggregate -->
- total_open: `20`
- by_type: { abfluss: `3`, fenster: `4`, schimmel: `3`, schluessel: `5`, wasserschaden: `5` }
- live source: `db.tickets WHERE unit_id=EH-022 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren

<!-- auto:dunning.summary -->[Routine] Mieter MIE-012 ist seit vier Monaten im Verzug; offener Betrag 5.840,00 EUR zzgl. 74,80 EUR Verzugszinsen, letzte Zahlung 2025-12-03 [(bank)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv#TX-01583). Vertraglich geschuldet sind monatlich 1.460,00 EUR (Kaltmiete 1.198,00 EUR + NK 262,00 EUR) [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-012). Verzug nach § 286 BGB festgestellt, Verzugszinsen § 288 I BGB; Mahnstufe 1 aktiv, nächster Schritt: 2. Mahnung nach 14 Tagen.<!-- /auto:dunning.summary -->

#### Per claim
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-012` | — | 1 | 5840.00 EUR | 2025-12-03 | — | — |
- live balance pointer: `db.tenant_balance.tenant_id=MIE-012`
<!-- /auto:dunning -->

### 3.4 Active Reductions / Deferrals (§ 536 BGB)
<!-- auto:reductions -->
- date_raised: 2024-03-07
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-03-21
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-03-22
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-03-29
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-04-16
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-04-16
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-04-26
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-10-29
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-11-07
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-11-08
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-05-28
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-07-29
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
| Mieterwechsel | 2025-07-30 | Kündigung erhalten | Verwaltung | TBD | Übergabe-Termin offen |
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
| `TH-d67d17` | Verkaufsabsicht WE 22 | 2025-02-27 | `EH-022` | active | 7 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250227_141600_EMAIL-03871.eml) |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `kontoauszug_2024_2025-csv` | bank | [bank/kontoauszug_2024_2025.csv](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv) | 2026-04-25 |
| `20240102_115800_EMAIL-00008-eml` | email | [emails/2024-01/20240102_115800_EMAIL-00008.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240102_115800_EMAIL-00008.eml) | 2024-01-02T11:58:00+00:00 |
| `20240109_202000_EMAIL-00076-eml` | email | [emails/2024-01/20240109_202000_EMAIL-00076.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240109_202000_EMAIL-00076.eml) | 2024-01-09T20:20:00+00:00 |
| `20240118_153900_EMAIL-00147-eml` | email | [emails/2024-01/20240118_153900_EMAIL-00147.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240118_153900_EMAIL-00147.eml) | 2024-01-18T15:39:00+00:00 |
| `20240125_111600_EMAIL-00195-eml` | email | [emails/2024-01/20240125_111600_EMAIL-00195.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240125_111600_EMAIL-00195.eml) | 2024-01-25T11:16:00+00:00 |
| `20240127_061600_EMAIL-00208-eml` | email | [emails/2024-01/20240127_061600_EMAIL-00208.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240127_061600_EMAIL-00208.eml) | 2024-01-27T06:16:00+00:00 |
| `20240226_085900_EMAIL-00472-eml` | email | [emails/2024-02/20240226_085900_EMAIL-00472.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240226_085900_EMAIL-00472.eml) | 2024-02-26T08:59:00+00:00 |
| `20240226_141400_EMAIL-00474-eml` | email | [emails/2024-02/20240226_141400_EMAIL-00474.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240226_141400_EMAIL-00474.eml) | 2024-02-26T14:14:00+00:00 |
| `20240226_170900_EMAIL-00480-eml` | email | [emails/2024-02/20240226_170900_EMAIL-00480.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240226_170900_EMAIL-00480.eml) | 2024-02-26T17:09:00+00:00 |
| `20240307_112600_EMAIL-00574-eml` | email | [emails/2024-03/20240307_112600_EMAIL-00574.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240307_112600_EMAIL-00574.eml) | 2024-03-07T11:26:00+00:00 |
| `20240321_103300_EMAIL-00695-eml` | email | [emails/2024-03/20240321_103300_EMAIL-00695.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240321_103300_EMAIL-00695.eml) | 2024-03-21T10:33:00+00:00 |
| `20240322_115200_EMAIL-00707-eml` | email | [emails/2024-03/20240322_115200_EMAIL-00707.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240322_115200_EMAIL-00707.eml) | 2024-03-22T11:52:00+00:00 |
| `20240322_133300_EMAIL-00709-eml` | email | [emails/2024-03/20240322_133300_EMAIL-00709.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240322_133300_EMAIL-00709.eml) | 2024-03-22T13:33:00+00:00 |
| `20240329_133300_EMAIL-00764-eml` | email | [emails/2024-03/20240329_133300_EMAIL-00764.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240329_133300_EMAIL-00764.eml) | 2024-03-29T13:33:00+00:00 |
| `20240410_214600_EMAIL-00895-eml` | email | [emails/2024-04/20240410_214600_EMAIL-00895.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240410_214600_EMAIL-00895.eml) | 2024-04-10T21:46:00+00:00 |
| `20240412_172500_EMAIL-00921-eml` | email | [emails/2024-04/20240412_172500_EMAIL-00921.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240412_172500_EMAIL-00921.eml) | 2024-04-12T17:25:00+00:00 |
| `20240416_120400_EMAIL-00956-eml` | email | [emails/2024-04/20240416_120400_EMAIL-00956.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240416_120400_EMAIL-00956.eml) | 2024-04-16T12:04:00+00:00 |
| `20240416_162900_EMAIL-00959-eml` | email | [emails/2024-04/20240416_162900_EMAIL-00959.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240416_162900_EMAIL-00959.eml) | 2024-04-16T16:29:00+00:00 |
| `20240416_163200_EMAIL-00960-eml` | email | [emails/2024-04/20240416_163200_EMAIL-00960.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240416_163200_EMAIL-00960.eml) | 2024-04-16T16:32:00+00:00 |
| `20240416_190400_EMAIL-00962-eml` | email | [emails/2024-04/20240416_190400_EMAIL-00962.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240416_190400_EMAIL-00962.eml) | 2024-04-16T19:04:00+00:00 |
| `20240416_213200_EMAIL-00964-eml` | email | [emails/2024-04/20240416_213200_EMAIL-00964.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240416_213200_EMAIL-00964.eml) | 2024-04-16T21:32:00+00:00 |
| `20240426_213200_EMAIL-01051-eml` | email | [emails/2024-04/20240426_213200_EMAIL-01051.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240426_213200_EMAIL-01051.eml) | 2024-04-26T21:32:00+00:00 |
| `20240430_085100_EMAIL-01076-eml` | email | [emails/2024-04/20240430_085100_EMAIL-01076.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240430_085100_EMAIL-01076.eml) | 2024-04-30T08:51:00+00:00 |
| `20240502_104300_EMAIL-01099-eml` | email | [emails/2024-05/20240502_104300_EMAIL-01099.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240502_104300_EMAIL-01099.eml) | 2024-05-02T10:43:00+00:00 |
| `20240513_165200_EMAIL-01203-eml` | email | [emails/2024-05/20240513_165200_EMAIL-01203.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240513_165200_EMAIL-01203.eml) | 2024-05-13T16:52:00+00:00 |
| `20240603_110200_EMAIL-01394-eml` | email | [emails/2024-06/20240603_110200_EMAIL-01394.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240603_110200_EMAIL-01394.eml) | 2024-06-03T11:02:00+00:00 |
| `20240605_104500_EMAIL-01407-eml` | email | [emails/2024-06/20240605_104500_EMAIL-01407.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240605_104500_EMAIL-01407.eml) | 2024-06-05T10:45:00+00:00 |
| `20240620_122000_EMAIL-01548-eml` | email | [emails/2024-06/20240620_122000_EMAIL-01548.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240620_122000_EMAIL-01548.eml) | 2024-06-20T12:20:00+00:00 |
| `20240623_182600_EMAIL-01578-eml` | email | [emails/2024-06/20240623_182600_EMAIL-01578.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240623_182600_EMAIL-01578.eml) | 2024-06-23T18:26:00+00:00 |
| `20240714_124600_EMAIL-01758-eml` | email | [emails/2024-07/20240714_124600_EMAIL-01758.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240714_124600_EMAIL-01758.eml) | 2024-07-14T12:46:00+00:00 |
| `20240714_142300_EMAIL-01760-eml` | email | [emails/2024-07/20240714_142300_EMAIL-01760.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240714_142300_EMAIL-01760.eml) | 2024-07-14T14:23:00+00:00 |
| `20240828_104700_EMAIL-02174-eml` | email | [emails/2024-08/20240828_104700_EMAIL-02174.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240828_104700_EMAIL-02174.eml) | 2024-08-28T10:47:00+00:00 |
| `20241003_163400_EMAIL-02507-eml` | email | [emails/2024-10/20241003_163400_EMAIL-02507.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241003_163400_EMAIL-02507.eml) | 2024-10-03T16:34:00+00:00 |
| `20241008_122500_EMAIL-02557-eml` | email | [emails/2024-10/20241008_122500_EMAIL-02557.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241008_122500_EMAIL-02557.eml) | 2024-10-08T12:25:00+00:00 |
| `20241020_132800_EMAIL-02663-eml` | email | [emails/2024-10/20241020_132800_EMAIL-02663.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241020_132800_EMAIL-02663.eml) | 2024-10-20T13:28:00+00:00 |
| `20241029_145000_EMAIL-02757-eml` | email | [emails/2024-10/20241029_145000_EMAIL-02757.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241029_145000_EMAIL-02757.eml) | 2024-10-29T14:50:00+00:00 |
| `20241107_200600_EMAIL-02843-eml` | email | [emails/2024-11/20241107_200600_EMAIL-02843.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241107_200600_EMAIL-02843.eml) | 2024-11-07T20:06:00+00:00 |
| `20241108_030600_EMAIL-02844-eml` | email | [emails/2024-11/20241108_030600_EMAIL-02844.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241108_030600_EMAIL-02844.eml) | 2024-11-08T03:06:00+00:00 |
| `20241114_173000_EMAIL-02910-eml` | email | [emails/2024-11/20241114_173000_EMAIL-02910.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241114_173000_EMAIL-02910.eml) | 2024-11-14T17:30:00+00:00 |
| `20241119_112700_EMAIL-02950-eml` | email | [emails/2024-11/20241119_112700_EMAIL-02950.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241119_112700_EMAIL-02950.eml) | 2024-11-19T11:27:00+00:00 |
| `20241206_184700_EMAIL-03107-eml` | email | [emails/2024-12/20241206_184700_EMAIL-03107.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241206_184700_EMAIL-03107.eml) | 2024-12-06T18:47:00+00:00 |
| `20241221_093200_EMAIL-03224-eml` | email | [emails/2024-12/20241221_093200_EMAIL-03224.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241221_093200_EMAIL-03224.eml) | 2024-12-21T09:32:00+00:00 |
| `20241227_080800_EMAIL-03286-eml` | email | [emails/2024-12/20241227_080800_EMAIL-03286.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241227_080800_EMAIL-03286.eml) | 2024-12-27T08:08:00+00:00 |
| `20250102_150800_EMAIL-03361-eml` | email | [emails/2025-01/20250102_150800_EMAIL-03361.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250102_150800_EMAIL-03361.eml) | 2025-01-02T15:08:00+00:00 |
| `20250117_153800_EMAIL-03495-eml` | email | [emails/2025-01/20250117_153800_EMAIL-03495.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250117_153800_EMAIL-03495.eml) | 2025-01-17T15:38:00+00:00 |
| `20250201_152000_EMAIL-03620-eml` | email | [emails/2025-02/20250201_152000_EMAIL-03620.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250201_152000_EMAIL-03620.eml) | 2025-02-01T15:20:00+00:00 |
| `20250221_111800_EMAIL-03802-eml` | email | [emails/2025-02/20250221_111800_EMAIL-03802.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250221_111800_EMAIL-03802.eml) | 2025-02-21T11:18:00+00:00 |
| `20250221_170100_EMAIL-03806-eml` | email | [emails/2025-02/20250221_170100_EMAIL-03806.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250221_170100_EMAIL-03806.eml) | 2025-02-21T17:01:00+00:00 |
| `20250223_050100_EMAIL-03817-eml` | email | [emails/2025-02/20250223_050100_EMAIL-03817.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250223_050100_EMAIL-03817.eml) | 2025-02-23T05:01:00+00:00 |
| `20250227_141600_EMAIL-03871-eml` | email | [emails/2025-02/20250227_141600_EMAIL-03871.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250227_141600_EMAIL-03871.eml) | 2025-02-27 |
| `20250304_061800_EMAIL-03914-eml` | email | [emails/2025-03/20250304_061800_EMAIL-03914.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250304_061800_EMAIL-03914.eml) | 2025-03-04T06:18:00+00:00 |
| `20250321_175700_EMAIL-04083-eml` | email | [emails/2025-03/20250321_175700_EMAIL-04083.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250321_175700_EMAIL-04083.eml) | 2025-03-21T17:57:00+00:00 |
| `20250330_005700_EMAIL-04154-eml` | email | [emails/2025-03/20250330_005700_EMAIL-04154.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250330_005700_EMAIL-04154.eml) | 2025-03-30T00:57:00+00:00 |
| `20250408_132600_EMAIL-04238-eml` | email | [emails/2025-04/20250408_132600_EMAIL-04238.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250408_132600_EMAIL-04238.eml) | 2025-04-08T13:26:00+00:00 |
| `20250420_125600_EMAIL-04339-eml` | email | [emails/2025-04/20250420_125600_EMAIL-04339.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250420_125600_EMAIL-04339.eml) | 2025-04-20T12:56:00+00:00 |
| `20250420_145600_EMAIL-04340-eml` | email | [emails/2025-04/20250420_145600_EMAIL-04340.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250420_145600_EMAIL-04340.eml) | 2025-04-20T14:56:00+00:00 |
| `20250519_113000_EMAIL-04559-eml` | email | [emails/2025-05/20250519_113000_EMAIL-04559.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250519_113000_EMAIL-04559.eml) | 2025-05-19T11:30:00+00:00 |
| `20250527_033000_EMAIL-04630-eml` | email | [emails/2025-05/20250527_033000_EMAIL-04630.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250527_033000_EMAIL-04630.eml) | 2025-05-27T03:30:00+00:00 |
| `20250528_145700_EMAIL-04647-eml` | email | [emails/2025-05/20250528_145700_EMAIL-04647.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250528_145700_EMAIL-04647.eml) | 2025-05-28T14:57:00+00:00 |
| `20250621_161800_EMAIL-04837-eml` | email | [emails/2025-06/20250621_161800_EMAIL-04837.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250621_161800_EMAIL-04837.eml) | 2025-06-21T16:18:00+00:00 |
| `20250623_140200_EMAIL-04857-eml` | email | [emails/2025-06/20250623_140200_EMAIL-04857.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250623_140200_EMAIL-04857.eml) | 2025-06-23T14:02:00+00:00 |
| `20250704_111600_EMAIL-04940-eml` | email | [emails/2025-07/20250704_111600_EMAIL-04940.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250704_111600_EMAIL-04940.eml) | 2025-07-04T11:16:00+00:00 |
| `20250729_162600_EMAIL-05158-eml` | email | [emails/2025-07/20250729_162600_EMAIL-05158.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250729_162600_EMAIL-05158.eml) | 2025-07-29T16:26:00+00:00 |
| `20250730_163500_EMAIL-05167-eml` | email | [emails/2025-07/20250730_163500_EMAIL-05167.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250730_163500_EMAIL-05167.eml) | 2025-07-30T16:35:00+00:00 |
| `20250809_130300_EMAIL-05234-eml` | email | [emails/2025-08/20250809_130300_EMAIL-05234.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250809_130300_EMAIL-05234.eml) | 2025-08-09T13:03:00+00:00 |
| `20250817_114400_EMAIL-05327-eml` | email | [emails/2025-08/20250817_114400_EMAIL-05327.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250817_114400_EMAIL-05327.eml) | 2025-08-17T11:44:00+00:00 |
| `20250819_014400_EMAIL-05345-eml` | email | [emails/2025-08/20250819_014400_EMAIL-05345.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250819_014400_EMAIL-05345.eml) | 2025-08-19T01:44:00+00:00 |
| `20250924_165600_EMAIL-05706-eml` | email | [emails/2025-09/20250924_165600_EMAIL-05706.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250924_165600_EMAIL-05706.eml) | 2025-09-24T16:56:00+00:00 |
| `20251012_113100_EMAIL-05848-eml` | email | [emails/2025-10/20251012_113100_EMAIL-05848.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251012_113100_EMAIL-05848.eml) | 2025-10-12T11:31:00+00:00 |
| `20251017_135100_EMAIL-05896-eml` | email | [emails/2025-10/20251017_135100_EMAIL-05896.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251017_135100_EMAIL-05896.eml) | 2025-10-17T13:51:00+00:00 |
| `20251017_235100_EMAIL-05901-eml` | email | [emails/2025-10/20251017_235100_EMAIL-05901.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251017_235100_EMAIL-05901.eml) | 2025-10-17T23:51:00+00:00 |
| `20251030_132500_EMAIL-06003-eml` | email | [emails/2025-10/20251030_132500_EMAIL-06003.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251030_132500_EMAIL-06003.eml) | 2025-10-30T13:25:00+00:00 |
| `20251031_222500_EMAIL-06012-eml` | email | [emails/2025-10/20251031_222500_EMAIL-06012.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251031_222500_EMAIL-06012.eml) | 2025-10-31T22:25:00+00:00 |
| `20251116_153500_EMAIL-06136-eml` | email | [emails/2025-11/20251116_153500_EMAIL-06136.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251116_153500_EMAIL-06136.eml) | 2025-11-16T15:35:00+00:00 |
| `20251123_135800_EMAIL-06206-eml` | email | [emails/2025-11/20251123_135800_EMAIL-06206.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251123_135800_EMAIL-06206.eml) | 2025-11-23T13:58:00+00:00 |
| `20251127_170800_EMAIL-06244-eml` | email | [emails/2025-11/20251127_170800_EMAIL-06244.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251127_170800_EMAIL-06244.eml) | 2025-11-27T17:08:00+00:00 |
| `20251129_110800_EMAIL-06256-eml` | email | [emails/2025-11/20251129_110800_EMAIL-06256.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251129_110800_EMAIL-06256.eml) | 2025-11-29T11:08:00+00:00 |
| `20251213_155800_EMAIL-06383-eml` | email | [emails/2025-12/20251213_155800_EMAIL-06383.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251213_155800_EMAIL-06383.eml) | 2025-12-13T15:58:00+00:00 |
| `20251217_091100_EMAIL-06417-eml` | email | [emails/2025-12/20251217_091100_EMAIL-06417.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251217_091100_EMAIL-06417.eml) | 2025-12-17T09:11:00+00:00 |
| `20251223_144700_EMAIL-06475-eml` | email | [emails/2025-12/20251223_144700_EMAIL-06475.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251223_144700_EMAIL-06475.eml) | 2025-12-23T14:47:00+00:00 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-25T20:52:09+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
