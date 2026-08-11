# USDC-0204 — Fairwater 1

## 一句话
Microsoft's first facility was company-reported fully operational on 2026-06-23; official/local records and Microsoft state that a second adjacent facility remains under construction

## 位置
- City: Mount Pleasant
- County: Racine
- State: WI
- 地址/地块: 

## 维护契约（每次更新必读）

### 数据源（按优先级）
1. 官方/地方政府：county/city 规划、permit、site plan、utility service records
2. 业主/开发商公告（company announcement）
3. 区域媒体 / 行业 tracker（CBRE/JLL/C&W/Savills/Cleanview/WoodMac 等）
4. 电网侧：utility interconnection queue / load forecasts

### 更新频率
- 至少每周刷新一次；重大公告（开工/获批/并网/跳票）即时更新
- 每条新事实必须带来源 URL 与日期

### 字段（data.json 保持这些 key）
- status_as_of_cutoff / evidence_grade
- capacity_mw（如可得）、owner、location
- milestones/actions（date, government_body, action_type, result_status）
- sources（URL 列表）、contradictions（如有多源冲突）

### 验证方式
- 已证实事实与推测/projected tails 分开标注
- 多源冲突记入 NOTES.md 并保留来源
- announced ≠ construction：状态分层按 baseline 的
  announced / local process / approved-permitted / site work-construction /
  energized / partial live / full buildout

### 如何更新（给后续 agent 的接手流程）
1. 读本 SKILL.md 与 data.json、NOTES.md
2. 按数据源优先级搜索新事实，优先官方/local-government 来源
3. 更新 data.json（同一 key 覆盖并保留旧值到 history）或追加 NOTES.md 新节
4. 更新 NOTES.md（日期 + 变化 + 来源 URL）
5. git add + commit（message 含 master_id 与变更摘要）

## 基线来源
- baseline: legacy-baseline-20260716/national_master_inventory.json (SHA 2113de4b…)
- master_id: USDC-0204
- phase3 stable_id: WI-MOUNT-PLEASANT-MICROSOFT-FAIRWATER

## 相关文件

- `data.json`（结构化数据真源）· `NOTES.md`（历次更新记录）
- 顶层 `SKILL.md`（方法论路由）· `ANATOMY.md`（结构地图）
