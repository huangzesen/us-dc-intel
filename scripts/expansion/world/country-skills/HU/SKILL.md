---
name: hu-datacenter-methodology
location: scripts/expansion/world/country-skills/HU/SKILL.md
description: |
  Hungary (HU) datacenter discovery & audit methodology — how to enumerate, verify, and update Hungary datacenter projects at county / city-with-county-rights / capital-city granularity (from world-manifest.jsonl). Hungary has no public national datacenter registry: enumeration joins E-epites/OENY/ETDR building-authority workflows, local and county government notices (kormanyhivatalok.hu, city portals), NMHH telecom-construction permits (e.g. BMW Hungary DC1 Debrecen optical connection), environmental records (OKIR/OKIRkapu), MAVIR/DSO/MEKH power evidence, EKR/Kozbeszerzes/TED public procurement (NISZ/FEAK/IdomSoft government datacenters), official cloud-region checks (no public HU hyperscale region; Oracle eu-budapest-1/IdomSoft is a sovereign-region lead), and operator pages (Magyar Telekom/T-Systems/Dataplex/Adatpark, 2Connect/Invitech, RackForest/Rackhost, VIVAnet, Servergarden/Systech, Datacenter.hu/DP Data Center, Wigner/CERN, KIFU/HPC). Hungarian terms matter (adatkozpont, szerverkozpont, szerverterem, gepterem, epitesi engedely, hasznalatbaveteli engedely); many “Budapest” listings physically sit in Pest county. Paks/Tolna AI campus claims stay planned until permit/grid/land evidence. Read this before running HU exploration/audit batches. Routes to explorer-official.md (permits/local-gov/environment/NMHH/energy/procurement/cloud/seeds/divisions) and explorer-industry.md (operators/trade press/directories/cloud checks/county patterns/grading).
---

# HU · 匈牙利数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：匈牙利**没有**公开的全国数据中心注册库；枚举靠**拼接** E-epites/OENY/ETDR 建筑主管工作流、地方政府与州政府公告、NMHH 电信建设许可、环境记录、MAVIR/DSO 电力证据、公共采购（EKR/Kozbeszerzes/TED）与运营商页。
> 高产区 = **布达佩斯 + Pest 州都市圈**（Budapest XIII/VIII/XI/XIV/X、Budaors、Torokbalint 等）；次级节点：Gyor、Szeged、Debrecen、Pecs、Nyiregyhaza、Szolnok、Szombathely、Eger、Zalaegerszeg；计划中的能源/HPC 线索围绕 **Paks/Tolna**。
> 官方门户深访问常需 KAÜ/DAP 登录：公开枚举用**公开通知页、被索引的官方 PDF、机构公告、EKR 附件与运营商确认的设施页**，并标注“仅为流程路由”的情况。
> 云销售办公室≠数据中心区域：AWS 有布达佩斯办公室但无 HU 区域/Local Zone；Azure/GCP 官方列表无 HU 区域；Oracle `eu-budapest-1`/IdomSoft 为主权/专属区域线索，须 Oracle 一手文档+本地政府记录确认。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供匈牙利探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：E-epites/ETDR/Lechner e-construction 建筑许可（epitesi engedely/hasznalatbaveteli engedely/egyszeru bejelentes）、地方政府与州政府（kormanyhivatalok.hu/城市门户/HESZ/议会纪要）、OKIR/OKIRkapu 环境、NMHH 电信建设许可与注册表（BMW DC1 光学连接范例）、MAVIR/MEKH/DSO（E.ON/MVM/OPUS）电力、EKR/Kozbeszerzes/TED 采购（NISZ/FEAK/IdomSoft/Wigner）、云区域官方核查（Azure/AWS/GCP/Oracle）、官方运营商/公共基础设施种子表、分区四遍枚举与优先级表、证据与去重规则 |
| `explorer-industry.md` | 行业/厂商发现：DCD/Magyar Epitok/dehir/Portfolio/hwsw/bitport/ITBusiness/teol/vg 媒体、运营商种子（Telekom/Dataplex/Adatpark 官方地址表、2Connect/Invitech 6,500 sqm 12 站点、RackForest/Rackhost、VIVAnet 2024-07 运营、Servergarden/Systech、Datacenter.hu-DP Data Center、KBC Torokbalint、Wigner/CERN、NISZ-FEAK-IdomSoft、BMW Debrecen DC1）、目录（DataCenterMap 18 设施/Baxtel/Inflect/PeeringDB-BIX）、云与超大规模核查、州/城市查询模式与分区种子词、核验工作流与分级、高风险假阳性 |

