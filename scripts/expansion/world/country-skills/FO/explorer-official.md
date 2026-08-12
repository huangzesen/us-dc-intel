# FO Explorer Official — 法罗群岛数据中心官方侧清点方法论 (Faroe Islands Datacenter Enumeration)

Status: Final. Last reviewed: 2026-08-12. Scope: Faroe Islands (FO). Repo division model: **country**; manifest divisions (1): `Faroe Islands`.

用途 (Purpose)：用官方/一手来源确认法罗群岛的数据中心、托管机房、政府/企业 IT hosting、海缆登陆站和电力/许可触发点。行业侧文件 `explorer-industry.md` 可用于发现候选；只有本文件定义的 A/B 证据足够时，才把候选计入设施表。Manifest 只有一个 division，因此所有设施最终都归入 `Faroe Islands`；下文的 6 个区域仅是覆盖检查网格。

## 0. 结构性事实 (Country Structure Facts)

### 0.1 行政与覆盖模型 (Administrative and Coverage Model)

- 法罗群岛（Føroyar / Færøerne）是丹麦王国下的自治地区。法罗政府官网说明其 1948 年自治安排；丹麦首相府说明法罗可承接除宪法、国籍、最高法院、外交/防务/安全、汇率和货币等之外的事务。官方入口：https://www.government.fo/ 与 https://english.stm.dk/the-prime-ministers-office/the-unity-of-the-realm/faroe-islands/ 。
- 法罗群岛不属于欧盟；丹麦加入欧盟不覆盖法罗。对采购、数据保护、电信、能源等问题，不要直接套用丹麦/EU 规则，必须查法罗本地法律和主管机关。
- Repo manifest 已核对：`{"country_code":"FO","country_name":"Faroe Islands","subnational_type":"country","divisions":["Faroe Islands"]}`。因此 repo 层面没有省/州级分区。
- 实施扫描时使用 6 个传统区域/岛区作为 coverage checklist：Streymoy、Eysturoy、Norðoyar、Vágar、Sandoy、Suðuroy。Hagstova Føroya 说明全国有 29 个市镇；市镇是地方规划/建筑许可检索的关键层级。统计入口：https://hagstova.fo/en/economy/economy/municipalities 。

| 覆盖区域 Coverage area | 重点市镇/地点 Key municipalities and localities |
|---|---|
| Streymoy | Tórshavn/Hoyvík/Argir、Kollafjørður、Vestmanna、Kvívík、Sunda 的 Streymoy 侧 |
| Eysturoy | Runavík、Fuglafjørður、Eysturkommuna、Eiði、Sjóvar kommuna、Sunda 的 Eysturoy 侧 |
| Norðoyar | Klaksvík、Viðareiði、Kunoy、Fugloy、Kalsoy/Svínoy 相关地点 |
| Vágar | Vága kommuna、Sørvágur、机场周边工业用地 |
| Sandoy | Sandur、Skálavík、Skopun、Húsavík、Skúvoy |
| Suðuroy | Tvøroyri、Vágur、Hvalba、Porkeri、Hov、Fámjin、Sumba |

覆盖完成标准：每次年度复核需在 `Faroe Islands` division 下记录这 6 个覆盖区域各自的确认设施，或带日期的负向/watch 记录。不要把 6 个区域写成 manifest divisions。

### 0.2 官方登记处与无专门 DC 登记处 (Official Registers; No DC Register)

- **公司登记 / Business register**：Skráseting Føroya（Faroese Business Authority / Company Registration Authority），https://www.skraseting.fo/en/about-us 。公司注册号、法人名称和注册地址可作 A 级公司事实，但不单独证明某个数据中心设施。
- **法律库 / Legal repository**：Lógasavn，https://www.logir.fo/ 。法律文本以该站为权威，含 Home Rule Act、Telecommunications Act 等。
- **电信监管 / Telecom regulator**：Fjarskiftiseftirlitið（Telecommunication Authority of the Faroe Islands），https://www.fjarskiftiseftirlitid.fo/fo/english/about-us 。该机构监管无线电和电信，并维护/处理运营商许可；它不是数据中心登记处。
- **电力 / Electricity**：SEV，https://www.sev.fo/ 。Hagstova 将 SEV 描述为 intermunicipal co-operative body 和主要电力供应商；SEV 新闻和年报是大负荷/电网事实的一手来源。
- **环境与地图 / Environment and maps**：Umhvørvisstovan，https://www.us.fo/ 。用于 EIA、环境许可、地理/地图和相关公示检索。
- **数据保护 / Data protection**：Dátueftirlitið，https://www.dat.fo/english 。用于个人数据处理和合规事实，不证明设施存在。
- **公共采购 / Procurement**：Keypsportalurin，https://keypsportal.fo/ 。该站披露采购、豁免和公共 IT 采购线索；例如其豁免页出现过 `Keyp av UPS til datacenter B í bygninginum B22, hædd 0` 这类政府数据中心/机房线索，应回查采购主体和地点。

