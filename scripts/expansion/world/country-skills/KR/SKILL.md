---
name: kr-datacenter-methodology
location: scripts/expansion/world/country-skills/KR/SKILL.md
description: |
  South Korea (KR) datacenter discovery & audit methodology — how to enumerate, verify, and update Korea datacenter projects across 17 first-level jurisdictions (특별시/광역시/도/특별자치시·도) and 229 local governments (시/군/구). Korea has no single public facility registry: enumeration combines building permits and building-register data (세움터 Seumteo / MOLIT Building HUB APIs), local-government committee minutes, KEPCO/MOTIE power-trail evidence (전기사용예정통지, 전력계통영향평가), MSIT/KISA disaster-management oversight (2022 Kakao/SK C&C outage), official cloud-region pages (AWS/Azure/GCP/OCI/NAVER/Kakao), and operator pages (kt cloud, SK Broadband, LG CNS, LG U+, Samsung SDS, SK C&C, NHN Cloud, KINX, Digital Realty, Equinix, STT GDC). Read this before running KR exploration/audit batches. Routes to explorer-official.md (permits/power/regulator/cloud) and explorer-industry.md (trade press/vendors/regional query patterns).
---

# KR · 韩国数据中心查询方法论（Datacenter Discovery & Audit Methodology）

> 目的：韩国**没有**统一的数据中心设施注册库；枚举需组合**建筑许可/建筑台账（세움터/건축HUB）**、**地方政府委员会纪要**、**电力轨迹（한전/산업통상자원부 대용량 심사）**、**MSIT/KISA 灾难管理监管**、**云区域官方页**与**运营商官方页**。
> 电力稀缺与居民反对使政府推动非首都圈（수도권 外）AI/DC 选址；成熟 수도권 市场与非首都圈新兴园区都要搜。
> 本 skill 汇总两份探索报告（官方管线 + 行业发现），供韩国探索与复核批次使用。

## 入口

| 文件 | 内容 |
|---|---|
| `explorer-official.md` | 官方/监管/云管线：세움터/e-AIS 与 MOLIT 건축HUB/data.go.kr API（229 시/군/구 系统扫描）、地方政府门户与委员会纪要、EIASS 环评、土地/产业园区、한전/MOTIE 电力管线（전기사용예정통지、전력계통영향평가、345kV 여유 변전소）、MSIT/KISA/CSAP、云区域与运营商官方种子、229 division 工作流与分级 |
| `explorer-industry.md` | 行业/厂商发现：ETNews/Digital Daily/ZDNet Korea/Bloter/IT Chosun/KHARN/The Elec/Yonhap/Maeil/DCD/W.Media 媒体、KDCC 协会与 C&W 市场报告、运营商/开发商种子表、区域枚举手册（수도권/강원/세종/충청/대전/경북·대구/경남·부산·울산/전라·광주/제주）、容量与负面词提取、한글 别名表 |

## 核心结构事实（框定每次搜索）

1. **建筑许可尤其重要**：韩国在《건축법 시행령》框架下把 **데이터센터** 增列为 **방송통신시설** 的子用途；但老 DC 仍可能以 업무시설/교육연구시설/공장 等混合用途许可——不要只按 “데이터센터” 过滤。
2. **电力轨迹**：关键线索是 **한전/MOTIE 대용량 전력 심사**、**전기사용예정통지**（约 5MW+ 级预申请路径，存在大量投机/重复申报——弱项目信号，须有供电合同/许可/施工佐证）与 **전력계통영향평가**（분산에너지법 时代新增大负荷评估）；MOTIE 2023 수도권 집중 완화 방안、2026 mega projects 公布 **345kV 계통 여유 변전소** 支持分散。
3. **2022 SK C&C 판교/Kakao 故障后监管加强**：MSIT 指定 주요 방송통신/재난관리 의무 사업자（KT Cloud、LG U+、SK Broadband、Samsung SDS、LG CNS、SK C&C、NAVER Cloud、MS 5673 Korea；门槛≈전산실 22,500 m² 或 사용가능 최대전력 40 MW 且 매출 100 亿韩元以上）——运营商种子，非设施普查。
4. **云区域=运营存在（A），非地址**：AWS `ap-northeast-2` Seoul 4 AZ；Azure Korea Central (Seoul) / Korea South (Busan)；GCP `asia-northeast3` Seoul；OCI `ap-seoul-1` / `ap-chuncheon-1`；NAVER GAK 춘천/세종（세종 超大规模 290,000 m²、60,000+ 服务器、2023-11 运营）；Kakao 안산（한양대 ERICA、47,378 m²、4,000 랙、120,000 服务器、6EB、2024-01 运营）。
5. **容量单位混乱**：`수전용량`（受电容量）≠ IT 부하；`MW/메가와트`、`GW`、`랙/상면`、`서버 수`、`연면적`、`EB` 各是不同度量——按原文记录并区分 IT load 与公用供电容量；100,000+ 服务器多为营销口径。
6. **MOU 通胀**：道级 AI 数据中心公告常报数万亿韩元与远期 MW，土地/电力/许可未落实前不计。
7. 地理：수도권（서울 구로/금천 가산、강남、영등포 여의도、용산、양천 목동；경기 성남 판교·분당、안양 평촌、하남、안산、부천、고양 일산、용인、화성、파주、김포；인천 서구 가좌·원창·청라、송도、남동）最高密度；非首都圈：부산 강서·미음、김해、대전、세종、춘천、예천/경북、구미、울산、전북 새만금/군산、광주·광양、제주。

