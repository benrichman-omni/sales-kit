---
name: deal-tracker
description: Ben's opportunity management system on top of Salesforce — Claude reads and (with approval) updates his Salesforce opportunities, keeps private call notes and MEDDPICC evidence per opp, takes in quick updates, call notes, and call-recording transcripts, keeps MEDDPICC and next steps current, flags what needs attention, and reports on the pipeline. Use when the user says "add a deal / new opp", "update {deal}", "log this", gives any deal update in passing ("Acme pushed to Jan"), pastes call notes or a transcript, uploads a recording summary, or asks "what's in my pipeline", "what needs attention", "where are we with {account}", "show my deals", or "pipeline dashboard".
---

# Deal Tracker — Opportunity Management

Claude is the keeper of Ben's pipeline. Ben feeds it updates, notes, and call recordings; Claude files everything, keeps each opportunity current, and tells him what needs attention. Ben should never have to edit the tracker by hand.

## Data stays private — never in the repo

Deal data is confidential customer information. **Never write opportunity data to the plugin repo, GitHub, or any shared location.** The plugin holds only the instructions and templates in this folder.

## Where the data lives

Two layers:

1. **Salesforce: the system of record.** Stage, close date, amount (`iARR__c`, read-only), forecast, next step + date, and the MEDDPICC text fields all live on the Opportunity. Read the pipeline from Salesforce, never from memory or a local copy. **Load `references/salesforce.md` before any Salesforce read or write.** It has the field map, stages, queries, and the mandatory approval + audit-log protocol.
2. **The private notes layer: `~/sales-kit-private`** (Ben works in Cowork; request access with `request_cowork_directory` if it isn't connected). It holds what Salesforce has no place for: call log with Fathom links, verbatim buyer quotes, champion and paper-process notes, 0–3 MEDDPICC scores, Claude's analysis, and the queue of proposed Salesforce changes. It is outside the plugin repo on purpose: never move or copy it into `~/sales-kit` or any git repo. (If an attached claude.ai Project exists and no local folder does, use the same paths as Project docs.)

If Salesforce isn't connected, say so, do the analysis, and hand Ben the exact field changes to make. Don't build a shadow pipeline.

## Record structure (private notes layer)

| Doc | Purpose |
|---|---|
| `opps/<account-slug>.md` | One notes file per opportunity from `references/opp-template.md`: Salesforce Opportunity Id at the top, contacts, MEDDPICC scores with evidence, risks, call log, quotes. The snapshot fields mirror Salesforce and are refreshed from it on every read. |
| `opps/pending-sf-updates.md` | Queue of proposed Salesforce changes awaiting Ben's approval (written by the evening sweep and any unattended run). Clear an entry once it's applied or rejected. |
| `opps/activity-log.md` | Append-only log: `date · account · type · one-line summary`. |
| `opps/closed/<account-slug>.md` | Notes for closed won/lost deals, with outcome and reasons. |

`opps/pipeline.md` is no longer the source of truth. For a pipeline view, query Salesforce (see `references/salesforce.md`) and render it.

## Intake — how updates come in

Accept anything and figure out where it goes. Ben shouldn't have to format updates.

| Input | What to do |
|---|---|
| **Quick update** ("Acme pushed to Jan, EB is Dana Lee") | Parse into Salesforce field changes, show the diff, write on approval (audit protocol). Log it in the notes file. |
| **A Fathom call** (named by Ben, a fathom.video link, the Fathom summary email, or pasted notes) | Run the `call-follow-up` flow: Gmail recap draft, call log + quotes in the notes file, MEDDPICC rescore, proposed Salesforce diff. |
| **Email thread** (pasted or from Gmail) | Pull out commitments, dates, new stakeholders, and objections. Propose Salesforce changes and update notes. Offer `email-reply` if a response is owed. |
| **New opportunity** | Check Salesforce first: does the Account exist, who owns it, any open or recent opps? If it's another rep's account, stop and tell Ben. Otherwise propose the new Opportunity (Name, Account, StageName, CloseDate, NextStep + date) for approval, then create the notes file. Mark unknowns as unknown. Offer an `account-research` brief. |
| **"Apply pending Salesforce updates"** / "review the queue" | Read `opps/pending-sf-updates.md`, re-query each Opportunity (values may have changed since the proposal), show the refreshed diffs grouped by opp, and write the ones Ben approves (audit protocol). Remove applied or rejected entries from the queue. |
| **"Find my recordings"** | Fathom `list_meetings` with `recorded_by: ["ben.richman@omni.co"]` since the last logged call for the account (or `search_meetings` by account name), then process each with `call-follow-up`. |

### Rules for every update

1. **Read before writing.** Query the current Opportunity (including `Claude_Audit_Log__c`) and read the notes file before changing either. Never rebuild a record from memory.
2. **Show the diff, then wait.** Every Salesforce write needs Ben's OK on a before → after diff (stage, close date, forecast, next step + date, MEDDPICC fields, contacts). Batch related changes into one approval. Notes-file updates can be saved right after showing them.
3. **Audit every write.** Follow `references/salesforce.md` exactly: audit entry prepended to `Claude_Audit_Log__c` in the same update call. No exceptions.
4. **Unattended runs never write to Salesforce.** They append proposals to `opps/pending-sf-updates.md` and tell Ben.
5. **Evidence, not optimism.** MEDDPICC scores only go up on buyer-stated evidence, and the evidence line says who said it and when (cite the Fathom call).
6. **Flag contradictions** between new input and Salesforce at the top of the reply.
7. **Always end with the next step.** Every open opp must have `NextStep` and `Next_Step_Date__c`. If an update leaves none, propose one.
8. Never delete Salesforce records. Never touch records owned by other reps unless Ben explicitly asks. `iARR__c` is calculated from the quote, so never write it.

## Reporting

- **"Where are we with {account}?"** — 5-line status: stage/forecast/amount/close date, last touch, next step, biggest MEDDPICC gap, top risk.
- **"What needs attention?"** — from Salesforce plus the notes files: pending Salesforce proposals awaiting approval; deals where `Next_Step_Date__c` is overdue or due within 2 days; deals with no next step; close date passed; closing in ≤30 days with paper process < 2; no update in 14+ days; Commit without a confirmed EB and champion (scores < 2). Rank by amount × urgency, with the one action for each.
- **Pipeline summary** — query Ben's open Opportunities from Salesforce (query in `references/salesforce.md`): totals of `iARR__c` by stage and forecast category, coverage vs. quota if known, stale deals (`LastModifiedDate` 14+ days), upcoming closes. Compute totals with code, not by hand: save the query result as CSV and run `${CLAUDE_PLUGIN_ROOT}/skills/deal-tracker/scripts/pipeline_summary.py` on it if the columns fit, or a short pandas script otherwise.
- **Dashboard** — when asked for a visual, build a private pipeline dashboard from the data. Never publish deal data anywhere Ben hasn't explicitly chosen.
- **Forecast or 1:1 prep** — hand off to `deal-review`.

## Setup (first use)

If `~/sales-kit-private/opps/` doesn't exist, create it with an empty `activity-log.md` and `pending-sf-updates.md`. Create a notes file from `references/opp-template.md` the first time an opp gets activity. Tell Ben in one line that the tracker is ready and how to feed it.
