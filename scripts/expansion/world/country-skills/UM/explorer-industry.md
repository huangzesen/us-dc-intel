# UM 行业渠道探索方法论 - 美国本土外小岛屿 (United States Minor Outlying Islands) 数据中心枚举

Date reviewed: 2026-08-12. Scope: **UM**. Manifest division model: **geographical unit**. Divisions: Johnston Atoll, Midway Islands, Navassa Island, Wake Island, Baker Island, Howland Island, Jarvis Island, Kingman Reef, Palmyra Atoll. Angle: industry, operator, procurement, directories, connectivity, and proposal filtering.

行业侧结论 (industry conclusion): there is **no verified commercial colocation, hyperscale, cloud-region, carrier-hotel, or retail data center market in UM**. The only meaningful pipeline to monitor is federal infrastructure: Wake military airfield/logistics, Johnston military/runway work, USFWS refuge operations, Palmyra/Midway research support, and satellite communications.

## 1. 可靠性分级 (Reliability Grades)

- **A** - operator/government primary: Air Force, PACAF, AFCEC, DoD budget/contract pages, SAM.gov, USASpending, USFWS/DOI, FCC ULS/IBFS, official cloud region pages, IANA, and named submarine cable operator pages.
- **B** - strong secondary: Honolulu Civil Beat, Stars and Stripes, AP/Reuters, Data Center Dynamics, Data Center Knowledge, TeleGeography/Submarine Cable Map, GAO, and named congressional budget reporting.
- **C** - weak lead: data center directories, cloud/contact forms, job boards, SEO country pages, market reports, social media, and old proposal coverage without permits or construction.
- **U** - rumor: no operator, no site, no dated source, or no independent confirmation.

Use the status verbs `operational`, `under construction`, `planned`, `procurement`, `proposal-only`, `verified-negative`, and `decommissioned`.

## 2. 市场现实 (Market Reality)

- **Demand filter**: UM has no ordinary city/enterprise market, no resident customer base, no local ISP ecosystem, and no local data center permitting/incentive agency.
- **Power filter**: island power is mission microgrid/generator/solar scale, not commercial multi-MW utility service. A multi-MW UM data center would require visible federal land, environmental, energy, and logistics approvals.
- **Connectivity filter**: present-day connectivity is expected to be satellite or federal mission communications. Historical Midway/Wake cable assets do not indicate current cable landing or data center service.
- **Land-use filter**: most divisions are USFWS refuges/monuments with restricted access. Commercial development is structurally incompatible absent a major federal legal/policy change.
- **Cloud filter**: AWS, Azure, Google Cloud, and Oracle official region lists show no UM region. Do not infer edge/cloud presence from U.S. region availability.

## 3. 行业源与使用方法 (Industry Sources and Use)

### 3.1 目录与互联数据库 - 负面核验工具

These sources are useful for false-positive detection and negative confirmation, but they are not enough to prove a facility without primary evidence.

- PeeringDB: https://www.peeringdb.com/
- DataCenterMap: https://www.datacentermap.com/
- Cloudscene: https://cloudscene.com/
- Baxtel: https://www.baxtel.com/
- Submarine Cable Map: https://www.submarinecablemap.com/
- TeleGeography cable references: https://www2.telegeography.com/
- IANA `.um`: https://www.iana.org/domains/root/db/um.html

```text
"United States Minor Outlying Islands" (colocation OR colo OR "rack space" OR "carrier hotel" OR "internet exchange")
"Wake Island" ("data center" OR datacenter OR colocation OR hosting OR "internet exchange")
"Midway Atoll" ("data center" OR datacenter OR colocation OR hosting OR cable)
"Johnston Atoll" ("data center" OR datacenter OR colocation OR hosting)
"Palmyra Atoll" ("data center" OR datacenter OR colocation OR hosting OR OTEC)
site:peeringdb.com ("United States Minor Outlying" OR "Wake Island" OR Palmyra OR Midway)
site:datacentermap.com ("United States Minor Outlying" OR "Wake Island" OR Palmyra OR Midway)
site:cloudscene.com ("United States Minor Outlying" OR "Wake Island" OR Palmyra OR Midway)
site:baxtel.com ("United States Minor Outlying" OR "Wake Island" OR Palmyra OR Midway)
```

Expected result: zero verified UM facilities. If a directory returns a generic country page or a remote job listing, mark it `C false-positive`.

### 3.2 云区域官方页 - 必查负面项

| Provider | Official source | UM handling |
|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | No UM region/AZ/local zone found in reviewed official list. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No UM public cloud region found in reviewed official list. |
| Google Cloud | https://cloud.google.com/about/locations | No UM region/zone found in reviewed official locations. |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ | No UM public cloud region found in reviewed official list. |

