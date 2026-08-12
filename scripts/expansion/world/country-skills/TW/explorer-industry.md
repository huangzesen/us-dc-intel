# TW Explorer Industry - 台灣資料中心列舉（行業／廠商／媒體／互聯）

Date verified: 2026-08-12. Country: **TW - Taiwan, Province of China**（ISO 3166-1 alpha-2: TW）。Scope: 以本地／國際行業媒體、營運商與廠商頁面、互連記錄、代管目錄、專案部落格與 division 級搜尋模式進行台灣資料中心列舉。與 `explorer-official.md` 搭配使用；衝突時以官方檔來源判定設施最終狀態。

Reliability grades:
- **A** = 一手／營運商／官方／政府：營運商服務頁或招標、政府（縣市、NCHC、TANet、GSN、SIPA、NSTM）、官方雲區域清單（見官方檔）。
- **B** = 強二級：工商時報、數位時代、中央社 CNA、自由時報、鉅亨網、鏡週刊、商業周刊、Taipei Times、Light Reading、Data Center Dynamics 等正規媒體（引官方／營運商公告為佳）。
- **C** = 僅線索：DataCenterMap、Baxtel、datacenters.com、DataCenterJournal、Arizton、TelecomGrid、部落格／轉載、無具名地點之廠商行銷、目錄列示。
- **U** = 未驗證：僅聚合器或單一弱來源；升級前須複核。

---

## 0. 台灣行業框架（Industry Frame）

- 台灣為**營運商主導的成熟 IDC 市場**：中華電信 CHT＋子公司是方電訊合計 IDC 市占約 78%（工商時報 2026-08-05，B）；CHT 被形容為 2025 年唯一在國內新建 IDC 的業者（工商時報 2025-04-07，B）。
- **超大型業者進場**：Google 在台已建 3 座（彰化營運中、台南 2019 宣布但用地閒置、雲林 2020 宣布購地中）；Microsoft/Azure 台灣區域 2024 第一階段（M365 資料落地）、2026 正式區域（官方，見官方檔）；聯發科銅鑼 R&D 資料中心 2026-05 啟用（全台首座浸沒式冷卻）；Vantage TPE11 2024-07 進入台灣。
- **北電南送壓力**：北部電力吃緊、機房滿載促使是方南下一期 AIDC（民報 2026-03-24，B）；CHT 宣布優先在中、南部新增單一設施 >20MW 之 AIDC（工商時報 2026-04-04，B，觀察項）。
- **互連地理**：約 95% 網路流量經 5 個海纜登陸站（頭城、淡水、八里、枋山、金門；14 條海纜，Fount Media B）；宜蘭頭城與新北淡水為兩大樞紐；馬祖海纜為唯二（斷纜依賴微波備援，Up Media B）。
- 資料保護（PDPA）、Microsoft 365 資料落地、政府雲端需求為本地代管需求背景。
- 語言：繁體中文召回最佳；英文次之（品牌／認證名）。

---

## 1. 本地媒體（Local Press）

