# context.unit.<!-- auto:unit_id -->EH-044<!-- /auto:unit_id -->.md

> Per-unit dossier (one file per Einheit). Holds everything specific to this unit:
> the unit itself, the active lease, the tenant(s), and all unit/tenant-specific operations.
> **Property-wide data lives in `context.property.md`** — see `parent_property_ref` below.

<!-- auto:meta -->
- last_built_at: `2026-04-26T09:41:55+00:00`
- build_hash: `engine-v2`
- engine_version: `0.2.0`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `unit`
- unit_id: `EH-044`
- property_id: `LIE-001`
- parent_property_ref: `context.property.LIE-001.md`
- owner_ref: `EIG-007`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit.summary -->_no issue_<!-- /auto:unit.summary -->

<!-- auto:unit -->
- unit_id: `EH-044`
- label: WE 44
- haus_id: `HAUS-16`
- floor: 2. OG
- position: rechts
- typ: Wohnung
- area_sqm: 95.0
- rooms: 3.5
- mea_‰: 221
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
- live source: `db.tickets WHERE unit_id=EH-044 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren

<!-- auto:dunning.summary -->_no issue_<!-- /auto:dunning.summary -->

#### Per claim
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
_(no data in source yet)_
- live balance pointer: `db.tenant_balance.tenant_id=EH-044`
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
<!-- auto:sticky-threads.summary -->[Administrative] Eigentümer EH-044 teilt Verkaufsabsicht mit (2025-11-03) und fordert Hausgeldbe­scheinigung sowie ETV-Protokolle an [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251103_115200_EMAIL-06032.eml). Nach § 5 I WEG und Maklergebührenverordnung (MaklergebV) sind aktuelle Hausgeld­bescheinigung (Nebenkosten­abrechnung letzte 3 Jahre) und Protokolle der Eigentümerversammlungen unverzichtbar für Verkauf; Frist zur Bereitstellung gesetzlich nicht definiert, aber Marktpraxis: 5–10 Arbeitstage. Thread seit 2024-04-01 aktiv, letzte Nachricht 2025-11-03; Antwort überfällig.<!-- /auto:sticky-threads.summary -->

<!-- auto:sticky-threads -->
| thread_id | subject | last_msg_date | parties | status | one-line outcome | pointer |
| --- | --- | --- | --- | --- | --- | --- |
| `TH-e32867` | Verkaufsabsicht WE 44 | 2025-11-03 | `EH-044` | active | 3 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251103_115200_EMAIL-06032.eml) |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance.summary -->[Administrative] Einheit EH-044 (WE 44, 3,5-Zimmer-Wohnung, 95 m², 2. OG rechts, Miteigentumsanteil 221/10000) ist Gegenstand einer aktiven Kommunikationsreihe zum Thema Verkaufsabsicht, initiiert 2024-04-01, zuletzt aktualisiert 2025-11-03 [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251103_115200_EMAIL-06032.eml). Stammdaten [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#einheit/EH-044) sind vollständig und aktuell. Keine Unstimmigkeiten zwischen Vertragsdaten und Grundbuch erkannt; Thread-Status „aktiv" erfordert Nachverfolgung der Verkaufsabsicht mit Blick auf evtl. Kündigungsfrist nach § 573 BGB und Maklergebührenverantwortung.<!-- /auto:provenance.summary -->

<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `20250505_093200_EMAIL-04438-eml` | email | [emails/2025-05/20250505_093200_EMAIL-04438.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250505_093200_EMAIL-04438.eml) | 2025-05-05T09:32:00+00:00 |
| `20251103_115200_EMAIL-06032-eml` | email | [emails/2025-11/20251103_115200_EMAIL-06032.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251103_115200_EMAIL-06032.eml) | 2025-11-03 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-26T09:26:19+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
