# TG Explorer Industry（行业线）· 多哥数据中心行业/媒体/厂商发现方法论

日期：2026-08-12。国家：**TG 多哥（Togo）**。分区模型（已核 `world-manifest.jsonl`）：**5 个大区（region）**：Central、Kara、Maritime、Plateaus、Savannahs（法文：Centrale、Kara、Maritime、Plateaux、Savanes）。商业/设施发现集中在 **Maritime - Lomé**。

行业线与 `explorer-official.md` 配套使用：行业来源用于发现、状态更新和技术细节；设施存在、投运、许可、融资和认证以官方/运营商/出资方一手来源优先。

可靠度分级：
- **A** = 一手/官方/运营商/出资方：Lomé Data Centre 官网、SIN/政府/部委、ARCEP、ARCOP、World Bank/IFC/AfDB/BOAD、CEET/CEB/ARSE、API-ZF/PIA、官方云区域列表。
- **A-** = 官方运营商或政府公告证明项目/服务/具名站点，但无许可/电力/地址/认证细节。
- **B** = 强二级：DatacenterDynamics、Togo First、Agence Ecofin、Connecting Africa、TechAfricaNews、Telecompaper、TeleGeography/SubmarineCableMap、ISOC Pulse、PeeringDB。
- **C** = 仅线索：DataCenterMap、Baxtel、datacenters.com、datacenterplanet、colo.exchange、LinkedIn/社交帖、无来源博客、未点名多哥站点的厂商营销。
- **U** = 未验证：仅见于聚合目录或单一弱来源；升级前必须复核。

规则：对具体声明分级。示例：Lomé Data Centre「存在性=A」「2021 启用=A-/B」「1+ MW=A（运营方营销值）」「五个 133 m2 服务器房=B」「Uptime 认证=A only if Uptime certificate/announcement found」。

---

## 0. 多哥行业框架（Industry Frame）

- 多哥市场很小，但有一个明确的核心设施：**Lomé Data Centre（LDC）**。它是洛美的运营中 carrier-neutral colocation / national data center，World Bank WARCIP 融资支持，政府 2022 页称其 2021 年 6 月已启用。
- 当前 LDC 官网营销 `1+ MW`、`800+ m2 usable space`、hosting、interconnection、remote hands、managed cybersecurity services，并列出 Equiano、regional IX partnerships、submarine/fiber routes。
- **ST Digital + SIN 私有云**是 2026 年服务级线索，部署在 LDC，不是新建物理数据中心。
- **互联资产强**：TGIX/TogoIX、WACS、Equiano。它们支持设施可用性判断，但不计 DC 容量。
- **超大规模云负向**：AWS/Azure/GCP/OCI 官方区域列表未列多哥 Region。
- 语言：法语召回最好；英语用于 DCD、World Bank、Connecting Africa、Telecompaper。关键词：`centre de données`、`data center`、`datacenter`、`carrier hotel`、`hébergement`、`colocation`、`cloud privé`、`salle des serveurs`、`fibre optique`、`point de présence`、`station d'atterrissement`、`mise en service`、`inauguration`。

---

## 1. 本地媒体与政府新闻（Local Press）

| 来源 | URL / 路由 | 用途 | 分级 |
|---|---|---|---|
| Togo First | https://www.togofirst.com/ | 多哥商业/经济新闻；LDC 2021 启用、SIN/ST Digital 2026 私有云 | B；引用官方时 A- |
| République Togolaise / Togo Officiel | https://www.republiquetogolaise.tg/ | 政府新闻；LDC 2022 私营管理授权与设施描述 | A |
| 数字部委 | https://numerique.gouv.tg/ | 部委项目页/新闻；部分旧内容页现为占位，需交叉验证 | A/A- |
| Agence Ecofin | https://www.agenceecofin.com/ | 法语数字/电信/融资报道 | B |
| ATOP | https://atop.tg/ | 官方通讯社线索；启用、部长活动、区域 ICT 新闻 | B/B+ |
| Togo Matin / Lomé Actu / TogoBreakingNews | 各站域 | 本地线索，需官方确认 | C+/B- |

查询模板：
```text
site:togofirst.com Togo "Lome Data Centre" OR "centre de donnees" OR "cloud prive"
site:republiquetogolaise.tg "Data Center de Lome" OR "Lome Data Centre"
site:numerique.gouv.tg "Lome Data Centre" OR "centre de donnees" OR datacenter
site:agenceecofin.com Togo "centre de donnees" OR datacenter OR "cloud prive"
site:atop.tg "centre de donnees" OR datacenter OR "Lome Data Centre"
```

生命周期动词：`projet / étude / MoU`（意向）；`appel d'offres / soumission / tender`（采购）；`construction / travaux / chantier`（在建）；`mise en service / inauguration / opérationnel / go-live`（启用）。

