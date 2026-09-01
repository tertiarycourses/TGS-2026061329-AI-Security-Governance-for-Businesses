"""
SINGLE SOURCE OF TRUTH — WSQ AI Security Governance for Businesses (TGS-2026061329).

Every artifact (PPT, LP, LG, LG.md, labs index, assessment) is generated from this
module plus data_domain1..4.py, so they stay 100% aligned.
"""

# ------------------------------------------------------------------ metadata
TITLE        = "AI Security Governance for Businesses"
SHORT_TITLE  = "AI Security Governance for Businesses"
COURSE_CODE  = "TGS-2026061329"
VERSION      = "v1.0"
VERSION_DATE = "1 September 2026"
ORG          = "Tertiary Infotech Academy Pte Ltd"
UEN          = "UEN: 201200696W"
TRAINER      = "Dr Alfred Ang"
DAYS         = 2

TSC_TITLE    = "Responsible AI and Generative AI Practices"
TSC_CODE     = "ICT-INT-0055-1.1"
TSC_LEVEL    = "Level 1"

COURSE_URL   = "https://www.tertiarycourses.com.sg/wsq-ai-security-governance-for-businesses.html"

# ------------------------------------------------------------------ outcomes
LEARNING_OUTCOMES = [
    "LO1: Analyse AI security governance foundations and the business risks that AI, "
    "generative AI and agentic AI systems introduce across an organisation.",
    "LO2: Evaluate AI governance frameworks and build an organisational governance "
    "structure of policies, roles, risk ownership and accountability.",
    "LO3: Develop and apply governance controls across the AI lifecycle, from data "
    "sourcing and model development through deployment, monitoring and decommissioning.",
    "LO4: Implement security controls for agentic AI, conduct an AI risk assessment and "
    "produce a prioritised AI security governance implementation roadmap.",
]

LO_SHORT = [
    ("LO1 · Analyse foundations & risks",
     "Analyse AI security governance foundations and the business risks that AI, generative AI and agentic AI introduce."),
    ("LO2 · Evaluate frameworks & build structure",
     "Evaluate AI governance frameworks and build a governance structure of policies, roles, risk ownership and accountability."),
    ("LO3 · Develop lifecycle controls",
     "Develop and apply governance controls across the AI lifecycle, from data and development to deployment and decommissioning."),
    ("LO4 · Implement agentic controls & roadmap",
     "Implement agentic AI security controls, run an AI risk assessment and produce a prioritised implementation roadmap."),
]

