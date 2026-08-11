# USDC-0076 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Proposed/under development in press coverage; McMinnville’s public engagement page records a data-center pause/study
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：从 “Proposed/under development in press coverage; McMinnville’s public engagement page records a data-center pause/study” 调整为 `local process / proposed`。理由：McMinnville 官方记录显示 Ordinance No. 2026-09 已在 2026-06-09 二读终读通过，对新的 data center / high-density computing 相关 land use、zoning、building、site plan、conditional use、variance 申请实施 18 个月 moratorium；未发现 Hixson 项目专属 zoning case、site plan、building permit、CO、construction 或 energization 记录。来源：https://mcminnvilletn.gov/Minutes%2006%2009%202026.pdf?t=202606261801300
- 官方补证：2026-06-03 special session packet 中的 Ordinance No. 2026-09 草案说明 moratorium 适用于 City of McMinnville 辖区内新的 Data Center / High-Density Computing facility 申请，并列出例外（既有合法运营设施、首读前已正式完整提交且 vested 的申请）。来源：https://cms2.revize.com/revize/mcminnville/Full%20Packet%206-3-26.pdf?ref=writing.strisker.com&t=202606031814180&t=202606031814180
- 官方补证：City project hub 说明 McMinnville 已暂停新的 data center 和 cryptocurrency mining development proposals 18 个月，用于研究 infrastructure、noise、economy、zoning 等影响；timeline 记录 2026-06-03 至 2026-06-09 为 policy adoption and moratorium implementation。来源：https://engage.zencity.io/mcminnville-tn/en-US/projects/high-impact-developments
- 官方补证：2026-06-09 public hearing minutes 记录 7 名访客就 Ordinance No. 2026-09 和 AI Data Centers 表达 concerns。来源：https://cms2.revize.com/revize/mcminnville/20260609%20Public%20Hearing%20for%20Ordinance%20No.%202026-09.pdf?t=202606261756040
- capacity 更新：`capacity_mw` 从 null 更新为 25。证据为 Hixson Data Center 自有网站标注 25 MW sellable IT output / Q1 2028 opening，以及 DCD 2026-05-27 报道 25 MW、96,065 sq ft、Q1 2028、financing and single-tenant search。该容量仅作为 proposed/sponsor-stated IT capacity，不代表获批或并网容量。来源：https://hixsondc.com/ ；https://www.datacenterdynamics.com/en/news/25mw-ai-data-center-to-be-built-in-mcminnville-tennessee/
- owner/sponsor 更新：`owner` 从 null 更新为 “Hixson Data Center / Hixson sponsor group”，但保留 caveat：公开政府记录中未核实 exact legal landowner / parcel owner。Hixson 官网列 Ray Hixson 为 Managing Principal、Alex Hixson 为 Director of Development，并称 site owned & controlled。来源：https://hixsondc.com/
- 最新公开记录检查：McMinnville BOMA agenda/minutes index 截至 2026-08-11、Planning Commission postings 截至 2026-08-04 未识别 Hixson-specific zoning、site-plan、conditional-use、variance、building-permit、construction、CO 或 energization 项。来源：https://www.mcminnvilletn.gov/city_government/agendas___minutes/board_of_mayor_and_aldermen_agendas_and_minutes.php ；https://www.mcminnvilletn.gov/city_government/agendas___minutes/agendas_and_minutes.php
- 多源冲突：DCD 使用 “is being built” 表述、Hixson 官网营销 Q1 2028 opening；但官方记录仅支持 citywide moratorium / public process，未支持 construction 或 permit-issued 状态。因此本次不升级到 `approved-permitted` 或 `site work-construction`。
- 无法核实：exact parcel、legal landowner、site-plan/permit number、utility interconnection/service agreement、construction start、CO/energization 均未在本次可访问官方/地方政府来源中核实。
- verified: true（对本次写入的新事实：官方 moratorium 与 public-process 事实、sponsor-stated 25 MW、无公开项目专属 approval/permit 记录的结论均已由可访问来源确认；未核实项已单独标注）。
