# Lab 1 — Build the AI System Inventory for NovaBank

**Course:** AI Security Governance for Businesses (TGS-2026061329)  ·  **Topic 01:** AI Security Governance Foundations and Business Risks

**Objective.** Analyse an organisation's AI footprint and produce the AI system inventory that every other governance control depends on.

**Goal.** You are the newly appointed AI Governance Lead at NovaBank, a mid-sized Singapore retail bank. Nobody can tell you how many AI systems the bank runs. You will work from the supplied discovery pack — an IT asset extract, a procurement export and a staff survey — to identify every AI system, classify it, and produce a defensible AI system inventory with named owners and risk tiers.

**What you'll build.** A completed AI System Inventory (ai-inventory.csv) covering 12 AI systems with owner, purpose, data classes, model, autonomy level and risk tier, plus a shadow-AI findings note.

**Tools and data.** Mock data pack (discovery-it-assets.csv, discovery-procurement.csv, discovery-staff-survey.csv), spreadsheet tool

## Data files in this lab

- `data/discovery-it-assets.csv`
- `data/discovery-procurement.csv`
- `data/discovery-staff-survey.csv`

## Step-by-step

1. Open the three discovery files in labs/lab-01-ai-inventory/data/ and read the column headings before you filter anything. Note that no single file contains the whole picture.
2. Identify AI systems in discovery-it-assets.csv. Flag any row whose vendor, product name or description indicates a model, assistant, copilot, chatbot, scoring engine or agent.
3. Cross-check discovery-procurement.csv for AI services bought outside IT — look for line items charged to a business cost centre rather than to IT.
4. Read discovery-staff-survey.csv for shadow AI: tools staff use that appear in neither of the other two files. These are your highest-priority findings.
5. Merge into one register. For each system record: System ID, Name, Business owner, Purpose, Data classes touched, Model/vendor, Hosting, Autonomy level, Personal data (Y/N).
6. Assign an autonomy level to each system using the four tiers: Tier 1 supervised (suggests only), Tier 2 constrained (acts within a fixed allowlist), Tier 3 broad with monitoring, Tier 4 full autonomy.
7. Assign a risk tier (High / Medium / Low) using two questions: does it make or materially influence a decision about a person, and does it touch personal or confidential data?
8. Name an accountable owner for every system. Any system without a named human owner is itself a finding — record it as such.
9. Write a half-page shadow-AI findings note: how many unapproved tools you found, what data they touch, and the single control you would introduce first.

## Test it

Your inventory has a row for every AI system in all three files, including at least three shadow-AI tools that appear only in the staff survey. Every row has a named owner, an autonomy tier and a risk tier, and you can justify each High rating in one sentence.

---

> Training use only. The organisation, data and individuals in this lab are fictional.
> Security techniques taught here must only be applied to systems you own or have written
> authorisation to test.
