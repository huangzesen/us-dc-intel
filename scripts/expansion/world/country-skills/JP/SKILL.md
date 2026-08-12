---
name: jp-datacenter-methodology
location: scripts/expansion/world/country-skills/JP/SKILL.md
description: |
  Japan (JP) datacenter discovery & audit methodology — how to enumerate, verify, and update Japan datacenter projects across 47 prefectures + municipalities / wards / cities. Japan has no datacenter operating license and no national planning-permit portal: enumeration is municipality-first inside prefectures, joining Building Standards Act building confirmation (建築確認) and development permission records, city-planning / landscape / resident-explanation / assembly-minutes trails, Tokyo & Osaka building-environmental-plan systems, METI subsidy and GX / Watt-Bit (ワット・ビット) policy lists, MIC telecom registration and JDCC member lists, TEPCO PG / Kansai TD and regional utility power evidence, official cloud-region pages (AWS Tokyo/Osaka, Azure Japan East/West, GCP Tokyo/Osaka, OCI Tokyo/Osaka), and operator pages (Equinix, NTT GDC, KDDI/Telehouse, IDC Frontier, SoftBank, Sakura Internet, AT TOKYO, MC Digital Realty, AirTrunk, Colt, STACK, Digital Edge, IIJ). Read this before running JP exploration/audit batches. Routes to explorer-official.md (permits/power/subsidy/cloud) and explorer-industry.md (trade press/vendors/prefecture query patterns).
---

# JP · 日本数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：日本**没有**统一的数据中心运营执照，也**没有**国家级可检索的规划许可门户；数据中心常以办公楼/电信设施/仓库/厂房等混合用途获批。枚举需**在市町村层面先行**、再归并到都道府县，组合 **建築確認/開発許可**、**都市計画審議会/景観審議会/住民説明会/議事録**、**東京都・大阪市の建築物環境計画制度**、**METI 補助金と GX/ワット・ビット政策**、**MIC 電気通信事業登録と JDCC 会員名簿**、**電力会社（TEPCO PG/関西送配電等）**、**官方云区域页**与**运营商官方页**。
> 核心地理由电力网络驱动：首都圈（尤其 **Chiba Inzai/Shiroi** 超大规模园区）、关西（Osaka/Sakai/Keihanna）、以及地方分散集群（Hokkaido Ishikari/Tomakomai、Kyushu Fukuoka/Kitakyushu、Fukushima Shirakawa 等）。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供日本探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：建築基準法建築確認（MLIT/指定確認検査機関）、東京都データセンターガイドラインと環境計画制度、Inzai/Shiroi・Osaka/Keihanna 自治体记录、METI/ANRE 节能与补助金、GX戦略地域/ワット・ビット、TEPCO PG 与各地域送配電、MIC 電気通信事業、JDCC、官方云区域页、47 都道府県工作流 |
| `explorer-industry.md` | 行业/厂商发现：Impress Cloud Watch/ITmedia Built/DCD/Nikkei/Bloomberg/Data Center Cafe 媒体、运营商/开发商种子表（NTT GDC、AT TOKYO、KDDI/Telehouse、Equinix、MC Digital Realty、AirTrunk、Colt、STACK、Digital Edge、IDC Frontier、SoftBank、Sakura、IIJ、NEC、Fujitsu 等）、日语关键词与状态词表、都道府県別枚举矩阵 |

## 核心结构事实（框定每次搜索）

