---
name: trigger-scan
description: Finds new prospect accounts with a fresh buying trigger — recent funding, a new data/analytics leader, or analytics job postings that reveal an incumbent BI tool like Looker — filters them against Ben's ICP, and produces a ranked morning list with why-now evidence, who to target, and a draft first email. Designed to run unattended overnight as a scheduled task. Use when the user says "run the trigger scan", "find me new accounts", "who raised money / hired a data leader this week", "find Looker shops", or when a scheduled run asks for the nightly scan.
---

# Trigger Scan

Find 5–10 accounts that have a real reason to look at Omni right now, and hand Ben a morning list he can act on in 20 minutes. Quality over volume: five accounts with a verified trigger beat twenty guesses.

## Setup for each run

1. Load `${CLAUDE_PLUGIN_ROOT}/skills/sales-playbook/references/company-context.md` (ICP), `competitors.md`, and `voice.md`.
2. Load the exclusion lists from Ben's private data home (`~/sales-kit-private`, or an attached Project; see `deal-tracker` → "Where the data lives"):
   - `opps/pipeline.md`: accounts already in pipeline
   - `prospecting/seen-accounts.md`: accounts surfaced in the last 60 days (don't repeat them unless there's a new, stronger trigger, and say so). Accounts in its "Watch list" section are not excluded; include them if they qualify and move them out of the watch list.
   - Omni customers and competitors from `company-context.md`
3. Note the lookback window: since the last run's date in `seen-accounts.md`, or 7 days if this is the first run or a Monday.

## Signals to search (public sources only)

Run several searches per signal and vary the wording. Prefer primary sources (company press release, the job posting itself) over aggregators.

| Signal | What to look for | Where |
|---|---|---|
| **Incumbent BI via job postings** (strongest) | Open roles for analytics engineer, BI developer/analyst, data analyst, head of analytics that name Looker/LookML, Tableau, Power BI, Sigma, Metabase, or Mode, ideally with Snowflake/BigQuery/Databricks and dbt | Public job boards and careers pages (Greenhouse, Lever, Ashby, Workable, company sites) via web search, e.g. `"LookML" analytics engineer site:boards.greenhouse.io` |
| **New data/analytics leader** | Head/Director/VP of Data, Analytics, BI; Chief Data Officer; new CFO (often reshapes reporting), hired in the last 90 days | Press releases, company news pages, business press |
| **Funding** | Series B or later in the lookback window. Growth money usually brings reporting and board-metric pressure | Funding news (TechCrunch, Business Wire, PR Newswire, company blogs) |
| **Other strong triggers** | Announced BI migration or consolidation, acquisition (two stacks to merge), IPO prep, new embedded-analytics product plans | News, engineering blogs, earnings or investor material |

Stacked triggers (e.g., funded and hiring an analytics engineer who'll use Looker) rank highest.

## Qualify every account

- **Size: 100–500 employees** (from the ICP; confirm from the company site or a reputable source, and give a range if unsure). Drop anything clearly outside.
- **Stack fit:** cloud warehouse evidence; incumbent BI tool or clear BI pain.
- **Not excluded** (pipeline, seen, customer, competitor).
- **Trigger is recent and verified**, with a dated source link. No link means no account.

## Output

Write the morning list to `prospecting/daily/{YYYY-MM-DD}.md` (the run date) in the data home, using `references/daily-list-template.md`. Then append each surfaced account under "## New entries" in `prospecting/seen-accounts.md` (`date · account · trigger · fit`), and update the "Last run" line at its top.

Each account gets:
1. Account, one-line description, size, HQ.
2. **Why now:** the trigger(s), each with date and source link.
3. **Stack evidence:** what they use, confidence (confirmed / likely), and the source.
4. **Who to target:** the persona and title. Name a specific person only if their name and role appear in a public professional source (press release, company team page, the job posting). Professional information only, nothing personal.
5. **Angle:** one or two sentences tying the trigger to an Omni point of view (Gap Selling: current state → cost → better future).
6. **Draft first email:** 50–90 words in Ben's voice, following `voice.md` exactly. Mark any product claim not confirmed in `company-context.md` as `[VERIFY: ...]`.
7. **Fit:** A / B / C with one line of reasoning.

Rank A's first. At the top, write a 3-line summary: how many accounts were found, the single best one and why, and anything unusual (e.g., a burst of Looker postings in one industry).

If fewer than 5 accounts qualify, return what's real and say so. Never pad the list.

## Unattended runs

When running as a scheduled task with no one watching:
- Don't ask questions; make the reasonable call and note it in the summary.
- **Never send emails, connection requests, or messages to anyone but Ben, and never add contacts to any tool.** The only email allowed is the list itself to Ben's own inbox, when the scheduled prompt asks for it. Prospect drafts stay drafts; Ben reviews everything.
- If the data home isn't available, deliver the full list in the final message of the run instead, and say so.
- Keep it to roughly 30–40 minutes of searching; stop once there are 10 solid accounts.

## Data handling

Prospect lists and drafts are working data: they live in the private data home, never in the plugin repo or GitHub.
