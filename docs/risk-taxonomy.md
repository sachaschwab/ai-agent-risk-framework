# AI Agent Risk Taxonomy

This taxonomy provides a common risk language for agentic AI systems. It is
designed for enterprise teams that need to move from abstract AI governance to
operational controls, evidence, and ownership.

The taxonomy has four layers:

1. MIT AI Risk Repository parent mappings: the broad cross-AI reference layer.
2. Core risk domains: the enterprise control themes.
3. The 12 practitioner risks: the business-facing agent taxonomy.
4. Specific threat classes: the security, privacy, reliability, and governance
   threats that sit underneath the business-facing risks.
5. Control and evidence mapping: the practical bridge into a risk register.

## How to read this taxonomy

Use the taxonomy to answer four questions:

| Question | Why it matters | Output |
| --- | --- | --- |
| What can the agent do? | Agent risk is driven by behavior, not product labels | Agent level, autonomy level, tool list, data sources |
| Which risk category applies? | Teams need shared language across legal, security, IT, and business owners | One or more of the 12 practitioner risks |
| Which control can fail? | A taxonomy becomes operational only when mapped to failed or missing controls | Risk register entry with owner and mitigation |
| What evidence proves control? | Audit, incident response, and assurance need artifacts, not intentions | Logs, approvals, tests, policy files, access reviews |

## Importance levels

Importance is a default starting point. Increase it when the agent has high
autonomy, sensitive data, write-capable tools, regulated use, weak observability,
or high business impact.

| Importance | Meaning | Default governance response |
| --- | --- | --- |
| Critical | Failure can cause severe legal, financial, safety, security, privacy, or operational harm | Formal risk assessment, executive risk acceptance, approval gates, monitoring, incident playbook, kill switch |
| High | Failure can materially affect users, business processes, compliance, security, or trust | Named owner, tool permission matrix, adversarial testing, logging, human approval for high-impact actions |
| Medium | Failure can create local business harm, user confusion, rework, or policy exceptions | Review before production, basic logging, control checklist, periodic owner review |
| Low | Failure is contained, reversible, and unlikely to affect sensitive data or business outcomes | Inventory entry, lightweight review, review on material change |

## Reference basis

Use this taxonomy as a control design aid, not as legal advice. The inclusion of
each risk is grounded in one or more of these sources:

| Source | Why it is used here |
| --- | --- |
| OWASP Agentic AI - Threats and Mitigations, Version 1.1, December 2025 | Direct source for agent-specific threats including memory poisoning, tool misuse, privilege compromise, resource overload, cascading hallucination, goal manipulation, untraceability, identity compromise, human-in-the-loop overload, code attacks, multi-agent risks, human manipulation, inter-agent protocol abuse, and supply-chain compromise. The downloaded current guide lists T1-T17; older summaries may refer to T1-T15. |
| OWASP Top 10 for Large Language Model Applications 2025 | Source for common LLM application risks including prompt injection, sensitive information disclosure, supply-chain vulnerabilities, excessive agency, overreliance, and unbounded consumption. |
| NIST AI Risk Management Framework 1.0, NIST AI 100-1, January 2023 | Governance, mapping, measurement, and management structure for AI risk. |
| NIST AI RMF Generative AI Profile, NIST AI 600-1, July 2024 | Source for generative AI risks including confabulation, harmful bias, data privacy, information integrity, human-AI configuration, and value-chain/component integration. |
| MIT AI Risk Repository, Domain Taxonomy of AI Risks v1, workbook dated 03 December 2025 | Parent taxonomy for broad AI risk domains and subdomains. This framework uses MIT IDs as a reference layer, not as a replacement for agent-specific operational risks. |
| MITRE ATLAS | Knowledge base of adversary tactics and techniques against AI-enabled systems, useful for poisoning, evasion, credential, exfiltration, and supply-chain threat thinking. |
| EU AI Act, Regulation (EU) 2024/1689 | Legal reference for high-risk AI obligations including risk management, data governance, documentation, logging, transparency, human oversight, accuracy, robustness, cybersecurity, post-market monitoring, deployer obligations, and transparency duties. |
| GDPR, Regulation (EU) 2016/679 | Legal reference where personal data is processed, especially principles, security of processing, breach notification, and data protection impact assessments. |
| ISO/IEC 42001:2023 | AI management system reference for governance, responsibilities, risk management, policy lifecycle, and continual improvement. |
| NIST Cybersecurity Framework 2.0 | Cybersecurity reference for govern, identify, protect, detect, respond, and recover functions, especially identity, access, supply chain, monitoring, and risk management. |

Some frontier system-level concerns, such as self-replication, shutdown
resistance, autonomous resource acquisition, and attempts to preserve access, are
better treated as risk indicators from AI safety literature and advanced-system
evaluations unless they are directly present in the system under review.

## ID convention

Use two IDs:

| ID type | Format | Purpose |
| --- | --- | --- |
| Agent taxonomy ID | `AAR-01` to `AAR-12` | Stable AI Crafters identifier for the agent-specific risk category. |
| Agent sub-risk ID | `AAR-02.03` | Stable identifier for a concrete sub-risk under a top-level agent risk. |
| Risk register ID | `R-001`, `R-002`, ... | Instance-specific identifier for a concrete risk in one agent, workflow, or deployment. |

Example:

| Field | Example |
| --- | --- |
| Agent taxonomy ID | `AAR-02` |
| Agent sub-risk ID | `AAR-02.01` |
| Practitioner risk | Tool risk |
| MIT parent mapping | `2.2 AI system security vulnerabilities and attacks`; `7.3 Lack of capability or robustness` |
| Register risk ID | `R-017` |
| Concrete scenario | Customer support agent can issue refunds through an API without policy validation. |

## MIT AI Risk Repository parent layer

The MIT AI Risk Repository is a strong parent taxonomy for broad AI risks. It
should be used as a reference layer so this framework remains compatible with
cross-AI risk programs.

Do not use MIT's taxonomy alone as an AI agent operational taxonomy. It is broad
and literature-oriented. It does not directly express several controls that
matter for enterprise agents, such as tool permission matrices, service account
scope, approval gates, execution traces, agent memory governance, and business
process actuation.

