---
name: account-research
description: Builds an account brief on a target company for prospecting — business priorities, data and analytics stack signals, buying triggers, key people, and a recommended angle and first-touch hypothesis. Use when the user says "research {company}", "build an account brief", "what should I know about {company}", "is {company} a good fit", "find me an angle on {company}", or pastes a list of accounts to prioritize.
---

# Account Research

Produce a tight, opinionated account brief that ends in a point of view on how to break in — not an encyclopedia entry.

## Before starting

1. Load `${CLAUDE_PLUGIN_ROOT}/skills/sales-playbook/references/company-context.md` (ICP, personas) and `competitors.md`.
2. If the user gave a list of accounts, switch to **Batch mode** below.

## Research checklist

Search the web (and any connected CRM, notes, or email) for:

- **Business snapshot:** what they sell, to whom, size (employees, revenue range if public), funding/ownership, growth trajectory.
- **Strategic priorities:** earnings calls, shareholder letters, CEO interviews, press releases, recent strategy shifts, M&A.
- **Triggers (last 6–12 months):** funding, new exec hires (especially CDO / VP Data / CFO / CIO), layoffs, reorgs, new product lines, international expansion, IPO prep, acquisitions — anything that creates reporting or data pressure.
- **Data stack signals:** job postings mentioning Snowflake / BigQuery / Databricks / Redshift, dbt, Looker / Tableau / Power BI / Sigma / etc.; engineering blog posts; conference talks; public GitHub. Job postings are the single best signal — read 2–3 data/analytics postings.
- **People:** data/analytics leadership, finance leadership, RevOps/BizOps, and (for embedded) product/engineering leaders. Note tenure — new leaders in their first 90–180 days are prime.
- **Existing relationship (check first):** query Salesforce for the Account (owner, `Type`, open and closed opps; "Account check" query in `deal-tracker/references/salesforce.md`). If another rep owns it, say so at the top of the brief before doing more work. Also check Gmail for prior touches and Fathom (`search_meetings` by company name) for past calls, including teammates' calls.

Cite every non-obvious fact with a source link. Mark inference clearly as inference.

## Output: account brief

Keep to roughly one screen. Use this structure:

**{Company} — account brief** (date)

1. **Why now (2–3 sentences):** the single strongest reason this account might buy in the next two quarters.
2. **Snapshot:** one short paragraph.
3. **Triggers:** bulleted, each with date and source.
4. **Stack signals:** what they use, how confident (confirmed / likely / guess), and the evidence.
5. **People to target:** table — name, title, persona, tenure, why them, LinkedIn/source link.
6. **Hypothesized pain:** 2–3 Gap Selling–style hypotheses (current state → problem → likely impact).
7. **Recommended angle:** the point of view to lead with and which persona to open with.
8. **Fit score:** A / B / C with one line of reasoning against the ICP (or "ICP not yet defined" if `company-context.md` is still TODO).
9. **Open questions:** what research couldn't answer.

Then offer: "Want a first-touch sequence for {top persona}?" (hands off to `outbound-prospecting`).

## Batch mode (list of accounts)

For 5+ accounts, do a lighter pass per account (snapshot, top trigger, stack signal, fit score) and return a ranked table: account, fit, top trigger, recommended first persona, one-line angle. If more than ~15 accounts, write the table to a spreadsheet/CSV instead of the reply. Offer full briefs on the top 3.

## Guardrails

- Business information only. Don't dig into people's personal lives, home locations, family, or non-professional social accounts.
- Don't fabricate tech stack. "No public signal" is a valid finding.
