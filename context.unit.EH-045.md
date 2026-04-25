# context.unit.<!-- auto:unit_id -->EH-045<!-- /auto:unit_id -->.md

> Per-unit dossier (one file per Einheit). Holds everything specific to this unit:
> the unit itself, the active lease, the tenant(s), and all unit/tenant-specific operations.
> **Property-wide data lives in `context.property.md`** — see `parent_property_ref` below.

<!-- auto:meta -->
- last_built_at: `2026-04-25T20:53:09+00:00`
- build_hash: `engine-v2`
- engine_version: `0.2.0`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `unit`
- unit_id: `EH-045`
- property_id: `LIE-001`
- parent_property_ref: `context.property.LIE-001.md`
- owner_ref: `EIG-020`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit -->
- unit_id: `EH-045`
- label: WE 45
- haus_id: `HAUS-16`
- floor: 3. OG
- position: links
- typ: Wohnung
- area_sqm: 66.0
- rooms: 2.0
- mea_‰: 153
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
- lease_id: `LEASE-MIE-006`
- unit_ref: `EH-045`
- start_date: 2023-01-29 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-006)
- end_date: _(no data in source yet)_
- term_type: `unbefristet`
- cancellation_status: `by_tenant` (notice_date: 2025-09-08, move_out_date: —)
- rent_components: { kaltmiete: 1076.0, betriebskosten_vorauszahlung: 180.0, total_warmmiete: 1256.00 }
- payment_mode: Überweisung
- iban_payer: DE80370400447710932480 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-006)
- kaution: { amount: 3228.0 }
- usage: `residential`
- subletting: { current_status: `requested` }
- special_agreements: _(no data in source yet)_
<!-- /auto:lease -->

### 2.1 Tenants on this Lease
<!-- auto:tenants -->
| tenant_id | name | role | contact_email | contact_phone | comms_pref | gesamtschuldner |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-006` | Frau Chantal Täsche | haupt | chantal.taesche@posteo.de | +49(0)0050 45562 | email | — |
<!-- /auto:tenants -->

---

## 3. Operations (this unit / this tenant)

### 3.1 Open Tickets — Critical (overdue or due ≤7 days)
<!-- auto:tickets.critical -->
| ticket_id | type | title | deadline | status | assignee |
| --- | --- | --- | --- | --- | --- |
| `TKT-c180598d` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-7301a7ae` | schimmel | Re: Schimmel im Schlafzimmer | — | open | — |
| `TKT-d78146e5` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-0d3ccbc0` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-a738e600` | wasserschaden | Re: Wasserschaden Bad | — | open | — |
| `TKT-540c54ea` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-6ee677bd` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-52973c48` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-54ed3109` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-1e3b8b8c` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-32485638` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-299892ad` | schimmel | Schimmel im Schlafzimmer | — | open | — |
<!-- /auto:tickets.critical -->

### 3.2 Open Tickets — Aggregate
<!-- auto:tickets.aggregate -->
- total_open: `21`
- by_type: { abfluss: `3`, schimmel: `7`, schluessel: `6`, wasserschaden: `5` }
- live source: `db.tickets WHERE unit_id=EH-045 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren

<!-- auto:dunning.summary -->[Routine] Mieter MIE-006 ist seit vier Monaten im Verzug; offener Betrag 5.024,00 EUR zzgl. 64,35 EUR Verzugszinsen, letzte Zahlung 2025-12-03 [(bank)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv#TX-01578). Vertraglich geschuldet sind monatlich 1.256,00 EUR (Kaltmiete 1.076,00 EUR + NK 273,00 EUR); Mahnstufe 1 seit 2025-07-17 [(letter)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/briefe/2025-07/20250717_mahnung_LTR-0132.pdf). Verzug nach § 286 BGB, Verzugszinsen § 288 I BGB (Basiszins + 5pp); nächster Schritt: 2. Mahnung nach Verzugsfrist.<!-- /auto:dunning.summary -->

#### Per claim
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-006` | — | 1 | 5024.00 EUR | 2025-12-03 | — | — |
- live balance pointer: `db.tenant_balance.tenant_id=MIE-006`
<!-- /auto:dunning -->

