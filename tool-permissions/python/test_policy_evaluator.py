from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parent))

from policy_evaluator import evaluate_tool, load_yaml


ROOT = Path(__file__).resolve().parents[1]
POLICY = ROOT / "examples" / "policies" / "customer-support-policy.yaml"


class PolicyEvaluatorTests(unittest.TestCase):
    def test_allow_under_threshold(self) -> None:
        policy = load_yaml(POLICY)
        request = load_yaml(ROOT / "examples" / "requests" / "refund-under-threshold.yaml")
        result = evaluate_tool(policy, request)
        self.assertEqual(result["decision"], "allow")

    def test_approval_over_threshold(self) -> None:
        policy = load_yaml(POLICY)
        request = load_yaml(ROOT / "examples" / "requests" / "refund-over-threshold.yaml")
        result = evaluate_tool(policy, request)
        self.assertEqual(result["decision"], "approval_required")

    def test_deny_explicit(self) -> None:
        policy = load_yaml(POLICY)
        request = load_yaml(ROOT / "examples" / "requests" / "delete-account.yaml")
        result = evaluate_tool(policy, request)
        self.assertEqual(result["decision"], "deny")


if __name__ == "__main__":
    unittest.main()
