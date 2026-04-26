# context.property.md — <!-- auto:property.display_name -->[PROPERTY_DISPLAY_NAME]<!-- /auto:property.display_name -->

> Property-level dossier (one file per Liegenschaft). Holds everything that is property-wide:
> owners, mandate, WEG decisions, vendors, utilities, authorities, compliance, financials, policies.
> **Per-unit data lives in `context.unit.<unit_id>.md` files** — see §2 Units Index for refs.
> Volatile data (live balances) is NOT stored here — pointers indicate live source.
> Manual edits outside `<!-- auto:* -->` blocks are preserved by the engine.

<!-- auto:meta -->
- last_built_at: `<ISO-8601>`
- build_hash: `<git-sha>`
- engine_version: `<semver>`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `property`
<!-- /auto:meta -->

---

## 1. Property
<!-- auto:property.summary -->_no issue_<!-- /auto:property.summary -->

<!-- auto:property -->
- property_id: `<UUID>` *(e.g. LIE-001)*
- address: `<street, postal_code, city>` [^addr]
- property_type: `residential`
- legal_form: `WEG | Sondereigentum | Alleineigentum`
- year_built: `<YYYY>` · year_renovated: `<YYYY>`
- total_area_sqm: `<n>` · total_units: `<n>` · houses: `[HAUS-XX, HAUS-YY, ...]`
- common_areas: `[Treppenhaus, Keller, Garten, ...]`
- tax: { steuernummer, vat_status: `not-applicable | opted-in`, datev_mandant }
- bank_accounts:
   - hausgeld: { iban, holder, bank }
   - ruecklage: { iban, holder, bank }
- documents: { grundbuch_ref, energieausweis: { type, valid_until }, hausordnung_ref, brandschutznachweis_ref, building_insurance: see §7.1 }
<!-- /auto:property -->

### 1.1 Owner(s)
<!-- auto:owners.summary -->_no issue_<!-- /auto:owners.summary -->

<!-- auto:owners -->
| owner_id | name | share_‰ (MEA) | unit_refs | contact | reporting_pref | sale_intent | beirat |
| --- | --- | --- | --- | --- | --- | --- | --- |
<!-- /auto:owners -->
*`sale_intent`: `none | considering | listed | under_contract`; if ≠ none → `{ since, requested_docs[] }` in footnote.*

### 1.2 Verwaltermandat
<!-- auto:mandate.summary -->_no issue_<!-- /auto:mandate.summary -->

<!-- auto:mandate -->
- manager: `<company>` · contact, iban, steuernummer
- start, term, notice_period, fee_basis, scope (`WEG | Sondereigentum | both`)
<!-- /auto:mandate -->

---

## 2. Units Index
> Roster only. Detail lives in per-unit files.

<!-- auto:units-index.summary -->_no issue_<!-- /auto:units-index.summary -->

<!-- auto:units-index -->
| unit_id | label | haus_id | floor | sqm | rooms | typ (`Wohnung|GE|Stellplatz`) | mea_‰ | occupancy (`rented|vacant|own-use`) | owner_ref | unit_md_ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
<!-- /auto:units-index -->

---

## 3. Compliance Calendar (property-wide)
<!-- auto:compliance.summary -->_no issue_<!-- /auto:compliance.summary -->

<!-- auto:compliance -->
| obligation | last_done | next_due | vendor_ref | status | evidence_doc_ref |
| --- | --- | --- | --- | --- | --- |
| Schornsteinfeger | | | | | |
| Heizungswartung | | | | | |
| Trinkwasseranalyse | | | | | |
| Aufzug-TÜV | | | | | |
| Rauchmelder-Prüfung | | | | | |
| Energieausweis-Erneuerung | | | n/a | | |
| Brandschutznachweis | | | n/a | | |
<!-- /auto:compliance -->

---

## 4. Vendor Operations (property-wide)

### 4.1 Open Vendor Quotes
<!-- auto:vendor-quotes.summary -->_no issue_<!-- /auto:vendor-quotes.summary -->

<!-- auto:vendor-quotes -->
| vendor_ref | scope | amount | valid_until | decision (`pending|accepted|rejected`) | doc_ref |
| --- | --- | --- | --- | --- | --- |
<!-- /auto:vendor-quotes -->

### 4.2 Vendor Dunning AGAINST US (Mahnungen, die wir bekommen)
<!-- auto:vendor-dunning.summary -->_no issue_<!-- /auto:vendor-dunning.summary -->

<!-- auto:vendor-dunning -->
| vendor_ref | invoice_no | amount | stage (`1|2|gerichtlich`) | since | deadline | reason |
| --- | --- | --- | --- | --- | --- | --- |
<!-- /auto:vendor-dunning -->

