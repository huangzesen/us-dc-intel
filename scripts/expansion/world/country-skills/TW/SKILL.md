---
name: "tw-datacenter-methodology"
location: scripts/expansion/world/country-skills/TW/SKILL.md
description: "Taiwan (TW) datacenter discovery & audit methodology — how to enumerate, verify, and update Taiwan datacenter projects at county/city/special municipality granularity (20 divisions in the current manifest). Taiwan has no public national datacenter registry and no machine-searchable national building-permit database: enumeration pivots on operator official pages & annual reports (CHT, Chief, Vantage), government/regulatory sources (NCC licence statistics, moda/NICS/GSN, MOE TANet regional network centers, NSTC/NCHC national cloud & science-park authorities, county/city government releases), official cloud-region lists (Azure Taiwan positive; AWS/GCP/OCI absent = negative), and interconnection signals (TPIX/TWIX, cable landing stations). Google Taiwan datacenters are NOT a Google Cloud region. Read this before running TW exploration/audit batches; routes to explorer-official.md (official/regulatory/cloud) and explorer-industry.md (industry/vendor/media/query patterns)."
---

# TW · 台灣資料中心查詢方法論（Datacenter Discovery & Audit Methodology）

> 目的：台灣**沒有**公開國家級資料中心註冊庫，也沒有可機器檢索的全國建照/使照資料庫（大型開發走環境部環評＋縣市政府建照，但無統一可檢索資料庫）——不能按單一門戶直接列舉。
> 台灣是**營運商主導的成熟 IDC 市場**（中華電信 CHT＋是方電訊 Chief 合計市占約 78%，工商時報 2026-08-05）＋**超大型業者進場**（Google 在台 3 座資料中心、Microsoft Azure 台灣區域 2026、Vantage TPE11、聯發科銅鑼 R&D 資料中心）。
> 本 skill 匯總兩份已審定（luna max Review record）的探索報告（官方/監管管線 + 行業/廠商發現），作為台灣探索與複核批次的入口；衝突時以官方/營運商來源判定設施最終狀態。

## 入口

| 文件 | 管線 | 內容 |
| --- | --- | --- |
| `explorer-official.md` | 官方/監管/雲管線 | NCC 執照普查、moda/NICS/GSN 政府網際服務網、教育部 TANet 區域網路中心、NSTC/NCHC 國網雲端資料中心與科學園區管理局（SIPA/中科/南科）、縣市政府公告（台南/嘉義已驗證 A）、營運商官方頁與年報（CHT/是方/Vantage）、官方雲區域清單（Azure 正證據、AWS/GCP/OCI 負證據）、20 division 列舉工作流與狀態規則 |
| `explorer-industry.md` | 行業/廠商發現 | 本地媒體（工商時報、數位時代、中央社、自由時報、鉅亨網、鏡週刊、商業周刊、Taipei Times 等）、國際行業媒體（Light Reading、DCD、TelecomGrid、DataCenterJournal）、營運商/廠商種子清單（CHT、是方、Acer eDC、Vantage、聯發科、台達電/敦陽等）、聚合目錄（DataCenterMap、Baxtel、datacenters.com、Arizton）、繁中/英文查詢模板 |

## 核心結構事實（框定每次搜索）

