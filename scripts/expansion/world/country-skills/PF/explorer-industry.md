# PF Explorer — 行业/媒体/厂商 (Industry / Trade Press / Vendor) — 法属波利尼西亚数据中心枚举方法

日期：2026-08-12。国家：**PF 法属波利尼西亚 (French Polynesia / Polynésie française / Pōrīnetia Farāni)**。
Manifest 已核对：`subnational_type = country`，**1 个分区：`French Polynesia`**。

本文件角度：行业媒体、厂商与目录发现；用于补全官方文件之外的新闻、客户、容量、扩容、海缆和供应链线索。保持规则：行业源用于发现与佐证，最终设施存在/地址/状态尽量回挂官方或法定来源。

可靠性分级：**A** = 官方运营商/业主页面、公共部门页面、监管/注册记录、官方招标、官方云/区域页面、交易所/公司文件、官方项目文件；**B** = 署名可靠的本地/区域/行业媒体（含日期与当事方）；**C** = 目录站、海缆地图库、SEO 主机页、社交媒体、无来源聚合。

---

## 0. 行业格局判断（Market Shape）

**法属波利尼西亚是小型已确认数据中心市场，不是空白市场。** 已验证线索集中在 Tahiti：

1. **Tahiti Nui Fortress (TNF)**：Tahiti Nui Telecom / Groupe OPT 体系；官方站点提供 datacenter、cloud、dedicated server、security、colocation/baie/salle informatique；地址在 Papenoo PK 16.7。分类：`operator_colo`。
2. **TDF Pic Rouge / Papeete**：TDF 官方宣布 2025-09-18 开放 Papeete Pic Rouge 数据中心，2025-06 交付，首批客户 Banque de Polynésie 与 Axians Polynésie，2026 计划扩容。分类：`commercial_colo` 或 `operator_colo`（取决于项目 schema 对 TDF 的运营商类别）。
3. **政府/机构托管需求**：DSI/SIPF、市镇、银行、大学、医疗、媒体等是本地客户/招标线索；单个企业机房默认 `enterprise_server_room`，不计商用 DC。
4. **海缆/卫星邻近资产**：Honotua、NATITUA、Manatua、Google Honomoana/Tabua、OneWeb/Galileo 站点可解释连接性与站点聚集，但不得替代 DC 证据。

核心结论写法：**confirmed small market / marché local confirmé mais très petit**。容量通常不公开，必须避免从目录站过度采信 MW/机柜数。

---

## 1. 行业媒体与贸易新闻（Trade Press & Media）

| 媒体/渠道 | URL / 查询路由 | 用途 | 等级 |
|---|---|---|---|
| TDF 官方新闻 | https://www.tdf.fr/en/tdf-inaugure-son-premier-data-center-a-papeete-en-polynesie-francaise/ | TDF Pic Rouge opening、交付、客户、扩容、Tier III level 审计 | A |
| Tahiti Nui Fortress 官方 | https://www.tnfortress.pf/ | TNF 服务、Papenoo 地址、法人、cloud/colo | A |
| Tahiti Infos | https://www.tahiti-infos.com/ | TNF 建成、企业托管、本地数字项目 | B |
| TNTV News | https://www.tntvnews.pf/ | TDF Pic Rouge 采访、扩容/baies/投资额、SIPF 招标线索 | B |
| Polynésie La 1ère | https://la1ere.francetvinfo.fr/polynesie/ | TDF/TNF/政府项目、电视广播基础设施 | B |
| La Dépêche de Tahiti | https://www.ladepeche.pf/ | 本地经济、企业、海缆、能源新闻 | B |
| RNZ Pacific | https://www.rnz.co.nz/pacific | 太平洋海缆、区域互联 | B |
| Data Center Dynamics | https://www.datacenterdynamics.com/ | TDF launch、Google/海缆、目录交叉核验 | B |
| AFD | https://www.afd.fr/ | NATITUA 融资与项目范围 | B（公共金融机构项目页，接近 A 但非设施业主） |
| Submarine Networks / TeleGeography map | https://www.submarinenetworks.com/ ；https://www.submarinecablemap.com/ | 海缆系统名、landing point 初筛 | B/C |
| Baxtel / DataCenterMap / DataCenters.com | baxtel.com、datacentermap.com、datacenters.com | DC 名称、目录坐标、容量发现 | C |

