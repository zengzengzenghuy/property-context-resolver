# context.unit.<!-- auto:unit_id -->EH-032<!-- /auto:unit_id -->.md

> Per-unit dossier (one file per Einheit). Holds everything specific to this unit:
> the unit itself, the active lease, the tenant(s), and all unit/tenant-specific operations.
> **Property-wide data lives in `context.property.md`** — see `parent_property_ref` below.

<!-- auto:meta -->
- last_built_at: `2026-04-25T20:52:51+00:00`
- build_hash: `engine-v2`
- engine_version: `0.2.0`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `unit`
- unit_id: `EH-032`
- property_id: `LIE-001`
- parent_property_ref: `context.property.LIE-001.md`
- owner_ref: `EIG-001`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit -->
- unit_id: `EH-032`
- label: WE 32
- haus_id: `HAUS-14`
- floor: 5. OG
- position: mitte
- typ: Wohnung
- area_sqm: 48.0
- rooms: 1.5
- mea_‰: 111
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
- lease_id: `LEASE-MIE-016`
- unit_ref: `EH-032`
- start_date: 2021-08-27 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-016)
- end_date: _(no data in source yet)_
- term_type: `unbefristet`
- cancellation_status: `by_tenant` (notice_date: 2025-12-31, move_out_date: —)
- rent_components: { kaltmiete: 776.0, betriebskosten_vorauszahlung: 125.0, total_warmmiete: 901.00 }
- payment_mode: Überweisung
- iban_payer: DE71120300002328588424 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-016)
- kaution: { amount: 2328.0 }
- usage: `residential`
- subletting: { current_status: `requested` }
- special_agreements: _(no data in source yet)_
<!-- /auto:lease -->

### 2.1 Tenants on this Lease
<!-- auto:tenants -->
| tenant_id | name | role | contact_email | contact_phone | comms_pref | gesamtschuldner |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-016` | Frau Magrit Mitschke | haupt | magrit.mitschke@gmail.com | +49(0)6120 04711 | email | — |
<!-- /auto:tenants -->

---

## 3. Operations (this unit / this tenant)

### 3.1 Open Tickets — Critical (overdue or due ≤7 days)
<!-- auto:tickets.critical -->
| ticket_id | type | title | deadline | status | assignee |
| --- | --- | --- | --- | --- | --- |
| `TKT-2f27e7b4` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-6b0eee6c` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-32286219` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-3da83eab` | wasserschaden | Re: Wasserschaden Bad | — | open | — |
| `TKT-a0c6254e` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-a0e2209a` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-54108361` | schimmel | Re: Schimmel im Schlafzimmer | — | open | — |
| `TKT-55c1c4de` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-9cff2581` | schimmel | Schimmel im Schlafzimmer | — | open | — |
<!-- /auto:tickets.critical -->

### 3.2 Open Tickets — Aggregate
<!-- auto:tickets.aggregate -->
- total_open: `23`
- by_type: { abfluss: `1`, fenster: `7`, schimmel: `4`, schluessel: `6`, wasserschaden: `5` }
- live source: `db.tickets WHERE unit_id=EH-032 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren

