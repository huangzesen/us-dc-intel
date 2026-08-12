# GU · 关岛数据中心探索方法（官方/监管线路）

范围（manifest 已核实）：`{"country_code":"GU","country_name":"Guam","subnational_type":"country","divisions":["Guam"]}`。GU 只有一个 division：`Guam`。枚举时先做全岛扫描，再按关岛 19 个 villages 做地名扫；Tumon、Harmon、Upper Tumon 属 Tamuning-Tumon-Harmon/Tamuning 语境，不作为独立 division 或独立 village 计数。

本文件是官方/监管线路（official pass）。配套 `explorer-industry.md` 是行业/厂商线路。两份文件对读后再创建、确认或拒绝设施记录。

## 底部结论（Bottom Line）

关岛是美国未建制领地，数据中心枚举要把三类设施分开：

- **商业托管 / Commercial colocation**：GTA、DOCOMO Pacific、IT&E、Guam Exchange/GNC 等有真实托管、机房或 cable landing station + data center 证据。运营商官方页、FCC、SAM.gov、DoD/NAVFAC 官方公告为最高优先级。
- **海缆登陆站 / Cable landing infrastructure**：关岛是西太平洋海缆枢纽，登陆点集中在 Piti、Tanguisson Point、Tumon Bay、Alupang/Agat 等。登陆站默认是电信基础设施；只有来源明确写出 data center、colocation、racks、第三方机柜/电力/冷却时才升级为 DC/colo 候选。
- **国防 / 联邦通信设施**：Andersen AFB、Joint Region Marianas、Marine Corps Base Camp Blaz、NCTS / Guam Telecommunications Site、DISA Pacific 等会出现 data center、communications center、teleport、network operations 线索。计数时单列 `defense/telecom`，不要混入商业 colo。

当前核实结论：AWS、Azure、Google Cloud、Oracle OCI 官方 region/location 列表没有 Guam 云区域；Google 在 Guam 有海缆项目，Cloudflare 等可能有边缘节点，但这些不是云区域，也不能自动推断为可枚举数据中心。

## 可靠性分级（Reliability Grades）

- **A（官方/一手）**：Government of Guam、DOA/GSA procurement、BSP、GPA、PUC、GEDA、Guam notices；FCC cable landing license / IBFS / public notice；SAM.gov；Defense.gov contracts；NAVFAC、CNIC/JRM、Andersen AFB、MCB Camp Blaz、DISA 官方页；运营商或设施运营方官方页；AWS/Azure/GCP/OCI 官方区域页。
- **B（强二级）**：Submarine Networks、TeleGeography Submarine Cable Map、Data Center Dynamics、Pacific Island Times、Pacific Daily News、Guam Daily Post、Marianas Business Journal、Guam Business Magazine、PNC、KUAM，以及有具名方、日期、项目细节的供应商新闻稿转载。
- **C（弱线索）**：DataCenterMap、Cloudscene、Baxtel、Datacenters.com、Inflect、WHTop、PeeringDB、LinkedIn、招聘帖、社交媒体、主机目录。目录可以引导搜索，但不能单独确认设施。

分级作用于**具体声明**。例如 NAVFAC 官方授标确认“communications center upgrades”是 A 级合同证据；若媒体把它称为 data center，则媒体称谓本身只按 B 级处理。

## 1. 关岛政府与公共采购（Government of Guam）

已核实入口：

- Government of Guam portal: https://www.guam.gov/
- Bureau of Statistics and Plans: https://bsp.guam.gov/
- Department of Administration: https://doa.guam.gov/
- General Services Agency procurement portal: https://gsa.doa.guam.gov/
- GSA Invitation for Bid: https://gsa.doa.guam.gov/invitation-for-bid/
- Official notices portal: https://notices.guam.gov/
- Guam Legislature: https://guamlegislature.org/
- Guam courts / code entry point: https://www.guamcourts.org/

官方政府来源可验证：

