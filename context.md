# context.md — <!-- auto:property.display_name -->[PROPERTY_DISPLAY_NAME]<!-- /auto:property.display_name -->

> Self-updating property dossier. Snapshot from authoritative sources at last build.
> Volatile data (live balances, real-time tx) is NOT stored here — pointers indicate live source.
> Manual edits outside `<!-- auto:* -->` blocks are preserved by the engine.

<!-- auto:meta -->
- last_built_at: `<ISO-8601>`
- build_hash: `<git-sha>`
- engine_version: `<semver>`
- schema_version: `spine-v1` (2026-04-25)
<!-- /auto:meta -->

---

## 1. Property
<!-- auto:property -->
- property_id: `<UUID>`
- address: `<street, postal_code, city>` [^addr]
- property_type: `residential`
- legal_form: `WEG | Sondereigentum | Alleineigentum`
- year_built: `<YYYY>`
- total_area_sqm: `<n>`
- total_units: `<n>`
- common_areas: `[Treppenhaus, Keller, Garten, ...]`
- tax: { steuernummer: `<...>`, vat_status: `not-applicable | opted-in`, datev_mandant: `<n>` }
- bank_account_property: { iban: `<DE...>`, holder: `<...>`, purpose: `rent inflow | hausgeld` }
- documents: { grundbuch_ref, energieausweis: { type, valid_until }, hausordnung_ref, building_insurance: see §6 }
<!-- /auto:property -->

### 1.1 Owner(s)
<!-- auto:owners -->
| owner_id | name | share_% | contact | reporting_pref | sale_intent |
| --- | --- | --- | --- | --- | --- |
<!-- /auto:owners -->
*`sale_intent`: `none | considering | listed | under_contract`; if ≠ none → `{ since, requested_docs[] }` in footnote.*

### 1.2 Verwaltermandat
<!-- auto:mandate -->
- manager: `<company>`
- start, term, notice_period, fee_basis, scope (`WEG | Sondereigentum | both`)
<!-- /auto:mandate -->

---

## 2. Units
<!-- auto:units -->
Per unit:
- unit_id, label, floor, position, area_sqm, rooms
- equipment: { kitchen, balcony, garage[], parking[], cellar }
- media_supply: { internet_provider, tv_contract, kollektivvertrag (bool), runs_until }
- key_inventory: [{ key_type, count, last_handover_date }]
- meters: [{ meter_id, type: `electric|gas|water|heat`, location, last_reading: { value, unit, date } }]
- occupancy_status: `rented | vacant | own-use`
- nk_keys: { area_sqm, person_count (Bewohnerzahl), unit_share }
<!-- /auto:units -->

---

## 3. Leases (Mietverhältnisse, voll)
Per active lease (one block per unit_id):

<!-- auto:lease.<unit_id> -->
- lease_id, unit_ref
- start_date, term_type (`befristet | unbefristet`), end_date (if befristet)
- cancellation_status: `none | by_tenant | by_landlord | mutual`
   - if cancelled: notice_date, move_out_date, remaining_rents
- household_size (Bewohnerzahl, treibt NK-Schlüssel)
- rent_components:
   - kaltmiete: `<€>`
   - betriebskosten_vorauszahlung: `<€>`
   - heizkosten_vorauszahlung: `<€>`
   - extras: [{ label (Garage|Stellplatz|...), amount }]
   - total_warmmiete: `<€>` (computed)
- rent_adjustment_mechanic:
   - type: `none | staffel | index`
   - if staffel: stages [{ from_date, kaltmiete }]
   - if index: index_basis (VPI), last_adjustment, next_eligible_adjustment
- payment_mode: `SEPA-Lastschrift | Überweisung`
- sepa_mandate: { mandate_id, signed_date, valid }
- iban_payer (if Überweisung): `<DE...>`
- third_party_payers: [{ name, iban, relation }]  *(e.g. parent of student tenant)*
- payment_due_day (1–31, from lease; fallback § 556b BGB)
- verwendungszweck_convention: `<string>`
- kaution: { amount, form (`Bareinzahlung | Bürgschaft | Sparbuch`), account_iban, paid_status, refund_status }
- usage: `residential`
- vat_option: `false` *(residential default)*
- heating_cost_distribution: { method (HeizkostenV §7–9), share_consumption_%, share_area_% }
- wohnungsgeberbestaetigung: { issued: bool, date }
- lease_documents: [{ doc_id, type (Hauptvertrag|Nachtrag|Anlage), url }]
- subletting: { permitted (`true | false | case-by-case`), current_status (`none | requested | approved | denied`), conditions, decision_date }
- bauliche_veraenderung_requests: [{ date, scope (`tragend | nicht-tragend | optisch`), status (`offen | genehmigt | abgelehnt`), decision_ref }]
- special_agreements: [one-line strings]
<!-- /auto:lease.<unit_id> -->