## 查询模式（复制粘贴模板见 explorer-official.md §1/§4 / explorer-industry.md §4/§5）

- 韩文核心词：`데이터센터` `AI 데이터센터` `인터넷데이터센터` `IDC` `클라우드센터` `전산센터` `방송통신시설` `건축허가` `착공` `준공` `사용승인` `투자협약` `업무협약` `MOU` `수전용량` `전력` `변전소` `송전선로` `교통영향평가` `환경영향평가` `산업단지` `첨단산업단지` `주민반대` `민원`。
- 建筑：`"{시군구}" 데이터센터 건축허가`、`"{시군구}" 데이터센터 착공 OR 준공 OR 사용승인`、`site:{local-gov}.go.kr 데이터센터 건축위원회`、`"{사업명}" 건축허가 OR 착공신고 OR 사용승인`。
- 电力：`데이터센터 전기사용예정통지 한전 "{시군구}"`、`데이터센터 전력계통영향평가 "{시군구}"`、`site:motie.go.kr 데이터센터 전력`、`site:kepco.co.kr 데이터센터 전기공급`、`"{시군구}" 데이터센터 변전소`。
- 监管：`site:msit.go.kr 데이터센터 재난관리`、`site:kisa.or.kr 데이터센터 클라우드 보안인증`、`클라우드 보안인증 CSAP 데이터센터`。
- 行业：`site:etnews.com 데이터센터 {회사}`、`site:ddaily.co.kr 데이터센터 평촌 부천 파주`、`site:zdnet.co.kr "{회사}" "AI 데이터센터"`、`site:yna.co.kr "{시군구}" 데이터센터`、`site:datacenterdynamics.com Korea "{operator}" "data center"`。
- 容量/负面：`"{프로젝트명}" (MW OR 메가와트 OR 수전용량 OR IT부하)`、`"{프로젝트명}" (준공 OR 가동 OR 상업운영)`、`"{프로젝트명}" (무산 OR 취소 OR 철회 OR 보류 OR 주민반대 OR 지연)`。
- 英文回退：`"{city}" Korea "data center" MW`、`"Greater Seoul Area" "data center" pipeline MW`、`"Incheon" "data center" AWS YIDO Cheongna`。

## 官方/监管管线要点（详见 explorer-official.md）

- 建筑台账：세움터/e-AIS（https://www.eais.go.kr，地址/地块手动验证，A）、MOLIT 건축HUB 与 data.go.kr API（건축인허가정보/건축물대장정보/건물에너지정보；229 행정코드 系统查询，按 `데이터센터`/`IDC`/`인터넷데이터센터`/`전산센터`/`클라우드센터`/`AI 데이터센터`/`방송통신시설` 及模糊用途 업무시설/교육연구시설/공장 过滤，A）。
- 地方政府：건축위원회/경관위원회/도시계획위원회 议程与纪要、교통영향평가、주민설명회、고시공고、의회 회의록（争议/停滞项目常在运营商 PR 前暴露，A）。
- 环评/土地：EIASS（https://www.eiass.go.kr；独立 DC 常不触发全量环评，但大型产业园/都市开发/电力设施含 DC 园区时出现，A）；토지매각/산업단지 분양공고（B，绑定许可或 한전 전력 승인 才升 A）。
- 电力：MOTIE（수도권 집중 완화 방안 PDF、11차 전력수급기본계획、2026 345kV 여유 변전소 공개）、한전 전기사용예정통지/전력계통영향평가（A=具名文件，B=可信报纸+具名地址/运营商，C=匿名 “확보된 전력” 声称）。
- 监管/云安全：MSIT 재난관리·보호조치、KISA CSAP（공공부문 클라우드 인증；AWS/GCP/Azure CSAP 官方页为 A）——用于识别受规管 CSP/运营商集合，不是设施证据。
- 云/运营商种子：kt cloud（용산/목동1·2/여의도/분당/강남/남구로/송정/대전/김해/천안/경북/가산）、NAVER GAK、Kakao 안산、LG CNS（상암/부산 글로벌/가산/인천）、SK Broadband（분당 스마트 IDC、서초/일산）、LG U+（평촌 메가센터 165 MW、평촌2 40,450 m²、파주 AI）、Samsung SDS（상암/수원/구미 AI）、SK C&C（판교）、NHN Cloud（광주/김해/순천）、KINX（도곡/가산/분당/과천）、Digital Realty（ICN10 마포·상암 12 MW；김포 구래동 64 MW 2021 宣布需单独核实）、Equinix（SL1/SL2x/SL4，고양 향동）、STT GDC（서울1 가산 30 MW）。