媒体查询模板：
```text
site:tntvnews.pf ("data center" OR datacenter OR "centre de données" OR "Pic Rouge" OR "Tahiti Nui Fortress")
site:tahiti-infos.com ("data center" OR datacenter OR "centre de données" OR "Tahiti Nui Fortress")
site:la1ere.francetvinfo.fr/polynesie ("data center" OR datacenter OR "centre de données" OR "Pic Rouge")
site:ladepeche.pf (datacenter OR "centre de données" OR "câble sous-marin")
site:datacenterdynamics.com ("French Polynesia" OR Tahiti OR Papeete) ("data center" OR datacenter OR cable)
"TDF" "Pic Rouge" "Papeete" ("data center" OR "centre de données" OR "baies")
"Tahiti Nui Fortress" ("Data Center" OR cloud OR colocation OR hébergement)
```

使用要点：捕获动词与日期：`annoncé`、`livré`、`inauguré`、`ouvert`、`opérationnel`、`extension prévue`、`accueille ses premiers clients`。把 “planned extension 2026” 与当前 operational 容量分开。

---

## 2. 运营商、设施与厂商（Operators, Facilities & Vendors）

| 主体 | 来源 URL / 路由 | 证据用途 | 等级 |
|---|---|---|---|
| Tahiti Nui Fortress | https://www.tnfortress.pf/datacenter/ | Data Center、colocation、baie/salle informatique、24/7 访问 | A |
| Tahiti Nui Fortress Cloud | https://www.tnfortress.pf/cloud/ | Cloud/hosted applications/data/platforms | A |
| Tahiti Nui Fortress legal/contact | https://www.tnfortress.pf/mentions-legales/ ；https://www.tnfortress.pf/contact/ | 法人 Tahiti Nui Telecom、RCS Papeete、Papenoo PK 16.7 | A |
| Tahiti Nui Telecom | https://www.tahitinuitelecom.pf/ | OPT 子公司、satellite/cable/cloud/fortress 品牌 | A |
| Groupe OPT | https://groupe.opt.pf/ | 母集团、海缆、NATITUA、公共运营商背景 | A |
| ONATi / Vini | https://www.onati.pf/ ；https://www.vini.pf/ | 电信服务与接入品牌；DC 需回挂 TNF/TNT | A（电信） |
| TDF | https://www.tdf.fr/ | Pic Rouge data center、TDF edge/colo 策略 | A |
| Banque de Polynésie / Axians Polynésie | 官方页 + TDF 新闻 | TDF 首批客户；不等于自营 DC | A/B |
| DSI/SIPF | https://www.service-public.pf/dsi/ | 政府 IT/潜在托管采购 | A（政府上下文） |
| EDT | https://www.edt.pf/ | 电力上下文 | A |
| ASN / NEC / Google / AFD | 官方新闻页 | 海缆供应链与项目事实 | A/B |
| Schneider / Vertiv / Caterpillar / Cummins 等 | 厂商新闻、招标 | UPS、冷却、发电机线索 | C 起，除非合同/业主确认 |

运营商/厂商查询模板：
```text
"Tahiti Nui Fortress" (rack OR baie OR colocation OR "salle informatique" OR "Tier3+" OR "Tier 3")
"Tahiti Nui Telecom" (datacenter OR "data center" OR cloud OR Papenoo OR "PK 16,7")
"TDF" "Polynésie française" ("data center" OR "Pic Rouge" OR "Tier III" OR "photovoltaïque")
"Banque de Polynésie" "TDF" "data center"
"Axians Polynésie" "TDF" "data center"
"Schneider Electric" OR Vertiv OR Cummins OR Caterpillar Tahiti ("data center" OR "salle serveurs" OR climatisation)
```

---

## 3. 云区域与超大规模（Cloud Regions & Hyperscalers）

**PF 无已确认公有云 region / availability zone。** 官方全球位置页应作为负面控制：
- AWS Regions and Availability Zones：https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html
- Azure geographies/regions：https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies
- Google Cloud locations：https://cloud.google.com/about/locations
- OCI public cloud regions：https://www.oracle.com/cloud/public-cloud-regions/

