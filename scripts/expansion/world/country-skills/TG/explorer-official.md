# TG Explorer Official（官方线）· 多哥数据中心官方/监管枚举方法论

日期：2026-08-12。国家：**TG 多哥（Togo）**。分区模型（已核 `world-manifest.jsonl`）：**5 个大区（region）**：Central、Kara、Maritime、Plateaus、Savannahs。法语常用拼写：Région Centrale、Région de la Kara、Région Maritime、Région des Plateaux、Région des Savanes；检索别名保留 `Plateaus/Plateaux`、`Savannahs/Savanes`、`Central/Centrale`。首都洛美（Lomé）位于 Maritime 区，并处在大洛美（Grand Lomé）城市圈。

范围：商业、电信、政府、企业与管线（pipeline）数据中心设施的官方与监管证据。多哥没有公开的国家数据中心注册库，官方枚举采用证据链：设施/运营者名称 -> 政府或运营方页面 -> 监管许可/决定 -> 建设或环评许可 -> 电力接入 -> 海缆/互联 -> 采购/融资记录。

可靠度分级：
- **A** = 一手/官方证据：`gouv.tg`、`republiquetogolaise.tg`、数字部委、Lomé Data Centre 官方站、ARCEP、ARCOP/公共采购、CEET/CEB/ARSE、IPDCP、世界银行/IFC/AfDB/BOAD、API-ZF/PIA 官方页、官方云区域页。
- **A-** = 政府、国有运营实体或运营商公告可证明具名设施/服务存在，但未给出许可、电力、地址或认证细节。
- **B** = 可信二级证据且含具体当事方/日期/地点事实：DatacenterDynamics、Togo First、Agence Ecofin、Connecting Africa、TeleGeography/SubmarineCableMap、ISOC Pulse、PeeringDB。
- **C** = 仅线索：目录站、SEO 列表、社交帖、市场报告、无来源的机架/MW/面积表、Wikipedia。
- **U** = 未验证：仅见于聚合目录或单一弱来源；升级前必须复核。

规则：对**具体声明**分级，而不是对整座设施分级。同一设施可「存在性=A」「开通日期=A/B」「Tier 认证=A-/B」「MW=A」「机架数=C」。

---

## 0. 多哥结构事实（Structure Facts）

- **已确认正簇：Maritime - Lomé**。Lomé Data Centre 是已投运的国家/运营商中立托管设施；TogoIX/TGIX、WACS 与 Equiano 海缆登陆、运营商总部和核心网络也集中在洛美。
- **其余四区（Plateaus、Central、Kara、Savannahs）预期低产出**。只在来源点名具名运营者+位置+托管/colo/计算基础设施时建记录；大学服务器房、行政系统、普通光纤 PoP 不自动计为数据中心。
- **官方云区域负向**：截至 2026-08-12，AWS、Azure、Google Cloud、Oracle OCI 官方区域列表未列多哥公有云 Region；CDN/缓存/边缘节点、经销商或本地云服务不得升级为 hyperscaler region。
- **容量处理**：多哥来源很少给 MW。Lomé Data Centre 官方页给出 `1+ MW`、`800+ m2 usable space`，Togo First 2021 报道给出 1 MW 主电源和两台 1000 kVA 发电机；不要从建筑面积或发电机规格反推 IT 负载。

---

## 1. 已核官方/准官方入口（Verified Official Anchors）

| 主题 | 已核 URL | 用途 | 分级 |
|---|---|---|---|
| 政府门户 | https://www.gouv.tg/ ; https://www.republiquetogolaise.tg/ | 政府新闻、路线图、政务文件；后者有 Lomé Data Centre 2022 管理安排报道 | A |
| 数字部委 | https://numerique.gouv.tg/ | 数字政策、项目新闻；Lomé Data Centre 旧新闻页存在但当前内容页显示占位，需交叉验证 | A/A- |
| Lomé Data Centre | https://lomedatacentre.tg/ | 运营设施、服务、容量、互联生态 | A |
| 电信监管 | https://arcep.tg/ | ARCEP 通信电子/邮政监管；法律、决定、许可、注册表 | A |
| 公共采购监管 | https://arcop.tg/ | ARCOP 采购监管、审查、公共采购线索 | A |
| 电力 | https://www.ceet.tg/tg/ ; https://www.cebnet.org/ ; https://www.arse.tg/ | CEET 配售电、CEB 区域输电、ARSE 电力监管/许可 | A |
| 数据保护 | https://ipdcp.tg/ | IPDCP；个人数据保护监管，不证明物理设施 | A |
| 投资/自贸区 | https://apizf.org/ ; https://pia-togo.com/ | API-ZF、PIA Adétikopé 投资/园区线索 | A |
| 国际融资 | https://www.worldbank.org/ ; https://projects.worldbank.org/ ; https://www.ifc.org/ | WARCIP/WARDIP/IFC 数字基础设施融资与采购 | A |

