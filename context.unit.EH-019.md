# context.unit.<!-- auto:unit_id -->EH-019<!-- /auto:unit_id -->.md

> Per-unit dossier (one file per Einheit). Holds everything specific to this unit:
> the unit itself, the active lease, the tenant(s), and all unit/tenant-specific operations.
> **Property-wide data lives in `context.property.md`** — see `parent_property_ref` below.

<!-- auto:meta -->
- last_built_at: `2026-04-25T20:52:33+00:00`
- build_hash: `engine-v2`
- engine_version: `0.2.0`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `unit`
- unit_id: `EH-019`
- property_id: `LIE-001`
- parent_property_ref: `context.property.LIE-001.md`
- owner_ref: `EIG-014`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit -->
- unit_id: `EH-019`
- label: WE 19
- haus_id: `HAUS-14`
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
- lease_id: `LEASE-MIE-025`
- unit_ref: `EH-019`
- start_date: 2022-07-13 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-025)
- end_date: _(no data in source yet)_
- term_type: `unbefristet`
- cancellation_status: `by_tenant` (notice_date: 2025-10-25, move_out_date: —)
- rent_components: { kaltmiete: 1031.0, betriebskosten_vorauszahlung: 175.0, total_warmmiete: 1206.00 }
- payment_mode: Überweisung
- iban_payer: DE29120300005766156545 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-025)
- kaution: { amount: 3093.0 }
- usage: `residential`
- subletting: { current_status: `requested` }
- special_agreements: _(no data in source yet)_
<!-- /auto:lease -->

### 2.1 Tenants on this Lease
<!-- auto:tenants -->
| tenant_id | name | role | contact_email | contact_phone | comms_pref | gesamtschuldner |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-025` | Frau Jasmin Trub | haupt | jasmin.trub@outlook.com | 01159 212499 | email | — |
<!-- /auto:tenants -->

---

## 3. Operations (this unit / this tenant)

### 3.1 Open Tickets — Critical (overdue or due ≤7 days)
<!-- auto:tickets.critical -->
| ticket_id | type | title | deadline | status | assignee |
| --- | --- | --- | --- | --- | --- |
| `TKT-29878910` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-7aa10874` | wasserschaden | Re: Water damage in bathroom | — | open | — |
| `TKT-85238301` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-ff0e0c76` | schimmel | Re: Schimmel im Schlafzimmer | — | open | — |
| `TKT-9eca372b` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-f8731b77` | wasserschaden | Re: Wasserschaden Bad | — | open | — |
| `TKT-5eef7bf8` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-dab9d13f` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-cdf6647a` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-e2a11fca` | wasserschaden | Wasserschaden Bad | — | open | — |
<!-- /auto:tickets.critical -->

### 3.2 Open Tickets — Aggregate
<!-- auto:tickets.aggregate -->
- total_open: `21`
- by_type: { abfluss: `5`, fenster: `4`, schimmel: `4`, schluessel: `2`, wasserschaden: `6` }
- live source: `db.tickets WHERE unit_id=EH-019 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren

<!-- auto:dunning.summary -->[Routine] Mieter MIE-025 ist seit vier Monaten im Verzug; offener Betrag 4.824,00 EUR zzgl. 61,79 EUR Verzugszinsen, letzte Zahlung 2025-12-01 [(bank)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv#TX-01557). Vertraglich geschuldet sind monatlich 1.206,00 EUR (Kaltmiete 1.031,00 EUR + NK 175,00 EUR) [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-025). Verzug nach § 286 BGB, Verzugszinsen § 288 I BGB; Mahnstufe 1 seit 2024-11-16 [(letter)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/briefe/2024-11/20241116_mahnung_LTR-0043.pdf), nächster Schritt: 2. Mahnung nach 14 Tagen.<!-- /auto:dunning.summary -->

#### Per claim
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-025` | — | 1 | 4824.00 EUR | 2025-12-01 | — | — |
- live balance pointer: `db.tenant_balance.tenant_id=MIE-025`
<!-- /auto:dunning -->

### 3.4 Active Reductions / Deferrals (§ 536 BGB)
<!-- auto:reductions -->
- date_raised: 2024-05-26
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-10-06
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-12-23
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-11-06
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-11-06
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
| Mieterwechsel | 2025-10-25 | Kündigung erhalten | Verwaltung | TBD | Übergabe-Termin offen |
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
| `TH-0ac7a6` | Mieterwechsel in WE 19 | 2025-02-25 | `EH-019` | active | 4 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250225_155500_EMAIL-03851.eml) |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `kontoauszug_2024_2025-csv` | bank | [bank/kontoauszug_2024_2025.csv](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv) | 2026-04-25 |
| `20241116_mahnung_LTR-0043-pdf` | letter | [briefe/2024-11/20241116_mahnung_LTR-0043.pdf](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/briefe/2024-11/20241116_mahnung_LTR-0043.pdf) | 2026-04-25 |
| `20240109_121000_EMAIL-00068-eml` | email | [emails/2024-01/20240109_121000_EMAIL-00068.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240109_121000_EMAIL-00068.eml) | 2024-01-09T12:10:00+00:00 |
| `20240111_113200_EMAIL-00086-eml` | email | [emails/2024-01/20240111_113200_EMAIL-00086.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240111_113200_EMAIL-00086.eml) | 2024-01-11T11:32:00+00:00 |
| `20240302_114900_EMAIL-00530-eml` | email | [emails/2024-03/20240302_114900_EMAIL-00530.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240302_114900_EMAIL-00530.eml) | 2024-03-02T11:49:00+00:00 |
| `20240304_172900_EMAIL-00550-eml` | email | [emails/2024-03/20240304_172900_EMAIL-00550.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240304_172900_EMAIL-00550.eml) | 2024-03-04T17:29:00+00:00 |
| `20240312_142400_EMAIL-00624-eml` | email | [emails/2024-03/20240312_142400_EMAIL-00624.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240312_142400_EMAIL-00624.eml) | 2024-03-12T14:24:00+00:00 |
| `20240326_131300_EMAIL-00735-eml` | email | [emails/2024-03/20240326_131300_EMAIL-00735.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240326_131300_EMAIL-00735.eml) | 2024-03-26T13:13:00+00:00 |
| `20240327_071300_EMAIL-00743-eml` | email | [emails/2024-03/20240327_071300_EMAIL-00743.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240327_071300_EMAIL-00743.eml) | 2024-03-27T07:13:00+00:00 |
| `20240329_143300_EMAIL-00767-eml` | email | [emails/2024-03/20240329_143300_EMAIL-00767.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240329_143300_EMAIL-00767.eml) | 2024-03-29T14:33:00+00:00 |
| `20240405_071300_EMAIL-00832-eml` | email | [emails/2024-04/20240405_071300_EMAIL-00832.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240405_071300_EMAIL-00832.eml) | 2024-04-05T07:13:00+00:00 |
| `20240421_103400_EMAIL-01007-eml` | email | [emails/2024-04/20240421_103400_EMAIL-01007.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240421_103400_EMAIL-01007.eml) | 2024-04-21T10:34:00+00:00 |
| `20240513_184200_EMAIL-01207-eml` | email | [emails/2024-05/20240513_184200_EMAIL-01207.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240513_184200_EMAIL-01207.eml) | 2024-05-13T18:42:00+00:00 |
| `20240520_112800_EMAIL-01260-eml` | email | [emails/2024-05/20240520_112800_EMAIL-01260.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240520_112800_EMAIL-01260.eml) | 2024-05-20T11:28:00+00:00 |
| `20240526_172500_EMAIL-01313-eml` | email | [emails/2024-05/20240526_172500_EMAIL-01313.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240526_172500_EMAIL-01313.eml) | 2024-05-26T17:25:00+00:00 |
| `20240527_102200_EMAIL-01315-eml` | email | [emails/2024-05/20240527_102200_EMAIL-01315.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240527_102200_EMAIL-01315.eml) | 2024-05-27T10:22:00+00:00 |
| `20240527_161000_EMAIL-01319-eml` | email | [emails/2024-05/20240527_161000_EMAIL-01319.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240527_161000_EMAIL-01319.eml) | 2024-05-27T16:10:00+00:00 |
| `20240527_191000_EMAIL-01322-eml` | email | [emails/2024-05/20240527_191000_EMAIL-01322.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240527_191000_EMAIL-01322.eml) | 2024-05-27T19:10:00+00:00 |
| `20240623_124200_EMAIL-01573-eml` | email | [emails/2024-06/20240623_124200_EMAIL-01573.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240623_124200_EMAIL-01573.eml) | 2024-06-23T12:42:00+00:00 |
| `20240625_102900_EMAIL-01584-eml` | email | [emails/2024-06/20240625_102900_EMAIL-01584.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240625_102900_EMAIL-01584.eml) | 2024-06-25T10:29:00+00:00 |
| `20240704_124800_EMAIL-01650-eml` | email | [emails/2024-07/20240704_124800_EMAIL-01650.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240704_124800_EMAIL-01650.eml) | 2024-07-04T12:48:00+00:00 |
| `20240721_150200_EMAIL-01824-eml` | email | [emails/2024-07/20240721_150200_EMAIL-01824.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240721_150200_EMAIL-01824.eml) | 2024-07-21T15:02:00+00:00 |
| `20240722_231100_EMAIL-01836-eml` | email | [emails/2024-07/20240722_231100_EMAIL-01836.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240722_231100_EMAIL-01836.eml) | 2024-07-22T23:11:00+00:00 |
| `20240723_120200_EMAIL-01843-eml` | email | [emails/2024-07/20240723_120200_EMAIL-01843.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240723_120200_EMAIL-01843.eml) | 2024-07-23T12:02:00+00:00 |
| `20240723_220900_EMAIL-01849-eml` | email | [emails/2024-07/20240723_220900_EMAIL-01849.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240723_220900_EMAIL-01849.eml) | 2024-07-23T22:09:00+00:00 |
| `20240724_154400_EMAIL-01854-eml` | email | [emails/2024-07/20240724_154400_EMAIL-01854.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240724_154400_EMAIL-01854.eml) | 2024-07-24T15:44:00+00:00 |
| `20240729_120200_EMAIL-01896-eml` | email | [emails/2024-07/20240729_120200_EMAIL-01896.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240729_120200_EMAIL-01896.eml) | 2024-07-29T12:02:00+00:00 |
| `20240902_163700_EMAIL-02225-eml` | email | [emails/2024-09/20240902_163700_EMAIL-02225.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240902_163700_EMAIL-02225.eml) | 2024-09-02T16:37:00+00:00 |
| `20240905_153200_EMAIL-02255-eml` | email | [emails/2024-09/20240905_153200_EMAIL-02255.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240905_153200_EMAIL-02255.eml) | 2024-09-05T15:32:00+00:00 |
| `20240907_003200_EMAIL-02269-eml` | email | [emails/2024-09/20240907_003200_EMAIL-02269.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240907_003200_EMAIL-02269.eml) | 2024-09-07T00:32:00+00:00 |
| `20240907_111900_EMAIL-02275-eml` | email | [emails/2024-09/20240907_111900_EMAIL-02275.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240907_111900_EMAIL-02275.eml) | 2024-09-07T11:19:00+00:00 |
| `20240914_003200_EMAIL-02346-eml` | email | [emails/2024-09/20240914_003200_EMAIL-02346.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240914_003200_EMAIL-02346.eml) | 2024-09-14T00:32:00+00:00 |
| `20241006_121800_EMAIL-02535-eml` | email | [emails/2024-10/20241006_121800_EMAIL-02535.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241006_121800_EMAIL-02535.eml) | 2024-10-06T12:18:00+00:00 |
| `20241020_143400_EMAIL-02664-eml` | email | [emails/2024-10/20241020_143400_EMAIL-02664.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241020_143400_EMAIL-02664.eml) | 2024-10-20T14:34:00+00:00 |
| `20241028_113700_EMAIL-02741-eml` | email | [emails/2024-10/20241028_113700_EMAIL-02741.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241028_113700_EMAIL-02741.eml) | 2024-10-28T11:37:00+00:00 |
| `20241029_025400_EMAIL-02751-eml` | email | [emails/2024-10/20241029_025400_EMAIL-02751.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241029_025400_EMAIL-02751.eml) | 2024-10-29T02:54:00+00:00 |
| `20241031_143400_EMAIL-02775-eml` | email | [emails/2024-10/20241031_143400_EMAIL-02775.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241031_143400_EMAIL-02775.eml) | 2024-10-31T14:34:00+00:00 |
| `20241105_165400_EMAIL-02826-eml` | email | [emails/2024-11/20241105_165400_EMAIL-02826.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241105_165400_EMAIL-02826.eml) | 2024-11-05T16:54:00+00:00 |
| `20241203_183100_EMAIL-03077-eml` | email | [emails/2024-12/20241203_183100_EMAIL-03077.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241203_183100_EMAIL-03077.eml) | 2024-12-03T18:31:00+00:00 |
| `20241204_203100_EMAIL-03086-eml` | email | [emails/2024-12/20241204_203100_EMAIL-03086.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241204_203100_EMAIL-03086.eml) | 2024-12-04T20:31:00+00:00 |
| `20241223_110100_EMAIL-03247-eml` | email | [emails/2024-12/20241223_110100_EMAIL-03247.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241223_110100_EMAIL-03247.eml) | 2024-12-23T11:01:00+00:00 |
| `20250104_120300_EMAIL-03374-eml` | email | [emails/2025-01/20250104_120300_EMAIL-03374.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250104_120300_EMAIL-03374.eml) | 2025-01-04T12:03:00+00:00 |
| `20250114_112600_EMAIL-03473-eml` | email | [emails/2025-01/20250114_112600_EMAIL-03473.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250114_112600_EMAIL-03473.eml) | 2025-01-14T11:26:00+00:00 |
| `20250131_110400_EMAIL-03610-eml` | email | [emails/2025-01/20250131_110400_EMAIL-03610.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250131_110400_EMAIL-03610.eml) | 2025-01-31T11:04:00+00:00 |
| `20250217_080300_EMAIL-03761-eml` | email | [emails/2025-02/20250217_080300_EMAIL-03761.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250217_080300_EMAIL-03761.eml) | 2025-02-17T08:03:00+00:00 |
| `20250225_155500_EMAIL-03851-eml` | email | [emails/2025-02/20250225_155500_EMAIL-03851.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250225_155500_EMAIL-03851.eml) | 2025-02-25 |
| `20250305_151500_EMAIL-03925-eml` | email | [emails/2025-03/20250305_151500_EMAIL-03925.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250305_151500_EMAIL-03925.eml) | 2025-03-05T15:15:00+00:00 |
| `20250309_112100_EMAIL-03963-eml` | email | [emails/2025-03/20250309_112100_EMAIL-03963.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250309_112100_EMAIL-03963.eml) | 2025-03-09T11:21:00+00:00 |
| `20250310_092100_EMAIL-03971-eml` | email | [emails/2025-03/20250310_092100_EMAIL-03971.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250310_092100_EMAIL-03971.eml) | 2025-03-10T09:21:00+00:00 |
| `20250317_092100_EMAIL-04037-eml` | email | [emails/2025-03/20250317_092100_EMAIL-04037.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250317_092100_EMAIL-04037.eml) | 2025-03-17T09:21:00+00:00 |
| `20250407_130000_EMAIL-04234-eml` | email | [emails/2025-04/20250407_130000_EMAIL-04234.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250407_130000_EMAIL-04234.eml) | 2025-04-07T13:00:00+00:00 |
| `20250409_110000_EMAIL-04245-eml` | email | [emails/2025-04/20250409_110000_EMAIL-04245.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250409_110000_EMAIL-04245.eml) | 2025-04-09T11:00:00+00:00 |
| `20250423_150800_EMAIL-04359-eml` | email | [emails/2025-04/20250423_150800_EMAIL-04359.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250423_150800_EMAIL-04359.eml) | 2025-04-23T15:08:00+00:00 |
| `20250423_180800_EMAIL-04361-eml` | email | [emails/2025-04/20250423_180800_EMAIL-04361.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250423_180800_EMAIL-04361.eml) | 2025-04-23T18:08:00+00:00 |
| `20250425_140100_EMAIL-04372-eml` | email | [emails/2025-04/20250425_140100_EMAIL-04372.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250425_140100_EMAIL-04372.eml) | 2025-04-25T14:01:00+00:00 |
| `20250513_112700_EMAIL-04502-eml` | email | [emails/2025-05/20250513_112700_EMAIL-04502.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250513_112700_EMAIL-04502.eml) | 2025-05-13T11:27:00+00:00 |
| `20250516_090400_EMAIL-04531-eml` | email | [emails/2025-05/20250516_090400_EMAIL-04531.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250516_090400_EMAIL-04531.eml) | 2025-05-16T09:04:00+00:00 |
| `20250517_175800_EMAIL-04543-eml` | email | [emails/2025-05/20250517_175800_EMAIL-04543.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250517_175800_EMAIL-04543.eml) | 2025-05-17T17:58:00+00:00 |
| `20250519_130300_EMAIL-04561-eml` | email | [emails/2025-05/20250519_130300_EMAIL-04561.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250519_130300_EMAIL-04561.eml) | 2025-05-19T13:03:00+00:00 |
| `20250520_172600_EMAIL-04575-eml` | email | [emails/2025-05/20250520_172600_EMAIL-04575.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250520_172600_EMAIL-04575.eml) | 2025-05-20T17:26:00+00:00 |
| `20250522_000300_EMAIL-04587-eml` | email | [emails/2025-05/20250522_000300_EMAIL-04587.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250522_000300_EMAIL-04587.eml) | 2025-05-22T00:03:00+00:00 |
| `20250707_165300_EMAIL-04964-eml` | email | [emails/2025-07/20250707_165300_EMAIL-04964.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250707_165300_EMAIL-04964.eml) | 2025-07-07T16:53:00+00:00 |
| `20250715_095700_EMAIL-05043-eml` | email | [emails/2025-07/20250715_095700_EMAIL-05043.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250715_095700_EMAIL-05043.eml) | 2025-07-15T09:57:00+00:00 |
| `20250806_150300_EMAIL-05211-eml` | email | [emails/2025-08/20250806_150300_EMAIL-05211.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250806_150300_EMAIL-05211.eml) | 2025-08-06T15:03:00+00:00 |
| `20250826_114000_EMAIL-05410-eml` | email | [emails/2025-08/20250826_114000_EMAIL-05410.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250826_114000_EMAIL-05410.eml) | 2025-08-26T11:40:00+00:00 |
| `20250904_103600_EMAIL-05516-eml` | email | [emails/2025-09/20250904_103600_EMAIL-05516.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250904_103600_EMAIL-05516.eml) | 2025-09-04T10:36:00+00:00 |
| `20250913_150800_EMAIL-05614-eml` | email | [emails/2025-09/20250913_150800_EMAIL-05614.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250913_150800_EMAIL-05614.eml) | 2025-09-13T15:08:00+00:00 |
| `20250914_040800_EMAIL-05619-eml` | email | [emails/2025-09/20250914_040800_EMAIL-05619.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250914_040800_EMAIL-05619.eml) | 2025-09-14T04:08:00+00:00 |
| `20250919_163300_EMAIL-05662-eml` | email | [emails/2025-09/20250919_163300_EMAIL-05662.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250919_163300_EMAIL-05662.eml) | 2025-09-19T16:33:00+00:00 |
| `20250920_140400_EMAIL-05667-eml` | email | [emails/2025-09/20250920_140400_EMAIL-05667.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250920_140400_EMAIL-05667.eml) | 2025-09-20T14:04:00+00:00 |
| `20250920_223300_EMAIL-05674-eml` | email | [emails/2025-09/20250920_223300_EMAIL-05674.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250920_223300_EMAIL-05674.eml) | 2025-09-20T22:33:00+00:00 |
| `20251025_091300_EMAIL-05961-eml` | email | [emails/2025-10/20251025_091300_EMAIL-05961.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251025_091300_EMAIL-05961.eml) | 2025-10-25T09:13:00+00:00 |
| `20251106_150200_EMAIL-06064-eml` | email | [emails/2025-11/20251106_150200_EMAIL-06064.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251106_150200_EMAIL-06064.eml) | 2025-11-06T15:02:00+00:00 |
| `20251106_230200_EMAIL-06069-eml` | email | [emails/2025-11/20251106_230200_EMAIL-06069.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251106_230200_EMAIL-06069.eml) | 2025-11-06T23:02:00+00:00 |
| `20251108_145400_EMAIL-06081-eml` | email | [emails/2025-11/20251108_145400_EMAIL-06081.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251108_145400_EMAIL-06081.eml) | 2025-11-08T14:54:00+00:00 |
| `20251111_121800_EMAIL-06100-eml` | email | [emails/2025-11/20251111_121800_EMAIL-06100.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251111_121800_EMAIL-06100.eml) | 2025-11-11T12:18:00+00:00 |
| `20251207_090900_EMAIL-06317-eml` | email | [emails/2025-12/20251207_090900_EMAIL-06317.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251207_090900_EMAIL-06317.eml) | 2025-12-07T09:09:00+00:00 |
| `20251211_162500_EMAIL-06357-eml` | email | [emails/2025-12/20251211_162500_EMAIL-06357.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251211_162500_EMAIL-06357.eml) | 2025-12-11T16:25:00+00:00 |
| `20251212_092500_EMAIL-06364-eml` | email | [emails/2025-12/20251212_092500_EMAIL-06364.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251212_092500_EMAIL-06364.eml) | 2025-12-12T09:25:00+00:00 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-25T20:52:09+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
