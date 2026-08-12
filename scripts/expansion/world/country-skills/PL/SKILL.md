---
name: pl-datacenter-methodology
location: scripts/expansion/world/country-skills/PL/SKILL.md
description: |
  Poland (PL) datacenter discovery & audit methodology. No national facility registry; build the census by joining GUNB RWDZ construction records (wyszukiwarka.gunb.gov.pl + API), gmina/powiat planning files (MPZP/WZ, BIP), environmental records (Ekoportal/GDOŚ/RDOŚ, KIP), PSE/grid connection records (Wykaz obiektów planowanych do przyłączenia, ESOP since 2026-07), DSO pages (PGE/Tauron/Enea/Energa/Stoen), UKE telecom context, official cloud regions (Azure Poland Central polandcentral, Google europe-central2 Warsaw, AWS Warsaw Local Zone only, OVHcloud Warsaw), and operator pages (Beyond.pl, Atman, Equinix, Netia, T-Mobile, Orange, DATA4, Vantage WAW1, EdgeConneX, 3S/Play, Polcom). Division model: 16 voivodeships with powiat/gmina drill-down. Read this before running PL exploration/audit batches. Routes to explorer-official.md (permits/grid/cloud) and explorer-industry.md (press/vendor/voivodeship matrix).
---
# PL · 波兰数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：为波兰数据中心枚举提供「GUNB/RWDZ 建筑许可 + gmina/powiat 规划文件 + 环评 + PSE/电网并网记录 + 云区域 + 运营商官网」六线并联的查询框架。波兰**没有全国性数据中心注册库**，普查 = GUNB **RWDZ（Rejestr Wniosków, Decyzji i Zgłoszeń）建筑记录** + gmina/powiat 规划文件 + 环境信息门户 + **PSE 并网记录** + 官方云区域页 + 运营商设施页的联合。**运营许可单位通常是 gmina 或 powiat/具有 powiat 权利的市**，而非省（wojewodztwo）；省门户与省长办公室仍用于环评、战略与上诉记录。波兰建筑记录可能不写「data center」，须按本地词与项目功能搜：`centrum danych`、`centrum przetwarzania danych`、`serwerownia`、`budynek usługowy`、`budynek technologiczny`、`budynek przemysłowy`、`stacja transformatorowa`、`agregaty prądotwórcze`、`magazyn energii`、`chłodzenie`。市场地理：**华沙/Mazowieckie 主导**云与互联；次要在波兹南、克拉科夫、弗罗茨瓦夫、卡托维兹、格但斯克、罗兹及大型电力/可再生能源电网站点。本 skill 汇总两份探索报告（官方管线 + 行业发现），供波兰探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：GUNB/RWDZ（搜索/地图/API）、MPZP/WZ/BIP、Ekoportal/GDOŚ/RDOŚ 环评、PSE 并网清单与 ESOP、DSO（PGE/Tauron/Enea/Energa/Stoen）、UKE、云区域页（Azure/Google/AWS Local Zone/OVHcloud）、运营商官网 |
| `explorer-industry.md` | 行业/厂商发现：TELKO.in/ITwiz/CRN/Computerworld/DCD 等媒体、PLDCA/Data Center Nation 生态、运营商/开发商按集群矩阵、逐省枚举矩阵（含重音/无重音变体）、KCPD 公共部门程序 |

## 核心结构事实（框定每次搜索）

