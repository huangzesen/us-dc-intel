# WS Explorer Industry - Samoa Datacenter Enumeration via Industry/Vendor Sources

Date: 2026-08-12. Scope: Independent State of Samoa (WS), all 11 districts: A'ana, Aiga-i-le-Tai, Atua, Fa'asaleleaga, Gaga'emauga, Gagaifomauga, Palauli, Satupa'itea, Tuamasaga, Va'a-o-Fonoti, Vaisigano. Angle: industry/vendor discovery for commercial datacenters, hosting/colo, telecom facilities, cable stations, cloud/vendor signals, and false positives.

Reliability grades used by this explorer: **A** = operator/vendor official page, regulator license list/order, SOE page, cloud-provider official region page, official project document; **B** = reputable trade/local/regional press, operator interview, contractor case study, multilateral project page; **C** = directories, cable trackers, PeeringDB/ASN aggregators, LinkedIn/social posts, reseller/SEO pages, market-report snippets. Grade C is lead-only unless independently anchored.

## 0. Verified Industry Baseline

- No Samoa company was found publicly selling neutral rack colocation, tiered datacenter services, or hyperscale capacity. The closest verified facility-grade assets are SSCC cable stations with RIO-based access/interconnection and telecom/ISP premises in Apia.
- Vendor/operator leads concentrate in **Apia / Tuamasaga**: SamoaTel, Digicel Samoa/Telstra Pacific, Vodafone Samoa, CSL, BlueWave, banks, and government ICT. The only non-Apia A-grade telecom facility lead is **SSCC Tuasivi** in **Fa'asaleleaga**.
- The Government of Samoa data-center project under World Bank DCRSP P180807 is a public-sector build/upgrade lead, not an industry colocation market signal.
- Starlink Samoa Ltd, CSL/Digicel/Vodafone Starlink retail, Kacific/SES/O3b-style satellite service, towers, Wi-Fi, and cable landing stations are connectivity/telecom assets. Do not count them as datacenters unless a primary source explicitly describes hosting, compute, racks, DR, or colocation.
- Use English queries first. Search both `data center` and `data centre`, plus `datacenter`, `colo`, `colocation`, `co-location`, `hosting`, `server`, `backup`, `cloud`, `IXP`, `cable station`, `landing station`, `NOC`, `switch`, and `facility access`.

## 1. Industry Source Map And Grades

| Source / player | URL | Use | Grade |
|---|---|---|---|
| Samoa Submarine Cable Company (SSCC) | https://www.ssccsamoa.com/ ; RIO page https://www.ssccsamoa.com/about/rio-reference-interconnection-offer/ ; RIO 2026 PDF https://www.ssccsamoa.com/wp-content/uploads/2026/03/Rio-2026.pdf | Wholesale capacity, IRU, FAA, cable-station access, Apia/Tuasivi facility definitions, strongest colo-adjacent evidence. | A |
| OOTR telecom orders/licensees | https://www.regulator.gov.ws/index.php/telecommunications-regulation/telecommunications/telecommunications-orders ; https://regulator.gov.ws/images/Telecommunications_Licensing_Rule/List-of-Telecommunications-Licensees-Final-2022_v3.pdf | Official licensed-provider list and RIO/tariff orders; validates operator existence/status. | A |
| SamoaTel | https://samoatel.ws/ (verify live) plus OOTR/government sources | Incumbent/state telecom lead for fixed/mobile/internet/gateway/switch facilities in Apia. | A for official pages/license; B/C for inferred facilities |
| Digicel Samoa / Telstra Pacific | https://www.digicelpacific.com/news/telstra-acquires-digicel-pacific ; Samoa location from Digicel site | Mobile operator core/network facilities; Telstra acquisition context; Starlink approved reseller per Samoa government release. | A for operator/acquisition; B/C for facilities |
| Vodafone Samoa | OOTR orders/licensee list plus `Vodafone Samoa` web search; do not rely on `vodafone.ws` unless it resolves during the run | Mobile/fixed broadband operator; ex-BlueSky lineage; approved Starlink reseller per Samoa government release. | A for official/license; B/C for facilities |
| CSL / Computer Services Limited | https://csl.ws/ ; press category https://csl.ws/category/press-release/ | Locally owned ISP/ICT firm; services include broadband, website development, ICT procurement, backups, software, network infrastructure, .ws domains, Starlink retail. | A for official services; C/B until facility is named |
| BlueWave | OOTR licensee list/orders; local press | WISP/ISP lead; check license status and compliance orders. | A for license; B/C for facility inference |
| Starlink Samoa Ltd | https://www.samoagovt.ws/2025/01/press-release-starlink-samoa-cheapest-tariff-in-the-world/ ; https://www.starlink.com/ | Licensed satellite internet service and equipment sales; negative-control for connectivity-only claims. | A for license/government press; not DC |
| World Bank DCRSP / MCIT | https://mcit.gov.ws/publications/digital-samoa/ ; https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099093024135596945 | Government data-center project and procurement watch. | A |
| EPC | https://www.epc.ws/ | Power feasibility and large-load sanity check. | A |
| Samoa Business Registry | https://www.businessregistries.gov.ws/ | Legal-entity confirmation for operators/resellers/project vehicles. | A |
| Submarine Networks | https://www.submarinenetworks.com/en/systems/australia-usa/tui-samoa ; https://www.submarinenetworks.com/en/systems/australia-usa/manatua/manatua-cable-lay-operations-complete | Route/capacity/date context for Tui-Samoa and Manatua. | B |
| ADB Samoa Submarine Cable Project | https://www.adb.org/projects/47320-001/main | Tui-Samoa official launch date and project context. | B/A depending document |
| Local/trade press | Samoa Observer, Samoa Global News, RNZ Pacific, Islands Business, Radio Polynesia, Data Center Dynamics | Cable outages, operator changes, Starlink/reseller issues, tenders, interviews. | B |
| Directories/cable trackers | Search `site:datacentermap.com Samoa OR Apia`; Cloudscene, datacenters.com, geocables, cablestatus, submarinecablemap | Negative controls and route leads. | C |

