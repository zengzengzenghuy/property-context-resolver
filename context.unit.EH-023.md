# context.unit.<!-- auto:unit_id -->EH-023<!-- /auto:unit_id -->.md

> Per-unit dossier (one file per Einheit). Holds everything specific to this unit:
> the unit itself, the active lease, the tenant(s), and all unit/tenant-specific operations.
> **Property-wide data lives in `context.property.md`** — see `parent_property_ref` below.

<!-- auto:meta -->
- last_built_at: `2026-04-25T20:04:22+00:00`
- build_hash: `engine-v2`
- engine_version: `0.2.0`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `unit`
- parent_property_ref: `context.property.LIE-001.md`
- owner_ref: `EIG-013`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit -->
- unit_id: `EH-023`
- label: WE 23
- haus_id: `HAUS-14`
- floor: 2. OG
- position: mitte
- typ: Wohnung
- area_sqm: 96.0
- rooms: 3.5
- mea_‰: 223
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
- lease_id: `LEASE-MIE-007`
- unit_ref: `EH-023`
- start_date: 2024-01-07 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-007)
- end_date: _(no data in source yet)_
- term_type: `unbefristet`
- cancellation_status: `none`
- rent_components: { kaltmiete: 1511.0, betriebskosten_vorauszahlung: 256.0, total_warmmiete: 1767.00 }
- payment_mode: Überweisung
- iban_payer: DE86100701244677378263 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-007)
- kaution: { amount: 4533.0 }
- usage: `residential`
- subletting: { current_status: `none` }
- special_agreements: _(no data in source yet)_
<!-- /auto:lease -->

