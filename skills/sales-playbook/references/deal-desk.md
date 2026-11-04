# Deal Desk, Legal & Security — Omni (INTERNAL)

Source: the Common Paper guide in the AE Operational Playbook, which is the source of record and may change. Check it before papering a deal.

## Who to go to

| Need | Contact / channel |
|---|---|
| Pricing or signer questions, non-standard deals | #deal-desk |
| Customer pushes on Standard Terms, or wants us to sign their trial paper | #legal-review |
| Trial CSA template status | #proj-csa-updates / Torsten |
| Security reviews | Craig. The **Security Center** (Google Drive) has SOC audits and security assessments |
| Professional services scoping | Joe Bertha (the PS x Sales process map shows when to engage PS in presales) |
| Legal generally | Run lean: drafted with AI, reviewed by Colin (CEO) |

## Common Paper: new business flow

The Salesforce quote is the **Fee Attachment**. The Common Paper Order Form is the **cover page**. They are separate documents that get joined at signing.

1. In app.commonpaper.com, create the agreement from **"[USE THIS] CSA Custom Terms (as of 4.20.26)"**.
2. Under "Keep informed," add the champion or dev contact if they want visibility.
3. Set **Order Date** to the day the contract starts.
4. In **Cloud Service Fees**, choose "Add as attachment" and upload the SFDC PDF order form.
5. **Uncheck Professional Services** if no PS hours were sold.
6. Save the draft, set the Omni signer, and route for customer signature.
7. After signing, download the PDF and upload it in the SFDC "close opp" window. The close date must be within 1 business day of the signature date.

**Signer routing:**
- **Colin Zima:** all new business, and non-standard renewals (>10% increase or new terms).
- **David Carlile:** flat renewals and renewals with less than a 10% increase.
- If unsure, ask #deal-desk. Don't pick the signer arbitrarily.

## Order Form rules

- **Never edit the Standard Terms.** Everything customizable lives in the Order Form or Fee Attachment.
- **Use Limitations** (the section that changes most often):
  - The default is internal BI only.
  - For affiliate access and/or embed, replace it with the pre-approved drop-in language. One block covers both.
- **Excess use / overage:** standard mechanics. Change it only to grant grace periods, using the drop-in sheet (see Torsten's Loom on overdeployment).
- **Payment Process:** don't edit. SFDC is the single source of truth.
- **SLA:** changes only through a legal redline approval.
- **Auto-renewal notice period:** change it only if the customer negotiated it.
- **Redline and paper thresholds:** see `pricing.md` (Omni paper <$50k, customer paper >$120k, SLAs >$75k).

## Trial agreements

- The dedicated POC template is marked [DO NOT USE]. Use the standard CSA template and work with Deal Desk to tailor it for a trial.
- **Confirm status in #proj-csa-updates first.** The trial template is the biggest gap in the process.
- If a prospect pushes its own paper for the trial, don't sign until it's been posted in #legal-review.

## NDAs

Handled in Common Paper. A Roam video in the playbook walks through it.

## Procurement

Rare in Commercial, but it happens. Reference calls: AG1 procurement rounds 1 and 2 (Gold Standard Library).