# ------------------------------------------------------------------ topics
TOPICS = [
    dict(num=1, code="01",
         title="AI Security Governance Foundations and Business Risks",
         subtitle="Why AI changes the risk picture · the AI threat landscape · GenAI and agentic risk · the business case",
         weighting="25%",
         concepts=[
            ("AI security governance defined", "The system of policies, roles, controls and evidence that keeps AI systems secure, lawful and accountable — distinct from, but built on, existing information-security governance."),
            ("Why AI breaks the old model", "Traditional controls assume deterministic software with a fixed attack surface. AI systems learn from data, behave probabilistically, and — when agentic — take actions in live systems."),
            ("The expanded attack surface", "AI adds five new asset classes to protect: training data, the model itself, prompts and context, the inference endpoint, and the tools an agent can invoke."),
            ("Traditional vs AI-specific threats", "SQL injection, XSS and weak credentials still apply. Prompt injection, data poisoning, model inversion, membership inference and model theft are new."),
            ("The NIST GenAI risk set", "NIST AI 600-1 names 12 risks unique to or exacerbated by generative AI, including confabulation, data privacy, information security, information integrity and value-chain risk."),
            ("Agentic AI raises the stakes", "An agent that can read private data, ingest untrusted content and communicate externally forms the 'lethal trifecta' — the pattern behind most 2025–2026 agent breaches."),
            ("Real incidents, real losses", "EchoLeak (CVE-2025-32711, CVSS 9.3) exfiltrated M365 Copilot context with zero user interaction; an over-scoped token let malicious instructions reach a build pipeline."),
            ("Shadow AI is the default state", "Staff adopt AI tools faster than governance can approve them; an unowned, uninventoried AI system is the single most common governance failure in businesses."),
            ("Business impact, not technical impact", "AI risk translates into regulatory penalties, contractual breach, IP leakage, reputational harm, service failure and unsafe automated decisions about people."),
            ("The Singapore context", "Businesses here must satisfy the PDPA, the PDPC AI Advisory Guidelines, IMDA's Model AI Governance Framework for Generative AI and AI Verify testing expectations."),
            ("Governance is a business enabler", "Organisations with mature AI governance deploy faster, because approval, evidence and assurance are routine rather than bespoke for every project."),
            ("The AI TRiSM market signal", "AI Trust, Risk and Security Management is one of the fastest-growing security segments — evidence that governance spend is now a board-level line item."),
         ]),
    dict(num=2, code="02",
         title="Building an AI Governance Framework: Policies, Roles and Risk Ownership",
         subtitle="NIST AI RMF · MGF for GenAI · PDPA duties · policy architecture · roles, RACI and the AI inventory",
         weighting="25%",
         concepts=[
            ("NIST AI RMF 1.0 at a glance", "A voluntary framework structured as four functions — GOVERN, MAP, MEASURE, MANAGE — that any organisation can adopt without buying a product."),
            ("The seven trustworthiness characteristics", "Valid and reliable; safe; secure and resilient; accountable and transparent; explainable and interpretable; privacy-enhanced; and fair with harmful bias managed."),
            ("GOVERN — the cross-cutting function", "GOVERN 1 policies and legal duties, GOVERN 2 accountability and training, GOVERN 3 diverse teams, GOVERN 4 risk culture, GOVERN 5 stakeholder engagement, GOVERN 6 third-party risk."),
            ("MAP, MEASURE and MANAGE", "MAP frames context and risk; MEASURE selects metrics and tests; MANAGE prioritises, treats, monitors and responds to risks including third-party and residual risk."),
            ("Singapore's MGF for Generative AI", "IMDA and AI Verify Foundation set nine dimensions: accountability, data, trusted development and deployment, incident reporting, testing and assurance, security, content provenance, safety R&D and public good."),
            ("AI Verify — testing as evidence", "Singapore's AI governance testing framework and toolkit lets an organisation demonstrate, not merely assert, that a system behaves as claimed."),
            ("PDPA duties that bite on AI", "Consent and Notification, Accountability, Protection and Retention obligations apply whenever personal data is used to develop or run an AI system."),
            ("Business Improvement and Research exceptions", "The PDPC guidelines explain when personal data may be used without fresh consent to develop AI systems — and the conditions and documentation that must accompany that reliance."),
            ("Policy architecture, not a single policy", "A workable set is an AI acceptable-use policy, an AI risk-management standard, a data-for-AI standard, a model/agent development standard, and a third-party AI standard."),
            ("Roles and risk ownership", "Board and executive accountability, an AI governance committee, business system owners, model owners, the DPO, security, legal, and a named human accountable for each deployment."),
            ("RACI beats goodwill", "Every control needs a Responsible doer, an Accountable owner, Consulted specialists and Informed stakeholders — ambiguity is where AI governance quietly fails."),
            ("The AI system inventory", "You cannot govern what you cannot see: a register of every AI system with owner, purpose, data classes, model, tools, risk tier and review date is the foundational control."),
            ("Risk tiering drives proportionality", "Classify systems by impact on people and business, then scale the control set — light-touch for low-risk internal aids, full assurance for decisions affecting individuals."),
         ]),
    dict(num=3, code="03",
         title="Governance Controls Across the AI Lifecycle",
         subtitle="Data governance · secure development · testing and red-teaming · deployment · monitoring · incident response · decommissioning",
         weighting="25%",
         concepts=[
            ("The AI lifecycle as a control surface", "Plan, source data, develop, test, deploy, operate and monitor, then decommission — each stage has its own failure modes and its own controls."),
            ("Data governance for AI", "Provenance, lawful basis, quality, classification, minimisation, de-identification, retention and deletion — decided before a model is trained, not after."),
            ("Personal data in AI systems", "Under the PDPC guidelines, organisations should apply data-protection measures such as minimisation, anonymisation and access control when using personal data in AI development."),
            ("Data poisoning and supply chain", "Training and fine-tuning data, embeddings, third-party models and packages are all supply-chain entry points; pin versions and validate sources."),
            ("Secure AI development", "Threat-model the system, protect prompts and secrets, isolate environments, review AI-generated code, and control who can change a model or instruction."),
            ("Testing, evaluation and assurance", "Functional accuracy is not enough: test robustness, bias, privacy leakage, jailbreak resistance and grounding before release, and record the evidence."),
            ("Red-teaming AI systems", "Adversarial testing against prompt injection, jailbreaks, data leakage and unsafe tool use — run before production and after every significant change."),
            ("Deployment gates", "A go/no-go decision with named approvers, documented residual risk, rollback plan, and a transparency notice where individuals are affected."),
            ("Human oversight by design", "Define where a human reviews, approves or can override, and make the escalation path fast enough to actually be used."),
            ("Continuous monitoring", "Watch drift, output quality, refusal and jailbreak rates, cost, latency and anomalous access — AI risk changes after deployment, not just before."),
            ("Logging and auditability", "Retain prompts, outputs, tool calls, approvals and model versions to the extent lawful, so an incident can be reconstructed and a decision explained."),
            ("AI incident response", "Extend the existing IR plan: how to disable an AI system fast, preserve evidence, assess personal-data impact, and notify under the PDPA where required."),
            ("Decommissioning safely", "Retire models and agents deliberately — revoke credentials, dispose of memory and embeddings, preserve audit logs and update dependent systems."),
         ]),
    dict(num=4, code="04",
         title="Security Controls for Agentic AI, Risk Assessment and Implementation Roadmap",
         subtitle="Agentic threat model · identity and least agency · guardrails and sandboxing · CSA agentic RMF profile · risk assessment · roadmap",
         weighting="25%",
         concepts=[
            ("What makes an agent different", "An agent plans, calls tools, keeps memory and acts — so its risk is set by the tools it can reach, not only by what the model says."),
            ("The lethal trifecta", "Private data access + exposure to untrusted content + the ability to communicate externally. Remove any one leg and mass exfiltration becomes far harder."),
            ("OWASP Agentic Security Top 10", "Goal hijack, tool misuse, identity and authorisation failures, supply chain, code execution, memory poisoning, RAG poisoning, excessive agency, weak isolation and poor operator oversight."),
            ("Agent identity is not user identity", "Each agent needs its own distinct identity, scoped credentials and audit trail so every action is attributable to an accountable owner."),
            ("Least agency, not just least privilege", "Constrain what an agent is allowed to decide, separately from what its credentials permit — the two are different controls."),
            ("Guardrails at the model boundary", "Input and output filtering for PII, jailbreak attempts, prompt injection and unsafe content — a necessary first wave, but never sufficient on its own."),
            ("Permission ladders and approvals", "Tool calls are authorised before execution by policy: deny, ask, or allow. Irreversible actions require a human approval gate."),
            ("Approval fatigue is a real control failure", "If almost every action prompts for approval, approval becomes telemetry rather than control — tune thresholds and measure the edit rate, not just the approval rate."),
            ("Sandboxing and blast radius", "Run agent code with OS-level isolation, restricted network egress and a scoped workspace so a compromised agent cannot reach beyond its task."),
            ("CSA agentic extensions to the NIST AI RMF", "Autonomy-tier classification, delegation accountability and an agent registry (GOVERN); tool-risk and action-consequence analysis (MAP); behavioural telemetry (MEASURE); agentic incident playbooks and decommissioning (MANAGE)."),
            ("Autonomy tiering", "Tier 1 supervised, Tier 2 constrained, Tier 3 broad with monitoring, Tier 4 full autonomy — each tier carries escalating oversight obligations."),
            ("Structured AI risk assessment", "Identify the asset and use case, name the threats, rate likelihood and impact, map existing controls, compute residual risk and assign a treatment and owner."),
            ("Prioritising the roadmap", "Sequence by risk reduction per unit of effort: quick wins first (inventory, acceptable use, logging), then structural controls, then assurance and automation."),
            ("Maturity and metrics", "Track inventory coverage, percentage of systems risk-assessed, time to disable an agent, incident count and mean time to respond — governance that is not measured does not persist."),
         ]),
]

