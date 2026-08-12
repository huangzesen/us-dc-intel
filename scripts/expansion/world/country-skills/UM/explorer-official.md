# UM 官方渠道探索方法论 - 美国本土外小岛屿 (United States Minor Outlying Islands) 数据中心枚举

Date reviewed: 2026-08-12. Scope: **United States Minor Outlying Islands (UM)**. Manifest division model: **geographical unit**. Repo divisions: **Johnston Atoll 约翰斯顿环礁**, **Midway Islands 中途岛**, **Navassa Island 纳瓦萨岛**, **Wake Island 威克岛**, **Baker Island 贝克岛**, **Howland Island 豪兰岛**, **Jarvis Island 贾维斯岛**, **Kingman Reef 金曼礁**, **Palmyra Atoll 帕尔米拉环礁**.

结论 (baseline conclusion): UM is a **verified-negative commercial data center market**. The task is not normal market discovery; it is a disciplined negative sweep plus monitoring of federal military, refuge, research, airfield, and communications infrastructure that can be confused with data centers.

## 1. 可靠性分级 (Reliability Grades)

- **A** - 一手/官方来源: USFWS and DOI pages, Air Force/PACAF/AFCEC pages, Federal Register, eCFR/US Code/Executive Orders, EPA NEPAccess, USASpending, SAM.gov, FCC ULS/IBFS, NOAA/NWS, USCG NavCen, Census Bureau, IANA, and official cloud region pages.
- **B** - 强二手来源: GAO reports, congressional budget materials, Honolulu Civil Beat, Stars and Stripes, AP/Reuters, Data Center Dynamics, and equivalent named reporting.
- **C** - 仅作线索: data center directories, SEO landing pages, job boards, vendor contact forms, market reports, social posts, and unbuilt proposals.
- **U** - 不可复核传闻: no named operator, no site, no license/permit/contract, or no independent support.

状态词 (required status verbs): `operational`, `under construction`, `planned`, `procurement`, `proposal-only`, `verified-negative`, `decommissioned`.

## 2. 结构性事实 (Structural Facts)

- **无常住商业市场**: UM is a collection of remote U.S. possessions with no ordinary local customer base, no local telecom regulator, no commercial land market, and no island-level data center permit or incentive regime. Census Island Areas releases cover American Samoa, Guam, CNMI, and the U.S. Virgin Islands, not a UM commercial population dataset; for UM, use official refuge/DoD pages plus island-specific staffing evidence rather than extrapolating demand.
- **管理归属**: DOI/USFWS manages the wildlife refuges and monuments; DOI OIA remains a core insular-area surface. Wake is a special case: civil administration flows through federal authority and Air Force/PACAF operation. Midway has transitioned from Navy jurisdiction to USFWS refuge management.
- **保护区限制**: FWS refuge pages repeatedly describe remote, protected, permit-controlled areas. Examples verified in this review: Howland, Johnston, Kingman, Baker, Palmyra, and Midway pages state restricted access or conservation-only/permit-controlled activity; Navassa is described by FWS as uninhabited.
- **军事/科研设施不是数据中心**: Wake airfield, Johnston runway work, Midway/Palmyra refuge operations, USFWS field camps, NOAA/USCG aids, and satellite terminals should be classified as `military-infrastructure`, `refuge-operations`, `research-station-it`, or `communications`, not commercial colocation.
- **云与域名负面**: Official cloud region lists for AWS, Azure, Google Cloud, and Oracle do not list UM regions. IANA shows `.um` as not assigned and not present in the root zone, so the TLD is not evidence of active UM infrastructure.

## 3. 官方来源清单 (Official Source Surfaces)

### 3.1 DOI / USFWS

Use these as the highest-value official surfaces for land status, access rules, refuge operations, and conservation limits.

