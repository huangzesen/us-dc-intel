---
name: astro-gridwatch
version: 1.0.0
description: |
  维护 GRIDWATCH 数据中心情报看板（Astro 正式版）。
  任何 agent 读此技能后可接手：重新导出数据、重新构建、部署到 GitHub Pages。
  看板位于 https://xhelio.ai/datacenters/（由 huangzesen/xhelio-datacenters 的 GitHub Pages + Cloudflare CNAME 提供）。
---

# GRIDWATCH Astro 看板维护契约

## 这是什么

`astro/` 是 US + 美洲数据中心情报的正式看板实现（GRIDWATCH 风格：SCADA×彭博、暗色主题、中英双语、国家范围切换）。

## 数据流

```
scripts/expansion/americas/results/batch-*.jsonl  （探索 daemon 产出）
        ↓ scripts/merge_americas.py（幂等合并，写 country/subnational 列）
scripts/merge_all_sources.py（US 部分：county/state/discovery → centers.jsonl + datacenters.db）
        ↓ scripts/export_astro_data.py（从 datacenters.db 聚合 states/funnel/years/developers/evidence/countries）
astro/src/data/datacenters.json
        ↓ npm run build
astro/dist/index.html（单文件静态页）
        ↓ 部署
huangzesen/xhelio-datacenters/datacenters/index.html → https://xhelio.ai/datacenters/
```

## 如何更新（全流程）

1. **探索新数据**：按 `scripts/expansion/americas/explore-brief.md` 契约派 daemon 探索新的国家/行政区，结果写入 `scripts/expansion/americas/results/batch-<NNN>.jsonl`。
2. **合并入 DB**：`python scripts/merge_americas.py`（美洲）+ `python scripts/merge_all_sources.py`（US）→ 生成 `datacenters.db`。
3. **导出看板数据**：`python scripts/export_astro_data.py` → 更新 `astro/src/data/datacenters.json`。
4. **构建**：`cd astro && npm run build`。
5. **验证**：`grep -rE '/Users/|scratch/|daemons/|logs/|token_' dist/` 必须无命中（防内部路径泄漏）。
6. **部署**：把 `astro/dist/` 内容推送到 `huangzesen/xhelio-datacenters` 仓库的 `datacenters/` 目录（⚠️ 仓库根 `index.html` 是 457B 重定向页，切勿覆盖；真正页面在 `datacenters/index.html`）。
7. **线上验证**：curl https://xhelio.ai/datacenters/ 检查 HTTP 200 与内容大小/关键字。Cloudflare CDN 缓存约 1-2 分钟刷新。

## 关键文件

- `astro/src/pages/index.astro`：单页看板（hero 计数、州/国家 tile 图、漏斗、年份浪潮、developer 榜、注册表、Dark/Light、EN/中文）。
- `scripts/export_astro_data.py`：从 DB 聚合导出。
- `scripts/merge_americas.py`：美洲结果合并（幂等）。
- `datacenters.db`：SQLite 主库（centers + sources 表，含 country/subnational 列）。

## 边界

- 禁止删除文件；禁止直接改 DB schema 之外的持久层；推送 GitHub 前确认身份（huangzesen / hzsbazinga@outlook.com）。
- 公开内容禁止内部路径/文件名泄漏。
