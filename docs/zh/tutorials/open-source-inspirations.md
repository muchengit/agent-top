---
i18n-key: tutorials-open-source-inspirations
last-synced: 2026-09-16
validated_date: 2026-09-16
---

# 开源项目灵感目录

本页基于常见 GitHub 开源 Agent 项目提炼主题。Agent-Top 不复制外部代码或正文；只把稳定学习主题映射到本地文档、Lab 和案例。

由于当前环境无法实时访问 GitHub，项目名作为维护者灵感索引；提交外部链接前请核对仓库地址和 license。

## 项目主题映射

| 项目 | 主题 | Agent-Top 吸收点 |
| --- | --- | --- |
| langchain | LLM application framework | tool calling、chains、memory、structured outputs |
| LangGraph | stateful graph workflows | explicit state、cycles、checkpointing、human-in-the-loop |
| LlamaIndex | RAG and data framework | retrieval、chunking、indexing、evaluation |
| Haystack | search and RAG pipeline | document pipelines、rankers、retriever boundaries |
| AutoGen | conversational multi-agent | message passing、role boundaries、group chat |
| CrewAI | role-based agent teams | task delegation、role prompts、workflows |
| smolagents | minimal agent examples | code-first actions、readability、small tool surfaces |
| Agno | lightweight agent runtime | fast iteration、agent state、tool integration |
| Pydantic AI | typed agents | schema-first validation、structured outputs、typed tools |
| Instructor | structured output extraction | JSON schema, validation, retry on extraction failures |
| DSPy | programmatic prompt optimization | signatures、metrics、optimizers、eval-driven tuning |
| OpenAI Agents SDK | model and agent tools | tool definitions、handoffs、guardrails、tracing |
| Claude Agent SDK / tool use patterns | tool-using assistant | tool execution loops、structured tool results、safety boundaries |
| Google ADK | application development kit | multi-agent app structure、workflow composition、platform tools |
| Semantic Kernel | enterprise plugins and orchestration | plugin governance、enterprise plugins、process integration |
| MCP ecosystem / modelcontextprotocol | tool and context protocol | tool discovery、resource exposure、protocol boundaries |
| Letta / MemGPT | agent memory | memory layers、summarization、long-term context |
| Mem0 | memory platform | memory extraction、deduplication、privacy considerations |
| Langfuse / OpenTelemetry GenAI patterns | tracing and observability | span naming、prompt/model/tool traces、cost and latency |
| Ragas / DeepEval / Arize Phoenix | RAG and LLM eval | faithfulness、answer relevance、hallucination, guardrail evals |
| DSPy / promptfoo / eval-driven examples | evaluation and regression | eval datasets、prompt regression, safety checks |
| SuperAGI / AgentOps-like projects | agent platforms | mission/task modeling, dashboarding, lifecycle observability |
| ELK / Elasticsearch / Kibana-like tooling | production observability | structured logs, trace visualization, alerting |
| Postmortem templates and incident-response repos | incident learning | blameless review、action ownership、recurrence prevention |
| Awesome LLM / Agent lists | community discovery | topic discovery, taxonomy, contribution routing |

## 可吸纳模式

- **Tool schema-first**：先定义工具输入、输出、风险，再写 prompt。
- **Graph/stateful workflows**：复杂流程显式建模状态和跳转。
- **Role-based teams**：角色必须有职责边界和停止条件。
- **Structured output**：模型输出进入 schema validation。
- **RAG evaluation**：检索质量、答案相关性、证据忠实度分开评估。
- **Memory lifecycle**：抽取、去重、过期、删除都要有策略。
- **Observability contract**：每轮记录 prompt、tool、retrieval、guardrail、cost、latency。
- **Incident learning**：事故必须转成 eval、guardrail、trace 或 rollback action。

## 贡献者提示

如果你想从开源项目补充 Agent-Top，请按这个顺序提交：

1. 主题摘要，不粘贴代码。
2. 稳定模式分析。
3. 框架特定细节放入 Lab 或对比表。
4. 对应 Agent-Top 本地 Lab 或案例。
5. 后续维护者需要核验的外部链接。
