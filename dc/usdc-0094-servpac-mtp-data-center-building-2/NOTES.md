# USDC-0094 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Company-reported under construction from a 2026-01-22 groundbreaking, with a company Q2 2026 completion target
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status/capacity 对比：刷新前为 company-reported under construction + Q2 2026 completion target、capacity_mw=null；刷新后保持 site work/construction（company-reported）且 Q2 2026 target 未升级为 complete/live，capacity_mw 仍为 null。Servpac 只披露 Building 2 会新增 15,500+ sq ft、使设施面积增加 50% 并 more than double center capacity，未披露 MW。
- 官方/local-gov-first 检查：Honolulu DPP 建筑许可页确认建筑许可/Permit Status/Property Search 为官方查询入口；可访问页面未直接给出 Building 2 的 completion、CO、energization、commissioning 或 live-service 记录。来源：https://www.honolulu.gov/dpp/permitting/building-permits-home/；https://dppweb.honolulu.gov/DPPWeb/Default.aspx?PossePresentation=BuildingPermitSearch
- 地块/permit context：DPP-derived Ikena parcel page for 200 Kahelu Ave / TMK 95046002 lists 5.068 acres, 20 DPP building permits on record, most recent issued 2023-11-17; permits 901525（Office）and 901526（sitework）are shown as Inspection(s) in Progress, and undated Office/Sitework rows are shown as Plans review in progress. This is treated as lower-grade parcel context, not proof of Building 2 completion. 来源：https://ai.ikenagroup.com/p/95046002
- Company source refreshed：Servpac page published 2026-01-28 / modified 2026-05-14 says the Jan. 22, 2026 groundbreaking adds 15,500+ sq ft, increases facility size by 50%, more than doubles center capacity, costs $13M, uses additional company-owned five acres, targets Q2 2026 completion, and lists Ralph S. Inouye Co. as general contractor with JB Construction among prime contractors. 来源：https://servpac.com/mtp-groundbreaking/
- Company release mirror：PRNewswire published the Servpac release on 2026-02-24 with the same scope, cost, Q2 2026 target, Tier IV design intent, and contractor context. 来源：https://www.prnewswire.com/news-releases/servpacs-mtp-data-center-celebrates-groundbreaking-for-building-2-302694909.html
- Local construction corroboration：Building Industry Hawaii published 2026-03-09, repeating the Jan. 22 groundbreaking, $13M / 15,500 sq ft scope, Q2 2026 anticipated completion, and expected Tier IV designation once complete. 来源：https://buildingindustryhawaii.com/2026/03/servpac-inc-breaks-ground-on-mtp-data-centers-building-2/
- 冲突：未发现可核实的多源事实冲突；主要不确定性是 company Q2 2026 target has passed by 2026-08-11, but no accessible official or company completion evidence was located.
- 无法核实/证据不足：Building 2 MW capacity, building permit closeout, certificate of occupancy, utility energization/interconnection, commissioning, and live customer service remain unverified.
- verified: false — scope/owner/site/construction announcement are verified by company and local-trade sources, but completion/CO/energization/live status and MW remain unverified.