### 3.1 Tenants per Lease
<!-- auto:tenants.<lease_id> -->
| tenant_id | name | role (haupt|mit) | contact_email | contact_phone | comms_pref | gesamtschuldner |
| --- | --- | --- | --- | --- | --- | --- |
<!-- /auto:tenants.<lease_id> -->

---

## 4. Operations

### 4.1 Tickets — Critical (overdue or due ≤7 days)
<!-- auto:tickets.critical -->
| ticket_id | type (Reparatur|Mieterwechsel|Modernisierung|Abrechnung) | title | unit/lease | deadline | status | assignee |
| --- | --- | --- | --- | --- | --- | --- |
<!-- /auto:tickets.critical -->

### 4.2 Tickets — Aggregate (all other open)
<!-- auto:tickets.aggregate -->
- total_open: `<n>`
- by_type: { Reparatur: `<n>`, Mieterwechsel: `<n>`, Modernisierung: `<n>`, Abrechnung: `<n>`, other: `<n>` }
- live source: `db.tickets WHERE property_id=<id> AND status='open'`
<!-- /auto:tickets.aggregate -->

### 4.3 Active Mahnverfahren (per claim)
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
- live balance pointer: `db.tenant_balance.tenant_id=<id>`
<!-- /auto:dunning -->

### 4.4 Active Reductions / Deferrals (§ 536 BGB)
<!-- auto:reductions -->
- per tenant: date_raised, amount_or_percent, reason, status (`agreed|unilateral|disputed`)
- *trigger: HITL exit if any entry present*
<!-- /auto:reductions -->

### 4.5 Compliance Calendar (next maintenance dates)
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

### 4.6 Latest Übergabeprotokoll (per unit)
<!-- auto:handover.<unit_id> -->
- next_scheduled: { date, type, contact, source_ref } *(if appointment requested but not yet executed)*
- last_completed:
   - date, type (`Einzug|Auszug|Zwischen`)
- meters_at_handover: [{ meter_id, value }]
- keys_handed_over: [{ type, count }]
- defects: [list]
- photos_ref: `<url-to-album>`
<!-- /auto:handover.<unit_id> -->

### 4.7 Recurring Process State (in-flight)
<!-- auto:recurring -->
| process_type (Mieterwechsel|Modernisierung|NK-Abrechnung) | started | current_step | owner | eta | blockers |
| --- | --- | --- | --- | --- | --- |
<!-- /auto:recurring -->

### 4.8 Open Vendor Quotes (Angebote ausstehend)
<!-- auto:vendor-quotes -->
| vendor_ref | scope | amount | valid_until | decision (`pending|accepted|rejected`) | doc_ref |
| --- | --- | --- | --- | --- | --- |
<!-- /auto:vendor-quotes -->

### 4.9 Vendor Dunning AGAINST US (Mahnungen, die wir bekommen)
<!-- auto:vendor-dunning -->
| vendor_ref | invoice_no | amount | stage (`1|2|gerichtlich`) | since | deadline | reason |
| --- | --- | --- | --- | --- | --- | --- |
<!-- /auto:vendor-dunning -->

### 4.10 Vermietungs-Pipeline (per vacant unit)
<!-- auto:vermietung.<unit_id> -->
- inserate_url, days_on_market, asking_kaltmiete
- prospects_count, scheduled_viewings_count, applications_received_count
- shortlist: [{ prospect_id, score, status (`new|invited|viewed|applied|rejected|approved`) }]
<!-- /auto:vermietung.<unit_id> -->

---

## 5. Financials (snapshot, last build)
<!-- auto:financials -->
- last_nk_abrechnung: { period, total_costs, total_advances, balance_per_unit, sent_date, disputes_open }
- last_hausgeld_abrechnung *(WEG only)*: { period, total, owner_balances, sent_date }
- last_owner_payout: { date, amount, period }
- ytd_aggregates *(for Anlage V / EÜR)*:
   - rental_income_ytd: `<€>`
   - werbungskosten_ytd: `<€>`
   - umlagefaehige_kosten_ytd: `<€>`
   - last_anlage_v_export: `<url>` | `<date>`
