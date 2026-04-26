# context.unit.<!-- auto:unit_id -->EH-003<!-- /auto:unit_id -->.md

> Per-unit dossier (one file per Einheit). Holds everything specific to this unit:
> the unit itself, the active lease, the tenant(s), and all unit/tenant-specific operations.
> **Property-wide data lives in `context.property.md`** — see `parent_property_ref` below.

<!-- auto:meta -->
- last_built_at: `2026-04-26T09:51:39+00:00`
- build_hash: `engine-v2`
- engine_version: `0.2.0`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `unit`
- unit_id: `EH-003`
- property_id: `LIE-001`
- parent_property_ref: `context.property.LIE-001.md`
- owner_ref: `EIG-025`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit.summary -->[Administrative] Einheit WE 03 (EH-003, 1. OG rechts, 62 qm, 2 Zimmer) in HAUS-12 mit Miteigentumsanteil 144/10000 — Verkaufsabsicht gemeldet 2025-12-28, Untervermietungsantrag gestellt 2025-03-11 (Status: angefordert) [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#einheit/EH-003). Hausgeldzahlung 2025-12 eingegangen (10,20 EUR von Hiltrud Speer) [(bank)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv#TX-00023); Mietperiode 12/2025 verbucht. Beide Vorgänge (Verkauf § 577 Abs. 1 BGB, Untervermietung § 540 BGB) erfordern Zustimmung des Vermieters — Status und Deadlines prüfen erforderlich.<!-- /auto:unit.summary -->

<!-- auto:unit -->
- unit_id: `EH-003`
- label: WE 03
- haus_id: `HAUS-12`
- floor: 1. OG
- position: rechts
- typ: Wohnung
- area_sqm: 62.0
- rooms: 2.0
- mea_‰: 144
- equipment: _(no data in source yet)_
- media_supply: _(no data in source yet)_
- key_inventory: _(no data in source yet)_
- meters: _(no data in source yet)_
- occupancy_status: `rented`
- nk_keys: _(no data in source yet)_
<!-- /auto:unit -->

---

## 2. Lease (Mietverhältnis, voll)
<!-- auto:lease.summary -->[Routine] Mieter MIE-008 (Ferenc Stahr, EH-003) hat den Mietvertrag zum nächstmöglichen Termin gekündigt [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251013_101200_EMAIL-05858.eml), Kündigungsdatum 2025-10-13; Mietbeginn 2022-04-29, Kaltmiete 861,00 EUR + NK 209,00 EUR, Kaution 2.583,00 EUR [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-008). Bei Kündigung durch Mieter gilt die Kündigungsfrist nach § 573 I BGB (vier Wochen zum Fünfzehnten oder zum Ende eines Kalendermonats); nächster potenzieller Kündigungstermin: 2025-11-30 oder 2025-12-31. Parallel: Untermiete-Anfrage vom 2025-03-10 [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250310_143800_EMAIL-03978.eml) unbeantwortet; Reparatur Küchenfenster gemeldet 2025-10-19 [(email)](https://github.com/zengzengzenghuy/property-<!-- /auto:lease.summary -->

<!-- auto:lease -->
- lease_id: `LEASE-MIE-008`
- unit_ref: `EH-003`
- start_date: 2022-04-29 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-008)
- end_date: _(no data in source yet)_
- term_type: `unbefristet`
- cancellation_status: `by_tenant` (notice_date: 2025-10-19, move_out_date: —)
- rent_components: { kaltmiete: 861.0, betriebskosten_vorauszahlung: 209.0, total_warmmiete: 1070.00 }
- payment_mode: Überweisung
- iban_payer: DE71100700004044997278 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-008)
- kaution: { amount: 2583.0 }
- usage: `residential`
- subletting: { current_status: `requested` }
- special_agreements: _(no data in source yet)_
<!-- /auto:lease -->

### 2.1 Tenants on this Lease
<!-- auto:tenants.summary -->_no issue_<!-- /auto:tenants.summary -->

