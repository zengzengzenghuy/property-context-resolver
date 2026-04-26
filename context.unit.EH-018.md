# context.unit.<!-- auto:unit_id -->EH-018<!-- /auto:unit_id -->.md

> Per-unit dossier (one file per Einheit). Holds everything specific to this unit:
> the unit itself, the active lease, the tenant(s), and all unit/tenant-specific operations.
> **Property-wide data lives in `context.property.md`** — see `parent_property_ref` below.

<!-- auto:meta -->
- last_built_at: `2026-04-26T09:31:43+00:00`
- build_hash: `engine-v2`
- engine_version: `0.2.0`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `unit`
- unit_id: `EH-018`
- property_id: `LIE-001`
- parent_property_ref: `context.property.LIE-001.md`
- owner_ref: `EIG-018`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit.summary -->[Administrative] Tiefgaragenplatz TG 18 (EH-018, Miteigentumsanteil 23/1000) verzeichnet Hausgeldzahlung 1,63 EUR für November 2025 [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#einheit/EH-018) von Irmingard Margraf [(bank)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv#TX-00030); Verkaufsabsicht dokumentiert 2025-04-09. Zahlung und Kommunikation sind nominal und im Plan; keine Verzugsfeststellung erforderlich.<!-- /auto:unit.summary -->

<!-- auto:unit -->
- unit_id: `EH-018`
- label: TG 18
- haus_id: `HAUS-12`
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
- live source: `db.tickets WHERE unit_id=EH-018 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren

<!-- auto:dunning.summary -->_no issue_<!-- /auto:dunning.summary -->

#### Per claim
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
_(no data in source yet)_
- live balance pointer: `db.tenant_balance.tenant_id=EH-018`
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
<!-- auto:sticky-threads.summary -->[Administrative] Einheit EH-018 (TG 18): Mieterwechsel seit Januar 2025 in Bearbeitung; Kündigungstermin ursprünglich 15.05.2025 bestätigt [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250409_033100_EMAIL-04242.eml), später auf 13.02.2026 verschoben [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251120_132200_EMAIL-06169.eml). Thread aktiv seit 2024-01-06 mit 4 Nachrichten; Stand 2025-11-20 zeigt Vermarktung und Übergabekoordination ausstehend — Nachverfolgung zur Abschlussbestätigung erforderlich.<!-- /auto:sticky-threads.summary -->

<!-- auto:sticky-threads -->
| thread_id | subject | last_msg_date | parties | status | one-line outcome | pointer |
| --- | --- | --- | --- | --- | --- | --- |
| `TH-42cc07` | Mieterwechsel in TG 18 | 2025-11-20 | `EH-018` | active | 4 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251120_132200_EMAIL-06169.eml) |
| `TH-311944` | Verkaufsabsicht TG 18 | 2025-04-09 | `EH-018` | active | 7 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250409_033100_EMAIL-04242.eml) |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance.summary -->[Administrative] Einheit EH-018 (TG 18, Tiefgarage, 12,5 m², Miteigentumsanteil 23/1000) zeigt aktiven Mieterwechsel-Thread seit 2024-01-06 mit Verkaufsabsicht dokumentiert 2025-04-09 [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#einheit/EH-018). Hausgeld-Zahlung 1,63 EUR für 11/2025 von Irmingard Margraf eingegangen 2025-11-04. Status: Thread aktiv (zuletzt 2025-11-20), Mieterwechsel noch nicht abgeschlossen — Vertragsübergang und Stammdata-Update erforderlich.<!-- /auto:provenance.summary -->

<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `kontoauszug_2024_2025-csv` | bank | [bank/kontoauszug_2024_2025.csv](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv) | 2025-11-04 |
| `20240106_175100_EMAIL-00044-eml` | email | [emails/2024-01/20240106_175100_EMAIL-00044.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240106_175100_EMAIL-00044.eml) | 2024-01-06T17:51:00+00:00 |
| `20240815_152300_EMAIL-02051-eml` | email | [emails/2024-08/20240815_152300_EMAIL-02051.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240815_152300_EMAIL-02051.eml) | 2024-08-15T15:23:00+00:00 |
| `20241023_031700_EMAIL-02693-eml` | email | [emails/2024-10/20241023_031700_EMAIL-02693.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241023_031700_EMAIL-02693.eml) | 2024-10-23T03:17:00+00:00 |
| `20250113_193000_EMAIL-03465-eml` | email | [emails/2025-01/20250113_193000_EMAIL-03465.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250113_193000_EMAIL-03465.eml) | 2025-01-13T19:30:00+00:00 |
| `20250409_033100_EMAIL-04242-eml` | email | [emails/2025-04/20250409_033100_EMAIL-04242.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250409_033100_EMAIL-04242.eml) | 2025-04-09T03:31:00+00:00 |
| `20250620_072900_EMAIL-04824-eml` | email | [emails/2025-06/20250620_072900_EMAIL-04824.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250620_072900_EMAIL-04824.eml) | 2025-06-20T07:29:00+00:00 |
| `20251120_132200_EMAIL-06169-eml` | email | [emails/2025-11/20251120_132200_EMAIL-06169.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251120_132200_EMAIL-06169.eml) | 2025-11-20 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-26T09:26:19+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
