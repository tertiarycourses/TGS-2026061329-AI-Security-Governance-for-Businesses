# Governed Training Dataset Specification — TEMPLATE
System: Churn Prediction Model · Owner: ____________ · Date: ____________

## 1. Purpose and lawful basis
Purpose: ____________
Lawful basis (from Lab 8): ____________
Exception relied on and why: ____________

## 2. Field decisions
(attach your completed data dictionary)
Fields in source: 24 · Fields dropped: ____ · Fields transformed: ____ · Fields retained as-is: ____

## 3. De-identification applied
| Field | Method | Reversible? | Still personal data? |
|---|---|---|---|
| | | | |

## 4. Cryptographic controls tested (Cryptography Toolkit)
| Control | Algorithm / setting | What it protects | Observed result |
|---|---|---|---|
| Field encryption | AES-256 CBC | | |
| Identifier hashing | | | |
| Key exchange | RSA 2048 | | |
| Dataset integrity | ECDSA P-256 | | |

**Key finding to record:** encryption is reversible, so an encrypted identifier remains personal
data in the hands of the key holder. Write in one sentence why this matters for your specification.

## 5. Access control
Who may access the governed dataset · where it is stored · how access is logged.

## 6. Retention and deletion
## 7. Approval
| Role | Name | Approved | Date |
|---|---|---|---|
| Data owner | | | |
| DPO | | | |
