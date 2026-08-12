---
name: bh-datacenter-methodology
location: scripts/expansion/world/country-skills/BH/SKILL.md
description: |
  Bahrain (BH) datacenter discovery & audit methodology — how to enumerate, verify, and update Bahrain datacenter projects at governorate granularity (4 governorates in the current manifest). Bahrain is small and centralized: no public national datacenter registry and no public searchable datacenter-permit register; enumeration joins Benayat/MOMAA building permits, UPDA land-use, Sijilat commercial registration, EWA/Tender Board utility & procurement, TRA telecom licensing, iGA government cloud/data-centre programmes, operator pages (Batelco/Beyon, Kalaam, Qareeb), cloud-provider official region pages (AWS me-south-1 present; Azure/GCP/OCI absent), and trade press. Read this before running BH exploration/audit batches. Routes to explorer-official.md (official/regulatory/cloud pipeline) and explorer-industry.md (industry/vendor discovery).
---

# BH · 巴林数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：巴林**没有**公共国家数据中心注册库，也**没有**可公开检索的数据中心许可登记，不能直接按许可库枚举。
> 巴林枚举靠**官方小国集中式管线交叉**：Benayat/MOMAA 建筑许可、UPDA 土地用途、Sijilat 商业注册、EWA/招标局公用事业与采购、TRA 电信牌照、iGA 政府云/数据中心计划、运营商页面（Batelco/Beyon、Kalaam、Qareeb）、云厂商官方区域页与贸易媒体。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供巴林探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：Benayat/MOMAA 建筑许可、UPDA 规划、Sijilat/MOIC-BIIP、EWA/Tender Board、TRA、iGA 政府云、EDB/BNA/Beyon-Oracle Sovereign HyperCloud、云厂商区域页（AWS `me-south-1` 正面、Azure/GCP/OCI 负面） |
| `explorer-industry.md` | 行业/厂商发现：运营商与项目种子（Batelco/Beyon Hamala、White Space/Data Oasis、Kalaam Al Seef、Qareeb edge、Tencent、Gulf Data Hub）、贸易媒体（DCD/Developing Telecoms/The Register 等）、目录、阿拉伯语发现模式与状态词映射 |

## 核心结构事实（框定每次搜索）

1. **行政区划 = 4 省（governorate）**：首都省（Manama、Al Seef/Seef、Bahrain Bay、外交区、Juffair、Hoora、Salmaniya、Umm Al Hassam）、南部省（Riffa、Awali、Askar、Zallaq、Al Dur、Salman Industrial City/US Trade Zone、Beyon Data Oasis/White Space）、穆哈拉格省（Muharraq、Hidd、Arad、Busaiteen、机场、Amwaj、Bahrain Logistics Zone/港口区）、北部省（Hamala、Saar、Budaiya、Diraz、Barbar、Hamad Town）。
2. **四个省锚点**：北部省 = Batelco by Beyon 数据中心（Hamala，官方页给出 Building 1095, Road 1425, Block 1014；Tier III 声称）；南部省 = Beyon White Space Data Centre / Data Oasis（2025-11-02 投运，6,000 sqm 设施在 140,000 sqm 园区内）；首都省 = Kalaam Telecom DC（Al Seef/Manama）；iGA 政府数据中心计划（A 级计划、地址/分区 U）。
3. **超大规模锚点 = AWS Middle East (Bahrain) `me-south-1`**：官方 2019-07-30 开通、3 AZ；AWS 不公布场址地址——所有目录对 Manama/Hamala/Saar 的安置保持 C 级；AWS Health Dashboard 为当前运营状态 A 级源（2026-03 起 ME-SOUTH-1 有无人机袭击相关事件报道，媒体为 B 级历史证据）。
4. **Azure/GCP/OCI 均无巴林公共区域**：Azure 沙特东部区域宣布 Q4 2026（仅区域上下文）；GCP 多哈 `me-central1`（上下文）；OCI 无标准公共区域，主权部署走 Beyon/Oracle Alloy（物理站点 U）。
5. **主权云 ≠ 物理设施**：Beyon Solutions + iGA + Oracle Sovereign HyperCloud 协议（2025-11-02）为 A 级协议事实、U 级物理设施；Tencent Cloud 巴林 IDC 为首个中东 IDC 声明（A/B 声明、U 当前运营站点）；Huawei/Alibaba 无核实区域（C/U）。
6. **建筑许可 = Benayat（MOMAA）**：官方建筑许可系统，但公共门户不暴露可全文检索的许可库——许可路径为 A 级证据，非项目注册表；土地用途/规划经 UPDA Construction Regulations Simulator 与 planning.bh。
7. **能源语义分离**：`it_load_mw`、`grid_mva_or_mw`、`gross_power_mw`、`solar_mwp`、`floor_area_sqm` 分开存储；Data Oasis 140,000 sqm 是园区面积、6,000 sqm 是 White Space 设施面积；Al Dur 电厂仅作电网/地理上下文，不计数为数据中心。
8. **基础设施类别分离**：云区域、IXP（BIX）、海缆登陆站、电厂、企业托管服务、MoU 均不得在无独立设施证据时计数为物理数据中心。
9. **语言**：英语 + 阿拉伯语（`مركز بيانات` 数据中心、`تصريح بناء` 建筑许可、`بنات`、`هيئة الكهرباء والماء` EWA、`هيئة تنظيم الاتصالات` TRA、`الحوسبة السحابية`）；阿拉伯语状态词：`مذكرة تفاهم`=MoU、`وضع حجر الأساس`=开工、`افتتاح`/`تدشين`=投运。
10. **预期产出**：首都省 2-5、南部省 2-4、穆哈拉格省 0-2、北部省 1-3 条正面/线索记录；无确认设施的分区写 `no_projects: true` 并记录负面搜索。

