# context.unit.<!-- auto:unit_id -->EH-051<!-- /auto:unit_id -->.md

> Per-unit dossier (one file per Einheit). Holds everything specific to this unit:
> the unit itself, the active lease, the tenant(s), and all unit/tenant-specific operations.
> **Property-wide data lives in `context.property.md`** — see `parent_property_ref` below.

<!-- auto:meta -->
- last_built_at: `2026-04-25T20:53:19+00:00`
- build_hash: `engine-v2`
- engine_version: `0.2.0`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `unit`
- unit_id: `EH-051`
- property_id: `LIE-001`
- parent_property_ref: `context.property.LIE-001.md`
- owner_ref: `EIG-032`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit -->
- unit_id: `EH-051`
- label: WE 51
- haus_id: `HAUS-16`
- floor: 4. OG
- position: rechts
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
- lease_id: `LEASE-MIE-004`
- unit_ref: `EH-051`
- start_date: 2021-07-23 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-004)
- end_date: _(no data in source yet)_
- term_type: `unbefristet`
- cancellation_status: `by_tenant` (notice_date: 2024-07-27, move_out_date: —)
- rent_components: { kaltmiete: 1283.0, betriebskosten_vorauszahlung: 254.0, total_warmmiete: 1537.00 }
- payment_mode: Überweisung
- iban_payer: DE52100700006717565512 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-004)
- kaution: { amount: 3849.0 }
- usage: `residential`
- subletting: { current_status: `requested` }
- special_agreements: _(no data in source yet)_
<!-- /auto:lease -->

### 2.1 Tenants on this Lease
<!-- auto:tenants -->
| tenant_id | name | role | contact_email | contact_phone | comms_pref | gesamtschuldner |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-004` | Herr Horst-Günter Zänker | haupt | horst.guenter.zaenker@posteo.de | +49(0)5961 58657 | email | — |
<!-- /auto:tenants -->

---

## 3. Operations (this unit / this tenant)

### 3.1 Open Tickets — Critical (overdue or due ≤7 days)
<!-- auto:tickets.critical -->
| ticket_id | type | title | deadline | status | assignee |
| --- | --- | --- | --- | --- | --- |
| `TKT-d6c0f748` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-2c1b8cbf` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-b4ae39e4` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-2c729cda` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-80161fb5` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-ca4e17ba` | schimmel | Schimmel im Schlafzimmer | — | open | — |
<!-- /auto:tickets.critical -->

### 3.2 Open Tickets — Aggregate
<!-- auto:tickets.aggregate -->
- total_open: `16`
- by_type: { abfluss: `2`, fenster: `4`, schimmel: `3`, schluessel: `4`, wasserschaden: `3` }
- live source: `db.tickets WHERE unit_id=EH-051 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren

<!-- auto:dunning.summary -->[Routine] Mieter MIE-004 ist seit vier Monaten im Verzug; offener Betrag 6.148,00 EUR zzgl. 78,74 EUR Verzugszinsen, letzte Zahlung 2025-12-02 [(bank)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv#TX-01563). Vertraglich geschuldet sind monatlich 1.537,00 EUR (Kaltmiete 1.283,00 EUR + NK 254,00 EUR) [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-004). Verzug nach § 286 BGB festgestellt, Verzugszinsen § 288 I BGB; Mahnstufe 1 aktiv, nächster Schritt: 2. Mahnung nach 14 Tagen.<!-- /auto:dunning.summary -->

#### Per claim
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-004` | — | 1 | 6148.00 EUR | 2025-12-02 | — | — |
- live balance pointer: `db.tenant_balance.tenant_id=MIE-004`
<!-- /auto:dunning -->

