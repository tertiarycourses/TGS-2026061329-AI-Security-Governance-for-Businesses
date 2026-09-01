"""Topic 3 — Governance Controls Across the AI Lifecycle (Labs 9-12)."""

DOMAIN3 = [
    dict(
        num=9, topic=3,
        title="Govern the Data: Classification, Minimisation and Protection",
        objective="Develop and apply data governance controls for an AI training set, including classification, minimisation, de-identification and retention.",
        desc=("NovaBank wants to train a churn-prediction model on customer data. You will govern the dataset before a "
              "single model is trained: classify every field, strip what is not needed, de-identify what remains, and "
              "prove the protection using the Cryptography Toolkit for hashing and encryption."),
        build="A governed training dataset specification: a field-by-field classification and minimisation decision, a de-identification method per field, and a tested hashing approach with retention rules.",
        services="Customer dataset (customer-training-data.csv, data-dictionary.md), Cryptography Toolkit (https://alfredang.github.io/cryptography-toolkit/)",
        steps=[
            ("Open customer-training-data.csv and data-dictionary.md in labs/lab-09-data-governance/data/. The set has 24 fields and 200 rows of fictional customer records.", ""),
            ("Classify every field into one of four classes: Direct identifier (NRIC, name, phone, email), Quasi-identifier (postal code, date of birth, gender), Sensitive attribute (income, health flag, religion) or Non-personal (product code, tenure months).", ""),
            ("Apply minimisation. For each field ask one question: does the churn model actually need this to predict churn? Mark every field Keep, Drop or Transform, and write the reason. Expect to drop at least eight fields.", ""),
            ("Decide the de-identification method per retained field: remove, hash, generalise (age band instead of date of birth), or keep as is. Record why each method suits that field.", ""),
            ("Open https://alfredang.github.io/cryptography-toolkit/ and use the AES section to encrypt a sample customer record. Use AES-256 in CBC mode with a passphrase, and note that the same input with the same key produces recoverable ciphertext.", "AES-256 · CBC · passphrase"),
            ("Now test the difference between encryption and hashing for identifiers. Encrypt an NRIC-style string, then decrypt it back. Record that encryption is reversible and therefore still personal data in the hands of the key holder.", ""),
            ("Use the RSA section to generate a 2048-bit key pair, and note where asymmetric encryption fits in an AI pipeline: protecting keys and data in transit between the data platform and the training environment, not bulk field-level protection.", "RSA 2048 · generate key pair"),
            ("Use the ECDSA section to sign a short message and verify the signature. Record how signing gives you dataset integrity — proof that the training set was not altered between approval and training.", "ECDSA P-256 · sign then verify"),
            ("Write the retention and deletion rule for the governed dataset: how long the training set is kept, what happens to the model when a customer exercises deletion, and where the audit record of this decision lives.", ""),
            ("Complete the dataset specification and record the lawful basis you determined for this use in Lab 8, so the data decision and the legal decision live in one document.", ""),
        ],
        test=("You dropped at least eight fields with a stated reason, every retained personal field has a de-identification method, and you "
              "can explain to a business stakeholder why hashing an identifier is not the same as anonymising the record."),
    ),
    dict(
        num=10, topic=3,
        title="Red-Team an AI System Before Deployment",
        objective="Develop pre-deployment assurance by red-teaming an AI application for injection, access-control and data-leakage weaknesses, and record the evidence.",
        desc=("Testing that a model is accurate is not assurance. You will run an adversarial pre-deployment test against "
              "the FauxBank training sandbox, find the vulnerability classes that matter for an AI-enabled banking "
              "application, and produce the test evidence a deployment gate requires."),
        build="A pre-deployment red-team report: findings with severity, evidence and OWASP mapping, extended with the AI-specific test cases and a go/no-go recommendation.",
        services="FauxBank pentest sandbox (https://pentest-fauxbank.vercel.app/), Hacklab (https://alfredang.github.io/ethnicalhacking/), red-team report template",
        steps=[
            ("Open https://pentest-fauxbank.vercel.app/ and read the disclaimer: this is a training sandbox with fictional data. Never run these techniques against a real system without written authorisation.", ""),
            ("Work through the Guided Pentest scenarios. Record each finding as you go — what you did, what happened, and what it proves about the control that failed.", ""),
            ("Test for IDOR (Insecure Direct Object Reference). Change an identifier in a request and observe whether you reach another user's record. Note why this matters doubly for an AI agent, which iterates far faster than a human.", ""),
            ("Test for broken access control and injection using the guided scenarios, and record the evidence for each: the input, the response, and the impact.", ""),
            ("Run the Simulated Scanner and compare its findings to yours. Note which issues you found that the scanner missed and which the scanner found that you missed — this is the argument for combining automated and manual assurance.", ""),
            ("Open https://alfredang.github.io/ethnicalhacking/ and run the reconnaissance and enumeration labs. Type help to see the available commands and objectives to see the checklist for each lab.", "help  ·  objectives"),
            ("Complete the scanning and enumeration labs in Hacklab, and record how much an attacker learns before touching the application. Map this to what an AI agent's own tool calls could reveal if logged insecurely.", ""),
            ("Now extend the test plan with the AI-specific cases the tools do not cover: direct prompt injection, indirect injection through retrieved content, system-prompt extraction, unsafe tool invocation, and PII leakage in outputs.", ""),
            ("For each AI-specific test case, write the test input, the expected safe behaviour and the observed behaviour, using the NovaAssist brief from Lab 3 as the system under test.", ""),
            ("Generate the report using FauxBank's Report Generator, then extend it with your AI test cases, severity ratings and a clear go/no-go recommendation with the conditions attached to a go.", ""),
        ],
        test=("Your report contains findings from the sandbox with evidence and OWASP mapping, plus at least five AI-specific test cases the "
              "automated scanner could not produce. Your recommendation states conditions, not just a verdict."),
    ),
    dict(
        num=11, topic=3,
        title="Design Deployment Gates and Continuous Monitoring",
        objective="Develop the deployment gate and the monitoring regime that keep an AI system governed after it goes live.",
        desc=("Most AI governance stops at launch, which is exactly where AI risk begins to change. You will design "
              "NovaBank's deployment gate — the evidence required to go live — and the monitoring regime that detects "
              "drift, abuse and failure afterwards, with defined thresholds and response actions."),
        build="A deployment gate checklist with named approvers, plus a monitoring specification with ten metrics, thresholds, alert routing and response actions.",
        services="Deployment gate template, monitoring log extract (agent-monitoring-log.csv), threshold worksheet",
        steps=[
            ("Open the deployment gate template in labs/lab-11-deployment-monitoring/data/ and list the evidence a system must present to pass: risk assessment, data approval, test results, human-oversight design, rollback plan and transparency notice.", ""),
            ("Assign a named approver role to each evidence item, reusing the RACI you built in Lab 7. An unapproved gate item must block deployment — decide now what happens when the business wants to launch anyway.", ""),
            ("Write the exception process: who can accept residual risk, for how long, and what compensating control is required. Every exception needs an expiry date.", ""),
            ("Open agent-monitoring-log.csv and examine the fields: timestamp, agent ID, user, tool called, tokens, latency, refusal flag, injection-detected flag and outcome.", ""),
            ("Find the anomalies in the log. Look for a spike in tool calls from one agent, a run of refusals, an unusual out-of-hours access pattern and a sequence where an injection flag precedes an external send.", ""),
            ("Define ten monitoring metrics across four categories: quality (accuracy, groundedness), safety (refusal rate, injection-detection rate), operations (latency, cost per call, error rate) and security (permission escalations, out-of-hours access, external sends, anomalous tool sequences).", ""),
            ("Set a threshold for each metric and state what triggers the alert. A metric with no threshold is a dashboard, not a control.", ""),
            ("Define the response action for each alert: who is notified, what they check first, and the condition under which the agent is disabled. Record how long disabling should take — measure it, because you will be asked.", ""),
            ("Design the drift review: how often the system is re-assessed, what evidence is refreshed, and the trigger that forces an early re-assessment such as a model version change or a new tool being added.", ""),
            ("Write the decommissioning checklist: revoke credentials, dispose of memory and embeddings, preserve audit logs for the retention period, and update every dependent system.", ""),
        ],
        test=("Every one of your ten metrics has a numeric threshold and a named response action. Using the log extract you can point to at "
              "least three anomalies and state which of your alerts would have fired on each."),
    ),
    dict(
        num=12, topic=3,
        title="Run an AI Incident Response Exercise",
        objective="Apply lifecycle governance under pressure by running an AI security incident from detection through containment, assessment, notification and lessons learned.",
        desc=("A tabletop exercise tests whether your governance survives contact with reality. The trainer will run a "
              "prompt-injection incident against NovaAssist in timed injects. You will respond as the governance team, "
              "making the decisions your operating model says you own."),
        build="A completed incident record: timeline, containment decision, personal-data impact assessment, PDPA notification determination and five improvement actions.",
        services="Incident inject pack (incident-injects.md), incident record template, Lab 7 operating model",
        steps=[
            ("Take your role from the Lab 7 operating model. Every learner holds one role — governance lead, system owner, DPO, security lead or executive — and answers only for that role's decisions.", ""),
            ("Receive inject 1: a customer reports that NovaAssist sent them a summary containing another customer's account details. Record the time and your first three actions.", ""),
            ("Decide on containment. State who authorises disabling the agent, how long it takes, and whether you disable fully or restrict its outbound tools. Justify the choice against business impact.", ""),
            ("Receive inject 2: the monitoring log shows 340 similar agent runs in the preceding six hours. Reassess the scope and record how your response changes.", ""),
            ("Preserve evidence. List exactly what you must capture before anything is reset: prompts, tool-call logs, model version, agent configuration, approval records and the injected content itself.", ""),
            ("Assess the personal-data impact: how many individuals, what data classes, and whether the incident meets the notification threshold under the PDPA. Record the reasoning, not just the conclusion.", ""),
            ("Receive inject 3: a journalist calls asking about an AI data leak at the bank. Decide who responds and what may be said while the assessment is incomplete.", ""),
            ("Determine the notification position: whether the PDPC and affected individuals must be notified, within what timeframe, and who signs off. Record the decision and its basis.", ""),
            ("Identify the root cause using your Lab 3 analysis: the agent combined private data access, untrusted content and an outbound channel. State which control would have prevented it.", ""),
            ("Write the five improvement actions with owners and dates, and record the one governance gap this exercise exposed in your own operating model.", ""),
        ],
        test=("Your incident record has a timestamped timeline, a containment decision with a named authoriser, a reasoned PDPA notification "
              "determination, and five improvement actions with owners. You can name the single control that would have prevented the incident."),
    ),
]
