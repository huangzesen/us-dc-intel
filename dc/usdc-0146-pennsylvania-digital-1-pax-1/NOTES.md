# USDC-0146 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: no status
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status: 从 `no status` 更新为 `site work-construction (enabling/blasting underway; phased land-development review still active)`。Middlesex Township 首页在 2026-06-03 更新中公告 “Data Center Site” blasting 将恢复并通常每日进行；同页还链接 PAX-1 long-term construction schedule。来源：https://middlesextwp.com/
- location: 补充地址 `256 Country Club Road, Carlisle, PA`，并记录项目沿 Country Club Road、约 693-700 acres。Middlesex Township summer 2026 newsletter 将 PAX-1 描述为 Country Club Road 上约 693 acres、五个地块（三个 data center campuses、PPL substation/switchyard、construction staging area），并在 FAQ 中列出地址。来源：https://middlesextwp.com/wp-content/uploads/summer2026.pdf
- capacity/owner: 补充 `capacity_mw=1350`；owner/developer 记录为 Pennsylvania Data Center Partners LLC / PowerHouse Data Centers JV，local service agreement counterparty 为 Carlisle Development Partners LLC。PowerHouse 2025-07-15 公告称 Pennsylvania Data Center Partners 与 PowerHouse 成立 JV，PAX 为 1.35 GW、可扩展到 1.8 GW；Middlesex Township Municipal Authority 2026 newsletter 称 2026-01 与 Carlisle Development Partners LLC 签署 PAX-1 水/污水服务协议。来源：https://www.powerhousedata.com/news/pennsylvania-data-center-partners-and-powerhouse-data-centers-launch-joint-venture-to-build-next-gen-1-35-gw-hyperscale-data-center-campus-in-carlisle-pennsylvania ；https://middlesextwp.com/wp-content/uploads/summer2026.pdf
- scope/schedule: 记录三 campus、16 buildings over 4.5 million sq ft、1.35 GW utility capacity，developer site 当前标为 `STATUS: UNDER CONSTRUCTION`，delivery Q4 2027，power delivery milestones Q4 2027 450 MW、Q2 2028 900 MW、Q2 2029 1350 MW。来源：https://www.padatacenters.com/campus
- local process: 2026-07-27 Planning Commission agenda 将 PAX-1 Phase 3 preliminary land development plan 与 Phase 1-B final land development plan 列为 possible action，BOS action deadline 为 2026-08-05；Middlesex Township 2026-08-07 公告 Board of Supervisors special meeting on 2026-08-19 6pm。来源：https://middlesextwp.com/wp-content/uploads/PA-07-27-2026-PC-AGENDA-ONLY.pdf ；https://middlesextwp.com/board-of-supervisors-special-meeting-wednesday-august-19-2026-6pm-at-middlesex-elementary-school/
- technical evidence: 2026-04-13 Kimley-Horn noise memo（township-hosted）描述 PAX-1 site 位于 Country Club Road/I-81 以北、Conodoguinet Creek 以南和以东、Bernheisel Bridge Road 以西；项目基于 2026-03-27 LIVIC Civil site plans，包含 16 data center buildings。来源：https://middlesextwp.com/wp-content/uploads/PAX1_Noise-Memo_04132026.pdf
- conflict/limits: 建筑数存在公开表述差异：PowerHouse 2025 公告称三 campuses、each six buildings（18 total implied）；2026 township/developer materials use 16 buildings. 当前采用 16 buildings，并在 `contradictions` 中保留差异。status 也分层处理：developer says under construction、township confirms blasting/site work，但 Phase 1-B/Phase 3 land-development approvals remain in public process, so not marked energized/live/full buildout。
- verified: true（公开 URL 均可访问；PA OTO fast-track 页面为 JS app，搜索结果可见但未作为主证据写入 data.json）。
