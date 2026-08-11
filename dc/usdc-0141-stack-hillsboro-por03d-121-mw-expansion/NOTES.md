# USDC-0141 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: STACK's current project page describes a 55-acre POR03 campus with 200 MW total critical capacity, 72 MW operational, 25 MW near-term availability, and 96 MW expansion capacity, including POR03D at 25
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：POR03D 仍按 announced/local process 处理；未找到 Hillsboro 项目级 final land-use decision、building permit、grading/stormwater permit、inspection、CO、utility/interconnection、energization 或 commissioning 记录。STACK 官网当前 POR03 页显示园区 55 acres、约 200 MW total critical capacity、72 MW operational、25 MW near-term availability、96 MW expansion capacity，并列 POR03D 为 220,000 sq ft / 25 MW。来源：https://www.stackinfra.com/locations/americas/portland/por03/
- capacity_mw 从 null 更新为 25，owner 从 null 更新为 STACK Infrastructure。依据为 STACK 官网 POR03D 条目及 DCD 2026-02-11 报道；DCD称 121 MW POR03D/E/F expansion 首期 POR03D 为 25 MW、目标 Q4 2027，之后为 42 MW POR03E 与 54 MW POR03F。来源：https://www.datacenterdynamics.com/en/news/data-center-developer-stack-to-expand-hillsboro-campus-by-121mw/
- 官方环境许可/风险评估补证：Oregon DEQ Cleaner Air Oregon 的 SI POR03 页面称 SI PORL3/STACK 申请 Standard Air Contaminant Discharge Permit，用于 4735 NE Starr Blvd 的 prospective data center，拟安装 49 台 3,000 kW diesel-fired emergency generators；DEQ 于 2021-04-07 批准 Level 3 Risk Assessment。该证据支持 POR03 campus 环境许可背景，但不等同于 POR03D city building permit、开工、并网或投运。来源：https://www.oregon.gov/deq/aq/cao/nwr/pages/stack-infrastructure.aspx
- 地方政府新背景：Hillsboro City Council 于 2026-07-27 通过 120-day land-use moratorium，暂停受定义约束的 new/expanded data center 与 BESS primary-use land-use applications；已在 moratorium 前提交申请的项目可继续。2026-08-03 市府后续说明列出 moratorium 结束目标日期 2026-11-24，并计划新增 utility service availability pre-submittal requirement。来源：https://www.hillsboro-oregon.gov/Home/Components/News/News/17551/ 与 https://www.hillsboro-oregon.gov/Home/Components/News/News/17569/
- 冲突：Cleanview 当前列 POR03D 为 planned、33 MW、expected 2027、220,000 sq ft；与 STACK/DCD 的 POR03D 25 MW 冲突。本次 data.json 使用业主/公司来源的 25 MW，并把 Cleanview 保留为 contradiction。来源：https://cleanview.co/data-centers/oregon/1076/stack-infrastructure-por03d
- verified: false。已验证 owner-published capacity、DCD expansion schedule、Oregon DEQ environmental-process record、Hillsboro citywide moratorium；但未能核实 POR03D-specific local permit/application status、utility allocation/interconnection、construction start、energization 或 commissioning。