未发现法罗有类似挪威 Nkom 数据中心登记的国家数据中心登记处。清点必须组合：公司登记、运营商自述、采购、规划/建筑许可、SEV 电力资料、电信许可、海缆/IXP 资料。

### 0.3 法律/监管基础 (Legal and Regulatory Basis)

- **电信法**：Lógasavn 的 `Løgtingslóg nr. 72 frá 22.05.2015 um fjarskifti`，现行页面显示截至 2024-05-16 的修订： https://www.logir.fo/Logtingslog/72-fra-22-05-2015-um-fjarskifti 。DC 运营者不因运营机房自动成为电信服务商；若提供公共通信服务、频谱或编号相关服务，再进入 Fjarskiftiseftirlitið 范围。
- **规划/建筑许可**：市镇网站和会议纪要是首要来源；Tórshavn、Klaksvík、Runavík、Vágar 等重点检索 `byggiloyvi`、`byggisamtykt`、`útstykking`、`vinnuøki`、`datacenter`。
- **EIA/环境**：Umhvørvisstovan 与 Lógasavn 检索 `umhvørvisárin`、`umhvørvismat`、`VVM`、`datacenter`、`data miðstøð`。EIA screening/decision 可以作为 A 级项目证据。
- **采购**：Keypsportalurin 的公告与 `undantøk` 页面为官方采购线索；TED/udbud.dk 仅作补充，因为法罗不属于 EU procurement regime 的常规覆盖。

## 1. 搜索词表 (Search Vocabulary)

法罗语优先，丹麦语和英语补充。自动检索时不要把 `OR` 混入 `site:` 查询的一行里；应拆成多条或使用引号。

```text
# Faroese
"data miðstøð" / "datamiðstøð" / datacenter
hýsing / "hýsingartænastur" / samhýsing
server / servari / "servarar" / "serverrúm"
"KT-rakstur" / "skipanarrakstur" / "KT-trygd"
ravmagn / elorka / elnet / netloysnir
byggiloyvi / byggisamtykt / vinnuøki
útboð / innkeyp / keyp / undantak
sjókaðal / kaðal / landingarstøð
Føroya Tele / FT / NET / Nema / Elektron / SEV
```

```text
# Danish / English
datacenter / data center / data centre / colocation / colo
hosting / managed hosting / IT drift / server room
submarine cable / cable landing station / landing point / IXP / peering
electricity / grid connection / large load / PPA / renewable power
building permit / planning permission / EIA / environmental assessment
public procurement / tender / exemption
```

## 2. 官方/一手管线 (Official and Primary-Source Pipeline)

### 2.1 规划、EIA、市政许可 (Planning, EIA, Municipal Permits)

优先级：

1. Tórshavn Kommuna：https://www.torshavn.fo/ 。重点查 Hoyvík/Klingran、政府办公楼、FT/NET/Elektron/Nema 相关地址、`byggiloyvi`、`vinnuøki`。
2. Klaksvík、Runavík、Vágar、Tvøroyri/Vágur 等市镇站。先查市政搜索，再查会议 PDF。
3. Umhvørvisstovan：https://www.us.fo/ 。查 EIA、地图和环境许可。

A 级证据：市政许可、会议纪要、EIA decision/screening、官方采购文件中指明设施、地点、建设/改造范围。

### 2.2 电力与电网 (Power and Grid)

