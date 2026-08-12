---
name: tr-datacenter-methodology
location: scripts/expansion/world/country-skills/TR/SKILL.md
description: |
  Turkiye (TR) datacenter discovery & audit methodology — how to enumerate, verify, and update Turkish datacenter projects across 81 provinces. Turkiye has no single public national datacenter permit register: enumeration is a province + municipality + organized-industrial-zone (OSB) exercise over national e-government indexes — e-Plan / Ministry GIS zoning, municipal planning portals, e-CED environmental decisions, EKAP public tenders, TEIAS/TEDAS/EPDK and regional DSO power evidence, BTK Yer Saglayici hosting-provider registry, Turkish Trade Registry Gazette, official cloud pages (AWS Istanbul Local Zone 2026-05, Google Cloud Turkiye region announced with Turkcell, no Azure/OCI region), and operator pages (Turkcell/Superonline, Turk Telekom, Vodafone, Equinix IL2/IL4, IsNet/Is Bankasi Atlas, ENKA, NGN, Radore, Teknotel/Telehouse, Mars, PenDC, TurkSat, Khazna, Edgnex/DAMAC, Trendyol/Castle). Read this before running TR exploration/audit batches. Routes to explorer-official.md (planning/energy/BTK/cloud) and explorer-industry.md (trade press/vendors/province query patterns).
---

# TR · 土耳其数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：土耳其**没有**统一的国家数据中心许可注册库；枚举是 **省 + 市 + 工业区（OSB）** 逐层推进，用国家 e-government 索引叠加：**e-Plan/部 GIS 规划**、**市政规划门户**、**e-CED 环境决定**、**EKAP 公共采购**、**TEIAS/TEDAS/EPDK 与区域配电公司电力证据**、**BTK Yer Saglayici 托管商注册**、**土耳其贸易注册公报**、**官方云页**与**运营商官方页**。
> 最高产出省：**Istanbul、Ankara、Izmir、Kocaeli（Gebze）、Tekirdag（Corlu/Kapakli）**；大部分超大规模/中立运营商证据集中于此五地。云区域页只证**云区域存在**（AWS Istanbul Local Zone、Google Cloud Turkiye 已宣布未上线；Azure/OCI 无土耳其公共区域）。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供土耳其探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：e-Devlet/e-Plan/部 GIS、市政与 OSB 规划门户、e-CED 环境、EKAP 招标、TEIAS/TEDAS/EPDK 与区域 DSO、BTK Yer Saglayici 与运营商授权、官方云区域（AWS Local Zone/Google announced/Azure·OCI 无）、运营商官方页种子、81 省工作流 |
| `explorer-industry.md` | 行业/厂商发现：DCD/AA/BThaber/Turk-internet/Cloud7/TechInside 媒体、运营商/项目地理矩阵（Istanbul 核心、Ankara、Izmir、Kocaeli、Tekirdag 及区域城市）、土语查询模式与状态词、省别名/区级线索表 |

## 核心结构事实（框定每次搜索）

1. **无全国许可库**：数据中心通常以 `veri merkezi`、`data center`、`bulut bolgesi`、`sistem odasi`、`barindirma`、`sunucu merkezi`、`telekom / bilisim tesisi`、`teknoloji ve operasyon merkezi` 或 **OSB 技术基础设施** 面貌出现，没有独立的数据中心执照类别。
2. **规划证据在市政/OSB**：每个大都市（`buyuksehir belediyesi`）、区（`ilce belediyesi`）与 OSB 发布规划变更、建筑许可公告、招标、议会决定或项目页——常比国家搜索更有效；提取 ada-parsel、kapali alan（封闭面积）、beyaz alan（白空间）、变压器/发电机描述、阶段排期。
3. **电力是门控信号**：TEIAS 输电容量/变电站文件（`Kapasite Duyurusu`、GIS TM、trafo merkezi）、TEDAS 配电资产验收、区域 DSO（BEDAS/AYEDAS、SEDAS、TREDAS、Baskent EDAS、GDZ、Toroslar、Meram、AKDENIZ、Yesilirmak 等）、EPDK 决定；`MVA`/`kurulu guc` 是受电容量 ≠ IT 负载。
4. **BTK Yer Saglayici 是运营商/托管商普查，不是设施普查**：可作法人/地址种子（Turkcell、Superonline、Turk Telekom、Vodafone、Equinix、IsNet、Radore、Mars、Pen、NGN、Veganet、FiberDC、Netdirekt、VeriTeknik、KocSistem），但需运营商页/许可/TSE·Uptime 认证才升为设施存在（A）。
5. **云区域**：AWS **Istanbul Local Zone 2026-05-20 GA**（+ 2025 AWS Direct Connect @ Equinix IL4）；Google Cloud 宣布 Turkiye 区域（与 Turkcell 多年投资，**coming not live**）；Azure/OCI 官方列表无土耳其公共区域（负控制搜索）。云区域≠自有数据中心——物理设施可能由 Equinix/伙伴运营。
6. **容量陷阱**：运营商发布集团级总量（如 Turkcell 4 个新一代/共 8 个 DC）不得分摊到单站；`MW`（超大规模/贸易媒体常指 IT load）vs `MVA`/`kurulu guc`（受电）vs `beyaz alan`（白空间 m²）分开记录；区分 `ilk faz/1. faz` 与 `tam kapasite/nihai kapasite`。
7. **土语字符影响召回**：同时搜 ASCII（`Turkiye`、`Istanbul`、`Izmir`、`Kocaeli`、`Tekirdag`）与土语（`Turkiye`、`Istanbul`、`Izmir`、`Tekirdag`、`Sanliurfa`、`Canakkale`、`Eskisehir`）；设施常按区（`Umraniye`、`Tuzla`、`Esenyurt`、`Gebze`、`Temelli`、`Golbasi`、`Menderes`、`Corlu`、`Kapakli`）而非省命名。

