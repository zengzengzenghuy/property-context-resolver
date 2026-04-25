# context.unit.<!-- auto:unit_id -->EH-039<!-- /auto:unit_id -->.md

> Per-unit dossier (one file per Einheit). Holds everything specific to this unit:
> the unit itself, the active lease, the tenant(s), and all unit/tenant-specific operations.
> **Property-wide data lives in `context.property.md`** — see `parent_property_ref` below.

<!-- auto:meta -->
- last_built_at: `2026-04-25T20:53:03+00:00`
- build_hash: `engine-v2`
- engine_version: `0.2.0`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `unit`
- unit_id: `EH-039`
- property_id: `LIE-001`
- parent_property_ref: `context.property.LIE-001.md`
- owner_ref: `EIG-021`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit -->
- unit_id: `EH-039`
- label: WE 39
- haus_id: `HAUS-16`
- floor: 1. OG
- position: links
- typ: Wohnung
- area_sqm: 64.0
- rooms: 2.0
- mea_‰: 149
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
- lease_id: `LEASE-MIE-014`
- unit_ref: `EH-039`
- start_date: 2022-02-26 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-014)
- end_date: _(no data in source yet)_
- term_type: `unbefristet`
- cancellation_status: `by_tenant` (notice_date: 2025-09-13, move_out_date: —)
- rent_components: { kaltmiete: 946.0, betriebskosten_vorauszahlung: 181.0, total_warmmiete: 1127.00 }
- payment_mode: Überweisung
- iban_payer: DE11100100103695944064 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-014)
- kaution: { amount: 2838.0 }
- usage: `residential`
- subletting: { current_status: `requested` }
- special_agreements: _(no data in source yet)_
<!-- /auto:lease -->

### 2.1 Tenants on this Lease
<!-- auto:tenants -->
| tenant_id | name | role | contact_email | contact_phone | comms_pref | gesamtschuldner |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-014` | Frau Wilma Roht | haupt | wilma.roht@gmail.com | 01604817549 | email | — |
<!-- /auto:tenants -->

---

## 3. Operations (this unit / this tenant)

### 3.1 Open Tickets — Critical (overdue or due ≤7 days)
<!-- auto:tickets.critical -->
| ticket_id | type | title | deadline | status | assignee |
| --- | --- | --- | --- | --- | --- |
| `TKT-3a588571` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-8bb9b7fe` | wasserschaden | Wasserschaden Bad | — | open | — |
<!-- /auto:tickets.critical -->

### 3.2 Open Tickets — Aggregate
<!-- auto:tickets.aggregate -->
- total_open: `12`
- by_type: { abfluss: `4`, fenster: `4`, schluessel: `2`, wasserschaden: `2` }
- live source: `db.tickets WHERE unit_id=EH-039 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren

<!-- auto:dunning.summary -->[Routine] Mieter MIE-014 ist seit vier Monaten im Verzug; offener Betrag 4.508,00 EUR zzgl. 57,74 EUR Verzugszinsen, letzte Zahlung 2025-12-02 [(bank)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv#TX-01566). Vertraglich geschuldet sind monatlich 1.127,00 EUR (Kaltmiete 946,00 EUR + NK 181,00 EUR) [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-014). Verzug nach § 286 BGB festgestellt, Verzugszinsen § 288 I BGB; Mahnstufe 1 aktiv, nächster Schritt: 2. Mahnung nach 14 Tagen.<!-- /auto:dunning.summary -->

#### Per claim
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-014` | — | 1 | 4508.00 EUR | 2025-12-02 | — | — |
- live balance pointer: `db.tenant_balance.tenant_id=MIE-014`
<!-- /auto:dunning -->

