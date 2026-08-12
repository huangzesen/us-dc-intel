---
name: lt-datacenter-methodology
location: scripts/expansion/world/country-skills/LT/SKILL.md
description: |
  立陶宛（Lithuania, LT）数据中心发现与审计方法论。10 个 county（apskritys）输出分区 + 60 个 municipality
  实操粒度。无公开 DC 登记册、无 DC 专属许可类别，需拼接 Infostatyba 施工许可、市政规划/PAV、Litgrid/ESO/VERT
  电力、Registru centras 不动产登记与运营商官方页。市场为 Vilnius-first：Telia 新 DC（Raisteniskes，在建）、
  Telecentras（Tier III colo + 4 个政府 DC 项目）、Delska LT DC1/DC2/DC3、Bite（Data Inn 租户部署）、Baltneta、
  Bacloud（Siauliai）；Kaunas 有 LETAS/Serveroffer/Host Baltic leads；Kruonis Technology Park 为国家级选址
  pipeline（siting lead）。无 AWS/Azure/GCP/OCI 公有云区域。立陶宛语术语优先（duomenu centras）。
  详见 explorer-official.md 与 explorer-industry.md。
---

# LT · 立陶宛数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：立陶宛无公共 DC 登记册且无可靠的 DC 专属许可类别，普查需拼接施工记录、市政记录、环评筛选、电力证据、
> 登记册证据、运营商页与贸易线索。`duomenu centras` 常指数据处理机构/办公室，误报极多。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供按 10 county 粒度复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管管线：Infostatyba 许可、市政规划/PAV、Litgrid/ESO/VERT、RRT、AAA 环评、Registru centras、Invest Lithuania（Kruonis）；10 county 逐 municipality 策略与记录字段/状态规则。 |
| `explorer-industry.md` | 行业/厂商发现：运营商种子（Telia/Telecentras/Delska/Bite/Baltneta/Bacloud/Kaunas 群/Vilnius 中小运营）、DCD/LRT/Verslo Zinios/施工媒体、目录别名与证据处理。 |

## 核心结构事实（框定每次搜索）

1. **行政区划双轨**：输出用 10 county（Alytus、Kaunas、Klaipeda、Marijampole、Panevezys、Siauliai、Taurage、Telsiai、Utena、Vilnius）；2010 年后县署废除，实际研究按 60 个 municipality 进行。
2. **无 DC 登记册/许可类**：强设施证据 = 运营商自有页/发布、Infostatyba 许可或完工记录、市政规划/议会/PAV 文档、非住宅技术建筑的不动产登记、或绑定具名项目/地址的电力/监管文档。
3. **误报控制**：排除 ZUDC（Zemes ukio duomenu centras）、Valstybes duomenu agentura、ID Vilnius、市政 GIS/统计单位、学校/机房、银行/部委 "data" 团队——除非明确为托管/colo/云/HPC/电信设施。
4. **市场形状**：Vilnius-first；Siauliai 有 Bacloud（2006 起）；Kaunas 区有托管/colo leads；Klaipeda/Panevezys/Alytus/Marijampole/Taurage/Telsiai/Utena 低产。
5. **Kruonis 是选址不是设施**：Kruonio technologiju parkas（Kaisiadorys 区、Kaunas county）75 ha、近期约 200 MW 电力潜力——出现锚定租户 + 许可/施工前不得计为运营 DC。
6. **无 hyperscaler 区域**：AWS/Azure/GCP/OCI 官方表均无 LT（2026-08-12）；Invest Lithuania 推广 ≠ 已实现容量。
7. **Tier 状态纪律**：Tier III 认证需 Uptime/认证证据；`Tier 3`/`Tier III by design` 是运营商声明。
8. **建筑 vs 租户足迹**：Bite 2022 设施信号是在 Data Inn/DLC 内的服务部署，不得重复计为独立建筑。

## 查询模式（复制粘贴模板见 explorer-official.md / explorer-industry.md）

```text
"duomenu centras" OR "duomenu centrai" (Vilnius OR Kaunas OR Siauliai OR Klaipeda)
site:infostatyba.planuojustatau.lt "duomenu" OR "{operator}"
"{municipality}" "duomenu centras" "projektiniai pasiulymai" OR "tarybos sprendimas"
"{operator}" "statyba leidziantis dokumentas" OR "statybos leidimas"
site:litgrid.eu OR site:eso.lt OR site:vert.lt "duomenu centras"
site:aaa.lrv.lt "atranka" OR "PAV" "duomenu"
site:vilnius.lt OR site:vrsa.lt "duomenu centras"
Telia "Raisteniskes" OR "Ukmerges g. 449" "duomenu centras"
Telecentras "Sausio 13-osios" OR "VDC" "duomenu centrai"
Delska "LT DC1" OR "J. Tiskeviciaus" OR "T. Sevcenkos" OR "A. Juozapaviciaus"
Bacloud Siauliai "data center"
"Kruonis" "data center" "200 MW"
site:lrt.lt OR site:vz.lt OR site:statybunaujienos.lt "duomenu centras"
"Lithuania" "data center" ("building permit" OR commissioned OR opened)
```

## 官方/监管管线要点（详见 explorer-official.md）

