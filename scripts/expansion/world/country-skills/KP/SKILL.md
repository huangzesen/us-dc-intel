---
name: "kp-datacenter-methodology"
location: scripts/expansion/world/country-skills/KP/SKILL.md
description: "Korea, Democratic People's Republic of (KP / North Korea) datacenter & IT-infrastructure discovery methodology — how to enumerate, verify, and update DPRK state IT facilities, government-hosting infrastructure (Kwangmyong intranet / Naenara), telco cores, semiconductor/electronics plants, and sanctions documentation at capital city/province/special city/metropolitan city granularity (13 divisions in the current manifest: 1 capital + 9 provinces + 1 metropolitan city + 2 special cities). KP is a closed state: no public licensing authority, no facility registry, no independent domestic press, no operator disclosure. Official evidence = international sanctions documentation (UN Security Council resolutions, Panel of Experts reports, MSMT, US Treasury OFAC designations) plus ROK government compilations (ROK Ministry of Unification NK Information Portal, NIA K2Base). DPRK state media are NOT official evidence (C at most). No commercial datacenter exists anywhere in KP; hyperscaler region lists are negative evidence. Low-exposure boundary: city/province context only, no precise coordinates, security layouts, personnel, or targeting inferences. Read this before running KP exploration/audit batches; routes to explorer-official.md (sanctions/ROK-government pipeline) and explorer-industry.md (OSINT/think-tank/media discovery)."
---

# KP · 朝鮮數據中心查詢方法論（Datacenter Discovery & Audit Methodology）

> 目的：朝鮮（DPRK）是封閉國家——**沒有**公開許可機關、沒有設施註冊庫、沒有獨立國內媒體、沒有營運商披露。外部可驗證性接近零；**全境沒有任何已確認的商業資料中心**，「行業」即國家 IT 機器（state IT apparatus）與其支撐網絡。
> 對本國而言「官方」證據指 **(a) 國際制裁文件**（UN 安理會決議與 Panel of Experts 報告、UNSCR-2270 基礎的 MSMT、US Treasury OFAC 指定）＋ **(b) ROK/韓國政府彙編**（統一部北韓資訊入口、NIA K2Base 研究入口）；**DPRK 官方媒體不算官方證據**（宣傳級，至多 C）。
> 本 skill 匯總兩份已審定（luna max Review record）的探索報告，作為朝鮮探索與複核批次的入口；衝突時以制裁文件/ROK 政府彙編判定設施最終狀態。

## 入口

| 文件 | 管線 | 內容 |
| --- | --- | --- |
| `explorer-official.md` | 官方/監管管線 | UN 制裁體制（UNSCR 1718/2270、Panel of Experts、MSMT/Japan MOFA）、OFAC 指定（KCC sm0099）、ROK 統一部北韓資訊入口、NIA K2Base、DPRK 官方媒體明確排除規則、低暴露處理、13 division 列舉工作流與狀態規則 |
| `explorer-industry.md` | 行業/OSINT 發現 | 本地/區域媒體（Daily NK、NK News、Korea IT Times、Sand Times、The Diplomat、Dong-A Ilbo、Tongil News、NK Economy）、智庫/OSINT（38 North、CSIS、North Korea Tech、38 North Digital Atlas）、州級 IT 實體（KCC、KPTC/Koryolink、Sunnet、Kang Song/Byol、Naenara、PIC、省級電子事務研究所、Hamhung 計算機技術大學）、互聯與負面證據、英/韓查詢模板 |

## 核心結構事實（框定每次搜索）