### 3.4 Active Reductions / Deferrals (§ 536 BGB)
<!-- auto:reductions -->
- date_raised: 2024-03-02
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-04-21
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-04-22
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-12-21
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-12-22
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-12-09
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-12-13
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-12-14
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
| Mieterwechsel | 2025-09-08 | Kündigung erhalten | Verwaltung | TBD | Übergabe-Termin offen |
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
| `20250717_mahnung_LTR-0132-pdf` | letter | [briefe/2025-07/20250717_mahnung_LTR-0132.pdf](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/briefe/2025-07/20250717_mahnung_LTR-0132.pdf) | 2026-04-25 |
| `20240107_114300_EMAIL-00049-eml` | email | [emails/2024-01/20240107_114300_EMAIL-00049.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240107_114300_EMAIL-00049.eml) | 2024-01-07T11:43:00+00:00 |
| `20240115_113200_EMAIL-00123-eml` | email | [emails/2024-01/20240115_113200_EMAIL-00123.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240115_113200_EMAIL-00123.eml) | 2024-01-15T11:32:00+00:00 |
| `20240128_155200_EMAIL-00225-eml` | email | [emails/2024-01/20240128_155200_EMAIL-00225.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240128_155200_EMAIL-00225.eml) | 2024-01-28T15:52:00+00:00 |
| `20240129_185200_EMAIL-00238-eml` | email | [emails/2024-01/20240129_185200_EMAIL-00238.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240129_185200_EMAIL-00238.eml) | 2024-01-29T18:52:00+00:00 |
| `20240302_112700_EMAIL-00529-eml` | email | [emails/2024-03/20240302_112700_EMAIL-00529.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240302_112700_EMAIL-00529.eml) | 2024-03-02T11:27:00+00:00 |
| `20240303_104400_EMAIL-00534-eml` | email | [emails/2024-03/20240303_104400_EMAIL-00534.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240303_104400_EMAIL-00534.eml) | 2024-03-03T10:44:00+00:00 |
| `20240305_054400_EMAIL-00553-eml` | email | [emails/2024-03/20240305_054400_EMAIL-00553.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240305_054400_EMAIL-00553.eml) | 2024-03-05T05:44:00+00:00 |
| `20240308_104200_EMAIL-00585-eml` | email | [emails/2024-03/20240308_104200_EMAIL-00585.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240308_104200_EMAIL-00585.eml) | 2024-03-08T10:42:00+00:00 |
| `20240314_124900_EMAIL-00642-eml` | email | [emails/2024-03/20240314_124900_EMAIL-00642.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240314_124900_EMAIL-00642.eml) | 2024-03-14T12:49:00+00:00 |
| `20240318_143900_EMAIL-00677-eml` | email | [emails/2024-03/20240318_143900_EMAIL-00677.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240318_143900_EMAIL-00677.eml) | 2024-03-18T14:39:00+00:00 |
| `20240421_101400_EMAIL-01006-eml` | email | [emails/2024-04/20240421_101400_EMAIL-01006.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240421_101400_EMAIL-01006.eml) | 2024-04-21T10:14:00+00:00 |
| `20240422_161400_EMAIL-01018-eml` | email | [emails/2024-04/20240422_161400_EMAIL-01018.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240422_161400_EMAIL-01018.eml) | 2024-04-22T16:14:00+00:00 |
| `20240503_130400_EMAIL-01109-eml` | email | [emails/2024-05/20240503_130400_EMAIL-01109.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240503_130400_EMAIL-01109.eml) | 2024-05-03T13:04:00+00:00 |
| `20240504_113400_EMAIL-01118-eml` | email | [emails/2024-05/20240504_113400_EMAIL-01118.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240504_113400_EMAIL-01118.eml) | 2024-05-04T11:34:00+00:00 |
| `20240505_023400_EMAIL-01123-eml` | email | [emails/2024-05/20240505_023400_EMAIL-01123.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240505_023400_EMAIL-01123.eml) | 2024-05-05T02:34:00+00:00 |
| `20240611_173900_EMAIL-01469-eml` | email | [emails/2024-06/20240611_173900_EMAIL-01469.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240611_173900_EMAIL-01469.eml) | 2024-06-11T17:39:00+00:00 |
| `20240612_144900_EMAIL-01478-eml` | email | [emails/2024-06/20240612_144900_EMAIL-01478.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240612_144900_EMAIL-01478.eml) | 2024-06-12T14:49:00+00:00 |
| `20240625_125300_EMAIL-01586-eml` | email | [emails/2024-06/20240625_125300_EMAIL-01586.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240625_125300_EMAIL-01586.eml) | 2024-06-25T12:53:00+00:00 |
| `20240625_171700_EMAIL-01588-eml` | email | [emails/2024-06/20240625_171700_EMAIL-01588.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240625_171700_EMAIL-01588.eml) | 2024-06-25T17:17:00+00:00 |
| `20240630_103300_EMAIL-01626-eml` | email | [emails/2024-06/20240630_103300_EMAIL-01626.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240630_103300_EMAIL-01626.eml) | 2024-06-30T10:33:00+00:00 |
| `20240705_155300_EMAIL-01666-eml` | email | [emails/2024-07/20240705_155300_EMAIL-01666.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240705_155300_EMAIL-01666.eml) | 2024-07-05T15:53:00+00:00 |
| `20240801_140400_EMAIL-01924-eml` | email | [emails/2024-08/20240801_140400_EMAIL-01924.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240801_140400_EMAIL-01924.eml) | 2024-08-01T14:04:00+00:00 |
| `20240802_060400_EMAIL-01929-eml` | email | [emails/2024-08/20240802_060400_EMAIL-01929.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240802_060400_EMAIL-01929.eml) | 2024-08-02T06:04:00+00:00 |
| `20240820_145000_EMAIL-02109-eml` | email | [emails/2024-08/20240820_145000_EMAIL-02109.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240820_145000_EMAIL-02109.eml) | 2024-08-20T14:50:00+00:00 |
| `20240821_171400_EMAIL-02116-eml` | email | [emails/2024-08/20240821_171400_EMAIL-02116.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240821_171400_EMAIL-02116.eml) | 2024-08-21T17:14:00+00:00 |
| `20240908_140300_EMAIL-02291-eml` | email | [emails/2024-09/20240908_140300_EMAIL-02291.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240908_140300_EMAIL-02291.eml) | 2024-09-08T14:03:00+00:00 |
| `20240912_110500_EMAIL-02324-eml` | email | [emails/2024-09/20240912_110500_EMAIL-02324.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240912_110500_EMAIL-02324.eml) | 2024-09-12T11:05:00+00:00 |
| `20241008_095500_EMAIL-02553-eml` | email | [emails/2024-10/20241008_095500_EMAIL-02553.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241008_095500_EMAIL-02553.eml) | 2024-10-08T09:55:00+00:00 |
| `20241014_140800_EMAIL-02610-eml` | email | [emails/2024-10/20241014_140800_EMAIL-02610.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241014_140800_EMAIL-02610.eml) | 2024-10-14T14:08:00+00:00 |
| `20241019_184700_EMAIL-02658-eml` | email | [emails/2024-10/20241019_184700_EMAIL-02658.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241019_184700_EMAIL-02658.eml) | 2024-10-19T18:47:00+00:00 |
| `20241023_100100_EMAIL-02694-eml` | email | [emails/2024-10/20241023_100100_EMAIL-02694.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241023_100100_EMAIL-02694.eml) | 2024-10-23T10:01:00+00:00 |
| `20241030_145900_EMAIL-02764-eml` | email | [emails/2024-10/20241030_145900_EMAIL-02764.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241030_145900_EMAIL-02764.eml) | 2024-10-30T14:59:00+00:00 |
| `20241102_221800_EMAIL-02801-eml` | email | [emails/2024-11/20241102_221800_EMAIL-02801.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241102_221800_EMAIL-02801.eml) | 2024-11-02T22:18:00+00:00 |
| `20241110_175900_EMAIL-02867-eml` | email | [emails/2024-11/20241110_175900_EMAIL-02867.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241110_175900_EMAIL-02867.eml) | 2024-11-10T17:59:00+00:00 |
| `20241118_120000_EMAIL-02944-eml` | email | [emails/2024-11/20241118_120000_EMAIL-02944.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241118_120000_EMAIL-02944.eml) | 2024-11-18T12:00:00+00:00 |
| `20241202_102500_EMAIL-03066-eml` | email | [emails/2024-12/20241202_102500_EMAIL-03066.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241202_102500_EMAIL-03066.eml) | 2024-12-02T10:25:00+00:00 |
| `20241211_155000_EMAIL-03149-eml` | email | [emails/2024-12/20241211_155000_EMAIL-03149.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241211_155000_EMAIL-03149.eml) | 2024-12-11T15:50:00+00:00 |
| `20241221_160900_EMAIL-03232-eml` | email | [emails/2024-12/20241221_160900_EMAIL-03232.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241221_160900_EMAIL-03232.eml) | 2024-12-21T16:09:00+00:00 |
| `20241222_030900_EMAIL-03234-eml` | email | [emails/2024-12/20241222_030900_EMAIL-03234.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241222_030900_EMAIL-03234.eml) | 2024-12-22T03:09:00+00:00 |
| `20250102_140600_EMAIL-03360-eml` | email | [emails/2025-01/20250102_140600_EMAIL-03360.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250102_140600_EMAIL-03360.eml) | 2025-01-02T14:06:00+00:00 |
| `20250118_173000_EMAIL-03507-eml` | email | [emails/2025-01/20250118_173000_EMAIL-03507.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250118_173000_EMAIL-03507.eml) | 2025-01-18T17:30:00+00:00 |
| `20250121_090100_EMAIL-03529-eml` | email | [emails/2025-01/20250121_090100_EMAIL-03529.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250121_090100_EMAIL-03529.eml) | 2025-01-21T09:01:00+00:00 |
| `20250122_103600_EMAIL-03538-eml` | email | [emails/2025-01/20250122_103600_EMAIL-03538.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250122_103600_EMAIL-03538.eml) | 2025-01-22T10:36:00+00:00 |
| `20250123_150500_EMAIL-03547-eml` | email | [emails/2025-01/20250123_150500_EMAIL-03547.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250123_150500_EMAIL-03547.eml) | 2025-01-23T15:05:00+00:00 |
| `20250125_165200_EMAIL-03562-eml` | email | [emails/2025-01/20250125_165200_EMAIL-03562.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250125_165200_EMAIL-03562.eml) | 2025-01-25T16:52:00+00:00 |
| `20250310_115500_EMAIL-03975-eml` | email | [emails/2025-03/20250310_115500_EMAIL-03975.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250310_115500_EMAIL-03975.eml) | 2025-03-10T11:55:00+00:00 |
| `20250324_151400_EMAIL-04112-eml` | email | [emails/2025-03/20250324_151400_EMAIL-04112.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250324_151400_EMAIL-04112.eml) | 2025-03-24T15:14:00+00:00 |
| `20250328_141500_EMAIL-04142-eml` | email | [emails/2025-03/20250328_141500_EMAIL-04142.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250328_141500_EMAIL-04142.eml) | 2025-03-28T14:15:00+00:00 |
| `20250407_131100_EMAIL-04235-eml` | email | [emails/2025-04/20250407_131100_EMAIL-04235.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250407_131100_EMAIL-04235.eml) | 2025-04-07T13:11:00+00:00 |
| `20250409_131100_EMAIL-04247-eml` | email | [emails/2025-04/20250409_131100_EMAIL-04247.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250409_131100_EMAIL-04247.eml) | 2025-04-09T13:11:00+00:00 |
| `20250514_120100_EMAIL-04514-eml` | email | [emails/2025-05/20250514_120100_EMAIL-04514.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250514_120100_EMAIL-04514.eml) | 2025-05-14T12:01:00+00:00 |
| `20250526_110000_EMAIL-04622-eml` | email | [emails/2025-05/20250526_110000_EMAIL-04622.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250526_110000_EMAIL-04622.eml) | 2025-05-26T11:00:00+00:00 |
| `20250529_162800_EMAIL-04659-eml` | email | [emails/2025-05/20250529_162800_EMAIL-04659.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250529_162800_EMAIL-04659.eml) | 2025-05-29T16:28:00+00:00 |
| `20250610_171600_EMAIL-04744-eml` | email | [emails/2025-06/20250610_171600_EMAIL-04744.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250610_171600_EMAIL-04744.eml) | 2025-06-10T17:16:00+00:00 |
| `20250618_111000_EMAIL-04807-eml` | email | [emails/2025-06/20250618_111000_EMAIL-04807.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250618_111000_EMAIL-04807.eml) | 2025-06-18T11:10:00+00:00 |
| `20250719_171800_EMAIL-05087-eml` | email | [emails/2025-07/20250719_171800_EMAIL-05087.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250719_171800_EMAIL-05087.eml) | 2025-07-19T17:18:00+00:00 |
| `20250907_130000_EMAIL-05557-eml` | email | [emails/2025-09/20250907_130000_EMAIL-05557.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250907_130000_EMAIL-05557.eml) | 2025-09-07T13:00:00+00:00 |
| `20250907_174300_EMAIL-05564-eml` | email | [emails/2025-09/20250907_174300_EMAIL-05564.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250907_174300_EMAIL-05564.eml) | 2025-09-07T17:43:00+00:00 |
| `20250908_083700_EMAIL-05568-eml` | email | [emails/2025-09/20250908_083700_EMAIL-05568.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250908_083700_EMAIL-05568.eml) | 2025-09-08T08:37:00+00:00 |
| `20250914_151300_EMAIL-05623-eml` | email | [emails/2025-09/20250914_151300_EMAIL-05623.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250914_151300_EMAIL-05623.eml) | 2025-09-14T15:13:00+00:00 |
| `20250921_105700_EMAIL-05675-eml` | email | [emails/2025-09/20250921_105700_EMAIL-05675.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250921_105700_EMAIL-05675.eml) | 2025-09-21T10:57:00+00:00 |
| `20250926_152800_EMAIL-05722-eml` | email | [emails/2025-09/20250926_152800_EMAIL-05722.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250926_152800_EMAIL-05722.eml) | 2025-09-26T15:28:00+00:00 |
| `20251015_161300_EMAIL-05888-eml` | email | [emails/2025-10/20251015_161300_EMAIL-05888.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251015_161300_EMAIL-05888.eml) | 2025-10-15T16:13:00+00:00 |
| `20251015_163900_EMAIL-05889-eml` | email | [emails/2025-10/20251015_163900_EMAIL-05889.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251015_163900_EMAIL-05889.eml) | 2025-10-15T16:39:00+00:00 |
| `20251027_110100_EMAIL-05980-eml` | email | [emails/2025-10/20251027_110100_EMAIL-05980.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251027_110100_EMAIL-05980.eml) | 2025-10-27T11:01:00+00:00 |
| `20251028_162100_EMAIL-05992-eml` | email | [emails/2025-10/20251028_162100_EMAIL-05992.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251028_162100_EMAIL-05992.eml) | 2025-10-28T16:21:00+00:00 |
| `20251111_112400_EMAIL-06097-eml` | email | [emails/2025-11/20251111_112400_EMAIL-06097.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251111_112400_EMAIL-06097.eml) | 2025-11-11T11:24:00+00:00 |
| `20251112_170800_EMAIL-06108-eml` | email | [emails/2025-11/20251112_170800_EMAIL-06108.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251112_170800_EMAIL-06108.eml) | 2025-11-12T17:08:00+00:00 |
| `20251115_120600_EMAIL-06125-eml` | email | [emails/2025-11/20251115_120600_EMAIL-06125.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251115_120600_EMAIL-06125.eml) | 2025-11-15T12:06:00+00:00 |
| `20251201_133900_EMAIL-06274-eml` | email | [emails/2025-12/20251201_133900_EMAIL-06274.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251201_133900_EMAIL-06274.eml) | 2025-12-01T13:39:00+00:00 |
| `20251207_151300_EMAIL-06319-eml` | email | [emails/2025-12/20251207_151300_EMAIL-06319.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251207_151300_EMAIL-06319.eml) | 2025-12-07T15:13:00+00:00 |
| `20251209_173300_EMAIL-06341-eml` | email | [emails/2025-12/20251209_173300_EMAIL-06341.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251209_173300_EMAIL-06341.eml) | 2025-12-09T17:33:00+00:00 |
| `20251213_141200_EMAIL-06381-eml` | email | [emails/2025-12/20251213_141200_EMAIL-06381.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251213_141200_EMAIL-06381.eml) | 2025-12-13T14:12:00+00:00 |
| `20251214_011200_EMAIL-06385-eml` | email | [emails/2025-12/20251214_011200_EMAIL-06385.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251214_011200_EMAIL-06385.eml) | 2025-12-14T01:12:00+00:00 |
| `20251216_155800_EMAIL-06415-eml` | email | [emails/2025-12/20251216_155800_EMAIL-06415.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251216_155800_EMAIL-06415.eml) | 2025-12-16T15:58:00+00:00 |
| `20251229_115600_EMAIL-06516-eml` | email | [emails/2025-12/20251229_115600_EMAIL-06516.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251229_115600_EMAIL-06516.eml) | 2025-12-29T11:56:00+00:00 |
| `20251230_105600_EMAIL-06527-eml` | email | [emails/2025-12/20251230_105600_EMAIL-06527.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251230_105600_EMAIL-06527.eml) | 2025-12-30T10:56:00+00:00 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-25T20:52:09+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