### 3.4 Active Reductions / Deferrals (§ 536 BGB)
<!-- auto:reductions -->
- date_raised: 2024-01-03
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-04-12
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-05-22
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-07-30
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-08-01
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-04-24
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
| Mieterwechsel | 2025-09-13 | Kündigung erhalten | Verwaltung | TBD | Übergabe-Termin offen |
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
| `TH-e16b61` | Kuendigung Mietvertrag | 2025-12-31 | `MIE-014` | active | 124 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251231_163500_EMAIL-06543.eml) |
| `TH-962ff1` | Verkaufsabsicht WE 39 | 2025-09-07 | `EH-039` | active | 4 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250907_140300_EMAIL-05558.eml) |
| `TH-dfaf2f` | Mieterwechsel in WE 39 | 2025-07-14 | `EH-039` | active | 5 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250714_115100_EMAIL-05028.eml) |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `kontoauszug_2024_2025-csv` | bank | [bank/kontoauszug_2024_2025.csv](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv) | 2026-04-25 |
| `20240103_155000_EMAIL-00020-eml` | email | [emails/2024-01/20240103_155000_EMAIL-00020.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240103_155000_EMAIL-00020.eml) | 2024-01-03T15:50:00+00:00 |
| `20240127_152200_EMAIL-00217-eml` | email | [emails/2024-01/20240127_152200_EMAIL-00217.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240127_152200_EMAIL-00217.eml) | 2024-01-27T15:22:00+00:00 |
| `20240205_114200_EMAIL-00306-eml` | email | [emails/2024-02/20240205_114200_EMAIL-00306.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240205_114200_EMAIL-00306.eml) | 2024-02-05T11:42:00+00:00 |
| `20240207_201400_EMAIL-00325-eml` | email | [emails/2024-02/20240207_201400_EMAIL-00325.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240207_201400_EMAIL-00325.eml) | 2024-02-07T20:14:00+00:00 |
| `20240220_180900_EMAIL-00430-eml` | email | [emails/2024-02/20240220_180900_EMAIL-00430.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240220_180900_EMAIL-00430.eml) | 2024-02-20T18:09:00+00:00 |
| `20240305_114200_EMAIL-00554-eml` | email | [emails/2024-03/20240305_114200_EMAIL-00554.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240305_114200_EMAIL-00554.eml) | 2024-03-05T11:42:00+00:00 |
| `20240314_103800_EMAIL-00638-eml` | email | [emails/2024-03/20240314_103800_EMAIL-00638.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240314_103800_EMAIL-00638.eml) | 2024-03-14T10:38:00+00:00 |
| `20240321_153000_EMAIL-00699-eml` | email | [emails/2024-03/20240321_153000_EMAIL-00699.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240321_153000_EMAIL-00699.eml) | 2024-03-21T15:30:00+00:00 |
| `20240408_112300_EMAIL-00869-eml` | email | [emails/2024-04/20240408_112300_EMAIL-00869.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240408_112300_EMAIL-00869.eml) | 2024-04-08T11:23:00+00:00 |
| `20240412_083900_EMAIL-00910-eml` | email | [emails/2024-04/20240412_083900_EMAIL-00910.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240412_083900_EMAIL-00910.eml) | 2024-04-12T08:39:00+00:00 |
| `20240412_133200_EMAIL-00913-eml` | email | [emails/2024-04/20240412_133200_EMAIL-00913.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240412_133200_EMAIL-00913.eml) | 2024-04-12T13:32:00+00:00 |
| `20240412_143900_EMAIL-00914-eml` | email | [emails/2024-04/20240412_143900_EMAIL-00914.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240412_143900_EMAIL-00914.eml) | 2024-04-12T14:39:00+00:00 |
| `20240413_203300_EMAIL-00932-eml` | email | [emails/2024-04/20240413_203300_EMAIL-00932.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240413_203300_EMAIL-00932.eml) | 2024-04-13T20:33:00+00:00 |
| `20240423_223300_EMAIL-01033-eml` | email | [emails/2024-04/20240423_223300_EMAIL-01033.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240423_223300_EMAIL-01033.eml) | 2024-04-23T22:33:00+00:00 |
| `20240522_153400_EMAIL-01282-eml` | email | [emails/2024-05/20240522_153400_EMAIL-01282.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240522_153400_EMAIL-01282.eml) | 2024-05-22T15:34:00+00:00 |
| `20240628_170100_EMAIL-01613-eml` | email | [emails/2024-06/20240628_170100_EMAIL-01613.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240628_170100_EMAIL-01613.eml) | 2024-06-28T17:01:00+00:00 |
| `20240628_220100_EMAIL-01615-eml` | email | [emails/2024-06/20240628_220100_EMAIL-01615.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240628_220100_EMAIL-01615.eml) | 2024-06-28T22:01:00+00:00 |
| `20240705_220100_EMAIL-01669-eml` | email | [emails/2024-07/20240705_220100_EMAIL-01669.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240705_220100_EMAIL-01669.eml) | 2024-07-05T22:01:00+00:00 |
| `20240709_145800_EMAIL-01710-eml` | email | [emails/2024-07/20240709_145800_EMAIL-01710.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240709_145800_EMAIL-01710.eml) | 2024-07-09T14:58:00+00:00 |
| `20240730_100900_EMAIL-01904-eml` | email | [emails/2024-07/20240730_100900_EMAIL-01904.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240730_100900_EMAIL-01904.eml) | 2024-07-30T10:09:00+00:00 |
| `20240730_123900_EMAIL-01906-eml` | email | [emails/2024-07/20240730_123900_EMAIL-01906.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240730_123900_EMAIL-01906.eml) | 2024-07-30T12:39:00+00:00 |
| `20240731_020900_EMAIL-01910-eml` | email | [emails/2024-07/20240731_020900_EMAIL-01910.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240731_020900_EMAIL-01910.eml) | 2024-07-31T02:09:00+00:00 |
| `20240801_073900_EMAIL-01918-eml` | email | [emails/2024-08/20240801_073900_EMAIL-01918.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240801_073900_EMAIL-01918.eml) | 2024-08-01T07:39:00+00:00 |
| `20240813_144900_EMAIL-02026-eml` | email | [emails/2024-08/20240813_144900_EMAIL-02026.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240813_144900_EMAIL-02026.eml) | 2024-08-13T14:49:00+00:00 |
| `20240814_084900_EMAIL-02031-eml` | email | [emails/2024-08/20240814_084900_EMAIL-02031.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240814_084900_EMAIL-02031.eml) | 2024-08-14T08:49:00+00:00 |
| `20240816_162000_EMAIL-02061-eml` | email | [emails/2024-08/20240816_162000_EMAIL-02061.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240816_162000_EMAIL-02061.eml) | 2024-08-16T16:20:00+00:00 |
| `20240817_084900_EMAIL-02066-eml` | email | [emails/2024-08/20240817_084900_EMAIL-02066.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240817_084900_EMAIL-02066.eml) | 2024-08-17T08:49:00+00:00 |
| `20240817_132000_EMAIL-02070-eml` | email | [emails/2024-08/20240817_132000_EMAIL-02070.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240817_132000_EMAIL-02070.eml) | 2024-08-17T13:20:00+00:00 |
| `20240913_185000_EMAIL-02344-eml` | email | [emails/2024-09/20240913_185000_EMAIL-02344.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240913_185000_EMAIL-02344.eml) | 2024-09-13T18:50:00+00:00 |
| `20240915_045000_EMAIL-02358-eml` | email | [emails/2024-09/20240915_045000_EMAIL-02358.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240915_045000_EMAIL-02358.eml) | 2024-09-15T04:50:00+00:00 |
| `20240915_093500_EMAIL-02359-eml` | email | [emails/2024-09/20240915_093500_EMAIL-02359.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240915_093500_EMAIL-02359.eml) | 2024-09-15T09:35:00+00:00 |
| `20240918_045000_EMAIL-02373-eml` | email | [emails/2024-09/20240918_045000_EMAIL-02373.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240918_045000_EMAIL-02373.eml) | 2024-09-18T04:50:00+00:00 |
| `20240918_112000_EMAIL-02376-eml` | email | [emails/2024-09/20240918_112000_EMAIL-02376.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240918_112000_EMAIL-02376.eml) | 2024-09-18T11:20:00+00:00 |
| `20241003_155300_EMAIL-02505-eml` | email | [emails/2024-10/20241003_155300_EMAIL-02505.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241003_155300_EMAIL-02505.eml) | 2024-10-03T15:53:00+00:00 |
| `20241004_085300_EMAIL-02510-eml` | email | [emails/2024-10/20241004_085300_EMAIL-02510.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241004_085300_EMAIL-02510.eml) | 2024-10-04T08:53:00+00:00 |
| `20241013_205500_EMAIL-02607-eml` | email | [emails/2024-10/20241013_205500_EMAIL-02607.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241013_205500_EMAIL-02607.eml) | 2024-10-13T20:55:00+00:00 |
| `20241113_125400_EMAIL-02892-eml` | email | [emails/2024-11/20241113_125400_EMAIL-02892.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241113_125400_EMAIL-02892.eml) | 2024-11-13T12:54:00+00:00 |
| `20241120_103600_EMAIL-02954-eml` | email | [emails/2024-11/20241120_103600_EMAIL-02954.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241120_103600_EMAIL-02954.eml) | 2024-11-20T10:36:00+00:00 |
| `20241125_182300_EMAIL-03010-eml` | email | [emails/2024-11/20241125_182300_EMAIL-03010.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241125_182300_EMAIL-03010.eml) | 2024-11-25T18:23:00+00:00 |
| `20241213_110500_EMAIL-03164-eml` | email | [emails/2024-12/20241213_110500_EMAIL-03164.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241213_110500_EMAIL-03164.eml) | 2024-12-13T11:05:00+00:00 |
| `20241214_090500_EMAIL-03170-eml` | email | [emails/2024-12/20241214_090500_EMAIL-03170.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241214_090500_EMAIL-03170.eml) | 2024-12-14T09:05:00+00:00 |
| `20241224_090300_EMAIL-03257-eml` | email | [emails/2024-12/20241224_090300_EMAIL-03257.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241224_090300_EMAIL-03257.eml) | 2024-12-24T09:03:00+00:00 |
| `20250106_140900_EMAIL-03396-eml` | email | [emails/2025-01/20250106_140900_EMAIL-03396.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250106_140900_EMAIL-03396.eml) | 2025-01-06T14:09:00+00:00 |
| `20250122_161300_EMAIL-03540-eml` | email | [emails/2025-01/20250122_161300_EMAIL-03540.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250122_161300_EMAIL-03540.eml) | 2025-01-22T16:13:00+00:00 |
| `20250122_172400_EMAIL-03541-eml` | email | [emails/2025-01/20250122_172400_EMAIL-03541.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250122_172400_EMAIL-03541.eml) | 2025-01-22T17:24:00+00:00 |
| `20250124_185800_EMAIL-03555-eml` | email | [emails/2025-01/20250124_185800_EMAIL-03555.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250124_185800_EMAIL-03555.eml) | 2025-01-24T18:58:00+00:00 |
| `20250131_105400_EMAIL-03609-eml` | email | [emails/2025-01/20250131_105400_EMAIL-03609.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250131_105400_EMAIL-03609.eml) | 2025-01-31T10:54:00+00:00 |
| `20250218_122900_EMAIL-03773-eml` | email | [emails/2025-02/20250218_122900_EMAIL-03773.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250218_122900_EMAIL-03773.eml) | 2025-02-18T12:29:00+00:00 |
| `20250311_154700_EMAIL-03989-eml` | email | [emails/2025-03/20250311_154700_EMAIL-03989.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250311_154700_EMAIL-03989.eml) | 2025-03-11T15:47:00+00:00 |
| `20250407_040300_EMAIL-04228-eml` | email | [emails/2025-04/20250407_040300_EMAIL-04228.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250407_040300_EMAIL-04228.eml) | 2025-04-07T04:03:00+00:00 |
| `20250417_094900_EMAIL-04312-eml` | email | [emails/2025-04/20250417_094900_EMAIL-04312.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250417_094900_EMAIL-04312.eml) | 2025-04-17T09:49:00+00:00 |
| `20250424_120600_EMAIL-04364-eml` | email | [emails/2025-04/20250424_120600_EMAIL-04364.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250424_120600_EMAIL-04364.eml) | 2025-04-24T12:06:00+00:00 |
| `20250429_121200_EMAIL-04395-eml` | email | [emails/2025-04/20250429_121200_EMAIL-04395.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250429_121200_EMAIL-04395.eml) | 2025-04-29T12:12:00+00:00 |
| `20250522_161500_EMAIL-04592-eml` | email | [emails/2025-05/20250522_161500_EMAIL-04592.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250522_161500_EMAIL-04592.eml) | 2025-05-22T16:15:00+00:00 |
| `20250602_151500_EMAIL-04691-eml` | email | [emails/2025-06/20250602_151500_EMAIL-04691.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250602_151500_EMAIL-04691.eml) | 2025-06-02T15:15:00+00:00 |
| `20250709_155300_EMAIL-04981-eml` | email | [emails/2025-07/20250709_155300_EMAIL-04981.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250709_155300_EMAIL-04981.eml) | 2025-07-09T15:53:00+00:00 |
| `20250714_115100_EMAIL-05028-eml` | email | [emails/2025-07/20250714_115100_EMAIL-05028.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250714_115100_EMAIL-05028.eml) | 2025-07-14 |
| `20250815_114100_EMAIL-05303-eml` | email | [emails/2025-08/20250815_114100_EMAIL-05303.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250815_114100_EMAIL-05303.eml) | 2025-08-15T11:41:00+00:00 |
| `20250903_101900_EMAIL-05504-eml` | email | [emails/2025-09/20250903_101900_EMAIL-05504.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250903_101900_EMAIL-05504.eml) | 2025-09-03T10:19:00+00:00 |
| `20250907_140300_EMAIL-05558-eml` | email | [emails/2025-09/20250907_140300_EMAIL-05558.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250907_140300_EMAIL-05558.eml) | 2025-09-07 |
| `20250912_154700_EMAIL-05611-eml` | email | [emails/2025-09/20250912_154700_EMAIL-05611.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250912_154700_EMAIL-05611.eml) | 2025-09-12T15:47:00+00:00 |
| `20250913_170600_EMAIL-05617-eml` | email | [emails/2025-09/20250913_170600_EMAIL-05617.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250913_170600_EMAIL-05617.eml) | 2025-09-13T17:06:00+00:00 |
| `20250917_201900_EMAIL-05647-eml` | email | [emails/2025-09/20250917_201900_EMAIL-05647.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250917_201900_EMAIL-05647.eml) | 2025-09-17T20:19:00+00:00 |
| `20251022_140700_EMAIL-05936-eml` | email | [emails/2025-10/20251022_140700_EMAIL-05936.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251022_140700_EMAIL-05936.eml) | 2025-10-22T14:07:00+00:00 |
| `20251117_080500_EMAIL-06144-eml` | email | [emails/2025-11/20251117_080500_EMAIL-06144.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251117_080500_EMAIL-06144.eml) | 2025-11-17T08:05:00+00:00 |
| `20251125_093300_EMAIL-06217-eml` | email | [emails/2025-11/20251125_093300_EMAIL-06217.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251125_093300_EMAIL-06217.eml) | 2025-11-25T09:33:00+00:00 |
| `20251127_182200_EMAIL-06247-eml` | email | [emails/2025-11/20251127_182200_EMAIL-06247.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251127_182200_EMAIL-06247.eml) | 2025-11-27T18:22:00+00:00 |
| `20251231_163500_EMAIL-06543-eml` | email | [emails/2025-12/20251231_163500_EMAIL-06543.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251231_163500_EMAIL-06543.eml) | 2025-12-31 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-25T20:52:09+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
