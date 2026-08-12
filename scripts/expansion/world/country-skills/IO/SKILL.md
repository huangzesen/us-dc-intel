---
name: io-datacenter-methodology
location: scripts/expansion/world/country-skills/IO/SKILL.md
description: 英属印度洋领地（BIOT）数据中心双线查询方法论——预期产出为 0（军事/基地通信与 .io TLD 均排除）；British Indian Ocean Territory datacenter dual-line methodology with expected yield 0 (military/base communications and .io TLD excluded). 运行 IO 探索/审计批次前必读；路由到 explorer-official.md 与 explorer-industry.md。
---

# IO · 英属印度洋领地数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：英属印度洋领地（British Indian Ocean Territory / BIOT, IO）是封闭的军事领地，本方法的目标不是“找设施”，而是用官方与行业双侧负向证据确认“无可入清单的商业设施”。官方线（explorer-official.md）覆盖领地行政、访问限制、军事边界与云区域负核；行业线（explorer-industry.md）覆盖媒体/目录/海缆/承包商负向核验与误判排除。任何“正结果”必须升级到 A 级来源才可进入候选。

## 入口

| 文件 | 职责 | 内容概要 |
|---|---|---|
| explorer-official.md | 官方/监管/云管线 | GOV.UK BIOT 页、BIOT Administration（biot.gov.io）、FCDO travel advice、legislation.gov.uk、UK/Mauritius treaty 页、U.S. Navy NSF Diego Garcia 页、云厂商官方区域负表（AWS/Azure/GCP/OCI）、`.io` ccTLD IANA 排除、海缆/IXP/公用事业负核 |
| explorer-industry.md | 行业/厂商/媒体发现 | 行业媒体（DCD、Reuters/AP/BBC、TeleGeography/Submarine Cable Map、Capacity、Light Reading、SubTel Forum）、聚合器与目录（Data Center Map、datacenters.com、Cloudscene、PeeringDB、IXPDB、Internet Exchange Map）、云/CDN/边缘负核、海缆军事连接性背景、基地承包商/国防 IT 排除、`.io` TLD 误判过滤 |

## 核心结构事实

1. **Division 模型**：manifest 已核验 `country_code="IO"`，`subnational_type: country`，`divisions: ["British Indian Ocean Territory"]`。IO 在清单模型中只按整个领地枚举，不拆分环礁或岛礁；公开有人活动集中在 Diego Garcia 迪戈加西亚的英美军事基地。
2. **官方结论（2026-08-12 最终来源核验）**：预期商业数据中心产出 = 0。IO 没有可公开枚举的商业 colocation、批发数据中心、云区域或民用托管市场；核验目标是确认“没有可入清单设施”。
3. **政治与法律**：BIOT 是英国海外领地，从伦敦管理、无永久人口、无本地正式外交/领事存在；BIOTA 由英国正式管理，Commissioner 由国王任命，Administrator 管日常事务，Brit Rep 在 Diego Garcia 代表行政机构；BIOT 有独立电信监管职责（治理事实，A 级），但不得误写为民用电信市场或 DC 许可框架。UK/Mauritius 关于 Chagos Archipelago（含 Diego Garcia）的条约 2025-05-22 提交英国议会，生效前 BIOT 仍按当前官方结构处理；主权变化不得直接解释为商业 DC 市场。
4. **访问限制**：BIOT 不是旅游目的地，进入受限、需许可、无商业航班；Diego Garcia 仅限与军事设施或领地行政相关人员进入。这是“无商业 DC 市场”的核心 A 级证据。
5. **军事边界**：U.S. Navy NSF Diego Garcia 官方页将该设施定位为印度洋/波斯湾前沿部署部队提供后勤支持；基地 IT、通信、电力、网络机房、卫星/海缆接入、承包商 IT 设施均属国防基础设施，不进入商业 DC 清单；只有公开 A 级来源明确表示某设施面向公众销售 colocation/hosting/cloud 服务才可转候选（当前预期无）。
6. **云区域为负**：AWS、Azure、Google Cloud、Oracle OCI 官方区域列表均无 IO/Diego Garcia 区域或 Local Zone；最近商业区域在印度、新加坡、南非、澳大利亚/中东方向；DoD/government 服务模型不是本地 IO 设施。
7. **`.io` ccTLD 排除**：`.io` 域名使用量、注册商生态、DNS/CDN/域名业务与领地本地基础设施无关；IANA `.io` root DB 只用于确认 ccTLD 委托；搜索到 `*.io`、startup、registrar、GoDaddy/Identity Digital/ICB 等内容标记为 TLD 背景，不得入设施候选；若商业 DC 公司使用 `.io` 域名，按其真实国家/设施地址枚举，不归入 IO。
8. **海缆/IXP/公用事业**：行业报道显示 Diego Garcia 存在与 Oman Australia Cable (OAC) 相关的秘密/军事用途支线（DCD 2023 等），这加强的是“军事通信基础设施存在”，不是商业登陆站、IXP 或 DC 市场；军事专用或未公开商业接入的一律不计为商业 DC 或 IXP；无民用电网/地产/客户市场，基地电力和通信不作公共 utility 市场处理。
9. **可靠性分级**：A = 官方/一级来源（政府、监管机构、法律文本、军方官方页、云厂商官方区域页、运营商自有设施页）；B = 强二级来源（可靠媒体、行业媒体、PeeringDB/TeleGeography/ISOC 等目录或研究）；C = 弱线索（聚合器、市场页、转售商、地址推断）；U = 未证实传闻，仅作搜索提示。
10. **计数与去重规则**：B/C/U 只能做线索；异常结果按序处理——①是否只是 `.io` TLD？是则排除 ②是否军事/基地通信？是则排除 ③是否只有聚合器/SEO 页面？无 A 级来源则丢弃 ④是否有运营商自有页面、云厂商区域页、政府许可/公告？若有转入人工复核并同步更新 explorer-official.md。产出记录写明：`0 commercial datacenter facilities; military/base communications excluded from public commercial inventory; .io TLD false positives excluded`。

