---
name: call-follow-up
description: Turns call notes or a transcript into a buyer-facing recap email, internal notes, MEDDPICC updates, and next steps — and updates the deal tracker. Use when the user says "recap this call", "write the follow-up", "here are my notes from", pastes a transcript (Gong, Zoom, Granola, etc.), or says "update the deal after my call with".
---

# Call Follow-up

## Input

Accept anything: rough bullet notes, a full transcript, voice-memo text, or a summary from a recording tool. If the input is thin, ask at most two questions (e.g., "What did they agree to as next step?") — otherwise work with what's there and flag gaps.

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

### 4. Deal tracker update

File it in the opportunity's record via the `deal-tracker` skill: add a call-log entry (date, type, attendees, recording link if any, what was learned, objections, agreed next steps), save the best short buyer quotes, rescore MEDDPICC with evidence, and update stage, next step + date, close date, amount, and risks in both the record and the pipeline table. Show the before → after diff and save it (ask first only on a conflict or a drastic change). If no record exists yet, create one.

## Rules

- Attribute commitments precisely — never put words in the buyer's mouth that the notes don't support.
- If the transcript shows the buyer said something that conflicts with what's in the tracker (timeline, budget, decision maker), call it out explicitly at the top.
- Don't send the recap. If an email connector is available, offer to save it as a draft.
