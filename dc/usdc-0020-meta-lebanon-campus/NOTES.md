# USDC-0020 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: no status
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：`no status` -> `site work-construction`。官方州/市页面均称 Meta 于 2026-02-11 在 Lebanon 的 LEAP Innovation and Research District campus broke ground；Mortenson 于 2026-02-16 进一步发布其参与建设的 contractor update。来源：https://iedc.in.gov/events/news/details/2026/02/11/gov.-braun-breaks-ground-on-10b-meta-data-center-campus-at-leap-district ; https://lebanon.in.gov/2026/02/11/meta-makes-lebanon-data-center-announcement-official/ ; https://www.mortenson.com/news-insights/mortenson-begins-indiana-data-center-construction
- capacity/owner 更新：`capacity_mw` 从 null 更新为 `1000`，`owner` 从 null 更新为 `Meta Platforms Inc.`。Meta 官方 2026-02-11 新闻稿称 Lebanon site designed to deliver 1GW，投资超过 $10B；IEDC 同日称 Meta Platforms Inc. 将分阶段投资超过 $10B。来源：https://about.fb.com/news/2026/02/metas-new-data-center-lebanon-indiana-marks-milestone-ai-investment/ ; https://iedc.in.gov/events/news/details/2026/02/11/gov.-braun-breaks-ground-on-10b-meta-data-center-campus-at-leap-district
- scope/location 补证：IEDC 官方页面称 campus 位于 Lebanon 的 LEAP Innovation and Research District，占地 1,500 acres，规划 13 total buildings，其中 10 data center buildings；Meta Data Centers 页面称 campus roughly 4 million square feet。来源：https://iedc.in.gov/events/news/details/2026/02/11/gov.-braun-breaks-ground-on-10b-meta-data-center-campus-at-leap-district ; https://datacenters.atmeta.com/2026/02/hello-lebanon/
- local-government moratorium 核实：Boone County Commissioners 于 2026-06-15 unanimously approved 一年期 moratorium，2026-06-16 至 2027-06-15 暂停 new data center facilities in unincorporated Boone County 的 filing/processing/review/acceptance；county release 明确称 ordinance applies only to new data center facilities and does not affect existing facilities or other types of development。此项不改变 Meta campus 的 construction status。来源：https://boonecounty.in.gov/2026/06/15/19190/
- utility/electricity 补证：Boone Power 公开 FAQ 称 Meta data center large load works with Boone Power/Wabash Valley Power Alliance, infrastructure used solely by the customer is paid by that customer, and WVPA aligns large loads with dedicated/independent power sources; 该来源支持电网侧成本/保障说明，但未披露 interconnection queue number 或 contract capacity。来源：https://www.boonepower.com/news/ceo-responsible-planning-supports-reliable-power
- 多源冲突：未发现影响 status/capacity/owner 的实质冲突。注意 city page 提到 public water infrastructure investment over $75M，而 Meta Newsroom 提到 over $120M toward critical water infrastructure and other public infrastructure; 本次未将公共基础设施金额写入结构化字段。
- 无法核实/证据不足：未找到可公开访问的 Lebanon/Boone building permit packet、site-plan case number、parcel/address detail、utility interconnection queue ID、energization date 或 operational-live date。
