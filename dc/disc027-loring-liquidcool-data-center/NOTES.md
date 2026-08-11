# disc027 — 更新记录

## 2026-08-11（discovery 并入）
- 由 codex discovery daemon 发现（candidates-secondary-markets.jsonl），人类审批后并入（Jason “开始做吧”, 2026-08-11）。
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 从 “leased; planned conversion at former Loring Air Force Base warehouse” 调整为 “local process; long-term lease signed for Building No. 7230, but financing/permitting/operational start not confirmed”。依据：Loring Development Authority 2025-10-23 board minutes 将 LiquidCool 列为项目议题，并记录许可/透明度/协调框架讨论；未发现施工或投运确认。来源：https://loringcommercecentre.com/wp-content/uploads/2026/06/2025.10.23-LDA_-Board_-Meeting_-Minutes-Final.pdf
- owner/project 补证：Green 4 Maine/Loring Commerce Centre announcement 称 LiquidCool Data Center 已签署长期租赁，并将在 former Loring Air Force Base warehouse 启动 AI data center。来源日期 2025-10-10。来源：https://www.einpresswire.com/article/857649265/green-4-maine-campus-and-innovation-hub-at-loring-welcomes-liquidcool-solutions-launches-maine-s-first-ai-data-center
- location/building 补证：Bangor Daily News 2025-10-14 报道 Green 4 Maine Campus and Innovation Hub 与 LiquidCool 的项目位于 former Loring Air Force Base 的 Building No. 7230，计划使用约 115,000 square feet，初期 5-6 MW。来源：https://www.bangordailynews.com/2025/10/14/aroostook/aroostook-business/ai-data-center-loring-air-force-base/
- capacity_mw 保持 6，作为初期容量；新增 capacity_notes 记录分层容量。The County 2026-03-10 报道称该建筑现有 2 MW 电力，Versant Power will-serve agreement 覆盖额外 24 MW，公司讨论过最高 50 MW 潜力，但融资仍在敲定，投运可能在融资完成后约六个月。来源：https://thecounty.me/2026/03/10/news/maines-proposed-data-center-ban-could-restrict-facility-planned-at-loring/
- regulatory note：Maine LD 307（可能限制 large-scale data center 的 temporary bill）在 2026-04-29 veto sustained，未成为法律；因此未将其视为当前生效限制，但保留为 2026 年监管风险背景。来源：https://legislature.maine.gov/legis/bills/display_ps.asp?LD=307&snum=132
- contradictions：容量口径存在 5-6 MW 初期、2 MW 现有、24 MW will-serve、50 MW 潜力四层；未把 24/50 MW 写入 capacity_mw。2025 年公告/媒体曾预期约六个月内运营，但 2026-03-10 报道仍称融资未最终完成，未发现官方投运确认。
