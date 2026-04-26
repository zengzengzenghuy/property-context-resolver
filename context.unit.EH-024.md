# context.unit.<!-- auto:unit_id -->EH-024<!-- /auto:unit_id -->.md

> Per-unit dossier (one file per Einheit). Holds everything specific to this unit:
> the unit itself, the active lease, the tenant(s), and all unit/tenant-specific operations.
> **Property-wide data lives in `context.property.md`** — see `parent_property_ref` below.

<!-- auto:meta -->
- last_built_at: `2026-04-26T09:34:14+00:00`
- build_hash: `engine-v2`
- engine_version: `0.2.0`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `unit`
- unit_id: `EH-024`
- property_id: `LIE-001`
- parent_property_ref: `context.property.LIE-001.md`
- owner_ref: `EIG-005`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit.summary -->_no issue_<!-- /auto:unit.summary -->

<!-- auto:unit -->
- unit_id: `EH-024`
- label: WE 24
- haus_id: `HAUS-14`
- floor: 2. OG
- position: rechts
- typ: Wohnung
- area_sqm: 115.0
- rooms: 4.5
- mea_‰: 267
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
- live source: `db.tickets WHERE unit_id=EH-024 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren

<!-- auto:dunning.summary -->_no issue_<!-- /auto:dunning.summary -->

#### Per claim
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
_(no data in source yet)_
- live balance pointer: `db.tenant_balance.tenant_id=EH-024`
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
<!-- auto:sticky-threads.summary -->[Routine] Mieterwechsel WE 24 in aktiver Nachverfolgung seit 2024-02-10 (7 Nachrichten, letzte vom 2024-11-30); Freizugstermin vertraglich 2025-01-20 [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241130_075400_EMAIL-03048.eml). Verwaltung hat Handwerkerbeauftragung für Übergabeprüfung zugesagt; Vermarktung und Koordination der Wohnungsübergabe ausstehend. Kein Anzeichen von Verzögerung, aber Nachverfolgung auf Completion erforderlich (Übergabetermin, Maklervertrag, Instandsetzungsauftrag müssen bis Januar 2025 finalisiert sein).<!-- /auto:sticky-threads.summary -->

<!-- auto:sticky-threads -->
| thread_id | subject | last_msg_date | parties | status | one-line outcome | pointer |
| --- | --- | --- | --- | --- | --- | --- |
| `TH-5f4768` | Mieterwechsel in WE 24 | 2024-11-30 | `EH-024` | active | 7 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241130_075400_EMAIL-03048.eml) |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance.summary -->[Administrative] Einheit EH-024 (WE 24, 4,5-Zimmer-Wohnung, 115 m², 2. OG rechts, Miteigentumsanteil 267/1000) in HAUS-14 mit aktiver Kommunikationsspur „Mieterwechsel in WE 24" seit 2024-02-10; zuletzt Anna Berger am 2024-11-30 [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#einheit/EH-024). Thread umfasst 7 Nachrichten über 9+ Monate [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241130_075400_EMAIL-03048.eml). Status: aktiv; Abschluss des Mieterwechsels oder Übergabe an Stammdaten erforderlich.<!-- /auto:provenance.summary -->

<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `20240415_084500_EMAIL-00945-eml` | email | [emails/2024-04/20240415_084500_EMAIL-00945.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240415_084500_EMAIL-00945.eml) | 2024-04-15T08:45:00+00:00 |
| `20241129_181500_EMAIL-03043-eml` | email | [emails/2024-11/20241129_181500_EMAIL-03043.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241129_181500_EMAIL-03043.eml) | 2024-11-29T18:15:00+00:00 |
| `20241130_075400_EMAIL-03048-eml` | email | [emails/2024-11/20241130_075400_EMAIL-03048.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241130_075400_EMAIL-03048.eml) | 2024-11-30T07:54:00+00:00 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-26T09:26:19+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