## 2. Operator And Vendor Sweep

### 2.1 SSCC - wholesale cable/interconnection

Verified industry relevance:

- SSCC publicly offers Leased Capacity, IRU, and Facility Access Agreements. Its 2026 RIO includes access guidelines for colocation/interconnection services and names cable stations at Apia and Tuasivi.
- Treat SSCC facilities as `colo_adjacent_telecom` or `telecom_cable_station`. They can support customer equipment/interconnection, but they are not evidence of a retail multi-tenant datacenter market.

Queries:

```text
site:ssccsamoa.com (RIO OR "Reference Interconnection Offer" OR "Facility Access" OR FAA OR colocation OR interconnection)
site:ssccsamoa.com ("Cable Station" OR "Cable Landing Station" OR CLS OR Apia OR Tuasivi OR Savai'i)
"SSCC" Samoa ("Facility Access" OR colocation OR "data center" OR "data centre" OR "cable station")
"Tui-Samoa" OR "Tui Samoa" (Apia OR Tuasivi OR Savai'i) ("landing station" OR "cable station")
"Manatua" Samoa Apia (landing OR RFS OR "cable station")
```

### 2.2 SamoaTel

Verified industry relevance:

- SamoaTel is a high-priority incumbent/state-telecom lead, but the live site may be sparse or unstable. Use OOTR licensee lists/orders, government pages, SamoaTel official channels, and reliable local press to confirm services and facilities.
- Record as a facility only with primary/strong evidence for a switch, gateway, NOC, hosting platform, or server room. Consumer web/email hosting is not enough by itself.

Queries:

```text
site:samoatel.ws (hosting OR server OR cloud OR "data" OR business OR enterprise OR NOC OR switch)
"SamoaTel" (Apia OR Maluafou OR Savalalo) (gateway OR switch OR NOC OR server OR hosting OR "data centre" OR "data center")
"SamoaTel" "Office of the Regulator" license OR licence OR annual report
```

### 2.3 Digicel Samoa / Telstra Pacific

Verified industry relevance:

- Digicel Pacific says Telstra completed the Digicel Pacific acquisition on 14 July 2022 and that the business operates in Samoa among six South Pacific markets.
- Treat Digicel Samoa as a mobile/network-core lead in Apia and as an approved Starlink reseller. Do not infer datacenter services from mobile broadband, app, or tower pages.

Queries:

```text
site:digicelpacific.com Samoa (enterprise OR business OR cloud OR hosting OR network OR "data")
site:digicelpacific.com Samoa "Telstra" OR "Digicel Pacific"
"Digicel Samoa" ("data center" OR "data centre" OR NOC OR switch OR hosting OR cloud OR server)
"Digicel Samoa" Starlink reseller Samoa
```

### 2.4 Vodafone Samoa

Verified industry relevance:

- Vodafone Samoa is an operator/licensee and Starlink-approved reseller per the Samoa government Starlink release. Use OOTR orders for official status and a fresh Vodafone Samoa web search for current service pages.
- Network core/switch sites are likely in Apia but should remain B/C facility inference without primary evidence.

Queries:

```text
site:vodafone.ws Samoa (business OR enterprise OR cloud OR hosting OR server OR network OR "data")
"Vodafone Samoa" ("data center" OR "data centre" OR NOC OR switch OR hosting OR cloud OR server)
"Vodafone Samoa" "Office of the Regulator" license OR licence OR tariff
"Vodafone Samoa" Starlink reseller Samoa
```

### 2.5 CSL / Computer Services Limited

Verified industry relevance:

- CSL's official site describes a locally owned ISP and lists broadband internet, website development, ICT procurement, backup solutions, software development, network infrastructure, .ws domains, and Starlink services.
- CSL is the best private hosting/managed-services lead, but its public pages do not by themselves prove a datacenter. Grade a physical facility C/B unless CSL or another primary source names server rooms, hosted infrastructure, backup/DR facility, or colocation.

Queries:

```text
site:csl.ws (hosting OR host OR server OR backup OR backups OR cloud OR "data center" OR "data centre" OR colocation)
site:csl.ws Starlink OR "Press Release" OR "Network Infrastructure" OR "Backups Solutions"
"Computer Services Limited" Samoa (hosting OR server OR cloud OR backup OR "data center" OR "data centre")
"CSL Samoa" AS38227 OR PeeringDB OR "Computer Services Limited" ISP
```

### 2.6 BlueWave and smaller ISPs

Use OOTR licensee lists and orders first, then local press. Small WISP/ISP equipment shelters, towers, and head-end rooms are not DCs.

```text
"BlueWave" Samoa (license OR licence OR OOTR OR "Office of the Regulator" OR compliance)
"BlueWave Wireless" Samoa (server OR hosting OR NOC OR "data center" OR "data centre")
site:regulator.gov.ws BlueWave OR "Samoa Broadband" OR "Lesa's Telephone"
```

### 2.7 Enterprise and public-sector server-room leads

Potential leads: Central Bank of Samoa, Samoa Bureau of Statistics, Samoa National Provident Fund, ANZ Samoa, BSP Samoa, National University of Samoa, USP Alafua, major hotels/airline/airport systems. These are normally internal server rooms or cloud consumers.

```text
"Central Bank of Samoa" ("data centre" OR "data center" OR "disaster recovery" OR "IT infrastructure" OR server)
"Samoa Bureau of Statistics" (server OR "data center" OR "data centre" OR cloud OR CAPI)
"Samoa National Provident Fund" ("data centre" OR "data center" OR "disaster recovery" OR ICT)
"ANZ Samoa" OR "BSP Samoa" ("data centre" OR "data center" OR "disaster recovery" OR server)
"National University of Samoa" OR "USP Alafua" (server OR "data centre" OR network OR hosting)
```

Record only when a source identifies a physical facility/site/function. Otherwise mark as `enterprise_server_room_lead` and skip facility inventory.

## 3. Trade Press, Directories, And Negative Controls

High-value press/directories:

- Samoa Observer: https://www.samoaobserver.ws/
- Samoa Global News: https://samoaglobalnews.com/
- RNZ Pacific: https://www.rnz.co.nz/pacific
- Islands Business: https://islandsbusiness.com/
- Radio Polynesia: use `Radio Polynesia Samoa telecom Starlink Digicel Vodafone` search if the site blocks automated fetches.
- Data Center Dynamics: https://www.datacenterdynamics.com/
- Submarine Networks: https://www.submarinenetworks.com/
- DataCenterMap: use `site:datacentermap.com Samoa OR Apia` because the site may rate-limit direct automated fetches.
- Cloudscene: https://cloudscene.com/
- geocables/cablestatus/submarinecablemap for cable leads only.

Search templates:

```text
"Samoa" ("data center" OR "data centre" OR datacenter OR colocation OR "co-location" OR "server hosting" OR "managed hosting") -proxy -VPS
"Apia" ("data center" OR "data centre" OR server OR hosting OR colocation OR "landing station" OR "cable station")
"Tuasivi" OR "Salelologa" ("landing station" OR "cable station" OR server OR internet OR telecom OR fibre OR fiber)
"SamoaTel" OR "SSCC" OR "Digicel Samoa" OR "Vodafone Samoa" OR BlueWave OR CSL ("data" OR network OR switch OR hosting OR "cable station")
"Starlink" Samoa (license OR tariff OR reseller OR retailer)
site:samoaobserver.ws ("data centre" OR "data center" OR internet OR broadband OR cable OR Starlink OR digital)
site:samoaglobalnews.com ("data centre" OR "data center" OR internet OR broadband OR cable OR Starlink OR digital)
site:datacenterdynamics.com Samoa OR Apia
site:datacentermap.com Samoa OR Apia
site:cloudscene.com Samoa OR Apia
site:geocables.com Apia Samoa cable
```