### 4.3 Recurring Property Processes (in-flight, property-wide)
<!-- auto:recurring-property.summary -->_no issue_<!-- /auto:recurring-property.summary -->

<!-- auto:recurring-property -->
| process_type (`Modernisierung|NK-Lauf|Hausgeld-Lauf|ETV-Vorbereitung`) | started | current_step | owner | eta | blockers |
| --- | --- | --- | --- | --- | --- |
<!-- /auto:recurring-property -->

---

## 5. Financials (snapshot, last build)
<!-- auto:financials.summary -->_no issue_<!-- /auto:financials.summary -->

<!-- auto:financials -->
- last_nk_abrechnung: { period, total_costs, total_advances, balance_per_unit_ref, sent_date, disputes_open }
- last_hausgeld_abrechnung *(WEG only)*: { period, total, owner_balances, sent_date }
- last_owner_payouts: [{ owner_ref, date, amount, period }]
- ytd_aggregates *(for Anlage V / EÜR)*: rental_income_ytd, werbungskosten_ytd, umlagefaehige_kosten_ytd, last_anlage_v_export
- ruecklage_balance: `<€>` *(snapshot)*
- live balances pointer: `db.account_balance WHERE property_id=<id>`
<!-- /auto:financials -->

### 5.1 Operations Summary (aggregated from all units)
> Materialized snapshot — built by Property Aggregator from all `context.unit.*.md` files.
> Deterministic counters; updated on Unit-Events or nightly batch. See `engine.aggregation-rules.md`.

<!-- auto:operations-summary -->
- units_status: { rented: `<n>`, vacant: `<n>`, own-use: `<n>`, total: `<n>` }
- active_dunning: { count: `<n>`, by_stage: { 1: `<n>`, 2: `<n>`, 3: `<n>` }, units: [`<EH-XX>`, ...] }
- active_reductions: { count: `<n>`, units: [`<EH-XX>`, ...] }
- pending_handovers_next_30d: { count: `<n>`, items: [{ unit, date, type }] }
- active_mieterwechsel_in_flight: { count: `<n>`, units: [`<EH-XX>`, ...] }
- critical_tickets_total: `<n>`
- vacancies_with_listings: { count: `<n>`, avg_days_on_market: `<n>` }
- vendor_open_balance_against_us_total: `<€>`
- last_aggregated_at: `<ISO-8601>`
<!-- /auto:operations-summary -->

---

## 6. Stakeholders

### 6.1 Service-Vendors & Versicherungen
<!-- auto:stakeholders.summary -->_no issue_<!-- /auto:stakeholders.summary -->

<!-- auto:stakeholders -->
| role | name | contact | vertragstyp (`monatlich|stundensatz|sporadisch`) | next_service_due | last_invoice (date/amount) | open_balance_against_us | iban_change_log_ref |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Heizungs-Service | | | | | | | |
| Schornsteinfeger | | | sporadisch | | | | |
| Aufzugswartung | | | monatlich | | | | |
| Sanitär/Heizung | | | stundensatz | | | | |
| Elektriker | | | stundensatz | | | | |
| Dachdecker | | | sporadisch | | | | |
| Schließanlage/Schlosser | | | stundensatz | | | | |
| Hausmeisterdienst | | | monatlich | | | | |
| Treppenhausreinigung | | | monatlich | | | | |
| Fassadenreinigung | | | sporadisch | | | | |
| Gartenpflege | | | monatlich | | | | |
| Notdienst (24/7) | | | sporadisch | | | | |
| Versicherung Wohngebäude | | policy_no | n/a | | | n/a | n/a |
| Versicherung Haftpflicht | | policy_no | n/a | | | n/a | n/a |
| Steuerberater | | | sporadisch | | | n/a | (DATEV-Anschluss) |
| Heizkostenabrechner | | | sporadisch | | | | (Techem\|Brunata\|...) |
| Mieterportal-Anbieter | | | monatlich | | | | |
<!-- /auto:stakeholders -->

### 6.2 Versorger (Strom, Gas, Wasser, Müll)
<!-- auto:utilities.summary -->_no issue_<!-- /auto:utilities.summary -->

<!-- auto:utilities -->
| type (`Strom|Gas|Wasser|Abwasser|Müll`) | provider | vertrag_no | meter_ref(s) | current_abschlag (€/Mon) | last_jahresabrechnung_period | next_jahresabrechnung_due | price_history_ref |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Strom Allgemein | | | | | | | |
| Gas | | | | | | | |
| Wasser/Abwasser | | | | | | | |
| Müllentsorgung | | | n/a | n/a | | | |
<!-- /auto:utilities -->

### 6.3 Behörden
<!-- auto:authorities.summary -->_no issue_<!-- /auto:authorities.summary -->

