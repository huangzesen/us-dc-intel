---
name: by-datacenter-methodology
location: scripts/expansion/world/country-skills/BY/SKILL.md
description: |
  Belarus（BY）数据中心发现以官方/监管管线（pravo.by 法律门户、NCPDP 数据保护机构、Minsvyazi/BelGIE、EGR 法人登记、goszakupki.by 采购、gse.by 国家建设鉴定、州/市行政委员会门户）和运营商一手证据（Beltelecom、beCloud RCOD、A1 Digital、MTS Cloud、NTSEU、Datahata）为主线，按 7 个行政区划（Brest; Gomel; Grodno; Minsk; Minsk City; Mogilev; Vitebsk）逐区枚举。
  全部已核实公开商业设施集中在 Minsk City 与 Minsk Oblast（beCloud RCOD 位于 Kolodishchi）；其余州区需做显式负向扫描，FEZ/NPP 电网叙事仅作选址线索；俄语/白俄罗斯语查询为本地发现主力。
---

# BY · 白俄罗斯数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：按 7 个行政区划（Brest; Gomel; Grodno; Minsk; Minsk City; Mogilev; Vitebsk）枚举白俄罗斯数据中心设施与项目。
> 分区模型：6 个州（Brest、Gomel、Grodno、Mogilev、Minsk、Vitebsk）＋享有州级地位的 Minsk City，即 world-manifest 所需 7 分区；实操搜索必须下沉到州执行委员会/市与区执行委员会层面，无全国统一建设许可门户。
> 已知种子：Beltelecom（datacenter.by）、beCloud RCOD（Kolodishchi, Tsentralnaya 22）、A1 Digital（Tier III 级）、MTS Cloud、NTSEU 国家云、Datahata、BY-IX。
> 本 skill 汇总两份探索报告：官方/监管管线见 explorer-official.md，行业/厂商发现见 explorer-industry.md。

## 入口

| 文件 | 管线 |
|---|---|
| explorer-official.md | 官方/监管管线：法律与监管（pravo.by、NCPDP、电信/信息法、数字经济发展令）、ICT/网络与国有 IT 机构（Minsvyazi、BelGIE、OAC、NTSEU、beCloud）、运营商一手证据、登记/地籍/规划/采购（EGR、NCA、gse.by、goszakupki.by、BUTB）、能源与选址（Minenergo、Belenergo、州电力公司、Astravets NPP）、州/市门户、投资与 FEZ（investinbelarus.by、HTP）、公有云区域核对 |
| explorer-industry.md | 行业/厂商发现：市场框架（Minsk-first、国有主导）、俄语/白俄语/英语检索词表、行业与贸易源（datacenter.by、becloud.by、a1digital.by、cloud.mts.by、nces.by、Onliner、OfficeLife、BELTA、ComNews、TAdviser、PeeringDB）、目录聚合器（DataCenterMap、Datacenters.com、Baxtel、DC-Union）、运营商与项目种子、IXP/连通性、政府/银行/封闭部门线索、全国查询扫掠、分区发现策略 |

## 核心结构事实（框定每次搜索）

1. 白俄罗斯是小型、Minsk-first、国家影响深重的市场：全部已核实公开商业/运营商设施集中在 Minsk City 与 Minsk Oblast，beCloud RCOD 是唯一已验证的旗舰实体设施（Minsk 区 Kolodishchi, Tsentralnaya 22）；Brest/Gomel/Grodno/Mogilev/Vitebsk 本轮未发现已核实公开商业设施，仍需显式负向扫描。
2. 无公共数据中心登记册、无全国开放建设许可库；建设许可/用地决定/公用设施接入/公告通常经州执行委员会和市/区执行委员会而非全国门户发布（official）。
3. 白俄罗斯为内陆国：海缆登陆站搜索为假阳性；连通性仅用陆路光缆、Beltelecom 国际网络与 BY-IX 作为互连背景，IXP 不算数据中心（除非另有设施/机柜声明）。
4. 俄语是发现主力语言（ЦОД / центр обработки данных / дата-центр / колокация / серверная），白俄罗斯语为次要词表；`ЦОД` 常指普通机房、部委 IT 部门、银行处理中心或软件平台，须有设施/托管/云/电信基础设施/建设证据才计数。
5. 2021-2022 年以来的制裁使西方超大规模新投资可能性低；不要用制裁评论作为设施证据。官方 AWS/Azure/GCP/OCI 全球基础设施页本轮均未列出白俄罗斯公有云区域或本地区（A 级仅证官方清单缺席）。
6. 记录字段含 UNP（法人统一登记号）、raion、power_connection_kv、tier_or_certification 等；状态标签 operational / tenant footprint / construction / planned / siting lead / unknown-historical / not datacenter；分级按所支持事实的来源（A 官方/运营商一手；B 商业/行业新闻与 PeeringDB；C 目录/聚合器/旧镜像；U 未决线索）。

