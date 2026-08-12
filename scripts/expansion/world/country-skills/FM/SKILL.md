---
name: fm-datacenter-methodology
location: scripts/expansion/world/country-skills/FM/SKILL.md
description: 密克罗尼西亚联邦（FSM/Micronesia）数据中心发现与审计方法论：官方/监管/云管线（TRA 电信监管局执照登记册、FSM 国家/州政府与 Digital FSM、FSMTC、FSMTCC/CableCorp/OAE、World Bank P170718、FCC/美国政府、云厂商官方区域列表）叠加行业/厂商发现（运营商、批发海缆运营商、卫星提供商、贸易媒体、对等/网络目录）；以清单中的 4 个州（Kosrae、Pohnpei、Chuuk、Yap）为划分粒度，设施先分类再定级。运行 FM 探索/审计批次前必读；路由到 explorer-official.md 与 explorer-industry.md。Bilingual discovery & audit methodology for the Federated States of Micronesia datacenters: official/regulatory/cloud pipeline + industry/vendor discovery, at the 4 state division granularity from the manifest; read before running FM exploration/audit batches; routes to explorer-official.md and explorer-industry.md.
---

# FM · 密克罗尼西亚联邦数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> **目的**：FSM 无官方来源证实存在在运营的商业托管或超大规模数据中心——按非常小的电信与政府数字基础设施市场枚举。最高置信设施宇宙为 A 级运营电信设施（Pohnpei 的 FSMTC 国际网关/海缆登陆设施；服务 Pohnpei、Chuuk、Yap、Kosrae 的 FSMTCC/CableCorp 海缆与 FTTP 交换局/中心局设施；Yap 的 iBoom/Boom 网络设施；Chuuk 持牌的 CPUC/iSolutions 设施）与 A 级规划/项目数据中心线索（Digital FSM 政府数据中心/FSM-Cloud 组件；World Bank P170718 目标到 2027-03 由私营运营绿色数据中心托管的 3 项新数字服务）。运行任何 FM 探索/审计批次前必须阅读本 skill，并按需路由到两份探索报告。

## 入口（Entry points）

| 文件 | 管线 | 内容 |
|---|---|---|
| explorer-official.md | 官方/监管/云管线 | TRA 执照登记册/瓶颈设施裁定、FSM 政府/DTCI/DFO/DoFA（Digital FSM ESMP）、FSMTC、FSMTCC/CableCorp/OAE、World Bank P130592/P170718 与捐赠方（AIFFP/NEC/EMC）、FCC/美国政府、云厂商官方缺席检查、四州官方工作流与枚举规则 |
| explorer-industry.md | 行业/厂商发现 | 运营商与厂商线索（FSMTC、FSMTCC/OAE、iBoom、卫星/无线提供商表）、超大规模/CDN 缺席、贸易媒体与目录、四州行业工作流、设施分类（operational_telecom / planned_telecom_colocation / planned_government_dc / planned_private_green_dc / no_projects）、监视列表 |

## 核心结构事实（框定每次搜索）

