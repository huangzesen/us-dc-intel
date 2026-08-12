---
name: cv-datacenter-methodology
location: scripts/expansion/world/country-skills/CV/SKILL.md
description: 佛得角（Cabo Verde）数据中心发现与审计方法论：官方/监管/云管线（BOE 公报、ARME 多部门监管局、NOSi 政府数据中心运营方、市政执照、AfDB/EIB/世行融资文档）叠加行业/贸易媒体发现（运营商、海缆、目录、行业媒体）；以清单中的 2 个地理大区（Ilhas de Barlavento / Ilhas de Sotavento）为划分粒度，每条设施记录须同时携带大区+岛屿+市镇。运行 CV 探索/审计批次前必读；分别路由到 explorer-official.md 与 explorer-industry.md。Bilingual discovery & audit methodology for Cabo Verde datacenters: official/regulatory/cloud pipeline + industry/trade-press discovery, at the 2 geographical-region division granularity from the manifest; read before running CV exploration/audit batches; routes to explorer-official.md and explorer-industry.md.
---

# CV · 佛得角数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> **目的**：佛得角没有公开的国家数据中心登记册；本方法论通过官方/监管/云管线（explorer-official.md）与行业/厂商发现（explorer-industry.md）双通道三角互证，枚举运营中、在建、规划及机构型数据中心设施。市场小而由州/电信主导：已确认设施全部集中在 Praia（Santiago / Sotavento），第二极点为 Mindelo（São Vicente / Barlavento）的 TechPark CV 园区。运行任何 CV 探索/审计批次前必须阅读本 skill，并按需路由到两份探索报告。

## 入口（Entry points）

| 文件 | 管线 | 内容 |
|---|---|---|
| explorer-official.md | 官方/监管/云管线 | 规划与市政执照（Câmara/BOE）、通信监管（ARME）、政府 ICT（NOSi、Digital Cabo Verde P171099）、数据保护（CNPD）、能源（ELECTRA/EDEC）、采购与项目融资（AfDB/EIB/世行）、海缆与云区域排除检查 |
| explorer-industry.md | 行业/厂商发现 | 运营商与设施扫描（TechPark、NOSi、CVTelecom、Unitel T+、MITT）、行业/媒体来源表、目录到一手信源工作流、岛屿/大区查询配方、产能与可靠性提取规则 |

## 核心结构事实（框定每次搜索）

1. **划分模型**：清单（world-manifest.jsonl）为 **2 个地理大区**（subnational_type = geographical region，非行政二级）：**Ilhas de Barlavento**（向风：Santo Antão、São Vicente、Santa Luzia、São Nicolau、Sal、Boa Vista）与 **Ilhas de Sotavento**（背风：Maio、Santiago、Fogo、Brava）。地理大区不是行政区划——每条设施记录必须携带大区 + 岛屿 + concelho（市镇），且大区名称按清单原拼写记录，绝不臆造清单外划分。
2. **核心设施集**：Sotavento/Santiago/Praia —— TechPark CV Praia 园区数据中心（NOSi 管理，园区 2025-05-05 启用，DC 约 2022 年底建成）、NOSi 数据中心（老 AfDB 支持设施，距 TechPark <2 km；**两条记录除非有地址级证据否则不得合并**）、CVTelecom 数据中心（运营商中立托管的服务主张为 B/C 级，地址/容量未验证）、Praia Data Center (MITT)（2010–2014 历史机构记录，C+ 种子）；Barlavento/São Vicente/Mindelo —— TechPark CV Mindelo 园区（2025-05-06 启用，二期为 DR 站点/两座数据中心，€14M 二期贷款 2023-08 签署）；另 Unitel T+ 数据中心（C 级线索）。
3. **关键机构**：ARME（多部门经济监管局，Decreto-lei 50/2018 合并 ARE+ANAC，监管通信/能源/水务/客运；含基础设施共享条例）、BOE（Boletim Oficial Eletrónico，boe.incv.cv，法律/特许/通告）、CNPD（国家数据保护委员会，Lei 41/VIII/2013）、NOSi（政府数字局与已证实的数据中心运营方，nosi.cv）、市政 câmaras（Praia Loja CMP 在线执照门户 lojacmp.com、São Vicente cmsv.cv）、ELECTRA/EDEC（电力）、AfDB/EIB/World Bank（项目融资）、IFC CPSD 2024。
4. **查询语言与拼写**：葡语为主（"centro de dados"、"datacenter"、"centro de processamento de dados"、"sala de servidores"、"hospedagem"、"colocação"、"estação de aterragem"、"cabo submarino"）+ 英语（"data center/data centre"、"landing station"）。永远加 "Cabo Verde" 或 "Cape Verde" 加岛屿/concelho；裸 "CV" 噪音大。
5. **容量语义**：所有设施的容量均未公开；`capacity_mw: null` 除非有显式一手来源。AfDB 贷款额（€14M 二期、€45.5M/€51.85M 园区、约 US$57M 合计）、EIB US$25M 海缆支持、CVT US$60M 项目均为融资事实而非 MW/机架数。
6. **海缆不是数据中心**：Praia 登陆的 EllaLink 分支、WACS、SHARE、CVT 国内海缆、Atlantis-2（RFS 2000，2022-01 报道断开）为连接性基础设施；只有出现服务器/托管/colo 证据才提升为数据中心记录。
7. **云区域缺失是已核查事实**：AWS/Azure/GCP/OCI 官方页面均无佛得角区域；每次刷新重查官方页面，经销商/VPS/边缘页面为常见误报。
8. **可靠度分级**：A = 官方/一手来源证实主张（BOE/法律文件、ARME 执照/决定、NOSi/政府页面、AfDB/EIB/世行项目文件、运营商官方页面/账号、云厂商官方区域页、认证注册）；B = 具名当事方/日期/地点的可靠媒体（Balai、Inforpress、Expresso das Ilhas、A Semana、Voz do Archipelago、DCD、Developing Telecoms、The Tech Capital、TechAfrica News、Submarine Networks 非业主报道）；C = 目录/市场/SEO 托管页、承包商作品集、社交/活动赞助页、转载或缺乏地址/设施证据的主张。
9. **诚实产量预期**：全国 **3–6 条设施记录** + 连接性站点；不得虚增。Santa Luzia（无人岛）明确记录为无公开项目。