已纠正：旧草稿中的 `artp.tg` 不作为主入口；多哥现用监管入口为 **ARCEP**（Autorité de Régulation des Communications Électroniques et des Postes）`arcep.tg`。`adetic.tg`/`adetic.td` 指向乍得相关 ADETIC，不得作为多哥官方来源。

---

## 2. 核心设施与官方证据（Facility Seeds）

| 设施/项目 | 当前状态 | 分区 | 官方处理 | 证据与备注 |
|---|---|---|---|---|
| **Lomé Data Centre / LDC / Centre de Données de Lomé** | **operational** | Maritime - Lomé | 存在性/服务=A；2021 启用=A-/B；World Bank 融资=A；当前容量=运营方 A | 政府官方页称 2021 年 6 月已启用、首个中立 colocation centre，并在 2022 年授权交由私人主体管理；World Bank 2021 新闻确认 WARCIP additional financing 支持 carrier-neutral colocation data center；LDC 官网列 hosting、interconnection、1+ MW、800+ m2 usable space、Equiano/IX 路由。 |
| **Société d'Infrastructures Numériques（SIN）** | owner/operator entity | Maritime - Lomé | A-/B，按来源拆分 | 政府/媒体称 SIN 管理国家数字资产并控制 LDC；当前行业报道称 SIN 运营 LDC 并与 ST Digital 合作私有云。若要写运营者，优先使用 LDC 官网/政府公告；Africa Data Centres 的 2021 管理角色需标日期。 |
| **ST Digital private cloud at LDC** | marketed/private cloud service | Maritime - Lomé | B，待官方合同/新闻升级 | Togo First、Connecting Africa 2026 报道 SIN 与 ST Digital 在 LDC 推出私有云服务；服务级记录，不等同新物理 DC。 |
| **TogoIX / TGIX** | operational IXP | Maritime - Lomé | B 互联资产 | ISOC Pulse 列 TGIX/Togo Internet Exchange Point；PeeringDB/LDC 可作设施位置线索。IXP 不计为 DC 容量。 |
| **WACS landing - Lomé/Afidegnigba** | operational cable landing | Maritime | B/A- 互联资产 | SubmarineCableMap/TeleGeography 与行业源列 WACS 在洛美/附近登陆。登陆站不是数据中心，除非来源点名托管功能。 |
| **Equiano landing - Lomé** | operational cable landing | Maritime | A-/B 互联资产 | Google/CSquared/SIN 公告经行业源确认 Equiano 2022 年在洛美登陆；CSquared Togo 页列 Equiano landing and CLS。旧草稿未确认 Equiano，定稿已补入。 |
| **GLO-1** | no confirmed direct Togo landing | n/a | B 负向/回程线索 | Submarine Networks/TeleGeography 常列 Nigeria、Ghana、Senegal、Mauritania、Morocco、Portugal、Spain、UK 等登陆点；无可靠来源前不要写 Lomé 直接登陆。 |
| **PIA Adétikopé** | watch zone, no DC confirmed | Maritime - Adétikopé | A 园区；DC=U/negative until sourced | PIA 官网确认 Togo + ARISE IIP 公私合作工业平台；无数据中心租户证据前不建设施。 |

---

## 3. 监管与许可路径（Regulatory Path）

### 3.1 ARCEP - 通信监管

ARCEP 是多哥电子通信与邮政监管机构。ARCEP 页面列出 Loi n°2012-018 sur les communications électroniques、Loi n°2013-003 修订、Décret n°2015-091/PR 组织运作、互联与业务许可相关法令。ARCEP **不是**数据中心建设许可机关；用于核实运营商许可、网络互联、频谱/VSAT/电子信任服务、`.tg` 域名与通信基础设施线索。

查询模板：
```text
site:arcep.tg "{operateur}" licence OR autorisation OR decision
site:arcep.tg "centre de donnees" OR "data center" OR hebergement OR colocation
site:arcep.tg "cable sous-marin" OR "station d'atterrissement" OR "fibre optique"
site:arcep.tg "Lome Data Centre" OR "Societe d'Infrastructures Numeriques" OR SIN
```

分级：ARCEP 页面/下载 = **A**；可信媒体转述 ARCEP 决定 = **B**；无 URL 的许可清单 = **C**。

### 3.2 数字政府、数据保护与网络安全

