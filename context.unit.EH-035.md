# context.unit.<!-- auto:unit_id -->EH-035<!-- /auto:unit_id -->.md

> Per-unit dossier (one file per Einheit). Holds everything specific to this unit:
> the unit itself, the active lease, the tenant(s), and all unit/tenant-specific operations.
> **Property-wide data lives in `context.property.md`** — see `parent_property_ref` below.

<!-- auto:meta -->
- last_built_at: `2026-04-25T20:52:54+00:00`
- build_hash: `engine-v2`
- engine_version: `0.2.0`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `unit`
- unit_id: `EH-035`
- property_id: `LIE-001`
- parent_property_ref: `context.property.LIE-001.md`
- owner_ref: `EIG-011`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit -->
- unit_id: `EH-035`
- label: WE 35
- haus_id: `HAUS-14`
- floor: 5. OG
- position: links
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
- lease_id: `LEASE-MIE-018`
- unit_ref: `EH-035`
- start_date: 2022-01-30 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-018)
- end_date: _(no data in source yet)_
- term_type: `unbefristet`
- cancellation_status: `by_tenant` (notice_date: 2025-12-21, move_out_date: —)
- rent_components: { kaltmiete: 1224.0, betriebskosten_vorauszahlung: 272.0, total_warmmiete: 1496.00 }
- payment_mode: Überweisung
- iban_payer: DE93100500007098593174 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-018)
- kaution: { amount: 3672.0 }
- usage: `residential`
- subletting: { current_status: `requested` }
- special_agreements: _(no data in source yet)_
<!-- /auto:lease -->

### 2.1 Tenants on this Lease
<!-- auto:tenants -->
| tenant_id | name | role | contact_email | contact_phone | comms_pref | gesamtschuldner |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-018` | Frau Louise Ladeck | haupt | louise.ladeck@outlook.com | +49(0)0537 73515 | email | — |
<!-- /auto:tenants -->

---

## 3. Operations (this unit / this tenant)

### 3.1 Open Tickets — Critical (overdue or due ≤7 days)
<!-- auto:tickets.critical -->
| ticket_id | type | title | deadline | status | assignee |
| --- | --- | --- | --- | --- | --- |
| `TKT-c9c82b71` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-feb77b6b` | schimmel | Re: Schimmel im Schlafzimmer | — | open | — |
| `TKT-4800dc83` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-df5d4a81` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-b1b196a4` | schimmel | Re: Schimmel im Schlafzimmer | — | open | — |
| `TKT-a0af52d9` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-3c8cee25` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-1e6eba79` | schimmel | Re: Schimmel im Schlafzimmer | — | open | — |
| `TKT-94caf8a1` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-f6e9bee1` | wasserschaden | Re: Wasserschaden Bad | — | open | — |
| `TKT-3e6f7fc1` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-62d663fe` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-ab373a73` | wasserschaden | Wasserschaden Bad | — | open | — |
<!-- /auto:tickets.critical -->

### 3.2 Open Tickets — Aggregate
<!-- auto:tickets.aggregate -->
- total_open: `29`
- by_type: { abfluss: `2`, fenster: `9`, schimmel: `8`, schluessel: `5`, wasserschaden: `5` }
- live source: `db.tickets WHERE unit_id=EH-035 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren

