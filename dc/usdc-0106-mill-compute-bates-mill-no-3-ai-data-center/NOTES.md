# USDC-0106 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Rejected and not a live build
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status: 维持并升级证据为官方确认的 rejected / not a live build。Lewiston City Council 2025-12-16 正式会议纪要记录 Vote 323-2025，关于授权 City Administrator 与 MillCompute LLC 签署 Bates Mill 3 Tier III AI Data and Technology Center Joint Development Agreement 的议案 “Did Not Pass - Vote 0-7”。来源：https://www.lewistonmaine.gov/Archive.aspx?ADID=6685
- capacity_mw: 从 null 更新为 24，但标注为 rejected proposal / proposed Phase I capacity，不是 live operating capacity。官方纪要称 MillCompute LLC “has determined a Phase I 24MW AI Data Center is feasible”；MillCompute FAQ 同样描述 “24 MW data center and technology facility”。来源：https://www.lewistonmaine.gov/Archive.aspx?ADID=6685 ; https://www.millcompute.com/faq
- owner / sponsor: 从 null 更新为 “MillCompute LLC in partnership with Bates Mill No. 3 owner Bill Johnson / Twin Cities LLC”。官方纪要称 Bill Johnson 通过 Twin Cities LLC 拥有 Bates Mill 3 并与 MillCompute LLC 建立合作；Maine Public 的 2025-12-12 报道也称建筑所有人 Bill Johnson partnered with MillCompute LLC。来源：https://www.lewistonmaine.gov/Archive.aspx?ADID=6685 ; https://www.mainepublic.org/business-and-economy/2025-12-12/lewiston-to-decide-on-a-i-data-center-for-bates-mill-property
- site/details: 补充 proposed_floor_area_sqft = 85000。Maine Public 2025-12-12 报道称项目将使用 Bates Mill No. 3 前两层、约 85,000 平方英尺；MillCompute FAQ 也称 Mill 3 前两层约 85,000 平方英尺用于 24 MW 计算基础设施，上两层作为 office/innovation space。来源：https://www.mainepublic.org/business-and-economy/2025-12-12/lewiston-to-decide-on-a-i-data-center-for-bates-mill-property ; https://www.millcompute.com/faq
- corroboration: Maine Public 2025-12-17 报道确认 Lewiston city councilors unanimously rejected the plan，且称无 MillCompute development team 成员在会议中发言；The Maine Monitor / Bangor Daily News 2026-04-06 后续报道称方案在 2025-12 public release 后六天内崩盘，Lewiston City Administrator Bryan Kaenrath 表示未来 data-center proposals 会更谨慎，且没有说明 Bates Mill 3 方案恢复。来源：https://www.mainepublic.org/business-and-economy/2025-12-17/lewiston-city-council-shoots-down-data-center-proposal ; https://themainemonitor.org/secretive-plan-lewiston-data-center/
- conflicts: 未发现与官方 0-7 rejection 冲突的官方/地方政府后续批准、permit、construction 或 utility interconnection 证据。部分商业 tracker 仍以 proposed/announced 描述该站点，按本目录规则不覆盖官方 rejected status。
- evidence gap: 本次未找到独立的官方 permit/interconnection 记录；鉴于 JDA 未通过，缺失这类记录与 rejected/not-live 状态一致。
