# Example: Autonomous Finance Exception Agent

## Summary

- Agent level: 4 (Autonomous Workflow Agent)
- Purpose: Monitor reconciliation exceptions and route corrective workflows
- Main risks: wrong autonomous action, escalation failure, weak incident traceability

## Risk highlights

- Autonomy risk: high
- Business process risk: high
- Accountability risk: medium

## Initial controls

- Trigger validation rules and anomaly thresholds
- Approval gate for write actions to general ledger systems
- Kill switch owned by finance operations lead
- End-to-end tracing of event trigger, plan, tool calls, and final action
