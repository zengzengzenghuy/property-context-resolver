# context.unit.<!-- auto:unit_id -->EH-041<!-- /auto:unit_id -->.md

> Per-unit dossier (one file per Einheit). Holds everything specific to this unit:
> the unit itself, the active lease, the tenant(s), and all unit/tenant-specific operations.
> **Property-wide data lives in `context.property.md`** — see `parent_property_ref` below.

<!-- auto:meta -->
- last_built_at: `2026-04-26T09:40:32+00:00`
- build_hash: `engine-v2`
- engine_version: `0.2.0`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `unit`
- unit_id: `EH-041`
- property_id: `LIE-001`
- parent_property_ref: `context.property.LIE-001.md`
- owner_ref: `EIG-029`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit.summary -->[Routine] Einheit WE 41 (EH-041): 4-Zimmer-Wohnung, 106 m², 1. OG rechts, Miteigentumsanteil 246/10000 [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#einheit/EH-041). Mieter Galina Wohlgemut zahlt regelmäßig (letzte Mietzahlung 2.111,00 EUR am 2025-12-03) [(bank)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv#TX-00009); offene Verwaltungsaufgabe: Schlüsselersatz-Ticket vom 2025-12-13 (Bearbeiter Thomas Kreuzer). Keine Verzugsanzeichen oder Mängel dokumentiert; Einheit läuft nach Vertrag.<!-- /auto:unit.summary -->

<!-- auto:unit -->
- unit_id: `EH-041`
- label: WE 41
- haus_id: `HAUS-16`
- floor: 1. OG
- position: rechts
- typ: Wohnung
- area_sqm: 106.0
- rooms: 4.0
- mea_‰: 246
- equipment: _(no data in source yet)_
- media_supply: _(no data in source yet)_
- key_inventory: _(no data in source yet)_
- meters: _(no data in source yet)_
- occupancy_status: `rented`
- nk_keys: _(no data in source yet)_
<!-- /auto:unit -->

---

## 2. Lease (Mietverhältnis, voll)
<!-- auto:lease.summary -->[Routine] Mieter MIE-021 (EH-041) hat am 2025-12-12 fristgerechte Kündigung des Mietvertrags eingereicht [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251212_160200_EMAIL-06369.eml); zuvor bereits drei identische Kündigungsanfragen seit 2025-03-11 gestellt. Mietvertrag seit 2021-11-14 laufend, Kaltmiete 1.840,00 EUR + NK 271,00 EUR, Kaution 5.520,00 EUR [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-021). Kündigungsfrist § 573 I BGB (vier Wochen zum 15. oder zum Ende eines Kalendermonats); aktuelle Kündigung ist zum 31.01.2026 wirksam; Bestätigungsschreiben und Übergabetermin sind fällig, Kaution-Abrechnung nach Auszug durchzuführen.<!-- /auto:lease.summary -->

<!-- auto:lease -->
- lease_id: `LEASE-MIE-021`
- unit_ref: `EH-041`
- start_date: 2021-11-14 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-021)
- end_date: _(no data in source yet)_
- term_type: `unbefristet`
- cancellation_status: `by_tenant` (notice_date: 2025-12-12, move_out_date: —)
- rent_components: { kaltmiete: 1840.0, betriebskosten_vorauszahlung: 271.0, total_warmmiete: 2111.00 }
- payment_mode: Überweisung
- iban_payer: DE86100500009318393352 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-021)
- kaution: { amount: 5520.0 }
- usage: `residential`
- subletting: { current_status: `requested` }
- special_agreements: _(no data in source yet)_
<!-- /auto:lease -->

### 2.1 Tenants on this Lease
<!-- auto:tenants.summary -->_no issue_<!-- /auto:tenants.summary -->

