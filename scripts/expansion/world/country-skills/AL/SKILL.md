---
name: al-datacenter-methodology
location: scripts/expansion/world/country-skills/AL/SKILL.md
description: |
  Albania (AL) datacenter discovery & audit methodology — how to enumerate, verify, and update Albania datacenter projects at county (qark) + municipality (bashki) granularity (12 counties, 61 municipalities in the current manifest). Albania has no public national datacenter registry and no hyperscale cloud region: enumeration joins E-Leja building permits (e-Albania service 6093 / AKPT-KKT), QKB business registry, ERE/OST/OSHEE grid evidence, AKEP telecom authorizations, AKSHI/APP public IT & procurement, RASH/ANIX interconnection records, and operator pages (Host.al, One Albania, Abissnet, Nisatel) plus the ADC/TEDA pipeline lead in Kashar. Read this before running AL exploration/audit batches. Routes to explorer-official.md (permits/registry/energy/telecom/state-IT/cloud) and explorer-industry.md (operators/trade press/directories/Albanian-language recipes).
---

# AL · 阿尔巴尼亚数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：阿尔巴尼亚**没有**公开的全国数据中心注册库，也无 AWS/Azure/GCP/OCI 公共云区域（每次运行重查官方列表）；市场 **Tirana 单极集中**，查询采用“建筑许可/注册库→电力→电信→州级政府 IT →互联网”多轨迹交叉。
> 分区模型：**12 州（qarqe）→ 61 市镇（bashki）**（INSTAT 行政分类），先州后市镇；Tirane 州主要产出，Durres/Vlore 为次级带。
> 已知种子：Host.al HS1（Tirana）、RASH/ANIX（Rruga e Durresit 219）、AKSHI 政府数据中心/云（APP 采购）、ADC/TEDA 项目（Kashar，32 MW 首期可能 100 MW，B 级）、One Albania/ALBtelecom 线索、Abissnet、Nisatel（Vlore）。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供阿尔巴尼亚探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：E-Leja（e-Albania 6093）、AKPT/planifikimi.gov.al 与 KKT/KKTU 决定、市镇门户、QBZ 法律（107/2014、VKM 408/2015）、QKB 注册库与 ASHK 地籍、ERE/OST/OSHEE/KESH 电力、AKEP 电信、AKSHI/APP/OpenProcurement 政府 IT、云负面核查、12 州枚举工作流与模板 |
| `explorer-industry.md` | 行业/厂商发现：运营商种子表（Host.al/RASH-ANIX/ADC-TEDA/One Albania/Abissnet/Nisatel/Vodafone/AKSHI）、Globes/DCD/SeeNews/Albania Economia 贸易媒体、Data Center Map 等目录（C）、互联/Italy-Albania 海缆线索、AIDA/TEDA 投资促进、阿尔巴尼亚语搜索配方 |

## 核心结构事实（框定每次搜索）

