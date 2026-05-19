#!/usr/bin/env python3
"""Basic AI agent risk scoring CLI.

This script intentionally uses only the Python standard library. It supports
the simple YAML shape used by the examples in this repository.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


SCORE_FIELDS = (
    "autonomy_score",
    "tool_access_score",
    "data_sensitivity_score",
    "business_impact_score",
)

FIELD_LABELS = {
    "autonomy_score": "Autonomy",
    "tool_access_score": "Tool access",
    "data_sensitivity_score": "Data sensitivity",
    "business_impact_score": "Business impact",
}

TIER_ORDER = {
    "Low": 1,
    "Medium": 2,
    "High": 3,
    "Unacceptable without redesign": 4,
}

CRITICAL_RED_FLAGS = (
    "no_business_owner",
    "no_logging",
    "excessive_permissions",
    "irreversible_action_without_approval",
    "unclear_legal_basis_for_personal_data",
)


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
        return int(value)
    except ValueError:
        return value


def parse_simple_yaml(text: str) -> dict[str, Any]:
    """Parse the small YAML subset used by the assessment examples.

    Supported patterns:
    - top-level `key: value`
    - top-level lists with scalar items
    - nested dictionaries
    - lists of dictionaries, one indentation level below a key
    """

    root: dict[str, Any] = {}
    lines = [line.rstrip() for line in text.splitlines()]
    i = 0

    while i < len(lines):
        raw = lines[i]
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            i += 1
            continue
        if raw.startswith(" "):
            raise ValueError(f"Unexpected indentation at line {i + 1}: {raw}")
        if ":" not in raw:
            raise ValueError(f"Expected key/value at line {i + 1}: {raw}")

        key, value = raw.split(":", 1)
        key = key.strip()
        value = value.strip()

        if value:
            root[key] = parse_scalar(value)
            i += 1
            continue

        nested: list[str] = []
        i += 1
        while i < len(lines) and (lines[i].startswith("  ") or not lines[i].strip()):
            if lines[i].strip():
                nested.append(lines[i])
            i += 1

        root[key] = parse_nested_block(nested)

    return root


def parse_nested_block(lines: list[str]) -> Any:
    if not lines:
        return {}

    first = lines[0].strip()
    if first.startswith("- "):
        return parse_list(lines)
    return parse_dict(lines)


def parse_dict(lines: list[str]) -> dict[str, Any]:
    data: dict[str, Any] = {}
    for raw in lines:
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if ":" not in stripped:
            raise ValueError(f"Expected nested key/value: {raw}")
        key, value = stripped.split(":", 1)
        data[key.strip()] = parse_scalar(value)
    return data


def parse_list(lines: list[str]) -> list[Any]:
    items: list[Any] = []
    current: dict[str, Any] | None = None

    for raw in lines:
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("- "):
            item = stripped[2:].strip()
            if ":" in item:
                key, value = item.split(":", 1)
                current = {key.strip(): parse_scalar(value)}
                items.append(current)
            else:
                current = None
                items.append(parse_scalar(item))
            continue
        if current is None:
            raise ValueError(f"Unexpected list continuation: {raw}")
        if ":" not in stripped:
            raise ValueError(f"Expected list item key/value: {raw}")
        key, value = stripped.split(":", 1)
        current[key.strip()] = parse_scalar(value)

    return items


def load_profile(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if path.suffix.lower() == ".json":
        return json.loads(text)
    return parse_simple_yaml(text)


def require_score(profile: dict[str, Any], field: str) -> int:
    raw = profile.get(field)
    if not isinstance(raw, int):
        raise ValueError(f"{field} must be an integer from 0 to 3")
    if raw < 0 or raw > 3:
        raise ValueError(f"{field} must be between 0 and 3")
    return raw


def red_flags(profile: dict[str, Any]) -> dict[str, bool]:
    raw = profile.get("red_flags", {})
    if not isinstance(raw, dict):
        return {}
    return {key: bool(raw.get(key, False)) for key in CRITICAL_RED_FLAGS}


def assign_tier(scores: dict[str, int], flags: dict[str, bool]) -> str:
    if any(flags.values()):
        return "Unacceptable without redesign"

    max_score = max(scores.values())
    total = sum(scores.values())

    if max_score == 3 or total >= 9:
        return "High"
    if max_score == 2 or total >= 5:
        return "Medium"
    return "Low"


def required_controls(tier: str, profile: dict[str, Any]) -> list[str]:
    controls = [
        "Named business and technical owners",
        "Inventory entry",
        "Basic logging",
        "Review date and reassessment trigger",
    ]

    if TIER_ORDER[tier] >= TIER_ORDER["Medium"]:
        controls.extend(
            [
                "Security/privacy review",
                "Least-privilege tool and data access review",
                "Monitoring owner",
            ]
        )

    if TIER_ORDER[tier] >= TIER_ORDER["High"]:
        controls.extend(
            [
                "Architecture review",
                "Human approval workflow for high-impact actions",
                "Prompt injection and tool misuse tests",
                "Audit log for request, context, tool calls, approvals, and final action",
                "Incident response path",
                "Explicit risk acceptance",
            ]
        )

    if tier == "Unacceptable without redesign":
        controls.insert(0, "Do not launch until critical red flags are remediated")

    if profile.get("tool_access_score") == 3:
        controls.append("Tool permission matrix for high-impact tools")
    if profile.get("data_sensitivity_score") >= 2:
        controls.append("Data classification and privacy review")

    return list(dict.fromkeys(controls))


def score_profile(profile: dict[str, Any]) -> dict[str, Any]:
    scores = {field: require_score(profile, field) for field in SCORE_FIELDS}
    flags = red_flags(profile)
    tier = assign_tier(scores, flags)
    return {
        "agent_name": profile.get("name", "Unnamed agent"),
        "business_owner": profile.get("business_owner", ""),
        "technical_owner": profile.get("technical_owner", ""),
        "scores": scores,
        "score_total": sum(scores.values()),
        "max_score": max(scores.values()),
        "red_flags": flags,
        "risk_tier": tier,
        "required_controls": required_controls(tier, profile),
    }


def print_text(result: dict[str, Any]) -> None:
    print(f"Agent: {result['agent_name']}")
    if result["business_owner"]:
        print(f"Business owner: {result['business_owner']}")
    if result["technical_owner"]:
        print(f"Technical owner: {result['technical_owner']}")
    print()
    print("Scores")
    for field, value in result["scores"].items():
        print(f"- {FIELD_LABELS[field]}: {value}")
    print(f"- Total: {result['score_total']}")
    print(f"- Max score: {result['max_score']}")
    print()
    print(f"Risk tier: {result['risk_tier']}")

    active_flags = [key for key, value in result["red_flags"].items() if value]
    if active_flags:
        print()
        print("Critical red flags")
        for flag in active_flags:
            print(f"- {flag}")

    print()
    print("Required controls")
    for control in result["required_controls"]:
        print(f"- {control}")


def score_command(args: argparse.Namespace) -> int:
    profile = load_profile(Path(args.profile))
    result = score_profile(profile)
    if args.format == "json":
        print(json.dumps(result, indent=2))
    else:
        print_text(result)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="agent-risk")
    subparsers = parser.add_subparsers(dest="command", required=True)

    score = subparsers.add_parser("score", help="score an agent YAML or JSON profile")
    score.add_argument("profile", help="path to an agent profile YAML or JSON file")
    score.add_argument("--format", choices=("text", "json"), default="text")
    score.set_defaults(func=score_command)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"agent-risk: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
