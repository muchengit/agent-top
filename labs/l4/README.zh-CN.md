---
title: L4 Labs
capability_level: L4
validated_date: 2026-09-19
---

# L4 Labs

英文版：[`README.md`](README.md)

## 目标

将 Agent 系统生产化：评估、安全、部署、成本与复盘。

## 前置条件

- L3：端到端 RAG、记忆与多 Agent 流程
- Python 3.10+
- 了解发布门禁与可观测性契约

## 本级别 Labs

- [`production_postmortem`](production_postmortem/README.md)：可执行的生产复盘结构、覆盖检查与行动项闭环。
- [`regression_gate`](regression_gate/README.md)：安全、trace、回滚与成本的发布门禁。
- [`cost_and_stability_guardrails`](cost_and_stability_guardrails/README.md)：运行时成本、延迟、重试与降级护栏。
- [`production_trace_integrity`](production_trace_integrity/README.md)：面向生产可观测性的确定性 trace 完整性校验。
- [`deployment_hygiene`](deployment_hygiene/README.md)：结合可观测性、成本与发布门禁的部署决策。

## 运行

```bash
python -m unittest discover -s labs/l4 -p "test_*.py"
```

## 常见踩坑

- 不做回归门禁就部署，门禁需检查安全、trace、回滚与成本。
- 写复盘只描述症状，没有覆盖度与行动项闭环。
- 忽略降级护栏，直到成本或延迟事故发生。

## 自检

1. 发布门禁在生产部署前校验什么？
2. 如何证明复盘行动项已闭环？
3. 哪些护栏在运行时保护成本与稳定性？
