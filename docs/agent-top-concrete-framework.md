# Agent-Top 具体框架（Concrete Framework）

> 本文由 5 位领域专家第一轮发散 + 首席框架设计师第二轮收敛讨论产出：
> 🏗️ Agent 系统架构专家 · 🎓 AI 教育/课程设计专家 · 🌐 开源社区运营/DevRel 专家 · 💼 技术招聘/面试教练 · ✍️ 技术内容策略专家。
>
> 配套文档：[agent-top-roadmap.md](agent-top-roadmap.md)（高层路线图）。本框架是其“具体落地版”。

---

## 一、讨论过程与冲突裁决（C1–C9）

| 编号 | 冲突双方 | 裁决 |
| --- | --- | --- |
| C1 | 架构（深度） vs 教育（浅度） | L2 以“能跑通并解释权衡”为出口，框架只教稳定边界与原理，不深挖源码。 |
| C2 | 架构（模式优先） vs 面试（广度速成） | 教程讲模式/原理深，面试讲广度速成 + 题型速刷；框架在教程侧按模式归类，面试侧仅做对照速查。 |
| C3 | 教育 vs 社区（翻译量） | 翻译是社区 DevRel 一等贡献路径（`translation-needed` 认领）；教育侧只交付 EN 主源并标注待译章节。 |
| C4 | 架构 vs 社区（评审瓶颈） | 技术评审分级：Maintainer 审架构/安全，Reviewer 审普通 Lab；框架“稳定边界清单”免深层评审。 |
| C5 | 内容 vs 社区（评审负载） | 产出与审校分离轮值：同人同月不兼作者与双审；Contributor of the Month 给免审额度。 |
| C6 | 内容 vs 教育（形态） | 默认 Markdown + 可执行 Lab 为唯一标准形态；富媒体仅作补充附件，不进主干。 |
| C7 | 面试 vs 教育（评估重叠） | 共用 rubric 但分流：学习评估测“会做”（quiz + demo），求职评估测“能讲权衡”（评分卡）。 |
| C8 | 内容 vs 开发指导（Lab 重复） | 开发指导的 Lab 即内容示例唯一来源；教程正文只引链接，不重复贴同类源码。 |
| C9 | 架构 vs 文档站（双语放大成本） | 框架示例一律带 `tested_against` 版本锚 + `validated_date`；CI 监测滞后自动开 `sync-required`，过期打 `deprecated`。 |

---

## 二、最终 L0–L5 能力模型

| 等级 | 定位 | 可测量出口标准 |
| --- | --- | --- |
| L0 入门 | 跑通第一个 LLM 调用 | 完成 1 个 API demo，并能口语化解释 token / 上下文窗口 / 系统提示。 |
| L1 核心 | 理解 Agent 四大组件 | 纯 Python 手搓最小 ReAct Agent 跑通，并讲清感知 / 工具 / 规划 / 记忆职责（无框架）。 |
| L2 框架层 | 用框架做可靠单 Agent | 完成单 Agent 项目 + 框架对比笔记，并调通 1 个 MCP server。 |
| L3 系统 | 端到端系统能力 | 自研 RAG pipeline + 接 Mem0 / Letta + Langfuse 评估报告；理清 RAG → 记忆 → 多 Agent → MCP 数据流。 |
| L4 生产 | 生产级工程化 | 完成多智能体拓扑设计 + 评估指标与自动化回归 + 安全护栏 + 成本优化；附 Postmortem 与线上复盘。 |
| L5 专家 | 定义标准 / 产出影响 | 形成原创框架或模式，并有开源 PR / 论文 / 演讲等外部影响力物证。 |

---

## 三、模块地图与学习路径

### 依赖排序

基础 → 核心四组件 → 框架层 → 数据流转 → 评估/可观测 → 安全/部署 → 自由组合

### 路径原则

先概念后代码 · 先本地后生产 · 先单组件后系统

### 模块要点

| 等级 | 模块要点 |
| --- | --- |
| L0 | API 基础、Prompt 工程 |
| L1 | 感知、工具调用、规划循环、记忆机制 |
| L2 | 选 1 主线框架深做（图编排 / 多智能体 / 轻量 / SDK 四阵营对照），其余对比；MCP 接入 |
| L3 | RAG pipeline、长期记忆（Mem0 / Letta）、可观测（Langfuse）、多 Agent 通信 |
| L4 | 评估体系、可观测性、安全护栏、部署与成本 |
| L5 | 原创模式、开源贡献、团队 Agent 基础设施 |

### 内容形态占比

概念讲解 30% · 代码 Lab 35% · 案例研究 20% · 速查表 10% · 论文导读 5%

