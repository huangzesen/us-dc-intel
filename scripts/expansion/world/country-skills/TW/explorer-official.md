# TW Explorer Official - 台灣資料中心列舉（官方／監管／政府／雲區域）

Date verified: 2026-08-12. Country: **TW - Taiwan, Province of China**（ISO 3166-1 alpha-2: TW；ISO 全名依 `world-manifest.jsonl`）。Angle: 以官方／監管／政府／雲區域來源識別資料中心設施、電信核心機房、政府主機代管基礎設施、國家級資料中心計畫與監理／許可訊號。行業／廠商／媒體／互聯來源見同目錄 `explorer-industry.md`，兩檔衝突時以本檔官方來源判定設施最終狀態。

Reliability grades:
- **A** = 官方或一手來源：政府機關頁面／公文書（地方政府、教育部 TANet、GSN、NCHC、SIPA、NSTM 館藏檔案）、營運商官方頁面與年報（中華電信 CHT、是方電訊 Chief、Vantage、Google／Microsoft 官方雲區域頁）、官方雲區域清單。
- **B** = 強二級來源：引述官方／營運商公告的正規媒體（工商時報、數位時代、中央社、Taipei Times、Light Reading 等）、官方新聞室／官方部落格。
- **C** = 僅線索：聚合目錄（DataCenterMap、Baxtel、datacenters.com、Arizton、DataCenterJournal、TelecomGrid）、無具名地點的廠商行銷、歷史未證實傳聞。
- **U** = 未驗證：僅見於聚合器或單一弱來源；升級前須複核。

Rule: 一條目之等級僅涵蓋其實際支持的事實。官方服務頁證明服務存在（A）不證明實體位址／機櫃數；政府公文證明電信基礎設施（A）不證明商業代管設施。

---

## 0. 結構事實（Structure Facts）

### 0.1 行政區模型（world-manifest divisions）

台灣在 `world-manifest.jsonl` 的子國家模型為 **county/city/special municipality**，恰為 **20 個 division**：Changhua, Chiayi, Hsinchu, Hualien, Yilan, Keelung, Kaohsiung, Kinmen, Lienchiang, Miaoli, Nantou, New Taipei, Penghu, Pingtung, Taoyuan, Tainan, Taipei, Taitung, Taichung, Yunlin。

注意模型細部：模型將 **Hsinchu**（新竹市＋新竹縣）與 **Chiayi**（嘉義市＋嘉義縣）各併為單一 division；本輪證據中「Hsinchu」下之設施證據位於新竹縣竹北市，「Chiayi」下之證據位於嘉義市。

| Division（模型名） | 中文 | 類型 | 資料中心要點摘要（本輪） |
|---|---|---|---|
| Taipei | 台北市 | 直轄市 | 內湖：是方電訊 LY（麗源大樓）／宏鼎大樓 AI IDC、TPIX 網際網路交換中心；Vantage TPE11（16MW，2024-07 啟用）；CHT 內湖濱江 IDC（規劃中） |
| New Taipei | 新北市 | 直轄市 | CHT 板橋 IDC（TIA-942 Rated 3 + Uptime M&O；2016 年報另稱 Rated 4）；板橋國慶路 8 號（聚合器） |
| Keelung | 基隆市 | 市 | 無商業資料中心（聚合器缺省檢查）；僅電信交換/POP 預期 |
| Taoyuan | 桃園市 | 直轄市 | CHT 龍潭 AIDC 園區（一期完成、啟用中）；Acer eDC 龍潭主機房；CHT 中壢仁美 IDC（聚合器） |
| Hsinchu | 新竹市／新竹縣 | 市＋縣（模型單一） | CHT 竹北 IDC（聚合器，新竹縣竹北）；竹科內僅 CHT 電信局端（SIPA 公文，非代管） |
| Miaoli | 苗栗縣 | 縣 | 聯發科銅鑼 R&D 資料中心（2026-05 啟用，全台首座浸沒式冷卻；行業來源，見 industry 檔） |
| Taichung | 台中市 | 直轄市 | 僅弱線索（DataHOUSE 聚合器、2013 NTT 舊聞）；CHT 中部 >20MW AIDC 為觀察項 |
| Changhua | 彰化縣 | 縣 | Google 彰濱工業區資料中心（2013 啟用，官方頁 A） |
| Nantou | 南投縣 | 縣 | 無已知商業資料中心（no_projects） |
| Yunlin | 雲林縣 | 縣 | Google 第 3 座資料中心（2020 宣布，雲林科技工業區竹圍子區；購地中） |
| Tainan | 台南市 | 直轄市 | Google 第 2 座（2019 宣布，用地閒置）；NCHC 國網雲端資料中心（南科，已啟用） |
| Kaohsiung | 高雄市 | 直轄市 | CHT 亞灣科技大樓（電信/雲基地）；Foxconn 高雄 DC（2015 行業來源）；NVIDIA/AMD 亞灣 R&D（政策樞紐）；無超大型 DC |
| Chiayi | 嘉義市 | 市 | 嘉義市綠能雲端資料中心（市府機房重建，2019-09 啟用） |
| Pingtung | 屏東縣 | 縣 | 枋山海纜登陸站（連通性）；無商業代管 |
| Hualien | 花蓮縣 | 縣 | 無資料中心；無海纜登陸站（負面背景） |
| Yilan | 宜蘭縣 | 縣 | 頭城海纜登陸站（連通性）；TANet 宜蘭區網中心（教育網路）；無商業代管 |
| Taitung | 台東縣 | 縣 | 僅 TANet 台東區網中心（東大）；無商業代管 |
| Penghu | 澎湖縣 | 縣 | 僅 CHT 本地電信設備（GSN 公告）；無資料中心 |
| Kinmen | 金門縣 | 縣 | 金廈海纜登陸（連通性）；CHT 烈嶼電信機房；無商業代管 |
| Lienchiang | 連江縣 | 縣 | 馬祖台馬海纜（斷纜依賴微波備援）；CHT 南竿機房；無商業代管 |

