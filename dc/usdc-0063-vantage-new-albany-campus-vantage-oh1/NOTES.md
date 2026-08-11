# USDC-0063 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: no status
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status: `no status` -> `site work-construction`; capacity: `null` -> `192 MW`.
- 官方/地方政府优先核实：New Albany 当前 project-updates 页列出 Vantage Buildings 1, 2, 3，均为 data center/data building 项目，承包商为 Turner Construction；Building 2 位于 3265 Horizon Court、Building 3 位于 3205 Horizon Court，二者均为 500,107 sf；Building 1 当前页写作 generally located at Jug & Horizon 且为 500,107 sf。来源（访问日 2026-08-11）：https://newalbanyohio.org/community-development/project-updates/
- 官方月报核实：New Albany Community Development 2025-12 commercial construction-status report 列出 Vantage Building 1 位于 3325 Horizon Court、200,107 sf、start date October 2024；Building 2 位于 3265 Horizon Court、500,107 sf、start date January 2025；Building 3 位于 3205 Horizon Court、500,107 sf、start date March 2025。该月报支持 construction/site-work 状态，但未给出 permit number、occupancy 或 energization。来源（报告月 2025-12）：https://newalbanyohio.org/wp-content/uploads/2026/01/CD-2025-12.pdf
- 业主/容量核实：Vantage 官方 OH1 页面称 New Albany, OH campus 位于 70 acres，三座 two-story hyperscale data centers，总计 192 MW（64 MW each）和 1.5M sf；campus address 为 3325 Horizon Court, New Albany, OH 43031；first building slated operational by December 2025，additional phases through 2028。来源（访问日 2026-08-11）：https://vantage-dc.com/data-center-locations/north-america/new-albany-ohio
- 融资/范围补证：Vantage 2025-06-03 公告称 $2.25B construction loan fully funds New Albany campus construction，三座 pre-leased hyperscale data centers，192 MW across 1.5M sf，first facility slated operational by December 2025。来源（公告日 2025-06-03）：https://vantage-dc.com/news/vantage-data-centers-secures-5b-in-incremental-green-loan-financings-to-support-demand-for-north-america-platform/
- 施工方补证：Turner Construction 页面称 Turner has begun work on a $2B project to expand Vantage Data Centers' New Albany campus, with groundbreaking attended by Vantage, Turner, and local organization representatives。来源（访问日 2026-08-11）：https://www.turnerconstruction.com/insights/turner-selected-for-2-billion-expansion-project-for-vantage-data-centers
- 地方批准/法律实体补证：New Albany Council 2024-08-20 minutes 的可检索文本识别 Vantage Data Centers OH11 LLC，并描述 100% real-property-tax exemption agreement；同一来源提到 proposed project would establish up to 3 new data center buildings。来源（会议日 2024-08-20）：https://newalbanyohio.org/wp-content/uploads/2020/03/Council-Minutes-8-20-24.pdf
- 多源冲突：City 当前 project-updates 页将 Building 1 标为 500,107 sf / generally located at Jug & Horizon；City 2025-12 monthly report 将 Building 1 标为 200,107 sf / 3325 Horizon Court。data.json 的 building-level 字段采用 dated monthly report 的 3325 Horizon Court / 200,107 sf，并在 action 中保留当前页差异。
- 无法核实/证据不足：未找到官方 occupancy、energization、partial-live 或 full-buildout 记录；Vantage 的 December 2025 first-facility operational date仍按 projection 处理，不升级为 energized/partial live。未找到可直接下载的 building permit numbers 或 utility interconnection record。
- verified: true for owner, campus scope/capacity, location set, and construction/site-work status; verified: false for occupancy, energization, and realized operational date.
