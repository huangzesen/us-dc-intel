# USDC-0015 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Company-reported under construction; no project-specific public energization, completion, or accessible building-permit record was located
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 调整：从 baseline 的 “Company-reported under construction” 改为 “Announced / company-listed development”。原因：本轮只核实到 STACK 官方公告/设施页/宣传册中的 development / will deliver 语言，未找到项目级官方施工许可、开工、并网、投运或完工记录。
  - STACK 2025-03-25 公告：36MW, Elk Grove Village, two-story 263,000 sq. ft., powered by local ComEd substation；未附 municipal approval / permit。https://www.stackinfra.com/about/news-press/press-releases/stack-infrastructure-announces-new-36mw-data-center-in-chicago/
  - STACK CHI02 当前设施页：CHI02 in Elk Grove Village will deliver 36MW on 18 acres。https://www.stackinfra.com/locations/americas/chicago/chi02/
  - STACK CHI02 brochure（2025-03 PDF）：36MW capacity, 18 acres, 263,620 sq. ft., shell or turnkey deployment options。https://www.stackinfra.com/wp-content/uploads/2025/03/CHI02-Brochure.pdf
- capacity_mw 从 null 更新为 36；owner 从 null 更新为 STACK Infrastructure。来源为 STACK 官方 2025-03-25 公告和当前 CHI02 页面。
- location 增补 address: 1830 Jarvis Ave，并标注 caveat：该街址来自 DataCenterMap/MLQ 等第三方设施/permit-tracker 页面；STACK 官方页面仅确认 Elk Grove Village，未发布街址。
  - DataCenterMap（2026-08-11 抓取）：listed as Planned, 1830 Jarvis Ave, 36MW, 263,000 sq. ft. https://www.datacentermap.com/usa/illinois/chicago/stack-infrastructure-chi02/
  - MLQ permit-tracker result（2026-08-11 搜索结果）：EGV-STACK-CHI02, 1830 Jarvis Ave；未作为官方许可证据使用。https://mlq.ai/permit-filings/usa/illinois/elk-grove-village/egv-stack-chi02/
- 官方/地方政府检查：Cook County Open Data permit dataset 搜索 STACK CHI02、EGV-STACK-CHI02、1830 Jarvis，以及 2025-2026 Elk Grove Village data-center permits，未返回 STACK CHI02 项目级 permit；返回的 data-center permit 记录属于 EdgeConneX、Stream、Aligned、Prime、Elk Grove Data Center 等其他项目。该 negative evidence 不能证明所有 Village 系统均无许可，只支持 “no accessible public project-specific permit located”。
  - Cook County Open Data permit query: https://datacatalog.cookcountyil.gov/resource/6yjf-dfxs.json?$limit=100&$where=municipality=%27VILLAGE%20OF%20ELK%20GROVE%20VILLAGE%27%20and%20year%20in(%272026%27,%272025.0%27,%272025%27)%20and%20upper(work_description)%20like%20%27%25DATA%25%27
  - Village 2026-05-20 data-center town-hall notice retained as general local context, not a CHI02 action/approval。https://www.elkgrove.org/Home/Components/Calendar/Event/9496/
- 行业媒体交叉检查：DCD 2025-03-26 报道同样描述为 announced/planned 36MW Elk Grove Village project，地址未由 STACK 披露，development timeline 未分享。https://www.datacenterdynamics.com/en/news/stack-announces-36mw-data-center-in-chicago-illinois/
- 多源冲突：baseline “under construction” 与本轮官方/industry evidence 的 announced/planned/development wording 冲突；本轮未找到足以支持 construction / energized / operational 的公开证据。
