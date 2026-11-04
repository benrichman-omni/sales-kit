---
name: call-follow-up
description: Turns a call (pulled from Fathom, or pasted notes/transcript) into a buyer-facing recap email, internal notes, MEDDPICC updates, and proposed Salesforce updates. Use when the user says "recap this call", "write the follow-up", "follow up on my {account} call", "here are my notes from", pastes a transcript or a Fathom link/summary email, or says "update the deal after my call with".
---

# Call Follow-up

## Input

**Default source: Fathom.** Ben records every call in Fathom. When he names a call ("my Acme call", "today's demo"), find it with the Fathom connector rather than asking him to paste:
- `list_meetings` with `recorded_by: ["ben.richman@omni.co"]` and a date filter; or `search_meetings` / `find_relevant_meetings` by account or attendee; a pasted fathom.video link → `get_recording_by_url`.
- Then `get_meeting_summary` and `get_meeting_transcript` (pass the url for timestamped links). Quote buyers only from the transcript, never from memory or the summary's paraphrase.
- Fathom also returns teammates' calls. Only treat a call as Ben's deal if Ben was on it or he says so.

Also accept rough notes, a pasted transcript, or the Fathom summary email. If the input is thin, ask at most two questions (e.g., "What did they agree to as next step?"); otherwise work with what's there and flag gaps.

## Produce four things

### 1. Buyer recap email (send-ready draft)

Load `${CLAUDE_PLUGIN_ROOT}/skills/sales-playbook/references/voice.md`.

- Subject: short, specific to the meeting.
- Open with their words: restate the problem and impact in the buyer's own language (this is the most persuasive part of a recap — it shows you listened and becomes forwardable internally).
- Brief prose on what you covered and what resonated.
- **Next steps** as bullets: owner, action, date — both sides' commitments.
- Close with the single most important next meeting and its date.
- No new pitching in the recap.

### 2. Internal notes (for CRM / the user's records)

Bulleted, factual: attendees and roles, what was learned, quotes worth saving (short), objections raised, competitive mentions, sentiment per stakeholder, risks.

### 3. MEDDPICC update

Load `methodology.md`. Table of all eight elements: what's now known (with evidence from the call), score 0–3, change since last update, and the biggest remaining gap. End with the one question that most needs answering next meeting.

### 4. Salesforce + notes update (via `deal-tracker`)

- **Salesforce (system of record):** propose the Opportunity changes as a before → after diff: `StageName`, `CloseDate`, `NextStep` + `Next_Step_Date__c`, and the MEDDPICC text fields (`Metrics__c`, `Economic_Buyer__c`, `Decision_Criteria__c`, `Decision_Process__c`, `Identified_Pain__c`, `Competitors__c`), plus discovery fields (`Use_Case__c`, `Data_Tools_In_Use__c`, `Database__c`, `Transformation_Tools__c`, `Scoping_Doc_Link__c`, `Positive_Feedback__c`) and contact-role proposals (Champion / Economic Buyer). Write only after Ben approves, following the audit protocol in `deal-tracker/references/salesforce.md`. Never touch `iARR__c` (calculated from the quote).
- **Local notes** (`~/sales-kit-private/opps/<account-slug>.md`): add a call-log entry (date, type, attendees, Fathom link, what was learned, objections, agreed next steps), the best short verbatim buyer quotes, champion-testing evidence and paper-process notes, and the 0–3 MEDDPICC scores.
- If no Opportunity exists yet, say so and offer to create one (with approval). Don't create it silently.
- After a POC kickoff or trial call, if there's no customer Slack channel yet (Teams for Microsoft shops), remind Ben to set one up.

## Rules

- Attribute commitments precisely — never put words in the buyer's mouth that the notes don't support.
- If the transcript shows the buyer said something that conflicts with what's in the tracker (timeline, budget, decision maker), call it out explicitly at the top.
- Don't send the recap. Save it as a Gmail draft (create_draft, addressed to the external attendees from the Fathom invite list) when asked or when running in the evening sweep.