| 來源 | URL／途徑 | 用途 | 等級 |
|---|---|---|---|
| 工商時報（ctee） | https://www.ctee.com.tw/ | 已驗證：五大業者撐起IDC一片天（CHT 內湖濱江規劃、龍潭一期完成）：https://www.ctee.com.tw/news/20250407700140-439901 ；CHT 集團 IDC 市占 78%（龍潭 AIDC 啟用案例）：https://www.ctee.com.tw/news/20260805701672-430502 ；宏碁雲架構（Acer eDC 龍潭主機房）：https://www.ctee.com.tw/news/20211028700464-431202 ；CHT 啟動 AIDC 大投資（中南部 >20MW）：https://www.ctee.com.tw/news/20260404700038-439901 ；聯發科銅鑼研發資料中心啟用：https://www.ctee.com.tw/news/20260507700774-430501 | B；引官方公告時可升 A |
| 民報（peoplenews） | https://www.peoplenews.tw/ | 是方砸 30 億南下一期 AIDC（中科；北部電力吃緊、機房滿載）：https://www.peoplenews.tw/articles/economic-news/22942 | B |
| 自由時報（ltn） | https://news.ltn.com.tw/ | Google 第 3 座資料中心落腳雲林（雲林科技工業區竹圍子區，約 20 公頃、NT$200 億）：https://news.ltn.com.tw/news/life/breakingnews/3280940 | B |
| 數位時代（bnext） | https://www.bnext.com.tw/ | Google 在台資料中心啟用 10 年（首座亞太 DC、約 6 萬就業）：https://www.bnext.com.tw/article/76840/google-taiwan-data-center-10-years ；超大型雲地圖（Google 台南未動工、A-Top 傳聞）：https://www.bnext.com.tw/article/82590/cloud-infrastructure-datacenter-taiwan-google-aws-microsoft-meta ；AI 問答彙整（雲林進度超前、台南延宕）：https://ai.bnext.com.tw/answer/google-13480-893905 | B/C |
| 鉅亨網（cnyes） | https://news.cnyes.com/ | 聯發科 AI 資料中心啟用、全台首座浸沒式冷卻佐證：https://news.cnyes.com/news/id/6446719 | B |
| 鏡週刊（mirrormedia） | https://www.mirrormedia.mg/ | 聯發科銅鑼資料中心約 45MW 規模、機器人巡檢機房：https://www.mirrormedia.mg/story/20260508fin001 | B |
| 商業周刊（businessweekly） | https://wealth.businessweekly.com.tw/ | 亞灣 2.0 智慧科技園區（NT$170 億／7 年；NVIDIA/AMD R&D 中心）：https://wealth.businessweekly.com.tw/m/GArticle.aspx?id=ARTL001001955 | B |
| 中央社 CNA | https://www.cna.com.tw/ | 海纜登陸站清單（淡水、八里、頭城、屏東枋山；花蓮無）：https://www.cna.com.tw/news/aipl/202501100035.aspx ；CHT 率 13 家業者進駐高雄亞洲新灣區 5G AIoT 大聯盟（NT$3 億投資資通訊基礎設施、雲端機房、5G 網路）：https://www.goodlinker.io/topic/80 | B |
| 蕃新聞（n.yam） | https://n.yam.com/ | CNA 轉載：CHT 亞灣科技大樓（5G 網路切片首驗證、+500 技術人員）：https://n.yam.com/Article/20231222307761 ；房市效應佐證 Google 雲林購地：https://n.yam.com/Article/20240305176189 | B/C |
| 好房網 News | https://news.housefun.com.tw/ | Google 台南 2nd DC 用地閒置（議會質詢）：https://news.housefun.com.tw/news/article/882897400263.html ；2013 臉書彰濱傳聞（未證實）：https://news.housefun.com.tw/news/article/533334113781.html | B/C |
| NOWnews | https://www.nownews.com/ | 嘉義市綠能雲端資料中心啟用（年省 20 萬 kWh、110t CO2）：https://www.nownews.com/news/3620157 | B |
| JWTnews | https://www.jwtnews.biz/ | 嘉義市綠能雲端資料中心獨立報導：https://www.jwtnews.biz/1080909-2.htm | B |
| Taipei Times | https://www.taipeitimes.com/ | Microsoft 擴張台灣 AI 生態與資料中心（Azure 區域 3-4 座 DC、2024 第一階段）：https://www.taipeitimes.com/News/biz/archives/2025/09/24/2003844304 ；南部矽谷走廊（嘉義縣無 DC 命名）：https://www.taipeitimes.com/News/front/archives/2025/01/03/2003829567 | B |
| MyGoNews | https://www.mygonews.com/ | Google 彰濱落成典禮投資加碼至 6 億美元：https://www.mygonews.com/news/detail/news_id/108024 | B |
| LINE Today 新聞 | https://today.line.me/tw/ | 員山鄉深層地熱開鑽（綠電→吸引資料中心潛力）：https://today.line.me/tw/v3/article/aGmgBqo | C |
| 放言 Fount Media | https://www.fountmedia.io/ | 海纜關鍵且脆弱（5 登陸站、14 條海纜、95% 流量）：https://www.fountmedia.io/article/265487 | B |
| 上報 Up Media | https://www.upmedia.mg/ | 馬祖 2 條海底電纜斷裂（2025-01-22；微波備援）：https://www.upmedia.mg/tw/focus/politics/222474 | B |