行政區驗證入口：`world-manifest.jsonl`（country_code TW，20 divisions）；縣市政府入口（如 tainan.gov.tw、chiayi.gov.tw 見第 9 節）；內政部行政區域查詢為行政事實錨點（非設施證據）。

### 0.2 註冊庫：存在與不存在

- **無公開國家級資料中心註冊庫**：沒有任何政府單頁列出營運中或規劃中資料中心。
- **無可可靠機器檢索的全國建照／使照資料庫**：大型開發需環評（環境部）與縣市政府建照，但無統整資料庫可直接搜尋資料中心專案。
- 最接近普查的組合：NCC 電信事業／頻率許可統計（執照清冊，非設施清冊）、NCHC／科學園區管理局公告、縣市政府新聞稿、GSN／TANet 網路中心清單、營運商官方頁（CHT 板橋、是方、Vantage）與官方雲區域清單。
- **官方雲區域清單同時是正證據（Azure 台灣）與負證據（AWS/GCP/OCI 無台灣區域）**，見第 3 節。
- 認證註冊庫：Uptime Institute / TIA-942 為設施等級的第三方佐證來源；台灣已驗證案例僅 CHT 板橋（官方頁稱 Rated 3 + Uptime M&O；2016 年報稱 Rated 4——並存記錄，見 6 節去重規則）。

### 0.3 法律與監理基礎

- **NCC（國家通訊傳播委員會）**：電信／通訊傳播監理機關；`電信管理法`（2020-07 施行）下的電信事業許可、網路互連與頻率管理。執照清冊是營運商普查來源，**執照不等於資料中心設施**。入口錨點：https://www.ncc.gov.tw/ （官方入口，供檢索；非本次證據）。
- **數位發展部（moda，2022-08-27 成立）**：數位基礎建設、資通安全政策、政府網路（GSN 政府網際服務網）之政策主管。入口錨點：https://www.moda.gov.tw/ 。本次已驗證之政府網路證據：GSN 澎湖 CHT 設備維護公告（A，2025-07-17）。
- **教育部 TANet 區域網路中心**：台東（國立台東大學）、宜蘭（國立宜蘭大學）、高屏澎（中山大學）等；教育網路機房，非商業代管（A 級證據見 2.3）。
- **國科會 NSTC／NCHC（國家高速網路與計算中心）**：NCHC 營運「國網雲端資料中心」（台南，南部科學園區，2023-03 動土、2025 完成、已啟用，A）；科學園區管理局（SIPA 竹科、中科、南科）管理園區土地與基礎建設，SIPA 公文證實竹科電信由 CHT 獨家提供（U，非代管 DC）。
- **個人資料保護法（PDPA）**：資料保護為監理／需求背景（本地代管需求動機），不是設施證據。
- **能源與電力**：台電（Taipower）供電；「用電大戶」再生能源義務；北部電力吃緊（民報 2026-03-24 引是方：北部電力吃緊、機房滿載 → 南下設 AIDC）為選址背景。台電入口錨點：https://www.taipower.com.tw/ 。
- **環境影響評估（環境部）**：大型資料中心專案之環評為動工級證據之一（本輪無已驗證環評記錄）。
- **TWNIC（財團法人台灣網路資訊中心）**：.tw 註冊管理機構與 TWIX 網際網路交換（互連錨點，非設施）。入口錨點：https://www.twnic.tw/ 。
- **投資主管機關**：經濟部「投資台灣事務所」為外資／投資公告入口（Google、Microsoft 投資公告常經此發布）；本輪 Google／Microsoft 證據以營運商官方頁與縣市政府為準。

---

## 1. 搜尋詞彙（Search Vocabulary）

台灣以繁體中文與英文為主。繁體中文召回最佳；英文次之（設施品牌名、認證名）。

繁體中文：資料中心、數據中心、機房、雲端、雲端資料中心、主機代管、代管、網際網路交換中心、網際網路交換、海纜、登陸站、光纖、伺服器、IDC、AI 資料中心、AIDC、算力、園區、科學園區、工業區、綠電、再生能源、用電大戶、環評、建照、使照、動工、動土、開工、啟用、營運、招標、決標、發包。

