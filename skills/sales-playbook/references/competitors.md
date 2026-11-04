# Competitive Landscape

**Official repository:** the Competitive Portal (as of July 2026; some content is dated).

**Sources for this file:**
- Sigma vs. Omni Messaging (June 2026)
- Stew's Sigma notes
- Omni's AI vs Sigma & Snowflake
- GTM Enablement: Hex

**Rules:**
- Never put unverified competitor claims in buyer-facing writing.
- In emails, compete on the buyer's problem, not by trashing a vendor.
- Lines marked INTERNAL never go to a buyer.

**What Commercial usually sees:**
1. BI shootouts, usually against Sigma
2. "AI on the warehouse" deals, meaning Claude/Cortex on Snowflake or another CDW (these can get scary)
3. Hex

**Internal help:**
- **Chris Daniel** (AE, ex-Sigma)
- **@omni in Slack** for past-deal examples ("examples of when we competed against X, where we won and lost")

## Sigma (biggest pure-BI competitor)

**Where you'll meet it:**
- Snowflake and Databricks accounts. Sigma is 4x Snowflake and 2x Databricks BI Partner of the Year.
- Spreadsheet-native "power users": ops, FP&A, merchandising, supply chain.
- Exec pitch: "self-service is your most important problem; keep governance in the warehouse/dbt to avoid lock-in."

**What they do well (be honest):**
- Input tables and writeback
- Real-time multiplayer editing
- Fast ad-hoc exploration; undo and version history
- Workbook actions; materialization back to the warehouse
- Pixel-perfect reporting (GA March 2026)
- Building data apps that replace PowerApps and Excel

**Pains to exploit:**
- Data sprawl, "spaghetti lineage," and "why doesn't your number match mine"
- Shallow semantic-layer integration:
  - Snowflake Semantic View facts can't be queried
  - dbt MetricFlow only through custom SQL
  - No Databricks Metric Views
- No native Git/CI/CD; as-code features are raw APIs, still in preview
- Brittle, UI-configured RLS
- No server-side cache
- AI not grounded in a governed model ("just use Cortex")

**Talk tracks:**
- "You don't have to choose: self-service *and* a governed model."
- "Move fast, but fall back on trusted results."
- "The only way to do AI correctly is with a semantic layer."
- Proof: Git and dbt branching with content validation; native dbt, Snowflake and Databricks integrations; AI modeling agent and business-user contributions to the model; caching; topic-level RLS; per-customer extensions for embed; 1:1 Excel formulas with cell references (Sigma is column-only).
- **ABCStores lesson:** lead with "full SDLC, backed by Git."

**Trap questions:**
- Different business definitions across teams?
- Changes to prod without validation?
- Users pointed at raw tables?
- Different numbers in the same meeting?
- Tracking spend and usage?
- Many customers or schemas for embed?

**More offensive moves:**
- Ask them to test Sigma's semantic-layer integration side by side.
- Ask for a Sigma reference customer on native AI.

**Discovery:** find out whether Sigma wrote the POC success criteria, the spreadsheet vs. SQL user mix, and Sigma's contract timing.

**Defense:**
- **Writeback:** "We have input tables for forecasts, scenarios, commentary."
  - Sigma will push writeback into POC criteria and call ours "CSV upload."
  - Discover early, and disqualify yourself if the deal is app-heavy.
- **Pixel perfect:** in progress; Omni Apps let AI build custom reports. Don't commit to a date.
- **Multiplayer:** "We let you branch content, contribute and review."
- **Workbook actions:** don't match feature for feature. Ask "how many are day-1 priorities?"
- **"Separate semantic layer / lock-in":** it's all YAML, with two-way dbt, Snowflake and Databricks integrations.
- **Cache demos:** Sigma shows Omni edit mode returning cached partial results. Raise it before they do.
- **Other FUD to expect:**
  - "Omni is for data teams"
  - "sells services because it's complex"
  - "Looker 2.0"
  - "risky at its stage"
  - "duplicate modeling": admit there's an initial lift that pays off over time

**Commercial:**
- Sigma uses consumption pricing; "free now, but it's in the contract for a reason."
- Writeback costs per row.
- Sigma won't cap renewal pricing in the MSA. Omni's CSA caps uplift (see `pricing.md`).
- Omni will discount seats to match Sigma's free viewers.