Directory handling:

- If a directory lists Samoa/Apia without an operator, street address, local license, or official product page, record it as `discarded_reseller_or_directory_lead`.
- If a directory names SSCC, SamoaTel, CSL, Digicel, or Vodafone, pivot back to the operator's official page and OOTR before counting.
- Absence in DataCenterMap/Cloudscene is a weak negative signal only; it does not prove no server rooms exist.

## 4. Per-District Industry Enumeration

Run one generic industry sweep per district, then follow the route below. This table covers all 11 Samoa districts exactly once.

Generic sweep:

```text
"{District}" Samoa ("data center" OR "data centre" OR datacenter OR colocation OR hosting OR "server room" OR cloud OR "landing station" OR "cable station" OR NOC OR switch OR fibre OR fiber OR broadband)
"{District}" Samoa (SamoaTel OR Digicel OR Vodafone OR CSL OR BlueWave OR SSCC OR Starlink)
"{District}" Samoa (tower OR Wi-Fi OR VSAT OR satellite OR backhaul OR broadband)
```

| District | Expected industry findings | Vendor route | Decision rule |
|---|---|---|---|
| Tuamasaga | All plausible private/government hosting leads; SSCC Apia; SamoaTel/Digicel/Vodafone/CSL/BlueWave HQ/core; bank and ministry server rooms | SSCC RIO, csl.ws, operator sites, OOTR, DCRSP, local press | Count only SSCC Apia and DCRSP when source conditions are met; keep operator cores as telecom leads unless facility evidence appears. |
| Fa'asaleleaga | SSCC Tuasivi cable station; Salelologa telecom/utility hub; SamoaTel/other exchange leads | SSCC RIO/progress; searches for Tuasivi/Salelologa; EPC context | Count Tuasivi as telecom cable station; do not infer a Savai'i DC from Salelologa commercial presence. |
| A'ana | Faleolo airport telecom; resort/business connectivity; no DC expected | Operator coverage pages, airport/press, Starlink/reseller coverage | Mark `no_projects` unless an operator or tender names a server/hosting facility. |
| Aiga-i-le-Tai | Mulifanua ferry/Manono/Apolima connectivity; Apolima solar false positive | Operator coverage and local press | Connectivity-only; mark `no_projects`. |
| Atua | East/south Upolu broadband, hydro/wind/power assets, towers | Operator coverage, EPC context, press | Power and tower hits are false positives. |
| Va'a-o-Fonoti | Taelefaga/Fagaloa telecom and hydro context | EPC and generic operator sweep | Hydro/coverage only; mark `no_projects`. |
| Gaga'emauga | North Savai'i villages and Upolu/Savai'i split/enclave searches | Operator coverage, local press | Telecom-only unless a named facility appears. |
| Gagaifomauga | North Savai'i tourism villages with connectivity hits | Operator coverage, Starlink/reseller press | Telecom/Starlink-only; no DC expected. |
| Palauli | Vailoa Palauli hydro and south Savai'i connectivity | EPC and operator coverage | Hydro false positive; no DC expected. |
| Satupa'itea | South Savai'i coverage | Generic sweep | Mark `no_projects`. |
| Vaisigano | Asau/Vaisala/Sataua coverage and small business connectivity | Operator coverage, Starlink, press | Telecom cabinets/towers only. |

## 5. Cloud, Satellite, And Connectivity Sweep

Official cloud absence checks:

```text
"Samoa" ("AWS region" OR "AWS Local Zone" OR "Azure region" OR "Google Cloud region" OR "OCI region")
"Samoa" ("cloud region" OR hyperscale OR "public cloud" OR "sovereign cloud")
```

Use official provider lists only: AWS https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ ; Azure https://learn.microsoft.com/en-us/azure/reliability/regions-list ; Google Cloud https://cloud.google.com/about/locations ; Oracle https://www.oracle.com/cloud/public-cloud-regions/ . As of this pass, no WS region was found.

