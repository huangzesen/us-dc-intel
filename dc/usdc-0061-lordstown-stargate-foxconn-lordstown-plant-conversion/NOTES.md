# USDC-0061 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: no status
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：从 `no status` 调整为 `site work-construction`。依据：Lordstown Planning Commission 2025-09-16 会议记录对 Foxconn Lordstown facility expansion 做 final site plan review，范围包括三处建筑扩建、一个 POC modular building、以及 existing concrete pad renovation，用于 AI server components / data-center infrastructure 的制造；2025-10-27 本地报道现场已在 former GM plant 前方/西北侧清理、拆除停车场/太阳能阵列等准备工作。来源：https://www.lordstown.com/wp-content/uploads/2025-9-16-Minutes.pdf；https://businessjournaldaily.com/preparation-work-begins-on-lordstown-data-center/
- owner/location 更新：地址补为 2300 Hallock-Young Road / 2823 Ellsworth Bailey Road, Lordstown, OH 44481。EPA 记录确认 former GM Lordstown Complex / Foxconn EV System LLC 位于 2300 Hallock-Young Road；本地报道援引 auditor data 称 property 于 2025-09-24 从 Foxconn EV Property Development LLC 转给 Crescent Dune，land/buildings 价格 8800 万美元，Foxconn 8 月宣布 plant+equipment 总额 3.75 亿美元。来源：https://www.epa.gov/nsr/foxconn-ev-system-llc；https://businessjournaldaily.com/softbank-affiliate-takes-title-to-lordstown-plant/
- Stargate 公告核实：OpenAI 2025-09-23 官方公告将 Lordstown, Ohio 列为 SoftBank/OpenAI 开发的 Stargate site，并称 Lordstown 与 Milam County 两处可在未来 18 个月 scale to 1.5 GW；Lordstown 单点 MW 未在官方公告拆分。来源：https://openai.com/index/five-new-stargate-sites/
- 容量处理：`capacity_mw` 仍保留 `null`。Cleanview 列 Lordstown planned 300 MW、2027 expected year、developer SoftBank，但这是行业 tracker，且与 OpenAI 只给两站合计 1.5 GW 的官方口径无法直接交叉验证。来源：https://cleanview.co/data-centers/ohio/1951/stargate-lordstown
- 当前地方管制：Lordstown Council 2026-01-05 Ordinance 1-2026 对 proposed Data Centers 的新 permit/application 设 180 天 temporary moratorium；2026-06-15 Ordinance 29-2026 又延长不超过 180 天，本地报道称 extension effective 2026-07-05。该 moratorium 影响新数据中心许可，不等同于撤销 2025-09-16 Foxconn expansion site plan approval。来源：https://www.lordstown.com/wp-content/uploads/1-2026.pdf；https://www.lordstown.com/wp-content/uploads/29-2026-1.pdf；https://www.tribtoday.com/news/local-news/2026/06/lordstown-extends-data-center-moratorium/
- 冲突/不确定性：OpenAI/SoftBank 将 Lordstown 称为 AI data center site；但 Lordstown mayor 与 Foxconn 在本地/规划会材料中称 POC modular building 是 engineering/design/showroom，不作为 working/fully functional operational data center 使用。因此本次不标记 energized / partial live / full buildout，也不把 1.5 GW 合计容量归属给 Lordstown。来源：https://www.vindy.com/uncategorized/2025/09/lordstown-chosen-as-one-of-five-ai-data-center-sites/；https://www.lordstown.com/wp-content/uploads/2025-9-16-Minutes.pdf；https://openai.com/index/five-new-stargate-sites/
- 未核实项：未找到 certificate of occupancy、utility energization、commissioning / first IT load、Lordstown 单点 MW allocation、或 moratorium 后续最终 data-center zoning standards。