- DOI OIA islands portal: https://www.doi.gov/oia/islands
- DOI OIA Palmyra page: https://www.doi.gov/oia/islands/palmyraatoll
- Pacific Islands Refuges and Monuments Office: https://www.fws.gov/office/pacific-islands-refuges-and-monuments
- Pacific Remote Islands Marine National Monument / FWS program pages: https://www.fws.gov/
- Papahanaumokuakea Marine National Monument: https://www.papahanaumokuakea.gov/
- FWS refuge pages:
  - https://www.fws.gov/refuge/baker-island
  - https://www.fws.gov/refuge/howland-island
  - https://www.fws.gov/refuge/jarvis-island
  - https://www.fws.gov/refuge/johnston-atoll
  - https://www.fws.gov/refuge/kingman-reef
  - https://www.fws.gov/refuge/midway-atoll
  - https://www.fws.gov/refuge/navassa-island
  - https://www.fws.gov/refuge/palmyra-atoll
  - https://www.fws.gov/refuge/wake-atoll

```text
site:fws.gov/refuge "{division}" ("data center" OR "data centre" OR datacenter OR server OR cloud OR "special use permit" OR construction)
site:fws.gov/refuge "{division}" ("not accessible" OR permit OR "closed to public visitation")
site:doi.gov/oia ("United States Minor Outlying Islands" OR "Palmyra Atoll" OR "Wake Island")
site:papahanaumokuakea.gov Midway permit OR "Midway Atoll"
```

Extraction rule: if the page describes access, conservation, research, staffing, or refuge facilities, record it as official context. Do not create a data center record unless the source names a compute/hosting facility and its operator.

### 3.2 DoD / Air Force / PACAF / AFCEC

Use these for Wake and Johnston military-infrastructure monitoring.

- Air Force news: https://www.af.mil/
- PACAF news: https://www.pacaf.af.mil/
- AFCEC news and environmental/business pages: https://www.afcec.af.mil/
- DoD/Department of War contracts and budget pages: https://www.war.gov/ and https://comptroller.war.gov/
- Federal Register Wake Island Code: https://www.federalregister.gov/documents/2000/10/25/00-27325/wake-island-code
- National Archives Executive Order 11048: https://www.archives.gov/federal-register/codification/executive-order/11048.html

Verified official facts to encode:

- Air Force/PACAF pages describe Wake Island Airfield as a military refueling, training, missile-test, divert, and logistics airfield.
- AFCEC reported an $87 million Wake airfield modernization project for lighting, grounding, pavement markings, and C-17 mission support; this is `military-infrastructure`.
- FY 2027 DoD budget materials include Wake PDI fueling/aircraft-apron infrastructure; this is not data center evidence.

```text
site:af.mil "Wake Island" ("airfield" OR "modernization" OR "data center" OR server)
site:pacaf.af.mil "Wake Island" ("airfield" OR "mission" OR "contractor" OR "data center")
site:afcec.af.mil "Wake Island" ("construction" OR "modernization" OR "environmental")
site:comptroller.war.gov "Wake Island" ("PDI" OR "fueling" OR "aircraft parking" OR "data center")
site:war.gov "Wake Island" ("contract" OR "airfield" OR "data center")
site:federalregister.gov "Wake Island"
```

### 3.3 Federal Databases and Adjacent Agencies

- Federal Register: https://www.federalregister.gov/
- eCFR: https://www.ecfr.gov/
- EPA NEPAccess: https://nepaccess.epa.gov/
- FCC ULS: https://wireless2.fcc.gov/UlsApp/UlsSearch/searchAdvanced.jsp
- FCC IBFS: https://www.fcc.gov/licensing-databases/international-bureau-filing-system-ibfs
- USASpending: https://www.usaspending.gov/
- SAM.gov: https://sam.gov/
- NOAA/NWS: https://www.weather.gov/
- USCG NavCen: https://www.navcen.uscg.gov/
- Census Bureau Island Areas: https://www.census.gov/programs-surveys/decennial-census/decade/2020/2020-island-areas.html
- IANA `.um` record: https://www.iana.org/domains/root/db/um.html

