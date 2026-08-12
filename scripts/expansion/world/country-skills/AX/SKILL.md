---
name: ax-datacenter-methodology
location: scripts/expansion/world/country-skills/AX/SKILL.md
description: 奥兰群岛数据中心发现与审计方法论（bilingual）。Åland Islands datacenter discovery & audit methodology: enumerate the official/regulatory/cloud pipeline (Ålands landskapsregering & Lagtinget, Traficom telecom, municipal planning/bygglov across 16 kommuner, Kraftnät Åland/el.ax/energi.ax power, ÅMHM environmental permits, EU TED/Hilma procurement, PRH/YTJ company registry, ÅSUB statistics, cloud-region absence checks) plus industry/trade-press discovery (Nya Åland, Ålandstidningen, Ålands Radio, HBL/Yle/Kauppalehti, DCD, FDCA/TIVIA, Ålcom operator pages, PeeringDB/directories). Division model: country with 1 division (Aland Islands); 16 municipalities are search buckets only. Read before running AX exploration/audit batches; routes to explorer-official.md and explorer-industry.md.
---

# AX · 奥兰群岛数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：奥兰群岛（Åland/Ahvenanmaa）为芬兰自治、非军事化、瑞典语地区（人口约 3 万，Mariehamn 占 40%+）；截至 2026-08-12 复核，**极不可能存在可枚举的商业数据中心市场**：未发现 Åland 云区域、未发现公开 colocation/hyperscale 设施，Ålcom 公开页面显示的是宽带、移动、电视、Webbhotell 与 AX 域名等服务，不构成数据中心设施证据。发现工作应按「快速证伪」执行：先扫官方、监管、电力、采购和运营商表面；无信号则记录为「无市场/未发现」。本方法论通过**官方/监管/云管线（explorer-official.md）**与**行业/媒体/厂商发现（explorer-industry.md）**双轨三角验证，行业侧线索须回到 official 管线的 A 级表面定稿；本 skill 汇总两份最终审定报告，作为 AX 探索/审计批次的入口。

## 入口

| 文件 | 管线 | 内容 |
| --- | --- | --- |
| explorer-official.md | 官方/监管/云管线 | regeringen.ax（政府）、lagtinget.ax（议会）、16 市镇规划/bygglov（{kommun}.ax）、Traficom（电信监管）、Kraftnät Åland/el.ax/energi.ax/Fingrid（电力/电网）、ÅMHM（环境许可 amhm.ax）、EU TED/Hilma（采购）、PRH/YTJ（公司登记）、ÅSUB/StatFi（统计）、海缆（Ålcom/TeleGeography）、四大云区域缺失检查 |
| explorer-industry.md | 行业/媒体/厂商发现 | 本地媒体（Nya Åland、Ålandstidningen、Ålands Radio）、芬兰/瑞典媒体（HBL、Yle、Kauppalehti、T&T/Tivi、DI、Computer Sweden）、国际 DC/互联媒体（DCD、Capacity、DCK）、协会/研究（Ålands Näringsliv、FDCA、TIVIA、EUDCA、JLL/CBRE）、运营商/厂商（Ålcom、Elisa/Telia/DNA、Tietoevry、Ålandsbanken、航运）、目录（PeeringDB、Baxtel、DataCenterMap、Cloudscene） |

## 核心结构事实

