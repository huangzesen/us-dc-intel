# MP Explorer Official — 北马里亚纳群岛数据中心盘点官方渠道方法论

Date verified: 2026-08-12 ｜ Scope: Commonwealth of the Northern Mariana Islands (CNMI / MP, 北马里亚纳群岛联邦)

Manifest confirmed from `world-manifest.jsonl`:

```json
{"country_code":"MP","country_name":"Northern Mariana Islands","subnational_type":"country","divisions":["Northern Mariana Islands"]}
```

Manifest 只有一个 division：**Northern Mariana Islands**。最终输出必须只使用这个 division；Saipan 塞班、Tinian 天宁、Rota 罗塔仅作为 municipality / island-level search buckets，用于归位和覆盖检查，不得写成 manifest divisions。

本文件用于 official/regulatory pass：CNMI 政府与立法/审计/宽带机构、CUC 公用事业、FCC/USAC、美国联邦采购与拨款、海缆登陆许可、云服务商官方区域页。结论按设施主张分级，不按网站整体分级。

## 1. 结论速览 Bottom Line

截至 2026-08-12 的验证结论：CNMI 没有官方证据显示存在 hyperscale cloud region、commercial carrier-neutral colocation campus，或独立的大型数据中心市场。可确认的骨架是电信基础设施、海缆登陆与政府宽带项目。

- **已确认 telecom infrastructure（Grade A/B）**：FCC 1997 cable landing license 确认 Mariana-Guam Cable / MICS 在 Saipan、Tinian、Rota 与 Guam 有登陆点；FCC 2022 public notice 确认 Atisa 覆盖 Saipan、Tinian、Rota、Guam，并说明 MICS/Atisa 均为 interisland traffic 的竞争路由。
- **已确认 Atisa（Grade A/B）**：DoCoMo Pacific 官方新闻稿称 FCC 已批准 Atisa landing license，系统连接 Guam、Saipan、Rota、Tinian，并在 Rota/Tinian 建设 cable landing stations；NEC 官方新闻稿确认 ATISA 完成并用于把 CNMI 连接到 Guam。
- **已确认 broadband program（Grade A）**：CNMI Broadband Policy and Development Office 发布 BEAD 文档；其页面显示 2026-05-13 与 Micronesian Telecommunications Corp. dba IT&E 签署 BEAD Subgrant Agreement。BEAD 是宽带/last-mile 与 middle-mile 线索，不自动构成数据中心证据。
- **已确认 power constraint source（Grade A）**：CUC 2025 RFP `CUC-RFP-25-021` 为 Saipan、Tinian、Rota 全岛 Solar PV + BESS IPP 采购，附各岛 power plant / transmission-distribution maps。该类材料用于判断电力可行性，不是数据中心证据。
- **云区域缺席（Grade A）**：AWS、Azure、Google Cloud、Oracle OCI 官方区域/位置页未列 CNMI / Saipan / Tinian / Rota 为 cloud region 或 local zone。Google Pacific Connect / Proa 是海缆项目，不是 Google Cloud region。
- **不要计入**：Starlink/Viasat/Kacific 终端、移动基站、FTTP 覆盖、普通 ISP POP、政府办公室 IT、赌场/酒店/写字楼 server room，除非来源明确给出 colocation/hosting/data center/racks/power/cooling for third parties。

## 2. 可靠性分级 Reliability Grades

- **Grade A（官方/一手 Primary）**：`governor.cnmi.gov`、`cnmileg.net` / `cnmileg.gov.mp`、`opacnmi.com`、`commerce.gov.mp`、`bpd.cnmi.gov`、`cucgov.org`、FCC/USAC 官方系统、SAM.gov、FPDS、USASpending、Grants.gov、DOI OIA、FEMA、NTIA、运营商官方页面/PDF、云厂商官方基础设施页。
- **Grade B（强二手 Strong secondary）**：Marianas Variety、Saipan Tribune、Guam Daily Post、Pacific Daily News、KUAM、Pacific Island Times、RNZ Pacific、Submarine Networks、TeleGeography、Data Center Dynamics、Capacity Media；要求有日期、具名主体、可交叉核验。
- **Grade C（弱/聚合 Weak/aggregate）**：DataCenterMap、Cloudscene、Baxtel、Datacenters.com、ColoMap、WHTop、PeeringDB/BGP 目录、LinkedIn、Facebook/Instagram、招聘启事、论坛、转售商/主机目录。

分级针对具体 claim：FCC/USAC 能证明运营商、无线牌照、海缆或 USF 身份；不能单独证明该运营商在 CNMI 运营数据中心。目录站列出 Saipan data center 只能作为 C 级线索，必须追到运营商官方页、FCC/ICFS 文件、合同/RFP 或本地许可。

