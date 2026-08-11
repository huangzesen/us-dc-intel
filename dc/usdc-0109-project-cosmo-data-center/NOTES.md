# USDC-0109 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: no status
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- 结论：将 `Project Cosmo data center` 从 seed-only 的 Eagan, Dakota County, Minnesota 记录纠正为 Cheyenne, Laramie County, Wyoming 的 Meta/Cheyenne Data Center。City of Cheyenne 项目页列出 `PUDC-24-47: Project Cosmo - Site Plan`，用途为 Data Center，2024-03-06 submitted，2024-06-17 approved；证书列出 owner Goat Systems LLC、地址 1800 High Plains Road、Lot 1 Block 1 High Plains Business Park、Proposed Use: Data Center (Project COSMO)。来源：https://connect.cheyennecity.org/m26462 与 https://connect.cheyennecity.org/Customer/File/Full/fcbde5be-4528-4ef1-b967-630e87d1d7c1
- 新增 2025 后续地方政府事实：City of Cheyenne 2025-12-01 Certificate of Review（PUDC-25-229）继续列出 1800 High Plains Road，Proposed Use: Data Center - Project Cosmo - RDS - CHY3 and CHY5，site conditions include landscape phasing through 2026/2028/2031；该证书有效至 2027-12-01。来源：https://connect.cheyennecity.org/Customer/File/Full/782d01fa-7dc2-4de9-a09a-0770114e5f4b
- 新增业主/开发商事实：Meta 于 2024-07-02 announced Cheyenne Data Center，称 Cheyenne, Wyoming 为其新 Meta data center，715,000 square feet，投资超过 $800 million，约 100 operational jobs，peak construction 超过 1,000 workers，并针对 AI workloads 优化；Fortis 项目页同样列出 Meta Cheyenne campus、715,000 sf、超过 $800 million。来源：https://datacenters.atmeta.com/2024/07/hello-cheyenne/ 与 https://fortisconstruction.com/project/meta-cheyenne-campus/
- status 更新：从 `null/no status` 更新为 `site work-construction`。依据：地方政府 site plan/COR 已批准且后续 2025 COR 覆盖 CHY3/CHY5；Meta/Fortis 项目页确认建设项目；2026-07-08 Guardian 报道称 Project Cosmo construction wastewater incident occurred during construction at the Cheyenne campus。来源：https://www.theguardian.com/us-news/2026/jul/08/meta-datacenter-ai-wyoming-water
- capacity_mw：未找到官方或公司披露的 MW 容量，保留 `null`。面积/投资已记录为证据但不等同于 MW capacity。
- 冲突：Electrical Marketing 2024-10-25 表格列出 “Project Cosmo Data Center, Eagan, MN, $390M, plans announced Sept. 2024, source construction.com”，与 Cheyenne 官方/Meta 来源冲突；Eagan 官方材料列出当地四个 existing/under construction data centers（Former Unisys、DataBank 20 MW、Centra 12 MW、Oppidan 5 MW）及 Q3 2025 business news 的 Oppidan/Centra 项目，未显示 Project Cosmo。保留此冲突于 data.json。来源：https://img.electricalmarketing.com/files/base/ebm/electricalmarketing/document/2024/10/671bb91a262dd6a45f0c2652-10252024em_digital.pdf?dl=671bb91a262dd6a45f0c2652-10252024em_digital.pdf 、https://cityofeagan.com/eagan-business-news-q3-2025 、https://eagan.granicus.com/MetaViewer.php?event_id=3640&meta_id=154152&view_id=8