---

## 2. 非洲/国际行业媒体（African & International Trade Press）

| 来源 | URL / 路由 | 用途 | 分级 |
|---|---|---|---|
| DatacenterDynamics（DCD） | https://www.datacenterdynamics.com/ | LDC 2021 开通、World Bank WARCIP、ADC/SIN 运营角色、Equiano landing | B/B+ |
| Connecting Africa | https://www.connectingafrica.com/ | SIN/ST Digital 私有云、CSquared Woezon/Equiano 部署 | B |
| TechAfricaNews | https://techafricanews.com/ | 泛非数字基础设施线索；SIN/ST Digital 报道 | B/C |
| Telecompaper | https://www.telecompaper.com/ | 电信/云服务快讯；通常需原始来源补强 | B |
| Submarine Networks | https://www.submarinenetworks.com/ | 海缆系统与登陆线索；需 TeleGeography/运营方交叉 | B |
| IFC / World Bank | https://www.ifc.org/ ; https://www.worldbank.org/ | CSquared/Equiano、WARCIP 融资一手证据 | A |
| ADCA / market reports | https://africadca.org/ | 区域背景，不作为单独设施证据 | B/C |

查询模板：
```text
site:datacenterdynamics.com Togo "Lome Data Centre" OR "data center" OR Equiano
site:connectingafrica.com Togo "data center" OR "Lome Data Centre" OR CSquared OR "ST Digital"
site:techafricanews.com Togo "Lome Data Centre" OR "cloud" OR "SIN"
site:telecompaper.com Togo "Lome Data Centre" OR "ST Digital"
site:ifc.org CSquared Togo Equiano
```

---

## 3. 运营商/托管商/厂商（Operators, Hosters, Vendors）

| 实体 | 已核/线索 URL | 行业信号 | 分级与处理 |
|---|---|---|---|
| Lomé Data Centre（LDC） | https://lomedatacentre.tg/ | Hosting、colocation racks/private cages、interconnection、managed cybersecurity、1+ MW、800+ m2 | A |
| Société d'Infrastructures Numériques（SIN） | LDC/政府/媒体；无稳定单独官网已确认 | LDC 所有/运营、国家数字资产管理、ST Digital 合作 | A-/B，按来源拆分 |
| ST Digital Togo | https://stdigital.io/（集团）+ Togo First/Connecting Africa | 与 SIN 在 LDC 推出私有云服务 | B 服务级，不建新设施 |
| Africa Data Centres（ADC） | https://www.africadatacentres.com/ | 2021 报道称 ADC 管理/运营 LDC；当前 LDC 官网未明显以 ADC 品牌呈现 | B 历史运营角色；需最新官方确认 |
| Togocom / Yas / Togo Telecom / Togocel | https://togocom.tg/ 等品牌页 | 运营商核心网、客户/连接；仅点名 hosting/colo/DC 时记录 | B/C，普通电信服务不计 DC |
| Moov Africa Togo | https://moov-africa.tg/ | 运营商核心网/企业服务；LDC 官网客户/生态 logo 线索 | B/C |
| CSquared Woezon / CSquared Togo | https://csquared.com/togo/ | Equiano landing、eGouv metro fiber、CEB fiber commercialisation | A-/B 互联，不是 DC |
| TogoIX / TGIX | ISOC Pulse、PeeringDB | 洛美 IXP，LDC 相邻互联线索 | B 互联 |
| PIA Adétikopé | https://pia-togo.com/ | 工业/自贸平台；ICT 租户 watch zone | A 园区；DC=U/negative until sourced |

运营商查询模板：
```text
site:lomedatacentre.tg hosting OR colocation OR "private cages" OR interconnection
"Societe d'Infrastructures Numeriques" Togo "Lome Data Centre" OR "data center"
"ST Digital" Togo "Lome Data Centre" OR "cloud prive"
site:togocom.tg "data center" OR datacenter OR "centre de donnees" OR hebergement OR cloud
site:moov-africa.tg "data center" OR datacenter OR "centre de donnees" OR hebergement
site:csquared.com/togo Equiano OR "eGouv" OR "metro fiber" OR "Lome"
```

---

## 4. 互联、IXP、聚合目录与云负向

