# US Data Center Intelligence — 顶层路由 SKILL（渐进式披露）

维护美国在建/规划数据中心的可自更新的情报库。每中心一个目录，每目录一份看护契约；本文件只做路由，细节在各中心 `SKILL.md` 与 `scripts/`。

## 查什么 / 去哪里查

| 想查 | 入口 |
|---|---|
| 某中心的最新状态 | `dc/<slug>/SKILL.md`（先读）+ `data.json`（结构化基线）+ `NOTES.md`（历次更新） |
| 全国汇总 / 渲染报告 | `legacy-baseline-20260716/us_data_center_construction_panorama.html`（7/16 冻结基线）；后续汇总由 scripts 生成 |
| 找「不在 208 里的数据中心」 | 见下方「补漏发现」 |
| 某州/区域概览 | `legacy-baseline-20260716/national_master_inventory.md` + `county_decision_register.json` |

## 怎么更新（给任何接手的 agent）

1. `git -C /Users/huangzesen/work/projects/us-dc-intel pull`（或 clone）
2. 读目标中心 `dc/<slug>/SKILL.md` 的「维护契约」节（数据源优先级、字段、验证方式）
3. 按官方/地方政府来源优先搜索新事实（permit、site plan、utility record、county vote、announcement）
4. 更新 `data.json`（保留旧值到 history）或追加 `NOTES.md` 新节（日期 + 变化 + 来源 URL）
5. `git add` + commit（message 含 master_id 与变更摘要）
6. 定期（每周）派发刷新：见 `scripts/` 与下方「派活模式」

## 派活模式（大规模刷新 / 补证据）

- **208 中心分批刷新**：每 daemon 1-2 个中心，任务书必须含：只读目标清单（`dc/<slug>` 路径）、NO-DELETION 契约、产出 = 更新后的 data.json/NOTES.md + 来源 URL、禁止 git 写入（由父 agent 统一 review 后提交）。
- **补漏发现（Jason 3107 指示）**：派 codex daemon 搜「不在 208 baseline 里的在建/规划数据中心」——超大规模新公告（xAI/Meta/Google/OpenAI Stargate 后续）、二三线市场、CBRE/JLL/C&W/Cleanview 覆盖外项目、电网 queue 新入列；产出 candidate list（名称/位置/来源 URL/口径），**人审后**再并入 repo（新增目录）。
- **证据缺口（23 seed-only records）**：这些只有 seed 无 phase3 详情，优先补证。

## 数据基线

- 冻结基线：`legacy-baseline-20260716/`（2026-07-16；`national_master_inventory.json` SHA `2113de4b…`，208 masters = 185 详细 + 23 seed-only）
- 来源所有权：baseline 原产物属 衡枢（codex）/算枢（datacenter-tracker）；本 repo 是 Jason 授权的独立维护形态
- 周更 runbook 参考（W32 实验 BLOCKED_INCOMPLETE，勿复用其结论）：算枢 `datacenter-tracker/workspace/weekly_refresh_2026W32_20260804T0630PDT/control/`

## 生成 / 脚本

- `scripts/generate_skeleton.py`：从冻结 baseline 生成/刷新 `dc/<slug>/` 骨架（幂等，不覆盖 NOTES.md）
- `scripts/` 后续可加：`refresh_one.py`（单中心刷新模板）、`discover_new.py`（补漏候选）、`render_summary.py`（全国汇总）

## 边界

- 不删 baseline 原始 bytes；不改算枢 workspace；不把 announced 当 construction；evidence vs projected 分开。
- 对外发布（huangzesen.github.io 等）需 Jason 另行授权。