1. **行政區模型**：manifest 為 **capital city/province/special city/metropolitan city**，恰好 **13 個 division = 1 首都（Pyongyang）+ 9 省（South/North Pyongan、Chagang、South/North Hwanghae、Kangwon、South/North Hamgyong、Ryanggang）+ 1 metropolitan city（Nampo）+ 2 special cities（Rason、Kaesong）**。manifest 為權威列舉模型；不要在北韓首都下再加第二個 Pyongyang 類別。韓文/中文名用於召回：평양、평안남도、평안북도、자강도、황해남도、황해북도、강원도、함경남도、함경북도、량강도/양강도、라선、남포、개성。行政驗證無法對照 DPRK 政府來源，以 ROK 統一部入口為規範行政參考。
2. **註冊庫現狀**：無公開國家資料中心註冊庫；無建照/EIA 檢索。最接近普查的組合：**(1) UN Panel of Experts 對朝報告；(2) MSMT 2nd report（2025-10-22 發布）；(3) US OFAC 對國家 IT 實體的指定；(4) ROK 統一部北韓資訊入口 ICT 行業概覽（2023-07 更新）；(5) NIA K2Base 的 Kwangmyong/.kp 記錄**。雲區域官方清單對超大規模設施為負面證據。
3. **法律與監管基礎**：UNSCR 1718（2006）及後續（含 UNSCR 2270（2016），開城工業區關閉與資產凍結的法律錨點）；MSMT（UNSCR 2270 para.28 機制，Japan MOFA 官方發布）；OFAC 指定（如 KCC 2017-06-01 指定為國家 IT 研發中心，HQ 平壤）；DPRK 國內 ICT 法不對外公開；ROK 政府彙編為實體/行業事實的系統性來源。
4. **制裁文件分級**：OFAC 指定（A）證明實體存在與指定時所述功能，**非**當前物理運營；UNSCR 文本（A）證明決議義務，**非**開城地區設施當前狀態；MSMT/UN/OFAC 文件記錄國家 IT 部門的存在與規模，**不單獨證明任何物理資料中心**。
5. **無商業市場**：Pyongyang 是唯一可信的 IT 聚落（KCC、Naenara/Kwangmyong 內網、電信核心）；全省級實體（省電子事務研究所）僅存在於官方媒體轉述（C）；Chagang 為真負面（no_projects）。
6. **連通性**：內陸國；網路出口經中國（近期報導亦有俄羅斯）；無公共 IXP、無海纜登陸、無任何 hyperscaler 區域；Kwangmyong 是封閉國家內網，**非**公共網際網路。
7. **低暴露邊界（每次列舉必須遵守）**：制裁、ROK 政府彙編與官方媒體轉述僅用於實體/功能/背景發現；**不發布或推斷精確坐標、安全敏感佈局、訪問控制、人員身份或運營漏洞**；具名城市/道為最大地點粒度，除非公開來源明確提供非敏感設施背景；物理設施狀態與實體級制裁證據分開記錄。

## 查詢模板（複製貼上，完整清單見 explorer-official.md §5 與 explorer-industry.md §5）

```text
site:un.org 1718 panel experts Korea IT OR cyber OR "data center"
site:home.treasury.gov DPRK OR "Korea Computer Center" OR IT designation
site:mofa.go.jp MSMT OR DPRK OR North Korea
site:nkinfo.unikorea.go.kr 정보통신 OR 반도체 OR 컴퓨터
site:k2base.re.kr 광명 OR 정보통신 OR 컴퓨터 OR 도메인
"North Korea" OR "DPRK" ("data center" OR datacenter OR "server room" OR hosting OR colocation)
"North Korea" (Kwangmyong OR Naenara OR KCC OR "Korea Computer Center") (intranet OR server OR hosting OR IT)
"Korea Computer Center" designation OR OFAC OR sanctions
"Pyongyang" OR "Hamhung" OR "Chongjin" OR "Haeju" ("data center" OR datacenter OR "server room" OR IT facility)
"Koryolink" OR "Kang Song" OR "Byol" North Korea subscribers OR launch OR network
"electronic affairs research institute" OR 전자업무연구소 North Korea
site:38north.org North Korea (telecom OR Kwangmyong OR Koryolink OR "base station" OR KIC)
site:csis.org DPRK OR "North Korea" IT workers OR cyber operations
site:northkoreatech.org Kwangmyong OR telecom OR internet
북한 데이터센터 OR 서버실 OR 정보통신 OR 전자업무연구소
평양 정보센터 OR 한국컴퓨터센터 OR 국가자료통신망
해주반도체공장 OR 함흥컴퓨터기술대학 OR 청진 전자업무연구소
"North Korea" internet exchange OR IXP OR egress China OR Russia（負面確認）
"DPRK" "data center" sanctions OR OFAC OR UNSCR OR MSMT
```