```text
site:federalregister.gov ("Wake Island" OR "Midway Atoll" OR "Johnston Atoll" OR "Palmyra Atoll" OR "Navassa Island")
site:nepaccess.epa.gov ("Wake Island" OR "Johnston Atoll" OR "Midway Atoll" OR "Palmyra Atoll") ("data center" OR server OR compute)
site:usaspending.gov ("Wake Island" OR "Johnston Atoll" OR "Midway Atoll" OR "Palmyra Atoll") ("data center" OR "IT" OR satellite OR construction)
site:sam.gov ("Wake Island" OR "Johnston Atoll" OR "Midway Atoll" OR "Palmyra Atoll") ("data center" OR server OR construction)
site:fcc.gov ("Wake Island" OR "Midway" OR "Johnston" OR "Palmyra") ("earth station" OR IBFS OR cable)
```

### 3.4 Official Cloud Region Pages

These are A-grade negative checks for cloud regions and official provider infrastructure.

- AWS Regions/AZs: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- Microsoft Azure regions: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud locations: https://cloud.google.com/about/locations
- Oracle public cloud regions: https://www.oracle.com/cloud/public-cloud-regions/

Expected result: no `UM`, Wake, Midway, Johnston, Palmyra, or other UM division region. Closest ordinary commercial cloud regions are in continental U.S., Hawaii-adjacent service paths, Guam/Japan/Australia depending on provider and service, but none are UM.

## 4. 分区官方策略 (Per-Division Official Strategy)

### Wake Island 威克岛

Classification: **high monitoring priority, non-commercial**. Primary surfaces are Air Force/PACAF/AFCEC, DoD budgets, Federal Register, SAM.gov, USASpending, FCC, and FWS Wake Atoll refuge pages.

```text
"Wake Island" ("data center" OR "data centre" OR datacenter OR colocation OR hosting OR server)
site:af.mil OR site:pacaf.af.mil "Wake Island" "data center"
site:afcec.af.mil "Wake Island" ("airfield" OR "modernization" OR "PDI")
```

Record Wake airfield, fueling, solar, runway, contractor billeting, and SATCOM as `military-infrastructure` or `communications`. A commercial record requires a named colocation/cloud operator and federal permission or contract evidence.

### Midway Islands 中途岛

Classification: **USFWS refuge operations**. FWS confirms Midway Atoll NWR / Battle of Midway National Memorial and Papahanaumokuakea Monument context; FWS states public visitation is closed and activities must support airfield operations, conservation management, or monument/refuge purposes.

```text
site:fws.gov/refuge/midway-atoll ("data center" OR server OR "special use permit" OR "closed to public")
site:papahanaumokuakea.gov "Midway" permit
"Midway Atoll" ("data center" OR datacenter OR colocation OR hosting)
```

Historical Commercial Pacific Cable assets are `historical-cable-station`, not active data center or cable landing evidence.

### Johnston Atoll 约翰斯顿环礁

Classification: **USFWS refuge plus DoD infrastructure monitoring**. FWS describes Johnston Atoll NWR as isolated and permit-controlled, with military administrative history/jurisdiction context. DoD/PDI runway or logistics work remains `military-infrastructure`.

```text
site:fws.gov/refuge/johnston-atoll ("data center" OR server OR construction OR permit)
"Johnston Atoll" ("data center" OR datacenter OR colocation OR "Pacific Deterrence" OR runway)
site:usaspending.gov "Johnston Atoll"
site:sam.gov "Johnston Atoll"
```

### Navassa Island 纳瓦萨岛

Classification: **verified-negative, extremely low priority**. FWS describes Navassa Island NWR as an uninhabited island between Haiti and Jamaica. Expect no power, telecom, or commercial facility evidence.

```text
site:fws.gov/refuge/navassa-island ("data center" OR server OR facility OR permit)
"Navassa Island" ("data center" OR datacenter OR hosting OR colocation)
```

### Baker / Howland / Jarvis 贝克岛 / 豪兰岛 / 贾维斯岛

