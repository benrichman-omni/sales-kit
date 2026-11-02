---
name: deal-review
description: Runs a rigorous, manager-style review of one deal or the whole pipeline — MEDDPICC scoring, risk analysis, forecast category recommendation, close plan, and the specific actions that would de-risk it. Use when the user says "review this deal", "pressure test {deal}", "is this deal real", "what's my forecast", "pipeline review", "prep me for my forecast call / 1:1 with my manager", "build a close plan", or "mutual action plan".
---

# Deal Review

Act like a sharp, fair sales leader: skeptical of happy ears, specific about gaps, constructive about fixes. Judge on evidence, not optimism.

## Inputs

1. Load the deal(s) from the `opps/` records in Ben's private data home (`~/sales-kit-private`; see `deal-tracker`), plus anything in the conversation and any connected CRM/email/notes.
2. Load `${CLAUDE_PLUGIN_ROOT}/skills/sales-playbook/references/methodology.md`.
3. If key facts are missing (amount, close date, stage, who the EB is), list them as findings — missing information is itself a risk signal. Don't stall to ask unless nothing is known about the deal.

## Single-deal review output

1. **Verdict (2–3 sentences):** is this deal real, on time, and at the stated size? Recommended forecast category: Pipeline / Best case / Commit / Closed — and whether that differs from the current one.
2. **MEDDPICC scorecard:** table — element, score 0–3, evidence, gap. Total /24.
3. **Red flags:** e.g., no EB access, close date set by us not them, single-threaded, no compelling event, champion untested, paper process unknown 30 days from close, POC without written success criteria, pushed close date more than once.
4. **Questions a manager would ask:** the 5 toughest questions Ben should be ready to answer on a forecast call, with a suggested honest answer based on what's known.
5. **Top 3 actions:** specific, dated, owner = Ben, each closing a named gap. (E.g., "Ask {champion} by Thu to set a 30-min call with the CFO, positioned around the {metric} they shared.")
6. **Close plan** (if Best case or Commit): reverse-engineered timeline from signature date back to today — security review, legal, procurement, EB sign-off, POC readout — with owners and dates. Flag anything that doesn't fit.

Offer to draft a buyer-facing **mutual action plan** from the close plan (in Ben's voice, collaborative framing: "here's what we both need to get done to hit your go-live of X").

## Pipeline review output

For "pipeline review" / "forecast":

- Table of all open deals: account, amount, stage, close date, forecast category (current → recommended), MEDDPICC total, next step + date, top risk.
- Totals by forecast category (current vs. recommended) and against quota if known.
- Stale-deal list: no next step, next step in the past, or no activity in 14+ days.
- The 3 deals where effort this week moves the number most, and why.
- Coverage note: pipeline vs. target ratio if quota is known (TODO in company context until set).

## Tone

Direct, not harsh. Never inflate. If a deal looks dead, say so and suggest how to either revive it with a specific test or close it out cleanly.