1. **行政区划模型**：manifest 为 **country**，恰好 **1 个 division：`Aland Islands`**（subnational_type="country"）；16 个市镇（Mariehamn、Jomala、Finström、Sund、Saltvik、Hammarland、Eckerö、Lemland、Lumparland、Vårdö、Geta、Föglö、Kökar、Sottunga、Kumlinge、Brändö）仅作检索桶与候选定位，**不得写成 manifest division**；高优先级市镇 Mariehamn/Jomala/Finström，中优先级 Sund/Saltvik/Hammarland/Eckerö/Lemland，其余为低密度覆盖。
2. **注册库现状**：不存在单独数据中心登记表；必须通过规划/建筑许可、环境许可、电力连接、采购、运营商设施页交叉验证；无公开商用 DC 市场为工作负基线（2026-08-12），仅当官方/监管/采购/运营商表面均无信号时才记录「未发现商用 DC 市场」。
3. **法律与监管**：Åland 自治地位（Lagtinget 议会 + Ålands landskapsregering 政府，regeringen.ax）；欧盟 VAT 区外（影响贸易/物流/账单，非设施证据）；电信监管由芬兰 **Traficom** 执行，本地主要运营商为 **Ålands Telekommunikation Ab / Ålcom**；**ÅMHM**（amhm.ax）为环境与健康许可/监管机构；公司登记仍在芬兰体系（PRH/YTJ）。
4. **电力/电网**：**Kraftnät Åland**（kraftnat.ax）为输电系统运营方，stamnät 页面说明 Sweden cable 80 MW、现有取电受订阅容量限制；**Ålands Elandelslag**（el.ax）与 **Mariehamns Energi**（energi.ax）为关键本地配电/能源表面；ÅL-Link/Finland cable 为 100 MW 级 HVDC（2015 投运，电力安全项目非 DC 项目）；DC 级项目若真实存在，通常至少在电力连接/容量升级/用地或环境许可中留痕。
5. **设施/项目种子（2026-08 证据状态）**：**无**已核实商业 DC 设施；**Ålcom Webbhotell & AX-domän**（alcom.ax）为网站空间/邮箱/DNS/备份服务——A 级服务存在、C 级设施推断不成立；候选类型仅限本地运营商机房、市政 IT 机房、银行/航运自用机房（Ålandsbanken、Eckerö Line/Viking Line——默认 C 不可入库），除非有明确客户托管、设施地址、许可或运营商设施页。
6. **语言与词汇**：**瑞典语为最重要检索语言**（datahall、serverhall、datacenter、datacentral、kolokalisering、IT-infrastruktur、molntjänst、elanslutning、bygglov、miljötillstånd、upphandling）；芬兰语（konesali、datakeskus、palvelinkeskus、palvelinhuone、pilvipalvelu、sähköliittymä）；英语（data center/centre、colocation、colo、edge、hosting、server farm、cloud region）；拼写召回须同时搜 Åland、Aland、Aland Islands、Ahvenanmaa、Mariehamn、Maarianhamina。
7. **可靠性分级**：A = 一手/官方/可问责来源（政府/议会/市政文件、法定许可、电信与能源监管文件、电力公司文件、运营商官方设施页、官方云区域页、TED/Hilma 采购、YTJ/PRH 公司登记、ÅSUB/StatFi 官方统计）；B = 强二级（成熟媒体、行业协会、研究报告、TeleGeography、与一手记录一致的运营商新闻稿）；C = 弱线索（聚合器、自报目录、社交媒体、无出处地图、顾问摘要、营销材料、签约仪式报道）。**A 级可直接定稿**（运营商设施页 + 位置、政府/市政 bygglov、ÅMHM 环境许可、电力连接、TED/Hilma 采购、官方云区域页、PRH/YTJ 实体登记）；B 级仅作线索/佐证；C 级不可单独入库；B 媒体 + A 许可/电力/运营商页 = 可入库。
8. **计数与去重规则**：**Web hosting ≠ colocation**（Ålcom Webbhotell 只记服务不记设施）；**电信机房 ≠ DC**（交换局、基站、POP、Metro Ethernet 节点仅当提供第三方托管/colocation 且可定位才算候选）；**电力/海缆新闻 ≠ DC 项目**（Sweden/Finland 电力海缆、区域光缆、风电扩容只说明基础设施背景）；**芬兰/瑞典服务覆盖 ≠ AX 设施**（运营商服务 Åland 客户不代表设施在 Åland）；容量语义：优先官方 IT load MW，其次电力连接容量、机架数、面积；园区总 MW 与已投产 MW 分开存储；聚合器空结果不是 A 级负证据。

## 常用查询模板

