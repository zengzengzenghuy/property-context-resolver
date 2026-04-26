# context.unit.<!-- auto:unit_id -->EH-052<!-- /auto:unit_id -->.md

> Per-unit dossier (one file per Einheit). Holds everything specific to this unit:
> the unit itself, the active lease, the tenant(s), and all unit/tenant-specific operations.
> **Property-wide data lives in `context.property.md`** — see `parent_property_ref` below.

<!-- auto:meta -->
- last_built_at: `2026-04-26T09:45:06+00:00`
- build_hash: `engine-v2`
- engine_version: `0.2.0`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `unit`
- unit_id: `EH-052`
- property_id: `LIE-001`
- parent_property_ref: `context.property.LIE-001.md`
- owner_ref: `EIG-010`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit.summary -->[Administrative] Eigentümer der Tiefgarageneinheit TG 52 (EH-052, Miteigentumsanteil 23/1000) hat Verkaufsabsicht mitgeteilt (2025-09-27); Hausgeld für 12/2025 eingegangen 2025-12-02 [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#einheit/EH-052). Nach § 17 I WEG ist Verwalter von Veräußerungsabsicht unterrichtet worden; Widerspruchsfrist und Vorkaufsrechte der Gemeinschaft sind zu prüfen. Kein Verzug oder physischer Mangel erkannt.<!-- /auto:unit.summary -->

<!-- auto:unit -->
- unit_id: `EH-052`
- label: TG 52
- haus_id: `HAUS-16`
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
- live source: `db.tickets WHERE unit_id=EH-052 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren

<!-- auto:dunning.summary -->_no issue_<!-- /auto:dunning.summary -->

#### Per claim
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
_(no data in source yet)_
- live balance pointer: `db.tenant_balance.tenant_id=EH-052`
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
<!-- auto:sticky-threads.summary -->[Administrative] Einheit EH-052 (TG 52): Verkaufsabsicht des Eigentümers seit 2025-03-07, aktive Kommunikation mit 3 Meldungen bis 2025-09-27 [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250927_223700_EMAIL-05730.eml). Kündigungstermin Miete bestätigt auf 2025-10-28, Wohnungsübergabe März 2026 geplant; Eigentümer forderte Hausgeldbescheinigung und ETV-Protokolle zur Verkaufsunterstützung an [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250916_220700_EMAIL-05642.eml). Übergabedokumentation und Maklerkoordination müssen bis Freigabetermin abgeschlossen sein.<!-- /auto:sticky-threads.summary -->

<!-- auto:sticky-threads -->
| thread_id | subject | last_msg_date | parties | status | one-line outcome | pointer |
| --- | --- | --- | --- | --- | --- | --- |
| `TH-030ee8` | Mieterwechsel in TG 52 | 2025-09-16 | `EH-052` | active | 3 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250916_220700_EMAIL-05642.eml) |
| `TH-3b09f9` | Verkaufsabsicht TG 52 | 2025-09-27 | `EH-052` | active | 3 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250927_223700_EMAIL-05730.eml) |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance.summary -->[Administrative] Einheit EH-052 (Tiefgarage TG 52, 12,5 qm, Miteigentumsanteil 23) ist Gegenstand einer aktiven Verkaufsabsicht [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#einheit/EH-052); Thread seit 2025-03-07 laufend (3 Nachrichten, letzte 2025-09-27). Hausgeldzahlung aktuell: 11,33 EUR vom Kontoeigentümer Ingbert Nerger am 2025-12-02 [(bank)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv#TX-00015) für Periode 12/2025. Verkaufsvorhaben unterliegt Zustimmungspflicht nach WEG § 16 und Vorkaufsrecht der Eigentümergemeinschaft nach § 577 BGB; Status und Käuferkommunikation zu dokumentieren.<!-- /auto:provenance.summary -->

<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `kontoauszug_2024_2025-csv` | bank | [bank/kontoauszug_2024_2025.csv](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv) | 2025-12-02 |
| `20250522_083900_EMAIL-04588-eml` | email | [emails/2025-05/20250522_083900_EMAIL-04588.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250522_083900_EMAIL-04588.eml) | 2025-05-22T08:39:00+00:00 |
| `20250916_220700_EMAIL-05642-eml` | email | [emails/2025-09/20250916_220700_EMAIL-05642.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250916_220700_EMAIL-05642.eml) | 2025-09-16T22:07:00+00:00 |
| `20250927_223700_EMAIL-05730-eml` | email | [emails/2025-09/20250927_223700_EMAIL-05730.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250927_223700_EMAIL-05730.eml) | 2025-09-27T22:37:00+00:00 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-26T09:26:19+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
