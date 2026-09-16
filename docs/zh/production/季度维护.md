---
i18n-key: production-quarterly-maintenance
last-synced: 2026-09-16
validated_date: 2026-09-16
---

季度维护指南

季度维护让 Agent 内容保持新鲜，但不把文档变成维护负担。

## Review 步骤

1. 检查每个 `validated_date`。
2. 检查 Lab 的 `tested_against`。
3. 运行 repository checks。
4. 运行 Lab tests。
5. 扫描死链。
6. 扫描 framework breaking changes。
7. Review translation sync。
8. Review deprecated content。
9. Check contributor workload。

## 健康指标

- Completion rate。
- Translation sync <= 14 days。
- Dead link rate < 1%。
- Stale Lab rate。
- Burnout signals。
- Reader feedback NPS。

## Breaking Change 流程

1. 加 `breaking-change` 标签。
2. 检查 Lab 是否仍运行。
3. 更新 `validated_date` 和 `tested_against`。
4. 一个季度未更新则 deprecated。
5. 提供 replacement link。