1. **划分模型**：清单要求覆盖 **4 个州**：**Kosrae、Pohnpei、Chuuk、Yap**。搜索锚定 "Federated States of Micronesia"、"FSM" 与州名；"Micronesia" 常指更广地区——噪音过滤器如 `-ship -vessel -registry -Guam -Palau -Saipan -Marshall -Kiribati -Nauru`。
2. **核心设施宇宙**：FSMTC（老牌零售运营商，Kolonia Pohnpei 总部；TRA 执照 IL-001 授权陆地/无线电/海缆与登陆站/国际网关设施；2021 完成 HANTRU-1 Pohnpei–Guam 升级；Chuuk–Pohnpei 海缆故障公告证实对 C-P 海缆与 FSMTCC/OAE 维护窗口的运营依赖）；FSMTCC/CableCorp（= OAE，政府所有的开放接入/批发实体，总部 Ocean View Plaza (East Wing) Suite 15, Pohnpei；执照 IL-002；OAE 批发材料明确设计中心局/交换局的托管空间、电力与制冷及未来托管/回程产品——**在现行资费/服务订单确认前按 planned_telecom_colocation 处理**）；iBoom/Boom（Yap，P.O. Box 215, Colonia Yap；授权陆地海缆、国际网关、卫星地面站；无线频谱——电信设施线索，非托管）；CPUC/iSolutions（Chuuk/Weno 持牌电信）；Kacific、MCS Pohnpei、Starlink Pacific Islands LLC（运营执照 2024-03-19 生效）、FSMtech（连接性线索）。
3. **关键机构**：TRA（telecom regulator，tra.fm；**无数据中心执照类别**——Individual Operating License / Class Operating License / Spectrum-Frequency License；公共执照登记册；瓶颈设施裁定：至 Pohnpei/Yap/Chuuk 的海缆 + Pohnpei/Weno/Yap Proper 的 FTTP；CableCorp 在建四州主岛开放接入 FTTP 并含托管附属服务）、FSM 政府/DTCI/DFO/DoFA（gov.fm、tci.gov.fm、dfo.gov.fm、dofa.gov.fm）、World Bank（FSM 连接项目 P130592；Digital FSM P170718，US$30.8M，IDA-D5560 + 增资 IDA-E5020，2027 修订关闭；目标 3 项绿色数据中心托管数字服务）、AIFFP/NEC（EMC 约 2,250 km 连接 Tarawa/Nauru/Kosrae/Pohnpei；NEC 2026-05-15 完工移交 FSMTCC/BNL/Cenpac）、FCC（HANTRU-1 DA-09-1309A1）。
4. **查询语言与拼写**：英语为主；"data center" / "data centre" / "datacenter" / "server room" / "cable landing station" / "international gateway" / "central office" / "colocation"；州名 + "Federated States of Micronesia"；不要用 "Micronesia" 单字（区域歧义）。
5. **容量语义**：无在运营商业 DC 容量可记录；OAE 托管为批发电信托管（中心局/交换局）直至现行资费/服务订单/运营手册确认；Digital FSM/FSM-Cloud 与绿色数据中心为项目线索直至采购/中标/调试文件点名位置/运营方；`no_projects: true` 用于仅有连接性服务或无从查证机房推断的州，并保留搜索轨迹。
6. **海缆/网关/中心局不是数据中心**：登陆站、网关、中心局、FTTP 头端、卫星地面站按 operational_telecom 分类，除非来源明确提供托管/主机/数据中心/服务器托管服务（CableCorp/OAE 例外为设计中的批发托管产品）。EMC 登陆站存放光传输与馈电设备——电信证据。
7. **云/CDN 缺席**：AWS/Azure/GCP/OCI 官方区域页无 FM 区域；Cloudflare/Akamai 网络页无 FM PoP；不从全球服务可用性、DNS、延迟测试或客户路由推断 PoP；经销商可用性页不作云区域证据。
8. **可靠度分级**：A = TRA 官方页/登记册/裁定、FSM 国家/州政府页与项目文件、FSMTC 官方页、FSMTCC/CableCorp 官方页与 PDF、World Bank 项目文件、FCC/美国政府记录、云厂商官方区域页、州公用事业官方记录；B = 具名当事方/日期的捐赠方/项目/行业来源（AIFFP、EMC 项目站、NEC 公告、Submarine Networks、DCD、RNZ Pacific、Pacific Island Times、APNIC）；C = 目录、社交（除非为运营方自家页）、LinkedIn、经销商/托管列表、论坛、营销页、从企业 IT 招聘帖推断。分级针对具体主张而非域名。
9. **降级纪律**："communications facility"、"gateway"、"earth station"、"central office" 除非来源说托管/主机/数据中心/云/机架/为第三方设备供电制冷等设施语言，否则不是数据中心；Starlink/Kacific/VSAT 终端、移动基站、FTTP 推广、零售互联网服务一律不计为数据中心；未证实美国军方/联邦 FSM 数据中心。

## 常用查询模板（详见 explorer-official.md / explorer-industry.md）

