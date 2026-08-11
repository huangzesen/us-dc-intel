# USDC-0183 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Utah government inventory lists Pole Canyon and Pony Express as proposed; possible overlap with Tract Tripletail land/development records is unresolved
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新为 local process / proposed：2026-05-26 Utah government inventory 仍列 Tract Pole Canyon（Eagle Mountain, Utah Co.）1,700 MW、PROPOSED，Tract Pony Express（Eagle Mountain area, Utah Co.）120 MW、PROPOSED。来源：https://www.utah.gov/pmn/files/1444799.pdf
- capacity_mw 从 null 更新为 1,820 MW（Pole Canyon 1,700 MW + Pony Express 120 MW）。Tract 当前项目页列 Pole Canyon 为 Owned & In Development、844 acres、1,700 MW、18 parcels、Industrial Zoning / By-Right Data Center；Pony Express 为 Owned & In Development、225 acres、120 MW、Within the Eagle Mountain RTI overlay zone、bordered by 345kV transmission lines、4 parcels。来源（访问日 2026-08-11）：https://www.tract.com/project/pole-canyon-technology-tract/ ，https://www.tract.com/project/pony-express-technology-tract/
- owner 从 null 更新为 Tract；相关 Eagle Mountain development-agreement party 记录为 UTLCO Eagle Mtn. Two, LLC。来源：https://www.tract.com/project/pole-canyon-technology-tract/ ，https://www.tract.com/project/pony-express-technology-tract/ ，https://www.utah.gov/pmn/files/1131687.pdf
- 新增 2024-01-18 Tract land-acquisition context：Tract 宣布已完成 Eagle Mountain 超过 668 acres land acquisition，位于 RTI Overlay，并称正与 Rocky Mountain Power 合作，到 2028 年通过新 transmission infrastructure 交付超过 400 MW。该信息仅作为 land-control / power-planning context，不等同于 interconnection approval 或 energized service。来源：https://tractcapital.com/news/tract-announces-acquisition-of-668-acres-in-eagle-mountain-ut-promising-further-investment-for-data-center-campuses/
- 新增 Eagle Mountain 2024-08-20 related land-process context：官方 City Council notice/packet 安排 Tract Development Agreement ordinance，约 672 acres / two parcels；同一议程描述 Triple Tail CRA：约 1,170.44 acres / 24 parcels，north parcels south of 4000 North, north of Pole Canyon Blvd, east of Tyson Pkwy；south parcel south of 1000 North and east of Pony Express Pkwy。该记录保留为相关地块/CRA 线索，不作为 building permit、site work、construction、energization 或 live-service 证据。来源：https://www.utah.gov/pmn/sitemap/notice/933950.html
- 冲突/不确定性：Tract 当前页面将 Pole Canyon（844 acres/1,700 MW）与 Pony Express（225 acres/120 MW）分别列为项目；Eagle Mountain 的 Tract/UTLCO 672-acre development agreement 与 Triple Tail CRA 记录是同一区域集群的重要线索，但本次未找到官方 parcel crosswalk 可把 Tripletail/development-agreement parcels 明确映射到两个 Tract 项目页。因此 USDC-0182 与 USDC-0183 overlap 仍未合并。
- 未核实项：未找到 building permit、final site-plan approval、construction start、utility interconnection approval、energization、commissioning、tenant/live-service 记录。capacity 为 developer/government inventory planning/nameplate capacity，不是已通电 IT load。