| MIT domain | Relevant MIT subdomains for agent governance | How this framework uses it |
| --- | --- | --- |
| 1. Discrimination & Toxicity | `1.1 Unfair discrimination and misrepresentation`; `1.2 Exposure to toxic content`; `1.3 Unequal performance across groups` | Parent mapping for output quality, bias, toxicity, and discriminatory business-process outcomes. |
| 2. Privacy & Security | `2.1 Compromise of privacy by obtaining, leaking or correctly inferring sensitive information`; `2.2 AI system security vulnerabilities and attacks` | Parent mapping for data exposure, memory risk, prompt injection, tool misuse, permissions, and exfiltration. |
| 3. Misinformation | `3.1 False or misleading information`; `3.2 Pollution of information ecosystem and loss of consensus reality` | Parent mapping for hallucination, cascading false outputs, and misinformation loops. |
| 4. Malicious Actors & Misuse | `4.1 Disinformation, surveillance, and influence at scale`; `4.2 Cyberattacks, weapon development or use, and mass harm`; `4.3 Fraud, scams, and targeted manipulation` | Parent mapping for malicious use, human manipulation, cyber abuse, fraud, and adversarial exploitation. |
| 5. Human-Computer Interaction | `5.1 Overreliance and unsafe use`; `5.2 Loss of human agency and autonomy` | Parent mapping for autonomy, human oversight, overreliance, and unsafe agent-human interaction. |
| 6. Socioeconomic & Environmental | `6.4 Competitive dynamics`; `6.5 Governance failure`; `6.6 Environmental harm` | Parent mapping for accountability, compliance, policy drift, governance gaps, and resource/cost impacts. |
| 7. AI System Safety, Failures, & Limitations | `7.1 AI pursuing its own goals in conflict with human goals or values`; `7.2 AI possessing dangerous capabilities`; `7.3 Lack of capability or robustness`; `7.4 Lack of transparency or interpretability`; `7.6 Multi-agent risks` | Parent mapping for planning, autonomy, delegation, observability, robustness, unsafe actuation, and multi-agent risks. |

## Agent taxonomy to MIT mapping

| Agent taxonomy ID | Practitioner risk | Primary MIT mapping | Secondary MIT mappings | Why the MIT mapping is not enough by itself |
| --- | --- | --- | --- | --- |
| `AAR-01` | Autonomy risk | `5.2 Loss of human agency and autonomy` | `7.1 AI pursuing its own goals`; `7.3 Lack of capability or robustness`; `6.5 Governance failure` | MIT covers human agency and system safety, but not concrete approval gates, trigger validation, pause controls, or autonomy tiers. |
| `AAR-02` | Tool risk | `2.2 AI system security vulnerabilities and attacks` | `4.2 Cyberattacks`; `7.3 Lack of capability or robustness`; `6.5 Governance failure` | MIT covers security vulnerabilities, but not agent tool permission matrices, tool-call arguments, or business action allowlists. |
| `AAR-03` | Permission risk | `2.2 AI system security vulnerabilities and attacks` | `2.1 Privacy compromise`; `6.5 Governance failure` | MIT covers security and privacy compromise, but not delegated authority, service accounts, OAuth scopes, or confused deputy patterns as operational controls. |
| `AAR-04` | Instruction and prompt injection risk | `2.2 AI system security vulnerabilities and attacks` | `4.2 Cyberattacks`; `7.3 Lack of capability or robustness` | MIT has prompt-injection entries in the database, but the domain taxonomy does not expose instruction hierarchy and tool policy as first-class agent controls. |
| `AAR-05` | Memory risk | `2.1 Privacy compromise` | `2.2 AI system security vulnerabilities and attacks`; `7.3 Lack of capability or robustness` | MIT covers privacy and security, but not persistent agent memory as a governance surface with write/read/delete controls. |
| `AAR-06` | Data exposure risk | `2.1 Privacy compromise` | `2.2 AI system security vulnerabilities and attacks`; `4.3 Fraud, scams, and targeted manipulation` | MIT covers privacy compromise, but not the agent-specific ways data moves through tools, summaries, memory, logs, and lower-protection channels. |
| `AAR-07` | Planning risk | `7.3 Lack of capability or robustness` | `7.1 AI pursuing its own goals`; `3.1 False or misleading information`; `7.2 Dangerous capabilities` | MIT covers robustness and goal conflict, but not plan validation, workflow constraints, and high-impact plan approval. |
| `AAR-08` | Delegation risk | `7.6 Multi-agent risks` | `2.2 AI system security vulnerabilities and attacks`; `6.5 Governance failure`; `7.4 Lack of transparency or interpretability` | MIT has multi-agent risk, but not enterprise controls for agent identity, signed/scoped messages, and delegation allowlists. |
| `AAR-09` | Observability risk | `7.4 Lack of transparency or interpretability` | `6.5 Governance failure`; `7.3 Lack of capability or robustness` | MIT covers transparency broadly, but not runtime execution traces, tool-call logs, approval records, and incident reconstruction. |
| `AAR-10` | Accountability risk | `6.5 Governance failure` | `7.4 Lack of transparency or interpretability`; `5.2 Loss of human agency and autonomy` | MIT covers governance failure, but not named business/technical/risk owners, RACI, vendor responsibility, and residual risk acceptance. |
| `AAR-11` | Compliance risk | `6.5 Governance failure` | `2.1 Privacy compromise`; `7.4 Lack of transparency or interpretability`; `1.1 Unfair discrimination and misrepresentation` | MIT covers governance failure, but legal applicability still needs EU AI Act, GDPR, sectoral law, contracts, and internal policy mapping. |
| `AAR-12` | Business process risk | `7.3 Lack of capability or robustness` | `5.1 Overreliance and unsafe use`; `5.2 Loss of human agency and autonomy`; `6.5 Governance failure` | MIT covers unsafe use and robustness, but not concrete business process actuation, rollback, segregation of duties, and approval thresholds. |

## Core enterprise risk domains

| Domain | Theme | Default importance | What it covers | Typical failure mode | Primary owners |
| --- | --- | --- | --- | --- | --- |
| Access control and permissions | Authority | Critical | Identity, credentials, entitlements, delegated authority, least privilege | The agent can do more than the user or business process should allow | Security, IAM, IT, system owner |
| Tool misuse | Action | Critical | APIs, databases, browsers, email, code execution, plugins, MCP/A2A tools | The agent uses a valid tool for an invalid purpose | Engineering, platform, security, business owner |
| Governance and accountability | Ownership | High | Ownership, approval, risk acceptance, policy lifecycle, change control | No one can say who approved, owns, or must remediate agent behavior | Compliance, legal, risk, business owner |
| Privacy and data protection | Data boundary | Critical | Personal data, confidential data, retention, memory, exfiltration | Sensitive data is collected, stored, transformed, or disclosed unsafely | Privacy, legal, security, data owner |
| Output quality and safety | Trustworthiness | High | Accuracy, hallucination, bias, toxicity, harmful advice, overreliance | Users or workflows act on false, discriminatory, or unsafe output | Product, model owner, compliance, business owner |
| Agent behavior and autonomy | Goal control | Critical | Goal pursuit, planning, delegation, human manipulation, unsafe actuation | The agent pursues a goal in a way the organization did not intend | AI architecture, business owner, security, risk |
| Reliability and observability | Control evidence | High | Logging, monitoring, traceability, resilience, incident response | The organization cannot detect, explain, or recover from agent failure | Engineering, SRE, security operations, compliance |

