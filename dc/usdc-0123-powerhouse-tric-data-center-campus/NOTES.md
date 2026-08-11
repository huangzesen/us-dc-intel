# USDC-0123 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: State-published material describes a PowerHouse TRIC shell campus, while the reviewed Storey County and utility search surfaces did not yield a project-specific permit, construction record, service da
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：从“state-published shell campus; active shell-construction language remains source-limited”更新为 `site work-construction`。PowerHouse 当前 Reno 项目页列出 Construction/Delivery 为 Q3 2024-Q2 2026、Power Delivery 为 Q4 2025、Delivery 为 April 2026；PowerHouse/DCD groundbreaking 页面称已在 Storey County 的 TRIC 开工并启动三栋楼中的第一栋。来源：https://www.powerhousedata.com/data-center/powerhouse-reno ；https://www.powerhousedata.com/news/powerhouse-breaks-ground-on-reno-data-center
- official/local-gov 补证：Storey County 2026-27 Secured Assessment Roll（roll date 2025-12-23）列出 POWERHOUSE RENO BRITAIN LLC 持有/计入 parcel 005-041-66 与 005-041-67，均显示 land value、building value 为 0。该证据支持业主/地块识别，不等同于 permit、CO 或 energization。来源：https://www.storeycounty.org/DocumentCenter/View/22761
- owner 更新：developer/operator 记录为 PowerHouse Data Centers；parent 记录为 American Real Estate Partners (AREP)；JV partner 记录为 Harrison Street；assessed owner 记录为 POWERHOUSE RENO BRITAIN LLC。来源：https://www.prnewswire.com/news-releases/powerhouse-data-centers-closes-on-nevada-site-for-powerhouse-reno-302039882.html ；https://www.storeycounty.org/DocumentCenter/View/22761
- capacity 更新：`capacity_mw` 采用当前 PowerHouse Reno 项目页的 200 MW。保留 capacity_history：2024-01-19 company release 为 “more than 65 MW bridging power”；groundbreaking coverage 为 65 MW campus；NAIOP/GBI case study 为 65 MW bridging power/Q1 2026 与 300 MW permanent power total；当前 PowerHouse 项目页为 200 MW。来源：https://www.powerhousedata.com/data-center/powerhouse-reno ；https://www.prnewswire.com/news-releases/powerhouse-data-centers-closes-on-nevada-site-for-powerhouse-reno-302039882.html ；https://www.credaglobal.org/research-and-publications/magazine/2024/Winter-2024-2025/development-ownership/pioneering-sustainable-design-for-data-centers
- conflict：公开来源对 capacity 存在未消解差异（65 MW bridging/campus、300 MW permanent total、200 MW current project-page value）。本次以当前 developer project page 的 200 MW 作为主值，并在 `contradictions` 与 `capacity_history` 保留其他数值。
- 仍无法核实：未在已审查的 Storey County permitting/building pages、ONE Accela public search surface、NV Energy public surfaces中找到 project-specific Storey County permit number、certificate of occupancy、utility first-service date 或 energization record。来源：https://www.storeycounty.org/685/Building-Permits ；https://aca-prod.accela.com/ONE/Cap/CapHome.aspx?TabName=Home&module=Building ；https://www.nvenergy.com/
- verified: false。核心 developer/parcel/source facts 已验证；permit/CO/energization 仍缺少公开可核验的一手记录，且 capacity_mw 存在多源冲突。
