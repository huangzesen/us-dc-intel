# USDC-0053 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Press reports conflict: one reported a January 2026 rezoning approval and another reported that a key zoning approval was voided and the process restarted in April
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：由“press reports conflict”改为 `local process`。Stokes County Board of Commissioners 官方声明称 2026-01-12 的 zoning changes 与 Project Delta rezoning 已被 void 且 “have no legal effect”；若申请方继续推进，需重新提交并完整走 notice/hearing 流程。来源：https://www.co.stokes.nc.us/news_detail_T1_R140.php
- 新申请：Stokes County 官方 Project Delta 页面列出 Submission Date: 2026-07-20；conditional rezoning application 请求将约 1,848.741 acres 从 R-A 改为 M-2-CZ，用于 data center 及 accessory uses。来源：https://www.co.stokes.nc.us/departments/data_center.php
- owner/applicant/location 补证：County-hosted application 与 2026-08-13 Planning Board notice 均列出 DFC Stokes, LLC and DFC Stokes 2, LLC；petitioner/applicant 为 Engineered Land Solutions, LLC；地块为 0 US Highway 311 & Tuttle Road、0 Off US 311 Highway、1290 Coon Joyce Road、1203 Tuttle Road, Walnut Cove, NC 27052；PINs 6973-76-7124、6973-73-4188、6964-91-8321、6973-49-0574。来源：https://www.co.stokes.nc.us/(1)%20Conditional%20Rezoning%20Application.pdf?t=202607220846010 与 https://www.co.stokes.nc.us/news_detail_T1_R156.php
- process milestone：申请方 Public Information Meeting 于 2026-07-08 举行；PIM report 称会后加入/强化 residential buffer、noise、water source/cooling、floodplain、lighting 等 proposed conditions。来源：https://www.co.stokes.nc.us/(5)%20PIM%20Written%20Report.pdf?t=202607220850020 与 https://www.co.stokes.nc.us/(2)%20Zoning%20Conditions%20.pdf?t=202607220846570
- local zoning context：Stokes County staff report 称 Ordinance Amendment R 于 2026-07-13 adopted，将 data center 加入 M-2 district 中仅可通过 conditional zoning district approval 的用途；这只是允许审查该类申请，不等于 Project Delta 获批。来源：https://www.co.stokes.nc.us/Project_Delta_Staff_Report_PB.pdf?t=202608041704390
- next local action：Stokes County posted/digitally signed 2026-08-04 Planning Board Special Meeting Notice，会议定于 2026-08-13 18:00 review and consider recommendations on the Project Delta conditional rezoning application。刷新日为 2026-08-11，会议尚未发生。来源：https://www.co.stokes.nc.us/news_detail_T1_R156.php
- staff recommendation：2026-08 staff report recommends approval as reasonable and in the public interest，但明确 Planning Board/Board of Commissioners findings 与后续 hearings 仍是独立步骤。来源：https://www.co.stokes.nc.us/Project_Delta_Staff_Report_PB.pdf?t=202608041704390
- capacity_mw 保持 null：官方 application/site plan/staff report/notice 未核实 MW 容量；site plan 标注 “PRELIMINARY - DO NOT USE FOR CONSTRUCTION”，且 staff report 将 energy demand/grid capacity 留给 utility interconnection process。来源：https://www.co.stokes.nc.us/Site%20Plan_(2).pdf?t=202607270820570 与 https://www.co.stokes.nc.us/Project_Delta_Staff_Report_PB.pdf?t=202608041704390
- 未核实/证据不足：未发现正式 Board of Commissioners project approval、building permit、construction start、utility interconnection approval、energized/operational 证据；end user/operator 未在官方材料中识别。
- 多源冲突：早期媒体所称 January approval 已由 2026-04-15 county statement 解释为 void/no legal effect；任何第三方 tracker capacity（如 300 MW）未被官方材料支持，未写入 `capacity_mw`。
- verified: true（对当前 local-process status、owner/applicant/location/parcels/acreage、pending hearing、staff recommendation 均有官方 county-hosted source；capacity/permits/construction/utility/end-user 明确标为未核实）。