| 渠道 | URL | 用途 | 分级 |
|---|---|---|---|
| LDC 官网 | https://lomedatacentre.tg/ | 当前服务、容量、生态、互联 | A |
| TogoIX/TGIX | https://pulse.internetsociety.org/en/ixp-tracker/country/TG/ ; PeeringDB | 洛美 IXP、成员与容量线索 | B |
| WACS | https://www.submarinecablemap.com/ ; Submarine Networks | Lomé/Afidegnigba 直接登陆 | B |
| Equiano | CSquared Togo、DCD、Submarine Networks、SubmarineCableMap | Lomé 直接登陆/CLS | A-/B |
| GLO-1 | Submarine Networks/SubmarineCableMap | 未确认 Togo direct landing；可能为 Ghana 回程线索 | B 负向/线索 |
| DataCenterMap | https://www.datacentermap.com/togo/ | LDC/LOM1 目录发现 | C，须 LDC/政府补强 |
| Baxtel | https://baxtel.com/data-center/togo | LDC/ADC: Lome LOM1 目录发现 | C，容量数字谨慎 |
| Uptime Institute | https://uptimeinstitute.com/ | Tier 认证核验 | A only if exact certificate/announcement; otherwise U |
| 云区域 | AWS/Azure/GCP/OCI 官方区域页 | 多哥 Region 负向证据 | A 负向 |

聚合/IXP 查询模板：
```text
"TogoIX" OR TGIX OR "Togo Internet Exchange Point" Lome
site:peeringdb.com "Lome Data Centre" OR "TGIX" OR Togo
site:datacentermap.com Togo "Lome Data Centre" OR LOM1
site:baxtel.com Togo "Lome" OR "Lome Data Centre"
site:uptimeinstitute.com Togo "Lome Data Centre" OR "SIN-1-LOME"
site:submarinecablemap.com WACS OR Equiano Togo Lome
```

---

## 5. 搜索模板（Search Templates）

### 5.1 英语模板

```text
"Togo" ("data center" OR "data centre" OR datacenter OR colocation) (Lome OR Lomé OR Maritime)
"Lome Data Centre" OR "Lomé Data Centre" (SIN OR "Africa Data Centres" OR "ST Digital" OR "World Bank")
"Togo" "carrier-neutral colocation data center" OR "carrier hotel"
"Togo" "data center" (inauguration OR operational OR "private cloud" OR MW OR racks)
"Togo" (WACS OR Equiano OR "GLO-1") (landing OR "landing station" OR "submarine cable")
filetype:pdf Togo "data center" OR "centre de donnees" OR "hebergement des donnees"
```

### 5.2 法语模板

```text
"Togo" ("centre de donnees" OR "data center" OR datacenter OR "centre d'hebergement" OR colocation)
"Lome Data Centre" OR "Data Center de Lome" "mise en service" OR inauguration OR "cloud prive"
"Societe d'Infrastructures Numeriques" Togo "centre de donnees" OR "Lome Data Centre"
"Togo" "appel d'offres" ("centre de donnees" OR serveurs OR hebergement OR "infrastructure numerique")
"Togo" (WACS OR Equiano OR "GLO-1" OR "cable sous-marin" OR "station d'atterrissement") Lome
"Adetikope" OR PIA Togo ("centre de donnees" OR datacenter OR numerique)
```

---

## 6. 分区枚举矩阵（Division Enumeration Matrix）

| 大区 | 搜索种子 | 预期产出/编码指引 |
|---|---|---|
| **Maritime** | `Lome/Lomé`、LDC、SIN、ST Digital、Togocom/Yas、Moov Africa、TogoIX/TGIX、WACS、Equiano、CSquared Woezon、`Adétikopé`/PIA、Grand Lomé | 正簇：Lomé Data Centre；服务级：ST Digital private cloud at LDC；互联资产：TGIX、WACS、Equiano；watch：PIA 与运营商核心/托管。 |
| **Plateaus（Plateaux）** | `Atakpamé`、`Kpalimé`、`Plateaux` + `centre de donnees`/`salle de serveurs`/`fibre`/`point de presence` | `no_projects_expected`；大学/行政/运营商 PoP 需具名托管证据才记录。 |
| **Central（Centrale）** | `Sokodé`、`Tchamba`、`Centrale` + 电信/光纤/许可词 | `no_projects_expected`；交换机房不自动计数。 |
| **Kara** | `Kara` 市、`Université de Kara`、`Niamtougou` + server/cloud/hosting | `no_projects_expected`；大学计算房线索仅作 C。 |
| **Savannahs（Savanes）** | `Dapaong`、`Mango`、`Savanes`、布基纳边境走廊/光纤 | `no_projects_expected`。 |

分区查询块：
```text
"Lome" OR "Lomé" OR "Maritime" Togo ("data center" OR datacenter OR "centre de donnees" OR colocation OR hebergement OR TGIX)
"Atakpame" OR "Kpalime" OR "Plateaux" Togo ("data center" OR "centre de donnees" OR "salle de serveurs" OR fibre)
"Sokode" OR "Tchamba" OR "Centrale" Togo ("data center" OR "centre de donnees" OR serveurs OR fibre)
"Kara" OR "Niamtougou" Togo ("data center" OR "centre de donnees" OR serveurs OR universite)
"Dapaong" OR "Mango" OR "Savanes" Togo ("data center" OR "centre de donnees" OR serveurs OR fibre)
```

