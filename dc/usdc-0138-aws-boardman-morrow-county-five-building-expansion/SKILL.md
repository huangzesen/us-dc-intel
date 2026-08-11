# USDC-0138 — AWS Boardman/Morrow County five-building expansion

## 一句话
Morrow County officially approved LUD-N-68-24 on 2024-09-24 by 4 yes / 3 no, subject to final zoning/address, road-use, airport, water, wastewater, stormwater, and occupancy conditions

## 位置
- City: Boardman area / outside Boardman UGB
- County: Morrow County
- State: OR
- 地址/地块: Parcel 2 of Partition Plat 2022-16; Tax Lot 138 of Assessor's Map 4N24E; southwest of Tower Road/I-84 interchange, adjacent to Boardman Airport

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
- master_id: USDC-0138
- phase3 stable_id: US-OR-AWS-BOARDMAN-2024
