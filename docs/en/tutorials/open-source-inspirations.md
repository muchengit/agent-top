---
i18n-key: tutorials-open-source-inspirations
last-synced: 2026-09-17
validated_date: 2026-09-17
---

# Open-Source Inspirations Directory

This page turns verified GitHub Agent projects into learning themes. Agent-Top does not copy external code or prose. It absorbs stable patterns and maps them to local concepts, Labs, cases, and maintenance workflow. For a distilled decision matrix, use [`open-source-pattern-matrix.md`](open-source-pattern-matrix.md).

This page uses GitHub project discoveries verified on 2026-09-16. External links are maintainer-verified learning signals, not authoritative framework documentation.
A 2026-09-17 coding-agent pass added research watch entries. They are treated as discovery signals, not authoritative documentation, until maintainers verify repository URLs and licenses.
A 2026-09-17 data-ingestion pass added web scraping, browser-use, vector ingestion, and evaluation platform research watch entries. They are also discovery signals until maintainers verify repository URLs and licenses.
A second 2026-09-17 open-source scan verified SSH reachability for promptfoo, Google ADK, Instructor, DSPy, Open Interpreter, OpenHands, and E2B, while HTTPS cloning timed out for some of those repositories. Agent-Top treats SSH reachability as discovery evidence only, not maintainer verification of licenses or API stability.
A 2026-09-17 GitHub-native pass re-verified several GitHub CLI, GitHub REST API, GitHub MCP Server, and Copilot coding-agent style projects with `git ls-remote`. These entries absorb repository review workflows, PR review patterns, CI-first validation, and platform-native tool boundaries.
A 2026-09-17 runtime-evidence pass checked reachable public repositories with `git ls-remote`: Sentry, Grafana Pyroscope, Ruff, uv, and Dapr. These entries are learning signals for incident grouping, profiling, deterministic lint gates, lockfile evidence, and workflow provenance; they are not authoritative setup guides.
A 2026-09-17 platform-evidence pass checked reachable public repositories with `git ls-remote`: OpenTelemetry semantic conventions, OpenTelemetry Python, OpenTelemetry Python contrib, Arize Phoenix, promptfoo, LiteLLM, Dify, Agno, Traceloop OpenLLMetry, vLLM, and open-webui. These entries are learning signals for GenAI telemetry, eval-as-CI, model gateway boundaries, platform portals, and inference runtime metrics; they are not authoritative setup guides.
A 2026-09-17 safety-evidence pass checked reachable public repositories with `git ls-remote`: Guardrails AI, OpenAI Evals, Langfuse, Mem0, Letta, Chroma, Ollama, Microsoft RAI Toolbox, Hugging Face Alignment Handbook, and MLflow. These entries are learning signals for output validation, safety eval batteries, trace datasets, memory governance, vector provenance, local model boundaries, responsible AI review, and experiment evidence; they are not authoritative setup guides.
A 2026-09-17 tool-boundary pass checked reachable public repositories with `git ls-remote`: LangChain, LangGraph, LangSmith CLI, OpenAI Agents Python, ModelContextProtocol servers, Google ADK Python, LlamaIndex, Haystack, browser-use, and Pydantic AI. These entries are learning signals for MCP server boundaries, graph state checkpoints, typed tool output, RAG pipeline evidence, browser action traces, and SDK handoff boundaries; they are not authoritative setup guides.

## Project-to-Topic Map

