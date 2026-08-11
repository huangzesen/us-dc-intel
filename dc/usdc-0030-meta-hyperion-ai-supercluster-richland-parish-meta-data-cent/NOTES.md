# USDC-0030 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Under construction with a major announced expansion
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：保持为 `site work-construction`，但补充 July 13, 2026 官方扩建事实。LED 宣布 Meta 对 Richland Parish Data Center 的承诺增至 $50B+，计划扩至 nearly 10 million sq ft 与 5 GW IT capacity；Meta 同日确认 Richland Parish AI-optimized data center 扩至 5 GW compute capacity，并称其为 Meta fleet 最大项目、Hyperion 最大 multi-gigawatt AI training cluster。来源：
  - https://www.opportunitylouisiana.gov/news/meta-commits-more-than-50-billion-for-north-louisiana-project-becoming-one-of-the-largest-data-centers-in-history
  - https://datacenters.atmeta.com/2026/07/deepening-our-investment-in-richland-parish-louisiana/
- capacity_mw 从 `null` 更新为 `5000`。该值来自 LED 的 "5 gigawatts of IT capacity" 与 Meta 的 "5 GW in compute capacity"；仍为 announced/planned buildout capacity，不代表 energized IT load。来源：
  - https://www.opportunitylouisiana.gov/data-center/meta
  - https://datacenters.atmeta.com/richland-parish-data-center/
- owner 从 `null` 更新为 `Meta Platforms, Inc.; utility docket materials identify Laidley LLC and Evest LLC as Meta-related project/customer entities in Richland Parish.` LPSC Order U-37425 identifies the data center as being developed by Meta Platforms through Laidley LLC; later LPSC application materials describe Evest LLC as a Meta subsidiary seeking an adjacent large hyperscale data center in Richland Parish. 来源：
  - https://lpscpubvalence.lpsc.louisiana.gov/portal/PSC/ViewFile?fileId=nDWn%2Fjuc2+A%3D
  - https://lpscpubvalence.lpsc.louisiana.gov/portal/PSC/ViewFile?fileId=PApWhMLmYIc%3D
- utility / grid context 更新：Entergy's March 27, 2026 announcement says an additional agreement with Meta, combined with prior agreements, is expected to deliver about $2.65B in customer benefits and supports a project with potential to scale up to 5 GW. This is utility/customer evidence only, not local land-use approval or operational proof. 来源：
  - https://www.entergy.com/entergy-louisiana-announces-a-new-agreement-with-meta-that-will-deliver-an-additional-2b-in-customer-savings
- local/official construction context: Meta states it has contracted more than $1.6B with Louisiana businesses since breaking ground; the Richland Parish Data Center project site states the project is being built for Meta by Mortenson, Turner Construction Company and DPR Construction. This supports under-construction classification but still does not provide a parish permit number or certificate of occupancy. 来源：
  - https://datacenters.atmeta.com/2026/07/deepening-our-investment-in-richland-parish-louisiana/
  - https://www.richlandparishdatacenter.com/
- 冲突/需后续核实：
  - planned scale: LED July 13, 2026 says nearly 10M sq ft / 5 GW, while richlandparishdatacenter.com still says 4M sq ft. Treat 5 GW / nearly 10M sq ft as current official announced planned scale; retain 4M sq ft as stale or initial-phase public site language until reconciled.
  - entity treatment: LPSC materials distinguish Laidley LLC and adjacent Evest LLC, while Meta/LED public communications present the expansion as one Meta Richland Parish/Hyperion campus. This record tracks one Meta Richland Parish/Hyperion campus and preserves the entity distinction.
  - no accessible parish building permit, site-plan approval, certificate of occupancy, or energized-load evidence located in this refresh.
