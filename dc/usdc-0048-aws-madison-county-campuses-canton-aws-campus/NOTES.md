# USDC-0048 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Multiple-campus construction/phased development is confirmed by state announcements; the 2026 state announcement adds an $11 billion Madison County expansion
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：从 state-announcement-backed construction/phased development 细化为 `site work-construction`。依据为州长办公室 2024-05-20 groundbreaking 公告、MDEQ construction stormwater coverage、Madison County Board of Supervisors 2026-08-03 utility-permit approval；仍未找到 building-level CO、energization record 或 live IT-load record。
  - https://governorreeves.ms.gov/amazon-web-services-breaks-ground-on-largest-economic-development-project-in-mississippi-history/
  - https://opcgis.deq.state.ms.us/ensearchonline/ai_info.aspx?ai=87129
  - https://www.madison-co.com/sites/default/files/bosquicknotes08032026final.pdf
- 2026-08-03 Madison County Board of Supervisors: agenda item listed `Amazon Data Services, Inc., Utility Permit - Madison County Parkway and Madison County Parkway East ROW`; quick notes say the Board approved Amazon Data Services' request to install utilities beneath Madison County Parkway right of way. This is recorded as county utility-permit approval, not energization.
  - https://tools.madison-co.net/elected-offices/board-of-supervisors/print-agenda.php
  - https://www.madison-co.com/sites/default/files/bosquicknotes08032026final.pdf
- MDEQ enSearch / permit certificate: Amazon Data Services Inc / Gray Construction `MSR109367` is listed for the `JAN 100 Site` in Madison County, with coverage date 2024-10-24, modification date 2025-05-14, and permit expiry 2027-01-31. This supports construction-site activity only.
  - https://opcgis.deq.state.ms.us/ensearchonline/ai_info.aspx?ai=87129
  - https://opcgis.deq.state.ms.us/enOnline/get_doc.aspx?dt=pdf&id=1784357
- MDEQ enSearch also lists Amazon Data Services Inc / Yates-Turner `MSR109366` for the MCEDA Megasite as terminated on 2026-05-28. This is retained as a stormwater-permit status update and is not treated as completion/energization evidence.
  - https://opcgis.deq.state.ms.us/ensearchonline/ai_info.aspx?ai=87129
- Owner populated from official sources as `Amazon Web Services / Amazon Data Services, Inc.`. AWS/state announcements identify AWS as the project and MDEQ/county records identify Amazon Data Services, Inc. as permit applicant.
  - https://governorreeves.ms.gov/amazon-continues-mississippi-expansion-announcing-plans-to-invest-a-total-of-25-billion-across-the-magnolia-state/
  - https://www.aboutamazon.com/news/company-news/amazon-25-billion-mississippi-data-centers
- Capacity remains `null`: no official MW value located in county/state/MDEQ/Amazon sources. No contradiction found between the 2026 state announcement and Amazon company announcement on planned investment: both describe an additional $11B Madison County expansion within broader $12B central Mississippi / $25B statewide plans.
