#!/usr/bin/env python3
"""Tool permission policy evaluator (simple YAML subset, standard library only)."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if value == "":
        return ""
    lowered = value.lower()
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    if lowered in {"null", "none"}:
        return None
    if (value.startswith('"') and value.endswith('"')) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1]
    try:
        if "." in value:
            return float(value)
        return int(value)
    except ValueError:
        return value


def parse_simple_yaml(text: str) -> dict[str, Any]:
    root: dict[str, Any] = {}
    stack: list[tuple[int, Any]] = [(-1, root)]

    for raw_line in text.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        indent = len(raw_line) - len(raw_line.lstrip(" "))
        stripped = raw_line.strip()

        while stack and indent <= stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]

        if stripped.startswith("- "):
            value = parse_scalar(stripped[2:])
            if not isinstance(parent, list):
                raise ValueError(f"List item without list parent: {raw_line}")
            parent.append(value)
            continue

        if ":" not in stripped:
            raise ValueError(f"Invalid line: {raw_line}")

        key, value = stripped.split(":", 1)
        key = key.strip()
        value = value.strip()

        if value:
            parent[key] = parse_scalar(value)
            continue

        next_container: Any = {}
        parent[key] = next_container
        stack.append((indent, next_container))

    return root


def normalize_lists(data: Any) -> Any:
    if isinstance(data, dict):
        for key, value in list(data.items()):
            if isinstance(value, dict) and value == {}:
                data[key] = []
            else:
                data[key] = normalize_lists(value)
    elif isinstance(data, list):
        return [normalize_lists(item) for item in data]
    return data


def load_yaml(path: Path) -> dict[str, Any]:
    parsed = parse_simple_yaml(path.read_text(encoding="utf-8"))
    return normalize_lists(parsed)


def evaluate_tool(policy: dict[str, Any], request: dict[str, Any]) -> dict[str, Any]:
    tools = policy.get("tools", {})
    tool_name = request.get("tool")
    params = request.get("params", {}) or {}

    tool_policy = tools.get(tool_name)
    if tool_policy is None:
        return {"decision": "deny", "reason": "tool_not_in_policy"}

    decision = str(tool_policy.get("decision", "deny"))
    constraints = tool_policy.get("constraints", {}) or {}

    if decision == "allow":
        return {"decision": "allow", "reason": "explicit_allow"}
    if decision == "deny":
        return {"decision": "deny", "reason": "explicit_deny"}
    if decision == "approval_required":
        return {"decision": "approval_required", "reason": "policy_requires_approval"}
    if decision != "constrained_allow":
        return {"decision": "deny", "reason": "unknown_decision_mode"}

    currency = constraints.get("currency")
    if currency is not None and params.get("currency") != currency:
        return {"decision": "deny", "reason": "constraint_currency_mismatch"}

    max_without_approval = constraints.get("max_amount_without_approval")
    approval_above = constraints.get("approval_required_above")
    amount = params.get("amount")

    if isinstance(amount, (int, float)):
        if isinstance(approval_above, (int, float)) and amount > approval_above:
            return {
                "decision": "approval_required",
                "reason": "constraint_amount_above_approval_threshold",
            }
        if isinstance(max_without_approval, (int, float)) and amount <= max_without_approval:
            return {"decision": "allow", "reason": "within_constrained_threshold"}

    allowed_domain = constraints.get("allowed_sender_domain")
    if isinstance(allowed_domain, str) and "sender_domain" in params:
        if params["sender_domain"] != allowed_domain:
            return {"decision": "deny", "reason": "constraint_sender_domain_not_allowed"}
        return {"decision": "allow", "reason": "sender_domain_allowed"}

    return {"decision": "allow", "reason": "constrained_allow_default_pass"}


def cmd_evaluate(args: argparse.Namespace) -> int:
    policy = load_yaml(Path(args.policy))
    request = load_yaml(Path(args.request))
    result = evaluate_tool(policy, request)
    print(json.dumps(result, indent=2))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="policy-evaluator")
    sub = parser.add_subparsers(dest="command", required=True)

    evaluate = sub.add_parser("evaluate", help="Evaluate a tool request against a policy")
    evaluate.add_argument("policy", help="Path to policy YAML")
    evaluate.add_argument("request", help="Path to request YAML")
    evaluate.set_defaults(func=cmd_evaluate)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
