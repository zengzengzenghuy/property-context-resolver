# context.unit.<!-- auto:unit_id -->EH-036<!-- /auto:unit_id -->.md

> Per-unit dossier (one file per Einheit). Holds everything specific to this unit:
> the unit itself, the active lease, the tenant(s), and all unit/tenant-specific operations.
> **Property-wide data lives in `context.property.md`** — see `parent_property_ref` below.

<!-- auto:meta -->
- last_built_at: `2026-04-26T09:38:50+00:00`
- build_hash: `engine-v2`
- engine_version: `0.2.0`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `unit`
- unit_id: `EH-036`
- property_id: `LIE-001`
- parent_property_ref: `context.property.LIE-001.md`
- owner_ref: `EIG-012`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit.summary -->[Administrative] Einheit WE 36 (4-Zimmer-Wohnung, 107 qm, 5. OG rechts) mit Miteigentumsanteil 248/1000 in HAUS-14 [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#einheit/EH-036). Kommunikationsreihe zur Modernisierungszustimmung dokumentiert von 2024-04 bis 2025-12 [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251210_085300_EMAIL-06344.eml); letzte Nachricht 2025-12-10 von Anna Berger. Einheit entspricht Stammdaten; Modernisierungszustimmung nach WEG § 8 III dokumentiert.<!-- /auto:unit.summary -->

<!-- auto:unit -->
- unit_id: `EH-036`
- label: WE 36
- haus_id: `HAUS-14`
- floor: 5. OG
- position: rechts
- typ: Wohnung
- area_sqm: 107.0
- rooms: 4.0
- mea_‰: 248
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
- live source: `db.tickets WHERE unit_id=EH-036 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren

<!-- auto:dunning.summary -->_no issue_<!-- /auto:dunning.summary -->

#### Per claim
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
_(no data in source yet)_
- live balance pointer: `db.tenant_balance.tenant_id=EH-036`
<!-- /auto:dunning -->

### 3.4 Active Reductions / Deferrals (§ 536 BGB)
<!-- auto:reductions.summary -->_no issue_<!-- /auto:reductions.summary -->

<!-- auto:reductions -->_(no data in source yet)_<!-- /auto:reductions -->

### 3.5 Latest Übergabeprotokoll
<!-- auto:handover.summary -->_no issue_<!-- /auto:handover.summary -->

<!-- auto:handover -->_(no data in source yet)_<!-- /auto:handover -->

### 3.6 Recurring Process State (this unit, in-flight)
<!-- auto:recurring.summary -->[Administrative] Mieter EH-036 hat den Mietvertrag per E-Mail vom 2025-07-21 gekündigt und fordert schriftliche Bestätigung des Kündigungstermins [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250721_204000_EMAIL-05107.eml). Kündigungsrecht des Mieters nach § 573 BGB (fristgerecht zum nächstmöglichen Termin); Annahme und schriftliche Kündigungsbestätigung erforderlich. Kündigungsfrist: 3 Monate zum 15. oder zum Ende eines Kalendermonats (§ 573 II BGB), mithin frühestens zum 2025-10-31 wirksam.<!-- /auto:recurring.summary -->

<!-- auto:recurring -->
| process_type | started | current_step | owner | eta | blockers |
| --- | --- | --- | --- | --- | --- |
| Mieterwechsel | 2025-07-21 | Kündigung erhalten | Verwaltung | TBD | Übergabe-Termin offen |
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
<!-- auto:sticky-threads.summary -->[Routine] Mieterwechsel in EH-036 eingeleitet; Mieter kündigt zum Monatsende, Leerstand ab 2026-02-16 geplant [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251128_100300_EMAIL-06249.eml). Thread aktiv seit 2024-09-11 mit 5 Nachrichten, letzte Aktivität 2025-11-28. Koordination der Wohnungsübergabe und Vermarktung erforderlich; Bestandsdaten (Kündigungsfrist, Übergabedatum, Mietzahlungen bis Leerstand) prüfen.<!-- /auto:sticky-threads.summary -->

<!-- auto:sticky-threads -->
| thread_id | subject | last_msg_date | parties | status | one-line outcome | pointer |
| --- | --- | --- | --- | --- | --- | --- |
| `TH-390f8e` | Mieterwechsel in WE 36 | 2025-11-28 | `EH-036` | active | 5 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251128_100300_EMAIL-06249.eml) |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance.summary -->[Administrative] Einheit EH-036 (WE 36, 4 Zimmer, 107 qm, 5. OG rechts) unterliegt aktivem Mieterwechsel-Thread seit 2024-09-11, zuletzt aktualisiert 2025-11-28 (5 Nachrichten) [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#einheit/EH-036). Mietvertrag wurde vom Mieter zum 2025-07-21 gekündigt [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250721_204000_EMAIL-05107.eml); Nachfolgemieterin Anna Berger hat Modernisierungszustimmung 2025-12-10 erteilt [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251210_085300_EMAIL-06344.eml). Miteigentumsanteil 248/10.000, Übergabeprozess läuft — Übergabeprotokoll und Neuvermietungsbestätigung erforderlich.<!-- /auto:provenance.summary -->

<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `20240412_055100_EMAIL-00908-eml` | email | [emails/2024-04/20240412_055100_EMAIL-00908.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240412_055100_EMAIL-00908.eml) | 2024-04-12T05:51:00+00:00 |
| `20241231_050600_EMAIL-03324-eml` | email | [emails/2024-12/20241231_050600_EMAIL-03324.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241231_050600_EMAIL-03324.eml) | 2024-12-31T05:06:00+00:00 |
| `20250704_141500_EMAIL-04942-eml` | email | [emails/2025-07/20250704_141500_EMAIL-04942.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250704_141500_EMAIL-04942.eml) | 2025-07-04T14:15:00+00:00 |
| `20250721_204000_EMAIL-05107-eml` | email | [emails/2025-07/20250721_204000_EMAIL-05107.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250721_204000_EMAIL-05107.eml) | 2025-07-21T20:40:00+00:00 |
| `20251003_101500_EMAIL-05763-eml` | email | [emails/2025-10/20251003_101500_EMAIL-05763.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251003_101500_EMAIL-05763.eml) | 2025-10-03T10:15:00+00:00 |
| `20251103_063200_EMAIL-06028-eml` | email | [emails/2025-11/20251103_063200_EMAIL-06028.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251103_063200_EMAIL-06028.eml) | 2025-11-03T06:32:00+00:00 |
| `20251128_100300_EMAIL-06249-eml` | email | [emails/2025-11/20251128_100300_EMAIL-06249.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251128_100300_EMAIL-06249.eml) | 2025-11-28 |
| `20251210_085300_EMAIL-06344-eml` | email | [emails/2025-12/20251210_085300_EMAIL-06344.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251210_085300_EMAIL-06344.eml) | 2025-12-10T08:53:00+00:00 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-26T09:26:19+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
