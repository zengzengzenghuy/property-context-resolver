# context.unit.<!-- auto:unit_id -->EH-042<!-- /auto:unit_id -->.md

> Per-unit dossier (one file per Einheit). Holds everything specific to this unit:
> the unit itself, the active lease, the tenant(s), and all unit/tenant-specific operations.
> **Property-wide data lives in `context.property.md`** — see `parent_property_ref` below.

<!-- auto:meta -->
- last_built_at: `2026-04-26T09:41:08+00:00`
- build_hash: `engine-v2`
- engine_version: `0.2.0`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `unit`
- unit_id: `EH-042`
- property_id: `LIE-001`
- parent_property_ref: `context.property.LIE-001.md`
- owner_ref: `EIG-019`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit.summary -->[Routine] Einheit EH-042 (WE 42, 4-Zimmer-Wohnung, 103 m², 2. OG links) — Mieter Anika Zimmer signalisierte am 2025-12-12 Mietminderung an; Zahlung vom 2025-12-03 über 1.925,00 EUR erfolgt [(bank)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv#TX-00008). Mietminderungsanspruch nach § 536 BGB erfordert sofortige Substanzprüfung (Art und Dauer des Mangels, Kausalität zum Schadensersatzanspruch); schriftliche Dokumentation des Mangels und Fristsetzung zur Abhilfe erforderlich. Status: Subletting-Anfrage gestellt (2025-07-30), Verkaufsabsicht angemeldet (2025-06-21) — beide Vorgänge parallel monitoren.<!-- /auto:unit.summary -->

<!-- auto:unit -->
- unit_id: `EH-042`
- label: WE 42
- haus_id: `HAUS-16`
- floor: 2. OG
- position: links
- typ: Wohnung
- area_sqm: 103.0
- rooms: 4.0
- mea_‰: 239
- equipment: _(no data in source yet)_
- media_supply: _(no data in source yet)_
- key_inventory: _(no data in source yet)_
- meters: _(no data in source yet)_
- occupancy_status: `rented`
- nk_keys: _(no data in source yet)_
<!-- /auto:unit -->

---

## 2. Lease (Mietverhältnis, voll)
<!-- auto:lease.summary -->[Administrative] Mieter MIE-020 kündigte den Mietvertrag für EH-042 am 2024-11-11 fristgerecht [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241111_162600_EMAIL-02874.eml); Mietbeginn 2022-06-29, Kaution 4.929,00 EUR hinterlegt [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-020). Am 2025-02-24/27 beantragte Mieter Untervermietung für 3 Monate — zulässig nur mit schriftlicher Zustimmung des Eigentümers gemäß § 540 I BGB. Status: Kündigungsfrist nach § 573 BGB (3 Monate zum Ende eines Kalendermonats ab 2024-11-11 = Kündigungstermin 2025-02-28 oder später); Untervermietungsantrag erfordert Eigentümer-Genehmigung vor Subletting-Beginn.<!-- /auto:lease.summary -->

<!-- auto:lease -->
- lease_id: `LEASE-MIE-020`
- unit_ref: `EH-042`
- start_date: 2022-06-29 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-020)
- end_date: _(no data in source yet)_
- term_type: `unbefristet`
- cancellation_status: `by_tenant` (notice_date: 2024-11-11, move_out_date: —)
- rent_components: { kaltmiete: 1643.0, betriebskosten_vorauszahlung: 282.0, total_warmmiete: 1925.00 }
- payment_mode: Überweisung
- iban_payer: DE21370400441585064317 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-020)
- kaution: { amount: 4929.0 }
- usage: `residential`
- subletting: { current_status: `requested` }
- special_agreements: _(no data in source yet)_
<!-- /auto:lease -->

### 2.1 Tenants on this Lease
<!-- auto:tenants.summary -->_no issue_<!-- /auto:tenants.summary -->

