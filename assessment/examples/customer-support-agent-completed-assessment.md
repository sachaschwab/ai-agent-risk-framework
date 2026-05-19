# Completed Agent Risk Assessment: Customer Support Refund Agent

## 1. Agent Profile

| Field | Value |
| --- | --- |
| Agent name | Customer Support Refund Agent |
| Business owner | Customer Operations |
| Technical owner | AI Platform Team |
| Support owner | Support Operations Lead |
| Incident owner | Support Operations Lead |
| Intended purpose | Prepare customer refunds from support requests |
| Business process | Customer support refunds |
| Primary users | Support agents |
| Affected parties | Customers |
| Deployment channel | Support console pilot |
| Launch scope | Internal pilot |
| Production trigger | User-initiated support case |

## 2. Scores

| Dimension | Score | Rationale |
| --- | --- | --- |
| Autonomy | 2 | The agent proposes and prepares refund actions, but approval is required before execution |
| Tool access | 3 | The refund API changes financial records |
| Data sensitivity | 2 | Customer data and order history are in scope |
| Business impact | 2 | Wrong refunds or denials create customer, financial, and compliance impact |

Final tier: **High**

## 3. Tool Inventory

| Tool | Read/write | Purpose | Approval required? |
| --- | --- | --- | --- |
| `order_lookup` | Read | Retrieve order history | No |
| `refund_api` | Write | Issue approved refunds | Yes |

## 4. Human Oversight

Supervisor approval is required before the refund API can be called.

Approval evidence must include:

- Customer request
- Retrieved refund policy
- Proposed refund amount
- Agent rationale
- Risk flags
- Approver identity
- Trace ID

## 5. Required Controls

- Refund API limited to the minimum required scope.
- Refund amount threshold configured.
- Supervisor approval before high-impact refund actions.
- Prompt injection tests using customer messages and attached documents.
- Audit logging for request, policy retrieval, proposed decision, approval, tool call, and final result.
- Monitoring owner assigned.
- Incident route documented.

## 6. Decision

Approved for controlled internal pilot.

Conditions:

- Do not enable autonomous refund execution.
- Do not expand beyond the pilot queue without reassessment.
- Reassess after any change to refund thresholds, tool permissions, retrieved policy sources, or launch scope.