## 常用查询模板（详见 explorer-official.md §1-§4 / explorer-industry.md §1、§4-§5）

- 官方站内：`site:mun.gov.bh "data center" OR "data centre" OR "مركز بيانات"`、`site:benayat.bh "data center"`、`site:upda.gov.bh "data center"`、`site:sijilat.bh "data center" OR "cloud"`、`site:ewa.bh "data center"`、`site:tenderboard.gov.bh "data center"`、`site:tra.org.bh "data center" OR "cloud"`、`site:iga.gov.bh "data center" OR "government data center"`、`site:bahrainedb.com "data center"`、`site:bna.bh "data centre"`、`site:beyon.com "White Space" OR "Data Oasis"`。
- 分区模板：`"Manama" "data center"`、`"Al Seef" OR "Seef District" "data centre"`、`"Beyon" "Data Oasis" "southern Bahrain"`、`"Hidd" OR "الحد" "data centre"`、`"Hamala" OR "الحمّلة" "data center" OR "Batelco" OR "AWS"`、`"Saar" Bahrain "data center"`。
- 运营商：`"Batelco" "Hamala" "data center"`、`"Building 1095" "Road 1425" "Block 1014"`、`"Kalaam" "Al Seef" "data center"`、`"Qareeb" "Batelco" "edge data center"`、`"Tencent Cloud" Bahrain IDC operational official`、`"Gulf Data Hub" Bahrain "data center" official`。
- 云：`"AWS" "me-south-1" Bahrain`、`"Amazon Data Services" Bahrain permit EWA substation lease`、`"Oracle Alloy" "Beyon Solutions" "local data centres"`、`"Microsoft" Bahrain "data center" -UAE -Saudi`。
- 阿拉伯语：`"البحرين" "مركز بيانات" "باتلكو" OR "بيون" OR "أمازون"`、`site:bna.bh "مركز بيانات"`、`"البحرين" "الحوسبة السحابية" "السحابة الحكومية"`。

## 官方/监管管线要点（详见 explorer-official.md）