1. **GUNB/RWDZ 是最重要官方建筑源**：公开搜索 https://wyszukiwarka.gunb.gov.pl/wyniki/（申请/决定/部分申报，公开 UI 可能需要 CAPTCHA）+ 地图 https://wyszukiwarka.gunb.gov.pl/mapa/（已知地址/地块后使用）+ API 文档 https://dev.wyszukiwarka.gunb.gov.pl/docs（可重复官方数据拉取，谨慎处理抓取）。捕获：文档类型（wniosek/decyzja/zgłoszenie）、机关（starosta/prezydent miasta/wojewoda/特别机关）、投资类别/描述、投资人法定名、地址/测绘区/地块号、提交日期/决定日期/决定状态、建筑类别（服务/工业/技术/电气建筑）。**不要要求含 `centrum danych` 字样**——许多项目按技术、服务、办公-技术、工业或电气建筑申报；用运营商公告的地址/地块反查。
2. **电网证据异常重要（PSE）**：PSE 季度 **Wykaz obiektów planowanych do przyłączenia do sieci przesyłowej**（https://www.pse.pl/obszary-dzialalnosci/krajowy-system-elektroenergetyczny/wykaz-obiektow-planowanych-do-przylaczenia）含发电/储能/配电系统/**odbiorcze 装置**、拒绝、待决申请与完整申请，附可编辑 XLS/XLSX——**A 级并网流程事实，但不是施工证明**；连接容量可用性页 https://www.pse.pl/obszary-dzialalnosci/krajowy-system-elektroenergetyczny/informacja-o-dostepnosci-mocy-przylaczeniowej；最高压网络规划 https://www.pse.pl/obszary-dzialalnosci/krajowy-system-elektroenergetyczny/plan-sieci-elektroenergetycznej-najwyzszych-napiec；**自 2026-07-01 起 PSE 经 ESOP（Elektroniczny System Obsługi Przyłączeń，https://esop.pse.pl）**处理输电并网条件申请。**注意**：当前并网申请嘈杂，可能含投机/重复大负荷请求；PSE 申请/条件 ≠ 建筑许可/开工/运营设施——分列 `requested_connection_MW`、`connection_point`、`application_status`、`permit_status`、`operational_status` 字段。DSO 按区域：PGE Dystrybucja https://pgedystrybucja.pl/、Tauron https://www.tauron-dystrybucja.pl/、Enea Operator https://www.operator.enea.pl/、Energa-Operator https://energa-operator.pl/、Stoen Operator（华沙）https://stoen.pl/。
3. **生命周期词（保守计数）**：`studium / MPZP / WZ` < `decyzja o środowiskowych uwarunkowaniach`（环评决定）< `wniosek o pozwolenie na budowę`（建筑许可申请）< `decyzja o pozwoleniu na budowę`（建筑许可决定）< `rozpoczęcie budowy`（开工）< `pozwolenie na użytkowanie`（使用许可）< `uruchomienie / oddanie do użytku`（投产）。只有 `pozwolenie na budowę`、`rozpoczęcie budowy`、`pozwolenie na użytkowanie` 或运营商确认投产计为强设施证据；MPZP/WZ 与 PSE 并网申请按 planned/pre-development 处理。
4. **规划与环评**：地方规划文件 **MPZP**（miejscowy plan zagospodarowania przestrzennego）、**WZ**（decyzja o warunkach zabudowy）、市议会决议与公众咨询多在 gmina/市 BIP 页而非国家门户；国家空间数据查看器 Geoportal https://www.geoportal.gov.pl/（A 级地籍/空间语境）；Ekoportal https://www.ekoportal.gov.pl/ + GDOŚ https://www.gov.pl/web/gdos（RDOŚ 区域环评机关）；地方 BIP 搜 `decyzja o środowiskowych uwarunkowaniach`、`obwieszczenie`、`karta informacyjna przedsięwzięcia`（KIP）、`raport ooś`。数据中心可能经备用发电（agregaty prądotwórcze）、燃料储存、电池/UPS、变电站、冷却技术、水需求、噪声、余热（ciepło odpadowe）/区域供热连接间接出现。
5. **云区域 = 逻辑区域存在，非精确地址**：Azure **Poland Central** `polandcentral`（华沙，官方称三个独立物理位置，2023-04-26 发布 https://news.microsoft.com/europe/2023/04/26/microsoft-launches-its-first-datacenter-region-in-poland...）；Google Cloud **Warsaw `europe-central2`**（zones a/b/c，https://cloud.google.com/blog/products/infrastructure/google-cloud-region-in-warsaw-poland-is-now-open；Google Cloud Interconnect 文档列 Atman WAW-1 为华沙互连设施）；**AWS 无波兰区域**（华沙仅 Local Zone 地理，作边缘/本地区域/网络种子，不作完整区域园区除非官方区域或本地许可证据）；OVHcloud 华沙数据中心/区域（A/B）；Oracle 无波兰公有云区域（须官方区域清单核实）。
6. **语言与变体**：波兰语优先——产品页常说 `data center`，但 BIP 与许可系统多用 `centrum danych`/`centrum przetwarzania danych`/`ośrodek przetwarzania danych`/`serwerownia`/`kolokacja`/`chmura obliczeniowa`/`obiekt teleinformatyczny`/`infrastruktura krytyczna`/`agregaty prądotwórcze`/`stacja transformatorowa`/`GPZ`/`przyłącze energetyczne`/`decyzja środowiskowa`/`KIP`/`pozwolenie na budowę`/`MPZP`/`WZ`/`uchwała`/`obwieszczenie`/`BIP`；用带重音与无重音变体（Łódź/Lodz、Wrocław/Wroclaw、Poznań/Poznan、Gdańsk/Gdansk、Śląskie/Slaskie、Małopolskie/Malopolskie），因为 OCR/BIP 搜索不一致。
7. **UKE 与容量类型**：UKE https://www.uke.gov.pl/ + BIP https://bip.uke.gov.pl/ 是电信/宽带监管语境（FERC/POPC 计划、光纤建设、运营商身份），**不是数据中心许可注册库**。容量分列：`IT load`、`gross power`、`requested grid connection`、`generator capacity`、`contracted energy`、`marketed campus capacity` 为独立字段；不把云区域/AZ 等同于精确设施。

