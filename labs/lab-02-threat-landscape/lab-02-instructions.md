# Lab 2 — Map the AI Threat Landscape with the Threat Simulator

**Course:** AI Security Governance for Businesses (TGS-2026061329)  ·  **Topic 01:** AI Security Governance Foundations and Business Risks

**Objective.** Analyse how traditional security threats and AI-specific threats combine in an AI-enabled business, and explain the business impact of each.

**Goal.** Governance decisions are only as good as your understanding of the threats. You will use the browser-based Cybersecurity Threat Simulator to experience the classic attack classes hands-on, then extend each one into its AI-era equivalent and record the business impact for NovaBank.

**What you'll build.** A completed Threat-to-Business-Impact map covering 8 threat classes, each with its AI-era variant, the NovaBank asset at risk and a first-line control.

**Tools and data.** Cybersecurity Threat Simulator (https://alfredang.github.io/cybersecuritysimulator/), threat-map worksheet

## Data files in this lab

- `data/threat-map-worksheet.csv`

## Step-by-step

1. Open https://alfredang.github.io/cybersecuritysimulator/ and review the Dashboard. Note the ten threat modules and the risk classification each one carries.
2. Run the Phishing module. Classify at least eight emails as Safe or Phishing, then read the annotated walkthrough and record the red flags you missed.
3. Run the SQL Injection module in vulnerable mode. Enter admin as the username and ' OR '1'='1 as the password, and read the live query display to see exactly why the login succeeds.

   ```
   admin  /  ' OR '1'='1
   ```

4. Run the XSS module. Type a script-like string and compare the unsafe rendering against the correctly escaped output. Note that the fix is output encoding, not input blocking alone.
5. Run the Password Lab. Test a weak password and a passphrase, and record the entropy in bits and the estimated crack time for each.
6. Run the Social Engineering trainer. Work through the scenarios and record your score, then note which tactic — pretexting, baiting, vishing, smishing or BEC — you found hardest to spot.
7. Run the Data Leakage risk estimator. Toggle encryption at rest, access controls, private buckets, protected backups, training and DLP, and record how the risk score responds to each control.
8. For each of the eight threat classes above, write the AI-era variant in your worksheet: phishing becomes GenAI-crafted spear-phishing at scale; SQL injection becomes prompt injection into a tool-calling agent; XSS becomes unsafe rendering of model output; weak passwords become over-scoped agent credentials; social engineering becomes model manipulation; data leakage becomes training-data and context-window leakage.
9. Complete the map: for each row add the NovaBank asset at risk, the business impact in one sentence, and the single most effective first-line control.

## Test it

Your map has all eight threat classes with both the traditional and the AI-era variant filled in. You can state, from the simulator, why parameterised queries stop SQL injection, and explain in one sentence why the same reasoning does not fully stop prompt injection.

---

> Training use only. The organisation, data and individuals in this lab are fictional.
> Security techniques taught here must only be applied to systems you own or have written
> authorisation to test.