1. **无全国设施注册库**：MIC/METI/JDCC 均非设施普查；日本枚举靠三角验证：①日语行业/建设媒体（開設/着工/用地取得/容量声明），②运营商官方位置页，③政府补助金採択・自治体誘致・建築/环境/公告记录・电网发布。
2. **规划证据在市町村**：建筑确认（建築確認）由自治体建筑主管或**指定確認検査機関**（私人机构）签发，很多不公开检索——公开痕迹常经都市計画審議会、景観審議会、地区計画、建築物環境計画制度、議会議事録、住民説明会、诉讼显现。
3. **电力是主要选址约束**：首都圈高收益线索 = **TEPCO PG / 送変電所脉络 + Inzai/Shiroi/Chiba 自治体规划记录 + 运营商公告**（NTT/TEPCO 合资直接指向 Inzai-Shiroi 区域）；关西用 Kansai TD / Osaka 记录 / Keihanna・Sakai 官方公告；Hokkaido・Fukushima・Kyushu 等需各地域电力会社与补助金 join。
4. **国家产业政策推动地方分散**：METI「データセンター地方拠点整備事業費補助金」（FY2023 公募/採択結果公开）、GX戦略地域（データセンター集積型，候选地/市町村粒度）、ワット・ビット連携——自上而下的种子列表，但非完整注册库。
5. **云区域=逻辑区域（A 级 metro 存在）**：AWS Tokyo `ap-northeast-1`（4 AZ）/ Osaka `ap-northeast-3`（3 AZ）；Azure Japan East（Tokyo/Saitama）/ Japan West（Osaka）；GCP Tokyo `asia-northeast1` / Osaka `asia-northeast2`；OCI Tokyo `ap-tokyo-1` / Osaka `ap-osaka-1`。不揭示精确园区，需 join 运营商/建筑/电力证据。
6. **容量单位混乱**：`受電容量`（受电容量）≠ `IT電力`/`IT負荷`；`MW` 常为园区总规划而非一期；`第1期`/`新棟`/`全体`/`最終`/`最大`/`将来的に` 需分别记录。
7. **别名陷阱**：英文 `Tokyo` 常指 Chiba Inzai/Shiroi 或 Saitama；`Osaka` 可能指京都/Nara 边界的 Keihanna；按 `(最终运营商, 园区名, 阶段/栋, 市町村)` 去重。

## 查询模式（复制粘贴模板见 explorer-official.md §1 与 explorer-industry.md §5）

- 日语核心词：`データセンター` `データセンタ` `DC` `IDC` `AIデータセンター` `計算基盤` `GPUクラウド` `クラウド基盤` `コロケーション` `サーバールーム` `コンテナ型データセンター` `グリーンデータセンター` `ゼロエミッション・データセンター` `地方分散` `ワット・ビット連携` `GX戦略地域`。
- 规划/建筑：`"{市区町村}" "データセンター" "建築確認"`、`"{市区町村}" "データセンター" "開発行為"`、`"{市区町村}" "データセンター" "都市計画審議会" OR "景観審議会" OR "地区計画" OR "住民説明会" OR "議事録"`、`site:{city}.lg.jp ("建築確認" OR "開発許可") データセンター`。
- 电力：`"データセンター" "特別高圧" "{市区町村}"`、`"データセンター" "変電所" "{市区町村}"`、`"データセンター" "系統接続" "{電力会社}"`、`site:tepco.co.jp/pg データセンター 印西 OR 白井`、`site:kansai-td.co.jp データセンター`、`site:kyuden.co.jp データセンター 北九州`。
- 政策/监管：`site:meti.go.jp "データセンター地方拠点整備事業費補助金"`、`site:meti.go.jp "GX戦略地域" "データセンター集積型"`、`site:enecho.meti.go.jp データセンター 省エネ`、`site:soumu.go.jp 電気通信事業者 届出 一覧 "{operator}"`、`site:jdcc.or.jp 会員一覧`。
- 媒体：`site:cloud.watch.impress.co.jp/docs データセンター "{都道府県}" (開設 OR 竣工 OR 着工 OR 増設)`、`site:built.itmedia.co.jp データセンター "{市区町村}" (MW OR メガワット OR 受電容量)`、`site:datacenterdynamics.com Japan "{operator}" "{city}"`。
- 状态词：`協定/覚書/基本合意/誘致`=意向（C）；`補助金採択/用地取得/土地取得/立地協定`=planned（B/A-）；`建築確認/開発許可/環境影響評価/公告/入札/落札`=主轨迹（A）；`地鎮祭/着工/起工式`=在建；`竣工/開設/稼働/運用開始/サービス開始`=运营（需运营商/政府确认）。
- 英文回退：`"{city}" Japan "data center" "groundbreaking" OR "opened" OR "land"`、`"Inzai" "data center" AirTrunk Colt Digital Realty STACK NTT`、`"Shiroi" "data center" NTT STACK ESR`、`"Keihanna" "data center" Colt NTT`、`"Tomakomai" "AI data center" SoftBank IDC Frontier`、`"Ishikari" "data center" Sakura KCCS renewable`。

