---
name: rs-datacenter-methodology
location: scripts/expansion/world/country-skills/RS/SKILL.md
description: |
  Parent-level data-center enumeration methodology for Serbia (RS). Serbia has an
  unusually useful telecom-regulator lead source (RATEL List of Data Centers), but
  no complete datacenter permit registry; enumeration cross-joins CEOP/APR
  construction documents, city/municipal environmental procena-uticaja records,
  EMS/EDS/AERS grid evidence, RATEL operator records, public procurement, official
  cloud-region pages (Oracle Serbia Central/Jovanovac present; AWS/Azure/GCP
  absent), and operator/trade/directory sources across 20 manifest divisions.
  Serbian searched in Latin and Cyrillic. Read this before running RS
  exploration/audit batches. Routes to explorer-official.md (official/regulatory/
  cloud pipeline) and explorer-industry.md (industry/operator/district patterns).
---

# RS · 塞尔维亚数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：Serbia has no complete datacenter permit registry，但有一个异常有用的监管线索源：**RATEL 发布 "List of Data Centers"**（电子通信活动通知页下）——商业 colo/电信设施的第一遍清单；正式枚举仍须拼接 CEOP/APR 施工文件、市政/环评记录、EMS/EDS/AERS 电网、RATEL 运营商记录、政府采购、官方云区域页与运营商/贸易/目录来源。
> 多轨三角测量：RATEL/CEOP/环评/电网/采购轨道产出 A 级证据，运营商页与云官方区域产出 A/B 级设施信号，贸易媒体与目录（C）仅作回填；塞尔维亚语拉丁与西里尔双拼。
> 本 skill 汇总两份探索报告（explorer-official.md / explorer-industry.md）为国家层方法论；批次执行前必读。

## 入口

| 文件 | 内容 | 说明 |
|---|---|---|
| explorer-official.md | 官方/监管/云管线：CEOP/APR 施工许可（`ceop.apr.gov.rs`）、市政环评（`procena uticaja`）、EMS/EDS/AERS 电网、公共采购（`jnportal.ujn.gov.rs`）、RATEL 数据中心清单与运营商注册、云区域核验（Oracle Serbia Central 现录）、分部枚举路线与交叉核验工作流 | A 级主干与查询模板 |
| explorer-industry.md | 行业/运营商/分部模式：Belgrade 商业集群、Kragujevac/Sumadija 政府云枢纽、Vojvodina 与南部线索、Kosovo-Metohija 管辖处理、云/超大规模枚举规则、塞尔维亚语别名表、提取与分级规则 | A/B/C 全谱系 |

## 核心结构事实（框定每次搜索）

