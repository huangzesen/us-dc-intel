# USDC-0060 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: no status
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：`null` -> `site work-construction`。依据：Orange Township BZA 2025-06-12 minutes 将 6853 Green Meadows Drive 北侧土地用途描述为 “under construction Cologix Data Center”，并说明较大的 Future Cologix Data Center site 有 active construction；Ohio EPA 2026-08-10 Construction NOI workbook 也列出 Cologix COL5 与 Cologix 7&8 stormwater construction records。来源：
  - https://www.orangetwp.org/wp-content/uploads/2025/08/06.12.2025-BZA-Minutes-VA-25-07-VA-25-08-CU-25-09-VA-CU-25-10-VA-CU-25-11.pdf
  - https://dam.assets.ohio.gov/raw/upload/epa.ohio.gov/Public/DSW/Construction.xlsx
- Johnstown campus scope/capacity 补证：Cologix 2024-11-20 announcement 称已在 Johnstown acquired approximately 154 acres，规划 full buildout 为 eight AI-ready data centers、potential 800 MW scalable capacity、2.0 million square feet，first phase anticipated to begin in 2025。`capacity_mw` 仅记录为 Johnstown campus potential full-buildout 800 MW，不推断 Orange Township COL5 MW。来源：https://cologix.com/news/cologix-expands-central-ohio-footprint-with-land-acquisition-for-new-ai-ready-800mw-data-center-campus/
- Orange Township / COL5 地点与时间补证：Worthington City Council minutes 记录 Orange Township JEDD amendment for a Cologix data center project near Green Meadows Drive and Home Road，占 roughly 28 acres，数据中心 approximately 135,000 square feet；Cologix COL5 页面列出 6787 Green Meadows Drive，expected ready for service in Q3 2026；Ohio EPA Construction NOI workbook 列出 permit 4GC10275*AG，Cologix COL5，6787 Green Meadows Drive，25.78 disturbed acres，issue date 2024-12-18。来源：
  - https://www.worthington.org/Archive.aspx?ADID=6527
  - https://cologix.com/data-centers/columbus/col5/
  - https://dam.assets.ohio.gov/raw/upload/epa.ohio.gov/Public/DSW/Construction.xlsx
- Johnstown / COL7-COL8 地点与施工记录补证：Cologix COL7 页面列出 12017 Duncan Plains Road，Johnstown；Cologix COL8 页面列出 11719 Duncan Plains Road，Johnstown，并给出 COL8 site capacity 21 MW；Ohio EPA Construction NOI workbook 列出 permit 4GC10864*AG，Cologix 7&8，Duncan Plains Road，154.47 disturbed acres，issue date 2025-10-07；Ohio EPA Copermittee workbook（report date 2026-08-10）列出 Turner、Precision Engineering、TWC、Lithko、Freeland 等 Cologix 7&8 copermittees，issue dates 2025-12-30 至 2026-06-12。来源：
  - https://cologix.com/data-centers/columbus/col7/
  - https://cologix.com/data-centers/columbus/col8/
  - https://dam.assets.ohio.gov/raw/upload/epa.ohio.gov/Public/DSW/Construction.xlsx
  - https://dam.assets.ohio.gov/raw/upload/epa.ohio.gov/Public/DSW/Copermittee.xlsx
- State incentive action 保留并补强：Ohio Tax Credit Authority 2026-06-01 minutes approved 50% data-center tax exemption for 10 years for Cologix in Orange Township, Delaware County and Johnstown, Licking County, in exchange for 90 FTEs, $10,000,000 new annual payroll, and $5,185,126 retained annual payroll; vote 3-0, Garczyk and Kelly abstained。来源：https://dam.assets.ohio.gov/image/upload/development.ohio.gov/business/stateincentives/TCA_Meeting_Minutes_6.1.2026.pdf
- 冲突：未发现直接多源冲突。
- 证据不足/未核实：未找到 local building permit、certificate of occupancy、energization/utility service approval；COL5 官方/company MW 未在本次可访问官方/公司页面中核实；800 MW 是 Johnstown campus potential full buildout，不代表当前 energized capacity。
