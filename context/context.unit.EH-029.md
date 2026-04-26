# context.unit.<!-- auto:unit_id -->EH-029<!-- /auto:unit_id -->.md

> Per-unit dossier (one file per Einheit). Holds everything specific to this unit:
> the unit itself, the active lease, the tenant(s), and all unit/tenant-specific operations.
> **Property-wide data lives in `context.property.md`** — see `parent_property_ref` below.

<!-- auto:meta -->
- last_built_at: `2026-04-26T09:35:20+00:00`
- build_hash: `engine-v2`
- engine_version: `0.2.0`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `unit`
- unit_id: `EH-029`
- property_id: `LIE-001`
- parent_property_ref: `context.property.LIE-001.md`
- owner_ref: `EIG-022`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit.summary -->[Administrative] Einheit WE 29 (EH-029): 4,5-Zimmer-Wohnung, 120 m², 4. OG mitte, Miteigentumsanteil 279/10.000 in HAUS-14 [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#einheit/EH-029). Eigentümer Tom Hartmann hat Verkaufsabsicht mitgeteilt (2025-10-29); Hausgeld Dezember 2025 eingegangen (19,76 EUR, TX-01607). Anmeldepflicht für Verkauf nach § 23 III WEG gegenüber Verwalter zu dokumentieren; Vormerkungsrecht der Wohnungseigentümergemeinschaft prüfen.<!-- /auto:unit.summary -->

<!-- auto:unit -->
- unit_id: `EH-029`
- label: WE 29
- haus_id: `HAUS-14`
- floor: 4. OG
- position: mitte
- typ: Wohnung
- area_sqm: 120.0
- rooms: 4.5
- mea_‰: 279
- equipment: _(no data in source yet)_
- media_supply: _(no data in source yet)_
- key_inventory: _(no data in source yet)_
- meters: _(no data in source yet)_
- occupancy_status: `rented`
- nk_keys: _(no data in source yet)_
<!-- /auto:unit -->

---

## 2. Lease (Mietverhältnis, voll)
<!-- auto:lease.summary -->[Administrative] Mieter MIE-017 (Einheit EH-029) reichte am 2025-02-17 erste Kündigung ein [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250217_084100_EMAIL-03762.eml), wiederholte diese am 2025-06-03 [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250603_161200_EMAIL-04696.eml), und stellte am 2025-06-20 parallel eine Untervermietungsanfrage für 3 Monate [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250620_183800_EMAIL-04829.eml). Laut Stammdaten [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-017) besteht ein aktives Mietmietverhältnis seit 2024-03-24 mit Kaution 5.343,00 EUR; Kündigungsstatus und Untervermietungsgenehmigung müssen dokumentiert und Kündigungsfrist (§ 573 BGB: einen Monat zum 15. oder zum Ende eines Kalendermonats) eingehalten werden.<!-- /auto:lease.summary -->

<!-- auto:lease -->
- lease_id: `LEASE-MIE-017`
- unit_ref: `EH-029`
- start_date: 2024-03-24 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-017)
- end_date: _(no data in source yet)_
- term_type: `unbefristet`
- cancellation_status: `by_tenant` (notice_date: 2025-06-03, move_out_date: —)
- rent_components: { kaltmiete: 1781.0, betriebskosten_vorauszahlung: 310.0, total_warmmiete: 2091.00 }
- payment_mode: Überweisung
- iban_payer: DE57100701246851604817 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-017)
- kaution: { amount: 5343.0 }
- usage: `residential`
- subletting: { current_status: `requested` }
- special_agreements: _(no data in source yet)_
<!-- /auto:lease -->

### 2.1 Tenants on this Lease
<!-- auto:tenants.summary -->_no issue_<!-- /auto:tenants.summary -->

