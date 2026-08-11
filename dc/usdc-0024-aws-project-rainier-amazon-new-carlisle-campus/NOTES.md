# USDC-0024 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: no status
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status: 从 `null` 更新为 partial live / operating-source evidence。依据：IDEM permitted_sources.xlsx 显示 Amazon Data Services Incorporated 在 New Carlisle 的 55001 Larrison Blvd.（source 18-141-00642 / permit 47750，permit timestamp 2025-01-28 08:55:40，expiration 2030-01-28 08:56:37）和 31100 SR 2（source 18-141-00650 / permit 48298，permit timestamp 2025-05-01 12:16:33，expiration 2030-05-01 12:17:03）均为 Operating。Source: https://www.in.gov/idem/airpermit/files/permitted_sources.xlsx
- owner: 从 `null` 更新为 Amazon Data Services Incorporated。依据同上 IDEM permitted-source register。Source: https://www.in.gov/idem/airpermit/files/permitted_sources.xlsx
- Project Rainier operational-use evidence: Amazon / AWS 在 2025-06-24 公告称 Project Rainier 已投入使用 / fully operational，包含近 50 万 Trainium2 chips，Anthropic workloads 已运行；同文将 St. Joseph County, Indiana 数据中心列为 Project Rainier sites 之一。Source: https://www.aboutamazon.com/news/aws/aws-project-rainier-ai-trainium-chips-compute-cluster
- Partner corroboration: Anthropic 在 2026-04-20 公告称其与 Amazon launched Project Rainier，并且 currently use over one million Trainium2 chips to train and serve Claude；该公告没有把全部 chips 或 MW 分配到 New Carlisle。Source: https://www.anthropic.com/news/anthropic-amazon-compute
- Prior announcement context retained: IEDC / Governor 在 2024-04-25 公告 AWS 计划投资 $11B 在 north central Indiana / St. Joseph County 建 data center campus、至少 1,000 jobs、并称 campus 将建在 Indiana Enterprise Center over the next decade；该公告仍是 announced/incentive evidence，不是 construction 或 full buildout evidence。Source: https://iedc.in.gov/events/news/details/2024/04/25/gov.-holcomb-announces-amazon-web-services-plans-to-invest-11b-to-create-a-new-data-center-campus-in-northern-indiana
- Local-government context: St. Joseph County BondLink / IEC project page currently describes the Indiana Enterprise Center east of New Carlisle / west of South Bend and its water, sewer, gas, dark fiber, electric, rail, highway, and airport service context; it links Amazon's 2025 Northern Indiana announcement but does not publish a building-level completion or MW-capacity record. Source: https://www.sjcindianabonds.com/st-joseph-county-indiana-in/about/project/i7824?projectId=69154
- capacity_mw: 保持 `null`。原因：官方来源核实了 investment、operating-source permits、Project Rainier operational use、chip count and broader Northern Indiana expansion, but no official MW figure specific to this New Carlisle campus was located. Amazon's 2025-11-24 "2.4 gigawatts" statement refers to additional Northern Indiana campuses/region, not a campus-specific MW field for USDC-0024. Source: https://www.aboutamazon.com/news/company-news/amazon-15-billion-indiana-data-centers
- 冲突/限制：第三方 trackers publish proposed/operational/2.2GW/250+MW/910MW/1,092MW-style estimates, but these conflict and are not used as authoritative capacity because they are not official/local-government records and lack a directly verified campus-specific source.
- verified: true for the updated owner/status/action facts; verified: false for any MW capacity or full-campus buildout conclusion because no public CO, energization, load-service, or building-by-building completion record was found.
