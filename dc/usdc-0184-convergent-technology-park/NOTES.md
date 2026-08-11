# USDC-0184 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: no status
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status: `no status` -> `local process`。Fauquier County Community Development 当前仍将 COMA-24-022504 - Convergent Technology Park 列在 applicant-sponsored proposed comprehensive plan amendments 下；本次检查 2026 年已归档 Board of Supervisors / Planning Commission 议程，未发现 Convergent/COMA-24-022504/REZN-24-022505/SPEX-24-022506 的公开听证或批准项。来源：https://www.fauquiercounty.gov/government/departments-a-g/community-development/comprehensive-plan/comprehensive-plan-amendments
- 官方受理事实补证：Fauquier County Department of Community Development 于 2024-08-20 向 Convergent VA, LLC 发函，确认申请已完成 completeness review 并 accepted for processing；案件号为 COMA-24-022504、REZN-24-022505、SPEX-24-022506；申请包括约 90.66 acres comprehensive plan amendment、约 156.14 acres rezoning，以及 Category 20 special exception for aboveground water storage facility。来源：https://www.pecva.org/wp-content/uploads/convergent-tech-park-acceptance-letter-fauquier-aug-20-2024.pdf
- 位置补证：县官方材料定位为 James Madison Street / James Madison Highway, Remington, Lee District，PIN 6888-13-7752-000 与 6888-25-0487-000；Baxtel 另列 11650 James Madison St。来源：https://www.fauquiercounty.gov/government/departments-a-g/community-development/comprehensive-plan/comprehensive-plan-amendments 和 https://baxtel.com/data-center/convergent-technology-park
- owner/developer: `null` -> `Convergent VA, LLC`。官方受理函列申请人为 Convergent VA, LLC；Cleanview 也列 developer 为 Convergent VA LLC。来源：https://www.pecva.org/wp-content/uploads/convergent-tech-park-acceptance-letter-fauquier-aug-20-2024.pdf 和 https://cleanview.co/data-centers/virginia/1712/convergent-technology-park
- capacity_mw: `null` -> `240`，但标注为 power need 而非经核实 IT load。DCD 2024-04-14 报道 Convergent VA 致 Dominion Energy 的信称 campus would need 240 MW to be powered，并称无 named end user。来源：https://www.datacenterdynamics.com/en/news/new-plans-shared-for-convergent-technology-park-in-fauquier-county-virginia/
- scope 补证：当前 proposal 为 4 栋数据中心，约 1.0-1.07 million sq ft，预计超过 $1B、3-4 年完成；DCD/Baxtel 称 60 ft buildings，PEC 称 each at least 65 ft；Cleanview 列 1,056,000 sq ft、139 acres、status planned。来源：https://www.datacenterdynamics.com/en/news/new-plans-shared-for-convergent-technology-park-in-fauquier-county-virginia/ 、https://baxtel.com/data-center/convergent-technology-park 、https://cleanview.co/data-centers/virginia/1712/convergent-technology-park 、https://www.pecva.org/region/fauquier/update-on-data-center-development-and-transmission-lines-in-fauquier/
- 电网/连接备注：PEC 2024-10-04 称 Convergent 不能直接接入穿过场地南部的 500 kV line，需以地下线路接到 Remington 的 off-site substation；这是 advocacy/NGO 来源，作为 grid constraint 备注，不提升为官方事实。来源：https://www.pecva.org/region/fauquier/update-on-data-center-development-and-transmission-lines-in-fauquier/
- 多源冲突：site acres 存在 90.66/156.14/139-140 acres 口径差异；gross sqft 存在约 1.0M/1.07M/1,056,000 sq ft 差异；building height 存在 60 ft 与 at least 65 ft 差异。已写入 `contradictions`。
- 无法核实/证据不足：未找到官方批准、permit issuance、construction/site-work、energization 或 named end-user 证据；EnerGov portal direct API 读取未能返回结构化记录，本次以县综合规划页和受理函为 official record。
- verified: true（对 `local process` 状态、官方案件号、申请人、位置/PIN、受理日期可确认）；capacity_mw verified as reported power need only。