### 3.4 Active Reductions / Deferrals (§ 536 BGB)
<!-- auto:reductions -->
- date_raised: 2024-01-31
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-02-01
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-02-08
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-01-26
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
| Mieterwechsel | 2024-07-27 | Kündigung erhalten | Verwaltung | TBD | Übergabe-Termin offen |
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
| `TH-f269b8` | Verkaufsabsicht WE 51 | 2024-12-12 | `EH-051` | active | 7 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241212_152500_EMAIL-03156.eml) |
| `TH-7fa943` | Mieterwechsel in WE 51 | 2025-07-09 | `EH-051` | active | 5 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250709_091800_EMAIL-04978.eml) |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `kontoauszug_2024_2025-csv` | bank | [bank/kontoauszug_2024_2025.csv](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv) | 2026-04-25 |
| `20240116_110000_EMAIL-00130-eml` | email | [emails/2024-01/20240116_110000_EMAIL-00130.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240116_110000_EMAIL-00130.eml) | 2024-01-16T11:00:00+00:00 |
| `20240122_123000_EMAIL-00178-eml` | email | [emails/2024-01/20240122_123000_EMAIL-00178.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240122_123000_EMAIL-00178.eml) | 2024-01-22T12:30:00+00:00 |
| `20240122_154100_EMAIL-00181-eml` | email | [emails/2024-01/20240122_154100_EMAIL-00181.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240122_154100_EMAIL-00181.eml) | 2024-01-22T15:41:00+00:00 |
| `20240127_120600_EMAIL-00214-eml` | email | [emails/2024-01/20240127_120600_EMAIL-00214.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240127_120600_EMAIL-00214.eml) | 2024-01-27T12:06:00+00:00 |
| `20240131_122300_EMAIL-00249-eml` | email | [emails/2024-01/20240131_122300_EMAIL-00249.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240131_122300_EMAIL-00249.eml) | 2024-01-31T12:23:00+00:00 |
| `20240201_112300_EMAIL-00262-eml` | email | [emails/2024-02/20240201_112300_EMAIL-00262.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240201_112300_EMAIL-00262.eml) | 2024-02-01T11:23:00+00:00 |
| `20240208_112300_EMAIL-00330-eml` | email | [emails/2024-02/20240208_112300_EMAIL-00330.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240208_112300_EMAIL-00330.eml) | 2024-02-08T11:23:00+00:00 |
| `20240216_141900_EMAIL-00399-eml` | email | [emails/2024-02/20240216_141900_EMAIL-00399.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240216_141900_EMAIL-00399.eml) | 2024-02-16T14:19:00+00:00 |
| `20240220_145200_EMAIL-00425-eml` | email | [emails/2024-02/20240220_145200_EMAIL-00425.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240220_145200_EMAIL-00425.eml) | 2024-02-20T14:52:00+00:00 |
| `20240306_104500_EMAIL-00562-eml` | email | [emails/2024-03/20240306_104500_EMAIL-00562.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240306_104500_EMAIL-00562.eml) | 2024-03-06T10:45:00+00:00 |
| `20240429_090700_EMAIL-01069-eml` | email | [emails/2024-04/20240429_090700_EMAIL-01069.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240429_090700_EMAIL-01069.eml) | 2024-04-29T09:07:00+00:00 |
| `20240430_050700_EMAIL-01075-eml` | email | [emails/2024-04/20240430_050700_EMAIL-01075.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240430_050700_EMAIL-01075.eml) | 2024-04-30T05:07:00+00:00 |
| `20240530_101300_EMAIL-01351-eml` | email | [emails/2024-05/20240530_101300_EMAIL-01351.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240530_101300_EMAIL-01351.eml) | 2024-05-30T10:13:00+00:00 |
| `20240530_173600_EMAIL-01357-eml` | email | [emails/2024-05/20240530_173600_EMAIL-01357.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240530_173600_EMAIL-01357.eml) | 2024-05-30T17:36:00+00:00 |
| `20240531_033500_EMAIL-01358-eml` | email | [emails/2024-05/20240531_033500_EMAIL-01358.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240531_033500_EMAIL-01358.eml) | 2024-05-31T03:35:00+00:00 |
| `20240706_120100_EMAIL-01673-eml` | email | [emails/2024-07/20240706_120100_EMAIL-01673.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240706_120100_EMAIL-01673.eml) | 2024-07-06T12:01:00+00:00 |
| `20240722_091100_EMAIL-01827-eml` | email | [emails/2024-07/20240722_091100_EMAIL-01827.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240722_091100_EMAIL-01827.eml) | 2024-07-22T09:11:00+00:00 |
| `20240727_203700_EMAIL-01885-eml` | email | [emails/2024-07/20240727_203700_EMAIL-01885.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240727_203700_EMAIL-01885.eml) | 2024-07-27T20:37:00+00:00 |
| `20240807_110100_EMAIL-01986-eml` | email | [emails/2024-08/20240807_110100_EMAIL-01986.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240807_110100_EMAIL-01986.eml) | 2024-08-07T11:01:00+00:00 |
| `20240818_085800_EMAIL-02073-eml` | email | [emails/2024-08/20240818_085800_EMAIL-02073.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240818_085800_EMAIL-02073.eml) | 2024-08-18T08:58:00+00:00 |
| `20240819_155300_EMAIL-02092-eml` | email | [emails/2024-08/20240819_155300_EMAIL-02092.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240819_155300_EMAIL-02092.eml) | 2024-08-19T15:53:00+00:00 |
| `20240922_120500_EMAIL-02411-eml` | email | [emails/2024-09/20240922_120500_EMAIL-02411.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240922_120500_EMAIL-02411.eml) | 2024-09-22T12:05:00+00:00 |
| `20240924_040500_EMAIL-02426-eml` | email | [emails/2024-09/20240924_040500_EMAIL-02426.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240924_040500_EMAIL-02426.eml) | 2024-09-24T04:05:00+00:00 |
| `20241001_150100_EMAIL-02489-eml` | email | [emails/2024-10/20241001_150100_EMAIL-02489.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241001_150100_EMAIL-02489.eml) | 2024-10-01T15:01:00+00:00 |
| `20241012_145300_EMAIL-02602-eml` | email | [emails/2024-10/20241012_145300_EMAIL-02602.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241012_145300_EMAIL-02602.eml) | 2024-10-12T14:53:00+00:00 |
| `20241103_125500_EMAIL-02806-eml` | email | [emails/2024-11/20241103_125500_EMAIL-02806.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241103_125500_EMAIL-02806.eml) | 2024-11-03T12:55:00+00:00 |
| `20241111_170900_EMAIL-02877-eml` | email | [emails/2024-11/20241111_170900_EMAIL-02877.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241111_170900_EMAIL-02877.eml) | 2024-11-11T17:09:00+00:00 |
| `20241112_145200_EMAIL-02884-eml` | email | [emails/2024-11/20241112_145200_EMAIL-02884.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241112_145200_EMAIL-02884.eml) | 2024-11-12T14:52:00+00:00 |
| `20241120_164700_EMAIL-02959-eml` | email | [emails/2024-11/20241120_164700_EMAIL-02959.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241120_164700_EMAIL-02959.eml) | 2024-11-20T16:47:00+00:00 |
| `20241125_173200_EMAIL-03009-eml` | email | [emails/2024-11/20241125_173200_EMAIL-03009.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241125_173200_EMAIL-03009.eml) | 2024-11-25T17:32:00+00:00 |
| `20241126_171400_EMAIL-03018-eml` | email | [emails/2024-11/20241126_171400_EMAIL-03018.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241126_171400_EMAIL-03018.eml) | 2024-11-26T17:14:00+00:00 |
| `20241212_152500_EMAIL-03156-eml` | email | [emails/2024-12/20241212_152500_EMAIL-03156.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241212_152500_EMAIL-03156.eml) | 2024-12-12 |
| `20250126_143000_EMAIL-03567-eml` | email | [emails/2025-01/20250126_143000_EMAIL-03567.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250126_143000_EMAIL-03567.eml) | 2025-01-26T14:30:00+00:00 |
| `20250206_165100_EMAIL-03666-eml` | email | [emails/2025-02/20250206_165100_EMAIL-03666.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250206_165100_EMAIL-03666.eml) | 2025-02-06T16:51:00+00:00 |
| `20250307_111900_EMAIL-03943-eml` | email | [emails/2025-03/20250307_111900_EMAIL-03943.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250307_111900_EMAIL-03943.eml) | 2025-03-07T11:19:00+00:00 |
| `20250527_145900_EMAIL-04637-eml` | email | [emails/2025-05/20250527_145900_EMAIL-04637.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250527_145900_EMAIL-04637.eml) | 2025-05-27T14:59:00+00:00 |
| `20250605_104900_EMAIL-04705-eml` | email | [emails/2025-06/20250605_104900_EMAIL-04705.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250605_104900_EMAIL-04705.eml) | 2025-06-05T10:49:00+00:00 |
| `20250709_091800_EMAIL-04978-eml` | email | [emails/2025-07/20250709_091800_EMAIL-04978.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250709_091800_EMAIL-04978.eml) | 2025-07-09 |
| `20250716_140600_EMAIL-05055-eml` | email | [emails/2025-07/20250716_140600_EMAIL-05055.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250716_140600_EMAIL-05055.eml) | 2025-07-16T14:06:00+00:00 |
| `20250803_082500_EMAIL-05191-eml` | email | [emails/2025-08/20250803_082500_EMAIL-05191.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250803_082500_EMAIL-05191.eml) | 2025-08-03T08:25:00+00:00 |
| `20250810_103400_EMAIL-05243-eml` | email | [emails/2025-08/20250810_103400_EMAIL-05243.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250810_103400_EMAIL-05243.eml) | 2025-08-10T10:34:00+00:00 |
| `20250823_105200_EMAIL-05381-eml` | email | [emails/2025-08/20250823_105200_EMAIL-05381.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250823_105200_EMAIL-05381.eml) | 2025-08-23T10:52:00+00:00 |
| `20250909_094500_EMAIL-05578-eml` | email | [emails/2025-09/20250909_094500_EMAIL-05578.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250909_094500_EMAIL-05578.eml) | 2025-09-09T09:45:00+00:00 |
| `20250915_165700_EMAIL-05632-eml` | email | [emails/2025-09/20250915_165700_EMAIL-05632.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250915_165700_EMAIL-05632.eml) | 2025-09-15T16:57:00+00:00 |
| `20251023_103800_EMAIL-05944-eml` | email | [emails/2025-10/20251023_103800_EMAIL-05944.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251023_103800_EMAIL-05944.eml) | 2025-10-23T10:38:00+00:00 |
| `20251124_181600_EMAIL-06214-eml` | email | [emails/2025-11/20251124_181600_EMAIL-06214.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251124_181600_EMAIL-06214.eml) | 2025-11-24T18:16:00+00:00 |
| `20251216_145500_EMAIL-06414-eml` | email | [emails/2025-12/20251216_145500_EMAIL-06414.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251216_145500_EMAIL-06414.eml) | 2025-12-16T14:55:00+00:00 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-25T20:52:09+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
