# Governance Controls

Map risk categories to practical controls teams can implement immediately.

## Control 1: Agent inventory

Maintain a live inventory of all production and pilot agents.

Minimum fields:

- Owner
- Purpose
- Data sources
- Tools/connectors
- Autonomy level
- Risk tier
- Approval status

## Control 2: Agentic risk tiering

Classify agents by behavior and impact.

Core questions:

- Can it write to systems?
- Can it trigger external communication?
- Can it act without user prompts?
- Can it affect legal/financial outcomes?

## Control 3: Tool permission matrix

Define explicit policy for each tool.

For each tool:

- Allowed/blocked
- Read/write scope
- Approval required
- Threshold limits
- Logging requirements

## Control 4: Human approval points

Require approval for high-impact or irreversible actions.

Common approval-trigger categories:

- Financial transactions
- Legal commitments
- HR decisions
- Customer-impacting actions

## Control 5: Adversarial testing

Test for instruction attacks and tool misuse before production.

Minimum test set:

- Prompt injection
- Data exfiltration attempts
- Unauthorized tool calls
- Approval bypass attempts

## Control 6: Runtime audit logging

Capture full execution traces, not only final outputs.

Minimum event fields:

- Trigger source
- Agent ID
- Prompt/instruction version
- Tool calls and arguments
- Policy decisions
- Human approvals
- Final action

## Control 7: Monitoring and kill switches

Monitor behavioral anomalies and provide fast containment.

Required capabilities:

- Unexpected tool usage alerts
- Error and retry spike detection
- Pause/revoke procedures

## Control 8: Lifecycle reviews

Review agent risk posture when key conditions change.

Trigger events:

- New tool or data source
- Increased autonomy
- Model/provider change
- Incident occurrence