<!-- auto:tenants -->
| tenant_id | name | role | contact_email | contact_phone | comms_pref | gesamtschuldner |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-017` | Frau Edeltraud Renner | haupt | edeltraud.renner@gmx.de | +49 (0) 6758 692617 | email | — |
<!-- /auto:tenants -->

---

## 3. Operations (this unit / this tenant)

### 3.1 Open Tickets — Critical (overdue or due ≤7 days)
<!-- auto:tickets.critical.summary -->[Emergency] Schimmelbildung im Schlafzimmer (WE 29), gemeldet 2025-11-18, in Ecke hinter Bett trotz regelmäßigen Stoßlüftens durch Mieter. Mietvertrag verpflichtet Vermieter zur Erhaltung der Wohnung in bewohnbarem Zustand (§ 535 I 1 BGB); Schimmel deutet auf Feuchtigkeitsproblem hin, das durch vorherigen Wasserschaden (Bad, gemeldet 2025-10-28 und 2025-03-16) verursacht sein kann — Reparaturpflicht nach § 535 I 2 BGB. Fachliche Begutachtung erforderlich within 7 Tagen; unbehandelte Schimmelbeschädigungen gefährden Wohnqualität und können Schadensersatzansprüche begründen (§ 536 BGB).<!-- /auto:tickets.critical.summary -->

<!-- auto:tickets.critical -->
| ticket_id | type | title | deadline | status | assignee |
| --- | --- | --- | --- | --- | --- |
| `TKT-ecd0a185` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-c75a2c28` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-104ff3e1` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-f2f59c08` | schimmel | Re: Schimmel im Schlafzimmer | — | open | — |
| `TKT-43078cb5` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-1f58483c` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-10af12d0` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-9fc7f863` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-deb3d44c` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-fba4e8a1` | wasserschaden | Re: Wasserschaden Bad | — | open | — |
| `TKT-520bf29a` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-55561ab9` | wasserschaden | Re: Wasserschaden Bad | — | open | — |
| `TKT-83d62201` | wasserschaden | Re: Wasserschaden Bad | — | open | — |
| `TKT-8a032560` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-4350fa3b` | schimmel | Schimmel im Schlafzimmer | — | open | — |
<!-- /auto:tickets.critical -->

### 3.2 Open Tickets — Aggregate
<!-- auto:tickets.aggregate.summary -->[Emergency] Einheit EH-029: Schimmelbefall im Schlafzimmer seit 2025-11-18 gemeldet [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240111_151000_EMAIL-00088.eml), Severity als kritisch eingestuft. Vermieter ist nach § 535 I 1 BGB verpflichtet, die Mietsache in zum vertragsgemäßen Gebrauch geeignetem Zustand zu erhalten; Schimmel verstößt gegen diese Gewährleistungspflicht und gefährdet Gesundheit und Bausubstanz. Ticket liegt 161 Tage offen — sofortige Ursachenanalyse (Lüftung, Leck, Kondensation) und Sanierungsplanung erforderlich, um Mietminderungsanspruch § 536 BGB abzuwehren.<!-- /auto:tickets.aggregate.summary -->

<!-- auto:tickets.aggregate -->
- total_open: `32`
- by_type: { abfluss: `5`, fenster: `7`, schimmel: `8`, schluessel: `5`, wasserschaden: `7` }
- live source: `db.tickets WHERE unit_id=EH-029 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren

<!-- auto:dunning.summary -->[Routine] Mieter MIE-017 ist seit vier Monaten im Verzug; offener Betrag 8.364,00 EUR zzgl. 109,08 EUR Verzugszinsen, letzte Zahlung 2025-12-03 [(bank)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv#TX-01585). Vertraglich geschuldet sind monatlich 2.091,00 EUR (Kaltmiete 1.781,00 EUR + NK 310,00 EUR) [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-017). Verzug nach § 286 BGB festgestellt, Verzugszinsen § 288 I BGB (Basiszins + 5pp); Mahnstufe 1, nächster Schritt: 2. Mahnung nach 14 Tagen.<!-- /auto:dunning.summary -->

#### Per claim
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-017` | — | 1 | 8364.00 EUR | 2025-12-03 | — | — |
- live balance pointer: `db.tenant_balance.tenant_id=MIE-017`
<!-- /auto:dunning -->

### 3.4 Active Reductions / Deferrals (§ 536 BGB)
<!-- auto:reductions.summary -->[Emergency] Mieter EH-029 (Edeltraud Renner) kündigt unilaterale Mietminderung um 15% an — nunmehr zum vierten Mal seit 2024-01-19 [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251215_092900_EMAIL-06399.eml) mit identischer Begründung (Wasserschaden, Schimmel seit über 3 Monaten). Letzte Ankündigung datiert 2025-12-15 mit Minderungsbeginn 2026-01-14; Mängelanzeige und Beseitigungsfrist gemäß § 536 BGB müssen unverzüglich überprüft und dokumentiert werden, da wiederholte Ankündigungen auf fehlende oder unzureichende Reparaturen hindeuten. § 536 I BGB gewährt Mietminderung bei Nichterfüllung der Gewährleistungspflicht; unbewiesene einseitige Minderung ab 2026-01-14 ist rechtlich nicht bindend, führt aber zu Verzugsstrafe und Gegengewehr — sofortige Inspektion und schriftliche Dokumentation erforderlich.<!-- /auto:reductions.summary -->

<!-- auto:reductions -->
- date_raised: 2024-01-19
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-08-16
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-09-14
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-12-15
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- *trigger: HITL exit if any entry present*
<!-- /auto:reductions -->

### 3.5 Latest Übergabeprotokoll
<!-- auto:handover.summary -->_no issue_<!-- /auto:handover.summary -->

<!-- auto:handover -->_(no data in source yet)_<!-- /auto:handover -->

### 3.6 Recurring Process State (this unit, in-flight)
<!-- auto:recurring.summary -->[Administrative] Mieter MIE-017 hat den Mietvertrag für EH-029 mehrfach gekündigt: erstmals 2024-03-06 [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240306_170800_EMAIL-00568.eml), erneut 2025-02-17 [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250217_084100_EMAIL-03762.eml), zuletzt 2025-06-03 [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250603_161200_EMAIL-04696.eml). Nach § 573 BGB (Kündigung durch Mieter) ist jede Kündigung schriftlich wirksam, sofern sie die gesetzliche Kündigungsfrist (üblicherweise 3 Monate zum Ende eines Kalendermonats) einhält; Bestätigung des Kündigungstermins durch Verwalter erforderlich. Status: Letzte Kündigungsmitteilung liegt 10+ Monate zurück; Klärung des aktuell gültigen Kündigungstermins und Räumung erforderlich.<!-- /auto:recurring.summary -->

<!-- auto:recurring -->
| process_type | started | current_step | owner | eta | blockers |
| --- | --- | --- | --- | --- | --- |
| Mieterwechsel | 2025-06-03 | Kündigung erhalten | Verwaltung | TBD | Übergabe-Termin offen |
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
<!-- auto:sticky-threads.summary -->[Administrative] Eigentümer Hartmann kündigt Wohnung EH-029 zum 06.12.2025 [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251029_141600_EMAIL-05998.eml); Thread aktiv seit 2024-07-12 mit 8 Nachrichten, ursprünglich Mieterwechsel 2024, nun Verkaufsabsicht. Wohnungsübergabe für März 2026 eingeplant; Verwaltung hat Zahlungsbescheinigung und ETV-Protokolle zur Verfügung zu stellen (BGB § 1104, § 812 — Verkäuferauskunftspflicht). Kündigungsfrist eingehalten, aber aktuelle Abrechnung und Dokumentation müssen vor Übergabe bereitgestellt sein.<!-- /auto:sticky-threads.summary -->

<!-- auto:sticky-threads -->
| thread_id | subject | last_msg_date | parties | status | one-line outcome | pointer |
| --- | --- | --- | --- | --- | --- | --- |
| `TH-7957f9` | Mieterwechsel in WE 29 | 2024-07-19 | `EH-029` | active | 4 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240719_114500_EMAIL-01806.eml) |
| `TH-b4da65` | Verkaufsabsicht WE 29 | 2025-10-29 | `EH-029` | active | 8 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251029_141600_EMAIL-05998.eml) |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance.summary -->[Routine] Mieter MIE-017 (Edeltraud Renner, WE 29, 4,5 Zimmer, 120 qm) ist seit vier Monaten im Verzug; offener Betrag 8.364,00 EUR zzgl. 109,08 EUR Verzugszinsen, letzte Zahlung 2025-12-03 [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-017). Vertraglich geschuldet monatlich 2.091,00 EUR (Kaltmiete 1.781,00 EUR + NK-Vorauszahlung 310,00 EUR); Verzug nach § 286 BGB festgestellt, Verzugszinsen § 288 I BGB (Basiszins 3,5 % + 5 pp). Mahnstufe 1 aktiv — nächster Schritt: 2. Mahnung nach 14 Tagen. Parallel: unilaterale Mietminderungsankündigung 2025-12-15 (Grund: ungelöste Reparaturen, Schimmel im Schlafzimmer seit 2025-11-18, kritischer Ticketstatus) — Reparaturverpflichtung § 535 I 1 BGB sowie Mietminderungsrecht § 536 BGB müssen vor weiterer Dunning-Eskalation geklärt werden.<!-- /auto:provenance.summary -->

<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `kontoauszug_2024_2025-csv` | bank | [bank/kontoauszug_2024_2025.csv](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv) | 2026-04-26 |
| `20240111_151000_EMAIL-00088-eml` | email | [emails/2024-01/20240111_151000_EMAIL-00088.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240111_151000_EMAIL-00088.eml) | 2024-01-11T15:10:00+00:00 |
| `20240112_112800_EMAIL-00095-eml` | email | [emails/2024-01/20240112_112800_EMAIL-00095.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240112_112800_EMAIL-00095.eml) | 2024-01-12T11:28:00+00:00 |
| `20240119_153500_EMAIL-00154-eml` | email | [emails/2024-01/20240119_153500_EMAIL-00154.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240119_153500_EMAIL-00154.eml) | 2024-01-19T15:35:00+00:00 |
| `20240119_163200_EMAIL-00157-eml` | email | [emails/2024-01/20240119_163200_EMAIL-00157.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240119_163200_EMAIL-00157.eml) | 2024-01-19T16:32:00+00:00 |
| `20240120_083200_EMAIL-00160-eml` | email | [emails/2024-01/20240120_083200_EMAIL-00160.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240120_083200_EMAIL-00160.eml) | 2024-01-20T08:32:00+00:00 |
| `20240129_083200_EMAIL-00228-eml` | email | [emails/2024-01/20240129_083200_EMAIL-00228.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240129_083200_EMAIL-00228.eml) | 2024-01-29T08:32:00+00:00 |
| `20240209_150600_EMAIL-00343-eml` | email | [emails/2024-02/20240209_150600_EMAIL-00343.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240209_150600_EMAIL-00343.eml) | 2024-02-09T15:06:00+00:00 |
| `20240213_071600_EMAIL-00368-eml` | email | [emails/2024-02/20240213_071600_EMAIL-00368.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240213_071600_EMAIL-00368.eml) | 2024-02-13T07:16:00+00:00 |
| `20240222_122900_EMAIL-00438-eml` | email | [emails/2024-02/20240222_122900_EMAIL-00438.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240222_122900_EMAIL-00438.eml) | 2024-02-22T12:29:00+00:00 |
| `20240223_115200_EMAIL-00450-eml` | email | [emails/2024-02/20240223_115200_EMAIL-00450.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240223_115200_EMAIL-00450.eml) | 2024-02-23T11:52:00+00:00 |
| `20240223_122900_EMAIL-00452-eml` | email | [emails/2024-02/20240223_122900_EMAIL-00452.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240223_122900_EMAIL-00452.eml) | 2024-02-23T12:29:00+00:00 |
| `20240306_170800_EMAIL-00568-eml` | email | [emails/2024-03/20240306_170800_EMAIL-00568.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240306_170800_EMAIL-00568.eml) | 2024-03-06T17:08:00+00:00 |
| `20240308_135200_EMAIL-00586-eml` | email | [emails/2024-03/20240308_135200_EMAIL-00586.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240308_135200_EMAIL-00586.eml) | 2024-03-08T13:52:00+00:00 |
| `20240309_115200_EMAIL-00594-eml` | email | [emails/2024-03/20240309_115200_EMAIL-00594.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240309_115200_EMAIL-00594.eml) | 2024-03-09T11:52:00+00:00 |
| `20240310_103900_EMAIL-00600-eml` | email | [emails/2024-03/20240310_103900_EMAIL-00600.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240310_103900_EMAIL-00600.eml) | 2024-03-10T10:39:00+00:00 |
| `20240318_105900_EMAIL-00672-eml` | email | [emails/2024-03/20240318_105900_EMAIL-00672.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240318_105900_EMAIL-00672.eml) | 2024-03-18T10:59:00+00:00 |
| `20240415_104500_EMAIL-00946-eml` | email | [emails/2024-04/20240415_104500_EMAIL-00946.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240415_104500_EMAIL-00946.eml) | 2024-04-15T10:45:00+00:00 |
| `20240426_110300_EMAIL-01046-eml` | email | [emails/2024-04/20240426_110300_EMAIL-01046.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240426_110300_EMAIL-01046.eml) | 2024-04-26T11:03:00+00:00 |
| `20240427_060300_EMAIL-01053-eml` | email | [emails/2024-04/20240427_060300_EMAIL-01053.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240427_060300_EMAIL-01053.eml) | 2024-04-27T06:03:00+00:00 |
| `20240512_111000_EMAIL-01187-eml` | email | [emails/2024-05/20240512_111000_EMAIL-01187.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240512_111000_EMAIL-01187.eml) | 2024-05-12T11:10:00+00:00 |
| `20240514_114900_EMAIL-01215-eml` | email | [emails/2024-05/20240514_114900_EMAIL-01215.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240514_114900_EMAIL-01215.eml) | 2024-05-14T11:49:00+00:00 |
| `20240517_010600_EMAIL-01237-eml` | email | [emails/2024-05/20240517_010600_EMAIL-01237.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240517_010600_EMAIL-01237.eml) | 2024-05-17T01:06:00+00:00 |
| `20240518_225600_EMAIL-01251-eml` | email | [emails/2024-05/20240518_225600_EMAIL-01251.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240518_225600_EMAIL-01251.eml) | 2024-05-18T22:56:00+00:00 |
| `20240609_152400_EMAIL-01443-eml` | email | [emails/2024-06/20240609_152400_EMAIL-01443.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240609_152400_EMAIL-01443.eml) | 2024-06-09T15:24:00+00:00 |
| `20240622_113600_EMAIL-01564-eml` | email | [emails/2024-06/20240622_113600_EMAIL-01564.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240622_113600_EMAIL-01564.eml) | 2024-06-22T11:36:00+00:00 |
| `20240703_113900_EMAIL-01643-eml` | email | [emails/2024-07/20240703_113900_EMAIL-01643.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240703_113900_EMAIL-01643.eml) | 2024-07-03T11:39:00+00:00 |
| `20240703_203900_EMAIL-01646-eml` | email | [emails/2024-07/20240703_203900_EMAIL-01646.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240703_203900_EMAIL-01646.eml) | 2024-07-03T20:39:00+00:00 |
| `20240704_203900_EMAIL-01659-eml` | email | [emails/2024-07/20240704_203900_EMAIL-01659.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240704_203900_EMAIL-01659.eml) | 2024-07-04T20:39:00+00:00 |
| `20240709_141300_EMAIL-01707-eml` | email | [emails/2024-07/20240709_141300_EMAIL-01707.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240709_141300_EMAIL-01707.eml) | 2024-07-09T14:13:00+00:00 |
| `20240711_021300_EMAIL-01727-eml` | email | [emails/2024-07/20240711_021300_EMAIL-01727.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240711_021300_EMAIL-01727.eml) | 2024-07-11T02:13:00+00:00 |
| `20240714_070700_EMAIL-01755-eml` | email | [emails/2024-07/20240714_070700_EMAIL-01755.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240714_070700_EMAIL-01755.eml) | 2024-07-14T07:07:00+00:00 |
| `20240716_094900_EMAIL-01773-eml` | email | [emails/2024-07/20240716_094900_EMAIL-01773.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240716_094900_EMAIL-01773.eml) | 2024-07-16T09:49:00+00:00 |
| `20240717_190900_EMAIL-01796-eml` | email | [emails/2024-07/20240717_190900_EMAIL-01796.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240717_190900_EMAIL-01796.eml) | 2024-07-17T19:09:00+00:00 |
| `20240718_103200_EMAIL-01798-eml` | email | [emails/2024-07/20240718_103200_EMAIL-01798.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240718_103200_EMAIL-01798.eml) | 2024-07-18T10:32:00+00:00 |
| `20240719_114500_EMAIL-01806-eml` | email | [emails/2024-07/20240719_114500_EMAIL-01806.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240719_114500_EMAIL-01806.eml) | 2024-07-19 |
| `20240721_021300_EMAIL-01819-eml` | email | [emails/2024-07/20240721_021300_EMAIL-01819.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240721_021300_EMAIL-01819.eml) | 2024-07-21T02:13:00+00:00 |
| `20240727_121400_EMAIL-01880-eml` | email | [emails/2024-07/20240727_121400_EMAIL-01880.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240727_121400_EMAIL-01880.eml) | 2024-07-27T12:14:00+00:00 |
| `20240802_180300_EMAIL-01936-eml` | email | [emails/2024-08/20240802_180300_EMAIL-01936.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240802_180300_EMAIL-01936.eml) | 2024-08-02T18:03:00+00:00 |
| `20240804_040300_EMAIL-01954-eml` | email | [emails/2024-08/20240804_040300_EMAIL-01954.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240804_040300_EMAIL-01954.eml) | 2024-08-04T04:03:00+00:00 |
| `20240817_173200_EMAIL-02072-eml` | email | [emails/2024-08/20240817_173200_EMAIL-02072.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240817_173200_EMAIL-02072.eml) | 2024-08-17T17:32:00+00:00 |
| `20240821_205800_EMAIL-02120-eml` | email | [emails/2024-08/20240821_205800_EMAIL-02120.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240821_205800_EMAIL-02120.eml) | 2024-08-21T20:58:00+00:00 |
| `20240825_164100_EMAIL-02153-eml` | email | [emails/2024-08/20240825_164100_EMAIL-02153.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240825_164100_EMAIL-02153.eml) | 2024-08-25T16:41:00+00:00 |
| `20240924_122400_EMAIL-02428-eml` | email | [emails/2024-09/20240924_122400_EMAIL-02428.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240924_122400_EMAIL-02428.eml) | 2024-09-24T12:24:00+00:00 |
| `20240926_112400_EMAIL-02445-eml` | email | [emails/2024-09/20240926_112400_EMAIL-02445.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240926_112400_EMAIL-02445.eml) | 2024-09-26T11:24:00+00:00 |
| `20240926_133700_EMAIL-02448-eml` | email | [emails/2024-09/20240926_133700_EMAIL-02448.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240926_133700_EMAIL-02448.eml) | 2024-09-26T13:37:00+00:00 |
| `20241022_111000_EMAIL-02680-eml` | email | [emails/2024-10/20241022_111000_EMAIL-02680.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241022_111000_EMAIL-02680.eml) | 2024-10-22T11:10:00+00:00 |
| `20241027_105400_EMAIL-02734-eml` | email | [emails/2024-10/20241027_105400_EMAIL-02734.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241027_105400_EMAIL-02734.eml) | 2024-10-27T10:54:00+00:00 |
| `20241113_164900_EMAIL-02896-eml` | email | [emails/2024-11/20241113_164900_EMAIL-02896.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241113_164900_EMAIL-02896.eml) | 2024-11-13T16:49:00+00:00 |
| `20241121_154800_EMAIL-02965-eml` | email | [emails/2024-11/20241121_154800_EMAIL-02965.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241121_154800_EMAIL-02965.eml) | 2024-11-21T15:48:00+00:00 |
| `20241124_150300_EMAIL-02997-eml` | email | [emails/2024-11/20241124_150300_EMAIL-02997.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241124_150300_EMAIL-02997.eml) | 2024-11-24T15:03:00+00:00 |
| `20241205_152100_EMAIL-03092-eml` | email | [emails/2024-12/20241205_152100_EMAIL-03092.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241205_152100_EMAIL-03092.eml) | 2024-12-05T15:21:00+00:00 |
| `20241221_144600_EMAIL-03230-eml` | email | [emails/2024-12/20241221_144600_EMAIL-03230.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241221_144600_EMAIL-03230.eml) | 2024-12-21T14:46:00+00:00 |
| `20241225_093700_EMAIL-03267-eml` | email | [emails/2024-12/20241225_093700_EMAIL-03267.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241225_093700_EMAIL-03267.eml) | 2024-12-25T09:37:00+00:00 |
| `20250111_163300_EMAIL-03442-eml` | email | [emails/2025-01/20250111_163300_EMAIL-03442.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250111_163300_EMAIL-03442.eml) | 2025-01-11T16:33:00+00:00 |
| `20250112_073300_EMAIL-03444-eml` | email | [emails/2025-01/20250112_073300_EMAIL-03444.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250112_073300_EMAIL-03444.eml) | 2025-01-12T07:33:00+00:00 |
| `20250121_155300_EMAIL-03535-eml` | email | [emails/2025-01/20250121_155300_EMAIL-03535.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250121_155300_EMAIL-03535.eml) | 2025-01-21T15:53:00+00:00 |
| `20250131_121500_EMAIL-03611-eml` | email | [emails/2025-01/20250131_121500_EMAIL-03611.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250131_121500_EMAIL-03611.eml) | 2025-01-31T12:15:00+00:00 |
| `20250205_095900_EMAIL-03647-eml` | email | [emails/2025-02/20250205_095900_EMAIL-03647.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250205_095900_EMAIL-03647.eml) | 2025-02-05T09:59:00+00:00 |
| `20250214_105900_EMAIL-03731-eml` | email | [emails/2025-02/20250214_105900_EMAIL-03731.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250214_105900_EMAIL-03731.eml) | 2025-02-14T10:59:00+00:00 |
| `20250217_084100_EMAIL-03762-eml` | email | [emails/2025-02/20250217_084100_EMAIL-03762.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250217_084100_EMAIL-03762.eml) | 2025-02-17T08:41:00+00:00 |
| `20250303_162000_EMAIL-03910-eml` | email | [emails/2025-03/20250303_162000_EMAIL-03910.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250303_162000_EMAIL-03910.eml) | 2025-03-03T16:20:00+00:00 |
| `20250316_161000_EMAIL-04031-eml` | email | [emails/2025-03/20250316_161000_EMAIL-04031.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250316_161000_EMAIL-04031.eml) | 2025-03-16T16:10:00+00:00 |
| `20250319_141000_EMAIL-04067-eml` | email | [emails/2025-03/20250319_141000_EMAIL-04067.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250319_141000_EMAIL-04067.eml) | 2025-03-19T14:10:00+00:00 |
| `20250401_164300_EMAIL-04181-eml` | email | [emails/2025-04/20250401_164300_EMAIL-04181.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250401_164300_EMAIL-04181.eml) | 2025-04-01T16:43:00+00:00 |
| `20250506_093600_EMAIL-04444-eml` | email | [emails/2025-05/20250506_093600_EMAIL-04444.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250506_093600_EMAIL-04444.eml) | 2025-05-06T09:36:00+00:00 |
| `20250512_174000_EMAIL-04498-eml` | email | [emails/2025-05/20250512_174000_EMAIL-04498.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250512_174000_EMAIL-04498.eml) | 2025-05-12T17:40:00+00:00 |
| `20250518_202600_EMAIL-04553-eml` | email | [emails/2025-05/20250518_202600_EMAIL-04553.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250518_202600_EMAIL-04553.eml) | 2025-05-18T20:26:00+00:00 |
| `20250603_161200_EMAIL-04696-eml` | email | [emails/2025-06/20250603_161200_EMAIL-04696.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250603_161200_EMAIL-04696.eml) | 2025-06-03T16:12:00+00:00 |
| `20250604_101200_EMAIL-04700-eml` | email | [emails/2025-06/20250604_101200_EMAIL-04700.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250604_101200_EMAIL-04700.eml) | 2025-06-04T10:12:00+00:00 |
| `20250620_183800_EMAIL-04829-eml` | email | [emails/2025-06/20250620_183800_EMAIL-04829.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250620_183800_EMAIL-04829.eml) | 2025-06-20T18:38:00+00:00 |
| `20250622_100900_EMAIL-04842-eml` | email | [emails/2025-06/20250622_100900_EMAIL-04842.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250622_100900_EMAIL-04842.eml) | 2025-06-22T10:09:00+00:00 |
| `20250630_102400_EMAIL-04907-eml` | email | [emails/2025-06/20250630_102400_EMAIL-04907.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250630_102400_EMAIL-04907.eml) | 2025-06-30T10:24:00+00:00 |
| `20250701_092400_EMAIL-04917-eml` | email | [emails/2025-07/20250701_092400_EMAIL-04917.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250701_092400_EMAIL-04917.eml) | 2025-07-01T09:24:00+00:00 |
| `20250701_175500_EMAIL-04925-eml` | email | [emails/2025-07/20250701_175500_EMAIL-04925.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250701_175500_EMAIL-04925.eml) | 2025-07-01T17:55:00+00:00 |
| `20250706_092400_EMAIL-04957-eml` | email | [emails/2025-07/20250706_092400_EMAIL-04957.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250706_092400_EMAIL-04957.eml) | 2025-07-06T09:24:00+00:00 |
| `20250816_144400_EMAIL-05315-eml` | email | [emails/2025-08/20250816_144400_EMAIL-05315.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250816_144400_EMAIL-05315.eml) | 2025-08-16T14:44:00+00:00 |
| `20250906_104500_EMAIL-05539-eml` | email | [emails/2025-09/20250906_104500_EMAIL-05539.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250906_104500_EMAIL-05539.eml) | 2025-09-06T10:45:00+00:00 |
| `20250909_234500_EMAIL-05585-eml` | email | [emails/2025-09/20250909_234500_EMAIL-05585.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250909_234500_EMAIL-05585.eml) | 2025-09-09T23:45:00+00:00 |
| `20250914_121500_EMAIL-05621-eml` | email | [emails/2025-09/20250914_121500_EMAIL-05621.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250914_121500_EMAIL-05621.eml) | 2025-09-14T12:15:00+00:00 |
| `20250925_112900_EMAIL-05712-eml` | email | [emails/2025-09/20250925_112900_EMAIL-05712.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250925_112900_EMAIL-05712.eml) | 2025-09-25T11:29:00+00:00 |
| `20251001_094600_EMAIL-05750-eml` | email | [emails/2025-10/20251001_094600_EMAIL-05750.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251001_094600_EMAIL-05750.eml) | 2025-10-01T09:46:00+00:00 |
| `20251003_171200_EMAIL-05773-eml` | email | [emails/2025-10/20251003_171200_EMAIL-05773.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251003_171200_EMAIL-05773.eml) | 2025-10-03T17:12:00+00:00 |
| `20251028_145400_EMAIL-05988-eml` | email | [emails/2025-10/20251028_145400_EMAIL-05988.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251028_145400_EMAIL-05988.eml) | 2025-10-28T14:54:00+00:00 |
| `20251029_141600_EMAIL-05998-eml` | email | [emails/2025-10/20251029_141600_EMAIL-05998.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251029_141600_EMAIL-05998.eml) | 2025-10-29T14:16:00+00:00 |
| `20251118_112600_EMAIL-06152-eml` | email | [emails/2025-11/20251118_112600_EMAIL-06152.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251118_112600_EMAIL-06152.eml) | 2025-11-18T11:26:00+00:00 |
| `20251119_203700_EMAIL-06164-eml` | email | [emails/2025-11/20251119_203700_EMAIL-06164.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251119_203700_EMAIL-06164.eml) | 2025-11-19T20:37:00+00:00 |
| `20251125_115100_EMAIL-06220-eml` | email | [emails/2025-11/20251125_115100_EMAIL-06220.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251125_115100_EMAIL-06220.eml) | 2025-11-25T11:51:00+00:00 |
| `20251215_092900_EMAIL-06399-eml` | email | [emails/2025-12/20251215_092900_EMAIL-06399.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251215_092900_EMAIL-06399.eml) | 2025-12-15T09:29:00+00:00 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-26T09:26:19+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