1. **无全国注册库、无超规模云区域**：建立记录必须联合建设许可、法人注册、电力、电信、采购、互联网与运营商页；云场景通常是 AKSHI 政府云/运营商云/外国区域转售，不等于本土设施。
2. **建设许可中央化但决策主体分散**：E-Leja 通过 e-Albania 服务码 6093，决策权可在市镇或 KKT/KKTU；官方路径 AKPT/planifikimi.gov.al（procedura + id=263 KKT 决定页）、AZHT、`bashkia<name>.gov.al` 市镇门户、Porta Vendore；法律基础 QBZ Law 107/2014 + VKM 408/2015（Law 41/2024 修正引入 KKTU 语言）。
3. **QKB 注册库是法人决胜关**：按 NIPT/NUIS 查证法人与地址，防止 ADC 后台（Alis Initiatives / H.A.P.I./Happy Technologies / DIT）名称碰撞；报道 SPV 在 QKB 确认前不计入。
4. **电力与电网：ERE/OST/OSHEE/KESH**：提取 MW/MVA、电压等级、变电站/馈线、连接申请与电化日期；ADC 的 32 MW/100 MW/专用变电站/水电供应在 OST/OSHEE/ERE 或许可执照前均为 B 级。
5. **AKEP 证明运营商身份，不证明设施**：电信授权/年报用于 One Albania/ALBtelecom/Abissnet/Nisatel/Vodafone 上下文；光纤 POP/移动核心机房≠数据中心。
6. **互联网高信号：ANIX/RASH（A）**：官方 ANIX 页证明其寄托于 RASH 中央 Tirana 的 carrier-grade 数据中心；PeeringDB fac/4508 + IX/2004 给地址 Rruga e Durresit 219（B）；Italy-Albania（Bari-Durres）海缆线为带线索。
7. **政府 IT 与采购：AKSHI + APP/OpenProcurement**：云/服务器采购（如 2024-03 EUR 7m AKSHI 云硬件招标）是设备更新还是新设施须分清；GOVnet 扩展项目为 EU/WBIF 背景。
8. **拼写与语言**：阿尔巴尼亚语 `qendra e te dhenave`、`qender e te dhenave`、`dhoma e servereve`、`kolokacion`、`leje ndertimi/zhvillimi`、`nenshtacion`、`bashkia`、`qarku`；无变音符变体均要搜；公报 QBZ + planifikimi PDF 为法律源。

## 查询模式（复制粘贴模板见 explorer-official.md §2-§8 / explorer-industry.md §1-§7）

- 建设许可：`site:planifikimi.gov.al "leje ndertimi" "data center"`、`site:planifikimi.gov.al "qendra e te dhenave"`、`site:tirana.al "leje ndertimi" "data center"`、`"{municipality}" "leje ndertimi" "qendra e te dhenave"`、`filetype:pdf "leje ndertimi" "qendra e te dhenave"`。
- 法律/注册：`site:qbz.gov.al "107/2014" "planifikimin dhe zhvillimin e territorit"`、`site:qkb.gov.al "Albania Data Center"`、`site:qkb.gov.al "Alis Initiatives"`、`"{operator}" "NIPT" Albania`、`site:ashk.gov.al "Kashar" "kadaster"`。
- 电力：`site:ere.gov.al "data center"`、`site:ost.al "nenshtacion" "Kashar"`、`site:oshee.al "kerkese per lidhje"`、`"{operator}" "OST" "MVA" Albania`。
- 电信/互联：`site:akep.al "qendra e te dhenave"`、`site:anix.al "data center" "Tirana"`、`site:peeringdb.com "RASH - ANIX"`、`"Italy-Albania" "Durres" "submarine cable"`。
- 政府 IT：`site:akshi.gov.al "qendra e te dhenave"`、`site:eprocurement.app.gov.al "AKSHI" "server"`、`site:openprocurement.al "AKSHI" "server"`、`"Qendra e te Dhenave Qeveritare" "Tirane"`。
- 州级通用：`"Qarku i {COUNTY}" "qendra e te dhenave"`、`"{municipality}" "leje ndertimi" "server"`、`"{municipality}" "prokurim publik" "server"`、`"{municipality}" "nenshtacion" "MW"`。
- 阿尔巴尼亚语全国：`"qendra e te dhenave" "Shqiperi"`、`"qender e te dhenave" "Tirane"`、`"kolokacion" "Tirane"`、`"qendra e te dhenave" "fletorja zyrtare"`。
- 贸易媒体：`site:seenews.com Albania "data centre" OR "data center"`、`site:datacenterdynamics.com Albania "data center"`、`site:en.globes.co.il Albania "data center"`、`"Albania Data Center" "TEDA" "Kashar"`。

## 官方/监管管线要点（详见 explorer-official.md）

