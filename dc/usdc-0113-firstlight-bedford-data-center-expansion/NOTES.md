# USDC-0113 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Company-announced expansion; construction, local approval, permit, utility, energization, commissioning, and service were not verified
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status/capacity: 维持 `announced`。FirstLight 2026-03-10 公告确认 Bedford 数据中心扩建，新增约 25% data-center space、additional power and cooling infrastructure，并支持 up to 100 additional racks、private suites、caged environments；仍未披露 MW、投资额、施工开始、竣工或投运日期。来源：https://www.firstlight.net/firstlight-expands-bedford-nh-data-center/ ；WordPress API 时间戳确认 published 2026-03-10、modified 2026-04-26：https://www.firstlight.net/wp-json/wp/v2/posts/18150
- location/property: Bedford/VGSI assessment record 将 `8 COMMERCE DR` 解析为 PID 5502、MBLU 35/98/23；parcel page 显示 owner of record 为 `8 COMMERCE DRIVE LLC`、1 building、8.95 acres、2026 total market value $8,616,200。该证据只用于地址/地块与现有建筑佐证，不证明扩建审批或施工。来源：https://gis.vgsi.com/bedfordnh/Parcel.aspx?Pid=5502 ；assessment database caveat/Bedford assessing page：https://gis.vgsi.com/bedfordnh/ 、https://www.bedfordnh.gov/149/Assessing
- permit/context: Bedford Building Code Compliance 页面提示需要 permit 的工作在 permit issued 前不得开始，包括 foundation excavation；Online Permitting System 页面说明可查看/支付 building permit status，但 building permits 仍需在 Safety Complex 申请。未在公开来源核实到与 FirstLight/8 Commerce Dr 扩建对应的 building permit、planning approval、utility interconnection、energization、commissioning 或 service record。来源：https://www.bedfordnh.gov/169/Building-Code-Compliance 、https://www.bedfordnh.gov/924/Online-Permitting-System
- secondary check: DCD 2026-03-10 报道复述 FirstLight 公告中的约 25% space 增量与 up to 100 additional racks；未提供独立 MW/permit/construction 证据。来源：https://www.datacenterdynamics.com/en/news/firstlight-expands-new-hampshire-data-center/
- conflicts: DataCenterMap 将 2026-03-10 event 标注为 `Phase Operational`/`completes expansion`，但这与 FirstLight/DCD 原文的 announcement wording 不一致，且未见官方 completion/energization source；未写入 status 升级。来源：https://www.datacentermap.com/usa/new-hampshire/manchester-nh/bedford-data-center/
