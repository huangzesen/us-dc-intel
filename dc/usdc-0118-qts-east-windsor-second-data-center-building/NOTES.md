# USDC-0118 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: no status
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status: 从 no status 更新为 approved-permitted。官方 East Windsor Planning Board 页面列出 EWT PB25-006，申请人为 QTS Investment Properties Princeton LLC，地址 159 Princeton-Hightstown Rd，Block 63, Lots 6, 6.01, 8, 9, 10.03, 10.04, 51，事项为 Preliminary and Final Site Plan with Bulk Variances（页面显示 FOR CARRYING PURPOSES ONLY）：https://www.east-windsor.nj.us/planning-board
- 业主/运营方：更新为 QTS Investment Properties Princeton LLC / QTS Data Centers。East Windsor Township 2024-04-09 Council minutes 对 159 Princeton-Hightstown Road 的 QTS Investment Properties Princeton LLC developer agreement 作出 R2024-058 批准，并说明 Planning Board Resolution 2023-17 在 2023-10-02 已就既有数据中心升级和潜在未来扩建授予 preliminary and final site plan approval with bulk variance and design waivers：https://www.east-windsor.nj.us/media/Minutes/2024/4.09.24%20Minutes.pdf
- 位置补全：159 Princeton-Hightstown Road, East Windsor, NJ 08520。QTS 官网同址列出 East Windsor 1，并披露 52-acre campus、on-site substation、70 MW+ critical power capacity，但 FAQ 同时说明不披露具体项目 power capacity：https://q.com/data-centers/east-windsor/
- 项目规模补证：QTS 官网披露本次 expansion project 为 additional $600 million investment，约 400 个 construction jobs 和 5-8 个 permanent positions；第三方/本地报道披露第二栋约 272,000 sq ft。DCD 于 2026-04-29 报道该第二数据中心位于 159 Princeton-Hightstown Road，4/27 听证未完成、投票推迟到 2026-05-04：https://www.datacenterdynamics.com/en/news/decision-on-qts-planned-expansion-of-data-center-in-east-windsor-new-jersey-postponed/
- 批准状态补证：Baxtel 当前页面称 East Windsor Planning Board 在 2026-05 会议批准该 second facility application，并标记 DC2 under construction；TAPinto 搜索结果标题也称 Planning Board green light/OKs second facility。未找到官方 2026-05 Planning Board minutes 或 building permit，因此 data.json 采用 approved-permitted，不采用 site work-construction：https://baxtel.com/data-center/qts-east-windsor-1-dc2 ; https://www.tapinto.net/towns/east-windsor-hightstown/sections/government/articles/new-qts-data-center-receives-green-light-from-east-windsor-planning-board
- 后续限制：East Windsor adopted ordinances 页面列出 Ordinance 2026-06，说明 through December 31, 2027 对 further data centers 实施 moratorium；PDF 正文删除 specified zones 中 computer/data storage centers 作为 permitted principal uses。未核实该 moratorium 是否影响已获批的 QTS PB25-006：https://www.east-windsor.nj.us/township-ordinances ; https://www.east-windsor.nj.us/media/Township%20Ordinance/2026/ordinance-2026-06-data-center-moratorium.pdf
- capacity_mw: 保持 null。可确认的是 campus-level 70 MW+，不是第二栋 building-level capacity；QTS FAQ 明确不披露具体 power capacity。
- 冲突/不足：Baxtel 的 under construction 与当前官方可核实资料之间存在证据级别差异；本次未找到官方施工许可、并网记录、JCP&L/PJM 队列记录或第二栋 MW。
