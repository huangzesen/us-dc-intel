# USDC-0155 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Company announcement / energy-center proposal; no county or state data-center approval located
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：从 “company announcement / energy-center proposal; no county or state data-center approval located” 升级为 “site work-construction evidence”。依据是 Google/Intersect 2026-06-04 宣布 Meitner Energy Center 正在建设，以及 TDLR 已登记三个 Co. Rd. 21 数据中心新建项目；仍未找到县级 zoning/building permit、utility service approval 或 energization 记录。
  - Google blog（2026-06-04）：https://blog.google/innovation-and-ai/infrastructure-and-cloud/global-network/meitner-energy-center/
  - Google PDF press release（2026-06-04）：https://storage.googleapis.com/gweb-uniblog-publish-prod/documents/Google_Intersect_Texas_Announcement_-_June_2026.pdf
  - Intersect press release（2026-06-04）：https://www.intersect.com/news/google-and-intersect-deepen-texas-roots-with-new-data-center-and-energy-investments-in-gray-and-roberts-counties
- 新增 TDLR / state-level 建设记录：
  - Project Pumpkin 2A / Data Center Building 2A, TABS2026011989, registered 2026-02-08, 8830 Co. Rd 21, Miami, TX 79059, Location County = Gray, planned 2026-02-06 to 2027-12-14, $400,000,000, 761,000 ft^2, owner IP Meitner Land LLC, status Project Registered. Source: https://www.tdlr.texas.gov/TABS/Search/Print/TABS2026011989
  - Project Pumpkin 1A / Data Center Building 1A, TABS2026014814, registered 2026-03-12, 8810 Co. Rd. 21, Miami, TX 79059, Location County = Gray, planned 2025-12-19 to 2027-11-30, $400,000,000, 761,000 ft^2, owner IP Meitner Land LLC, status Review Complete. Source: https://www.tdlr.texas.gov/TABS/Search/Print/TABS2026014814
  - Project Pumpkin 3A / Data Center Building 3A, TABS2026014835, registered 2026-03-12, 8850 Co. Rd. 21, Miami, TX 79059, Location County = Gray, planned 2026-03-09 to 2028-04-18, $400,000,000, 761,000 ft^2, owner IP Meitner Land LLC, status Project Registered. Source: https://www.tdlr.texas.gov/TABS/Search/Print/TABS2026014835
- owner/location 更新：owner 字段补为 Google（announced data center）、IP Meitner Land LLC（TDLR building owner）、Intersect（energy co-location partner）。location.city 从 not published 改为 Miami postal area / Pampa region，并加入 TDLR Co. Rd. 21 地址。
- capacity_mw 保持 null：Google/Intersect 官方只披露 co-located wind/solar/battery storage “more than a gigawatt”，没有披露 data-center IT load 或可直接写入 capacity_mw 的数据中心容量。未采用第三方 840 MW / 1.3 GW / $14B 等未经官方核实的容量或投资额。
- 冲突/待核实：
  - TDLR records use Miami, TX 79059 addresses but list Location County = Gray; Roberts County official site lists the Roberts County courthouse at Miami, TX 79059, and Google/Intersect describe the project as in Gray and Roberts Counties. Exact parcel/county split remains unresolved until county parcel/tax/site-plan records are located. Roberts County official site: https://www.co.roberts.tx.us/
  - TDLR 是 Texas Architectural Barriers / construction registration evidence, not county zoning approval, not utility interconnection/service approval, and not proof of energization.
- SKILL.md 一句话（line 4）已同步刷新状态：从 baseline 的 “company announcement / energy-center proposal; no county or state data-center approval located” 更新为 “site work-construction evidence: Google/Intersect announced construction of the Meitner Energy Center on 2026-06-04, and Texas TDLR registered three new-construction data-center buildings on Co. Rd. 21; no county or state data-center approval located”，与 data.json 的 status_as_of_cutoff 一致。