```text
# 官方/监管
site:regeringen.ax (datacenter OR serverhall OR datahall OR datacentral OR konesali OR "digital infrastruktur" OR upphandling server OR "elanslutning" data)
site:lagtinget.ax (datacenter OR serverhall OR datahall OR "digital infrastruktur" OR "dataskydd")
site:{kommun}.ax bygglov server ; site:{kommun}.ax datahall ; site:{kommun}.ax datacenter
site:mariehamn.ax (bygglov OR datahall OR datacenter)
"{kommun}" "bygglov" "serverhall" Åland
# 电信/运营商
site:alcom.ax (webbhotell OR hosting OR serverhall OR datahall OR colocation OR "Metro Ethernet")
"Ålcom" OR "Ålands Telekommunikation" "serverhall" OR "datahall"
# 电力
site:kraftnat.ax (data OR server OR "elanslutning" OR "stamnät") ; site:el.ax ("ny elanslutning" OR datahall) ; site:energi.ax server
"Åland" "elanslutning" "datacenter" MW ; "Åland" "serverhall" MW
# 环境许可
site:amhm.ax (datahall OR serverhall OR "miljötillstånd" data)
"Åland" "miljötillstånd" "datacenter"
# 采购/公司登记
site:ted.europa.eu (Åland datacenter OR Ahvenanmaa server)
site:hankintailmoitukset.fi (Åland server OR Ahvenanmaa konesali)
site:prh.fi "Ålands Telekommunikation" ; "Åland" datacenter Ab ; "Ahvenanmaa" datakeskus yritys
# 本地媒体/行业
site:nyan.ax (datacenter OR serverhall OR datahall OR datacentral)
site:alandstidningen.ax (datacenter OR serverhall)
site:alandsradio.ax (datahall OR serverhall)
"Åland" "serverhall" ; "Åland" "datahall" ; "Åland" "datacenter" ("planerar" OR "bygger" OR "öppnar" OR "inviger")
site:hbl.fi Åland (datacenter OR serverhall) ; site:yle.fi Ahvenanmaa (datakeskus OR konesali)
site:kauppalehti.fi Ahvenanmaa datakeskus ; site:di.se Åland datacenter
site:datacenterdynamics.com (Åland OR "Aland Islands") ; site:capacitymedia.com Åland submarine cable
site:fdca.fi (Åland OR Ahvenanmaa) ; site:an.ax (datacenter OR serverhall OR digitalisering)
# 三语万能模板
"Åland" ("data center" OR "data centre" OR colocation OR "server farm" OR "cloud region" OR hyperscale)
"Ahvenanmaa" ("konesali" OR "datakeskus" OR "palvelinkeskus" OR "sähköliittymä" "datakeskus")
"Aland Islands" ("data center" OR "data centre" OR colocation)
# 目录（仅发现，C 级）
peeringdb Åland ; peeringdb Mariehamn ; site:baxtel.com Åland ; site:datacentermap.com Åland ; site:cloudscene.com Åland
# 云缺失检查
site:aws.amazon.com OR site:learn.microsoft.com OR site:cloud.google.com OR site:oracle.com (Åland OR "Aland Islands" OR Ahvenanmaa) - absence check
```

## 官方/监管管线要点（详见 explorer-official.md）

