# context.unit.<!-- auto:unit_id -->EH-027<!-- /auto:unit_id -->.md

> Per-unit dossier (one file per Einheit). Holds everything specific to this unit:
> the unit itself, the active lease, the tenant(s), and all unit/tenant-specific operations.
> **Property-wide data lives in `context.property.md`** — see `parent_property_ref` below.

<!-- auto:meta -->
- last_built_at: `2026-04-26T09:34:54+00:00`
- build_hash: `engine-v2`
- engine_version: `0.2.0`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `unit`
- unit_id: `EH-027`
- property_id: `LIE-001`
- parent_property_ref: `context.property.LIE-001.md`
- owner_ref: `EIG-006`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit.summary -->_no issue_<!-- /auto:unit.summary -->

<!-- auto:unit -->
- unit_id: `EH-027`
- label: WE 27
- haus_id: `HAUS-14`
- floor: 3. OG
- position: rechts
- typ: Wohnung
- area_sqm: 82.0
- rooms: 3.0
- mea_‰: 190
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
<!-- auto:tickets.critical.summary -->[Routine] Mieter EH-027 meldet verstopften Abfluss in der Dusche seit 2025-06-22, Eigenversuch mit Pömpel erfolglos [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250622_100900_EMAIL-04842.eml). Mangelhaftigkeit der Mietsache nach § 536 BGB (Gebrauchstauglichkeit der Ablaufanlage); Verwalter schuldet unverzügliche Beseitigung nach § 537 I BGB. Ticket offen seit 10 Monaten — Handwerk beauftragen und Rückmeldung dokumentieren.<!-- /auto:tickets.critical.summary -->

<!-- auto:tickets.critical -->
| ticket_id | type | title | deadline | status | assignee |
| --- | --- | --- | --- | --- | --- |
_(no data in source yet)_
<!-- /auto:tickets.critical -->

### 3.2 Open Tickets — Aggregate
<!-- auto:tickets.aggregate.summary -->[Routine] Einheit EH-027 meldet verstopften Abfluss seit 2025-06-22 [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250622_100900_EMAIL-04842.eml). Abflussreparaturen fallen unter Mängelbeseitigung gem. § 535 II BGB (Vermieter trägt Instandhaltungslasten); Severity: normal, kein Wasserschaden oder Verhinderung der Gebrauchsfähigkeit gemeldet. Reparaturauftrag überfällig (Beseitigungsfrist 14 Tage ab Meldung überschritten) — Handwerker beauftragen und Abschluss dokumentieren.<!-- /auto:tickets.aggregate.summary -->

<!-- auto:tickets.aggregate -->
- total_open: `1`
- by_type: { abfluss: `1` }
- live source: `db.tickets WHERE unit_id=EH-027 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren

<!-- auto:dunning.summary -->_no issue_<!-- /auto:dunning.summary -->

#### Per claim
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
_(no data in source yet)_
- live balance pointer: `db.tenant_balance.tenant_id=EH-027`
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
<!-- auto:sticky-threads.summary -->[Administrative] Eigentümer Herr Ullmann signalisiert Mieterwechsel in EH-027 mit Kündigungsfrist zum Monatsende und Freigabedatum 15.10.2025; Thread läuft seit 2024-08-17 mit vier Meldungen, zuletzt 2025-08-04 [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250804_090500_EMAIL-05198.eml). Zuvor (2025-01-26) forderte Eigentümer Hausgeldbescheinigung und ETV-Protokolle an, was auf geplanten Verkauf hindeutet [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250126_095800_EMAIL-03565.eml). Status aktiv; Übergabe- und Vermarktungskoordination erforderlich gemäß Mietvertrag und WEG-Verwaltungsabläufe.<!-- /auto:sticky-threads.summary -->

<!-- auto:sticky-threads -->
| thread_id | subject | last_msg_date | parties | status | one-line outcome | pointer |
| --- | --- | --- | --- | --- | --- | --- |
| `TH-9f8b2f` | Mieterwechsel in WE 27 | 2025-08-04 | `EH-027` | active | 4 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250804_090500_EMAIL-05198.eml) |
| `TH-58c4ac` | Verkaufsabsicht WE 27 | 2025-01-26 | `EH-027` | active | — | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250126_095800_EMAIL-03565.eml) |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance.summary -->[Administrative] Einheit EH-027 (WE 27, 3-Zimmer-Wohnung, 82 m², 3. OG rechts, Miteigentumsanteil 190/10000) ist im Stammdaten erfasst [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#einheit/EH-027). Hausgeldzahlung 28,76 EUR vom 2025-12-05 durch Winfried Ullmann dokumentiert (TX-01602); Mieterwechsel-Thread aktiv seit 2024-08-17 (4 Nachrichten, letzte 2025-08-04); Verkaufsabsicht-Anfrage 2024-12-28; offenes Ticket „Verstopfter Abfluss" seit 2025-06-22. Keine Anomalien in Stammdaten oder Zahlungsfluss erkannt.<!-- /auto:provenance.summary -->

<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `kontoauszug_2024_2025-csv` | bank | [bank/kontoauszug_2024_2025.csv](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv) | 2025-12-05 |
| `20241228_012500_EMAIL-03297-eml` | email | [emails/2024-12/20241228_012500_EMAIL-03297.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241228_012500_EMAIL-03297.eml) | 2024-12-28T01:25:00+00:00 |
| `20250126_095800_EMAIL-03565-eml` | email | [emails/2025-01/20250126_095800_EMAIL-03565.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250126_095800_EMAIL-03565.eml) | 2025-01-26 |
| `20250622_100900_EMAIL-04842-eml` | email | [emails/2025-06/20250622_100900_EMAIL-04842.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250622_100900_EMAIL-04842.eml) | 2025-06-22T10:09:00+00:00 |
| `20250804_090500_EMAIL-05198-eml` | email | [emails/2025-08/20250804_090500_EMAIL-05198.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250804_090500_EMAIL-05198.eml) | 2025-08-04 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-26T09:26:19+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
