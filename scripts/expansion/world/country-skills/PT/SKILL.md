---
name: pt-datacenter-methodology
location: scripts/expansion/world/country-skills/PT/SKILL.md
description: |
  Portugal (PT) datacenter discovery & audit methodology — how to enumerate, verify, and update Portugal datacenter projects at district + concelho/municipality granularity (manifest division labels White Castle=Castelo Branco, Royal Town=Vila Real are machine-translated). Portugal has no single public national datacenter facility registry: enumeration joins five pipelines — (1) national policy / PIN strategic-investment records (Plano Nacional de Centros de Dados, Resolução do Conselho de Ministros 70/2026; AICEP/Portugal Global), (2) APA/SIAIA + Participa environmental assessment and public-consultation files (model case Data Center Sines 4.0, AIA 3633/RECAPE 564), (3) municipal planning/licensing records (PIP, licenciamento urbanístico, licença de construção, câmara minutes), (4) electricity evidence (REN transmission, E-REDES distribution, DGEG, ERSE — substations, lines, MVA), and (5) cloud/colo/operator official pages (Start Campus/SINES DC, Equinix LS1/LS2, AtlasEdge, Edged/MERLIN, Asterion/Altice Covilhã, IP Telecom, NOS, MEO; AWS announced Lisbon sovereign Local Zone eusc-de-east-1-lis-1a — no standard AWS/Azure/GCP/OCI Portugal public region). Read this before running PT exploration/audit batches. Routes to explorer-official.md (PNCD/EIA/municipal/grid/cloud) and explorer-industry.md (PortugalDC/trade press/vendor seeds/district recipes).
---

# PT · 葡萄牙数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：葡萄牙**没有**单一全国数据中心设施注册库；可靠方法是拼接五条管线：**① 国家政策/PIN 战略投资记录（PNCD）② 环评与公众咨询文件（APA/SIAIA + Participa）③ 市政规划/许可记录 ④ 电力输配连接证据（REN/E-REDES/DGEG/ERSE）⑤ 云/colo/运营商官方页**。
> 大型园区常以**能源、工业区或环评许可**新闻先于 colo 营销页出现（Sines 4.0 是 APA/SIAIA 模型案例）；电力是限制性证据——营销 GW 是设计/已锁容量，须绑定阶段、变电站或并网文件；manifest 的 `White Castle`=Castelo Branco、`Royal Town`=Vila Real 是机器翻译标签。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供葡萄牙探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：PNCD（RCM 70/2026，A 级）、Diário da República/Portugal.gov/AICEP/IAPMEI、APA/SIAIA + Participa（含 Sines 4.0 AIA 3633/RECAPE 564 提取字段）、市政 urbanismo（Lisboa/Porto/Sines/Azambuja/Abrantes 模式）、REN/E-REDES/DGEG/ERSE 电网、ANACOM/CNCS 电信与网络安全、云区域核查（AWS 里斯本主权 Local Zone 宣布；无标准公共区域）、运营商种子（Start Campus/Equinix/MEO-Altice/NOS/Claranet/DE-CIX/IP Telecom）、逐区枚举策略与验证分级 |
| `explorer-industry.md` | 行业/厂商发现：PortugalDC/APDC/Atlantic Convergence 协会与市场报告、DCD/ECO/Jornal de Negócios/Portugal News 等贸易与葡语商业媒体、目录（DataCenterMap/Baxtel/PeeringDB 等）、运营商/开发商种子（Start Campus/Equinix/AtlasEdge/Edged-MERLIN/Asterion-Altice Covilhã/IP Telecom/Claranet/NOS/Decsis/FF Ventures/EDC One/Hyperion/Voltekko/Google 电缆）、云/本地区扫描（AWS Local Zone、Microsoft-Nscale-Sines 承诺、Google Azores/Sines 电缆）、逐区配方、容量/状态提取与分级 |

## 核心结构事实（框定每次搜索）

