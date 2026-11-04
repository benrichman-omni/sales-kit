# Company Context — Omni

Seeded from public sources on 2026-10-24. Updated 2026-11-04 from the Commercial Onboarding Master Reference Doc.

Lines marked `TODO` are unknown. Never fill them with guesses in buyer-facing output.

## What Omni is (public)

- **AI analytics / BI platform.** It replaces the manual BI workflow (dataset prep, hand-written SQL, dashboard building) with a governed semantic model and several ways to work with data:
  - natural-language chat
  - a SQL editor
  - a point-and-click workbook
  - a spreadsheet interface
- **Semantic model:** business definitions that keep metrics consistent and guide how the AI interprets questions.
- **AI runs with the user's own permissions** and shows its reasoning.
- **Context modeling** exposes data definitions and SQL guidance to third-party AI tools. An MCP server lets AI agents work with Omni.
- **Embedded analytics:** visualizations embedded in customers' products and styled to match.
- **CEO:** Colin Zima. TODO: founding team background for credibility stories.
- **Funding:** $120M Series C at a $1.5B valuation (April 2026), led by ICONIQ with GV and Redpoint. Revenue roughly tripled YoY.
- **Publicly named customers:** Perplexity, dbt Labs. Cribl has a published Omni + dbt case study. TODO: full referenceable logo list.

## Ideal customer profile

Starter ICP (Ben's working definition until Omni's official ICP and territory arrive):

- **Size:** 100–500 employees.
  - Salesforce `Segment__c`: SMB ≤100, Commercial ≤500, Enterprise >500. Ben is a Commercial AE.
  - Starter is the default internal package for ≤100 employees (see `pricing.md`).
- **Data maturity:** on a cloud warehouse (Snowflake, BigQuery, Databricks, Redshift). dbt is a plus.
  - A supported tech stack is a Stage 2 exit criterion.
- **Incumbent:** a BI tool (Looker, Tableau, Power BI, Sigma, Metabase, Mode, etc.), or clear BI pain on spreadsheets/SQL. "AI on the warehouse" projects count too.
- **Exclude:**
  - Omni customers, competitors and partners (`Account.Type`)
  - Accounts owned by another rep
  - Accounts already in Ben's pipeline
  - Check Salesforce first (`deal-tracker/references/salesforce.md`).
- TODO: official industries
- TODO: territory / account list (arriving week of 2026-11-09)

## Personas

| Persona | Typical title | What they care about | Common objection |
|---|---|---|---|
| Economic buyer | VP/Head of Data, CDO, CFO | TODO | TODO |
| Champion | Analytics/data eng lead | TODO | TODO |
| Technical evaluator | Analytics engineer | Git/SDLC, dbt integration, modeling | "Duplicate modeling" vs. dbt/Snowflake semantic layer |
| Business user | Ops/finance/RevOps leaders | Self-serve answers they trust | Spreadsheet power users may prefer Sigma |
| Embedded buyer | VP Product / CTO / CPO | Tenant isolation, branding, per-customer customization | Pricing model; the mirrored-platform ask |

## Value pillars

- TODO: official messaging pillars. Pull them from the AI Sales Deck (June 2026) and the Master Sales Deck (July 2026, RVG).
- **Recurring themes in enablement** (OK to use, phrased in Ben's voice):
  - Self-service *and* governance, no trade-off.
  - AI is only trustworthy with semantic context: text-to-semantics, not text-to-SQL.
  - Full SDLC backed by Git.
  - Move fast and trust the results.

## Pricing & packaging

See `pricing.md` (internal).

Never offer discounts or concessions in writing without Ben's explicit say-so.

## Proof points

- **Internal call examples (Gold Standard Library; confirm referenceability before naming a customer to a buyer):**
  - StackHawk: qualified inbound where everything goes right
  - Nicus: competitive win vs. Sigma
  - Sutter Health: the prospect posted about Omni on LinkedIn
  - Lovevery: internal analytics, working with the VP Data as EB
  - Embed POCs: LevelTen, Block, Digible
  - Embed pricing: Rad AI, Arine
- Cribl: Omni + dbt case study
- TODO: quantified outcomes by segment.

## Partners

**Snowflake**
- **Partner lead:** Rachel Griffin. Ben Froelich covers while she's on leave (from end of July 2026).
- Run account questions through Ben Froelich, **not** the shared Slack channel. Some Snowflake folks there are Sigma fans and may tip Sigma off.
- Snowflake AEs get **2x commission credit on compute driven by Omni**. Omni is one of only a few vendors with this, so it's a reason for the Snowflake AE to help. This is internal context; don't put it in a customer deck.

**dbt**
- **Partner lead:** Madison Nelson.
- Assets: "dbt + Omni" (use cases, features, objection handling) and "AS dbt for Omni SEs".

## Sales process at Omni

- **Stages, gates and forecasting:** `methodology.md`. Salesforce fields and write protocol: `deal-tracker/references/salesforce.md`. Paper process: `deal-desk.md`.
- **First call = discovery + demo.** POC/trial is standard, with a Lead SE assigned before Stage 2.
- **Co-founders do roadmap calls** late in the cycle. This is required before Stage 5.
- **Professional services:**
  - Joe Bertha owns PS; set up 30 min with him in the first 2 weeks.
  - Omni stays a software company: PS is discounted to $0 before giving up ARR, with no pushback from PS.
- **Customer channels:** a shared Slack channel per POC (prospect + AE + SE); Teams if the customer is a Microsoft shop. See the "How to set up Customer Channels" guide.

## Tools

| Tool | Use | Notes |
|---|---|---|
| Salesforce | CRM, system of record | Stage gates enforce fields |
| Fathom | Call recording and transcripts | Search is buggy: find the call on the calendar, then use "All Teams" for that day. No Gong |
| Amplemarket | Sequencing, contact data | |
| LinkedIn Sales Navigator | Prospecting | |
| RevenueHero | Booking links and inbound routing | Connect Zoom + Google Calendar, or inbounds won't route |
| Zoom / Roam | External / internal meetings | In Roam, joining while the speaker is off stage defaults to mic on ("Whisper") |
| Common Paper | Contracts, NDAs, signatures | See `deal-desk.md` |
| Kaizen (Google Sheet) | Weekly forecast | See `methodology.md` |
| Omni apps | Master Sales Dashboard (official iARR/pipeline), closed/lost revival kit, Customer Overdeployment dashboard | |
| Rippling / Ramp | HR and org chart / expenses | HR is run by Jake (VP Finance) |

## Content

- **Decks:**
  - Traditional "Internal BI call deck" (June 2026)
  - "AI Sales Deck" (June 2026, most current)
  - "Embedded Analytics first call deck" (June 2026)
  - RVG's "Master Sales Deck" (July 2026)
  - Most AEs build their own from the BI and AI decks. Copy them; never edit a master.
- **Libraries:** GTM Hub (official decks, competitive briefs, case studies, logos), the Content Library sheet, and the Competitive Portal.

## Sources

- SiliconANGLE, "Omni raises $120M round backed by GV for AI analytics platform," 2026-04-23.
- Comm Onboarding Master Reference Doc, read 2026-11-04.
- Omni Pricing & Packaging sheet, OFFICIAL 6.26.26 tab.