- 数字部委：`numerique.gouv.tg` 是已核入口；当前部委名显示为 Ministère de l'Efficacité du Service Public et de la Transformation Numérique。历史名称 `Ministère de l'Économie Numérique et de la Transformation Digitale` 可保留作搜索别名。
- ANCy：`ancy.gouv.tg` 为已核官方站；其页面称 ANCy 由 Loi n°2018-026 du 07 décembre 2018 sur la cybersécurité et la cybercriminalité 创建。用于关键信息基础设施/安全标准线索，不证明物理 DC。
- IPDCP：`ipdcp.tg` 为已核官方站；页面称 IPDCP 由 Loi n°2019-014 relative à la protection des données à caractère personnel 创建。数据保护登记/合规不证明物理设施。

查询模板：
```text
site:numerique.gouv.tg "Lome Data Centre" OR "centre de donnees" OR datacenter
site:republiquetogolaise.tg "Data Center de Lome" OR "centre de donnees"
site:ancy.gouv.tg "centre de donnees" OR "infrastructure critique" OR hebergement
site:ipdcp.tg hebergement OR "centre de donnees" OR "transfert transfrontalier"
```

### 3.3 采购、融资、投资

公共采购监管入口为 `arcop.tg`；数据中心项目采购通常更可能出现在世界银行/IFC/AfDB 或部委文件中。World Bank 2021 press release 确认 WARCIP additional financing 用于 carrier-neutral colocation data center，并给出 WARCIP-Togo 总额 $30m、追加融资 $11m。不要把 WARDIP 项目编号写入 TG 记录，除非当批从 World Bank 项目页直接核到 Togo 组件。

查询模板：
```text
site:arcop.tg "centre de donnees" OR datacenter OR "infrastructure numerique"
site:worldbank.org Togo WARCIP "carrier-neutral colocation data center"
site:projects.worldbank.org Togo "data center" OR "centre de donnees" OR WARCIP OR WARDIP
site:ifc.org CSquared Togo Equiano "data center" OR "landing"
site:apizf.org "data center" OR datacenter OR "centre de donnees" OR numerique
site:pia-togo.com "data center" OR datacenter OR "centre de donnees" OR TIC
```

### 3.4 电力、环境、建设许可

- CEET：`www.ceet.tg/tg/`，配电/售电与接入线索。
- CEB：`www.cebnet.org/`，贝宁-多哥发输电共同体，跨境/高压输电线索。
- ARSE：`www.arse.tg/`，电力监管、生产/自发电/许可和服务质量。
- 环评/建设许可：按 Grand Lomé、Golfe/Agoè-Nyivé 等地方政府与环境关键词检索；未见统一机检全国数据库。备用发电机、燃料、冷却、水耗、噪音等只能按 EIES/许可原文记录。

查询模板：
```text
site:ceet.tg "Lome Data Centre" OR datacenter OR "centre de donnees" OR raccordement
site:arse.tg "Lome Data Centre" OR datacenter OR "autoproduction" OR "groupe electrogene"
"Lome Data Centre" "permis de construire" OR EIES OR "certificat de conformite"
"Grand Lome" "centre de donnees" OR datacenter OR "permis de construire"
```

---

## 4. 海缆与互联（Submarine Cables & Interconnection）

已核处理：
- **WACS**：可作为 Lomé/Afidegnigba 直接登陆证据；互联资产，非 DC。
- **Equiano**：已补为多哥直接登陆证据。CSquared Togo 页面列 Equiano landing in Lomé/CLS；行业报道称 Google、SIN、CSquared 公告 2022 年在洛美登陆。
- **GLO-1**：未确认多哥直接登陆。可记录「经加纳/区域回程线索」但不得写 Lomé landing。
- **TogoIX/TGIX**：ISOC Pulse/PeeringDB 证据可用于互联生态和 LDC 相邻线索；不计入商业 DC 容量。

查询模板：
```text
site:submarinecablemap.com WACS Lome Togo
site:submarinecablemap.com Equiano Lome Togo
site:csquared.com Togo Equiano Lome "landing"
"Togo Internet Exchange Point" OR TGIX OR TogoIX Lome
site:pulse.internetsociety.org "Togo Internet Exchange Point" OR TGIX
site:peeringdb.com "Lome Data Centre" OR TGIX OR Togo
```

---

## 5. 官方云区域负向检查（Cloud-Region Negative Evidence）

每批运行对照官方页面：
- AWS Regions/AZs: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- Azure regions: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud locations: https://cloud.google.com/about/locations
- Oracle OCI regions: https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm

截至 2026-08-12，四家官方列表均未列多哥公有云 Region。负向证据 = **A（按核验日期）**。不得从 CDN、edge cache、Marketplace、本地合作伙伴、私有云服务或数据驻留营销创建多哥 hyperscaler facility。

---

## 6. 分区官方覆盖图（Per-Division Official Coverage Map）

| 大区 | 官方策略 | 当前预期产出 |
|---|---|---|
| **Maritime** | 搜 Lomé/LDC/SIN/ST Digital、TogoIX/TGIX、WACS、Equiano、CSquared Woezon、Togocom/Yas/Moov、Grand Lomé 建设/环评、CEET 接入、PIA/Adétikopé。 | 正簇：Lomé Data Centre；互联资产：TGIX、WACS、Equiano；watch：PIA、运营商核心/托管服务。 |
| **Plateaus（Plateaux）** | 搜 Atakpamé、Kpalimé、Plateaux + `centre de donnees`/`salle serveurs`/`fibre`/`mairie`/`CEET`。 | `no_projects_expected`，仅 PoP/行政机房线索。 |
| **Central（Centrale）** | 搜 Sokodé、Tchamba、Centrale + 电信节点/光纤/许可/服务器房。 | `no_projects_expected`，交换机房需官方证据。 |
| **Kara** | 搜 Kara、市政府、Université de Kara、Niamtougou + 服务器/ICT/云/托管。 | `no_projects_expected`，大学计算房线索不自动计数。 |
| **Savannahs（Savanes）** | 搜 Dapaong、Mango、Savanes + 边境光纤、政府机房、CEET/电信。 | `no_projects_expected`。 |

分区通用扫描：
```text
"{division_or_city}" Togo "centre de donnees" OR datacenter OR "data center" OR "salle de serveurs"
"{division_or_city}" Togo hebergement OR colocation OR cloud OR "point de presence"
site:arcep.tg "{division_or_city}" fibre OR licence OR autorisation
site:ceet.tg "{division_or_city}" raccordement OR poste OR "grand client"
site:republiquetogolaise.tg "{division_or_city}" numerique OR "centre de donnees"
```

负向规则：`no_projects: true` 仅在完成带日期与查询记录的扫网后写入，不得静默遗漏。

---

## 7. 计数、分级与去重规则

- 设施存在当且仅当来源点名**基础设施+位置**且足以区分物理站点。无具名站点的托管/云服务 = 服务级线索，单独保留。
- `facility_type` 保持精确：`commercial_colocation`、`government_hosting`、`national_data_center`、`telco_core`、`ixp`、`landing_station`、`planned_commercial_dc`、`lead_only`、`negative`。
- `status` 保持精确：`operational`、`marketed_service`、`announced`、`procurement`、`under_construction`、`commissioning`、`unknown`、`negative`。
- Lomé Data Centre 当前应写 `operational`，而不是 `announced/under_construction`。
- 「Tier III」若由政府/运营方称述可记声明；若需认证级事实，必须查 Uptime Institute 证书/公告或证书号。`Tier III+` 不是标准 Uptime 等级，按营销措辞记录。
- MW/机架/面积字段：只记录来源明示单位。LDC 可记录运营方 `1+ MW`、`800+ m2 usable space`；Togo First 2021 的 server-room/generator details 作为 B 级补充。
- 去重：LDC、TGIX、WACS/Equiano landing、Togocom/Moov 核心网络、ST Digital 私有云服务分开；IXP/landing station 不计商业 DC 容量。

---

## 8. 输出字段模板（Output Guidance）

```json
{
  "country_code": "TG",
  "division": "Maritime",
  "commune": "Lome",
  "name": "Lome Data Centre",
  "operator": "Societe d'Infrastructures Numeriques (SIN) / current operator per latest official source",
  "status": "operational",
  "facility_type": "national_data_center / carrier_neutral_colocation",
  "capacity_mw": 1.0,
  "capacity_mw_note": "operator markets 1+ MW; do not infer IT load beyond source wording",
  "area_sqm": 800,
  "area_note": "operator markets 800+ m2 usable space; 2021 media gives five 133 m2 server rooms",
  "tier": "Tier III / Tier III+ claim; require Uptime certificate for certification-grade field",
  "source_urls": [
    "https://lomedatacentre.tg/",
    "https://www.republiquetogolaise.tg/infrastructures/2212-7585-le-data-center-de-lome-sera-confie-a-un-operateur-prive",
    "https://www.worldbank.org/en/news/press-release/2021/05/24/improving-connectivity-in-togo-through-digital-infrastructure"
  ],
  "evidence_grade": "A for current operator/government/World Bank existence; B for trade-media technical details",
  "evidence_date": "2026-08-12"
}
```

最终说明：多哥是小市场，官方枚举应以 Lomé Data Centre 为核心，补足互联资产和运营商/服务线索；不要把海缆登陆站、IXP、私有云服务或普通电信 PoP 误计为独立数据中心。
