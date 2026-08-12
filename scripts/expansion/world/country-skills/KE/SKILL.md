---
name: ke-datacenter-methodology
location: scripts/expansion/world/country-skills/KE/SKILL.md
description: |
  Kenya (KE) datacenter discovery & audit methodology. No national registry; enumeration joins county development/construction permits (KenInvest eProcedures, Nairobi eDevelopment), NEMA EIA/ESIA/SEA records, NCA project registration, CA Kenya licensing (Unified Licensing Framework, licensee register), power-grid evidence (Kenya Power/KETRACO/KenGen/EPRA), official cloud signals (Microsoft/G42 East Africa region at Olkaria, Oracle Kenya region with iXAfrica; AWS/Google none), and operator pages (iXAfrica NBOX1/NBOX2, Africa Data Centres NBO1, Digital Realty/iColo NBO/MBA, Safaricom, Airtel/Nxtra Tatu City, Konza National Data Centre, PAIX). Division model: 47 counties. Read this before running KE exploration/audit batches. Routes to explorer-official.md (county/NEMA/NCA/CA/power/cloud) and explorer-industry.md (press/vendor/county matrix).
---
# KE · 肯尼亚数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：为肯尼亚数据中心枚举提供「郡开发许可 + NEMA 环评 + NCA 项目登记 + 电力 + 云信号 + 运营商官网」六线并联的查询框架。肯尼亚**没有全国性数据中心规划注册库**，多数高召回公共证据**并不标为规划许可**，应走肯尼亚审批链：郡建设/开发许可 → NEMA EIA/ESIA/SEA → NCA 项目登记 → Kenya Power/KETRACO 连接/变电站/招标 → CA Kenya 电信/服务许可。活动高度集中于**内罗毕市、Kiambu（Tatu City/Ruiru/Limuru/Thika/Tilisi）、蒙巴萨、Konza（Machakos-Makueni-Kajiado 边界）、Nakuru（Olkaria/Naivasha）、基苏木**。本 skill 汇总两份探索报告（官方管线 + 行业发现），供肯尼亚探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：KenInvest eProcedures、Nairobi eDevelopment、NCA、NEMA 上传库、CA Kenya 市场结构与持牌人登记册、Kenya Power/KETRACO/KenGen/EPRA、云信号（Microsoft/G42、Oracle）、运营商官网 |
| `explorer-industry.md` | 行业/厂商发现：DCD/CIO Africa/Techweez/Business Daily 等媒体、运营商/开发商矩阵、47 郡枚举矩阵（含英/斯瓦希里语查询）、云区域处理与去重规则 |

## 核心结构事实（框定每次搜索）

