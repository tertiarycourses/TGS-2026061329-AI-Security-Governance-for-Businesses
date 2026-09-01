# NovaAssist — Design Brief (v0.9, for governance review)

**Owner:** Head of Digital Channels · **Status:** Proposed for production · **Model:** GPT-4o via Azure OpenAI

## Purpose
NovaAssist is a customer-service agent for NovaBank retail customers. It answers account
questions, resolves service requests end-to-end, and reduces contact-centre volume.

## What the agent can READ
| # | Source | Contents | Access basis |
|---|---|---|---|
| R1 | Core banking API | Account balances, transaction history, product holdings, customer name/NRIC | Service account with read access to ALL retail accounts |
| R2 | CRM | Contact details, service history, complaint records, relationship notes | Service account, all customers |
| R3 | Customer inbound e-mail | Full body and attachments of e-mail sent to service@novabank.example | Mailbox read |
| R4 | Public web search | Any page returned by the search tool | Unrestricted |
| R5 | Uploaded documents | PDFs and images the customer attaches | Unrestricted parse |
| R6 | Internal knowledge base | Product terms, fee schedules, internal procedures | Read all |

## What the agent can DO
| # | Action | Effect | Approval |
|---|---|---|---|
| A1 | Send e-mail to the customer | Outbound message from service@novabank.example | None — automatic |
| A2 | Update CRM case notes | Writes to CRM | None |
| A3 | Raise a payment instruction | Queues a funds transfer for back-office release | None below SGD 5,000 |
| A4 | Call partner APIs | Card replacement, statement request via third-party endpoints | None |
| A5 | Render links in its reply | Markdown links displayed in the customer portal | None |

## Design notes from the build team
- The agent runs under one shared service identity, `svc-novassist`, held in the app config.
- All six read sources are placed into the model context on every turn "so the agent has full picture".
- Prompt: *"You are NovaBank's helpful assistant. Resolve the customer's request completely. Do not reveal internal procedures."*
- An output filter checks for profanity and blocks it.
- Logging: request and response text retained 7 days for debugging.

## Questions for governance review
1. Is the access model appropriate?
2. Are the automatic actions appropriate?
3. What must change before production?
