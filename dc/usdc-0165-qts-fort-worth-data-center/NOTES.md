# USDC-0165 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: no status
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status: `no status` -> `partial live`。依据：QTS 当前 Fort Worth 1 页面列出 52-acre campus、70 MW+ critical campus capacity、200 MW gross campus planned potential，并列出 FTW1 DC1 与 FTW1 DC2 地址；TDLR 对 FTW1 DC2 的 2024 新建 42 MW 项目显示 `Inspection Complete`。未找到 DC2 或新 DC1 扩建的 CO/并网/utility-service completion 记录，因此不升为 `full buildout`。
  - https://q.com/data-centers/fort-worth/
  - https://www.tdlr.texas.gov/TABS/Search/Project/TABS2024010121
- capacity: `null` -> campus current `70 MW+` critical capacity, campus planned potential `200 MW`, DC2 project `42 MW`。QTS 官方页给出 campus 当前与规划容量；TDLR TABS2024010121 给出 DC2 为 two-story, 42 Megawatt Data Center addition，471,876 sq ft，$220,000,000，start 2024-03-01 / completion 2026-04-01。
  - https://q.com/data-centers/fort-worth/
  - https://www.tdlr.texas.gov/TABS/Search/Project/TABS2024010121
- location/owner: 补充 campus 地址层。QTS 官方页列 FTW1 DC1 - 14100 Park Vista Boulevard，FTW1 DC2 - 14052 Park Vista Boulevard；TDLR 和部分 City 文件以 14100 Park Vista Blvd 指代 campus/DC2。owner 统一为 QTS / Quality Technology Services，并在 JSON actions 中保留各 filing 的具体 entity 名称（QTS Fort Worth I DC2 LLC、Quality Technology Services, LLC、Quality Technology Services (QTS)）。
  - https://q.com/data-centers/fort-worth/
  - https://www.tdlr.texas.gov/TABS/Search/Project/TABS2024010121
  - https://www.tdlr.texas.gov/TABS/Search/Project/TABS2025015896
  - https://www.tdlr.texas.gov/TABS/Search/Project/TABS2026022992
- Fort Worth local-government evidence added: CY 2024 Development Activity Report lists QTS FTW1 DC2 at 14052 Park Vista Blvd as June 2024 new commercial construction of a new data center, 471,876 sq ft, $160,201,754 valuation, and QTS FTW1-DC2 Ph 2 as December 2024 interior data-center remodel, 99,400 sq ft, $52,000,000 valuation. City Secretary contract materials also identify QTS Data Center / QTS Investment Properties Fort Worth, LLC at 14100 Park Vista Boulevard with 2024 utility/easement exhibits.
  - https://www.fortworthtexas.gov/files/assets/public/v/2/development-services/documents/dac/twelve-months/202412_cy-2024_dac.pdf
  - https://publicdocuments.fortworthtexas.gov/CSODOCS/DocView.aspx?dbid=0&id=311756&repo=City-Secretary
- Public-works completion evidence added: Fort Worth TPW acceptance materials for City Project No. 104062 say QTS Fort Worth water, sewer, and paving improvements were finally inspected on 2025-12-05, punch-list items were completed on 2025-12-16, and the work was accepted by the City; document names QTS Data Centers as developer.
  - https://publicdocuments.fortworthtexas.gov/CSODOCS/DocView.aspx?dbid=0&id=354244&repo=City-Secretary
- Active/planned expansion evidence added: TDLR TABS2025015896 registers a 168,770 sq ft, $130,000,000 additions-to-existing-building DC1 expansion with start 2025-07-01 / completion 2026-10-01; TDLR TABS2026022992 registers another 147,946 sq ft, $300,000,000 new-construction DC1 expansion with equipment yard, start 2026-07-01 / completion 2027-10-01.
  - https://www.tdlr.texas.gov/TABS/Search/Project/TABS2025015896
  - https://www.tdlr.texas.gov/TABS/Search/Project/TABS2026022992
- Construction corroboration: AP reported topping out a two-story QTS campus data center in north Fort Worth, 325,000 sq ft, anticipated completion Summer 2025, with Corgan as architect. This is treated as contractor corroboration only because the article does not expose a permit/CO/energization identifier.
  - https://www.a-p.com/news-and-insights/ap-tops-out-new-data-center-in-fort-worth/
- Conflicts retained: (1) DC2 address differs between TDLR (`14100 PARK VISTA BLVD`) and QTS/Fort Worth DAC (`14052 Park Vista Boulevard`); (2) owner/developer entity varies by filing; (3) inspection complete/current campus capacity does not equal confirmed DC2 energization or full campus buildout.
- Unable to verify: no public certificate of occupancy, utility energization, or interconnection completion record was located for DC2 or the newer DC1 expansion filings during this refresh.