Google 在 PF 的相关资产是 **subsea cable / landing infrastructure**，不是 Google Cloud region。Google 官方 South Pacific Connect 说明 Honomoana/Tabua 将连接 Fiji、French Polynesia、US、Australia，并建设 PF/Fiji 多样化登陆站与 interlink cable。

负面控制模板：
```text
"French Polynesia" ("cloud region" OR "availability zone" OR "edge location")
"Tahiti" "Google Cloud" (region OR zone OR location)
"Tahiti" (AWS OR Azure OR "Oracle Cloud") (region OR datacenter)
site:aws.amazon.com "French Polynesia" "Region"
site:azure.microsoft.com "French Polynesia" "Region"
site:cloud.google.com/about/locations "French Polynesia"
site:oracle.com/cloud/public-cloud-regions "French Polynesia"
"Tahiti" colocation (Equinix OR NTT OR "Digital Realty" OR Interxion)
```

---

## 4. 法语查询模板（French Query Templates）

核心法语词汇：
- 数据中心：`centre de données`、`datacenter`、`data center`、`centre informatique`、`salle serveurs`、`salle informatique`
- 托管/云：`hébergement`、`hébergement de données`、`colocation`、`baie`、`cloud`、`serveur dédié`、`infogérance`、`externalisation`
- 状态：`livré`、`ouvert`、`inauguré`、`mis en service`、`opérationnel`、`extension prévue`、`en construction`
- 海缆/网络：`câble sous-marin`、`station d'atterrissement`、`point d'atterrissement`、`fibre optique`、`liaison hertzienne`、`station terrienne`
- 电力/设施：`poste source`、`ligne haute tension`、`groupe électrogène`、`climatisation`、`détection incendie`、`extinction incendie`、`photovoltaïque`
- 许可/采购：`permis de construire`、`certificat d'urbanisme`、`étude d'impact`、`enquête publique`、`appel d'offres`、`marché public`、`avis d'attribution`

法语发现模板：
```text
"Polynésie française" ("centre de données" OR datacenter OR "salle serveurs" OR hébergement)
"Tahiti" ("centre de données" OR datacenter OR colocation OR "salle informatique")
"Papeete" "Pic Rouge" ("centre de données" OR datacenter)
"Papenoo" ("Tahiti Nui Fortress" OR datacenter OR "centre de données")
"centre de données" "Polynésie française" (projet OR construction OR "mis en service" OR opérationnel)
"hébergement de données" "Polynésie française"
"salle serveurs" (OPT OR "Tahiti Nui Telecom" OR TDF OR gouvernement OR SIPF)
"câble sous-marin" "Polynésie française" (Honotua OR NATITUA OR Manatua OR Honomoana OR Tabua OR atterrissement)
```

英文回填模板：
```text
"French Polynesia" ("data center" OR "data centre" OR datacenter OR colocation)
"Tahiti" ("data center" OR "data centre") (Papeete OR Papenoo OR "Pic Rouge" OR hosting)
"French Polynesia" (subsea cable OR "landing station") (Honotua OR Natitua OR Manatua OR Honomoana OR Tabua)
```

---

## 5. 塔希提语 / 地名变体（Tahitian & Place-Name Variants）

塔希提语主要用于地名规范和本地社区媒体；官方文件以法语为主。地名变体用于发现，设施事实仍需法语/官方/业主源确认。

| 法语/常用名 | 塔希提语/变体 | 用途 |
|---|---|---|
| Tahiti | Tahiti Nui / Tahiti Iti | 主岛；TNF/TDF 所在市场 |
| Papeete | Pape'ete | 首府；TDF Pic Rouge |
| Papenoo | Papeno'o / Papenoo | TNF / Tahiti Nui Telecom / Honotua 相关 |
| Faaa | Fa'a'ā / Faa'a | 机场都市区；电信/企业线索 |
| Pirae | Pīra'e | 都市区 |
| Punaauia | Puna'auia | 都市区 |
| Moorea | Mo'orea | Honotua 国内段/近岛 |
| Bora Bora | Porapora / Bora-Bora | Honotua/Manatua 线索 |
| Raiatea | Ra'iātea | 背风群岛 |
| Huahine | Huahine | Honotua 国内段 |
| Rangiroa / Manihi / Hao / Makemo | 同名为主 | NATITUA |
| Nuku Hiva / Hiva Oa | Hiva 'Oa | NATITUA / Marquesas |