English: data center, data centre, datacenter, colocation, cloud region, availability zone, internet exchange point, IXP, submarine cable, cable landing station, point of presence, tier III, tier IV, Uptime Institute, TIA-942, rack space, MW, IT load, renewable energy, PPA, hyperscaler, sovereign cloud.

Lifecycle 動詞（中英來源捕捉）：projet／意向／MoU／規劃（意向）；招標／決標／tender／awarded（採購）；動工／動土／breaking ground（施工中）；啟用／營運／inaugurated／go-live（營運中）；取消／延宕／閒置／idle（負面狀態）。

---

## 2. 官方與監理管道（Official And Regulatory Pipeline）

### 2.1 NCC - 電信監理（執照普查，非設施清冊）

- 入口：https://www.ncc.gov.tw/ ；電信管理法框架下之電信事業許可、頻率、互連。
- 用法：以 NCC 執照／營運商清冊建立營運商清單（CHT、台灣大哥大、遠傳、亞太電信、是方電訊等），再以營運商官方頁確認設施。NCC 執照本身**不是**資料中心設施證據。

查詢：
```text
site:ncc.gov.tw 電信事業 許可 OR 執照 OR IDC OR 資料中心
site:ncc.gov.tw 網際網路交換 OR IXP OR 互連
「NCC」台灣 「資料中心」 OR 「IDC」 OR 主機代管 執照
```

### 2.2 moda／NICS／GSN - 數位政策、資安、政府網路

- moda：https://www.moda.gov.tw/ （數位基礎建設政策）。
- GSN 政府網際服務網：政府骨幹網路；已驗證證據：**GSN 澎湖公告**（2025-07-17，CHT 澎湖地區設備維護造成約 30 分鐘 GSN 電路中斷）→ 證明澎湖僅有 CHT 本地電信網路設備，無資料中心（A）。

查詢：
```text
site:moda.gov.tw 資料中心 OR 機房 OR 算力 OR 數位基礎建設
site:gsn.nat.gov.tw 資料中心 OR 機房 OR 中華電信 OR 設備
「政府網際服務網」 OR GSN 台灣 資料中心 OR 機房
```

### 2.3 教育部 TANet 區域網路中心（教育網路，非商業代管）

已驗證（A）：
- **台東區網中心**：國立台東大學（TANet-NTTU-NTSR760 設備遷移公告）：https://ttrc.nttu.edu.tw/ 。
- **教育部 TANet 區域網路中心清單**（確認台東區網中心設於東大；高屏澎區網中心設於中山大學、服務澎湖——澎湖無本地區網中心／資料中心）：https://depart.moe.edu.tw/ED2700/cp.aspx?n=FBB9B41A2800414D 。
- **宜蘭區網中心**：國立宜蘭大學（TANet-NIU-NTSR760 設備遷移公告，via ttrc.nttu.edu.tw 公告）。

查詢：
```text
site:depart.moe.edu.tw TANet 區域網路中心 列表 OR 清單
site:ttrc.nttu.edu.tw 機房 OR 遷移 OR 設備
「TANet」 台灣 區網中心 機房 台東 OR 宜蘭 OR 澎湖
```

### 2.4 國科會 NCHC 與科學園區管理局

已驗證（A）：
- **NCHC 國網雲端資料中心（台南）**：2023-03-27 於南部科學園區（台南）動土，約 800 機櫃，目標 2025 完成；目的為吸引國際海纜與雲端營運商進駐、提升台灣 IDC 容量。NCHC 官方動土記錄：https://www.nchc.org.tw/Videos/VideoView/44?mid=55&page=1 ；NCHC 頁面：https://www.nchc.org.tw/Page?itemid=118&mid=216 （台南雲端算力中心已啟用，支援超級電腦／AI 研究）。台南市政府動土新聞稿：https://www.tainan.gov.tw/News_Content.aspx?n=13370&s=8176319 。
- **SIPA 竹科公文（U，非代管）**：新竹科學園區管理局「湖濱一路宿舍興建工程長中長期個案計畫（核定本，2023-09）」：園區電信服務由 CHT 獨家提供、2.5 萬門交換容量——證實園區內為 CHT 電信基礎設施，**非商業代管資料中心**：https://www.sipa.gov.tw/uploaddowndoc?flag=doc&file=/pubdata/form/202601020944370.pdf 。

查詢：
```text
site:nchc.org.tw 國網 OR 雲端 OR 資料中心 OR 台南 OR 算力
site:sipa.gov.tw 電信 OR 機房 OR 資料中心
site:stsp.gov.tw OR site:ctsp.gov.tw 資料中心 OR 機房 OR 算力
「國網雲端資料中心」 台南 OR 南科
```

### 2.5 地方政府公告（投資與設施訊號）

