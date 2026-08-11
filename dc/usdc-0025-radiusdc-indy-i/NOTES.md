# USDC-0025 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: no status
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 从 `no status` 更新为 `approved-permitted`：Town of Plainfield 项目页显示 DP-25-087、DP-25-088、PP-25-094 的 Primary Plat and Development Plans approved；项目位置为 Smith Road 与 AllPoints Parkway 东南角。来源（访问 2026-08-11）：https://www.townofplainfield.com/2009/Radius-Data-Centers-Allpoints-18-and-19
- 官方项目索引补证：Plainfield Plan Commission 2026-01-05 条目列出 DP-25-088 为 100,833 square foot data center、PP-25-094 为 two-lot non-residential plat，位置同为 Smith Road 与 AllPoints Parkway 东南角。来源（访问 2026-08-11）：https://www.townofplainfield.com/1554/Plan-Commission-Projects
- staff report 补证：2026-01-05 Plan Commission report 记录 Radiant DC REIT III-B, LLC 为 petitioner，AllPoints 19 为 100,833 平方英尺数据中心，地块合计 31.235 acres；报告同时列出 future actions 包括 Secondary Plat、Improvement Location Permit and other required permits，且写明 Plan Commission/Town Council 对部分后续项 not required。来源（访问 2026-08-11）：https://s3.amazonaws.com/iworq-upload/PLAINFIELD/601/30087910-RadiusDataCenterAllpoints.pdf
- capacity 更新为 12 MW：AllPoints 19 / RadiusDC Indianapolis 1 project summary dated 2025-12-15 lists approximately 100,000 SFT, single story, with ~12MW critical load; schedule says applicant desired to commence Lot 19 in 2026 with Lot 18 to follow. 该 schedule 仅作 applicant intent，不作为开工证据。来源（访问 2026-08-11）：https://s3.amazonaws.com/iworq-upload/PLAINFIELD/601/50d90d4aafbac31a514a2ccb5fb0712d_25.12.18_Project_Summary_-_AllPoints_19_-_Updated.pdf
- utility 补证：Duke Energy letter dated 2025-11-21 states Duke is the electric service provider for the 30.3 acres at AllPoints 19 and AllPoints 18 and has facilities in the area to serve the proposed development; letter also says it is not a formal commitment or formal approval. 来源（访问 2026-08-11）：https://s3.amazonaws.com/iworq-upload/PLAINFIELD/601/86482b3f8b5d26d17f8bcb56032a67e9_25.12.18_Project_RadiusDC_-_Will_Serve_Letter.pdf
- company/tracker cross-check：RadiusDC Indianapolis location page describes the Plainfield campus as two facilities, Indy I and Indy II, at AllPoints Parkway; RadiusDC January 2026 announcement describes a 24MW edge colocation campus starting with Indy I and notes a new Duke Energy substation under development next to the property. Cleanview lists the Radius AllPoints Data Center as planned, 24 MW, 200,000 square feet. Sources（访问 2026-08-11）：https://www.radius-dc.com/location/indianapolis ; https://www.radius-dc.com/newsroom-and-events/radiusdc-expands-its-footprint-with-edge-colocation-campus-in-indianapolis-in ; https://cleanview.co/data-centers/indiana/1919/radius-allpoints-data-center
- 未核实项：未找到 Improvement Location Permit、building permit、construction start、energized service、CO/occupancy 的公开一手证据；因此不升级为 site work-construction / energized / live。
- 冲突：无实质冲突。名称层面存在 RadiusDC brand、Radiant DC REIT III-B applicant、AllPoints 19、RadiusDC Indianapolis 1 / Indy I 的对应关系，已在 aliases/owner 字段分开记录。
