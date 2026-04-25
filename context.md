# <!--

# context.md — single source of truth for one property

## CONVENTIONS

1. Anything inside `<!-- auto:NAME -->` ... `<!-- /auto:NAME -->` is engine-managed.
   The Merger only writes inside these blocks. Field-level diffs only — never full rewrites.

2. Anything OUTSIDE auto-blocks is HUMAN-OWNED. The engine never touches it.

3. Conflict marker convention: when two sources disagree on a fact, the engine inserts
   `<!-- conflict: source_a=X | source_b=Y -->` next to the value and emits a review event.
   Conflicts pause auto-updates of that field until a human resolves them.

4. Provenance: every machine-written fact carries a footnote like `[^src-123]`
   linking to the source artefact that produced it.

5. Placeholder syntax: `<...>` marks a field to fill. Grep for `<` to find unfilled spots.

6. Repeating blocks: where you see `<!-- repeat per tenant -->`, duplicate the block
   for every tenant with the appropriate IDs substituted.
   ================================================================
   -->

# Property Context — <PROPERTY_NAME>

<!-- auto:meta -->

- **Address:** <STREET, ZIP CITY>
- **Property Manager:** <NAME>
- **Owner(s):** <NAME(S)>
- **Property ID (canonical, from stammdaten):** <PROPERTY_ID>
- **Last Engine Run:** <ISO_DATETIME>
- **Engine Version:** <VERSION>
<!-- /auto:meta -->

## Property Policies

<!-- auto:policies -->

- **Mahngebühren:**
  - Stage 1: € <N>
  - Stage 2: € <N>
- **Default-Interest Base Rate (Basiszinssatz):** <X.XX> % p.a. (effective <DATE>)
- **Default-Interest Formula:** § 288 Abs. 1 BGB — `open × (basiszinssatz + 0.05) × default_days / 365`
- **Werktage Definition:** Mon–Fri (Saturday excluded per BGH on § 556b BGB)
- **Buffer:** Bank reconciliation runs T+1 WT after rent due date
- **Stage-0 Eligibility:** Überweisung mode, first 2 rent payments of the lease only
- **Letter Templates:** see `/properties/<PROPERTY_ID>/templates/`
<!-- /auto:policies -->

## Units

<!-- auto:units -->
<!-- repeat per unit -->

### Unit <UNIT_ID> — <SHORT_DESCRIPTION>

- **Unit ID (canonical):** <UNIT_ID>
- **Address:** <FULL_ADDRESS_INCL_FLOOR_AND_UNIT>
- **Type:** <e.g. 3-Zimmer, EG, links>
- **Size:** <m²>
- **Lease Status:** leased | vacant
- **Active Lease ID:** <LEASE_ID | none>

<!-- /repeat -->
<!-- /auto:units -->

## Leases

<!-- auto:leases -->
<!-- repeat per active lease -->

### Lease <LEASE_ID> — Unit <UNIT_ID>

#### Parties

- **Tenant(s):** <TENANT_ID_1>, <TENANT_ID_2>
- **Joint & Several Liability:** yes | no
- **Lease Start:** <DATE>
- **Lease End:** <DATE | open-ended>

#### Cancellation Status

- **Status:** none | cancelled-by-tenant | cancelled-by-landlord
- **Cancellation Date:** <DATE | n/a>
- **Move-out Date:** <DATE | n/a>
- **Remaining Rents:** <N>

#### Rent Components (extracted from lease contract)

- **Kaltmiete:** € <N>
- **Nebenkosten Vorauszahlung:** € <N>
- **Heizkosten Vorauszahlung:** € <N>
- **Extras (Stellplatz/Garage/etc.):** € <N>
- **Total Monthly Due:** € <N>
- **Due Day:** <DAY> of month (per lease) — fallback § 556b BGB
- **Payment Mode:** Überweisung | SEPA-Lastschrift
- **SEPA Mandate Reference:** <MANDATE_ID | n/a>

#### Provenance

- Source contract: <PATH_TO_LEASE_PDF> [^lease-<LEASE_ID>]

<!-- /repeat -->
<!-- /auto:leases -->

## Tenants

<!-- auto:tenants -->
<!-- repeat per tenant -->

### Tenant <TENANT_ID> — <FULL_NAME>

#### Identity

- **Full Name:** <FIRST LAST>
- **Date of Birth:** <DATE | unknown>
- **Address (current):** <FULL_ADDRESS>
- **Email:** <EMAIL>
- **Phone:** <PHONE>
- **Preferred Communication Channel:** email | letter | both
- **Lease ID:** <LEASE_ID>
- **Joint & Several with:** <OTHER_TENANT_IDs | none>

#### Banking

- **Primary IBAN:** <IBAN>
- **Bank Name:** <BANK>
- **Known Third-Party Payers:**
  - <IBAN_1> — <NAME, RELATIONSHIP> (e.g. "Mutter", "Bürge", "Mitbewohner")
- **Verwendungszweck Convention:** "<TEMPLATE_OR_OBSERVED_PATTERN>"

#### Active Reductions (§ 536 BGB)

<!-- If empty: dunning continues normally. -->
<!-- If non-empty: BLOCK dunning → Human-in-the-Loop. -->