## 查询模式（复制粘贴模板见 explorer-official.md §3 / explorer-industry.md §6）

- 俄语核心：`"центр обработки данных" Беларусь`、`"ЦОД" Беларусь Минск`、`"дата-центр" Беларусь`、`"колокация" Минск`、`"размещение оборудования" "ЦОД" Беларусь`、`"серверная" "разрешение на строительство" Беларусь`、`"ЦОД" "госэкспертиза" Беларусь`、`"ЦОД" "трансформаторная подстанция"`、`"облачная платформа" Беларусь`、`"Республиканский центр обработки данных"`、`"точка обмена трафиком" Минск`。
- 白俄罗斯语：`"цэнтр апрацоўкі дадзеных"`、`"дата-цэнтр" Мінск`、`"калакацыя"`。
- 官方/采购（分开跑，勿依赖单个 OR 行）：`site:goszakupki.by ЦОД`、`site:goszakupki.by дата-центр`、`site:goszakupki.by серверная`、`site:zakupki.butb.by ЦОД`、`site:gse.by ЦОД`、`site:mpt.gov.by ЦОД`、`filetype:pdf ЦОД строительство Беларусь`。
- 英文：`"Belarus" "data center"`、`"Belarus" "data centre"`、`"Minsk" "data center" "Tier III"`、`"Beltelecom" "data center"`、`"beCloud" "RCOD" Kolodishchi`、`"A1 Digital" "data center" Minsk`、`"MTS Cloud" "data center" Minsk`、`"Belarus" "internet exchange" BY-IX`。
- 能源：`технологическое присоединение ЦОД`、`присоединение к электросетям дата-центр`、`трансформаторная подстанция ЦОД`、`резервное питание ИБП дата-центр`、`дизельные генераторы ЦОД`、`10 кВ ЦОД`、`выделенная мощность дата-центр`。
- 已知算子核对：`site:beltelecom.by ЦОД`、`site:datacenter.by размещение оборудования`、`"Республиканский центр обработки данных" beCloud`、`beCloud Колодищи Центральная 22`、`A1 Digital дата-центр Минск`、`МТС Cloud "78 серверных стоек"`、`МТС Cloud "два дата-центра"`、`"НЦЭУ" "облачное хранилище"`、`BY-IX Минск PeeringDB`。
- 分区扫掠（每州）：`"{city}" "ЦОД"`、`"{city}" "дата-центр"`、`"{city}" "серверная"`、`"{city}" "колокация"`、`site:goszakupki.by "{city}" ЦОД`、`site:gse.by "{city}" ЦОД`、`site:{oblast-portal} ЦОД`，外加 `"Островец" "ЦОД"`、`"БелАЭС" "дата-центр"`、`"Новополоцк" "дата-центр"`、`"Могилёв" "ЦОД"`（见 official §4 / industry §7）。

## 官方/监管管线要点（详见 explorer-official.md）