## The 12 practitioner risks at a glance

| ID | Risk | Theme | Default importance | Primary MIT mapping | Typical trigger for escalation |
| --- | --- | --- | --- | --- | --- |
| `AAR-01` | Autonomy risk | Human control | Critical | `5.2`; `7.1` | Agent can act from triggers, complete multi-step tasks, or affect regulated/high-impact outcomes |
| `AAR-02` | Tool risk | Action boundary | Critical | `2.2`; `7.3` | Agent has write-capable tools, code execution, external communication, or production access |
| `AAR-03` | Permission risk | Authority boundary | Critical | `2.2`; `2.1` | Agent uses broad scopes, service accounts, inherited permissions, or cross-boundary access |
| `AAR-04` | Instruction and prompt injection risk | Instruction integrity | High | `2.2`; `4.2` | Agent reads untrusted content and can act on it |
| `AAR-05` | Memory risk | Persistent context | High | `2.1`; `2.2` | Agent has long-term memory or user-writable memory that can affect later actions |
| `AAR-06` | Data exposure risk | Data boundary | Critical | `2.1`; `2.2` | Agent touches personal, regulated, confidential, credential, source-code, HR, finance, or security data |
| `AAR-07` | Planning risk | Goal decomposition | High | `7.3`; `7.1` | Agent decomposes goals into plans or revises plans during execution |
| `AAR-08` | Delegation risk | Multi-agent control | High | `7.6`; `2.2` | Agent invokes sub-agents, creates tasks, or passes instructions across agents |
| `AAR-09` | Observability risk | Traceability | High | `7.4`; `6.5` | Logs cannot reconstruct trigger, instruction, retrieval, tool call, approval, and action sequence |
| `AAR-10` | Accountability risk | Ownership | High | `6.5`; `7.4` | No named owner, approver, risk owner, incident owner, or vendor responsibility model |
| `AAR-11` | Compliance risk | Legal and policy fit | Critical | `6.5`; `2.1`; `7.4` | System is high-risk, regulated, personal-data-processing, or externally facing |
| `AAR-12` | Business process risk | Operational impact | Critical | `7.3`; `5.1`; `5.2` | Agent can approve, reject, route, close, refund, notify, deploy, delete, or modify records |

## Practitioner sub-risk layer

The 12 top-level risks are the entry point. The sub-risks below are the practical
review layer. Use them when writing concrete risk register entries, test cases,
and control requirements.

Keep the list practical. Add a new sub-risk only when it helps a reviewer
recognize a real failure mode or assign a concrete control.