## 查询模式（复制粘贴模板见 explorer-official.md §1 与 explorer-industry.md §2-5）

- `site:wyszukiwarka.gunb.gov.pl "centrum danych" "{miasto}"` / `"{miasto}" "centrum danych" "pozwolenie na budowe"` / `"{legal_entity}" "pozwolenie na uzytkowanie"`
- `site:{gmina-domain} "centrum danych" "MPZP"` / `site:{gmina-domain} "centrum danych" "warunki zabudowy"` / `site:{gmina-domain} "centrum danych" "decyzja srodowiskowa"`
- `site:pse.pl "centrum danych" "warunki przyłączenia"` / `site:pse.pl "Wykaz obiektów planowanych do przyłączenia" "centrum danych"` / `site:pse.pl "instalacji odbiorczych" "centrum danych"`
- `site:ekoportal.gov.pl "centrum danych"` / `site:gov.pl "centrum danych" "decyzja o środowiskowych uwarunkowaniach"` / `site:gov.pl "centrum danych" "Regionalny Dyrektor Ochrony Środowiska"`
- `site:uke.gov.pl "centrum danych"` / `site:uke.gov.pl "węzeł telekomunikacyjny" "{miasto}"`
- `"Poland" "data center" "building permit"` / `"Warsaw" "Azure" "Poland Central" "datacenter region"` / `"Warsaw" "Google Cloud" "europe-central2"` / `"AWS" "Local Zone" "Warsaw" "Poland"`
- `"Beyond.pl" Poznan "pozwolenie na budowe"` / `"Atman" Duchnice "pozwolenie na budowe"` / `"Equinix" WA4x Warsaw "building permit"` / `"T-Mobile" Szlachecka "centrum przetwarzania danych"`
- 阶段词映射：MPZP/WZ/studium=早期规划（planned）；decyzja o środowiskowych uwarunkowaniach=环评决定（permitted-阶段）；pozwolenie na budowę=建筑许可（A）；rozpoczęcie budowy=开工（A/B）；pozwolenie na użytkowanie/oddanie do użytku=运营（A）；PSE/DSO 并网申请=grid pipeline（非设施计数）。

## 官方/监管管线要点（详见 explorer-official.md）