已驗證（A）：
- **台南市政府（2019-09-11）**：Google 宣布於台南科技工業園區（安南區）取得資料中心用地並購買當地綠電——Google 在台第 2 座資料中心：https://www.tainan.gov.tw/en/News_Content.aspx?n=13205&s=4239338 。
- **嘉義市政府（2019-09-09）**：「綠能雲端資料中心」啟用（市府機房重建，與台達電、敦陽科技合作；熱通道／冷通道封閉、異地備援；台中以南區域樞紐）：https://www.chiayi.gov.tw/News_Content.aspx?n=454&s=401590 。市府機房重建，**非商業代管**。

查詢：
```text
site:tainan.gov.tw Google OR 資料中心 OR 雲端 OR 算力
site:chiayi.gov.tw 雲端 OR 資料中心 OR 機房 OR 綠能
site:*.gov.tw 資料中心 動土 OR 啟用 OR 招標（縣市層級）
```

### 2.6 營運商官方頁面與年報

已驗證（A）：
- **是方電訊 Chief Telecom**：
  - TPIX 官方 datasheet（2020-09）：TPIX 網際網路交換中心設於 LY IDC（麗源大樓），台北市內湖區陽光街 250 號，11491——內湖載波中立（carrier-neutral）共置樞紐：https://en.chief.com.tw/wp-content/uploads/2020/09/TPIX.pdf 。
  - 官方 IDC 頁（存取 2026-08-12）：載波中立、10,000+ 坪樓板、ISO／DCOS-4 認證；台北內湖麗源／宏鼎設施：https://www.chief.com.tw/idc/ 。
  - LY2 麗源大樓 AI IDC 官方頁：是方聯雲 AI 智能資料中心，宏鼎大樓雙節點設計（內湖科技園區）：https://www.chief.com.tw/resource/video/moneydjly2-2/ 。
- **中華電信 CHT**：
  - CHT IDC 官方頁（板橋 IDC，新北市板橋區）：台灣首座取得 TIA-942 Rated 3 與 Uptime Institute M&O 認證之資料中心：https://www.idc.hinet.net/chtidc_eng/Environment_Location_Taipei_Banqiao.html 。
  - CHT 2016 年報（2017-05-23）：板橋 IDC 暨雲端資料中心 2016-07-29 啟用，TIA-942 Rated 4，綠色資料中心園區：https://www.cht.com.tw/home/cht/-/media/Web/PDF/Investors/Annual-Report/2016/20170523_annual_report2016_ch.pdf 。
- **Vantage Data Centers**：官方頁（存取 2026-08-12）：TPE11 五層載波中立 DC，16MW IT 負載、215k 平方呎，2024-07 啟用；行銷為台北園區（距桃園機場約 35 分鐘），頁面未載明確切市區地址：https://vantage-dc.com/data-center-locations/apac/taipei-taiwan/ 。

查詢：
```text
site:chief.com.tw IDC OR TPIX OR 麗源 OR 宏鼎 OR 資料中心
site:cht.com.tw OR site:idc.hinet.net IDC OR 板橋 OR 資料中心 OR 龍潭
site:vantage-dc.com taipei OR taiwan
site:acer-edc.com 龍潭 OR 資料中心（Acer eDC 官方頁，本輪未驗證到官方頁）
```

### 2.6a 電信商／IDC 供應商交叉檢查（provider-level，不等同實體設施）

CHT、是方之外，應固定檢查 **遠傳電信、台灣大哥大、亞太電信** 的企業雲／IDC／主機代管頁面；這些頁面若只證明服務或品牌，記為 `provider_service`，不得直接建立具名資料中心。**NEXTDC** 亦列入反向查詢：本輪未把 NEXTDC 台灣字樣或亞太市場頁面視為台灣設施，只有官方頁面同時給出可定位的台灣站點與基礎設施時才升級。

```text
site:fareastone.com.tw （IDC OR "資料中心" OR 雲端 OR 主機代管）
site:taiwanmobile.com （IDC OR "資料中心" OR 雲端 OR 主機代管）
site:aptg.com.tw （IDC OR "資料中心" OR 雲端 OR 主機代管）
site:nextdc.com Taiwan OR 台灣 OR Taipei
```

判定規則：服務型頁面＝A（provider-level 服務存在）但不證明地址／機櫃；官方設施頁、年報或許可文件同時指明站點與功能才可建立 `commercial_colocation`／`telco_core`。未找到台灣實體站點時保留 `negative` 或 `U`，並注明查詢日期。

### 2.7 官方雲區域清單（正／負證據）

