# context.unit.<!-- auto:unit_id -->EH-037<!-- /auto:unit_id -->.md

> Per-unit dossier (one file per Einheit). Holds everything specific to this unit:
> the unit itself, the active lease, the tenant(s), and all unit/tenant-specific operations.
> **Property-wide data lives in `context.property.md`** — see `parent_property_ref` below.

<!-- auto:meta -->
- last_built_at: `2026-04-26T09:39:05+00:00`
- build_hash: `engine-v2`
- engine_version: `0.2.0`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `unit`
- unit_id: `EH-037`
- property_id: `LIE-001`
- parent_property_ref: `context.property.LIE-001.md`
- owner_ref: `EIG-001`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit.summary -->[Administrative] Gewerbeeinheit GE 37 (142 m², Miteigentumsanteil 348/10000, EG Ladenlokal) zeigt Hausgeldzahlung 32,51 EUR vom 2025-12-05 [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#einheit/EH-037), gleichzeitig Untermietzusage (Status: requested, 2025-06-04) und offene Nebenkostenfrage (2025-11-04). Vertraglich zu klären: Untermiete erfordert Zustimmung gem. Mietvertrag und WEG-Beschluss; Nebenkosten nach § 556 BGB Abs. 3 + BetrKV zu dokumentieren. Nächster Schritt: Untermietzustimmung (Frist 1 Monat nach Anfrage, läuft noch), Nebenkostenabrechnung 2025 vor 2026-12-31 vorlegen.<!-- /auto:unit.summary -->

<!-- auto:unit -->
- unit_id: `EH-037`
- label: GE 37
- haus_id: `HAUS-14`
- floor: EG Ladenlokal
- position: _(no data in source yet)_
- typ: Gewerbe
- area_sqm: 142.0
- rooms: _(no data in source yet)_
- mea_‰: 348
- equipment: _(no data in source yet)_
- media_supply: _(no data in source yet)_
- key_inventory: _(no data in source yet)_
- meters: _(no data in source yet)_
- occupancy_status: `rented`
- nk_keys: _(no data in source yet)_
<!-- /auto:unit -->

---

## 2. Lease (Mietverhältnis, voll)
<!-- auto:lease.summary -->[Administrative] Mieter MIE-023 (Björn Weinhage, EH-037) hat Mietvertrag zweimal gekündigt — zunächst 2025-03-25 [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250325_105100_EMAIL-04116.eml), dann erneut 2025-12-22 [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251222_093100_EMAIL-06466.eml); beide mit Verweis auf fristgerechte Kündigung zum nächstmöglichen Termin. Mietbeginn 2020-08-11, Kaltmiete 3.661,00 EUR + NK 435,00 EUR, Kaution 10.983,00 EUR [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-023). § 573 BGB (ordentliche Kündigung, dreimomentig) und § 574 BGB (Bestätigungspflicht des Vermieters) erfordern unverzügliche schriftliche Bestätigung des genauen Beendigungstermins; offene Kündigungsbestätigung und Status der Kaution sind klärungsbedürftig — zweite Kündigung deutet auf fehlende Rückmeldung zur ersten<!-- /auto:lease.summary -->

<!-- auto:lease -->
- lease_id: `LEASE-MIE-023`
- unit_ref: `EH-037`
- start_date: 2020-08-11 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-023)
- end_date: _(no data in source yet)_
- term_type: `unbefristet`
- cancellation_status: `by_tenant` (notice_date: 2025-12-22, move_out_date: —)
- rent_components: { kaltmiete: 3661.0, betriebskosten_vorauszahlung: 435.0, total_warmmiete: 4096.00 }
- payment_mode: Überweisung
- iban_payer: DE97100500009084700766 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-023)
- kaution: { amount: 10983.0 }
- usage: `residential`
- subletting: { current_status: `requested` }
- special_agreements: _(no data in source yet)_
<!-- /auto:lease -->

### 2.1 Tenants on this Lease
<!-- auto:tenants.summary -->_no issue_<!-- /auto:tenants.summary -->

