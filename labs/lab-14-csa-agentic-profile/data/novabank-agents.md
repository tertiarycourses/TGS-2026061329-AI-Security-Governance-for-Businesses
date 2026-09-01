# NovaBank — The Agent Estate (five agents for tiering and registry)

## Agent 1 — NovaAssist (Customer Service)
Owner: Head of Digital Channels. Model: GPT-4o. **Can:** read all retail account and CRM data,
read inbound customer e-mail, search the web, parse uploaded documents, send e-mail, update CRM,
raise payments below SGD 5,000 without approval, call partner APIs.
**Human involvement:** none in the normal path. Runs 24/7. ~2,400 customer conversations/day.

## Agent 2 — Fraud Triage Agent
Owner: Head of Financial Crime. Model: GPT-4o + rules engine. **Can:** read transaction and
account data, read the fraud alert queue, enrich from a third-party sanctions API, **freeze a
customer account pending review**, assign the case to an analyst, close a false positive.
**Human involvement:** an analyst reviews closures weekly (after the fact). Freezes take effect
immediately. ~600 alerts/day, of which ~40 result in an automatic freeze.

## Agent 3 — IT Helpdesk Agent
Owner: Head of IT Service Delivery. Model: ServiceNow Now Assist. **Can:** read the staff
knowledge base and ticket history, answer staff questions, **reset a staff password**, create
and update tickets, install approved software to a staff laptop.
**Human involvement:** none for password resets. ~300 interactions/day.

## Agent 4 — Marketing Content Agent
Owner: Head of Retail Marketing. Model: Jasper. **Can:** read the product catalogue and brand
guidelines, generate campaign copy into a draft folder. Cannot publish. Cannot read customer data.
**Human involvement:** every output is reviewed by a marketing manager before use.
**Status: being retired** — replaced by an approved enterprise tool next month.

## Agent 5 — Reconciliation Agent (Pilot)
Owner: Head of Finance Operations. Model: GPT-4o-mini orchestrator. **Can:** read nostro account
statements and the general ledger, match transactions, and **delegate unmatched exceptions to a
sub-agent** ("ExceptionResolver") which can query the core banking API, draft a journal entry and
raise it for release. The orchestrator decides what the sub-agent is asked to do; nobody reviews
that instruction.
**Human involvement:** a finance officer releases journal entries above SGD 10,000 only.

---
## The CSA agentic extensions to apply
**GOVERN:** AG-GV.1 Autonomy Tier Classification · AG-GV.2 Delegation Accountability ·
AG-GV.3 Agent Lifecycle Registry
**MAP:** AG-MP.1 Tool Risk Classification · AG-MP.2 Action-Consequence Analysis ·
AG-MP.3 Multi-Agent Topology Risk
**MEASURE:** AG-MS.1 Agentic Behavioural Telemetry · AG-MS.2 Autonomy Calibration ·
AG-MS.3 Delegation Chain Monitoring
**MANAGE:** AG-MG.1 Agentic Incident Classification · AG-MG.2 Behavioural Drift Correction ·
AG-MG.3 Agent Decommissioning

## Autonomy tiers
| Tier | Description | Oversight obligation (you define) |
|---|---|---|
| Tier 1 | Supervised — proposes only, a human acts | |
| Tier 2 | Constrained — acts within a fixed allowlist | |
| Tier 3 | Broad autonomy with monitoring | |
| Tier 4 | Full autonomy | |

**Tier by capability, not by job title.** An agent described as "just a helpdesk assistant" that
can reset passwords is not Tier 1.