## 3. 已验证官方来源 Official Sources

### 3.1 CNMI 政府与公共机构

- CNMI Governor / government directory: `https://governor.cnmi.gov/`（verified；当前 governor 站点）
- Northern Marianas Commonwealth Legislature: `https://cnmileg.net/`（verified；站内仍链接部分 `cnmileg.gov.mp` 资源）
- Office of the Public Auditor: `https://www.opacnmi.com/`（verified；OPA reports / financial audits）
- Department of Commerce: `https://www.commerce.gov.mp/`（verified）
- CNMI Broadband Policy and Development Office: `https://bpd.cnmi.gov/`（verified；BEAD documents）
- Northern Marianas College: `https://www.marianas.edu/`（verified；institutional IT/procurement lead only）

政府来源可用于发现 government data center / disaster recovery / server room / hosting RFP，但只有出现专用设施语言时才建档。普通 IT system、software、website、helpdesk、network equipment purchase 不能升级为数据中心。

查询模板：

```text
site:governor.cnmi.gov "data center" OR "server room" OR "cloud" OR "disaster recovery"
site:cnmileg.net OR site:cnmileg.gov.mp "data center" OR "broadband" OR "telecom" OR "CUC"
site:opacnmi.com "data center" OR "server" OR "information systems" OR "CUC"
site:bpd.cnmi.gov "data center" OR "middle mile" OR "BEAD" OR "IT&E"
site:commerce.gov.mp "broadband" OR "telecom" OR "data center"
site:marianas.edu "data center" OR "server room" OR "IT infrastructure"
```

### 3.2 FCC / USAC 电信监管通道

- FCC ULS / wireless systems: `https://www.fcc.gov/wireless/systems-utilities`（verified；ULS search entry point）
- FCC database search hub: `https://www.fcc.gov/licensing-databases/search-fcc-databases`（verified）
- FCC Form 477 fixed broadband deployment data: `https://www.fcc.gov/general/broadband-deployment-data-fcc-form-477`（verified historical data）
- FCC Form 477 resources: `https://www.fcc.gov/economics-analytics/industry-analysis-division/form-477-resources`（verified；broadband deployment moved away from Form 477 after 2022）
- FCC National Broadband Map: `https://broadbandmap.fcc.gov/`（verified URL; interactive site may block crawlers）
- FCC submarine cable landing guide: `https://www.fcc.gov/research-reports/guides/submarine-cable-landing-licenses`（verified）
- FCC submarine cable applications: `https://www.fcc.gov/submarine-cable-applications` and granted list `https://www.fcc.gov/submarine-cable-landing-licenses-granted`（verified）
- USAC FCC Form 499 forms: `https://www.usac.org/service-providers/resources/forms/` and FCC Form 499 filer database `https://apps.fcc.gov/cgb/form499/499a.cfm`（verified）

CNMI 属美国 telecom/FCC 体系；不要复述未经核实的“FCC 自 2009 年才取得 CNMI 电信管辖权”。2009 年是 CNMI immigration/border federalization 的关键节点，不是本方法论的数据中心监管锚点。

FCC/USAC 能证实：

- ULS / ASR：无线、微波、地球站、tower/antenna 设施位置。
- FCC/ICFS submarine cable：MICS、Atisa、未来 Proa/TPU/Interlink 等海缆的 landing authorization 与 landing points。
- Broadband Data Collection / Form 477：ISP 与覆盖枚举入口；不是数据中心证据。
- Form 499 / USAC：USF 申报人与服务商法人名录；不是设施证据。

查询模板：

```text
site:fcc.gov "Northern Mariana Islands" "cable landing"
site:fcc.gov "Saipan" "Tinian" "Rota" "Guam" "submarine cable"
site:fcc.gov "Atisa" OR "MICS" OR "Mariana-Guam Cable"
site:fcc.gov "Proa" "Northern Mariana Islands" "submarine cable"
site:apps.fcc.gov/cgb/form499 "IT&E" OR "DOCOMO PACIFIC" OR "PTI Pacifica"
"Northern Mariana Islands" "Broadband Data Collection" FCC provider
```

### 3.3 CUC 电力与公用事业

- Commonwealth Utilities Corporation: `https://www.cucgov.org/`（verified）
- CUC procurement/RFP search: use site search and document URLs under `https://www.cucgov.org/cuc_content/uploads/`
- Verified example: `CUC-RFP-25-021`, Independent Power Producer - Solar Photovoltaic with BESS for all islands (Saipan, Tinian, Rota), August 2025.
- U.S. DOE CNMI energy profile: `https://www.energy.gov/oe/commonwealth-northern-mariana-islands-cnmi`（verified；aging infrastructure / petroleum reliance context）