<!-- auto:tenants -->
| tenant_id | name | role | contact_email | contact_phone | comms_pref | gesamtschuldner |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-021` | Frau Galina Wohlgemut | haupt | galina.wohlgemut@outlook.com | +49 (0) 9042 284210 | email | — |
<!-- /auto:tenants -->

---

## 3. Operations (this unit / this tenant)

### 3.1 Open Tickets — Critical (overdue or due ≤7 days)
<!-- auto:tickets.critical.summary -->[Routine] Mieter EH-041 hat am 12.12.2025 Schlüsselverlust gemeldet; Verwaltung bestätigte Auftragserteilung am 13.12.2025, Status bleibt offen. Vertraglich trägt der Mieter Kosten für Schlüsselverluste nach Hausordnung und Mietvertrag (Ersatzschlüssel auf Mieterkosten); § 535 BGB verpflichtet Vermieter zur Gebrauchsfähigkeit, nicht zur kostenlosen Wiederbeschaffung fremder Schlüssel. Meldefrist überschritten (13+ Tage seit Meldung), nächster Schritt: Kostenschätzung und Leistungsbestätigung vom Handwerker einholen, Kostenaufteilung schriftlich mitteilen.<!-- /auto:tickets.critical.summary -->

<!-- auto:tickets.critical -->
| ticket_id | type | title | deadline | status | assignee |
| --- | --- | --- | --- | --- | --- |
| `TKT-e93a9081` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-a62120bd` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-f5b9ab82` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-5ef726f1` | schimmel | Re: Schimmel im Schlafzimmer | — | open | — |
| `TKT-dca7ed9f` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-c145f846` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-a07513c8` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-61337cd9` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-17f429a9` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-0b16d773` | wasserschaden | Wasserschaden Bad | — | open | — |
<!-- /auto:tickets.critical -->

### 3.2 Open Tickets — Aggregate
<!-- auto:tickets.aggregate.summary -->[Routine] Einheit EH-041: Schlüsselaustausch angefordert, Ticket eröffnet 2025-12-13. Keine vertragliche oder gesetzliche Frist für Schlüsselersatz definiert; Handlung fällt unter Verwaltungspflicht zur Instandhaltung des Mietgegenstands. Status: 135 Tage offen (Stand 2026-04-26), Eskalation erforderlich, falls noch nicht bearbeitet [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240216_091400_EMAIL-00397.eml).<!-- /auto:tickets.aggregate.summary -->

<!-- auto:tickets.aggregate -->
- total_open: `21`
- by_type: { abfluss: `5`, fenster: `2`, schimmel: `5`, schluessel: `4`, wasserschaden: `5` }
- live source: `db.tickets WHERE unit_id=EH-041 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren

<!-- auto:dunning.summary -->[Routine] Mieter MIE-021 ist seit vier Monaten im Verzug; offener Betrag 8.444,00 EUR zzgl. 110,12 EUR Verzugszinsen, letzte Zahlung 2025-12-03 [(bank)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv#TX-01588). Vertraglich geschuldet sind monatlich 2.111,00 EUR (Kaltmiete 1.840,00 EUR + NK 271,00 EUR) [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-021). Verzug nach § 286 BGB festgestellt, Verzugszinsen § 288 I BGB; Mahnstufe 1, nächster Schritt: 2. Mahnung nach 14 Tagen.<!-- /auto:dunning.summary -->

#### Per claim
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-021` | — | 1 | 8444.00 EUR | 2025-12-03 | — | — |
- live balance pointer: `db.tenant_balance.tenant_id=MIE-021`
<!-- /auto:dunning -->

### 3.4 Active Reductions / Deferrals (§ 536 BGB)
<!-- auto:reductions.summary -->[Emergency] Mieter EH-041 kündigt seit Juni 2024 wiederholt unilaterale Mietminderung um 15% an [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251213_081200_EMAIL-06373.eml) — Grund: Wasserschaden und Schimmel über 18+ Monate unbehoben; letzte Ankündigung 2025-12-13 mit Wirkung ab 2026-01-12. Rechtliche Grundlage nach § 536 BGB (Gewährleistung für Mängel, die die Tauglichkeit der Wohnung aufheben) liegt vor, wenn Mängel nachgewiesen und Vorankündigung nicht widersprochen wurde; Mieter ist gleichzeitig zum 2025-06-19 ausgezogen [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250515_032100_EMAIL-04519.eml). Sofortige Klärung erforderlich: Bestand der Mängel, Dokumentation von Reparaturversuchen, Geltendmachung von Mietminderungen ab 2024-06-02, Schadensersatz nach § 280 BGB.<!-- /auto:reductions.summary -->

<!-- auto:reductions -->
- date_raised: 2024-06-02
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-09-09
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-01-01
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-04-28
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-05-14
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-05-15
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-05-16
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-12-13
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- *trigger: HITL exit if any entry present*
<!-- /auto:reductions -->

### 3.5 Latest Übergabeprotokoll
<!-- auto:handover.summary -->_no issue_<!-- /auto:handover.summary -->

<!-- auto:handover -->_(no data in source yet)_<!-- /auto:handover -->

### 3.6 Recurring Process State (this unit, in-flight)
<!-- auto:recurring.summary -->[Administrative] Mieter MIE-021 hat den Mietvertrag für EH-041 viermal eingereicht — zuerst 2025-01-09 [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250109_144700_EMAIL-03425.eml), dann 2025-03-11, 2025-06-28, und zuletzt 2025-12-12 [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251212_160200_EMAIL-06369.eml) — jeweils mit identischem Text und Forderung nach schriftlicher Bestätigung. Die erste Kündigung (2025-01-09) ist nach § 573 I BGB mit dreimonatiger Frist zum Ende eines Kalendermonats wirksam geworden (Kündigungstermin: 2025-04-30); Wiederholungseinreichungen deuten auf fehlende Empfangsbestätigung hin und erfordern sofortige schriftliche Bestätigung des ursprünglichen Kündigungstermins, um Missverstände auszuräumen.<!-- /auto:recurring.summary -->

<!-- auto:recurring -->
| process_type | started | current_step | owner | eta | blockers |
| --- | --- | --- | --- | --- | --- |
| Mieterwechsel | 2025-12-12 | Kündigung erhalten | Verwaltung | TBD | Übergabe-Termin offen |
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
<!-- auto:sticky-threads.summary -->[Administrative] Eigentuemer von EH-041 signalisiert Verkaufsabsicht (Mitteilung 2025-12-21) und fordert Hausgeldbesch­einigung sowie ETV-Protokolle an [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251221_115400_EMAIL-06453.eml). Thread ist aktiv seit 2024-01-07 mit 10 Eintraegen; letzte Aktivitaet 2025-12-21. Auskunftspflicht nach § 28 III WEG (Hausgeldbestaetigung, Abrechnungen, Protokolle) innerhalb angemessener Frist zu erfuellen; Verkauf erfordert vorherige Benachrichtigung des Verwalters, Ankauf­rechtswahrung (§ 28 II WEG), keine ausstehenden Charges.<!-- /auto:sticky-threads.summary -->

<!-- auto:sticky-threads -->
| thread_id | subject | last_msg_date | parties | status | one-line outcome | pointer |
| --- | --- | --- | --- | --- | --- | --- |
| `TH-4236b5` | Verkaufsabsicht WE 41 | 2025-12-21 | `EH-041` | active | 10 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251221_115400_EMAIL-06453.eml) |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance.summary -->[Routine] Mieter MIE-021 (Galina Wohlgemut, WE 41, 106 m², 4 Zimmer) ist seit vier Monaten im Verzug; offener Betrag 8.444,00 EUR zzgl. 110,12 EUR Verzugszinsen, letzte Zahlung 2025-12-03 [(bank)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv#TX-00009). Vertraglich geschuldet sind monatlich 2.111,00 EUR (Kaltmiete 1.840,00 EUR + NK 271,00 EUR); Verzug nach § 286 BGB, Verzugszinsen § 288 I BGB. Parallel: Mietminderungsankündigung 2025-12-13 wegen ungelöster Reparaturen (unilateral Status), Kündigung durch Mieter 2025-12-12 (beendet Vertrag ab regulärer Kündigungsfrist); Mahnstufe 1 aktiv — offener Betrag bleibt bis Auszugstermin geschuldet [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-021).<!-- /auto:provenance.summary -->

<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `kontoauszug_2024_2025-csv` | bank | [bank/kontoauszug_2024_2025.csv](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv) | 2026-04-26 |
| `20240109_114200_EMAIL-00067-eml` | email | [emails/2024-01/20240109_114200_EMAIL-00067.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240109_114200_EMAIL-00067.eml) | 2024-01-09T11:42:00+00:00 |
| `20240201_132300_EMAIL-00267-eml` | email | [emails/2024-02/20240201_132300_EMAIL-00267.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240201_132300_EMAIL-00267.eml) | 2024-02-01T13:23:00+00:00 |
| `20240202_172300_EMAIL-00278-eml` | email | [emails/2024-02/20240202_172300_EMAIL-00278.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240202_172300_EMAIL-00278.eml) | 2024-02-02T17:23:00+00:00 |
| `20240212_171700_EMAIL-00365-eml` | email | [emails/2024-02/20240212_171700_EMAIL-00365.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240212_171700_EMAIL-00365.eml) | 2024-02-12T17:17:00+00:00 |
| `20240213_011700_EMAIL-00367-eml` | email | [emails/2024-02/20240213_011700_EMAIL-00367.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240213_011700_EMAIL-00367.eml) | 2024-02-13T01:17:00+00:00 |
| `20240216_091400_EMAIL-00397-eml` | email | [emails/2024-02/20240216_091400_EMAIL-00397.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240216_091400_EMAIL-00397.eml) | 2024-02-16T09:14:00+00:00 |
| `20240219_133400_EMAIL-00417-eml` | email | [emails/2024-02/20240219_133400_EMAIL-00417.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240219_133400_EMAIL-00417.eml) | 2024-02-19T13:34:00+00:00 |
| `20240330_083600_EMAIL-00772-eml` | email | [emails/2024-03/20240330_083600_EMAIL-00772.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240330_083600_EMAIL-00772.eml) | 2024-03-30T08:36:00+00:00 |
| `20240331_144300_EMAIL-00783-eml` | email | [emails/2024-03/20240331_144300_EMAIL-00783.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240331_144300_EMAIL-00783.eml) | 2024-03-31T14:43:00+00:00 |
| `20240412_112800_EMAIL-00912-eml` | email | [emails/2024-04/20240412_112800_EMAIL-00912.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240412_112800_EMAIL-00912.eml) | 2024-04-12T11:28:00+00:00 |
| `20240413_093500_EMAIL-00923-eml` | email | [emails/2024-04/20240413_093500_EMAIL-00923.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240413_093500_EMAIL-00923.eml) | 2024-04-13T09:35:00+00:00 |
| `20240423_213500_EMAIL-01031-eml` | email | [emails/2024-04/20240423_213500_EMAIL-01031.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240423_213500_EMAIL-01031.eml) | 2024-04-23T21:35:00+00:00 |
| `20240501_115100_EMAIL-01086-eml` | email | [emails/2024-05/20240501_115100_EMAIL-01086.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240501_115100_EMAIL-01086.eml) | 2024-05-01T11:51:00+00:00 |
| `20240509_135400_EMAIL-01164-eml` | email | [emails/2024-05/20240509_135400_EMAIL-01164.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240509_135400_EMAIL-01164.eml) | 2024-05-09T13:54:00+00:00 |
| `20240523_150500_EMAIL-01288-eml` | email | [emails/2024-05/20240523_150500_EMAIL-01288.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240523_150500_EMAIL-01288.eml) | 2024-05-23T15:05:00+00:00 |
| `20240528_134500_EMAIL-01330-eml` | email | [emails/2024-05/20240528_134500_EMAIL-01330.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240528_134500_EMAIL-01330.eml) | 2024-05-28T13:45:00+00:00 |
| `20240529_194500_EMAIL-01345-eml` | email | [emails/2024-05/20240529_194500_EMAIL-01345.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240529_194500_EMAIL-01345.eml) | 2024-05-29T19:45:00+00:00 |
| `20240602_085600_EMAIL-01381-eml` | email | [emails/2024-06/20240602_085600_EMAIL-01381.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240602_085600_EMAIL-01381.eml) | 2024-06-02T08:56:00+00:00 |
| `20240602_144000_EMAIL-01386-eml` | email | [emails/2024-06/20240602_144000_EMAIL-01386.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240602_144000_EMAIL-01386.eml) | 2024-06-02T14:40:00+00:00 |
| `20240603_104500_EMAIL-01393-eml` | email | [emails/2024-06/20240603_104500_EMAIL-01393.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240603_104500_EMAIL-01393.eml) | 2024-06-03T10:45:00+00:00 |
| `20240605_125100_EMAIL-01409-eml` | email | [emails/2024-06/20240605_125100_EMAIL-01409.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240605_125100_EMAIL-01409.eml) | 2024-06-05T12:51:00+00:00 |
| `20240610_094600_EMAIL-01450-eml` | email | [emails/2024-06/20240610_094600_EMAIL-01450.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240610_094600_EMAIL-01450.eml) | 2024-06-10T09:46:00+00:00 |
| `20240613_090400_EMAIL-01481-eml` | email | [emails/2024-06/20240613_090400_EMAIL-01481.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240613_090400_EMAIL-01481.eml) | 2024-06-13T09:04:00+00:00 |
| `20240614_023700_EMAIL-01489-eml` | email | [emails/2024-06/20240614_023700_EMAIL-01489.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240614_023700_EMAIL-01489.eml) | 2024-06-14T02:37:00+00:00 |
| `20240704_163400_EMAIL-01656-eml` | email | [emails/2024-07/20240704_163400_EMAIL-01656.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240704_163400_EMAIL-01656.eml) | 2024-07-04T16:34:00+00:00 |
| `20240715_091400_EMAIL-01768-eml` | email | [emails/2024-07/20240715_091400_EMAIL-01768.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240715_091400_EMAIL-01768.eml) | 2024-07-15T09:14:00+00:00 |
| `20240718_191400_EMAIL-01804-eml` | email | [emails/2024-07/20240718_191400_EMAIL-01804.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240718_191400_EMAIL-01804.eml) | 2024-07-18T19:14:00+00:00 |
| `20240720_170200_EMAIL-01816-eml` | email | [emails/2024-07/20240720_170200_EMAIL-01816.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240720_170200_EMAIL-01816.eml) | 2024-07-20T17:02:00+00:00 |
| `20240809_162900_EMAIL-02003-eml` | email | [emails/2024-08/20240809_162900_EMAIL-02003.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240809_162900_EMAIL-02003.eml) | 2024-08-09T16:29:00+00:00 |
| `20240820_111000_EMAIL-02104-eml` | email | [emails/2024-08/20240820_111000_EMAIL-02104.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240820_111000_EMAIL-02104.eml) | 2024-08-20T11:10:00+00:00 |
| `20240909_201300_EMAIL-02306-eml` | email | [emails/2024-09/20240909_201300_EMAIL-02306.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240909_201300_EMAIL-02306.eml) | 2024-09-09T20:13:00+00:00 |
| `20240920_165400_EMAIL-02391-eml` | email | [emails/2024-09/20240920_165400_EMAIL-02391.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240920_165400_EMAIL-02391.eml) | 2024-09-20T16:54:00+00:00 |
| `20241005_142800_EMAIL-02528-eml` | email | [emails/2024-10/20241005_142800_EMAIL-02528.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241005_142800_EMAIL-02528.eml) | 2024-10-05T14:28:00+00:00 |
| `20241011_093900_EMAIL-02588-eml` | email | [emails/2024-10/20241011_093900_EMAIL-02588.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241011_093900_EMAIL-02588.eml) | 2024-10-11T09:39:00+00:00 |
| `20241015_173200_EMAIL-02621-eml` | email | [emails/2024-10/20241015_173200_EMAIL-02621.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241015_173200_EMAIL-02621.eml) | 2024-10-15T17:32:00+00:00 |
| `20241016_103800_EMAIL-02625-eml` | email | [emails/2024-10/20241016_103800_EMAIL-02625.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241016_103800_EMAIL-02625.eml) | 2024-10-16T10:38:00+00:00 |
| `20241107_102800_EMAIL-02839-eml` | email | [emails/2024-11/20241107_102800_EMAIL-02839.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241107_102800_EMAIL-02839.eml) | 2024-11-07T10:28:00+00:00 |
| `20241114_151800_EMAIL-02903-eml` | email | [emails/2024-11/20241114_151800_EMAIL-02903.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241114_151800_EMAIL-02903.eml) | 2024-11-14T15:18:00+00:00 |
| `20250101_141900_EMAIL-03345-eml` | email | [emails/2025-01/20250101_141900_EMAIL-03345.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250101_141900_EMAIL-03345.eml) | 2025-01-01T14:19:00+00:00 |
| `20250108_090300_EMAIL-03413-eml` | email | [emails/2025-01/20250108_090300_EMAIL-03413.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250108_090300_EMAIL-03413.eml) | 2025-01-08T09:03:00+00:00 |
| `20250109_144700_EMAIL-03425-eml` | email | [emails/2025-01/20250109_144700_EMAIL-03425.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250109_144700_EMAIL-03425.eml) | 2025-01-09T14:47:00+00:00 |
| `20250109_200300_EMAIL-03426-eml` | email | [emails/2025-01/20250109_200300_EMAIL-03426.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250109_200300_EMAIL-03426.eml) | 2025-01-09T20:03:00+00:00 |
| `20250119_090300_EMAIL-03516-eml` | email | [emails/2025-01/20250119_090300_EMAIL-03516.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250119_090300_EMAIL-03516.eml) | 2025-01-19T09:03:00+00:00 |
| `20250123_105900_EMAIL-03545-eml` | email | [emails/2025-01/20250123_105900_EMAIL-03545.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250123_105900_EMAIL-03545.eml) | 2025-01-23T10:59:00+00:00 |
| `20250126_175800_EMAIL-03571-eml` | email | [emails/2025-01/20250126_175800_EMAIL-03571.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250126_175800_EMAIL-03571.eml) | 2025-01-26T17:58:00+00:00 |
| `20250126_225800_EMAIL-03572-eml` | email | [emails/2025-01/20250126_225800_EMAIL-03572.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250126_225800_EMAIL-03572.eml) | 2025-01-26T22:58:00+00:00 |
| `20250202_101500_EMAIL-03628-eml` | email | [emails/2025-02/20250202_101500_EMAIL-03628.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250202_101500_EMAIL-03628.eml) | 2025-02-02T10:15:00+00:00 |
| `20250219_134000_EMAIL-03784-eml` | email | [emails/2025-02/20250219_134000_EMAIL-03784.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250219_134000_EMAIL-03784.eml) | 2025-02-19T13:40:00+00:00 |
| `20250227_103400_EMAIL-03866-eml` | email | [emails/2025-02/20250227_103400_EMAIL-03866.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250227_103400_EMAIL-03866.eml) | 2025-02-27T10:34:00+00:00 |
| `20250310_083300_EMAIL-03970-eml` | email | [emails/2025-03/20250310_083300_EMAIL-03970.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250310_083300_EMAIL-03970.eml) | 2025-03-10T08:33:00+00:00 |
| `20250311_105400_EMAIL-03985-eml` | email | [emails/2025-03/20250311_105400_EMAIL-03985.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250311_105400_EMAIL-03985.eml) | 2025-03-11T10:54:00+00:00 |
| `20250322_210800_EMAIL-04097-eml` | email | [emails/2025-03/20250322_210800_EMAIL-04097.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250322_210800_EMAIL-04097.eml) | 2025-03-22T21:08:00+00:00 |
| `20250401_122700_EMAIL-04178-eml` | email | [emails/2025-04/20250401_122700_EMAIL-04178.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250401_122700_EMAIL-04178.eml) | 2025-04-01T12:27:00+00:00 |
| `20250428_121500_EMAIL-04389-eml` | email | [emails/2025-04/20250428_121500_EMAIL-04389.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250428_121500_EMAIL-04389.eml) | 2025-04-28T12:15:00+00:00 |
| `20250514_122100_EMAIL-04515-eml` | email | [emails/2025-05/20250514_122100_EMAIL-04515.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250514_122100_EMAIL-04515.eml) | 2025-05-14T12:21:00+00:00 |
| `20250515_032100_EMAIL-04519-eml` | email | [emails/2025-05/20250515_032100_EMAIL-04519.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250515_032100_EMAIL-04519.eml) | 2025-05-15T03:21:00+00:00 |
| `20250516_102100_EMAIL-04534-eml` | email | [emails/2025-05/20250516_102100_EMAIL-04534.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250516_102100_EMAIL-04534.eml) | 2025-05-16T10:21:00+00:00 |
| `20250612_141600_EMAIL-04757-eml` | email | [emails/2025-06/20250612_141600_EMAIL-04757.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250612_141600_EMAIL-04757.eml) | 2025-06-12T14:16:00+00:00 |
| `20250614_021600_EMAIL-04768-eml` | email | [emails/2025-06/20250614_021600_EMAIL-04768.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250614_021600_EMAIL-04768.eml) | 2025-06-14T02:16:00+00:00 |
| `20250628_161200_EMAIL-04896-eml` | email | [emails/2025-06/20250628_161200_EMAIL-04896.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250628_161200_EMAIL-04896.eml) | 2025-06-28T16:12:00+00:00 |
| `20250711_121800_EMAIL-05002-eml` | email | [emails/2025-07/20250711_121800_EMAIL-05002.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250711_121800_EMAIL-05002.eml) | 2025-07-11T12:18:00+00:00 |
| `20250712_180400_EMAIL-05016-eml` | email | [emails/2025-07/20250712_180400_EMAIL-05016.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250712_180400_EMAIL-05016.eml) | 2025-07-12T18:04:00+00:00 |
| `20250728_114000_EMAIL-05146-eml` | email | [emails/2025-07/20250728_114000_EMAIL-05146.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250728_114000_EMAIL-05146.eml) | 2025-07-28T11:40:00+00:00 |
| `20250728_194000_EMAIL-05152-eml` | email | [emails/2025-07/20250728_194000_EMAIL-05152.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250728_194000_EMAIL-05152.eml) | 2025-07-28T19:40:00+00:00 |
| `20250801_184500_EMAIL-05180-eml` | email | [emails/2025-08/20250801_184500_EMAIL-05180.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250801_184500_EMAIL-05180.eml) | 2025-08-01T18:45:00+00:00 |
| `20250802_194500_EMAIL-05189-eml` | email | [emails/2025-08/20250802_194500_EMAIL-05189.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250802_194500_EMAIL-05189.eml) | 2025-08-02T19:45:00+00:00 |
| `20250814_100200_EMAIL-05288-eml` | email | [emails/2025-08/20250814_100200_EMAIL-05288.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250814_100200_EMAIL-05288.eml) | 2025-08-14T10:02:00+00:00 |
| `20250814_114900_EMAIL-05292-eml` | email | [emails/2025-08/20250814_114900_EMAIL-05292.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250814_114900_EMAIL-05292.eml) | 2025-08-14T11:49:00+00:00 |
| `20250814_130200_EMAIL-05293-eml` | email | [emails/2025-08/20250814_130200_EMAIL-05293.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250814_130200_EMAIL-05293.eml) | 2025-08-14T13:02:00+00:00 |
| `20250814_172000_EMAIL-05297-eml` | email | [emails/2025-08/20250814_172000_EMAIL-05297.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250814_172000_EMAIL-05297.eml) | 2025-08-14T17:20:00+00:00 |
| `20250820_130200_EMAIL-05357-eml` | email | [emails/2025-08/20250820_130200_EMAIL-05357.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250820_130200_EMAIL-05357.eml) | 2025-08-20T13:02:00+00:00 |
| `20250821_132500_EMAIL-05365-eml` | email | [emails/2025-08/20250821_132500_EMAIL-05365.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250821_132500_EMAIL-05365.eml) | 2025-08-21T13:25:00+00:00 |
| `20250827_133700_EMAIL-05419-eml` | email | [emails/2025-08/20250827_133700_EMAIL-05419.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250827_133700_EMAIL-05419.eml) | 2025-08-27T13:37:00+00:00 |
| `20250830_052500_EMAIL-05451-eml` | email | [emails/2025-08/20250830_052500_EMAIL-05451.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250830_052500_EMAIL-05451.eml) | 2025-08-30T05:25:00+00:00 |
| `20250901_150900_EMAIL-05480-eml` | email | [emails/2025-09/20250901_150900_EMAIL-05480.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250901_150900_EMAIL-05480.eml) | 2025-09-01T15:09:00+00:00 |
| `20250905_161500_EMAIL-05531-eml` | email | [emails/2025-09/20250905_161500_EMAIL-05531.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250905_161500_EMAIL-05531.eml) | 2025-09-05T16:15:00+00:00 |
| `20251009_111400_EMAIL-05820-eml` | email | [emails/2025-10/20251009_111400_EMAIL-05820.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251009_111400_EMAIL-05820.eml) | 2025-10-09T11:14:00+00:00 |
| `20251020_090300_EMAIL-05914-eml` | email | [emails/2025-10/20251020_090300_EMAIL-05914.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251020_090300_EMAIL-05914.eml) | 2025-10-20T09:03:00+00:00 |
| `20251107_161300_EMAIL-06075-eml` | email | [emails/2025-11/20251107_161300_EMAIL-06075.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251107_161300_EMAIL-06075.eml) | 2025-11-07T16:13:00+00:00 |
| `20251124_123500_EMAIL-06212-eml` | email | [emails/2025-11/20251124_123500_EMAIL-06212.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251124_123500_EMAIL-06212.eml) | 2025-11-24T12:35:00+00:00 |
| `20251212_145500_EMAIL-06367-eml` | email | [emails/2025-12/20251212_145500_EMAIL-06367.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251212_145500_EMAIL-06367.eml) | 2025-12-12T14:55:00+00:00 |
| `20251212_160200_EMAIL-06369-eml` | email | [emails/2025-12/20251212_160200_EMAIL-06369.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251212_160200_EMAIL-06369.eml) | 2025-12-12T16:02:00+00:00 |
| `20251213_081200_EMAIL-06373-eml` | email | [emails/2025-12/20251213_081200_EMAIL-06373.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251213_081200_EMAIL-06373.eml) | 2025-12-13T08:12:00+00:00 |
| `20251213_095500_EMAIL-06377-eml` | email | [emails/2025-12/20251213_095500_EMAIL-06377.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251213_095500_EMAIL-06377.eml) | 2025-12-13T09:55:00+00:00 |
| `20251221_115400_EMAIL-06453-eml` | email | [emails/2025-12/20251221_115400_EMAIL-06453.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251221_115400_EMAIL-06453.eml) | 2025-12-21 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-26T09:26:19+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