## 核心结构事实（框定每次搜索）

1. **建筑许可主干（A）**：E-epites（e-epites.hu）、ETDR（建筑主管案件工作流：许可/拆除/保留/使用许可/简单通知/遗产程序）、Lechner E-construction（ETDR 为国家电子文档系统）、E-naplo、E-kozmu（地块级基础设施上下文）；深访问需认证——用公开索引通知/官方 PDF/市州 PDF。
2. **许可文件很少写 “data center”**：搜 `adatkozpont` `szerverkozpont` `szerverterem` `gephaz` `iroda es technologiai epulet` `telekommunikacios letesitmeny` `informatikai kozpont` `szamitastechnikai kozpont` `gepterem` + 支撑词 `aggregator` `UPS` `hutestechnika` `transzformatorallomas` `optikai csatlakozas`；提取 helyrajzi szam/地籍地块、地址、区、市镇、许可类型、日期、专业机构参与、技术线索（IT 房/备用发电机/变压器房/冷却厂/燃料库/UPS 电池房/光纤）。
3. **生命周期词**：`telepulesrendezesi terv/HESZ/SZT` < `telepuleskepi velemeny` < `kornyezeti vizsgalat/elozetes vizsgalat` < `kornyezetvedelmi engedely/levegotisztasag-vedelmi engedely` < `epitesi engedely` < `epitesi naplo megnyitasa` < `hasznalatbaveteli engedely/tudomasulvetele` < `uzembe helyezes/atadas`；强证据=epitesi engedely、hasznalatbaveteli engedely、官方启用/当前设施页、官方采购/合同点名物理数据中心、NMHH 许可点名 DC 连接、官方 HPC/云区域启用；规划/电网讨论/意向书=计划/开发前。
4. **NMHH 电信建设许可（A）**：BMW Hungary Kft. DC1 在 Debrecen 的光学连接许可通知（CD60532/2023 号决定）证明园区内 DC 相关基础设施；用 NMHH 查光纤路由、运营商法人 pivot、电信建设许可；服务提供商注册表=法人/运营商身份 A、设施存在 C（须匹配设施页/许可/采购/互联/建设记录）。
5. **电力（MAVIR/MEKH/DSO）**：MAVIR=TSO；DSO：E.ON Hungaria、MVM Halozat/EMASZ/DEMASZ、OPUS TITASZ、ELMU（E.ON/MVM 旧页）；提取 MW/MVA、电压、变电站、冗余馈线、接入点、备用发电机/燃料、储能/光伏/BESS；需求侧电力证据通常比可再生更难公开检索——作佐证与选址，不作独立设施证明（除非文档点名项目）。
6. **采购（EKR/Kozbeszerzes/TED，A）**：术语 `kormanyzati adatkozpont` `FEAK` `NISZ` `IdomSoft` `DKU` `szerver hosting` `adatkozpont uzemeltetes/bovites` `sotetszal` `BIX`；实例：`Adatkozpont uzemeltetes tamogatas 2024`（EKR szerzodes 951653）、附件点名 `NISZ Kormanyzati Adatkozpont`、`Wigner Datacenter`、`FEAK Fuggetlen Energetikai Adatkozpont Zrt.`；采购多为设备/服务而非新建——用它找公共部门 DC、扩容、托管站点、暗光纤与精确地址。
7. **云区域（负面核查 + 主权线索）**：Azure/AWS/GCP 官方列表无 HU 区域（AWS 2023 布达佩斯办公室=市场存在）；Oracle `eu-budapest-1` 出现在工具/支持区域列表、Visual Builder Studio 引用 `IdomSoft Budapest Hungary (JSK)`——作 Oracle/IdomSoft 主权/专属区域线索，须当前 Oracle 文档+采购+本地记录确认，不得当普通公共 OCI 区域。
8. **去重/归派**：市场化的 “Budapest” 设施可能物理在 **Pest 州**（Budaors/Torokbalint 等）——按实际市镇/地址归一；企业/园区/服务器房（BMW Debrecen DC1、KBC Torokbalint、SK Innovation Komarom）与商业 colo/超大规模分开计数；研究/HPC（Wigner/CERN、KIFU/Komondor、大学超算、ZalaZONE EMAK）单独计数；国家/采购容量不得赋给单站点（除非源为设施特定）。