1. **行政區模型**：manifest 為 **county/city/special municipality**，恰好 **20 個 division**：Changhua、Chiayi、Hsinchu、Hualien、Yilan、Keelung、Kaohsiung、Kinmen、Lienchiang、Miaoli、Nantou、New Taipei、Penghu、Pingtung、Taoyuan、Tainan、Taipei、Taitung、Taichung、Yunlin。模型細節：**Hsinchu**（新竹市＋新竹縣）與 **Chiayi**（嘉義市＋嘉義縣）各併為單一 division——本輪證據中「Hsinchu」下設施證據位於新竹縣竹北市，「Chiayi」下證據位於嘉義市。
2. **無全國註冊庫**：最接近普查的組合是 **NCC 電信事業/頻率許可統計（執照清冊，非設施清冊）＋ NCHC/科學園區管理局公告 ＋ 縣市政府新聞稿 ＋ GSN/TANet 網路中心清單 ＋ 營運商官方頁（CHT 板橋、是方、Vantage）＋ 官方雲區域清單**。認證註冊庫：Uptime Institute / TIA-942 為設施等級第三方佐證來源（台灣已驗證案例僅 CHT 板橋）。
3. **官方雲區域清單同時是正證據與負證據**：Azure 台灣為唯一官方宣布之台灣雲區域（2024 第一階段 M365 資料落地啟用、2026 正式區域，城市未公開，A）；**AWS/GCP/OCI 官方區域清單無台灣（負證據）**；**Google 台灣資料中心（彰化 2013 啟用、台南 2019 宣布用地閒置、雲林 2020 宣布購地中）≠ Google Cloud 區域**——Google Cloud locations 清單不含台灣，不可混記。
4. **電力是選址背景**：台電供電、用電大戶再生能源義務；北部電力吃緊、機房滿載 → 是方南下中科第 4 座 AIDC（民報 2026-03-24，B）、CHT 優先在中南部新增單一設施 >20MW 之 AIDC（工商時報 2026-04-04，B，觀察項）。
5. **互聯地理**：約 95% 網路流量經 5 個海纜登陸站（頭城、淡水、八里、枋山、金門；14 條海纜，Fount Media B）；TPIX（內湖麗源大樓，是方官方 datasheet A）與 TWIX/TWNIC 為互聯錨點——**登陸站/IXP 是連通性基礎設施，不得計為資料中心容量**。
6. **生命週期與狀態語義**：`意向/MoU/規劃` < `招標/決標` < `動工/動土/開工` < `啟用/營運`；`取消/延宕/閒置` 為負面狀態。僅 `啟用/營運`（官方/營運商/政府來源）算營運證據；`宣布` 不等於 `營運`（Google 台南 2019 宣布、2026 仍閒置；Google 雲林 2020 宣布、購地中）。
7. **語言**：繁體中文召回最佳，英文次之（品牌/認證名）。

## 查詢模板（複製貼上，完整清單見 explorer-official.md §1/§2 與 explorer-industry.md §5）

```text
site:ncc.gov.tw 電信事業 許可 OR 執照 OR IDC OR 資料中心
site:moda.gov.tw 資料中心 OR 機房 OR 算力 OR 數位基礎建設
site:nchc.org.tw 國網 OR 雲端 OR 資料中心 OR 台南 OR 算力
site:sipa.gov.tw 電信 OR 機房 OR 資料中心
site:*.gov.tw 資料中心 動土 OR 啟用 OR 招標（縣市層級）
「中華電信」 「資料中心」 OR IDC 龍潭 OR 板橋 OR 內湖 OR 竹北
「是方電訊」 OR Chief 資料中心 OR IDC OR TPIX
site:datacenters.google taiwan ；site:datacenters.microsoft.com taiwan ；site:azure.microsoft.com taiwan region
「Google」 台灣 資料中心 彰化 OR 台南 OR 雲林
site:ctee.com.tw 資料中心 OR IDC OR AIDC OR 機房
site:bnext.com.tw 資料中心 OR 雲端 OR Google OR Microsoft
site:lightreading.com taiwan data center ；site:datacenterdynamics.com taiwan OR "Taipei" data center
site:datacentermap.com taiwan ；site:baxtel.com taiwan ；site:datacenters.com taiwan
「台灣」 （「資料中心」 OR 「數據中心」 OR 「機房」 OR 「主機代管」） （台北 OR 新北 OR 桃園 OR 台中 OR 台南 OR 高雄）
「{縣市名}」 （「資料中心」 OR 「機房」 OR 「雲端」 OR 「IDC」）
（「海纜」 OR 「登陸站」） 台灣 （頭城 OR 淡水 OR 八里 OR 枋山 OR 金門）
「動土」 OR 「啟用」 資料中心 2025 OR 2026
```

## 官方/監管管線要點（詳見 explorer-official.md）