<!-- auto:tenants -->
| tenant_id | name | role | contact_email | contact_phone | comms_pref | gesamtschuldner |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-023` | Herr Björn Weinhage | haupt | bjoern.weinhage@gmx.de | +49(0)7758 917839 | email | — |
<!-- /auto:tenants -->

---

## 3. Operations (this unit / this tenant)

### 3.1 Open Tickets — Critical (overdue or due ≤7 days)
<!-- auto:tickets.critical.summary -->[Routine] Mieter EH-037 meldet seit 2025-11-07 verstopften Abfluss in der Dusche, den er selbst mit Pumpversuch nicht beheben konnte. Vertraglich geschuldet ist die Instandhaltung von Abflussanlagen durch Vermieter gemäß § 535 I BGB (Erhaltung der Mietsache in gebrauchsfähigem Zustand). Ticket geöffnet 2025-11-07, Severity normal — Handwerkereinsatz erforderlich zur Feststellung, ob Verschulden Mieter oder Bauwerk.<!-- /auto:tickets.critical.summary -->

<!-- auto:tickets.critical -->
| ticket_id | type | title | deadline | status | assignee |
| --- | --- | --- | --- | --- | --- |
| `TKT-01deac36` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-a9668576` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-ffb0f2c6` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-d4a9d2f9` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-f8cfc3ad` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-65b39b5f` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-9085b593` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-23d65ad3` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-63969d31` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-eac40ac6` | wasserschaden | Wasserschaden Bad | — | open | — |
<!-- /auto:tickets.critical -->

### 3.2 Open Tickets — Aggregate
<!-- auto:tickets.aggregate.summary -->[Routine] Einheit EH-037: Verstopfter Abfluss, gemeldet 2025-11-07, Schweregrad normal [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240113_104100_EMAIL-00106.eml). Abflussreparaturen fallen unter die Verkehrssicherungspflicht des Vermieters (§ 535 I BGB); instandhaltungspflichtig als Bestandteil der Mietsache. Ticket steht seit 171 Tagen offen — Reparaturzeitlimit (2–4 Wochen je nach Dringlichkeit) überschritten; Folgemaßnahme erforderlich.<!-- /auto:tickets.aggregate.summary -->

<!-- auto:tickets.aggregate -->
- total_open: `29`
- by_type: { abfluss: `4`, fenster: `11`, schimmel: `4`, schluessel: `4`, wasserschaden: `6` }
- live source: `db.tickets WHERE unit_id=EH-037 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren

<!-- auto:dunning.summary -->[Routine] Mieter MIE-023 ist seit vier Monaten im Verzug; offener Betrag 16.384,00 EUR zzgl. 213,67 EUR Verzugszinsen, letzte Zahlung 2025-12-03 [(bank)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv#TX-01590). Vertraglich geschuldet sind monatlich 4.096,00 EUR (Kaltmiete 3.661,00 EUR + NK 435,00 EUR) [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-023). Verzug nach § 286 BGB festgestellt, Verzugszinsen nach § 288 I BGB; Mahnstufe 1 aktiv, nächster Schritt: 2. Mahnung nach 14 Tagen.<!-- /auto:dunning.summary -->

#### Per claim
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-023` | — | 1 | 16384.00 EUR | 2025-12-03 | — | — |
- live balance pointer: `db.tenant_balance.tenant_id=MIE-023`
<!-- /auto:dunning -->

### 3.4 Active Reductions / Deferrals (§ 536 BGB)
<!-- auto:reductions.summary -->[Emergency] Mieter EH-037 kündigte Mietminderung um 15% an (erstmals 2024-03-11, zuletzt 2025-07-29 für ab 2025-08-28), begründet mit ungelöstem Wasserschaden und Schimmel seit über 3 Monaten [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250729_141100_EMAIL-05156.eml). Verwaltung bestätigte Handwerkerbeauftragung 2025-02-11, doch keine Nachfassung dokumentiert; Mangel besteht seit mindestens 2024-02, d.h. über 2 Jahre ungelöst. Mietminderungsrecht nach § 536 I BGB greift bei erheblichen Mängeln, die Gebrauchstauglichkeit beeinträchtigen; Verzögerung der Mängelbeseitigung über 24 Monate ohne Abschluss begründet Minderungsanspruch rückwirkend — sofortige Handwerkerleistung und Dokumentation erforderlich zur Schadensabwehr.<!-- /auto:reductions.summary -->

<!-- auto:reductions -->
- date_raised: 2024-03-11
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-03-11
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-05-12
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-08-13
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-02-11
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-02-11
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-02-26
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-07-29
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-08-02
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- *trigger: HITL exit if any entry present*
<!-- /auto:reductions -->