## 官方/监管管线要点（详见 explorer-official.md）

- 建筑确认：MLIT 指定確認検査機関名单（https://www.mlit.go.jp/jutakukentiku/house/jutakukentiku_house_tk_000019.html ）与コンテナ型データセンター技术意见（https://www.mlit.go.jp/report/press/house05_hh_000234.html ）；先自治体后都道府县。
- 东京：データセンター都市づくりガイドライン（https://www.toshiseibi.metro.tokyo.lg.jp/machizukuri/smarttokyo/datacenter ）+ 建築物環境計画制度（https://green-building-pgm.metro.tokyo.lg.jp/KSA00101 ）——A 级过程源；江東/品川/港/中央/大手町/多摩/府中/临海。
- Inzai/Shiroi：市报道/地区計画资料（例 https://www.city.inzai.lg.jp/0000021271.html ）；NTT/TEPCO 联合开发指向 Inzai-Shiroi（https://www.tepco.co.jp/pg/company/press-information/press/2023/1666668_8618.html ，A）。
- 大阪/関西：大阪市建築物環境計画書公表（https://www.city.osaka.lg.jp/toshikeikaku/page/0000665562.html ）、堺/けいはんな（精華町・木津川）自治体记录。
- METI/ANRE：データセンター地方拠点整備事業費補助金 公募（k230922001）与採択結果（s231107001，A=受赏者/補助范围）；GX戦略地域（20260424007）；ワット・ビットWG 资料；省エネ法ベンチマーク（PUE）。
- MIC/JDCC：電気通信事業法 Article 9 注册/Article 16 届出（运营商法律状态 A，非设施注册库）；JDCC 会員名簿（B+ 运营商种子）。
- 云区域（A=metro 存在）：AWS `ap-northeast-1`/`ap-northeast-3`；Azure Japan East/West；GCP `asia-northeast1`/`asia-northeast2`；OCI `ap-tokyo-1`/`ap-osaka-1`。
- 运营商官方页（存在性 A，容量 B）：Equinix Tokyo 14 个 DC（TY1/TY2/TY3/TY11/TY12x/TY13x/TY15）+ Osaka OS；NTT GDC Tokyo/Osaka/Shiroi/Keihanna（OSK12 首栋 18 MW IT load / 36 MW 园区）；KDDI/Telehouse 9 处战略地点（大阪堺 2026-01-22 运营）；IDC Frontier（府中/北九州/白河）；SoftBank 苫小牧 AI DC（FY2026 首期 50 MW、后续 300 MW+）；Sakura Internet 石狩コンテナ型 DC（2025-05 完工，约 3.5MVA/40 机架）；AT TOKYO（13 个 DC）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 媒体：Impress Cloud Watch（B+，最佳日语公开源）、ITmedia BUILT（B+，建设/地产）、DCD（B+，AirTrunk/Colt/Digital Realty/NTT/STACK/GAW/ESR/GLP）、Nikkei/xTECH/Bloomberg Japan（B，大额投资/地产/能源）、Data Center Cafe/DC ASIA（B-/C+，需回溯原始源）、ASCII/INTERNET Watch/EnterpriseZine（B-/C+）。
- 运营商/开发商种子（官方页 A-，容量 B）：NTT DATA/GDC（Shiroi SHR1、Keihanna OSK11/OSK12）、AT TOKYO（中央/豊洲、大阪、北海道、広島、福岡、沖縄；DCD 报 CC3 40 MW）、KDDI/Telehouse（大手町/多摩/名古屋/福岡）、Equinix Japan（TY/OS IBX）、MC Digital Realty/Digital Realty（Chiba Inzai NRT 园区、Osaka KIX 园区）、AirTrunk（TOK1 Inzai 40 MW 新栋/300 MW+ 园区）、Colt DCS（Inzai 4=20 MW IT power、Osaka Keihanna 45 MW-class）、STACK（Inzai 两栋 36 MW）、Digital Edge（Tokyo/Osaka，2021 收购 CTC 站点）、IDC Frontier/SoftBank（府中/有明/横浜/吹田/北九州+苫小牧 AI）、Sakura Internet（石狩）、IIJ（松江 DC Park、白井 DC 园区）、NEC（神戸/川崎/Inzai/名古屋）、Fujitsu（館林/横浜/明石）、NRI/野村総研、地域运营商（STNet、QTnet、K-Opticom/OPTAGE、HTNet、HBA、AGS、青い森クラウドベース、KCCS）。
- 地产/基建开发商：ESR、GLP、Gaw Capital、Goodman、三井/Fidelity JV、大和ハウス、ヒューリック、三菱地所、Keppel、STT GDC、EdgeConneX、Vantage、CyrusOne/KEPCO——多为计划/土地阶段，状态必须验证。
- 目录源（C）：DataCenterMap、Baxtel、Cloudscene、Datacenters.com、OCOLO——仅别名/邻近设施线索，不作容量终源。