Do not count U.S. West, U.S. East, Hawaii-serving networks, Guam/Japan/Australia regions, CDN country coverage, or country selectors as UM facilities.

### 3.3 DoD / Military Infrastructure Pipeline

The strongest industry-adjacent activity is military construction, not commercial data center development.

- Air Force / PACAF / AFCEC: Wake Island Airfield operations, modernization, mission support, environmental work.
- DoD budget: PDI-related Wake fueling and aircraft-apron infrastructure; possible Johnston runway/logistics work.
- SAM.gov and USASpending: contract opportunities and awards by place of performance.
- Federal Register / NEPAccess: regulatory and environmental notices.

```text
site:af.mil OR site:pacaf.af.mil "Wake Island" ("construction" OR "modernization" OR "data center")
site:afcec.af.mil "Wake Island" ("airfield" OR "environmental" OR "modernization")
site:comptroller.war.gov ("Wake Island" OR "Johnston Atoll") ("PDI" OR "MILCON" OR "data center")
site:sam.gov ("Wake Island" OR "Johnston Atoll") ("data center" OR "information technology" OR satellite OR generator OR construction)
site:usaspending.gov ("Wake Island" OR "Johnston Atoll") ("data center" OR IT OR satellite OR construction)
```

Classify runway, apron, fueling, billeting, environmental, logistics, solar, diesel, and SATCOM work as `military-infrastructure` or `communications`. Upgrade to `commercial-colo` only with a named operator and federal authorization for hosting/colocation service.

### 3.4 USFWS / Research Operations Pipeline

Relevant but non-commercial surfaces:

- FWS refuge pages and news for Midway, Johnston, Palmyra, Baker, Howland, Jarvis, Kingman, Navassa, Wake.
- DOI OIA Palmyra page for civil-administration and The Nature Conservancy ownership context.
- Papahanaumokuakea permitting for Midway.
- TNC/Palmyra research references only as supporting context, not facility proof unless paired with FWS/DOI.

```text
site:fws.gov/refuge "{division}" ("server" OR "IT" OR "communications" OR "data center" OR research OR permit)
site:doi.gov/oia "Palmyra Atoll" ("Nature Conservancy" OR "civil administrator")
"Palmyra Atoll Research Station" (server OR satellite OR "data center" OR communications)
"Midway Atoll" ("server" OR "communications" OR satellite OR "data center")
```

Research station IT, field communications, conservation monitoring, and visitor/permit systems are `research-station-it`, `refuge-operations`, or `communications`, not commercial data centers.

### 3.5 Industry Media / Proposal Monitoring

Use B/C sources to catch old or emerging narratives, then verify through primary records.

- Data Center Dynamics: https://www.datacenterdynamics.com/
- Data Center Knowledge: https://www.datacenterknowledge.com/
- Honolulu Civil Beat: https://www.civilbeat.org/
- Stars and Stripes: https://www.stripes.com/
- AP/Reuters and other named reporting for DoD Pacific infrastructure.

```text
site:datacenterdynamics.com (Wake OR Midway OR Johnston OR Palmyra OR "Minor Outlying")
site:datacenterknowledge.com (Wake OR Midway OR Johnston OR Palmyra OR "Minor Outlying")
site:civilbeat.org ("Wake Island" OR "Johnston Atoll") ("runway" OR "military" OR "data center")
site:stripes.com ("Wake Island" OR "Johnston Atoll") ("runway" OR "military" OR "data center")
"Palmyra" (OTEC OR "ocean thermal" OR "green data center" OR datacenter)
```

Palmyra OTEC/green data center coverage from circa 2010-2011 is a known `proposal-only` false-positive family. It remains unbuilt unless supported by current NEPA, USFWS/DOI permit, construction, and operator evidence.

## 4. 分区行业策略 (Per-Division Strategy)

| Division | Priority | Industry interpretation | Upgrade threshold |
|---|---:|---|---|
| Wake Island | High | USAF airfield, refueling, training, missile-test support, contractors, power/communications. | Only upgrade if a named data center/colo/cloud operator appears with DoD/federal land or contract evidence. |
| Johnston Atoll | High | USFWS refuge plus possible DoD runway/logistics/PDI monitoring. | Runway/logistics stay `military-infrastructure`; compute claims need federal primary proof. |
| Midway Islands | Medium | USFWS refuge, memorial, airfield support, historical cable structures, rotating biological staff. | Refuge IT only; commercial claim needs operator + permit/contract. |
| Palmyra Atoll | Medium | USFWS/TNC research context and old OTEC data center proposal filtering. | Research IT is non-commercial; proposal upgrades only with NEPA/permit/construction. |
| Navassa Island | Very low | FWS uninhabited refuge, no ordinary facilities. | Any named facility requires FWS/DOI or federal contract proof. |
| Baker Island | Very low | FWS refuge, restricted/permit-only context. | Same. |
| Howland Island | Very low | FWS refuge, explicitly uninhabited and permit-controlled. | Same. |
| Jarvis Island | Very low | FWS refuge and monument context. | Same. |
| Kingman Reef | Very low | FWS reef/refuge, very low elevation, permit-controlled. | Same. |

