# Agent Risk Assessment Form

Use this form before an AI agent is approved for production.

## 1. Agent Profile

| Field | Value |
| --- | --- |
| Agent name |  |
| Business owner |  |
| Technical owner |  |
| Support owner |  |
| Incident owner |  |
| Intended purpose |  |
| Business process |  |
| Primary users |  |
| Affected parties |  |
| Deployment channel |  |
| Launch scope |  |
| Production trigger |  |

## 2. Autonomy

| Score | Level | Description |
| --- | --- | --- |
| 0 | Answer only | The agent answers questions and does not take action |
| 1 | Recommend | The agent suggests actions, but a human performs them |
| 2 | Act with approval | The agent can prepare or execute actions after explicit approval |
| 3 | Act autonomously | The agent can act from triggers or complete steps without case-by-case approval |

Selected score:

Rationale:

Questions:

- Can the agent run without a user message?
- Can it complete more than one step before returning to a human?
- Can it decide which tool to call?
- Can it decide when a task is complete?
- Can it retry, escalate, delegate, or change plans?
- Can it affect customer, employee, finance, legal, security, or infrastructure state?

## 3. Tool Access

| Score | Level | Description |
| --- | --- | --- |
| 0 | No tools | The agent only generates responses |
| 1 | Read-only tools | The agent can retrieve data but cannot change systems |
| 2 | Limited write tools | The agent can create drafts, tickets, notes, or low-impact records |
| 3 | High-impact tools | The agent can change customer, finance, HR, legal, security, or infrastructure state |

Selected score:

Rationale:

Tool inventory:

| Tool | Read/write | Purpose | Identity | Scopes | Approval required? | Notes |
| --- | --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |  |

## 4. Data Sensitivity

| Score | Level | Description |
| --- | --- | --- |
| 0 | Public | Public information only |
| 1 | Internal | Non-public business information with low sensitivity |
| 2 | Confidential or personal | Customer, employee, commercial, contractual, or operational data |
| 3 | Restricted or regulated | Special category personal data, credentials, secrets, payment data, legal privilege, regulated records, or security-sensitive information |

Selected score:

Rationale:

Data sources:

| Data source | Data category | Sensitivity | Purpose | Retention | Notes |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

## 5. Human Oversight

Describe the review and approval design:

- Who reviews?
- What do they see?
- What decisions can they make?
- Can they reject, edit, escalate, pause, or stop the agent?
- Is approval captured in an audit log?
- What happens if the reviewer is unavailable?

Approval points:

| Action | Approval threshold | Approver | Evidence captured |
| --- | --- | --- | --- |
|  |  |  |  |

## 6. Business Impact

| Score | Level | Description |
| --- | --- | --- |
| 0 | Minimal | Minor inconvenience or easily corrected output |
| 1 | Low | Internal rework, limited user confusion, or small operational cost |
| 2 | Moderate | Customer impact, compliance evidence gap, financial loss, data exposure, or process disruption |
| 3 | Severe | Material legal, financial, safety, rights, security, regulatory, or reputational harm |

Selected score:

Rationale:

Failure modes:

- Incorrect answer
- Overconfident recommendation
- Prompt injection
- Wrong tool arguments
- Sensitive data exposure
- Approval bypass
- Silent failure
- Scaled repeated action
- Missing audit evidence

## 7. Final Risk Tier

| Tier | Production posture |
| --- | --- |
| Low | Standard review, owner assigned, basic logging |
| Medium | Security/privacy review, access controls, monitoring, user guidance |
| High | Architecture review, approval workflow, audit logging, testing, incident plan, risk acceptance |
| Unacceptable without redesign | Do not launch until redesigned |

Final tier:

Required controls:

- [ ] Named business owner and technical owner
- [ ] Approved use-case intake
- [ ] Inventory entry
- [ ] Tool permission matrix
- [ ] Data classification and privacy review where needed
- [ ] Human oversight design
- [ ] Logging and traceability plan
- [ ] Prompt injection and misuse testing for tool-using agents
- [ ] Monitoring and alerting plan
- [ ] Incident response owner and escalation path
- [ ] Review date and reassessment trigger

Decision:

Approver:

Review date:

Reassessment trigger:
