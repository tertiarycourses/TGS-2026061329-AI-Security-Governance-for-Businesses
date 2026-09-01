"""Topic 4 — Security Controls for Agentic AI, Risk Assessment and Roadmap (Labs 13-16)."""

DOMAIN4 = [
    dict(
        num=13, topic=4,
        title="Design the Agentic Security Control Stack",
        objective="Implement layered security controls for an agentic AI system: identity, guardrails, permission ladders, sandboxing and human approval gates.",
        desc=("You will redesign NovaAssist with a real defence-in-depth stack. Working from the OWASP Agentic Security "
              "Top 10, you will specify each control layer, decide which tool calls need approval, and write the "
              "permission policy that governs the agent before it acts."),
        build="A layered agentic control specification: agent identity and scopes, guardrail rules, a deny/ask/allow permission policy for 12 tools, sandbox boundaries and human approval gates.",
        services="NovaAssist tool catalogue (agent-tool-catalogue.csv), OWASP ASI Top 10 reference, control stack template",
        steps=[
            ("Open agent-tool-catalogue.csv in labs/lab-13-agentic-controls/data/. Twelve tools are listed with their function, the data they reach and whether their effect is reversible.", ""),
            ("Classify every tool by consequence: read-only, write-reversible, write-irreversible or external-communication. This classification, not the tool name, determines the control it needs.", ""),
            ("Layer 1 — identity. Specify NovaAssist's own agent identity, separate from any user account, with the minimum scopes it needs. State how each action stays attributable to the accountable owner.", ""),
            ("Layer 2 — guardrails. Define the input checks (PII detection, jailbreak and injection patterns) and the output checks (PII redaction, unsafe-content filtering, grounding check). Record explicitly what guardrails cannot do.", ""),
            ("Layer 3 — permission ladder. For each of the twelve tools assign deny, ask or allow. Every irreversible or external-communication tool must be ask or deny. Justify each allow in one sentence.", "deny → ask → allow"),
            ("Write three concrete deny rules that a policy engine could enforce, for example: deny any outbound send whose body contains an account number pattern; deny any tool call in the same turn as a detected injection; deny writes outside the case workspace.", ""),
            ("Layer 4 — sandboxing. Define the blast radius: the filesystem the agent may touch, the network destinations it may reach, and the credentials it never holds directly.", ""),
            ("Layer 5 — human approval. Specify which actions require a human gate, what the approver sees, and the service level for a response. Then address approval fatigue: state the volume above which your gate stops being a control.", ""),
            ("Map your stack to the OWASP Agentic Security Top 10 and confirm coverage for goal hijack, tool misuse, identity and authorisation, memory poisoning, RAG poisoning and excessive agency. Record any risk your stack does not cover.", ""),
            ("State the residual risk honestly: name the two attack paths that survive all five layers and the compensating detection you would add for each.", ""),
        ],
        test=("Every irreversible and external-communication tool is set to ask or deny. Your three deny rules are specific enough to be "
              "implemented, and you can name at least two attack paths your stack does not stop."),
    ),
    dict(
        num=14, topic=4,
        title="Apply the CSA Agentic Extensions to the NIST AI RMF",
        objective="Implement agentic-specific governance by applying autonomy tiering, delegation accountability, an agent registry and behavioural telemetry.",
        desc=("The NIST AI RMF treats a read-only recommender and an autonomous executor identically. The CSA agentic "
              "profile closes that gap. You will apply its extensions to NovaBank's agent estate: tier every agent, "
              "document delegation accountability, build the agent registry and define behavioural telemetry."),
        build="An agentic governance pack: five agents tiered with justification, a delegation accountability record, a completed agent registry and a behavioural telemetry specification.",
        services="Agent estate pack (novabank-agents.md), CSA agentic RMF profile reference, registry template",
        steps=[
            ("Open novabank-agents.md in labs/lab-14-csa-agentic-profile/data/. Five agents are described: NovaAssist, a fraud triage agent, an internal IT helpdesk agent, a marketing content agent and a reconciliation agent.", ""),
            ("Apply AG-GV.1 Autonomy Tier Classification. Assign each agent a tier: Tier 1 supervised, Tier 2 constrained, Tier 3 broad with monitoring, Tier 4 full autonomy. Justify each from what the agent can do, not from how it is described.", ""),
            ("State the oversight obligation that comes with each tier: what review, what approval and what monitoring frequency. The obligation must escalate with the tier or the tiering is decorative.", ""),
            ("Apply AG-GV.2 Delegation Accountability. For the reconciliation agent, which delegates to a sub-agent, document the oversight boundary, the escalation trigger, the scope of delegated authority and the accountability lineage back to a named human.", ""),
            ("Apply AG-GV.3 Agent Lifecycle Registry. Build the registry with columns: agent ID, owner, purpose, autonomy tier, tools and scopes, data reached, sub-agents, review date and kill-switch procedure.", ""),
            ("Apply AG-MP.1 Tool Risk Classification and AG-MP.2 Action-Consequence Analysis. For the fraud triage agent, draw the consequence graph: which tool sequences lead to a customer account being frozen, and what happens if that decision is wrong.", ""),
            ("Apply AG-MP.3 Multi-Agent Topology Risk for the reconciliation agent and its sub-agent: identify the trust boundary between them and how a compromise would propagate.", ""),
            ("Apply AG-MS.1 Agentic Behavioural Telemetry. Specify the runtime metrics: action velocity, permission escalation rate, cross-boundary invocations, delegation depth and exception rate, each with a baseline and an alert threshold.", ""),
            ("Apply AG-MG.1 Agentic Incident Classification. Write a one-line containment playbook for each of the four incident types: agent compromise, behavioural hijack, runaway agent and delegation chain compromise.", ""),
            ("Apply AG-MG.3 Agent Decommissioning to the marketing content agent, which is being retired: credential revocation, memory disposition, audit log preservation and downstream updates.", ""),
        ],
        test=("All five agents are tiered with a justification drawn from their capabilities, your registry has no blank kill-switch field, and "
              "your telemetry metrics each have a baseline and a threshold. You can explain why tiering by capability beats tiering by job title."),
    ),
    dict(
        num=15, topic=4,
        title="Conduct a Full AI Security Risk Assessment",
        objective="Implement a structured AI risk assessment producing rated risks, mapped controls, residual risk and assigned treatments with owners.",
        desc=("This is the assessment that a regulator, an auditor or a board will ask to see. You will run a complete "
              "structured risk assessment on NovaAssist, combining everything from the previous fourteen labs into a "
              "single defensible document with rated, owned and treated risks."),
        build="A complete AI security risk assessment: 12 rated risks with likelihood, impact, existing controls, residual rating, treatment decision, owner and target date.",
        services="Risk assessment template (risk-assessment-template.csv), 5x5 rating matrix, all prior lab outputs",
        steps=[
            ("Open risk-assessment-template.csv and the rating matrix in labs/lab-15-risk-assessment/data/. Confirm the scoring: likelihood 1-5, impact 1-5, risk score as the product, with bands Low 1-6, Medium 8-12, High 15-25.", ""),
            ("Define the assessment scope precisely: the system, its version, its data, its tools, its users and the boundary of the assessment. An unbounded scope produces an unusable assessment.", ""),
            ("Identify twelve risks by drawing on your earlier work: the trifecta exposure from Lab 3, the NIST GenAI risks, the OWASP agentic risks from Lab 13, the data risks from Lab 9 and the PDPA risks from Lab 8.", ""),
            ("Write each risk as a proper risk statement in the form: cause leads to event leads to consequence. 'Prompt injection' is not a risk statement; 'untrusted e-mail content injects instructions, causing the agent to send account data externally, resulting in a PDPA breach' is.", ""),
            ("Rate inherent likelihood and impact for each risk before controls, using the matrix. Record the reasoning for any rating of 4 or 5 — those are the ratings that will be challenged.", ""),
            ("Map the existing and planned controls from Labs 11 and 13 to each risk. A risk with no mapped control keeps its inherent rating; do not credit controls you have not specified.", ""),
            ("Rate residual likelihood and impact after controls, and compute the residual score. Be honest: guardrails reduce likelihood, they rarely reduce impact.", ""),
            ("Assign a treatment to every risk: treat, tolerate, transfer or terminate. Any residual High risk must be treated or escalated for formal acceptance by the executive owner — record which.", ""),
            ("Assign an owner and a target date to every treatment action. An unowned treatment is a wish; check that every owner is a role that exists in your Lab 7 operating model.", ""),
            ("Write the two-paragraph executive summary: the overall risk position, the three risks that matter most, and your clear recommendation on whether NovaAssist should go live and under what conditions.", ""),
        ],
        test=("All twelve risks are written as cause-event-consequence statements, every residual High risk has either a treatment plan or a "
              "recorded acceptance by a named executive, and every treatment has an owner who exists in your operating model."),
    ),
    dict(
        num=16, topic=4,
        title="Capstone — Build the AI Security Governance Roadmap",
        objective="Implement a prioritised, costed and sequenced AI security governance implementation roadmap and present it for executive approval.",
        desc=("The capstone brings the whole course together. You will consolidate every artefact you have produced into "
              "a 12-month AI security governance implementation roadmap for NovaBank, sequenced by risk reduction per "
              "unit of effort, with metrics that prove the programme is working — then present it for approval."),
        build="A 12-month AI security governance roadmap across three phases with initiatives, owners, effort, dependencies and success metrics, plus a five-slide executive presentation.",
        services="Roadmap template, maturity model, all prior lab outputs, presentation template",
        steps=[
            ("Consolidate your inputs: the Lab 5 gap register, the Lab 15 risk assessment, the Lab 6 policy set, the Lab 7 operating model, the Lab 13 control stack and the Lab 14 agentic registry.", ""),
            ("Assess current maturity across five domains — governance structure, policy, inventory and risk, lifecycle controls, and agentic controls — scoring each 1 to 5 with the evidence behind the score.", ""),
            ("Set the 12-month target maturity per domain. Targeting level 5 everywhere is not a plan; choose where NovaBank genuinely needs to be and say why.", ""),
            ("Build Phase 1 (months 1-3), the foundation: complete the AI inventory with owners, issue the acceptable-use policy, stand up the governance committee and turn on logging. These are cheap, fast and close the widest gaps.", ""),
            ("Build Phase 2 (months 4-8), the controls: risk assessment for every High-tier system, deployment gates, the agentic control stack for NovaAssist, monitoring with thresholds, and the incident playbooks.", ""),
            ("Build Phase 3 (months 9-12), the assurance: red-teaming as routine, third-party AI assurance, independent review, metrics reporting to the board and the first full re-assessment cycle.", ""),
            ("For every initiative record owner, effort (S/M/L), dependencies and the specific gap or risk it closes. An initiative that closes nothing from your registers should be cut.", ""),
            ("Sequence by risk reduction per unit of effort and resolve the dependencies — you cannot risk-assess systems you have not inventoried, and you cannot enforce a policy you have not issued.", ""),
            ("Define six programme metrics with baselines and 12-month targets: inventory coverage, percentage of High-risk systems assessed, policy attestation rate, time to disable an agent, AI incidents and mean time to respond.", ""),
            ("Build the five-slide executive presentation: where we are, what could go wrong, what we will do, what it costs, and what you are approving. Present in five minutes and defend one challenge from the trainer as board chair.", ""),
        ],
        test=("Every initiative in your roadmap traces back to a specific gap or a specific rated risk, the phases respect their dependencies, "
              "and all six metrics have a baseline and a target. Your five-slide deck makes the ask explicit on the final slide."),
    ),
]
