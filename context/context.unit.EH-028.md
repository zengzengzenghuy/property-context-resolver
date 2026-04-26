# context.unit.<!-- auto:unit_id -->EH-028<!-- /auto:unit_id -->.md

> Per-unit dossier (one file per Einheit). Holds everything specific to this unit:
> the unit itself, the active lease, the tenant(s), and all unit/tenant-specific operations.
> **Property-wide data lives in `context.property.md`** — see `parent_property_ref` below.

<!-- auto:meta -->
- last_built_at: `2026-04-26T09:35:08+00:00`
- build_hash: `engine-v2`
- engine_version: `0.2.0`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `unit`
- unit_id: `EH-028`
- property_id: `LIE-001`
- parent_property_ref: `context.property.LIE-001.md`
- owner_ref: `EIG-008`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit.summary -->_no issue_<!-- /auto:unit.summary -->

<!-- auto:unit -->
- unit_id: `EH-028`
- label: WE 28
- haus_id: `HAUS-14`
- floor: 4. OG
- position: links
- typ: Wohnung
- area_sqm: 96.0
- rooms: 3.5
- mea_‰: 223
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
- live source: `db.tickets WHERE unit_id=EH-028 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren

<!-- auto:dunning.summary -->_no issue_<!-- /auto:dunning.summary -->

#### Per claim
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
_(no data in source yet)_
- live balance pointer: `db.tenant_balance.tenant_id=EH-028`
<!-- /auto:dunning -->

### 3.4 Active Reductions / Deferrals (§ 536 BGB)
<!-- auto:reductions.summary -->_no issue_<!-- /auto:reductions.summary -->

<!-- auto:reductions -->_(no data in source yet)_<!-- /auto:reductions -->

### 3.5 Latest Übergabeprotokoll
<!-- auto:handover.summary -->_no issue_<!-- /auto:handover.summary -->

<!-- auto:handover -->_(no data in source yet)_<!-- /auto:handover -->

### 3.6 Recurring Process State (this unit, in-flight)
<!-- auto:recurring.summary -->[Administrative] Mieter EH-028 hat den Mietvertrag per E-Mail vom 2024-07-16 mit Wunsch nach fristgerechter Beendigung zum nächstmöglichen Termin gekündigt [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240716_094900_EMAIL-01773.eml). Schriftliche Kündigungsfrist nach § 573 I BGB beträgt drei Monate zum 15. oder zum Ende eines Kalendermonats; bei Eingang 2024-07-16 ist frühester Kündigungstermin 2024-10-31. Bestätigung der Kündigungsfrist und des Auszugstermins erforderlich; anschließend Übergabetermin koordinieren und Nebenkostenabrechnung einleiten.<!-- /auto:recurring.summary -->

<!-- auto:recurring -->
| process_type | started | current_step | owner | eta | blockers |
| --- | --- | --- | --- | --- | --- |
| Mieterwechsel | 2024-07-16 | Kündigung erhalten | Verwaltung | TBD | Übergabe-Termin offen |
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
<!-- auto:sticky-threads.summary -->[Administrative] Mieterwechsel in WE 28: Kündigungsfrist zum 03.03.2026, Thread seit 26.07.2025 aktiv, 7 Nachrichten. Eigentümerin Schacht hat im Juli 2025 Verkaufsabsicht angemeldet und Hausgeldbescheinigung + ETV-Protokolle angefordert [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250726_163000_EMAIL-05137.eml); am 31.12.2025 Beauftragung Handwerker zur Vorbereitung Wohnungsübergabe angeboten [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251231_000700_EMAIL-06539.eml). Übergabeabwicklung und Vermarktung ab 03.03.2026 zu koordinieren; Staffelung der Revisionsarbeiten vor Neuvermietung prüfen.<!-- /auto:sticky-threads.summary -->

<!-- auto:sticky-threads -->
| thread_id | subject | last_msg_date | parties | status | one-line outcome | pointer |
| --- | --- | --- | --- | --- | --- | --- |
| `TH-13b249` | Mieterwechsel in WE 28 | 2025-12-31 | `EH-028` | active | 7 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251231_000700_EMAIL-06539.eml) |
| `TH-8eabec` | Verkaufsabsicht WE 28 | 2025-07-26 | `EH-028` | active | 4 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250726_163000_EMAIL-05137.eml) |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance.summary -->[Administrative] Einheit EH-028 (WE 28, 3,5-Zimmer-Wohnung, 96 qm, 4. OG links) unterliegt einem aktiven Mieterwechsel-Thread seit 2024-07-26 [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240716_094900_EMAIL-01773.eml) mit Kündigungsmitteilung durch Mieter am 2024-07-16 und anschließender Verkaufsabsicht gemeldet am 2024-09-09 [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240909_091800_EMAIL-02297.eml). Der Thread bleibt mit sieben Nachrichten bis 2025-12-31 aktiv; Status und Abschluss der Übergabe müssen geprüft werden [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#einheit/EH-028).<!-- /auto:provenance.summary -->

<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `20240716_094900_EMAIL-01773-eml` | email | [emails/2024-07/20240716_094900_EMAIL-01773.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240716_094900_EMAIL-01773.eml) | 2024-07-16T09:49:00+00:00 |
| `20240909_091800_EMAIL-02297-eml` | email | [emails/2024-09/20240909_091800_EMAIL-02297.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240909_091800_EMAIL-02297.eml) | 2024-09-09T09:18:00+00:00 |
| `20250726_163000_EMAIL-05137-eml` | email | [emails/2025-07/20250726_163000_EMAIL-05137.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250726_163000_EMAIL-05137.eml) | 2025-07-26 |
| `20251007_083500_EMAIL-05803-eml` | email | [emails/2025-10/20251007_083500_EMAIL-05803.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251007_083500_EMAIL-05803.eml) | 2025-10-07T08:35:00+00:00 |
| `20251021_171400_EMAIL-05930-eml` | email | [emails/2025-10/20251021_171400_EMAIL-05930.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251021_171400_EMAIL-05930.eml) | 2025-10-21T17:14:00+00:00 |
| `20251231_000700_EMAIL-06539-eml` | email | [emails/2025-12/20251231_000700_EMAIL-06539.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251231_000700_EMAIL-06539.eml) | 2025-12-31T00:07:00+00:00 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-26T09:26:19+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
