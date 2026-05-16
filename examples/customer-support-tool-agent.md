# Example: Customer Support Tool Agent

## Summary

- Agent level: 3 (Tool-Using Agent)
- Purpose: Retrieve order information and draft refund recommendations
- Main risks: unauthorized tool use, excessive permissions, approval bypass

## Risk highlights

- Tool risk: high
- Permission risk: high
- Observability risk: medium

## Initial controls

- Tool permission matrix with allow/deny/approval-required categories
- Human approval required for any refund action above threshold
- Mandatory audit logging of tool calls and policy decisions
- Prompt injection and unauthorized-action test suite before production
