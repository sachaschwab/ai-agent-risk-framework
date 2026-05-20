export type Decision = 'allow' | 'deny' | 'approval_required' | 'constrained_allow';

export type ToolPolicy = {
  decision: Decision;
  access?: 'read' | 'write' | 'admin' | 'draft';
  constraints?: {
    currency?: string;
    max_amount_without_approval?: number;
    approval_required_above?: number;
    allowed_sender_domain?: string;
  };
};

export type Policy = {
  policy_name?: string;
  version?: string;
  tools: Record<string, ToolPolicy>;
};

export type ToolRequest = {
  tool: string;
  params?: Record<string, unknown>;
};

export type EvalResult = {
  decision: 'allow' | 'deny' | 'approval_required';
  reason: string;
};

export function evaluateTool(policy: Policy, request: ToolRequest): EvalResult {
  const toolPolicy = policy.tools[request.tool];
  const params = request.params ?? {};

  if (!toolPolicy) {
    return { decision: 'deny', reason: 'tool_not_in_policy' };
  }

  if (toolPolicy.decision === 'allow') {
    return { decision: 'allow', reason: 'explicit_allow' };
  }
  if (toolPolicy.decision === 'deny') {
    return { decision: 'deny', reason: 'explicit_deny' };
  }
  if (toolPolicy.decision === 'approval_required') {
    return { decision: 'approval_required', reason: 'policy_requires_approval' };
  }

  const c = toolPolicy.constraints ?? {};
  if (c.currency && params.currency !== c.currency) {
    return { decision: 'deny', reason: 'constraint_currency_mismatch' };
  }

  const amount = typeof params.amount === 'number' ? params.amount : undefined;
  if (amount !== undefined) {
    if (typeof c.approval_required_above === 'number' && amount > c.approval_required_above) {
      return { decision: 'approval_required', reason: 'constraint_amount_above_approval_threshold' };
    }
    if (typeof c.max_amount_without_approval === 'number' && amount <= c.max_amount_without_approval) {
      return { decision: 'allow', reason: 'within_constrained_threshold' };
    }
  }

  if (typeof c.allowed_sender_domain === 'string' && typeof params.sender_domain === 'string') {
    if (params.sender_domain !== c.allowed_sender_domain) {
      return { decision: 'deny', reason: 'constraint_sender_domain_not_allowed' };
    }
    return { decision: 'allow', reason: 'sender_domain_allowed' };
  }

  return { decision: 'allow', reason: 'constrained_allow_default_pass' };
}
