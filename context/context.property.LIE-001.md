# context.property.md — <!-- auto:property.display_name -->WEG Immanuelkirchstraße 26<!-- /auto:property.display_name -->

> Property-level dossier (one file per Liegenschaft). Holds everything that is property-wide:
> owners, mandate, WEG decisions, vendors, utilities, authorities, compliance, financials, policies.
> **Per-unit data lives in `context.unit.<unit_id>.md` files** — see §2 Units Index for refs.
> Volatile data (live balances) is NOT stored here — pointers indicate live source.
> Manual edits outside `<!-- auto:* -->` blocks are preserved by the engine.

<!-- auto:meta -->
- last_built_at: `2026-04-26T09:54:22+00:00`
- build_hash: `engine-v2`
- engine_version: `0.2.0`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `property`
<!-- /auto:meta -->

---

## 1. Property
<!-- auto:property.summary -->_no issue_<!-- /auto:property.summary -->

<!-- auto:property -->
- property_id: `LIE-001`
- address: Immanuelkirchstraße 26, 10405 Berlin
- property_type: `residential`
- legal_form: `WEG`
- year_built: 1928 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#liegenschaft/LIE-001)
- year_renovated: 2008 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#liegenschaft/LIE-001)
- total_units: 52
- houses: `HAUS-12`, `HAUS-14`, `HAUS-16`
- bank_accounts.hausgeld: { iban: DE02 1001 0010 0123 4567 89 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#liegenschaft/LIE-001), bank: Postbank Berlin [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#liegenschaft/LIE-001) }
- bank_accounts.ruecklage: { iban: DE12 1203 0000 0098 7654 32 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#liegenschaft/LIE-001) }
- documents: _(no data in source yet)_
<!-- /auto:property -->

### 1.1 Owner(s)
<!-- auto:owners.summary -->_no issue_<!-- /auto:owners.summary -->

<!-- auto:owners -->
| owner_id | name | share_‰ (MEA) | unit_refs | contact | reporting_pref | sale_intent | beirat |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `EIG-001` | Marcus Dowerg | 459 | EH-037, EH-032 | marcus.dowerg@outlook.com | — | none | — |
| `EIG-002` | Gertraud Holsten | 531 | EH-047, EH-033 | gertraud.holsten@gmail.com | — | none | — |
| `EIG-003` | Arnulf Heintze | 520 | EH-025, EH-049 | arnulf.heintze@gmail.com | — | none | — |
| `EIG-004` | Erdal Beckmann | 485 | EH-043, EH-015 | erdal.beckmann@gmx.de | — | none | True |
| `EIG-005` | Josefine Nohlmans | 371 | EH-007, EH-024 | josefine.nohlmans@gmail.com | — | none | — |
| `EIG-006` | Winfried Ullmann | 406 | EH-027, EH-026 | winfried.ullmann@yahoo.de | — | none | — |
| `EIG-007` | Anni Wagenknecht | 370 | EH-048, EH-044 | anni.wagenknecht@gmx.de | — | none | — |
| `EIG-008` | Dunja Schacht | 478 | EH-012, EH-028 | dunja.schacht@gmx.de | — | none | — |
| `EIG-009` | Horst Vollbrecht | 137 | EH-002, EH-038 | horst.vollbrecht@gmx.de | — | none | — |
| `EIG-010` | Ingbert Nerger | 160 | EH-052, EH-050 | ingbert.nerger@gmx.de | — | none | True |
| `EIG-011` | Caroline Bohlander | 436 | EH-031, EH-035 | caroline.bohlander@gmx.de | — | none | — |
| `EIG-012` | Kunigunda Ditschlerin | 503 | EH-005, EH-036 | kunigunda.ditschlerin@icloud.com | — | none | — |
| `EIG-013` | Dominic Jacobs | 474 | EH-023, EH-016 | dominic.jacobs@t-online.de | — | none | — |
| `EIG-014` | Hulda Eckbauer | 305 | EH-019, EH-009 | hulda.eckbauer@t-online.de | — | none | — |
| `EIG-015` | Kranz Vermoegensverwaltung | 388 | EH-011, EH-017 | kranz.vermoegensverwaltung@capital-partners.com | — | none | — |
| `EIG-016` | Wolfgang Hettner | 488 | EH-034, EH-010 | wolfgang.hettner@web.de | — | none | — |
| `EIG-017` | Osman Jacob | 462 | EH-001, EH-030 | osman.jacob@yahoo.de | — | none | — |
| `EIG-018` | Irmingard Margraf | 23 | EH-018 | irmingard.margraf@t-online.de | — | none | — |
| `EIG-019` | Mina Textor | 239 | EH-042 | mina.textor@icloud.com | — | none | — |
| `EIG-020` | Ronald Kelley | 153 | EH-045 | ronald.kelley@icloud.com | — | none | True |
| `EIG-021` | Dörte Kraus | 149 | EH-039 | doerte.kraus@gmx.de | — | none | — |
| `EIG-022` | Tom Hartmann | 279 | EH-029 | tom.hartmann@icloud.com | — | none | — |
| `EIG-023` | Gottlob Hahn | 169 | EH-040 | gottlob.hahn@gmail.com | — | none | — |
| `EIG-024` | Willfried Harloff | 195 | EH-013 | willfried.harloff@yahoo.de | — | none | — |
| `EIG-025` | Hiltrud Speer | 144 | EH-003 | hiltrud.speer@t-online.de | — | none | — |
| `EIG-026` | Silja Henschel | 107 | EH-020 | silja.henschel@posteo.de | — | none | — |
| `EIG-027` | Ingolf Röhricht | 197 | EH-014 | ingolf.roehricht@gmail.com | — | none | — |
| `EIG-028` | Oswald Gröttner | 174 | EH-022 | oswald.groettner@t-online.de | — | none | — |
| `EIG-029` | Sükrü Aumann | 246 | EH-041 | suekrue.aumann@posteo.de | — | none | — |
| `EIG-030` | Dorothe Wulf | 197 | EH-046 | dorothe.wulf@icloud.com | — | none | — |
| `EIG-031` | Dörthe Hövel | 190 | EH-021 | doerthe.hoevel@t-online.de | — | none | — |
| `EIG-032` | Jo Reuter | 197 | EH-051 | jo.reuter@icloud.com | — | none | — |
| `EIG-033` | Xenia Conradi | 111 | EH-008 | xenia.conradi@outlook.com | — | none | — |
| `EIG-034` | Harro Bloch | 139 | EH-004 | harro.bloch@gmail.com | — | none | — |
| `EIG-035` | Markus Fliegner | 118 | EH-006 | markus.fliegner@gmx.de | — | none | — |
<!-- /auto:owners -->
*`sale_intent`: `none | considering | listed | under_contract`; if ≠ none → `{ since, requested_docs[] }` in footnote.*

### 1.2 Verwaltermandat
<!-- auto:mandate.summary -->_no issue_<!-- /auto:mandate.summary -->

<!-- auto:mandate -->
- manager: Huber & Partner Immobilienverwaltung GmbH [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#liegenschaft/LIE-001)
- contact_email: info@huber-partner-verwaltung.de [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#liegenschaft/LIE-001)
- contact_phone: +49 30 12345-0 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#liegenschaft/LIE-001)
- iban: DE89 3704 0044 0532 0130 00 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#liegenschaft/LIE-001)
- bank: Commerzbank Berlin [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#liegenschaft/LIE-001)
- steuernummer: 13/456/78901 [(source)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json#liegenschaft/LIE-001)
- scope: WEG
<!-- /auto:mandate -->

---

## 2. Units Index
> Roster only. Detail lives in per-unit files.

<!-- auto:units-index.summary -->_no issue_<!-- /auto:units-index.summary -->

<!-- auto:units-index -->
| unit_id | label | haus_id | floor | sqm | rooms | typ | mea_‰ | occupancy | owner_ref | unit_md_ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `EH-001` | WE 01 | HAUS-12 | 1. OG | 103.0 | 4.0 | Wohnung | 241 | own-use | `EIG-017` | `context.unit.EH-001.md` |
| `EH-002` | WE 02 | HAUS-12 | 1. OG | 49.0 | 1.5 | Wohnung | 114 | rented | `EIG-009` | `context.unit.EH-002.md` |
| `EH-003` | WE 03 | HAUS-12 | 1. OG | 62.0 | 2.0 | Wohnung | 144 | rented | `EIG-025` | `context.unit.EH-003.md` |
| `EH-004` | WE 04 | HAUS-12 | 2. OG | 60.0 | 2.0 | Wohnung | 139 | own-use | `EIG-034` | `context.unit.EH-004.md` |
| `EH-005` | WE 05 | HAUS-12 | 2. OG | 110.0 | 4.0 | Wohnung | 255 | own-use | `EIG-012` | `context.unit.EH-005.md` |
| `EH-006` | WE 06 | HAUS-12 | 2. OG | 51.0 | 1.5 | Wohnung | 118 | rented | `EIG-035` | `context.unit.EH-006.md` |
| `EH-007` | WE 07 | HAUS-12 | 3. OG | 45.0 | 1.5 | Wohnung | 104 | own-use | `EIG-005` | `context.unit.EH-007.md` |
| `EH-008` | WE 08 | HAUS-12 | 3. OG | 48.0 | 1.5 | Wohnung | 111 | own-use | `EIG-033` | `context.unit.EH-008.md` |
| `EH-009` | WE 09 | HAUS-12 | 3. OG | 67.0 | 2.0 | Wohnung | 156 | vacant | `EIG-014` | `context.unit.EH-009.md` |
| `EH-010` | WE 10 | HAUS-12 | 4. OG | 92.0 | 3.5 | Wohnung | 214 | rented | `EIG-016` | `context.unit.EH-010.md` |
| `EH-011` | WE 11 | HAUS-12 | 4. OG | 95.0 | 3.5 | Wohnung | 221 | own-use | `EIG-015` | `context.unit.EH-011.md` |
| `EH-012` | WE 12 | HAUS-12 | 4. OG | 110.0 | 4.0 | Wohnung | 255 | own-use | `EIG-008` | `context.unit.EH-012.md` |
| `EH-013` | WE 13 | HAUS-12 | 5. OG | 84.0 | 3.0 | Wohnung | 195 | rented | `EIG-024` | `context.unit.EH-013.md` |
| `EH-014` | WE 14 | HAUS-12 | 5. OG | 85.0 | 3.0 | Wohnung | 197 | own-use | `EIG-027` | `context.unit.EH-014.md` |
| `EH-015` | WE 15 | HAUS-12 | 5. OG | 115.0 | 4.5 | Wohnung | 267 | own-use | `EIG-004` | `context.unit.EH-015.md` |
| `EH-016` | WE 16 | HAUS-12 | 5. OG | 108.0 | 4.0 | Wohnung | 251 | rented | `EIG-013` | `context.unit.EH-016.md` |
| `EH-017` | WE 17 | HAUS-12 | 5. OG | 72.0 | 2.5 | Wohnung | 167 | own-use | `EIG-015` | `context.unit.EH-017.md` |
| `EH-018` | TG 18 | HAUS-12 | Tiefgarage | 12.5 | — | Tiefgarage | 23 | own-use | `EIG-018` | `context.unit.EH-018.md` |
| `EH-019` | WE 19 | HAUS-14 | 1. OG | 64.0 | 2.0 | Wohnung | 149 | rented | `EIG-014` | `context.unit.EH-019.md` |
| `EH-020` | WE 20 | HAUS-14 | 1. OG | 46.0 | 1.5 | Wohnung | 107 | own-use | `EIG-026` | `context.unit.EH-020.md` |
| `EH-021` | WE 21 | HAUS-14 | 1. OG | 82.0 | 3.0 | Wohnung | 190 | rented | `EIG-031` | `context.unit.EH-021.md` |
| `EH-022` | WE 22 | HAUS-14 | 2. OG | 75.0 | 2.5 | Wohnung | 174 | rented | `EIG-028` | `context.unit.EH-022.md` |
| `EH-023` | WE 23 | HAUS-14 | 2. OG | 96.0 | 3.5 | Wohnung | 223 | rented | `EIG-013` | `context.unit.EH-023.md` |
| `EH-024` | WE 24 | HAUS-14 | 2. OG | 115.0 | 4.5 | Wohnung | 267 | own-use | `EIG-005` | `context.unit.EH-024.md` |
| `EH-025` | WE 25 | HAUS-14 | 3. OG | 109.0 | 4.0 | Wohnung | 253 | rented | `EIG-003` | `context.unit.EH-025.md` |
| `EH-026` | WE 26 | HAUS-14 | 3. OG | 93.0 | 3.5 | Wohnung | 216 | own-use | `EIG-006` | `context.unit.EH-026.md` |
| `EH-027` | WE 27 | HAUS-14 | 3. OG | 82.0 | 3.0 | Wohnung | 190 | own-use | `EIG-006` | `context.unit.EH-027.md` |
| `EH-028` | WE 28 | HAUS-14 | 4. OG | 96.0 | 3.5 | Wohnung | 223 | own-use | `EIG-008` | `context.unit.EH-028.md` |
| `EH-029` | WE 29 | HAUS-14 | 4. OG | 120.0 | 4.5 | Wohnung | 279 | rented | `EIG-022` | `context.unit.EH-029.md` |
| `EH-030` | WE 30 | HAUS-14 | 4. OG | 95.0 | 3.5 | Wohnung | 221 | own-use | `EIG-017` | `context.unit.EH-030.md` |
| `EH-031` | WE 31 | HAUS-14 | 5. OG | 103.0 | 4.0 | Wohnung | 239 | rented | `EIG-011` | `context.unit.EH-031.md` |
| `EH-032` | WE 32 | HAUS-14 | 5. OG | 48.0 | 1.5 | Wohnung | 111 | rented | `EIG-001` | `context.unit.EH-032.md` |
| `EH-033` | WE 33 | HAUS-14 | 5. OG | 119.0 | 4.5 | Wohnung | 276 | own-use | `EIG-002` | `context.unit.EH-033.md` |
| `EH-034` | WE 34 | HAUS-14 | 5. OG | 118.0 | 4.5 | Wohnung | 274 | rented | `EIG-016` | `context.unit.EH-034.md` |
| `EH-035` | WE 35 | HAUS-14 | 5. OG | 85.0 | 3.0 | Wohnung | 197 | rented | `EIG-011` | `context.unit.EH-035.md` |
| `EH-036` | WE 36 | HAUS-14 | 5. OG | 107.0 | 4.0 | Wohnung | 248 | own-use | `EIG-012` | `context.unit.EH-036.md` |
| `EH-037` | GE 37 | HAUS-14 | EG Ladenlokal | 142.0 | — | Gewerbe | 348 | rented | `EIG-001` | `context.unit.EH-037.md` |
| `EH-038` | TG 38 | HAUS-14 | Tiefgarage | 12.5 | — | Tiefgarage | 23 | vacant | `EIG-009` | `context.unit.EH-038.md` |
| `EH-039` | WE 39 | HAUS-16 | 1. OG | 64.0 | 2.0 | Wohnung | 149 | rented | `EIG-021` | `context.unit.EH-039.md` |
| `EH-040` | WE 40 | HAUS-16 | 1. OG | 73.0 | 2.5 | Wohnung | 169 | own-use | `EIG-023` | `context.unit.EH-040.md` |
| `EH-041` | WE 41 | HAUS-16 | 1. OG | 106.0 | 4.0 | Wohnung | 246 | rented | `EIG-029` | `context.unit.EH-041.md` |
| `EH-042` | WE 42 | HAUS-16 | 2. OG | 103.0 | 4.0 | Wohnung | 239 | rented | `EIG-019` | `context.unit.EH-042.md` |
| `EH-043` | WE 43 | HAUS-16 | 2. OG | 94.0 | 3.5 | Wohnung | 218 | own-use | `EIG-004` | `context.unit.EH-043.md` |
| `EH-044` | WE 44 | HAUS-16 | 2. OG | 95.0 | 3.5 | Wohnung | 221 | own-use | `EIG-007` | `context.unit.EH-044.md` |
| `EH-045` | WE 45 | HAUS-16 | 3. OG | 66.0 | 2.0 | Wohnung | 153 | rented | `EIG-020` | `context.unit.EH-045.md` |
| `EH-046` | WE 46 | HAUS-16 | 3. OG | 85.0 | 3.0 | Wohnung | 197 | rented | `EIG-030` | `context.unit.EH-046.md` |
| `EH-047` | WE 47 | HAUS-16 | 3. OG | 110.0 | 4.0 | Wohnung | 255 | own-use | `EIG-002` | `context.unit.EH-047.md` |
| `EH-048` | WE 48 | HAUS-16 | 4. OG | 64.0 | 2.0 | Wohnung | 149 | own-use | `EIG-007` | `context.unit.EH-048.md` |
| `EH-049` | WE 49 | HAUS-16 | 4. OG | 115.0 | 4.5 | Wohnung | 267 | rented | `EIG-003` | `context.unit.EH-049.md` |
| `EH-050` | WE 50 | HAUS-16 | 4. OG | 59.0 | 2.0 | Wohnung | 137 | rented | `EIG-010` | `context.unit.EH-050.md` |
| `EH-051` | WE 51 | HAUS-16 | 4. OG | 85.0 | 3.0 | Wohnung | 197 | rented | `EIG-032` | `context.unit.EH-051.md` |
| `EH-052` | TG 52 | HAUS-16 | Tiefgarage | 12.5 | — | Tiefgarage | 23 | vacant | `EIG-010` | `context.unit.EH-052.md` |
<!-- /auto:units-index -->

---

## 3. Compliance Calendar (property-wide)
<!-- auto:compliance.summary -->_no issue_<!-- /auto:compliance.summary -->

<!-- auto:compliance -->
| obligation | last_done | next_due | vendor_ref | status | evidence_doc_ref |
| --- | --- | --- | --- | --- | --- |
_(no data in source yet)_
<!-- /auto:compliance -->

---

## 4. Vendor Operations (property-wide)

### 4.1 Open Vendor Quotes
<!-- auto:vendor-quotes.summary -->_no issue_<!-- /auto:vendor-quotes.summary -->

<!-- auto:vendor-quotes -->
| vendor_ref | scope | amount | valid_until | decision | doc_ref |
| --- | --- | --- | --- | --- | --- |
_(no data in source yet)_
<!-- /auto:vendor-quotes -->

### 4.2 Vendor Dunning AGAINST US (Mahnungen, die wir bekommen)
<!-- auto:vendor-dunning.summary -->_no issue_<!-- /auto:vendor-dunning.summary -->

<!-- auto:vendor-dunning -->
| vendor_ref | invoice_no | amount | stage | since | deadline | reason |
| --- | --- | --- | --- | --- | --- | --- |
_(no data in source yet)_
<!-- /auto:vendor-dunning -->

### 4.3 Recurring Property Processes (in-flight, property-wide)
<!-- auto:recurring-property.summary -->[Routine] Portoflio-weite Kündigungswelle: 27 Einheiten durch Mieter gekündigt zwischen 2024-04-19 (EH-049) und 2025-12-31 (EH-032), davon 18 Kündigungen seit Oktober 2025 [(email)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251025_115500_EMAIL-05964.eml). Jede Kündigung unterliegt § 573 I BGB (ordentliche Kündigung mit Frist) oder Mietvertrag-Sonderfristen; Kündigungsfrist beträgt regelmäßig drei Monate zum Ende eines Kalendermonats. Eskalation ab Oktober 2025 deutet auf systemische Situation hin (Marktlage, Immissionen, Management-Problem) — Ursachenanalyse und Exit-Management erforderlich.<!-- /auto:recurring-property.summary -->

<!-- auto:recurring-property -->
| process_type | started | current_step | owner | eta | blockers |
| --- | --- | --- | --- | --- | --- |
| Mieterwechsel EH-002 | 2025-08-20 | Kündigung erhalten | Verwaltung | TBD | — |
| Mieterwechsel EH-003 | 2025-10-19 | Kündigung erhalten | Verwaltung | TBD | — |
| Mieterwechsel EH-006 | 2025-05-05 | Kündigung erhalten | Verwaltung | TBD | — |
| Mieterwechsel EH-009 | 2025-08-27 | Kündigung erhalten | Verwaltung | TBD | — |
| Mieterwechsel EH-013 | 2025-09-13 | Kündigung erhalten | Verwaltung | TBD | — |
| Mieterwechsel EH-016 | 2025-10-28 | Kündigung erhalten | Verwaltung | TBD | — |
| Mieterwechsel EH-019 | 2025-10-25 | Kündigung erhalten | Verwaltung | TBD | — |
| Mieterwechsel EH-021 | 2025-10-04 | Kündigung erhalten | Verwaltung | TBD | — |
| Mieterwechsel EH-022 | 2025-07-30 | Kündigung erhalten | Verwaltung | TBD | — |
| Mieterwechsel EH-025 | 2025-11-03 | Kündigung erhalten | Verwaltung | TBD | — |
| Mieterwechsel EH-028 | 2024-07-16 | Kündigung erhalten | Verwaltung | TBD | — |
| Mieterwechsel EH-029 | 2025-06-03 | Kündigung erhalten | Verwaltung | TBD | — |
| Mieterwechsel EH-031 | 2025-11-26 | Kündigung erhalten | Verwaltung | TBD | — |
| Mieterwechsel EH-032 | 2025-12-31 | Kündigung erhalten | Verwaltung | TBD | — |
| Mieterwechsel EH-034 | 2025-08-02 | Kündigung erhalten | Verwaltung | TBD | — |
| Mieterwechsel EH-035 | 2025-12-21 | Kündigung erhalten | Verwaltung | TBD | — |
| Mieterwechsel EH-036 | 2025-07-21 | Kündigung erhalten | Verwaltung | TBD | — |
| Mieterwechsel EH-037 | 2025-12-22 | Kündigung erhalten | Verwaltung | TBD | — |
| Mieterwechsel EH-039 | 2025-09-13 | Kündigung erhalten | Verwaltung | TBD | — |
| Mieterwechsel EH-041 | 2025-12-12 | Kündigung erhalten | Verwaltung | TBD | — |
| Mieterwechsel EH-042 | 2024-11-11 | Kündigung erhalten | Verwaltung | TBD | — |
| Mieterwechsel EH-045 | 2025-09-08 | Kündigung erhalten | Verwaltung | TBD | — |
| Mieterwechsel EH-046 | 2025-07-29 | Kündigung erhalten | Verwaltung | TBD | — |
| Mieterwechsel EH-049 | 2024-04-19 | Kündigung erhalten | Verwaltung | TBD | — |
| Mieterwechsel EH-050 | 2025-05-11 | Kündigung erhalten | Verwaltung | TBD | — |
| Mieterwechsel EH-051 | 2024-07-27 | Kündigung erhalten | Verwaltung | TBD | — |
<!-- /auto:recurring-property -->

---

## 5. Financials (snapshot, last build)
<!-- auto:financials.summary -->_no issue_<!-- /auto:financials.summary -->

<!-- auto:financials -->
- last_nk_abrechnung: _(no data in source yet)_
- last_hausgeld_abrechnung: _(no data in source yet)_
- last_owner_payouts: _(no data in source yet)_
- ytd_aggregates: _(no data in source yet)_
- ruecklage_balance: _(no data in source yet)_
- live balances pointer: `db.account_balance WHERE property_id=LIE-001`
<!-- /auto:financials -->

### 5.1 Operations Summary (aggregated from all units)
> Materialized snapshot — built by Property Aggregator from all `context.unit.*.md` files.
> Deterministic counters; updated on Unit-Events or nightly batch. See `engine.aggregation-rules.md`.

<!-- auto:operations-summary -->
- units_status: { rented: `25`, vacant: `3`, own-use: `24`, total: `52` }
- active_dunning: { count: `25`, by_stage: { 1: `24`, 2: `1`, 3: `0` }, units: ['EH-002', 'EH-003', 'EH-006', 'EH-010', 'EH-013', 'EH-016', 'EH-019', 'EH-021', 'EH-022', 'EH-023', 'EH-025', 'EH-029', 'EH-031', 'EH-032', 'EH-034', 'EH-035', 'EH-037', 'EH-039', 'EH-041', 'EH-042', 'EH-045', 'EH-046', 'EH-049', 'EH-050', 'EH-051'] }
- active_reductions: { count: `23`, units: ['EH-002', 'EH-003', 'EH-006', 'EH-009', 'EH-013', 'EH-016', 'EH-019', 'EH-021', 'EH-022', 'EH-025', 'EH-029', 'EH-031', 'EH-032', 'EH-035', 'EH-037', 'EH-039', 'EH-041', 'EH-042', 'EH-045', 'EH-046', 'EH-049', 'EH-050', 'EH-051'] }
- pending_handovers_next_30d: `0`
- active_mieterwechsel_in_flight: { count: `26`, units: ['EH-002', 'EH-003', 'EH-006', 'EH-009', 'EH-013', 'EH-016', 'EH-019', 'EH-021', 'EH-022', 'EH-025', 'EH-028', 'EH-029', 'EH-031', 'EH-032', 'EH-034', 'EH-035', 'EH-036', 'EH-037', 'EH-039', 'EH-041', 'EH-042', 'EH-045', 'EH-046', 'EH-049', 'EH-050', 'EH-051'] }
- critical_tickets_total: `263`
- vendor_open_balance_against_us_total: `0.00 EUR`
- last_aggregated_at: `2026-04-26T09:54:28+00:00`
<!-- /auto:operations-summary -->

---

## 6. Stakeholders

### 6.1 Service-Vendors & Versicherungen
<!-- auto:stakeholders.summary -->_no issue_<!-- /auto:stakeholders.summary -->

<!-- auto:stakeholders -->
| role | name | contact | vertragstyp | next_service_due | last_invoice (date/amount) | open_balance_against_us | id |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Hausmeisterdienst | Hausmeister Mueller GmbH | slawomir.soelzer@hausmeister-mueller.de | monatlich €650.0 | — | 2025-12-28 INV-00189 | — | `DL-001` |
| Aufzugswartung | Aufzug Schindler & Co. GmbH | paul.heinz.koehler@aufzug-schindler-co.de | monatlich €185.0 | — | 2025-12-18 INV-00187 | — | `DL-002` |
| Heizungswartung | Heiztechnik Berlin GmbH | olga.holsten@heiztechnik-berlin.de | stundensatz €78.0 | — | 2025-12-19 INV-00188 | — | `DL-003` |
| Treppenhausreinigung | Reinigungsservice Kowalski | malte.becker@reinigungsservice-kowalski.de | monatlich €420.0 | — | 2025-12-28 INV-00190 | — | `DL-004` |
| Gartenpflege | Gaertnerei Gruener Daumen | ekkehart.wende@gaertnerei-gruener-daumen.de | monatlich €180.0 | — | 2025-12-28 INV-00191 | — | `DL-005` |
| Schornsteinfeger | Schornsteinfegermeister Bauer | jacek.weinhold@schornsteinfegermeister-bauer.de | stundensatz €48.0 | — | 2025-03-14 INV-00122 | — | `DL-006` |
| Gebaeudeversicherung | Allianz Versicherungs-AG | rolf.schoenland@allianz-versicherungs-ag.de | sporadisch | — | 2025-01-10 INV-00100 | — | `DL-007` |
| Strom Allgemein | Vattenfall Europe Sales GmbH | bernd.dieter.fiebig@vattenfall-europe-sales.de | sporadisch | — | 2025-02-14 INV-00108 | — | `DL-008` |
| Gas | GASAG Berliner Gaswerke AG | irmengard.mentzel@gasag-berliner-gaswerke-ag.de | sporadisch | — | 2025-03-08 INV-00119 | — | `DL-009` |
| Wasser/Abwasser | Berliner Wasserbetriebe | falk.trommler@berliner-wasserbetriebe.de | sporadisch | — | 2025-02-25 INV-00113 | — | `DL-010` |
| Muellentsorgung | BSR Berliner Stadtreinigung | mehdi.faust@bsr-berliner-stadtreinigung.de | sporadisch | — | 2025-02-22 INV-00112 | — | `DL-011` |
| Elektriker | Elektro Schmidt e.K. | carola.buchholz@elektro-schmidt-e-k.de | stundensatz €65.0 | — | 2025-12-15 INV-00186 | — | `DL-012` |
| Sanitaer/Heizung | Sanitaer Schulze GmbH | ernst.august.jessel@sanitaer-schulze.de | stundensatz €72.0 | — | 2025-11-13 INV-00179 | — | `DL-013` |
| Dachdecker | Dachdecker Richter | catherine.heydrich@dachdecker-richter.de | stundensatz €68.0 | — | 2025-11-09 INV-00178 | — | `DL-014` |
| Schliessanlage | SecureLock Systems Ltd. | thomas.kennedy@securelock-systems-ltd.com | stundensatz €85.0 | — | 2025-12-03 INV-00184 | — | `DL-015` |
| Fassadenreinigung | TechClean International | lisa.brown@techclean-international.com | stundensatz €55.0 | — | 2025-10-20 INV-00171 | — | `DL-016` |
<!-- /auto:stakeholders -->

### 6.2 Versorger (Strom, Gas, Wasser, Müll)
<!-- auto:utilities.summary -->_no issue_<!-- /auto:utilities.summary -->

<!-- auto:utilities -->
| type | provider | vertrag_no | meter_ref(s) | current_abschlag (€/Mon) | last_jahresabrechnung_period | next_jahresabrechnung_due | id |
| --- | --- | --- | --- | --- | --- | --- | --- |
_(no data in source yet)_
<!-- /auto:utilities -->

### 6.3 Behörden
<!-- auto:authorities.summary -->_no issue_<!-- /auto:authorities.summary -->

<!-- auto:authorities -->
| behörde | zuständigkeit | ansprechpartner | last_contact | open_request | compliance_doc_required |
| --- | --- | --- | --- | --- | --- |
_(no data in source yet)_
<!-- /auto:authorities -->

---

## 7. Policies (defaults & rules)
<!-- auto:policies.summary -->_no issue_<!-- /auto:policies.summary -->

<!-- auto:policies -->
- mahngebuehren: { stage_1: €5, stage_2: €10 }
- verzugszinssatz: basiszinssatz + 5pp (§ 288 I BGB)
- werktage_definition: Mo–Fr (Sa exkl. per BGH zu § 556b)
- nk_default_keys: `area_sqm | person_count | verbrauch | unit_share`
- heizkosten_method: HeizkostenV §7 (default 70/30 Verbrauch/Grundkosten)
- communication_preference_default: `email`
<!-- /auto:policies -->

---

## 8. Decisions & History (property-wide)

### 8.1 WEG-Beschlüsse — Decided
<!-- auto:weg-decisions.summary -->_no issue_<!-- /auto:weg-decisions.summary -->

<!-- auto:weg-decisions -->
| date | beschluss-no | topic | status | one-line summary | protocol_ref |
| --- | --- | --- | --- | --- | --- |
_(no data in source yet)_
<!-- /auto:weg-decisions -->

### 8.2 WEG-Agenda Backlog (proposed for next ETV)
<!-- auto:weg-agenda-backlog.summary -->_no issue_<!-- /auto:weg-agenda-backlog.summary -->

<!-- auto:weg-agenda-backlog -->
| proposed_at | proposed_by (owner_id) | topic | status | doc_ref |
| --- | --- | --- | --- | --- |
_(no data in source yet)_
<!-- /auto:weg-agenda-backlog -->

### 8.3 Einspruch-Log (per Beschluss)
<!-- auto:weg-einsprueche.summary -->_no issue_<!-- /auto:weg-einsprueche.summary -->

<!-- auto:weg-einsprueche -->
| beschluss-no | einspruch_by (owner_id) | date | reason (one-line) | status |
| --- | --- | --- | --- | --- |
_(no data in source yet)_
<!-- /auto:weg-einsprueche -->

### 8.4 Modernisierungs-Maßnahmen (property-wide)
<!-- auto:modernization.summary -->_no issue_<!-- /auto:modernization.summary -->

<!-- auto:modernization -->
| date_completed | scope | total_cost | umlage_per_year | affected_units | rent_increase | opt-outs |
| --- | --- | --- | --- | --- | --- | --- |
_(no data in source yet)_
<!-- /auto:modernization -->

### 8.5 Cross-Unit Patterns (auto-detected via aggregation)
> Patterns spanning multiple units, surfaced by the Property Aggregator. LLM-detected.
> Trigger: nightly batch + on-demand when N+1 same-type events accumulate (default: 3 in 90d).

<!-- auto:cross-unit-patterns.summary -->_no issue_<!-- /auto:cross-unit-patterns.summary -->

<!-- auto:cross-unit-patterns -->
| pattern_type | involved_units | incident_count | first_seen | last_seen | trigger_action_suggested | confidence |
| --- | --- | --- | --- | --- | --- | --- |
_(no data in source yet)_

_(LLM pattern detection — Hour 6+, see `engine.aggregation-rules.md` §8.5.)_
<!-- /auto:cross-unit-patterns -->

*`pattern_type`: `Konflikt | Wartung | Vendor-Quality | Owner-Behaviour | Insurance-Trigger`*
*`trigger_action_suggested`: e.g. `Versicherungsschaden eröffnen`, `Vendor wechseln`, `WEG-Beschluss vorbereiten`, `Beirat einbinden`*

---

## 9. Provenance & Source Index
<!-- auto:provenance.summary -->_no issue_<!-- /auto:provenance.summary -->

<!-- auto:provenance -->
| source-id | type | path | last_seen |
| --- | --- | --- | --- |
| `bank-bank` | bank | [bank](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/bank/kontoauszug_2024_2025.csv) | 2026-04-26 |
| `email-emails-2024-01` | email | [emails/2024-01/ (245 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-01/20240131_203200_EMAIL-00257.eml) | 2024-01-31T20:32:00+00:00 |
| `email-emails-2024-02` | email | [emails/2024-02/ (236 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-02/20240229_172400_EMAIL-00506.eml) | 2024-02-29T17:24:00+00:00 |
| `email-emails-2024-03` | email | [emails/2024-03/ (262 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-03/20240331_180900_EMAIL-00786.eml) | 2024-03-31T18:09:00+00:00 |
| `email-emails-2024-04` | email | [emails/2024-04/ (280 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-04/20240430_172700_EMAIL-01083.eml) | 2024-04-30T17:27:00+00:00 |
| `email-emails-2024-05` | email | [emails/2024-05/ (266 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-05/20240531_181100_EMAIL-01370.eml) | 2024-05-31T18:11:00+00:00 |
| `email-emails-2024-06` | email | [emails/2024-06/ (242 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-06/20240630_181000_EMAIL-01630.eml) | 2024-06-30T18:10:00+00:00 |
| `email-emails-2024-07` | email | [emails/2024-07/ (269 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-07/20240731_200300_EMAIL-01916.eml) | 2024-07-31T20:03:00+00:00 |
| `email-emails-2024-08` | email | [emails/2024-08/ (271 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-08/20240831_222600_EMAIL-02208.eml) | 2024-08-31T22:26:00+00:00 |
| `email-emails-2024-09` | email | [emails/2024-09/ (258 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-09/20240930_232900_EMAIL-02486.eml) | 2024-09-30T23:29:00+00:00 |
| `email-emails-2024-10` | email | [emails/2024-10/ (282 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-10/20241031_205200_EMAIL-02781.eml) | 2024-10-31T20:52:00+00:00 |
| `email-emails-2024-11` | email | [emails/2024-11/ (249 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-11/20241130_171500_EMAIL-03052.eml) | 2024-11-30T17:15:00+00:00 |
| `email-emails-2024-12` | email | [emails/2024-12/ (269 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2024-12/20241231_182100_EMAIL-03338.eml) | 2024-12-31T18:21:00+00:00 |
| `email-emails-2025-01` | email | [emails/2025-01/ (257 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-01/20250131_202500_EMAIL-03615.eml) | 2025-01-31T20:25:00+00:00 |
| `email-emails-2025-02` | email | [emails/2025-02/ (247 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-02/20250228_143200_EMAIL-03882.eml) | 2025-02-28T14:32:00+00:00 |
| `email-emails-2025-03` | email | [emails/2025-03/ (277 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-03/20250331_221400_EMAIL-04173.eml) | 2025-03-31T22:14:00+00:00 |
| `email-emails-2025-04` | email | [emails/2025-04/ (218 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-04/20250430_093300_EMAIL-04401.eml) | 2025-04-30T09:33:00+00:00 |
| `email-emails-2025-05` | email | [emails/2025-05/ (254 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-05/20250531_175300_EMAIL-04677.eml) | 2025-05-31T17:53:00+00:00 |
| `email-emails-2025-06` | email | [emails/2025-06/ (222 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-06/20250630_152400_EMAIL-04914.eml) | 2025-06-30T15:24:00+00:00 |
| `email-emails-2025-07` | email | [emails/2025-07/ (246 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-07/20250731_164200_EMAIL-05175.eml) | 2025-07-31T16:42:00+00:00 |
| `email-emails-2025-08` | email | [emails/2025-08/ (281 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-08/20250831_180400_EMAIL-05473.eml) | 2025-08-31T18:04:00+00:00 |
| `email-emails-2025-09` | email | [emails/2025-09/ (264 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-09/20250930_111000_EMAIL-05749.eml) | 2025-09-30T11:10:00+00:00 |
| `email-emails-2025-10` | email | [emails/2025-10/ (245 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-10/20251031_222500_EMAIL-06012.eml) | 2025-10-31T22:25:00+00:00 |
| `email-emails-2025-11` | email | [emails/2025-11/ (245 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-11/20251130_214300_EMAIL-06271.eml) | 2025-11-30T21:43:00+00:00 |
| `email-emails-2025-12` | email | [emails/2025-12/ (260 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2025-12/20251231_164200_EMAIL-06544.eml) | 2025-12-31T16:42:00+00:00 |
| `email-emails-2026-01` | email | [emails/2026-01/ (2 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/emails/2026-01/20260101_084400_EMAIL-06546.eml) | 2026-01-01T08:44:00+00:00 |
| `external-engine-aggregator` | external | [engine://aggregator](engine://aggregator/2026-04-26) | 2026-04-26 |
| `invoice-rechnungen-2024-01` | invoice | [rechnungen/2024-01/ (8 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/rechnungen/2024-01/20240128_DL-001_INV-00006.pdf) | 2024-01-28 |
| `invoice-rechnungen-2024-02` | invoice | [rechnungen/2024-02/ (9 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/rechnungen/2024-02/20240228_DL-001_INV-00015.pdf) | 2024-02-28 |
| `invoice-rechnungen-2024-03` | invoice | [rechnungen/2024-03/ (7 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/rechnungen/2024-03/20240328_DL-001_INV-00022.pdf) | 2024-03-28 |
| `invoice-rechnungen-2024-04` | invoice | [rechnungen/2024-04/ (7 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/rechnungen/2024-04/20240428_DL-001_INV-00029.pdf) | 2024-04-28 |
| `invoice-rechnungen-2024-05` | invoice | [rechnungen/2024-05/ (8 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/rechnungen/2024-05/20240528_DL-001_INV-00037.pdf) | 2024-05-28 |
| `invoice-rechnungen-2024-06` | invoice | [rechnungen/2024-06/ (7 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/rechnungen/2024-06/20240628_DL-001_INV-00044.pdf) | 2024-06-28 |
| `invoice-rechnungen-2024-07` | invoice | [rechnungen/2024-07/ (5 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/rechnungen/2024-07/20240728_DL-001_INV-00049.pdf) | 2024-07-28 |
| `invoice-rechnungen-2024-08` | invoice | [rechnungen/2024-08/ (10 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/rechnungen/2024-08/20240828_DL-013_INV-00061.pdf) | 2024-08-28 |
| `invoice-rechnungen-2024-09` | invoice | [rechnungen/2024-09/ (7 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/rechnungen/2024-09/20240928_DL-001_INV-00066.pdf) | 2024-09-28 |
| `invoice-rechnungen-2024-10` | invoice | [rechnungen/2024-10/ (7 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/rechnungen/2024-10/20241028_DL-001_INV-00073.pdf) | 2024-10-28 |
| `invoice-rechnungen-2024-11` | invoice | [rechnungen/2024-11/ (11 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/rechnungen/2024-11/20241128_DL-001_INV-00084.pdf) | 2024-11-28 |
| `invoice-rechnungen-2024-12` | invoice | [rechnungen/2024-12/ (10 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/rechnungen/2024-12/20241228_DL-013_INV-00096.pdf) | 2024-12-28 |
| `invoice-rechnungen-2025-01` | invoice | [rechnungen/2025-01/ (8 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/rechnungen/2025-01/20250128_DL-001_INV-00102.pdf) | 2025-01-28 |
| `invoice-rechnungen-2025-02` | invoice | [rechnungen/2025-02/ (13 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/rechnungen/2025-02/20250228_DL-001_INV-00115.pdf) | 2025-02-28 |
| `invoice-rechnungen-2025-03` | invoice | [rechnungen/2025-03/ (11 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/rechnungen/2025-03/20250328_DL-001_INV-00126.pdf) | 2025-03-28 |
| `invoice-rechnungen-2025-04` | invoice | [rechnungen/2025-04/ (4 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/rechnungen/2025-04/20250428_DL-001_INV-00130.pdf) | 2025-04-28 |
| `invoice-rechnungen-2025-05` | invoice | [rechnungen/2025-05/ (8 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/rechnungen/2025-05/20250528_DL-001_INV-00138.pdf) | 2025-05-28 |
| `invoice-rechnungen-2025-06` | invoice | [rechnungen/2025-06/ (6 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/rechnungen/2025-06/20250628_DL-001_INV-00144.pdf) | 2025-06-28 |
| `invoice-rechnungen-2025-07` | invoice | [rechnungen/2025-07/ (7 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/rechnungen/2025-07/20250728_DL-001_INV-00151.pdf) | 2025-07-28 |
| `invoice-rechnungen-2025-08` | invoice | [rechnungen/2025-08/ (9 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/rechnungen/2025-08/20250828_DL-001_INV-00160.pdf) | 2025-08-28 |
| `invoice-rechnungen-2025-09` | invoice | [rechnungen/2025-09/ (8 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/rechnungen/2025-09/20250928_DL-001_INV-00168.pdf) | 2025-09-28 |
| `invoice-rechnungen-2025-10` | invoice | [rechnungen/2025-10/ (5 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/rechnungen/2025-10/20251028_DL-001_INV-00172.pdf) | 2025-10-28 |
| `invoice-rechnungen-2025-11` | invoice | [rechnungen/2025-11/ (8 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/rechnungen/2025-11/20251128_DL-001_INV-00181.pdf) | 2025-11-28 |
| `invoice-rechnungen-2025-12` | invoice | [rechnungen/2025-12/ (8 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/rechnungen/2025-12/20251228_DL-001_INV-00189.pdf) | 2025-12-28 |
| `letter-briefe-2024-04` | letter | [briefe/2024-04/ (36 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/briefe/2024-04/20240420_etv_einladung_LTR-0036.pdf) | 2024-04-20 |
| `letter-briefe-2024-06` | letter | [briefe/2024-06/ (3 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/briefe/2024-06/20240627_mahnung_LTR-0039.pdf) | 2026-04-26 |
| `letter-briefe-2024-10` | letter | [briefe/2024-10](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/briefe/2024-10/20241018_mieterhoehung_LTR-0040.pdf) | 2024-10-18 |
| `letter-briefe-2024-11` | letter | [briefe/2024-11/ (4 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/briefe/2024-11/20241116_mahnung_LTR-0043.pdf) | 2026-04-26 |
| `letter-briefe-2024-12` | letter | [briefe/2024-12](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/briefe/2024-12/20241205_mieterhoehung_LTR-0045.pdf) | 2024-12-05 |
| `letter-briefe-2025-02` | letter | [briefe/2025-02](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/briefe/2025-02/20250218_mahnung_LTR-0046.pdf) | 2026-04-26 |
| `letter-briefe-2025-03` | letter | [briefe/2025-03/ (15 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/briefe/2025-03/20250325_hausgeld_LTR-0061.pdf) | 2025-03-25 |
| `letter-briefe-2025-04` | letter | [briefe/2025-04/ (54 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/briefe/2025-04/20250425_hausgeld_LTR-0114.pdf) | 2025-04-25 |
| `letter-briefe-2025-05` | letter | [briefe/2025-05/ (16 files)](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/briefe/2025-05/20250528_etv_protokoll_LTR-0131.pdf) | 2025-05-28 |
| `letter-briefe-2025-07` | letter | [briefe/2025-07](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/briefe/2025-07/20250717_mahnung_LTR-0132.pdf) | 2026-04-26 |
| `letter-briefe-2025-10` | letter | [briefe/2025-10](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/briefe/2025-10/20251019_mahnung_LTR-0133.pdf) | 2025-10-19 |
| `letter-briefe-2025-11` | letter | [briefe/2025-11](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/briefe/2025-11/20251105_kuendigung_LTR-0134.pdf) | 2025-11-05 |
| `letter-briefe-2025-12` | letter | [briefe/2025-12](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/briefe/2025-12/20251208_mahnung_LTR-0135.pdf) | 2026-04-26 |
| `stammdaten-stammdaten` | stammdaten | [stammdaten](https://github.com/zengzengzenghuy/property-context-resolver/blob/main/raw/stammdaten/stammdaten.json) | 2026-04-26T09:54:05+00:00 |
<!-- /auto:provenance -->

---

[^addr]: stammdaten/stammdaten.json → liegenschaft

*Schema: spine-v2-split (2026-04-25). Field-language English; German legal terms preserved (Kaltmiete, Mahnstufe, Werktage, Wohnungsgeberbestätigung, …). Companion: `context.unit.<unit_id>.md` per unit.*
