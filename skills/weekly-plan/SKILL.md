---
name: weekly-plan
description: Builds Ben's weekly sales operating plan and Friday review — pipeline priorities, deals needing action, meetings to prep, prospecting targets, and a scorecard of activity vs. goals. Use when the user says "plan my week", "Monday plan", "what should I focus on this week", "Friday review", "weekly recap for my manager", or "how did my week go".
---

# Weekly Plan & Review

## Monday plan

1. Pull the deal tracker (via `deal-tracker`) and run its "what needs attention" check.
2. If a calendar connector is available, list this week's external meetings; flag any without prep.
3. Check connected email for buyer threads awaiting Ben's reply for 2+ business days.
4. Produce:
   - **The one thing:** the single highest-leverage outcome for the week, in a sentence.
   - **Deals to move (top 3–5):** deal, the specific action, the day to do it.
   - **Meetings this week:** table — day, account, type, prep status; offer `meeting-prep` for each.
   - **Replies owed:** list with suggested priority.
   - **Prospecting block:** target accounts/personas for the week and a number (default 25 new personalized touches/week until Ben sets his own target), with time blocks suggested on the calendar if a calendar connector is available — only create events after the user approves.
   - **Ramp tasks** (first 90 days): pull open items from the `ramp-plan` skill if one is in progress.

## Friday review

- What moved: stage changes, new deals, closed deals, amount changes (from Salesforce: Ben's Opportunities with `LastModifiedDate` this week, plus `opps/activity-log.md` in `~/sales-kit-private`); calls held this week from Fathom (`recorded_by` Ben).
- Activity vs. goal: meetings held, new touches, new opportunities.
- What slipped and why (honest, brief).
- Next week's first move.
- Optional: a short manager update in Ben's voice (prose, 5–8 sentences, leads with numbers, names risks plainly).

Keep both outputs to one phone screen where possible.