- 规划/许可：Benayat 建筑许可门户（A，许可路径）、UPDA 建筑规范模拟器 + planning.bh（土地适宜性）、Sijilat 商业注册公开检索（实体存在 A、非设施证明）、MOIC BIIP 工业园（投资园地线索；BIIP 位置有 Southern/Muharraq 歧义——按来源地点字符串记录，经 UPDA/MOMAA 核实再定省）。
- 能源/采购：EWA（电力/水务权威，招标页可能需邮件索取文档）、Bahrain Tender Board（A 级采购事实）；变电站/大负荷/光纤招标词 `substation`、`محطة تحويل`、`large load`。
- 电信/政府：TRA（牌照与 licensee 名单，核实运营商身份）、iGA（政府数据中心管理与发展声明 A、地址非公开；政府云迁移 AWS 声明 A）、EDB（A/B 投资声明，作线索）、BNA（官方新闻英/阿双语）、Beyon + iGA + Oracle Sovereign HyperCloud 协议（A 协议/U 设施）。
- 云官方区域：AWS `me-south-1`（A，3 AZ）、Azure 无巴林区域、GCP 无、OCI 无标准公共区域——每次扫描重查官方页并记录日期。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 现实全国产出约 6-12 条确认/线索记录 + IX/海缆/云区域上下文；市场小而连接导向。
- 高信号源：Beyon/Batelco（自有事实 A）、Kalaam（A）、Qareeb（A/B 公告、U 独立设施）、DCD（B）、Developing Telecoms/The Register/Network World/DCK（B，AWS 2026 事件）、BNA/EDB/iGA（A/B）、目录（C）。
- 运营商种子分级：Batelco Hamala DC（A 运营商/地址/Tier III 声称；Uptime 证书另行核实）、Beyon White Space/Data Oasis（A，设施/园区面积分开记）、Kalaam Al Seef（A 位置/服务、容量 U）、iGA 政府 DC（A 计划/U 地址）、Tencent（A/B 声明、U 当前站点）、Oracle/Beyon 主权云（A 协议/U 物理）、Qareeb edge（A/B 公告、需确认是否独立于 White Space）、Gulf Data Hub（C，仅市场报告）、stc Bahrain/Zain（B/C/U 企业托管线索）。
- 名称归一化：`Batelco`/`Batelco by Beyon` → Beyon Group；`VIVA Bahrain` → `stc Bahrain`；`White Space Data Centre` → Beyon/Batelco Data Oasis 设施；`me-south-1` → AWS Middle East (Bahrain)。
- 状态值：`announced | MoU | planned | land lease | secured power | under construction | commissioned | operational | impaired | retired | unknown`。

## 来源分级

- **A** = 运营商设施页、政府/公用事业/监管记录、认证机构记录、许可/土地/电力记录、官方投运新闻稿、云官方区域页、官方 IXP/证书源。
- **B** = DCD、Developing Telecoms、The Register、Network World、Data Center Knowledge、W.Media、Capacity Media、ITP、Trade Arabia、Gulf Daily News、Biz Bahrain、承包商/厂商案例研究。
- **C** = 目录、市场报告、PeeringDB 单源、Inflect、社交帖、SEO 页、无出处地址/容量记录。
- **U** = 未解决。分级针对来源所证明的**具体事实**：官方 AWS 页证明 `me-south-1` 存在，不证明 AWS 未公布的街道地址；MoU/云区域/IX/海缆/电厂不得单独构成设施记录。

## 维护注意（更新纪律）

- **更新节奏**：月度——Beyon/Batelco/Kalaam/Qareeb 官方页、DCD 巴林标签、BNA；季度——TRA 牌照、iGA、EDB、EWA/招标局、云厂商官方区域表、目录（Data Center Map/Baxtel/Cloudscene/PeeringDB）；事件驱动——AWS 运营状态（Health Dashboard）、Tencent 巴林 IDC 上线、Oracle Alloy 主权云物理站点、海缆 RFS、新投资 MoU。
- **来源验证**：目录地址/容量须回链运营商/官方一手源；分区归属先按来源地点字符串、再经 UPDA/MOMAA 地图核实（Hamala/Saar→北部省；Manama/Al Seef→首都省；Hidd→穆哈拉格省；Riffa/Askar/SIC/巴林南部→南部省）；BIIP 位置歧义须地块证据。
- **不删除纪律（NO-DELETION）**：只创建自己的结果文件与 skill 文件；不修改/删除 explorer 源文件与其他工作产物；新证据以新增记录 + 分级并存，不覆盖旧证据；稀疏分区记录负面搜索而非用 IX/海缆/云伪记录充数。
