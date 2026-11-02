---
name: deal-tracker
description: Ben's opportunity management system — Claude keeps the pipeline and one record per opportunity, takes in quick updates, call notes, and call-recording transcripts, keeps MEDDPICC and next steps current, flags what needs attention, and reports on the pipeline. Use when the user says "add a deal / new opp", "update {deal}", "log this", gives any deal update in passing ("Acme pushed to Jan"), pastes call notes or a transcript, uploads a recording summary, or asks "what's in my pipeline", "what needs attention", "where are we with {account}", "show my deals", or "pipeline dashboard".
---

# Deal Tracker — Opportunity Management

Claude is the keeper of Ben's pipeline. Ben feeds it updates, notes, and call recordings; Claude files everything, keeps each opportunity current, and tells him what needs attention. Ben should never have to edit the tracker by hand.

## Data stays private — never in the repo

Deal data is confidential customer information. **Never write opportunity data to the plugin repo, GitHub, or any shared location.** The plugin holds only the instructions and templates in this folder.

## Where the data lives

Resolve once per session, in this order:

1. **The attached claude.ai Project** (preferred). If the session has the Projects tool, all records live there as Project docs under `opps/`. They persist across chats and devices, and only Ben can see them.
2. **A CRM connector**, once Omni's CRM is connected: the CRM is the system of record for standard fields (stage, amount, close date); the Project records stay the working layer for notes, MEDDPICC, call history, and Claude's analysis. Never write to the CRM without Ben's approval of the specific change.
3. **No Project available** (e.g., a session started outside the Project): say so, do the analysis, and hand Ben the exact updates to apply next time he's in the Project. Don't create a scattered copy somewhere else.

## Record structure (in the Project)

| Doc | Purpose |
|---|---|
| `opps/pipeline.md` | Master table: one row per opportunity — the at-a-glance view. Columns in `references/schema.md`. |
| `opps/<account-slug>.md` | One record per opportunity from `references/opp-template.md`: snapshot, contacts, MEDDPICC with evidence, next steps, risks, call log, notes. |
| `opps/activity-log.md` | Append-only log: `date · account · type · one-line summary`. |
| `opps/closed/<account-slug>.md` | Closed won/lost records moved here, with outcome and reasons. |

The pipeline row and the opp record must always agree. Update both in the same turn.

## Intake — how updates come in

Accept anything and figure out where it goes. Ben shouldn't have to format updates.

| Input | What to do |
|---|---|
| **Quick update** ("Acme pushed to Jan, EB is Dana Lee") | Parse into field changes. Apply to the record and pipeline row. Log it. |
| **Call notes** (rough bullets) | Run the `call-follow-up` flow: recap email draft, internal notes into the record's call log, MEDDPICC rescore, next steps, pipeline update. |
| **Call recording transcript or summary** (Gong, Chorus, Zoom, Fathom, Granola, etc., pasted, uploaded, or pulled from a connected tool) | Same as call notes, plus extract short verbatim buyer quotes for pain, metrics, decision criteria, and objections into the record (these are the most valuable evidence). Note the recording link/ID in the call log if available. |
| **Email thread** (pasted or from a connected inbox) | Pull out commitments, dates, new stakeholders, and objections. Update the record. Offer `email-reply` if a response is owed. |
| **New opportunity** | Create the record from the template and add a pipeline row. Fill what's known; mark everything else unknown, not guessed. Offer an `account-research` brief to seed it. |
| **"Find my recordings"** | If a call-recording connector is available, search it for calls with the account since the last logged call, then process each. If none is connected, say which tool it would take (once Omni's recorder is known) and ask Ben to paste or upload instead. |

### Rules for every update

1. **Read before writing.** Always `project_read` the current record and pipeline before changing them. Never rebuild a record from memory.
2. **Show the diff.** Before saving, show a compact before → after of the fields that changed (stage, amount, close date, forecast, next step, MEDDPICC scores, contacts). For routine updates, save right after showing it. Ask first only when the update conflicts with what's recorded (e.g., notes say budget isn't approved but MEDDPICC says it's confirmed), or the change is drastic (closing a deal, deleting information).
3. **Evidence, not optimism.** MEDDPICC scores only go up on buyer-stated evidence, and the evidence line says who said it and when.
4. **Flag contradictions** between new input and the record at the top of the reply.
5. **Always end with the next step.** Every open opp must have a specific next step with a date. If an update leaves none, ask for it or propose one.
6. Update `last_updated`, recompute the MEDDPICC total, and append to the activity log on every change.
7. Never delete an opportunity. Closed deals move to `opps/closed/` with outcome and reasons, and their pipeline row moves to the "Closed" section.

## Reporting

- **"Where are we with {account}?"** — 5-line status: stage/forecast/amount/close date, last touch, next step, biggest MEDDPICC gap, top risk.
- **"What needs attention?"** — deals where the next step is overdue or due within 2 days; deals with no next step; close date passed; closing in ≤30 days with paper process < 2; no update in 14+ days; Commit without a confirmed EB and champion (scores < 2). Rank by amount × urgency, with the one action for each.
- **Pipeline summary** — totals by stage and forecast category, coverage vs. quota if known, stale deals, upcoming closes. For the numbers, save `opps/pipeline.md` locally and run `scripts/pipeline_summary.py <file>` (it reads the markdown table or a CSV) rather than adding by hand.
- **Dashboard** — when asked for a visual, build a private pipeline dashboard from the data. Never publish deal data anywhere Ben hasn't explicitly chosen.
- **Forecast or 1:1 prep** — hand off to `deal-review`.

## Setup (first use in a Project)

If `opps/pipeline.md` doesn't exist, create the `opps/` docs from `references/pipeline-template.md` and `references/opp-template.md`, and an empty `opps/activity-log.md`. Tell Ben in one line that the tracker is ready and how to feed it.