<!-- auto:tenants -->
| tenant_id | name | role | contact_email | contact_phone | comms_pref | gesamtschuldner |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-020` | Frau Anika Zimmer | haupt | anika.zimmer@gmx.de | 03293183933 | email | — |
<!-- /auto:tenants -->

---

## 3. Operations (this unit / this tenant)

### 3.1 Open Tickets — Critical (overdue or due ≤7 days)
<!-- auto:tickets.critical.summary -->[Routine] Verstopfter Abfluss in der Dusche (WE 42) seit 2024-12-29 gemeldet, zuletzt bestätigt 2025-05-30; Mieter hat selbst Pumper versucht [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250530_145500_EMAIL-04663.eml). Verwaltung bestätigte Handwerkerauftrag 2025-02-22, aber keine Abschlussdokumentation in den vorliegenden Unterlagen; vertragliche Instandhaltungspflicht nach § 535 Abs. 1 BGB. Ticket geöffnet 2025-05-30 mit Schweregrad "normal" — Folgekontakt mit Handwerk und Mieter erforderlich, um Reparaturstatus zu klären.<!-- /auto:tickets.critical.summary -->

<!-- auto:tickets.critical -->
| ticket_id | type | title | deadline | status | assignee |
| --- | --- | --- | --- | --- | --- |
| `TKT-035bbf0b` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-d2d0dd1d` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-ddf3e4e2` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-c0cacf64` | schimmel | Schimmel im Schlafzimmer | — | open | — |
<!-- /auto:tickets.critical -->

### 3.2 Open Tickets — Aggregate
<!-- auto:tickets.aggregate.summary -->[Routine] Abflussverkehrung in EH-042 seit 2025-05-30 gemeldet, Schweregrad normal, Status ungeklärt [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240126_113000_EMAIL-00202.eml). Vermieter haftet für Mängel an gemeinsamen Leitungen nach § 535 I 1 BGB; Instandhaltungspflicht gilt auch für Abflussanlagen. Ticket besteht seit 331 Tagen ohne dokumentierte Behebung — dringend Handwerkstermin koordinieren oder Closure dokumentieren.<!-- /auto:tickets.aggregate.summary -->

<!-- auto:tickets.aggregate -->
- total_open: `17`
- by_type: { abfluss: `6`, fenster: `1`, schimmel: `3`, schluessel: `6`, wasserschaden: `1` }
- live source: `db.tickets WHERE unit_id=EH-042 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren

<!-- auto:dunning.summary -->[Routine] Mieter MIE-020 ist seit vier Monaten im Verzug; offener Betrag 7.700,00 EUR zzgl. 100,42 EUR Verzugszinsen, letzte Zahlung 2025-12-03 [(bank)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv#TX-01587). Vertraglich geschuldet sind monatlich 1.925,00 EUR (Kaltmiete 1.643,00 EUR + NK 282,00 EUR) [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-020). Verzug nach § 286 BGB festgestellt, Verzugszinsen § 288 I BGB; Mahnstufe 1 aktiv, nächster Schritt: 2. Mahnung nach 14 Tagen.<!-- /auto:dunning.summary -->

#### Per claim
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-020` | — | 1 | 7700.00 EUR | 2025-12-03 | — | — |
- live balance pointer: `db.tenant_balance.tenant_id=MIE-020`
<!-- /auto:dunning -->

### 3.4 Active Reductions / Deferrals (§ 536 BGB)
<!-- auto:reductions.summary -->[Emergency] Mieter EH-042 (Anika Zimmer) kündigt seit Juli 2024 wiederholt einseitige Mietminderung von 15% an — zuletzt 21.12.2025 mit Beginn 20.01.2026 — wegen ungelöster Wasserschäden und Schimmel (über 3 Monate ausstehend) [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251210_180300_EMAIL-06349.eml). Verwaltung bestätigte 12.12.2025 Handwerkereinsatz, jedoch keine Abschlussmeldung dokumentiert; Mietminderungsrecht nach § 536 BGB entsteht bei Mängeln, die Wohngebrauch erheblich beeinträchtigen, und läuft parallel zur Kündigungsfrist (Mietvertrag endet regulär 26.06.2025, jedoch Mieter zahlt seit Mai/Juni 2025 nicht regulär). Sofortiger Nachweis der Mängelbeseitigung erforderlich, um Minderungsanspruch abzuwehren und offene Forderungen zu sichern.<!-- /auto:reductions.summary -->