## 行业/厂商发现要点（详见 explorer-industry.md）

- 媒体：ETNews（B，最佳 ICT 贸易源）、Digital Daily（B，云/IDC 专线）、ZDNet Korea（B，AI 基础设施政策）、Bloter（B）、IT Chosun（B）、KHARN（B，HVAC/RE100/KDCC）、The Elec（B）、Yonhap（B+，道级 MOU 发现）、Maeil/Pulse（B，地产/国际资本）、Korea Herald/JoongAng（B，英文）、DCD（B，全球交叉验证）、W.Media（B/C+）。
- 协会/市场：KDCC 한국데이터센터연합회（B+，会员名单与市场报告；部分会员/密码门控）、C&W Seoul Data Centre MarketBeat（B+，수도권 运营 MW/管线）、KESIS（B，全国上下文）。
- 聚合器：DataCenterMap/Baxtel/datacenters.com/OCOLO/Cloudscene = C（地址/邻近设施交叉核对），从不单独用于高置信容量。
- DART（https://dart.fss.or.kr/，A）用于上市公司的 이사회 결의/토지 매입/투자 금액（Samsung SDS、LG U+、KT、SKT/SKB、KINX、Kakao、NAVER 等）。
- 官方-ish 名单：MSIT 재난관리 의무 사업자 명단（A-/B+，运营商种子）；IFEZ/GFEZ/산업단지 官方页（A 公开项目事实；纯招商宣传册 C）。

## 来源分级

- **A** = 官方/一手：세움터/건축HUB 许可与台账记录、地方政府委员会纪要/公告/条例、MOTIE/한전 具名电力记录、EIASS 记录、云区域官方文档（区域/AZ 存在）、运营商官方 DC 页/新闻稿（存在/状态；容量 B）、DART 披露、IFEZ/GFEZ/산업단지 官方项目页。
- **B** = 强二级：KDCC/C&W/JLL/CBRE 具名管线市场报告（B+）、Yonhap 与成熟韩媒（具名场地/开发商/容量）、DCD/W.Media/商业媒体（基于公司声明）。
- **C** = 弱/未验证：DataCenterMap/Baxtel/OCOLO/datacenters.com 单独引用、地产营销 PDF、地方宣传稿、无出处博客、居民传闻。
- 状态语义：`MOU/투자협약/업무협약`=意向；`건축허가`=已批准未动工；`착공/기공식`=在建；`준공/개소/가동/상업운영`=运营（区分整园区 vs 一期）；负面词 `무산/취소/철회/보류/주민반대/지연` 定稿前必查。
- 去重：同一园区可有 landlord、投资 SPV、运营商、云品牌、区昵称、楼名多种称呼；按 地块/地址 + 运营商/租户图 + 供电点 去重。

## 使用流程（探索/复核批次）

1. 读取批次 JSONL（country_code=KR，divisions=17 一级行政区 + 229 시/군/구）。
2. 建运营商种子表：MSIT 재난관리 명단 + KDCC 会员 + NAVER/Kakao/kt cloud/LG U+/SKB/Samsung SDS/LG CNS/SK C&C/NHN/KINX/Digital Realty/Equinix/STT GDC 官方页 + AWS/Azure/GCP/Oracle 区域页。
3. 建 229-division 矩阵，每 division 跑韩文查询（데이터센터/IDC/AI 데이터센터/방송통신시설 + 状态词）。
4. 拉建筑许可/台账证据（건축HUB/data.go.kr API 广搜 + 세움터 地址验证），记录 용도/연면적/허가일/사용승인。
5. 搜地方政府/议会记录（건축위원회/도시계획위원회/교통영향평가/주민설명회/고시공고）。
6. 电力可行性检查：MOTIE/한전 词围绕每个场地；`전기사용예정통지` 仅标 “power-request lead”，除非供电合同/许可进度/施工佐证。
7. 状态判定与负面核查（무산/취소/철회/보류/지연/주민반대）；输出 world 同 schema，容量按原文存单位并区分 IT 부하 vs 수전용량；无项目 division 写 `no_projects: true`。
8. 遵循 NO-DELETION；只创建自己的结果文件。

## 待办（2026-08-12 02:09Z）

- 两份 explorer 初稿完成（explorer-official.md / explorer-industry.md）。
- 下一步：50× codex terra agent（max thinking）每 agent 分批复核韩国数据中心（17 一级行政区 → 229 시/군/구）；本 skill 作为每个 daemon 的国家层参考注入。
- 待核实：구미/당진/예천 등 GW 级大园区需 DART/地方政府分阶段核实；Digital Realty 김포 64 MW 当前状态；Kakao 제2 데이터센터（경기/시흥·하남 传闻）；정부 AI 컴퓨팅 센터 选址落地；전기사용예정통지 投机占比需在批次中标注。