1. **RATEL 数据中心清单**：`ratel.rs` 通知页邀请拥有数据中心的法人提交数据并发布清单（2024-11-25 文档含 Yettel、Beotelnet、Sat-Trakt、Orion Telekom、A1 Srbija、Telekom Srbija、SBB、Conexio、HiTeam 等条目）——A 级第一遍来源，但非完整许可登记。
2. **施工许可链（CEOP/APR）**：`informacija o lokaciji`/`lokacijski uslovi` < `građevinska dozvola`/`rešenje o odobrenju izvođenja radova` < `prijava radova` < `upotrebna dozvola`（西里尔：`локацијски услови`、`грађевинска дозвола`、`решење о одобрењу извођења радова`、`пријава радова`、`употребна дозвола`）；公共门户 `ceop.apr.gov.rs`，Belgrade 城市页确认统一程序仅经 CEOP 电子申报；A 级流程与文件来源。
3. **环评分散化**：国家环保部（`ekologija.gov.rs`）+ 各市/直辖市 `procena uticaja` 页面；数据中心常经备用发电机、油箱、冷水机组、屋顶基站与 EIA 筛选公告浮现；Kragujevac 城市公告直接点名 A1 Serbia 位于 "Data centar" 与 Telekom Srbija 基站 `KG - Data centar`——官方页/PDF 点名场地即 A 级。
4. **政府数据中心**：Office for IT and eGovernment（`ite.gov.rs`）运营 Kragujevac 政府数据中心园区（约 14,000 m²、4 ha 地块、class 4/Tier 4 级标准、州与商业用户、Oracle/IBM/Huawei/CERN 引用）与 Belgrade 首个国家数据中心——A 级。
5. **云区域（关键正负控制）**：**Oracle 官方现录 Serbia Central (Jovanovac)、区域标识 `eu-jovanovac-1`、region key BEG、realm OC20、1 个可用域**——A 级逻辑云区域存在；AWS/Azure/GCP 官方区域页无塞尔维亚区域；Kragujevac 的 Azure Stack Hub / Government Cloud 是主权/政府平台而非 Azure 公有区域；`Jovanovac/Kragujevac/Sumadija` 按集群处理，物理地址以地块/许可单独验证。
6. **语言（拉丁 + 西里尔）**：核心词 `data centar`/`дата центар`、`centar podataka`、`državni data centar`、`računarski centar`、`serverska sala`、`kolokacija`（注意电信塔站共享语境）、`telehousing`、`katastarska parcela`/`k.p.`、`trafostanica`、`priključenje na elektroenergetsku mrežu`、`procena uticaja na životnu sredinu`；门户常省略变音符，用 ASCII 回退。
7. **Kosovo-Metohija**：manifest 含此分部，但公开来源通常将 Pristina/Fushe Kosove 设施按 Kosovo 处理；输出保留 manifest 分部，notes 中明确管辖/来源措辞。
8. **陷阱**：`data centar` 可能指小型服务器机房、网络节点或应用/数据门户；电信基站环评公告证明场地存在但不证明新数据中心建设；云计费/客户可用性 ≠ 物理区域；可再生能源或工业负载并网 ≠ 数据中心证据；不得合并 Kragujevac 国有园区、OCI 逻辑区域、Data Cloud Technology 法人/商业实体与未来 e& 扩建，除非来源证明同一物理地块；目录容量按来源单独分级。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§2 / explorer-industry.md §1-§4）

- CEOP/许可：`site:ceop.apr.gov.rs "data centar" "{city}"`、`site:ceop.apr.gov.rs "građevinska dozvola" "data centar"`、`"data centar" "{city}" "lokacijski uslovi"`、`"data centar" "{city}" "upotrebna dozvola"`、`filetype:pdf "дата центар" "грађевинска дозвола" "{city}"`。
- 市政/环评：`site:beograd.rs "data centar" "procena uticaja"`、`site:kragujevac.ls.gov.rs "data centar"`、`site:novisad.rs "data centar" OR "дата центар"`、`"A1 Srbija" "Data centar" "procena uticaja"`、`"Telekom Srbija" "Data centar" "procena uticaja"`、`site:ekologija.gov.rs "data centar"`。
- 电网：`site:ems.rs "data centar" OR "priključenje objekta"`、`site:eds.rs "data centar"`、`site:aers.rs "procedura za priključenje objekta"`、`"data centar" "trafostanica" "{city}"`、`"eu-jovanovac-1" "Jovanovac" "trafostanica"`。
- 监管/采购：`site:ratel.rs "List of Data Centers"`、`site:registar.ratel.rs "{operator}" "elektronske komunikacije"`、`site:jnportal.ujn.gov.rs "data centar"`、`site:ite.gov.rs "data centar" "javna nabavka"`、`site:undp.org/serbia "Government Data Center" "Kragujevac"`、`"Government Data Center" "Kragujevac" "Modules"`。
- 云：`"Oracle Cloud" "Jovanovac" "Serbia"`、`"OCI Serbia Central" "eu-jovanovac-1"`、`"AWS Serbia" "Region" "Local Zone"`、`"Azure Stack Hub" "Kragujevac" "State Data Centre"`。
- 英语：`"Serbia" "data center" "building permit"`、`"Kragujevac" "data center" "expansion" "MW"`、`"Serbia" "data center" "RATEL"`。
- 分部通用：`"{division}" "data center" Serbia`、`"{locality}" "data centar"`、`"{locality_cyrillic}" "дата центар"`、`"{locality}" "kolokacija"`、`"{locality}" "trafostanica" "data centar"`、`site:ratel.rs "{locality}" "data centar"`、`site:ekapija.com "{locality}" "data centar"`。
- 生命周期词：`"otvoren data centar"`（开业）、`"pušten u rad"`（投运）、`"izgradnja data centra"`/`"gradi se data centar"`（建设中）、`"planira data centar"`（计划）、`"memorandum"`（MoU，不按建成计）、`"dozvola"`、`"urbanistički projekat"`、`"trafostanica"`。

