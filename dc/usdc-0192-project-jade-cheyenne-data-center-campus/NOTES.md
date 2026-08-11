# USDC-0192 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Laramie County’s July 8 official notice says Project Jade is now Project Tembo, identifies Google d
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新为 local process / administrative resubmittal。Laramie County 2026-07-08 memo 明确 Project Jade 现为 Project Tembo，Crusoe Energy 已退出，县方与 Google d.b.a. Jupiter Star Holdings, LLC 就 resubmittal 进行沟通；数据中心部分由五栋、4,025,500 sq. ft. 缩减为四栋、3,080,000 sq. ft.，县方计划按 administrative Site Plan Revision 处理。来源: https://www.laramiecountywy.gov/files/sharedassets/public/v/1/county/public-notice/project-tembo-memo-07082026.pdf
- owner 从 null 更新为 Google d.b.a. Jupiter Star Holdings, LLC。该 owner 身份为官方县 memo 直接证据；Cowboy State Daily 2026-07-08 与 DCD 2026-07-14 作为二级/行业补证。来源: https://www.laramiecountywy.gov/files/sharedassets/public/v/1/county/public-notice/project-tembo-memo-07082026.pdf ; https://cowboystatedaily.com/2026/07/08/google-revealed-as-owner-of-wyomings-largest-data-center-now-project-tembo/ ; https://www.datacenterdynamics.com/en/news/google-is-customer-behind-27gw-data-center-campus-near-cheyenne-wyoming/
- capacity_mw 从 null 更新为 2700，但证据等级加 caveat：2.7 GW 与 716-acre / Switchgrass Industrial Park / 2031 completion target 来自 Cowboy State Daily 对规划文件的报道，并由 DCD 转载/补证；本次可访问的官方县 memo 只确认建筑数量、总建筑面积、Google/Jupiter Star 身份、PZ-26-00057/PZ-26-00058 与流程状态，未直接列出 MW 容量或 parcel IDs。来源: https://cowboystatedaily.com/2026/07/08/google-revealed-as-owner-of-wyomings-largest-data-center-now-project-tembo/ ; https://www.datacenterdynamics.com/en/news/google-is-customer-behind-27gw-data-center-campus-near-cheyenne-wyoming/
- August 13, 2026 Planning Commission hearing 仍标记为 pending，因为本次刷新日期为 2026-08-11。该 hearing 仅针对 office-complex CUP PZ-26-00057；data-center Site Plan Revision PZ-26-00058 不应从该 future hearing 推断为已批准。来源: https://www.laramiecountywy.gov/files/sharedassets/public/v/1/county/public-notice/project-tembo-memo-07082026.pdf
- 负面核实：未发现 final revised data-center approval、building permit、CO/inspection、utility interconnection 或 energization 记录。Laramie County SmartGov portal 可访问，但详细申请材料检索受 portal/search/login 限制，本次未使用账号或 records request。来源: https://co-laramie-wy.smartgovcommunity.com/
- 冲突/注意：部分 tracker 或行业页面把项目列为 under construction/permitted；本目录保守保留为 local process / administrative resubmittal，除非后续官方记录确认 revised site plan/building permits/site work/energization。Tallgrass power hub construction underway 不等同于 Google/Jupiter Star data-center buildings under construction。