模板：
```text
"Pape'ete" OR Papeete (datacenter OR "centre de données" OR "Pic Rouge")
Papenoo OR "Papeno'o" ("Tahiti Nui Fortress" OR "Tahiti Nui Telecom" OR datacenter)
"Fa'a'ā" OR Faaa (datacenter OR "centre de données" OR télécommunications)
"Mo'orea" OR Moorea (datacenter OR "centre de données" OR Honotua)
"Ra'iātea" OR Raiatea ("câble sous-marin" OR Honotua OR datacenter)
```

---

## 6. 枚举矩阵（Enumeration Matrix）

| 资产类 | 地理重点 | 主要查询模式 | 期望结果 | 等级 |
|---|---|---|---|---|
| TNF operator colo/cloud | Papenoo / Hitiaa O Te Ra / Tahiti | tnfortress.pf、tahitinuitelecom.pf、groupe.opt.pf | 官方 datacenter/cloud/contact/legal pages | A |
| TDF Pic Rouge data center | Papeete / Pic Rouge / Tahiti | tdf.fr + TNTV/DCD | 官方 opening、客户、扩容；媒体容量补充 | A/B |
| 政府/机构托管 | Papeete / Tahiti | service-public.pf/dsi、Te Ariari、Lexpol | SIPF/DSI 招标、外包、政策 | A |
| 企业/银行机房 | Tahiti 都市区 | Banque de Polynésie、Socredo、UPF、医疗机构 + salle serveurs | 企业自用机房；一般非商用 DC | C 起 |
| 海缆登陆站 | Papenoo、Bora Bora、Moorea、Tuamotu、Marquesas | Honotua/NATITUA/Manatua/Honomoana/Tabua | 系统、登陆点、RFS/建设状态 | A/B |
| 云区域/超大规模 | 全境 | 官方云区域负面控制 | 无 PF region/AZ | A（负面控制） |
| 电力设施 | Tahiti + 外岛 | EDT、poste source、MW、groupe électrogène | 电力上下文 | A |
| 卫星/teleport | Papenoo | OneWeb、Galileo、station terrienne | 邻近通信资产 | A/B |

岛屿组矩阵：

| 岛屿组 | 预期结论 | 必跑查询 |
|---|---|---|
| Îles du Vent（Tahiti、Mo'orea） | 确认市场核心；TNF/TDF | "Tahiti" OR "Papeete" OR Papenoo（datacenter / "centre de données" / hébergement） |
| Îles Sous-le-Vent（Raiatea、Huahine、Bora Bora） | 海缆/电信为主；无独立 DC | "Raiatea" OR "Bora Bora"（"câble sous-marin" / Honotua / Manatua / datacenter） |
| Tuamotu-Gambier | NATITUA 通信节点；无 DC | "Rangiroa" OR Hao OR Makemo（datacenter / "centre de données" / NATITUA） |
| Marquesas | NATITUA 通信节点；无 DC | "Nuku Hiva" OR "Hiva Oa"（datacenter / "centre de données" / NATITUA） |
| Australes | 无 DC，保留通信/电力上下文 | "Tubuai" OR "Australes"（datacenter / "centre de données"） |

---

## 7. 分级规则（Grading Rules）

### 7.1 来源分级

| 等级 | PF 示例 |
|---|---|
| **A** | TNF/Tahiti Nui Telecom/TDF 官方页；Groupe OPT 官方新闻；Service Public PF；Lexpol/JOPF；ANFR PF 监管说明；APC 正式意见；Te Ariari/PLACE 采购；EDT；官方云区域页；Google Cloud 官方海缆博客；RCS/mentions légales |
| **B** | TNTV、Tahiti Infos、Polynésie La 1ère、La Dépêche、RNZ Pacific、DCD、AFD 项目页、TeleGeography 报告文本、厂商新闻稿 |
| **C** | Baxtel、DataCenterMap、DataCenters.com、Submarine Cable Map、SEO hosting/VPS/VPN、LinkedIn/Facebook、无来源聚合 |

