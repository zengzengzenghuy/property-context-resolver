# context.unit.<!-- auto:unit_id -->EH-015<!-- /auto:unit_id -->.md

> Per-unit dossier (one file per Einheit). Holds everything specific to this unit:
> the unit itself, the active lease, the tenant(s), and all unit/tenant-specific operations.
> **Property-wide data lives in `context.property.md`** — see `parent_property_ref` below.

<!-- auto:meta -->
- last_built_at: `2026-04-26T09:30:32+00:00`
- build_hash: `engine-v2`
- engine_version: `0.2.0`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `unit`
- unit_id: `EH-015`
- property_id: `LIE-001`
- parent_property_ref: `context.property.LIE-001.md`
- owner_ref: `EIG-004`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit.summary -->_no issue_<!-- /auto:unit.summary -->

<!-- auto:unit -->
- unit_id: `EH-015`
- label: WE 15
- haus_id: `HAUS-12`
- floor: 5. OG
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
<!-- auto:tickets.critical.summary -->[Routine] Mieter EH-015 meldet Schlüsselverlust am 2025-08-17 und fragt nach Austauschprozess [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250817_165400_EMAIL-05333.eml). Schlüsselbeschaffung und -austausch sind Instandhaltungspflicht des Vermieters nach § 535 II BGB, Kosten trägt der Vermieter bei Verschulden des Mieters (fahrlässiger Verlust). Ticket seit 8+ Monate offen — Rückmeldung und Beauftragung erforderlich.<!-- /auto:tickets.critical.summary -->

<!-- auto:tickets.critical -->
| ticket_id | type | title | deadline | status | assignee |
| --- | --- | --- | --- | --- | --- |
_(no data in source yet)_
<!-- /auto:tickets.critical -->

### 3.2 Open Tickets — Aggregate
<!-- auto:tickets.aggregate.summary -->[Routine] Einheit EH-015: Schlüsselersatz angefordert am 2025-08-17 [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250817_165400_EMAIL-05333.eml). Severity normal, kein Hinweis auf Notfall oder Sperrung. Bearbeitungsstand zu überprüfen; nach 8+ Monaten sollte Ticket geschlossen oder Verzögerungsgrund dokumentiert sein.<!-- /auto:tickets.aggregate.summary -->

<!-- auto:tickets.aggregate -->
- total_open: `1`
- by_type: { schluessel: `1` }
- live source: `db.tickets WHERE unit_id=EH-015 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren

<!-- auto:dunning.summary -->_no issue_<!-- /auto:dunning.summary -->

#### Per claim
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
_(no data in source yet)_
- live balance pointer: `db.tenant_balance.tenant_id=EH-015`
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
<!-- auto:sticky-threads.summary -->[Administrative] Einheit EH-015: Mieterwechsel-Thread seit 2024-07-14 aktiv, letzter Eintrag 2024-10-12. Kündigungstermin bestätigt auf 2024-10-25, Wohnungsübergabe geplant letzte Märzwoche (Inconsistenz: Freigabedatum im ersten Mail "06.01.2025", Übergabetermin vage) [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241012_103400_EMAIL-02597.eml). Thread ist 18 Monate alt — Status "active" überprüfen, ob Übergabe dokumentiert und Vermarktung abgeschlossen, oder ob Blockade vorliegt.<!-- /auto:sticky-threads.summary -->

<!-- auto:sticky-threads -->
| thread_id | subject | last_msg_date | parties | status | one-line outcome | pointer |
| --- | --- | --- | --- | --- | --- | --- |
| `TH-5df28e` | Mieterwechsel in WE 15 | 2024-10-12 | `EH-015` | active | 3 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241012_103400_EMAIL-02597.eml) |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance.summary -->[Administrative] Einheit EH-015 (WE 15, 4,5 Zimmer, 115 qm, 5. OG rechts) zeigt eine aktive Mieterwechsel-Korrespondenz vom 2024-07-14 bis 2024-10-12 [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241012_103400_EMAIL-02597.eml) sowie ein Ticket vom 2025-08-17 zur Schlüsselersetzung. Stammdaten erfassen Miteigentumsanteil 267 und Hausadresse HAUS-12 [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#einheit/EH-015). Prüfe Mieterwechsel-Dokumentation (Übergabeprotokoll, Kaution, neue Mietvertragsabwicklung) und Status Schlüsselmanagement seit August 2025 [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250817_165400_EMAIL-05333.eml).<!-- /auto:provenance.summary -->

<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `20241012_103400_EMAIL-02597-eml` | email | [emails/2024-10/20241012_103400_EMAIL-02597.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241012_103400_EMAIL-02597.eml) | 2024-10-12T10:34:00+00:00 |
| `20250817_165400_EMAIL-05333-eml` | email | [emails/2025-08/20250817_165400_EMAIL-05333.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250817_165400_EMAIL-05333.eml) | 2025-08-17T16:54:00+00:00 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-26T09:26:19+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