Satellite/connectivity rules:

- Starlink Samoa license and approved resellers/retailers are A-grade for connectivity and equipment retail, not datacenters. The Samoa government release names direct Starlink purchase plus local approved resellers/retailers including Digicel, Vodafone, CSL, and Bluebird Lumber.
- Kacific/SES/O3b-style references are remote-connectivity leads only unless a Samoa gateway facility is named.
- Tui-Samoa, Manatua, and SAS/Apia-Pago Pago are cable/connectivity leads. Only SSCC RIO-style facility access can support `colo_adjacent_telecom` classification.

## 6. Capture Fields For Any Hit

For each possible facility, capture:

```text
name:
operator_or_owner:
district:
town_or_site:
coordinates_or_address:
source_url:
source_date:
source_grade: A|B|C
facility_type: commercial_colo | government_dc | telecom_cable_station | telecom_core | enterprise_server_room | tower_edge | connectivity_only | false_positive
status: proposed | planned | procurement | under_construction | operational | discontinued | false_positive
basis_for_status:
capacity_or_power_claim:
power_evidence:
license_or_registry_anchor:
notes:
```

Promotion rules:

- Promote to `commercial_colo` only with an operator page, tariff/product page, facility page, or contract saying colocation/racks/datacenter service in Samoa.
- Promote to `government_dc` only with MCIT/MOF/World Bank/government evidence naming the government data center and its status.
- Keep cable stations as `telecom_cable_station` unless the source says datacenter/colo service.
- Keep Starlink, towers, Wi-Fi, VSAT, and broadband coverage as `connectivity_only`.

## 7. Pitfalls

- American Samoa results dominate searches for Samoa cables. Reject AS-only assets as WS facilities.
- SEO hosting pages frequently advertise Samoa VPS/dedicated servers with no physical WS facility. Treat as Grade C/ignore.
- `Cloud` on a vendor page may mean resale, backups, website hosting, or SaaS. Require physical-site evidence before recording a datacenter.
- Operator HQ in Apia does not equal datacenter. Use `telecom_core_lead` until a facility/function is verified.
- SSCC RIO access is strong telecom-facility evidence but still not a neutral retail colo market.
- DCRSP is planned government infrastructure. Do not mark operational until procurement/completion evidence appears.
- Power assets (EPC hydro/solar/diesel, BESS, substations) are feasibility context, not datacenters.

## 8. Source Quick List

- SSCC: https://www.ssccsamoa.com/ ; https://www.ssccsamoa.com/about/rio-reference-interconnection-offer/ ; https://www.ssccsamoa.com/wp-content/uploads/2026/03/Rio-2026.pdf ; https://www.ssccsamoa.com/home/progress/
- OOTR: https://regulator.gov.ws/ ; licensee PDF https://regulator.gov.ws/images/Telecommunications_Licensing_Rule/List-of-Telecommunications-Licensees-Final-2022_v3.pdf ; telecom orders https://www.regulator.gov.ws/index.php/telecommunications-regulation/telecommunications/telecommunications-orders
- MCIT/DCRSP/World Bank: https://mcit.gov.ws/publications/digital-samoa/ ; https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099093024135596945
- SamoaTel/Vodafone/Digicel/CSL: https://samoatel.ws/ ; use OOTR and search for Vodafone Samoa if `vodafone.ws` is unavailable ; https://www.digicelpacific.com/news/telstra-acquires-digicel-pacific ; https://csl.ws/
- Starlink Samoa license: https://www.samoagovt.ws/2025/01/press-release-starlink-samoa-cheapest-tariff-in-the-world/
- EPC: https://www.epc.ws/
- Registry: https://www.businessregistries.gov.ws/
- Cable/trade leads: https://www.submarinenetworks.com/en/systems/australia-usa/tui-samoa ; https://www.submarinenetworks.com/en/systems/australia-usa/manatua/manatua-cable-lay-operations-complete ; https://www.adb.org/projects/47320-001/main
- Press/directories: https://www.samoaobserver.ws/ ; https://samoaglobalnews.com/ ; https://www.rnz.co.nz/pacific ; https://islandsbusiness.com/ ; https://www.datacenterdynamics.com/ ; use `site:datacentermap.com Samoa OR Apia` for DataCenterMap if direct access is rate-limited ; https://cloudscene.com/

Refresh instruction: re-run operator pages, OOTR licensee/order pages, SSCC RIO, DCRSP procurement/ISR, local press, and cloud-region lists before changing Samoa facility status.
