# USDC-0139 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: City of Hillsboro public notice confirms an administrative-review application for a phased CoreSite data-center campus
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 保持 `local process`：官方 City of Hillsboro 记录仍只支持 DR-012-26 处于 development review / public notice 阶段；未找到 final land-use approval、building permit issuance、construction start、inspection、CO、utility/interconnection、energization 或 service-date 证据。来源：https://www.hillsboro-oregon.gov/Home/Components/News/News/17484/4315
- 官方补证：City Manager's Report（2026-07-07）列出 “DR-012-26 Coresite Data Center”为近期发布的 data center development-review public notice。来源：https://hillsboro-oregon.civicweb.net/document/261246/City%20Manager_s%20Report_070726.pdf?handle=651A5C5FCE6A4E8CB93031766D8978E4
- 官方补证：City Council 于 2026-07-27 enacted 120-day temporary land-use moratorium for new/expanded primary-use data center and BESS applications；city notice 同时说明 moratorium 前已提交申请的项目可继续推进。因此该事实不等于 DR-012-26 获批，也不等于暂停/终止。来源：https://www.hillsboro-oregon.gov/Home/Components/News/News/17551/4300
- 官方补证：City 于 2026-08-03 发布 moratorium 后续工作表，称 120-day moratorium 预计至 2026-11-24，期间将推进 code amendments、utility-service pre-submittal requirement、environmental/economic analysis 与 public meetings。来源：https://www.hillsboro-oregon.gov/Home/Components/News/News/17569/
- 地址/规模补证：Hillsboro Herald（2026-07-19）报道该申请位于 5420 NE Sewell Avenue，拟建 phased 547,239-square-foot high-density computing campus，并称 property 于 2025-09 由 Coresite Real Estate Hillsboro, LLC 购入。该来源作为本地报道/申请细节线索，不作为批准或施工证据。来源：https://hillsboroherald.com/coresite-proposes-massive-multi-story-hillsboro-data-campus-opposite-county-homes-and-over-wetlands-a-showdown-is-brewing/
- 业主/实体补证：American Tower FY2025 SEC Exhibit 21 lists CoreSite Real Estate Hillsboro LLC as a Delaware subsidiary；结合本地报道，将 `owner` 从 null 更新为 `CoreSite Real Estate Hillsboro LLC`，并在 data.json 保留 caveat，待 county deed 或 city application packet 直接验证。来源：https://www.sec.gov/Archives/edgar/data/1053507/000105350726000035/exhibit21fy2025.htm
- capacity_mw 仍为 null：未找到项目级 contracted load、available electrical service capacity、interconnection queue、energization 或 MW capacity 公开证据；moratorium 中的 20 MW threshold 是 citywide primary-use definition，不可当作本项目容量。
- 多源冲突：无直接事实冲突。Herald 报道给出 combined square footage 547,239 sf，与 baseline 中 Phase 1 234,531 sf + Phase 2 312,708 sf 可相加一致；Herald 对 code/environmental issues 的评价未写入结构化状态。
- verified: true（限于本次写入事实均有可访问来源；地址/owner 作为 lower-grade evidence 已标注 caveat）。
