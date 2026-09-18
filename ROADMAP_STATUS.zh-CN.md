---
title: 路线状态
validated_date: 2026-09-18
---

# 路线状态

## 当前状态

| 模块 | 状态 | 证据 |
| --- | --- | --- |
| 仓库基础 | Done | `README.md`, `README.zh-CN.md`, `LICENSE`, `.gitignore` |
| 具体框架 | Done | `docs/en/agent-top-concrete-framework.md` |
| 概念 | Done | `docs/en/concepts/`, 包括架构、MCP、多 Agent 调度、长期记忆、模型幻觉、Plan 决策、核心概念深挖来源和核心 Agent 实施手册 |
| 框架地图 | Done | `docs/en/frameworks/framework-map.md` |
| 可执行 Lab | Done | `labs/l0` 到 `labs/l5`，包括补充 Lab |
| 任务优先入口 | Done | `docs/en/tutorials/quick-navigation.md`、`docs/zh/tutorials/快速导航卡.md`、`examples/README.md`、`examples/agent-decision-trace/`、`examples/rag-evidence-refusal/`、`examples/memory-vs-evidence/`、`examples/coding-workspace-safety/`、`examples/data-source-policy/`、`examples/coding-task-navigation/`、`examples/agent-eval-regression/`、`examples/github-agent-review/` 和 `examples/observability-trace/`, `examples/model-gateway/`, `examples/safety-eval/`, `examples/mcp-tool-boundary/`, `examples/memory-index-evidence/`, `examples/release-gate-evidence/`、`examples/multilingual-support/`、`examples/compliance-review/`, 包括 runtime、gateway、safety、tool-boundary、index、release-gate、多语言路由、基于证据的审批 evidence |
| 设计审查资产 | Done | `docs/en/concepts/design-review-workshop.md`、`docs/en/concepts/agent-system-blueprint.md` 及中文镜像 |
| 练习手册 | Done | `docs/en/tutorials/practice-handbook.md` 及中文镜像 |
| 贡献资产 | Done | 案例研究模板、贡献自查清单和增强 PR 模板 |
| 评估 Playbook | Done | `docs/en/production/evals-playbook.md`、中文镜像和 eval report 模板 |
| 开源模式矩阵 | Done | `docs/en/tutorials/open-source-pattern-matrix.md`、中文镜像、`examples/memory-vs-evidence/`、`examples/coding-workspace-safety/`、`examples/data-source-policy/`、`examples/coding-task-navigation/`、`examples/agent-eval-regression/`、`examples/github-agent-review/` 和 `examples/observability-trace/`, `examples/model-gateway/`, `examples/safety-eval/`, `examples/mcp-tool-boundary/`, `examples/memory-index-evidence/`, `examples/release-gate-evidence/`, 包括 runtime、gateway、safety、tool-boundary、index、release-gate evidence |
| 详细教程 | Done | `docs/en/` 和 `docs/zh/` 覆盖 L0-L5 |
| 行业对标与 L5 专家路径 | Done | `docs/en/tutorials/industry-benchmark-and-l5-expert-path.md`、中文镜像和 `templates/l5-expert-evidence-template.md` |
| 团队 Agent 基础设施 | Done | `docs/en/production/team-agent-infrastructure.md`、`docs/zh/production/团队Agent基础设施.md` |
| 中文教程文件名 | Done | `docs/zh/` 下的中文镜像 |
| 面试资产 | Done | `docs/en/interviews/`, `docs/zh/interviews/`, 含 STAR 回答范例 |
| 作品集路径 | Done | `docs/en/portfolio/projects.md`、个人 Agent 作品集、开源影响力指南 |
| 生产指南 | Done | `docs/en/production/`、成本稳定性运行手册、评估与回归 Playbook、可观测性与 Trace 契约、生产速查表、`examples/observability-trace/`, `examples/model-gateway/`, `examples/safety-eval/`, `examples/mcp-tool-boundary/`, `examples/memory-index-evidence/`, `examples/release-gate-evidence/`, 包括 runtime、gateway、safety、tool-boundary、index、release-gate evidence |
| 案例研究 | Done | `docs/en/cases/` |
| 速查表 | Done | `docs/en/quick-reference/` |
| Agent 技能体系 | Done | `docs/en/skills/README.md`、`docs/zh/skills/Agent技能指南.md`、`templates/agent-skill-card-template.md` |
| Vibe Coding | Done | `docs/en/vibe-coding/README.md` 与 `docs/zh/vibe-coding/README.md`，含规范先行、运行校验与常见踩坑指南，以及 `labs/l5/vibe_coding_spec` Lab 与双语规范模板 |
| 双语文档结构 | Done | `docs/en/` + `docs/zh/` |
| 社区治理 | Done | `GOVERNANCE.md`, `CONTRIBUTING.md`, `CONTRIBUTING.zh-CN.md`, `docs/en/community/` |
| GitHub 标签配置 | Done | `.github/labels.yml` |
| 安全策略 | Done | `SECURITY.md`, `SECURITY.zh-CN.md` |
| CI 检查 | Done | `.github/workflows/ci.yml` |
| 可复用模板 | Done | `templates/`，含 Agent 设计模板和 postmortem 模板 |