<!-- auto:reductions -->
- date_raised: 2024-02-18
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-04-19
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2024-07-11
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-03-23
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-05-22
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-05-24
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-07-23
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-12-10
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-12-12
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-12-21
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- *trigger: HITL exit if any entry present*
<!-- /auto:reductions -->

### 3.5 Latest Übergabeprotokoll
<!-- auto:handover.summary -->_no issue_<!-- /auto:handover.summary -->

<!-- auto:handover -->_(no data in source yet)_<!-- /auto:handover -->

### 3.6 Recurring Process State (this unit, in-flight)
<!-- auto:recurring.summary -->[Administrative] Mieter MIE-020 (Einheit EH-042) hat Kündigungsanträge in vier separaten E-Mails eingereicht (21.03.2024, 24.03.2024, 06.04.2024, 11.11.2024) [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241111_162600_EMAIL-02874.eml), jeweils mit Bitte um schriftliche Bestätigung des Kündigungstermins. Nach § 573 BGB ist die erste wirksame Kündigung vom 21.03.2024 maßgeblich; die nachfolgenden Anträge sind redundant. Erforderlich: schriftliche Kündigungsbestätigung mit exaktem Beendigungstermin und Übergabemodalitäten an Mieter übermitteln.<!-- /auto:recurring.summary -->

<!-- auto:recurring -->
| process_type | started | current_step | owner | eta | blockers |
| --- | --- | --- | --- | --- | --- |
| Mieterwechsel | 2024-11-11 | Kündigung erhalten | Verwaltung | TBD | Übergabe-Termin offen |
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
<!-- auto:sticky-threads.summary -->
[Routine] Mieter MIE-020 (WE 32) kündigt Mietminderung um 15 % ab 20.01.2026 an [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251221_135600_EMAIL-06459.eml); Begründung: Wasserschaden und Schimmel seit über 3 Monaten nicht behoben (Mangelbeginn ~September 2025). Mietminderungsanspruch nach § 536 BGB voraussetzungsmäßig begründet, wenn Mangel tatsächlich vorliegt und Fristsetzung zur Abhilfe nicht eingehalten wurde. Sofortige Schadensaufnahme und Reparaturbeauftragung erforderlich; Verwaltung muss Abwehrposition (Beseitigung vor 20.01.2026) oder Vergleich dokumentieren.

[Routine] Liegenschaftseinheit EH-042 hat seit Februar 2024 offene Thread zu Verkaufsabsicht mit zuletzt 6 Nachrichten (letzte: 21.06.2025) [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250604_152200_EMAIL-04703.eml). Eigentümer Mina Textor meldete Mieterwechsel und Freigabe ab 22.07.2025; Verwaltung versprach Handw
<!-- /auto:sticky-threads.summary -->