- (none) | <list:>
  - **Date raised:** <DATE>
  - **Amount/Percent claimed:** <€ N | X%>
  - **Reason cited:** <TEXT>
  - **Type:** unilateral | agreed
  - **Status:** open | resolved | escalated
  - **Source:** [^email-<ID>] | [^brief-<ID>]

#### Active Deferrals / Payment Plans

<!-- If non-empty: dunning paused → follow plan. -->

- (none) | <list:>
  - **Date agreed:** <DATE>
  - **Terms:** <TEXT>
  - **Schedule:** <DATES + AMOUNTS>
  - **Current adherence:** on-track | behind | breached
  - **Source:** [^email-<ID>] | [^brief-<ID>]

<!-- /repeat -->
<!-- /auto:tenants -->

## Payment Status

<!-- auto:payments -->
<!-- repeat per tenant -->

### Tenant <TENANT_ID> — <NAME>

| Month     | Expected | Received | Matched-Via                                  | Open  | Status                    |
| --------- | -------- | -------- | -------------------------------------------- | ----- | ------------------------- |
| <YYYY-MM> | € <N>    | € <N>    | IBAN \| Reference \| Name fuzzy \| 3rd-party | € <N> | paid \| partial \| unpaid |
| <YYYY-MM> | …        | …        | …                                            | …     | …                         |
| <YYYY-MM> | …        | …        | …                                            | …     | …                         |
| <YYYY-MM> | …        | …        | …                                            | …     | …                         |
| <YYYY-MM> | …        | …        | …                                            | …     | …                         |
| <YYYY-MM> | …        | …        | …                                            | …     | …                         |

- **Open Balance (sum of unpaid claims):** € <N>
- **Last Successful Payment:** <DATE>, € <N>, matched via <METHOD>
- **Default Interest Accrued (live):** € <N> (as of <DATE>)
- **Mahngebühren Accrued:** € <N>

<!-- /repeat -->
<!-- /auto:payments -->

## Mahnstufen History

<!-- auto:mahnstufen -->
<!-- repeat per tenant per claim -->

### Tenant <TENANT_ID> — Claim <CLAIM_ID> (<RENT_MONTH>)

- **Current Stage:** 0 | 1 | 2 | 3
- **Open Amount:** € <N>
- **Default Days (since T+1 WT):** <N>
- **Next Action:** <Stage-N notice | END-paid | Human review | Pre-escalation>
- **Next Trigger Date:** <DATE>

#### History

- **Stage 0** — sent: <DATE> · deadline: <DATE> · met: yes/no
- **Stage 1** — sent: <DATE> · fee: € <N> · deadline: <DATE> · met: yes/no
- **Stage 2** — sent: <DATE> · fee: € <N> · deadline: <DATE> · met: yes/no
- **Stage 3** — case file compiled: <DATE> · status: <pending-human | escalated>

<!-- /repeat -->
<!-- /auto:mahnstufen -->

## Audit Trail — Last Reconciliation

<!-- auto:audit -->

- **Run Date:** <ISO_DATETIME>
- **Bank Statement Window:** <START_DATE> → <END_DATE>
- **Expected Rents (count, sum):** <N>, € <N>
- **Received Payments (count, sum):** <N>, € <N>
- **Matched:** <N>
- **Unmatched Residual:** <N> tx, € <N>

#### Match Method Distribution

- IBAN exact: <N>
- Verwendungszweck: <N>
- Name fuzzy: <N>
- Third-party IBAN: <N>
- Unmatched (→ Human Review): <N>

#### Inputs Used (versioning for proof-of-default)

- **Basiszinssatz:** <X.XX>% (effective <DATE>)
- **Third-Party-IBAN List Version:** <HASH | DATE>
- **Stammdaten Snapshot:** <HASH | DATE>
<!-- /auto:audit -->

## Recent Correspondence (signal-filtered)

<!-- auto:correspondence -->
<!-- Only items the noise filter classified as "relevant" appear here. -->
<!-- repeat per item, newest first, capped at last N items -->

- **<DATE>** — <FROM_NAME> → <TO_NAME> · <CHANNEL: email/letter> · <SHORT_SUMMARY> · classifier: <relevant | borderline> [^src-<ID>]

<!-- /repeat -->
<!-- /auto:correspondence -->

## Open Items / Notes Surfaced by Engine

<!-- auto:open_items -->
<!-- Things the engine wants the human to look at but cannot resolve alone. -->

- (none) | <list:>
  - **Type:** unmatched-payment | conflict | borderline-classification | missing-field
  - **Detail:** <TEXT>
  - **Source:** [^src-<ID>]
  - **Suggested action:** <TEXT>
  <!-- /auto:open_items -->

---

<!-- ============================================================
HUMAN-EDITED REGION — engine NEVER touches anything below this line.
============================================================ -->

## Human Notes

(Free-form notes by the property manager. Decisions, reminders, soft context.
Survives every engine run. Use this for things that don't fit the schema —
informal agreements, history, gut-feel observations, owner preferences.)

## Sources (footnotes managed by engine but readable by humans)

<!-- auto:sources -->

[^src-001]: <FILE_PATH or URL or message-id>

[^src-002]: <...>

[^lease-001]: <PATH_TO_LEASE_PDF>

[^email-001]: <message-id or path>

[^brief-001]: <PATH_TO_BRIEF_PDF>

<!-- /auto:sources -->
