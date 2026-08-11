# USDC-0054 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Applied Digital's Ellendale HPC expansion is supported by official North Dakota inspection and utility/environmental records
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：从“官方记录支持建设/许可流程，未定容量”更新为 `partial live`。Applied Digital 2026-07-01 公告称 Polaris Forge 1 的 Building 2 Phase 1 达到 Ready for Service，新增 75 MW operational AI capacity，使园区 live capacity 达 175 MW；2026-07-27 财报稿进一步称首个 100 MW building 于 2025-10 operational，Building 2 Phase 1 于 2026-06-30 delivered，其他 Polaris Forge 1 buildings 仍处于不同建设阶段。来源：https://ir.applieddigital.com/news-events/press-releases/detail/157/applied-digital-delivers-second-building-at-polaris-forge-1；https://ir.applieddigital.com/news-events/press-releases/detail/159/applied-digital-reports-fiscal-fourth-quarter-and-full-year
- capacity_mw 从 null 更新为 175；同时新增 capacity_context，保留 400 MW contracted/full-buildout 作为 owner-reported planned/contracted figure，而非政府核发容量。来源：https://ir.applieddigital.com/news-events/press-releases/detail/157/applied-digital-delivers-second-building-at-polaris-forge-1
- owner 从 null 更新为 Applied Digital Corporation。NDDEQ draft Permit to Construct lists Applied Digital Corporation as permittee for ELN Generation Plant at 9663 87th Ave. SE, Ellendale, Dickey County, with backup diesel generation for computer processing/data preparation services. 来源：https://deq.nd.gov/aq/Notices/AppliedDigital/DRAFT_ACP18338v1_0.pdf
- 补入地方政府证据：Dickey County 2025-03-04 minutes 记录 Applied Digital 代表称已有 ten operational buildings、一个 380,000-square-foot building under construction，并已开始两个 900,000-square-foot buildings 的 dirt work；2026-04-07 minutes 记录夏季将新增 400-600 employees，并提到 Pheasant Lake 附近 workforce housing。来源：https://dickeynd.com/ufile/f1/Commission-Minutes/2025/March.pdf；https://dickeynd.com/ufile/minutes/4-april-29b796.pdf
- PSC man-camp utility case 更新：PU-26-173 case page 显示 2026-07-27 Commission Motion to Adopt the Order 和 Order；该案仍仅作为 Applied Digital man camp electric service 证据，不升级为 data-center building energization。来源：https://apps.psc.nd.gov/cases/pscasedetail?getId=26&getId2=173；https://www.psc.nd.gov/webdocs/case/26-0173/006-010.pdf
- 冲突/表述 caveat：DCD 2026-07-02 标题称 completed second building，但正文与 Applied Digital primary release 均限定为 Building 2 Phase 1 / 75 MW / total live capacity 175 MW；本次不认定 Building 2 全 150 MW 已完整投运。来源：https://www.datacenterdynamics.com/en/news/applied-digital-completes-second-building-at-north-dakota-data-center-campus/
- 未核实项：未找到独立 government CO、data-center energization register、building-by-building commissioning register；因此 live capacity 采用 owner-reported，并在 evidence_grade 中降级说明。
