# Sales Kit (Omni)

A portable set of Claude skills for running a full sales cycle end to end, from SMB to enterprise — built for Ben's ramp at Omni (start date 2026-11-02), designed to move between Claude accounts (personal → work) without losing anything.

## What's inside

| Skill | What it does | Try saying |
|---|---|---|
| `sales-playbook` | Shared foundation: Omni context, personas, competitors, MEDDPICC/Gap Selling, Ben's writing voice. Every other skill reads from it. | "What's our positioning against Looker?" |
| `account-research` | Account briefs with triggers, stack signals, people, and a recommended angle. Batch mode ranks a territory list. | "Research Ramp and find me an angle" |
| `outbound-prospecting` | Cold emails, multi-touch sequences, LinkedIn notes, call openers, voicemails, multi-threading. | "Build a sequence for the VP Data at Ramp" |
| `trigger-scan` | Runs every weekday before you wake up: finds 5–10 new accounts (100–500 employees) with a fresh trigger (funding, a new data leader, analytics job posts naming Looker/Tableau/etc.), each with sources, who to target, and a draft email. Lands in the Project under `prospecting/daily/`. Public sources only, never sends anything. | "Run the trigger scan" |
| `meeting-prep` | One-page brief: objective, attendees, questions mapped to MEDDPICC gaps, demo storyline, objections. | "Prep me for tomorrow's demo with Acme" |
| `email-reply` | Diagnoses what the buyer really means, then drafts replies (2 strategic variants when stakes are high). | "They pushed back on price — help me reply" |
| `call-follow-up` | Notes/transcript → buyer recap, internal notes, MEDDPICC update, tracker update. | "Here are my notes from the Acme call" |
| `deal-review` | Manager-grade deal pressure test, forecast call prep, close plans, mutual action plans, pipeline review. | "Pressure test the Acme deal" |
| `deal-tracker` | Opportunity management: Claude keeps your pipeline and a record per opp in your private claude.ai Project (never GitHub). Feed it quick updates, notes, or call transcripts; it updates MEDDPICC, next steps, and risks, and flags what needs attention. | "Acme pushed to Jan, EB is Dana" · "What needs attention?" |
| `weekly-plan` | Monday focus plan and Friday review / manager update. | "Plan my week" |
| `ramp-plan` | 30/60/90 plan and learning capture that feeds what you learn at Omni back into the playbook. | "I just learned how we position embedded" |

## Installing on any Claude account

**As a plugin (Cowork / Claude desktop / Claude Code):** install `sales-kit-omni.plugin` — open it from the chat and accept, or add it through the plugin settings on the other account.

**As individual skills (claude.ai web/mobile):** the `skills-zips/` folder has one zip per skill. Upload each through Skills in your Claude settings. Upload `sales-playbook` first — the others reference it.

**As a Project:** create a Project on the other account, paste `PROJECT_INSTRUCTIONS.md` into its instructions, and add the files in `skills/sales-playbook/references/` as project knowledge.

Moving to the work account: re-upload the latest zip. Since everything is plain files, the source of truth is this folder — keep it in Google Drive or a private GitHub repo and repackage when it changes.

## Scheduled tasks

The `schedules/` folder holds the setup for each recurring task (schedule, connectors, and the exact prompt) so they can be recreated on any account. Ask Claude to "set up the tasks in schedules/ for {your email}".

## Customize first (week one at Omni)

1. Fill the `TODO`s in `skills/sales-playbook/references/company-context.md` from enablement (ICP, personas, pillars, proof points, stages, CRM).
2. Replace `competitors.md` working notes with official battlecards.
3. Swap placeholder stages in `methodology.md` and `deal-tracker/references/schema.md` for Omni's.
4. Tell Claude your weekly activity targets and quota so `weekly-plan` and `deal-review` can measure against them.

The `ramp-plan` skill will help do all of this conversationally.

## Connectors that make it better

Email (Gmail/Outlook) for thread context and drafts · Calendar for meeting prep and weekly plans · Google Sheets for a shared live tracker · Omni's CRM (Salesforce/HubSpot — TBD) once available · call recording (Gong etc.) for transcripts. Nothing is ever sent without explicit approval.

## Roadmap (ideas for v0.2+)

- CRM sync skill once Omni's CRM is known (reconcile tracker ↔ CRM, write call notes back)
- Demo storytelling skill with per-persona Omni demo scripts
- Business case / ROI builder (metrics → one-page value summary for the EB)
- Objection library that grows from real calls
- Champion enablement kit (internal pitch deck + email the champion forwards)
- Win/loss analysis across closed deals
- Scheduled tasks: Monday 8am weekly plan, daily "replies owed" check, Friday review
- Trigger scan v2: plug in Sales Navigator alerts and Omni's data tool (ZoomInfo/Apollo/Clay) once known; champion job-change tracking

## Version

0.3.1 — 2026-11-02. ICP size changed to 100–500 employees (Ben works accounts 100–500).
0.3.0 — 2026-10-28. Nightly trigger scan; starter ICP (200–1,000 employees).
0.2.0 — 2026-10-24. Deal tracker becomes an opportunity management system stored in the private Project; deal-data guard added.
0.1.0 — 2026-10-24. Initial scaffold.

## Updating the installed plugin

This repo is the source of truth. After changes, ask Claude to repackage the plugin from `benrichman1995/sales-kit-omni`, or zip the repo contents (excluding `.git`) as `sales-kit-omni.plugin` and install it on each account.

## What goes in GitHub (and what never does)

This repo is the **skeleton**: skills, blank templates, rules, and the summary script. It's how the kit moves between computers and accounts.

Your **actual deals** (pipeline, opportunity records, call notes, transcripts, buyer quotes) live only in the claude.ai Project on whichever account you're using (`opps/` docs). On your work account, they live in your work Project and never come back here.

Guards:
- The skills are instructed never to write deal data to the repo.
- `.gitignore` excludes `opps/`, `data/`, and root-level pipeline files.
- A pre-commit hook blocks commits that contain deal folders or filled-in pipeline rows. Turn it on in each new clone: `git config core.hooksPath .githooks`.