查詢：
```text
site:ctee.com.tw 資料中心 OR IDC OR AIDC OR 機房
site:peoplenews.tw 資料中心 OR IDC OR 機房
site:ltn.com.tw Google OR 資料中心 OR 機房
site:bnext.com.tw 資料中心 OR 雲端 OR Google OR Microsoft
site:cna.com.tw 資料中心 OR 海纜 OR IDC
site:mirrormedia.mg OR site:cnyes.com 資料中心 OR AI 機房
site:housefun.com.tw 資料中心 OR Google OR 雲端
site:businessweekly.com.tw 資料中心 OR 雲端 OR 亞灣
site:upmedia.mg OR site:fountmedia.io 海纜 OR 資料中心 OR 登陸站
```

Lifecycle 動詞：意向／MoU／規劃；招標／決標；動工／動土；啟用／營運；延宕／閒置／取消。

---

## 2. 國際行業媒體（Trade Press）

| 來源 | URL | 已驗證項目 | 等級 |
|---|---|---|---|
| Light Reading | https://www.lightreading.com/ | Vantage 以 16MW 資料中心進入台灣市場：https://www.lightreading.com/data-centers/vantage-data-centers-expands-into-taiwan-with-a-16mw-data-center | B |
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com/ | Foxconn 高雄資料中心營運（IaaS/NEC SDN 平台）：https://www.datacenterdynamics.com/en/analysis/foxconn-wants-to-build-your-data-centers/ | B |
| TelecomGrid（專業部落格） | https://telecomgrid.com/ | CHT 龍潭（Lunping）AI 資料中心營運、滿載 36MW：https://telecomgrid.com/ai/chunghwa-telecom-powers-up-ai-future-with-36mw-data-center-in-taoyuan-taiwan/ | C（與官方檔交叉） |
| DataCenterJournal | https://www.datacenterjournal.com/ | 台中列表僅 1 筆 VeeTIME（細節欄卻引台北，內部不一致）：https://www.datacenterjournal.com/data-centers/taiwan/taichung/ | C |

查詢：
```text
site:lightreading.com taiwan data center
site:datacenterdynamics.com taiwan OR "Taipei" data center
site:telecomgrid.com taiwan OR chunghwa OR taoyuan
site:datacenterjournal.com taiwan
"Taiwan" "data center" news (2025 OR 2026) Taipei OR Taoyuan OR Tainan
```

---

## 3. 營運商、代管與廠商（Operators, Hosters, Vendors）