- 政府采购：server room、disaster recovery、cloud migration、network operations、data center equipment、UPS/generator/HVAC、fiber services。
- 政府 ICT 项目：只有出现地点、运营方/承包方、阶段或采购号时才形成设施候选；泛泛的 cloud/IT modernization 不计数。
- 立法/公告：大型海缆、数据中心招商、电力可行性研究、税收激励、公共听证。

查询模板：

```text
site:guam.gov "data center" OR "datacenter" OR "server room" OR "disaster recovery"
site:bsp.guam.gov "data center" OR "ICT" OR "broadband" OR "submarine cable"
site:doa.guam.gov procurement OR solicitation "data center" OR "server" OR "cloud"
site:gsa.doa.guam.gov "data center" OR "server" OR "network" OR "UPS" OR "generator"
site:notices.guam.gov "data center" OR "cloud" OR "server room" OR "telecommunications"
site:guamlegislature.org "data center" OR "submarine cable" OR "broadband"
```

## 2. 经济发展、能源与公用事业（GEDA / GPA / PUC）

已核实入口：

- Guam Economic Development Authority / Invest Guam: https://www.investguam.com/
- GEDA contact / address page: https://www.investguam.com/contact-us/
- Guam Power Authority: https://www.guampowerauthority.com/
- GPA about page: https://www.guampowerauthority.com/corporate/about-us
- GPA procurement / OpenGovGuam tenders: https://go.opengovguam.com/bids/available/gpa
- Guam Public Utilities Commission: https://guampuc.com/
- Consolidated Commission on Utilities: https://www.guamccu.org/
- Guam Energy Office: https://www.guamenergy.com/

可验证内容：

- GPA 是关岛公用电力系统核心来源；GPA 官方页说明其为 Government of Guam public corporation，费率受 Guam PUC 监管。大型 DC 线索应查 GPA procurement、interconnection、substation、feeder、large load、generation adequacy 与 PUC docket。
- GEDA 可出现数据中心招商、投资激励、Qualified Opportunity Zone / QC 类材料；这些通常是项目背景或政策线索，不能单独确认设施。
- PUC/CCU 可确认费率、供电、utility-level approval；若项目用电规模出现，记录原单位（MW、MVA、kW、kWh），不要换算成 IT MW。

查询模板：

```text
site:investguam.com "data center" OR "digital infrastructure" OR "submarine cable" OR "ICT"
site:guampowerauthority.com "data center" OR "large load" OR "substation" OR "interconnection"
site:go.opengovguam.com/bids/available/gpa "data center" OR "fiber" OR "SCADA" OR "server"
site:guampuc.com "data center" OR "GPA" "large load" OR "rate case" OR docket
site:guamccu.org "data center" OR "broadband" OR "fiber" OR "GPA"
site:guamenergy.com "data center" OR "critical infrastructure" OR "renewable"
"Guam Power Authority" "data centers" OR "data center" OR "large load"
```

## 3. 电信监管与海缆许可（FCC / Cable Landing）

关岛属美国 FCC 管辖。海缆登陆许可、license modification、special temporary authority、foreign ownership / Team Telecom 条件等要以 FCC 和申请方官方材料为 A 级锚点。

已核实入口：

- FCC International Bureau landing license / international: https://www.fcc.gov/international
- FCC public documents: https://docs.fcc.gov/
- FCC IBFS search path: https://licensing.fcc.gov/myibfs/
- TeleGeography Submarine Cable Map, Guam country page: https://www.submarinecablemap.com/country/guam
- Submarine Networks, USA-Guam station page: https://www.submarinenetworks.com/en/stations/north-america/usa-guam

已核实的关键登陆站/项目线索：