- **Microsoft Azure - 台灣區域（正證據，A）**：官方部落格（2025-10-09）宣布 2026 年啟用 Azure 台灣資料中心區域（與印度同步）：https://azure.microsoft.com/en-us/blog/microsofts-commitment-to-supporting-cloud-infrastructure-demand-in-asia/ ；Microsoft Datacenters 台灣地理頁（「Reimagine Taiwan」計畫下第一個資料中心區域，位置未公開）：https://datacenters.microsoft.com/globe/explore/?info=geography_taiwan ；台灣微軟新聞室（2024-11-14）：Microsoft 365 台灣資料落地服務正式啟用（台灣資料中心第一階段），城市未公開：https://news.microsoft.com/zh-tw/microsoft-365ga/ 。
- **Google - 台灣資料中心（正證據，A）**：官方位置頁（2023-09-26）：台灣資料中心位於彰化縣線西鄉彰濱工業區，2013 年首座啟用並持續擴建：https://datacenters.google/intl/zh-TW_ALL/locations/taiwan/ 。注意：Google 在台為資料中心（data center），非 Google Cloud 區域（region）——官方 Google Cloud locations 清單不含台灣，最近區域為東京／大阪／新加坡（負面證據）。
- **AWS / OCI（負證據）**：官方區域清單無台灣區域（最近為東京／新加坡／首爾／香港等）；Oracle OCI 亦無台灣區域。

查詢：
```text
site:microsoft.com taiwan datacenter region OR geography
site:datacenters.microsoft.com taiwan
site:datacenters.google taiwan OR changhua OR 彰化
site:aws.amazon.com regions taiwan（負面確認）
site:docs.oracle.com regions taiwan（負面確認）
```

---

## 3. 雲區域、邊緣與互連訊號（含負面證據）

| 訊號 | 來源 | 台灣解讀 |
|---|---|---|
| Azure 台灣區域 | 官方部落格 2025-10-09；Microsoft Datacenters 地理頁；M365 新聞室 2024-11-14 | 2024 第一階段（M365 資料落地）已啟用；2026 正式區域啟用；區域計畫由 3-4 座資料中心組成（Taipei Times 2025-09-24，B）；城市級位置未公開 |
| Google 台灣 DC | 官方位置頁（彰化，2013 啟用）；台南（2019 宣布、用地閒置）；雲林（2020 宣布、購地中） | Google 資料中心 ≠ Google Cloud 區域；官方 locations 清單無台灣雲區域（負面） |
| AWS / GCP / OCI 區域清單 | 官方區域頁 | 無台灣區域（負面證據，本地無超大型雲區域） |
| TPIX（台北網際網路交換中心） | 是方 TPIX datasheet（A，2020-09） | 設於麗源大樓（內湖）；互連基礎設施，非資料中心容量本身 |
| TWIX / TWNIC | TWNIC（官方入口錨點） | .tw 註冊與網際網路交換；互連錨點 |
| 海纜登陸站 | CNA 2025-01-10（B）：淡水、八里、頭城、屏東（枋山）；Fount Media（B）：5 站點 14 條海纜（頭城、淡水、八里、枋山、金門）；Flymia（C）：金廈海纜（金門-廈門，約 21km）；智瑞科技（C）：台馬 3 號（TM3）南竿段距南竿機房 7.7km | 連通性基礎設施，**不得計為資料中心**；登陸站所在縣市（宜蘭頭城、新北淡水／八里、屏東枋山、金門、連江南竿）無商業代管證據 |
| GSN 澎湖公告 | GSN 官方（A，2025-07-17） | 澎湖僅 CHT 本地電信設備維護；無資料中心 |
| TANet 區網中心（台東、宜蘭、高屏澎） | 教育部／東大／宜大官方（A） | 教育網路機房；非商業代管 |

資料落地（data residency）背景：Microsoft 365 台灣資料落地 2024-11-14 啟用；PDPA 為監理背景——均為需求動機，非設施證據。

---

## 4. 設施與專案種子清單（2026-08 證據狀態）