## 官方/监管管线要点（详见 explorer-official.md）

- **RATEL**：数据中心清单（A 级提交条目）+ 电子通信运营商注册（A 级运营商状态，非设施证明）+ 宽带地理与基础设施共享页（A 级语境）；以清单条目下钻运营商页、CEOP、环评。
- **CEOP/APR 与城市页**：提取发证机关、程序类型、案卷号、日期、投资者（`investitor`/`nosilac projekta`）、工程名称与用途、地址/地籍市镇（KO）/地籍地块（k.p.）、建筑类别、`trafostanica`/`agregat`/`UPS`/冷却/油箱/光纤路由/安防围栏/通路引用、许可状态；真实记录可能仅写 `IKT infrastruktura`、`računarski centar`、`serverska sala`、`tehnički objekat`、`telekomunikacioni objekat`、`centar za obradu podataka`——不必苛求 "data centar" 字样。
- **环评记录**：可揭示项目业主与确切场地/地块、柴油发电机数量/功率与储油、屋顶无线基站/电信塔、冷却/HVAC 与噪声控制、EIA 研究是否豁免、公众评议期与决定日期。
- **EMS / AERS / EDS / EPS**：EMS 输电连接页引用能源法、规划建设法与供电法令；AERS 公开 EMS 输电系统发展计划（2025-2034）与投资计划（2025-2029）批准材料；电力来源用于支撑容量与位置，不单独创建数据中心记录（除非文档点名数据中心）；捕获 `requested_connection_MW`、`installed_power_MW`、电压等级、变电站、DSO/TSO、连接研究/合同状态，并区分设施状态与电力基础设施状态。
- **公共采购**：`jnportal.ujn.gov.rs`（A 级公告/中标/计划/合同变更）、Office for IT 采购页（历史条目如 `IKT infrastruktura za državni Data centar`）、UNDP Serbia（Kragujevac 政府数据中心 Phase III 模块扩建咨询/采购，A/B 视承包路径）、TED（英文检索便利，A/B）；采购词含 `projektovanje`/`izvođenje radova`/`rekonstrukcija serverske sale`/`rezervni data centar`/`superkompjuter`。
- **政府/云枢纽（Sumadija）**：`ite.gov.rs` 政府数据中心页（A）；e& enterprise 2025-09 MoU 称现有 Tier-4 园区 14 MW、1,080 机架、已锁定土地可扩至 40 MW（A 级运营商/伙伴公告，计划级直至许可/合同证明施工）；Office 页另述 Block 2/新模块约 56 MW 计划；Oracle 区域枢纽位于 Kragujevac 政府数据中心（`ite.gov.rs/vest/en/771` 官方确认）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **Belgrade 集群（Tier 1）**：CETIN（Omladinskih brigada 90/92，A，PeeringDB fac 6734/SOX）、Telekom Srbija/MTS（Katiceva 14-18 等，A/B）、SBB Telepark/Yettel（Nehruova，B/C）、Orion Telekom（Zemun Polje Mala pruga 8，Tier-3、8 kW+ 机架、主权 AI Factory/GPU，A/B）、phoenixNAP（Omladinskih brigada 92，B）、NetCast（Omladinskih brigada 21，A）、BeotelNet（Bulevar Vojvode Misica 37，B/C）、BeeNet RS-1（A）、Absolut Solutions（C）；地址词高收益。
- **Kragujevac / Sumadija（Tier 1）**：国有/政府数据中心园区（A）、Data Cloud Technology / DCT（A/B，PeeringDB 11606）、Oracle Cloud Jovanovac（A）、Government Cloud / Azure Stack Hub（A，主权平台）、CERN/IBM/Huawei 托管负载（A/B，不得各自计为新设施）、Eviden/国家超算（B，园区内 HPC）、e& 40 MW 扩建（A 公告/planned）、City Data Center Kragujevac（A/B，仅当来源证明物理独立时分开）。
- **Vojvodina**：ZELEN DATA CENTAR / HiTeam / E-Smart（Vrsac Technology Park，Beogradski put 2g，首个绿色数据中心，A/B）、BeeNet RS-2 Vrsac（A/B）、NEOplanta / NEO Data Center Novi Sad（E-CAPS，A/B）、Sat-Trakt（Becej，C/B 待运营商页）；市/大学服务器机房按独立类别。
- **Nisava / 南部**：NiNet 数据中心 Nis（Bulevar Nemanjića 25，A/B 项目 + C+ 目录容量）、Interreg IPA Bulgaria-Serbia DATACENTERSBGSR（BGRS0500152，A 级招标/扩展证据）、Tehnis 计划 20 MW 数据中心（B/C 待城市规划/土地/电网/采购）、Jotel 等本地 ISP（C）。
- **Kosovo-Metohija**：IPKO（Fushe Kosove 工业区主设施 + Ulpiana/Pristina 备份，A 级官方，管辖标注 Kosovo）、Telecom of Kosovo（C）、Kujtesa/Artmotion（C）。
- **媒体/协会（B/C）**：DCD、SeeNews、Telecompaper、ITA Serbia Digital Economy、eKapija、Balkan Green Energy News、Energetski Portal、BIRN、Uptime Institute（B 级 Tier/Class 证据）、DCAS（成员清单/活动报告 B 级线索）、RNIDS/RSNOG（B/C）；目录 DataCenterMap、Baxtel、Datacenters.com、DataCenterPlatform、datacenters.rs、connectbase/newby 等默认 C。
- **互连数据库（B/C）**：PeeringDB/SOX（IX 424、CETIN fac 6734、Data Cloud Technology DC Kragujevac、Državni Data Centar DDC、NiNet DC Nis、Orion、SBB、Telekom Srbija 等）——验证互连存在，不验证 MW/建造日期/所有权。