## 查询模式（复制粘贴模板见 explorer-official.md §1/§4 / explorer-industry.md §1/§4）

- 许可/市政：`site:e-epites.hu "adatkozpont" "{city}"`、`site:etdr.gov.hu "adatkozpont"`、`site:kormanyhivatalok.hu "{county}" "adatkozpont"`、`site:{city-domain} "HESZ" "adatkozpont"`、`site:{city-domain} "szabalyozasi terv" "adatkozpont"`、`filetype:pdf "adatkozpont" "epitesi engedely" "{city}"`、`"{operator}" "{city}" "epitesi engedely"`。
- 环境/电力/电信：`site:webgis.okir.hu "adatkozpont"`、`site:kormanyhivatalok.hu "szerverterem" "levegotisztasag"`、`site:mavir.hu "{city}" "transzformatorallomas"`、`site:mekh.hu "adatkozpont" OR "{operator}"`、`site:eon.hu "adatkozpont" "{city}"`、`site:mvmhalozat.hu "adatkozpont"`、`site:nmhh.hu "optikai csatlakozas" "adatkozpont"`、`site:nmhh.hu "{city}" "DC1" "adatkozpont"`。
- 采购：`site:kozbeszerzes.hu "{division}" "adatkozpont"`、`site:ekr.gov.hu "{division}" "adatkozpont"`、`"Kormanyzati Adatkozpont"`、`"FEAK" "adatkozpont"`、`"IdomSoft" "adatkozpont"`、`site:ted.europa.eu Hungary "data centre"`。
- 英文/云：`"Hungary" "data center" "building permit"`、`"Budapest" "data center" "MAVIR"`、`"AWS Hungary" "Local Zone" site:aws.amazon.com`、`"Oracle Cloud" "Budapest" "eu-budapest-1"`、`"IdomSoft" "Budapest" "Oracle Cloud"`。
- 行业：`site:datacenterdynamics.com Hungary "data center" Budapest`、`site:datacenterdynamics.com Hungary "data centre" Paks`、`site:magyarepitok.hu adatkozpont Debrecen`、`site:dehir.hu Debrecen adatkozpont`、`site:portfolio.hu adatkozpont Magyarorszag`、`site:hwsw.hu adatkozpont`、`site:teol.hu Paks adatkozpont MI`。
- 布达佩斯/Pest：`"Budapest" "adatkozpont" Magyar Telekom Dataplex RackForest VIVAnet Invitech Servergarden`、`"Budaors" "adatkozpont" Telekom Invitech 2Connect`、`"Torokbalint" "data centre" KBC`、`site:2connect.hu "adatkozpont"`、`site:rackforest.com "Budapest" "georedundancia"`。
- 状态词（匈）：`bejelentette/szandeknyilatkozat/tervezett/vizsgaljak`=计划/意向；`epul/kivitelezes/alapkőletetel/beruhazas/engedely`=管线/在建；`atadtak/megnyilt/uzemel/szolgaltatas elerheto/hasznalatbavetel`=运营线索。

## 官方/监管管线要点（详见 explorer-official.md）