1. **PNCD 是国家政策锚点**：`Plano Nacional de Centros de Dados` 经 Resolução do Conselho de Ministros 70/2026（2026-04-13）批准，明确承认葡萄牙装机容量低于欧洲均值、存在项目组合与审批冗长/电网接入约束等障碍；PAPNCD 2026-2027 是观察“绿区”、许可简化、中央投资者互动与国家优先级的来源（https://diariodarepublica.pt/dr/detalhe/resolucao-conselho-ministros/70-2026-1084345989，A 级）。
2. **规划在市政层**：大型 DC 需要市政 urbanismo 记录——`PIP`（pedido de informação prévia）、`licenciamento urbanístico`、`licença de construção`、`obras de urbanização`、`deliberação de câmara`、偶发 PDM/unidade de execução 修订；市政纪要/议程 PDF 常先于全国媒体出现。
3. **环评是中枢**：数据中心本身未必是列名 EIA 项目，但大型园区经工业区工程、输电线路、变电站、水/冷却、备用发电、风电/光伏或配套电网工程触发 EIA/RECAPE；Start Campus Sines 文件是 APA/SIAIA 模型案例（`Data Center Sines 4.0`，AIA 3633 + RECAPE 564）；DIA/RECAPE 是许可里程碑，非运营状态。
4. **电力是限制性证据**：高置信容量需 REN 输电、E-REDES 配电、DGEG 能源许可或 EIA/RECAPE 变电站/线路细节；`design_capacity_mw`/`secured_grid_mw`/`phase_capacity_mw`/`live_capacity_mw` 分开；MVA ≠ IT MW。
5. **云区域=负控制 + 边缘信号**：AWS 官方宣布里斯本主权 Local Zone（`eusc-de-east-1-lis-1a`，AWS European Sovereign Cloud Germany 父区域）+ Equinix LS1 AWS Direct Connect（2025）——云边缘/连接，非标准区域；Azure/GCP/OCI 官方区域表均无葡萄牙公共区域；Microsoft/Nscale/Start Campus Sines 投资是客户/AI 基础设施承诺，非 Azure 区域证据。
6. **主集群**：Lisboa 大都会（Equinix LS1/LS2、AtlasEdge LIS001-3 21.1 MW→30 MW、Edged/MERLIN 180 MW Vila Franca de Xira、Claranet、IP Telecom、Altice/MEO 遗留）、Sines/Setúbal（Start Campus 1.2 GW 园区，SIN01 运营/SIN02 在建、Google Nuvem 电缆登陆）、Covilhã/Castelo Branco（Asterion/Altice 6.8 MW 园区 + 扩建潜力）、Porto/Matosinhos/Leixões、Viseu（IP Telecom）、Pego/Abrantes/Santarém（EDC One、Hyperion II 200 MVA）、Aljustrel/Beja（FF Ventures）、Azores/Madeira（MEO/NOS 岛域节点 + Google Azores CLS）。
7. **多拼写**：`data center`/`data centre`/`datacenter`/`centro de dados`/`centro de processamento de dados`/`CPD`/`sala técnica` 全要搜；`centro de dados municipal` 常是小公共 IT 机房，须与商业/colo/超大规模分类。
8. **反重复**：Start Campus/SINES DC/Sines 4.0/SIN01-SIN06 是园区/阶段别名；Altice/MEO/Portugal Telecom Data Center Covilhã/Asterion 是所有者/运营商别名；RNCA/CNCA/UMinho Guimarães/DST 是同一公共 HPC 设施。

## 查询模式（复制粘贴模板见 explorer-official.md §1 / explorer-industry.md §2、§6）

- 葡语核心词：`centro de dados` `data center` `datacenter` `centro de processamento de dados` `CPD` `sala técnica` `colocation` `alojamento` `cloud` `IA`；规划：`pedido de informação prévia` `PIP` `licenciamento urbanístico` `licença de construção` `obras de urbanização` `deliberação` `ata` `plano de pormenor` `unidade de execução` `loteamento`；环评：`AIA` `EIA` `DIA` `RECAPE` `consulta pública` `proposta de definição de âmbito (PDA)`；电网：`subestação` `linha 150 kV` `400/150 kV` `ponto de ligação` `ligação à rede` `MVA` `MW`；状态：`memorando`/`MoU`/`manifestação de interesse`=意向；`PIP`/`licenciamento`/`AIA`/`RECAPE`=许可中；`licença de construção`/`empreitada`/`consignação`/`início da obra`=在建；`operacional`/`inaugurado`/`entrada em operação`/`ready for service`=运营。
- 官方：`site:diariodarepublica.pt "centro de dados" Portugal`、`site:portugal.gov.pt "centro de dados"`、`site:siaia.apambiente.pt "centro de dados" OR "data center"`、`site:participa.pt "centro de dados"`、`site:dgeg.gov.pt "centro de dados"`、`site:ren.pt ("data center" OR "centro de dados") ("Sines" OR "Pego")`、`site:e-redes.pt "ligação à rede" "centro de dados"`、`site:anacom.pt "centros de dados"`、`site:cm-{municipio}.pt "centro de dados"`、`site:base.gov.pt ("centro de dados" OR datacenter)`。
- 行业：`site:datacenterdynamics.com/en/tags/portugal/ Portugal`、`site:eco.sapo.pt ("data center" OR "centro de dados") Portugal`、`site:jornaldenegocios.pt ("data center" OR "centro de dados")`、`site:itchannel.pt "data center" Portugal`、`site:theportugalnews.com "data centre" Portugal`、`site:portugaldc.pt "{operator}"`。
- 容量/状态提取：`"{project}" (MW OR MVA OR "capacidade IT" OR "fase 1" OR RECAPE)`、`"{project}" ("subestação" OR "linha 150 kV" OR "ponto de ligação")`。
- 云 pivot：`site:aws.amazon.com Portugal "Local Zone"`、`"Microsoft" "Start Campus" Sines "data center"`、`"Nscale" "Start Campus" Sines GPU`、`"Google" Nuvem Sol Sines Azores "cable landing station"`。