### 3.5 Latest Übergabeprotokoll
<!-- auto:handover.summary -->_no issue_<!-- /auto:handover.summary -->

<!-- auto:handover -->_(no data in source yet)_<!-- /auto:handover -->

### 3.6 Recurring Process State (this unit, in-flight)
<!-- auto:recurring.summary -->[Routine] Mieter MIE-023 hat den Mietvertrag für Einheit EH-037 zweimal eingereicht — erstmals 2025-03-25 [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250325_105100_EMAIL-04116.eml) und erneut 2025-12-22 [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251222_093100_EMAIL-06466.eml). Beide Schreiben berufen sich auf fristgerechte Kündigung zum nächstmöglichen Termin, ohne dass eine Bestätigung des ersten Kündigungstermins dokumentiert ist. Prüfung erforderlich: Welcher Kündigungstermin ist wirksam geworden (§ 573 BGB), und warum wurde die März-Kündigung nicht bestätigt oder abgeschlossen?<!-- /auto:recurring.summary -->

<!-- auto:recurring -->
| process_type | started | current_step | owner | eta | blockers |
| --- | --- | --- | --- | --- | --- |
| Mieterwechsel | 2025-12-22 | Kündigung erhalten | Verwaltung | TBD | Übergabe-Termin offen |
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
<!-- auto:sticky-threads.summary -->[Emergency] Mieter MIE-023 meldet seit 2024-01-10 aktiven Wasserschaden im Bad (WE 21); Thread mit 114 Nachrichten, letzte Meldung 2025-12-24 [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251224_103700_EMAIL-06481.eml). Wasser tropft aus Decke, Quelle vermutlich Wohnung darüber — Gefahr für Schimmelbildung und Strukturschaden nach § 536 I BGB (Mangelhaftung, Mieter Minderungsrecht). Sofortmaßnahme erforderlich: Handwerkerauftrag, Schadensumfang dokumentieren, Versicherung benachrichtigen, Ursachenklärung (obere Wohnung prüfen).<!-- /auto:sticky-threads.summary -->

<!-- auto:sticky-threads -->
| thread_id | subject | last_msg_date | parties | status | one-line outcome | pointer |
| --- | --- | --- | --- | --- | --- | --- |
| `TH-711abd` | Defektes Fenster | 2025-12-23 | `MIE-023` | active | 128 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251223_150600_EMAIL-06476.eml) |
| `TH-d13043` | Wasserschaden Bad | 2025-12-24 | `MIE-023` | active | 114 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251224_103700_EMAIL-06481.eml) |
| `TH-9cb87c` | Mieterwechsel in GE 37 | 2025-10-06 | `EH-037` | active | 5 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251006_222800_EMAIL-05801.eml) |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance.summary -->[Routine] Mieter MIE-023 (Björn Weinhage, Gewerbeeinheit GE 37, Mietbeginn 2020-08-11) ist seit vier Monaten im Verzug; offener Betrag 16.384,00 EUR zzgl. 213,67 EUR Verzugszinsen, letzte Zahlung 2025-12-03 [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-023). Vertraglich geschuldet sind monatlich 4.096,00 EUR (Kaltmiete 3.661,00 EUR + NK 435,00 EUR); Mahnstufe 1 seit 2026-04-26. Verzug nach § 286 BGB festgestellt, Verzugszinsen § 288 I BGB (Basiszins 3,5 % + 5 pp). Notiz: Mieter hat Kündigungsmitteilung am 2025-12-22 eingereicht; Wasserschaden-Ticket (seit 2024-01-10, aktiv) parallel in Bearbeitung — Entgeltkürzungsanspruch § 536 BGB prüfen bei Kalkulation des ausstehenden Betrags.<!-- /auto:provenance.summary -->

