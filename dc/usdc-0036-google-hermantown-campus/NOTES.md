# USDC-0036 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Google is publicly identified as the proposed developer/operator
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：由“Google publicly identified / AUAR scoping remained open”更新为 `local process`。City of Hermantown 项目页（Page Updated: 2026-08-05）称 Final Updated Hermantown Industrial AUAR 已于 2026-08-04 提交给 Environmental Quality Board，计划 2026-08-11 登载于 EQB Monitor；2026-07-27 市议会 work-session 材料称 Final AUAR 的 City Council deliberation/adoption 预计在 2026 fall。来源：https://hermantownmn.com/project/ 与 https://hermantownmn.com/wp-content/uploads/2026/07/7.27.2026-Presentation.pdf
- owner/proposer 更新：Final Updated AUAR 将 proposer 记为 Harmony Group LLC, a subsidiary of Google LLC；AUAR 还称已识别的 end user intends to own and operate a data center campus。`owner` 更新为 “Harmony Group LLC (subsidiary of Google LLC; proposed owner/operator)”。来源：https://hermantownmn.com/wp-content/uploads/2026/08/2026-08-04-Hermantown-Industrial-Final-AUAR-1.pdf
- project scope 补证：Final Updated AUAR 评估 26 parcels / 278 acres，maximum-build scenario 为 up to four one-story data-center buildings、one warehouse、two office buildings，总计 1.8 million square feet of data-center / warehouse / storage / office development。来源：https://hermantownmn.com/wp-content/uploads/2026/08/2026-08-04-Hermantown-Industrial-Final-AUAR-1.pdf
- permitting/status 补证：Final Updated AUAR 明确 data center use 在 Business and Light Manufacturing District 需要 Special Use Permit；preliminary construction（tree clearing）不早于 2027，且取决于 permitting approvals；public water/sewer extensions 预计最早 2027 spring 开始并约需两年。未发现最终 SUP、CIDP/site plan、building permit、construction start、inspection、CO、interconnection approval、energization、commissioning 或 service record。来源：https://hermantownmn.com/wp-content/uploads/2026/08/2026-08-04-Hermantown-Industrial-Final-AUAR-1.pdf
- Draft AUAR comment-period 补证：City 2026-06-12 press release 称第二轮 public comment period 于 2026-06-12 开始，关注 Draft AUAR 与 Mitigation Plan，comment period 截止 2026-07-16。来源：https://hermantownmn.com/community/community-highlights/second-comment-period-opens-for-google-data-center/
- power/capacity 核实：Minnesota Power 2026-03-16 官方演示称 MP has an agreement with Google to provide electric service for the proposed Hermantown data center，ESA 将提交 MPUC 审批，并称该安排 enables 700 megawatts of new clean energy resources；Google 2026-05-04 演示称 backup generation “Light” at 25-49 MWs。未将这些数值写入 `capacity_mw`，因为它们不是已核实的数据中心 IT load/campus demand capacity。来源：https://hermantownmn.com/wp-content/uploads/2026/03/Hermantown-City-Council-MP-Presentation-2026-03-16.pdf 与 https://hermantownmn.com/wp-content/uploads/2026/05/Hermantown-TAA-DA-Meeting-May-4-2026.pdf
- conflicts：未发现多源事实冲突。需要注意：May 2026 Google presentation 的 Q3-Q4 2027 “Construction Permitting” 是 anticipated if approved；Final AUAR 的 “preliminary construction as early 2027” 也是取决于 permits，均不可升级为 construction。
- verified: true（官方市政页面/官方 AUAR/官方会议材料均可访问；容量字段仍为 null 是因为公开来源证据不足，而非未完成核实）。
