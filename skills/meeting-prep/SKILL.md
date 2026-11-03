---
name: meeting-prep
description: Prepares Ben for a sales meeting — discovery calls, demos, exec meetings, technical deep-dives, POC kickoffs, negotiations — with attendee research, objectives, agenda, tailored questions, demo storyline, likely objections, and the next step to ask for. Use when the user says "prep me for my call with", "meeting prep", "I have a demo with", "what should I ask {person}", "brief me on tomorrow's meetings", or "build a demo story for".
---

# Meeting Prep

## Gather context

1. **Find the meeting.** If a calendar connector is available and the user didn't give details, look up the event (attendees, time, description). For "tomorrow's meetings", pull all external meetings for that day and prep each briefly.
2. **Pull history.** Check the conversation; the Salesforce Opportunity and Account (stage, MEDDPICC fields, next step, contacts); past Fathom calls with the account (`search_meetings` / `find_relevant_meetings`, including teammates' calls, with transcripts for exact quotes); Gmail threads; Google Calendar for the attendee list; and the notes file in `~/sales-kit-private/opps/<account>.md` (see `deal-tracker`) for prior interactions, open questions, and deal stage.
3. **Research attendees.** For each external attendee: title, tenure, background relevant to the meeting, likely persona and what they care about. Professional information only.
4. Load `sales-playbook` references: `methodology.md` always; `company-context.md` and `competitors.md` as needed; `voice.md` if drafting any buyer-facing text (agenda email, etc.).

## Identify the meeting type

Tailor the prep to: **Discovery**, **Demo**, **Executive / EB**, **Technical deep-dive**, **POC kickoff / readout**, **Negotiation / pricing**, **Renewal / expansion**. If unclear, infer from the invite and stage, and say what you assumed.

## Output: one-page brief

**{Company} — {meeting type} — {date/time}**

1. **Objective:** what a great outcome looks like in one sentence, plus the specific next step to ask for (with a date).
2. **Where we are:** stage, MEDDPICC gaps this meeting should close (name them), what happened last time.
3. **Who's in the room:** table — name, title, persona, what they care about, how to win them, risk (e.g., "possible detractor — owns current BI tool").
4. **Agenda (proposed):** timed, with ~5 minutes left for next steps.
5. **Questions to ask:** 6–10, ordered, mapped to the MEDDPICC gap or Gap Selling stage each one closes. Open-ended, one at a time, no leading.
6. **Demo storyline** (demo meetings only): a Resonate-style arc — their current state (the "what is") → the better future (the "what could be") → 3 moments in the product that bridge the gap, each tied to a pain they stated. Start with the outcome, not the login screen. Note what NOT to show.
7. **Likely objections:** 3–5 with short, consultative responses.
8. **Landmines:** competitive or political risks, things not to say.
9. **Follow-up plan:** what goes in the recap and who gets it.

Keep it scannable — Ben will read it 10 minutes before the call on his phone.

## Optional add-ons (offer, don't do by default)

- Pre-meeting agenda email to the buyer (in Ben's voice).
- Mutual action plan draft for later-stage deals.
- Talk track for the opening 2 minutes.