## 查询模式（复制粘贴模板见 explorer-official.md §1-§4 与 explorer-industry.md §2）

- 土语核心词：`veri merkezi` `veri merkezleri` `sunucu barindirma` `sunucu merkezi` `sistem odasi` `bulut bolgesi` `hiper olcekli bulut` `barindirma merkezi` `beyaz alan` `kabinet/kabin` `trafo merkezi` `kesintisiz guc kaynagi` `jenerator` `imar ruhsati` `yapi ruhsati` `iskan / yapi kullanma izin belgesi` `CED gerekli degildir` `CED olumlu`。
- 发现：`"{il}" +"veri merkezi" +(acildi OR temel OR yatirim OR insaat OR kapasite OR "beyaz alan")`、`"{il}" +"data center" +(opened OR launch OR construction OR MW OR capacity)`、`"{il}" +"veri merkezi" +(MW OR MVA OR kabinet OR rack OR Tier OR "Uptime" OR "TSE 50600" OR "LEED Gold")`。
- 规划/市政：`site:{municipality-domain} "veri merkezi" "imar" OR "yapi ruhsati" OR "meclis karari"`、`site:{osb-domain} "veri merkezi"`、`"{project}" "yapi ruhsati" OR "yapi kullanma izin" OR "iskan"`。
- 环境：`site:eced-duyuru.csb.gov.tr "veri merkezi"`、`"{operator}" "CED gerekli degildir" "veri merkezi"`、`"{il}" "veri merkezi" "CED olumlu"`。
- 电力：`site:teias.gov.tr "veri merkezi"`、`site:teias.gov.tr "{district}" "trafo merkezi"`、`site:{dso-domain} "veri merkezi" "baglanti"`、`"{project}" (MW OR MVA OR "elektrik kapasitesi" OR "baglanti gorusu")`、`"{district}" ("154 kV" OR "34.5 kV") "veri merkezi"`。
- 监管/法人：`site:internet.btk.gov.tr/yer-saglayici-listesi "{operator}"`、`site:btk.gov.tr "{legal name}" "ISS" OR "AIH"`、`site:ticaretsicil.gov.tr "{legal name}" "veri merkezi"`、`site:kurumsal.btk.gov.tr/yetkilendirmeler`。
- 云：`"AWS Local Zone" "Istanbul" "Turkiye"`、`"Google Cloud" "Turkiye region" "Turkcell"`、`"Azure" "Turkiye" "region" site:learn.microsoft.com`、`"bulut bolgesi" "veri merkezi" "Ankara"`。
- 媒体：`site:aa.com.tr "{il}" "veri merkezi"`、`site:datacenterdynamics.com "{il}" "data center" Turkey`、`site:turk-internet.com OR site:bthaber.com OR site:cloud7.news OR site:techinside.com "{il}" "veri merkezi"`。
- 状态词：`acildi/hizmete acildi/faaliyete gecti/devreye alindi`=运营（需运营商/官方/强媒体）；`temeli atildi/insaat basladi/yapimi suruyor`=在建；`anlasma imzaladi/yatirim planliyor/kuracak`=announced/planned。

## 官方/监管管线要点（详见 explorer-official.md）

