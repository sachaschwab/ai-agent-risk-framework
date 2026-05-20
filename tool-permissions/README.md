# Agent Tool Permissions Matrix

Practical module for implementing tool-level permission policy for AI agents.

## Includes

- YAML policy format
- Example policies
- Python evaluator + tests
- TypeScript evaluator + tests
- Static HTML preview tool

## Policy decisions

- `allow`
- `deny`
- `approval_required`
- `constrained_allow`

## Quick start (Python)

From this folder:

```bash
python3 python/policy_evaluator.py evaluate examples/policies/customer-support-policy.yaml examples/requests/refund-under-threshold.yaml
```

Run tests:

```bash
python3 -m unittest python/test_policy_evaluator.py
```

## Quick start (TypeScript source)

TypeScript source and tests are in:

- `typescript/policyEvaluator.ts`
- `typescript/policyEvaluator.test.ts`

The TypeScript test file mirrors the Python test scenarios (`allow`, `deny`, `approval_required`, `constrained_allow`).

## Static preview

Open:

- `tool-permission-matrix-tool.html`

It provides a browser-only interactive evaluator for sample tool actions.