<!-- auto:tenants -->
| tenant_id | name | role | contact_email | contact_phone | comms_pref | gesamtschuldner |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-008` | Herr Ferenc Stahr | haupt | ferenc.stahr@gmx.de | +49(0)7482175946 | email | — |
<!-- /auto:tenants -->

---

## 3. Operations (this unit / this tenant)

### 3.1 Open Tickets — Critical (overdue or due ≤7 days)
<!-- auto:tickets.critical.summary -->[Routine] Mieter Ferenc Stahr (EH-003) hat seit Juli 2024 wiederholt Abflussblockaden in der Dusche gemeldet (zuletzt 2025-10-13), daneben Wasserschäden im Bad (2024-07-04, 2024-12-24) und Schimmelbildung im Schlafzimmer (2025-09-12, 2025-10-13). Vertraglich ist der Vermieter zur Beseitigung von Mängeln verpflichtet, die die Tauglichkeit zur Miete beeinträchtigen (§ 535 I 1 BGB); Stahr hat die Mängel ordnungsgemäß angezeigt. Die Kündigungsfrist des Mieters läuft zum 2025-12-04; vor Wohnungsübergabe müssen alle Mängel dokumentiert werden, um Schadensersatzansprüche nach § 537 BGB auszuschließen. Sofortiges Handwerk erforderlich vor Auszug.<!-- /auto:tickets.critical.summary -->

<!-- auto:tickets.critical -->
| ticket_id | type | title | deadline | status | assignee |
| --- | --- | --- | --- | --- | --- |
| `TKT-4322ecd0` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-852cd6ad` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-0a74de18` | wasserschaden | Re: Water damage in bathroom | — | open | — |
| `TKT-397a5dc1` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-da2c416a` | wasserschaden | Wasserschaden Bad | — | open | — |
| `TKT-183ad0b6` | schimmel | Schimmel im Schlafzimmer | — | open | — |
| `TKT-09b8e1af` | schimmel | Schimmel im Schlafzimmer | — | open | — |
<!-- /auto:tickets.critical -->

### 3.2 Open Tickets — Aggregate
<!-- auto:tickets.aggregate.summary -->[Routine] Einheit EH-003: Abflussstörung gemeldet am 2025-10-15 [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240105_092700_EMAIL-00032.eml), Schweregrad normal, Status offen. Instandhaltungspflicht Vermieter nach § 535 I 1 BGB (Erhaltung des Mietgegenstands in tauglichem Zustand), Anspruch Mieter auf unverzügliche Mängelbeseitigung § 535 I 2 BGB. Seit Meldung 194 Tage verstrichen ohne Abschlussbestätigung — Reaktionszeit überschritten, Eskalation erforderlich.<!-- /auto:tickets.aggregate.summary -->

<!-- auto:tickets.aggregate -->
- total_open: `20`
- by_type: { abfluss: `7`, schimmel: `3`, schluessel: `6`, wasserschaden: `4` }
- live source: `db.tickets WHERE unit_id=EH-003 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren

<!-- auto:dunning.summary -->[Routine] Mieter MIE-008 ist seit vier Monaten im Verzug; offener Betrag 4.280,00 EUR zzgl. 55,82 EUR Verzugszinsen, letzte Zahlung 2025-12-03 [(bank)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv#TX-01580). Vertraglich geschuldet sind monatlich 1.070,00 EUR (Kaltmiete 861,00 EUR + NK 209,00 EUR) [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-008). Verzug nach § 286 BGB festgestellt, Verzugszinsen nach § 288 I BGB; Mahnstufe 1 aktiv, nächster Schritt: 2. Mahnung nach 14 Tagen.<!-- /auto:dunning.summary -->

#### Per claim
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-008` | — | 1 | 4280.00 EUR | 2025-12-03 | — | — |
- live balance pointer: `db.tenant_balance.tenant_id=MIE-008`
<!-- /auto:dunning -->

### 3.4 Active Reductions / Deferrals (§ 536 BGB)
<!-- auto:reductions.summary -->[Emergency] Mieter EH-003 (Ferenc Stahr) kündigt unilaterale Mietminderung um 15% ab 2025-07-31 an; gleichlautende Ankündigungen erfolgten bereits 2024-07-14 und 2025-06-01 [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250701_110800_EMAIL-04918.eml). Grund: Wasserschaden und Schimmel seit über 3 Monaten unbehoben — Mangel der Mietsache nach § 535 BGB II. Reparaturobliegenheit der Verwaltung gemäß Mietvertrag; Mieter hat Minderungsrecht nach § 536 BGB, sofern Mangel dokumentiert und Frist zur Abhilfe (üblicherweise 2 Wochen nach Mängelanzeige) verstrichen ist — sofortige Prüfung des Reparaturstatus und Nachweis der Abhilfeversuche erforderlich.<!-- /auto:reductions.summary -->