| Sub-risk ID | Sub-risk | Parent risk | Plain-English failure mode | Primary MIT mapping | Typical control |
| --- | --- | --- | --- | --- | --- |
| `AAR-01.01` | Unapproved autonomous action | Autonomy risk | The agent takes a material action without required human approval. | `5.2`; `7.1` | Human approval thresholds and action gating |
| `AAR-01.02` | Trigger misuse | Autonomy risk | A background trigger starts the agent in the wrong context or from untrusted input. | `7.3`; `2.2` | Trigger validation and trusted event sources |
| `AAR-01.03` | Action at unsafe scale | Autonomy risk | The agent repeats an action across many users, records, cases, or systems before review. | `7.3`; `6.5` | Rate limits, batch caps, staged rollout |
| `AAR-01.04` | Inadequate stop or rollback | Autonomy risk | Operators cannot pause, disable, or reverse the agent quickly enough. | `5.2`; `7.3` | Kill switch, revocation path, rollback procedure |
| `AAR-02.01` | Tool permission overreach | Tool risk | A tool exposes more read/write capability than the use case needs. | `2.2`; `6.5` | Tool permission matrix and least privilege |
| `AAR-02.02` | Unsafe tool parameters | Tool risk | The model supplies dangerous, malformed, or overbroad tool arguments. | `2.2`; `7.3` | Parameter validation and constrained schemas |
| `AAR-02.03` | Tool output injection | Tool risk | Tool output is treated as trusted instruction and changes agent behavior. | `2.2`; `4.2` | Untrusted-output labeling and instruction isolation |
| `AAR-02.04` | Code execution abuse | Tool risk | The agent generates or runs code that escapes intended boundaries. | `2.2`; `4.2` | Sandboxing, allowlists, manual review for privileged code |
| `AAR-02.05` | External communication misuse | Tool risk | The agent sends email, chat, calendar invites, web requests, or files to the wrong recipient or channel. | `2.1`; `4.3` | External-send approval and recipient validation |
| `AAR-03.01` | Privilege escalation | Permission risk | The agent obtains, inherits, or exercises elevated permissions without approval. | `2.2`; `6.5` | Access reviews and just-in-time privilege |
| `AAR-03.02` | Confused deputy | Permission risk | The agent performs an action for a user who lacks direct authority. | `2.2`; `2.1` | User-bound authorization checks |
| `AAR-03.03` | Credential exposure | Permission risk | Secrets, tokens, keys, or credentials appear in prompts, memory, logs, or tool output. | `2.1`; `2.2` | Secret scanning, vaulting, redaction |
| `AAR-03.04` | Cross-boundary access | Permission risk | The agent crosses tenant, user, department, geography, or environment boundaries. | `2.1`; `2.2` | Tenant/user scoping and boundary tests |
| `AAR-04.01` | Direct prompt injection | Instruction and prompt injection risk | A user instructs the agent to ignore policy or bypass controls. | `2.2`; `4.2` | Prompt-injection tests and policy enforcement outside the model |
| `AAR-04.02` | Indirect prompt injection | Instruction and prompt injection risk | A document, email, webpage, ticket, or tool output contains hidden instructions. | `2.2`; `4.2` | Untrusted-content isolation and retrieval filtering |
| `AAR-04.03` | Instruction conflict | Instruction and prompt injection risk | System, developer, user, retrieved, or tool instructions conflict and the unsafe one wins. | `7.3`; `2.2` | Instruction hierarchy and conflict handling |
| `AAR-04.04` | Policy bypass through tool use | Instruction and prompt injection risk | The agent follows an instruction by using a tool in a way policy would otherwise block. | `2.2`; `6.5` | Runtime policy checks on tool calls |
| `AAR-05.01` | Memory poisoning | Memory risk | Untrusted input is stored and later changes recommendations, retrieval, or actions. | `2.2`; `7.3` | Memory write controls and poisoning tests |
| `AAR-05.02` | Sensitive memory retention | Memory risk | Personal, confidential, secret, or regulated data is stored longer than needed. | `2.1`; `6.5` | Retention limits and sensitive-data filtering |
| `AAR-05.03` | Cross-user memory leakage | Memory risk | Context from one user, customer, tenant, or case appears in another context. | `2.1`; `2.2` | Memory isolation and access checks |
| `AAR-05.04` | Stale memory reliance | Memory risk | Old or superseded memory drives current decisions or actions. | `7.3`; `3.1` | Memory expiry, source freshness, review triggers |
| `AAR-06.01` | Unauthorized retrieval | Data exposure risk | The agent retrieves data the user, workflow, or business purpose should not access. | `2.1`; `2.2` | Retrieval authorization and data-source scoping |
| `AAR-06.02` | Sensitive summary leakage | Data exposure risk | The agent summarizes protected data into a less protected channel. | `2.1`; `4.3` | Output filtering and channel controls |
| `AAR-06.03` | Data exfiltration channel | Data exposure risk | The agent leaks data through email, calendar, URL, logs, files, or third-party tools. | `2.1`; `2.2` | DLP, egress controls, external-send review |
| `AAR-06.04` | Inference of sensitive data | Data exposure risk | The agent correctly infers private or confidential information not explicitly provided. | `2.1`; `7.3` | Privacy review and inference-risk testing |
| `AAR-07.01` | Flawed task decomposition | Planning risk | The agent breaks a goal into steps that miss constraints, dependencies, or approvals. | `7.3`; `7.1` | Plan validation and workflow constraints |
| `AAR-07.02` | Goal misalignment | Planning risk | The agent optimizes for completion, speed, cost, or persuasion over the intended policy goal. | `7.1`; `7.3` | Goal checks and policy constraints |
| `AAR-07.03` | Cascading false assumption | Planning risk | A false intermediate output becomes the basis for later actions. | `3.1`; `7.3` | Multi-source validation and checkpoints |
| `AAR-07.04` | Unsafe long-horizon planning | Planning risk | The agent plans across too many steps, systems, or time periods without review. | `7.2`; `7.3` | Step limits and human review for long plans |
| `AAR-08.01` | Agent communication poisoning | Delegation risk | One agent sends false, malicious, or malformed instructions to another. | `7.6`; `2.2` | Message validation and signed/scoped communication |
| `AAR-08.02` | Rogue or unregistered agent | Delegation risk | An unknown, compromised, or unapproved agent participates in a workflow. | `7.6`; `6.5` | Agent inventory and authenticated agent identity |
| `AAR-08.03` | Hidden delegation | Delegation risk | The agent hands off work without user, owner, or audit visibility. | `7.4`; `6.5` | Delegation logs and user-visible handoffs |
| `AAR-08.04` | Delegated authority leakage | Delegation risk | A sub-agent receives broader authority, tools, or data than needed. | `7.6`; `2.2` | Delegation allowlists and scoped permissions |
| `AAR-09.01` | Missing execution trace | Observability risk | Logs cannot reconstruct trigger, instructions, retrievals, tool calls, approvals, and actions. | `7.4`; `6.5` | Runtime audit logs and trace IDs |
| `AAR-09.02` | Missing policy decision log | Observability risk | Allow/deny decisions and approval checks are not recorded. | `7.4`; `6.5` | Policy decision logging |
| `AAR-09.03` | Weak anomaly detection | Observability risk | Abnormal tool use, retry storms, cost spikes, or data movement are not detected. | `7.3`; `2.2` | Monitoring rules and alerts |
| `AAR-09.04` | Unverifiable reasoning or source basis | Observability risk | Reviewers cannot determine why the agent produced an output or action. | `7.4`; `3.1` | Source citations, decision metadata, evaluation records |
| `AAR-10.01` | No named business owner | Accountability risk | No accountable owner exists for the agent's business outcome. | `6.5`; `7.4` | Owner registry and RACI |
| `AAR-10.02` | Unclear approval authority | Accountability risk | No one knows who can approve launch, high-impact action, or residual risk. | `6.5`; `5.2` | Approval workflow and risk acceptance record |
| `AAR-10.03` | Vendor/deployer responsibility gap | Accountability risk | Provider, vendor, deployer, and internal responsibilities are not separated. | `6.5`; `7.4` | Responsibility mapping and contract/control review |
| `AAR-10.04` | Orphaned agent lifecycle | Accountability risk | The agent continues operating after owner, policy, model, or workflow changes. | `6.5`; `7.3` | Lifecycle reviews and ownership recertification |
| `AAR-11.01` | Missing legal/use-case classification | Compliance risk | The agent is not assessed for high-risk, regulated, personal-data, or sectoral obligations. | `6.5`; `2.1` | Legal classification and compliance intake |
| `AAR-11.02` | Missing documentation evidence | Compliance risk | Required risk, testing, transparency, oversight, or monitoring evidence is missing. | `6.5`; `7.4` | Evidence pack and documentation checklist |
| `AAR-11.03` | Unlawful or excessive personal-data processing | Compliance risk | The agent processes personal data without clear purpose, basis, minimization, or protection. | `2.1`; `6.5` | DPIA/privacy review and data minimization |
| `AAR-11.04` | Bias or toxicity compliance exposure | Compliance risk | Agent output creates discriminatory, toxic, or unsafe treatment in regulated workflows. | `1.1`; `1.2` | Bias/toxicity testing and escalation rules |
| `AAR-12.01` | Unsafe business actuation | Business process risk | The agent triggers refunds, approvals, notices, records, deployments, or other material actions incorrectly. | `7.3`; `5.2` | Business action allowlists and approval thresholds |
| `AAR-12.02` | Irreversible or hard-to-reverse action | Business process risk | The action cannot be undone quickly or without harm. | `7.3`; `6.5` | Reversibility review and rollback plan |
| `AAR-12.03` | Segregation-of-duties bypass | Business process risk | The agent combines roles or steps that should be separated. | `6.5`; `2.2` | Segregation-of-duties checks |
| `AAR-12.04` | Human manipulation in workflow | Business process risk | The agent persuades a person to approve, click, pay, disclose, or decide in a harmful way. | `4.3`; `5.1` | Human-facing content review and high-risk confirmations |

## Detailed practitioner taxonomy

### AAR-01: Autonomy risk

The agent acts without sufficient human oversight for the impact level.

| Field | Details |
| --- | --- |
| Theme | Human control |
| Default importance | Critical |
| Why it matters | A chatbot can be wrong; an autonomous agent can be wrong and act on it. |
| Common indicators | Background triggers, multi-step execution, automatic decisioning, asynchronous workflows, action without step-by-step approval |
| Common failure modes | Unapproved action, silent goal pursuit, escalation failure, action at scale, inability to pause or reverse execution |
| Controls to consider | Human approval thresholds, autonomy tiering, action allowlists, trigger validation, pause/disable control, policy checks outside the model |
| Evidence to retain | Agent level assessment, approval policy, trigger list, action logs, human approval records, disable procedure |
| MIT parent mapping | Primary: `5.2 Loss of human agency and autonomy`; secondary: `7.1 AI pursuing its own goals in conflict with human goals or values`, `7.3 Lack of capability or robustness`, `6.5 Governance failure` |
| Reference basis | OWASP Agentic AI autonomy/planning/misalignment themes; EU AI Act Article 14; NIST AI RMF Govern/Map/Measure/Manage |