| 候選 | 狀態 | 等級 | 地點處理 | 為何重要／證據 |
|---|---|---|---|---|
| 是方電訊 LY IDC（麗源大樓）＋TPIX | 營運中（IXP 於 2020-09 datasheet） | A（官方 datasheet／官方頁） | 台北市內湖區陽光街 250 號，11491 | 載波中立共置樞紐；官方 IDC 頁稱 10,000+ 坪、ISO／DCOS-4 |
| 是方電訊宏鼎大樓／LY2 AI IDC | 營運中（行銷中） | A（官方頁） | 台北內湖科技園區（宏鼎大樓） | LY2 官方頁：是方聯雲 AI 智能資料中心、雙節點設計 |
| Vantage TPE11 | 營運中（2024-07 啟用） | A（官方頁） | 台北園區（頁面未載確切地址；距桃園機場約 35 分鐘） | 16MW IT 負載、215k 平方呎、五層；Light Reading（B）佐證 |
| CHT 板橋 IDC | 營運中（2016-07-29 啟用） | A（官方頁／年報） | 新北市板橋區國慶路 8 號（聚合器 C） | TIA-942 Rated 3 + Uptime M&O（官方頁）；2016 年報稱 Rated 4——並存記錄 |
| CHT 龍潭 AIDC 園區 | 一期完成、啟用中 | B（媒體引官方）；C（36MW 部落格） | 桃園龍潭 | 工商時報 2025-04-07（一期完成）、2026-08-05（啟用案例）；TelecomGrid 稱滿載可達 36MW（C） |
| CHT 中壢仁美 IDC | 僅聚合器列示 | C | 桃園中壢 | DataCenterMap：https://www.datacentermap.com/taiwan/taoyuan/cht-zhongli-renmei-idc/ |
| CHT 內湖濱江 IDC 大樓 | 規劃中 | B | 台北內湖 | 工商時報 2025-04-07：龍潭一期後續建置 |
| CHT 竹北 IDC | 僅聚合器列示 | C | 新竹縣竹北市 | DataCenterMap＋Baxtel 雙聚合器；無官方頁 |
| Acer eDC 龍潭主機房 | 營運中 | B（媒體）；C（廠商案） | 桃園龍潭 | 工商時報 2021-10-28：18,000 坪、7 級耐震、99.999% 設計；TECO 工程案（C）佐證 |
| Microsoft Azure 台灣區域 | 2024 第一階段啟用；2026 區域啟用 | A（官方） | 城市未公開 | 官方部落格／Datacenters 地理頁／M365 新聞室；3-4 座 DC（B） |
| Google 彰化資料中心 | 營運中（2013 起擴建） | A（官方位置頁） | 彰化縣線西鄉彰濱工業區 | 官方頁；首座亞太 DC（數位時代 B）、US$600M 投資（MyGoNews B）、US$780M 一期（維基 B） |
| Google 台南資料中心 | 2019 宣布，用地閒置（2025-2026） | A（宣布）；B（現況） | 台南科技工業園區（安南區） | 台南市政府 A；數位時代 2025-03（未動工）、好房網 2026（議會質詢用地閒置） |
| Google 雲林資料中心 | 2020 宣布，購地／進度中 | B（宣布）；C（進度） | 雲林科技工業區竹圍子區（斗六） | 自由時報 2020-09-03（第 3 座、約 20 公頃、NT$200 億）；數位時代 AI 問答 C（進度超前）；官方無雲林頁 |
| NCHC 國網雲端資料中心（台南） | 已啟用（2025 完成） | A | 南部科學園區（台南） | NCHC＋台南市政府：約 800 機櫃，吸引海纜／雲端業者；國家級 IDC |
| CHT 亞灣科技大樓（高雄） | 營運中（電信／雲基地） | B（CNA 轉載） | 高雄亞洲新灣區 | 5G 網路切片首個驗證場域、+500 技術人員（蕃新聞 2023-12-21） |
| 嘉義市綠能雲端資料中心 | 營運中（2019-09-09 啟用） | A（市政府） | 嘉義市 | 市府機房重建（台達電、敦陽科技）；年省 20 萬 kWh、110t CO2（NOWnews B）——政府機房，非商業 colo |
| 南投／基隆／花蓮／澎湖／金門／連江／台東商業／宜蘭商業／屏東商業 | 無已知專案 | U（負面） | 各縣市 | no_projects 記錄（搜尋細節見 industry 檔第 6 節） |

---

## 5. 每 Division 列舉要點（Per-Division Enumeration Approach）

每個列舉週期跑全部 20 個 division；無活動者記錄 `no_projects`。市場集中於北台灣（台北／新北／桃園）與超大型業者選址（彰化、台南、雲林、苗栗）；東部與離島以負面結果為主。

1. **台北**：是方（麗源／宏鼎、TPIX）、Vantage TPE11、CHT 內湖濱江（規劃）。最高產出 division；DataCenterMap 列 17 座 DC／9 家營運商（C，交叉檢查用）。
2. **新北**：CHT 板橋 IDC（唯一已驗證大型 colo）；淡水／八里海纜登陸站（連通性）。
3. **基隆**：預期負面；僅電信交換／POP。查：基隆 機房／資料中心／IDC。
4. **桃園**：CHT 龍潭 AIDC（一期）、Acer eDC 龍潭、CHT 中壢仁美（C）；A-Top 園區為 AWS/MSFT/Meta 傳聞地（數位時代 2025-03，北部、超出本輪範圍）。
5. **新竹**：CHT 竹北 IDC（C）；竹科內僅 CHT 電信局端（SIPA U）。
6. **苗栗**：聯發科銅鑼 R&D DC（2026-05 啟用；行業來源）；苗栗縣資訊中心更新案（C，政府機房）。
7. **台中**：僅弱線索（DataHOUSE C、2013 NTT 舊聞 C）；CHT 中部 >20MW AIDC 為觀察項（B，2026-04-04）。
8. **彰化**：Google 彰濱工業區（A）。
9. **南投**：no_projects（中興新村研究園區無 DC 證據）。
10. **雲林**：Google 第 3 座（2020 宣布；購地／進度中，B/C）。
11. **台南**：Google 第 2 座（2019 宣布、閒置）；NCHC 國網雲端資料中心（A）；沙崙智慧綠能科學城算力（C）。
12. **高雄**：CHT 亞灣、Foxconn DC（2015，B）、NVIDIA/AMD 亞灣 R&D；楠梓無 DC（no_projects）。
13. **嘉義**：嘉義市綠能雲端資料中心（A）；嘉義縣科學園區僅 TSMC CoWoS 封裝廠（B，無 DC 命名）。
14. **屏東**：枋山海纜登陸站（B）；無商業代管（U）。
15. **花蓮**：no_projects；無海纜登陸站（負面背景）。
16. **宜蘭**：頭城海纜登陸站（B/C）；TANet 宜蘭區網（A）；地熱綠電為潛在未來（C）。
17. **台東**：僅 TANet 台東區網（A）；商業負面。
18. **澎湖**：僅 CHT 本地電信（GSN A）；負面。
19. **金門**：金廈海纜登陸（B/C）；CHT 烈嶼機房（C）；負面。
20. **連江**：馬祖海纜（台馬 3 號等，斷纜依微波備援）；CHT 南竿機房（C）；負面。

