# USDC-0137 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Under construction based on the state groundbreaking release; first service date, building permits, and occupancy were not located
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 从通用 "Under construction" 细化为 `site work-construction`：Meta、Oklahoma Department of Commerce、PartnerTulsa 均在 2026-04-21 记录 Tulsa Data Center / Project Anthem 已 groundbreaking；Oklahoma Commerce Q2 2026 New and Expanding Companies report 将 Meta Platforms, Inc. / Project Anthem 的 development stage 列为 `Under Construction`。来源：
  - https://datacenters.atmeta.com/2026/04/hello-tulsa/
  - https://www.okcommerce.gov/meta-breaks-ground-on-data-center-in-tulsa/
  - https://partnertulsa.org/meta-breaks-ground-on-new-1-billion-data-center-in-tulsa/
  - https://www.okcommerce.gov/wp-content/uploads/New-and-Expanding-Companies-Quarter-2-2026.pdf
- owner 从 `null` 更新为 `Meta Platforms, Inc.`。公司页称 Tulsa 将成为 Meta 的 next AI data center；Oklahoma Commerce Q2 2026 report 的 employer 字段列 Meta Platforms, Inc.。来源：
  - https://datacenters.atmeta.com/2026/04/hello-tulsa/
  - https://www.okcommerce.gov/wp-content/uploads/New-and-Expanding-Companies-Quarter-2-2026.pdf
- location 补充为 Fair Oaks Innovation Park / east Tulsa，并记录 City Council 基础设施议程中 ATMOSS, LLC 位于 21304 E. 11th St. S. 的 Project Anthem 相关 dedication/easement items。该地址作为基础设施事项位置使用，不等同于完整 campus 地址。来源：
  - https://www.okcommerce.gov/meta-breaks-ground-on-data-center-in-tulsa/
  - https://tulsa-ok.granicus.com/AgendaViewer.php?clip_id=7411&view_id=4
- 补入本地政府过程：Tulsa City Council item 24-357 记录 Project Anthem Economic Development Project Plan and Supporting Incentive District 于 2024-05-01 进入 Council action；City Council item 26-196 记录 2026-03-25 data center moratorium 文件，例外条款不适用于 Project Anthem Phase 1，并为一个可能的 Phase 2 留出依 zoning 而定的例外。来源：
  - https://www.cityoftulsa.org/apps/CouncilDocuments?item=46238
  - https://www.cityoftulsa.org/apps/CouncilDocuments?item=49527
- 单独记录 Phase 2 / adjacent expansion local-process fact：TMAPC agenda 将 Z-7851 / CPA-128 描述为 East 11th Street South 与 East 21st Street South 之间、South 193rd East Avenue 以东多宗地的 AG-to-IL rezoning / Neighborhood-to-Employment land-use change；2026-04-01 TMAPC minutes 记录 Z-7851 与 CPA-128 均由 applicant 于 2026-03-30 withdrawn。该事实不推翻 Phase 1 已开工状态。来源：
  - https://tulsaplanning.org/agendas/april-1-2026-tmapc-agenda/
  - https://tulsaplanning.org/tmapc/agendas/exhibits/2026-04-01-TMAPC-Minutes.pdf
- capacity_mw 保持 `null`。Meta / Oklahoma Commerce / PartnerTulsa 的 "1,500+ MW" 是 Oklahoma clean-energy projects under contract / grid additions，用于匹配用电，不是 Tulsa facility load capacity；未找到公开 facility-load MW、interconnection queue MW、energization、first service 或 occupancy 证据。来源：
  - https://datacenters.atmeta.com/2026/04/hello-tulsa/
  - https://www.okcommerce.gov/meta-breaks-ground-on-data-center-in-tulsa/
- 未发现多源冲突。需后续继续核实：Tulsa building/grading permits、PSO interconnection/load-serving records、first service / energization / occupancy、以及 Phase 2 是否以新案号重新提交。
