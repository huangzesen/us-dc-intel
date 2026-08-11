# USDC-0168 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Local tax-abatement agreement and two TDLR construction registrations are documented; municipal building permits and final occupancy were not found
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：从“tax-abatement + two TDLR construction registrations; no municipal permit/occupancy found”刷新为“TDLR 记录显示 4200 County Road 132 的 Building 1/2 core/shell、initial improvements、fit-out、fit-up 多项登记，当前 TDLR status 均为 Project Registered；仍未核实到 Hutto 市政 building permit 编号、CO、并网或 live/operational 官方证据”。来源：
  - https://www.tdlr.texas.gov/TABS/Search/Project/TABS2024003524
  - https://www.tdlr.texas.gov/TABS/Search/Project/TABS2024010542
  - https://www.tdlr.texas.gov/TABS/Search/Project/TABS2024015381
  - https://www.tdlr.texas.gov/TABS/Search/Project/TABS2024016331
  - https://www.tdlr.texas.gov/TABS/Search/Project/TABS2025026905
  - https://www.tdlr.texas.gov/TABS/Search/Project/TABS2026001377
- 新增 Building 1 官方登记：2024-01-31 TDLR TABS2024010542（Skybox-Hutto 1 Initial Improvements），235,730 sf，$149,000,000，start 2024-01-01，completion 2026-06-30；2024-04-16 TDLR TABS2024016331（SKYBOX-HUTTO 1 Fit Out），235,730 sf，$163,000,000，start 2024-06-01，completion 2024-12-01。来源：
  - https://www.tdlr.texas.gov/TABS/Search/Project/TABS2024010542
  - https://www.tdlr.texas.gov/TABS/Search/Project/TABS2024016331
- 新增 Building 2 官方登记：2025-08-28 TDLR TABS2025026905（Skybox-Hutto 2 Fit Out），234,820 sf，$125,000,000，start 2025-10-01，completion 2026-06-01；2025-09-19 TDLR TABS2026001377（Skybox-Hutto 2 Fit Up），234,820 sf，$470,000,000，start 2025-10-15，completion 2026-10-15。来源：
  - https://www.tdlr.texas.gov/TABS/Search/Project/TABS2025026905
  - https://www.tdlr.texas.gov/TABS/Search/Project/TABS2026001377
- owner/location 补强：TDLR owner 为 Hutto Data Center Campus, LLC；多项 TDLR 登记位置为 4200 County Road 132, Hutto, TX 78634。Skybox 当前 Austin location 页将 PowerCampus Austin 标为 Hutto, TX。来源：
  - https://www.tdlr.texas.gov/TABS/Search/Project/TABS2024003524
  - https://www.tdlr.texas.gov/TABS/Search/Project/TABS2025026905
  - https://www.skyboxdatacenters.com/locations/austin
- capacity 更新：data.json 采用 Skybox 当前 Austin location 页的 “Up to 400 MW Critical Load”（PowerCampus Austin, Hutto, TX, 1,280,000 SF）。同一业主资料/宣传 PDF 仍列 600 MW 与 3,880,000 SF/total-load design，因此把 600 MW 保留为 capacity_notes/contradictions，不作为 capacity_mw 主值。来源：
  - https://www.skyboxdatacenters.com/locations/austin
  - https://www.skyboxdatacenters.com/images/PowerCampus-Austin-Brochure-Final.pdf
  - https://www.skyboxdatacenters.com/images/PC-Austin-Brochure-Final-Formatting.pdf
- Hutto 官方记录补充：检索到 Hutto 2026 archive PDF（indexed snippet 显示 February 5, 2026 effective date，并引用 Hutto Data Center Campus LLC as Assignor 的 assignment/assumption）；本轮可访问 PDF，但文本抽取为空，未能核实 assignee、vote tally 或完整条款。来源：
  - https://www.huttotx.gov/Archive/ViewFile/Item/1864
- 许可检索 caveat：Hutto 官方 building permit 页面显示市政 permit 通过 GovWell 处理，并提示 CO/change-of-use 等需要 City of Hutto 和 Williamson County ESD #3 inspection；公开检索未发现 Skybox/Hutto Data Center Campus 的市政 permit 编号或 CO。来源：
  - https://www.huttotx.gov/163/Building-Permit-Applications
  - https://www.huttotx.gov/511/Permits
- 多源冲突：第三方 tracker 有 “operational/under construction/approved permit” 说法，但本轮没有找到可公开核实的市政 permit、CO 或 energized/live 官方来源；未据此升级 status。示例来源：
  - https://www.datacenter.fyi/facility/skybox-powercampus-austin-tx-2cc13724
  - https://www.interconnection.fyi/data-center/project/skybox-5df0e31e
