---
i18n-key: community-translation-workflow
last-synced: 2026-09-16
validated_date: 2026-09-16
---

翻译流程

英文 `docs/en` 是主源。中文 `docs/zh` 通过元数据保持同步。

## 必要元数据

```yaml
i18n-key: stable-key
last-synced: YYYY-MM-DD
```

## 流程

1. 英文源内容变化。
2. 添加或更新 `i18n-key`。
3. 打开或认领 `translation-needed`。
4. 翻译贡献者更新中文文件。
5. Reviewer 检查含义、术语和链接。
6. Maintainer 检查 `last-synced`。
7. 滞后则加 `sync-required`。

## SLA

- 主动认领后 3 个工作日内完成。
- 整体双语同步不超过 14 天。
- 不要静默保留过期中文内容。