- e-Devlet（https://www.turkiye.gov.tr/ ）服务发现；e-Plan/Ministry GIS（https://cbs.csb.gov.tr/ ）查看已知项目周边规划背景与 `imar plani/nazim imar plani/uygulama imar plani` 修改；市政与 OSB 门户（最高产出）；土耳其贸易注册公报（https://www.ticaretsicil.gov.tr/ ）验证 SPV/地址/增资/经营范围含 `veri merkezi/bulut/barindirma/telekomunikasyon`。
- e-CED（https://eced.csb.gov.tr/ + https://eced-duyuru.csb.gov.tr/eced-prod/duyurular.xhtml ）：数据中心非固定 CED 类别、召回低，但大建筑/发电机群/变电站/燃料/冷却/光伏风电并网可能触发（A=公告具名项目）。
- EKAP（https://ekap.kik.gov.tr/ ）公共采购：`veri merkezi`、`sistem odasi`、`sunucu odasi`、`felaket kurtarma merkezi`、UPS/发电机/HVAC/网络机房建设招标；Invest in Turkiye（https://www.invest.gov.tr/en/news/ ）官方投资新闻 A-/B+。
- 电力：TEIAS（https://www.teias.gov.tr/ ）输电容量/变电站/GIS 环境社会计划/合同；TEDAS（https://www.tedas.gov.tr/ ）配电资产验收；EPDK（https://www.epdk.gov.tr/ ）董事会决定与并网语境；区域 DSO 名单按省选用。
- BTK（https://www.btk.gov.tr/ + https://internet.btk.gov.tr/yer-saglayici-listesi + https://kurumsal.btk.gov.tr/yetkilendirmeler ）：Yer Saglayici 列表=法人/地址种子（A 实体、C 设施）；`ISS`（ISP）/`AIH`（基础设施运营）授权确认合法运营商。
- 云区域（A=区域存在）：AWS Istanbul Local Zone（2026-05-20 GA）+ Direct Connect @ Equinix IL4；Google Cloud Turkiye（announced，Turkcell 伙伴）；Azure/OCI 无土耳其公共区域（负控制）。
- 运营商官方页（存在性 A，容量另证）：Turkcell/Superonline（Kocaeli/Gebze、Ankara/Temelli、Izmir/Menderes、Tekirdag/Corlu、Istanbul 遗留；4 新一代/共 8 个 DC）、Turk Telekom（Istanbul Esenyurt/Gayrettepe、Ankara Umitkoy；三设施 12,700 m² 白空间；Ronesans Ankara 项目早期）、Vodafone（Istanbul 欧亚侧、Ankara、Izmir、Adana；2024 Izmir Edgnex/DAMAC JV USD 100M、初 6 MW 可扩 12 MW）、Equinix Istanbul IL2/IL4（Umraniye/Dudullu OSB）、IsBank/IsNet Atlas（Tuzla，Tier IV 级）、ENKA Tuzla（官方进度页 11 MW IT load）、NGN Star of Bosphorus（16 MW、Uptime Tier III）、Radore、Teknotel/Telehouse Istanbul（Tier 3+）、Mars、PenDC、Netdirekt（Izmir）、KocSistem、TurkSat Golbasi（33 MVA 政府战略设施）、Trendyol/Castle/Khazna Ankara Data Hub（USD 500M、48 MW、首期 Q3 2026）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 媒体：DCD Turkey tag（B，Equinix IL4/Khazna Ankara/Edgnex-Vodafone/Google-Turkcell）、Anadolu Agency（B+，部长/运营商引语、就职日期、省计数；引官方典礼可 A-/B+）、Daily Sabah/TRT（B）、Invest in Turkiye（A-）、BThaber/Turk-internet/Cloud7/TechInside（B，本地 ICT/托管媒体）、BT Gunlugu/Webrazzi（B-/C+）、DC Network Turkiye/Data Center Eurasia 活动参与名单（C/B 线索）。
- 地理矩阵：**Istanbul**（Equinix IL2/IL4、Turk Telekom Esenyurt/Gayrettepe、Vodafone、IsBank Atlas/Tuzla、ENKA Tuzla、Radore、Mars、PenDC、NGN、Teknotel/Telehouse、KocSistem Camlica、机场/公共设施；区级：Umraniye/Tuzla/Esenyurt/Besiktas/Basaksehir/Pendik/Sancaktepe/Kadikoy/Atasehir）；**Ankara**（Turkcell Temelli/Anadolu OSB、Turk Telekom Umitkoy、TURKSAT Golbasi、Khazna、Trendyol/Castle Data Hub、Vodafone、VeriTeknik、OSTIM、Baskent OSB）；**Izmir**（Turkcell Menderes、Vodafone-Edgnex、Netdirekt、PlusLayer、Izmir Ataturk OSB）；**Kocaeli**（Turkcell Gebze、GOSB、SEDAS）；**Tekirdag**（Turkcell Avrupa Veri Merkezi/Corlu、Kapakli/Karaagac OSB、TREDAS）。
- 区域城市：Adana（Vodafone）、Antalya/Kayseri/Konya/Samsun/Trabzon/Isparta（AA 2026 全国盘点提及运营设施但常无运营商名）、Rize（FiberDC）、Gaziantep（Veganet）、Eskisehir/Edirne/Bursa（机构/市政线索）；大学/市政/OSB 变体：`{il} universitesi veri merkezi`、`belediye veri merkezi`、`valiligi veri merkezi`、`teknopark veri merkezi`、`OSB veri merkezi`。
- 目录源（C 种子）：Baxtel、DataCenterMap、DataCenters.com、Data Center Catalog、PeeringDB（网络存在 B，容量/状态 C）、DCHub、本地地图——需运营商页/BTK/认证佐证才升级。

