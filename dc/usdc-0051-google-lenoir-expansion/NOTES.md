# USDC-0051 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Caldwell County and Lenoir jointly approved economic-development measures aimed at streamlining a possible expansion in October 2024
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新为 `announced / local process`：2024-10-22 Caldwell County Board of Commissioners 与 City of Lenoir City Council 批准潜在 Google 扩建相关的经济发展协议/激励，官方市府稿说明扩建拟位于现有 708 Lynhaven Drive 园区旁约 60 acres，市府另批准关闭 815-1021 Virginia Street 之间一段道路，并称 Google 自愿出资 $6.8 million 支持园区供水能力。来源：https://www.cityoflenoir.com/CivicAlerts.aspx?AID=498
- 会议纪要补证：Caldwell County 2024-10-22 special meeting minutes 记录 Project Cardinal 激励协议 public hearing，county motion carried unanimously，并在会后明确 Project Cardinal 是 Google 在 Lenoir 的扩建；该纪要未提供建筑许可或施工证据。来源：https://www.caldwellcountync.org/DocumentCenter/View/2106/October-22-2024-Special-Meeting-Minutes-Final
- 2026-03-13 投资公告由“business press reported”改为官方可访问来源：City of Lenoir 2026-03-17 发布 Google 公告，称 Google 将在未来两年内于 North Carolina 新增 $1 billion 投资，以增长 Lenoir 数据中心基础设施，并同步公布 $2 million Energy Impact Fund 等社区/能源项目。该公告仍不是 permit、CO、并网或施工里程碑。来源：https://www.cityoflenoir.com/m/newsflash/Home/Detail/594
- Google 官方地点页补证现有 Lenoir 数据中心：Google 称其自 2007 年在 Lenoir 建设/运营，2008 年开设首个 Lenoir data center，累计在 North Carolina 投资超过 $4 billion；页面未披露本次扩建 MW 容量或施工状态。来源：https://datacenters.google/locations/north-carolina/
- NCDEQ 补证现有 708 Lynhaven Drive 设施：2025-07-09 NCDEQ 对 Tapaha Dynamics, LLC 的 Title V Operation Permit 09733T11 / Application ID 1400204.25A 开启 EPA comment period；draft permit review 称该 reopen-for-cause 是补加 CO PSD avoidance limit，“does not represent a physical change or change in the method of operation”。因此该记录不能作为扩建施工证据。来源：https://www.deq.nc.gov/news/events/epa-comment-period-tapaha-dynamics-llc-1 和 https://www.deq.nc.gov/draft-permit-review-tapaha-dynamics-llc/open
- owner 字段从 null 更新为 “Google; NCDEQ air-permit records identify Tapaha Dynamics, LLC at 708 Lynhaven Drive, and industry reporting describes Tapaha Dynamics, LLC as Google's affiliate for the local incentive filing.” 行业来源用于 affiliate/parcel/job 细节交叉参考，未用于提升状态。来源：https://www.datacenterdynamics.com/en/news/google-looks-to-expand-data-center-campus-outside-charlotte-north-carolina/
- capacity_mw 维持 null：未找到官方或地方政府记录披露本次扩建的 MW/IT load。
- 未发现可核实的 building permit、site plan approval、certificate of occupancy、utility interconnection、energization 或 commissioning 证据；不提升到 `approved-permitted` 或 `site work-construction`。
- 多源冲突：无硬冲突。注意口径差异：2024 incentive 语境常见 $600 million/Project Cardinal，2026 官方公告为 statewide/NC $1 billion within two years to grow Lenoir data-center infrastructure；两者可能是不同口径/阶段，当前不合并为单一容量或单一 CAPEX 字段。
