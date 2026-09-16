# Agent-Top 风格规范

Agent-Top 使用模式优先、中英双语、文档 + Lab 的工作流。保持改动小、可审查、可运行。

## 内容原则

- 先教稳定模式，再教框架 API。
- 英文内容放在 `docs/en`，中文结构镜像到 `docs/zh`。
- 框架相关代码放入 Lab。
- 优先选择无需 API key 的本地示例。
- 解释失败模式，不只写 happy path。
- 用 trade-off 解释，而不是口号。

## Markdown 规范

- 默认使用 Markdown。
- 图表使用 Mermaid 或可编辑源。
- 教程和 Lab 应包含预期输出。
- 对比和评分用表格。
- 中英文镜像的标题结构尽量一致。

## Frontmatter

`docs/en` 和 `docs/zh` 下的双语文档应包含：

```yaml
i18n-key: stable-key
last-synced: YYYY-MM-DD
validated_date: YYYY-MM-DD
```

框架相关或时效性内容使用 `validated_date`。Lab 或框架示例使用 `tested_against`。

## 链接

- 优先使用能通过 `python scripts/check_repository.py` 的相对链接。
- 英文文档可直接链接 Lab。
- 中文文档存在中文镜像时优先链接中文。
- 英文内容完整时，不要让中文页面停留在占位状态。

## Lab 规范

每个 Lab 应包含：

- Goal。
- Prerequisites。
- Run command。
- Common Pitfalls。
- Self-Check。
- 确定性测试覆盖。

Lab 不应要求 API key，也不应调用真实生产系统。

## 术语表

核心术语保持稳定翻译：

- Agent: Agent
- RAG: RAG
- MCP: MCP
- ReAct: ReAct
- Guardrail: guardrail / 护栏
- Rollback: rollback / 回滚
- Postmortem: postmortem

## 审查清单

提交前运行：

```bash
python scripts/check_repository.py
python -m unittest discover -s labs -p "test_*.py"
python -m compileall -q labs scripts
python -m ruff check .
```

好的 PR 应说明：

- 改了什么。
- 为什么改。
- 跑了哪些检查。
- 是否影响双语同步。
- 框架或 Lab 示例是否需要 `validated_date` 或 `tested_against`。