- **GUNB/RWDZ（A 级）**：e-Budownictwo 前门 https://e-budownictwo.gunb.gov.pl/ + 搜索 + 地图 + API 文档（见核心结构事实 §1）。
- **地方规划（A 级）**：MPZP/WZ/议会决议/公众咨询在 gmina/市 BIP；Geoportal 作地籍语境；规划证据用于早期管线检测，除非计划明确为 `centrum danych` 预留土地或点名投资人/项目，否则分级低于许可证据。
- **环评（A 级）**：Ekoportal + GDOŚ/RDOŚ + 地方 BIP（KIP/raport ooś）；提取发电机/燃料/UPS、电力需求/变压器/变电站、冷却/水/噪声、场地面积与分期、余热/区域供热、环评决定日期与机关。
- **PSE/电网（A 级）**：并网清单 XLS/XLSX + 容量可用性 + ESOP（2026-07 起）+ 最高压网络规划；提取连接条件申请（等待验证）、完整申请、已签发/拒绝条件、对象类型（instalacja odbiorcza/储能/发电/配电系统）、连接点/变电站、申请 MW、申请人名、公社/省。
- **UKE（支持性语境）**：宽带计划、FERC/POPC 材料、电信运营商身份与网络/光纤语境。
- **云区域页**：Azure https://news.microsoft.com/europe/2023/04/26/... + https://learn.microsoft.com/en-us/azure/reliability/regions-list（polandcentral）；GCP https://cloud.google.com/blog/products/infrastructure/google-cloud-region-in-warsaw-poland-is-now-open + https://docs.cloud.google.com/compute/docs/regions-zones（europe-central2）+ Interconnect 设施 https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/choosing-colocation-facilities（Atman WAW-1）；AWS https://docs.aws.amazon.com/local-zones/latest/ug/available-local-zones.html（华沙 Local Zone）；OVHcloud https://www.ovhcloud.com/en/about-us/global-infrastructure/regions/。
- **运营商官方页（A 级存在性）**：Beyond.pl https://www.beyond.pl/en/data-centers-campus/location-poland/（波兹南园区，官方称多级 150 MW 园区，DC2 位于 A. Kreglewskiego 11，有空间/PUE/认证）；Atman https://atman.pl/en/atman-data-center/warsaw-1/ + warsaw-2 + https://datacenterpoland.com/（Warsaw-1 Grochowska 21a、Warsaw-2 华沙中心、WAW-3 Duchnice/Ozarow 园区官方活动站 14.4 MW/楼、目标 43.2 MW；KTW-1 Katowice）；Equinix https://www.equinix.com/data-centers/europe-colocation/poland-colocation/warsaw-data-centers（WA1 Aleje Jerozolimskie 65/79、WA2 Poleczki 23、WA3 Salomea、WA4x/xScale）；Netia https://www.netia.pl/en/instytucje-publiczne/produkty/data-center-cloud/data-center（MIND Jawczyce、SOUL Krakow、BRAIN Grodzisk Mazowiecki、HEART Warsaw）；T-Mobile Polska https://biznes.t-mobile.pl/en/products-and-services/data-center/server-colocation（官方称克拉科夫/华沙/弗罗茨瓦夫 5 个商业数据中心；Szlachecka 扩建 2021-12 完工；Piaseczno 为最大/关键设施）；Orange Polska（Warsaw Data Hub、Lazy）；DATA4 https://www.data4group.com/en/data-centers-warsaw-poland/（Jawczyce 园区）；Vantage WAW1 https://vantage-dc.com/data-center-locations/emea/warsaw-poland/（华沙附近，48 MW 规划/关键 IT 负载）；EdgeConneX https://www.edgeconnex.com/locations/emea/warsaw-pl/；3S/Play https://3s.pl/infrastruktura/nasze-obiekty/（Katowice ul. Gospodarcza 12、Bytom、Gdansk、Warsaw；DCD 报 Katowice 新设施与 Warsaw/Gdansk/Wroclaw 计划）；Polcom https://polcom.com.pl/en/about-us/data-center/（Skawina、Alwernia——Alwernia 属 Malopolskie，贸易页可能说「near Katowice」，勿错归 Slaskie）；Comarch（Krakow）。
- **B 级/公共部门**：KCPD（Krajowe Centrum Przetwarzania Danych，政府战略数据中心项目，非商业托管；位置可能敏感/模糊，只用公开源并保守标注置信度；NASK 存档页 + https://www.gov.pl/web/cyfryzacja/wieloletni-program-krajowe-centrum-przetwarzania-danych-kcpd-etap-i--wsparcie-procesu-przygotowania-projektu + eZamowienia/TED 招标）；PSNC/PCSS（波兹南，研究/HPC）；Cyfronet AGH（克拉科夫，学术/HPC）；TASK（格但斯克，研究/HPC）；Exea（Toruń 线索）；Aruba Cloud PL1、Lukman、Free/Play 3S Warsaw、银行/金融设施、NASK/COI。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **贸易媒体分级**：TELKO.in（B，波兰电信/DC 行业最佳：KCPD、Atman、DATA4、3S/Play、telco DC 与容量趋势）、ITwiz（B，KCPD/协会/公共部门/Microsoft/Google/Atman/Beyond.pl）、CRN Polska（B，渠道/业务：KCPD 资金/采购）、Computerworld Polska（B，云区域公告/Orange Warsaw Data Hub）、CyberDefence24/Bankier/WNP/Rzeczpospolita（B/C，KCPD 与投资政策）、DCD（B，超大规模园区公告/华沙市场总结/3S Katowice）、Data Centre Magazine/DatacenterDynamics/Baxtel 片段（C）。协会/生态：PLDCA https://pldca.pl/en/（成员种子，非设施注册库）、Data Center Nation Warsaw、DATA CENTER Expo Poland（C）。法律/地产分析（Dudkowiak/Miller Canfield/Haskoning/Cundall/JLL/CBRE）为 B 流程解释、B/C 集群语境。
- **运营商/开发商矩阵（按集群）**：Mazowieckie=Atman（Warsaw-1/2/3）、Equinix WA1/WA2/WA3/WA4x、DATA4 Jawczyce、Vantage WAW1、EdgeConneX、Netia Jawczyce/Grodzisk、T-Mobile Piaseczno/Szlachecka、Orange Warsaw Data Hub/Lazy、Microsoft/Google/OVHcloud 华沙信号、Aruba PL1/Lukman；Wielkopolskie=Beyond.pl 波兹南园区 + PSNC；Malopolskie=Polcom Skawina/Alwernia、Netia SOUL、T-Mobile Krakow、Comarch、Cyfronet；Slaskie=3S/Play Katowice/Bytom、Atman KTW-1、工业棕地/电信；Dolnoslaskie=Wroclaw 次要/边缘市场 + 3S 扩张雄心 + Wroclaw Centre for Networking and Supercomputing；Pomorskie=3S/Play Gdansk、TASK、OVHcloud 格但斯克仅办公室（非 DC）；Lodzkie=罗兹/Strykow 物流/电力地理；Kujawsko-Pomorskie=Exea Toruń；其余低密度省按 BIP/GUNB/环评/电网四轮扫。
- **目录来源（C+）**：Data Center Map https://www.datacentermap.com/poland/（旧托管地址种子）、Datacenters.com、Baxtel https://baxtel.com/data-center/poland（超大规模/园区邻接与 Microsoft/Data4/EdgeConneX 映射，须核实）、PeeringDB（B 活跃互联信号）。
- **去重与陷阱**：不把销售办公室/工程办公室/云伙伴办公室/网络 PoP 计为数据中心；波兰来源混用 `data center`/`centrum danych`/`centrum przetwarzania danych`，全变体+无重音都搜；GUNB/RWDZ 建筑许可可能用泛化建筑类别或投资人 SPV 而非最终运营商（按运营商公告的地址/地块与 `budynek usługowy`/`budynek techniczny`/`stacja transformatorowa`/`agregaty prądotwórcze` 反查）；运营商页与市场报告的容量存为 claimed/planned 除非许可/并网/开业公告/正式规格表背书；KCPD 位置与安全信息可能有意受限；PSE 投机/重复并网申请不合并计数除非同一法人/站点经核实。