<!-- auto:reductions -->
- date_raised: 2024-07-14
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-06-01
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- date_raised: 2025-07-01
- amount_or_percent: —
- reason: ungelöste Reparaturen (auto-detected)
- status: **unilateral**

- *trigger: HITL exit if any entry present*
<!-- /auto:reductions -->

### 3.5 Latest Übergabeprotokoll
<!-- auto:handover.summary -->_no issue_<!-- /auto:handover.summary -->

<!-- auto:handover -->_(no data in source yet)_<!-- /auto:handover -->

### 3.6 Recurring Process State (this unit, in-flight)
<!-- auto:recurring.summary -->[Routine] Mieter MIE-008 (Ferenc Stahr) hat Mietvertrag für EH-003 am 2025-10-19 gekündigt [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251013_101200_EMAIL-05858.eml); dies ist die zweite schriftliche Kündigungsmitteilung nach vorheriger Kündigung vom 2025-01-02. Parallel wurden zwei Mängelberichte eingereicht: Heizungsausfall (2025-01-09) und defektes Küchenfenster (2025-10-19) [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251019_021200_EMAIL-05909.eml). Kündigungsfrist § 573 BGB (4 Wochen zum 15./Ende eines Kalendermonats); unverjährte Mängel nach § 536 BGB müssen vor Übergabe dokumentiert und behoben oder Schadensersatzansprüche begründet werden.<!-- /auto:recurring.summary -->

<!-- auto:recurring -->
| process_type | started | current_step | owner | eta | blockers |
| --- | --- | --- | --- | --- | --- |
| Mieterwechsel | 2025-10-19 | Kündigung erhalten | Verwaltung | TBD | Übergabe-Termin offen |
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
[Administrative] EH-003: Verkaufsabsicht seit 2024-01-08, aktiver Thread mit 6 Nachrichten; Verkäufer Hiltrud Speer bestätigte Kündigungstermin 2026-01-18, Wohnungsübergabe geplant März 2026 [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251228_105000_EMAIL-06506.eml). Parallel: Mieterwechsel gemeldet (Mieter kündigt zum Monatsende 2025-12-31, Freizug 2026-02-10). Verwalter muss Hausgeldbescheinigung und ETV-Protokolle bereitstellen (Verkäuferdokumentation) und Übergabetermine koordinieren.

[Routine] MIE-008 (Ferenc Stahr): Internet/TV-Anschluss-Thread seit 2024-01-08, 125 Nachrichten, aktiv bis 2025-12-24 [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251224_165900_EMAIL-06485.eml). Anfrage nach Kollektivvertrag und Wechseloptionen; Verwalter (Thomas Kreuzer) signalisierte Prüfung am 2025-12-24, noch kein Abschluss dokumentiert. Klärung erforderlich: Besteht Kollektivvertrag
<!-- /auto:sticky-threads.summary -->