## 健康目标

| 指标 | 目标 |
| --- | --- |
| 死链率 | < 1% |
| 双语同步 | <= 14 天 |
| 框架示例保鲜 | 过期阈值前 review |
| 审查覆盖 | 每个活跃模块 >= 2 个备份 |
| Lab 测试覆盖 | 97 个确定性 Lab 测试本地通过 |

## 近期改进

| 模块 | 状态 | 证据 |
| --- | --- | --- |
| README 目录树 | Done | `README.md` 和 `README.zh-CN.md` 中的精简目录树 |
| Lab 层入口 README | Done | `labs/README.md` 和 `labs/l0/README.md` 到 `labs/l5/README.md` |
| 文档索引交叉引用 | Done | `docs/en/README.md` 和 `docs/zh/README.md` 现已链接 Labs 与 Examples 索引 |
| CI link-and-artifact-integrity job | Done | `.github/workflows/ci.yml` 中的 `link-and-artifact-integrity` job |
| 仓库检查 | Done | `scripts/check_repository.py` 中的 `check_docs_topic_dirs`、`check_lab_level_readmes`、`check_example_dirs_readmes` 和 `check_readme_mentions_lab_levels` |
| 贡献 Quality Gates | Done | `CONTRIBUTING.md` 和 `CONTRIBUTING.zh-CN.md` 中的 `Quality Gates` 章节 |
| 文档站点 Labs 入口 | Done | `docs-site/index.html` 中的 Labs 导航条目 |
| 模板双语覆盖 | Done | 全部 22 对模板均有 EN/CN 镜像；`docs-site/search.html` 覆盖全部 289 个 markdown 文件 |

## 下一步优先级

将路线愿景拆解为可追踪的任务。主题 1-3 为核心承诺；主题 4-5 为可选新增。

### 1. 真实世界案例扩充

- [x] 在 `examples/` 下新增多语言客服场景（如 `examples/multilingual-support/`），覆盖语言路由、跨语言记忆与拒答降级。验收：包含 README 与可运行的 trace/evidence，且 `check_example_dirs_readmes` 通过。
- [x] 新增合规审查场景（如 `examples/compliance-review/`），演示基于证据的审批决策与审计日志。验收：遵循 `examples/README.md` 中的既有示例模板。
- [x] 为既有示例目录（如 `examples/rag-evidence-refusal/`、`examples/model-gateway/`）补充“扩展练习”提示。验收：每个示例 README 列出 2-3 个关联教程或 Lab 的延伸练习。
- [x] 新示例落地后同步刷新 `examples/README.md` 索引与开源模式矩阵相关行。验收：EN/ZH 两份索引文件均有交叉引用。

### 2. 双语 SLA 维持

- [x] 新文档从创建之日起即为 EN/ZH 成对提交；标记只添加单语文的 PR。验收：CI 中 `scripts/check_repository.py` 的双语检查通过。
- [x] 任一侧修改时同步刷新两侧镜像的 `last-synced` frontmatter。验收：无任何 EN/ZH 成对文档漂移超过 14 天健康目标。
- [ ] 每个 PR 与每季度运行 `scripts/check_repository.py`，合并前修复死链与缺失镜像。验收：`check_repository.py` 的 CI job 保持绿色。

### 3. 框架示例保鲜

- [x] 上游 API 变化时，对框架文档（`docs/en/frameworks/`、`docs/en/agent-top-concrete-framework.md`）保持 `sync-required` 标签流程。验收：PR 模板包含该标签的检查项。
- [x] 在框架示例 frontmatter 中记录 `tested_against` 与 `validated_date`（如 `examples/model-gateway/`、`examples/mcp-tool-boundary/`）。验收：所有示例 frontmatter 均包含这两个键。
- [x] 依据 `docs/en/production/quarterly-maintenance.md` 维护季度维护日历，在过期阈值前 review 框架示例。验收：季度 review 记录落入 `templates/monthly-contributor-report.md` 或维护日志。

### 4. Labs 覆盖（可选新增）

- [x] 新增 L4 实战 Lab：真实部署卫生（可观测性 + 成本 + 发布门禁）。验收：`labs/l4/` 下新增带 README 链接的 Lab，含 2+ 个确定性测试。
- [x] 新增 L5 实战 Lab：多 Agent 生产监督与故障响应。验收：Lab 双语呈现，并纳入 `labs/README.md` 与 CI Lab 测试。

### 5. 社区运营（可选新增）

- [x] 使用 `templates/monthly-contributor-report.md` 发布月度贡献者报告。验收：报告按月提交到 `docs/en/community/`。
- [x] 建立社区实验节奏（如每季度一个实验）：先提案、原型验证，再晋升或归档示例/Lab 候选。验收：`docs/en/community/` 下存在实验记录。

优先级顺序：先完成主题 1-3；当贡献者带宽允许时，再排期主题 4-5。

## 完成说明

仓库现已包含核心学习框架、可运行 Labs、双语 L0-L5 教程、面试题库、面试答案范例、作品集路径、开源影响力指南、生产指南、可复用设计模板、社区运营、治理与 CI 检查。