- **NCC（國家通訊傳播委員會）**：電信管理法（2020-07 施行）下電信事業許可、網路互連與頻率管理；執照清冊是營運商普查來源，**執照 ≠ 資料中心設施**。入口：ncc.gov.tw。
- **moda / NICS / GSN**：數位發展部（2022-08-27 成立）主管數位基礎建設/資通安全/政府網路（GSN）；已驗證證據：GSN 澎湖公告（2025-07-17，CHT 設備維護造成 GSN 電路中斷）→ 證明澎湖僅 CHT 本地電信設備、無資料中心（A）。
- **教育部 TANet 區域網路中心**：台東（東大）、宜蘭（宜大）、高屏澎（中山）等——教育網路機房，非商業代管（A）；查 depart.moe.edu.tw 清單。
- **NSTC / NCHC 與科學園區管理局**：NCHC 營運「國網雲端資料中心」（台南，南部科學園區，2023-03 動土、2025 完成已啟用，約 800 機櫃，A）；SIPA 竹科公文證實園區電信由 CHT 獨家提供（U，非代管 DC）。
- **縣市政府公告**：台南市政府（2019-09-11，Google 第 2 座資料中心用地＋綠電，A）；嘉義市政府（2019-09-09，綠能雲端資料中心啟用——市府機房重建，非商業代管，A）。
- **營運商官方頁與年報**：是方（TPIX datasheet、官方 IDC 頁、LY2 麗源大樓 AI IDC 官方頁）；CHT（板橋 IDC 官方頁，TIA-942 Rated 3 + Uptime M&O；2016 年報另稱 Rated 4——並存記錄）；Vantage（TPE11 官方頁，16MW IT 負載、215k 平方英呎、2024-07 啟用）。
- **provider-level 交叉檢查**：遠傳、台灣大哥大、亞太電信與 NEXTDC 的服務/市場頁面若未同時指明台灣實體站點與基礎設施功能，只記 `provider_service`，不得直接建立具名資料中心。
- **官方雲區域清單**：Azure 台灣（正證據，A）；AWS/GCP/OCI（負證據）；Google 資料中心 ≠ Google Cloud 區域。

## 行業/廠商發現要點（詳見 explorer-industry.md）

- **本地媒體（B，引官方可升 A）**：工商時報（五大業者/78% 市占/龍潭一期/AIDC 大投資/聯發科）、民報（是方南下 AIDC）、自由時報（Google 第 3 座雲林）、數位時代（Google 10 年/超大規模雲地圖/AI 問答）、鉅亨網、鏡週刊（聯發科 45MW 規模傳聞）、商業周刊（亞灣 2.0）、中央社 CNA（海纜登陸站清單/亞灣 5G AIoT）、NOWnews/JWTnews（嘉義綠能雲端）、Taipei Times（Azure 3-4 座 DC、南部矽谷走廊）、MyGoNews（Google 彰濱 US$600M）、放言/上報（海纜）。
- **國際行業媒體（B）**：Light Reading（Vantage 16MW 進入台灣）、DCD（Foxconn 高雄資料中心）、TelecomGrid（CHT 龍潭 36MW，C，與官方檔交叉）、DataCenterJournal（台中列表，C）。
- **營運商/廠商種子（A=存在 / B=容量 / C=聚合器）**：CHT（板橋 A、龍潭 AIDC B/C、內湖濱江規劃 B、中壢仁美/竹北 C）、是方（麗源/宏鼎 AI IDC、TPIX，A）、Acer eDC 宏碁雲架構（龍潭主機房 18,000 坪/7 級耐震，B/C，官方頁待補）、Vantage TPE11（A）、VeeTIME/DataHOUSE（台中，C/U）、聯發科銅鑼（B，2026-05 啟用，15MW 一期/45MW 傳聞）、台達電/敦陽（嘉義市府機房合作，B，政府機房非 colo）、惠國科技（苗栗縣資訊中心更新，C，政府設施）、東元 TECO（工程案佐證，C）。
- **目錄/聚合器（C/U 線索源）**：DataCenterMap（台北 17 座/9 家，C）、Baxtel、datacenters.com（DataHOUSE）、Arizton（27 座既有/6 座規劃 colo，僅涵蓋 7 縣市——台東/宜蘭/金門/連江/澎湖缺席為負面佐證，C）、TelecomGrid（36MW C）。
- **狀態語義**：`announced`＝不計數；`規劃`＝管線；`動工/動土`＝在建；`啟用/營運`＝營運（仍區分殼樓/裝機 IT load/租賃容量）；`閒置/取消/延宕`＝負面證據保留。

## 來源分類（官方/監管 vs 行業/廠商）與 A/B/C/U 分級