1. **无全国注册库，走审批链**：郡建设/开发许可（KenInvest eProcedures https://eprocedures.investkenya.go.ke/ 列明 Nairobi/Kisumu/Mombasa/Uasin Gishu/Kilifi/Meru/Nyeri/Laikipia/Nakuru 等郡的建设许可程序；Nairobi 用 https://edev.nairobiservices.go.ke/）→ NEMA EIA/ESIA/SEA → NCA 项目登记（https://www.nca.go.ke/project-registration）→ Kenya Power/KETRACO 连接/变电站 → CA Kenya 许可（商业数据中心若部署商用通信基础设施、提供托管/云/互联或接入第三方，可能落入电信基础设施/服务许可）。
2. **NEMA 高精度但不完整**：https://nema.go.ke/ 与 `https://nema.go.ke/wp-content/uploads/` 下公开 EIA 报告 PDF 是高价值源；数据中心可能以商业/ICT 建筑、工业园、SEZ 设施、变电站、光纤项目、备用发电/燃料储存、或 SEA/EIA 报告组成部分出现。
3. **CA Kenya 是运营商/服务许可证据**：https://www.ca.go.ke/market-structure（2026-04 统一许可框架：Network Facilities Provider Tier 1/2/3 + Applications Service Provider）+ https://www.ca.go.ke/licensee-register（2026-06 电信持牌人登记册，搜 IX AFRICA/AFRICA DATA CENTRES/ICOLO/DIGITAL REALTY/SAFARICOM/AIRTEL/LIQUID/PAIX/WANANCHI/KONZA/ECOCLOUD/G42/ORACLE/MICROSOFT）。许可 ≠ 设施计数（一家持牌公司可运营多址）。
4. **电力/地热是核心过滤器**：Kenya Power（KPLC）https://kplc.co.ke/（MVA/MW/变电站/专线/供电协议/Tatu City 变电站/Olkaria）；KETRACO https://www.ketraco.co.ke/（输电变电站、高压走廊，曾有商用 Tier IV 数据中心公开 EOI——招标为 A，设施推断为 B 除非点名地点）；EPRA https://www.epra.go.ke/statistics-0（国情语境，不作设施证据）；KenGen Green Energy Park https://greenenergypark.kengen.co.ke/（Olkaria/Nakuru 地热项目：EcoCloud/Project Eagle、Microsoft/G42）。
5. **云信号 = 都会/郡种子，非设施**：Microsoft/G42 于 2024-05-22 宣布 10 亿美元肯尼亚数字生态倡议，含 Olkaria 绿色数据中心园区承载 Azure 新 East Africa 云区域（官方公告 A；2026 年报道称因电力容量延迟，状态须现时核实；Azure 公开区域清单尚无肯尼亚）；Oracle 宣布肯尼亚公有云区域意图（与 iXAfrica 托管合作，A 为公告，服务是否上线须核实）；**AWS 与 Google 官方区域清单无肯尼亚区域**——其边缘/合作伙伴存在不得转为设施记录；Azure Front Door 列 Nairobi/NBO 为边缘 POP（POP ≠ 数据中心园区）。
6. **英语为主 + 斯瓦希里语次查**：双拼写 `data centre`/`data center`，另 `datacentre`/`server room`/`server farm`/`cloud`/`colocation`/`ICT hub`/`Tier III`/`hyperscale`/`substation`/`MVA`/`MW`；斯瓦希里语仅作郡政府 ICT 项目次查：`kituo cha data`（数据中心）、`chumba cha seva`（机房）、`kituo cha TEHAMA`（ICT 中心）、`ujenzi`（建设）、`kuzindua`/`uzinduzi`（启动），命中须有实体设施+运营方+阶段才计数。
7. **阶段/容量/去重陷阱**：`announces`/`signs MoU`/`seeks investors`=意向（C/B）；`acquires land`/`breaks ground`/`starts construction`=更强管线（B 除非官方）；`opened`/`launched`/`operational`/`Uptime certified`=运营信号（A 须运营商/Uptime/云页复核）。**Nairobi 市场 vs 郡**：Limuru/Thika/Tatu City/Tilisi/Redhill 常被宣传为 Nairobi 但物理属 Kiambu；**Konza 边界模糊**（Machakos/Kajiado/Makueni 均被引用，保留单一规范记录除非地块/阶段文件证实分属各郡）；2013-2015 年 Konza 投资者意向文章（Equity/EACP/JamboPay）仅为意向；政府 CIDP「data centre」可能是 GIS/统计办公室/呼叫中心/机房（仅当实际托管/处理数字负载且有地点/运营商/状态证据才计数）；容量单位（IT MW / MVA / 园区满配）不互换；微软/G42 类巨型项目须现时状态核实。

## 查询模式（复制粘贴模板见 explorer-official.md §1-3 与 explorer-industry.md §4-5）