- **Infostatyba**（infostatyba.lt + infostatyba.planuojustatau.lt + data.gov.lt/datasets/3740）：A 级施工许可/完工面；按运营方法人、地址、地块与技术词搜索（系统可能不用 `duomenu centras` 字样）。
- **市政/环评**：市政页（vilnius.lt、kaunas.lt、klaipeda.lt 等）为 A 级议会决议/规划/PAV 通知；AAA（aaa.lrv.lt）PAV 面，DC 常以发电机/燃料/冷却/热回收/用水/走廊筛选出现。
- **电力**：Litgrid（TSO）、ESO（配网）、VERT（监管）——只有绑定具名项目/地址/地块才是 A 级设施证据；电网容量（Kruonis/Vilnius/Kaunas/Klaipeda/Siauliai/Panevezys）仅为选址背景。
- **RRT**：电子通信运营商监管背景，非设施登记册。
- **Registru centras**：法人/不动产/地块/已登记建筑证据（免费查询受限，可能需付费摘录）。
- **Invest Lithuania**：官方推广（A），Kruonis 相关；已实现容量仍需运营商/项目/许可证明（C）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- **Telia Lietuva**（telia.lt/ndc）：Raisteniskes/Ukmerges g. 449、Vilnius District 新 DC 在建，投资从 2022 年 EUR 10M 计划升至施工期报道 EUR 26M，2027 年预期服务；与 Telia 两个既有 Vilnius DC 互联。
- **Telecentras**：营销 Tier III colo/hosting；VDC 项目页称建设 4 个政府数据中心（Tier III 可用性要求）；电视塔区 Sausio 13-osios g. 10 为公开位置锚点，保密政府站点地址不得推断。
- **Delska**（前 DLC/Data Inn）：LT DC1 J. Tiskeviciaus g. 72（2 MW/220 racks/Tier III）、LT DC2 T. Sevcenkos g. 16J（2 MW/140 racks/Tier III，RackRay 并入）、LT DC3 A. Juozapaviciaus g. 13（2 MW/180 racks/EN 50600-2）。
- **Bite**：2022-09 在 Data Inn（DLC 运营）开 Tier III 客户环境——租户/服务足迹，按 schema 决定是否单列。
- **Baltneta**：Vilnius 专用 Tier 3 DC、96 机柜；Liepkalnis/Paneriu g. 26 地址需运营商/Infostatyba 确认。
- **Bacloud**：主 DC 在 Siauliai，2006 年起运营（A 级运营商页）。
- **Kaunas 群**：Serveroffer（自有 Kaunas DC colo）、LETAS、Host Baltic（注册线索 C）。
- **Vilnius 中小运营**：Hostline（自有 Vilnius DC + 合作 DC）、VPSnet、Cherry Servers、CSC Telecom——地址/宿主未明前为服务 lead。

## 已知设施/项目与证据状态

| 设施/项目 | 县/地点 | 状态与证据 |
|---|---|---|
| Telia 新 DC | Vilnius County / Vilnius District（Raisteniskes, Ukmerges g. 449） | 在建（EUR 26M 报道），2027 预期服务；A 级项目页，许可待 Infostatyba 补。 |
| Telecentras colo + 4 政府 DC（VDC） | Vilnius（Sausio 13-osios g. 10 公开锚点） | 运营 colo + 政府项目；保密站点不推断地址。 |
| Delska LT DC1 / Data Inn | Vilnius（J. Tiskeviciaus g. 72） | Operational，2 MW/220 racks，Tier III（运营商声明）。 |
| Delska LT DC2 / RackRay | Vilnius（T. Sevcenkos g. 16J） | Operational，2 MW/140 racks，Tier III。 |
| Delska LT DC3 | Vilnius（A. Juozapaviciaus g. 13） | Operational，2 MW/180 racks，EN 50600-2。 |
| Bite 在 Data Inn 的 Tier III 足迹 | Vilnius | 2022 运营，租户/服务部署，非独立建筑。 |
| Baltneta 专用 DC | Vilnius（Liepkalnis/Paneriu g. 26 待核） | 运营/在售，96 机柜；地址待确认。 |
| Bacloud DC | Siauliai County | 运营（2006 起），A 级运营商页。 |
| Serveroffer/LETAS/Host Baltic | Kaunas County | 托管/colo leads；自有 DC 声明需地址/建筑证据。 |
| Kruonis Technology Park | Kaunas County / Kaisiadorys District | siting lead（75 ha、约 200 MW），无锚定租户不计设施。 |

## 更新节奏

- 每批次：重跑运营商页（Telia/Telecentras/Delska/Bite/Baltneta/Bacloud）、Infostatyba/市政验证、Litgrid/ESO/VERT 电力与 DCD/LRT/VZ/施工媒体；盯 Telia Raisteniskes 许可/完工与 Baltneta 地址确认。
- 每季度：重核 hyperscaler 官方区域表；重跑 10 county 逐 municipality 扫描（低产区以 PAV 页为主面）。
- 待办（2026-08-12）：两份 explorer 初稿已完成；下一步 codex terra agent 分批复核（10 county 粒度）；本 skill 作为国家层参考注入。
