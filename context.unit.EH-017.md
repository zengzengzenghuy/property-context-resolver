# context.unit.<!-- auto:unit_id -->EH-017<!-- /auto:unit_id -->.md

> Per-unit dossier (one file per Einheit). Holds everything specific to this unit:
> the unit itself, the active lease, the tenant(s), and all unit/tenant-specific operations.
> **Property-wide data lives in `context.property.md`** — see `parent_property_ref` below.

<!-- auto:meta -->
- last_built_at: `2026-04-26T09:31:30+00:00`
- build_hash: `engine-v2`
- engine_version: `0.2.0`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `unit`
- unit_id: `EH-017`
- property_id: `LIE-001`
- parent_property_ref: `context.property.LIE-001.md`
- owner_ref: `EIG-015`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit.summary -->_no issue_<!-- /auto:unit.summary -->

<!-- auto:unit -->
- unit_id: `EH-017`
- label: WE 17
- haus_id: `HAUS-12`
- floor: 5. OG
- position: rechts
- typ: Wohnung
- area_sqm: 72.0
- rooms: 2.5
- mea_‰: 167
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
<!-- auto:tickets.critical.summary -->[Routine] Mieter EH-017 meldet Schlüsselverlust am 2024-09-05 und fragt nach Austausch der Schliessanlage [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240905_153200_EMAIL-02255.eml). Vertraglich trägt der Mieter typischerweise die Kosten für verschlossene oder verlorene Schlüssel; Schliessanlagenwechsel ist Sache des Vermieters, sofern Sicherheit gefährdet ist. Sachverhalt klären: Alleiniger Schlüsselverlust oder Befürchtung unbefugten Zugriffs; ggf. Kostenvoranschlag einholen und Kostenteilung nach Mietvertrag festlegen.<!-- /auto:tickets.critical.summary -->

<!-- auto:tickets.critical -->
| ticket_id | type | title | deadline | status | assignee |
| --- | --- | --- | --- | --- | --- |
_(no data in source yet)_
<!-- /auto:tickets.critical -->

### 3.2 Open Tickets — Aggregate
<!-- auto:tickets.aggregate.summary -->[Routine] Mieter EH-017 meldet Schlüsselverlust am 2024-09-05 [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240905_153200_EMAIL-02255.eml). Vertraglich ist der Mieter für Schlüsselverwaltung und -sicherung verantwortlich; Kosten für Nachfertigung oder Schlosswechsel können nach § 280 I BGB auf den Mieter umgelegt werden, sofern Verschulden nachgewiesen ist. Ticket ist 595 Tage offen — Status und Abschluss prüfen erforderlich.<!-- /auto:tickets.aggregate.summary -->

<!-- auto:tickets.aggregate -->
- total_open: `1`
- by_type: { schluessel: `1` }
- live source: `db.tickets WHERE unit_id=EH-017 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren

<!-- auto:dunning.summary -->_no issue_<!-- /auto:dunning.summary -->

#### Per claim
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
_(no data in source yet)_
- live balance pointer: `db.tenant_balance.tenant_id=EH-017`
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
<!-- auto:sticky-threads.summary -->[Administrative] Mieterwechsel WE 17: Mieter kündigte zum Monatsende, Wohnung wird ab 2026-01-16 frei [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251217_030400_EMAIL-06416.eml). Thread seit 2025-02-08 aktiv, 6 Nachrichten bis 2025-12-17; Verwaltung bestätigte Prüfung der Wohnungsübergabe und Vermarktung. Status: Übergabe liegt >3 Monate zurück (2026-01-16); Vermarktungserfolg und Maklerabrechnung prüfen.<!-- /auto:sticky-threads.summary -->

<!-- auto:sticky-threads -->
| thread_id | subject | last_msg_date | parties | status | one-line outcome | pointer |
| --- | --- | --- | --- | --- | --- | --- |
| `TH-bdb506` | Mieterwechsel in WE 17 | 2025-12-17 | `EH-017` | active | 6 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251217_030400_EMAIL-06416.eml) |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance.summary -->[Administrative] Einheit EH-017 (WE 17, 5. OG rechts, 72 qm, 2,5 Zimmer) — aktiver Mieterwechsel-Thread seit 2025-02-08 mit 6 Meldungen, letzte Aktivität 2025-12-17 [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251217_030400_EMAIL-06416.eml). Zusätzlich offenes Ticket „Schlüsselverlust" vom 2024-09-05 unter Verwalterin Anna Berger [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240905_153200_EMAIL-02255.eml). Stammdaten konsistent [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#einheit/EH-017); beide Vorgänge müssen auf Abschluss oder Eskalation überprüft werden.<!-- /auto:provenance.summary -->

<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `20240830_104200_EMAIL-02189-eml` | email | [emails/2024-08/20240830_104200_EMAIL-02189.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240830_104200_EMAIL-02189.eml) | 2024-08-30T10:42:00+00:00 |
| `20240905_153200_EMAIL-02255-eml` | email | [emails/2024-09/20240905_153200_EMAIL-02255.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240905_153200_EMAIL-02255.eml) | 2024-09-05T15:32:00+00:00 |
| `20250415_204600_EMAIL-04302-eml` | email | [emails/2025-04/20250415_204600_EMAIL-04302.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250415_204600_EMAIL-04302.eml) | 2025-04-15T20:46:00+00:00 |
| `20251217_030400_EMAIL-06416-eml` | email | [emails/2025-12/20251217_030400_EMAIL-06416.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251217_030400_EMAIL-06416.eml) | 2025-12-17 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-26T09:26:19+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