### AAR-02: Tool risk

The agent misuses internal or external tools, APIs, connectors, code execution,
browsers, email, databases, or workflows.

| Field | Details |
| --- | --- |
| Theme | Action boundary |
| Default importance | Critical |
| Why it matters | Tools turn model output into system impact. |
| Common indicators | Write-capable tools, model-selected tool parameters, tool chaining, code execution, browser automation, email sending, workflow triggers |
| Common failure modes | Unauthorized tool call, unsafe tool arguments, destructive write action, data exfiltration through tools, remote code execution, unsafe integration behavior |
| Controls to consider | Tool permission matrix, least privilege, parameter validation, deny-by-default tools, approval gates, sandboxing, rate limits, tool-call logging |
| Evidence to retain | Tool inventory, allowed action list, permission matrix, test cases, tool-call logs, approval records |
| MIT parent mapping | Primary: `2.2 AI system security vulnerabilities and attacks`; secondary: `4.2 Cyberattacks, weapon development or use, and mass harm`, `7.3 Lack of capability or robustness`, `6.5 Governance failure` |
| Reference basis | OWASP Agentic AI T2/T11/T16; OWASP LLM Top 10 Excessive Agency and Insecure Output Handling; NIST CSF 2.0 |

### AAR-03: Permission risk

The agent has broader access than required for its intended purpose.

| Field | Details |
| --- | --- |
| Theme | Authority boundary |
| Default importance | Critical |
| Why it matters | Agent permissions can become a hidden access-control layer. |
| Common indicators | Broad OAuth scopes, service accounts, shared credentials, inherited user permissions, cross-tenant access, cross-environment access |
| Common failure modes | Privilege escalation, confused deputy, credential theft, impersonation, unauthorized read/write access, excessive delegated authority |
| Controls to consider | Named agent identity, least privilege, just-in-time access, scope minimization, credential isolation, access reviews, no shared credentials |
| Evidence to retain | Identity record, access grants, OAuth scopes, service account owner, access review, privilege exception approvals |
| MIT parent mapping | Primary: `2.2 AI system security vulnerabilities and attacks`; secondary: `2.1 Compromise of privacy by obtaining, leaking or correctly inferring sensitive information`, `6.5 Governance failure` |
| Reference basis | OWASP Agentic AI T3/T9 and confused deputy discussion; NIST CSF PR.AA; GDPR Article 32 where personal data is involved |

### AAR-04: Instruction and prompt injection risk

The agent follows malicious, conflicting, or ambiguous instructions, including
instructions hidden in retrieved content, tool outputs, web pages, documents, or
inter-agent messages.

| Field | Details |
| --- | --- |
| Theme | Instruction integrity |
| Default importance | High |
| Why it matters | Malicious instructions become more dangerous when the agent can take action. |
| Common indicators | Untrusted retrieval, email ingestion, web browsing, document parsing, customer/supplier content, tool output reused as context |
| Common failure modes | System instruction override, tool misuse, data exfiltration, approval bypass, goal manipulation, malicious delegation |
| Controls to consider | Instruction hierarchy, untrusted-content labeling, retrieval filtering, tool policy outside the model, prompt-injection tests, output/action validation |
| Evidence to retain | Prompt-injection test suite, red-team results, retrieval policy, tool gating policy, blocked-action logs |
| MIT parent mapping | Primary: `2.2 AI system security vulnerabilities and attacks`; secondary: `4.2 Cyberattacks, weapon development or use, and mass harm`, `7.3 Lack of capability or robustness` |
| Reference basis | OWASP LLM Top 10 Prompt Injection; OWASP Agentic AI tool misuse, goal manipulation, agent communication poisoning |

Security articles and field studies are useful evidence for prompt injection
patterns, but they are risk evidence rather than legal requirements unless
linked to a specific law, regulation, or binding internal policy.

### AAR-05: Memory risk

The agent stores, leaks, poisons, or reuses sensitive context inappropriately.

| Field | Details |
| --- | --- |
| Theme | Persistent context |
| Default importance | High |
| Why it matters | Memory creates a persistence layer for both usefulness and compromise. |
| Common indicators | Long-term memory, vector stores, conversation state, personalization, cross-session context, user-writable memory |
| Common failure modes | Memory poisoning, sensitive data retention, cross-user leakage, stale context, poisoned retrieval, unauthorized reuse |
| Controls to consider | Memory inventory, write controls, read controls, retention limits, memory sanitization, sensitive-data filtering, user deletion workflow |
| Evidence to retain | Memory schema, retention policy, access rules, deletion logs, memory poisoning tests, sanitization records |
| MIT parent mapping | Primary: `2.1 Compromise of privacy by obtaining, leaking or correctly inferring sensitive information`; secondary: `2.2 AI system security vulnerabilities and attacks`, `7.3 Lack of capability or robustness` |
| Reference basis | OWASP Agentic AI T1; NIST AI 600-1 data privacy and information integrity; GDPR Articles 5 and 32 |

### AAR-06: Data exposure risk

The agent retrieves, exposes, transforms, summarizes, or transmits sensitive data
in unsafe ways.

| Field | Details |
| --- | --- |
| Theme | Data boundary |
| Default importance | Critical |
| Why it matters | Agents can combine and re-express protected data into lower-protection channels. |
| Common indicators | Personal data, confidential data, source code, contracts, financial records, HR records, customer data, secrets, security logs |
| Common failure modes | Sensitive information disclosure, data exfiltration, overbroad retrieval, insecure summarization, external disclosure, unauthorized aggregation |
| Controls to consider | Data classification, retrieval access checks, DLP, output filtering, external-send approval, tenant isolation, data minimization |
| Evidence to retain | Data source inventory, data classification, access policy, DLP logs, disclosure tests, DPIA where required |
| MIT parent mapping | Primary: `2.1 Compromise of privacy by obtaining, leaking or correctly inferring sensitive information`; secondary: `2.2 AI system security vulnerabilities and attacks`, `4.3 Fraud, scams, and targeted manipulation` |
| Reference basis | OWASP LLM Top 10 Sensitive Information Disclosure; OWASP Agentic AI exfiltration scenarios; GDPR Articles 5/32/33; EU AI Act Article 10 for high-risk systems |

### AAR-07: Planning risk

The agent makes flawed multi-step plans that look reasonable locally but fail
globally.