- 法律与监管：国家法律互联网门户 pravo.by（精确 regnum/guid 链接优先）；个人数据法 2021-05-07 No. 99-Z 于 2021-11-15 生效；数据保护机构为国家个人数据保护中心 NCPDP（cpd.by，勿用 pdp.by 假设域名）；电信法为 2005 No. 45-Z（429-Z 是错误引用）；信息法 2008 No. 455-Z；数字经济发展总统令 No. 8（2017-12-21）；HTP 创始总统令 No. 12（2005-09-22）；国家计划《数字发展 2021-2025》与《数字白俄罗斯 2026-2030》。
- ICT/网络安全与国有 IT：Minsvyazi（mpt.gov.by）、BelGIE（belgie.by，电信监管与信息系统登记语境，非设施登记册）、OAC（oac.gov.by，信息安全监管）、NTSEU（nces.by，国家电子政务/云存储平台，非商业托管）、beCloud（becloud.by，RCOD 运营商）。
- 登记/地籍/规划/采购：EGR 法人登记（egr.gov.by）、国家地籍局 NCA 与公共地籍图 map.nca.by、国家建设鉴定 gse.by / mygse.by、建设部 masa.gov.by、官方采购门户 goszakupki.by（含全部采购列表）、BUTB 采购平台 zakupki.by 商业监测仅作 C 级线索。
- 能源与选址：Minenergo、Belenergo、六州电力公司（Brestenergo、Vitebskenergo、Gomelenergo、Grodnoenergo、Minskenergo、Mogilevenergo）；Astravets NPP（belaes.by）仅作电力语境，不作数据中心证据。
- 州/市门户与投资：各州/市执行委员会门户（Minsk City 预期收益最高，minsk.gov.by 本轮曾 503）；investinbelarus.by 投资地图/项目库；HTP park.by；六个 FEZ（Brest、Gomel-Raton、Grodnoinvest、Minsk、Mogilev、Vitebsk）仅作选址线索。
- 公有云核对：AWS/Azure/GCP/OCI 官方区域页年度复查，本轮白俄罗斯无公有云区域/本地区。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 运营商锚点：Beltelecom 商用数据中心/托管（datacenter.by、beltelecom.by/business/hosting）；beCloud RCOD 位于 Minsk 区 Kolodishchi, Tsentralnaya 22；A1 Digital 2017 年建成、自称 Tier III 级/白俄罗斯最高可靠性等级，公开页未给精确物理地址；MTS Cloud 自有/受保护 Minsk 数据中心（about 页称 78 机柜，更新新闻称基于两个数据中心）；Datahata 服务声明；Serverspace.by、hoster.by、besthost.by、hostfly.by、bcr.by 等云/VPS 服务商须先确认是否租用 beCloud RCOD（tenant footprint），避免重复计数。
- 行业与贸易源：Onliner Tech（历史运营商文章）、OfficeLife（RCOD/Tier 报道）、BELTA（国家通讯社）、ComNews（俄语电信市场）、TAdviser（项目史，需一手确认）、Dev.by；PeeringDB（BY-IX org 598）仅作互连信号。
- 目录聚合器仅作别名/地址/种子列表：DataCenterMap、Datacenters.com、Inflect、DataCenterJournal、Baxtel、Cloudscene、DC-Union base、zakupki 监测站（C 级，最终计数不得仅凭目录）。
- 政府/银行/封闭部门：NTSEU 国家云为已验证平台但非公共托管设施；国家银行、铁路、部委、OAC/CII 引用可能指向封闭 IT 基础设施，无设施级官方证据不计入。
- 假阳性规则：`ЦОД` 用于普通机房/内部数据处理部门；无托管/机柜声明的 IXP、电信 POP、IP 中转节点；在他人设施内运营的云 MSP/转售页；无命名运营商/站点/建设证据的加密货币或 AI 头条；非活跃项目的 FEZ/投资地图设想。

## 已知设施/项目与证据状态

| 设施/项目 | 分区 | 状态与证据 |
|---|---|---|
| Beltelecom 数据中心服务 | Minsk City 为主；区域性为线索 | 运营中服务/设施提供；A（运营商服务页 datacenter.by）；区域地点需另行佐证 |
| Beltelecom 历史 TsOD, Zakharova 55 | Minsk City | 历史/可能运营中；B（Onliner/贸易历史报道，需运营商或市政当前证明） |
| beCloud 共和数据中心中心（RCOD） | Minsk Oblast, Minsk 区, Kolodishchi | 运营中；A（becloud.by/contacts、regulations-rcod 确认 Tsentralnaya 22） |
| beCloud 国家云/共和国平台 | 物理设施为 RCOD；公司总部 Minsk City | 运营中平台；A |
| A1 Digital 数据中心 | Minsk City | 运营中；A（运营商自称 Tier III 级）；认证时效与精确地址需独立证据 |
| MTS Cloud / MTS 数据中心基础设施 | Minsk City（公开声明）；精确站点未公开 | 运营中；A（运营商声明 78 机柜/两个数据中心）；目录地址为 C |
| NTSEU 国家云/电子政务 | Minsk City | 运营中国家平台，非商业托管；A |
| Datahata 托管/主机服务 | Minsk City 线索 | 运营中服务声明；A（服务），设施地址需佐证 |
| BY-IX | Minsk City | 运营中 IXP，非数据中心；B（PeeringDB org 598 互连证据） |
| Astravets NPP（БелАЭС） | Grodno Oblast, Ostrovets 区 | 仅能源语境；A（NPP 存在），非数据中心证据 |
| AWS/Azure/GCP/OCI 公有云区域 | 无 | 官方清单无白俄罗斯公有云区域/本地区；A（仅证官方清单缺席） |

## 更新节奏

- 季度：Beltelecom、beCloud、A1 Digital、MTS Cloud、Datahata、goszakupki.by、zakupki.butb.by、gse.by、Minsvyazi 新闻。
- 半年：完整 7 分区扫掠（含州/市门户与已知运营商 EGR 查询）。
- 年度：云区域页、PeeringDB 国家/BY-IX 复查、RCOD/A1 的 Uptime 认证时效核对、制裁与监管复查、FEZ/HTP 项目搜索。
- 触发事件：新数字经济/个人数据法、NPP/电网计划公告、FEZ/HTP 数据中心公告、MTS/A1 所有权变更、采购中出现 `ЦОД`、`дата-центр`、`серверная`、`облачная платформа`。
- 待办（2026-08-12）：BY 属 batch-10 已复核国家；后续按本方法论推进 7 分区枚举，codex terra agent 分批复核后更新证据分级。