## 常用查询模板（详见 explorer-official.md / explorer-industry.md）

```text
("data center" OR "data centre" OR datacenter OR "centro de dados") ("Cabo Verde" OR "Cape Verde")
("sala de servidores" OR servidor OR hospedagem OR colocation OR colocação) ("Cabo Verde" OR Praia OR Mindelo)
site:arme.cv ("data center" OR "centro de dados" OR colocation)
site:nosi.cv ("data center" OR "centro de dados" OR cloud OR hosting)
site:boe.incv.cv "{concelho}" ("data center" OR telecom OR subestação)
site:afdb.org Cabo Verde ("data center" OR "technology park" OR TechPark OR NOSi)
"Cabo Verde Telecom" ("data center" OR datacenter OR colocation OR "carrier-neutral")
"{island}" "Cabo Verde" ("data center" OR "centro de dados" OR colocation OR "sala de servidores")
"Cabo Verde" (colocation OR "carrier-neutral" OR "cloud hosting" OR VPS)   # 负向控制
"Cabo Verde" (AWS OR Azure OR "Google Cloud" OR OCI) ("data center" OR region)  # 云排除复核
(TechPark OR "centro de dados") "Cabo Verde" (rack OR sqm OR MW OR MVA OR capacidade)  # 容量
```

## 官方/监管管线要点（详见 explorer-official.md）

- 规划/执照：市政 câmaras（Praia Loja CMP、São Vicente 等 22 个 concelho）签发建设/占用许可；BOE 提供法律/土地特许/公共利益声明（含 ZEET 2022 经济特区、2.5% 公司税率）。
- 监管：ARME 界定获授权运营商宇宙（CVTelecom 集团、Unitel T+、CV Multimédia、CV WiFi、CABOCOM、MB Investimentos、TELMAX），从牌照转向设施。
- 政府 ICT：NOSi（数据中心运营方）、World Bank Digital Cabo Verde P171099（评估数字化/数据基础设施组件）、gov.cv（部委更迭频繁——引述前须从 gov.cv 重新推导现任部委/部长）。
- 数据保护：CNPD 依据 Lei 41/VIII/2013 处理登记/授权义务——需求侧与合规信号，非设施登记册。
- 能源：ELECTRA/EDEC 记录用于佐证大负荷/变电站/备电/EIA 条件；TechPark 二期明确为可再生能源供电 DC，Praia/Mindelo 园区能源记录高信号。
- 融资/采购：AfDB（TechPark 一期约 €45.5M + 二期 €14M）、EIB（EllaLink/CVT US$25M）、World Bank P171099；政府采购经 gov.cv concursos 与 BOE 合同公告。
- 云排除：每次刷新核查 AWS/Azure/GCP/OCI 官方区域页。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 目录到一手工作流：仅从目录（datacenters.com、colo.exchange、PQ.Hosting、DataCenterMap、Baxtel、PeeringDB）播种，再对 arme.cv / nosi.cv / techpark.cv / cvtelecom.cv / uniteltmais.cv / governo.cv / boe.incv.cv / afdb.org / eib.org / documents.worldbank.org 核验；位置经市政执照、ARME 执照或运营商官方地址验证；目录条目保持 C 级，除非名称/地址/运营商对齐否则不并入已确认设施。
- 状态验证：以启用/开幕/认证/运营服务证据为准（如 2025-05-05/06 TechPark 开幕）；仅规划/新闻声明用 announced/lead。
- 容量提取：不从未经验证的"carrier-neutral"、"world-class"、"Tier III"等营销措辞推断（本趟未发现 CV 的 TIA/Uptime 认证条目）。

## 维护注意（更新纪律）

- **更新节奏**：每次探索/审计批次刷新时重查云区域官方页、ARME/BOE/NOSi/gov.cv 与 AfDB/EIB 页面；部委组合变更时重新推导。
- **来源核验**：techpark.cv 可能为薄/存根站点，园区主张须与 AfDB/政府/媒体交叉核对；A Semana 对命令行客户端可能返回 403；目录条目一律视为 C 级种子。
- **不删除纪律**：无法核实的旧线索保留为降级线索并注明缺失证据，而非静默删除；NOSi DC 与 TechPark DC 两条记录在没有地址/地块证据前不得合并。
- 大区名称按清单原拼写（"Ilhas de Barlavento" / "Ilhas de Sotavento"），岛屿+concelho 为自然子层，搜索须组合大区+岛屿+市镇。
