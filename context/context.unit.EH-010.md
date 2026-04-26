# context.unit.<!-- auto:unit_id -->EH-010<!-- /auto:unit_id -->.md

> Per-unit dossier (one file per Einheit). Holds everything specific to this unit:
> the unit itself, the active lease, the tenant(s), and all unit/tenant-specific operations.
> **Property-wide data lives in `context.property.md`** — see `parent_property_ref` below.

<!-- auto:meta -->
- last_built_at: `2026-04-26T09:28:51+00:00`
- build_hash: `engine-v2`
- engine_version: `0.2.0`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `unit`
- unit_id: `EH-010`
- property_id: `LIE-001`
- parent_property_ref: `context.property.LIE-001.md`
- owner_ref: `EIG-016`
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit.summary -->[Administrative] Einheit WE 10 (EH-010): 3,5-Zimmer-Wohnung, 92 qm, 4. OG links, Miteigentumsanteil 214/10000 [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#einheit/EH-010). Letzte Mietzahlung 1.583,00 EUR am 2025-11-03 durch Kiara Mcintyre erfasst [(bank)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv#TX-00004); Ticket "Key replacement" von Anna Berger am 2025-12-22 dokumentiert. Keine Abweichungen oder Verzugsmerkmale in aktuellen Stammdaten erkannt.<!-- /auto:unit.summary -->

<!-- auto:unit -->
- unit_id: `EH-010`
- label: WE 10
- haus_id: `HAUS-12`
- floor: 4. OG
- position: links
- typ: Wohnung
- area_sqm: 92.0
- rooms: 3.5
- mea_‰: 214
- equipment: _(no data in source yet)_
- media_supply: _(no data in source yet)_
- key_inventory: _(no data in source yet)_
- meters: _(no data in source yet)_
- occupancy_status: `rented`
- nk_keys: _(no data in source yet)_
<!-- /auto:unit -->

---

## 2. Lease (Mietverhältnis, voll)
<!-- auto:lease.summary -->_no issue_<!-- /auto:lease.summary -->

<!-- auto:lease -->
- lease_id: `LEASE-MIE-013`
- unit_ref: `EH-010`
- start_date: 2020-10-20 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-013)
- end_date: _(no data in source yet)_
- term_type: `unbefristet`
- cancellation_status: `none`
- rent_components: { kaltmiete: 1261.0, betriebskosten_vorauszahlung: 322.0, total_warmmiete: 1583.00 }
- payment_mode: Überweisung
- iban_payer: DE54100701244740748217 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-013)
- kaution: { amount: 3783.0 }
- usage: `residential`
- subletting: { current_status: `none` }
- special_agreements: _(no data in source yet)_
<!-- /auto:lease -->

### 2.1 Tenants on this Lease
<!-- auto:tenants.summary -->_no issue_<!-- /auto:tenants.summary -->