| Project or ecosystem | Topic | What Agent-Top absorbs |
| --- | --- | --- |
| langchain | LLM application framework | tool calling, chains, memory, structured outputs |
| LangGraph | stateful graph workflows | explicit state, cycles, checkpointing, human-in-the-loop |
| MetaGPT | software-company multi-agent pattern | role specialization, shared artifacts, software development workflows |
| LlamaIndex | RAG and data framework | retrieval, chunking, indexing, evaluation |
| Haystack | search and RAG pipeline | document pipelines, rankers, retriever boundaries |
| AutoGen | conversational multi-agent systems | message passing, role boundaries, group chat |
| CrewAI | role-based agent teams | task delegation, role prompts, workflows |
| smolagents | minimal agent examples | code-first actions, readability, small tool surfaces |
| Agno | lightweight agent runtime | fast iteration, agent state, tool integration |
| Mastra | TypeScript Agent platform | workflows, evals, MCP, web-first Agent app structure |
| Pydantic AI | typed agents | schema-first validation, structured outputs, typed tools |
| Instructor | structured output extraction | JSON schema, validation, retry on extraction failures |
| DSPy | programmatic prompt optimization | signatures, metrics, optimizers, eval-driven tuning |
| OpenAI Agents SDK | model and agent tools | tool definitions, handoffs, guardrails, tracing |
| Claude Agent SDK / tool use patterns | tool-using assistant | tool execution loops, structured tool results, safety boundaries |
| Semantic Kernel | enterprise plugins and orchestration | plugin governance, enterprise plugins, process integration |
| MCP ecosystem / modelcontextprotocol | tool and context protocol | tool discovery, resource exposure, protocol boundaries |
| FastMCP | fast MCP server/client SDK | lightweight tool servers, client-server boundaries, developer ergonomics |
| GitHub MCP Server | official platform tool boundary | code and issue tools, repository workflow integration, permissions model |
| Playwright MCP | browser automation MCP | browser action traces, visual workflows, safe web interaction boundaries |
| Letta / MemGPT | agent memory | memory layers, summarization, long-term context |
| Mem0 | memory platform | memory extraction, deduplication, privacy considerations |
| TencentDB Agent Memory | team-level Agent memory hub | shared memory governance, code graph memory, reuse and access control |
| nanobot | lightweight personal Agent framework | local-first Agent experience, tools, memory, chat apps |
| 12-factor-agents | production Agent operating principles | deployment discipline, environment configuration, operational boundaries |
| Agent-S | computer-use Agent framework | desktop/browser action traces, visual grounding, recovery under noisy UI |
| Prompt optimization examples | prompt catalog and generate-evaluate-critique loops | prompt versioning, automated critique, eval-driven iteration |
| Langfuse / OpenTelemetry GenAI patterns | tracing and observability | span naming, prompt/model/tool traces, cost and latency |
| MLflow | AI engineering platform | experiment tracking, evaluation, monitoring, model serving boundaries |
| LangWatch | LLM evaluation and Agent testing | prompt comparisons, regression suites, Agent testing workflows |
| OpenLit | OpenTelemetry Agent observability | traces, prompt/tool spans, cost telemetry, runtime visibility |
| KimYx0207/AI-Coding-Guide-Zh | task-first tutorial structure | task-to-output navigation cards, local exercise materials, staged learning paths, and explicit environment/version guidance |
| Future-AGI | Agent evaluation and simulation platform | simulations, datasets, gateway guardrails, improvement loops |
| Opik | LLM observability and evaluation | traces, automated evaluation, dashboards, agentic workflow monitoring |
| AI-Infra-Guard | AI red teaming and security scanning | MCP/tool safety scans, jailbreak evals, agent security risk taxonomy |
| Januscope | local-first MCP policy proxy | tool blocking, mutation gates, PII redaction, rate limits, audit logs |
| AgentTrust / AgentLock patterns | pre-action Agent authorization | deny-by-default permissions, provenance checks, parameter gating |
| Doberman-style runtime guards | input/output/tool-call runtime guardrails | unsafe action interception before execution |
| Ragas / DeepEval / Arize Phoenix | RAG and LLM eval | faithfulness, answer relevance, hallucination checks, guardrail evals |
| DSPy / promptfoo / eval-driven examples | evaluation and regression | eval datasets, prompt regression, safety checks |
| SuperAGI / AgentOps-like projects | agent platforms | mission/task modeling, dashboarding, lifecycle observability |
| ELK / Elasticsearch / Kibana-like tooling | production observability | structured logs, trace visualization, alerting |
| Postmortem templates and incident-response repos | incident learning | blameless review, action ownership, recurrence prevention |
| Awesome LLM / Agent lists | community discovery | topic discovery, taxonomy, contribution routing |
| Aider / Continue.dev / Cline | coding Agent assistants | repository-aware edits, command boundaries, editable diffs, permissioned file writes |
| AIDABench / CodeBench-style benchmarks | coding Agent evaluation | benchmark task taxonomy, deterministic failure cases, code diff correctness checks |
| Copilot / Cursor / Trae / Bolt-style ecosystems | editor and app-generation Agents | editor context boundaries, suggestion acceptance rates, workspace safety, user confirmation for side effects |
| Unstructured / Firecrawl / Scrapling-style projects | data ingestion and web extraction | source allowlists, crawler permissions, parser boundaries, chunking rules, freshness metadata, and ingestion failure handling |
| browser-use / Playwright / desktop-Agent projects | browser and computer-use Agents | visual grounding, action traces, sandboxing, retry budgets, and rollback for noisy UI states |
| Vector / embedding / local-store projects | local retrieval and ingestion | namespace isolation, deletion propagation, embedding refresh, source provenance, and index drift detection |
| Phoenix / DeepEval / promptfoo-style projects | evaluation and regression tooling | dataset design, metric definitions, prompt regression, guardrail checks, and eval-report evidence |
| Promptfoo / prompt evaluation style projects | AI evaluation and regression | YAML-like test cases, prompt comparisons, guardrail assertions, CI-style pass/fail evidence |
| Open Interpreter / terminal coding agents | code execution agents | local execution boundaries, command confirmation, shell safety, and test evidence |
| OpenHands / task execution agents | task-oriented Agent runtime | event-driven Agent history, file/terminal tools, rollbackable plans, execution environment isolation |
| E2B / AI sandbox projects | code execution sandboxing | isolated execution environments, filesystem boundaries, resource limits, and command approval patterns |
| GitHub CLI (`gh`) | repository-native Agent commands | issue, PR, Actions, code search, and review flows directly from the repository platform |
| GitHub REST API | platform automation contract | issues, pull requests, checks, code search, status checks, and rate-limited workflow automation |
| GitHub MCP Server | MCP platform tools | repository tools, issue tools, PR tools, search tools, and permission-bound GitHub workflows |
| GitHub Copilot coding-agent style projects | code execution and review agents | PR-oriented work items, review loops, command boundaries, and CI-gated code changes |
| OpenTelemetry semantic conventions / GenAI attributes | portable trace vocabulary | stable span/event naming, provider-neutral attributes, vendor-agnostic cost and token fields |
| OpenTelemetry Python SDK / contrib | instrumentation discipline | deterministic instrumentation, resource labels, exporters, and trace-context propagation boundaries |
| Arize Phoenix-style LLM observability | eval and trace analysis | trace-to-eval linking, dataset curation from production traces, reviewer workflow evidence |
| promptfoo-style prompt evaluation | eval-as-CI | declarative test matrices, pass/fail assertions, prompt comparisons, and regression gates |
| LiteLLM-style model gateways | provider-neutral model routing | fallback, retry, budget, rate limit, spend tracking, and model routing decision evidence |
| Dify-style LLM application platforms | app and workflow boundaries | workflow nodes, knowledge sources, app config, environment variables, and permissioned human review |
| Agno-style Agent runtimes | agent runtime state and toolkits | lightweight toolkits, run/session state, memory, and production-ready Agent composition |
| Traceloop OpenLLMetry-style integrations | LLM framework instrumentation | library-specific traces, model-call spans, retrieval spans, and prompt/tool telemetry |
| vLLM-style inference runtimes | serving runtime metrics | throughput, batching, KV cache pressure, timeout behavior, and local/self-hosted deployment boundaries |
| open-webui-style Agent portals | user-facing Agent application layer | chat UI boundaries, document tools, web tools, permissioned sharing, and user-facing action evidence |
| Guardrails AI-style validation layers | output and tool validation | validator chains, retry/repair policy, fail-closed decisions, and validation evidence |
| OpenAI Evals-style suites | eval suite structure | versioned tasks, graders, data assets, and comparison reports |
| Langfuse-style LLM engineering observability | trace dataset and feedback loop | traces, datasets, annotation, prompt comparisons, and review workflow evidence |
| Mem0-style memory layers | extracted memory lifecycle | memory extraction, deduplication, update/delete behavior, privacy scoping, and conflict visibility |
| Letta-style stateful agent memory | agent state and memory tools | memory blocks, recall steps, archival memory, and stateful Agent boundaries |
| Chroma-style local vector stores | vector evidence and namespaces | collection/namespace boundaries, deletion propagation, source ids, and local indexing evidence |
| Ollama-style local model runtimes | local inference boundaries | model registry, local pull/run evidence, resource use, and offline/private runtime boundaries |
| Microsoft RAI Toolbox-style review workflows | responsible AI review | fairness, toxicity, representativeness, bias, transparency, and mitigation review evidence |
| Hugging Face Alignment Handbook-style guidance | alignment evaluation concepts | helpfulness, honesty, harmlessness, safety metrics, and evaluation methodology boundaries |
| MLflow-style experiment tracking | experiment evidence | run id, parameters, metrics, artifacts, and comparison evidence |
| LangChain-style agent frameworks | composable Agent building blocks | chains, tools, memory, output parsers, and framework-specific boundaries kept out of stable docs |
| LangGraph-style state graphs | graph state and checkpointing | explicit state schema, transitions, checkpoints, retries, interrupts, and stop conditions |
| LangSmith-style developer CLI | developer workflow evidence | trace inspection, deployment metadata, app/thread context, and eval/report linkage |
| OpenAI Agents Python-style SDK | SDK agent boundaries | agents, tools, handoffs, guardrails, sessions, and trace-friendly orchestration boundaries |
| ModelContextProtocol servers ecosystem | official MCP server catalog boundary | local filesystem/server examples, tool discovery, resource exposure, and server lifecycle evidence |
| Google ADK Python-style Agent SDK | production Agent composition | deterministic agents, tool use, sessions, memory, and deployment boundary |
| LlamaIndex-style data frameworks | RAG pipeline evidence | indexing, retrieval, node metadata, query engine boundaries, and evaluation hooks |
| Haystack-style pipelines | composable pipeline components | retriever, ranker, reader, writer, and component boundary evidence |
| browser-use-style browser Agents | browser action traces | visible page context, action intent, DOM/screenshot evidence, retry budgets, and rollback notes |
| Pydantic AI-style typed Agents | typed tool outputs | typed dependencies, tool definitions, structured output, validation, and model-call boundaries |
| Sentry-style error monitoring | incident grouping and release-aware errors | issue fingerprinting, release association, error grouping, alert routing, and blameless root-cause evidence |
| Grafana Pyroscope-style continuous profiling | runtime hotspots and resource evidence | sampling or continuous profiling, service/resource labels, hotspot routes, and cost diagnosis without full traces |
| Ruff-style deterministic linters | local quality gates | fast deterministic checks, explicit rule output, CI pass/fail evidence, and small reviewable diffs |
| uv-style Python package manager | dependency and tool lock evidence | lockfile reproducibility, pinned tool versions, isolated environments, and release evidence for package resolution |
| Dapr-style distributed application runtime | workflow provenance and operation boundaries | activity/workflow boundaries, component boundaries, retry/dead-letter patterns, and distributed operation provenance |