| 主體 | 主要或線索 URL | 行業訊號 | 等級與處理 |
|---|---|---|---|
| 中華電信 CHT | 官方 IDC 頁／年報（官方檔 2.6）；媒體見第 1 節 | 板橋 IDC（2016-07-29 啟用）、龍潭 AIDC 園區（一期完成）、內湖濱江（規劃）、中壢仁美（C）、竹北（C）；集團市占 78%（B） | A 官方頁；B 媒體；C 聚合器。板橋 Rated 3/4 宣稱衝突見官方檔 6 節 |
| 是方電訊 Chief | TPIX datasheet、官方 IDC 頁、LY2 頁（官方檔 2.6）；民報（B） | 麗源／宏鼎 AI IDC、TPIX；南下中科第 4 座 AIDC（民報 B） | A 官方頁；B 媒體 |
| Acer eDC（宏碁雲架構） | 工商時報 2021-10-28（B）；TECO 工程案頁（C）：https://tecoie.teco.com.tw/page/21 | 龍潭主機房：18,000 坪、7 級耐震、99.999% 設計；桃園 5F 機房改善工程（TECO） | B 媒體；C 廠商案。官方頁本輪未驗證 |
| Vantage Data Centers | 官方頁（A）；Light Reading（B） | TPE11 16MW、215k 平方呎、2024-07 啟用 | A/B |
| VeeTIME | DataCenterJournal 台中列表（C） | 台中 9,537 sq ft 列表，細節欄引台北、內部不一致 | C（弱／未驗證） |
| DataHOUSE | https://www.datacenters.com/datahouse-taichung（C） | 台中設施列示，無營運商頁面／規模 | C |
| 台達電 Delta／敦陽科技 Sysage | 嘉義市政府公告（官方檔）＋NOWnews/JWTnews（B） | 嘉義市綠能雲端資料中心合作廠商（市府機房重建） | B；政府機房非 colo |
| 惠國科技 | https://www.hgnet.com.tw/苗栗資訊中心更新建置案第一期工程/（C，2024） | 苗栗縣政府資訊中心重建（150kW×2 框式 UPS、N+1、40 分鐘電池）——政府設施非 colo | C |
| 東元 TECO | https://tecoie.teco.com.tw/page/21（C） | Acer eDC 桃園 5F 機房改善工程承攬案 | C 佐證 |
| 智瑞科技（部落格） | https://www.jhihrui.com.tw/blogs/news-20251017102206（C） | 台馬 3 號海纜（TM3）南竿段距南竿機房 7.7km；CHT 馬祖機房存在 | C |
| Flymia（部落格） | https://ppundsh.github.io/posts/b545/（C） | 台灣海纜登陸整理：頭城 5、淡水 5、八里 1、枋山 3；金廈海纜（金門-廈門）約 21km | C |
| 中古車/目錄 ji.zhupiter | https://ji.zhupiter.com/p-204996-中華電信南高雄營運處金門服務中心工務課網路股烈嶼機房.html（C） | CHT 金門烈嶼交換機房（烈嶼鄉東林，082-363-044）——電信交換，非 colo | C |
| 台南新聞平台（qnews 聚合） | https://qnews.tainanoutlook.com/news/8792805（C） | 沙崙智慧綠能科學城與 AMD/NCHC 提供免費 AI 算力（研究 HPC 樞紐） | C |

營運商查詢：
```text
site:cht.com.tw OR site:chief.com.tw OR site:acer-edc.com 資料中心 OR IDC
「Acer eDC」 龍潭 OR 桃園 資料中心 OR 機房
「聯發科」 OR MediaTek 銅鑼 資料中心 OR 算力
「Vantage」 台北 OR 台灣 資料中心
site:datacenters.com taiwan OR taichung OR datahouse
「台達電」 OR 「敦陽科技」 嘉義 綠能雲端資料中心
site:fareastone.com.tw （IDC OR 「資料中心」 OR 雲端 OR 主機代管）
site:taiwanmobile.com （IDC OR 「資料中心」 OR 雲端 OR 主機代管）
site:aptg.com.tw （IDC OR 「資料中心」 OR 雲端 OR 主機代管）
site:nextdc.com Taiwan OR 台灣 OR Taipei
```