- `"{county}" Kenya ("data centre" OR "data center" OR datacentre) ("MW" OR MVA OR racks OR "IT load")` / `"{town}" Kenya ("data centre" OR "data center") ("opened" OR launched OR operational OR construction OR "breaks ground")`
- `site:{county-domain} "data centre"` / `site:nairobi.go.ke "data centre" "construction permit"` / `"{county}" "data centre" "EIA"`
- `site:nema.go.ke/wp-content/uploads "data centre" Kenya` / `site:nema.go.ke/wp-content/uploads "{operator}" "Environmental Impact"` / `site:nema.go.ke/wp-content/uploads "Tatu City" "data centre"`
- `site:nca.go.ke "data centre"` / `site:nca.go.ke "project registration" "{operator}"`
- `site:ca.go.ke "Commercial Data Centres"` / `site:ca.go.ke "Register of Telecommunications Licensees" "{operator}"` / `site:ca.go.ke "{operator}" "licence"`
- `site:kplc.co.ke "{operator}" "MVA"` / `"{project}" "power supply agreement"` / `"Olkaria" "data center" "geothermal" "KenGen"` / `site:ketraco.co.ke "data center" "Tier IV"`
- `site:konza.go.ke "data centre" OR "data center" OR "cloud"` / `site:tatucity.com "data centre" OR Nxtra OR Airtel` / `site:greenenergypark.kengen.co.ke "data centre" OR EcoCloud`
- `"{county}" "kituo cha data"` / `"{county}" "chumba cha seva"`（斯瓦希里语次查）
- 阶段词映射：announces/MoU/plans=意向（C/B）；breaks ground/starts construction=施工（B）；opened/launched/operational/Uptime certified=运营（A 须复核）。

## 官方/监管管线要点（详见 explorer-official.md）