- Tanguisson cable landing station：Submarine Networks 列出 CUCN、AAG、AJC、Guam-Philippines；AJC 官方 Guam landing page 说明 Tanguisson 站扩建、电力与空调能力。
- Tumon Bay cable landing station：Submarine Networks 列出 TPC-5、AJC、Pacrim West。
- Tata Piti cable landing station：Submarine Networks 列出 TGN-Pacific、TGN-IA、PPC-1。
- GTA Piti-I / GNC iX：Submarine Networks 列出 SEA-US、JGA South、JGA North、HK-G、SxS 等；GNC iX 明确为 combined neutral cable landing station and data center。
- ATISA：DOCOMO Pacific 官方新闻页确认 FCC 批准 ATISA cable landing license。
- Google subsea projects：Google Cloud 官方博客确认 Proa/Taihei 与 Bulikula/Halaihai 包含 Guam 连接；这些是海缆/连接性线索，不是 Google Cloud region 证据。

查询模板：

```text
site:fcc.gov Guam "cable landing license" OR "submarine cable" OR "IBFS"
site:docs.fcc.gov Guam "cable landing" OR "special temporary authority"
site:submarinecablemap.com/country/guam
site:submarinenetworks.com "Guam" "cable landing station" OR "GNC"
site:ajcable.com Guam "landing points" OR "Tanguisson"
site:docomopacific.com "ATISA" "FCC"
site:aboutus.docomopacific.com "ATISA" "FCC"
site:cloud.google.com/blog Guam Proa OR Taihei OR Bulikula OR Halaihai
```

## 4. 运营商官方设施页（Carrier Official Evidence）

已核实入口：

- GTA data center: https://www.gta.net/data-center
- GTA cable landing station: https://www.gta.net/cable-landing-station
- DOCOMO Pacific business data center colocation: https://business.docomopacific.com/data-center-colocation
- DOCOMO Pacific carrier services: https://business.docomopacific.com/carrier-services
- DOCOMO Pacific network: https://www.docomopacific.com/about-us/network
- IT&E data services: https://shop.ite.net/business/data-services/
- IT&E managed IT services: https://shop.ite.net/business/managed-it-services/
- Guam Exchange colocation: https://guamexchange.com/colocation-services

官方页当前可确认：

- GTA 官方页描述 GU1/GU2 为 Tier 3-designed data centers and cable landing stations，约 11,800 sq ft、2 MW；GU3 规划为 32,000+ sq ft、4 MW，ready for equipment in Q3 2025；GTA CLS 提供 cable station colocation、power services 和到主要 data centers/landing stations 的光纤。
- DOCOMO Pacific 官方 business 页提供 data center colocation，并点名 Agana、Harmon、Piti 三个 secure off-site colocation facilities；carrier services 页写有 power、cooling、security、connectivity 与 SLA。
- IT&E 官方 data services 页写有 co-location and hosting services；若要确认为单一物理设施，需继续用地址、目录和官方联系人交叉核实。
- Guam Exchange 官方页提供 colocation services，并给出地址 `122 West Harmon Industrial Park Rd Ste. 103, Tamuning, 96913, Guam`。它是 A 级运营方页面；容量/面积如果来自 Inflect/DC Byte/Baxtel，仍按 C 或 B/C。

查询模板：

```text
site:gta.net "GU1" OR "GU2" OR "GU3" OR "data center" OR "cable landing station"
site:gta.net "colocation" OR "Tier 3" OR "Piti" OR "Alupang"
site:business.docomopacific.com "Data Center Colocation" OR Agana OR Harmon OR Piti
site:docomopacific.com "ATISA" OR "submarine" OR "network"
site:shop.ite.net/business "co-location" OR "colocation" OR "hosting" OR "data services"
site:guamexchange.com "colocation" OR "data center" OR "Harmon"
```

## 5. 联邦采购与国防设施（Federal / Defense）

已核实入口：

- SAM.gov: https://sam.gov/
- Defense.gov contracts: https://www.defense.gov/News/Contracts/
- DISA: https://www.disa.mil/
- NAVFAC: https://www.navfac.navy.mil/
- NAVFAC Pacific / Marianas public documents: https://pacific.navfac.navy.mil/
- Joint Region Marianas / CNIC: https://www.cnic.navy.mil/
- Andersen AFB: https://www.andersen.af.mil/
- Marine Corps Base Camp Blaz: https://www.mcbblaz.marines.mil/
- USACE Honolulu District: https://www.poh.usace.army.mil/
- Guam National Guard: https://www.guanguard.com/

