# USDC-0129 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: no status
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status: `no status` -> `site work-construction`; capacity: `null` -> reported/planned `1000 MW` cluster scale; owner: `null` -> `Meta`.
- 官方/地方政府优先核实：New Albany 当前 project-updates 页列出多个 Meta 新 data center / data building 项目，分布在 1500 Beech Rd.、13385 Green Chapel Rd. 与 Clover Valley Rd.，包括 Meta LCO 2、NLH/NAB/NAH 系列建筑；已列出面积合计约 2,364,061 sf（不含 Meta NAH9，当前页未给面积）。该页支持 construction/site-work 状态，但不发布 permit number、occupancy、energization 或 MW。来源（访问日 2026-08-11）：https://newalbanyohio.org/community-development/project-updates/
- 官方月报补证：New Albany Community Development 2025-12 construction-status report 列出 Meta LCO 3、NLH9S、NLH1、NLH2、NLH3、NLH5、NLH100、NLH6、NAB1、NAB2、NAB9、NAB3、NAB5、NAB100、NAH9 等 2025 start dates，并列出 Meta LCO DCB1 partial occupancy expiration date 为 2026-03-29。来源（报告月 2025-12）：https://newalbanyohio.org/wp-content/uploads/2026/01/CD-2025-12.pdf
- 地方政府能源/定位核实：New Albany 2026-01 statement 称 Meta 的 New Albany data center 将从 regional electric grid 取电、Meta 支付其用电全额成本，并将 Meta 的核能协议与 New Albany International Business Park 的 Prometheus supercluster 关联；同页称 New Albany 没有核电厂建设计划。来源（2026-01）：https://newalbanyohio.org/news/2026/01/statement-regarding-metas-nuclear-energy-projects/
- 业主/公司核实：Meta 2026-01-22 公告称其核能项目将向支持 Meta operations 的电网供电，包括 New Albany, Ohio 的 Prometheus supercluster；Meta New Albany campus 页面称 Meta 自 2017 年在 New Albany data center 破土以来已在 Ohio data centers 投资 $1.5B+，支持 300+ operational jobs，峰值 1,200 skilled trade workers。来源（公告日 2026-01-22）：https://about.fb.com/news/2026/01/meta-nuclear-energy-projects-power-american-ai-leadership/；来源（访问日 2026-08-11）：https://datacenters.atmeta.com/ohio-new-albany/
- 容量/时间口径：Zuckerberg 2025-07-14 Threads post（本次直接打开 Threads 遇到 429 rate limit；采用 DCD 与 Business Insider 对原帖的引述）称 Meta 正在建设多个 multi-GW clusters，第一个名为 Prometheus、预计 2026 online，并引用 SemiAnalysis 的 1 GW-plus supercluster 口径。因此 data.json 将 `capacity_mw` 记为 `1000`，但标注为 reported/planned cluster scale，非已并网或已投产负荷。来源（报道日 2025-07-14/15）：https://www.datacenterdynamics.com/en/news/meta-to-invest-hundreds-of-billions-of-dollars-into-compute-to-build-superintelligence-with-several-multi-gw-data-center-clusters/；https://www.businessinsider.com/meta-mark-zuckerberg-building-ai-data-centers-tents-catch-up-2025-7；原帖 URL：https://www.threads.com/@zuck/post/DMF6tngx-dC/semianalysis-just-reported-that-meta-is-on-track-to-be-the-first-lab-to-bring-a-
- 多源冲突：未发现核心冲突。注意 City 当前 project-updates 页可证明多个 Meta building records 和 site-work/construction，但不直接把每栋楼命名为 Prometheus；Prometheus 关联来自 New Albany energy statement、Meta energy announcement 与 Zuckerberg/SemiAnalysis coverage。
- 无法核实/证据不足：未找到官方 building permit numbers、utility interconnection records、metered load、energization、partial-live 或 full-buildout 证明。2026 online 与 1 GW-plus 均按 reported/planned 处理，不升级为 energized / partial live。
- verified: true for owner, New Albany location, Prometheus-New Albany linkage, and construction/site-work status; verified: false for live operational status, full energization, and realized MW.
