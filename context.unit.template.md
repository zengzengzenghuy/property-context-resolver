# context.unit.<!-- auto:unit_id -->[UNIT_ID]<!-- /auto:unit_id -->.md

> Per-unit dossier (one file per Einheit). Holds everything specific to this unit:
> the unit itself, the active lease, the tenant(s), and all unit/tenant-specific operations.
> **Property-wide data lives in `context.property.md`** — see `parent_property_ref` below.

<!-- auto:meta -->
- last_built_at: `<ISO-8601>`
- build_hash: `<git-sha>`
- engine_version: `<semver>`
- schema_version: `spine-v2-split` (2026-04-25)
- file_role: `unit`
- parent_property_ref: `context.property.md` *(or property_id)*
- owner_ref: `<EIG-XX>` *(from property.owners)*
<!-- /auto:meta -->

---

## 1. Unit
<!-- auto:unit.summary -->_no issue_<!-- /auto:unit.summary -->

<!-- auto:unit -->
- unit_id: `<EH-XX>`
- label: `<WE 19 | GE 37 | Stellplatz 3>`
- haus_id: `<HAUS-XX>` · floor: `<n>` · position: `<links|mitte|rechts>`
- typ: `Wohnung | Gewerbeeinheit (im residential context selten) | Stellplatz`
- area_sqm: `<n>` · rooms: `<n>` · mea_‰: `<n>`
- equipment: { kitchen, balcony, garage[], parking[], cellar }
- media_supply: { internet_provider, tv_contract, kollektivvertrag (bool), runs_until }
- key_inventory: [{ key_type, count, last_handover_date }]
- meters: [{ meter_id, type: `electric|gas|water|heat`, location, last_reading: { value, unit, date } }]
- occupancy_status: `rented | vacant | own-use`
- nk_keys: { area_sqm, person_count (Bewohnerzahl), unit_share }
<!-- /auto:unit -->

---

## 2. Lease (Mietverhältnis, voll)
<!-- auto:lease.summary -->_no issue_<!-- /auto:lease.summary -->

<!-- auto:lease -->
- lease_id, unit_ref *(this unit)*
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
- third_party_payers: [{ name, iban, relation }]
- payment_due_day (1–31, from lease; fallback § 556b BGB)
- verwendungszweck_convention: `<string>`
- kaution: { amount, form (`Bareinzahlung | Bürgschaft | Sparbuch`), account_iban, paid_status, refund_status }
- usage: `residential`
- vat_option: `false` *(residential default)*
- heating_cost_distribution: { method (HeizkostenV §7–9), share_consumption_%, share_area_% }
- wohnungsgeberbestaetigung: { issued: bool, date }
- lease_documents: [{ doc_id, type (Hauptvertrag|Nachtrag|Anlage), url }]
- subletting: { permitted (`true|false|case-by-case`), current_status (`none|requested|approved|denied`), conditions, decision_date }
- bauliche_veraenderung_requests: [{ date, scope (`tragend|nicht-tragend|optisch`), status (`offen|genehmigt|abgelehnt`), decision_ref }]
- special_agreements: [one-line strings]
<!-- /auto:lease -->

### 2.1 Tenants on this Lease
<!-- auto:tenants.summary -->_no issue_<!-- /auto:tenants.summary -->

<!-- auto:tenants -->
| tenant_id | name | role (haupt|mit) | contact_email | contact_phone | comms_pref | gesamtschuldner |
| --- | --- | --- | --- | --- | --- | --- |
<!-- /auto:tenants -->

---

## 3. Operations (this unit / this tenant)

### 3.1 Open Tickets — Critical (overdue or due ≤7 days)
<!-- auto:tickets.critical.summary -->_no issue_<!-- /auto:tickets.critical.summary -->

<!-- auto:tickets.critical -->
| ticket_id | type (Reparatur|Mieterwechsel|Modernisierung|Abrechnung) | title | deadline | status | assignee |
| --- | --- | --- | --- | --- | --- |
<!-- /auto:tickets.critical -->

### 3.2 Open Tickets — Aggregate
<!-- auto:tickets.aggregate.summary -->_no issue_<!-- /auto:tickets.aggregate.summary -->

