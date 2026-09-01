"""Topic 1 — AI Security Governance Foundations and Business Risks (Labs 1-4)."""

DOMAIN1 = [
    dict(
        num=1, topic=1,
        title="Build the AI System Inventory for NovaBank",
        objective="Analyse an organisation's AI footprint and produce the AI system inventory that every other governance control depends on.",
        desc=("You are the newly appointed AI Governance Lead at NovaBank, a mid-sized Singapore retail bank. "
              "Nobody can tell you how many AI systems the bank runs. You will work from the supplied discovery "
              "pack — an IT asset extract, a procurement export and a staff survey — to identify every AI system, "
              "classify it, and produce a defensible AI system inventory with named owners and risk tiers."),
        build="A completed AI System Inventory (ai-inventory.csv) covering 12 AI systems with owner, purpose, data classes, model, autonomy level and risk tier, plus a shadow-AI findings note.",
        services="Mock data pack (discovery-it-assets.csv, discovery-procurement.csv, discovery-staff-survey.csv), spreadsheet tool",
        steps=[
            ("Open the three discovery files in labs/lab-01-ai-inventory/data/ and read the column headings before you filter anything. Note that no single file contains the whole picture.", ""),
            ("Identify AI systems in discovery-it-assets.csv. Flag any row whose vendor, product name or description indicates a model, assistant, copilot, chatbot, scoring engine or agent.", ""),
            ("Cross-check discovery-procurement.csv for AI services bought outside IT — look for line items charged to a business cost centre rather than to IT.", ""),
            ("Read discovery-staff-survey.csv for shadow AI: tools staff use that appear in neither of the other two files. These are your highest-priority findings.", ""),
            ("Merge into one register. For each system record: System ID, Name, Business owner, Purpose, Data classes touched, Model/vendor, Hosting, Autonomy level, Personal data (Y/N).", ""),
            ("Assign an autonomy level to each system using the four tiers: Tier 1 supervised (suggests only), Tier 2 constrained (acts within a fixed allowlist), Tier 3 broad with monitoring, Tier 4 full autonomy.", ""),
            ("Assign a risk tier (High / Medium / Low) using two questions: does it make or materially influence a decision about a person, and does it touch personal or confidential data?", ""),
            ("Name an accountable owner for every system. Any system without a named human owner is itself a finding — record it as such.", ""),
            ("Write a half-page shadow-AI findings note: how many unapproved tools you found, what data they touch, and the single control you would introduce first.", ""),
        ],
        test=("Your inventory has a row for every AI system in all three files, including at least three shadow-AI tools that appear only in "
              "the staff survey. Every row has a named owner, an autonomy tier and a risk tier, and you can justify each High rating in one sentence."),
    ),
    dict(
        num=2, topic=1,
        title="Map the AI Threat Landscape with the Threat Simulator",
        objective="Analyse how traditional security threats and AI-specific threats combine in an AI-enabled business, and explain the business impact of each.",
        desc=("Governance decisions are only as good as your understanding of the threats. You will use the browser-based "
              "Cybersecurity Threat Simulator to experience the classic attack classes hands-on, then extend each one into "
              "its AI-era equivalent and record the business impact for NovaBank."),
        build="A completed Threat-to-Business-Impact map covering 8 threat classes, each with its AI-era variant, the NovaBank asset at risk and a first-line control.",
        services="Cybersecurity Threat Simulator (https://alfredang.github.io/cybersecuritysimulator/), threat-map worksheet",
        steps=[
            ("Open https://alfredang.github.io/cybersecuritysimulator/ and review the Dashboard. Note the ten threat modules and the risk classification each one carries.", ""),
            ("Run the Phishing module. Classify at least eight emails as Safe or Phishing, then read the annotated walkthrough and record the red flags you missed.", ""),
            ("Run the SQL Injection module in vulnerable mode. Enter admin as the username and ' OR '1'='1 as the password, and read the live query display to see exactly why the login succeeds.", "admin  /  ' OR '1'='1"),
            ("Run the XSS module. Type a script-like string and compare the unsafe rendering against the correctly escaped output. Note that the fix is output encoding, not input blocking alone.", ""),
            ("Run the Password Lab. Test a weak password and a passphrase, and record the entropy in bits and the estimated crack time for each.", ""),
            ("Run the Social Engineering trainer. Work through the scenarios and record your score, then note which tactic — pretexting, baiting, vishing, smishing or BEC — you found hardest to spot.", ""),
            ("Run the Data Leakage risk estimator. Toggle encryption at rest, access controls, private buckets, protected backups, training and DLP, and record how the risk score responds to each control.", ""),
            ("For each of the eight threat classes above, write the AI-era variant in your worksheet: phishing becomes GenAI-crafted spear-phishing at scale; SQL injection becomes prompt injection into a tool-calling agent; XSS becomes unsafe rendering of model output; weak passwords become over-scoped agent credentials; social engineering becomes model manipulation; data leakage becomes training-data and context-window leakage.", ""),
            ("Complete the map: for each row add the NovaBank asset at risk, the business impact in one sentence, and the single most effective first-line control.", ""),
        ],
        test=("Your map has all eight threat classes with both the traditional and the AI-era variant filled in. You can state, from the "
              "simulator, why parameterised queries stop SQL injection, and explain in one sentence why the same reasoning does not fully stop prompt injection."),
    ),
    dict(
        num=3, topic=1,
        title="Analyse the Lethal Trifecta in a Live Agent Design",
        objective="Analyse an agentic AI design, identify the lethal-trifecta exposure and the applicable NIST GenAI risks, and propose an architectural break.",
        desc=("NovaBank's digital team has proposed 'NovaAssist', a customer-service agent that reads the customer's account, "
              "searches incoming e-mail and web content for context, and can send e-mails and raise payment instructions. "
              "You will analyse the design against the lethal trifecta and the NIST AI 600-1 GenAI risk set, and recommend a redesign."),
        build="A completed agent risk analysis: the trifecta assessment, five mapped NIST GenAI risks, a documented attack path and a redesign that breaks the trifecta.",
        services="NovaAssist design brief (novassist-design-brief.md), NIST AI 600-1 risk list, trifecta worksheet",
        steps=[
            ("Read novassist-design-brief.md in labs/lab-03-lethal-trifecta/data/. List every data source the agent reads and every action it can take.", ""),
            ("Test the design against leg 1 — access to private data. Record exactly which confidential or personal data the agent can reach, and under whose permissions it reads them.", ""),
            ("Test leg 2 — exposure to untrusted content. Identify every input the agent ingests that an outsider can influence: customer e-mail, web pages, uploaded documents, third-party API responses.", ""),
            ("Test leg 3 — ability to communicate externally. List every outbound channel: sending e-mail, calling external APIs, writing to shared systems, even rendering links that auto-fetch.", ""),
            ("Write the attack path in five steps: how an attacker gets untrusted text in front of the agent, how that text redirects the agent's goal, and how data leaves the bank. Base it on the EchoLeak pattern.", ""),
            ("Map the design against the NIST AI 600-1 GenAI risk set and select the five most relevant: Information Security, Data Privacy, Information Integrity, Human-AI Configuration and Value Chain and Component Integration.", ""),
            ("For each of the five risks, write one sentence of business impact specific to a Singapore retail bank, including the PDPA exposure where personal data is involved.", ""),
            ("Propose the architectural break. Choose which leg of the trifecta to remove and justify it — for example, splitting the agent so the tool that reads untrusted content has no outbound channel and no access to account data.", ""),
            ("Record the residual risk after your redesign, and name the one control you would still add on top of the architecture.", ""),
        ],
        test=("You can state which of the three legs your redesign removes and why removing that leg is more effective than adding an output "
              "filter to the original design. Your five NIST risks are each tied to a concrete NovaBank consequence, not a generic description."),
    ),
    dict(
        num=4, topic=1,
        title="Build the Business Case for AI Security Governance",
        objective="Analyse the cost of inaction and present a business case that justifies AI security governance investment to a board.",
        desc=("Governance competes for budget. You will quantify NovaBank's exposure using the incident pack and the "
              "cost assumptions provided, then produce a one-page board paper that argues for the governance programme "
              "in the language executives use: risk reduction, regulatory exposure and time to deploy."),
        build="A one-page board paper with a quantified exposure estimate, three prioritised investments and the expected risk reduction for each.",
        services="Incident cost pack (incident-cost-assumptions.csv, sector-incident-data.csv), board paper template",
        steps=[
            ("Open incident-cost-assumptions.csv and sector-incident-data.csv in labs/lab-04-business-case/data/ and identify the four cost categories: regulatory, remediation, business interruption and reputational.", ""),
            ("Use your Lab 1 inventory to count NovaBank's High-risk AI systems and the number that process personal data.", ""),
            ("Estimate annual expected loss for one realistic scenario — a prompt-injection data leak from a customer-facing agent — using the likelihood and impact figures in the cost pack.", ""),
            ("Add the regulatory dimension: note the PDPA financial penalty exposure and the reputational consequence of a reported breach for a licensed financial institution.", ""),
            ("Identify the three highest-value governance investments from your findings so far: the AI inventory and ownership, an acceptable-use policy with mandatory logging, and pre-deployment risk assessment with a human approval gate.", ""),
            ("For each investment, estimate cost, time to implement and the specific risk it reduces. Express the reduction as a change in likelihood or impact, not as a vague improvement.", ""),
            ("Add the enabler argument: governed organisations deploy faster because approval and evidence are routine. Quantify it as weeks saved per AI project.", ""),
            ("Write the one-page board paper: the exposure, the three investments, the expected reduction, and a single clear ask.", ""),
            ("Present your paper in two minutes to the class and take one challenge question from the trainer acting as CFO.", ""),
        ],
        test=("Your board paper fits on one page, states a number for annual expected loss with its assumptions visible, and each of the "
              "three investments names the specific risk it reduces. You can answer the CFO challenge 'why not just buy a tool?' in one sentence."),
    ),
]
