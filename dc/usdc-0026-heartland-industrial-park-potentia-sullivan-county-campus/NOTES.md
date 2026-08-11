# USDC-0026 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: no status
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status: `null` -> `site work-construction`。依据：Heartland Industrial Park LLC 的 Project Nova tree-clearing 与 Phase 1 Construction Stormwater General Permit NOI public notices，以及 Potentia 2026-04-23 宣布 Heartland Industrial Park 已开始施工；尚未找到县官网发布的会议包/纪要、建筑许可、CO、并网/energization 或 live-service 记录。来源：
  - https://marketplace.tribstar.com/default/notices-legals/heartland-industrial-park-llc-/AC1E05740560a00676QqXFBACDEE
  - https://marketplace.tribstar.com/terre-haute-in/public-notices/heartland-industrial-park-llc-/AC1E032409dea017140nJ3766E92
  - https://www.businesswire.com/news/home/20260423900539/en/Potentia-Begins-Construction-on-Major-Infrastructure-Development-at-Heartland-Industrial-Park-in-Sullivan-County-Indiana
- location 补强为 Sullivan area / Sullivan County / IN；公开描述为 Sullivan 西南、U.S. Route 41 沿线、近 Merom Generating Station；NOI public notices 将地块定位到 Township 7 North, Range 10 West, Sections 10-15。未确认 civic street address。来源：
  - https://www.ipm.org/news/2026-04-01/65-billion-industrial-park-coming-to-sullivan-county
  - https://www.insideindianabusiness.com/articles/potentia-leader-details-timeline-investment-for-65b-industrial-park-in-sullivan-county
  - https://marketplace.tribstar.com/terre-haute-in/public-notices/heartland-industrial-park-llc-/AC1E032409dea017140nJ3766E92
- owner: `null` -> `Potentia Inc. / Heartland Industrial Park LLC (developer/project entity; anchor tenant not publicly disclosed)`。Potentia 自称开发方；NOI public notices 的 permittee/project entity 为 Heartland Industrial Park LLC。首栋 tenant 据 Inside INdiana Business 为未披露的数据中心运营商。来源：
  - https://potentia.inc/news/heartland-local-support/
  - https://www.businesswire.com/news/home/20260423900539/en/Potentia-Begins-Construction-on-Major-Infrastructure-Development-at-Heartland-Industrial-Park-in-Sullivan-County-Indiana
  - https://www.insideindianabusiness.com/articles/potentia-leader-details-timeline-investment-for-65b-industrial-park-in-sullivan-county
- capacity_mw: 保持 `null`。未找到公开 IT/load MW；Potentia 的 “gigawatt-scale” 与 $65B phased tenant/partner investment 不能等同于数据中心容量 MW。来源：
  - https://www.businesswire.com/news/home/20260423900539/en/Potentia-Begins-Construction-on-Major-Infrastructure-Development-at-Heartland-Industrial-Park-in-Sullivan-County-Indiana
  - https://sullivanenergydata.com/data-centers/heartland-industrial-park/
- county agreements: 地方媒体/区域媒体报道 Sullivan County Commissioners 在 2026-03-30 左右签署 road-use agreement 与 community-enhancement agreement；Inside INdiana Business 链接了第三方取得的 agreement PDF，并概述 CR 200 South、CR 400 West、施工时段、噪声、排水、$250k inspection payment、$500k/mile surety bond、$50M infrastructure、$4.5M charities、15 acres fire-station land donation 等条款。县官网可访问搜索未定位到官方托管会议包/纪要。来源：
  - https://www.wvut.org/2026/03/31/major-industrial-park-project-moves-ahead-in-sullivan-county/
  - https://www.insideindianabusiness.com/articles/road-funding-agreements-detailed-for-65-billion-sullivan-county-project
- 冲突/时间线：Indiana Public Media 2026-04-01 报道 construction date not announced；后续 Potentia 2026-04-23 宣布施工开始，Inside INdiana Business 2026-05-04 报道 Phase 1 construction underway，故以较新的 construction/site-work 证据覆盖 4/1 的尚未公布施工日期。completion timing 仍为 projection：Potentia local-support page 称 Phase 1 scheduled for 2027，IIB 采访称 first building by end-2026、second building early/mid-2027，二者均不当作 completion/CO/service 证据。来源：
  - https://www.ipm.org/news/2026-04-01/65-billion-industrial-park-coming-to-sullivan-county
  - https://potentia.inc/news/heartland-local-support/
  - https://www.insideindianabusiness.com/articles/potentia-leader-details-timeline-investment-for-65b-industrial-park-in-sullivan-county
- 证据不足/待核实：未找到 IURC cause number、IEDC project award、anchor tenant identity、prime contractor、actual MW, power-supply/interconnection document, county building permit, CO/inspection, energization/commissioning, or live-service evidence。Sullivan Energy Data 也记录截至其 2026-04-24 review 未确认 IURC cause、IEDC award 或 anchor tenant。来源：
  - https://sullivanenergydata.com/data-centers/heartland-industrial-park/
  - https://sullivanenergydata.com/reading-the-fine-print-on-the-heartland-industrial-park-deal/