负向搜索规则：ICT 办公室、网吧、NGO 服务器房、GIS 房、软件平台、普通运营商 PoP 不计数，除非来源描述具名运营者+位置的托管/colo/计算基础设施。

---

## 7. 分级与验证规则（Grading & Verification Rules）

- **A 运营设施**：官方/运营商/出资方来源点名站点+位置+基础设施功能。Lomé Data Centre 当前满足。
- **B 运营设施**：强媒体点名站点/位置且足以区分设施，最好引用官方。
- **C 线索**：聚合目录、社交/招聘帖、经销商页、无本地物理证据的服务页。
- **U 未验证**：目录 DC、未核 Uptime/TIA 认证、GLO-1 直接登陆、PIA 数据中心租户、运营商未点名设施的 cloud/hosting 营销。
- **服务级**：ST Digital/SIN 私有云、运营商云、托管报价但无新物理站点，保留为服务，不新增设施。
- **互联资产**：TGIX/TogoIX、WACS、Equiano、GLO-1 回程、PeeringDB PoP、陆地光纤不是 DC 容量。
- **容量**：除非官方/运营商/招标来源明示，MW/机架/面积一律 null；LDC 运营方数字可写但保留原文单位。
- **云**：AWS/Azure/GCP/OCI 官方区域页 = 多哥负向证据。
- **去重**：LDC 可能承载 IXP、运营商、私有云或网络 PoP；按物理设施、服务、互联资产分别记录，不把服务当新楼。

---

## 8. 已记录的多哥数据中心/互联公告（Documented Announcements）

1. **Lomé Data Centre（Maritime - Lomé）**：已投运。政府官方页称 2021 年 6 月启用、2022 年授权交由私人主体管理；World Bank WARCIP 融资支持；LDC 官网营销 hosting/interconnection、1+ MW、800+ m2 usable space。状态写 `operational`。
2. **SIN + ST Digital private cloud at LDC**：2026 年报道的私有云服务，部署在 LDC。状态写 `marketed_service` 或 `service_at_existing_facility`，不新增数据中心。
3. **TogoIX/TGIX**：洛美运营中 IXP；互联资产。
4. **WACS + Equiano Lomé landings**：直接海缆登陆；互联资产。Equiano 是旧草稿缺口，现已补为确认线索。
5. **GLO-1**：未确认多哥直接登陆；不得写 Lomé landing。
6. **PIA Adétikopé**：工业园区 watch zone；无 DC 租户证据前不建记录。

每批核查动作：① LDC 官网与 news 页 ② `republiquetogolaise.tg`/`numerique.gouv.tg`/Togo First ③ World Bank/IFC ④ DCD/Connecting Africa/Agence Ecofin ⑤ ISOC Pulse/PeeringDB/SubmarineCableMap ⑥ AWS/Azure/GCP/OCI 官方区域页。

---

## 9. 来源锚点（Source Anchors）

- LDC 官方：https://lomedatacentre.tg/
- 政府：https://www.republiquetogolaise.tg/ ; https://www.gouv.tg/ ; https://numerique.gouv.tg/
- 监管：ARCEP https://arcep.tg/ ; ARCOP https://arcop.tg/
- 电力：CEET https://www.ceet.tg/tg/ ; CEB https://www.cebnet.org/ ; ARSE https://www.arse.tg/
- 数据保护/网络安全：IPDCP https://ipdcp.tg/ ; ANCy https://ancy.gouv.tg/ ; CERT.tg https://cert.tg/
- 投资/园区：API-ZF https://apizf.org/ ; PIA https://pia-togo.com/
- 媒体/行业：Togo First https://www.togofirst.com/ ; DCD https://www.datacenterdynamics.com/ ; Connecting Africa https://www.connectingafrica.com/ ; Agence Ecofin https://www.agenceecofin.com/
- 互联：SubmarineCableMap https://www.submarinecablemap.com/ ; ISOC Pulse https://pulse.internetsociety.org/ ; PeeringDB https://www.peeringdb.com/ ; CSquared Togo https://csquared.com/togo/
- 云区域负向：AWS、Azure、Google Cloud、Oracle OCI 官方区域列表。

最终说明：多哥枚举应围绕一个已运营的 LDC 设施展开，谨慎分离「物理数据中心」「私有云服务」「IXP」「海缆登陆站」「运营商 PoP」。行业目录可用于发现别名（如 LOM1/ADC Lome），但不得覆盖官方/运营方证据。
