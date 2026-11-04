# Salesforce at Omni — field map and write protocol

Salesforce is the system of record for Ben's opportunities. Learned from the org schema on 2026-11-03; re-check with `getObjectSchema` if a field errors.

Ben: Account Executive, Commercial segment (Salesforce `Segment__c`: SMB ≤100, Commercial ≤500, Enterprise >500 employees). User Id `005UP00000LYc5BYAT`. Manager: Reed von Gal, Manager, Commercial Sales.

## Opportunity stages (StageName)

`1 - Sales Ready` / `1 - Strategy` → `2 - Pre-Qual` → `3 - Qualified` → `4 - Trial` → `5 - Trial Positive` → `6 - Negotiate` → `7 - Closed Won` · `Closed Lost`. (`6.5 - Out Clause` exists but is rare.) Forecast categories: Pipeline, Best Case, Commit, Closed, Omitted.

At Omni, forecast category follows stage and is not set independently. The real forecast is the Kaizen sheet (`sales-playbook/references/methodology.md`).

**Stage gates:** full table in `methodology.md`. Before proposing any stage change, query the gate fields for the target stage and list what's missing. A move that would fail a hard gate gets proposed as "blocked by {fields}", not written.

| Into stage | Hard gates to check |
|---|---|
| 2 - Pre-Qual | `Lead_Solutions_Engineer__c`. `Omni_Exec_Sponsor__c` is not required broadly: most opps at Stage 2+ have it blank (checked 2026-11-04). Set it only when an exec is actually involved; ask Reed if a save errors |
| 4 - Trial | Primary Quote synced (`SyncedQuoteId` not null) with OpportunityLineItems; Instance = `Org_Name__c` (the customer's Omni org name, e.g. "pensionbee"; inferred, confirm on first error); OpportunityContactRole with Role = `Champion` and Role = `Economic Buyer` |
| 5 - Trial Positive | `Roadmap_Session_Completed__c`, `Roadmap_Session_Date__c`, `Roadmap_Omni_Session_Sponsor__c`, `Omni_Exec_Sponsor__c`. Enforcement looks partial: most new-business opps reaching Stage 5+ in the last 120 days have Roadmap Completed = false. Treat it as expected, and ask Reed when it applies |
| 7 - Closed Won | `Billing_Email__c`, quote synced + products, Champion + EB roles, signed PDF uploaded via the close-opp window (close date within 1 business day of signature) |
| Closed Lost | `Lost_Reason__c` (+ `Lost_Description__c`, competitor fields, Account follow-up date if Timing) |

## Field map (Opportunity)

| Kit concept | Salesforce field | Notes |
|---|---|---|
| Stage | `StageName` | Picklist above |
| Close date | `CloseDate` | |
| Amount for quota | `iARR__c` | **Read-only.** Calculated from the synced quote. To change it, the quote changes; never try to write it. `Amount`, `Stretch_iARR__c` also exist. |
| Forecast | `ForecastCategoryName`, `Forecast__c` | |
| Next step | `NextStep` (255 chars) + `Next_Step_Date__c` (date) | Always set both |
| Metrics | `Metrics__c` (1,000) | |
| Economic buyer | `Economic_Buyer__c` (1,000) | Name, title, evidence |
| Decision criteria | `Decision_Criteria__c` (5,000) | |
| Decision process | `Decision_Process__c` (10,000) | |
| Identify pain | `Identified_Pain__c` | |
| Competition | `Competitors__c` | Picklist; read valid values from schema before writing. `PoC_Competitors__c` for trial competitors |
| Champion | OpportunityContactRole, Role = `Champion` | Hard gate at Stage 4 and Closed Won. Evidence of testing goes in the notes file. A "Champion left" flag also exists |
| Economic buyer (role) | OpportunityContactRole, Role = `Economic Buyer` | The stage guide calls it "Executive Buyer." The picklist value is `Economic Buyer`. Keep `Economic_Buyer__c` text in sync. Other roles in use: Influencer, Executive Sponsor, Business User, Technical Decision Maker, Other |
| Instance | `Org_Name__c` | The customer's Omni org name. Inferred as the "Instance" gate |
| Timeline, Technical win | — | No field exists. Capture timeline in `Decision_Process__c` and the technical win in `Positive_Feedback__c` + notes |
| Paper process | — | Notes file + `Decision_Process__c` |
| Pipeline channel | `Pipeline_Channel__c` | Inbound / Outbound / Channel. Baseline on every save. Channel deals also need Referring Partner + Referring Contact |
| Lead SE / exec sponsor | `Lead_Solutions_Engineer__c`, `Omni_Exec_Sponsor__c` | |
| Use case / tech stack | `Use_Case__c`, `Data_Tools_In_Use__c`, `Database__c`, `Transformation_Tools__c` | Stage 3 exit criteria; fill from discovery |
| POC scope | `Scoping_Doc_Link__c` | Link to agreed success criteria |
| Roadmap session | `Roadmap_Session_Completed__c`, `Roadmap_Session_Date__c`, `Roadmap_Omni_Session_Sponsor__c` | Stage 5 hard gate |
| Technical win support | `Positive_Feedback__c` | |
| Billing | `Billing_Email__c` | Closed Won hard gate |
| Loss | `Lost_Reason__c`, `Lost_Description__c`, `Competitor_Chosen__c`, `Competitor_Existing_Solution__c`, `Competitor_New_Solution__c` | |
| Audit | `Claude_Audit_Log__c` (131,072) | Required on every write; see below |

Account: `Type` (Prospect, Customer, Partner, Competitor, Prospect - Not Converted), `OwnerId`, `NumberOfEmployees`.

All field names above were confirmed against the Opportunity schema on 2026-11-04. `Data_Tools_In_Use_OLD__c` and `PoC_Competitors_old__c` are legacy fields; don't write them.

## Useful queries

- Gate check for one opp: `SELECT Id, StageName, Pipeline_Channel__c, Lead_Solutions_Engineer__c, Omni_Exec_Sponsor__c, Use_Case__c, Identified_Pain__c, SyncedQuoteId, Scoping_Doc_Link__c, Roadmap_Session_Completed__c, Roadmap_Session_Date__c, Org_Name__c, Billing_Email__c, (SELECT Role, Contact.Name FROM OpportunityContactRoles) FROM Opportunity WHERE Id = '{id}'`

- Ben's open pipeline: `SELECT Id, Name, Account.Name, StageName, CloseDate, iARR__c, ForecastCategoryName, NextStep, Next_Step_Date__c, LastModifiedDate FROM Opportunity WHERE OwnerId = '005UP00000LYc5BYAT' AND IsClosed = false ORDER BY CloseDate`
- Account check (ownership, customer status, history): `SELECT Id, Name, Type, Owner.Name, OwnerId, NumberOfEmployees, (SELECT StageName, CloseDate, Owner.Name FROM Opportunities ORDER BY CreatedDate DESC LIMIT 3) FROM Account WHERE Name LIKE '{name}%' LIMIT 5`

## Write protocol (mandatory — Omni org policy)

Applies to every write to Account, Opportunity, Lead, Contact, Campaign, CampaignMember, or Partner_Introduction__c, by any method.

1. **Approval first.** Show Ben a compact before → after diff of every field and wait for his OK. Never write during unattended/scheduled runs; queue the proposal instead.
2. **Read the current values**, including `Claude_Audit_Log__c`, of each target record right before writing.
3. **Compose the audit entry** in exactly this format, one `Changed:` line per field:

   ```
   [YYYY-MM-DD HH:MM PT] | Ben Richman (ben.richman@omni.co) | Claude MCP
   Prompt: {1–2 sentence summary of Ben's request}
   Changed: {FieldApiName: OldValue → NewValue}
   Rationale: {context from Ben, or "not provided"}
   ---
   ```

   CampaignMember adds: `Changed: Status: [created] → {Status}`; deletes: `Changed: Status: {Status} → [deleted]`. If an old value couldn't be read first, write `OldValue: not captured`.
4. **Prepend** the entry to the existing log (newest on top). If the result exceeds 131,072 characters, trim the oldest entries from the bottom. Never overwrite existing entries.
5. **One call:** write `Claude_Audit_Log__c` in the same update as the target fields, never separately.
6. Never skip the entry because a change seems minor. Never create, reassign, or touch records owned by other reps without Ben explicitly asking.
