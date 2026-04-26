# context.unit.<!-- auto:unit_id -->EH-020<!-- /auto:unit_id -->.md

> Per-unit dossier (one file per Einheit). Holds everything specific to this unit:
> the unit itself, the active lease, the tenant(s), and all unit/tenant-specific operations.
> **Property-wide data lives in `context.property.md`** — see `parent_property_ref` below.

<!-- auto:meta -->
- last_built_at: `2026-04-26T09:32:31+00:00`
- build_hash: `engine-v2`
- engine_version: `0.2.0`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `unit`
- unit_id: `EH-020`
- property_id: `LIE-001`
- parent_property_ref: `context.property.LIE-001.md`
- owner_ref: `EIG-026`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit.summary -->[Administrative] Einheit EH-020 (WE 20, 1,5-Zimmer-Wohnung, 46 qm, 1. OG mitte) [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#einheit/EH-020): Hausgeldzahlung 7,58 EUR von Silja Henschel am 2025-11-02 verbucht [(bank)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv#TX-00045). Miteigentumsanteil 107/10.000, Verwendungszweck Hausgeld 11/2025. Verkaufsabsicht dokumentiert 2024-04-19; Mieterwechsel-Korrespondenz 2025-08-12 — Status aktualisieren und Eigentümerwechsel ggf. in Stammdaten konsolidieren.<!-- /auto:unit.summary -->

<!-- auto:unit -->
- unit_id: `EH-020`
- label: WE 20
- haus_id: `HAUS-14`
- floor: 1. OG
- position: mitte
- typ: Wohnung
- area_sqm: 46.0
- rooms: 1.5
- mea_‰: 107
- equipment: _(no data in source yet)_
- media_supply: _(no data in source yet)_
- key_inventory: _(no data in source yet)_
- meters: _(no data in source yet)_
- occupancy_status: `own-use`
- nk_keys: _(no data in source yet)_
<!-- /auto:unit -->

---

## 2. Lease (Mietverhältnis, voll)
<!-- auto:lease.summary -->_no issue_<!-- /auto:lease.summary -->

<!-- auto:lease -->_(no data in source yet)_<!-- /auto:lease -->

### 2.1 Tenants on this Lease
<!-- auto:tenants.summary -->_no issue_<!-- /auto:tenants.summary -->

<!-- auto:tenants -->
| tenant_id | name | role | contact_email | contact_phone | comms_pref | gesamtschuldner |
| --- | --- | --- | --- | --- | --- | --- |
_(no data in source yet)_
<!-- /auto:tenants -->

---

## 3. Operations (this unit / this tenant)

### 3.1 Open Tickets — Critical (overdue or due ≤7 days)
<!-- auto:tickets.critical.summary -->_no issue_<!-- /auto:tickets.critical.summary -->

<!-- auto:tickets.critical -->
| ticket_id | type | title | deadline | status | assignee |
| --- | --- | --- | --- | --- | --- |
_(no data in source yet)_
<!-- /auto:tickets.critical -->

### 3.2 Open Tickets — Aggregate
<!-- auto:tickets.aggregate.summary -->_no issue_<!-- /auto:tickets.aggregate.summary -->

<!-- auto:tickets.aggregate -->
- total_open: `0`
- by_type: { — }
- live source: `db.tickets WHERE unit_id=EH-020 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren

<!-- auto:dunning.summary -->_no issue_<!-- /auto:dunning.summary -->

#### Per claim
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
_(no data in source yet)_
- live balance pointer: `db.tenant_balance.tenant_id=EH-020`
<!-- /auto:dunning -->

### 3.4 Active Reductions / Deferrals (§ 536 BGB)
<!-- auto:reductions.summary -->_no issue_<!-- /auto:reductions.summary -->

<!-- auto:reductions -->_(no data in source yet)_<!-- /auto:reductions -->

### 3.5 Latest Übergabeprotokoll
<!-- auto:handover.summary -->_no issue_<!-- /auto:handover.summary -->

<!-- auto:handover -->_(no data in source yet)_<!-- /auto:handover -->

### 3.6 Recurring Process State (this unit, in-flight)
<!-- auto:recurring.summary -->_no issue_<!-- /auto:recurring.summary -->

<!-- auto:recurring -->
| process_type | started | current_step | owner | eta | blockers |
| --- | --- | --- | --- | --- | --- |
_(no data in source yet)_
<!-- /auto:recurring -->

### 3.7 Vermietungs-Pipeline *(if vacant)*
<!-- auto:vermietung.summary -->_no issue_<!-- /auto:vermietung.summary -->

<!-- auto:vermietung -->_Not yet activated. Triggers when occupancy_status flips to vacant after move-out._<!-- /auto:vermietung -->

---

## 4. Decisions & History (this unit / this tenant)

### 4.1 Tenant Special Agreements
<!-- auto:tenant-agreements.summary -->_no issue_<!-- /auto:tenant-agreements.summary -->

<!-- auto:tenant-agreements -->
| date | type | one-line | doc_ref |
| --- | --- | --- | --- |
_(no data in source yet)_
<!-- /auto:tenant-agreements -->

### 4.2 Modernisierungs-Maßnahmen (this unit)
<!-- auto:modernization-unit.summary -->_no issue_<!-- /auto:modernization-unit.summary -->

<!-- auto:modernization-unit -->
| date_completed | scope | umlage_per_year | rent_increase_per_month | tenant_opted_out |
| --- | --- | --- | --- | --- |
_(no data in source yet)_
<!-- /auto:modernization-unit -->

### 4.3 Sticky Communication Threads (this tenant)
<!-- auto:sticky-threads.summary -->[Routine] Einheit EH-020 (WE 51): Mieter berichtet seit 22.12.2025, dass Mietkontoauszüge seit drei Monaten nicht zugestellt werden [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251222_143100_EMAIL-06469.eml). Vertraglich ist die regelmäßige Übermittlung von Nebenkostenabrechnungen geschuldet; § 256 III BGB verpflichtet zur Abrechnung spätestens zum Ende des folgenden Jahres, verzögerter Versand kann zur Verjährungshemmung führen. Thread seit 2024-01-01 aktiv mit 189 Nachrichten (zuletzt 2025-12-22); letzte Auszugszustellung prüfen und fehlendes Material nach sachbearbeiter@huber-partner (Januar 2026) nachversenden.<!-- /auto:sticky-threads.summary -->

<!-- auto:sticky-threads -->
| thread_id | subject | last_msg_date | parties | status | one-line outcome | pointer |
| --- | --- | --- | --- | --- | --- | --- |
| `TH-871352` | SEV - Monatsauszug | 2025-12-22 | `EH-020` | active | 189 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251222_143100_EMAIL-06469.eml) |
| `TH-6f2c58` | Mieterwechsel in WE 20 | 2025-08-12 | `EH-020` | active | 4 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250812_015300_EMAIL-05263.eml) |
| `TH-0d62db` | Verkaufsabsicht WE 20 | 2024-04-19 | `EH-020` | active | 3 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240419_230300_EMAIL-00995.eml) |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance.summary -->_no issue_<!-- /auto:provenance.summary -->

<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `kontoauszug_2024_2025-csv` | bank | [bank/kontoauszug_2024_2025.csv](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv) | 2025-11-02 |
| `20240209_130200_EMAIL-00341-eml` | email | [emails/2024-02/20240209_130200_EMAIL-00341.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240209_130200_EMAIL-00341.eml) | 2024-02-09T13:02:00+00:00 |
| `20240417_025000_EMAIL-00965-eml` | email | [emails/2024-04/20240417_025000_EMAIL-00965.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240417_025000_EMAIL-00965.eml) | 2024-04-17T02:50:00+00:00 |
| `20240419_230300_EMAIL-00995-eml` | email | [emails/2024-04/20240419_230300_EMAIL-00995.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240419_230300_EMAIL-00995.eml) | 2024-04-19T23:03:00+00:00 |
| `20240905_102000_EMAIL-02250-eml` | email | [emails/2024-09/20240905_102000_EMAIL-02250.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240905_102000_EMAIL-02250.eml) | 2024-09-05T10:20:00+00:00 |
| `20241111_145700_EMAIL-02873-eml` | email | [emails/2024-11/20241111_145700_EMAIL-02873.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241111_145700_EMAIL-02873.eml) | 2024-11-11T14:57:00+00:00 |
| `20250328_031800_EMAIL-04139-eml` | email | [emails/2025-03/20250328_031800_EMAIL-04139.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250328_031800_EMAIL-04139.eml) | 2025-03-28T03:18:00+00:00 |
| `20250407_104100_EMAIL-04230-eml` | email | [emails/2025-04/20250407_104100_EMAIL-04230.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250407_104100_EMAIL-04230.eml) | 2025-04-07T10:41:00+00:00 |
| `20250812_015300_EMAIL-05263-eml` | email | [emails/2025-08/20250812_015300_EMAIL-05263.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250812_015300_EMAIL-05263.eml) | 2025-08-12T01:53:00+00:00 |
| `20251222_143100_EMAIL-06469-eml` | email | [emails/2025-12/20251222_143100_EMAIL-06469.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251222_143100_EMAIL-06469.eml) | 2025-12-22 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-26T09:26:19+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
