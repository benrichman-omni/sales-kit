# Sales Methodology

Omni qualifies with MEDDPICC, enforced through Salesforce stage gates. Gap Selling is used for discovery and Challenger for messaging.

Stage gates come from Omni's stage guide (current as of 7.22.26; "hit the actual document for most up to date"). Gates marked VERIFY in that guide aren't confirmed production rules.

## Omni nuances (different from most companies)

- **Forecast category is NOT independent of stage.** It follows the stage, so don't set it separately.
- **Discovery and demo usually happen on the same first call.**
- **Co-founders do a product roadmap call** with qualified deals and executives. It's a late-stage step, tracked by the Roadmap fields at Stage 5.
- **Trials:** a customer Slack channel is set up for every POC (Teams if they're a Microsoft shop).

## MEDDPICC

| Letter | Element | What "good" looks like | Evidence required | Where it lives in Salesforce |
|---|---|---|---|---|
| M | Metrics | Quantified business impact, in the buyer's numbers | Buyer said or wrote the number | `Metrics__c` |
| E | Economic buyer | Named person who can sign and fund, and we've met them | Direct conversation | `Economic_Buyer__c` + **Economic Buyer contact role** |
| D | Decision criteria | Technical and business criteria, ideally shaped by us | Criteria in the buyer's words | `Decision_Criteria__c` |
| D | Decision process | Steps, people and dates to signature | MAP or a clear verbal sequence | `Decision_Process__c` |
| P | Paper process | Legal, security and procurement steps, owners, timing | Security review / CSA path / PO identified | Notes + `deal-desk.md` |
| I | Identify pain | Pain with consequence, tied to a person; why now | Stated by the buyer | `Identified_Pain__c` |
| C | Champion | Has influence, sells when we're absent, tested | Took an action that cost them something | **Champion contact role** |
| C | Competition | Alternatives, including status quo and "Claude on the warehouse" | Named by the buyer | `Competitors__c`, `PoC_Competitors__c` |

**Scoring:** 0 unknown · 1 assumed/secondhand · 2 partially confirmed · 3 confirmed with evidence. A deal with Champion or EB below 2 shouldn't be counted in the forecast call.

## Stage gates

**Status key:**
- **HARD** = Salesforce blocks progression.
- **PROCESS** = expected exit criterion.
- **COND** = only applies to some motions.

**Baseline on every save:** Name, Account, Close Date, Stage, `Pipeline_Channel__c` (Inbound / Outbound / Channel).

| Move | Hard gates (Salesforce) | Process exit criteria |
|---|---|---|
| **1 Sales Ready → 2 Pre-Qual** | `Lead_Solutions_Engineer__c` assigned. (`Omni_Exec_Sponsor__c` is not required on most deals, per Salesforce data) | Worth pursuing; second meeting scheduled or being scheduled; supported tech stack |
| **2 Pre-Qual → 3 Qualified** | None verified | Pain (`Identified_Pain__c`), Timeline, Potential Champion, Use Case (`Use_Case__c`), Tech stack (`Data_Tools_In_Use__c`, `Database__c`, `Transformation_Tools__c`), Next Step + date |
| **3 Qualified → 4 Trial** | **Synced quote** with Opportunity Products / quote lines; **Instance** (`Org_Name__c`); **Champion** and **Economic Buyer** contact roles | Competition, Decision Maker, Decision Criteria, Decision Process; POC scope and success criteria linked (`Scoping_Doc_Link__c`); executive outreach done |
| **4 Trial → 5 Trial Positive** | `Roadmap_Session_Completed__c`, `Roadmap_Session_Date__c`, `Roadmap_Omni_Session_Sponsor__c`, `Omni_Exec_Sponsor__c`. The guide calls this a hard gate, but most recent new-business deals passed it without a roadmap session. Ask Reed when it applies | Champion actively selling internally; most decision criteria met in the trial |
| **5 Trial Positive → 6 Negotiate** | None verified | **Technical win:** the prospect explicitly says Omni is the technical preference (`Positive_Feedback__c` supports it) |
| **6 Negotiate → 7 Closed Won** | `Billing_Email__c`; final quote synced and matching the signed terms; products; Champion + EB roles; correct price book / Active Contract (COND: expansion) | Pricing agreed, EB approved, legal and security approved or waived, agreement signed. Upload the signed PDF at close; the close date must be within 1 business day of the signature date |
| **Any → Closed Lost** | `Lost_Reason__c` | `Lost_Description__c`; `PoC_Competitors__c`, `Competitor_Chosen__c`, `Competitor_Existing_Solution__c` / `Competitor_New_Solution__c` as applicable; Account follow-up date if the reason is Timing |

The quote is a hard gate at Stage 4, so pricing is presented before the trial, not after.

A quote can exist and still fail the gate if it isn't synced or has no products applied.

**Motion-specific extras:**
- **Partner/Channel:** Referring Partner and Referring Contact are required (missing contacts have blocked opps).
- **Expansion:** Active Contract and the correct price book.
- **PS subsidies:** may need approvals before late-stage moves.

## Trial structure

- **Phase 1, trial (about 2–4 weeks):** POC scoping call → kickoff → co-dev sessions (usually 2–4 × 1 hr) → end-user demo (optional) → vendor choice chat.
  - Extensions need manager approval.
  - Write success criteria so they favor Omni's strengths (see `competitors.md`).
- **Phase 2, procurement:** pricing discussion → implementation scoping → contract wrap.
- **Trial paper:** see `deal-desk.md`.

## Forecasting (Kaizen)

- Omni forecasts in a Google Sheet called **Kaizen**, with two columns per week:
  - `{date}`: what Ben thinks closes **this quarter**
  - `{date} ({Month})`: what closes **this month**
- "Call" and "Best case" columns are treated the same.
- Late in a quarter, forecast both the current and the next quarter (two tabs).
- **The official revenue view** is the Master Sales Dashboard (Omni app): iARR, AE performance, pipeline.

## Gap Selling discovery flow

1. **Current state:** facts, both technical and business.
2. **Problems:** root cause, not symptoms.
3. **Impact:** what it costs. Get a number.
4. **Future state:** in their words.
5. **The gap:** the size of the gap is the size of the deal.
6. **Urgency:** why now.

## Challenger posture

- **Teach:** reframe their problem. Example: why AI needs semantic context, and text-to-semantics vs. text-to-SQL.
- **Tailor** to each stakeholder.
- **Take control** of next steps, process and money.
