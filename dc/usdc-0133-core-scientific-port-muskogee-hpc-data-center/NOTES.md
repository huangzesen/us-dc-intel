# USDC-0133 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Under construction with an active expansion reported; Phase 1 delivery was targeted for 2026 and a second 82
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 从 under construction 更新为 `partial live / site work-construction`。依据：Core Scientific 2026-07-28 Form 10-Q 称 Polaris 交易会新增约 40 acres adjacent to the company's existing data center operating in Muskogee；但未找到 City/utility CO、inspection、energization record，因此不升为 full buildout。来源：https://investors.corescientific.com/sec-filings/all-sec-filings/content/0001839341-26-000014/core-20260630.htm
- capacity_mw 从 null 更新为 100（Muskogee 1 gross facility power）。同一项目的约 70 MW critical IT load、138,000 sf、65 acres 也写入 capacity_context。来源：https://investors.corescientific.com/news-events/press-releases/detail/99/core-scientific-and-port-muskogee-break-ground-on-100-mw-hpc-data-center 和 https://corescientific.com/high-density-data-centers/muskogee-ok/
- owner 从 null 更新为 Core Scientific Inc. / Core Scientific Muskogee operations；CoreWeave 作为首栋约 70 MW critical IT load 的客户/承租方保留在 owner/context。来源：https://investors.corescientific.com/news-events/press-releases/detail/99/core-scientific-and-port-muskogee-break-ground-on-100-mw-hpc-data-center
- 添加 local-government 过程证据：City of Muskogee 2025-09-08 minutes 记载 Council rescinded Ordinance No. 4266-A，并通过 Resolution No. 3052 重启 John T. Griffin Industrial Park II annexation，涉及 Port Authority、OG&E、Core Scientific、Polaris parcels，表决分别为 7-1 与 6-2。来源：https://public.destinyhosted.com/muskodocs/2025/CCNCL/20251027_4795/16462_09-08-2025_spccmin.pdf
- 添加 2025-09-25 annexation/service-plan materials：agenda/service-plan 标识 Core Scientific 与 Polaris/OG&E/Port Authority parcels，并说明 undeveloped property 在取得 building permit 前需符合 City subdivision regulations。未找到最终签署 ordinance/minutes 或 building permit。来源：https://public.destinyhosted.com/muskodocs/2025/SPEC/20250925_4885/AGENDApacket__09-25-25_0211_4881.pdf
- 更新 2026-05-06 expansion 事实为官方/company-first：Core Scientific 与 Port Muskogee 均称 campus 目标为约 1.5 GW gross / 1.0 GW leasable；Polaris DS LLC 交易包含 440 MW gross power under OG&E energy agreement；第二栋 82.5 MW unleased building 已开工、Q4 2027 initial delivery；current leased 70 MW building 正在 final testing/commissioning，目标 Q2 2026 delivery。来源：https://investors.corescientific.com/news-events/press-releases/detail/135/core-scientific-plans-expansion-to-1-5-gigawatts-of-gross-power-at-muskogee-oklahoma-campus 和 https://www.portmuskogee.com/core-scientific-announces-expansion-in-muskogee-with-acquisition-of-polaris/
- 记录 AMD lease caveat：2026-07-27 AMD leases 覆盖 Pecos, Muskogee, Hunt County 合计 377 MW critical IT capacity，但未披露 Muskogee site allocation，因此未计入 Muskogee capacity_mw。来源：https://investors.corescientific.com/sec-filings/all-sec-filings/content/0001839341-26-000014/core-20260630.htm
- 冲突/不足：公司 May 2026 release 仍称首栋 final testing/commissioning，July 2026 10-Q 称 Muskogee data center operating；无 local CO/energization。容量方面，100 MW/70 MW 是首栋事实，1.5 GW/1.0 GW、440 MW、82.5 MW 与 AMD aggregate lease 均为 expansion/future/portfolio context。
