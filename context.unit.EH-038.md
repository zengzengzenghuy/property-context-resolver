# context.unit.<!-- auto:unit_id -->EH-038<!-- /auto:unit_id -->.md

> Per-unit dossier (one file per Einheit). Holds everything specific to this unit:
> the unit itself, the active lease, the tenant(s), and all unit/tenant-specific operations.
> **Property-wide data lives in `context.property.md`** — see `parent_property_ref` below.

<!-- auto:meta -->
- last_built_at: `2026-04-26T09:39:43+00:00`
- build_hash: `engine-v2`
- engine_version: `0.2.0`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `unit`
- unit_id: `EH-038`
- property_id: `LIE-001`
- parent_property_ref: `context.property.LIE-001.md`
- owner_ref: `EIG-009`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit.summary -->_no issue_<!-- /auto:unit.summary -->

<!-- auto:unit -->
- unit_id: `EH-038`
- label: TG 38
- haus_id: `HAUS-14`
- floor: Tiefgarage
- position: _(no data in source yet)_
- typ: Tiefgarage
- area_sqm: 12.5
- rooms: _(no data in source yet)_
- mea_‰: 23
- equipment: _(no data in source yet)_
- media_supply: _(no data in source yet)_
- key_inventory: _(no data in source yet)_
- meters: _(no data in source yet)_
- occupancy_status: `vacant`
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
- live source: `db.tickets WHERE unit_id=EH-038 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren

<!-- auto:dunning.summary -->_no issue_<!-- /auto:dunning.summary -->

#### Per claim
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
_(no data in source yet)_
- live balance pointer: `db.tenant_balance.tenant_id=EH-038`
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

<!-- auto:vermietung -->
- inserate_url: _(no data in source yet)_
- days_on_market: _(no data in source yet)_
- asking_kaltmiete: _(no data in source yet)_
- prospects_count: _(no data in source yet)_
- scheduled_viewings_count: _(no data in source yet)_
- applications_received_count: _(no data in source yet)_
- shortlist: _(no data in source yet)_
<!-- /auto:vermietung -->

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
<!-- auto:sticky-threads.summary -->[Administrative] Eigentümer EH-038 teilt Verkaufsabsicht mit (31.05.2025) und fordert aktuelle Hausgeldbescheinigung sowie ETV-Protokolle an [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250531_082500_EMAIL-04667.eml). Thread seit 07.04.2024 aktiv, 4 Nachrichten; letzte Aktivität 31.05.2025. Gemäß § 10 IV WEG und § 47 a GBO ist Verwaltung verpflichtet, beglaubigte Auszüge aus Verwaltungsakten sowie Nachweise fehlender Rückstände innerhalb angemessener Frist bereitzustellen.<!-- /auto:sticky-threads.summary -->

<!-- auto:sticky-threads -->
| thread_id | subject | last_msg_date | parties | status | one-line outcome | pointer |
| --- | --- | --- | --- | --- | --- | --- |
| `TH-816859` | Verkaufsabsicht TG 38 | 2025-05-31 | `EH-038` | active | 4 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250531_082500_EMAIL-04667.eml) |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance.summary -->[Administrative] Einheit EH-038 (TG 38, Tiefgarage, 12,5 qm, Miteigentumsanteil 23/1000) ist seit 2024-04-07 Gegenstand einer aktiven Verkaufsabsicht-Kommunikation [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#einheit/EH-038) mit vier dokumentierten Meldungen; letzte Aktivität 2025-05-31 [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250531_082500_EMAIL-04667.eml). Verkaufsabsicht muss nach § 573 Abs. 2 BGB dem Makler/Käufer offenbart werden; parallele Mitteilungspflichten gegenüber der Hausverwaltung und WEG-Gemeinschaft nach WEG-Gesetz sind zu prüfen. Zu klären: Verkaufsstand, etwaige Notwendigkeit einer WEG-Zustimmung bei Eigentümerwechsel und Compliance mit Modernisierungszustimmung (vgl. 2024-12-08 Korrespondenz).<!-- /auto:provenance.summary -->

<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `20240408_001600_EMAIL-00863-eml` | email | [emails/2024-04/20240408_001600_EMAIL-00863.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240408_001600_EMAIL-00863.eml) | 2024-04-08T00:16:00+00:00 |
| `20241208_045500_EMAIL-03119-eml` | email | [emails/2024-12/20241208_045500_EMAIL-03119.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241208_045500_EMAIL-03119.eml) | 2024-12-08T04:55:00+00:00 |
| `20250531_082500_EMAIL-04667-eml` | email | [emails/2025-05/20250531_082500_EMAIL-04667.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250531_082500_EMAIL-04667.eml) | 2025-05-31 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-26T09:26:19+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
