# AI Agent Risk Scoring Model

This scoring model is intentionally simple. It helps teams compare agentic AI
risks consistently before they have enough operational data for quantitative
modeling.

## ID and mapping fields

Keep taxonomy identity separate from risk-instance identity.

| Field | Example | Purpose |
| --- | --- | --- |
| Agent taxonomy ID | `AAR-02` | Stable AI Crafters agent-risk category. |
| Agent sub-risk ID | `AAR-02.03` | Practical child risk used for concrete control design. |
| Register risk ID | `R-017` | Concrete risk instance for one agent, workflow, or deployment. |
| MIT domain/subdomain | `2.2 AI system security vulnerabilities and attacks` | Broad parent mapping into the MIT AI Risk Repository. |
| MIT mapping confidence | `High`, `Medium`, `Low` | Indicates how directly the MIT parent category fits the agent-specific risk. |

Use the MIT mapping for alignment with enterprise AI risk inventories. Use the
`AAR-*` taxonomy ID for the high-level agent risk. Use the `AAR-xx.yy` sub-risk
ID when writing test cases, control requirements, and risk register entries.

## Score dimensions

Score each dimension from 1 to 5.

| Dimension | 1 | 3 | 5 |
| --- | --- | --- | --- |
| Likelihood | Unlikely in normal use | Plausible in realistic misuse or failure | Expected without strong controls |
| Impact | Low inconvenience | Material business, user, or compliance impact | Severe financial, legal, safety, or operational impact |
| Autonomy | User-triggered response only | Tool use with user involvement | Background or multi-step action without step-by-step approval |
| Data sensitivity | Public or low sensitivity | Internal or confidential business data | Personal, regulated, secret, credential, or high-value data |
| Tool criticality | No write actions | Limited write actions or internal workflow changes | External communication, payments, legal, HR, production, security, or infrastructure action |
| Observability gap | Full trace and alerting | Partial logs or delayed review | Cannot reconstruct triggers, instructions, tool calls, approvals, or actions |

## Composite score

Use the weighted score below:

```text
composite_score =
  (impact * 2)
  + likelihood
  + autonomy
  + data_sensitivity
  + tool_criticality
  + observability_gap
```

Impact is weighted because agentic failures are usually governed by consequence,
not only probability.

## Risk tiers

| Composite score | Tier | Default action |
| --- | --- | --- |
| 6-11 | Low | Track in inventory and review on material change |
| 12-17 | Medium | Require owner, basic controls, logging, and review before production |
| 18-24 | High | Require risk assessment, tool permission matrix, adversarial testing, and approval gates |
| 25-35 | Critical | Require executive risk acceptance, runtime monitoring, incident playbook, kill switch, and formal evidence pack |

## Mandatory escalation triggers

Escalate to at least High even when the numeric score is lower if the agent:

- Can initiate payments, refunds, contracts, legal notices, hiring, termination, medical, safety, security, or production infrastructure actions.
- Can access credentials, secrets, regulated personal data, confidential customer data, source code, or security logs.
- Can act without a user prompt.
- Can delegate to other agents or invoke code execution.
- Has a known prompt injection, memory poisoning, data exfiltration, or privilege escalation path that has not been mitigated.

Also escalate the mapping confidence review when:

- The MIT parent category is only a loose fit, but the concrete agent risk is high impact.
- A single risk maps to multiple MIT domains, such as privacy, malicious misuse, and system safety.
- The risk is primarily an enterprise control failure, such as missing approval gates or missing tool-call logs, rather than a broad AI harm category.

## Evidence checklist

For High and Critical risks, attach evidence for:

- Agent owner and approved use case.
- Agent taxonomy ID, agent sub-risk ID, and MIT parent mapping.
- Agent level and autonomy assessment.
- Tool permission matrix.
- Data source and memory inventory.
- Prompt injection and tool misuse test results.
- Human approval points.
- Runtime logs and monitoring rules.
- Incident response and disable procedure.
- Residual risk owner and approval record.

## Review triggers

Re-score the agent when any of these change:

- New tool, connector, API, browser, code execution, or workflow action.
- New data source or memory store.
- Higher autonomy level.
- New user group, geography, or business process.
- Model, provider, orchestration framework, or system prompt change.
- Incident, near miss, policy exception, or audit finding.