## 常用查询模板

```text
site:gov.uk/world/british-indian-ocean-territory ("data centre" OR "data center" OR cloud OR colocation)
site:biot.gov.io ("data centre" OR "data center" OR cloud OR colocation OR "telecoms regulator")
site:legislation.gov.uk "British Indian Ocean Territory" ("telecommunications" OR "data" OR "company")
site:gov.uk "Diego Garcia" "military base"
site:cnrj.cnic.navy.mil/Installations/NSF-Diego-Garcia ("data center" OR "communications" OR "mission")
"British Indian Ocean Territory" ("data centre" OR "data center" OR datacenter OR colocation OR "cloud region")
"Diego Garcia" ("commercial data center" OR colocation OR "cloud region" OR IXP)
"Diego Garcia" "submarine cable" "data center"
site:submarinecablemap.com "Diego Garcia"
site:datacenterdynamics.com "Diego Garcia" "Oman Australia Cable"
site:datacentermap.com "Diego Garcia"
site:peeringdb.com "Diego Garcia"
site:ixpdb.euro-ix.net "British Indian Ocean Territory" OR "Diego Garcia"
"AWS" "British Indian Ocean Territory" "region"
"Azure" "Diego Garcia" "region"
"Google Cloud" "British Indian Ocean Territory" "location"
"OCI" "Diego Garcia" "cloud region"
"NSF Diego Garcia" ("IT" OR "communications" OR "network operations" OR "telecommunications")
site:sam.gov "Diego Garcia" ("IT" OR "communications" OR "network")
".io" "data center"
"Identity Digital" ".io"
site:iana.org/domains/root/db/io.html
```

## 官方/监管管线要点（详见 explorer-official.md）