## 来源分级

- **A** = 官方/一手：RWDZ 建筑许可/申请/申报记录、gmina/powiat BIP 规划文件（MPZP/WZ/决议/公告）、环境决定（decyzja o środowiskowych uwarunkowaniach/KIP/raport ooś）、PSE/DSO 并网文件（Wykaz/ESOP/连接条件/拒绝）、官方云区域文档（区域存在）、运营商官方设施页（声称的设施存在性）、政府程序页（KCPD 公开材料）。
- **B** = 强二级：DCD、TELKO.in、ITwiz、CRN、Computerworld、WysokieNapiecie（引用 PSE 并网队列）、法律简报（CMS/Dudkowiak/Miller Canfield）、商业地产报告、PLDCA/协会发布；点名项目/运营商/容量。
- **C** = 弱线索：Data Center Map、Datacenters.com、Baxtel、Datacentre Magazine 片段、活动页、市场摘要、社交帖、无来源容量声称。
- 状态语义：operational=运营商官方页/使用许可/投产公告；construction=建筑许可+开工/运营商声明/招标/现场记录；planned/permitted=RWDZ 建筑许可决定/环评决定/点名 MPZP-WZ/带项目描述的土地交易；grid pipeline only=PSE/DSO 申请/条件/拒绝且无规划/建筑许可（不合并投机重复申请）；云区域/AZ 不等同精确设施。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=PL，divisions=16 voivodeships，powiat/gmina 下钻），按 explorer-industry.md §5 每省三/四轮：行业/运营商轮（B/A）→ 本地 BIP/GUNB 轮（A）→ 环评/电网轮（A/B）。
2. 种子：国家官方拉取（RWDZ 搜 `centrum danych`/`centrum przetwarzania danych`/`serwerownia` + 已知运营商法定名；PSE XLS/XLSX 并网文件；Ekoportal/GDOŚ/RDOŚ；UKE）→ 云/托管种子（Azure/Google/AWS Local Zone/OVHcloud + Beyond.pl/Atman/Equinix/Netia/T-Mobile 页）→ 省扫描（省长办公室/RDOŚ/元帅办公室/区域发展页）→ powiat/gmina 扫描（BIP/决议/规划/土地出售/地方建筑机关；RWDZ 地图反查候选地块）→ 电网验证（PSE/DSO：warunki przyłączenia/GPZ/stacja transformatorowa/110-400 kV/moc przyłączeniowa/odmowa przyłączenia）。
3. 验证：A 级=许可/环评/电网/运营商官方；按省优先级（Mazowieckie 第一，尤其华沙市郊 gminy——Duchnice/Ozarow、Jawczyce、Piaseczno、Lazy/Raszyn/Lesznowola、Grodzisk、Pruszkow；再 Wielkopolskie/Malopolskie/Dolnoslaskie/Slaskie/Pomorskie）；字段含 wojewodztwo/powiat/gmina/miasto/operator/legal_entity/parcel/document_type/decision_status/requested_connection_MW/connection_point/IT load/gross power/permit status/operational status。
4. 输出：按 world schema 写结果，附证据日期与分级；容量类型分列；用无重音+重音变体。
5. 无项目判定：低密度省（Lubuskie/Opolskie/Podlaskie/Swietokrzyskie/Warminsko-Mazurskie 等）用 BIP/GUNB/环评/电网四轮显式负面搜索，区分公共服务机房与商业托管；三面无信号才设 no_projects: true。
6. 遵守 NO-DELETION；本 skill 与两份 explorer 均为只读输入，只新增 SKILL.md 与 ANATOMY.md。

## 待办（2026-08-12 02:33Z）

- [x] explorer-official.md 与 explorer-industry.md 已完成并合并为本 SKILL.md。
- [ ] 下一步：每批 50× codex terra agents，注入本 skill 后按 16 省逐省枚举（优先 Mazowieckie、Wielkopolskie、Malopolskie、Slaskie、Dolnoslaskie、Pomorskie、Lodzkie）。
- [ ] 待核实：Atman WAW-3（Duchnice 43.2 MW 目标）与 Equinix WA4x/xScale 的建筑许可/并网记录；Vantage WAW1 48 MW 的 RWDZ/PSE 证据；Microsoft Poland Central 三个物理位置的本地 SPV 与许可线索；DATA4 Jawczyce 分期状态；KCPD 公开位置/建设状态（敏感，保守标注）；PSE 并网清单中华沙周边大负荷（instalacja odbiorcza）项目的法人/站点匹配。
