# USDC-0070 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: South Carolina officially announced site selection and planned four-facility campus
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：从单纯 state/company announced 提升为 local process/economic-development approved。Cherokee County Council 在 2025-06-23 通过 Ordinance No. 2025-22 三读，批准 Project King Fisher 的 FILOT / Special Source Revenue Credit Agreement；会议纪要同时确认 Project Kingfisher 即 Cielo Digital Infrastructure，并说明项目为 Ford Road, Gaffney 的约 $2.1B data center、30 个预期岗位、初始运营预计 2028。来源：https://cherokeecountysc.gov/wp-content/uploads/2025/07/Minutes-6-23-35.pdf
- 补入前置县级动作：Cherokee County Council 在 2025-05-19 通过 Resolution No. 2025-02，并通过 Ordinance No. 2025-22 一读，均涉及 Project Kingfisher 的 FILOT / Special Source Revenue Credit Agreement。来源：https://cherokeecountysc.gov/wp-content/uploads/2025/06/Minutes-5-19-2025.pdf
- 补入最新找到的县级动作：Cherokee County Council 在 2026-01-05 通过 Ordinance No. 2025-25 三读，确认和追认与 Spartanburg County 共同设立、位于 Cherokee County 的 Jointly Owned & Operated Industrial/Business Park，会议纪要标注该事项 related to Project Kingfisher。来源：https://cherokeecountysc.gov/wp-content/uploads/2026/02/Minutes-1-5-26.pdf
- 官方项目范围保持：South Carolina Governor 2025-06-24 公告确认 Cielo Digital Infrastructure, LLC 选择 Cherokee County，计划在 000 Ford Road 建设四栋约 400,000 平方英尺设施及关联电力变电站，投资约 $2.1B、预期 30 个岗位、初始运营预计 2028 年底。来源：https://governor.sc.gov/news/2025-06/cielo-digital-infrastructure-selects-cherokee-county-first-south-carolina-development
- capacity_mw 仍保持 null：官方/县级来源未发布 MW。DCD 2025-06-24 报道 full build-out could total up to 300MW，Cleanview 当前 tracker 也列 300 MW planned / 1,600,000 平方英尺；本次仅在 capacity_mw_basis 记录，未写入 capacity_mw。来源：https://www.datacenterdynamics.com/en/news/cielo-digital-infrastructure-plans-300mw-data-center-campus-in-south-carolina/ ，https://cleanview.co/data-centers/south-carolina/808/cielo-cherokee-county-campus
- 未核实项：未找到公开 county/city site plan、building permit、environmental permit、utility-service/interconnection、construction-start、CO、energization 或 live-service 记录；因此不提升到 approved-permitted、site work-construction、energized、partial live 或 full buildout。
- 冲突：未发现实质冲突；官方只缺 MW，行业/tracker 的 300 MW 作为非官方容量上下文保留。