## 官方/监管管线要点（详见 explorer-official.md）

- **国家政策（A）**：Diário da República（PNCD/法令号/日期）、Portugal.gov.pt（政府声明 A / 转述公司投资数字 B）、AICEP/Portugal Global（PIN/投资者支持状态 A-/B+）、IAPMEI（官方经济支持记录，召回低）。
- **环评（A）**：APA/SIAIA 最佳 EIA/RECAPE PDF 库（搜 `data center` 与 `centro de dados`，也搜 `subestação`/`linha`/`parque eólico`/`fotovoltaico`/`Sines`/`Pego`/`Azambuja`）；Participa 公众咨询；提取提议人/SPV、地块、工业区单元、市镇/区、阶段（Fase 1 vs Fases 2-6）、面积、变电站、发电机数、冷却、取排水、配套线路、DIA/RECAPE 条件。
- **市政（A）**：Lisboa urbanismo/开放数据（召回低，多数 DC 在大里斯本市镇）、Porto `Consulta online de processos`、Sines（`NEST`/`Sines 4.0`/`Unidade de Execução` PDF 关键）、Azambuja（Alcoentre PIP）、Abrantes（Pego 第二 PIP）；市政纪要/议程 PDF 常先于可搜索项目页。
- **电网（A）**：REN（输电、rentelecom、EllaLink、Sines/Pego 变电站）、E-REDES（配电连接流程 + open data）、DGEG（能源/效率/GIS）、ERSE（市场规则语境，少点名）；>10 MW 主张须搜项目名+市镇+变电站+电压+MVA+配套可再生资产。
- **电信/数字（A，语境）**：ANACOM（海底电缆/连接/NIS2 内容）、CNCS/MyCiber（网络安全义务，设施发现价值低）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **协会/事件**：PortugalDC（B，国家数据中心协会，成员/政策种子，非设施注册表）、APDC（B/C）、Atlantic Convergence（C/B，Sines/Lisbon/Azores 电缆-云-AI）、Copenhagen Economics 报告（B 语境/C 设施细节）、ResearchAndMarkets/Arizton 片段（C/B 线索）。
- **贸易媒体**：DCD Portugal tag（B，最佳英文流）、ECO/Sapo（B，葡语商业）、Jornal de Negócios（B，企业投资/M&A/Covilhã/CTS）、Portugal News（B/C）、IT Channel/Business IT/Computerworld Portugal（B）、RTP/Lusa/本地报（B/C）；AICEP 新闻镜像（B）。
- **目录（C 线索）**：DataCenterMap、Datacenters.com、Baxtel、Cloudscene、PeeringDB、Inflect。
- **运营商种子（A=存在/B=容量）**：Start Campus（SINES DC，1.2 GW 园区，SIN01 运营/SIN02 在建/规划，APA AIA 3633）、Equinix（LS1/LS2 Lisbon/Prior Velho）、AtlasEdge（LIS001-3 Carnaxide/Oeiras，21.1 MW→30 MW）、Edged/MERLIN（Vila Franca de Xira 180 MW AI 园区）、Asterion/Altice/MEO（Covilhã 6.8 MW + 扩建，Uptime 认证）、IP Telecom（Lisboa/Porto/Viseu 三家自有，ISO 27001）、Claranet（Prior Velho/Beato）、NOS（Porto/Matosinhos + Azores/Madeira）、Decsis（Évora）、FF Ventures（Aljustrel/Mancoca）、EDC One + Hyperion II（Pego/Abrantes，200 MVA）、Voltekko（Alcochete）、Google（Azores Lagoa/Sines 电缆登陆，非 GCP 区域）、DE-CIX（SINES DC PoP，互连证据）。
- **状态语义（葡语）**：`protocolo`/`memorando`/`investimento anunciado`/`manifestação de interesse`=宣布/计划；`PIP`/`licenciamento`/`AIA`/`RECAPE`/`consulta pública`=许可中；`obra`/`construção`/`empreitada`/`adjudicação`/`início da construção`=在建；`inaugurado`/`operacional`/`ready for service`/`clientes instalados`/`em funcionamento`=运营。

