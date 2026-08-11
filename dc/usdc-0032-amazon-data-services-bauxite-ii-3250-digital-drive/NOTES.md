# USDC-0032 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Maryland issued a final air-quality permit for Amazon's generator plant on March 25, 2026
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新为 `approved-permitted`：MDE 已于 2026-03-25 向 Amazon Data Services, Inc. 签发空气质量 permit-to-construct / final air permit；该证据仍只证明应急发电机空气许可，不证明 building permit、CO、utility interconnection、PSC large-load registration、energized、partial live 或 full buildout。来源：https://news.maryland.gov/mde/2026/03/25/maryland-department-of-environment-approves-air-permit-for-frederick-data-center/；https://mde.maryland.gov/datacenters/Documents/2026_AmazonDataServicesBWIIssuedPTC.pdf
- owner 从 `null` 更新为 `Amazon Data Services, Inc.`；MDE issued permit 首页列出 legal owner 为 Amazon Data Services, Inc.，站点为 BWI-150 through BWI-153 / 3250 Digital Drive / Frederick, MD 21703。来源：https://mde.maryland.gov/datacenters/Documents/2026_AmazonDataServicesBWIIssuedPTC.pdf
- permit 编号补证：MDE issued permit 列出 Control No. B-08076、premises no. 021-0809；此前 data.json 中 permit number 未填。来源：https://mde.maryland.gov/datacenters/Documents/2026_AmazonDataServicesBWIIssuedPTC.pdf
- 备份发电容量补证为 257.75 MW nameplate（92 * 2.75 MW + 6 * 0.75 MW + 1 * 0.25 MW），但 `capacity_mw` 继续保留 `null`，因为没有官方 IT load / utility capacity 证据。来源：https://mde.maryland.gov/datacenters/Documents/2026_AmazonDataServicesBWIIssuedPTC.pdf
- MDE Frederick Data Center Sampling/Reports 页面核实该项目位于 Quantum Maryland / Quantum Frederick campus，Amazon Data Services project 为 3250 Digital Drive 的 four buildings，并链接 2026 Amazon Data Services BWI final air permit 与 determination/response。来源：https://mde.maryland.gov/datacenters/Pages/FrederickDataCenter.aspx
- Frederick County 2026-07-01 policy context 已更新：县方暂停接收/处理新的 Critical Digital Infrastructure facilities 或 substations 申请至 2026-12-31；县页面称暂停不适用于 2025-06-17 前已有 development approvals 的物业，且不停止目前 under construction 的项目；另要求开发审查中提供 Maryland PSC large-load customer registry 注册证明。来源：https://frederickcountymd.gov/9310/Data-Centers；https://frederickcountymd.gov/m/newsflash/Home/Detail/5845
- 多源冲突/口径差异：MDE news release 用 “99 diesel-fired emergency generators”；issued permit 细分为 92 台 2,750-kW 主应急机组、6 台 750-kW、1 台 250-kW，合计仍为 99 台，因此不是实质冲突。行业媒体常把约 258 MW 当作项目 capacity；本次按官方口径记录为 backup-generation nameplate，不写入 `capacity_mw`。
- 无法核实/证据不足：未找到官方可访问记录证明 building permit 编号、certificate of occupancy、PSC large-load registry 条目、utility interconnection、实际开工/施工进度、energized IT load、tenant service live date 或 full buildout。
