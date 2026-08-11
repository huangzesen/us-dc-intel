# USDC-0081 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Developer says a specific plan was approved and construction claimed, but the underlying Pima action, permit, and TEP record were not independently verified
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：从“developer claim / underlying Pima action, permit, and TEP record not independently verified”更新为 `site work-construction`。Pima County 官方材料已核实 2025-06-17 Board of Supervisors 批准 specific-plan zoning change 与 land acquisition agreement；2025-12-24 土地出售已 closing；2026-04-23 county memo 附件列出已批准/已签发的 specific plan、site construction、capacity letter、septic transfer、other structures 等记录。来源：
  - https://content.civicplus.com/api/assets/32428b1b-4a81-444a-92a4-72b1fa039655
  - https://www.pima.gov/3552/Project-Blue-FAQ
- location/owner 更新：Pima County closing memo 的 settlement statement 标明 buyer 为 Bobcat B1 LLC，property 为 11295 S Harrison Road, Tucson, AZ；项目地为 Pima County Fairgrounds 以北、SELC 内约 290-acre parcel。来源：
  - https://content.civicplus.com/api/assets/93418380-b75f-4118-a254-04d7511f4a74
  - https://www.pima.gov/3552/Project-Blue-FAQ
- capacity_mw 更新：记录为 286 MW，限定为 TEP/ACC electric-service agreement capacity，不等同于 IT critical capacity 或 delivered load。Pima County 2025-08-25 memo 记录 TEP 向 ACC filing up to 286 MW；ACC 2025-12-09 官方新闻稿记录 2025-12-03 以 4-1 vote 批准 TEP special agreement。来源：
  - https://content.civicplus.com/api/assets/6b2dfc39-d95c-4377-a177-b52d05985e5d
  - https://www.azcc.gov/news/home/2025/12/09/vice-chair-myers-confirms-tep-customers-protected-from-data-center-cost-shift
- construction/site work 补证：Pima County 2026-04-23 memo permit table 列出 P25SC00055 与 P25SC00120 为 Issued Site Construction；Pima County Department of Environmental Quality 2026-05-12 对 AMES Construction 的 fugitive-dust notice of violation 说明其正在 Project Blue site 做 site preparation work。来源：
  - https://content.civicplus.com/api/assets/32428b1b-4a81-444a-92a4-72b1fa039655
  - https://www.pima.gov/?contentId=95d783ec-a245-40e3-874d-48e4772b1433
- 多源冲突/需后续核实：水源与用水路径仍需保留为未归一化项。2025-06-10 Pima County 材料描述 reclaimed-water phased approach；2026 年地方公共媒体报道 Bobcat Tucson Water LLC 申请/获批两口 commercial wells，年用水约 31 million gallons。未在本轮直接取得 ADWR 原始 well permit 文件，因此未写入核心字段。来源：
  - https://content.civicplus.com/api/assets/c389f127-6e01-48fc-b258-68508aa1841a
  - https://www.azpm.org/s/103423-arizona-water-officials-approve-wells-tied-to-project-blue-data-center/
- 证据不足项：未找到 certificate of occupancy、utility energization、first IT load、operational/partial live/full buildout 记录；Pima County FAQ 称 first building could be operational as soon as 2027，按 projected tail 处理，不升级为 energized 或 live。
- verified: true（针对 approval / land closing / site-construction permit / ACC electric-service approval / site-prep enforcement 这些本轮更新事实）；verified: false（针对 ADWR well permit 原始文件、CO、energization、live IT load）。