# ------------------------------------------------------------------ day themes
DAY_THEMES = {
    1: "Foundations, Business Risks and Building the Governance Framework",
    2: "Lifecycle Controls, Agentic AI Security and the Implementation Roadmap",
}

# ------------------------------------------------------------------ assessment
ASSESSMENT = dict(
    written="Written Assessment (WA) — Short-Answer Questions (SAQ), 1 hour, open book.",
    practical="Case Study (CS) — one coherent governance case study, 1 hour, open book.",
    note="A minimum of 75% attendance is required to be eligible for assessment and funding.",
)

RECOMMENDED_COURSES = [
    "WSQ - Developing Ethical Strategies for Responsible Generative AI",
    "WSQ - Cybersecurity Risk Management for Businesses",
    "WSQ - Data Protection and Privacy Management (PDPA)",
    "WSQ - Applied Generative AI for Business Productivity",
]

TOOLS = [
    ("Cybersecurity Threat Simulator", "https://alfredang.github.io/cybersecuritysimulator/"),
    ("Hacklab — Ethical Hacking Lab Simulator", "https://alfredang.github.io/ethnicalhacking/"),
    ("FauxBank — Pentest Training Sandbox", "https://pentest-fauxbank.vercel.app/"),
    ("Cryptography Toolkit", "https://alfredang.github.io/cryptography-toolkit/"),
]
