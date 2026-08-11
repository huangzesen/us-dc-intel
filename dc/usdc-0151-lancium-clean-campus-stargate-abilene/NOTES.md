# USDC-0151 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: First-phase and additional buildings are supported by TDLR/TCEQ and local tax records; the complete building-by-building permit, energization, and service record was not assembled
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：从“first-phase/additional buildings supported but permit/energization record incomplete”改为 `partial live / site work-construction`。Oracle 的 Abilene facts page 标注信息截至 2026-01，称 AI workloads 已上线，并称 campus 为 8 栋、1,100 acres、4 million sq ft；但该页面不是 utility energization/CO 记录。来源：https://www.oracle.com/data-centers/abilene/
- capacity 更新：`capacity_mw` 从 `null` 改为 `2100`，含义为 Crusoe 2026-03-27 公告中的 projected full Abilene site capacity（existing Abilene infrastructure + new adjacent 900 MW Microsoft campus）。当前已上线容量低于 2.1 GW；Crusoe 同文称前两栋 100 MW buildings 已 energized，第二阶段把总 campus capacity 提至 1.2 GW 预计 2026 年底完成，新 900 MW campus 首栋预计 2027 年中 energized。来源：https://www.crusoe.ai/resources/newsroom/crusoe-announces-new-900-mw-ai-factory-campus-in-abilene-texas-to-support-microsoft-ai-infrastructure
- 补充 TDLR 官方记录：Building 01 TI（TABS2025000156，2024-09-04 registration，351 Lancium Way，484,960 sq ft，Review Complete）；Building 02 TI（TABS2025007742，2024-12-16 registration，251 Lancium Way，484,960 sq ft，Review Complete）。来源：https://www.tdlr.texas.gov/TABS/Search/Print/TABS2025000156 ，https://www.tdlr.texas.gov/TABS/Search/Print/TABS2025007742
- 补充 TDLR Building 8 官方记录：Crusoe Building 8（TABS2025016967，2025-04-17 registration，480,000 sq ft，Review Complete）与 Building 8 TI（TABS2025019022，2025-06-23 start，485,000 sq ft，Review Complete）。来源：https://www.tdlr.texas.gov/TABS/Search/Print/TABS2025016967 ，https://www.tdlr.texas.gov/TABS/Search/Print/TABS2025019022
- 补充地方政府 phase 9/10/power-plant evidence：Taylor County 2025-09-09 minutes show adoption of a resolution approving tax-abatement and second tax-abatement agreements for Lancium with Abilene DC 9, Abilene DC 10, and Abilene DC TPP; vote 4-1, Commissioner Kendrick voted no。来源：https://www.taylorcounty.texas.gov/ArchiveCenter/ViewFile/Item/1344
- City of Abilene tax-abatement page now lists executed tax-abatement materials for phases 1-8 and Resolution No. 249-2025 plus agreements for phases 9-10 and the electricity generation plant; it also warns that execution does not necessarily mean an agreement is currently in effect. 来源：https://abilenetx.gov/2476/Tax-Abatements
- 冲突/证据边界：未发现直接冲突；但 official local records are tax-abatement/reinvestment-zone records, TDLR records are architectural-barriers registrations, and company sources provide live/capacity claims. Municipal building permits, certificates of occupancy, and utility interconnection/service records remain unassembled.