## 来源分级

- **A** = 官方/一手：METI/MIC/デジタル庁補助金与政策页、自治体许可/公告/環境計画、运营商官方设施页/新闻稿（存在/状态）、上市公司有価証券報告書（TDnet/EDINET）、电力公司/电网发布、官方云区域页、政府采购/落札公告。
- **B** = 强二级：Impress Cloud Watch、ITmedia Built、DCD、Nikkei/Bloomberg（具名业主/场地/MW 时）、JDCC 会員名簿（运营商种子）、CBRE/JLL/Cushman/IDC/Arizton 等经纪人报告（市场脉络）、承包商项目页。
- **C** = 弱线索：DataCenterMap/Baxtel/Cloudscene/Datacenters.com/OCOLO、地方誘致宣传稿、社媒、无出处 AI 园区声明。
- 状态语义：`運用開始/稼働/開設/竣工`=运营（需运营商/政府或多次贸易媒体确认）；`着工/地鎮祭/起工式`=在建；`誘致/覚書/協定/構想/予定/最大/将来的に`=计划；`補助金採択/用地取得/土地取得/立地協定`=较强 planned。电力预留（系統接続関心）无具名项目仅为线索。
- 去重：同一园区可有运营商/JV/地主/承包商/云客户多重身份；按 `(最终运营商, 园区名, 阶段/栋, 市町村)` 记录；`受電容量` 与 `IT電力` 并存时按原文标签分别记录；大规模项目需查 `住民説明会/反対/騒音/排熱/景観/中止/撤回/延期/白紙`。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=JP，divisions=47 都道府県 → 市町村/区）。
2. **种子运营商**：JDCC 会員名簿 + 头部厂商页 + 聚合器地图，建运营商字典（日文名/英文名/母公司/官方域名）。
3. **贸易媒体扫描**：Impress Cloud Watch、ITmedia Built、DCD、Nikkei/Bloomberg、Data Center Cafe 近 5 年状态词扫描。
4. **都道府県矩阵**：优先 Chiba（Inzai/Shiroi）、Tokyo、Osaka、Kyoto（けいはんな）、Kanagawa、Saitama、Hokkaido（石狩/苫小牧）、Fukuoka（北九州）、Aomori、Miyagi、Shimane（松江）、Kagawa、Okinawa、Aichi、Hyogo、Gunma（館林）。
5. **官方轨迹**：METI 補助金採択、デジタル庁/MIC 政策页、自治体公告、建築物環境計画、電力会社发布、建設入札；东京/大阪环境计划系统查运营商名与 `データセンター`。
6. **容量/状态验证**：运营商发布或官方/地方记录；区分运营/在建/计划园区；`IT電力` vs `受電容量` 分开；输出 world 同 schema，无项目 division 写 `no_projects: true`。
7. 遵守 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12 02:15Z）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：50× codex terra agent（max thinking）每 agent 分批复核日本数据中心（47 都道府県）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：AirTrunk TOK1 300 MW+ 园区分阶段、SoftBank 苫小牧 1 GW 可能园区（官方首期 50 MW）、NTT Shiroi SHR1 动工状态、各 hyperscaler 物理站点（AWS/Azure/GCP/OCI 日本园区）、KDDI 堺后续阶段、NEC 三个核心云 DC 出售/管线。
