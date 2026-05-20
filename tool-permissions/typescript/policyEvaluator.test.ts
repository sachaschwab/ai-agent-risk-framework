import { evaluateTool, type Policy } from './policyEvaluator';

const policy: Policy = {
  tools: {
    issue_refund: {
      decision: 'constrained_allow',
      constraints: {
        currency: 'EUR',
        max_amount_without_approval: 100,
        approval_required_above: 100,
      },
    },
    delete_customer_account: {
      decision: 'deny',
    },
    send_customer_email: {
      decision: 'approval_required',
    },
  },
};

function assertEqual(actual: unknown, expected: unknown, label: string): void {
  if (actual !== expected) {
    throw new Error(`${label}: expected ${String(expected)} but got ${String(actual)}`);
  }
}

export function runTests(): void {
  const allow = evaluateTool(policy, {
    tool: 'issue_refund',
    params: { currency: 'EUR', amount: 50 },
  });
  assertEqual(allow.decision, 'allow', 'allow case');

  const approval = evaluateTool(policy, {
    tool: 'issue_refund',
    params: { currency: 'EUR', amount: 200 },
  });
  assertEqual(approval.decision, 'approval_required', 'approval case');

  const deny = evaluateTool(policy, {
    tool: 'delete_customer_account',
    params: { customer_id: 'CUST-1' },
  });
  assertEqual(deny.decision, 'deny', 'deny case');
}