- 建筑许可：E-epites/ETDR/OENY（A 流程与系统）；ETDR 流程路由≠公开项目列表——用 ETDR 公开数据/索引官方通知/市州 PDF；不抓取认证案件材料。
- 地方政府：市/州政府办公室（kormanyhivatalok.hu，A）、城市门户（budapest.hu、bp13.hu、jozsefvaros.hu、ujbuda.hu、kobanya.hu、debrecen.hu、gyor.hu、szegedvaros.hu、pecs.hu…）、HESZ/规划/议会纪要/土地出售/公用事业地役权；规划证据单独=项目存在 B/C，升级需许可/采购/电网/运营商确认。
- 环境：OKIR 地图与数据浏览器（A 官方环境对象/排放/废物/水数据集）、OKIRkapu（流程源）、州政府环境通知；DC 以空气排放许可（备用柴油发电机）、冷却噪声、燃料库、电池/UPS、消防、用水、elozetes vizsgalat 出现；A=公开机构文档点名设施/运营商，B=仅佐证已知运营商站点附近电力/冷却设施。
- NMHH：注册表（A 运营商/服务注册，非设施证明）+ 电信建设许可（BMW DC1 范例）+ 指南；用于光纤路由、法人 pivot、园区 DC 连接。
- 电网：MAVIR/MEKH/DSO；提取需求/合同 MW/MVA、电压、变电站、冗余、接入点、备用发电机、储能/光伏；区分负荷连接/能源项目/市场上下文。
- 采购：EKR/Kozbeszerzes/TED；找出公共部门设施与扩容、暗光纤、精确地址；合同状态取决于内容。
- 云：Azure/AWS/GCP 无 HU 区域（负面对照）；Oracle eu-budapest-1/IdomSoft 作主权线索。
- 运营商种子（A=官方存在/当前足迹）：Magyar Telekom/T-Systems/Dataplex/Adatpark（Budapest Asztalos Sandor u. 13、Budaors Ipartelep u. 13-15、Victor Hugo 18-22、Adatpark Gyor Teleki Laszlo u. 36、Adatpark Szeged Rokusi krt. 2-10）、2Connect/Invitech（6,500+ sqm、12 站点、3 商业+9 电信）、NMHH BMW DC1、Wigner/CERN、KIFU/HPC（Debrecen/Szeged/Budapest）、NISZ/FEAK/IdomSoft（采购渠道）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 媒体：DCD（B，Dataplex/Wigner-CERN/EuroHPC/4iG/Paks 历史与线索）、Magyar Epitok/dehir/Portfolio/hwsw/bitport/ITBusiness/ictglobal/computerworld/profitline/teol/vg（B/C 本地）；状态词按上表解读。
- 运营商种子：Telekom（A，官方地址表）、2Connect/Invitech/4iG-One（A/B）、RackForest/Rackhost/Rendszerinformatika（A/B，5 机房 3 布达佩斯地点 georedundancy；Victor Hugo 站点）、VIVAnet（A，2024-07 运营、一期 140 racks 载波中立）、Servergarden/Systech Ilka utcai（A/B，DC10/DC14 虚拟概念）、Datacenter.hu/DP Data Center/Dryvit Profi（Debrecen A/B，EPS-Connect 施工报道 B）、KBC Torokbalint（B，Cummins 案例，企业/银行设施）、Wigner/CERN（A，研究）、NISZ/FEAK/IdomSoft（A 采购源）、BMW Debrecen DC1（A NMHH 许可，企业/园区）、区域：Dravanet Pecs、Giganet Nyiregyhaza、KMAK/Kelet-Magyarorszagi Adatkozpont Szolnok、DC Hosting Eger、ISIS-COM Szombathely、SK Innovation Komarom（企业电力线索）、ZalaZONE EMAK（R&D）、Paks/Tolna（计划 B/C）。
- 目录（C/C+ 线索）：DataCenterMap（当前 18 设施：Budapest/Szeged/Nyiregyhaza/Pecs/Szombathely）、Baxtel（C+，Dataplex 8 MW 等容量片段须核）、Inflect/DatacenterPlatform/Datacenters.com/Cloudscene（别名：Invitech DC10、NTT/Budaors legacy、Servergarden、SZTAKI、PanTel）、PeeringDB/BIX（B/C 互联）、HIPA/IVSZ（B/C 市场上下文）、Data Center Event Budapest（C）。
- 假阳性：`adatkozpont` 可指数据库/数据枢纽；`szerverterem` 可指办公室/学校/医院/工厂小机房；政府采购常为现有 DC 买硬件而非新建；承包商引用缺业主/地址/日期/范围（保持 C）；Paks AI 园区报道可能引用 LOI/委任措辞（计划级，须许可/电网/土地证据）；云销售办公室/meetup/伙伴活动/CDN PoP 只是上下文。