## 来源分级

- **A** = 官方/一手：Diário da República、PNCD/PAPNCD、APA/SIAIA EIA/RECAPE/DIA、Participa 咨询、市政 PIP/许可/纪要、REN/E-REDES/DGEG 电网/能源文件、ERSE 规则、ANACOM/CNCS 监管出版物、运营商官方设施页（存在/位置）、Uptime 认证、Base.gov 合同。
- **A- / B+** = 运营商官方页容量（营销）、AICEP/Portugal.gov 转述的投资数字、PIN 状态。
- **B** = 强二级：DCD、Data Center Frontier、Capacity、TeleGeography、ECO/Lusa、Jornal de Negócios、SAPO TEK、IT Insight、Jornal Económico、APDC（点名运营商+市镇+项目细节）。
- **C** = 弱/聚合：DataCenterMap、Baxtel、PeeringDB、Datacenters.com、市场报告片段、LinkedIn、会议材料；仅作种子。
- **容量规则**：`design_capacity_mw`/`secured_grid_mw`/`phase_capacity_mw`/`live_capacity_mw` 分开；MVA 记作电网/导入容量除非源明确 IT load；Sines 相关可再生/电网项目可能只把 DC 当作承购方——作为配套基础设施链接，不作独立 DC；PIN 加速协调但不替代市政/环评/电网许可。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=PT，divisions=区/自治区；`White Castle`→Castelo Branco、`Royal Town`→Vila Real）。
2. 国家种子扫描：Diário da República/Portugal.gov/AICEP/ANACOM 搜 `Plano Nacional de Centros de Dados`/`PIN`/`centro de dados`/`Sines`/`cloud soberana`。
3. APA/SIAIA + Participa 扫描：`data center`/`centro de dados`/`Sines`/`Pego`/`Azambuja`/`Alcoentre`/`subestação`/`parque eólico`/`linha 150 kV`；从 PDF 提取提议人/阶段/MW/MVA/日期。
4. 逐区市政扫描：优先 Setúbal/Sines、大里斯本、Porto、Braga/Famalicão、Castelo Branco/Covilhã、Santarém/Abrantes；搜市政站/纪要/议程/urbanismo 门户/开放数据。
5. 电力验证：>10 MW 主张搜 REN/E-REDES/DGEG/ERSE（项目名+市镇+变电站+电压+MVA+可再生资产）。
6. 运营商/云扫描：Start Campus/Equinix/MEO-Altice/AtlasEdge/Edged/DE-CIX + AWS/Azure/GCP/OCI 官方位置（AWS 里斯本 Local Zone 状态季度复查）；标记运营/服务状态。
7. 贸易媒体线索补缺，仅在一个官方或运营商源确认后提升记录；去重别名（Sines 园区/阶段、Covilhã 所有者、Guimarães 公共 HPC）。
8. 输出字段：`{country_code: PT, district_or_region, municipality, facility_or_project_name, proponent/operator, status, design_capacity_mw, phase_capacity_mw, live_capacity_mw, grid_evidence, planning_evidence, environmental_evidence, source_urls, evidence_grade, evidence_date, notes}`；无项目 division 写 `no_projects: true`。
9. 遵循 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：批量复核葡萄牙数据中心（区/市镇粒度，Sines+大里斯本深扫）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：Start Campus SIN02 建设与后续阶段、Microsoft/Nscale Sines 实际设施、Edged/MERLIN Vila Franca de Xira 180 MW 许可、AtlasEdge LIS003 与 30 MW 园区、Asterion Covilhã 扩建、EDC One/Hyperion II Pego 许可（200 MVA）、FF Ventures Aljustrel 市政协议、Voltekko Alcochete、AWS 里斯本主权 Local Zone 上线时间、Guimarães RNCA 公共 HPC。