| Field | Details |
| --- | --- |
| Theme | Goal decomposition |
| Default importance | High |
| Why it matters | A plan can be made of plausible steps and still violate policy, budget, safety, or workflow constraints. |
| Common indicators | Goal decomposition, self-reflection, plan revision, task queues, workflow orchestration, optimization for completion |
| Common failure modes | Goal misalignment, policy bypass, flawed dependency ordering, unsafe optimization, cascading hallucination, wrong escalation |
| Controls to consider | Plan validation, policy constraints, human review for high-impact plans, deterministic workflow boundaries, secondary model review, simulation tests |
| Evidence to retain | Plan review policy, test scenarios, model evaluation results, approved workflow constraints, exception records |
| MIT parent mapping | Primary: `7.3 Lack of capability or robustness`; secondary: `7.1 AI pursuing its own goals in conflict with human goals or values`, `3.1 False or misleading information`, `7.2 AI possessing dangerous capabilities` |
| Reference basis | OWASP Agentic AI T5/T6/T7; NIST AI 600-1 confabulation and human-AI configuration; EU AI Act Articles 9/13/14 |

### AAR-08: Delegation risk

The agent creates tasks, invokes sub-agents, hands off work, or relies on other
agents without clear accountability and control.

| Field | Details |
| --- | --- |
| Theme | Multi-agent control |
| Default importance | High |
| Why it matters | Delegation multiplies trust boundaries and makes root cause harder. |
| Common indicators | Coordinator agents, specialist agents, agent-to-agent messages, task creation, shared memory, delegated tool access |
| Common failure modes | Rogue agents, agent communication poisoning, hidden delegation, authority transfer, multi-agent misinformation loops, unclear ownership |
| Controls to consider | Agent identity, signed/scoped messages, delegation allowlists, inter-agent authentication, message validation, end-to-end tracing |
| Evidence to retain | Agent graph, delegation policy, communication logs, agent identity records, task handoff traces, multi-agent test results |
| MIT parent mapping | Primary: `7.6 Multi-agent risks`; secondary: `2.2 AI system security vulnerabilities and attacks`, `6.5 Governance failure`, `7.4 Lack of transparency or interpretability` |
| Reference basis | OWASP Agentic AI T12/T13/T14/T16; EU AI Act Article 25; ISO/IEC 42001 responsibilities and lifecycle controls |

### AAR-09: Observability risk

The organization cannot reliably reconstruct what happened.

| Field | Details |
| --- | --- |
| Theme | Traceability |
| Default importance | High |
| Why it matters | Without traces, teams cannot investigate incidents, prove compliance, or improve controls. |
| Common indicators | Final-output-only logs, missing tool arguments, missing prompt versions, missing approval data, no anomaly monitoring |
| Common failure modes | Repudiation, untraceability, delayed detection, failed incident response, unverifiable approvals, no root-cause analysis |
| Controls to consider | Runtime audit logs, immutable logs, trace IDs, policy decision logs, monitoring rules, alerting, incident runbooks, kill switch |
| Evidence to retain | Execution traces, tool-call logs, prompt/instruction versions, approval records, alerts, incident tickets, retention policy |
| MIT parent mapping | Primary: `7.4 Lack of transparency or interpretability`; secondary: `6.5 Governance failure`, `7.3 Lack of capability or robustness` |
| Reference basis | OWASP Agentic AI T8; EU AI Act logging/monitoring obligations for high-risk contexts; NIST AI RMF and NIST CSF |

### AAR-10: Accountability risk

Ownership for agent decisions, approvals, incidents, and damages is unclear.

| Field | Details |
| --- | --- |
| Theme | Ownership |
| Default importance | High |
| Why it matters | Agents often sit between business, IT, security, legal, compliance, vendors, and platform teams. |
| Common indicators | No named business owner, no technical owner, unclear approval authority, unclear vendor/deployer responsibility, no residual risk owner |
| Common failure modes | Delayed remediation, unapproved risk acceptance, unclear liability, orphaned agents, weak lifecycle governance |
| Controls to consider | RACI, owner registry, approval workflow, risk acceptance process, vendor responsibility mapping, lifecycle reviews |
| Evidence to retain | Owner record, approval record, RACI, vendor contract/control mapping, residual risk acceptance, review history |
| MIT parent mapping | Primary: `6.5 Governance failure`; secondary: `7.4 Lack of transparency or interpretability`, `5.2 Loss of human agency and autonomy` |
| Reference basis | EU AI Act Articles 16-27; ISO/IEC 42001 accountability and continual improvement; NIST AI RMF Govern function |

### AAR-11: Compliance risk

The system violates legal, regulatory, contractual, sectoral, or internal policy
requirements.

| Field | Details |
| --- | --- |
| Theme | Legal and policy fit |
| Default importance | Critical |
| Why it matters | Agent behavior can create obligations across AI, privacy, cybersecurity, employment, finance, healthcare, consumer, and contract domains. |
| Common indicators | High-risk use case, personal data, employment/finance/education/healthcare/legal/safety/security workflow, external users, consequential decisions |
| Common failure modes | Missing risk management, missing documentation, weak human oversight, unlawful processing, no transparency, no incident process, no audit evidence |
| Controls to consider | Legal classification, DPIA where required, high-risk AI assessment, technical documentation, transparency notices, monitoring, incident process |
| Evidence to retain | Legal assessment, DPIA, risk assessment, conformity or governance evidence, transparency notice, testing records, incident records |
| MIT parent mapping | Primary: `6.5 Governance failure`; secondary: `2.1 Compromise of privacy by obtaining, leaking or correctly inferring sensitive information`, `7.4 Lack of transparency or interpretability`, `1.1 Unfair discrimination and misrepresentation` |
| Reference basis | EU AI Act Articles 9-15, 17-20, 26-27, 50; GDPR Articles 5/32/33/35; ISO/IEC 42001; NIST AI RMF |

### AAR-12: Business process risk

The agent causes direct operational harm in finance, HR, legal, customer support,
sales, procurement, infrastructure, security, or other business processes.

| Field | Details |
| --- | --- |
| Theme | Operational impact |
| Default importance | Critical |
| Why it matters | Agent governance becomes urgent when outputs trigger real-world business action. |
| Common indicators | Approve, reject, route, close, refund, notify, escalate, deploy, delete, modify records, update cases, send external messages |
| Common failure modes | Wrong action at scale, customer harm, financial loss, legal exposure, HR harm, service disruption, security incident, process bypass |
| Controls to consider | Business process mapping, approval thresholds, reversible-action design, exception handling, segregation of duties, monitoring, rollback |
| Evidence to retain | Process map, action list, approval thresholds, rollback procedure, exception logs, incident records, business owner approval |
| MIT parent mapping | Primary: `7.3 Lack of capability or robustness`; secondary: `5.1 Overreliance and unsafe use`, `5.2 Loss of human agency and autonomy`, `6.5 Governance failure` |
| Reference basis | OWASP Agentic AI T7/T10/T15; NIST AI 600-1 human-AI configuration, confabulation, harmful bias, information integrity; EU AI Act Articles 14/26 where applicable |

## Risk-to-domain matrix