## Absorbable Patterns

- **Tool schema-first**: define inputs, outputs, and risk before writing prompts.
- **Graph and stateful workflows**: model state and transitions explicitly for complex flows.
- **Role-based teams**: give each role boundaries, stop conditions, and escalation rules.
- **Structured output**: validate model output before business logic consumes it.
- **RAG evaluation**: evaluate retrieval quality, answer relevance, and evidence faithfulness separately.
- **Memory lifecycle**: define extraction, deduplication, expiry, and deletion policies.
- **Observability contract**: record prompts, tools, retrieval, guardrails, cost, and latency for every turn.
- **Security red-team**: adversarially test prompts, tools, MCP boundaries, and agent workflows.
- **Incident learning**: convert incidents into evals, guardrails, traces, or rollback actions.
- **Prompt optimization loop**: version prompts, generate candidates, evaluate on datasets, and promote only measurable wins.
- **MCP policy proxy**: keep permissions, audit, mutation gates, PII redaction, and rate limits close to tool execution.
- **12-factor operating discipline**: treat environment, scaling, state, logs, and release strategy as Agent architecture concerns.
- **Coding Agent workspace boundary**: separate repository context, command execution, file writes, tests, and rollback state.
- **Patch-first editing**: prefer reviewable diffs over direct mutation when the Agent changes code.
- **Test-driven Agent validation**: every code-changing Agent step should identify the smallest command that proves the change.
- **Suggestion acceptance workflow**: distinguish recommendation, approval, execution, and post-check for user-facing coding tools.
- **Source policy boundary**: treat crawling, parsing, storage, retrieval, and citation as separate authorization decisions.
- **Ingestion metadata contract**: preserve source URL, crawl time, freshness, permission state, parser version, and deletion state.
- **Browser action trace**: record visible context, action intent, screenshot or DOM summary, and rollback state for UI-changing actions.
- **Eval dataset discipline**: keep datasets versioned and tie every metric to a clear pass/fail rule.
- **Structured output validation**: define JSON schema, retry policy, invalid-output escalation, and validation failures before business logic.
- **Sandboxed execution boundary**: treat shell, filesystem, network, and credentials as separate execution permissions.
- **Eval gate discipline**: a prompt, tool, or model change ships only when dataset version, pass rate, regression diff, and owner approval are recorded.
- **Error grouping evidence**: classify runtime failures by fingerprint, release SHA, route, owner, recurrence, and severity so postmortems can aggregate repeats instead of debating single traces.
- **Runtime hotspot evidence**: bind latency, CPU/memory, token cost, and tool hotspots to commit, release, model, prompt, tool, and dataset versions.
- **Deterministic lint gate**: require a fast deterministic formatter/linter result with tool version and exact findings before treating style or safety issues as resolved.
- **Tool and dependency lock evidence**: preserve lockfile/tool versions for Python, CLI, Agent, and MCP dependencies so a release can be replayed with the same toolchain.
- **Workflow provenance**: record workflow/activity id, input event id, retry attempt, dead-letter state, and owner so distributed Agent workflows can be traced across services.
- **GenAI telemetry vocabulary**: standardize span names, event names, model/provider attributes, token counts, cost units, and tenant/workflow labels so traces stay comparable across vendors.
- **Eval-as-CI**: represent prompt, model, tool, and retrieval tests as repeatable matrices with pass/fail assertions and release decisions.
- **Model gateway evidence**: record route, provider/model, fallback used, retry count, budget decision, rate-limit reason, and final response status before the Agent decides to continue.
- **Inference runtime metrics**: capture throughput, latency percentile, timeout, concurrency, batching, and resource pressure for self-hosted or gateway-managed inference.
- **Platform app boundary**: separate user chat surface, app workflow, tool calls, knowledge sources, permissions, and audit trail in production Agent portals.
- **Guardrail evidence**: record validator name, verdict, repair attempt, fail-closed decision, matched policy, and owner so safety checks are replayable.
- **Safety eval battery**: maintain versioned tests for prompt injection, refusal, data leakage, toxicity/harm, hallucination, and safety-vs-usability tradeoffs.
- **Trace dataset loop**: convert production traces into reviewed datasets, annotation labels, and eval cases without treating raw private prompts as golden fixtures.
- **Memory governance evidence**: record memory source, confidence, owner, conflict, update/delete action, and privacy scope before using memory as evidence.
- **Local model boundary**: separate local model registry, pull/run command, model id/version, resource limits, network policy, and trace fields for private inference.
- **Experiment evidence**: bind prompt, model, tool, and dataset changes to run id, parameters, metrics, artifacts, and comparison decision.
- **MCP server boundary**: record server id, tool name, input schema, permission scope, transport/lifecycle state, result status, and audit actor before execution.
- **Graph state boundary**: define state schema, node transitions, checkpoint id, retry count, interrupt owner, and stop condition for multi-step Agent flows.
- **Typed tool output**: validate tool and model outputs against schema before downstream state changes; record validation errors and retry budget.
- **RAG pipeline boundary**: keep ingestion, retrieval, ranking, reranking, citation, and answer policy as separate evidence points.
- **Browser action trace**: record visible context, action intent, DOM/screenshot summary, retry budget, and rollback note for UI-changing actions.