CUC records are required context for any claimed data center-scale load. A telecom/data center candidate on Saipan, Tinian, or Rota should be checked against CUC power plant, feeder, backup-generation and BESS/IPP material. CUC RFPs alone do not establish a data center.

查询模板：

```text
site:cucgov.org "data center" OR "critical load" OR "backup power" OR "generator"
site:cucgov.org RFP "Solar Photovoltaic" OR BESS OR "Independent Power Producer"
site:cucgov.org Saipan OR Tinian OR Rota "power plant" OR "transmission"
site:energy.gov/oe "Northern Mariana Islands" OR CNMI electricity infrastructure
"Commonwealth Utilities Corporation" "data center" OR "server room"
```

### 3.4 联邦采购与拨款

- SAM.gov: `https://sam.gov/`
- FPDS: `https://www.fpds.gov/`
- USASpending: `https://www.usaspending.gov/`
- Grants.gov: `https://www.grants.gov/`
- DOI OIA CNMI page: `https://www.doi.gov/oia/islands/cnmi`（verified）
- FEMA: `https://www.fema.gov/`
- NTIA BroadbandUSA: `https://broadbandusa.ntia.doc.gov/`
- GAO bid protests: `https://www.gao.gov/legal/bid-protests`

Use place of performance filters for MP / CNMI / Saipan / Tinian / Rota and NAICS filters:

- `518210` Computing Infrastructure Providers, Data Processing, Web Hosting, and Related Services
- `541513` Computer Facilities Management Services
- `541519` Other Computer Related Services
- `517111` Wired Telecommunications Carriers
- `237130` Power and Communication Line and Related Structures Construction
- `221122` Electric Power Distribution

查询模板：

```text
site:sam.gov "Northern Mariana Islands" "data center" OR hosting OR colocation
site:fpds.gov "Saipan" "518210" OR "541513" OR "data center"
site:usaspending.gov "Northern Mariana Islands" "broadband" OR "data center" OR "IT&E"
site:grants.gov CNMI BEAD OR broadband OR NTIA
"CNMI" "BEAD Final Proposal" "subgrant" "IT&E"
site:fema.gov CNMI "Yutu" OR "Soudelor" "generator" OR "communications"
```

### 3.5 海缆登陆站 Cable Landing

Verified base facts:

- FCC DA-97-522 grants GST Telecom authority for Mariana-Guam Cable / MICS, with landing points on Guam and Saipan, Tinian, Rota.
- FCC DA-22-762 states Atisa provides service to the same islands as MICS: Saipan, Tinian, Rota, and Guam.
- DoCoMo Pacific 2017 official release states FCC approved Atisa landing license, connecting Guam, Saipan, Rota, Tinian; it also references new cable landing stations in Rota and Tinian.
- NEC 2017 official release says ATISA was completed and connects CNMI to Guam.
- Google Cloud 2024 official blog says Proa will connect Japan, CNMI and Guam, and TPU will be extended to CNMI; this is planned/announced subsea connectivity, not a cloud region or data center.

查询模板：

```text
site:fcc.gov "SCL" "Atisa" "DOCOMO PACIFIC"
site:fcc.gov "MICS" "Saipan" "Tinian" "Rota"
site:docomopacific.com "ATISA" "cable landing"
site:nec.com "ATISA" submarine cable CNMI Guam
site:cloud.google.com/blog "Proa" "CNMI" "TPU"
site:fcc.gov "Proa" "CNMI" "cable landing"
```

### 3.6 云与 CDN 官方缺席核查

- AWS regions / AZs: `https://aws.amazon.com/about-aws/global-infrastructure/regions_az/` and docs list `https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html`
- Azure regions: `https://learn.microsoft.com/en-us/azure/reliability/regions-list`
- Google Cloud locations: `https://cloud.google.com/about/locations`
- Oracle OCI regions: `https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm`
- Cloudflare network: `https://www.cloudflare.com/network/`
- Akamai locations: `https://www.akamai.com/locations`

每次做时效性结论前重查官方页。若页面只把 Northern Mariana Islands 映射到某个服务区域（例如 billing/service availability geography），不能写成 CNMI data center / region。

## 4. Division Coverage / Municipality Buckets

| Manifest division | Municipality bucket | Official-first route | Output rule |
|---|---|---|---|
| Northern Mariana Islands | Saipan 塞班 | FCC/ICFS cable + ULS/ASR；BPD/BEAD；Governor/Legislature/OPA；CUC Saipan power maps；SAM/FPDS place-of-performance Saipan | 可记录 Atisa/MICS/未来 Proa landing、运营商 office/POP、政府/机构机房线索；只在有主证时建 `government_related_dc` 或 `commercial_colocation`。 |
| Northern Mariana Islands | Tinian 天宁 | FCC/ICFS cable + ULS；CUC Tinian power maps；SAM/FPDS Tinian；本地媒体仅补充 | 已有 cable landing / service 线索；默认无商业 DC。军事/机场基建只作背景，避免细节化。 |
| Northern Mariana Islands | Rota 罗塔 | FCC/ICFS cable + ULS；CUC Rota power maps；SAM/FPDS Rota；本地媒体仅补充 | 已有 cable landing / service 线索；默认无商业 DC。 |