Provider-level rule: 遠傳、台灣大哥大、亞太或 NEXTDC 的服務／市場頁面若未同時指明台灣實體站點與基礎設施，只記為 `provider_service` 或 `lead_only`；不得因品牌、雲服務或亞太市場頁面計入設施。官方設施頁、年報、許可或規劃文件須同時證明站點與功能，才可建立 `commercial_colocation`／`telco_core`；未發現台灣實體站點時保留 `negative`／`U`，並記錄查詢日期。
```

---

## 4. 互連、IXP、聚合器與超大型雲負面證據

| 通道 | URL | 用途 | 等級 |
|---|---|---|---|
| TPIX（台北網際網路交換中心） | 是方 datasheet：https://en.chief.com.tw/wp-content/uploads/2020/09/TPIX.pdf | 內湖麗源大樓之 IXP；互連錨點，非 DC 容量 | A（官方）；B（互連） |
| TWIX／TWNIC | https://www.twnic.tw/（入口錨點） | .tw 註冊與網際網路交換 | 互連錨點 |
| 海纜登陸站 | CNA：https://www.cna.com.tw/news/aipl/202501100035.aspx ；Fount：https://www.fountmedia.io/article/265487 ；Flymia、智瑞科技（C）；Up Media（B） | 頭城（宜蘭）、淡水／八里（新北）、枋山（屏東）、金門、馬祖（台馬 3 號）——連通性，非 DC | B/C |
| DataCenterMap | 台北目錄（17 座 DC／9 營運商）：https://www.datacentermap.com/taiwan/taipei/ ；台灣目錄（缺省檢查）：https://www.datacentermap.com/taiwan/ ；CHT 板橋：https://www.datacentermap.com/taiwan/taipei/cht-taipei-banqiao-idc/ ；中壢仁美：https://www.datacentermap.com/taiwan/taoyuan/cht-zhongli-renmei-idc/ ；竹北：https://www.datacentermap.com/taiwan/zhubei/cht-hsinchu-zhubei-idc/ | 設施發現與交叉檢查（板橋地址：板橋區國慶路 8 號） | C |
| Baxtel | https://baxtel.com/data-center/cht-hsinchu-zhubei-idc | 竹北 IDC 第二聚合器交叉 | C |
| datacenters.com | https://www.datacenters.com/datahouse-taichung | DataHOUSE 台中列示 | C |
| Arizton 台灣市場組合報告 | https://www.arizton.com/market-reports/taiwan-data-center-portfolio | 27 座既有／6 座規劃 colo DC，僅覆蓋彰化、高雄、台中、台南、台北、桃園、竹北——台東／宜蘭／金門／連江／澎湖缺席（負面佐證） | C |
| TelecomGrid | 見第 2 節 | CHT 龍潭 36MW（C） | C |
| 超大型雲區域 | Azure 台灣（官方 A，正）；AWS/GCP/OCI 官方區域清單（負） | 見官方檔第 3 節 | A 負/正 |
| Uptime Institute／TIA-942 | https://uptimeinstitute.com/ （入口錨點） | 板橋認證宣稱（Rated 3 + M&O vs 2016 Rated 4）需官方認證紀錄確認 | C/U |

聚合器／互連查詢：
```text
site:datacentermap.com taiwan
site:baxtel.com taiwan
site:datacenters.com taiwan
site:arizton.com taiwan data center portfolio
「台灣」 「資料中心」 列表 OR 目錄（DuckDuckGo 等）
「TPIX」 OR 「TWIX」 OR 「網際網路交換」 台灣 設施
```

---

## 5. 搜尋模板（Search Templates）

### 5.1 繁體中文模板

```text
「台灣」 （「資料中心」 OR 「數據中心」 OR 「機房」 OR 「主機代管」） （台北 OR 新北 OR 桃園 OR 台中 OR 台南 OR 高雄）
「縣市名」 （「資料中心」 OR 「機房」 OR 「雲端」 OR 「IDC」）
「中華電信」 （IDC OR 「資料中心」 OR 「機房」） （龍潭 OR 板橋 OR 內湖 OR 竹北 OR 中壢）
「是方電訊」 OR 「宏碁雲架構」 OR 「Vantage」 （資料中心 OR IDC OR 機房）
「Google」 OR 「微軟」 OR 「Microsoft」 台灣 （資料中心 OR 雲端 OR 區域）
「聯發科」 銅鑼 資料中心 OR 算力 OR 浸沒式
「科學園區」 （資料中心 OR 機房 OR 算力） （竹科 OR 中科 OR 南科）
（「海纜」 OR 「登陸站」） 台灣 （頭城 OR 淡水 OR 八里 OR 枋山 OR 金門）
「動土」 OR 「啟用」 資料中心 2025 OR 2026
```

### 5.2 English templates

```text
"Taiwan" ("data center" OR "data centre" OR colocation) (Taipei OR Taoyuan OR Tainan OR Kaohsiung OR Taichung)
"Taiwan" (Chunghwa OR CHT OR Chief OR Vantage OR MediaTek) "data center" OR colocation OR IDC
"Google" Taiwan data center (Changhua OR Tainan OR Yunlin) construction OR idle OR progress
"Microsoft" Taiwan data center region 2026 OR Azure
"Taiwan" submarine cable landing (Toucheng OR Tamsui OR Bali OR Fangshan OR Kinmen)
filetype:pdf Taiwan "data center" OR "資料中心" OR "機房"
"Taiwan" "data center" tender OR procurement 2025 OR 2026
```

---

## 6. Division 列舉（20 divisions）與 no_projects 記錄

| Division | 種子與預期 |
|---|---|
| Taipei | 是方（麗源／宏鼎、TPIX）、Vantage TPE11、CHT 內湖濱江（規劃）；DataCenterMap 17 座／9 家（C）。最高產出 |
| New Taipei | CHT 板橋（A，見官方檔）；淡水／八里登陸站；其餘負面 |
| Keelung | no_projects（U）：DataCenterMap 台灣目錄缺省檢查——CHT／是方／遠傳／台哥大／AWS／Azure／Google／Vantage 全缺席；僅電信交換/POP 預期 |
| Taoyuan | CHT 龍潭 AIDC（B/C）、Acer eDC 龍潭（B/C）、CHT 中壢仁美（C）；A-Top 傳聞（數位時代 B，北部） |
| Hsinchu | CHT 竹北 IDC（C，雙聚合器）；竹科內僅 CHT 局端（SIPA，官方檔） |
| Miaoli | 聯發科銅鑼 R&D DC（B，2026-05 啟用，15MW 一期／45MW 傳聞）；苗栗縣資訊中心（C，政府） |
| Taichung | DataHOUSE（C，https://www.datacenters.com/datahouse-taichung ）、VeeTIME（C，https://www.datacenterjournal.com/data-centers/taiwan/taichung/ ，內部不一致）、2013 NTT 中部雲端舊聞（C，https://windrivernews.pixnet.net/blog/post/320475770 ）；CHT 中部 >20MW AIDC 觀察項（B） |
| Changhua | Google 彰濱（A 官方，見官方檔）；維基（B，https://zh.wikipedia.org/zh-tw/Google台灣資料中心 ）US$780M 一期、數位時代（B）10 年、MyGoNews（B）US$600M、好房網（C）2013 臉書傳聞未證實 |
| Nantou | no_projects（U）：搜尋「南投 資料中心／機房／雲端／建置」「中興新村 資料中心／園區」無商業 DC；中興新村高教研究園區無 DC 證據 |
| Yunlin | Google 第 3 座（自由時報 B，2020；數位時代 C 進度超前；蕃新聞 C 購地） |
| Tainan | Google 2nd DC（B：數位時代 2025-03 未動工、好房網 2026 用地閒置）；NCHC 國網雲端（A 官方）；沙崙算力（C） |
| Kaohsiung | Foxconn DC（DCD B，2015）；CHT 亞灣（B）；亞灣 2.0 NVIDIA/AMD R&D（B）；楠梓 no_projects（U——僅 TSMC 廠、日月光物流測試建物） |
| Chiayi | 嘉義市綠能雲端（A 官方＋NOWnews/JWTnews B）；嘉義縣僅 TSMC CoWoS（Taipei Times B，無 DC 命名） |
| Pingtung | 枋山登陸站（CNA B）；no_projects（U）——無商業 DC |
| Hualien | no_projects（U）；CNA（B）負面背景：無登陸站 |
| Yilan | 頭城登陸站（NSTM B 館藏、Fount B）；TANet 宜蘭區網（A）；ilrc 機房頁（C，https://www.ilrc.edu.tw/p/404-1000-1094.php?Lang=zh-tw ：2×60KVA UPS、600KW 發電機、500L 油槽）；地熱（LINE Today C）；no_projects（U）商業 |
| Taitung | TANet 台東區網（A）；Arizton（C）缺席；no_projects（U）商業 |
| Penghu | CHT 本地電信（GSN A）；Arizton（C）缺席；no_projects（U） |
| Kinmen | 金廈海纜（Fount B、Flymia C）；CHT 烈嶼機房（zhupiter C）；Arizton（C）缺席；no_projects（U） |
| Lienchiang | 馬祖海纜斷纜（Up Media B）；TM3 南竿段（智瑞 C）；Arizton（C）缺席；no_projects（U） |

Division 查詢區塊：
```text
「台北」 OR 內湖 （「資料中心」 OR 機房 OR TPIX） （是方 OR Chief OR Vantage OR 中華電信）
「桃園」 （龍潭 OR 中壢 OR 蘆竹） （資料中心 OR IDC OR 機房）
「苗栗」 OR 銅鑼 （聯發科 OR 資料中心 OR 算力）
「台中」 OR 「雲林」 OR 「彰化」 （Google OR 資料中心 OR 雲端）
「台南」 OR 「高雄」 OR 「屏東」 （資料中心 OR 機房 OR 雲端 OR 海纜）
「宜蘭」 OR 「花蓮」 OR 「台東」 （資料中心 OR 機房 OR 海纜 OR 登陸站）
「澎湖」 OR 「金門」 OR 「馬祖」 OR 「連江」 （資料中心 OR 機房 OR 海纜）
```

負面搜尋規則：網路咖啡、電腦教室、NGO 伺服器室、GIS 室、軟體平台不計，除非來源描述具名營運商與地點之主機／代管／運算基礎設施。

---

## 7. 分級與驗證規則

- **A 營運設施**：官方／營運商／政府來源指明場址＋地點＋基礎設施功能。
- **B 營運設施**：強二級媒體指明場址／地點、足以區分設施，最好引述官方／營運商。
- **C 線索**：聚合器列示、社群／職缺貼文、轉售頁、無本地實體證據之服務頁（DataHOUSE、VeeTIME、CHT 中壢仁美、竹北、2013 NTT 舊聞、2013 臉書傳聞）。
- **U**：僅聚合器或單一弱來源；升級前複核（DataHOUSE、VeeTIME、TelecomGrid 36MW、竹北、中壢仁美、雲林進度）。
- **Provider-level 服務**：官方主機／雲／伺服器服務但無具名設施（CHT 服務、Acer eDC 服務）——分開記。
- **規劃／管道**：Google 台南（2019 宣布、閒置）、Google 雲林（2020 宣布、購地中）、CHT 內湖濱江（2025 宣布）、CHT 中南部 >20MW AIDC（2026 宣布、選址未定）、是方中科第 4 座（2026 宣布）——維持非營運狀態直到動工／啟用證據。
- **互連**：TPIX、TWIX、海纜登陸站、PeeringDB——非資料中心容量。
- **電信核心**：CHT／台哥大／遠傳／台灣大／亞太之核心機房僅在來源描述核心／網路／伺服器／主機基礎設施時計入。
- **容量**：除非官方／營運商／招標來源明示，否則保持 null（Vantage 16MW 官方；TelecomGrid 36MW C；Acer eDC 18,000 坪 B；聯發科 15MW 一期／45MW 傳聞 B）。
- **電力**：大型宣稱與台電供電、用電大戶義務、北部電力吃緊背景交叉（民報 B）。
- **雲**：Azure 台灣正證據（官方）；AWS/GCP/OCI 負證據（官方區域頁）。
- **去重**：一棟樓多營運者分開記（麗源 = LY IDC + TPIX）；一園區多棟分開記（麗源 vs 宏鼎）；同一設施多重宣稱並存（板橋 Rated 3+M&O vs 2016 Rated 4，現行官方頁為準）；登陸站／教育網路／電信交換／政府機房各按其類型記錄，不計為商業 colo。

---

## 8. 已驗證來源錨點（行業側，2026-08）

媒體：
- 工商時報：https://www.ctee.com.tw/ ；五大業者 https://www.ctee.com.tw/news/20250407700140-439901 ；78% 市占 https://www.ctee.com.tw/news/20260805701672-430502 ；宏碁雲架構 https://www.ctee.com.tw/news/20211028700464-431202 ；AIDC 大投資 https://www.ctee.com.tw/news/20260404700038-439901 ；聯發科 https://www.ctee.com.tw/news/20260507700774-430501
- 民報：https://www.peoplenews.tw/articles/economic-news/22942
- 自由時報：https://news.ltn.com.tw/news/life/breakingnews/3280940
- 數位時代：https://www.bnext.com.tw/article/76840/google-taiwan-data-center-10-years ；https://www.bnext.com.tw/article/82590/cloud-infrastructure-datacenter-taiwan-google-aws-microsoft-meta ；https://ai.bnext.com.tw/answer/google-13480-893905
- 鉅亨網：https://news.cnyes.com/news/id/6446719
- 鏡週刊：https://www.mirrormedia.mg/story/20260508fin001
- 商業周刊：https://wealth.businessweekly.com.tw/m/GArticle.aspx?id=ARTL001001955
- 中央社 CNA：https://www.cna.com.tw/news/aipl/202501100035.aspx
- 蕃新聞：https://n.yam.com/Article/20231222307761 ；https://n.yam.com/Article/20240305176189
- 好房網：https://news.housefun.com.tw/news/article/882897400263.html ；https://news.housefun.com.tw/news/article/533334113781.html
- NOWnews：https://www.nownews.com/news/3620157 ；JWTnews：https://www.jwtnews.biz/1080909-2.htm
- Taipei Times：https://www.taipeitimes.com/News/biz/archives/2025/09/24/2003844304 ；https://www.taipeitimes.com/News/front/archives/2025/01/03/2003829567
- MyGoNews：https://www.mygonews.com/news/detail/news_id/108024
- LINE Today：https://today.line.me/tw/v3/article/aGmgBqo
- 放言：https://www.fountmedia.io/article/265487 ；上報：https://www.upmedia.mg/tw/focus/politics/222474

國際媒體／部落格：
- Light Reading：https://www.lightreading.com/data-centers/vantage-data-centers-expands-into-taiwan-with-a-16mw-data-center
- DCD：https://www.datacenterdynamics.com/en/analysis/foxconn-wants-to-build-your-data-centers/
- TelecomGrid：https://telecomgrid.com/ai/chunghwa-telecom-powers-up-ai-future-with-36mw-data-center-in-taoyuan-taiwan/
- DataCenterJournal：https://www.datacenterjournal.com/data-centers/taiwan/taichung/

廠商／工程／部落格：
- TECO：https://tecoie.teco.com.tw/page/21 ；惠國科技：https://www.hgnet.com.tw/苗栗資訊中心更新建置案第一期工程/ ；智瑞科技：https://www.jhihrui.com.tw/blogs/news-20251017102206 ；Flymia：https://ppundsh.github.io/posts/b545/ ；zhupiter 烈嶼：https://ji.zhupiter.com/p-204996-中華電信南高雄營運處金門服務中心工務課網路股烈嶼機房.html ；台南新聞平台：https://qnews.tainanoutlook.com/news/8792805

聚合器：
- DataCenterMap 台北：https://www.datacentermap.com/taiwan/taipei/ ；台灣：https://www.datacentermap.com/taiwan/ ；板橋 https://www.datacentermap.com/taiwan/taipei/cht-taipei-banqiao-idc/ ；中壢仁美 https://www.datacentermap.com/taiwan/taoyuan/cht-zhongli-renmei-idc/ ；竹北 https://www.datacentermap.com/taiwan/zhubei/cht-hsinchu-zhubei-idc/
- Baxtel 竹北：https://baxtel.com/data-center/cht-hsinchu-zhubei-idc
- datacenters.com DataHOUSE：https://www.datacenters.com/datahouse-taichung
- Arizton：https://www.arizton.com/market-reports/taiwan-data-center-portfolio

Final note: 台灣市場已由官方檔（營運商官方頁、政府、雲區域）定調；本檔之媒體與聚合器證據（Vantage 進入、聯發科銅鑼、CHT 龍潭細節、Google 台南／雲林進度、台中弱線索、東部與離島負面）用於發現與佐證。所有 U/C 級項目（DataHOUSE、VeeTIME、竹北、中壢仁美、TelecomGrid 36MW、雲林進度、2013 舊聞）維持其真實等級直至複核。

## Review record

- Date: 2026-08-12
- Reviewer: gpt5.6-luna
- Conclusion: **REVISED**
- Key changes: confirmed all 20 manifest divisions are enumerated; added executable checks for 遠傳電信、台灣大哥大、亞太電信 and NEXTDC; added a provider-service versus physical-facility rule so brand, cloud, and Asia-Pacific market pages cannot inflate the facility count; preserved A/B/C/U and negative-search semantics.