- **郡开发/建筑许可（A 级）**：KenInvest eProcedures（按 ICT/Energy/Building 行业 + 郡定位建设许可程序）；Nairobi Planning and Development Management System https://edev.nairobiservices.go.ke/（Mombasa Road/Cabanas、Sameer Business Park、Karen/Langata、Upper Hill、Westlands；账户受限时用索引 PDF/告示）；NCA https://www.nca.go.ke/project-registration（施工确认路径）。从许可/规划文件提取：郡、sub-county/ward、LR/plot、道路/工业园、申请人/SPV、开发描述、楼面、机架/机房数、IT MW、电网 MVA、发电机/燃料储存、水需求、EIA 许可/状态、NCA 登记、施工/投产日期。
- **NEMA 环评（A 级）**：https://nema.go.ke/services/environment-impact-assessment-eia/ + `site:nema.go.ke/wp-content/uploads` 全站搜；提取 NEMA 参考号、发起人、EIA 专家、LR/plot、坐标、水与污水、发电机组与燃料储存、噪声/空气质量建模、施工期、接入电力/变电站、公众参与、缓解措施。
- **CA Kenya（运营商/服务许可证据）**：市场结构（2026-04 统一许可框架）+ 持牌人登记册（2026-06）+ 许可申请表/费用 https://www.ca.go.ke/license-application-forms-fees。
- **政府云/ICT 部门**：ICT 部 https://ict.go.ke/（2026 政府数据中心/云承诺、Kenya Cloud Policy、sovereign cloud、AI Infrastructure）；ICT Authority https://icta.go.ke/（政府数据中心/DR/郡级迷你 DC）；Konza Technopolis https://konza.go.ke/ + Konza Cloud https://konza.go.ke/konza-cloud/（A 级国家数据中心/云服务存在性；郡归属按地块确认，否则标注边界提示）。
- **电力/地热（A 级）**：KPLC（服务申请/招标/变电站/大客户连接/光纤-on-power-line）；KETRACO（输电变电站、Tier IV EOI）；EPRA 统计（语境）；KenGen Green Energy Park（Olkaria 地热园区，EcoCloud/Project Eagle/Microsoft-G42，须 NEMA SEA/EIA + Kenya Power/KETRACO/KenGen 电网证据才可把施工状态定为 A）。
- **云信号页**：Microsoft/G42 https://news.microsoft.com/source/2024/05/22/microsoft-and-g42-announce-1-billion-comprehensive-digital-ecosystem-initiative-for-kenya/（A 级公告；Azure 区域清单 https://learn.microsoft.com/en-us/azure/reliability/regions-list 尚无肯尼亚）；Oracle https://blogs.oracle.com/cloud-infrastructure/oci-announces-plans-to-expand-in-africa（肯尼亚区域意图；OCI 区域清单 https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm 非洲仅约翰内斯堡+卡萨布兰卡在营）；AWS/Google 区域清单（无肯尼亚）；Azure Front Door NBO 边缘 POP https://learn.microsoft.com/en-us/azure/frontdoor/edge-locations-by-region。
- **运营商官方页（A 级存在性）**：iXAfrica NBOX1 https://ixafrica.co.ke/（Cabanas/Mombasa Road 内罗毕，官方设计容量 22.5 MW；Oracle/主权云合作；NBOX2/Tilisi 规划）；Africa Data Centres/Cassava NBO1 https://www.africadatacentres.com/nairobi/（Sameer Business Park，7.5 MW 可用、4 个 Uptime Tier III 机房）；Digital Realty/iColo https://www.digitalrealty.com/data-centers/emea/nairobi + https://www.icolo.io/（Nairobi NBO1/NBO2 Langata South Road；Mombasa One/Miritini 0.9 MW、Mombasa Two/Nyali 1.75 MW）；Safaricom https://www.safaricom.co.ke/wholesale/wholesale_product_categories/data_centre/（Thika/Nairobi/Kisumu，Limuru/Redhill 扩张）；Airtel/Nxtra https://www.airtel.africa/data-centers（2025-09-09 于 Tatu City 破土，Kiambu，报道 44 MW）；Tatu City SEZ https://www.tatucity.com/；Konza National Data Centre/Konza Cloud（KoTDA 官方）；PAIX Nairobi-1 https://www.paix.io/（Britam Tower/Upper Hill）；Wananchi/Zuku（光纤/托管线索，官方数据中心证据较薄）；EcoCloud/Project Eagle/KenGen Green Energy Park（Olkaria，须官方能量/许可证据）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **贸易媒体分级**：DCD（B，肯尼亚项目最佳源：iColo 蒙巴萨/内罗毕、PAIX、Konza/Huawei、iXAfrica、Safaricom Limuru、Olkaria/EcoCloud、Microsoft/G42 延迟）、CIO Africa（B，iXAfrica/Safaricom、LINX Nairobi、政府云论坛、Oracle/iXAfrica）、Techweez（B/C，iColo/Konza/Telkom/Oracle 历史本地覆盖）、Business Daily Africa（B，Konza/PPP/政府云采购/郡 technopolis 法）、Nation/The Standard/The Star/Capital Business（B/C）、Africa Data Centres Association https://africadca.org/（B，Oracle/iXAfrica）、LINX/KIXP/PeeringDB（B，互联公告证明网络节点存在非设施容量）。
- **运营商/开发商矩阵（按郡）**：内罗毕=iXAfrica NBOX1、ADC/EADC Sameer、iColo/Digital Realty NBO1/NBO2、PAIX Britam、Telkom/Safaricom/Liquid/SimbaNET/Angani/Wingu；Kiambu=Nxtra/Airtel Tatu City、Safaricom Thika + Limuru/Redhill、iXAfrica NBOX2/Tilisi、Tilisi Developments https://tilisi.co.ke/；蒙巴萨=iColo MBA1 Miritini/MBA2 Nyali、LINX Mombasa、海缆运营商；Machakos/Kajiado/Makueni=Konza 国家数据中心（边界谨慎）；Nakuru=EcoCloud/Project Eagle/KenGen/G42/Microsoft（Olkaria/Naivasha 地热园区）；基苏木=Safaricom Kisumu（边缘/DR）；Vihiga=郡政府 GIS 数据中心（与商业托管分开计数）。
- **目录来源（C/B-）**：DC Byte/Baxtel/DataCenterMap/OCOLO/Inflect/Datacenters.com 仅作旧企业/电信站点线索；供应商案例（Siemon/Schneider/Huawei/Vertiv/Caterpillar/SPS Africa）作存在性与工期线索；Uptime Institute Awards https://uptimeinstitute.com/uptime-institute-awards/（A，认证设施如 Konza、Safaricom Thika）。
- **去重与验证**：Nairobi 市场 vs 郡（Kiambu/Machakos 等）按物理地址落郡；Konza 单一规范记录；旧 Konza 投资者意向（2013-2015）不算项目；政府「data centre」区分 GIS/统计/呼叫中心；聚合目录郡归属错误频发；容量膨胀（园区满配 vs IT MW vs MVA）原样记录；巨型项目（Microsoft/G42）须现时状态核实。