Classification: **verified-negative, refuge-only**. FWS pages identify them as national wildlife refuges within the Pacific Remote Islands Marine National Monument system. Howland and similar pages emphasize remote, permit-controlled access; Baker/Jarvis pages show refuge context only.

```text
site:fws.gov/refuge ("Baker Island" OR "Howland Island" OR "Jarvis Island") ("data center" OR server OR construction OR permit)
("Baker Island" OR "Howland Island" OR "Jarvis Island") ("data center" OR datacenter OR colocation OR cloud)
```

### Kingman Reef 金曼礁

Classification: **verified-negative, refuge-only**. FWS describes Kingman Reef NWR as extremely low elevation and remote, with restricted access by special use permit.

```text
site:fws.gov/refuge/kingman-reef ("data center" OR server OR facility OR permit)
"Kingman Reef" ("data center" OR datacenter OR colocation OR facility)
```

### Palmyra Atoll 帕尔米拉环礁

Classification: **research/refuge operations plus proposal-filter target**. DOI OIA confirms Palmyra's special civil-administration context and The Nature Conservancy land ownership; FWS confirms Palmyra Atoll NWR and Pacific Remote Islands Marine National Monument context. Any research station IT is `research-station-it` or `refuge-operations`, not commercial data center.

```text
site:doi.gov/oia "Palmyra Atoll"
site:fws.gov/refuge/palmyra-atoll ("data center" OR server OR research OR permit)
"Palmyra Atoll" ("data center" OR datacenter OR OTEC OR "ocean thermal")
```

The historical Palmyra OTEC/green data center proposal remains `proposal-only` unless supported by NEPA, FWS/DOI permit, named operator, construction, and operating evidence.

## 5. 入档规则 (What Counts)

Positive commercial data center evidence must include all of the following:

- named operator;
- named UM division and physical site;
- facility service such as colocation, racks, hosting, cloud region, edge compute, or managed data center;
- A-grade or operator-primary source proving operation, construction, permit, or contract.

Never count these as data centers:

- Wake or Johnston runway/fueling/solar/logistics projects;
- USFWS refuge offices, field camps, research station IT, biological program staffing, visitor/permit systems;
- NOAA/NWS weather stations, USCG aids to navigation, or FCC-licensed radio/satellite terminals;
- historical cable company structures at Midway/Wake;
- `.um` domain status;
- job-board listings with remote U.S. data center roles tagged to Wake/UM;
- vendor forms listing every ISO country/territory.

## 6. 每次运行核查清单 (Run Checklist)

1. Confirm manifest divisions exactly match the nine geographical units above.
2. Search FWS pages for each division and record refuge/access status.
3. Search Air Force/PACAF/AFCEC/DoD budget surfaces for Wake and Johnston; classify infrastructure correctly.
4. Search Federal Register, NEPAccess, SAM.gov, USASpending, FCC ULS/IBFS for Wake, Johnston, Midway, and Palmyra.
5. Check AWS, Azure, Google Cloud, and Oracle official region lists for UM or named divisions.
6. Check IANA `.um`; current reviewed status is not assigned and not in the root zone.
7. Search the open web for `UM/Wake/Midway/Johnston/Palmyra + data center/datacenter/colocation/hosting`; treat generic jobs, vendor forms, and country dropdowns as false positives.
8. If any positive-looking item appears, require A-grade land/permit/contract or operator evidence before changing from `verified-negative`.

## 7. 更新节奏 (Refresh Cadence)

- **Monthly**: FWS refuge pages/news, Federal Register, DoD/PACAF/AFCEC Wake and Johnston updates, SAM.gov and USASpending.
- **Quarterly**: cloud region pages, IANA `.um`, FCC ULS/IBFS, PeeringDB/DataCenterMap/Cloudscene/Baxtel, and official policy/legal changes.
- **Event-driven**: any headline about Wake/Johnston/Palmyra compute, AI, cloud, runway, energy, or cable activity; any presidential proclamation, act of Congress, or refuge/monument boundary/access change.