<!-- auto:dunning.summary -->[Routine] Mieter MIE-016 ist seit vier Monaten im Verzug; offener Betrag 3.604,00 EUR zzgl. 46,16 EUR Verzugszinsen, letzte Zahlung 2025-12-03 [(bank)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv#TX-01584). Vertraglich geschuldet sind monatlich 901,00 EUR (Kaltmiete 776,00 EUR + NK 125,00 EUR). Verzug nach § 286 BGB festgestellt, Verzugszinsen § 288 I BGB (Basiszins + 5pp); Mahnstufe 1, nächster Schritt: 2. Mahnung nach 14 Tagen.<!-- /auto:dunning.summary -->

#### Per claim
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-016` | — | 1 | 3604.00 EUR | 2025-12-03 | — | — |
- live balance pointer: `db.tenant_balance.tenant_id=MIE-016`
<!-- /auto:dunning -->

### 3.4 Active Reductions / Deferrals (§ 536 BGB)
<!-- auto:reductions -->
- date_raised: 2024-12-27
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-12-21
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
| Mieterwechsel | 2025-12-31 | Kündigung erhalten | Verwaltung | TBD | Übergabe-Termin offen |
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
| `TH-b0ce09` | Ruhestoerung | 2025-12-31 | `MIE-016` | active | 115 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251231_113700_EMAIL-06541.eml) |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `kontoauszug_2024_2025-csv` | bank | [bank/kontoauszug_2024_2025.csv](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv) | 2026-04-25 |
| `20240103_085700_EMAIL-00013-eml` | email | [emails/2024-01/20240103_085700_EMAIL-00013.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240103_085700_EMAIL-00013.eml) | 2024-01-03T08:57:00+00:00 |
| `20240112_113900_EMAIL-00097-eml` | email | [emails/2024-01/20240112_113900_EMAIL-00097.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240112_113900_EMAIL-00097.eml) | 2024-01-12T11:39:00+00:00 |
| `20240113_143900_EMAIL-00109-eml` | email | [emails/2024-01/20240113_143900_EMAIL-00109.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240113_143900_EMAIL-00109.eml) | 2024-01-13T14:39:00+00:00 |
| `20240209_114700_EMAIL-00340-eml` | email | [emails/2024-02/20240209_114700_EMAIL-00340.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240209_114700_EMAIL-00340.eml) | 2024-02-09T11:47:00+00:00 |
| `20240220_155400_EMAIL-00427-eml` | email | [emails/2024-02/20240220_155400_EMAIL-00427.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240220_155400_EMAIL-00427.eml) | 2024-02-20T15:54:00+00:00 |
| `20240304_153400_EMAIL-00548-eml` | email | [emails/2024-03/20240304_153400_EMAIL-00548.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240304_153400_EMAIL-00548.eml) | 2024-03-04T15:34:00+00:00 |
| `20240329_174800_EMAIL-00770-eml` | email | [emails/2024-03/20240329_174800_EMAIL-00770.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240329_174800_EMAIL-00770.eml) | 2024-03-29T17:48:00+00:00 |
| `20240330_091900_EMAIL-00773-eml` | email | [emails/2024-03/20240330_091900_EMAIL-00773.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240330_091900_EMAIL-00773.eml) | 2024-03-30T09:19:00+00:00 |
| `20240414_110700_EMAIL-00937-eml` | email | [emails/2024-04/20240414_110700_EMAIL-00937.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240414_110700_EMAIL-00937.eml) | 2024-04-14T11:07:00+00:00 |
| `20240416_020700_EMAIL-00951-eml` | email | [emails/2024-04/20240416_020700_EMAIL-00951.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240416_020700_EMAIL-00951.eml) | 2024-04-16T02:07:00+00:00 |
| `20240429_100300_EMAIL-01071-eml` | email | [emails/2024-04/20240429_100300_EMAIL-01071.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240429_100300_EMAIL-01071.eml) | 2024-04-29T10:03:00+00:00 |
| `20240529_130000_EMAIL-01341-eml` | email | [emails/2024-05/20240529_130000_EMAIL-01341.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240529_130000_EMAIL-01341.eml) | 2024-05-29T13:00:00+00:00 |
| `20240605_165700_EMAIL-01412-eml` | email | [emails/2024-06/20240605_165700_EMAIL-01412.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240605_165700_EMAIL-01412.eml) | 2024-06-05T16:57:00+00:00 |
| `20240807_083400_EMAIL-01985-eml` | email | [emails/2024-08/20240807_083400_EMAIL-01985.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240807_083400_EMAIL-01985.eml) | 2024-08-07T08:34:00+00:00 |
| `20240814_143000_EMAIL-02038-eml` | email | [emails/2024-08/20240814_143000_EMAIL-02038.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240814_143000_EMAIL-02038.eml) | 2024-08-14T14:30:00+00:00 |
| `20240818_150900_EMAIL-02079-eml` | email | [emails/2024-08/20240818_150900_EMAIL-02079.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240818_150900_EMAIL-02079.eml) | 2024-08-18T15:09:00+00:00 |
| `20240819_170900_EMAIL-02094-eml` | email | [emails/2024-08/20240819_170900_EMAIL-02094.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240819_170900_EMAIL-02094.eml) | 2024-08-19T17:09:00+00:00 |
| `20240904_144500_EMAIL-02243-eml` | email | [emails/2024-09/20240904_144500_EMAIL-02243.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240904_144500_EMAIL-02243.eml) | 2024-09-04T14:45:00+00:00 |
| `20240904_164500_EMAIL-02246-eml` | email | [emails/2024-09/20240904_164500_EMAIL-02246.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240904_164500_EMAIL-02246.eml) | 2024-09-04T16:45:00+00:00 |
| `20240906_133300_EMAIL-02262-eml` | email | [emails/2024-09/20240906_133300_EMAIL-02262.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240906_133300_EMAIL-02262.eml) | 2024-09-06T13:33:00+00:00 |
| `20240907_063300_EMAIL-02270-eml` | email | [emails/2024-09/20240907_063300_EMAIL-02270.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240907_063300_EMAIL-02270.eml) | 2024-09-07T06:33:00+00:00 |
| `20240908_104500_EMAIL-02288-eml` | email | [emails/2024-09/20240908_104500_EMAIL-02288.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240908_104500_EMAIL-02288.eml) | 2024-09-08T10:45:00+00:00 |
| `20240910_084500_EMAIL-02308-eml` | email | [emails/2024-09/20240910_084500_EMAIL-02308.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240910_084500_EMAIL-02308.eml) | 2024-09-10T08:45:00+00:00 |
| `20240921_124400_EMAIL-02398-eml` | email | [emails/2024-09/20240921_124400_EMAIL-02398.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240921_124400_EMAIL-02398.eml) | 2024-09-21T12:44:00+00:00 |
| `20240928_131900_EMAIL-02470-eml` | email | [emails/2024-09/20240928_131900_EMAIL-02470.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240928_131900_EMAIL-02470.eml) | 2024-09-28T13:19:00+00:00 |
| `20240930_061900_EMAIL-02480-eml` | email | [emails/2024-09/20240930_061900_EMAIL-02480.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240930_061900_EMAIL-02480.eml) | 2024-09-30T06:19:00+00:00 |
| `20241016_135900_EMAIL-02628-eml` | email | [emails/2024-10/20241016_135900_EMAIL-02628.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241016_135900_EMAIL-02628.eml) | 2024-10-16T13:59:00+00:00 |
| `20241018_035900_EMAIL-02642-eml` | email | [emails/2024-10/20241018_035900_EMAIL-02642.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241018_035900_EMAIL-02642.eml) | 2024-10-18T03:59:00+00:00 |
| `20241027_035900_EMAIL-02732-eml` | email | [emails/2024-10/20241027_035900_EMAIL-02732.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241027_035900_EMAIL-02732.eml) | 2024-10-27T03:59:00+00:00 |
| `20241102_092300_EMAIL-02793-eml` | email | [emails/2024-11/20241102_092300_EMAIL-02793.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241102_092300_EMAIL-02793.eml) | 2024-11-02T09:23:00+00:00 |
| `20241221_113100_EMAIL-03228-eml` | email | [emails/2024-12/20241221_113100_EMAIL-03228.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241221_113100_EMAIL-03228.eml) | 2024-12-21T11:31:00+00:00 |
| `20241222_013100_EMAIL-03233-eml` | email | [emails/2024-12/20241222_013100_EMAIL-03233.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241222_013100_EMAIL-03233.eml) | 2024-12-22T01:31:00+00:00 |
| `20241227_135900_EMAIL-03290-eml` | email | [emails/2024-12/20241227_135900_EMAIL-03290.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241227_135900_EMAIL-03290.eml) | 2024-12-27T13:59:00+00:00 |
| `20241227_154000_EMAIL-03294-eml` | email | [emails/2024-12/20241227_154000_EMAIL-03294.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241227_154000_EMAIL-03294.eml) | 2024-12-27T15:40:00+00:00 |
| `20250127_171700_EMAIL-03577-eml` | email | [emails/2025-01/20250127_171700_EMAIL-03577.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250127_171700_EMAIL-03577.eml) | 2025-01-27T17:17:00+00:00 |
| `20250127_191700_EMAIL-03579-eml` | email | [emails/2025-01/20250127_191700_EMAIL-03579.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250127_191700_EMAIL-03579.eml) | 2025-01-27T19:17:00+00:00 |
| `20250129_140000_EMAIL-03595-eml` | email | [emails/2025-01/20250129_140000_EMAIL-03595.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250129_140000_EMAIL-03595.eml) | 2025-01-29T14:00:00+00:00 |
| `20250130_090000_EMAIL-03601-eml` | email | [emails/2025-01/20250130_090000_EMAIL-03601.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250130_090000_EMAIL-03601.eml) | 2025-01-30T09:00:00+00:00 |
| `20250203_090000_EMAIL-03635-eml` | email | [emails/2025-02/20250203_090000_EMAIL-03635.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250203_090000_EMAIL-03635.eml) | 2025-02-03T09:00:00+00:00 |
| `20250225_091400_EMAIL-03844-eml` | email | [emails/2025-02/20250225_091400_EMAIL-03844.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250225_091400_EMAIL-03844.eml) | 2025-02-25T09:14:00+00:00 |
| `20250303_143100_EMAIL-03906-eml` | email | [emails/2025-03/20250303_143100_EMAIL-03906.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250303_143100_EMAIL-03906.eml) | 2025-03-03T14:31:00+00:00 |
| `20250304_123100_EMAIL-03916-eml` | email | [emails/2025-03/20250304_123100_EMAIL-03916.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250304_123100_EMAIL-03916.eml) | 2025-03-04T12:31:00+00:00 |
| `20250307_231400_EMAIL-03949-eml` | email | [emails/2025-03/20250307_231400_EMAIL-03949.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250307_231400_EMAIL-03949.eml) | 2025-03-07T23:14:00+00:00 |
| `20250323_113500_EMAIL-04103-eml` | email | [emails/2025-03/20250323_113500_EMAIL-04103.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250323_113500_EMAIL-04103.eml) | 2025-03-23T11:35:00+00:00 |
| `20250326_100300_EMAIL-04124-eml` | email | [emails/2025-03/20250326_100300_EMAIL-04124.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250326_100300_EMAIL-04124.eml) | 2025-03-26T10:03:00+00:00 |
| `20250327_230300_EMAIL-04138-eml` | email | [emails/2025-03/20250327_230300_EMAIL-04138.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250327_230300_EMAIL-04138.eml) | 2025-03-27T23:03:00+00:00 |
| `20250406_103500_EMAIL-04217-eml` | email | [emails/2025-04/20250406_103500_EMAIL-04217.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250406_103500_EMAIL-04217.eml) | 2025-04-06T10:35:00+00:00 |
| `20250410_114100_EMAIL-04253-eml` | email | [emails/2025-04/20250410_114100_EMAIL-04253.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250410_114100_EMAIL-04253.eml) | 2025-04-10T11:41:00+00:00 |
| `20250418_113500_EMAIL-04319-eml` | email | [emails/2025-04/20250418_113500_EMAIL-04319.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250418_113500_EMAIL-04319.eml) | 2025-04-18T11:35:00+00:00 |
| `20250510_101600_EMAIL-04470-eml` | email | [emails/2025-05/20250510_101600_EMAIL-04470.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250510_101600_EMAIL-04470.eml) | 2025-05-10T10:16:00+00:00 |
| `20250517_140400_EMAIL-04540-eml` | email | [emails/2025-05/20250517_140400_EMAIL-04540.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250517_140400_EMAIL-04540.eml) | 2025-05-17T14:04:00+00:00 |
| `20250522_161300_EMAIL-04591-eml` | email | [emails/2025-05/20250522_161300_EMAIL-04591.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250522_161300_EMAIL-04591.eml) | 2025-05-22T16:13:00+00:00 |
| `20250606_154900_EMAIL-04712-eml` | email | [emails/2025-06/20250606_154900_EMAIL-04712.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250606_154900_EMAIL-04712.eml) | 2025-06-06T15:49:00+00:00 |
| `20250608_054900_EMAIL-04720-eml` | email | [emails/2025-06/20250608_054900_EMAIL-04720.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250608_054900_EMAIL-04720.eml) | 2025-06-08T05:49:00+00:00 |
| `20250613_114400_EMAIL-04764-eml` | email | [emails/2025-06/20250613_114400_EMAIL-04764.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250613_114400_EMAIL-04764.eml) | 2025-06-13T11:44:00+00:00 |
| `20250621_164800_EMAIL-04839-eml` | email | [emails/2025-06/20250621_164800_EMAIL-04839.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250621_164800_EMAIL-04839.eml) | 2025-06-21T16:48:00+00:00 |
| `20250710_103000_EMAIL-04991-eml` | email | [emails/2025-07/20250710_103000_EMAIL-04991.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250710_103000_EMAIL-04991.eml) | 2025-07-10T10:30:00+00:00 |
| `20250723_104600_EMAIL-05119-eml` | email | [emails/2025-07/20250723_104600_EMAIL-05119.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250723_104600_EMAIL-05119.eml) | 2025-07-23T10:46:00+00:00 |
| `20250829_134200_EMAIL-05442-eml` | email | [emails/2025-08/20250829_134200_EMAIL-05442.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250829_134200_EMAIL-05442.eml) | 2025-08-29T13:42:00+00:00 |
| `20250901_140200_EMAIL-05479-eml` | email | [emails/2025-09/20250901_140200_EMAIL-05479.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250901_140200_EMAIL-05479.eml) | 2025-09-01T14:02:00+00:00 |
| `20250901_162000_EMAIL-05483-eml` | email | [emails/2025-09/20250901_162000_EMAIL-05483.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250901_162000_EMAIL-05483.eml) | 2025-09-01T16:20:00+00:00 |
| `20250901_232000_EMAIL-05490-eml` | email | [emails/2025-09/20250901_232000_EMAIL-05490.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250901_232000_EMAIL-05490.eml) | 2025-09-01T23:20:00+00:00 |
| `20250920_152000_EMAIL-05670-eml` | email | [emails/2025-09/20250920_152000_EMAIL-05670.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250920_152000_EMAIL-05670.eml) | 2025-09-20T15:20:00+00:00 |
| `20250920_160300_EMAIL-05672-eml` | email | [emails/2025-09/20250920_160300_EMAIL-05672.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250920_160300_EMAIL-05672.eml) | 2025-09-20T16:03:00+00:00 |
| `20251003_170300_EMAIL-05771-eml` | email | [emails/2025-10/20251003_170300_EMAIL-05771.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251003_170300_EMAIL-05771.eml) | 2025-10-03T17:03:00+00:00 |
| `20251003_170500_EMAIL-05772-eml` | email | [emails/2025-10/20251003_170500_EMAIL-05772.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251003_170500_EMAIL-05772.eml) | 2025-10-03T17:05:00+00:00 |
| `20251005_000300_EMAIL-05782-eml` | email | [emails/2025-10/20251005_000300_EMAIL-05782.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251005_000300_EMAIL-05782.eml) | 2025-10-05T00:03:00+00:00 |
| `20251005_010500_EMAIL-05783-eml` | email | [emails/2025-10/20251005_010500_EMAIL-05783.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251005_010500_EMAIL-05783.eml) | 2025-10-05T01:05:00+00:00 |
| `20251007_010500_EMAIL-05802-eml` | email | [emails/2025-10/20251007_010500_EMAIL-05802.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251007_010500_EMAIL-05802.eml) | 2025-10-07T01:05:00+00:00 |
| `20251025_115500_EMAIL-05964-eml` | email | [emails/2025-10/20251025_115500_EMAIL-05964.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251025_115500_EMAIL-05964.eml) | 2025-10-25T11:55:00+00:00 |
| `20251027_045500_EMAIL-05978-eml` | email | [emails/2025-10/20251027_045500_EMAIL-05978.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251027_045500_EMAIL-05978.eml) | 2025-10-27T04:55:00+00:00 |
| `20251030_161800_EMAIL-06004-eml` | email | [emails/2025-10/20251030_161800_EMAIL-06004.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251030_161800_EMAIL-06004.eml) | 2025-10-30T16:18:00+00:00 |
| `20251116_174000_EMAIL-06142-eml` | email | [emails/2025-11/20251116_174000_EMAIL-06142.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251116_174000_EMAIL-06142.eml) | 2025-11-16T17:40:00+00:00 |
| `20251208_145800_EMAIL-06326-eml` | email | [emails/2025-12/20251208_145800_EMAIL-06326.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251208_145800_EMAIL-06326.eml) | 2025-12-08T14:58:00+00:00 |
| `20251216_111100_EMAIL-06411-eml` | email | [emails/2025-12/20251216_111100_EMAIL-06411.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251216_111100_EMAIL-06411.eml) | 2025-12-16T11:11:00+00:00 |
| `20251221_135600_EMAIL-06459-eml` | email | [emails/2025-12/20251221_135600_EMAIL-06459.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251221_135600_EMAIL-06459.eml) | 2025-12-21T13:56:00+00:00 |
| `20251229_173700_EMAIL-06520-eml` | email | [emails/2025-12/20251229_173700_EMAIL-06520.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251229_173700_EMAIL-06520.eml) | 2025-12-29T17:37:00+00:00 |
| `20251231_113700_EMAIL-06541-eml` | email | [emails/2025-12/20251231_113700_EMAIL-06541.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251231_113700_EMAIL-06541.eml) | 2025-12-31 |
| `20251231_163500_EMAIL-06543-eml` | email | [emails/2025-12/20251231_163500_EMAIL-06543.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251231_163500_EMAIL-06543.eml) | 2025-12-31T16:35:00+00:00 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-25T20:52:09+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
