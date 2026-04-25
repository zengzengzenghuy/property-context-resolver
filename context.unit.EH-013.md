# context.unit.<!-- auto:unit_id -->EH-013<!-- /auto:unit_id -->.md

> Per-unit dossier (one file per Einheit). Holds everything specific to this unit:
> the unit itself, the active lease, the tenant(s), and all unit/tenant-specific operations.
> **Property-wide data lives in `context.property.md`** — see `parent_property_ref` below.

<!-- auto:meta -->
- last_built_at: `2026-04-25T20:52:28+00:00`
- build_hash: `engine-v2`
- engine_version: `0.2.0`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `unit`
- unit_id: `EH-013`
- property_id: `LIE-001`
- parent_property_ref: `context.property.LIE-001.md`
- owner_ref: `EIG-024`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit -->
- unit_id: `EH-013`
- label: WE 13
- haus_id: `HAUS-12`
- floor: 5. OG
- position: links
- typ: Wohnung
- area_sqm: 84.0
- rooms: 3.0
- mea_‰: 195
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
- lease_id: `LEASE-MIE-005`
- unit_ref: `EH-013`
- start_date: 2022-07-20 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-005)
- end_date: _(no data in source yet)_
- term_type: `unbefristet`
- cancellation_status: `by_tenant` (notice_date: 2025-09-13, move_out_date: —)
- rent_components: { kaltmiete: 1392.0, betriebskosten_vorauszahlung: 261.0, total_warmmiete: 1653.00 }
- payment_mode: Überweisung
- iban_payer: DE76370400445168087603 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-005)
- kaution: { amount: 4176.0 }
- usage: `residential`
- subletting: { current_status: `requested` }
- special_agreements: _(no data in source yet)_
<!-- /auto:lease -->

### 2.1 Tenants on this Lease
<!-- auto:tenants -->
| tenant_id | name | role | contact_email | contact_phone | comms_pref | gesamtschuldner |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-005` | Frau Steffi Riehl | haupt | steffi.riehl@posteo.de | +49(0)9134316117 | email | — |
<!-- /auto:tenants -->

---

## 3. Operations (this unit / this tenant)

### 3.1 Open Tickets — Critical (overdue or due ≤7 days)
<!-- auto:tickets.critical -->
| ticket_id | type | title | deadline | status | assignee |
| --- | --- | --- | --- | --- | --- |
| `TKT-cc83411e` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-24645fdc` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-87d94c98` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-fbc254e7` | schimmel | Re: Schimmel im Schlafzimmer | — | open | — |
| `TKT-e144831c` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-c7237093` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-94c0d110` | wasserschaden | Wasserschaden Bad | — | open | — |
<!-- /auto:tickets.critical -->

### 3.2 Open Tickets — Aggregate
<!-- auto:tickets.aggregate -->
- total_open: `18`
- by_type: { abfluss: `1`, fenster: `7`, schimmel: `5`, schluessel: `3`, wasserschaden: `2` }
- live source: `db.tickets WHERE unit_id=EH-013 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren

<!-- auto:dunning.summary -->[Routine] Mieter MIE-005 ist seit vier Monaten im Verzug; offener Betrag 6.612,00 EUR zzgl. 84,69 EUR Verzugszinsen, letzte Zahlung 2025-12-02 [(bank)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv#TX-01564). Vertraglich geschuldet sind monatlich 1.653,00 EUR (Kaltmiete 1.392,00 EUR + NK 261,00 EUR) [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-005). Verzug nach § 286 BGB, Verzugszinsen § 288 I BGB; Mahnstufe 1 aktiv, zweite Mahnung erforderlich.<!-- /auto:dunning.summary -->

#### Per claim
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-005` | — | 1 | 6612.00 EUR | 2025-12-02 | — | — |
- live balance pointer: `db.tenant_balance.tenant_id=MIE-005`
<!-- /auto:dunning -->