```text
site:tra.fm "data center" "Micronesia"
site:tra.fm colocation OR "co-location" CableCorp
site:tra.fm "Public Register of Licences" FSMTC FSMTCC Starlink iBoom iSolutions
site:tra.fm "bottleneck facilities" "Pohnpei" "Weno" "Yap"
site:gov.fm "data center" OR "FSM-Cloud" OR "server"
site:tci.gov.fm "Secure Government Network" "Data Center"
site:dofa.gov.fm "Digital FSM Project" "data center" OR "green data centers"
site:fsmtc.fm "data center" OR "server" OR "hosting" OR "colocation"
site:fsmtc.fm HANTRU OR "Pohnpei and Guam"
site:fsmcable.com colocation OR "co-location" OR "central office" OR exchange
site:fsmcable.com "landing station" "Pohnpei" OR "Chuuk" OR "Yap" OR "Kosrae"
site:worldbank.org Micronesia "P170718" "green data centers"
"{State}" "Federated States of Micronesia" "data center" OR "data centre" OR "server room"
"{State}" "FSMTCC" OR "CableCorp" OR "OAE" "landing station" OR "central office"
"Federated States of Micronesia" "data center" OR "datacenter" OR colocation -ship -registry
site:aws.amazon.com OR site:docs.aws.amazon.com "Micronesia" "region" "AWS"   # 云缺席
site:cloudflare.com/network "Micronesia" OR "Pohnpei"   # CDN 缺席
site:dofa.gov.fm "green data centers" OR "FSM-Cloud" OR "data center"   # 监视列表
```

## 官方/监管管线要点（详见 explorer-official.md）

- TRA：先查公共执照登记册与市场进入页识别持牌运营商与允许设施类型；FSMTC IL-001、FSMTCC IL-002、Boom! Inc. 授权；Kacific/CPUC/Starlink/iSolutions/MCS/FSMtech 为连接性线索。注意：TRA 菜单中的 "S-band spectrum" 链接解析到账号暂停页——勿引用；Starlink 执照信息用登记册。
- 政府：Digital FSM 含 Secure Government Network and Data Center、DR/BC 与 FSM-Cloud 组件——官方证据表明政府数据中心/政府云工作流存在，但在实施记录点名站点/运营方前不是公共托管设施；州政府页面仅用于分配可能设施/办公室，普通 IT 办公室不升级。
- 海缆时间线：Pohnpei 有 HANTRU-1 与 C-P 海缆 Pohnpei 侧登陆；Chuuk 的 C-P 海缆 2019-04-27 运营、有 Chuuk 登陆站；Yap 到 SEA-US 的支线 2018 年 6 月底服役；Kosrae 经 EMC 2026 完工移交。
- 云缺席：仅用官方供应商区域页记录缺席。

## 行业/厂商发现要点（详见 explorer-industry.md）

- FSMTC：PeeringDB（org/36890）仅 C/B 路由上下文，不得单独作为设施来源；"Dedicated Internet Access"、域名、邮件/网页托管目录条目为服务线索非数据中心证据；未发现 FSMTC 公共托管产品。
- FSMTCC/OAE：批发/开放接入实体；"colocation" 作为交换局/中心局的批发电信托管，直至现行资费或服务订单确认可用。
- iBoom：Yap 的 ISP/移动竞争者，无已核实数据中心/托管产品。
- 目录规则：DataCenterMap/Cloudscene 缺席仅是弱负向信号；WHTop/托管目录条目为 C 级且通常识别网页托管品牌而非物理 DC。
- 监视列表：dofa.gov.fm 绿色数据中心/FSM-Cloud、tci.gov.fm FSM-Cloud/Secure Government Network/Data Center、fsmcable.com 托管产品/运营手册、tra.fm 新基础设施通知、"East Micronesia Cable System" RFS；未来结果点名私营运营方/站点/资费/机架功率规格/调试日期时，仅凭一手证据提升并归属到四州之一。

## 维护注意（更新纪律）

- **更新节奏**：每次刷新重查 AWS/Azure/GCP/OCI/Cloudflare/Akamai 官方页、TRA 登记册、FSMTC/FSMTCC 官方页、World Bank P170718 状态材料、NEC/AIFFP/EMC 公告；监视 CableCorp/OAE 托管上线、Digital FSM/FSM-Cloud 采购或调试记录、任何 P170718 项下具名私营绿色数据中心。
- **来源核验**：TRA S-band 链接已失效勿用；EMC 项目页说登陆站存光传输与馈电设备——电信证据；World Bank 目标（2027-03 前 3 项绿色数据中心托管服务）是项目目标非在运营设施清单。
- **不删除纪律**：无法核实的旧线索保留为降级线索并注明缺失证据；每条设施记录先分类（operational_telecom / planned_telecom_colocation / planned_government_dc / planned_private_green_dc / no_projects）再定级，物理电信设施与 FSMTC/FSMTCC 一手记录、世行/捐赠方记录、FCC 记录或州公用事业/政府记录交叉核对。
