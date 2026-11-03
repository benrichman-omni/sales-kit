# Pipeline Schema

The **pipeline table** (`opps/pipeline.md`, "Open" section) holds the at-a-glance fields. Everything else (contacts, MEDDPICC evidence, quotes, call log) lives in each opportunity's record (`opps/<account-slug>.md`, from `opp-template.md`).

| Column | Type | Allowed values / notes |
|---|---|---|
| deal_id | text | `{ACCOUNT-SLUG}-{YYYYMM}` (month created), unique |
| account | text | Company name |
| opportunity | text | e.g., "Platform – Analytics team", "Embedded" |
| amount | number | Annual contract value, no currency symbols; blank if unknown |
| stage | text | Omni Salesforce `StageName`: `1 - Sales Ready`, `1 - Strategy`, `2 - Pre-Qual`, `3 - Qualified`, `4 - Trial`, `5 - Trial Positive`, `6 - Negotiate`, `7 - Closed Won`, `Closed Lost` |
| forecast_category | text | `Pipeline`, `Best Case`, `Commit`, `Closed`, `Omitted` |
| close_date | date | YYYY-MM-DD |
| next_step | text | Specific action, never "follow up" |
| next_step_date | date | YYYY-MM-DD |
| meddpicc_total | 0–24 | Sum of the eight element scores in the record |
| meddpicc_e | 0–3 | Economic buyer score (shown for Commit checks) |
| meddpicc_c1 | 0–3 | Champion score (shown for Commit checks) |
| meddpicc_p | 0–3 | Paper process score (shown for late-stage checks) |
| top_risk | text | One short phrase |
| last_updated | date | YYYY-MM-DD |

MEDDPICC scoring: 0 unknown · 1 assumed or secondhand · 2 partially confirmed · 3 confirmed by the buyer with evidence.