- SEV：https://www.sev.fo/english/ 。SEV 年报、新闻与技术资料用于确认电网、发电结构、大用户和电源改造。
- Hagstova 电力统计：https://hagstova.fo/en/environment/energy/electricity-production-sev 。该页确认 SEV 是主要电力提供者，并列出风、水、热电三类来源。
- SEV 2024 年报/新闻显示 2024 年可持续电力生产达到 271 GWh、占总生产 56.6%（新闻：https://www.sev.fo/english/news/annual-accounts-2024 ）。2030 年 100% 可再生目标可作为市场背景，但不能当作某个 DC 项目证据。

A 级证据：SEV 文件直接提到某个数据中心、机房、UPS/发电机、电网接入、大用户合同或地点。一般能源转型材料只作背景。

### 2.3 电信、海缆、IXP (Telecom, Cables, IXP)

- **Føroya Tele / FT**：https://www.ft.fo/ 。当前 FT 主页确认总部地址 Klingran 3, FO-188 Hoyvík；未在当前公开页面确认独立商业 colocation/data center 产品。FT/NET 可作为电信机房、海缆、网络基础设施线索。
- **NET**：https://www.net.fo/ 。Føroya Tele 集团网络公司；页面确认 P/F Net 地址 Klingran 3, FO-188 Hoyvík，负责光纤网络。
- **Fjarskiftiseftirlitið**：https://www.fjarskiftiseftirlitid.fo/fo/fjarskifti/fjarskiftisveitarar 。许可/运营商信息是电信普查，不是设施清单。
- **Farice**：https://farice.is/network/ 与 https://farice.is/company-history/ 。Farice 自述 FARICE-1 从 Seyðisfjörður 到 Dunnet Bay，并通过 branch unit 接入 Funningsfjørður；点到点服务延伸到 Reykjavík、Torshavn、Edinburgh/London。
- **SHEFA-2**：https://www.shefa.fo/elbowroom/ 和 https://www.shefa.fo/connecting-islands/ 。TeleGeography Submarine Cable Map 的 SHEFA-2 页列出 Torshavn、Ayre of Cara、Banff 等登陆点：https://www.submarinecablemap.com/submarine-cable/shefa-2 。
- **PeeringDB / Internet Society Pulse**：https://www.peeringdb.com/advanced_search?country=FO 与 https://pulse.internetsociety.org/en/ixp-tracker/country/FO/ 。自报/聚合，C 级；只用于发现名称。

海缆登陆站、PoP 和网络节点不是 DC。只有在同一设施有 hosting/colocation/IT operations 证据时，才可作为数据中心/机房条目的一部分。

### 2.4 政府 IT 和采购 (Government IT and Procurement)

- **Talgildu Føroyar / Digital Faroe Islands**：https://www.talgildu.fo/english/english/ 。说明国家数字化计划由财政部牵头，可发现政府平台、身份认证、云/hosting 采购线索。
- **Keypsportalurin**：https://keypsportal.fo/undantok/ 。用 `datacenter`、`UPS`、`Oracle`、`hýsing`、`Talgildu Føroyar`、`KT Landsins` 检索豁免/采购记录。
- 政府采购中的 `datacenter B`、UPS、服务器、Oracle support 等说明政府机房/平台存在或维护需求，但必须记录采购主体、建筑/地址、用途，避免扩大解释为商业 DC。

### 2.5 超大规模云区域检查 (Hyperscaler Official-Region Check)

截至 2026-08-12，AWS/Azure/GCP/Oracle 官方区域页未列出 FO/Faroe Islands 公共云区域。每半年复核：

```text
https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/
https://cloud.google.com/about/locations
https://www.oracle.com/cloud/public-cloud-regions/
```

## 3. 可用查询模板 (Usable Query Templates)

每条查询保持简单，避免一行内混用多个未加括号的 `OR`。

