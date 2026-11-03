# Company Context — Omni

Seeded from public sources on 2026-10-24. Everything here should be confirmed or replaced with Omni's internal enablement material after onboarding starts (11/2). Lines marked `TODO` are unknown — never fill them with guesses in buyer-facing output.

## What Omni is (public)

- AI analytics / business intelligence platform. Replaces the manual BI workflow (dataset prep, hand-written SQL, dashboard building) with a governed semantic model plus multiple ways to work with data: natural-language chat, a SQL editor, a point-and-click workbook, and a spreadsheet interface that can sync with warehouses like Snowflake.
- Semantic model: business definitions that keep metrics consistent and guide how the AI interprets questions.
- AI runs with the user's own permissions and shows its reasoning.
- Context modeling exposes data definitions and SQL guidance to third-party AI tools; an MCP server lets AI agents work with Omni.
- Embedded analytics: visualizations can be embedded in customers' own products, styled to match.
- CEO: Colin Zima. (TODO: confirm founding team background for credibility stories.)
- Funding: $120M Series C at a $1.5B valuation (April 2026), led by ICONIQ with GV and Redpoint participating. Company reported revenue roughly tripled year over year.
- Publicly named customers: Perplexity, dbt Labs. (TODO: full referenceable logo list by industry and segment.)

## Ideal customer profile

Starter ICP for prospecting (Ben's working definition until Omni's official ICP and territory are known):

- Company size: 100–500 employees.
- Data maturity: on a cloud warehouse (Snowflake, BigQuery, Databricks, Redshift); dbt usage is a plus.
- Incumbent BI tool present (Looker, Tableau, Power BI, Sigma, Metabase, Mode, etc.) or clear BI pain on spreadsheets/SQL.
- Exclude: Omni customers and competitors (Salesforce `Account.Type` = Customer / Competitor / Partner), accounts owned by another rep in Salesforce, and accounts already in Ben's pipeline. Check Salesforce before surfacing or researching any account (`deal-tracker/references/salesforce.md`).
- Segments (Salesforce `Segment__c`): SMB ≤100, Commercial ≤500, Enterprise >500 employees. Ben is a Commercial AE.
- TODO: official industries
- TODO: territory / account list for Ben (arriving week of 2026-11-09)

## Personas

| Persona | Typical title | What they care about | Common objection |
|---|---|---|---|
| Economic buyer | VP/Head of Data, CDO, CFO | TODO | TODO |
| Champion | Analytics/data eng lead | TODO | TODO |
| Technical evaluator | Analytics engineer | TODO | TODO |
| Business user | Ops/finance/RevOps leaders | TODO | TODO |
| Embedded buyer | VP Product / CTO | TODO | TODO |

## Value pillars

- TODO: official messaging pillars from enablement
- Working hypotheses until then (do not present as official): one governed source of truth across chat, SQL, workbook, and spreadsheet users; AI answers that are trustworthy because they sit on the semantic model; faster time-to-insight for business users without bypassing the data team.

## Pricing & packaging

- TODO. Never quote pricing in drafts; use `[VERIFY: pricing]`.

## Proof points

- TODO: case studies, quantified outcomes, reference customers by segment.

## Sales process at Omni

- **CRM: Salesforce** (system of record). Stages: 1 Sales Ready/Strategy → 2 Pre-Qual → 3 Qualified → 4 Trial → 5 Trial Positive → 6 Negotiate → 7 Closed Won / Closed Lost. Quota amount is `iARR__c`, calculated from the quote. MEDDPICC lives in Opportunity fields. Field map, queries and the mandatory write/audit protocol: `deal-tracker/references/salesforce.md`.
- **Call recorder: Fathom.** Every call is recorded with an AI summary, emailed to Ben after the call, and readable through the Fathom connector (transcripts, summaries, action items). Fathom also shows teammates' recorded calls, which is useful for shadowing during ramp.
- **Prospecting / sales engagement: Amplemarket** (contact data, sequences). Salesforce also carries legacy Outreach sequence fields.
- Trials: a POC/trial stage (4 → 5) is standard, with an SE involved (e.g., "POC Trial Kickoff" calls). TODO: trial norms, SE engagement rules, exit criteria, deal desk / legal process.

## Sources

- SiliconANGLE, "Omni raises $120M round backed by GV for AI analytics platform," 2026-04-23.