## 官方/監管管線要點（詳見 explorer-official.md）

- **UN 制裁體制**：UNSCR 2270 官方文本（A）；Panel of Experts 報告（A 級普查源，逐期檢查具名 IT 實體與地點）。
- **US Treasury OFAC**：KCC 指定（2017-06-01，A，實體/功能級）；指定命名實體與聲稱功能，很少給街道級設施數據——不得把指定轉換為物理設施狀態；監控 recent-actions 與 sanctionssearch.ofac.treas.gov。
- **MSMT / Japan MOFA**：MSMT 2nd report 官方發布（2025-10-22，A）量化國家 IT 機器（每工人 $3,500-$10,000/月；CSIS 估計年化 $350-800M）；38 North 解讀（B）。
- **ROK 政府彙編**：統一部北韓資訊入口（ICT 概覽 2023-07，驗證記錄：Haeju 半導體廠（C）、Hamhung 計算機技術大學（B））；NIA K2Base（Kwangmyong 光纖 2004 平壤全境、2005 咸興/清津；內網屬信息工業省，C 級線索）。
- **明確排除**：DPRK 官方媒體（KCNA、Rodong Sinmun、Chosun Today、Arirang Meare）為宣傳級；其 ICT 宣稱經 NK Economy/Tongil News 轉述至多記 C，直到衛星分析、脫北者報導或制裁文件佐證。
- **來源優先檢查表**：UNSCR/Panel of Experts → MSMT（Japan MOFA/UN 渠道）→ OFAC 指定 → ROK 統一部入口 → NIA K2Base → 38 North/CSIS（B 級佐證）→ 引官方文件的貿易媒體（B）→ DPRK 官方媒體轉述（僅 C）。
- **更新節奏**：每季——Panel of Experts 報告、MSMT 發布、OFAC 對朝行動；每半年——ROK 統一部 ICT 概覽；每年——K2Base 記錄與全部 U/C 設施宣稱複核；事件驅動——新 UNSCR/OFAC 指定/MSMT 點名物理設施為最大變數，記錄前必須對照制裁文件驗證。

## 行業/OSINT 發現要點（詳見 explorer-industry.md）

- **本地/區域媒體**：Daily NK（B，脫北者運營，最強境內來源：Mirae Wi-Fi、Wonsan smishing、Chongjin IT 培訓）、NK News（B，引官方文件可 A）、Korea IT Times（C，KCC 檔案）、Sand Times（C，Kang Song 300 萬 vs Koryolink 170 萬用戶）、The Diplomat（U，新義州 5G 監控單一來源）、Dong-A Ilbo（B，KT 開城通訊中心 2006 建設）、Tongil News/NK Economy（C，官方媒體轉述）。
- **智庫/OSINT**：38 North/Stimson（B，衛星分析：KIC 2021-2023 活動、MSMT 報告評估、1000+ 基地台）、38 North DPRK Digital Atlas（B，全國電信基礎設施衛星枚舉）、CSIS（B，KCC 位置/IT 工人經濟學）、North Korea Tech（B，Kwangmyong 長期追蹤）。
- **州級 IT 實體種子**：KCC（OFAC A 指定；設施細節 C；容量 U）、KPTC/Koryolink（B，JV 事實）、Sunnet（B，2002 Rason+平壤 2G、2004 停用）、Kang Song/Byol（C/U）、Naenara Information Center（C）、Pyongyang Informatics Center（B，CSIS 具名）、省級電子事務研究所（C，官方媒體轉述，如清津）、Hamhung 計算機技術大學（B/C，成立年 1985 vs 2001 來源分歧須標註）、Bureau 95（C，境內宣稱）、KT KIC 通訊中心（B 歷史/U 現狀）。
- **互聯與負面證據**：Kwangmyong 內網（C/B，政府託管背景非商業 DC）、Mirae Wi-Fi（B，平壤/平城/南浦）、移動網絡核心（B，網絡上下文非 DC）、.kp（U）、IXP（無，負面）、海纜（內陸，地理負面）、hyperscaler 區域（官方清單負面，A）。
- **分級**：A 營運設施對 KP 實質上不可達（本輪無任何來源命名具位置的在運資料中心，不得記錄）；B 強 OSINT 具名基礎設施＋地點（現有 B 級皆為網絡/機構/歷史設施，非在運商業 DC）；C 官方媒體轉述/ROK 媒體/Naver blog/Wikipedia，保持 C 直到佐證；U NamuWiki/YouTube/單一來源（Samtaesong 手機、新義州 5G 宣稱）。
- **no_projects 記錄**：Chagang（2026-08-12 已搜）與 DC 負面道（South/North Hwanghae、Kangwon、Ryanggang）以 U 級＋搜索日期如實記錄——負面是真正的發現，不是缺口。
- **計數/去重/容量**：KCC 是單一實體（Mangyongdae District / Sunlae-Dong Mangyong District = 同一區不同羅馬化，不倍增）；Mirae Wi-Fi 兩來源佐證同一網絡；Koryolink 用戶數不出現在多來源重複計數；容量字段全境保持 null（唯一樓板面積 KT KIC ~9,900 m² 為 2006 歷史報導 B）；負面搜索：大學電腦室、礦山自動化、森林防火監控、半導體製造 ≠ 資料中心，除非來源描述具名營運商與地點的託管/colo/計算基礎設施。

