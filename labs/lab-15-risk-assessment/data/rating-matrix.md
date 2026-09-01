# 5x5 Risk Rating Matrix

## Likelihood
| Score | Label | Guide |
|---|---|---|
| 1 | Rare | Not expected in 5 years |
| 2 | Unlikely | Once in 3–5 years |
| 3 | Possible | Once a year |
| 4 | Likely | Several times a year |
| 5 | Almost certain | Monthly or more; or already happening |

## Impact
| Score | Label | Financial | Regulatory | Customer | Reputation |
|---|---|---|---|---|---|
| 1 | Insignificant | <SGD 10k | None | <10 affected | None |
| 2 | Minor | 10k–100k | Internal finding | 10–100 | Local complaint |
| 3 | Moderate | 100k–500k | Regulator informed | 100–1,000 | Trade press |
| 4 | Major | 500k–2m | Enforcement action | 1,000–10,000 | National press |
| 5 | Severe | >SGD 2m | Licence condition / penalty | >10,000 | Sustained national coverage |

## Score bands
| Score | Band | Required action |
|---|---|---|
| 1–6 | **Low** | Tolerate with monitoring |
| 8–12 | **Medium** | Treat within the plan cycle |
| 15–25 | **High** | Treat now, or formal acceptance by the executive owner |

## Writing a risk statement
A risk statement has three parts: **cause → event → consequence.**

❌ "Prompt injection"  — this is a cause, not a risk.
✅ "Untrusted content in inbound customer e-mail injects instructions into NovaAssist (cause),
causing the agent to include other customers' account data in outbound replies (event),
resulting in a reportable PDPA breach affecting several hundred individuals (consequence)."

## Honest residual rating
Guardrails and detection usually reduce **likelihood**. They rarely reduce **impact** — if the
data still leaves, it still leaves. Only architectural change (breaking a trifecta leg, removing
an outbound channel) reduces impact. Rate accordingly.