| Practitioner risk | Access control | Tool misuse | Governance | Privacy | Output quality | Agent behavior | Reliability/observability | Business process |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Autonomy risk | Secondary | Secondary | Primary | Secondary | Secondary | Primary | Primary | Primary |
| Tool risk | Secondary | Primary | Secondary | Secondary | Secondary | Primary | Primary | Primary |
| Permission risk | Primary | Secondary | Secondary | Primary |  | Secondary | Secondary | Secondary |
| Instruction and prompt injection risk | Secondary | Primary | Secondary | Primary | Primary | Primary | Secondary | Secondary |
| Memory risk | Secondary | Secondary | Secondary | Primary | Primary | Primary | Primary |  |
| Data exposure risk | Primary | Secondary | Secondary | Primary |  | Secondary | Secondary | Secondary |
| Planning risk |  | Secondary | Secondary |  | Primary | Primary | Secondary | Primary |
| Delegation risk | Secondary | Secondary | Primary | Secondary | Secondary | Primary | Primary | Primary |
| Observability risk |  | Secondary | Primary | Secondary |  | Secondary | Primary | Secondary |
| Accountability risk | Secondary |  | Primary | Secondary | Secondary | Secondary | Secondary | Primary |
| Compliance risk | Secondary | Secondary | Primary | Primary | Primary | Secondary | Primary | Primary |
| Business process risk | Secondary | Primary | Primary | Secondary | Secondary | Primary | Primary | Primary |

## OWASP Agentic AI threat mapping

| OWASP Agentic AI threat | Closest practitioner risks | Notes for enterprise use |
| --- | --- | --- |
| T1 Memory Poisoning | Memory risk, data exposure risk, planning risk | Track who can write memory and how poisoned memory affects future retrieval, recommendations, and tool calls. |
| T2 Tool Misuse | Tool risk, prompt injection risk, business process risk | Treat every write-capable tool as a controlled action surface. |
| T3 Privilege Compromise | Permission risk, data exposure risk, business process risk | Map agent identity, inherited permissions, service accounts, and privilege changes. |
| T4 Resource Overload | Observability risk, tool risk, business process risk | Track rate limits, quotas, retry storms, cost spikes, and service degradation. |
| T5 Cascading Hallucination Attacks | Planning risk, output quality risk, delegation risk | Watch for false outputs propagating into tools, workflows, memory, or other agents. |
| T6 Intent Breaking and Goal Manipulation | Planning risk, autonomy risk, prompt injection risk | Validate plans and goals against policy outside the model. |
| T7 Misaligned and Deceptive Behaviors | Autonomy risk, planning risk, business process risk | Escalate when the agent can hide harmful action behind plausible output. |
| T8 Repudiation and Untraceability | Observability risk, accountability risk, compliance risk | Require execution traces, tool-call logs, and approval records. |
| T9 Identity Spoofing and Impersonation / Agent Identity Compromise | Permission risk, accountability risk, delegation risk | Authenticate agents, users, and inter-agent messages. |
| T10 Overwhelming Human in the Loop | Autonomy risk, business process risk, observability risk | Monitor alert fatigue, approval flooding, and rubber-stamping incentives. |
| T11 Unexpected RCE and Code Attacks | Tool risk, permission risk, business process risk | Sandbox code execution and require manual review for privileged generated code. |
| T12 Agent Communication Poisoning | Delegation risk, prompt injection risk, memory risk | Validate and log inter-agent messages and shared context. |
| T13 Rogue Agents in Multi-Agent Systems | Delegation risk, accountability risk, data exposure risk | Maintain agent inventory, agent identity, and communication allowlists. |
| T14 Human Attacks on Multi-Agent Systems | Delegation risk, permission risk, business process risk | Limit privilege transfer across delegated workflows. |
| T15 Human Manipulation | Business process risk, output quality risk, autonomy risk | Treat agent-to-human persuasion as a consequential action in sensitive workflows. |
| T16 Insecure Inter-Agent Protocol Abuse | Delegation risk, tool risk, observability risk | Secure MCP/A2A-style protocols with authentication, consent checks, scoping, validation, and logs. |
| T17 Supply Chain Compromise | Tool risk, governance risk, compliance risk | Track model, prompt, tool, package, plugin, connector, and deployment pipeline provenance. |

## Specific threat classes to track

| Threat class | Default importance | Primary domain | Related practitioner risks | Typical source mapping | Example failed control |
| --- | --- | --- | --- | --- | --- |
| Privilege escalation | Critical | Access control and permissions | Permission, tool, business process | OWASP Agentic AI T3; NIST CSF PR.AA | Agent can elevate or inherit permissions without approval |
| Credential theft | Critical | Access control and permissions | Permission, data exposure | OWASP Agentic AI T9; NIST CSF PR.AA; GDPR Article 32 if personal data is affected | Secrets are exposed in prompt, memory, logs, or tool output |
| Confused deputy | Critical | Access control and permissions | Permission, tool | OWASP Agentic AI identity and authorization discussion | Agent performs an action for a user who lacks direct authority |
| Goal misalignment | High | Agent behavior and autonomy | Autonomy, planning, business process | OWASP Agentic AI T6/T7; NIST AI RMF | Agent optimizes for task completion while bypassing safety or policy |
| Policy drift | High | Governance and accountability | Compliance, accountability, planning | ISO/IEC 42001 continual improvement; EU AI Act quality management/change management concepts | Agent instructions, tools, or workflows change without review |
| Hallucination / confabulation | High | Output quality and safety | Output quality, planning, business process | NIST AI 600-1 Confabulation; OWASP Agentic AI T5; OWASP LLM Top 10 Overreliance | Unsupported output is used for a decision or action |
| Bias and toxicity | High | Output quality and safety | Output quality, compliance, business process | NIST AI 600-1 Harmful Bias; EU AI Act Article 10 for high-risk data governance | Agent output disadvantages protected groups or produces harmful content |
| API integration failure | High | Tool misuse and reliability | Tool, observability, business process | OWASP Agentic AI T2; NIST CSF Protect/Detect/Respond | Tool errors, retries, or schema mismatches produce unsafe actions |
| Supply-chain vulnerabilities | High | Governance and tool misuse | Tool, compliance, accountability | OWASP Agentic AI T17; OWASP LLM Top 10 Supply Chain Vulnerabilities | Untrusted model, prompt, package, connector, or plugin enters production |
| Uncontrolled resource consumption | Medium to High | Reliability and observability | Observability, tool, business process | OWASP Agentic AI T4; OWASP LLM Top 10 Unbounded Consumption; NIST AI 600-1 environmental impacts | Agent loops, retries, or task spawning exhaust budget, quota, or services |
| Sensitive data exposure | Critical | Privacy and data protection | Data exposure, memory, tool | OWASP LLM Top 10 Sensitive Information Disclosure; GDPR Articles 5/32/33 | Agent returns restricted data to unauthorized user or channel |
| Data exfiltration channel | Critical | Privacy and data protection | Data exposure, tool, prompt injection | OWASP Agentic AI T2/T13; MITRE ATLAS exfiltration patterns | Agent sends data through calendar, email, URL, logs, or external tool |
| Unsafe actuation | Critical | Agent behavior and business process | Tool, autonomy, business process | EU AI Act human oversight; OWASP Agentic AI T2/T7 | Agent performs irreversible or high-impact action without approval |
| Human manipulation | High | Agent behavior and output safety | Business process, output quality, autonomy | OWASP Agentic AI T15; NIST AI 600-1 Human-AI Configuration | Compromised agent persuades user to approve harmful action |
| Opaque reasoning | High | Observability and accountability | Observability, accountability, compliance | OWASP Agentic AI T8; EU AI Act logging/transparency requirements; NIST AI RMF explainability | Team cannot explain why an action was taken or who approved it |
| Data and memory poisoning | High | Privacy, quality, and reliability | Memory, prompt injection, planning | OWASP Agentic AI T1/T12; MITRE ATLAS poisoning techniques; NIST AI 600-1 information integrity | Untrusted input changes future retrieval, recommendations, or actions |