```text
# 法律、监管、EIA
site:logir.fo "datacenter"
site:logir.fo "hýsing"
site:logir.fo "fjarskifti"
site:us.fo "data miðstøð"
site:us.fo "datacenter"
site:us.fo "umhvørvismat"
site:fjarskiftiseftirlitid.fo "fjarskiftisveitarar"

# 采购/政府 IT
site:keypsportal.fo "datacenter"
site:keypsportal.fo "UPS" "datacenter"
site:keypsportal.fo "hýsing"
site:keypsportal.fo "Talgildu Føroyar" "Oracle"
site:talgildu.fo "hýsing"
site:talgildu.fo "datacenter"

# 公司/运营商
site:skraseting.fo "Elektron"
site:skraseting.fo "Nema"
site:elektron.fo "hýsing"
site:elektron.fo "servarar"
site:nema.fo "hýsing"
site:ft.fo "server"
site:ft.fo "SHEFA"
site:net.fo "Klingran 3"

# 市政规划/建筑许可
site:torshavn.fo "datacenter"
site:torshavn.fo "byggiloyvi" "Klingran"
site:torshavn.fo "byggiloyvi" "Staravegur"
site:klaksvik.fo "datacenter"
site:runavik.fo "datacenter"
site:vagar.fo "datacenter"
site:tvoroyri.fo "datacenter"

# 电力/电网
site:sev.fo "datacenter"
site:sev.fo "data miðstøð"
site:sev.fo "stórnýtsla"
site:sev.fo "hýsing"
"Elektron" "SEV" "hýsing"
"Nema" "SEV" "hýsing"

# 海缆/连接性
site:farice.is "FARICE-1" "Torshavn"
site:shefa.fo "SHEFA-2"
site:submarinecablemap.com "Faroe Islands" "Torshavn"
"Faroe Islands" "IXP" "PeeringDB"
```

## 4. Division 清点方法 (Division Enumeration Approach)

Repo division 只有 `Faroe Islands`。内部按 6 个覆盖区域做负向/观察记录。

| 覆盖区域 | 当前判断 | 官方清点方法 |
|---|---|---|
| Streymoy | Light | Tórshavn/Hoyvík 是核心。查 Elektron、Nema、FT/NET、Talgildu Føroyar、Keypsportal、Tórshavn 许可、SEV。海缆/PoP 只作连接性，不单独计 DC。 |
| Eysturoy | None/watch | 查 Runavík、Fuglafjørður、Eysturkommuna、Sunda；重点是工业用地、电网项目、政府/银行/渔业 IT 机房线索。 |
| Norðoyar | None/watch | 查 Klaksvík 市政、Nema/电信网络、Norðlýsið；无官方 hosting/permit/electricity 证据则保持 watch。 |
| Vágar | None/watch | 查机场和工业用地、Vága/Sørvágur 规划、SEV；机场通信机房不自动计 DC。 |
| Sandoy | None/watch | Sandoyartunnilin 后做年度负向扫描；无 confirmed facility。 |
| Suðuroy | None/watch | 查 Tvøroyri/Vágur、SEV 孤岛电力/储能项目；电力项目不等于 DC。 |

## 5. 可靠性分级 (Reliability Grades)

- **A** — 一手/官方证据直接证明该事实：市政许可/会议纪要、Umhvørvisstovan EIA、SEV 文件、Skráseting 记录、Lógasavn 法律文本、运营商自有 hosting/facility 页面、Keypsportal 采购记录、Farice/SHEFA 自有电缆页面。
- **B** — 可信二手或厂商案例，具名公司/地点/日期/状态：HPE customer story、DCD、Capacity、KVF、Portal、Dimmalætting、Sosialurin、Norðlýsið、Computerworld DK、Version2、Energiwatch、供应商新闻稿。B 可证明“该来源如此报道”，但设施事实仍需尽量回查 A。
- **C** — 聚合/自报/弱证据：PeeringDB、Pulse、Submarine Cable Map、BGP/IP 数据库、DataCenterMap、Baxtel、Scamalytics/IP2Location、LinkedIn、市场报告摘要、Wikipedia。
- **U** — 未验证或不可用，不进入最终设施表。

分级只针对具体事实。例如 Elektron 自家页面能 A 级证明其提供 hýsing；HPE 案例能 B 级证明 Elektron 有 managed/in-house environments 和 HPE infrastructure upgrade；BGP 中的 `Elektron DataCenter` 仍只是 C 级网络标签。

## 6. 已确认设施/平台与官方证据 (Confirmed Facilities, Platforms and Evidence)

截至 2026-08-12，未确认法罗有公开规格的超大规模或独立第三方 colocation campus。已确认的是本地 managed hosting / IT operations providers、政府机房采购线索和海缆连接性。