- live balances pointer: `db.account_balance WHERE property_id=<id>`
<!-- /auto:financials -->

---

## 6. Stakeholders (Address Book)

### 6.1 Service-Vendors & Versicherungen
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
<!-- auto:utilities -->
| type (`Strom|Gas|Wasser|Abwasser|Müll`) | provider | vertrag_no | meter_ref(s) | current_abschlag (€/Mon) | last_jahresabrechnung_period | next_jahresabrechnung_due | price_history_ref |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Strom Allgemein | | | | | | | |
| Gas | | | | | | | |
| Wasser/Abwasser | | | | | | | |
| Müllentsorgung | | | n/a | n/a | | | |
<!-- /auto:utilities -->

### 6.3 Behörden (öffentliche Institutionen)
<!-- auto:authorities -->
| behörde | zuständigkeit | ansprechpartner | last_contact | open_request | compliance_doc_required |
| --- | --- | --- | --- | --- | --- |
| Bauamt (Bezirk) | Bauanträge, Brandschutz | | | | |
| Schornsteinfeger-Bezirk | Feuerstättenbescheid | | | | |
| Gesundheitsamt | Trinkwasser | | | | |
<!-- /auto:authorities -->

---

## 7. Policies (defaults & rules)
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

## 8. Decisions & History (sticky)

### 8.1 WEG-Beschlüsse *(if WEG)*
**Decided:**
<!-- auto:weg-decisions -->
| date | beschluss-no | topic | status (`umgesetzt|offen|angefochten`) | one-line summary | protocol_ref |
| --- | --- | --- | --- | --- | --- |
<!-- /auto:weg-decisions -->

**Agenda Backlog (proposed for next ETV):**
<!-- auto:weg-agenda-backlog -->
| proposed_at | proposed_by (owner_id) | topic | status (`pending|on_next_agenda|withdrawn|decided`) | doc_ref |
| --- | --- | --- | --- | --- |
<!-- /auto:weg-agenda-backlog -->

**Einspruch-Log (per Beschluss):**
<!-- auto:weg-einsprueche -->
| beschluss-no | einspruch_by (owner_id) | date | reason (one-line) | status (`offen|zurückgezogen|gerichtlich`) |
| --- | --- | --- | --- | --- |
<!-- /auto:weg-einsprueche -->

### 8.2 Tenant Special Agreements
<!-- auto:tenant-agreements -->
| tenant_ref | date | type (`Vergleich|Stundung|Sondergenehmigung|Mietminderung`) | one-line | doc_ref |
| --- | --- | --- | --- | --- |
<!-- /auto:tenant-agreements -->

### 8.3 Modernisierungs-Maßnahmen
<!-- auto:modernization -->
| date_completed | scope | total_cost | umlage_per_year | affected_units | rent_increase | opt-outs |
| --- | --- | --- | --- | --- | --- | --- |
<!-- /auto:modernization -->

### 8.4 Sticky communication threads
<!-- auto:sticky-threads -->
| thread_id | subject | last_msg_date | parties | status | one-line outcome | pointer |
| --- | --- | --- | --- | --- | --- | --- |
<!-- /auto:sticky-threads -->

### 8.5 Konflikt-Patterns (recurring)
<!-- auto:konflikt-patterns -->
| units_pair (or unit→house) | type (`Lärm|Treppenhaus|Müll|Parken|Sonstiges`) | incident_count | first_seen | last_incident | current_status | last_action |
| --- | --- | --- | --- | --- | --- | --- |
<!-- /auto:konflikt-patterns -->

---

## 9. Provenance & Source Index
Each fact above carries an inline footnote `[^source-id]`. Index:
<!-- auto:provenance -->
| source-id | type (`stammdaten|bank|lease-pdf|email|brief|rechnung|weg-protocol|external`) | path | last_seen |
| --- | --- | --- | --- |
<!-- /auto:provenance -->

---

[^addr]: stammdaten/objekt.csv

*Schema: spine-v1 (2026-04-25). Field-language English; German legal terms preserved (Kaltmiete, Mahnstufe, Werktage, Wohnungsgeberbestätigung, …).*