<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `kontoauszug_2024_2025-csv` | bank | [bank/kontoauszug_2024_2025.csv](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv) | 2026-04-26 |
| `20240109_164500_EMAIL-00073-eml` | email | [emails/2024-01/20240109_164500_EMAIL-00073.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240109_164500_EMAIL-00073.eml) | 2024-01-09T16:45:00+00:00 |
| `20240113_104100_EMAIL-00106-eml` | email | [emails/2024-01/20240113_104100_EMAIL-00106.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240113_104100_EMAIL-00106.eml) | 2024-01-13T10:41:00+00:00 |
| `20240114_074100_EMAIL-00114-eml` | email | [emails/2024-01/20240114_074100_EMAIL-00114.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240114_074100_EMAIL-00114.eml) | 2024-01-14T07:41:00+00:00 |
| `20240121_074100_EMAIL-00167-eml` | email | [emails/2024-01/20240121_074100_EMAIL-00167.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240121_074100_EMAIL-00167.eml) | 2024-01-21T07:41:00+00:00 |
| `20240123_060900_EMAIL-00183-eml` | email | [emails/2024-01/20240123_060900_EMAIL-00183.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240123_060900_EMAIL-00183.eml) | 2024-01-23T06:09:00+00:00 |
| `20240126_125800_EMAIL-00204-eml` | email | [emails/2024-01/20240126_125800_EMAIL-00204.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240126_125800_EMAIL-00204.eml) | 2024-01-26T12:58:00+00:00 |
| `20240127_085800_EMAIL-00211-eml` | email | [emails/2024-01/20240127_085800_EMAIL-00211.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240127_085800_EMAIL-00211.eml) | 2024-01-27T08:58:00+00:00 |
| `20240130_145300_EMAIL-00244-eml` | email | [emails/2024-01/20240130_145300_EMAIL-00244.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240130_145300_EMAIL-00244.eml) | 2024-01-30T14:53:00+00:00 |
| `20240225_103500_EMAIL-00463-eml` | email | [emails/2024-02/20240225_103500_EMAIL-00463.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240225_103500_EMAIL-00463.eml) | 2024-02-25T10:35:00+00:00 |
| `20240227_133500_EMAIL-00489-eml` | email | [emails/2024-02/20240227_133500_EMAIL-00489.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240227_133500_EMAIL-00489.eml) | 2024-02-27T13:35:00+00:00 |
| `20240228_103200_EMAIL-00492-eml` | email | [emails/2024-02/20240228_103200_EMAIL-00492.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240228_103200_EMAIL-00492.eml) | 2024-02-28T10:32:00+00:00 |
| `20240311_101500_EMAIL-00614-eml` | email | [emails/2024-03/20240311_101500_EMAIL-00614.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240311_101500_EMAIL-00614.eml) | 2024-03-11T10:15:00+00:00 |
| `20240311_171500_EMAIL-00621-eml` | email | [emails/2024-03/20240311_171500_EMAIL-00621.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240311_171500_EMAIL-00621.eml) | 2024-03-11T17:15:00+00:00 |
| `20240401_130300_EMAIL-00788-eml` | email | [emails/2024-04/20240401_130300_EMAIL-00788.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240401_130300_EMAIL-00788.eml) | 2024-04-01T13:03:00+00:00 |
| `20240402_010300_EMAIL-00796-eml` | email | [emails/2024-04/20240402_010300_EMAIL-00796.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240402_010300_EMAIL-00796.eml) | 2024-04-02T01:03:00+00:00 |
| `20240408_090800_EMAIL-00864-eml` | email | [emails/2024-04/20240408_090800_EMAIL-00864.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240408_090800_EMAIL-00864.eml) | 2024-04-08T09:08:00+00:00 |
| `20240408_100500_EMAIL-00866-eml` | email | [emails/2024-04/20240408_100500_EMAIL-00866.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240408_100500_EMAIL-00866.eml) | 2024-04-08T10:05:00+00:00 |
| `20240423_174900_EMAIL-01029-eml` | email | [emails/2024-04/20240423_174900_EMAIL-01029.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240423_174900_EMAIL-01029.eml) | 2024-04-23T17:49:00+00:00 |
| `20240427_101200_EMAIL-01054-eml` | email | [emails/2024-04/20240427_101200_EMAIL-01054.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240427_101200_EMAIL-01054.eml) | 2024-04-27T10:12:00+00:00 |
| `20240512_115100_EMAIL-01188-eml` | email | [emails/2024-05/20240512_115100_EMAIL-01188.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240512_115100_EMAIL-01188.eml) | 2024-05-12T11:51:00+00:00 |
| `20240525_113000_EMAIL-01299-eml` | email | [emails/2024-05/20240525_113000_EMAIL-01299.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240525_113000_EMAIL-01299.eml) | 2024-05-25T11:30:00+00:00 |
| `20240531_143200_EMAIL-01365-eml` | email | [emails/2024-05/20240531_143200_EMAIL-01365.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240531_143200_EMAIL-01365.eml) | 2024-05-31T14:32:00+00:00 |
| `20240531_143600_EMAIL-01366-eml` | email | [emails/2024-05/20240531_143600_EMAIL-01366.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240531_143600_EMAIL-01366.eml) | 2024-05-31T14:36:00+00:00 |
| `20240609_150400_EMAIL-01442-eml` | email | [emails/2024-06/20240609_150400_EMAIL-01442.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240609_150400_EMAIL-01442.eml) | 2024-06-09T15:04:00+00:00 |
| `20240610_040400_EMAIL-01448-eml` | email | [emails/2024-06/20240610_040400_EMAIL-01448.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240610_040400_EMAIL-01448.eml) | 2024-06-10T04:04:00+00:00 |
| `20240613_031100_EMAIL-01480-eml` | email | [emails/2024-06/20240613_031100_EMAIL-01480.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240613_031100_EMAIL-01480.eml) | 2024-06-13T03:11:00+00:00 |
| `20240623_150600_EMAIL-01575-eml` | email | [emails/2024-06/20240623_150600_EMAIL-01575.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240623_150600_EMAIL-01575.eml) | 2024-06-23T15:06:00+00:00 |
| `20240626_203800_EMAIL-01596-eml` | email | [emails/2024-06/20240626_203800_EMAIL-01596.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240626_203800_EMAIL-01596.eml) | 2024-06-26T20:38:00+00:00 |
| `20240703_113900_EMAIL-01644-eml` | email | [emails/2024-07/20240703_113900_EMAIL-01644.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240703_113900_EMAIL-01644.eml) | 2024-07-03T11:39:00+00:00 |
| `20240705_201700_EMAIL-01668-eml` | email | [emails/2024-07/20240705_201700_EMAIL-01668.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240705_201700_EMAIL-01668.eml) | 2024-07-05T20:17:00+00:00 |
| `20240710_153700_EMAIL-01725-eml` | email | [emails/2024-07/20240710_153700_EMAIL-01725.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240710_153700_EMAIL-01725.eml) | 2024-07-10T15:37:00+00:00 |
| `20240712_105200_EMAIL-01741-eml` | email | [emails/2024-07/20240712_105200_EMAIL-01741.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240712_105200_EMAIL-01741.eml) | 2024-07-12T10:52:00+00:00 |
| `20240725_152000_EMAIL-01858-eml` | email | [emails/2024-07/20240725_152000_EMAIL-01858.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240725_152000_EMAIL-01858.eml) | 2024-07-25T15:20:00+00:00 |
| `20240731_143600_EMAIL-01913-eml` | email | [emails/2024-07/20240731_143600_EMAIL-01913.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240731_143600_EMAIL-01913.eml) | 2024-07-31T14:36:00+00:00 |
| `20240813_093800_EMAIL-02022-eml` | email | [emails/2024-08/20240813_093800_EMAIL-02022.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240813_093800_EMAIL-02022.eml) | 2024-08-13T09:38:00+00:00 |
| `20240823_141900_EMAIL-02131-eml` | email | [emails/2024-08/20240823_141900_EMAIL-02131.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240823_141900_EMAIL-02131.eml) | 2024-08-23T14:19:00+00:00 |
| `20240904_103300_EMAIL-02239-eml` | email | [emails/2024-09/20240904_103300_EMAIL-02239.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240904_103300_EMAIL-02239.eml) | 2024-09-04T10:33:00+00:00 |
| `20241007_172100_EMAIL-02551-eml` | email | [emails/2024-10/20241007_172100_EMAIL-02551.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241007_172100_EMAIL-02551.eml) | 2024-10-07T17:21:00+00:00 |
| `20241010_081200_EMAIL-02577-eml` | email | [emails/2024-10/20241010_081200_EMAIL-02577.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241010_081200_EMAIL-02577.eml) | 2024-10-10T08:12:00+00:00 |
| `20241010_181200_EMAIL-02584-eml` | email | [emails/2024-10/20241010_181200_EMAIL-02584.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241010_181200_EMAIL-02584.eml) | 2024-10-10T18:12:00+00:00 |
| `20241201_224600_EMAIL-03063-eml` | email | [emails/2024-12/20241201_224600_EMAIL-03063.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241201_224600_EMAIL-03063.eml) | 2024-12-01T22:46:00+00:00 |
| `20241202_044600_EMAIL-03065-eml` | email | [emails/2024-12/20241202_044600_EMAIL-03065.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241202_044600_EMAIL-03065.eml) | 2024-12-02T04:46:00+00:00 |
| `20241207_110200_EMAIL-03110-eml` | email | [emails/2024-12/20241207_110200_EMAIL-03110.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241207_110200_EMAIL-03110.eml) | 2024-12-07T11:02:00+00:00 |
| `20241210_105600_EMAIL-03138-eml` | email | [emails/2024-12/20241210_105600_EMAIL-03138.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241210_105600_EMAIL-03138.eml) | 2024-12-10T10:56:00+00:00 |
| `20241220_111200_EMAIL-03216-eml` | email | [emails/2024-12/20241220_111200_EMAIL-03216.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241220_111200_EMAIL-03216.eml) | 2024-12-20T11:12:00+00:00 |
| `20241231_115300_EMAIL-03328-eml` | email | [emails/2024-12/20241231_115300_EMAIL-03328.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241231_115300_EMAIL-03328.eml) | 2024-12-31T11:53:00+00:00 |
| `20241231_152400_EMAIL-03335-eml` | email | [emails/2024-12/20241231_152400_EMAIL-03335.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241231_152400_EMAIL-03335.eml) | 2024-12-31T15:24:00+00:00 |
| `20250108_091400_EMAIL-03414-eml` | email | [emails/2025-01/20250108_091400_EMAIL-03414.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250108_091400_EMAIL-03414.eml) | 2025-01-08T09:14:00+00:00 |
| `20250111_032400_EMAIL-03436-eml` | email | [emails/2025-01/20250111_032400_EMAIL-03436.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250111_032400_EMAIL-03436.eml) | 2025-01-11T03:24:00+00:00 |
| `20250211_120400_EMAIL-03697-eml` | email | [emails/2025-02/20250211_120400_EMAIL-03697.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250211_120400_EMAIL-03697.eml) | 2025-02-11T12:04:00+00:00 |
| `20250211_170400_EMAIL-03699-eml` | email | [emails/2025-02/20250211_170400_EMAIL-03699.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250211_170400_EMAIL-03699.eml) | 2025-02-11T17:04:00+00:00 |
| `20250220_165600_EMAIL-03797-eml` | email | [emails/2025-02/20250220_165600_EMAIL-03797.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250220_165600_EMAIL-03797.eml) | 2025-02-20T16:56:00+00:00 |
| `20250226_150700_EMAIL-03860-eml` | email | [emails/2025-02/20250226_150700_EMAIL-03860.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250226_150700_EMAIL-03860.eml) | 2025-02-26T15:07:00+00:00 |
| `20250301_110200_EMAIL-03886-eml` | email | [emails/2025-03/20250301_110200_EMAIL-03886.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250301_110200_EMAIL-03886.eml) | 2025-03-01T11:02:00+00:00 |
| `20250307_111500_EMAIL-03942-eml` | email | [emails/2025-03/20250307_111500_EMAIL-03942.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250307_111500_EMAIL-03942.eml) | 2025-03-07T11:15:00+00:00 |
| `20250315_112900_EMAIL-04020-eml` | email | [emails/2025-03/20250315_112900_EMAIL-04020.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250315_112900_EMAIL-04020.eml) | 2025-03-15T11:29:00+00:00 |
| `20250316_192900_EMAIL-04032-eml` | email | [emails/2025-03/20250316_192900_EMAIL-04032.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250316_192900_EMAIL-04032.eml) | 2025-03-16T19:29:00+00:00 |
| `20250318_131400_EMAIL-04053-eml` | email | [emails/2025-03/20250318_131400_EMAIL-04053.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250318_131400_EMAIL-04053.eml) | 2025-03-18T13:14:00+00:00 |
| `20250318_191400_EMAIL-04060-eml` | email | [emails/2025-03/20250318_191400_EMAIL-04060.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250318_191400_EMAIL-04060.eml) | 2025-03-18T19:14:00+00:00 |
| `20250325_105100_EMAIL-04116-eml` | email | [emails/2025-03/20250325_105100_EMAIL-04116.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250325_105100_EMAIL-04116.eml) | 2025-03-25T10:51:00+00:00 |
| `20250325_192900_EMAIL-04122-eml` | email | [emails/2025-03/20250325_192900_EMAIL-04122.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250325_192900_EMAIL-04122.eml) | 2025-03-25T19:29:00+00:00 |
| `20250328_191400_EMAIL-04147-eml` | email | [emails/2025-03/20250328_191400_EMAIL-04147.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250328_191400_EMAIL-04147.eml) | 2025-03-28T19:14:00+00:00 |
| `20250329_120300_EMAIL-04150-eml` | email | [emails/2025-03/20250329_120300_EMAIL-04150.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250329_120300_EMAIL-04150.eml) | 2025-03-29T12:03:00+00:00 |
| `20250330_060300_EMAIL-04155-eml` | email | [emails/2025-03/20250330_060300_EMAIL-04155.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250330_060300_EMAIL-04155.eml) | 2025-03-30T06:03:00+00:00 |
| `20250331_172800_EMAIL-04170-eml` | email | [emails/2025-03/20250331_172800_EMAIL-04170.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250331_172800_EMAIL-04170.eml) | 2025-03-31T17:28:00+00:00 |
| `20250419_134700_EMAIL-04329-eml` | email | [emails/2025-04/20250419_134700_EMAIL-04329.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250419_134700_EMAIL-04329.eml) | 2025-04-19T13:47:00+00:00 |
| `20250419_153300_EMAIL-04331-eml` | email | [emails/2025-04/20250419_153300_EMAIL-04331.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250419_153300_EMAIL-04331.eml) | 2025-04-19T15:33:00+00:00 |
| `20250429_161400_EMAIL-04398-eml` | email | [emails/2025-04/20250429_161400_EMAIL-04398.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250429_161400_EMAIL-04398.eml) | 2025-04-29T16:14:00+00:00 |
| `20250501_101400_EMAIL-04406-eml` | email | [emails/2025-05/20250501_101400_EMAIL-04406.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250501_101400_EMAIL-04406.eml) | 2025-05-01T10:14:00+00:00 |
| `20250527_203100_EMAIL-04639-eml` | email | [emails/2025-05/20250527_203100_EMAIL-04639.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250527_203100_EMAIL-04639.eml) | 2025-05-27T20:31:00+00:00 |
| `20250602_142600_EMAIL-04690-eml` | email | [emails/2025-06/20250602_142600_EMAIL-04690.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250602_142600_EMAIL-04690.eml) | 2025-06-02T14:26:00+00:00 |
| `20250604_022600_EMAIL-04698-eml` | email | [emails/2025-06/20250604_022600_EMAIL-04698.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250604_022600_EMAIL-04698.eml) | 2025-06-04T02:26:00+00:00 |
| `20250616_134600_EMAIL-04794-eml` | email | [emails/2025-06/20250616_134600_EMAIL-04794.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250616_134600_EMAIL-04794.eml) | 2025-06-16T13:46:00+00:00 |
| `20250620_125400_EMAIL-04826-eml` | email | [emails/2025-06/20250620_125400_EMAIL-04826.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250620_125400_EMAIL-04826.eml) | 2025-06-20T12:54:00+00:00 |
| `20250729_111400_EMAIL-05153-eml` | email | [emails/2025-07/20250729_111400_EMAIL-05153.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250729_111400_EMAIL-05153.eml) | 2025-07-29T11:14:00+00:00 |
| `20250729_141100_EMAIL-05156-eml` | email | [emails/2025-07/20250729_141100_EMAIL-05156.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250729_141100_EMAIL-05156.eml) | 2025-07-29T14:11:00+00:00 |
| `20250802_001100_EMAIL-05181-eml` | email | [emails/2025-08/20250802_001100_EMAIL-05181.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250802_001100_EMAIL-05181.eml) | 2025-08-02T00:11:00+00:00 |
| `20250809_143800_EMAIL-05235-eml` | email | [emails/2025-08/20250809_143800_EMAIL-05235.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250809_143800_EMAIL-05235.eml) | 2025-08-09T14:38:00+00:00 |
| `20250818_121400_EMAIL-05337-eml` | email | [emails/2025-08/20250818_121400_EMAIL-05337.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250818_121400_EMAIL-05337.eml) | 2025-08-18T12:14:00+00:00 |
| `20250824_160300_EMAIL-05394-eml` | email | [emails/2025-08/20250824_160300_EMAIL-05394.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250824_160300_EMAIL-05394.eml) | 2025-08-24T16:03:00+00:00 |
| `20250826_104600_EMAIL-05407-eml` | email | [emails/2025-08/20250826_104600_EMAIL-05407.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250826_104600_EMAIL-05407.eml) | 2025-08-26T10:46:00+00:00 |
| `20250830_125300_EMAIL-05455-eml` | email | [emails/2025-08/20250830_125300_EMAIL-05455.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250830_125300_EMAIL-05455.eml) | 2025-08-30T12:53:00+00:00 |
| `20250923_154900_EMAIL-05696-eml` | email | [emails/2025-09/20250923_154900_EMAIL-05696.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250923_154900_EMAIL-05696.eml) | 2025-09-23T15:49:00+00:00 |
| `20250926_131900_EMAIL-05721-eml` | email | [emails/2025-09/20250926_131900_EMAIL-05721.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250926_131900_EMAIL-05721.eml) | 2025-09-26T13:19:00+00:00 |
| `20251003_114900_EMAIL-05766-eml` | email | [emails/2025-10/20251003_114900_EMAIL-05766.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251003_114900_EMAIL-05766.eml) | 2025-10-03T11:49:00+00:00 |
| `20251006_222800_EMAIL-05801-eml` | email | [emails/2025-10/20251006_222800_EMAIL-05801.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251006_222800_EMAIL-05801.eml) | 2025-10-06 |
| `20251020_101400_EMAIL-05916-eml` | email | [emails/2025-10/20251020_101400_EMAIL-05916.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251020_101400_EMAIL-05916.eml) | 2025-10-20T10:14:00+00:00 |
| `20251103_134200_EMAIL-06033-eml` | email | [emails/2025-11/20251103_134200_EMAIL-06033.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251103_134200_EMAIL-06033.eml) | 2025-11-03T13:42:00+00:00 |
| `20251104_143600_EMAIL-06042-eml` | email | [emails/2025-11/20251104_143600_EMAIL-06042.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251104_143600_EMAIL-06042.eml) | 2025-11-04T14:36:00+00:00 |
| `20251104_174200_EMAIL-06045-eml` | email | [emails/2025-11/20251104_174200_EMAIL-06045.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251104_174200_EMAIL-06045.eml) | 2025-11-04T17:42:00+00:00 |
| `20251107_162600_EMAIL-06076-eml` | email | [emails/2025-11/20251107_162600_EMAIL-06076.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251107_162600_EMAIL-06076.eml) | 2025-11-07T16:26:00+00:00 |
| `20251127_162800_EMAIL-06242-eml` | email | [emails/2025-11/20251127_162800_EMAIL-06242.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251127_162800_EMAIL-06242.eml) | 2025-11-27T16:28:00+00:00 |
| `20251130_094700_EMAIL-06265-eml` | email | [emails/2025-11/20251130_094700_EMAIL-06265.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251130_094700_EMAIL-06265.eml) | 2025-11-30T09:47:00+00:00 |
| `20251204_113200_EMAIL-06292-eml` | email | [emails/2025-12/20251204_113200_EMAIL-06292.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251204_113200_EMAIL-06292.eml) | 2025-12-04T11:32:00+00:00 |
| `20251211_104300_EMAIL-06350-eml` | email | [emails/2025-12/20251211_104300_EMAIL-06350.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251211_104300_EMAIL-06350.eml) | 2025-12-11T10:43:00+00:00 |
| `20251222_093100_EMAIL-06466-eml` | email | [emails/2025-12/20251222_093100_EMAIL-06466.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251222_093100_EMAIL-06466.eml) | 2025-12-22T09:31:00+00:00 |
| `20251223_150600_EMAIL-06476-eml` | email | [emails/2025-12/20251223_150600_EMAIL-06476.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251223_150600_EMAIL-06476.eml) | 2025-12-23 |
| `20251224_103700_EMAIL-06481-eml` | email | [emails/2025-12/20251224_103700_EMAIL-06481.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251224_103700_EMAIL-06481.eml) | 2025-12-24 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-26T09:26:19+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