<!-- auto:sticky-threads -->
| thread_id | subject | last_msg_date | parties | status | one-line outcome | pointer |
| --- | --- | --- | --- | --- | --- | --- |
| `TH-8344fa` | Mietminderung Ankuendigung | 2025-12-21 | `MIE-020` | active | 130 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251221_135600_EMAIL-06459.eml) |
| `TH-e47a38` | Mieterwechsel in WE 42 | 2025-06-04 | `EH-042` | active | 6 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250604_152200_EMAIL-04703.eml) |
| `TH-0b8dcb` | Verkaufsabsicht WE 42 | 2025-06-21 | `EH-042` | active | 6 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250621_153700_EMAIL-04836.eml) |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance.summary -->[Routine] Mieter MIE-020 (Anika Zimmer, EH-042 WE 42, 103 qm, 4 Zimmer, 2. OG links) ist seit vier Monaten im Verzug; offener Betrag 7.700,00 EUR zzgl. 100,42 EUR Verzugszinsen, letzte Zahlung 2025-12-03 [(bank)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv#TX-01587). Vertraglich geschuldet sind monatlich 1.925,00 EUR (Kaltmiete 1.643,00 EUR + NK 282,00 EUR). Verzug nach § 286 BGB, Verzugszinsen § 288 I BGB (Basiszins 3,5 % + 5 pp); Mahnstufe 1 aktiv seit 2026-04-26 [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-020); parallel aktive Mietminderungsankündigung seit 2025-12-21 (Status: ungelöste Reparaturen, Thread seit 2024-01-03, 130 Nachrichten) — Verzugsabwicklung und Mängelbeseitigung müssen koordiniert werden.<!-- /auto:provenance.summary -->

<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `kontoauszug_2024_2025-csv` | bank | [bank/kontoauszug_2024_2025.csv](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv) | 2026-04-26 |
| `20240126_113000_EMAIL-00202-eml` | email | [emails/2024-01/20240126_113000_EMAIL-00202.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240126_113000_EMAIL-00202.eml) | 2024-01-26T11:30:00+00:00 |
| `20240204_093900_EMAIL-00293-eml` | email | [emails/2024-02/20240204_093900_EMAIL-00293.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240204_093900_EMAIL-00293.eml) | 2024-02-04T09:39:00+00:00 |
| `20240206_201400_EMAIL-00319-eml` | email | [emails/2024-02/20240206_201400_EMAIL-00319.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240206_201400_EMAIL-00319.eml) | 2024-02-06T20:14:00+00:00 |
| `20240207_143900_EMAIL-00323-eml` | email | [emails/2024-02/20240207_143900_EMAIL-00323.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240207_143900_EMAIL-00323.eml) | 2024-02-07T14:39:00+00:00 |
| `20240209_135900_EMAIL-00342-eml` | email | [emails/2024-02/20240209_135900_EMAIL-00342.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240209_135900_EMAIL-00342.eml) | 2024-02-09T13:59:00+00:00 |
| `20240213_110000_EMAIL-00371-eml` | email | [emails/2024-02/20240213_110000_EMAIL-00371.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240213_110000_EMAIL-00371.eml) | 2024-02-13T11:00:00+00:00 |
| `20240215_000400_EMAIL-00384-eml` | email | [emails/2024-02/20240215_000400_EMAIL-00384.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240215_000400_EMAIL-00384.eml) | 2024-02-15T00:04:00+00:00 |
| `20240218_102000_EMAIL-00409-eml` | email | [emails/2024-02/20240218_102000_EMAIL-00409.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240218_102000_EMAIL-00409.eml) | 2024-02-18T10:20:00+00:00 |
| `20240229_160000_EMAIL-00504-eml` | email | [emails/2024-02/20240229_160000_EMAIL-00504.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240229_160000_EMAIL-00504.eml) | 2024-02-29T16:00:00+00:00 |
| `20240302_145600_EMAIL-00531-eml` | email | [emails/2024-03/20240302_145600_EMAIL-00531.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240302_145600_EMAIL-00531.eml) | 2024-03-02T14:56:00+00:00 |
| `20240321_115700_EMAIL-00697-eml` | email | [emails/2024-03/20240321_115700_EMAIL-00697.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240321_115700_EMAIL-00697.eml) | 2024-03-21T11:57:00+00:00 |
| `20240324_103400_EMAIL-00721-eml` | email | [emails/2024-03/20240324_103400_EMAIL-00721.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240324_103400_EMAIL-00721.eml) | 2024-03-24T10:34:00+00:00 |
| `20240406_095500_EMAIL-00845-eml` | email | [emails/2024-04/20240406_095500_EMAIL-00845.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240406_095500_EMAIL-00845.eml) | 2024-04-06T09:55:00+00:00 |
| `20240408_100500_EMAIL-00867-eml` | email | [emails/2024-04/20240408_100500_EMAIL-00867.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240408_100500_EMAIL-00867.eml) | 2024-04-08T10:05:00+00:00 |
| `20240410_030500_EMAIL-00880-eml` | email | [emails/2024-04/20240410_030500_EMAIL-00880.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240410_030500_EMAIL-00880.eml) | 2024-04-10T03:05:00+00:00 |
| `20240417_142700_EMAIL-00971-eml` | email | [emails/2024-04/20240417_142700_EMAIL-00971.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240417_142700_EMAIL-00971.eml) | 2024-04-17T14:27:00+00:00 |
| `20240419_121900_EMAIL-00987-eml` | email | [emails/2024-04/20240419_121900_EMAIL-00987.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240419_121900_EMAIL-00987.eml) | 2024-04-19T12:19:00+00:00 |
| `20240419_150500_EMAIL-00990-eml` | email | [emails/2024-04/20240419_150500_EMAIL-00990.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240419_150500_EMAIL-00990.eml) | 2024-04-19T15:05:00+00:00 |
| `20240429_103400_EMAIL-01072-eml` | email | [emails/2024-04/20240429_103400_EMAIL-01072.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240429_103400_EMAIL-01072.eml) | 2024-04-29T10:34:00+00:00 |
| `20240503_090900_EMAIL-01106-eml` | email | [emails/2024-05/20240503_090900_EMAIL-01106.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240503_090900_EMAIL-01106.eml) | 2024-05-03T09:09:00+00:00 |
| `20240507_101000_EMAIL-01141-eml` | email | [emails/2024-05/20240507_101000_EMAIL-01141.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240507_101000_EMAIL-01141.eml) | 2024-05-07T10:10:00+00:00 |
| `20240508_051000_EMAIL-01150-eml` | email | [emails/2024-05/20240508_051000_EMAIL-01150.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240508_051000_EMAIL-01150.eml) | 2024-05-08T05:10:00+00:00 |
| `20240522_135400_EMAIL-01280-eml` | email | [emails/2024-05/20240522_135400_EMAIL-01280.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240522_135400_EMAIL-01280.eml) | 2024-05-22T13:54:00+00:00 |
| `20240628_113700_EMAIL-01605-eml` | email | [emails/2024-06/20240628_113700_EMAIL-01605.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240628_113700_EMAIL-01605.eml) | 2024-06-28T11:37:00+00:00 |
| `20240711_150700_EMAIL-01731-eml` | email | [emails/2024-07/20240711_150700_EMAIL-01731.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240711_150700_EMAIL-01731.eml) | 2024-07-11T15:07:00+00:00 |
| `20240712_091700_EMAIL-01740-eml` | email | [emails/2024-07/20240712_091700_EMAIL-01740.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240712_091700_EMAIL-01740.eml) | 2024-07-12T09:17:00+00:00 |
| `20240721_133800_EMAIL-01820-eml` | email | [emails/2024-07/20240721_133800_EMAIL-01820.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240721_133800_EMAIL-01820.eml) | 2024-07-21T13:38:00+00:00 |
| `20240803_144100_EMAIL-01947-eml` | email | [emails/2024-08/20240803_144100_EMAIL-01947.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240803_144100_EMAIL-01947.eml) | 2024-08-03T14:41:00+00:00 |
| `20240818_152800_EMAIL-02081-eml` | email | [emails/2024-08/20240818_152800_EMAIL-02081.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240818_152800_EMAIL-02081.eml) | 2024-08-18T15:28:00+00:00 |
| `20240825_102000_EMAIL-02147-eml` | email | [emails/2024-08/20240825_102000_EMAIL-02147.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240825_102000_EMAIL-02147.eml) | 2024-08-25T10:20:00+00:00 |
| `20240825_212000_EMAIL-02157-eml` | email | [emails/2024-08/20240825_212000_EMAIL-02157.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240825_212000_EMAIL-02157.eml) | 2024-08-25T21:20:00+00:00 |
| `20240901_033100_EMAIL-02210-eml` | email | [emails/2024-09/20240901_033100_EMAIL-02210.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240901_033100_EMAIL-02210.eml) | 2024-09-01T03:31:00+00:00 |
| `20240921_110600_EMAIL-02396-eml` | email | [emails/2024-09/20240921_110600_EMAIL-02396.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240921_110600_EMAIL-02396.eml) | 2024-09-21T11:06:00+00:00 |
| `20240922_020600_EMAIL-02401-eml` | email | [emails/2024-09/20240922_020600_EMAIL-02401.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240922_020600_EMAIL-02401.eml) | 2024-09-22T02:06:00+00:00 |
| `20241003_122300_EMAIL-02502-eml` | email | [emails/2024-10/20241003_122300_EMAIL-02502.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241003_122300_EMAIL-02502.eml) | 2024-10-03T12:23:00+00:00 |
| `20241011_141600_EMAIL-02593-eml` | email | [emails/2024-10/20241011_141600_EMAIL-02593.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241011_141600_EMAIL-02593.eml) | 2024-10-11T14:16:00+00:00 |
| `20241018_115600_EMAIL-02647-eml` | email | [emails/2024-10/20241018_115600_EMAIL-02647.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241018_115600_EMAIL-02647.eml) | 2024-10-18T11:56:00+00:00 |
| `20241024_103100_EMAIL-02706-eml` | email | [emails/2024-10/20241024_103100_EMAIL-02706.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241024_103100_EMAIL-02706.eml) | 2024-10-24T10:31:00+00:00 |
| `20241025_233100_EMAIL-02723-eml` | email | [emails/2024-10/20241025_233100_EMAIL-02723.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241025_233100_EMAIL-02723.eml) | 2024-10-25T23:31:00+00:00 |
| `20241027_233100_EMAIL-02739-eml` | email | [emails/2024-10/20241027_233100_EMAIL-02739.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241027_233100_EMAIL-02739.eml) | 2024-10-27T23:31:00+00:00 |
| `20241104_144900_EMAIL-02815-eml` | email | [emails/2024-11/20241104_144900_EMAIL-02815.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241104_144900_EMAIL-02815.eml) | 2024-11-04T14:49:00+00:00 |
| `20241109_014900_EMAIL-02855-eml` | email | [emails/2024-11/20241109_014900_EMAIL-02855.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241109_014900_EMAIL-02855.eml) | 2024-11-09T01:49:00+00:00 |
| `20241111_162600_EMAIL-02874-eml` | email | [emails/2024-11/20241111_162600_EMAIL-02874.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241111_162600_EMAIL-02874.eml) | 2024-11-11T16:26:00+00:00 |
| `20241226_144400_EMAIL-03282-eml` | email | [emails/2024-12/20241226_144400_EMAIL-03282.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241226_144400_EMAIL-03282.eml) | 2024-12-26T14:44:00+00:00 |
| `20241229_100700_EMAIL-03303-eml` | email | [emails/2024-12/20241229_100700_EMAIL-03303.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241229_100700_EMAIL-03303.eml) | 2024-12-29T10:07:00+00:00 |
| `20250120_095700_EMAIL-03525-eml` | email | [emails/2025-01/20250120_095700_EMAIL-03525.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250120_095700_EMAIL-03525.eml) | 2025-01-20T09:57:00+00:00 |
| `20250126_150400_EMAIL-03568-eml` | email | [emails/2025-01/20250126_150400_EMAIL-03568.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250126_150400_EMAIL-03568.eml) | 2025-01-26T15:04:00+00:00 |
| `20250212_154200_EMAIL-03710-eml` | email | [emails/2025-02/20250212_154200_EMAIL-03710.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250212_154200_EMAIL-03710.eml) | 2025-02-12T15:42:00+00:00 |
| `20250220_154000_EMAIL-03795-eml` | email | [emails/2025-02/20250220_154000_EMAIL-03795.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250220_154000_EMAIL-03795.eml) | 2025-02-20T15:40:00+00:00 |
| `20250222_114000_EMAIL-03812-eml` | email | [emails/2025-02/20250222_114000_EMAIL-03812.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250222_114000_EMAIL-03812.eml) | 2025-02-22T11:40:00+00:00 |
| `20250223_140900_EMAIL-03822-eml` | email | [emails/2025-02/20250223_140900_EMAIL-03822.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250223_140900_EMAIL-03822.eml) | 2025-02-23T14:09:00+00:00 |
| `20250224_145200_EMAIL-03837-eml` | email | [emails/2025-02/20250224_145200_EMAIL-03837.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250224_145200_EMAIL-03837.eml) | 2025-02-24T14:52:00+00:00 |
| `20250227_130900_EMAIL-03870-eml` | email | [emails/2025-02/20250227_130900_EMAIL-03870.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250227_130900_EMAIL-03870.eml) | 2025-02-27T13:09:00+00:00 |
| `20250306_160500_EMAIL-03937-eml` | email | [emails/2025-03/20250306_160500_EMAIL-03937.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250306_160500_EMAIL-03937.eml) | 2025-03-06T16:05:00+00:00 |
| `20250314_092000_EMAIL-04010-eml` | email | [emails/2025-03/20250314_092000_EMAIL-04010.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250314_092000_EMAIL-04010.eml) | 2025-03-14T09:20:00+00:00 |
| `20250323_170800_EMAIL-04108-eml` | email | [emails/2025-03/20250323_170800_EMAIL-04108.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250323_170800_EMAIL-04108.eml) | 2025-03-23T17:08:00+00:00 |
| `20250404_155500_EMAIL-04205-eml` | email | [emails/2025-04/20250404_155500_EMAIL-04205.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250404_155500_EMAIL-04205.eml) | 2025-04-04T15:55:00+00:00 |
| `20250406_015100_EMAIL-04214-eml` | email | [emails/2025-04/20250406_015100_EMAIL-04214.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250406_015100_EMAIL-04214.eml) | 2025-04-06T01:51:00+00:00 |
| `20250507_164000_EMAIL-04454-eml` | email | [emails/2025-05/20250507_164000_EMAIL-04454.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250507_164000_EMAIL-04454.eml) | 2025-05-07T16:40:00+00:00 |
| `20250522_160800_EMAIL-04590-eml` | email | [emails/2025-05/20250522_160800_EMAIL-04590.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250522_160800_EMAIL-04590.eml) | 2025-05-22T16:08:00+00:00 |
| `20250524_010800_EMAIL-04604-eml` | email | [emails/2025-05/20250524_010800_EMAIL-04604.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250524_010800_EMAIL-04604.eml) | 2025-05-24T01:08:00+00:00 |
| `20250530_145500_EMAIL-04663-eml` | email | [emails/2025-05/20250530_145500_EMAIL-04663.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250530_145500_EMAIL-04663.eml) | 2025-05-30T14:55:00+00:00 |
| `20250604_152200_EMAIL-04703-eml` | email | [emails/2025-06/20250604_152200_EMAIL-04703.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250604_152200_EMAIL-04703.eml) | 2025-06-04 |
| `20250621_153700_EMAIL-04836-eml` | email | [emails/2025-06/20250621_153700_EMAIL-04836.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250621_153700_EMAIL-04836.eml) | 2025-06-21T15:37:00+00:00 |
| `20250717_124500_EMAIL-05060-eml` | email | [emails/2025-07/20250717_124500_EMAIL-05060.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250717_124500_EMAIL-05060.eml) | 2025-07-17T12:45:00+00:00 |
| `20250719_094300_EMAIL-05079-eml` | email | [emails/2025-07/20250719_094300_EMAIL-05079.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250719_094300_EMAIL-05079.eml) | 2025-07-19T09:43:00+00:00 |
| `20250721_024500_EMAIL-05101-eml` | email | [emails/2025-07/20250721_024500_EMAIL-05101.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250721_024500_EMAIL-05101.eml) | 2025-07-21T02:45:00+00:00 |
| `20250723_110800_EMAIL-05120-eml` | email | [emails/2025-07/20250723_110800_EMAIL-05120.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250723_110800_EMAIL-05120.eml) | 2025-07-23T11:08:00+00:00 |
| `20250730_181900_EMAIL-05168-eml` | email | [emails/2025-07/20250730_181900_EMAIL-05168.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250730_181900_EMAIL-05168.eml) | 2025-07-30T18:19:00+00:00 |
| `20250812_111300_EMAIL-05267-eml` | email | [emails/2025-08/20250812_111300_EMAIL-05267.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250812_111300_EMAIL-05267.eml) | 2025-08-12T11:13:00+00:00 |
| `20250812_201300_EMAIL-05274-eml` | email | [emails/2025-08/20250812_201300_EMAIL-05274.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250812_201300_EMAIL-05274.eml) | 2025-08-12T20:13:00+00:00 |
| `20250813_132800_EMAIL-05282-eml` | email | [emails/2025-08/20250813_132800_EMAIL-05282.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250813_132800_EMAIL-05282.eml) | 2025-08-13T13:28:00+00:00 |
| `20250813_201300_EMAIL-05287-eml` | email | [emails/2025-08/20250813_201300_EMAIL-05287.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250813_201300_EMAIL-05287.eml) | 2025-08-13T20:13:00+00:00 |
| `20251003_121100_EMAIL-05767-eml` | email | [emails/2025-10/20251003_121100_EMAIL-05767.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251003_121100_EMAIL-05767.eml) | 2025-10-03T12:11:00+00:00 |
| `20251102_144900_EMAIL-06023-eml` | email | [emails/2025-11/20251102_144900_EMAIL-06023.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251102_144900_EMAIL-06023.eml) | 2025-11-02T14:49:00+00:00 |
| `20251102_163700_EMAIL-06025-eml` | email | [emails/2025-11/20251102_163700_EMAIL-06025.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251102_163700_EMAIL-06025.eml) | 2025-11-02T16:37:00+00:00 |
| `20251121_094300_EMAIL-06177-eml` | email | [emails/2025-11/20251121_094300_EMAIL-06177.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251121_094300_EMAIL-06177.eml) | 2025-11-21T09:43:00+00:00 |
| `20251207_185500_EMAIL-06322-eml` | email | [emails/2025-12/20251207_185500_EMAIL-06322.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251207_185500_EMAIL-06322.eml) | 2025-12-07T18:55:00+00:00 |
| `20251208_185500_EMAIL-06332-eml` | email | [emails/2025-12/20251208_185500_EMAIL-06332.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251208_185500_EMAIL-06332.eml) | 2025-12-08T18:55:00+00:00 |
| `20251210_180300_EMAIL-06349-eml` | email | [emails/2025-12/20251210_180300_EMAIL-06349.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251210_180300_EMAIL-06349.eml) | 2025-12-10T18:03:00+00:00 |
| `20251212_040300_EMAIL-06362-eml` | email | [emails/2025-12/20251212_040300_EMAIL-06362.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251212_040300_EMAIL-06362.eml) | 2025-12-12T04:03:00+00:00 |
| `20251221_040300_EMAIL-06450-eml` | email | [emails/2025-12/20251221_040300_EMAIL-06450.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251221_040300_EMAIL-06450.eml) | 2025-12-21T04:03:00+00:00 |
| `20251221_135600_EMAIL-06459-eml` | email | [emails/2025-12/20251221_135600_EMAIL-06459.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251221_135600_EMAIL-06459.eml) | 2025-12-21 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-26T09:26:19+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
