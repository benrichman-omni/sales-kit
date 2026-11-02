---
name: sales-playbook
description: Ben's core sales operating context — company and product positioning, ideal customer profile, personas, competitors, sales methodology, and writing voice. Load this whenever drafting any customer-facing sales content (emails, sequences, talk tracks, recaps) or analyzing a deal, and whenever the user asks "what's our positioning", "who do we sell to", "how do we beat X", or "what's my voice".
---

# Sales Playbook (shared foundation)

This skill is the shared context every other skill in this plugin draws on. Load the relevant reference files before producing sales output so positioning, voice, and methodology stay consistent.

## Reference files

| File | Load when |
|------|-----------|
| `references/voice.md` | Writing anything a buyer will read |
| `references/company-context.md` | Positioning, product claims, ICP, personas, pricing questions |
| `references/competitors.md` | A competitor is named, or the buyer uses an incumbent tool |
| `references/methodology.md` | Qualifying, deal reviews, discovery, forecasting |

Paths are relative to this skill: `${CLAUDE_PLUGIN_ROOT}/skills/sales-playbook/references/`.

## Rules for using this context

1. Never invent product capabilities, customer logos, metrics, or pricing. If `company-context.md` doesn't cover a claim, either leave a clearly marked `[VERIFY: ...]` placeholder or ask the user.
2. Treat any line in a reference file marked `TODO` as unknown. Do not fill it with a guess in buyer-facing output.
3. When the user teaches something new about the company, product, a competitor, or their preferences, offer to add it to the right reference file so the plugin gets smarter over time. Show the exact line to be added before writing.
4. Voice rules in `voice.md` override generic "sales email best practices".