- **领地行政与法律**：GOV.UK BIOT 页（gov.uk/world/british-indian-ocean-territory/news）确认“从伦敦管理、无永久人口”；BIOT Administration（biot.gov.io）管治理/访问许可/法律 Gazette/科学渔业许可；Governance 页列 Commissioner/Administrator/Brit Rep/BIOT Police/Customs/Immigration/独立电信监管者；legislation.gov.uk 检索 `British Indian Ocean Territory Constitution Order` 与相关 Ordinances。
- **主权安排监控**：UK/Mauritius treaty 页（gov.uk/government/publications/ukmauritius-agreement-concerning-the-chagos-archipelago-including-diego-garcia-cs-mauritius-no12025）用于监控变更；条约生效才会改变领地状态，不得用政治新闻推断 DC 市场。
- **访问限制核验**：site:biot.gov.io/visiting 与 site:gov.uk/foreign-travel-advice/british-indian-ocean-territory 查 access restricted/permit/commercial flights；预期：访问受限、无商业航班、Diego Garcia 仅限军事/行政相关进入。
- **军事边界**：site:cnrj.cnic.navy.mil/Installations/NSF-Diego-Garcia 查 mission/logistic support；官方军页面可作“基地存在/任务性质”证据；不枚举基地内 server room、通信节点、NOC、机房、卫星/海缆接入、承包商 IT 设施。
- **云区域负表**：每轮重跑 AWS（docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html + localzones）、Azure（learn.microsoft.com/en-us/azure/reliability/regions-list）、GCP（cloud.google.com/about/locations）、OCI（oracle.com/cloud/public-cloud-regions）并记录日期；官方页面优先，市场博客不能证明区域存在。
- **`.io` TLD 排除**：IANA `.io` root DB 确认 ccTLD 委托；域名注册和注册局运营不代表 BIOT 境内基础设施。
- **海缆/IXP/公用事业**：`"Diego Garcia" "submarine cable"`、`"British Indian Ocean Territory" IXP` 等检索；公开图或行业报道若显示 Diego Garcia landing/spur，先判断是否服务军方/基地——军事专用或未公开商业接入的一律不计为商业 DC 或 IXP。
- **检查员清单**：①确认 manifest 仍为 IO/country/[British Indian Ocean Territory] ②打开 GOV.UK BIOT、BIOT governance/visiting、FCDO、NSF Diego Garcia 页记录日期 ③检查 treaty/UK law 页（生效则更新命名与治理部分，仍不得将主权变化直接解释为商业 DC 市场）④重跑 cloud-region 负表 ⑤重跑 `.io` 排除与海缆/IXP 检索，OAC/Diego Garcia spur 类报道标注 military connectivity, excluded ⑥与 explorer-industry.md 目录/聚合器/贸易媒体/承包商检索交叉核对 ⑦发现商业正信号必须取得 A 级来源 ⑧产出记录写明 0。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **行业媒体与新闻**：DCD（查 Diego Garcia/BIOT/OAC，2023 报道为军事海缆支线背景，不是商业 DC）、Reuters/AP/BBC（主权与军事基地新闻，政治/军事背景不直接构成设施证据）、TeleGeography/Submarine Cable Map（海缆与 landing-point 背景，需区分商业系统与军事/未公开支线）、Capacity Media/Light Reading/SubTel Forum（连接性补充）、国防行业媒体（国防合同和基地支持线索，只作 exclusion 背景）。行业媒体只要没有明确商业运营商、商业服务、设施地址/客户市场，就不得入候选。
- **聚合器与目录**：Data Center Map、datacenters.com、Cloudscene 预期无 IO 商业设施；出现条目按 C 处理、需 A 级复核否则丢弃；PeeringDB 预期无 Diego Garcia/BIOT public facility 或 IXP（B/C 负证据，网络对象不等于 DC）；IXPDB/Euro-IX 与 Internet Exchange Map 无 IO IXP（无结果支持 0 结论）；RIPE/APNIC/ARIN DB 对象可能与军方、TLD、研究或远程地址相关，不证明设施。
- **云/CDN/边缘负核**：无全球云厂商在 IO 设公开商业 region/zone/local zone/edge market；Cloudflare/Akamai CDN edge 官方网络页 + PeeringDB 预期无公开 IO PoP，任何 Diego Garcia 军事服务排除；不用销售覆盖、合作伙伴、`.io` 客户、军事/政府云合同推断本地设施。
- **连接性与海缆**：OAC 通往 Diego Garcia 美海军基地的密秘支线报道价值在于说明 military communications exist，不是商业 landing station、IXP 或数据中心；任何 OAC/Diego Garcia、US Pacific Fleet、Pentagon、SubCom、Big Wave、base communications 结果都标记为军事连接性背景；Cable landing station 也不自动等于数据中心。
- **基地承包商与国防 IT**：基地支持合同可能出现 IT、communications、network operations、data、telecom、fiber、power、facility maintenance 关键词——这是 exclusion search，不是设施发现；合同/招聘/承包商案例只能证明基地有 IT/通信需求；不记录承包商 office、network room、communications facility、power plant、satellite terminal、fiber landing 为商业 DC；若承包商声称提供 data center operations，仍需确认是否公开商业服务，基地内国防运维仍排除。
- **负向核验汇总**：每次更新 IO 清单前完整跑负向查询包并保存检索日期和异常结果；异常按 ①`.io` TLD ②军事/基地通信 ③无 A 级来源的聚合器 ④有运营商/云厂商/政府 A 级来源（转人工复核并更新 explorer-official.md）四步处理。
- **最终产出**：`0 commercial datacenter facilities; military/base communications excluded; .io TLD false positives excluded`。

## 维护注意（更新纪律）

- **更新节奏**：每次更新 IO 清单前重跑负向查询包与云区域负表，记录检索日期和异常结果；主权/条约变更触发的是治理刷新，不是自动的市场假设。
- **来源核验**：任何商业正信号必须补齐：设施运营商、物理地点、商业服务类型、官方/运营商来源、division=`British Indian Ocean Territory`；B/C/U 只能做线索。
- **不删除纪律**：本目录只新增/更新 SKILL.md、ANATOMY.md 与探索产物，禁止删除/移动任何现有文件（explorer-official.md、explorer-industry.md 与历史证据保留为原始记录）。