- **A（官方/一手）**：政府機關頁面/公文书（縣市政府、教育部 TANet、GSN、NCHC、SIPA、NSTM 館藏檔案）、營運商官方頁與年報（CHT、是方、Vantage、Google/Microsoft 官方雲區域頁）、官方雲區域清單（Azure 台灣正證據；AWS/GCP/OCI 負證據）。
- **B（強二級）**：引述官方/營運商公告的正規媒體（工商時報、數位時代、中央社、Taipei Times、Light Reading 等）、官方新聞室/官方部落格。
- **C（僅線索）**：聚合目錄（DataCenterMap、Baxtel、datacenters.com、Arizton、DataCenterJournal、TelecomGrid）、無具名地點的廠商行銷、歷史未證實傳聞（2013 NTT 台中、2013 臉書彰濱）。
- **U（未驗證）**：僅見於聚合器或單一弱來源；升級前須複核（DataHOUSE、VeeTIME、竹北、中壢仁美、TelecomGrid 36MW、雲林進度、Acer eDC 官方頁）。
- **分級只涵蓋該來源實際支持的事實**：官方服務頁證明服務存在（A）不證明實體地址/機櫃數；政府公文證明電信基礎設施（A）不證明商業代管設施。容量字段（MW/機櫃/樓板）除非官方/營運商/招標來源明示，否則保持 null（Vantage 16MW 官方頁數值；TelecomGrid 36MW 為 C；NCHC 800 機櫃官方；Acer eDC 18,000 坪媒體引述 B）。
- **計數與去重**：設施存在須來源同時指明基礎設施**與**足以區分實體場址的地點；同一棟樓多營運者分開記（麗源大樓 = LY IDC + TPIX）；同一園區多棟分開記（麗源 vs 宏鼎 LY2）；同一設施多重宣稱並存（板橋 Rated 3 + M&O vs 2016 年報 Rated 4，以現行官方頁為準）；登陸站/教育網路/電信交換/政府機房各按其類型記錄，不計為商業 colo；宣布 ≠ 營運。
- **負面搜索規則**：網路咖啡、電腦教室、NGO 伺服器室、GIS 室、軟體平台不計，除非來源描述具名營運商與地點之主機/代管/運算基礎設施。

## 使用流程（探索/複核批次）

1. 讀取批次 JSONL（country_code=TW，divisions=county/city/special municipality，20 目標）。
2. 歸一化 division：確定縣市、次級區/鄉鎮（Hsinchu→新竹縣竹北市；Chiayi→嘉義市）；項目常以縣市或園區命名。
3. 官方查詢：縣市政府（資料中心/機房/雲端/動土/啟用/招標）→ NCC/moda/GSN/TANet/NCHC/SIPA → 營運商官方頁（CHT/是方/Vantage/Acer eDC）。
4. 雲/營運商 pivot：台北/新北/桃園查全部大營運商；官方雲區域清單做正/負確認（Azure vs AWS/GCP/OCI）；Google 台灣 DC 與 Google Cloud 區域分開記。
5. 行業佐證：本地媒體（工商時報/數位時代/中央社/Taipei Times）與國際媒體（Light Reading/DCD）對 A 級項目做 B 級佐證；聚合目錄僅作發現與交叉。
6. 去重：同一園區可能是營運商品牌、SPV、街道地址、園區名、規劃號；按（營運商母公司、縣市、街道/地塊、園區名）聚類。輸出 world 同 schema；無項目 division 寫 `no_projects: true`。
7. 遵行 NO-DELETION；只創建自己的結果文件。

## 待辦（2026-08-12）

- 兩份 explorer 已審定（explorer-official.md / explorer-industry.md，Review record 已追加）。
- 下一步：探索/複核批次（縣市粒度）以本 skill 作為每個 agent 的國家層參考注入。
- 待核實：Azure 台灣區域 2026 啟用時城市揭露；Google 台南/雲林動工訊號（縣市政府＋官方頁）；CHT 內湖濱江、台中/南部 >20MW AIDC 選址；聯發科銅鑼擴建；Acer eDC 官方頁補齊；U 級聚合目錄條目（DataHOUSE、VeeTIME、竹北、中壢仁美、TelecomGrid 36MW）年度複核；Uptime/TIA-942 認證現況確認。