## Contributor Workflow

When adding another open-source project, submit in this order:

1. One-paragraph topic summary without copied code.
2. Stable pattern analysis.
3. Framework-specific details isolated in a Lab or comparison table.
4. Mapping to local Agent-Top concepts, Labs, cases, or interviews.
5. Verified external repository URL and license note for maintainers.

## Local Mapping Examples

| External theme | Agent-Top entry point |
| --- | --- |
| RAG evaluation | [`../l3-rag-memory-observability.md`](../l3-rag-memory-observability.md), [`../../labs/l3/rag_evaluator/README.md`](../../../labs/l3/rag_evaluator/README.md) |
| Supervisor routing | [`../../labs/l3/multi_agent_supervisor/README.md`](../../../labs/l3/multi_agent_supervisor/README.md) |
| Release regression | [`../l4-production.md`](../l4-production.md), [`../../labs/l4/regression_gate/README.md`](../../../labs/l4/regression_gate/README.md) |
| Production postmortem | [`../../labs/l4/production_postmortem/README.md`](../../../labs/l4/production_postmortem/README.md) |
| Cost and stability guardrails | [`../../labs/l4/cost_and_stability_guardrails/README.md`](../../../labs/l4/cost_and_stability_guardrails/README.md) |
| Cost and stability operations | [`../l4-production.md`](../l4-production.md), [`../production/cost-stability-operations.md`](../production/cost-stability-operations.md) |
| Original patterns | [`../l5-custom-patterns.md`](../l5-custom-patterns.md), [`../../labs/l5/pattern_catalog/README.md`](../../../labs/l5/pattern_catalog/README.md) |
| Coding Agent workspace safety | [`../concepts/implementation-guide.md`](../concepts/implementation-guide.md), [`../production/safety-checklist.md`](../production/safety-checklist.md) |
| Coding Agent eval design | [`../production/evals-playbook.md`](../production/evals-playbook.md), [`../../labs/l4/regression_gate/README.md`](../../../labs/l4/regression_gate/README.md) |
| Data-source ingestion safety | [`../concepts/rag-memory-mcp-flow.md`](../concepts/rag-memory-mcp-flow.md), [`../../examples/data-source-policy/README.md`](../../../examples/data-source-policy/README.md) |
| Browser or desktop action safety | [`../concepts/implementation-guide.md`](../concepts/implementation-guide.md), [`../production/safety-checklist.md`](../production/safety-checklist.md) |
| Evaluation gate and regression evidence | [`../production/evals-playbook.md`](../production/evals-playbook.md), [`../../examples/agent-eval-regression/README.md`](../../../examples/agent-eval-regression/README.md) |
| GitHub-native review workflow | [`../concepts/implementation-guide.md`](../concepts/implementation-guide.md), [`../../examples/github-agent-review/README.md`](../../../examples/github-agent-review/README.md) |
| Code execution sandboxing | [`../concepts/implementation-guide.md`](../concepts/implementation-guide.md), [`../production/safety-checklist.md`](../production/safety-checklist.md) |
| Error grouping and incident routing | [`../production/observability-trace-contract.md`](../production/observability-trace-contract.md), [`../../examples/observability-trace/README.md`](../../../examples/observability-trace/README.md) |
| Runtime profiling and cost hotspots | [`../production/cost-stability-operations.md`](../production/cost-stability-operations.md), [`../../examples/observability-trace/README.md`](../../../examples/observability-trace/README.md) |
| Deterministic lint gate | [`../production/evals-playbook.md`](../production/evals-playbook.md), [`../../examples/observability-trace/README.md`](../../../examples/observability-trace/README.md) |
| Tool and dependency lock evidence | [`../l4-production.md`](../l4-production.md), [`../../examples/observability-trace/README.md`](../../../examples/observability-trace/README.md) |
| Workflow provenance | [`../concepts/multi-agent-scheduling.md`](../concepts/multi-agent-scheduling.md), [`../production/observability-trace-contract.md`](../production/observability-trace-contract.md) |
| GenAI telemetry vocabulary | [`../production/observability-trace-contract.md`](../production/observability-trace-contract.md), [`../../examples/observability-trace/README.md`](../../../examples/observability-trace/README.md) |
| Eval-as-CI | [`../production/evals-playbook.md`](../production/evals-playbook.md), [`../../examples/agent-eval-regression/README.md`](../../../examples/agent-eval-regression/README.md) |
| Model gateway evidence | [`../production/cost-stability-operations.md`](../production/cost-stability-operations.md), [`../../examples/model-gateway/README.md`](../../../examples/model-gateway/README.md) |
| Inference runtime metrics | [`../production/cost-stability-operations.md`](../production/cost-stability-operations.md), [`../../examples/model-gateway/README.md`](../../../examples/model-gateway/README.md) |
| Platform app boundary | [`../concepts/agent-system-architecture.md`](../concepts/agent-system-architecture.md), [`../production/safety-checklist.md`](../production/safety-checklist.md) |
| Guardrail evidence | [`../production/safety-checklist.md`](../production/safety-checklist.md), [`../../examples/safety-eval/README.md`](../../../examples/safety-eval/README.md) |
| Safety eval battery | [`../production/evals-playbook.md`](../production/evals-playbook.md), [`../../examples/safety-eval/README.md`](../../../examples/safety-eval/README.md) |
| Trace dataset loop | [`../production/observability-trace-contract.md`](../production/observability-trace-contract.md), [`../../examples/agent-eval-regression/README.md`](../../../examples/agent-eval-regression/README.md) |
| Memory governance evidence | [`../concepts/long-term-memory.md`](../concepts/long-term-memory.md), [`../../examples/memory-vs-evidence/README.md`](../../../examples/memory-vs-evidence/README.md) |
| Local model boundary | [`../production/cost-stability-operations.md`](../production/cost-stability-operations.md), [`../production/safety-checklist.md`](../production/safety-checklist.md) |
| Experiment evidence | [`../production/evals-playbook.md`](../production/evals-playbook.md), [`../production/observability-trace-contract.md`](../production/observability-trace-contract.md) |
| MCP server boundary | [`../skills/tool-mcp-safety.md`](../skills/tool-mcp-safety.md), [`../../examples/mcp-tool-boundary/README.md`](../../../examples/mcp-tool-boundary/README.md) |
| Graph state boundary | [`../concepts/plan-decision-making.md`](../concepts/plan-decision-making.md), [`../../examples/mcp-tool-boundary/README.md`](../../../examples/mcp-tool-boundary/README.md) |
| Typed tool output | [`../concepts/agent-system-architecture.md`](../concepts/agent-system-architecture.md), [`../production/evals-playbook.md`](../production/evals-playbook.md) |
| RAG pipeline boundary | [`../l3-rag-memory-observability.md`](../l3-rag-memory-observability.md), [`../production/evals-playbook.md`](../production/evals-playbook.md) |
| Browser action trace | [`../concepts/implementation-guide.md`](../concepts/implementation-guide.md), [`../production/safety-checklist.md`](../production/safety-checklist.md) |

## Maintenance Rule

External projects change quickly. Keep the project list as a discovery and pattern map, not as authoritative framework documentation. When a project introduces a stable learning theme, update the local concept page or Lab and leave framework API details in the Lab.