---

## 四、内容生产标准

### 文章 / Lab 模板

目标 → 前置（Lx + 依赖 + 时长）→ 步骤 → 代码（`tested_against` 版本）→ 踩坑 → 自测（3–5 题）

### 图表规范

- 仅使用 Mermaid 或可编辑源。
- 每张图必须带图注与“适用能力层 Lx”标签。
- 风格必须解释“为什么”。

### 保鲜 / 弃用流程

- 每篇头部写明 `validated_date` + `tested_against`（框架 / SDK 版本）。
- 季度 review 扫描死链 / 过期内容；breaking change 即时标记 `yellow-flag`。
- 过期内容打 `deprecated` 徽章，并指向替代文；保留 1 季度后归档。

### 生产级思维差异化

强制包含以下板块：

- Postmortem
- Trade-off 论证
- Production Checklist（鉴权 / 限流 / 可观测 / 评估集）

### 健康度指标

完成率 · 双语同步率（≤14 天）· 死链率（<1%）· 读者反馈 NPS

---

## 五、双语贡献与社区框架

### 角色分级

Contributor → Reviewer → Maintainer → Core

### 四类贡献路径

撰稿 / 翻译 / 校对 / 维护

### 入口

`good first issue` · `docs-only` · `translation-needed`

### 双语工作流

- 平行目录：`docs/en` + `docs/zh`
- frontmatter 包含：`i18n-key` + `last-synced`
- `translation-needed` 认领锁定
- CI 监测 `last-synced` 滞后后，自动开 `sync-required`
- EN 为主源，ZH 由贡献者认领；每章 ≤3 天出 ZH

### 社区与增长

- 主阵地：GitHub Discussions
- 补充阵地：Discord / 微信群 / 论坛
- 内容节奏：双周教程 / 月度面试题 / 季度路线图回顾
- 活动节奏：季度 Hackathon / 双周论文共读 / 月度 showcase
- 激励闭环：Contributor of the Month

### 治理与质量

- `GOVERNANCE.md`
- 每模块 ≥2 备份，季度轮值，防 burnout
- 双审制：内容审 + 语言审
- `STYLE.md` + `glossary` 术语表
- CI 校验：拼写 / 链接 / i18n / 死链 / 构建预览

---

## 六、面试框架

### 题库

- 二维结构：知识模块 × 难度（L1–L5）
- 题型路径：概念 → 实现 → 调试 → 设计
- 每条题包含：答案要点 + 面试官想听（trade-off / 生产反例 / 数据思维）

### 系统设计题

题目：从零设计多智能体客服系统

评分维度：

- 需求拆解
- 组件划分
- 通信
- 错误隔离
- 可观测
- 成本与延迟

### STAR 模板 + 作品集验证

对应 4 个项目梯度：

1. 个人知识库 Agent → 证明 RAG + 记忆能力
2. 企业多工具 Agent → 证明 Tool / MCP 编排能力
3. 多 Agent 协作项目 → 证明编排与一致性能力
4. 自研框架 → 证明抽象与工程化深度

### 评分卡

| 等级 | 评分重点 |
| --- | --- |
| L1 | 组件理解 + 跑通 demo（70%） |
| L2 | 可靠单 Agent + guardrail |
| L3 | 多 Agent 无单点失败 |
| L4 | 生产化 + 有线上复盘 |
| L5 | 架构权衡 + 垂直专家能力 |

### 2026 雇主实际考察重点

评估体系、安全护栏、生产化思维、线上复盘。

典型追问：给定 incident，说明 root cause 与防复发方案。

---

## 七、框架覆盖总策略（模式优先 · 抗速朽）

### 根本原则

模式优先于框架。

### 执行方式

- 教程深挖 ReAct / 规划 / 记忆 / 多 Agent 拓扑等稳定模式。
- 框架仅作“稳定边界”示例。
- 框架代码隔离在 Lab；原理文字独立，强调 first principles。
- 统一标注版本与 `validated_date`。
- CI 监测滞后与 breaking change。

### 17 个框架按阵营抽象对照

| 阵营 | 代表框架 |
| --- | --- |
| 图编排 | LangGraph |
| 多智能体 | CrewAI, AutoGen |
| 轻量 | Smolagents, Agno |
| SDK | OpenAI, Claude, Google ADK |
| 类型安全 | Pydantic AI |
| 企业 | Semantic Kernel |
| RAG | LlamaIndex, Haystack |
| 优化 | DSPy |

### 对应冲突落地

- C1：深度给模式、浅度给框架。
- C2：教程讲模式深、面试讲广度快。
- C9：版本锚 + 自动 sync 控成本。
