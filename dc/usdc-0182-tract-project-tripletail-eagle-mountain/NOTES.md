# USDC-0182 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Land-acquisition/development-agreement and CRA stage; no construction or utility service evidence located
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：从 “Land-acquisition/development-agreement and CRA stage; no construction or utility service evidence located” 调整为 `local process / entitlement and CRA implementation evidence`。依据为 Eagle Mountain/EDCUtah 的 2024-01-18 acquisition 公告、2024-08-20 官方会议通知中的 Tract Development Agreement 与 Triple Tail CRA Plan 条目、以及 2025 年 CRA interlocal/UFSA 修订记录；仍未找到 building permit、CO、utility service、interconnection/energization 或 construction-start 证据。
- owner 更新：`null` -> `Tract`。Eagle Mountain City 称 Tract 已购买 668 acres；EDCUtah 同日公告 Project Tripletail；Tract 当前项目页将 Pole Canyon 与 Pony Express 列为 owned and in development。
- capacity 更新：不设为单一确认值，改为冲突结构。2024 DCD 报道称 Tract 正与 Rocky Mountain Power 合作，目标 2028 年通过新输电基础设施提供 400+ MW；Tract 当前页面列 Pole Canyon 1,700 MW / 844 acres、Pony Express 120 MW / 225 acres。官方 CRA/agenda 描述 north parcels near Pole Canyon 和 south parcel east of Pony Express，但未找到公开 crosswalk 证明 Tripletail 与当前两个 Tract 页面完全一一对应。
- 本次新增/确认事实：
  - 2024-01-18 Eagle Mountain City: Tract purchased 668 acres in Eagle Mountain; city frames it as ongoing Technology Overlay Zone investment. Source: https://eaglemountain.gov/tract-announces-acquisition-of-668-acres-in-em/
  - 2024-01-18 EDCUtah: Project Tripletail; more than 668 acres; $7B capex; RTI Overlay by-right data-center use and expedited administrative review context. Source: https://www.edcutah.org/recent-news/tract-announces-acquisition-of-668-acres-in-eagle-mountain-utah
  - 2024-08-20 Utah PMN/Eagle Mountain agenda: Tract Development Agreement covering approximately 672 acres in two parcels; Triple Tail CRA Plan covering 24 parcels, with north parcels south of 4000 North / north of Pole Canyon Blvd / east of Tyson Pkwy and south parcel south of 1000 North / east of Pony Express Pkwy. Source: https://www.utah.gov/pmn/sitemap/notice/933950.html
  - 2024-08-20 Triple Tail CRA hearing notice: Phase 1 requested $54,372,571 in tax increment for project-area costs; increment only generated if the project area is developed. Source: https://www.utah.gov/pmn/files/1150731.pdf
  - 2025-02-04 Eagle Mountain RDA minutes: approved amended UFSA interlocal cooperation agreement for incremental property taxes within Triple Tail CRA; 4 yes, 1 absent. Source: https://www.utah.gov/pmn/files/1328093.pdf
  - 2025-02-18 UFSA/LBA minutes: adopted Resolution 02-2025A amending the Eagle Mountain RDA/Triple Tail CRA interlocal agreement with UFSA. Source: https://www.utah.gov/pmn/files/1243023.pdf
  - 2025-02-24 official interlocal notice: taxing entities entered interlocal agreements to remit portions of tax increment generated within Triple Tail CRA; notice lists 40-year/20-year terms and caps. Source: https://www.utah.gov/pmn/files/1237341.pdf
  - 2026-08-11 current Tract pages accessed: Pole Canyon is listed as 844 acres / 1,700 MW / owned and in development; Pony Express is listed as 225 acres / 120 MW / owned and in development. Sources: https://www.tract.com/project/pole-canyon-technology-tract/ and https://www.tract.com/project/pony-express-technology-tract/
  - 2026-08-11 current third-party corroboration: Cleanview separately lists Tract Pole Canyon as planned 1,700 MW and Tract Pony Express as planned 120 MW. Sources: https://cleanview.co/data-centers/utah/2137/tract-pole-canyon and https://cleanview.co/data-centers/utah/2138/tract-pony-express
- 多源冲突：
  - capacity/scope: 2024 Project Tripletail reporting says 400+ MW by 2028; current Tract company pages list 1,700 MW Pole Canyon and 120 MW Pony Express. Public official sources reviewed do not explain whether this is an expansion, split, or different named marketing scope.
  - acreage: city/EDCUtah/DA materials cite roughly 668/672 acres; current Tract pages total 1,069 acres across Pole Canyon and Pony Express.
- 无法核实/证据不足：
  - 未找到 Tract/Tripletail/Pole Canyon/Pony Express 的 project-specific building permit、CO、utility service、interconnection queue entry、energization record 或 construction-start record。
  - Eagle Mountain 2025-01-16 city article says Rocky Mountain Power has indicated limited capacity to expand generation in the near term and that no local energy-generation projects are currently on the table, but 该文是 citywide energy-planning context，不是 Tripletail permit/status 证据。Source: https://eaglemountain.gov/planning-commission-recommends-denial-of-zoning-changes-for-energy-generation/
- verified: true for land acquisition, owner, local CRA/interlocal process, and current company-stated Pole Canyon/Pony Express capacities; verified: false for a single definitive Tripletail buildout capacity and for construction/energization status.