已核实的国防线索：

- NAVFAC Pacific 2025 官方公告：$289M communications center upgrades in Guam，工程包括 consolidated communications center facility、warehouses、fiber communications cable。官方公告是 A 级；是否计作 data center 需看 solicitation/award 中是否明确 data center 或 IT rooms。
- DCD 2025 报道：US Navy intends to build a data center at Andersen AFB，引用 NAVFAC tender，称两层 reinforced concrete communications center and administrative support space for the 36th Communications Squadron，含 generator building。DCD 为 B；回填时必须找 SAM.gov/NAVFAC 原始 solicitation。
- NAVFAC PA memos 确认 Camp Blaz / Finegayan 与 former Naval Base Guam Telecommunications Site 的位置语境；这些是地理和工程背景，不等同 DC 证据。
- DISA 官方站点可作为组织与服务来源；关岛具体设施需 SAM.gov、Defense.gov、NAVFAC 或 DISA local office/contract 文件确认。

查询模板：

```text
site:sam.gov "Guam" "data center" OR "datacenter" OR "communications center"
site:sam.gov "Guam" "teleport" OR "satellite communications" OR "network operations"
site:defense.gov/News/Contracts "Guam" "data center" OR "communications center" OR "teleport"
site:navfac.navy.mil Guam "communications center" OR "data center" OR "fiber communications"
site:pacific.navfac.navy.mil Guam "Camp Blaz" "telecommunications" OR "communications"
site:andersen.af.mil "communications" OR "data center" OR "36th Communications Squadron"
site:mcbblaz.marines.mil "communications" OR "network" OR "data center"
"NCTS Guam" OR "Naval Computer and Telecommunications Station Guam" "data" OR "network"
"DISA Pacific" Guam "network" OR "data center" OR "teleport"
```

## 6. 云区域与边缘（Cloud Regions / Edge）

已核实官方入口：

- AWS Global Infrastructure / Regions and AZs: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- AWS global infrastructure overview: https://aws.amazon.com/about-aws/global-infrastructure/
- Azure regions list: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Azure geographies: https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies
- Google Cloud locations: https://cloud.google.com/about/locations
- Google data center locations: https://datacenters.google/locations
- Oracle OCI regions: https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm
- Cloudflare Guam deployment: https://blog.cloudflare.com/cloudflare-deployment-in-guam/

规则：

- 官方 region/location 列表没有 Guam 时，记录为 A 级负向证据：无 AWS/Azure/GCP/OCI Guam cloud region。
- Cloudflare Guam deployment 是官方边缘节点证据，可记作 CDN/edge PoP 线索；不要把它扩展为独立商业 data center，除非来源提供设施运营方、地址、机柜或 colo 语言。
- Google 在 Guam 的海缆项目只证明 connectivity/subsea landing 线索，不证明 Google Cloud region 或 Google-owned data center。

查询模板：

```text
site:aws.amazon.com Guam "region" OR "local zone" OR "wavelength"
site:learn.microsoft.com/azure Guam "region" OR "geography"
site:cloud.google.com/about/locations Guam OR "Northern Mariana" OR "Pacific"
site:datacenters.google Guam
site:docs.oracle.com/iaas Guam "region"
site:cloudflare.com Guam "deployment" OR "network"
site:blog.cloudflare.com Guam "deployment" OR "network"
```

## 7. Division 与 19 Villages 覆盖

Manifest division 只有 `Guam`。为了避免漏扫，将全岛按官方 19 villages 做二级搜索：

