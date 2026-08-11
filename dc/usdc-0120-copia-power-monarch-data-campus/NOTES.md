# USDC-0120 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Lyon County’s official record shows a Planning Commission recommendation and a December 4, 2025 Board approval of a master-plan amendment by 4–1, while expressly stating that the action does not appro
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：从 “local process / no PUD approval found” 更新为 “approved-permitted（tentative PUD only）”。Lyon County BOCC 在 2026-08-06 以 3-1、1 abstention 批准 Copia Power Devco, LLC 将约 505.4 acres rezoned to Planned Unit Development for the Monarch Data Center；县方同时说明这是 tentative PUD approval，Copia 必须在一年内申请 final PUD approval。来源：https://www.lyon-county.org/m/newsflash/Home/Detail/402
- 仍未上调为 construction / energized：县方 2026-08-07 meeting summary 明确列出施工前仍需 final drainage plans、emergency response plans、fire suppression/emergency response plans、roadway improvements、NDEP permits、Nevada State Engineer water-right conversion approval 等要求；未找到 final PUD、building permit、construction start 或 energization 公开记录。来源：https://www.lyon-county.org/m/newsflash/Home/Detail/402
- 新增 2026-07-14 Planning Commission PUD recommendation：Planning Commission 记录显示 PLZ-2026-041 推荐批准，项目描述为 4.6 million square feet、1,000 MW、8 栋两层数据中心建筑、500 MW battery energy storage、500 MW natural gas backup、substation、high-voltage lines，约 505.40 acres；投票 4 Ayes / 3 Nay。来源：https://www.lyon-county.org/AgendaCenter/ViewFile/Agenda/_08112026-2085
- 新增 2026-08-06 BOCC agenda 佐证：正式议程列明 10:00 AM action item 6.b，请求批准 PLZ-2026-041 PUD zone change，并列出 4.6 million square foot、1,000 MW、8 buildings、500-MW BESS、500-MW gas backup、APNs 014-201-07 and 014-201-30。来源：https://www.lyon-county.org/DocumentCenter/View/14287/BOCC-08062026-Agenda
- capacity_mw 从 null 更新为 1000；owner 从 null 更新为 Copia Power Devco, LLC。Copia 官方 footprint 页列出 Monarch, Lyon NV, Data Center Capacity 1000MW, PV Capacity 200MW, Storage Capacity 500MW, Thermal Capacity 500MW。来源：https://www.copiapower.com/interactive-map-collection/ru9ht9lachmjgoqnn73bq8grhyfjei-mhprk-gd4f3-yf9ax-93my9-9ftc2-rf7hh-jg6rr-224sc-t23mt-h5xp6-zw5cj-a9x2y-6c978-tthy2-7a46w-ejjen-ln25x-2jarn-e98nn-7yg8p
- 补充媒体交叉核实：The Nevada Independent 于 2026-08-08 报道 BOCC approval 是 tentative，Copia 仍需 final design returned to the Board before construction, separate NDEP and State Engineer approvals, and completion of land purchase；该说法与县方 “tentative PUD / pre-construction conditions” 一致。来源：https://thenevadaindependent.com/article/a-massive-data-center-in-rural-nevada-is-one-step-closer-to-being-built
- 冲突/限制：没有发现官方来源冲突。规划委员会材料中仍提到 95-foot building request，而 BOCC approval summary 报告最终 maximum building height 为 75 feet；data.json 采用 BOCC 最新批准条件的 75 feet，并在 action 记录中保留 Planning Commission 阶段事实。
- 修正（2026-08-11 fix pass）：data.json actions 数组按日期严格升序重排（2026-07-16 负向搜索 action 移至 2026-07-14 Planning Commission PUD 推荐之后），无内容变更；修复前顺序为 2025-07-08 → 2025-12-04 → 2026-02-19 → 2026-07-16 → 2026-07-14 → 2026-08-06。