### 7.2 按事实分级

- **主体存在**：官方页/法律声明 = A；媒体 = B；目录 = C。
- **设施存在**：业主官方 datacenter page/opening release = A；媒体探访/报道 = B；目录 = C。
- **地址/边界**：官方 contact/legal/许可/环评 = A；媒体地标 = B；目录坐标 = C。
- **容量（MW/机柜/baies）**：官方规格/合同/环评 = A；TNTV/DCD 等采访 = B；Baxtel/DCM 锁库或估算 = C。
- **状态**：官方 opened/delivered/RFS = A；媒体 inaugurated = B；planned/MoU = C。
- **认证/Tier**：证书或审计报告 = A；TDF 官方 “Tier III level” 合规审计可作 A 级官方声明；TNF “Tier3+” 若无证书只写 claimed。

### 7.3 PF 特有陷阱

- **旧结论过时**：2025 TDF Pic Rouge 之后，PF 不再能写成“无商用数据中心市场”。
- **ARCEP PF 假阳性**：不要使用 `arcep.pf`；法国 ARCEP 也不直接监管 PF 电信市场。
- **NATITUA 误分类**：NATITUA 是 Tuamotu/Marquesas 外岛连接项目，不是 Tahiti-Hawaii。
- **Papenoo 多资产混合**：TNF data center、Honotua landing、satellite teleport、Galileo/OneWeb 都可能同场域，必须拆资产。
- **目录容量膨胀**：Baxtel/DCM 可发现 TDF/TNF，但 MW/机柜数需降级或回证。
- **Google cable ≠ cloud region**：Honomoana/Tabua 是海缆与 landing stations；无 GCP PF region。
- **官方语言与拼写**：法语搜索优先；英文和塔希提语只补发现。

---

## 8. 推荐流程（Recommended Pipeline）

1. **官方设施种子**：TNF datacenter/cloud/contact/legal pages；TDF Pic Rouge official release。
2. **官方/法定回证**：Service Public PF、Lexpol/JOPF、ANFR PF、APC、Te Ariari、PLACE。
3. **媒体补充**：TNTV/Tahiti Infos/DCD/La 1ère 捕获采访、客户、扩容、投资额。
4. **容量严控**：官方规格优先；媒体容量为 B；目录容量为 C。
5. **海缆拆分**：Honotua/NATITUA/Manatua/Honomoana/Tabua 落 `cable_landing_station` 或 connectivity context。
6. **云负面控制**：AWS/Azure/GCP/OCI 官方区域页确认无 PF region/AZ。
7. **地理去重**：Manifest division 固定为 `French Polynesia`；site/commune 字段用 Papeete/Pic Rouge/Papenoo 等细化。
8. **监控频率**：月度 TDF/TNF/Service Public/TNTV；季度 Lexpol/Te Ariari/APC；海缆按 Google/OPT/RFS 公告更新。

快速启动查询集：
```text
"French Polynesia" ("data center" OR "data centre" OR datacenter OR colocation)
"Polynésie française" ("centre de données" OR datacenter OR "salle serveurs")
"Tahiti Nui Fortress" (datacenter OR cloud OR colocation OR "baie")
"TDF" "Papeete" "Pic Rouge" datacenter
site:tnfortress.pf (datacenter OR "centre de données" OR colocation OR cloud)
site:tdf.fr Papeete ("data center" OR datacenter OR "Pic Rouge")
site:tntvnews.pf ("data center" OR datacenter OR "Pic Rouge" OR "Tahiti Nui Fortress")
site:tahiti-infos.com ("data center" OR "Tahiti Nui Fortress")
site:service-public.pf/dsi (hébergement OR cloud OR "centre de données")
site:service-public.pf/marchespublics (datacenter OR "centre de données" OR hébergement)
site:autorite-concurrence.pf ("Tahiti Nui Telecom" OR "data center" OR Honotua OR Honomoana)
"French Polynesia" ("cloud region" OR "availability zone")
"Honotua" OR "NATITUA" OR "Manatua" OR "Honomoana" OR "Tabua" atterrissement
```