## 来源分级

- **A** = 官方/一手：CEOP/APR 施工文件、城市/直辖市许可或环评决定、RATEL 数据中心清单条目与运营商注册、EMS/EDS/AERS 电网文件、官方采购公告/中标、官方云供应商区域页（Oracle Jovanovac）、官方运营商设施页、Office for IT and eGovernment 页、EU/Interreg 招标、e& 官方扩建公告。
- **B** = 强二手：DCD、SeeNews、Telecompaper、ITA、Uptime Institute、UNDP 采购、承包商案例、官方协会材料（不自身证明设施地址/状态）、维护良好的 PeeringDB/SOX 设施记录。
- **C** = 弱线索：目录、市场列表、泛托管页、旧论坛/新闻、未验证容量主张、无来源市场报告。
- **状态规则**：**Planned** = MoU/可行性研究/土地与城市规划行动/采购规划/UNDP 咨询设计招标/无施工许可的公告扩建；**Approved** = CEOP 施工许可、环评决定、已签公共采购/施工合同或命名范围的官方政府批准；**Construction** = 开工通知、施工合同中标、官方奠基或运营商/政府称施工进行中；**Operational** = RATEL 清单、官方运营商服务页、官方启用、使用许可、官方云区域可用性或官方政府页描述在运服务。
- **容量规则**：仅明确时记录 MW、kW/机架、机架、sqm、机柜或场地面积；保留来源单位不随意换算；目录容量与设施存在性分开分级；发电机/变电站值不可推断 IT 负载。
- **类型标签**：`commercial_colocation`、`telecom_datacenter`、`government_datacenter`、`sovereign_cloud_region`、`HPC/supercomputer`、`enterprise_private`、`edge/IX/PoP`、`server_room`。
- **去重/红旗**：`Omladinskih brigada 90/92` 可能同时显示 Yettel/CETIN/phoenixNAP 或互连枢纽；`Milutina Milankovica` 建筑可能有多个运营商套间；Telekom 多址；基站在既有数据中心场地的环评公告不证明新建设；云计费/可用性 ≠ 物理区域；可再生能源/工业并网 ≠ 数据中心证据。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL 中 `country_code == "RS"` 的条目，按 division 分组（20 分部：Belgrade、Sumadija、Vojvodina、Nisava、Kosovo-Metohija 为 Tier 1，其余为 Tier 2）。
2. 每分部固定顺序：(1) RATEL 清单/运营商枢轴；(2) CEOP/APR 精确短语与运营商/地址检索；(3) 市/直辖市环评 `procena uticaja` 页；(4) 公共采购门户与本地采购页；(5) EMS/EDS/AERS 电网与变电站检索；(6) 最后才用贸易媒体/目录补线索与容量。
3. 锚点清单做种子：Belgrade（CETIN、Telekom/MTS、SBB/Yettel、Orion、phoenixNAP、NetCast、BeotelNet、BeeNet RS-1）；Sumadija（政府数据中心/Data Cloud Technology、OCI Serbia Central、e& 扩建、城市数据中心、Telekom Atinska 1）；Vojvodina（ZELENDATA、BeeNet RS-2、Sat-Trakt、NEOplanta）；Nisava（NiNet、Interreg、Tehnis）；Kosovo-Metohija（IPKO）。
4. 逐条候选规范化：设施名（保留塞尔维亚语变音符）、运营商/法人、manifest 分部与来源地点/地址、状态、类型、容量（仅明确时）、来源链（监管/运营商/云 → 政府 → 贸易 → 目录）。
5. 交叉核验：RATEL/运营商/云/采购线索 → CEOP 精确地址/法人/城市检索（记录案卷类型与文件号）→ 市政环评（EIA 决定日期、发电机/冷却线索、地块 ID）→ EMS/EDS/AERS（仅设施相关电力事实）→ 采购（项目标题变体）→ 目录/贸易补缺；去重同址条目。
6. 按 world schema 输出：`{country_code: "RS", country_name: "Serbia", division, city, name, operator, status, capacity_mw, source_urls, evidence_date, evidence_grade, notes}`（参考 explorer-official.md §5 最小字段清单，含 permit_refs/environment_refs/energy_refs/cloud_refs）；负结果 `no_projects: true` 仅在对 RATEL、CEOP、市政环评、采购、电网、贸易/目录全部为负后标记（见 explorer-industry.md §4.3 负向控制清单）。
7. **NO-DELETION**：不改写 explorer-official.md / explorer-industry.md；复核批次只增补不删行。

## 待办（2026-08-12 02:41Z）

- 两份探索报告已合并为国家层方法论；下一步以本 skill 为国家层参考运行 RS 探索/复核批次（20 分部）。
- 需验证：Kragujevac/Jovanovac 园区、OCI Serbia Central 逻辑区域、Data Cloud Technology 法人、e& 40 MW/Block 2 56 MW 扩建的物理地块与许可阶段；Orion AI Factory 物理位置与 GPU 设施；NiNet Nis 现设施与 Interreg 扩展状态；Tehnis 计划 20 MW 是否出现城市规划/土地/电网证据；Vrsac ZELENDATA/BeeNet RS-2 容量；Kosovo-Metohija 条目（IPKO 等）的管辖标注；RATEL 清单条目（Yettel/A1/Telekom/SBB/Conexio 等）逐个以 CEOP/环评/运营商页升级。
