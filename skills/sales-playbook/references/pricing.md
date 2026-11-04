# Pricing & Packaging — Omni (INTERNAL)

Source of truth: "Omni Pricing & Packaging" sheet, tab **OFFICIAL 6.26.26**. The pricing calculator is "Omni Pricing 2026 Q1". Commercial guidance comes from the Commercial Onboarding Master Reference Doc. Re-check the official tab before any quote, because pricing changes.

**Internal only.** Never put discounts, approval thresholds, margin, or comp math in buyer-facing drafts. List prices may go in a draft only when Ben says so. Otherwise use `[VERIFY: pricing]`.

## Mindset

Omni is flexible and plays to win on price, especially in head-to-head Sigma competes and Looker displacements. Protect iARR first. Give away things that don't count toward iARR before cutting it.

## Platform tiers (list, per year)

| | Starter | Standard | Enterprise |
|---|---|---|---|
| Platform fee | $24k | $36k | $100k |
| Users included | 10 (any mix) | 10 | 20 |
| AI credits included / month | 50 | 100 | 500 |
| RSD discount floor | $15k | $24k | $100k |

- **Starter** is the default for internal use at companies with 1–100 employees.
- **Standard** is the default for embedded use at 1–100 employees. Be ready to fall back to Starter if cost is a concern.
- RSDs can approve discounts down to the floors above. Going lower needs CTO, VP Finance and VP Sales.

## Users (list, per month)

Viewer $15 · Standard $30 · Developer/Admin $60.

Seats can be discounted aggressively to reach parity with competitors (for example, Sigma gives viewers away free).

## AI credits

- **Included credits** = (iARR / 12) × 10%, per month. AEs can include up to 10% of iARR as monthly credits with no approval.
  - Example: a $42,857 iARR deal gets about 357 credits/month at 10%.
- **Approvals above 10%:** VP Sales up to 12.5%, VP Finance up to 15%, CEO above 15%.
- **Additional credits** are billed in arrears at $1/credit. Pre-purchase is possible but should be right-sized, because there are no rollovers or refunds.
- Natural-language Q&A, AI summarization, Calculation AI, AI branding and MCP / AI APIs are included in all tiers.
- **BYOK (bring your own LLM key):** not available on Starter, in progress on Standard, included on Enterprise. BYOK still runs through Omni's AI harness, so it isn't free.
- ⚠ **Conflict to resolve:** the onboarding doc says "100/month standard OR up to 10% of iARR," and its example of $42,857 iARR → 428 credits doesn't match (iARR/12)×10%. Use the official formula and confirm with Reed.

## Add-ons

| Item | Starter | Standard | Enterprise | Approval / floor |
|---|---|---|---|---|
| Whitelabel (embed) | $6k/yr | $6k/yr | incl. | RSD; can go to $0 |
| Additional workspaces (dev/staging/prod) | — | $24k/yr | incl. | RSD; can go to $0 |
| IP whitelisting | — | incl. | incl. | RSD |
| PrivateLink | — | $6k/yr | incl. | RSD; can go to $0 |
| Additional regions (multitenant) | — | $24k existing / $50k new | 3 existing AWS regions incl.; then same | CTO before pricing any new region |
| Single-tenant hosting | — | — | +$75k per environment | Floor $50k; CTO + VP Sales + VP Finance before showing any discount |

- Shared model extensions, custom roles and OAuth data connections are on Standard and Enterprise, not Starter.
- Git integration, SSO/OIDC and APIs are on every tier.

## Paper, SLAs, renewal caps

- **Redlines on Omni paper:**
  - Below $50k iARR, accept changes to the Cover Page and Order Form only, not the CSA.
  - Any agreement below $50k iARR needs CEO, CTO and VP Sales approval.
- **Customer paper:** push back in every case. It's typically considered only above $120k iARR, and needs CEO, CTO and VP Sales approval.
- **Technical support and uptime SLAs:** Standard and Enterprise above $75k iARR. Below that, the CTO must approve.
- **Slack support** is on all tiers (business hours only on Starter). Customer security reviews are on Standard and Enterprise.
- **Renewal uplift (contract):** up to the greater of 6%/yr or CPI-U.
  - Negotiable without approval: 12-month term 5%, 24-month 4%, 36+ month 3% per year/CPI.
  - Going lower needs VP Finance and VP Sales.

## Deal structure

- **Term:** 1 or 2 years is standard; 3 years only on request. The FY27 comp plan pays 1% on additional years, so multi-year is not a big comp lever.
- **iARR is annualized.** Free months reduce iARR.
  - Example: $50k over 14 months = $3,571 MRR × 12 = **$42,857 iARR**.
  - Avoid adding free months as a concession.
- **Elegant negotiables, in order:**
  1. **Services to $0.** AEs aren't comped on PS, it needs no approval, and PS is fully aligned with this.
  2. **Overdeployment in a 2-year deal.** Allow significant overdeployment in Year 1, with a true-up in Year 2 (it doesn't have to be at rate card).
  3. **Discount the platform fee.** This is the first iARR lever, because it preserves future seat upsell.
  4. **Discount seats** to reach competitive parity.
- **Professional services:** Omni Quickstart package is about $6k–7.5k one-time on the calculator. [VERIFY: current PS packages with Joe Bertha.]

## Embedded pricing

- **Three models:** pay per user, per tenant (client), or per active user. All are flexible.
- **Internal + embed buyers:** start with a "mirrored platform," meaning 2 platforms (internal + external) plus the required seats. Embed seats have the same roles (Viewer, Standard, Admin).
- **If the buyer pushes back:** "You don't want internal users breaking your external embedded dashboards" (separation of church and state).
- **Calculator reference (Q1 2026 tab; may be dated):**
  - Embed viewer bulk tiers: $3.67 (1–200), $3.00 (201–400), $2.50 (401–600), $2.10 (601–800), $1.75 (801+) per user/month.
  - Client (tenant) pricing: $75/client/month, with bulk tiers $70 → $49 and custom above 800.
- **Good embed pricing discovery calls:** Rad AI and Arine (Gold Standard Library).

## Approvals cheat sheet

| Ask | Who |
|---|---|
| Platform discount to the tier floor | RSD |
| Below the floor | CTO + VP Finance + VP Sales |
| AI credits >10% / >12.5% / >15% of iARR | VP Sales / VP Finance / CEO |
| Agreement <$50k iARR with redlines | CEO + CTO + VP Sales |
| Customer paper | CEO + CTO + VP Sales |
| SLAs <$75k iARR | CTO |
| Renewal cap below the term threshold | VP Finance + VP Sales |
| Unsure | #deal-desk |