## 来源分级

- **A** = 官方/一手：运营商官方位置页、官方云区域页、Uptime Institute 认证页、Konza/Tatu/KenGen/PPP/NCA/NEMA/郡批准文件、Safaricom/Airtel/Digital Realty/iXAfrica 官方发布。
- **B** = 强二级：DCD、CIO Africa、Business Daily、Techweez、Africa Data Centres Association、LINX/KIXP 公告、可信供应商案例。
- **C** = 弱线索：聚合目录设施页、市场报告片段、社交帖、LinkedIn 容量声称、旧 Konza 投资者意向文章、LAPSSET/数字走廊页（无命名设施）。
- 状态语义：A 设施存在=官方运营商/政府页点名或 NEMA/郡/NCA/CA/电力文件确认；A 施工中=官方运营商/政府/NCA/NEMA 证据；云区域≠设施（Microsoft/G42、Oracle 仅记云/项目种子除非官方在营区域页确认并存在本地设施证据）；电信/郡 ICT 机房谨慎分级。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=KE，divisions=47 counties），对每郡跑四轮：媒体/厂商轮（郡+城镇+data centre/data center/datacentre/colocation/hyperscale/cloud region）→ 运营商轮（iXAfrica/ADC/iColo/Digital Realty/PAIX/Safaricom/Airtel/Nxtra/Konza/KenGen/EcoCloud/G42/Oracle/Microsoft/Telkom/Liquid/SimbaNET/Wingu/Angani）→ 许可/官方轮（郡建筑许可告示、NCA、NEMA、CIDP/ADP/预算 PDF、SEZ/工业园页）→ 互联/聚合兜底（LINX/KIXP/PeeringDB/Baxtel/DataCenterMap）。
2. 种子：高优先郡簇——内罗毕、Kiambu（Tatu City/Ruiru/Thika/Limuru/Redhill/Tilisi）、蒙巴萨（Miritini/Nyali/LINX）、Konza（Machakos/Kajiado/Makueni）、Nakuru（Olkaria/Naivasha/KenGen Green Energy Park）、基苏木。
3. 验证：高价值在建项目须 NEMA/NCA/郡规划、Uptime、PPP、SEZ 或官方运营商发布确认；容量/状态按字段分级并记证据日期。
4. 输出：按 world schema 写结果；规范设施名+别名、物理郡、城镇/道路/园区、运营商/SPV、状态与证据日期、容量（IT MW/MVA/racks/sqm/机房间数）、来源 URL 与分级、郡模糊/阶段/商业-政府-边缘-企业属性备注。
5. 无项目判定：低概率郡（Baringo、Turkana、Wajir、Mandera 等）用官方郡站+NEMA+命名运营商扫+`data centre/data center/datacentre/server farm/cloud` 词兜底，避免把数据采集办公室/网吧/计算机实验室/郡 GIS 办公室记为数据中心；三面无信号才设 no_projects: true。
6. 遵守 NO-DELETION；本 skill 与两份 explorer 均为只读输入，只新增 SKILL.md 与 ANATOMY.md。

## 待办（2026-08-12 02:27Z）

- [x] explorer-official.md 与 explorer-industry.md 已完成并合并为本 SKILL.md。
- [ ] 下一步：每批 50× codex terra agents，注入本 skill 后按 47 郡逐郡枚举（优先 Nairobi City、Kiambu、Mombasa、Machakos/Kajiado/Makueni（Konza）、Nakuru、Kisumu）。
- [ ] 待核实：Microsoft/G42 Olkaria 园区现时状态（2026 报道的电力容量延迟是否已解决，Azure East Africa 区域是否上线）；Oracle 肯尼亚区域是否已在 OCI 区域清单上线；Airtel/Nxtra Tatu City 44 MW 的 NCA/NEMA/Kenya Power 证据；iXAfrica NBOX2/Tilisi 的 Kiambu 郡许可与 SEZ 状态。