## 來源分類（制裁文件 / ROK 政府彙編 / 行業媒體）與 A/B/C/U 分級

- **A（官方/一手）**：UN 安理會決議與 Panel of Experts 報告、MSMT（UNSCR-2270 基礎）官方發布、US Treasury OFAC 新聞稿/指定、ROK 統一部北韓資訊入口記錄、NIA K2Base 政府研究入口記錄。
- **B（強二級，引官方材料）**：38 North（Stimson）對 MSMT/UN 報告的分析、NK News / North Korea Tech 引官方文件、具名官方來源的 ROK 主要日報。
- **C（僅線索）**：無原始連結的 ROK 政府彙編、官方媒體轉述摘要、聚合器/二級頁面（Korea IT Times、Sand Times、NK Economy、Tongil News、Naver blog、Wikipedia）。
- **U（未驗證）**：單一弱來源、wiki 宣稱、視頻證據、境內單一來源宣稱；升級前複核（NamuWiki、YouTube、The Diplomat 5G 宣稱、Samtaesong 手機）。
- **制裁交叉檢查**：任何新的朝鮮「資料中心」宣稱必須先對照 OFAC 指定、UN Panel/MSMT 報告與 38 North 衛星分析，才可記 C 以上。

## 使用流程（探索/複核批次）

1. 讀取批次 JSONL（country_code=KP，divisions=capital city/province/special city/metropolitan city，13 目標）。
2. 低暴露預檢：本輪輸出僅允許城市/道上下文；禁止精確坐標、安全佈局、人員身份與針對性推斷。
3. 官方查詢：UN/OFAC/MSMT（制裁文件）→ ROK 統一部入口/K2Base（政府彙編）→ 38 North/CSIS（B 級佐證）。
4. 行業查詢：Daily NK/NK News/North Korea Tech → 州級 IT 實體種子 → 韓文模板（ROK 入口召回）。
5. 雲/互聯負面確認：AWS/Azure/GCP/OCI 官方區域清單（負）；IXP/海纜/Starlink 無證據。
6. 去重與分級：同一實體多來源（KCC/Mirae）不倍增；實體級記錄與設施級記錄分開；容量保持 null；無活動 division 寫 `no_projects: true`（附搜索日期）。
7. 遵行 NO-DELETION；只創建自己的結果文件。

## 待辦（2026-08-12）

- 兩份 explorer 已審定（explorer-official.md / explorer-industry.md，Review record 已追加）。
- 下一步：探索/複核批次（13 division）以本 skill 作為每個 agent 的國家層參考注入。
- 待核實：MSMT/UN Panel 後續報告是否有具名物理設施；OFAC 後續對朝 IT 指定；KCC 設施細節（需衛星/脫北者/制裁佐證方可升 C 以上）；Kwangmyong 託管具體化；清津電子事務研究所（2022 官方媒體宣稱）外部佐證；Chagang 與負面道維持 no_projects。
