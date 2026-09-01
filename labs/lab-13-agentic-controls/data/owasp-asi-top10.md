# OWASP Agentic Security Initiative (ASI) Top 10 — Reference

| ID | Risk | What it looks like in practice | Control that addresses it |
|---|---|---|---|
| ASI01 | **Goal Hijack** | Prompt injection redirects the agent's objective away from the user's request | Treat retrieved content as data not instructions; separate untrusted-content handling from privileged tools |
| ASI02 | **Tool Misuse** | The agent calls a legitimate tool for an unintended purpose | Permission ladder per tool; deny rules on dangerous parameter patterns |
| ASI03 | **Identity & Authorisation** | Missing or over-broad authentication; shared service identity | Per-agent identity, scoped short-lived credentials, audience-bound tokens |
| ASI04 | **Supply Chain** | Compromised dependency, package or model artefact | Pin versions in lockfiles; pin actions by commit SHA; scan in CI |
| ASI05 | **Code Execution** | Untrusted code runs on agent infrastructure | OS-level sandbox, restricted egress, no shared credentials in the sandbox |
| ASI06 | **Memory Poisoning** | Malicious content contaminates persistent agent memory | Validate what enters memory; scope and expire memory; review before reuse |
| ASI07 | **RAG Poisoning** | Malicious documents planted where retrieval will find them | Control what can be indexed; provenance on retrieved chunks |
| ASI08 | **Excessive Agency** | The agent has capabilities beyond what its task requires | Least agency: constrain what it may DECIDE, separately from what it may access |
| ASI09 | **Improper Model Isolation** | The model reaches functions outside its intended scope | Tool allowlist per agent; enforce at the gateway, not in the prompt |
| ASI10 | **Operator-Facing Safety** | Insufficient human oversight; approval fatigue | Gate irreversible actions; tune volume so approval stays meaningful |

## The lethal trifecta (Simon Willison)
**Private data access + exposure to untrusted content + ability to communicate externally.**
An agent with all three can be steered by an attacker into disclosing data through permitted
actions. Removing any one leg is worth more than any filter added to a design that keeps all three.

## What guardrails CANNOT do
Content filters inspect text. They do not enforce tool authorisation, filesystem or network
boundaries, credential scope, irreversibility of side effects, or supply-chain validity.