## 来源分级

- **A** = 官方/一手：国家或地方机构记录、NMHH 电信建设通知、官方环境记录、MAVIR/DSO/MEKH 记录、EKR/采购局通知、官方云基础设施页、官方运营商页、CERN/EuroHPC/大学一手页（研究/HPC 范围）。
- **B** = 强二级：成熟贸易媒体、运营商关联承包商案例、HIPA/协会材料、Uptime/认证记录。
- **C** = 弱线索：目录、市场页、无设施细节的通用托管页、旧新闻、市场报告片段、未验证容量声称。
- 电力字段分开存：`requested_connection_mw`、`contracted_mva`、`it_load_mw`、`generator_mw`、`facility_power_mw`、`source_power_term`；机架数/总面积/技术面积/设施功率/IT load/MVA 不混用。
- Paks/Tolna AI 园区须 ≥2 类证据（官方开发商公告/地方或州许可/电网能源批准/土地市政记录/可信施工开始），意向书仍为计划 B/C。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=HU，divisions=州/州级市/首都）。
2. 建种子：运营商官方页（Telekom/2Connect/RackForest/VIVAnet/Servergarden/Datacenter.hu）+ 地址 pivot（Asztalos Sandor 13、Ipartelep 13-15、Victor Hugo 18-22、Teleki Laszlo 36、Rokusi krt. 2-10、Ilka utca、Galamb）+ NMHH/EKR 首扫。
3. 每 division 四遍：① 已知运营商遍（Telekom/2Connect/RackForest/VIVAnet/Servergarden/Datacenter.hu/本地 ISP/大学 HPC/公共部门）；② 官方许可遍（ETDR/E-epites 公开数据、城市/区门户、州政府办公室通知、HESZ/议会纪要）；③ 监管/基础设施遍（NMHH、MAVIR/DSO/MEKH、OKIR/环境、灾管、EKR/Kozbeszerzes/TED）；④ 交叉核验遍（运营商页、认证、采购地址、PeeringDB/BIX、目录弱线索）。
4. 优先级 division：Budapest（XIII/VIII/XI/X/XIV/IX 区）、Pest（Budaors/Torokbalint/Dunakeszi-Fot/Vecses/Szigetszentmiklos/Biatorbagy）、Debrecen（DP DC/BMW DC1/大学 Komondor）、Gyor（Adatpark/Audi）、Szeged（Adatpark/Rackhost/大学）、Pecs、Nyiregyhaza、Szolnok、Eger、Szombathely、Zalaegerszeg（ZalaZONE）、Tolna/Paks（计划）；其余 division 跑通用模板+本地工业/大学词，无信号写 `no_projects: true`。
5. 状态：atadtak/uzemel/hasznalatbavetel/官方页=运营；epul/engedely=在建/已许可；tervezett/意向=计划；按设施类型分类（commercial_colocation/telecom_datacenter/hosting_provider_facility/public_sector_datacenter/research_hpc/enterprise_campus_server_room/planned_ai_energy_campus）。
6. 输出 world 同 schema；容量按字段区分；遵循 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：codex terra agent（max thinking）每 agent 分批复核匈牙利数据中心（州/城市粒度）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：Oracle/IdomSoft `eu-budapest-1` 的官方区域确认与采购证据；Paks/Tolna AI 园区的许可/电网/土地进展（LOI 不得升级）；VIVAnet 2024-07 后扩建与容量；DP Data Center Debrecen 当前运营状态；2Connect 12 站点清单的 NMHH/地址佐证；Telekom Dataplex 历史容量（Baxtel 8 MW）与当前运营；BMW Debrecen DC1 是否作为独立设施计数。