<!-- auto:tickets.aggregate -->
- total_open: `<n>`
- by_type: { Reparatur: `<n>`, Mieterwechsel: `<n>`, Modernisierung: `<n>`, Abrechnung: `<n>`, other: `<n>` }
- live source: `db.tickets WHERE unit_id=<id> AND status='open'`
<!-- /auto:tickets.aggregate -->

### 3.3 Active Mahnverfahren

<!-- auto:dunning.summary -->_no issue_<!-- /auto:dunning.summary -->

#### Per claim
<!-- auto:dunning -->
| tenant_ref | claim_id | current_stage | amount_open | default_since | deadline_for_stage | last_letter |
| --- | --- | --- | --- | --- | --- | --- |
- live balance pointer: `db.tenant_balance.tenant_id=<id>`
<!-- /auto:dunning -->

### 3.4 Active Reductions / Deferrals (§ 536 BGB)
<!-- auto:reductions.summary -->_no issue_<!-- /auto:reductions.summary -->

<!-- auto:reductions -->
- date_raised, amount_or_percent, reason, status (`agreed|unilateral|disputed`)
- *trigger: HITL exit if any entry present*
<!-- /auto:reductions -->

### 3.5 Latest Übergabeprotokoll
<!-- auto:handover.summary -->_no issue_<!-- /auto:handover.summary -->

<!-- auto:handover -->
- next_scheduled: { date, type, contact, source_ref } *(if appointment requested but not yet executed)*
- last_completed:
   - date, type (`Einzug|Auszug|Zwischen`)
- meters_at_handover: [{ meter_id, value }]
- keys_handed_over: [{ type, count }]
- defects: [list]
- photos_ref: `<url-to-album>`
<!-- /auto:handover -->

### 3.6 Recurring Process State (this unit, in-flight)
<!-- auto:recurring.summary -->_no issue_<!-- /auto:recurring.summary -->

<!-- auto:recurring -->
| process_type (`Mieterwechsel|Modernisierung|NK-Streitfall`) | started | current_step | owner | eta | blockers |
| --- | --- | --- | --- | --- | --- |
<!-- /auto:recurring -->

### 3.7 Vermietungs-Pipeline *(if vacant)*
<!-- auto:vermietung.summary -->_no issue_<!-- /auto:vermietung.summary -->

<!-- auto:vermietung -->
- inserate_url, days_on_market, asking_kaltmiete
- prospects_count, scheduled_viewings_count, applications_received_count
- shortlist: [{ prospect_id, score, status (`new|invited|viewed|applied|rejected|approved`) }]
<!-- /auto:vermietung -->

---

## 4. Decisions & History (this unit / this tenant)

### 4.1 Tenant Special Agreements
<!-- auto:tenant-agreements.summary -->_no issue_<!-- /auto:tenant-agreements.summary -->

<!-- auto:tenant-agreements -->
| date | type (`Vergleich|Stundung|Sondergenehmigung|Mietminderung`) | one-line | doc_ref |
| --- | --- | --- | --- |
<!-- /auto:tenant-agreements -->

### 4.2 Modernisierungs-Maßnahmen (this unit)
<!-- auto:modernization-unit.summary -->_no issue_<!-- /auto:modernization-unit.summary -->

<!-- auto:modernization-unit -->
| date_completed | scope | umlage_per_year | rent_increase_per_month | tenant_opted_out |
| --- | --- | --- | --- | --- |
<!-- /auto:modernization-unit -->

### 4.3 Sticky Communication Threads (this tenant)
<!-- auto:sticky-threads.summary -->_no issue_<!-- /auto:sticky-threads.summary -->

<!-- auto:sticky-threads -->
| thread_id | subject | last_msg_date | parties | status | one-line outcome | pointer |
| --- | --- | --- | --- | --- | --- | --- |
<!-- /auto:sticky-threads -->

---

## 5. Provenance & Source Index (this unit/tenant)
<!-- auto:provenance.summary -->_no issue_<!-- /auto:provenance.summary -->

<!-- auto:provenance -->
| source-id | type (`stammdaten|bank|lease-pdf|email|brief|rechnung|external`) | path | last_seen |
| --- | --- | --- | --- |
<!-- /auto:provenance -->

---

*Schema: spine-v2-split (2026-04-25). See `context.property.md` for owner, mandate, vendors, utilities, authorities, policies, WEG-decisions, compliance calendar.*