| 设施/平台/项目 | Repo division | 覆盖区域 | 状态 | 证据 / 分级 |
|---|---|---|---|---|
| P/F Elektron hosting / managed IT platform | Faroe Islands | Streymoy/Tórshavn | Confirmed hosting provider; facility specs/address not public enough for DC campus classification | A：Elektron 自家页面列 `Hýsing`，说明为客户安全存储/处理数据；2022 年报说明服务与 hýsing 部门 24/7 提供 hosting、管理约 1,500 servers。B：HPE 2025 case 描述 Elektron 在 Faroe Islands 提供 IT services、managed environments、mission-critical services。URLs: https://elektron.fo/kt-trygd/ , https://elektron.fo/wp-content/uploads/2025/06/Arsroknskapur-fyri-2022.pdf , https://community.hpe.com/t5/alliances/elektron-migrates-from-vmware-to-hyper-v-on-hpe-hybrid-cloud/ba-p/7242211 |
| Nema Hýsing | Faroe Islands | Streymoy / possibly Klaksvík | Confirmed hosting service; physical facility details not public | A：Nema data-processing agreement for `Nema Hýsing` states physical data storage in Føroyar; Nema pages/news mention hýsing and admin security. URL: https://www.nema.fo/wp-content/uploads/2023/06/Databehandleraftale_NEMA_Hysing.pdf |
| Government `datacenter B` UPS procurement line | Faroe Islands | Streymoy likely, exact building B22 to confirm | Government IT room/data-center lead; not commercial DC | A：Keypsportal `undantøk` page includes `Keyp av UPS til datacenter B í bygninginum B22, hædd 0`。URL: https://keypsportal.fo/undantok/ |
| Føroya Tele / NET network facilities, Klingran 3, Hoyvík | Faroe Islands | Streymoy/Hoyvík | Telecom/network facility lead; current FT site does not prove commercial DC product | A：FT and NET pages show Klingran 3, FO-188 Hoyvík contact/address; NET describes fibre network role. URLs: https://www.ft.fo/ , https://www.net.fo/ |
| FARICE-1 cable branch / Torshavn service access | Faroe Islands | Eysturoy/Funningsfjørður and Streymoy/Tórshavn | Connectivity infrastructure; not DC | A：Farice company history/network pages. URL: https://farice.is/company-history/ |
| SHEFA-2 Torshavn landing | Faroe Islands | Streymoy/Tórshavn | Connectivity infrastructure; not DC | A/B：SHEFA official pages; C/B corroboration from TeleGeography map. URLs: https://www.shefa.fo/elbowroom/ , https://www.submarinecablemap.com/submarine-cable/shefa-2 |
| AWS/Azure/GCP/Oracle public cloud region | Faroe Islands | National | Not present on official region pages as of review date | A：official hyperscaler region pages listed in 2.5 |

## 7. 负向/观察覆盖 (Negative and Watch Coverage)

- **Streymoy**：confirmed hosting activity exists through Elektron and Nema; FT/NET and cable landing/connectivity are important but should not be counted as standalone commercial DC without further evidence. Continue Tórshavn permit, Keypsportal and SEV checks.
- **Eysturoy**：FARICE-1 branch lands at Funningsfjørður, but no confirmed commercial DC. Watch Runavík/Fuglafjørður/Eysturkommuna planning and SEV grid projects.
- **Norðoyar**：no confirmed DC/hosting facility from official sources. Watch Klaksvík/Nema/telecom network and municipal permits.
- **Vágar**：no confirmed DC. Watch airport/industrial permits and SEV.
- **Sandoy**：no confirmed DC. Watch post-tunnel industrial and utility changes.
- **Suðuroy**：no confirmed DC. Watch SEV island-grid/storage projects and municipal permits; grid projects are not DC evidence.

## 8. 更新节奏 (Update Cadence)

- **每月**：Elektron/Nema/FT/NET 新闻；Keypsportal `datacenter`/`hýsing`/`UPS`；SEV 新闻；Tórshavn permits。
- **每季**：Fjarskiftiseftirlitið operator list、PeeringDB/Pulse FO、Farice/SHEFA cable updates、local media。
- **每半年**：AWS/Azure/GCP/Oracle region pages、Skráseting company records、Elektron/Nema annual reports or policy documents。
- **年度**：按 6 个覆盖区域做完整负向扫描，并与 `explorer-industry.md` 对账。

事件触发：EIA screening、建筑许可、UPS/发电机/电力采购、大用户电网接入、新海缆/PoP、hosting provider 设施页、收购/品牌变更、政府云/身份平台采购。