### 2.1 Tenants on this Lease
<!-- auto:tenants -->
| tenant_id | name | role | contact_email | contact_phone | comms_pref | gesamtschuldner |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-007` | Herr David Jenkins | haupt | david.jenkins@gmail.com | +1-622-921-9693x79237 | email | — |
<!-- /auto:tenants -->

---

## 3. Operations (this unit / this tenant)

### 3.1 Open Tickets — Critical (overdue or due ≤7 days)
<!-- auto:tickets.critical -->
| ticket_id | type | title | deadline | status | assignee |
| --- | --- | --- | --- | --- | --- |
| `TKT-02b70d83` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-a6de2bee` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-bb5abf11` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-b9c0cfa5` | wasserschaden | Re: Water damage in bathroom | — | open | — |
| `TKT-831a0873` | wasserschaden | Re: Water damage in bathroom | — | open | — |
| `TKT-620d983c` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-fd489f6f` | wasserschaden | Re: Water damage in bathroom | — | open | — |
| `TKT-b66b680e` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-488af38b` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-aa6323d0` | wasserschaden | Re: Water damage in bathroom | — | open | — |
| `TKT-d8b40083` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-1c0086f3` | wasserschaden | Re: Water damage in bathroom | — | open | — |
| `TKT-bc81f487` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-082a62a6` | wasserschaden | Re: Water damage in bathroom | — | open | — |
| `TKT-d60f2093` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-ce17dc85` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-1d4ebb68` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-6801847d` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-dee57dc9` | wasserschaden | Re: Water damage in bathroom | — | open | — |
| `TKT-12fa623c` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-d4dd587b` | wasserschaden | Re: Water damage in bathroom | — | open | — |
| `TKT-0c25cf43` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-04d0e1f8` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-0644b524` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-3ee287c6` | wasserschaden | Re: Water damage in bathroom | — | open | — |
<!-- /auto:tickets.critical -->

### 3.2 Open Tickets — Aggregate
<!-- auto:tickets.aggregate -->
- total_open: `31`
- by_type: { schluessel: `6`, wasserschaden: `25` }
- live source: `db.tickets WHERE unit_id=EH-023 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren (per claim)
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-007` | — | 1 | 7068.00 EUR | 2025-12-03 | — | — |
- live balance pointer: `db.tenant_balance.tenant_id=MIE-007`
<!-- /auto:dunning -->

### 3.4 Active Reductions / Deferrals (§ 536 BGB)
<!-- auto:reductions -->_(no data in source yet)_<!-- /auto:reductions -->

### 3.5 Latest Übergabeprotokoll
<!-- auto:handover -->_(no data in source yet)_<!-- /auto:handover -->

### 3.6 Recurring Process State (this unit, in-flight)
<!-- auto:recurring -->
| process_type | started | current_step | owner | eta | blockers |
| --- | --- | --- | --- | --- | --- |
_(no data in source yet)_
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
| `TH-b6c54f` | Noise complaint | 2025-12-15 | `MIE-007` | active | 56 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251215_104800_EMAIL-06401.eml) |
| `TH-d078ba` | Question about utility bill | 2025-11-14 | `MIE-007` | active | 44 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251114_144200_EMAIL-06120.eml) |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `kontoauszug_2024_2025-csv` | bank | [bank/kontoauszug_2024_2025.csv](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv) | 2026-04-25 |
| `20240128_140800_EMAIL-00224-eml` | email | [emails/2024-01/20240128_140800_EMAIL-00224.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240128_140800_EMAIL-00224.eml) | 2024-01-28T14:08:00+00:00 |
| `20240201_083000_EMAIL-00260-eml` | email | [emails/2024-02/20240201_083000_EMAIL-00260.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240201_083000_EMAIL-00260.eml) | 2024-02-01T08:30:00+00:00 |
| `20240201_150700_EMAIL-00270-eml` | email | [emails/2024-02/20240201_150700_EMAIL-00270.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240201_150700_EMAIL-00270.eml) | 2024-02-01T15:07:00+00:00 |
| `20240203_150700_EMAIL-00287-eml` | email | [emails/2024-02/20240203_150700_EMAIL-00287.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240203_150700_EMAIL-00287.eml) | 2024-02-03T15:07:00+00:00 |
| `20240208_150700_EMAIL-00334-eml` | email | [emails/2024-02/20240208_150700_EMAIL-00334.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240208_150700_EMAIL-00334.eml) | 2024-02-08T15:07:00+00:00 |
| `20240217_092400_EMAIL-00404-eml` | email | [emails/2024-02/20240217_092400_EMAIL-00404.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240217_092400_EMAIL-00404.eml) | 2024-02-17T09:24:00+00:00 |
| `20240219_162900_EMAIL-00418-eml` | email | [emails/2024-02/20240219_162900_EMAIL-00418.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240219_162900_EMAIL-00418.eml) | 2024-02-19T16:29:00+00:00 |
| `20240416_105500_EMAIL-00953-eml` | email | [emails/2024-04/20240416_105500_EMAIL-00953.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240416_105500_EMAIL-00953.eml) | 2024-04-16T10:55:00+00:00 |
| `20240417_045500_EMAIL-00966-eml` | email | [emails/2024-04/20240417_045500_EMAIL-00966.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240417_045500_EMAIL-00966.eml) | 2024-04-17T04:55:00+00:00 |
| `20240427_161600_EMAIL-01056-eml` | email | [emails/2024-04/20240427_161600_EMAIL-01056.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240427_161600_EMAIL-01056.eml) | 2024-04-27T16:16:00+00:00 |
| `20240428_121600_EMAIL-01061-eml` | email | [emails/2024-04/20240428_121600_EMAIL-01061.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240428_121600_EMAIL-01061.eml) | 2024-04-28T12:16:00+00:00 |
| `20240505_185800_EMAIL-01130-eml` | email | [emails/2024-05/20240505_185800_EMAIL-01130.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240505_185800_EMAIL-01130.eml) | 2024-05-05T18:58:00+00:00 |
| `20240506_121600_EMAIL-01136-eml` | email | [emails/2024-05/20240506_121600_EMAIL-01136.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240506_121600_EMAIL-01136.eml) | 2024-05-06T12:16:00+00:00 |
| `20240804_155200_EMAIL-01961-eml` | email | [emails/2024-08/20240804_155200_EMAIL-01961.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240804_155200_EMAIL-01961.eml) | 2024-08-04T15:52:00+00:00 |
| `20240805_145200_EMAIL-01972-eml` | email | [emails/2024-08/20240805_145200_EMAIL-01972.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240805_145200_EMAIL-01972.eml) | 2024-08-05T14:52:00+00:00 |
| `20240820_114600_EMAIL-02106-eml` | email | [emails/2024-08/20240820_114600_EMAIL-02106.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240820_114600_EMAIL-02106.eml) | 2024-08-20T11:46:00+00:00 |
| `20240906_155300_EMAIL-02266-eml` | email | [emails/2024-09/20240906_155300_EMAIL-02266.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240906_155300_EMAIL-02266.eml) | 2024-09-06T15:53:00+00:00 |
| `20240914_145500_EMAIL-02353-eml` | email | [emails/2024-09/20240914_145500_EMAIL-02353.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240914_145500_EMAIL-02353.eml) | 2024-09-14T14:55:00+00:00 |
| `20240919_102500_EMAIL-02382-eml` | email | [emails/2024-09/20240919_102500_EMAIL-02382.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240919_102500_EMAIL-02382.eml) | 2024-09-19T10:25:00+00:00 |
| `20240919_182500_EMAIL-02387-eml` | email | [emails/2024-09/20240919_182500_EMAIL-02387.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240919_182500_EMAIL-02387.eml) | 2024-09-19T18:25:00+00:00 |
| `20240930_102900_EMAIL-02482-eml` | email | [emails/2024-09/20240930_102900_EMAIL-02482.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240930_102900_EMAIL-02482.eml) | 2024-09-30T10:29:00+00:00 |
| `20240930_232900_EMAIL-02486-eml` | email | [emails/2024-09/20240930_232900_EMAIL-02486.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240930_232900_EMAIL-02486.eml) | 2024-09-30T23:29:00+00:00 |
| `20241003_080800_EMAIL-02498-eml` | email | [emails/2024-10/20241003_080800_EMAIL-02498.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241003_080800_EMAIL-02498.eml) | 2024-10-03T08:08:00+00:00 |
| `20241005_000800_EMAIL-02524-eml` | email | [emails/2024-10/20241005_000800_EMAIL-02524.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241005_000800_EMAIL-02524.eml) | 2024-10-05T00:08:00+00:00 |
| `20250113_124200_EMAIL-03454-eml` | email | [emails/2025-01/20250113_124200_EMAIL-03454.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250113_124200_EMAIL-03454.eml) | 2025-01-13T12:42:00+00:00 |
| `20250114_081700_EMAIL-03467-eml` | email | [emails/2025-01/20250114_081700_EMAIL-03467.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250114_081700_EMAIL-03467.eml) | 2025-01-14T08:17:00+00:00 |
| `20250119_174800_EMAIL-03521-eml` | email | [emails/2025-01/20250119_174800_EMAIL-03521.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250119_174800_EMAIL-03521.eml) | 2025-01-19T17:48:00+00:00 |
| `20250211_160400_EMAIL-03698-eml` | email | [emails/2025-02/20250211_160400_EMAIL-03698.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250211_160400_EMAIL-03698.eml) | 2025-02-11T16:04:00+00:00 |
| `20250220_114400_EMAIL-03791-eml` | email | [emails/2025-02/20250220_114400_EMAIL-03791.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250220_114400_EMAIL-03791.eml) | 2025-02-20T11:44:00+00:00 |
| `20250220_134400_EMAIL-03792-eml` | email | [emails/2025-02/20250220_134400_EMAIL-03792.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250220_134400_EMAIL-03792.eml) | 2025-02-20T13:44:00+00:00 |
| `20250223_152400_EMAIL-03825-eml` | email | [emails/2025-02/20250223_152400_EMAIL-03825.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250223_152400_EMAIL-03825.eml) | 2025-02-23T15:24:00+00:00 |
| `20250223_192400_EMAIL-03828-eml` | email | [emails/2025-02/20250223_192400_EMAIL-03828.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250223_192400_EMAIL-03828.eml) | 2025-02-23T19:24:00+00:00 |
| `20250227_192400_EMAIL-03877-eml` | email | [emails/2025-02/20250227_192400_EMAIL-03877.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250227_192400_EMAIL-03877.eml) | 2025-02-27T19:24:00+00:00 |
| `20250305_172300_EMAIL-03926-eml` | email | [emails/2025-03/20250305_172300_EMAIL-03926.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250305_172300_EMAIL-03926.eml) | 2025-03-05T17:23:00+00:00 |
| `20250307_162300_EMAIL-03944-eml` | email | [emails/2025-03/20250307_162300_EMAIL-03944.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250307_162300_EMAIL-03944.eml) | 2025-03-07T16:23:00+00:00 |
| `20250317_091600_EMAIL-04036-eml` | email | [emails/2025-03/20250317_091600_EMAIL-04036.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250317_091600_EMAIL-04036.eml) | 2025-03-17T09:16:00+00:00 |
| `20250318_163600_EMAIL-04058-eml` | email | [emails/2025-03/20250318_163600_EMAIL-04058.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250318_163600_EMAIL-04058.eml) | 2025-03-18T16:36:00+00:00 |
| `20250330_112300_EMAIL-04158-eml` | email | [emails/2025-03/20250330_112300_EMAIL-04158.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250330_112300_EMAIL-04158.eml) | 2025-03-30T11:23:00+00:00 |
| `20250330_113800_EMAIL-04159-eml` | email | [emails/2025-03/20250330_113800_EMAIL-04159.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250330_113800_EMAIL-04159.eml) | 2025-03-30T11:38:00+00:00 |
| `20250401_043800_EMAIL-04174-eml` | email | [emails/2025-04/20250401_043800_EMAIL-04174.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250401_043800_EMAIL-04174.eml) | 2025-04-01T04:38:00+00:00 |
| `20250504_171300_EMAIL-04434-eml` | email | [emails/2025-05/20250504_171300_EMAIL-04434.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250504_171300_EMAIL-04434.eml) | 2025-05-04T17:13:00+00:00 |
| `20250531_121400_EMAIL-04672-eml` | email | [emails/2025-05/20250531_121400_EMAIL-04672.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250531_121400_EMAIL-04672.eml) | 2025-05-31T12:14:00+00:00 |
| `20250720_175700_EMAIL-05099-eml` | email | [emails/2025-07/20250720_175700_EMAIL-05099.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250720_175700_EMAIL-05099.eml) | 2025-07-20T17:57:00+00:00 |
| `20250802_100300_EMAIL-05182-eml` | email | [emails/2025-08/20250802_100300_EMAIL-05182.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250802_100300_EMAIL-05182.eml) | 2025-08-02T10:03:00+00:00 |
| `20250808_163100_EMAIL-05226-eml` | email | [emails/2025-08/20250808_163100_EMAIL-05226.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250808_163100_EMAIL-05226.eml) | 2025-08-08T16:31:00+00:00 |
| `20250810_090400_EMAIL-05241-eml` | email | [emails/2025-08/20250810_090400_EMAIL-05241.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250810_090400_EMAIL-05241.eml) | 2025-08-10T09:04:00+00:00 |
| `20250810_203200_EMAIL-05249-eml` | email | [emails/2025-08/20250810_203200_EMAIL-05249.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250810_203200_EMAIL-05249.eml) | 2025-08-10T20:32:00+00:00 |
| `20250811_033200_EMAIL-05250-eml` | email | [emails/2025-08/20250811_033200_EMAIL-05250.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250811_033200_EMAIL-05250.eml) | 2025-08-11T03:32:00+00:00 |
| `20250811_151800_EMAIL-05257-eml` | email | [emails/2025-08/20250811_151800_EMAIL-05257.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250811_151800_EMAIL-05257.eml) | 2025-08-11T15:18:00+00:00 |
| `20250825_095100_EMAIL-05396-eml` | email | [emails/2025-08/20250825_095100_EMAIL-05396.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250825_095100_EMAIL-05396.eml) | 2025-08-25T09:51:00+00:00 |
| `20250828_110100_EMAIL-05429-eml` | email | [emails/2025-08/20250828_110100_EMAIL-05429.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250828_110100_EMAIL-05429.eml) | 2025-08-28T11:01:00+00:00 |
| `20250910_181600_EMAIL-05591-eml` | email | [emails/2025-09/20250910_181600_EMAIL-05591.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250910_181600_EMAIL-05591.eml) | 2025-09-10T18:16:00+00:00 |
| `20250911_160100_EMAIL-05599-eml` | email | [emails/2025-09/20250911_160100_EMAIL-05599.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250911_160100_EMAIL-05599.eml) | 2025-09-11T16:01:00+00:00 |
| `20250912_071600_EMAIL-05602-eml` | email | [emails/2025-09/20250912_071600_EMAIL-05602.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250912_071600_EMAIL-05602.eml) | 2025-09-12T07:16:00+00:00 |
| `20250924_123600_EMAIL-05700-eml` | email | [emails/2025-09/20250924_123600_EMAIL-05700.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250924_123600_EMAIL-05700.eml) | 2025-09-24T12:36:00+00:00 |
| `20251008_182000_EMAIL-05817-eml` | email | [emails/2025-10/20251008_182000_EMAIL-05817.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251008_182000_EMAIL-05817.eml) | 2025-10-08T18:20:00+00:00 |
| `20251011_142500_EMAIL-05843-eml` | email | [emails/2025-10/20251011_142500_EMAIL-05843.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251011_142500_EMAIL-05843.eml) | 2025-10-11T14:25:00+00:00 |
| `20251012_092500_EMAIL-05847-eml` | email | [emails/2025-10/20251012_092500_EMAIL-05847.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251012_092500_EMAIL-05847.eml) | 2025-10-12T09:25:00+00:00 |
| `20251110_143800_EMAIL-06094-eml` | email | [emails/2025-11/20251110_143800_EMAIL-06094.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251110_143800_EMAIL-06094.eml) | 2025-11-10T14:38:00+00:00 |
| `20251111_133000_EMAIL-06101-eml` | email | [emails/2025-11/20251111_133000_EMAIL-06101.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251111_133000_EMAIL-06101.eml) | 2025-11-11T13:30:00+00:00 |
| `20251114_144200_EMAIL-06120-eml` | email | [emails/2025-11/20251114_144200_EMAIL-06120.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251114_144200_EMAIL-06120.eml) | 2025-11-14T14:42:00+00:00 |
| `20251119_101200_EMAIL-06159-eml` | email | [emails/2025-11/20251119_101200_EMAIL-06159.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251119_101200_EMAIL-06159.eml) | 2025-11-19T10:12:00+00:00 |
| `20251121_080000_EMAIL-06174-eml` | email | [emails/2025-11/20251121_080000_EMAIL-06174.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251121_080000_EMAIL-06174.eml) | 2025-11-21T08:00:00+00:00 |
| `20251122_141500_EMAIL-06191-eml` | email | [emails/2025-11/20251122_141500_EMAIL-06191.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251122_141500_EMAIL-06191.eml) | 2025-11-22T14:15:00+00:00 |
| `20251124_081500_EMAIL-06210-eml` | email | [emails/2025-11/20251124_081500_EMAIL-06210.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251124_081500_EMAIL-06210.eml) | 2025-11-24T08:15:00+00:00 |
| `20251126_161300_EMAIL-06233-eml` | email | [emails/2025-11/20251126_161300_EMAIL-06233.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251126_161300_EMAIL-06233.eml) | 2025-11-26T16:13:00+00:00 |
| `20251128_161300_EMAIL-06252-eml` | email | [emails/2025-11/20251128_161300_EMAIL-06252.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251128_161300_EMAIL-06252.eml) | 2025-11-28T16:13:00+00:00 |
| `20251130_145700_EMAIL-06268-eml` | email | [emails/2025-11/20251130_145700_EMAIL-06268.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251130_145700_EMAIL-06268.eml) | 2025-11-30T14:57:00+00:00 |
| `20251215_104800_EMAIL-06401-eml` | email | [emails/2025-12/20251215_104800_EMAIL-06401.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251215_104800_EMAIL-06401.eml) | 2025-12-15 |
| `20251217_105000_EMAIL-06418-eml` | email | [emails/2025-12/20251217_105000_EMAIL-06418.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251217_105000_EMAIL-06418.eml) | 2025-12-17T10:50:00+00:00 |
| `20251218_135000_EMAIL-06433-eml` | email | [emails/2025-12/20251218_135000_EMAIL-06433.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251218_135000_EMAIL-06433.eml) | 2025-12-18T13:50:00+00:00 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-25T20:04:11+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
