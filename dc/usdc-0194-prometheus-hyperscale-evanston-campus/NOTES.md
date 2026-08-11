# USDC-0194 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Wyoming Business Council material describes a planned 1
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：由 planning/state-program evidence 更新为 approved-permitted。Uinta County 的 Approved Conditional Use Permits 页面说明 CUP 需 Planning Commission 与 Board of County Commissioners 审批，并列出 2026 approved CUP 文档；县方 CUP-26-01 PDF 搜索索引显示 `Prometheus Wyoming I LLC`、`Conditional Use Permit`、`CUP 26-01`，并指向 2026-06-16 County Commission hearing/decision。来源：https://uintacountywy.gov/964/Conditional-Use-Permits；https://www.uintacountywy.gov/DocumentCenter/View/9751/CUP-26-01
- 2026-06-17 Prometheus Hyperscale 公告称，Uinta County Board of Commissioners 于 2026-06-16 unanimous approval 该 Evanston campus CUP；项目为约 506-acre site，initial capacity 1.25 GW，development path to 5 GW，islanded/on-site power；construction anticipated within six months of final permitting。来源：https://www.prometheushyperscale.com/news/prometheus-hyperscale-secures-unanimous-conditional-use-permit-approval-from-uinta-county-commissioners
- 2026-06-18 WyoFile/Uinta County Herald 报道称，Uinta County Commission 批准 Prometheus east of Evanston data center CUP，并列出 15 条条件：五年内开始施工并通知县方、满足 Wyoming Industrial Siting Act/DEQ/EPA 等适用许可、年度县方检查、年度现场用水报告、道路/桥涵维护、DarkSky lighting、噪声/排放等要求。来源：https://wyofile.com/uinta-county-data-center-moves-forward/
- 2026-05-28 Cowboy State Daily 报道称，Uinta County Planning and Zoning Commission 于 2026-05-27 unanimous recommendation zoning/CUP approvals；项目位置描述为 Township 15 North, Range 118 West, Section 13，I-80 exit 13 附近，约 500 acres，initial campus 1.25 GW，five phases，off-grid/on-site power。来源：https://cowboystatedaily.com/2026/05/28/uinta-county-planners-give-unanimous-ok-to-1-25-gigawatt-prometheus-data-center/
- 2026-05-26 City of Evanston hosted flyer noticed a public community conversation for Build Wyoming's Prometheus Hyperscale project in Uinta County at The Roundhouse, describing a next-generation liquid-cooled AI computing campus coming to Wyoming。来源：https://evanstonwy.org/DocumentCenter/View/6171/Uinta-Community-May-26-Meeting-flyer
- Capacity/owner/location 更新：capacity_mw 从 null 更新为 1250；owner 从 null 更新为 `Prometheus Wyoming I LLC / Prometheus Hyperscale`；location 增加 506 acres、Township 15 North, Range 118 West, Section 13 / I-80 exit 13 附近描述。来源同上。
- 冲突/限制：无发现互相否定的来源；但容量表述存在 1.2 GW（WBC/PureWest-era materials）与 1.25 GW/1.25GW+（2026 company/local-government-process materials）差异，本次采用较新的 2026 CUP/公司口径 1.25 GW。未核实到 building/grading/air/industrial-siting final permit issuance、construction start、inspection/CO、energization 或完整 parcel/GIS geometry；因此不提升为 site work-construction。