查詢區塊（官方角度）：
```text
site:*.gov.tw 「資料中心」 OR 「機房」 OR 「雲端」 動土 OR 啟用 OR 招標
site:ncc.gov.tw 資料中心 OR IDC OR 主機代管
site:moda.gov.tw 資料中心 OR 算力 OR 數位基礎建設
site:nchc.org.tw 國網 OR 雲端 OR 資料中心
「中華電信」 「資料中心」 OR IDC 龍潭 OR 板橋 OR 內湖 OR 竹北
「是方電訊」 OR Chief 資料中心 OR IDC OR TPIX
site:datacenters.google taiwan；site:datacenters.microsoft.com taiwan；site:azure.microsoft.com taiwan region
「Google」 台灣 資料中心 彰化 OR 台南 OR 雲林
「NCC」 OR 「電信管理法」 資料中心 OR IDC 執照
```

---

## 6. 計數、分級與去重規則（官方角度）

- 設施只有在來源同時指明基礎設施**與**足以區分實體場址的地點時才成立。未具名場址的行銷主機代管／雲服務是 provider-level 服務線索（分開記）。
- `facility_type` 精確度：`commercial_colocation`、`telco_core`、`ixp`、`government_hosting`、`planned_commercial_dc`、`hyperscale_dc`、`cable_landing`、`edu_network`、`telecom_exchange`、`lead_only`、`negative`。
- `status` 精確度：`operational`、`marketed_service`、`announced`、`mou`、`procurement`、`under_construction`、`unknown`、`negative`。
- 容量欄位（MW／機櫃／樓板）除非官方／營運商／招標來源明示，否則保持 null。Vantage 16MW 為官方頁數值；TelecomGrid 36MW 為 C 級部落格數值；NCHC 800 機櫃為官方；Acer eDC 18,000 坪為媒體引述（B）。
- 雲區域：Azure 台灣為唯一官方宣布之台灣雲區域（A）；AWS/GCP/OCI 無台灣區域（負面）。Google 在台資料中心與 Google Cloud 區域是兩件事，不可混記。
- **去重反例規則（De-dup counterexamples）**：
  - 同一棟樓多營運者：麗源大樓 = LY IDC + TPIX —— 一棟樓、按功能分開記（IDC 與 IXP 各自一條）。
  - 同一園區多棟：麗源大樓 vs 宏鼎大樓（LY2）—— 不同棟、分開記，不併為「是方內湖」。
  - 同一設施多重宣稱：板橋 IDC 官方頁稱 TIA-942 Rated 3 + Uptime M&O，2016 年報稱 Rated 4 —— 同一設施不同時期宣稱，並存記錄，以現行官方頁為準，升級認證需 Uptime/TIA 官方紀錄。
  - 海纜登陸站 ≠ 資料中心：頭城、淡水、八里、枋山、金門登陸站為連通性設施，記錄為 `cable_landing`。
  - 教育網路中心 ≠ 商業代管：TANet 台東（東大）、宜蘭（宜大）、高屏澎（中山）為 `edu_network`。
  - 電信交換機房 ≠ 資料中心：金門烈嶼機房、馬祖南竿機房、澎湖 CHT 設備為 `telecom_exchange`。
  - 政府資訊中心重建 ≠ 商業代管：嘉義市綠能雲端資料中心、苗栗縣資訊中心更新案為 `government_hosting`。
  - 宣布 ≠ 營運：Google 台南（2019 宣布、2026 仍閒置）、Google 雲林（2020 宣布、購地中）、Azure 台灣（2024 第一階段、2026 區域）——維持其真實 status。
  - 科學園區電信局端 ≠ 代管 DC：SIPA 竹科公文證實 CHT 電信交換容量，非商業 colo。
- 負面搜尋規則：網路咖啡、電腦教室、NGO 伺服器室、GIS 室、軟體平台，除非來源描述具名營運商與地點的主機／代管／運算基礎設施，否則不計。

---

## 7. 來源優先清單（官方角度）