## 来源分级

- **A** = 官方/一手：市政建筑许可/规划决定、e-CED 决定、TEIAS/DSO 并网证据、TEDAS 验收、官方开业/移交、TSE/Uptime/LEED 具名设施记录、运营商具名设施页（省/区+服务状态）、BTK 实体/通知/地址、Invest.gov.tr/部委/AA·TRT 官方引语（A-/B+）、上市公司/监管文件。
- **B** = 强二级：DCD、AA、BThaber、Turk-internet、Cloud7、TechInside、TRT/Daily Sabah 官方引语转述、承包商项目进度页（如 ENKA）、认证页。
- **C** = 弱线索：Baxtel/DataCenterMap/DataCenters.com/Data Center Catalog/DCHub、仅 PeeringDB 条目、博客、LinkedIn/社媒、Google Maps、经销商页、市场报告。
- 状态语义：`announced`（仅 MoU/投资公告）→ `planned`（场地/区/项目名已知，无建设证据）→ `construction`（基础/承包商进度/建筑许可/CED 批准/电网接入/官方建设更新）→ `operational`（开业公告/运营商设施页/活跃服务页/认证/带佐证的 PeeringDB 设施/客户或政府移交）。
- 去重：Equinix IL2/IL4 vs 前 Zenium/Istanbul One；Turkcell Ankara vs Temelli/Anadolu OSB；Turkcell Europe DC vs Tekirdag/Corlu/Kapakli/Karaagac OSB；BTK 托管≠数据中心（办公室/转售/虚拟主机）；公共/大学 `veri merkezi` 常是小机房——单独标注 institutional。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=TR，divisions=81 省）。
2. **种子设施宇宙**：官方运营商页（Turkcell、Turk Telekom、Vodafone、Equinix、IsNet/Atlas、ENKA、TurkSat、NGN、Radore、Teknotel）+ AWS/Google 官方云页。
3. **Tier 1 省深度扫描**：Istanbul、Ankara、Izmir、Kocaeli、Tekirdag——规划 + e-CED + TEIAS/DSO + BTK 全查询族。
4. **BTK Yer Saglayici 找区域小运营商**：按省抓取，法人名转到官方设施/贸易注册/PeeringDB/认证/市政证据。
5. **其余省**：市政/大学/OSB 招标 `sistem odasi`/`sunucu odasi`/`felaket kurtarma merkezi`/`veri merkezi`；无线索前跑通用土语模板+大学/市政/OSB 变体。
6. **状态与容量**：TEIAS/DSO/EPDK/运营商容量声明后才记 MW；`capacity_mw` 仅用于明确 IT load，其余按字段存（MVA/kurulu guc/beyaz alan）；输出 world 同 schema，无项目 division 写 `no_projects: true`。
7. 遵守 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12 02:15Z）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：50× codex terra agent（max thinking）每 agent 分批复核土耳其数据中心（81 省）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：Google Cloud Turkiye 区域落地（Ankara/Kocaeli/Tekirdag 候选与许可）、Khazna Ankara 建设状态、Trendyol/Castle Ankara Data Hub 首期（Q3 2026 48 MW）、Azure 是否新增土耳其区域（每次运行复查官方列表）、Equinix IL4 扩建/许可、Turkcell Google 合作园区物理站点、TURKSAT Golbasi 33 MVA 当前状态。
