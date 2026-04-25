# context.unit.<!-- auto:unit_id -->EH-002<!-- /auto:unit_id -->.md

> Per-unit dossier (one file per Einheit). Holds everything specific to this unit:
> the unit itself, the active lease, the tenant(s), and all unit/tenant-specific operations.
> **Property-wide data lives in `context.property.md`** — see `parent_property_ref` below.

<!-- auto:meta -->
- last_built_at: `2026-04-25T20:52:19+00:00`
- build_hash: `engine-v2`
- engine_version: `0.2.0`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `unit`
- unit_id: `EH-002`
- property_id: `LIE-001`
- parent_property_ref: `context.property.LIE-001.md`
- owner_ref: `EIG-009`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit -->
- unit_id: `EH-002`
- label: WE 02
- haus_id: `HAUS-12`
- floor: 1. OG
- position: mitte
- typ: Wohnung
- area_sqm: 49.0
- rooms: 1.5
- mea_‰: 114
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
- lease_id: `LEASE-MIE-009`
- unit_ref: `EH-002`
- start_date: 2021-01-21 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-009)
- end_date: _(no data in source yet)_
- term_type: `unbefristet`
- cancellation_status: `by_tenant` (notice_date: 2025-08-20, move_out_date: —)
- rent_components: { kaltmiete: 724.0, betriebskosten_vorauszahlung: 140.0, total_warmmiete: 864.00 }
- payment_mode: Überweisung
- iban_payer: DE73100500009636057662 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-009)
- kaution: { amount: 2172.0 }
- usage: `residential`
- subletting: { current_status: `requested` }
- special_agreements: _(no data in source yet)_
<!-- /auto:lease -->

### 2.1 Tenants on this Lease
<!-- auto:tenants -->
| tenant_id | name | role | contact_email | contact_phone | comms_pref | gesamtschuldner |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-009` | Frau Marliese Hermann | haupt | marliese.hermann@posteo.de | 04367 136959 | email | — |
<!-- /auto:tenants -->

---

## 3. Operations (this unit / this tenant)

### 3.1 Open Tickets — Critical (overdue or due ≤7 days)
<!-- auto:tickets.critical -->
| ticket_id | type | title | deadline | status | assignee |
| --- | --- | --- | --- | --- | --- |
| `TKT-74588164` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-1d552ddf` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-14fbf107` | schimmel | Re: Schimmel im Schlafzimmer | — | open | — |
| `TKT-23fd05f2` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-49c90752` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-750caddf` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-7669c372` | wasserschaden | Wasserschaden Bad | — | open | — |
<!-- /auto:tickets.critical -->

### 3.2 Open Tickets — Aggregate
<!-- auto:tickets.aggregate -->
- total_open: `29`
- by_type: { abfluss: `7`, fenster: `10`, schimmel: `4`, schluessel: `5`, wasserschaden: `3` }
- live source: `db.tickets WHERE unit_id=EH-002 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren

<!-- auto:dunning.summary -->[Routine] Mieter MIE-009 ist seit vier Monaten im Verzug; offener Betrag 3.456,00 EUR zzgl. 44,27 EUR Verzugszinsen, letzte Zahlung 2025-12-03 [(bank)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv#TX-01581). Vertraglich geschuldet sind monatlich 864,00 EUR (Kaltmiete 724,00 EUR + NK 140,00 EUR) [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-009). Verzug nach § 286 BGB festgestellt, Verzugszinsen § 288 I BGB; Mahnstufe 1 erreicht, nächster Schritt: 2. Mahnung nach 14 Tagen.<!-- /auto:dunning.summary -->

#### Per claim
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-009` | — | 1 | 3456.00 EUR | 2025-12-03 | — | — |
- live balance pointer: `db.tenant_balance.tenant_id=MIE-009`
<!-- /auto:dunning -->

