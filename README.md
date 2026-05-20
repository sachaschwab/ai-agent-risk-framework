# AI Agent Risk Framework

A practical starter framework for teams that need to govern AI agents in real enterprise workflows.

This repository is designed for compliance teams, IT/security teams, AI architects, and engineering leads who need a shared language and a first operating baseline for agent risk.

## What this is

This is a lightweight, implementation-oriented framework to help teams answer:

1. What kind of agent are we dealing with?
2. What are the primary risks?
3. How do those risks map to broad AI risk frameworks such as the MIT AI Risk Repository?
4. What controls should we apply first?

## Core idea

An agent is a product category. Agentic behavior is a risk property.

Do not govern labels. Govern behavior.

## Who this is for

- Compliance and legal teams
- IT and security leaders
- AI architects and engineering leads
- Product and business owners deploying agentic workflows

## Start here

1. Read [agent-levels.md](docs/agent-levels.md)
2. Review [risk-taxonomy.md](docs/risk-taxonomy.md)
3. Score the risk with [risk-scoring-model.md](docs/risk-scoring-model.md)
4. Assess the agent with the [Agent Risk Assessment](assessment/README.md) templates and CLI
5. Define tool controls with the [Tool Permissions Matrix](tool-permissions/README.md)
6. Run [ai-agent-first-review-checklist.md](checklists/ai-agent-first-review-checklist.md) on one real agent
7. Fill in [agent-risk-summary-template.md](templates/agent-risk-summary-template.md)
8. Add open risks to [risk-register-template.csv](templates/risk-register-template.csv)

## Repository structure

- `docs/`: framework definitions and control guidance
- `assessment/`: pre-production assessment template, completed example, YAML example, and scoring CLI
- `tool-permissions/`: policy format, example policies, Python/TypeScript evaluators, tests, and static tool preview
- `checklists/`: fast operational review checklists
- `templates/`: reusable governance templates
- `examples/`: sample agent profiles and risk summaries

## Current scope

- Five-level agent behavior model
- 12-category agent risk taxonomy with `AAR-*` IDs
- Practical sub-risk layer with `AAR-xx.yy` IDs
- MIT AI Risk Repository parent-domain mapping
- Risk register template
- Initial risk scoring model
- Initial controls map
- Agent risk assessment template and basic scoring CLI
- Static HTML agent risk assessment tool preview
- Tool permission matrix examples with allow/deny/approval/constrained-allow policies
- Python and TypeScript policy evaluators with decision tests
- Static HTML tool permission matrix preview
- First-pass review checklist
- Agent risk summary template
- Example agent profiles

## Agent risk assessment CLI

From `assessment/`:

```bash
../bin/agent-risk score examples/customer-support-agent.yaml
```

Or, if `bin/` is on your `PATH`:

```bash
agent-risk score examples/customer-support-agent.yaml
```

## What is intentionally out of scope for now

- Full article-by-article regulatory control mapping
- Full evidence-by-evidence mapping to every row in the MIT AI Risk Database
- Automated scoring engine
- End-to-end policy enforcement code

These can be added in subsequent iterations.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