<!-- auto:tenants -->
| tenant_id | name | role | contact_email | contact_phone | comms_pref | gesamtschuldner |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-013` | Frau Kiara Mcintyre | haupt | kiara.mcintyre@icloud.com | (547)845-1712 | email | — |
<!-- /auto:tenants -->

---

## 3. Operations (this unit / this tenant)

### 3.1 Open Tickets — Critical (overdue or due ≤7 days)
<!-- auto:tickets.critical.summary -->[Emergency] Wasserschaden in EH-010 seit 2025-10-08 gemeldet (wiederholte Meldungen 2025-10-08, 2025-10-10, 2025-10-26, 2025-12-02, 2025-12-04, 2025-12-13/14); Verwaltung bestätigte Auftragserteilung mehrfach [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251010_144100_EMAIL-05835.eml), aber kein Nachweis der Behebung nach 171 Tagen. Mieterin hat Recht auf „unverzügliche" Mängelbeseitigung (§ 535 II BGB); Wassereintritt aus Obergeschoss ist Wohnmangel, der Gebrauchstauglichkeit erheblich mindert. Deadline zur Handwerkereinsatz überschritten; Verwaltung muss Beseitigung nachweisen oder Schadensersatzforderung der Mieterin ist fällig (§ 536a BGB).<!-- /auto:tickets.critical.summary -->

<!-- auto:tickets.critical -->
| ticket_id | type | title | deadline | status | assignee |
| --- | --- | --- | --- | --- | --- |
| `TKT-d3e61dd9` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-37f1e8e5` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-06a0ccdd` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-6834feff` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-2bf2ef15` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-0cb369b7` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-078ac1d6` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-09454ad1` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-92b60c37` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-afcf065b` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-a4101b68` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-5aa30413` | wasserschaden | Re: Water damage in bathroom | — | open | — |
| `TKT-13612a18` | wasserschaden | Re: Water damage in bathroom | — | open | — |
| `TKT-793d9826` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-bf0a88d7` | wasserschaden | Re: Water damage in bathroom | — | open | — |
| `TKT-e46982e0` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-c59ba490` | wasserschaden | Re: Water damage in bathroom | — | open | — |
| `TKT-d2484c1f` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-26f81368` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-f92b0977` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-dd24ec77` | wasserschaden | Re: Water damage in bathroom | — | open | — |
| `TKT-f4dafa66` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-d96baf28` | wasserschaden | Re: Water damage in bathroom | — | open | — |
| `TKT-4bf6a06a` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-71de9834` | wasserschaden | Re: Water damage in bathroom | — | open | — |
| `TKT-32f1b42f` | wasserschaden | Water damage in bathroom | — | open | — |
| `TKT-b2f64ab1` | wasserschaden | Water damage in bathroom | — | open | — |
<!-- /auto:tickets.critical -->

### 3.2 Open Tickets — Aggregate
<!-- auto:tickets.aggregate.summary -->[Routine] Einheit EH-010: Schlüsselersatz-Anfrage eingegangen am 2025-12-22, Status „normal". Anfrage dokumentiert in mehreren E-Mail-Austauschprozessen seit Januar 2024 [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240118_100000_EMAIL-00142.eml). Schlüsselersatz ist Instandhaltungspflicht des Vermieters nach § 535 Abs. 1 BGB; Bearbeitung erforderlich.<!-- /auto:tickets.aggregate.summary -->

<!-- auto:tickets.aggregate -->
- total_open: `52`
- by_type: { schluessel: `25`, wasserschaden: `27` }
- live source: `db.tickets WHERE unit_id=EH-010 AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren

<!-- auto:dunning.summary -->[Routine] Mieter MIE-013 ist seit vier Monaten im Verzug; offener Betrag 6.332,00 EUR zzgl. 82,58 EUR Verzugszinsen, letzte Zahlung 2025-12-02 [(bank)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv#TX-01565). Vertraglich geschuldet sind monatlich 1.583,00 EUR (Kaltmiete 1.261,00 EUR + NK-Vorauszahlung 322,00 EUR) [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-013). Verzug nach § 286 BGB festgestellt, Verzugszinsen § 288 I BGB; Mahnstufe 1 aktiv, nächster Schritt: 2. Mahnung nach 14 Tagen fällig.<!-- /auto:dunning.summary -->

#### Per claim
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
| `MIE-013` | — | 1 | 6332.00 EUR | 2025-12-02 | — | — |
- live balance pointer: `db.tenant_balance.tenant_id=MIE-013`
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
<!-- auto:sticky-threads.summary -->[Routine] Mieter MIE-013 (WE 10) meldet seit 2024-01-19 Schlüsselverlust; Thread mit 45 Nachrichten, letzte Antwort der Verwaltung 2025-12-22 mit Zusage zur Beauftragung eines Handwerkers [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251222_235000_EMAIL-06471.eml). Schlüsselersatz ist Vermieterpflicht (Instandhaltung nach BGB § 535 I BGB, Schlosswechsel § 433 BGB), Umsetzung überfällig; Handwerker-Auftrag muss spätestens bis 2026-05-03 dokumentiert sein. Parallel: EH-010 Mieterwechsel seit 2025-03-06 initiiert, Freiwerdung 2025-04-30 geplant — Schlüsselübergabe an Nachmieter muss mit neuer Schließanlage koordiniert werden.<!-- /auto:sticky-threads.summary -->

<!-- auto:sticky-threads -->
| thread_id | subject | last_msg_date | parties | status | one-line outcome | pointer |
| --- | --- | --- | --- | --- | --- | --- |
| `TH-9b2179` | Water damage in bathroom | 2025-12-18 | `MIE-013` | active | 61 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251218_135000_EMAIL-06433.eml) |
| `TH-91663d` | Key replacement | 2025-12-22 | `MIE-013` | active | 45 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251222_235000_EMAIL-06471.eml) |
| `TH-fb3e38` | Mieterwechsel in WE 10 | 2025-03-06 | `EH-010` | active | 3 msgs | [(emails)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250306_150700_EMAIL-03935.eml) |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance.summary -->[Routine] Mieter MIE-013 (Kiara Mcintyre, WE 10) ist seit vier Monaten im Verzug; offener Betrag 6.332,00 EUR zzgl. 82,58 EUR Verzugszinsen, letzte Zahlung 2025-12-02 [(bank)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv#TX-00004). Vertraglich geschuldet sind monatlich 1.583,00 EUR (Kaltmiete 1.261,00 EUR + NK-Vorauszahlung 322,00 EUR) [(stammdaten)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#mieter/MIE-013). Verzug nach § 286 BGB festgestellt, Verzugszinsen § 288 I BGB (Basiszins 3,5 % + 5 pp); Mahnstufe 1 aktiv seit 2026-04-26, nächster Schritt: 2. Mahnung nach 14 Tagen (Fälligkeitsdatum ca. 2026-05-10).<!-- /auto:provenance.summary -->

<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `kontoauszug_2024_2025-csv` | bank | [bank/kontoauszug_2024_2025.csv](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv) | 2026-04-26 |
| `20240118_100000_EMAIL-00142-eml` | email | [emails/2024-01/20240118_100000_EMAIL-00142.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240118_100000_EMAIL-00142.eml) | 2024-01-18T10:00:00+00:00 |
| `20240203_145800_EMAIL-00286-eml` | email | [emails/2024-02/20240203_145800_EMAIL-00286.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240203_145800_EMAIL-00286.eml) | 2024-02-03T14:58:00+00:00 |
| `20240204_015800_EMAIL-00292-eml` | email | [emails/2024-02/20240204_015800_EMAIL-00292.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240204_015800_EMAIL-00292.eml) | 2024-02-04T01:58:00+00:00 |
| `20240206_150600_EMAIL-00318-eml` | email | [emails/2024-02/20240206_150600_EMAIL-00318.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240206_150600_EMAIL-00318.eml) | 2024-02-06T15:06:00+00:00 |
| `20240214_183700_EMAIL-00382-eml` | email | [emails/2024-02/20240214_183700_EMAIL-00382.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240214_183700_EMAIL-00382.eml) | 2024-02-14T18:37:00+00:00 |
| `20240304_114700_EMAIL-00546-eml` | email | [emails/2024-03/20240304_114700_EMAIL-00546.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240304_114700_EMAIL-00546.eml) | 2024-03-04T11:47:00+00:00 |
| `20240307_175200_EMAIL-00579-eml` | email | [emails/2024-03/20240307_175200_EMAIL-00579.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240307_175200_EMAIL-00579.eml) | 2024-03-07T17:52:00+00:00 |
| `20240331_145100_EMAIL-00784-eml` | email | [emails/2024-03/20240331_145100_EMAIL-00784.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240331_145100_EMAIL-00784.eml) | 2024-03-31T14:51:00+00:00 |
| `20240514_141900_EMAIL-01220-eml` | email | [emails/2024-05/20240514_141900_EMAIL-01220.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240514_141900_EMAIL-01220.eml) | 2024-05-14T14:19:00+00:00 |
| `20240515_110000_EMAIL-01227-eml` | email | [emails/2024-05/20240515_110000_EMAIL-01227.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240515_110000_EMAIL-01227.eml) | 2024-05-15T11:00:00+00:00 |
| `20240517_154100_EMAIL-01240-eml` | email | [emails/2024-05/20240517_154100_EMAIL-01240.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240517_154100_EMAIL-01240.eml) | 2024-05-17T15:41:00+00:00 |
| `20240519_181400_EMAIL-01256-eml` | email | [emails/2024-05/20240519_181400_EMAIL-01256.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240519_181400_EMAIL-01256.eml) | 2024-05-19T18:14:00+00:00 |
| `20240618_161400_EMAIL-01530-eml` | email | [emails/2024-06/20240618_161400_EMAIL-01530.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240618_161400_EMAIL-01530.eml) | 2024-06-18T16:14:00+00:00 |
| `20240624_160400_EMAIL-01582-eml` | email | [emails/2024-06/20240624_160400_EMAIL-01582.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240624_160400_EMAIL-01582.eml) | 2024-06-24T16:04:00+00:00 |
| `20240629_131700_EMAIL-01622-eml` | email | [emails/2024-06/20240629_131700_EMAIL-01622.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240629_131700_EMAIL-01622.eml) | 2024-06-29T13:17:00+00:00 |
| `20240701_101700_EMAIL-01632-eml` | email | [emails/2024-07/20240701_101700_EMAIL-01632.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240701_101700_EMAIL-01632.eml) | 2024-07-01T10:17:00+00:00 |
| `20240708_095000_EMAIL-01692-eml` | email | [emails/2024-07/20240708_095000_EMAIL-01692.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240708_095000_EMAIL-01692.eml) | 2024-07-08T09:50:00+00:00 |
| `20240708_101700_EMAIL-01693-eml` | email | [emails/2024-07/20240708_101700_EMAIL-01693.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240708_101700_EMAIL-01693.eml) | 2024-07-08T10:17:00+00:00 |
| `20240708_150800_EMAIL-01699-eml` | email | [emails/2024-07/20240708_150800_EMAIL-01699.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240708_150800_EMAIL-01699.eml) | 2024-07-08T15:08:00+00:00 |
| `20240709_130800_EMAIL-01706-eml` | email | [emails/2024-07/20240709_130800_EMAIL-01706.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240709_130800_EMAIL-01706.eml) | 2024-07-09T13:08:00+00:00 |
| `20240714_160900_EMAIL-01762-eml` | email | [emails/2024-07/20240714_160900_EMAIL-01762.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240714_160900_EMAIL-01762.eml) | 2024-07-14T16:09:00+00:00 |
| `20240716_000900_EMAIL-01770-eml` | email | [emails/2024-07/20240716_000900_EMAIL-01770.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240716_000900_EMAIL-01770.eml) | 2024-07-16T00:09:00+00:00 |
| `20240720_112100_EMAIL-01812-eml` | email | [emails/2024-07/20240720_112100_EMAIL-01812.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240720_112100_EMAIL-01812.eml) | 2024-07-20T11:21:00+00:00 |
| `20240725_175400_EMAIL-01861-eml` | email | [emails/2024-07/20240725_175400_EMAIL-01861.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240725_175400_EMAIL-01861.eml) | 2024-07-25T17:54:00+00:00 |
| `20240905_131800_EMAIL-02254-eml` | email | [emails/2024-09/20240905_131800_EMAIL-02254.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240905_131800_EMAIL-02254.eml) | 2024-09-05T13:18:00+00:00 |
| `20240913_110300_EMAIL-02342-eml` | email | [emails/2024-09/20240913_110300_EMAIL-02342.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240913_110300_EMAIL-02342.eml) | 2024-09-13T11:03:00+00:00 |
| `20240914_165900_EMAIL-02355-eml` | email | [emails/2024-09/20240914_165900_EMAIL-02355.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240914_165900_EMAIL-02355.eml) | 2024-09-14T16:59:00+00:00 |
| `20240915_020300_EMAIL-02357-eml` | email | [emails/2024-09/20240915_020300_EMAIL-02357.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240915_020300_EMAIL-02357.eml) | 2024-09-15T02:03:00+00:00 |
| `20240919_225700_EMAIL-02388-eml` | email | [emails/2024-09/20240919_225700_EMAIL-02388.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240919_225700_EMAIL-02388.eml) | 2024-09-19T22:57:00+00:00 |
| `20240923_020300_EMAIL-02419-eml` | email | [emails/2024-09/20240923_020300_EMAIL-02419.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240923_020300_EMAIL-02419.eml) | 2024-09-23T02:03:00+00:00 |
| `20241005_153500_EMAIL-02531-eml` | email | [emails/2024-10/20241005_153500_EMAIL-02531.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241005_153500_EMAIL-02531.eml) | 2024-10-05T15:35:00+00:00 |
| `20241017_153200_EMAIL-02636-eml` | email | [emails/2024-10/20241017_153200_EMAIL-02636.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241017_153200_EMAIL-02636.eml) | 2024-10-17T15:32:00+00:00 |
| `20241017_171500_EMAIL-02639-eml` | email | [emails/2024-10/20241017_171500_EMAIL-02639.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241017_171500_EMAIL-02639.eml) | 2024-10-17T17:15:00+00:00 |
| `20241019_131500_EMAIL-02654-eml` | email | [emails/2024-10/20241019_131500_EMAIL-02654.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241019_131500_EMAIL-02654.eml) | 2024-10-19T13:15:00+00:00 |
| `20241026_111700_EMAIL-02726-eml` | email | [emails/2024-10/20241026_111700_EMAIL-02726.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241026_111700_EMAIL-02726.eml) | 2024-10-26T11:17:00+00:00 |
| `20241110_110400_EMAIL-02863-eml` | email | [emails/2024-11/20241110_110400_EMAIL-02863.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241110_110400_EMAIL-02863.eml) | 2024-11-10T11:04:00+00:00 |
| `20241116_165600_EMAIL-02932-eml` | email | [emails/2024-11/20241116_165600_EMAIL-02932.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241116_165600_EMAIL-02932.eml) | 2024-11-16T16:56:00+00:00 |
| `20241127_094600_EMAIL-03020-eml` | email | [emails/2024-11/20241127_094600_EMAIL-03020.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241127_094600_EMAIL-03020.eml) | 2024-11-27T09:46:00+00:00 |
| `20241209_163100_EMAIL-03134-eml` | email | [emails/2024-12/20241209_163100_EMAIL-03134.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241209_163100_EMAIL-03134.eml) | 2024-12-09T16:31:00+00:00 |
| `20241210_123100_EMAIL-03140-eml` | email | [emails/2024-12/20241210_123100_EMAIL-03140.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241210_123100_EMAIL-03140.eml) | 2024-12-10T12:31:00+00:00 |
| `20241223_160200_EMAIL-03255-eml` | email | [emails/2024-12/20241223_160200_EMAIL-03255.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241223_160200_EMAIL-03255.eml) | 2024-12-23T16:02:00+00:00 |
| `20241226_100500_EMAIL-03280-eml` | email | [emails/2024-12/20241226_100500_EMAIL-03280.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241226_100500_EMAIL-03280.eml) | 2024-12-26T10:05:00+00:00 |
| `20250110_110500_EMAIL-03431-eml` | email | [emails/2025-01/20250110_110500_EMAIL-03431.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250110_110500_EMAIL-03431.eml) | 2025-01-10T11:05:00+00:00 |
| `20250206_163800_EMAIL-03665-eml` | email | [emails/2025-02/20250206_163800_EMAIL-03665.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250206_163800_EMAIL-03665.eml) | 2025-02-06T16:38:00+00:00 |
| `20250208_145900_EMAIL-03677-eml` | email | [emails/2025-02/20250208_145900_EMAIL-03677.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250208_145900_EMAIL-03677.eml) | 2025-02-08T14:59:00+00:00 |
| `20250215_144700_EMAIL-03745-eml` | email | [emails/2025-02/20250215_144700_EMAIL-03745.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250215_144700_EMAIL-03745.eml) | 2025-02-15T14:47:00+00:00 |
| `20250223_104000_EMAIL-03819-eml` | email | [emails/2025-02/20250223_104000_EMAIL-03819.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250223_104000_EMAIL-03819.eml) | 2025-02-23T10:40:00+00:00 |
| `20250223_144000_EMAIL-03824-eml` | email | [emails/2025-02/20250223_144000_EMAIL-03824.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250223_144000_EMAIL-03824.eml) | 2025-02-23T14:40:00+00:00 |
| `20250226_084600_EMAIL-03856-eml` | email | [emails/2025-02/20250226_084600_EMAIL-03856.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250226_084600_EMAIL-03856.eml) | 2025-02-26T08:46:00+00:00 |
| `20250306_150700_EMAIL-03935-eml` | email | [emails/2025-03/20250306_150700_EMAIL-03935.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250306_150700_EMAIL-03935.eml) | 2025-03-06 |
| `20250308_102200_EMAIL-03952-eml` | email | [emails/2025-03/20250308_102200_EMAIL-03952.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250308_102200_EMAIL-03952.eml) | 2025-03-08T10:22:00+00:00 |
| `20250318_153900_EMAIL-04057-eml` | email | [emails/2025-03/20250318_153900_EMAIL-04057.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250318_153900_EMAIL-04057.eml) | 2025-03-18T15:39:00+00:00 |
| `20250318_233900_EMAIL-04062-eml` | email | [emails/2025-03/20250318_233900_EMAIL-04062.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250318_233900_EMAIL-04062.eml) | 2025-03-18T23:39:00+00:00 |
| `20250321_233900_EMAIL-04087-eml` | email | [emails/2025-03/20250321_233900_EMAIL-04087.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250321_233900_EMAIL-04087.eml) | 2025-03-21T23:39:00+00:00 |
| `20250331_085900_EMAIL-04165-eml` | email | [emails/2025-03/20250331_085900_EMAIL-04165.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250331_085900_EMAIL-04165.eml) | 2025-03-31T08:59:00+00:00 |
| `20250331_201400_EMAIL-04171-eml` | email | [emails/2025-03/20250331_201400_EMAIL-04171.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250331_201400_EMAIL-04171.eml) | 2025-03-31T20:14:00+00:00 |
| `20250331_221400_EMAIL-04173-eml` | email | [emails/2025-03/20250331_221400_EMAIL-04173.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250331_221400_EMAIL-04173.eml) | 2025-03-31T22:14:00+00:00 |
| `20250404_221400_EMAIL-04208-eml` | email | [emails/2025-04/20250404_221400_EMAIL-04208.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250404_221400_EMAIL-04208.eml) | 2025-04-04T22:14:00+00:00 |
| `20250405_092300_EMAIL-04209-eml` | email | [emails/2025-04/20250405_092300_EMAIL-04209.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250405_092300_EMAIL-04209.eml) | 2025-04-05T09:23:00+00:00 |
| `20250422_090300_EMAIL-04347-eml` | email | [emails/2025-04/20250422_090300_EMAIL-04347.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250422_090300_EMAIL-04347.eml) | 2025-04-22T09:03:00+00:00 |
| `20250422_220300_EMAIL-04354-eml` | email | [emails/2025-04/20250422_220300_EMAIL-04354.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250422_220300_EMAIL-04354.eml) | 2025-04-22T22:03:00+00:00 |
| `20250423_143500_EMAIL-04356-eml` | email | [emails/2025-04/20250423_143500_EMAIL-04356.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250423_143500_EMAIL-04356.eml) | 2025-04-23T14:35:00+00:00 |
| `20250425_133500_EMAIL-04370-eml` | email | [emails/2025-04/20250425_133500_EMAIL-04370.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250425_133500_EMAIL-04370.eml) | 2025-04-25T13:35:00+00:00 |
| `20250502_142400_EMAIL-04415-eml` | email | [emails/2025-05/20250502_142400_EMAIL-04415.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250502_142400_EMAIL-04415.eml) | 2025-05-02T14:24:00+00:00 |
| `20250503_154200_EMAIL-04428-eml` | email | [emails/2025-05/20250503_154200_EMAIL-04428.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250503_154200_EMAIL-04428.eml) | 2025-05-03T15:42:00+00:00 |
| `20250613_114200_EMAIL-04763-eml` | email | [emails/2025-06/20250613_114200_EMAIL-04763.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250613_114200_EMAIL-04763.eml) | 2025-06-13T11:42:00+00:00 |
| `20250622_102000_EMAIL-04843-eml` | email | [emails/2025-06/20250622_102000_EMAIL-04843.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250622_102000_EMAIL-04843.eml) | 2025-06-22T10:20:00+00:00 |
| `20250622_202000_EMAIL-04851-eml` | email | [emails/2025-06/20250622_202000_EMAIL-04851.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250622_202000_EMAIL-04851.eml) | 2025-06-22T20:20:00+00:00 |
| `20250707_171300_EMAIL-04965-eml` | email | [emails/2025-07/20250707_171300_EMAIL-04965.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250707_171300_EMAIL-04965.eml) | 2025-07-07T17:13:00+00:00 |
| `20250708_001300_EMAIL-04967-eml` | email | [emails/2025-07/20250708_001300_EMAIL-04967.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250708_001300_EMAIL-04967.eml) | 2025-07-08T00:13:00+00:00 |
| `20250718_114200_EMAIL-05068-eml` | email | [emails/2025-07/20250718_114200_EMAIL-05068.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250718_114200_EMAIL-05068.eml) | 2025-07-18T11:42:00+00:00 |
| `20250719_155800_EMAIL-05085-eml` | email | [emails/2025-07/20250719_155800_EMAIL-05085.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250719_155800_EMAIL-05085.eml) | 2025-07-19T15:58:00+00:00 |
| `20250720_004200_EMAIL-05090-eml` | email | [emails/2025-07/20250720_004200_EMAIL-05090.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250720_004200_EMAIL-05090.eml) | 2025-07-20T00:42:00+00:00 |
| `20250723_121100_EMAIL-05121-eml` | email | [emails/2025-07/20250723_121100_EMAIL-05121.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250723_121100_EMAIL-05121.eml) | 2025-07-23T12:11:00+00:00 |
| `20250730_100100_EMAIL-05160-eml` | email | [emails/2025-07/20250730_100100_EMAIL-05160.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250730_100100_EMAIL-05160.eml) | 2025-07-30T10:01:00+00:00 |
| `20250730_125100_EMAIL-05162-eml` | email | [emails/2025-07/20250730_125100_EMAIL-05162.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250730_125100_EMAIL-05162.eml) | 2025-07-30T12:51:00+00:00 |
| `20250730_150100_EMAIL-05165-eml` | email | [emails/2025-07/20250730_150100_EMAIL-05165.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250730_150100_EMAIL-05165.eml) | 2025-07-30T15:01:00+00:00 |
| `20250817_165400_EMAIL-05333-eml` | email | [emails/2025-08/20250817_165400_EMAIL-05333.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250817_165400_EMAIL-05333.eml) | 2025-08-17T16:54:00+00:00 |
| `20250819_095400_EMAIL-05347-eml` | email | [emails/2025-08/20250819_095400_EMAIL-05347.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250819_095400_EMAIL-05347.eml) | 2025-08-19T09:54:00+00:00 |
| `20250827_160100_EMAIL-05420-eml` | email | [emails/2025-08/20250827_160100_EMAIL-05420.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250827_160100_EMAIL-05420.eml) | 2025-08-27T16:01:00+00:00 |
| `20250828_230100_EMAIL-05434-eml` | email | [emails/2025-08/20250828_230100_EMAIL-05434.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250828_230100_EMAIL-05434.eml) | 2025-08-28T23:01:00+00:00 |
| `20250921_184000_EMAIL-05683-eml` | email | [emails/2025-09/20250921_184000_EMAIL-05683.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250921_184000_EMAIL-05683.eml) | 2025-09-21T18:40:00+00:00 |
| `20250924_141600_EMAIL-05702-eml` | email | [emails/2025-09/20250924_141600_EMAIL-05702.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250924_141600_EMAIL-05702.eml) | 2025-09-24T14:16:00+00:00 |
| `20251008_144100_EMAIL-05812-eml` | email | [emails/2025-10/20251008_144100_EMAIL-05812.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251008_144100_EMAIL-05812.eml) | 2025-10-08T14:41:00+00:00 |
| `20251008_152500_EMAIL-05814-eml` | email | [emails/2025-10/20251008_152500_EMAIL-05814.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251008_152500_EMAIL-05814.eml) | 2025-10-08T15:25:00+00:00 |
| `20251010_144100_EMAIL-05835-eml` | email | [emails/2025-10/20251010_144100_EMAIL-05835.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251010_144100_EMAIL-05835.eml) | 2025-10-10T14:41:00+00:00 |
| `20251026_152300_EMAIL-05974-eml` | email | [emails/2025-10/20251026_152300_EMAIL-05974.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251026_152300_EMAIL-05974.eml) | 2025-10-26T15:23:00+00:00 |
| `20251026_182300_EMAIL-05977-eml` | email | [emails/2025-10/20251026_182300_EMAIL-05977.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251026_182300_EMAIL-05977.eml) | 2025-10-26T18:23:00+00:00 |
| `20251202_144500_EMAIL-06280-eml` | email | [emails/2025-12/20251202_144500_EMAIL-06280.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251202_144500_EMAIL-06280.eml) | 2025-12-02T14:45:00+00:00 |
| `20251204_124500_EMAIL-06294-eml` | email | [emails/2025-12/20251204_124500_EMAIL-06294.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251204_124500_EMAIL-06294.eml) | 2025-12-04T12:45:00+00:00 |
| `20251213_221700_EMAIL-06384-eml` | email | [emails/2025-12/20251213_221700_EMAIL-06384.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251213_221700_EMAIL-06384.eml) | 2025-12-13T22:17:00+00:00 |
| `20251214_175300_EMAIL-06395-eml` | email | [emails/2025-12/20251214_175300_EMAIL-06395.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251214_175300_EMAIL-06395.eml) | 2025-12-14T17:53:00+00:00 |
| `20251218_135000_EMAIL-06433-eml` | email | [emails/2025-12/20251218_135000_EMAIL-06433.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251218_135000_EMAIL-06433.eml) | 2025-12-18 |
| `20251221_165000_EMAIL-06462-eml` | email | [emails/2025-12/20251221_165000_EMAIL-06462.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251221_165000_EMAIL-06462.eml) | 2025-12-21T16:50:00+00:00 |
| `20251222_235000_EMAIL-06471-eml` | email | [emails/2025-12/20251222_235000_EMAIL-06471.eml](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251222_235000_EMAIL-06471.eml) | 2025-12-22T23:50:00+00:00 |
| `stammdaten-json` | stammdaten | [stammdaten/stammdaten.json](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-26T09:26:19+00:00 |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