**Landmines:**
- Don't claim writeback *to the database / other apps*. Enablement material contradicts itself on this.
- Spreadsheet power users who drive the deal tend to like Sigma, and we'll have a hard time. Qualify for that early.
- Omni has no materialization.
- Proof deal: **Nicus**, a competitive shootout with Sigma (full cycle in the Gold Standard Library). Giggle Finance demo vs. Sigma.

## "AI on the warehouse" (Claude/Cortex on Snowflake, bring your own model)

**Snowflake's semantic layer:**
- Covers the basics, and Omni can inherit that work.
- But it's an add-on that wasn't built for BI. It has no period-over-period, so the LLM "will make it up."
- Only data engineers can extend it.

**Talk track: "faster, better, cheaper"**
- Omni's harness gives the LLM only the relevant semantic context.
- **Text-to-semantics** (deterministic, matches the UI) vs. **text-to-SQL** (not deterministic). See Jamie's blog on why text-to-SQL fails.
- "You're welcome to work in Snowflake's semantic layer; you'll end up doing some in Omni too."

**BYOM defense:**
- Bringing your own model isn't automatically more secure, because it adds another provider.
- BYOK still carries a harness fee; token efficiency offsets it.
- [VERIFY with SE] the claims that "data doesn't leave your VPC" and that the internal test beat Claude given the full semantic layer.

**Sigma angle:** Sigma "passes through" Cortex, so the AI cost is hidden in warehouse spend, not gone.

**INTERNAL, never say:** "We've optimized for Claude models, so a customer's own Claude isn't that different."

## Hex (growing, especially in AI-on-the-warehouse style deals)

**Who:** data science and analytics-engineering teams, now moving into business analytics.

**Strengths:**
- Good product and good marketing (it can make Omni's breadth look like "bloat").
- Quick to trial; modeling is optional.
- Threads chat; a Cursor-style notebook agent.
- Context Studio and endorsed mode.
- Hex AI has full SQL/Python freedom.

**Weaknesses:**
- Shallow semantics: no extensions, aggregate awareness or user attributes.
- Limits on version control, dbt CI/CD, multi-database and complex joins.
- The UI feels technical once business users leave chat.
- No way for business users to contribute to the model.

**Talk track:** "Hex is fantastic for technical people who want a sandbox to move fast and break things. If you want to move fast and *trust* things across the whole org, go with Omni."

**Plays:**
- Out-hustle Hex in discovery on governance, semantic complexity and business-user needs.
- Demo AI building governed metrics, instant period-over-period/KPI views, and safe model edits from the UI.
- Show POC progress in hours or days.

**Landmine:** confirm the current Claude Code / CLI story before citing it, since enablement slides conflict.

**Example call:** "getting a leaning out of a prospect in a 2-way shootout w/ Hex" (Gold Standard Library).

## Looker (displacement)

- Omni will get creative on pricing to displace existing Looker contracts (see `pricing.md`).
- Founding team context: TODO. [VERIFY: Looker migration tooling before claiming ease of migration.]

## MicroStrategy

Enterprise take-outs only. Don't spend time on it in Commercial.

## Others (working notes, not enablement)

| Competitor | Angle (verify) | Landmine |
|---|---|---|
| Tableau | Single semantic layer across every user type | Don't fight on chart polish |
| Power BI | Total cost and data-team time | "Free" bundling perception |
| ThoughtSpot | AI grounded in the semantic model, runs with user permissions | TODO |
| Lightdash | TODO | Open-source price anchor |
| Holistics | Ask @omni for past competes | TODO |
| Sisense | Embedded styling + semantic layer | Ben's insider context: respect confidentiality |
| Status quo | Quantify backlog and metric drift (Gap Selling) | The real competitor in most deals |

## Discovery questions that surface competitive pain

- "When two teams bring different numbers to the same meeting, how does that get resolved?"
- "What happens if someone changes a prod dashboard without validation?"
- "Where are people asking AI tools questions about your data today, and do you trust the answers?"
- "What happens at your next BI renewal — decision point or formality?"
