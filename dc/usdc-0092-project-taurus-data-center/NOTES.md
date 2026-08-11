# USDC-0092 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Colorado Springs’ official notice documents a proposed development-plan modification and neighborhood meeting
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：从“官方 notice + 待核实审批/上诉”更新为“local process / approved-permitted but under appeal”。官方 Colorado Springs Legistar/附件确认 DEPN-26-0039 的 Development Plan Modification、June 2026 行政审批文件、July 23 Planning Commission 上诉听证 docket；CPR 报道 Planning Commission 于 2026-07-23 以 6-2 维持行政审批，且 2026-08-06 报道该决定已再次上诉至 City Council，听证需在 2026-08-29 至 2026-09-28 之间举行，预计 9 月中旬。来源：
  - https://coloradosprings.legistar.com/LegislationDetail.aspx?ID=8141471&GUID=FD9DB1D0-50A3-4244-A803-D3F56E2A837F&Options=&Search=
  - https://coloradosprings.legistar.com/MeetingDetail.aspx?GUID=42D16A91-11EF-4917-BACD-1FE19AF1EA93&ID=1428871&Options=info%7C&Search=
  - https://www.cpr.org/2026/07/24/project-taurus-appeal-fails/
  - https://www.cpr.org/2026/08/06/colorado-springs-city-council-data-center-hearing/
- 行政审批日期修正/冲突：city approval letter 写明 Land Use Review Division 于 2026-06-10 administratively approved Corporate Ridge Filing No. 1 Lot 4 Development Plan Modification；approved plan sheets stamped 2026-06-11；staff report 文字说 modified development plan approved on 2026-06-11；早前媒体/通知口径存在 June 12 说法。data.json 以 approval letter 的 2026-06-10 作为 action date，并在 contradictions 保留日期冲突。来源：
  - https://coloradosprings.legistar.com/View.ashx?M=F&ID=15703073&GUID=ADDC612A-C5E1-44DF-9A57-7DC1715CB7A1
  - https://coloradosprings.legistar.com/View.ashx?M=F&ID=15703074&GUID=55A405C9-9539-4E01-AA3D-8ACD17A09511
  - https://coloradosprings.legistar.com/View.ashx?M=F&ID=15703963&GUID=0E5B7010-1DD3-476F-ADE2-4BAD2857C76A
- owner/developer/location 补强：city staff report lists owner as 3G Venture II LLC, developer as Raeden, address/location as 1565 High Tech Way, and site size as approximately 21.96 acres. Approval letter says the approval establishes a data center use in the existing industrial building and site improvements on the 21.96-acre BP-zoned site. 来源：
  - https://coloradosprings.legistar.com/View.ashx?M=F&ID=15703963&GUID=0E5B7010-1DD3-476F-ADE2-4BAD2857C76A
  - https://coloradosprings.legistar.com/View.ashx?M=F&ID=15703073&GUID=ADDC612A-C5E1-44DF-9A57-7DC1715CB7A1
- capacity_mw 更新：capacity_mw 从 null 更新为 50，但标注为 reported cap, not independently finalized city action. Colorado Politics 报道 Planning Commission 的附加限制包括不超过 50 MW、10 年公开 utility usage、扩展 noise monitoring；官方 Legistar 当前能确认 July 23 appeal docket 与附件，但 reviewed public page 未发布 finalized action/result。来源：
  - https://www.coloradopolitics.com/2026/08/03/appeals-filed-to-send-project-taurus-decision-to-the-colorado-springs-city-council/
  - https://coloradosprings.legistar.com/LegislationDetail.aspx?ID=8141471&GUID=FD9DB1D0-50A3-4244-A803-D3F56E2A837F&Options=&Search=
- sound/noise 条件补强：city-posted Sound Monitoring Plan dated 2026-07-15 requires pre-construction baseline monitoring, post-construction monthly reporting once operational, public availability through project/city records, and complaint/remediation procedures. It identifies Raeden Corporation as applicant and confirms chillers operate during facility operations while backup generators are standby-only except outages/monthly maintenance. 来源：
  - https://coloradosprings.legistar.com/View.ashx?M=F&ID=15703088&GUID=2DE98EA8-4338-433E-BA88-8F629624AB0B
- 未核实/不足：未找到 finalized Planning Commission minutes/action result、City Council appeal Legistar item/date、building permit、construction start、CO、utility interconnection/service approval、tenant identity或 energization 证据。状态不得提升为 construction/energized。
