# USDC-0135 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Major phased expansion announced around an existing operational campus; active expansion permit/building status was not located
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- 结论：status 保持在 `announced / existing operational campus`，不提升为 `approved-permitted` 或 `site work-construction`。Google 官方在 2025-08-13 宣布未来两年向 Oklahoma cloud/AI infrastructure 追加 90 亿美元，明确包括 Stillwater 新园区与 Pryor 现有设施扩建，但未公开 Pryor 扩建 MW、地块、permit、开工或投产时间。来源：https://blog.google/company-news/inside-google/company-announcements/google-american-innovation-oklahoma/
- Google 官方 Oklahoma data-center 页面已更新为：自 2007 Mayes County 数据中心建设以来在 Oklahoma 投资超过 150 亿美元，并列出 2025 年 Oklahoma cloud/AI infrastructure 90 亿美元投资里程碑；该页仍未给出 Pryor 扩建容量或施工状态。来源：https://datacenters.google/locations/oklahoma/
- 政府侧补证：Oklahoma Department of Labor 2026-07-01 Elevator Master List 在 Mayes County/Pryor 下列出多处 Google 建筑与设备记录，包括 Google Building 5B/5C/6A/7A at 3130 Main Street/MAIP、Google Hub 2 at 3500 Main Street、Google Mega Cub at 4581 Webb Street，多项记录有 2025 inspection/test 日期。该记录支持“现有多建筑运营园区”，但不是扩建许可或开工证据。来源：https://oklahoma.gov/content/dam/ok/en/labor/documents/compliance-lists/elevator/2026/july-2026/070129-ElevatorMasterList.pdf
- 本次 local-gov-first 检索：Pryor Creek Agenda Center 公开索引可访问；本次未在页面索引中定位到 Google/data-center expansion 相关议题，因此 `government_body`/permit/case number 仍为空。来源：https://pryorcreek.org/agendacenter
- 区域媒体补充：The Frontier 2026-02-23 报道称 Pryor Google data center 在 2024-07-01 至 2025-06-30 用水超过 11 亿加仑，并称 Google 由 state-owned MidAmerica Industrial Park 取水；这属于水务/运营背景，不证明扩建审批。来源：https://www.readfrontier.org/stories/as-data-centers-boom-in-oklahoma-so-does-water-demand/
- 数据变更：`status_as_of_cutoff` 改写为分层状态说明；新增 `evidence_grade: B` 与 `status_history`；`owner` 从 null 改为 Google；`location.site_context` 增加 MAIP/Pryor 多建筑政府记录背景；`actions` 增加 Google 官方公告与 Oklahoma Department of Labor 政府记录；`sources.refresh_2026_08_11` 增加本次核验 URL。
- 冲突：未发现直接多源冲突。第三方 tracker 提到 180 MW/under construction，但本次未找到官方或地方政府证据支撑，未写入 `capacity_mw` 或提升状态。
- 证据不足项：Pryor 扩建的容量、具体 parcel/address、local permit/site-plan approval、construction start、energization/commissioning date 均未核实。