```text
Agana Heights
Agat / Hågat
Asan-Maina
Barrigada
Chalan Pago-Ordot
Dededo
Hagåtña / Hagatna / Agana
Inalåhan / Inarajan
Malesso' / Merizo
Mangilao
Mongmong-Toto-Maite
Piti
Sånta Rita-Sumai / Santa Rita
Sinajana
Talo'fo'fo / Talofofo
Tamuning / Tamuning-Tumon-Harmon / Tumon / Harmon
Humåtak / Umatac
Yigo
Yona
```

全岛模板：

```text
"Guam" "data center" OR "datacenter" OR "colocation" OR "server hosting" -Guamá -ship -registry
"Guam" "cable landing station" OR "international gateway" OR "neutral cable landing"
"Guam" "communications center" OR "teleport" OR "satellite earth station" OR "network operations"
"Guam" "GPA" "data center" OR "large load" OR "substation"
"Guam" "government" "server room" OR "disaster recovery" OR "cloud migration"
```

Village 模板：

```text
"{village}" "Guam" "data center" OR "datacenter" OR "colocation" OR "server room"
"{village}" "Guam" "landing station" OR "central office" OR "exchange" OR "gateway"
"{village}" "Guam" "teleport" OR "communications center" OR "fiber"
"{village}" "Guam" "GPA" "substation" OR "large load" OR "feeder"
site:guam.gov "{village}" "data center" OR "server" OR "ICT"
```

高优先级地名：

- **Piti**：GTA Piti-I、GNC iX、Tata Piti、GPA/Cabras/Piti 电力语境。
- **Tamuning / Harmon / Tumon**：Guam Exchange、运营商办公室/机房、Tanguisson/Tumon Bay 周边、商业 ICT。
- **Hagåtña / Agana**：政府 ICT、DOCOMO colocation location label。
- **Yigo / Andersen AFB**：空军通信、可能的数据中心/communications center。
- **Dededo / Finegayan**：Camp Blaz、NCTS / telecommunications site。
- **Santa Rita / Agat**：Naval Base Guam 与新海缆 landing point 语境。

## 8. 枚举规则与噪声过滤

1. 每条设施候选必须记录：规范名、别名、运营方/业主、村庄或可定位地址、设施类别、状态、证据 URL、证据等级。
2. 商业 colo 需有运营方/官方页或一手材料写明 colocation、data center、hosting、racks、power/cooling/security 等语言。
3. Cable landing station 默认归 `telecom/landing`；只有明确托管服务或 combined CLS + DC 才可列为 DC/colo 候选。
4. 军事设施归 `defense/telecom`；公开资料不足时用基地/项目名，不猜测机房坐标。
5. 政府 cloud、CDN edge、satellite terminal、retail broadband、cell tower、FTTH、office IT、university lab 默认不计 DC。
6. 目录来源（DataCenterMap、Baxtel、Inflect、Cloudscene）只作 C 级线索，必须回到运营方、FCC、SAM.gov、Defense.gov 或 NAVFAC 验证。
7. 无项目 village 需要保留负向搜索轨迹，至少覆盖 DC/colo、landing/exchange、government/utility 三类模板。

噪声过滤：

```text
-Guamá -Cuba -vessel -registry -"Guam ship" -"Guam airport" -flight -hotel -resort
```

## 观察清单（Watch List）

```text
site:gta.net "GU3" OR "new data center" OR "commissioned"
site:guamexchange.com "new data center" OR "commissioned" OR "Harmon"
site:business.docomopacific.com "colocation" OR "data center"
site:shop.ite.net "colocation" OR "data center"
site:fcc.gov Guam "cable landing license" "Google" OR "Bulikula" OR "Proa"
site:docs.fcc.gov Guam "cable landing license" "Google" OR "Bulikula" OR "Proa"
site:sam.gov "Guam" "communications center" OR "data center" OR "teleport"
site:defense.gov/News/Contracts "Guam" "communications center" OR "data center"
site:navfac.navy.mil Guam "communications center" OR "fiber communications"
site:guampowerauthority.com "data center" OR "large load"
site:guampuc.com "data center" OR "large load"
"Guam" "data center" "opened" OR "ready for equipment" OR "commissioned"
```
