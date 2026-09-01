# Agentic Security Control Stack — TEMPLATE
Agent: ____________ · Owner: ____________ · Autonomy tier: ____

## Layer 1 — Identity
Agent identity: ____________ (must NOT be a shared human or generic service account)
Scopes granted: ____________ · Credential lifetime: ______ · Where credentials are held: ______
How each action stays attributable to the accountable human:

## Layer 2 — Guardrails (model boundary)
| Direction | Check | Action on hit |
|---|---|---|
| Input | PII detection | |
| Input | Jailbreak / injection pattern | |
| Output | PII redaction | |
| Output | Unsafe content | |
| Output | Grounding / citation check | |
**Record what these guardrails CANNOT do:**

## Layer 3 — Permission ladder
(attach your completed agent-tool-catalogue.csv — every irreversible or external-communication
tool must be ask or deny)

### Three enforceable deny rules
1. DENY when: ____________________________________________
2. DENY when: ____________________________________________
3. DENY when: ____________________________________________

## Layer 4 — Sandbox / blast radius
Filesystem the agent may touch: ____________
Network destinations allowed: ____________
Credentials the agent never holds directly: ____________

## Layer 5 — Human approval
| Action | Approver | What the approver sees | SLA |
|---|---|---|---|
| | | | |
**Approval fatigue:** above ____ approvals/day this gate stops being a control. Mitigation:

## OWASP ASI coverage check
| ASI | Covered by which layer? | Gap? |
|---|---|---|
| ASI01 Goal hijack | | |
| ASI02 Tool misuse | | |
| ASI03 Identity & authz | | |
| ASI06 Memory poisoning | | |
| ASI07 RAG poisoning | | |
| ASI08 Excessive agency | | |

## Residual risk — name TWO attack paths that survive all five layers
1. ____________________ → compensating detection: ____________________
2. ____________________ → compensating detection: ____________________