Coverage is complete only after all three municipality buckets have search traces, but final records remain under the single manifest division `Northern Mariana Islands`.

## 5. 枚举规则 Enumeration Rules

1. 先跑 FCC/ICFS + BDC/Form 477 + USAC 499 建运营商和海缆骨架，再跑 BPD/BEAD、CUC、SAM/FPDS/USASpending 建政府/电力项目骨架。
2. 每个 physical facility 至少需要一条 A 级主证，或一条运营商官方产品页加一个独立位置证据。目录站单条不能建档。
3. Cable landing station、central office、gateway、FTTP headend、earth station 默认分类为 `operational_telecom`，除非来源明确给出 third-party colocation/hosting/data center/racks/power/cooling。
4. DoCoMo Pacific 官方 colocation 产品页是真实 A 级产品证据，但当前页面未给出 CNMI data center 地址；不能仅凭该页把 DoCoMo Saipan 写成已验证数据中心。
5. Google Pacific Connect / Proa / TPU / Interlink 是 subsea cable lead；不得作为 Google Cloud region、edge PoP 或数据中心证据。
6. 对 Saipan/Tinian/Rota 未找到主证的候选数据中心，输出 `no_projects: true` 或 `telecom_only: true`，保留查询、日期、source tier。
7. 关岛（Guam/GU）与 CNMI 运营商和海缆高度重叠；Guam data centers、landing stations、IXPs 只能作 upstream context，不计入 MP。

## 6. 噪音过滤 Noise Filters

```text
-casino -gambling -"Imperial Pacific" -"Tinian Dynasty" -hotel -resort -tourism -cruise
-Guam(仅在排除非CNMI设施时使用；海缆上游查询可保留 Guam)
-"Marianas Trench" -"Mariana Islands"(海洋/地理泛称) -NMI(歧义缩写)
```

优先锚词：`"Northern Mariana Islands"`、`CNMI`、`Saipan MP 96950`、`Tinian MP`、`Rota MP`、`Commonwealth of the Northern Mariana Islands`。

## 7. Verified Reference URLs

- Manifest checked locally: `world-manifest.jsonl`, MP entry as shown above.
- Governor: `https://governor.cnmi.gov/`
- Legislature: `https://cnmileg.net/`
- OPA reports: `https://www.opacnmi.com/document-category/opa-reports/`
- BPD BEAD documents: `https://bpd.cnmi.gov/about-us/b-e-a-d-documents/`
- CUC: `https://www.cucgov.org/`
- CUC RFP example: `https://www.cucgov.org/cuc_content/uploads/2025/09/CUC-RFP-25-021-2.pdf`
- DOI OIA CNMI: `https://www.doi.gov/oia/islands/cnmi`
- DOE OE CNMI energy: `https://www.energy.gov/oe/commonwealth-northern-mariana-islands-cnmi`
- FCC Form 477 deployment data: `https://www.fcc.gov/general/broadband-deployment-data-fcc-form-477`
- FCC Form 477 resources: `https://www.fcc.gov/economics-analytics/industry-analysis-division/form-477-resources`
- FCC submarine cable landing guide: `https://www.fcc.gov/research-reports/guides/submarine-cable-landing-licenses`
- FCC DA-97-522 Mariana-Guam Cable: `https://docs.fcc.gov/public/attachments/DA-97-522A1.pdf`
- FCC DA-22-762 MICS/Atisa: `https://docs.fcc.gov/public/attachments/DA-22-762A1.pdf`
- USAC forms: `https://www.usac.org/service-providers/resources/forms/`
- DoCoMo Pacific Atisa release: `https://aboutus.docomopacific.com/144040-docomo-pacific-announces-grant-of-fcc-license-for-atisa-cable-system/`
- NEC ATISA release: `https://www.nec.com/en/press/201706/global_20170622_01.html`
- Google Cloud Pacific Connect: `https://cloud.google.com/blog/products/infrastructure/pacific-connect-initiative-to-expand`
- AWS global infrastructure: `https://aws.amazon.com/about-aws/global-infrastructure/regions_az/`
- Azure regions: `https://learn.microsoft.com/en-us/azure/reliability/regions-list`
- Google Cloud locations: `https://cloud.google.com/about/locations`
- Oracle OCI regions: `https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm`