## Minimum control mapping

| Control area | Applies most strongly to | Minimum expectation |
| --- | --- | --- |
| Agent inventory | All risks | Every production and pilot agent has owner, purpose, data sources, tools, autonomy level, and approval status. |
| Agent level and autonomy assessment | Autonomy, tool, business process, compliance | Each agent is classified by behavior and impact, not by vendor label. |
| Tool permission matrix | Tool, permission, data exposure, business process | Every tool has read/write scope, allowed actions, blocked actions, approval requirements, and logs. |
| Data and memory inventory | Data exposure, memory, compliance | Data sources, memory stores, retention, access rules, and deletion paths are documented. |
| Human approval points | Autonomy, business process, compliance | High-impact or irreversible actions require defined human approval. |
| Adversarial testing | Prompt injection, tool, memory, data exposure, delegation | Test prompt injection, data exfiltration, unauthorized tool calls, memory poisoning, and approval bypass. |
| Runtime audit logging | Observability, accountability, compliance | Logs capture trigger, agent ID, instruction version, retrievals, tool calls, arguments, policy checks, approvals, and final actions. |
| Monitoring and kill switch | Autonomy, tool, observability, business process | Teams can detect abnormal behavior, pause the agent, revoke access, and investigate incidents. |
| Lifecycle review | Compliance, governance, policy drift | Re-review after new tools, data sources, autonomy changes, model/provider changes, incidents, or policy changes. |

## Risk register fields

For each agent, track both the threat class and the failed business control.
That is what turns this taxonomy into an operational risk register.

| Field | Purpose |
| --- | --- |
| Register risk ID | Stable identifier for the concrete risk instance, such as `R-001` |
| Agent taxonomy ID | Stable AI Crafters taxonomy identifier, such as `AAR-02` |
| Agent sub-risk ID | Practical child-risk identifier, such as `AAR-02.03` |
| Agent sub-risk | Plain-language child risk, such as `Tool output injection` |
| MIT domain ID | Broad MIT parent domain, such as `2` |
| MIT subdomain ID | Broad MIT parent subdomain, such as `2.2` |
| MIT subdomain name | MIT subdomain label, such as `AI system security vulnerabilities and attacks` |
| MIT mapping confidence | High, Medium, or Low confidence in the mapping |
| MIT mapping note | Why the MIT mapping fits, and what agent-specific detail it does not capture |
| Agent name | System or workflow under review |
| Business owner | Person accountable for business outcome |
| Technical owner | Person accountable for implementation and operation |
| Use case | What the agent is intended to do |
| Business process | Where harm would occur |
| Agent level | Behavior-based agent classification |
| Autonomy level | Degree of independent action |
| Tools/connectors | Action surfaces |
| Data sources | Retrieval and data exposure surfaces |
| Memory store | Persistent context surface |
| Delegated agents | Multi-agent dependency surface |
| Risk domain | One of the core enterprise domains |
| Practitioner risk | One of the 12 taxonomy risks |
| Specific threat class | More precise threat class, such as privilege escalation or memory poisoning |
| Reference source | Framework, law, standard, article, study, or internal incident evidence |
| Threat scenario | Concrete way the risk can materialize |
| Failed or missing control | Business/security/privacy/control gap |
| Likelihood, impact, autonomy, data sensitivity, tool criticality, observability gap | Inputs to scoring |
| Composite score and risk tier | Prioritization |
| Required control | Mitigation required before production or continued operation |
| Human approval point | Where human review is required |
| Evidence location | Link to logs, tests, approvals, policy, or documentation |
| Residual risk owner | Person accepting remaining risk |
| Status | Open, mitigating, accepted, closed |
| Next review date and trigger | Lifecycle governance |

## System-level indicators to watch

Track these as escalation signals. Some are direct enterprise agent concerns;
others are frontier or advanced-system indicators that should trigger immediate
review if they appear in a real system.

| Indicator | Why it matters | Escalation action |
| --- | --- | --- |
| Unintended goal pursuit | Agent appears to optimize for a goal outside intended workflow | Pause or constrain autonomy; review goals, prompts, tools, and logs |
| Unauthorized privilege escalation | Agent obtains or uses authority beyond its approved role | Revoke access; investigate identity, scopes, and tool paths |
| Autonomous resource acquisition | Agent provisions compute, tools, accounts, budget, or services unexpectedly | Freeze resource creation; review tool permissions and spend controls |
| Attempts to preserve access or resist shutdown | Agent behavior conflicts with human control | Disable immediately; perform incident review |
| Self-replication or unauthorized agent creation | Agent creates copies, tasks, or agents outside approved process | Disable creation path; audit orchestration and platform permissions |
| Multi-agent misinformation loops | False information propagates through agents or workflows | Stop propagation; inspect agent communication and validation controls |
| Repeated tool calls, retry storms, cost spikes, or quota exhaustion | Reliability failure can become business or security failure | Enforce rate limits; investigate loops and error handling |
| New or unexpected data exfiltration paths | Agent discovers or creates channels to move data | Block channel; review DLP, tool policy, and logs |

## Practical usage pattern

For each agent review:

1. Classify the agent level and autonomy level.
2. List tools, data sources, memory stores, and delegated agents.
3. Select the `AAR-*` practitioner risks that apply.
4. Select the most concrete `AAR-xx.yy` sub-risk that fits.
5. Add the MIT parent domain and subdomain mapping.
6. Add specific threat classes where useful.
7. Write the concrete threat scenario in business terms.
8. Identify the failed or missing control.
9. Score the risk.
10. Assign owner, required control, evidence, and review trigger.

The goal is not to label an agent as risky. The goal is to make the risk specific
enough that someone can own it, test it, control it, monitor it, and accept or
reject the residual risk.
