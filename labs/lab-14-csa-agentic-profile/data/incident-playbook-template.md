# AG-MG.1 Agentic Incident Classification — Containment Playbooks

| Incident type | What it looks like | Detection signal | Pre-authorised containment (one line) | Who may authorise |
|---|---|---|---|---|
| **Agent compromise** | Adversary controls the agent's decision-making | | | |
| **Behavioural hijack** | Injected instructions override legitimate directives | | | |
| **Runaway agent** | Unauthorised scope expansion through error or manipulation | | | |
| **Delegation chain compromise** | Malicious instruction injected into a sub-agent | | | |

**Pre-authorised** means the containment action can be taken immediately without waiting for a
committee. Record who holds that standing authority and how they are reached out of hours.

## AG-MG.3 Decommissioning checklist — Marketing Content Agent
☐ Credentials and API keys revoked — by whom: ____________
☐ Agent identity disabled in the directory
☐ Persistent memory / embeddings disposed of — method: ____________
☐ Audit logs preserved for ______ (retention period and location)
☐ Downstream systems and integrations updated — list: ____________
☐ Removed from the agent registry with a retirement date
☐ Licence / contract terminated
☐ Staff notified of the replacement route
