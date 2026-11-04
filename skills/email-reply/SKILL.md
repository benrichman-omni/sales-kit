---
name: email-reply
description: Drafts replies to buyer emails in Ben's voice — objections, pricing questions, "not now" / timing pushback, ghosting re-engagement, security or legal requests, scheduling, intros, and internal escalations. Use when the user pastes or references a buyer email and says "help me respond", "draft a reply", "how should I answer this", "they went dark", "they pushed back on price", or "write a follow-up".
---

# Email Reply

## Steps

1. **Get the thread.** Use the pasted text, or if an email connector is available and the user referenced a thread, fetch it. Read the whole thread, not just the last message.
2. **Diagnose before drafting.** In 1–3 lines, state what the buyer is actually saying underneath the words (e.g., "'Circle back next quarter' + no reason given = no urgency established, or champion lost internal support"), and what the reply needs to accomplish.
3. Load `${CLAUDE_PLUGIN_ROOT}/skills/sales-playbook/references/voice.md`. Load `company-context.md` / `competitors.md` / `methodology.md` if the reply touches product, competition, or deal process.
4. **Draft.** For high-stakes or ambiguous replies (pricing, objections, a deal at risk, conflict), give 2 variants that pursue different outcomes, each with a 2–4 word label (e.g., "Hold the line" vs. "Trade for commitment"). For routine replies (scheduling, sending materials, thank-yous), give one draft.
5. **Self-check:** shorter than or equal to their email unless more is truly needed; one ask; no defensive tone; no unverified claims (`[VERIFY: ...]`); no "just," no apologizing for following up.

## Playbook by situation

- **Price pushback:** don't discount in email. Acknowledge, re-anchor to the value/metrics they agreed to, ask a question that uncovers what's behind it (budget cycle, competitor quote, unclear ROI), propose a conversation. Never give up price without getting something (term, timing, scope, reference, signature date). Load `pricing.md` and trade in the elegant-negotiables order: services to $0 → Year-1 overdeployment with Year-2 true-up → platform fee → seats. Never add free months (they cut iARR). If the ask is beyond AE/RSD authority, draft a "let me see what I can do" reply and flag the approval needed to Ben.
- **"Not now" / timing:** test whether it's real. Ask what changes between now and then; offer something useful that keeps you relevant; agree on a specific re-engage date.
- **Competitor mention:** don't trash them. Ask what's driving the comparison, re-center on their decision criteria, offer a specific proof point.
- **Ghosting:** after two unanswered touches, change the format — a short, low-pressure, slightly humorous or candid note that makes it easy to say "not now." Give them an out; it often gets the reply.
- **Security / legal / procurement:** confirm receipt, set an owner and a date, route internally. Do not answer security questionnaire content from memory — route per `deal-desk.md` (Craig + the Security Center for security; #legal-review for Standard Terms changes or customer paper; never agree to sign the buyer's trial paper).
- **Feature request / "can it do X":** if `company-context.md` doesn't confirm it, don't claim it. Draft a reply that asks what they're trying to accomplish and promises a confirmed answer.
- **Intro to a new stakeholder:** thank the introducer briefly (move them to BCC), address the new person with something specific to their role.

## Sending

Never send. If an email connector is available, offer to save the draft to the thread, and only do it after the user says yes.
