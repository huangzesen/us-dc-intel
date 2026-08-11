# USDC-0130 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Provisional planning lead only; no primary government, utility, or developer record was located
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：从 “Provisional planning lead only” 更新为 `site work-construction`。Meta 官方于 2026-04-21 宣布 Tulsa Data Center 开工，项目投资超过 $1B，本地基础设施投入超过 $25M，峰值施工工人超过 1,000，运营岗位约 100；Meta 还称 Tulsa facility 用电将由新增清洁能源匹配，Oklahoma 已签约项目超过 1,500 MW。来源：https://datacenters.atmeta.com/2026/04/hello-tulsa/
- owner/identity 更新：owner 从 null 更新为 `Meta Platforms, Inc. (publicly announced operator/developer); local Project Anthem agreements and utility records use Atmoss, LLC`。Tulsa City Council 2024-05-01 议程页把 Project Anthem data center 与 City of Tulsa、Tulsa Authority for Economic Opportunity、Atmoss, LLC 的 conditional development and financing agreement 关联；Meta/PartnerTulsa 2026-04-21 公告确认 Meta Tulsa Data Center。来源：https://www.cityoftulsa.org/apps/CouncilDocuments?item=46254 ；https://partnertulsa.org/meta-breaks-ground-on-new-1-billion-data-center-in-tulsa/
- location 更新：county 从 Tulsa 改为 Wagoner；保留 city=Tulsa，并增加地址/位置描述 `21304 E 11th St, Catoosa, OK 74015`、`West of the Creek Turnpike between East 11th Street South and East 21st Street South`、acreage=339.11。TMAPC substation staff report列出 Project Anthem full site 约 339.11 acres，位置在 Creek Turnpike 与 East 11th Street South 西南；2026-05-20 TMAPC minutes列出 Project Anthem 位于 Creek Turnpike 以西、East 11th Street South 与 East 21st Street South 之间。来源：https://tulsaplanning.org/tmapc/agendas/exhibits/Project%20Anthem%20%28PSO%20Substation%29.pdf ；https://tulsaplanning.org/tmapc/agendas/exhibits/2026-05-20-TMAPC-Minutes.pdf
- milestones/actions 更新：新增 2024-05-01 tax exemption/development agreement、2025-03-05 PSO substation accelerated permit-release staff report、2026-04-21 Meta/PartnerTulsa groundbreaking、2026-05-20 preliminary plat extension and accelerated building permit release、2026-07-22 TMUA revised will-serve letter。2026-05-20 TMAPC vote 为 6-0-0，批准 Project Anthem preliminary subdivision plat extension to 2027-08-07，并批准 accelerated release of a building permit。来源：https://tulsaplanning.org/tmapc/agendas/exhibits/2026-05-20-TMAPC-Minutes.pdf
- utility/service 更新：TMUA 2026-07-22 agenda 记录 revised Will Serve Letter between City of Tulsa and Atmoss, LLC，将 peak water usage 从 2.75 MGD 增至 5.7 MGD，将 wastewater flow 从 500,000 gpd 增至 1,950,000 gpd，并包括 additional 16-inch water main 与 Lower Bird Creek WWTP Supplemental Carbon Treatment Improvements。来源：https://www.cityoftulsa.org/apps/COTDisplayDocument/?DocumentIdentifiers=32469&DocumentType=Agenda
- capacity_mw：保持 null。未在 Meta 官方公告、Tulsa planning/council/TMUA primary records 中找到可核实 MW 容量；未采用 trade/tracker MW 数字。
- 冲突/注意：旧 county=Tulsa 与官方规划/税收实体语境中的 Wagoner County 不一致，本次改为 Wagoner；Project Anthem 一期/二期媒体报道有 acreage 差异，本次仅采用官方 TMAPC/Meta/PartnerTulsa 可核实面积与规模；二期撤回/扩展报道未写入主状态，因为本条目录记录的是已开工的 Meta Tulsa Data Center / Project Anthem 主体。
- verified: true（status/owner/location/service facts 均有官方或本地政府来源；MW capacity 因无官方证据保留 null）。