- **regeringen.ax**：政策/新闻/采购/能源/环境/基础设施/法律草案/政府物业项目；任何大型 DC 投资、公共 IT 采购或能源接入争议都可能在此留痕。
- **lagtinget.ax**：landskapslag、预算、议会问题、委员会材料；验证 DC 激励、能源例外、规划法变更或数据保护争议。
- **市镇规划/建筑许可**：Mariehamn 与其余 15 个 `{kommun}.ax` 站点（本轮复核均可达）；大型机房会涉及 bygglov、详细规划、用地变更、消防/环境条件或公用事业连接。
- **Traficom/Ålcom**：Traficom 查电信网络/编号/频谱/NIS2 安全要求；Ålcom 查企业服务/wholesale/Metro Ethernet/Webbhotell 及任何 colocation/serverhall 页面；已核验 Ålcom 有 Webbhotell & AX-domän，无公开 colocation/serverhall/datahall 披露。
- **电力**：Kraftnät Åland（输电/海缆/备用发电）、el.ax、energi.ax、Fingrid（芬兰侧对照）；大负荷连接、电网容量、海缆、备用发电、输配电边界。
- **环境许可**：ÅMHM（miljötillstånd、tillsyn、燃油备用电源、冷却、水使用、噪声）；小型设备间可能无可见环境许可，大型设施应有痕迹。
- **采购/公司登记**：EU TED、芬兰 Hilma、regeringen.ax 站内 upphandling、各市镇站点；采购只能证明需求或合同，不自动证明设施所在地；PRH/YTJ 核实公司实体、Business ID、注册地址、行业代码。
- 执行顺序：regeringen/lagtinget/ÅMHM → 高优先市镇 bygglov/detaljplan/upphandling → 电力（kraftnat/el.ax/energi.ax 大型连接与扩容）→ Ålcom 服务页（Web hosting 只记服务）→ 四大云区域页 → TED/Hilma + PRH/YTJ → 行业侧补充；全部无 A/B 信号时结论写为：`Aland Islands: no commercial data center facilities found in verified official/regulatory/operator surfaces`。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 本地媒体：Nya Åland（B，本地项目/市政/能源/电信/企业新闻；若有 AX DC 极可能出现）、Ålandstidningen（B）、Ålands Radio och TV（B，公共广播）；芬兰/瑞典媒体：HBL、Yle/Svenska Yle、Kauppalehti、Tekniikka & Talous/Tivi/Talouselämä、Dagens Industri、Computer Sweden/Ny Teknik（均 B）。
- 国际 DC/互联媒体：DCD（B，已见 Finland 报道未见 AX 设施信号）、Capacity Media（B）、Data Center Knowledge（B）、Dgtl Infra/W.Media（B/C）；协会/研究：Ålands Näringsliv（A/B）、FDCA（B，AX 若出现即高信号）、TIVIA（B）、EUDCA（B）、JLL/CBRE/C&W 北欧 DC 报告（B）、TeleGeography（B）、Submarine Cable Map（C）。
- 运营商/厂商：Ålcom（A 服务页/C 设施推断）、Elisa/Telia/DNA（B/C，通常非 AX 设施）、Tietoevry（B，托管线索须核实设施所在地）、Ålandsbanken（C）、Eckerö Line/Viking Line（C，航运 IT/灾备）。
- 分级与升级规则：A 级可直接定稿；B 级仅线索/佐证（媒体只能证明「有报道」，设施状态/容量/位置必须回到官方许可、运营商设施页、采购、电力连接或公司登记核实）；C 级不可单独入库；B 媒体 + A 许可/电力/运营商页 = 可入库；C 聚合器 + A 官方页 = 可入库；C 孤证 = 不入库；仅 hosting/webbhotell/DNS/email/cloud 服务无客户托管或设施披露 = 降为服务线索，不计 DC。
- 诚实结论（2026-08）：AX 无公开商业 DC 市场；Ålcom 仅 Web 托管；对照市场为芬兰大陆 Helsinki/Hamina/Turku 与瑞典 Stockholm——任何「服务 Åland」或「连接 Åland」报道都要区分设施是否实际在 AX。

## 维护注意（更新纪律）

- **更新节奏**：每季度——Nya Åland/Ålandstidningen/Ålands Radio 本地扫描（datacenter/datahall/serverhall/konesali）、Ålcom 服务页核验、Kraftnät/el.ax/energi.ax 电力表面、TED/Hilma 采购扫描、四大云区域页复检（Åland/Aland Islands/Ahvenanmaa）；每半年——regeringen/lagtinget 政策与项目页、ÅMHM 环境许可、PRH/YTJ 实体登记、FDCA/TIVIA/Ålands Näringsliv 报告；事件驱动——任何 AX 云区域/colo/hyperscale 公告为最大变化信号，立即升级并核对区域/Local Zone/edge 类型。
- **来源核验**：A 级 URL 逐个点击；YTJ 直连可能拒绝/超时（官方 BIS 入口，必要时从 PRH 或 Suomi.fi 进入）；拼写召回必须覆盖 Åland/Aland/Aland Islands/Ahvenanmaa/Mariehamn/Maarianhamina。
- **不删除纪律（no-deletion）**：已核实记录不得删除；状态变化改标（planerar/announced/MoU → bygglov/elanslutning/miljötillstånd/upphandling → 运营/近运营）并保留原始证据链；无支撑条目降级为 C 保留而非移除；负向检索（无项目）须如实记录而非跳过。