- 入口：E-Leja/e-Albania 6093（可能防爬虫，用浏览器会话/缓存）→ AKPT/planifikimi → 市镇门户（tirana.al、durres.gov.al、`bashkia<name>.gov.al`）→ QKB 法人（NIPT/NUIS）→ ASHK 地籍；每州必跑：许可 + QKB + APP/采购 + AKEP + ERE/OST/OSHEE + AKSHI + 市镇文件。
- 电力：ERE、OST（输电/变电站）、OSHEE（配电连接申请）、KESH（发电）；ADC 电力证据仅 B 级直至官方记录。
- 云：无 AL 区域（AWS/Azure/GCP/OCI 官方页负面核查）；宣布时仍需许可/电力证据才给设施。
- 证据规则：报道不升 A（ADC/TEDA=B）；聚合器不升 A；电信节点/政府服务器房与商业 colo 分开；地址确认以官方地址/地籍/许可/QKB 为准（Kashar 属 Tirane 市镇，勿归 Durres）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 贸易媒体：Globes（ADC）、DCD（ADC 与 One Albania 合并）、SeeNews（H.A.P.I./Alis 线索）、Albania Economia、ATA（官方新闻社）、Monitor.al/CNA/Tirana Times 等本地媒；实例：Globes/DCD/SeeNews 2026 ADC（EUR ~100m/32 MW首期）为 B。
- 运营商种子：Host.al HS1（A 官方 colo 页）、RASH/ANIX（A 互联）、AKSHI（A 采购）、ADC/TEDA（B/C）、One Albania/ALBtelecom（C——旧名合并后须 One 官方页确认）、Abissnet（B/C）、Nisatel（C，Vlore）、iregisterdata.center/Tirana DataCom（C）。
- 目录（C，仅作种子）：Data Center Map（当前 5 设施全在 Tirana）、datacenters.com、DataCenterJournal（旧 ALBtelecom/RASH/Pronet 线索）、Baxtel、Inflect、PeeringDB fac/4508（B）。
- 生命周期动词：`plans/selected/preparing/land lease`=线索；`tender/design/permit/grid connection/construction started`=强在建线索；`opened/operates/hosts/colocation/IXP hosted at`=更强设施信号。

## 已知设施/项目与证据状态

| 设施/项目 | 州/市镇 | 状态与证据 |
|---|---|---|
| Host.al Datacenter Albania HS1 | Tirane/Tirana | A（官方 colocation 页）；地址/QKB/许可/电力 待补；PeeringDB 地址 Tefta Tashko Koco 23 为 B/C |
| RASH / ANIX carrier-grade DC | Tirane/Tirana | A（ANIX 官方声明）+B（PeeringDB fac/4508，Rruga e Durresit 219）；互联场景限定，非大型 colo 校区 |
| AKSHI 政府数据中心/云 | Tirane/Tirana | A（官方采购时）/B（报道）；确认地址/招标范围/赢标方 |
| Albania Data Center (ADC) / TEDA | Tirane/Kashar | B（Globes/DCD/SeeNews/Albania Economia；32 MW首期、100 MW扩展、水电/专用变电站主张）；QKB/KKTU/TEDA 租赁/OST-OSHEE/EBRD 待验证 |
| One Albania / ALBtelecom 数据中心 | Tirane/Kashar | C（聚合器地址 Autostrada Tirane-Durres Km 7）；One 官方/许可前不计入 |
| Abissnet hosting/network | Tirane/Tirana | B/C；确定是否有可计 colo/DC |
| Nisatel hosting/network | Vlore（注册地） | C；物理设施未确认 |
| Data Center Map 5 设施 | Tirana | C 种子清单，须一一对账 |

## 更新节奏

- 每批次：云区域负面核查（AWS/Azure/GCP/OCI）、ADC/TEDA 进展（QKB/KKTU/TEDA/OST-OSHEE/EBRD）、Data Center Map 对账、Tirana 市镇许可新增。
- 季度：12 州通用扫与负面记录回顾；One Albania、Host.al 设施页变更；新海缆/能源走廊线索（Durres/Vlore）。
- 待办（2026-08-12）：两份 explorer 初稿已完成；下一步 codex terra agent 分批复核（12 州粒度）；本 skill 作为国家层参考注入。