1. NCC 執照／統計、電信管理法公告。
2. moda／NICS 政策（數位基礎建設、資安、GSN）。
3. 教育部 TANet 區網中心清單與公告。
4. NCHC 專案頁、科學園區管理局（SIPA／中科／南科）公文與公告。
5. 縣市政府新聞稿（台南、嘉義已驗證 A）。
6. 營運商官方頁與年報（CHT、是方、Vantage；Acer eDC 官方頁待補）。
7. 官方雲區域清單（Azure 台灣正證據；AWS/GCP/OCI 負證據）。
8. 強二級媒體引官方（工商時報、數位時代、中央社、Taipei Times）。
9. 聚合器（DataCenterMap、Baxtel、datacenters.com、Arizton）僅作 C/U 發現用。

---

## 8. 更新／複查節奏

- **每季**：官方雲區域清單（Azure 台灣 2026 啟用觀察）、NCC 執照頁、營運商官方頁（CHT／是方／Vantage）與 Acer eDC 官方頁補齊。
- **每季**：CHT 內湖濱江、台中／南部 >20MW AIDC 選址、Google 台南／雲林動工訊號（縣市政府＋官方頁）。
- **半年**：NCHC／科學園區管理局公告、moda 政策頁、TANet 清單異動。
- **每年**：複核全部 U 級聚合器列示（CHT 竹北、中壢仁美、DataHOUSE）；確認 Uptime Institute／TIA-942 認證現況。
- **事件驅動**：Azure 台灣區域正式啟用（城市揭露）、Google 台南／雲林動工、聯發科銅鑼擴建——任一發生即為最大變數。

## 9. 已驗證來源錨點（官方側，2026-08）

政府／監理：
- 教育部 TANet 清單：https://depart.moe.edu.tw/ED2700/cp.aspx?n=FBB9B41A2800414D
- 台東區網中心（東大）：https://ttrc.nttu.edu.tw/
- GSN 澎湖公告：https://gsn.nat.gov.tw/GSNConstructions/ConstructionsContents/19029e4f74600000227f
- NCHC 動土記錄：https://www.nchc.org.tw/Videos/VideoView/44?mid=55&page=1 ；NCHC 台南雲端算力頁：https://www.nchc.org.tw/Page?itemid=118&mid=216
- SIPA 竹科核定本：https://www.sipa.gov.tw/uploaddowndoc?flag=doc&file=/pubdata/form/202601020944370.pdf
- 台南市政府（Google 2019）：https://www.tainan.gov.tw/en/News_Content.aspx?n=13205&s=4239338
- 台南市政府（NCHC 2023）：https://www.tainan.gov.tw/News_Content.aspx?n=13370&s=8176319
- 嘉義市政府（綠能雲端資料中心）：https://www.chiayi.gov.tw/News_Content.aspx?n=454&s=401590
- NSTM 電信文物典藏（頭城登陸站，館藏檔案）：https://telecom.nstm.gov.tw/ArtifactDetail.aspx?sid=997

營運商官方：
- 是方 TPIX datasheet：https://en.chief.com.tw/wp-content/uploads/2020/09/TPIX.pdf
- 是方官方 IDC 頁：https://www.chief.com.tw/idc/
- 是方 LY2 AI IDC 官方頁：https://www.chief.com.tw/resource/video/moneydjly2-2/
- CHT IDC 板橋官方頁：https://www.idc.hinet.net/chtidc_eng/Environment_Location_Taipei_Banqiao.html
- CHT 2016 年報：https://www.cht.com.tw/home/cht/-/media/Web/PDF/Investors/Annual-Report/2016/20170523_annual_report2016_ch.pdf
- Vantage 台北官方頁：https://vantage-dc.com/data-center-locations/apac/taipei-taiwan/

雲區域官方：
- Azure 部落格（2026 區域）：https://azure.microsoft.com/en-us/blog/microsofts-commitment-to-supporting-cloud-infrastructure-demand-in-asia/
- Microsoft Datacenters 台灣地理：https://datacenters.microsoft.com/globe/explore/?info=geography_taiwan
- 台灣微軟新聞室（M365 資料落地）：https://news.microsoft.com/zh-tw/microsoft-365ga/
- Google 台灣資料中心官方位置頁：https://datacenters.google/intl/zh-TW_ALL/locations/taiwan/

Final note: 台灣是成熟的電信營運商主導市場，官方／監理證據以 CHT、是方、Vantage 官方頁、地方政府公告、NCHC／TANet／GSN 政府網路與 Azure／Google 官方雲頁為骨幹；Google 台南／雲林與 Azure 台灣為 2026 年最重要觀察項。聚合器與媒體（見 industry 檔）僅作發現與佐證，不改變官方檔判定之設施狀態。

## Review record

- Date: 2026-08-12
- Reviewer: gpt5.6-luna
- Conclusion: **REVISED**
- Key changes: confirmed the 20-division manifest coverage; added provider-level screening for 遠傳電信、台灣大哥大、亞太電信 and NEXTDC; clarified that service/market pages do not establish a physical Taiwan facility; retained cloud-region, AI/AIDC, IDC, telco-core, cable-landing, education-network, and government-hosting distinctions with A/B/C/U handling.
