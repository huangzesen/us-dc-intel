# USDC-0204 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Microsoft's first facility was company-reported fully operational on 2026-06-23; official/local records and Microsoft state that a second adjacent facility remains under construction
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status/capacity: status 保持为“首栋设施已由 Microsoft 于 2026-06-23 宣布 fully operational；第二座相邻设施仍在施工，完整 campus buildout 未证实”。capacity_mw 仍为 null；未找到官方 MW 容量、CO 或独立并网记录。来源：https://news.microsoft.com/source/2026/06/23/microsoft-completes-construction-on-first-datacenter-facility-in-mount-pleasant-wisconsin/
- 地方政府补证：Mount Pleasant 官方 TID No. 5 页面列出 Microsoft data center Area 3B set for operation in 2026、Area 3A set for completion in 2028，以及 Area II / North Area future data center development；该证据支持“分阶段推进”，不支持 full buildout。来源：https://www.mtpleasantwi.gov/2793/Tax-Incremental-District-No-5
- 地址/地块补证：Mount Pleasant 经济发展地图明细将 Microsoft Data Center (Area 3B) 标在 4800 90th Street，并列为 Under Construction；Wisconsin DOR qualified-data-center 页面列 Microsoft, 90th Street, Mount Pleasant, WI，certification date 2023-10-01。来源：https://www.mtpleasantwi.gov/DocumentCenter/View/4895/20251201-Economic-Development-Map-Details?bidId=；https://www.revenue.wi.gov/Pages/FAQS/ExemptionforQualifiedDataCenter.aspx
- 投资/阶段补证：WEDC 2025-09-18 官方公告称 Microsoft 总投资超过 $7B；第一座 AI datacenter 计划 early 2026 online，第二座 datacenter 约 $4B、同一区域、目标 2028。该来源早于 Microsoft 2026-06-23 operational 公告，作为投资和二期规模背景，不覆盖当前 operational 状态。来源：https://wedc.org/gov-evers-microsoft-officials-announce-new-4-billion-investment-in-mount-pleasant-datacenter/
- 区域更新页：RCEDC/Microsoft Racine County 页面截至本次抓取称 Microsoft 在 Mount Pleasant 拥有 1,575 acres、planned investment estimated at $7.3B、Phase I well underway，并转载 2026-06-23 completion item；作为区域经济开发汇总站，不优先于 Village/WEDC/Microsoft 原始来源。来源：https://rcedc.org/microsoft-in-racine-county/
- 数据变更：owner 从 null 更新为 Microsoft；location 增加 street_address = "4800 90th Street / 90th Street"；新增 evidence_grade；sources 增加本次核验 URL 列表；新增一条 2026-08-11 Village TID No. 5 status action。
- 冲突：未发现新的硬冲突。注意“operation in 2026 / fully operational”仅覆盖首栋或 Area 3B，不等同整个 campus 完成。
- verified: true（上述来源均可访问；但 CO、building permit register、utility energization/MW capacity 未能在公开来源核实）。
