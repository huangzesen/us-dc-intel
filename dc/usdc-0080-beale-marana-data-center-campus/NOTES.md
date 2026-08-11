# USDC-0080 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Planned/under development on developer and utility-planning evidence; local approval path and construction were not verified
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：由 “Planned/under development ... local approval path and construction were not verified” 更新为 “approved-permitted” 层级中的本地 rezoning/specific-plan approval。Town of Marana 项目页确认 Luckett Road North/South 两个 data-center rezoning applications 于 2025-12-10 经 Planning and Zoning Commission unanimous recommendation，并于 2026-01-06 Town Council public hearings approved；未核实到 site-plan approval、building permit、construction start、energization、tenant/operator 或 full buildout。来源：https://www.maranaaz.gov/Government/Data-Centers/Luckett-Road-North-and-South-Data-Centers
- identity 修正：本目录应跟踪 Marana 的 Luckett Road North and South Data Centers / Luckett Road Data Center，而不是 Pima County Fairgrounds 附近的 Project Blue。Beale 自有 Marana 页面将该项目称为 Luckett Road Data Center；Pima County FAQ 将 Project Blue 定位为 unincorporated Pima County、Houghton Road 以西、Pima County Fairgrounds 以北的 290-acre 项目。来源：https://bealeinfra.com/location/marana/ ，https://www.pima.gov/3552/Project-Blue-FAQ
- location 补证：Town of Marana 项目页描述站点为约 600 acres、两个相邻约 300-acre parcels，位于 I-10 以西、Luckett and Hardin Roads、Pinal County line 以南；附近包括 Arizona Veterans' Memorial Cemetery、quarry、solar field 和 farmland。来源：https://www.maranaaz.gov/Government/Data-Centers/Luckett-Road-North-and-South-Data-Centers
- capacity 处理：capacity_mw 保持 null。Town source 给出 estimated electrical demand 为每个 site 550-750 MW，且两块地分别由 Tucson Electric Power 与 Trico Electric Cooperative service；这是 utility demand range，不是 verified IT critical load 或 energized capacity，因此写入 capacity_note 和 contradictions，不填 scalar capacity_mw。来源：https://www.maranaaz.gov/Government/Data-Centers/Luckett-Road-North-and-South-Data-Centers
- owner/developer 补证：owner 字段改为 Beale Infrastructure is developer；underlying parcels owned by Herbert Kai S12 LLC / Kai Trst 97 S12 LLC / Jihong S12 LLC and the Corporation of the Presiding Bishop of The Church of Jesus Christ of Latter-day Saints。来源：https://www.maranaaz.gov/Government/Data-Centers/Luckett-Road-North-and-South-Data-Centers
- referendum/procedural caveat：AZPM 2026-02-10 报道 Marana residents 提交 referendum petitions，Beale 当时表示 next phase would go into design and permitting with no word on groundbreaking；本次刷新未找到 approval overturned 的证据。Town official referendum article URL 在搜索中可见但 browser 访问未返回正文，故该项作为 caveat 而非 status downgrade。来源：https://news.azpm.org/p/azpmnews/2026/2/10/228403-marana-residents-submit-petitions-to-put-data-center-project-to-a-vote/
- developer corroboration：Beale Marana 页面称 Luckett Road Data Center 是 planned multi-building campus，并称 final building count and phasing will be in formal site plan submission；这支持“尚未核实正式 site-plan/building permit/construction”的判断。来源：https://bealeinfra.com/location/marana/
- 多源冲突：Project Blue 名称与 Marana Luckett Road 项目发生混用；已在 data.json contradictions 记录并移除 alias “Project Blue Marana”。另一个冲突是公开 MW 数字为 demand range，不等于 capacity_mw。
- verified: true（官方/地方政府页面、开发商页面和区域报道均可访问；但 site-plan/building permit、construction start、energization、tenant/operator 和 verified IT load 均未找到公开可核实证据）。