### 3.4 Active Reductions / Deferrals (§ 536 BGB)
<!-- auto:reductions -->
- date_raised: 2024-03-20
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-04-23
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-02-05
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-09-09
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-12-12
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
| `TH-ac58ac` | Verkaufsabsicht WE 13 | 2025-12-09 | `EH-013` | active | 8 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251209_114900_EMAIL-06337.eml) |
| `TH-46701c` | Mieterwechsel in WE 13 | 2025-12-05 | `EH-013` | active | 6 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251205_095900_EMAIL-06304.eml) |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `kontoauszug_2024_2025-csv` | bank | [bank/kontoauszug_2024_2025.csv](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv) | 2026-04-25 |
| `20240110_172300_EMAIL-00084-eml` | email | [emails/2024-01/20240110_172300_EMAIL-00084.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240110_172300_EMAIL-00084.eml) | 2024-01-10T17:23:00+00:00 |
| `20240117_113200_EMAIL-00136-eml` | email | [emails/2024-01/20240117_113200_EMAIL-00136.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240117_113200_EMAIL-00136.eml) | 2024-01-17T11:32:00+00:00 |
| `20240124_111400_EMAIL-00189-eml` | email | [emails/2024-01/20240124_111400_EMAIL-00189.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240124_111400_EMAIL-00189.eml) | 2024-01-24T11:14:00+00:00 |
| `20240131_152500_EMAIL-00252-eml` | email | [emails/2024-01/20240131_152500_EMAIL-00252.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240131_152500_EMAIL-00252.eml) | 2024-01-31T15:25:00+00:00 |
| `20240202_122500_EMAIL-00274-eml` | email | [emails/2024-02/20240202_122500_EMAIL-00274.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240202_122500_EMAIL-00274.eml) | 2024-02-02T12:25:00+00:00 |
| `20240202_170100_EMAIL-00277-eml` | email | [emails/2024-02/20240202_170100_EMAIL-00277.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240202_170100_EMAIL-00277.eml) | 2024-02-02T17:01:00+00:00 |
| `20240203_210100_EMAIL-00291-eml` | email | [emails/2024-02/20240203_210100_EMAIL-00291.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240203_210100_EMAIL-00291.eml) | 2024-02-03T21:01:00+00:00 |
| `20240213_135600_EMAIL-00373-eml` | email | [emails/2024-02/20240213_135600_EMAIL-00373.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240213_135600_EMAIL-00373.eml) | 2024-02-13T13:56:00+00:00 |
| `20240302_151800_EMAIL-00532-eml` | email | [emails/2024-03/20240302_151800_EMAIL-00532.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240302_151800_EMAIL-00532.eml) | 2024-03-02T15:18:00+00:00 |
| `20240320_175100_EMAIL-00694-eml` | email | [emails/2024-03/20240320_175100_EMAIL-00694.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240320_175100_EMAIL-00694.eml) | 2024-03-20T17:51:00+00:00 |
| `20240322_091200_EMAIL-00704-eml` | email | [emails/2024-03/20240322_091200_EMAIL-00704.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240322_091200_EMAIL-00704.eml) | 2024-03-22T09:12:00+00:00 |
| `20240404_112000_EMAIL-00827-eml` | email | [emails/2024-04/20240404_112000_EMAIL-00827.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240404_112000_EMAIL-00827.eml) | 2024-04-04T11:20:00+00:00 |
| `20240423_083500_EMAIL-01020-eml` | email | [emails/2024-04/20240423_083500_EMAIL-01020.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240423_083500_EMAIL-01020.eml) | 2024-04-23T08:35:00+00:00 |
| `20240429_092800_EMAIL-01070-eml` | email | [emails/2024-04/20240429_092800_EMAIL-01070.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240429_092800_EMAIL-01070.eml) | 2024-04-29T09:28:00+00:00 |
| `20240507_104100_EMAIL-01143-eml` | email | [emails/2024-05/20240507_104100_EMAIL-01143.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240507_104100_EMAIL-01143.eml) | 2024-05-07T10:41:00+00:00 |
| `20240515_103500_EMAIL-01226-eml` | email | [emails/2024-05/20240515_103500_EMAIL-01226.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240515_103500_EMAIL-01226.eml) | 2024-05-15T10:35:00+00:00 |
| `20240521_124000_EMAIL-01272-eml` | email | [emails/2024-05/20240521_124000_EMAIL-01272.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240521_124000_EMAIL-01272.eml) | 2024-05-21T12:40:00+00:00 |
| `20240610_144000_EMAIL-01456-eml` | email | [emails/2024-06/20240610_144000_EMAIL-01456.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240610_144000_EMAIL-01456.eml) | 2024-06-10T14:40:00+00:00 |
| `20240612_074000_EMAIL-01472-eml` | email | [emails/2024-06/20240612_074000_EMAIL-01472.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240612_074000_EMAIL-01472.eml) | 2024-06-12T07:40:00+00:00 |
| `20240626_183400_EMAIL-01595-eml` | email | [emails/2024-06/20240626_183400_EMAIL-01595.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240626_183400_EMAIL-01595.eml) | 2024-06-26T18:34:00+00:00 |
| `20240708_165500_EMAIL-01700-eml` | email | [emails/2024-07/20240708_165500_EMAIL-01700.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240708_165500_EMAIL-01700.eml) | 2024-07-08T16:55:00+00:00 |
| `20240714_164800_EMAIL-01765-eml` | email | [emails/2024-07/20240714_164800_EMAIL-01765.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240714_164800_EMAIL-01765.eml) | 2024-07-14T16:48:00+00:00 |
| `20240716_113200_EMAIL-01777-eml` | email | [emails/2024-07/20240716_113200_EMAIL-01777.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240716_113200_EMAIL-01777.eml) | 2024-07-16T11:32:00+00:00 |
| `20240725_175900_EMAIL-01862-eml` | email | [emails/2024-07/20240725_175900_EMAIL-01862.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240725_175900_EMAIL-01862.eml) | 2024-07-25T17:59:00+00:00 |
| `20240726_120100_EMAIL-01869-eml` | email | [emails/2024-07/20240726_120100_EMAIL-01869.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240726_120100_EMAIL-01869.eml) | 2024-07-26T12:01:00+00:00 |
| `20240727_140100_EMAIL-01881-eml` | email | [emails/2024-07/20240727_140100_EMAIL-01881.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240727_140100_EMAIL-01881.eml) | 2024-07-27T14:01:00+00:00 |
| `20240802_140100_EMAIL-01933-eml` | email | [emails/2024-08/20240802_140100_EMAIL-01933.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240802_140100_EMAIL-01933.eml) | 2024-08-02T14:01:00+00:00 |
| `20240818_144000_EMAIL-02077-eml` | email | [emails/2024-08/20240818_144000_EMAIL-02077.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240818_144000_EMAIL-02077.eml) | 2024-08-18T14:40:00+00:00 |
| `20240906_150000_EMAIL-02265-eml` | email | [emails/2024-09/20240906_150000_EMAIL-02265.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240906_150000_EMAIL-02265.eml) | 2024-09-06T15:00:00+00:00 |
| `20240912_150900_EMAIL-02331-eml` | email | [emails/2024-09/20240912_150900_EMAIL-02331.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240912_150900_EMAIL-02331.eml) | 2024-09-12T15:09:00+00:00 |
| `20240918_101600_EMAIL-02375-eml` | email | [emails/2024-09/20240918_101600_EMAIL-02375.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240918_101600_EMAIL-02375.eml) | 2024-09-18T10:16:00+00:00 |
| `20240918_141600_EMAIL-02378-eml` | email | [emails/2024-09/20240918_141600_EMAIL-02378.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240918_141600_EMAIL-02378.eml) | 2024-09-18T14:16:00+00:00 |
| `20240927_175900_EMAIL-02466-eml` | email | [emails/2024-09/20240927_175900_EMAIL-02466.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240927_175900_EMAIL-02466.eml) | 2024-09-27T17:59:00+00:00 |
| `20240929_025900_EMAIL-02477-eml` | email | [emails/2024-09/20240929_025900_EMAIL-02477.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240929_025900_EMAIL-02477.eml) | 2024-09-29T02:59:00+00:00 |
| `20241102_163100_EMAIL-02800-eml` | email | [emails/2024-11/20241102_163100_EMAIL-02800.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241102_163100_EMAIL-02800.eml) | 2024-11-02T16:31:00+00:00 |
| `20241104_153800_EMAIL-02816-eml` | email | [emails/2024-11/20241104_153800_EMAIL-02816.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241104_153800_EMAIL-02816.eml) | 2024-11-04T15:38:00+00:00 |
| `20241105_113800_EMAIL-02822-eml` | email | [emails/2024-11/20241105_113800_EMAIL-02822.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241105_113800_EMAIL-02822.eml) | 2024-11-05T11:38:00+00:00 |
| `20241125_145400_EMAIL-03004-eml` | email | [emails/2024-11/20241125_145400_EMAIL-03004.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241125_145400_EMAIL-03004.eml) | 2024-11-25T14:54:00+00:00 |
| `20241211_130300_EMAIL-03147-eml` | email | [emails/2024-12/20241211_130300_EMAIL-03147.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241211_130300_EMAIL-03147.eml) | 2024-12-11T13:03:00+00:00 |
| `20241213_060300_EMAIL-03162-eml` | email | [emails/2024-12/20241213_060300_EMAIL-03162.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241213_060300_EMAIL-03162.eml) | 2024-12-13T06:03:00+00:00 |
| `20241227_082100_EMAIL-03287-eml` | email | [emails/2024-12/20241227_082100_EMAIL-03287.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241227_082100_EMAIL-03287.eml) | 2024-12-27T08:21:00+00:00 |
| `20250102_100800_EMAIL-03354-eml` | email | [emails/2025-01/20250102_100800_EMAIL-03354.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250102_100800_EMAIL-03354.eml) | 2025-01-02T10:08:00+00:00 |
| `20250116_150800_EMAIL-03490-eml` | email | [emails/2025-01/20250116_150800_EMAIL-03490.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250116_150800_EMAIL-03490.eml) | 2025-01-16T15:08:00+00:00 |
| `20250118_182800_EMAIL-03508-eml` | email | [emails/2025-01/20250118_182800_EMAIL-03508.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250118_182800_EMAIL-03508.eml) | 2025-01-18T18:28:00+00:00 |
| `20250119_140800_EMAIL-03519-eml` | email | [emails/2025-01/20250119_140800_EMAIL-03519.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250119_140800_EMAIL-03519.eml) | 2025-01-19T14:08:00+00:00 |
| `20250205_185700_EMAIL-03659-eml` | email | [emails/2025-02/20250205_185700_EMAIL-03659.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250205_185700_EMAIL-03659.eml) | 2025-02-05T18:57:00+00:00 |
| `20250209_140100_EMAIL-03681-eml` | email | [emails/2025-02/20250209_140100_EMAIL-03681.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250209_140100_EMAIL-03681.eml) | 2025-02-09T14:01:00+00:00 |
| `20250210_210100_EMAIL-03691-eml` | email | [emails/2025-02/20250210_210100_EMAIL-03691.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250210_210100_EMAIL-03691.eml) | 2025-02-10T21:01:00+00:00 |
| `20250302_094800_EMAIL-03898-eml` | email | [emails/2025-03/20250302_094800_EMAIL-03898.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250302_094800_EMAIL-03898.eml) | 2025-03-02T09:48:00+00:00 |
| `20250302_234800_EMAIL-03904-eml` | email | [emails/2025-03/20250302_234800_EMAIL-03904.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250302_234800_EMAIL-03904.eml) | 2025-03-02T23:48:00+00:00 |
| `20250309_144200_EMAIL-03966-eml` | email | [emails/2025-03/20250309_144200_EMAIL-03966.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250309_144200_EMAIL-03966.eml) | 2025-03-09T14:42:00+00:00 |
| `20250314_142500_EMAIL-04013-eml` | email | [emails/2025-03/20250314_142500_EMAIL-04013.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250314_142500_EMAIL-04013.eml) | 2025-03-14T14:25:00+00:00 |
| `20250315_052500_EMAIL-04018-eml` | email | [emails/2025-03/20250315_052500_EMAIL-04018.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250315_052500_EMAIL-04018.eml) | 2025-03-15T05:25:00+00:00 |
| `20250402_144500_EMAIL-04189-eml` | email | [emails/2025-04/20250402_144500_EMAIL-04189.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250402_144500_EMAIL-04189.eml) | 2025-04-02T14:45:00+00:00 |
| `20250405_180700_EMAIL-04213-eml` | email | [emails/2025-04/20250405_180700_EMAIL-04213.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250405_180700_EMAIL-04213.eml) | 2025-04-05T18:07:00+00:00 |
| `20250513_112300_EMAIL-04501-eml` | email | [emails/2025-05/20250513_112300_EMAIL-04501.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250513_112300_EMAIL-04501.eml) | 2025-05-13T11:23:00+00:00 |
| `20250514_070400_EMAIL-04509-eml` | email | [emails/2025-05/20250514_070400_EMAIL-04509.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250514_070400_EMAIL-04509.eml) | 2025-05-14T07:04:00+00:00 |
| `20250519_133800_EMAIL-04562-eml` | email | [emails/2025-05/20250519_133800_EMAIL-04562.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250519_133800_EMAIL-04562.eml) | 2025-05-19T13:38:00+00:00 |
| `20250520_093800_EMAIL-04569-eml` | email | [emails/2025-05/20250520_093800_EMAIL-04569.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250520_093800_EMAIL-04569.eml) | 2025-05-20T09:38:00+00:00 |
| `20250523_142600_EMAIL-04600-eml` | email | [emails/2025-05/20250523_142600_EMAIL-04600.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250523_142600_EMAIL-04600.eml) | 2025-05-23T14:26:00+00:00 |
| `20250524_155300_EMAIL-04613-eml` | email | [emails/2025-05/20250524_155300_EMAIL-04613.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250524_155300_EMAIL-04613.eml) | 2025-05-24T15:53:00+00:00 |
| `20250525_155300_EMAIL-04618-eml` | email | [emails/2025-05/20250525_155300_EMAIL-04618.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250525_155300_EMAIL-04618.eml) | 2025-05-25T15:53:00+00:00 |
| `20250526_153500_EMAIL-04629-eml` | email | [emails/2025-05/20250526_153500_EMAIL-04629.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250526_153500_EMAIL-04629.eml) | 2025-05-26T15:35:00+00:00 |
| `20250625_135300_EMAIL-04871-eml` | email | [emails/2025-06/20250625_135300_EMAIL-04871.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250625_135300_EMAIL-04871.eml) | 2025-06-25T13:53:00+00:00 |
| `20250708_115100_EMAIL-04972-eml` | email | [emails/2025-07/20250708_115100_EMAIL-04972.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250708_115100_EMAIL-04972.eml) | 2025-07-08T11:51:00+00:00 |
| `20250719_105800_EMAIL-05082-eml` | email | [emails/2025-07/20250719_105800_EMAIL-05082.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250719_105800_EMAIL-05082.eml) | 2025-07-19T10:58:00+00:00 |
| `20250804_090200_EMAIL-05197-eml` | email | [emails/2025-08/20250804_090200_EMAIL-05197.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250804_090200_EMAIL-05197.eml) | 2025-08-04T09:02:00+00:00 |
| `20250806_090200_EMAIL-05207-eml` | email | [emails/2025-08/20250806_090200_EMAIL-05207.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250806_090200_EMAIL-05207.eml) | 2025-08-06T09:02:00+00:00 |
| `20250806_095200_EMAIL-05208-eml` | email | [emails/2025-08/20250806_095200_EMAIL-05208.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250806_095200_EMAIL-05208.eml) | 2025-08-06T09:52:00+00:00 |
| `20250818_122900_EMAIL-05339-eml` | email | [emails/2025-08/20250818_122900_EMAIL-05339.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250818_122900_EMAIL-05339.eml) | 2025-08-18T12:29:00+00:00 |
| `20250823_114200_EMAIL-05383-eml` | email | [emails/2025-08/20250823_114200_EMAIL-05383.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250823_114200_EMAIL-05383.eml) | 2025-08-23T11:42:00+00:00 |
| `20250909_142600_EMAIL-05582-eml` | email | [emails/2025-09/20250909_142600_EMAIL-05582.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250909_142600_EMAIL-05582.eml) | 2025-09-09T14:26:00+00:00 |
| `20250910_092100_EMAIL-05587-eml` | email | [emails/2025-09/20250910_092100_EMAIL-05587.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250910_092100_EMAIL-05587.eml) | 2025-09-10T09:21:00+00:00 |
| `20250913_103900_EMAIL-05613-eml` | email | [emails/2025-09/20250913_103900_EMAIL-05613.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250913_103900_EMAIL-05613.eml) | 2025-09-13T10:39:00+00:00 |
| `20250913_170200_EMAIL-05616-eml` | email | [emails/2025-09/20250913_170200_EMAIL-05616.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250913_170200_EMAIL-05616.eml) | 2025-09-13T17:02:00+00:00 |
| `20251018_113400_EMAIL-05905-eml` | email | [emails/2025-10/20251018_113400_EMAIL-05905.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251018_113400_EMAIL-05905.eml) | 2025-10-18T11:34:00+00:00 |
| `20251021_154900_EMAIL-05928-eml` | email | [emails/2025-10/20251021_154900_EMAIL-05928.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251021_154900_EMAIL-05928.eml) | 2025-10-21T15:49:00+00:00 |
| `20251205_095900_EMAIL-06304-eml` | email | [emails/2025-12/20251205_095900_EMAIL-06304.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251205_095900_EMAIL-06304.eml) | 2025-12-05 |
| `20251209_114900_EMAIL-06337-eml` | email | [emails/2025-12/20251209_114900_EMAIL-06337.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251209_114900_EMAIL-06337.eml) | 2025-12-09 |
| `20251212_165200_EMAIL-06371-eml` | email | [emails/2025-12/20251212_165200_EMAIL-06371.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251212_165200_EMAIL-06371.eml) | 2025-12-12T16:52:00+00:00 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-25T20:52:09+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