### 3.4 Active Reductions / Deferrals (§ 536 BGB)
<!-- auto:reductions -->
- date_raised: 2024-04-03
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-03-02
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
| Mieterwechsel | 2025-08-20 | Kündigung erhalten | Verwaltung | TBD | Übergabe-Termin offen |
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
| `TH-45d495` | Frage zur Nebenkostenabrechnung | 2025-12-16 | `MIE-009` | active | 141 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251216_155800_EMAIL-06415.eml) |
| `TH-e72611` | Verstopfter Abfluss | 2025-12-30 | `MIE-009` | active | 117 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251230_144800_EMAIL-06532.eml) |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `kontoauszug_2024_2025-csv` | bank | [bank/kontoauszug_2024_2025.csv](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv) | 2026-04-25 |
| `20240201_103600_EMAIL-00261-eml` | email | [emails/2024-02/20240201_103600_EMAIL-00261.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240201_103600_EMAIL-00261.eml) | 2024-02-01T10:36:00+00:00 |
| `20240213_153700_EMAIL-00374-eml` | email | [emails/2024-02/20240213_153700_EMAIL-00374.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240213_153700_EMAIL-00374.eml) | 2024-02-13T15:37:00+00:00 |
| `20240225_114200_EMAIL-00465-eml` | email | [emails/2024-02/20240225_114200_EMAIL-00465.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240225_114200_EMAIL-00465.eml) | 2024-02-25T11:42:00+00:00 |
| `20240226_173400_EMAIL-00481-eml` | email | [emails/2024-02/20240226_173400_EMAIL-00481.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240226_173400_EMAIL-00481.eml) | 2024-02-26T17:34:00+00:00 |
| `20240306_161700_EMAIL-00566-eml` | email | [emails/2024-03/20240306_161700_EMAIL-00566.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240306_161700_EMAIL-00566.eml) | 2024-03-06T16:17:00+00:00 |
| `20240307_021700_EMAIL-00569-eml` | email | [emails/2024-03/20240307_021700_EMAIL-00569.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240307_021700_EMAIL-00569.eml) | 2024-03-07T02:17:00+00:00 |
| `20240307_113600_EMAIL-00575-eml` | email | [emails/2024-03/20240307_113600_EMAIL-00575.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240307_113600_EMAIL-00575.eml) | 2024-03-07T11:36:00+00:00 |
| `20240308_152400_EMAIL-00588-eml` | email | [emails/2024-03/20240308_152400_EMAIL-00588.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240308_152400_EMAIL-00588.eml) | 2024-03-08T15:24:00+00:00 |
| `20240309_103600_EMAIL-00593-eml` | email | [emails/2024-03/20240309_103600_EMAIL-00593.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240309_103600_EMAIL-00593.eml) | 2024-03-09T10:36:00+00:00 |
| `20240321_175300_EMAIL-00701-eml` | email | [emails/2024-03/20240321_175300_EMAIL-00701.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240321_175300_EMAIL-00701.eml) | 2024-03-21T17:53:00+00:00 |
| `20240403_123900_EMAIL-00816-eml` | email | [emails/2024-04/20240403_123900_EMAIL-00816.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240403_123900_EMAIL-00816.eml) | 2024-04-03T12:39:00+00:00 |
| `20240420_123000_EMAIL-00998-eml` | email | [emails/2024-04/20240420_123000_EMAIL-00998.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240420_123000_EMAIL-00998.eml) | 2024-04-20T12:30:00+00:00 |
| `20240606_112700_EMAIL-01417-eml` | email | [emails/2024-06/20240606_112700_EMAIL-01417.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240606_112700_EMAIL-01417.eml) | 2024-06-06T11:27:00+00:00 |
| `20240620_122600_EMAIL-01549-eml` | email | [emails/2024-06/20240620_122600_EMAIL-01549.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240620_122600_EMAIL-01549.eml) | 2024-06-20T12:26:00+00:00 |
| `20240708_135300_EMAIL-01696-eml` | email | [emails/2024-07/20240708_135300_EMAIL-01696.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240708_135300_EMAIL-01696.eml) | 2024-07-08T13:53:00+00:00 |
| `20240709_205300_EMAIL-01716-eml` | email | [emails/2024-07/20240709_205300_EMAIL-01716.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240709_205300_EMAIL-01716.eml) | 2024-07-09T20:53:00+00:00 |
| `20240711_171400_EMAIL-01735-eml` | email | [emails/2024-07/20240711_171400_EMAIL-01735.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240711_171400_EMAIL-01735.eml) | 2024-07-11T17:14:00+00:00 |
| `20240818_181500_EMAIL-02084-eml` | email | [emails/2024-08/20240818_181500_EMAIL-02084.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240818_181500_EMAIL-02084.eml) | 2024-08-18T18:15:00+00:00 |
| `20240819_112300_EMAIL-02089-eml` | email | [emails/2024-08/20240819_112300_EMAIL-02089.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240819_112300_EMAIL-02089.eml) | 2024-08-19T11:23:00+00:00 |
| `20240911_143400_EMAIL-02317-eml` | email | [emails/2024-09/20240911_143400_EMAIL-02317.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240911_143400_EMAIL-02317.eml) | 2024-09-11T14:34:00+00:00 |
| `20240914_141400_EMAIL-02352-eml` | email | [emails/2024-09/20240914_141400_EMAIL-02352.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240914_141400_EMAIL-02352.eml) | 2024-09-14T14:14:00+00:00 |
| `20240927_102600_EMAIL-02457-eml` | email | [emails/2024-09/20240927_102600_EMAIL-02457.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240927_102600_EMAIL-02457.eml) | 2024-09-27T10:26:00+00:00 |
| `20240927_125700_EMAIL-02458-eml` | email | [emails/2024-09/20240927_125700_EMAIL-02458.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240927_125700_EMAIL-02458.eml) | 2024-09-27T12:57:00+00:00 |
| `20240928_172600_EMAIL-02476-eml` | email | [emails/2024-09/20240928_172600_EMAIL-02476.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240928_172600_EMAIL-02476.eml) | 2024-09-28T17:26:00+00:00 |
| `20241001_055700_EMAIL-02487-eml` | email | [emails/2024-10/20241001_055700_EMAIL-02487.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241001_055700_EMAIL-02487.eml) | 2024-10-01T05:57:00+00:00 |
| `20241017_164700_EMAIL-02638-eml` | email | [emails/2024-10/20241017_164700_EMAIL-02638.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241017_164700_EMAIL-02638.eml) | 2024-10-17T16:47:00+00:00 |
| `20241018_024700_EMAIL-02641-eml` | email | [emails/2024-10/20241018_024700_EMAIL-02641.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241018_024700_EMAIL-02641.eml) | 2024-10-18T02:47:00+00:00 |
| `20241022_105000_EMAIL-02679-eml` | email | [emails/2024-10/20241022_105000_EMAIL-02679.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241022_105000_EMAIL-02679.eml) | 2024-10-22T10:50:00+00:00 |
| `20241118_124400_EMAIL-02945-eml` | email | [emails/2024-11/20241118_124400_EMAIL-02945.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241118_124400_EMAIL-02945.eml) | 2024-11-18T12:44:00+00:00 |
| `20241126_110300_EMAIL-03011-eml` | email | [emails/2024-11/20241126_110300_EMAIL-03011.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241126_110300_EMAIL-03011.eml) | 2024-11-26T11:03:00+00:00 |
| `20241126_200300_EMAIL-03019-eml` | email | [emails/2024-11/20241126_200300_EMAIL-03019.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241126_200300_EMAIL-03019.eml) | 2024-11-26T20:03:00+00:00 |
| `20241206_104700_EMAIL-03102-eml` | email | [emails/2024-12/20241206_104700_EMAIL-03102.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241206_104700_EMAIL-03102.eml) | 2024-12-06T10:47:00+00:00 |
| `20241209_094700_EMAIL-03130-eml` | email | [emails/2024-12/20241209_094700_EMAIL-03130.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241209_094700_EMAIL-03130.eml) | 2024-12-09T09:47:00+00:00 |
| `20241216_151800_EMAIL-03191-eml` | email | [emails/2024-12/20241216_151800_EMAIL-03191.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241216_151800_EMAIL-03191.eml) | 2024-12-16T15:18:00+00:00 |
| `20250104_162000_EMAIL-03377-eml` | email | [emails/2025-01/20250104_162000_EMAIL-03377.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250104_162000_EMAIL-03377.eml) | 2025-01-04T16:20:00+00:00 |
| `20250114_142000_EMAIL-03478-eml` | email | [emails/2025-01/20250114_142000_EMAIL-03478.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250114_142000_EMAIL-03478.eml) | 2025-01-14T14:20:00+00:00 |
| `20250119_181100_EMAIL-03522-eml` | email | [emails/2025-01/20250119_181100_EMAIL-03522.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250119_181100_EMAIL-03522.eml) | 2025-01-19T18:11:00+00:00 |
| `20250128_143300_EMAIL-03583-eml` | email | [emails/2025-01/20250128_143300_EMAIL-03583.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250128_143300_EMAIL-03583.eml) | 2025-01-28T14:33:00+00:00 |
| `20250128_233300_EMAIL-03590-eml` | email | [emails/2025-01/20250128_233300_EMAIL-03590.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250128_233300_EMAIL-03590.eml) | 2025-01-28T23:33:00+00:00 |
| `20250204_233300_EMAIL-03644-eml` | email | [emails/2025-02/20250204_233300_EMAIL-03644.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250204_233300_EMAIL-03644.eml) | 2025-02-04T23:33:00+00:00 |
| `20250220_103700_EMAIL-03789-eml` | email | [emails/2025-02/20250220_103700_EMAIL-03789.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250220_103700_EMAIL-03789.eml) | 2025-02-20T10:37:00+00:00 |
| `20250224_135000_EMAIL-03835-eml` | email | [emails/2025-02/20250224_135000_EMAIL-03835.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250224_135000_EMAIL-03835.eml) | 2025-02-24T13:50:00+00:00 |
| `20250225_005000_EMAIL-03840-eml` | email | [emails/2025-02/20250225_005000_EMAIL-03840.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250225_005000_EMAIL-03840.eml) | 2025-02-25T00:50:00+00:00 |
| `20250302_154200_EMAIL-03902-eml` | email | [emails/2025-03/20250302_154200_EMAIL-03902.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250302_154200_EMAIL-03902.eml) | 2025-03-02T15:42:00+00:00 |
| `20250306_005000_EMAIL-03928-eml` | email | [emails/2025-03/20250306_005000_EMAIL-03928.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250306_005000_EMAIL-03928.eml) | 2025-03-06T00:50:00+00:00 |
| `20250317_110000_EMAIL-04039-eml` | email | [emails/2025-03/20250317_110000_EMAIL-04039.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250317_110000_EMAIL-04039.eml) | 2025-03-17T11:00:00+00:00 |
| `20250323_103500_EMAIL-04101-eml` | email | [emails/2025-03/20250323_103500_EMAIL-04101.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250323_103500_EMAIL-04101.eml) | 2025-03-23T10:35:00+00:00 |
| `20250408_145100_EMAIL-04241-eml` | email | [emails/2025-04/20250408_145100_EMAIL-04241.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250408_145100_EMAIL-04241.eml) | 2025-04-08T14:51:00+00:00 |
| `20250415_083300_EMAIL-04295-eml` | email | [emails/2025-04/20250415_083300_EMAIL-04295.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250415_083300_EMAIL-04295.eml) | 2025-04-15T08:33:00+00:00 |
| `20250416_103300_EMAIL-04304-eml` | email | [emails/2025-04/20250416_103300_EMAIL-04304.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250416_103300_EMAIL-04304.eml) | 2025-04-16T10:33:00+00:00 |
| `20250424_161300_EMAIL-04367-eml` | email | [emails/2025-04/20250424_161300_EMAIL-04367.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250424_161300_EMAIL-04367.eml) | 2025-04-24T16:13:00+00:00 |
| `20250504_095000_EMAIL-04430-eml` | email | [emails/2025-05/20250504_095000_EMAIL-04430.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250504_095000_EMAIL-04430.eml) | 2025-05-04T09:50:00+00:00 |
| `20250510_112800_EMAIL-04471-eml` | email | [emails/2025-05/20250510_112800_EMAIL-04471.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250510_112800_EMAIL-04471.eml) | 2025-05-10T11:28:00+00:00 |
| `20250511_202800_EMAIL-04491-eml` | email | [emails/2025-05/20250511_202800_EMAIL-04491.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250511_202800_EMAIL-04491.eml) | 2025-05-11T20:28:00+00:00 |
| `20250528_152600_EMAIL-04648-eml` | email | [emails/2025-05/20250528_152600_EMAIL-04648.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250528_152600_EMAIL-04648.eml) | 2025-05-28T15:26:00+00:00 |
| `20250529_162600_EMAIL-04658-eml` | email | [emails/2025-05/20250529_162600_EMAIL-04658.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250529_162600_EMAIL-04658.eml) | 2025-05-29T16:26:00+00:00 |
| `20250531_162600_EMAIL-04674-eml` | email | [emails/2025-05/20250531_162600_EMAIL-04674.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250531_162600_EMAIL-04674.eml) | 2025-05-31T16:26:00+00:00 |
| `20250611_105100_EMAIL-04748-eml` | email | [emails/2025-06/20250611_105100_EMAIL-04748.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250611_105100_EMAIL-04748.eml) | 2025-06-11T10:51:00+00:00 |
| `20250627_113000_EMAIL-04887-eml` | email | [emails/2025-06/20250627_113000_EMAIL-04887.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250627_113000_EMAIL-04887.eml) | 2025-06-27T11:30:00+00:00 |
| `20250628_144000_EMAIL-04894-eml` | email | [emails/2025-06/20250628_144000_EMAIL-04894.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250628_144000_EMAIL-04894.eml) | 2025-06-28T14:40:00+00:00 |
| `20250702_091200_EMAIL-04928-eml` | email | [emails/2025-07/20250702_091200_EMAIL-04928.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250702_091200_EMAIL-04928.eml) | 2025-07-02T09:12:00+00:00 |
| `20250711_104300_EMAIL-05000-eml` | email | [emails/2025-07/20250711_104300_EMAIL-05000.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250711_104300_EMAIL-05000.eml) | 2025-07-11T10:43:00+00:00 |
| `20250814_103900_EMAIL-05289-eml` | email | [emails/2025-08/20250814_103900_EMAIL-05289.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250814_103900_EMAIL-05289.eml) | 2025-08-14T10:39:00+00:00 |
| `20250817_161800_EMAIL-05332-eml` | email | [emails/2025-08/20250817_161800_EMAIL-05332.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250817_161800_EMAIL-05332.eml) | 2025-08-17T16:18:00+00:00 |
| `20250820_141700_EMAIL-05358-eml` | email | [emails/2025-08/20250820_141700_EMAIL-05358.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250820_141700_EMAIL-05358.eml) | 2025-08-20T14:17:00+00:00 |
| `20250828_100100_EMAIL-05426-eml` | email | [emails/2025-08/20250828_100100_EMAIL-05426.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250828_100100_EMAIL-05426.eml) | 2025-08-28T10:01:00+00:00 |
| `20250830_090100_EMAIL-05453-eml` | email | [emails/2025-08/20250830_090100_EMAIL-05453.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250830_090100_EMAIL-05453.eml) | 2025-08-30T09:01:00+00:00 |
| `20250906_132700_EMAIL-05542-eml` | email | [emails/2025-09/20250906_132700_EMAIL-05542.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250906_132700_EMAIL-05542.eml) | 2025-09-06T13:27:00+00:00 |
| `20250909_150100_EMAIL-05584-eml` | email | [emails/2025-09/20250909_150100_EMAIL-05584.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250909_150100_EMAIL-05584.eml) | 2025-09-09T15:01:00+00:00 |
| `20250915_162900_EMAIL-05631-eml` | email | [emails/2025-09/20250915_162900_EMAIL-05631.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250915_162900_EMAIL-05631.eml) | 2025-09-15T16:29:00+00:00 |
| `20250924_100100_EMAIL-05697-eml` | email | [emails/2025-09/20250924_100100_EMAIL-05697.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250924_100100_EMAIL-05697.eml) | 2025-09-24T10:01:00+00:00 |
| `20251006_140500_EMAIL-05794-eml` | email | [emails/2025-10/20251006_140500_EMAIL-05794.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251006_140500_EMAIL-05794.eml) | 2025-10-06T14:05:00+00:00 |
| `20251016_102500_EMAIL-05892-eml` | email | [emails/2025-10/20251016_102500_EMAIL-05892.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251016_102500_EMAIL-05892.eml) | 2025-10-16T10:25:00+00:00 |
| `20251022_142100_EMAIL-05937-eml` | email | [emails/2025-10/20251022_142100_EMAIL-05937.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251022_142100_EMAIL-05937.eml) | 2025-10-22T14:21:00+00:00 |
| `20251102_123200_EMAIL-06019-eml` | email | [emails/2025-11/20251102_123200_EMAIL-06019.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251102_123200_EMAIL-06019.eml) | 2025-11-02T12:32:00+00:00 |
| `20251104_120100_EMAIL-06040-eml` | email | [emails/2025-11/20251104_120100_EMAIL-06040.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251104_120100_EMAIL-06040.eml) | 2025-11-04T12:01:00+00:00 |
| `20251109_115600_EMAIL-06084-eml` | email | [emails/2025-11/20251109_115600_EMAIL-06084.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251109_115600_EMAIL-06084.eml) | 2025-11-09T11:56:00+00:00 |
| `20251205_090500_EMAIL-06303-eml` | email | [emails/2025-12/20251205_090500_EMAIL-06303.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251205_090500_EMAIL-06303.eml) | 2025-12-05T09:05:00+00:00 |
| `20251206_200500_EMAIL-06316-eml` | email | [emails/2025-12/20251206_200500_EMAIL-06316.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251206_200500_EMAIL-06316.eml) | 2025-12-06T20:05:00+00:00 |
| `20251216_155800_EMAIL-06415-eml` | email | [emails/2025-12/20251216_155800_EMAIL-06415.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251216_155800_EMAIL-06415.eml) | 2025-12-16 |
| `20251230_144800_EMAIL-06532-eml` | email | [emails/2025-12/20251230_144800_EMAIL-06532.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251230_144800_EMAIL-06532.eml) | 2025-12-30 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-25T20:52:09+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
