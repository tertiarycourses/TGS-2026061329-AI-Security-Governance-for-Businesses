"""Topic 2 — Building an AI Governance Framework (Labs 5-8)."""

DOMAIN2 = [
    dict(
        num=5, topic=2,
        title="Run a NIST AI RMF Gap Assessment",
        objective="Evaluate an organisation against the NIST AI RMF GOVERN, MAP, MEASURE and MANAGE functions and produce a prioritised gap register.",
        desc=("NovaBank has an information-security programme but no AI-specific governance. You will assess the bank "
              "against the NIST AI RMF using the supplied evidence pack — policy extracts, meeting minutes and interview "
              "notes — scoring each subcategory and producing a gap register that drives the rest of the course."),
        build="A completed NIST AI RMF gap assessment across 16 subcategories, each scored with evidence, plus a top-10 prioritised gap register.",
        services="Evidence pack (policy-extracts.md, governance-interviews.md, existing-controls.csv), RMF assessment worksheet",
        steps=[
            ("Open the evidence pack in labs/lab-05-nist-rmf-gap/data/. Read policy-extracts.md and governance-interviews.md fully before scoring anything — score on evidence, not impression.", ""),
            ("Score the GOVERN function. Assess GOVERN 1.1 legal and regulatory requirements, 1.2 trustworthiness in policy, 1.6 AI system inventory, 1.7 decommissioning, 2.1 roles and responsibilities, 2.3 executive accountability and 6.1 third-party AI risk.", ""),
            ("Use a four-point scale for every subcategory: 0 Not in place, 1 Ad hoc, 2 Defined but not consistently applied, 3 Managed with evidence. Record the specific evidence line that justifies each score.", ""),
            ("Score the MAP function: MAP 1.1 intended purpose and context, 1.5 risk tolerances, 2.3 TEVV considerations, and whether risk is framed per system or only at portfolio level.", ""),
            ("Score the MEASURE function: MEASURE 1.1 metrics selected, 1.3 independent internal review, and whether any AI system is currently tested for bias, robustness or jailbreak resistance.", ""),
            ("Score the MANAGE function: MANAGE 1.2 risk prioritisation, 1.4 residual risk documented and accepted by a named owner, and 4.1 post-deployment monitoring.", ""),
            ("Calculate the average score per function and identify which function is weakest. In most organisations with mature InfoSec, MEASURE scores lowest — check whether that holds here.", ""),
            ("Build the gap register: for each gap record the subcategory, current score, target score, business risk if unaddressed, remediation action, owner and effort (S/M/L).", ""),
            ("Prioritise the top ten gaps by risk reduction per unit of effort, not by score alone. A cheap fix closing a High risk outranks an expensive fix closing a Medium one.", ""),
        ],
        test=("Every subcategory score cites a specific line of evidence from the pack. Your gap register's top three items are all "
              "High-risk, and you can defend why a lower-scoring subcategory did not make the top ten."),
    ),
    dict(
        num=6, topic=2,
        title="Draft the AI Acceptable Use and Governance Policy Set",
        objective="Evaluate policy requirements and develop an enforceable AI policy set aligned to the NIST AI RMF and Singapore's MGF for Generative AI.",
        desc=("Policy is where governance becomes enforceable. You will draft NovaBank's AI Acceptable Use Policy and the "
              "supporting standard, working from the gap register you produced in Lab 5 and the nine dimensions of "
              "Singapore's Model AI Governance Framework for Generative AI."),
        build="A complete AI Acceptable Use Policy (2 pages) plus a one-page AI Risk Management Standard, both mapped to MGF dimensions and RMF subcategories.",
        services="Policy templates (aup-template.md, standard-template.md), MGF nine dimensions reference, Lab 5 gap register",
        steps=[
            ("Open aup-template.md in labs/lab-06-policy-set/data/ and review the required sections: purpose, scope, definitions, permitted use, prohibited use, approval, roles, monitoring, breach and review.", ""),
            ("Define scope precisely. State whether the policy covers public GenAI tools, embedded AI features in existing SaaS, internally built models and third-party agents — vague scope is the most common policy defect.", ""),
            ("Write the permitted-use section. Specify what staff may do with approved AI tools, with which data classifications, and under what logging.", ""),
            ("Write the prohibited-use section with concrete rules: no confidential or personal customer data into unapproved tools; no AI-generated code merged without human review; no automated decision about a customer without a documented human check.", ""),
            ("Write the approval pathway. State who approves a new AI system, what evidence they need, and the maximum turnaround — a pathway with no service level is a pathway staff will bypass.", ""),
            ("Map every clause to the MGF dimension it serves — accountability, data, trusted development and deployment, incident reporting, testing and assurance, security, content provenance — and record the mapping in a table.", ""),
            ("Draft the one-page AI Risk Management Standard: risk tiering criteria, the assessment required at each tier, who signs off, and the review frequency.", ""),
            ("Add the enforcement and consequence section, and the review cycle with a named owner and a date. A policy with no owner and no review date is already obsolete.", ""),
            ("Peer-review another group's policy against one test: could a member of staff read this and know exactly what they may and may not do on Monday morning? Record two specific improvements.", ""),
        ],
        test=("Your AUP states at least six concrete prohibited actions, names the approver and the turnaround time, and every clause maps "
              "to at least one MGF dimension. A peer confirms they could apply your policy without asking you a question."),
    ),
    dict(
        num=7, topic=2,
        title="Design the Governance Operating Model and RACI",
        objective="Evaluate accountability requirements and develop a governance operating model with committee structure, roles and a control-level RACI.",
        desc=("Policies fail without owners. You will design NovaBank's AI governance operating model: the committee that "
              "decides, the roles that execute, and a RACI matrix that removes ambiguity from the twelve controls you have "
              "identified so far."),
        build="A governance operating model diagram, committee terms of reference, six role descriptions and a RACI matrix covering twelve AI governance controls.",
        services="Org chart (novabank-org-chart.md), role catalogue, RACI template",
        steps=[
            ("Open novabank-org-chart.md in labs/lab-07-operating-model/data/ and identify which existing forums and roles you can reuse. Building a parallel governance structure is a known failure mode — reuse first.", ""),
            ("Define the AI Governance Committee: purpose, membership, chair, quorum, meeting frequency and — critically — its decision rights. A committee that can only advise cannot govern.", ""),
            ("Write the escalation path: which decisions the committee takes, which go to the executive risk committee, and which reach the board. Name the trigger for each escalation.", ""),
            ("Define six roles with one paragraph each: Executive Accountable Owner, AI Governance Lead, AI System Owner, Data Protection Officer, Security Lead and Model/Agent Developer.", ""),
            ("For each role state the one decision that role owns outright. If two roles claim the same decision, resolve it now — that conflict will otherwise surface during an incident.", ""),
            ("Build the RACI across twelve controls: inventory maintenance, risk assessment, data approval, model approval, pre-deployment testing, deployment sign-off, human-oversight design, monitoring, logging, incident response, third-party AI review and decommissioning.", ""),
            ("Apply the single-A rule: exactly one Accountable per control. Multiple A's mean nobody is accountable — fix every row that breaks this rule.", ""),
            ("Cross-check the RACI against NIST GOVERN 2.1 roles and responsibilities and GOVERN 2.3 executive accountability, and record how your model satisfies each.", ""),
            ("Stress-test the model: walk through the Lab 3 NovaAssist prompt-injection incident and confirm your model shows who detects it, who decides to disable the agent, and who notifies the PDPC if personal data was exposed.", ""),
        ],
        test=("Every one of the twelve controls has exactly one Accountable role. Walking the NovaAssist incident through your model "
              "produces a named person at every step, with no gaps and no two people claiming the same decision."),
    ),
    dict(
        num=8, topic=2,
        title="Apply the PDPA and PDPC AI Advisory Guidelines",
        objective="Evaluate the lawful basis for using personal data in AI systems under Singapore's PDPA and apply the PDPC AI advisory guidelines to four scenarios.",
        desc=("Singapore-specific compliance is where many AI projects stall. You will assess four NovaBank AI use cases "
              "against the PDPA obligations and the PDPC Advisory Guidelines on the Use of Personal Data in AI "
              "Recommendation and Decision Systems, and determine the lawful basis and the required notifications."),
        build="A PDPA compliance determination for four AI use cases, each with lawful basis, required notification, accountability measures and documentation.",
        services="PDPA scenario pack (pdpa-scenarios.md), PDPC guidelines summary, determination worksheet",
        steps=[
            ("Open pdpa-scenarios.md in labs/lab-08-pdpa-application/data/. The four scenarios are: a product recommendation model, a credit-decision support model, a staff-facing GenAI assistant, and a third-party developed fraud model.", ""),
            ("For scenario 1, the recommendation model, assess whether the Business Improvement Exception applies. Check the purpose against the exception's conditions and record whether fresh consent is needed.", ""),
            ("For scenario 2, the credit decision support model, note that it materially affects an individual. Determine the notification required and the human-oversight measure that must accompany the decision.", ""),
            ("For scenario 3, the staff GenAI assistant, identify the risk that customer personal data is pasted into prompts. Determine the controls: data classification rules, input filtering, logging and retention limits.", ""),
            ("For scenario 4, the third-party fraud model, identify the developer's status as a data intermediary and the Protection and Retention Obligations that follow, plus the contractual terms you require.", ""),
            ("For every scenario record the Consent and Notification position: whether consent is relied on, whether an exception applies, and exactly what must be told to the individual.", ""),
            ("Apply the Accountability Obligation to all four: what policies, records and internal processes must NovaBank be able to produce if the PDPC asks.", ""),
            ("Record the data-protection measures the PDPC guidelines expect when personal data is used in AI development: minimisation, anonymisation or pseudonymisation where feasible, access control and retention limits.", ""),
            ("Write the one-paragraph determination for each scenario: lawful basis, notification, controls, documentation and the residual legal risk you would escalate to the DPO.", ""),
        ],
        test=("Each of the four scenarios has a stated lawful basis with a reason. You can explain the difference between the Business "
              "Improvement Exception and the Research Exception in one sentence, and say which scenario needs the strongest human-oversight measure and why."),
    ),
]