<!-- auto:sticky-threads -->
| thread_id | subject | last_msg_date | parties | status | one-line outcome | pointer |
| --- | --- | --- | --- | --- | --- | --- |
| `TH-1cea7c` | Internet/TV-Anschluss | 2025-12-24 | `MIE-008` | active | 125 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251224_165900_EMAIL-06485.eml) |
| `TH-df26e4` | Verkaufsabsicht WE 03 | 2025-12-28 | `EH-003` | active | 6 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251228_105000_EMAIL-06506.eml) |
| `TH-555059` | Mieterwechsel in WE 03 | 2025-12-17 | `EH-003` | active | 7 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251217_145100_EMAIL-06423.eml) |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance.summary -->[Routine] Mieter MIE-008 (Ferenc Stahr) ist seit vier Monaten im Verzug; offener Betrag 4.280,00 EUR zzgl. 55,82 EUR Verzugszinsen, letzte Zahlung 2025-12-03 [(bank)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv#TX-00023). Vertraglich geschuldet monatlich 1.070,00 EUR (Kaltmiete 861,00 EUR + NK 209,00 EUR) für Einheit EH-003 [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#einheit/EH-003). Verzug § 286 BGB, Verzugszinsen § 288 I BGB; Mahnstufe 1, nächste Mahnung fällig nach 14 Tagen — parallel: Kündigung durch Mieter 2025-10-19 dokumentiert, Mietvertragsstatus zur Bestätigung prüfen [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-008).<!-- /auto:provenance.summary -->

<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `kontoauszug_2024_2025-csv` | bank | [bank/kontoauszug_2024_2025.csv](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv) | 2026-04-26 |
| `20240105_092700_EMAIL-00032-eml` | email | [emails/2024-01/20240105_092700_EMAIL-00032.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240105_092700_EMAIL-00032.eml) | 2024-01-05T09:27:00+00:00 |
| `20240107_091200_EMAIL-00045-eml` | email | [emails/2024-01/20240107_091200_EMAIL-00045.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240107_091200_EMAIL-00045.eml) | 2024-01-07T09:12:00+00:00 |
| `20240109_084500_EMAIL-00063-eml` | email | [emails/2024-01/20240109_084500_EMAIL-00063.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240109_084500_EMAIL-00063.eml) | 2024-01-09T08:45:00+00:00 |
| `20240122_112300_EMAIL-00177-eml` | email | [emails/2024-01/20240122_112300_EMAIL-00177.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240122_112300_EMAIL-00177.eml) | 2024-01-22T11:23:00+00:00 |
| `20240126_131200_EMAIL-00205-eml` | email | [emails/2024-01/20240126_131200_EMAIL-00205.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240126_131200_EMAIL-00205.eml) | 2024-01-26T13:12:00+00:00 |
| `20240127_081200_EMAIL-00209-eml` | email | [emails/2024-01/20240127_081200_EMAIL-00209.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240127_081200_EMAIL-00209.eml) | 2024-01-27T08:12:00+00:00 |
| `20240201_081200_EMAIL-00258-eml` | email | [emails/2024-02/20240201_081200_EMAIL-00258.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240201_081200_EMAIL-00258.eml) | 2024-02-01T08:12:00+00:00 |
| `20240211_164800_EMAIL-00355-eml` | email | [emails/2024-02/20240211_164800_EMAIL-00355.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240211_164800_EMAIL-00355.eml) | 2024-02-11T16:48:00+00:00 |
| `20240213_084800_EMAIL-00369-eml` | email | [emails/2024-02/20240213_084800_EMAIL-00369.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240213_084800_EMAIL-00369.eml) | 2024-02-13T08:48:00+00:00 |
| `20240220_102700_EMAIL-00422-eml` | email | [emails/2024-02/20240220_102700_EMAIL-00422.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240220_102700_EMAIL-00422.eml) | 2024-02-20T10:27:00+00:00 |
| `20240328_130600_EMAIL-00755-eml` | email | [emails/2024-03/20240328_130600_EMAIL-00755.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240328_130600_EMAIL-00755.eml) | 2024-03-28T13:06:00+00:00 |
| `20240405_122700_EMAIL-00836-eml` | email | [emails/2024-04/20240405_122700_EMAIL-00836.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240405_122700_EMAIL-00836.eml) | 2024-04-05T12:27:00+00:00 |
| `20240430_112200_EMAIL-01081-eml` | email | [emails/2024-04/20240430_112200_EMAIL-01081.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240430_112200_EMAIL-01081.eml) | 2024-04-30T11:22:00+00:00 |
| `20240510_221500_EMAIL-01172-eml` | email | [emails/2024-05/20240510_221500_EMAIL-01172.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240510_221500_EMAIL-01172.eml) | 2024-05-10T22:15:00+00:00 |
| `20240511_061500_EMAIL-01174-eml` | email | [emails/2024-05/20240511_061500_EMAIL-01174.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240511_061500_EMAIL-01174.eml) | 2024-05-11T06:15:00+00:00 |
| `20240604_164100_EMAIL-01404-eml` | email | [emails/2024-06/20240604_164100_EMAIL-01404.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240604_164100_EMAIL-01404.eml) | 2024-06-04T16:41:00+00:00 |
| `20240613_172100_EMAIL-01485-eml` | email | [emails/2024-06/20240613_172100_EMAIL-01485.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240613_172100_EMAIL-01485.eml) | 2024-06-13T17:21:00+00:00 |
| `20240615_152100_EMAIL-01504-eml` | email | [emails/2024-06/20240615_152100_EMAIL-01504.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240615_152100_EMAIL-01504.eml) | 2024-06-15T15:21:00+00:00 |
| `20240618_202100_EMAIL-01534-eml` | email | [emails/2024-06/20240618_202100_EMAIL-01534.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240618_202100_EMAIL-01534.eml) | 2024-06-18T20:21:00+00:00 |
| `20240704_142900_EMAIL-01653-eml` | email | [emails/2024-07/20240704_142900_EMAIL-01653.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240704_142900_EMAIL-01653.eml) | 2024-07-04T14:29:00+00:00 |
| `20240704_182900_EMAIL-01658-eml` | email | [emails/2024-07/20240704_182900_EMAIL-01658.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240704_182900_EMAIL-01658.eml) | 2024-07-04T18:29:00+00:00 |
| `20240706_154200_EMAIL-01674-eml` | email | [emails/2024-07/20240706_154200_EMAIL-01674.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240706_154200_EMAIL-01674.eml) | 2024-07-06T15:42:00+00:00 |
| `20240707_121800_EMAIL-01683-eml` | email | [emails/2024-07/20240707_121800_EMAIL-01683.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240707_121800_EMAIL-01683.eml) | 2024-07-07T12:18:00+00:00 |
| `20240714_111900_EMAIL-01756-eml` | email | [emails/2024-07/20240714_111900_EMAIL-01756.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240714_111900_EMAIL-01756.eml) | 2024-07-14T11:19:00+00:00 |
| `20240714_163800_EMAIL-01764-eml` | email | [emails/2024-07/20240714_163800_EMAIL-01764.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240714_163800_EMAIL-01764.eml) | 2024-07-14T16:38:00+00:00 |
| `20240722_163800_EMAIL-01832-eml` | email | [emails/2024-07/20240722_163800_EMAIL-01832.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240722_163800_EMAIL-01832.eml) | 2024-07-22T16:38:00+00:00 |
| `20240723_093800_EMAIL-01838-eml` | email | [emails/2024-07/20240723_093800_EMAIL-01838.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240723_093800_EMAIL-01838.eml) | 2024-07-23T09:38:00+00:00 |
| `20240729_120500_EMAIL-01897-eml` | email | [emails/2024-07/20240729_120500_EMAIL-01897.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240729_120500_EMAIL-01897.eml) | 2024-07-29T12:05:00+00:00 |
| `20240731_092000_EMAIL-01911-eml` | email | [emails/2024-07/20240731_092000_EMAIL-01911.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240731_092000_EMAIL-01911.eml) | 2024-07-31T09:20:00+00:00 |
| `20240909_154700_EMAIL-02303-eml` | email | [emails/2024-09/20240909_154700_EMAIL-02303.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240909_154700_EMAIL-02303.eml) | 2024-09-09T15:47:00+00:00 |
| `20241102_122600_EMAIL-02797-eml` | email | [emails/2024-11/20241102_122600_EMAIL-02797.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241102_122600_EMAIL-02797.eml) | 2024-11-02T12:26:00+00:00 |
| `20241114_155700_EMAIL-02905-eml` | email | [emails/2024-11/20241114_155700_EMAIL-02905.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241114_155700_EMAIL-02905.eml) | 2024-11-14T15:57:00+00:00 |
| `20241119_172100_EMAIL-02952-eml` | email | [emails/2024-11/20241119_172100_EMAIL-02952.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241119_172100_EMAIL-02952.eml) | 2024-11-19T17:21:00+00:00 |
| `20241123_193100_EMAIL-02994-eml` | email | [emails/2024-11/20241123_193100_EMAIL-02994.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241123_193100_EMAIL-02994.eml) | 2024-11-23T19:31:00+00:00 |
| `20241201_131700_EMAIL-03058-eml` | email | [emails/2024-12/20241201_131700_EMAIL-03058.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241201_131700_EMAIL-03058.eml) | 2024-12-01T13:17:00+00:00 |
| `20241223_151800_EMAIL-03254-eml` | email | [emails/2024-12/20241223_151800_EMAIL-03254.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241223_151800_EMAIL-03254.eml) | 2024-12-23T15:18:00+00:00 |
| `20241224_133300_EMAIL-03261-eml` | email | [emails/2024-12/20241224_133300_EMAIL-03261.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241224_133300_EMAIL-03261.eml) | 2024-12-24T13:33:00+00:00 |
| `20250102_081300_EMAIL-03352-eml` | email | [emails/2025-01/20250102_081300_EMAIL-03352.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250102_081300_EMAIL-03352.eml) | 2025-01-02T08:13:00+00:00 |
| `20250109_221300_EMAIL-03427-eml` | email | [emails/2025-01/20250109_221300_EMAIL-03427.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250109_221300_EMAIL-03427.eml) | 2025-01-09T22:13:00+00:00 |
| `20250201_100000_EMAIL-03617-eml` | email | [emails/2025-02/20250201_100000_EMAIL-03617.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250201_100000_EMAIL-03617.eml) | 2025-02-01T10:00:00+00:00 |
| `20250306_011900_EMAIL-03929-eml` | email | [emails/2025-03/20250306_011900_EMAIL-03929.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250306_011900_EMAIL-03929.eml) | 2025-03-06T01:19:00+00:00 |
| `20250308_091600_EMAIL-03950-eml` | email | [emails/2025-03/20250308_091600_EMAIL-03950.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250308_091600_EMAIL-03950.eml) | 2025-03-08T09:16:00+00:00 |
| `20250310_143800_EMAIL-03978-eml` | email | [emails/2025-03/20250310_143800_EMAIL-03978.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250310_143800_EMAIL-03978.eml) | 2025-03-10T14:38:00+00:00 |
| `20250311_143800_EMAIL-03987-eml` | email | [emails/2025-03/20250311_143800_EMAIL-03987.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250311_143800_EMAIL-03987.eml) | 2025-03-11T14:38:00+00:00 |
| `20250330_110300_EMAIL-04157-eml` | email | [emails/2025-03/20250330_110300_EMAIL-04157.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250330_110300_EMAIL-04157.eml) | 2025-03-30T11:03:00+00:00 |
| `20250517_145300_EMAIL-04542-eml` | email | [emails/2025-05/20250517_145300_EMAIL-04542.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250517_145300_EMAIL-04542.eml) | 2025-05-17T14:53:00+00:00 |
| `20250518_111100_EMAIL-04548-eml` | email | [emails/2025-05/20250518_111100_EMAIL-04548.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250518_111100_EMAIL-04548.eml) | 2025-05-18T11:11:00+00:00 |
| `20250601_153800_EMAIL-04681-eml` | email | [emails/2025-06/20250601_153800_EMAIL-04681.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250601_153800_EMAIL-04681.eml) | 2025-06-01T15:38:00+00:00 |
| `20250607_153100_EMAIL-04717-eml` | email | [emails/2025-06/20250607_153100_EMAIL-04717.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250607_153100_EMAIL-04717.eml) | 2025-06-07T15:31:00+00:00 |
| `20250627_163500_EMAIL-04891-eml` | email | [emails/2025-06/20250627_163500_EMAIL-04891.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250627_163500_EMAIL-04891.eml) | 2025-06-27T16:35:00+00:00 |
| `20250701_110800_EMAIL-04918-eml` | email | [emails/2025-07/20250701_110800_EMAIL-04918.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250701_110800_EMAIL-04918.eml) | 2025-07-01T11:08:00+00:00 |
| `20250705_160400_EMAIL-04954-eml` | email | [emails/2025-07/20250705_160400_EMAIL-04954.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250705_160400_EMAIL-04954.eml) | 2025-07-05T16:04:00+00:00 |
| `20250714_221000_EMAIL-05038-eml` | email | [emails/2025-07/20250714_221000_EMAIL-05038.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250714_221000_EMAIL-05038.eml) | 2025-07-14T22:10:00+00:00 |
| `20250723_172900_EMAIL-05126-eml` | email | [emails/2025-07/20250723_172900_EMAIL-05126.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250723_172900_EMAIL-05126.eml) | 2025-07-23T17:29:00+00:00 |
| `20250824_091400_EMAIL-05389-eml` | email | [emails/2025-08/20250824_091400_EMAIL-05389.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250824_091400_EMAIL-05389.eml) | 2025-08-24T09:14:00+00:00 |
| `20250825_143500_EMAIL-05399-eml` | email | [emails/2025-08/20250825_143500_EMAIL-05399.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250825_143500_EMAIL-05399.eml) | 2025-08-25T14:35:00+00:00 |
| `20250910_165500_EMAIL-05590-eml` | email | [emails/2025-09/20250910_165500_EMAIL-05590.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250910_165500_EMAIL-05590.eml) | 2025-09-10T16:55:00+00:00 |
| `20250912_145600_EMAIL-05608-eml` | email | [emails/2025-09/20250912_145600_EMAIL-05608.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250912_145600_EMAIL-05608.eml) | 2025-09-12T14:56:00+00:00 |
| `20251002_124100_EMAIL-05758-eml` | email | [emails/2025-10/20251002_124100_EMAIL-05758.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251002_124100_EMAIL-05758.eml) | 2025-10-02T12:41:00+00:00 |
| `20251012_150900_EMAIL-05850-eml` | email | [emails/2025-10/20251012_150900_EMAIL-05850.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251012_150900_EMAIL-05850.eml) | 2025-10-12T15:09:00+00:00 |
| `20251013_101200_EMAIL-05858-eml` | email | [emails/2025-10/20251013_101200_EMAIL-05858.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251013_101200_EMAIL-05858.eml) | 2025-10-13T10:12:00+00:00 |
| `20251013_105700_EMAIL-05859-eml` | email | [emails/2025-10/20251013_105700_EMAIL-05859.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251013_105700_EMAIL-05859.eml) | 2025-10-13T10:57:00+00:00 |
| `20251013_170600_EMAIL-05869-eml` | email | [emails/2025-10/20251013_170600_EMAIL-05869.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251013_170600_EMAIL-05869.eml) | 2025-10-13T17:06:00+00:00 |
| `20251014_111300_EMAIL-05877-eml` | email | [emails/2025-10/20251014_111300_EMAIL-05877.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251014_111300_EMAIL-05877.eml) | 2025-10-14T11:13:00+00:00 |
| `20251015_005700_EMAIL-05883-eml` | email | [emails/2025-10/20251015_005700_EMAIL-05883.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251015_005700_EMAIL-05883.eml) | 2025-10-15T00:57:00+00:00 |
| `20251019_021200_EMAIL-05909-eml` | email | [emails/2025-10/20251019_021200_EMAIL-05909.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251019_021200_EMAIL-05909.eml) | 2025-10-19T02:12:00+00:00 |
| `20251022_030900_EMAIL-05931-eml` | email | [emails/2025-10/20251022_030900_EMAIL-05931.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251022_030900_EMAIL-05931.eml) | 2025-10-22T03:09:00+00:00 |
| `20251022_112900_EMAIL-05934-eml` | email | [emails/2025-10/20251022_112900_EMAIL-05934.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251022_112900_EMAIL-05934.eml) | 2025-10-22T11:29:00+00:00 |
| `20251027_144600_EMAIL-05982-eml` | email | [emails/2025-10/20251027_144600_EMAIL-05982.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251027_144600_EMAIL-05982.eml) | 2025-10-27T14:46:00+00:00 |
| `20251208_175900_EMAIL-06331-eml` | email | [emails/2025-12/20251208_175900_EMAIL-06331.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251208_175900_EMAIL-06331.eml) | 2025-12-08T17:59:00+00:00 |
| `20251217_145100_EMAIL-06423-eml` | email | [emails/2025-12/20251217_145100_EMAIL-06423.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251217_145100_EMAIL-06423.eml) | 2025-12-17 |
| `20251224_135900_EMAIL-06483-eml` | email | [emails/2025-12/20251224_135900_EMAIL-06483.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251224_135900_EMAIL-06483.eml) | 2025-12-24T13:59:00+00:00 |
| `20251224_165900_EMAIL-06485-eml` | email | [emails/2025-12/20251224_165900_EMAIL-06485.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251224_165900_EMAIL-06485.eml) | 2025-12-24 |
| `20251228_105000_EMAIL-06506-eml` | email | [emails/2025-12/20251228_105000_EMAIL-06506.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251228_105000_EMAIL-06506.eml) | 2025-12-28T10:50:00+00:00 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-26T09:51:02+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