<!-- auto:dunning.summary -->[Routine] Mieter MIE-018 ist seit vier Monaten im Verzug; offener Betrag 5.984,00 EUR zzgl. 76,64 EUR Verzugszinsen, letzte Zahlung 2025-12-01 [(bank)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv#TX-01556). Vertraglich geschuldet sind monatlich 1.496,00 EUR (Kaltmiete 1.224,00 EUR + NK 272,00 EUR) [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-018). Verzug nach § 286 BGB festgestellt, Verzugszinsen § 288 I BGB; Mahnstufe 1 aktiv, nächste Mahnung fällig nach 14 Tagen.<!-- /auto:dunning.summary -->

#### Per claim
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-018` | — | 1 | 5984.00 EUR | 2025-12-01 | — | — |
- live balance pointer: `db.tenant_balance.tenant_id=MIE-018`
<!-- /auto:dunning -->

### 3.4 Active Reductions / Deferrals (§ 536 BGB)
<!-- auto:reductions -->
- date_raised: 2024-05-09
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-05-11
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-10-22
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-10-23
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-11-01
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-12-18
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-01-29
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
| Mieterwechsel | 2025-12-21 | Kündigung erhalten | Verwaltung | TBD | Übergabe-Termin offen |
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
| `TH-1e3564` | Mieterwechsel in WE 35 | 2025-04-19 | `EH-035` | active | 7 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250419_181700_EMAIL-04334.eml) |
| `TH-eabeff` | Verkaufsabsicht WE 35 | 2025-05-24 | `EH-035` | active | 5 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250524_094000_EMAIL-04608.eml) |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `kontoauszug_2024_2025-csv` | bank | [bank/kontoauszug_2024_2025.csv](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv) | 2026-04-25 |
| `20240104_150100_EMAIL-00028-eml` | email | [emails/2024-01/20240104_150100_EMAIL-00028.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240104_150100_EMAIL-00028.eml) | 2024-01-04T15:01:00+00:00 |
| `20240131_203200_EMAIL-00257-eml` | email | [emails/2024-01/20240131_203200_EMAIL-00257.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240131_203200_EMAIL-00257.eml) | 2024-01-31T20:32:00+00:00 |
| `20240223_171500_EMAIL-00455-eml` | email | [emails/2024-02/20240223_171500_EMAIL-00455.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240223_171500_EMAIL-00455.eml) | 2024-02-23T17:15:00+00:00 |
| `20240225_171500_EMAIL-00469-eml` | email | [emails/2024-02/20240225_171500_EMAIL-00469.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240225_171500_EMAIL-00469.eml) | 2024-02-25T17:15:00+00:00 |
| `20240227_153000_EMAIL-00490-eml` | email | [emails/2024-02/20240227_153000_EMAIL-00490.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240227_153000_EMAIL-00490.eml) | 2024-02-27T15:30:00+00:00 |
| `20240320_101200_EMAIL-00688-eml` | email | [emails/2024-03/20240320_101200_EMAIL-00688.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240320_101200_EMAIL-00688.eml) | 2024-03-20T10:12:00+00:00 |
| `20240504_110600_EMAIL-01116-eml` | email | [emails/2024-05/20240504_110600_EMAIL-01116.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240504_110600_EMAIL-01116.eml) | 2024-05-04T11:06:00+00:00 |
| `20240505_163000_EMAIL-01127-eml` | email | [emails/2024-05/20240505_163000_EMAIL-01127.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240505_163000_EMAIL-01127.eml) | 2024-05-05T16:30:00+00:00 |
| `20240509_104000_EMAIL-01161-eml` | email | [emails/2024-05/20240509_104000_EMAIL-01161.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240509_104000_EMAIL-01161.eml) | 2024-05-09T10:40:00+00:00 |
| `20240510_164700_EMAIL-01170-eml` | email | [emails/2024-05/20240510_164700_EMAIL-01170.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240510_164700_EMAIL-01170.eml) | 2024-05-10T16:47:00+00:00 |
| `20240511_104000_EMAIL-01180-eml` | email | [emails/2024-05/20240511_104000_EMAIL-01180.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240511_104000_EMAIL-01180.eml) | 2024-05-11T10:40:00+00:00 |
| `20240511_161000_EMAIL-01182-eml` | email | [emails/2024-05/20240511_161000_EMAIL-01182.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240511_161000_EMAIL-01182.eml) | 2024-05-11T16:10:00+00:00 |
| `20240521_141700_EMAIL-01274-eml` | email | [emails/2024-05/20240521_141700_EMAIL-01274.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240521_141700_EMAIL-01274.eml) | 2024-05-21T14:17:00+00:00 |
| `20240521_185200_EMAIL-01277-eml` | email | [emails/2024-05/20240521_185200_EMAIL-01277.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240521_185200_EMAIL-01277.eml) | 2024-05-21T18:52:00+00:00 |
| `20240523_145200_EMAIL-01287-eml` | email | [emails/2024-05/20240523_145200_EMAIL-01287.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240523_145200_EMAIL-01287.eml) | 2024-05-23T14:52:00+00:00 |
| `20240603_111600_EMAIL-01395-eml` | email | [emails/2024-06/20240603_111600_EMAIL-01395.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240603_111600_EMAIL-01395.eml) | 2024-06-03T11:16:00+00:00 |
| `20240622_160900_EMAIL-01566-eml` | email | [emails/2024-06/20240622_160900_EMAIL-01566.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240622_160900_EMAIL-01566.eml) | 2024-06-22T16:09:00+00:00 |
| `20240703_102700_EMAIL-01642-eml` | email | [emails/2024-07/20240703_102700_EMAIL-01642.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240703_102700_EMAIL-01642.eml) | 2024-07-03T10:27:00+00:00 |
| `20240707_042700_EMAIL-01679-eml` | email | [emails/2024-07/20240707_042700_EMAIL-01679.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240707_042700_EMAIL-01679.eml) | 2024-07-07T04:27:00+00:00 |
| `20240707_100100_EMAIL-01681-eml` | email | [emails/2024-07/20240707_100100_EMAIL-01681.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240707_100100_EMAIL-01681.eml) | 2024-07-07T10:01:00+00:00 |
| `20240708_150300_EMAIL-01698-eml` | email | [emails/2024-07/20240708_150300_EMAIL-01698.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240708_150300_EMAIL-01698.eml) | 2024-07-08T15:03:00+00:00 |
| `20240712_203700_EMAIL-01750-eml` | email | [emails/2024-07/20240712_203700_EMAIL-01750.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240712_203700_EMAIL-01750.eml) | 2024-07-12T20:37:00+00:00 |
| `20240730_054600_EMAIL-01902-eml` | email | [emails/2024-07/20240730_054600_EMAIL-01902.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240730_054600_EMAIL-01902.eml) | 2024-07-30T05:46:00+00:00 |
| `20240816_170600_EMAIL-02063-eml` | email | [emails/2024-08/20240816_170600_EMAIL-02063.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240816_170600_EMAIL-02063.eml) | 2024-08-16T17:06:00+00:00 |
| `20240816_171300_EMAIL-02064-eml` | email | [emails/2024-08/20240816_171300_EMAIL-02064.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240816_171300_EMAIL-02064.eml) | 2024-08-16T17:13:00+00:00 |
| `20240910_114500_EMAIL-02310-eml` | email | [emails/2024-09/20240910_114500_EMAIL-02310.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240910_114500_EMAIL-02310.eml) | 2024-09-10T11:45:00+00:00 |
| `20241004_174900_EMAIL-02522-eml` | email | [emails/2024-10/20241004_174900_EMAIL-02522.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241004_174900_EMAIL-02522.eml) | 2024-10-04T17:49:00+00:00 |
| `20241009_144900_EMAIL-02572-eml` | email | [emails/2024-10/20241009_144900_EMAIL-02572.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241009_144900_EMAIL-02572.eml) | 2024-10-09T14:49:00+00:00 |
| `20241013_161000_EMAIL-02606-eml` | email | [emails/2024-10/20241013_161000_EMAIL-02606.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241013_161000_EMAIL-02606.eml) | 2024-10-13T16:10:00+00:00 |
| `20241018_113800_EMAIL-02646-eml` | email | [emails/2024-10/20241018_113800_EMAIL-02646.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241018_113800_EMAIL-02646.eml) | 2024-10-18T11:38:00+00:00 |
| `20241018_154900_EMAIL-02652-eml` | email | [emails/2024-10/20241018_154900_EMAIL-02652.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241018_154900_EMAIL-02652.eml) | 2024-10-18T15:49:00+00:00 |
| `20241022_150500_EMAIL-02687-eml` | email | [emails/2024-10/20241022_150500_EMAIL-02687.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241022_150500_EMAIL-02687.eml) | 2024-10-22T15:05:00+00:00 |
| `20241023_000500_EMAIL-02691-eml` | email | [emails/2024-10/20241023_000500_EMAIL-02691.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241023_000500_EMAIL-02691.eml) | 2024-10-23T00:05:00+00:00 |
| `20241101_084200_EMAIL-02782-eml` | email | [emails/2024-11/20241101_084200_EMAIL-02782.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241101_084200_EMAIL-02782.eml) | 2024-11-01T08:42:00+00:00 |
| `20241109_141600_EMAIL-02857-eml` | email | [emails/2024-11/20241109_141600_EMAIL-02857.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241109_141600_EMAIL-02857.eml) | 2024-11-09T14:16:00+00:00 |
| `20241113_171500_EMAIL-02898-eml` | email | [emails/2024-11/20241113_171500_EMAIL-02898.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241113_171500_EMAIL-02898.eml) | 2024-11-13T17:15:00+00:00 |
| `20241125_161500_EMAIL-03007-eml` | email | [emails/2024-11/20241125_161500_EMAIL-03007.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241125_161500_EMAIL-03007.eml) | 2024-11-25T16:15:00+00:00 |
| `20241201_161300_EMAIL-03062-eml` | email | [emails/2024-12/20241201_161300_EMAIL-03062.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241201_161300_EMAIL-03062.eml) | 2024-12-01T16:13:00+00:00 |
| `20241207_114000_EMAIL-03111-eml` | email | [emails/2024-12/20241207_114000_EMAIL-03111.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241207_114000_EMAIL-03111.eml) | 2024-12-07T11:40:00+00:00 |
| `20241207_121400_EMAIL-03112-eml` | email | [emails/2024-12/20241207_121400_EMAIL-03112.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241207_121400_EMAIL-03112.eml) | 2024-12-07T12:14:00+00:00 |
| `20241209_121400_EMAIL-03133-eml` | email | [emails/2024-12/20241209_121400_EMAIL-03133.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241209_121400_EMAIL-03133.eml) | 2024-12-09T12:14:00+00:00 |
| `20241218_115700_EMAIL-03202-eml` | email | [emails/2024-12/20241218_115700_EMAIL-03202.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241218_115700_EMAIL-03202.eml) | 2024-12-18T11:57:00+00:00 |
| `20241221_111600_EMAIL-03227-eml` | email | [emails/2024-12/20241221_111600_EMAIL-03227.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241221_111600_EMAIL-03227.eml) | 2024-12-21T11:16:00+00:00 |
| `20241221_131600_EMAIL-03229-eml` | email | [emails/2024-12/20241221_131600_EMAIL-03229.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241221_131600_EMAIL-03229.eml) | 2024-12-21T13:16:00+00:00 |
| `20250105_113400_EMAIL-03384-eml` | email | [emails/2025-01/20250105_113400_EMAIL-03384.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250105_113400_EMAIL-03384.eml) | 2025-01-05T11:34:00+00:00 |
| `20250110_140700_EMAIL-03434-eml` | email | [emails/2025-01/20250110_140700_EMAIL-03434.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250110_140700_EMAIL-03434.eml) | 2025-01-10T14:07:00+00:00 |
| `20250125_163700_EMAIL-03561-eml` | email | [emails/2025-01/20250125_163700_EMAIL-03561.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250125_163700_EMAIL-03561.eml) | 2025-01-25T16:37:00+00:00 |
| `20250127_133400_EMAIL-03573-eml` | email | [emails/2025-01/20250127_133400_EMAIL-03573.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250127_133400_EMAIL-03573.eml) | 2025-01-27T13:34:00+00:00 |
| `20250128_171700_EMAIL-03588-eml` | email | [emails/2025-01/20250128_171700_EMAIL-03588.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250128_171700_EMAIL-03588.eml) | 2025-01-28T17:17:00+00:00 |
| `20250129_124200_EMAIL-03593-eml` | email | [emails/2025-01/20250129_124200_EMAIL-03593.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250129_124200_EMAIL-03593.eml) | 2025-01-29T12:42:00+00:00 |
| `20250205_094900_EMAIL-03646-eml` | email | [emails/2025-02/20250205_094900_EMAIL-03646.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250205_094900_EMAIL-03646.eml) | 2025-02-05T09:49:00+00:00 |
| `20250208_111700_EMAIL-03675-eml` | email | [emails/2025-02/20250208_111700_EMAIL-03675.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250208_111700_EMAIL-03675.eml) | 2025-02-08T11:17:00+00:00 |
| `20250216_085700_EMAIL-03749-eml` | email | [emails/2025-02/20250216_085700_EMAIL-03749.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250216_085700_EMAIL-03749.eml) | 2025-02-16T08:57:00+00:00 |
| `20250216_195700_EMAIL-03757-eml` | email | [emails/2025-02/20250216_195700_EMAIL-03757.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250216_195700_EMAIL-03757.eml) | 2025-02-16T19:57:00+00:00 |
| `20250225_110900_EMAIL-03847-eml` | email | [emails/2025-02/20250225_110900_EMAIL-03847.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250225_110900_EMAIL-03847.eml) | 2025-02-25T11:09:00+00:00 |
| `20250227_060900_EMAIL-03864-eml` | email | [emails/2025-02/20250227_060900_EMAIL-03864.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250227_060900_EMAIL-03864.eml) | 2025-02-27T06:09:00+00:00 |
| `20250310_003500_EMAIL-03969-eml` | email | [emails/2025-03/20250310_003500_EMAIL-03969.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250310_003500_EMAIL-03969.eml) | 2025-03-10T00:35:00+00:00 |
| `20250310_093300_EMAIL-03972-eml` | email | [emails/2025-03/20250310_093300_EMAIL-03972.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250310_093300_EMAIL-03972.eml) | 2025-03-10T09:33:00+00:00 |
| `20250418_162700_EMAIL-04326-eml` | email | [emails/2025-04/20250418_162700_EMAIL-04326.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250418_162700_EMAIL-04326.eml) | 2025-04-18T16:27:00+00:00 |
| `20250419_181700_EMAIL-04334-eml` | email | [emails/2025-04/20250419_181700_EMAIL-04334.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250419_181700_EMAIL-04334.eml) | 2025-04-19 |
| `20250523_103600_EMAIL-04596-eml` | email | [emails/2025-05/20250523_103600_EMAIL-04596.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250523_103600_EMAIL-04596.eml) | 2025-05-23T10:36:00+00:00 |
| `20250524_094000_EMAIL-04608-eml` | email | [emails/2025-05/20250524_094000_EMAIL-04608.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250524_094000_EMAIL-04608.eml) | 2025-05-24 |
| `20250610_154700_EMAIL-04742-eml` | email | [emails/2025-06/20250610_154700_EMAIL-04742.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250610_154700_EMAIL-04742.eml) | 2025-06-10T15:47:00+00:00 |
| `20250709_170000_EMAIL-04984-eml` | email | [emails/2025-07/20250709_170000_EMAIL-04984.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250709_170000_EMAIL-04984.eml) | 2025-07-09T17:00:00+00:00 |
| `20250718_082600_EMAIL-05065-eml` | email | [emails/2025-07/20250718_082600_EMAIL-05065.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250718_082600_EMAIL-05065.eml) | 2025-07-18T08:26:00+00:00 |
| `20250809_172000_EMAIL-05238-eml` | email | [emails/2025-08/20250809_172000_EMAIL-05238.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250809_172000_EMAIL-05238.eml) | 2025-08-09T17:20:00+00:00 |
| `20250829_151600_EMAIL-05445-eml` | email | [emails/2025-08/20250829_151600_EMAIL-05445.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250829_151600_EMAIL-05445.eml) | 2025-08-29T15:16:00+00:00 |
| `20250912_122200_EMAIL-05605-eml` | email | [emails/2025-09/20250912_122200_EMAIL-05605.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250912_122200_EMAIL-05605.eml) | 2025-09-12T12:22:00+00:00 |
| `20250920_153300_EMAIL-05671-eml` | email | [emails/2025-09/20250920_153300_EMAIL-05671.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250920_153300_EMAIL-05671.eml) | 2025-09-20T15:33:00+00:00 |
| `20250921_193300_EMAIL-05684-eml` | email | [emails/2025-09/20250921_193300_EMAIL-05684.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250921_193300_EMAIL-05684.eml) | 2025-09-21T19:33:00+00:00 |
| `20250924_114900_EMAIL-05699-eml` | email | [emails/2025-09/20250924_114900_EMAIL-05699.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250924_114900_EMAIL-05699.eml) | 2025-09-24T11:49:00+00:00 |
| `20251013_170100_EMAIL-05868-eml` | email | [emails/2025-10/20251013_170100_EMAIL-05868.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251013_170100_EMAIL-05868.eml) | 2025-10-13T17:01:00+00:00 |
| `20251102_185200_EMAIL-06026-eml` | email | [emails/2025-11/20251102_185200_EMAIL-06026.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251102_185200_EMAIL-06026.eml) | 2025-11-02T18:52:00+00:00 |
| `20251113_082500_EMAIL-06110-eml` | email | [emails/2025-11/20251113_082500_EMAIL-06110.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251113_082500_EMAIL-06110.eml) | 2025-11-13T08:25:00+00:00 |
| `20251115_123400_EMAIL-06126-eml` | email | [emails/2025-11/20251115_123400_EMAIL-06126.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251115_123400_EMAIL-06126.eml) | 2025-11-15T12:34:00+00:00 |
| `20251116_084400_EMAIL-06132-eml` | email | [emails/2025-11/20251116_084400_EMAIL-06132.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251116_084400_EMAIL-06132.eml) | 2025-11-16T08:44:00+00:00 |
| `20251116_163500_EMAIL-06139-eml` | email | [emails/2025-11/20251116_163500_EMAIL-06139.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251116_163500_EMAIL-06139.eml) | 2025-11-16T16:35:00+00:00 |
| `20251117_131500_EMAIL-06147-eml` | email | [emails/2025-11/20251117_131500_EMAIL-06147.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251117_131500_EMAIL-06147.eml) | 2025-11-17T13:15:00+00:00 |
| `20251123_120900_EMAIL-06202-eml` | email | [emails/2025-11/20251123_120900_EMAIL-06202.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251123_120900_EMAIL-06202.eml) | 2025-11-23T12:09:00+00:00 |
| `20251209_160800_EMAIL-06340-eml` | email | [emails/2025-12/20251209_160800_EMAIL-06340.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251209_160800_EMAIL-06340.eml) | 2025-12-09T16:08:00+00:00 |
| `20251221_102300_EMAIL-06452-eml` | email | [emails/2025-12/20251221_102300_EMAIL-06452.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251221_102300_EMAIL-06452.eml) | 2025-12-21T10:23:00+00:00 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-25T20:52:09+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
