# USDC-0174 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Utah government inventory lists the project under construction at a 5–30 MW range; Provo permit and commissioning evidence were not located
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新为 local process denied / no verified construction：Provo 官方 2026-03-10 市议会会议纪要显示，1507 S 180 E 从 PIC 改为 PICDC 数据中心 overlay 的 Ordinance 2026-10 / PLRZ20250622 动议以 0:7 失败；未找到后续施工、building permit、energization 或 commissioning 证据。来源：https://agendas.provo.gov/Documents/DownloadFileBytes/Work_Meeting_2306_Agenda_Packet_5_26_2026_1_00_00_PM.pdf?documentType=5&isAttachment=True&meetingId=2306
- 补充官方本地规划事实：Provo Planning Commission 2026-02-11 packet 列出 Stephen Styler 的 PLRZ20250622 overlay 请求、Reid Wintersteen 的 PLPPA20250210 project-plan 请求，地址 1507 S 180 E，owner 为 B+F TIMPANOGOS TECH CENTER LLC，parcel IDs 66:484:0001 / 66:484:0002，面积 7.29 acres。来源：https://www.provo.gov/DocumentCenter/View/7493
- 补充规模/设计事实：官方 packet 描述项目为拆除既有建筑并新建 66,000 sq ft footprint、两层合计 132,000 sq ft data center；用 Provo City/Provo Power grid power，不做 onsite power generation；closed-loop water system 估算 7,000-12,000 gallons/day，development agreement 上限 4,380,000 gallons/year；项目 power usage 规划为 5-50 MW as available from Provo Power，更多容量需要 code changes。来源：https://www.provo.gov/DocumentCenter/View/7493
- 保留冲突：baseline/Utah government inventory 曾列为 under construction、5-30 MW；Provo 本地官方审批记录显示 overlay 已被否决，因此本次将 Provo 市级 entitlement 记录作为当前 status 的权威来源。baseline 来源：https://www.utah.gov/pmn/files/1444799.pdf
- 第三方佐证：BYU Daily Universe 2026-03-17 报道市议会 2026-03-10 以 7-0 反对该 zoning reclassification，并称提案为 5 MW、潜在 50 MW；DCD 2026-02-06 报道早期材料称初始约 5 MW、潜在 30 MW IT capacity、约 $280M 投资；Baxtel 当前页面仍标为 Planned 并列出 1507 S 180 E、operator B+F Timpanogos Tech Center LLC，但其叙述仍称 March 10 vote scheduled，未反映否决结果。来源：https://universe.byu.edu/metro/provo-city-council-votes-against-east-bay-data-center ; https://www.datacenterdynamics.com/en/news/warehouse-in-provo-utah-to-be-replaced-with-data-center/ ; https://baxtel.com/data-center/b-f-timpanogos-provo
- 无法核实/证据不足：未找到公司公告、可访问 building permit、final approved Planning Commission minutes、utility service/interconnection approval、construction start、power-on、CO 或 commissioning 记录。
