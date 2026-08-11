# USDC-0161 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: no status
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status: `no status` -> `local process`。本次核实到两个官方 Texas Department of Licensing and Regulation (TDLR) SAT82 记录，但未核实到官方建筑许可、施工检查、CO、utility interconnection、energization 或 live-service 证据；因此不升为 `site work-construction`。
- owner: `null` -> `Microsoft`。TDLR TABS2026008231 owner 为 Microsoft；TDLR TABS2024023976 owner 为 Microsoft Corporation。
- 官方记录 1（较新 SAT82）：TDLR TABS2026008231，注册日期 2025-12-17，项目名 Microsoft SAT82 Data Center，facility SAT82，地址 3580 FM 471 N, Castroville, TX 78009，Medina County，Current Status: Project Registered；新建 1-story、5 Colo data center，含 Tier II IDF network 与 Tier II AZNG network，195,670 sq ft，estimated cost $400,000,000，计划 start 2026-08-13、completion 2028-07-24。来源：https://www.tdlr.texas.gov/TABS/Search/Project/TABS2026008231
- 官方记录 2（较早 SAT82）：TDLR TABS2024023976，注册日期 2024-07-25，项目名/设施名 SAT82 Data Center，地址 18844 FM 1957 Castroville, Castroville, TX 78009，Medina County，Current Status: Review Complete；新建 1-story、5-colo data center，244,676 gross sq ft，estimated cost $482,600,000，计划 start 2026-04-11、completion 2028-02-08，design firm WSP USA, Inc.。来源：https://www.tdlr.texas.gov/TABS/Search/Project/TABS2024023976
- 公司侧确认：Microsoft Greater San Antonio local page 当前说明 Microsoft operates datacenters in Bexar and Medina counties，但未按 SAT82 单体披露容量、施工状态或投运日期。来源：https://local.microsoft.com/communities/americas/greater-san-antonio/
- 行业媒体/tracker 交叉检查：DCD 2026-01-12 报道较新 3580/FM 471 N SAT82 filing，并指出 Microsoft 2024 年曾提交另一个 SAT82 at 18844 FM 1957，尚不清楚新申请是追加项目还是替代旧项目。来源：https://www.datacenterdynamics.com/en/news/microsoft-plans-400m-data-center-in-castroville-texas/
- 行业媒体/tracker 交叉检查：Data Center Map 记录 2024-07 SAT82 at 18844 FM1957 announced，并记录 2025-12 Microsoft filed again for SAT82 at a different site, uncertain if expansion or discarded first filing。来源：https://www.datacentermap.com/usa/texas/san-antonio/microsoft-san-antonio-sat82/
- 冲突/不确定：同一 SAT82 名称对应两个官方 TDLR 地址、面积、金额、日期；本次无法判定是同一项目 refiling/relocation、旧项目取消、还是两个 SAT82-labeled buildings。data.json 以较新 TDLR TABS2026008231 地址作为主 location，并把 18844 FM 1957 保留为 alternate/prior filing 与 contradiction。
- 证据不足项：capacity_mw 未见官方披露；第三方 `under construction`/`construction` 标签未被官方 building permit、inspection、CO、utility service 或 energization 记录确认。