<!-- auto:authorities -->
| behörde | zuständigkeit | ansprechpartner | last_contact | open_request | compliance_doc_required |
| --- | --- | --- | --- | --- | --- |
| Bauamt (Bezirk) | Bauanträge, Brandschutz | | | | |
| Schornsteinfeger-Bezirk | Feuerstättenbescheid | | | | |
| Gesundheitsamt | Trinkwasser | | | | |
<!-- /auto:authorities -->

---

## 7. Policies (defaults & rules)
<!-- auto:policies.summary -->_no issue_<!-- /auto:policies.summary -->

<!-- auto:policies -->
- mahngebuehren: { stage_1: €5, stage_2: €10 }
- verzugszinssatz: { basiszinssatz: `<pct>` (Bundesbank, refreshed `<date>`), plus 5pp (§ 288 I BGB) }
- werktage_definition: Mo–Fr (Sa exkl. per BGH zu § 556b)
- nk_default_keys: `area_sqm | person_count | verbrauch | unit_share`
- heizkosten_method: HeizkostenV §7 (default 70/30 Verbrauch/Grundkosten)
- letter_templates: `<pointer>`
- sepa_lastschrift_default_offset_days: `<n>`
- communication_preference_default: `email | epost | mieterportal`
<!-- /auto:policies -->

---

## 8. Decisions & History (property-wide)

### 8.1 WEG-Beschlüsse — Decided
<!-- auto:weg-decisions.summary -->_no issue_<!-- /auto:weg-decisions.summary -->

<!-- auto:weg-decisions -->
| date | beschluss-no | topic | status (`umgesetzt|offen|angefochten`) | one-line summary | protocol_ref |
| --- | --- | --- | --- | --- | --- |
<!-- /auto:weg-decisions -->

### 8.2 WEG-Agenda Backlog (proposed for next ETV)
<!-- auto:weg-agenda-backlog.summary -->_no issue_<!-- /auto:weg-agenda-backlog.summary -->

<!-- auto:weg-agenda-backlog -->
| proposed_at | proposed_by (owner_id) | topic | status (`pending|on_next_agenda|withdrawn|decided`) | doc_ref |
| --- | --- | --- | --- | --- |
<!-- /auto:weg-agenda-backlog -->

### 8.3 Einspruch-Log (per Beschluss)
<!-- auto:weg-einsprueche.summary -->_no issue_<!-- /auto:weg-einsprueche.summary -->

<!-- auto:weg-einsprueche -->
| beschluss-no | einspruch_by (owner_id) | date | reason (one-line) | status (`offen|zurückgezogen|gerichtlich`) |
| --- | --- | --- | --- | --- |
<!-- /auto:weg-einsprueche -->

### 8.4 Modernisierungs-Maßnahmen (property-wide)
<!-- auto:modernization.summary -->_no issue_<!-- /auto:modernization.summary -->

<!-- auto:modernization -->
| date_completed | scope | total_cost | umlage_per_year | affected_units | rent_increase | opt-outs |
| --- | --- | --- | --- | --- | --- | --- |
<!-- /auto:modernization -->

### 8.5 Cross-Unit Patterns (auto-detected via aggregation)
> Patterns spanning multiple units, surfaced by the Property Aggregator. LLM-detected.
> Trigger: nightly batch + on-demand when N+1 same-type events accumulate (default: 3 in 90d).

<!-- auto:cross-unit-patterns.summary -->_no issue_<!-- /auto:cross-unit-patterns.summary -->

<!-- auto:cross-unit-patterns -->
| pattern_type | involved_units | incident_count | first_seen | last_seen | trigger_action_suggested | confidence |
| --- | --- | --- | --- | --- | --- | --- |
<!-- /auto:cross-unit-patterns -->

*`pattern_type`: `Konflikt | Wartung | Vendor-Quality | Owner-Behaviour | Insurance-Trigger`*
*`trigger_action_suggested`: e.g. `Versicherungsschaden eröffnen`, `Vendor wechseln`, `WEG-Beschluss vorbereiten`, `Beirat einbinden`*

---

## 9. Provenance & Source Index
<!-- auto:provenance.summary -->_no issue_<!-- /auto:provenance.summary -->

<!-- auto:provenance -->
| source-id | type (`stammdaten|bank|brief|email|rechnung|weg-protocol|external`) | path | last_seen |
| --- | --- | --- | --- |
<!-- /auto:provenance -->

---

[^addr]: stammdaten/stammdaten.json → liegenschaft

*Schema: spine-v2-split (2026-04-25). Field-language English; German legal terms preserved (Kaltmiete, Mahnstufe, Werktage, Wohnungsgeberbestätigung, …). Companion: `context.unit.<unit_id>.md` per unit.*
