# Agent Risk Assessment

Use this module to assess an AI agent before production.

It turns the article-level assessment model into a practical artifact:

- Spreadsheet-style CSV template
- Markdown assessment form
- Example completed assessment
- Static HTML assessment tool preview
- Basic Python scoring CLI

## Assessment flow

1. Fill in `agent-risk-assessment-form.md` for the agent.
2. Capture row-level values in `agent-risk-assessment-template.csv` if your review process uses spreadsheets.
3. Open `agent-risk-assessment-tool.html` to preview a simple browser-only scoring GUI.
4. Score a YAML profile with the CLI.
5. Store the final assessment and risk acceptance evidence with the agent inventory.

## CLI quick start

From this `assessment/` directory:

```bash
../bin/agent-risk score examples/customer-support-agent.yaml
```

If you add `bin/` to your `PATH`, you can also run:

```bash
agent-risk score examples/customer-support-agent.yaml
```

The scorer is intentionally simple. It is designed to make assessment criteria explicit, not to replace review judgment.

## Risk tiers

The CLI scores four dimensions from 0 to 3:

- Autonomy
- Tool access
- Data sensitivity
- Business impact

It then assigns a tier:

| Tier | Rule of thumb |
| --- | --- |
| Low | Low scores, no red flags |
| Medium | Moderate score or moderate total |
| High | Any score at 3, high total, or high-impact red flag |
| Unacceptable without redesign | Critical red flags such as no owner, no logging, excessive permissions, or irreversible action without approval |

Use the generated result as an input to governance review, architecture review, and risk acceptance.