## 5. 候选记录字段 (Candidate Record Fields)

```text
country_code: UM
division: Johnston Atoll | Midway Islands | Navassa Island | Wake Island | Baker Island | Howland Island | Jarvis Island | Kingman Reef | Palmyra Atoll | Unknown UM
facility_or_project_name:
operator:
facility_type: military-infrastructure | refuge-operations | research-station-it | communications-earth-station | historical-cable-station | commercial-colo | cloud-region | proposal-only | verified-negative
status: operational | under construction | planned | procurement | proposal-only | verified-negative | decommissioned
capacity_or_scale:
power:
connectivity:
evidence_grade: A | B | C | U
primary_urls:
secondary_urls:
site_address:
coordinates:
notes:
last_checked: 2026-08-12
```

Minimum positive standard: named operator + named physical site + service/function + A-grade or operator-primary evidence. If any field is missing, keep as lead or false positive.

## 6. 已验证负面与误报清单 (Verified Negatives / False Positives)

- **Commercial colo/hosting**: no verified UM commercial provider found in official or open-web searches reviewed on 2026-08-12.
- **Cloud regions**: no AWS, Azure, Google Cloud, or Oracle official UM region.
- **`.um` TLD**: IANA lists `.um` as not assigned and absent from the root zone; this supports non-operational domain infrastructure, not a facility.
- **Job boards**: Wake/UM data center job pages usually reflect remote U.S. roles, generic location tagging, or scraped listings; classify C unless the employer names a UM facility.
- **Vendor country dropdowns**: Iron Mountain, NTT, coatings/cooling vendors, and similar pages may list UM/Wake in forms; these are market coverage forms, not facilities.
- **Military projects**: Wake airfield modernization, fueling, apron, billeting, solar/diesel, and Johnston runway/logistics work are not data centers.
- **Research/refuge IT**: Palmyra/Midway servers, radios, field science equipment, and visitor/permit systems are non-commercial.
- **Historical cable structures**: Commercial Pacific Cable history at Midway/Wake is `historical-cable-station`, not current colocation.
- **Palmyra OTEC proposal**: keep as `proposal-only` unless primary records prove current construction/operation.

## 7. 推荐检查顺序 (Recommended Sweep Order)

1. Confirm nine manifest divisions.
2. Run commercial keyword sweep for UM plus each division.
3. Check AWS/Azure/GCP/OCI official region pages.
4. Check PeeringDB, DataCenterMap, Cloudscene, Baxtel, and Submarine Cable Map.
5. Check IANA `.um`.
6. Sweep Wake and Johnston through Air Force/PACAF/AFCEC, DoD budget, SAM.gov, USASpending, Federal Register, and NEPAccess.
7. Sweep all FWS refuge pages for access, operations, research, communications, and construction.
8. Review industry media only after official negative/positive checks, and downgrade unsupported items to C/U.

## 8. 中文检索 (Chinese-Language Noise Sweep)

Chinese results are useful only as C-grade leads unless they link back to U.S. official or named operator evidence.

```text
"美国本土外小岛屿" ("数据中心" OR "算力" OR "云" OR "托管" OR "机房")
"威克岛" ("数据中心" OR "算力" OR "美军" OR "机场" OR "能源")
"中途岛" ("数据中心" OR "海底电缆" OR "机房" OR "保护区")
"约翰斯顿环礁" ("数据中心" OR "跑道" OR "太平洋威慑")
"帕尔米拉环礁" ("数据中心" OR "绿色" OR "海洋温差" OR OTEC)
```

Do not promote Chinese media claims unless they identify a UM site and can be reconciled to USFWS/DOI/DoD/FCC/contract records.

## 9. 更新节奏 (Refresh Cadence)

- **Monthly**: Wake/Johnston DoD project surfaces, FWS news, Federal Register, SAM.gov, USASpending.
- **Quarterly**: cloud region pages, IANA `.um`, PeeringDB/directories, FCC ULS/IBFS, Submarine Cable Map.
- **Event-driven**: any UM compute/AI/data center headline, any Palmyra OTEC revival, any new Wake/Johnston energy or communications award, or any refuge/monument legal change.
