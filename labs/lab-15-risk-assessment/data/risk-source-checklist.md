# Risk Identification Checklist — draw your twelve risks from these sources

## From Lab 3 (lethal trifecta / NIST AI 600-1)
☐ Information Security — prompt injection leading to data disclosure
☐ Data Privacy — personal data in prompts, context or outputs
☐ Information Integrity — confabulated or ungrounded output relied upon
☐ Human-AI Configuration — over-reliance, no effective human check
☐ Value Chain and Component Integration — third-party model/package compromise

## From Lab 13 (OWASP ASI)
☐ ASI01 Goal hijack   ☐ ASI02 Tool misuse   ☐ ASI03 Identity & authorisation
☐ ASI06 Memory poisoning   ☐ ASI07 RAG poisoning   ☐ ASI08 Excessive agency

## From Lab 9 (data governance)
☐ Excessive data retained in the training set
☐ Re-identification from quasi-identifiers
☐ Discriminatory feature learned from proxy data (e.g. postal code)

## From Lab 8 (PDPA)
☐ No lawful basis recorded for a live use of personal data
☐ Inadequate notification for a decision materially affecting an individual
☐ Data intermediary obligations not contractually secured

## From Lab 11 (operations)
☐ No monitoring threshold configured — incident undetected
☐ Kill-switch untested / time-to-disable unknown
☐ Model or prompt changed without approval (change bypass)

## From Lab 1 (inventory)
☐ Shadow AI processing customer data outside all controls
☐ AI system with no named owner
