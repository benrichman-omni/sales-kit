---
name: outbound-prospecting
description: Writes personalized outbound prospecting — cold emails, multi-touch sequences, LinkedIn connection notes and messages, call openers, and voicemail scripts — in Ben's voice. Use when the user says "write a cold email to", "build a sequence for", "prospect into {company}", "LinkedIn message for", "cold call script", "voicemail", "multi-thread {account}", or asks to rewrite outbound copy.
---

# Outbound Prospecting

## Before writing

1. Load `${CLAUDE_PLUGIN_ROOT}/skills/sales-playbook/references/voice.md` — mandatory.
2. Load `company-context.md` for personas and value pillars. Load `competitors.md` if an incumbent tool is known.
3. Get the inputs. If an account brief exists in the conversation, use it. Otherwise collect the minimum: company, person (name/title), and one real, specific observation. If there's no observation, do a quick research pass (2–4 searches: recent news, the person's role/tenure, a data job posting) before writing. Never write a cold email built on nothing but their title.

## Single cold email

Produce **two variants** with genuinely different angles (e.g., trigger-led vs. insight-led), each with a subject line. Follow the structure in `voice.md`: specific observation → tension/cost → credible point of view → low-friction, interest-based ask. 50–90 words.

After the drafts, add one line on which variant you'd send and why.

## Sequence

Default sequence for enterprise and upper mid-market (adjust if the user specifies). For SMB and lower mid-market, compress to 5 steps over ~10 days: drop the second LinkedIn touch and the day-17 call.

| Step | Day | Channel | Purpose |
|---|---|---|---|
| 1 | 1 | Email | Lead angle |
| 2 | 1 | LinkedIn connect | No pitch; short, human note (under 200 chars) or blank |
| 3 | 3 | Call + voicemail | Reference the email; 20-second voicemail |
| 4 | 5 | Email (reply to thread) | New angle or proof point, 25–50 words |
| 5 | 9 | LinkedIn message | Share something useful (insight, relevant content) |
| 6 | 12 | Email | Different persona angle or customer story |
| 7 | 17 | Call | Opener focused on their likely pain |
| 8 | 21 | Email | Breakup — low-pressure, leave door open, no guilt |

Every step must earn its place with new information or a new angle. No "bumping this to the top of your inbox."

Output as a table (step, day, channel) followed by the full copy for each step. If the user will load it into a sequencing tool, also offer a CSV with columns: step, day, channel, subject, body.

## Multi-threading

When asked to multi-thread an account, write a coordinated set: one opener per persona (economic buyer, champion, technical evaluator, business user), each tailored to what that persona cares about, with consistent underlying narrative. Note sending order and spacing so contacts at the same company don't get identical-feeling emails the same day.

## Call openers & voicemails

- Opener: permission-based or problem-based, 2–3 sentences, then a single question that invites them to describe their current state.
- Voicemail: under 20 seconds spoken (~50 words). Name, company once, one specific reason, "I'll send a note too." No callback number recited twice.
- Include 3 likely objections with short, non-defensive responses.

## Self-check before returning

- Would this make sense if sent to a different company? If yes, it's not specific enough — rewrite.
- Any banned words from `voice.md`? Remove.
- Any product claim not in `company-context.md`? Replace with `[VERIFY: ...]`.
- One ask only.

Do not send anything. If an email connector is available, offer to save drafts, and only create drafts after the user says yes.
