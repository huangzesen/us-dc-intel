# USDC-0162 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Candidate is supported by company/SEC material and a Texas Comptroller registry row under the Cedarvale/Barstow-Pyote name; that registry's exemption ended 2026-03-15
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status/capacity: 从 `candidate / capacity unknown` 更新为 `energized / 234 MW current energized capacity`。Ionic 2026-06-29 S-1 披露 Ward County property as of 2026-03-31 为 self-owned, recently constructed, fully energized facility powered by 234 MW；Nscale 的 AI 服务交付仍描述为从 2026 Q3 分阶段开始，因此不标为 full buildout。来源：https://www.sec.gov/Archives/edgar/data/2007691/000118518526002704/ionicdigis1061026.htm
- state registration: Texas Comptroller current list 在 `Registered Qualifying Large Data Center Projects` 下新增/当前列示 `Cedarvale, Barslow/Pyote TX Data Center`，effective date 2026-03-16，owner 为 Ionic Digital Cedarvale LLC (`LD449964-OW1`)，occupant 为 Nscale Ward County Borrower SPV, LLC (`LD449964-OC1`)，operator 包含 Nscale Ward County, LLC 与 Ionic Digital Mining, LLC (`LD449964-OP1`, `LD449964-OP2`)。这解释了 baseline 中 2026-03-15 结束的旧 qualified data-center row 后续状态。来源：https://comptroller.texas.gov/taxes/data-centers/data-center-lists.php
- lease/parties: SEC-filed lease agreement effective 2025-10-14、amended 2026-02-27，landlord 为 Ionic Digital Cedarvale LLC，tenant 为 Nscale Ward County LLC；Exhibit A 将 premises 描述为 Ward County Section 229, Block 34, H. & T.C. RR. Co. Survey, Abstract No. 292 中 50.079 acres，且 leased premises 不包括 substation land。来源：https://www.sec.gov/Archives/edgar/data/2007691/000118518526002704/ionicdigiex10-16.htm
- company announcements: Ionic 2025-10-14/2025-10-15 press release 称 Nscale lease Cedarvale facility in Barstow, Texas 的 full 234 MW capacity，10-year triple-net lease，约 $2B contracted revenues。来源：https://ionicdigital.com/press-releases/ionic-digital-secures-transformational-lease-agreement-of-cedarvale-facility-with-nscale/
- customer/offtake: Nscale 2025-10-15 announcement 称将为 Microsoft 在 Texas leased from Ionic Digital 的约 240 MW hyperscale AI campus 交付约 104,000 NVIDIA GB300 GPUs，NVIDIA AI infrastructure services phased delivery from Q3 2026，并称 footprint 计划 over time 扩至 1.2 GW、Microsoft 有 late 2027 起 second phase 700 MW option。来源：https://www.nscale.com/press-releases/nscale-microsoft-2025
- current Nscale site page: Nscale AI Infrastructure 页面列出 Ward County, Texas, United States，描述为 roughly 240MW AI data center in West Texas, developed in partnership with Ionic Digital, with plans to expand to 1.2GW。来源：https://www.nscale.com/ai-infrastructure
- expansion caveat: 234 MW 是本次采用的 verified current capacity；+89 MW、700 MW、1.2 GW 均为 contingent/planned expansion。Ionic S-1 明确 +89 MW subject to regulatory approval，cannot guarantee expansion；700 MW 为 Ionic 对 Ward County property 的目标支持容量；1.2 GW 为 Nscale footprint over-time statement。
- conflict: 精确容量在 Ionic/SEC 中为 234 MW，Nscale 对外页面/公告四舍五入为 roughly 240 MW。data.json 采用 234 MW，保留 conflict note。
- unable to verify: 未找到 Ward County/city local permit、site-plan approval、construction permit 或 utility interconnection record 的公开可核验页面；现有“energized”判断依赖 Texas Comptroller state registration、SEC disclosure/lease、company announcements。
