# Salesforce at Omni — field map and write protocol

Salesforce is the system of record for Ben's opportunities. Learned from the org schema on 2026-11-03; re-check with `getObjectSchema` if a field errors.

Ben: Account Executive, Commercial segment (Salesforce `Segment__c`: SMB ≤100, Commercial ≤500, Enterprise >500 employees). User Id `005UP00000LYc5BYAT`. Manager: Reed von Gal, Manager, Commercial Sales.

## Opportunity stages (StageName)

`1 - Sales Ready` / `1 - Strategy` → `2 - Pre-Qual` → `3 - Qualified` → `4 - Trial` → `5 - Trial Positive` → `6 - Negotiate` → `7 - Closed Won` · `Closed Lost`. (`6.5 - Out Clause` exists but is rare.) Forecast categories: Pipeline, Best Case, Commit, Closed, Omitted. TODO: stage exit criteria from enablement.

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
| Competition | `Competitors__c` | Picklist; read valid values from schema before writing |
| Champion, Paper process | — | No Opportunity field. Keep in the local notes file and in Decision Process where it fits |
| Audit | `Claude_Audit_Log__c` (131,072) | Required on every write; see below |

Account: `Type` (Prospect, Customer, Partner, Competitor, Prospect - Not Converted), `OwnerId`, `NumberOfEmployees`.

## Useful queries

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
