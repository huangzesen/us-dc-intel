# PW Explorer Industry - Palau Datacenter Enumeration via Operators, Cable/Telecom Infrastructure, Trade Press, Directories, and Locality Query Patterns

Date: 2026-08-12. Scope: Palau (PW), all 16 state divisions: Aimeliik, Airai, Angaur, Hatohobei, Kayangel, Koror, Melekeok, Ngaraard, Ngarchelong, Ngardmau, Ngatpang, Ngchesar, Ngeremlengui, Ngiwal, Peleliu, Sonsorol. Angle: industry/operator-led discovery, with official verification required before any facility is promoted to operational inventory.

Reliability grades used by this explorer: **A** = operator official page, public-sector owner page, regulator/registry record, multilateral project document, hyperscaler official location page, or stock-exchange/company filing; **B** = reputable trade, local, or regional press with named parties and dates; **C** = directory, marketplace, SEO hosting page, unverifiable marketing page, or repost with no primary link.

## 0. Market Shape And Current Conclusion

- Palau is a pre-commercial datacenter market. No operational third-party colocation, hyperscale, or public cloud region in Palau was verified in this pass.
- The real operator landscape is telecom/cable-heavy: Belau Submarine Cable Corporation (BSCC) owns wholesale submarine/fiber assets; PNCC is the incumbent retail communications provider; smaller retail ISPs and hotspot providers buy capacity or operate access networks.
- The strongest positive datacenter lead is the February 2022 DC Alliance / Pacific Blockchain Corporation proposal. The primary SGX filing is a non-binding MOU with a 12-month term, not a construction award or operational announcement: https://links.sgx.com/1.0.0/corporate-announcements/3CWI072CXHPQGQJH/701605_FHL%20-%20MOU%20between%20DCA%20and%20PBC.pdf. Keep the project as `announced_mou` or `stale_unverified` until new primary evidence appears.
- PC2/Echo branch status needs current handling: older 2023/2024 press projected 2025 activation, but BSCC's 2025-2029 business plan expects PC2 Ready for Service in 2026 and AIFFP's 2026 fact sheet says completion mid-2026. Use 2026 as the current expected service window unless a newer BSCC/AIFFP/Google/Meta source confirms RFS.
- Guam is the nearest meaningful commercial colocation/interconnection market. Guam facilities can be cited as regional fallback only; never count them as Palau inventory.
- Industry pages claiming `Palau data center`, `Melekeok dedicated servers`, or `Ngerulmud VPS` are often SEO-location pages. Treat them as Grade C false positives unless tied to an operator address, registry record, utility approval, or named facility.

## 1. Operator And Vendor Sweep

| Operator / lead | Source URL | State focus | Evidence use | Grade |
|---|---|---|---|---|
| Belau Submarine Cable Corporation (BSCC) | https://belaucable.com/ and https://belaucable.com/about | Ngeremlengui, Ngardmau, Airai | State-owned wholesale cable/fiber owner. PC1/CAP-N, PC2/Echo branch, and CAP-A are core datacenter-adjacent infrastructure. | A |
| BSCC Business Plan FY 2025-2029 | https://belaucable.com/s/BSCC-Business-Plan-2025-2029.pdf | Ngeremlengui, Ngardmau, Airai | Current PC2 timing, wholesale RSP model, CAP-A and network strategy. | A |
| AIFFP Palau ECHO fact sheet | https://www.aiffp.gov.au/sites/default/files/2026-05/AIFFP_DSN_Factsheet_%237_Expanding%20digital%20connectivity%20in%20Palau%20via%20a%20submarine%20cable%20system_20260527.pdf | Ngardmau | Confirms dedicated ECHO branch, Ngardmau landing station, mid-2026 completion target. | A |
| PNCC | https://www.pnccpalau.com/ | Koror, Airai, national | Incumbent mobile/internet/telephone/digital TV operator. Leads for exchange/server rooms; no public commercial DC evidence. | A |
| Palau Telecom / PT Waves | Operator and local press searches | Koror/Airai likely | Retail wireless/internet lead. Verify through official pages, licensing, or press before recording any facility. | B unless official page found |
| Palau Wifi | Operator and local press searches | Koror/tourism corridor likely | WiFi/hotspot lead. Hotspots are not datacenters. | B/C depending source |
| DC Alliance Pte Ltd | SGX filing and https://dcalliance.com.au/ | Site not named | Proposed Tier III datacenter MOU with Pacific Blockchain Corporation; no verified build found. | A for SGX MOU terms; B for trade coverage |
| Pacific Blockchain Corporation | SGX filing, FIB/registry, press | Site not named; Koror likely for offices | Palau-side datacenter proposal partner. Verify legal status and any FIAC/minutes before using. | A if registry/FIB, B for press |
| NEC | https://www.nec.com/submarine/ | Ngeremlengui, Ngardmau | Supplier context for PC1/PC2 submarine systems. Confirms cable vendor relationships, not datacenter operation. | A for NEC releases, B when via trade |
| DXN / Data Exchange Networks | https://dxn.solutions/ and DCD trade coverage | Ngardmau | Modular cable landing station supplier for PC2/Echo branch. Useful for facility-equipment evidence, not commercial DC evidence. | A for DXN, B for DCD |
| GTA TeleGuam | https://www.gta.net/data-center | Guam only | Regional Tier 3-designed colocation/cable landing context. Exclude from Palau inventory. | A for Guam only |
| Guam Exchange / Citadel Pacific | Guam Exchange/Citadel pages and press | Guam only | Regional IXP/datacenter context. Exclude from Palau inventory. | A/B for Guam only |

Operator search templates:

```text
"{operator}" Palau "data centre" OR "data center" OR datacenter
"{operator}" Palau colocation OR "co-location" OR hosting OR "server room"
"{operator}" Palau "rack" OR "MW" OR "Tier III" OR Uptime
"{operator}" Palau "cable landing" OR "landing station" OR POP OR "access point"
"{operator}" "{state}" Palau
"{operator}" Palau construction OR commissioned OR operational OR "ready for service"
```

## 2. DC Alliance / Pacific Blockchain Proposal Handling

Verified primary terms from the SGX filing dated 10 February 2022:

- Figtree Holdings announced that its 27.5%-owned associated company DC Alliance Pte Ltd signed a non-binding MOU with Palau-based Pacific Blockchain Corporation.
- The MOU was to explore a Tier III-rated datacenter in the Republic of Palau.
- The MOU duration was 12 months from 10 February 2022 unless replaced by a term sheet or binding agreement.
- The proposed facility was described as 1 MW and up to 200 racks initially, with development potential to 5 MW and up to 1,000 racks.
- The filing promised further updates for material developments; none was found in public searches through 2026-08-12.

Secondary/trade sources that repeat the proposal:

- Data Center Dynamics: https://www.datacenterdynamics.com/en/news/dc-alliance-to-develop-first-tier-iii-data-center-on-palau/
- Island Times: https://islandtimes.org/data-centre-set-to-be-the-first-in-palau/
- w.media: https://w.media/dc-alliance-pacific-blockchain-partner-to-explore-building-the-first-data-centre-in-republic-of-palau/
- Baxtel and other news reposts.

Status rule:

- Record as `announced_mou` or `stale_unverified_proposal`, not `planned` or `under_construction`, unless a newer Grade A or strong Grade B source names a site, land lease, financing close, EPC, construction, utility interconnection, commissioning, or customer launch.

Negative-control queries:

```text
"DC Alliance" "Palau" construction OR commissioned OR operational OR "ready for service"
"DC Alliance" "Pacific Blockchain" "term sheet" OR "binding agreement"
"Pacific Blockchain Corporation" Palau "data centre" OR "data center" "construction"
"Palau" "Tier III" "data centre" -MOU -"memorandum"
"Palau" "data center" "under construction" OR commissioned OR opened
site:links.sgx.com "DC Alliance" "Palau" "data centre"
```

## 3. Cable And Telecom Infrastructure Leads

| Lead | State | Current interpretation | Evidence path | Reliability |
|---|---|---|---|---|
| PC1 / BSCCnet landing station, CAP-N | Ngeremlengui | Operational cable landing station and telecom equipment site; datacenter-adjacent, not commercial DC | BSCC official pages/plans; ADB project records; Submarine Networks PC1 page | A/B |
| CAP-A airport access point | Airai | Customer access point and possible low-cost co-location/access site for RSPs; not a standalone datacenter | BSCC About and business plans | A |
| PC2 / Echo Palau Branch landing station | Ngardmau | Modular cable landing station; under construction/pre-service with 2026 completion/RFS target | BSCC 2025-2029 plan, AIFFP 2026 fact sheet, Blue Dot Network project page, DCD/DXN coverage | A/B |
| PNCC internal exchange/NOC/server rooms | Koror, Airai | Operational telecom support facilities; capacity undisclosed; record only if inventory scope allows internal telecom sites | PNCC official pages, local press, licensing context | A/B |
| Palau Telecom/PT Waves network equipment | Koror/Airai likely | ISP network lead; no confirmed datacenter | Official/press searches, FIB/registry | B/C until primary source found |
| Palau Wifi hotspot/network equipment | Koror/tourism corridor likely | Access-network lead only; do not treat hotspots as facilities | PNCC/press/operator searches | B/C |

Cable/telecom queries:

```text
site:belaucable.com "Ready for Service" OR RFS OR PC1 OR PC2 OR Echo
site:belaucable.com "CAP-A" OR "CAP-N" OR "co-location" OR colocation
site:submarinenetworks.com Palau "Ngeremlengui" OR "Ngardmau"
site:datacenterdynamics.com Palau DXN "cable landing station"
"Palau" "Echo" "Ngardmau" "landing station"
"PNCC" "NOC" OR "network operations" OR "server room" Palau
```

## 4. Trade Press And Secondary Sources

| Source | URL | Palau use | Grade |
|---|---|---|---|
| Island Times | https://islandtimes.org/ | Main local source for DC Alliance MOU, BSCC capacity, PC2 delay, telecom policy, energy and cybersecurity context. | B |
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com/en/news/ | DC Alliance proposal and DXN modular cable landing station reporting. | B |
| Submarine Networks | https://www.submarinenetworks.com/ | PC1/PC2 route and landing details, PC2 delay history. | B |
| SubTel Forum | https://subtelforum.com/ | Syndicated/regional subsea cable and Guam IXP/datacenter context. | B |
| Islands Business | https://islandsbusiness.com/ | Pacific business coverage; useful for PC2 timing and Palau digital economy. | B |
| Blue Dot Network | https://www.bluedot-network.org/ | PC2 certification/project status, contractors, timeline. | A/B depending page authority; use as project certification context. |
| Singapore Exchange (SGX) | https://links.sgx.com/ | Primary filing for Figtree/DC Alliance MOU. | A |
| Baxtel | https://baxtel.com/ | Datacenter directory/news and Guam market context. Use Palau proposal reposts only as leads. | C unless it links primary |
| DataCenterMap / Datacenters.com / Cloudscene | respective sites | Negative controls for absence; nearby Guam listings. | C for facility discovery |
| Pacific Island Times / RNZ Pacific / PACNEWS / PDN / Marianas Variety | regional press | Regional telecom, Guam, and Palau policy context. | B |

Trade query examples:

```text
site:islandtimes.org Palau "data centre" OR "data center" OR datacenter
site:islandtimes.org Palau "submarine cable" OR "PC2" OR "Echo" OR "BSCC"
site:datacenterdynamics.com/en/news/ Palau "data center" OR DXN OR Echo
site:submarinenetworks.com Palau "cable landing" OR "Ready for Service"
site:islandsbusiness.com Palau "2nd submarine cable" OR "digital connectivity"
"Palau" "data centre" "MOU" OR "Tier III" OR "200 racks"
```

## 5. Directory-To-Primary Verification Workflow

1. Search directories and marketplaces only after the operator/official sweep, or as a negative-control pass.
2. If a directory claims a Palau facility, require an operator official page, address, registry record, FIB record, utility/permit evidence, or reputable press with named parties.
3. Check whether the directory result is actually in Guam, Hawaii, Singapore, Australia, or another regional market.
4. Record SEO-only hosting claims as `false_positive` with Grade C and the missing evidence noted.
5. Do not create a facility from a `.pw domain`, a virtual location selector, IP geolocation, CDN node, VPN endpoint, or hosting checkout country list.

Directory/false-positive queries:

```text
site:datacentermap.com Palau "data center" OR colocation
site:datacenters.com Palau "data center" OR colocation
site:cloudscene.com Palau "data center" OR colocation
site:baxtel.com Palau "data center" OR colocation
"Palau" "dedicated server" OR VPS OR "cloud server" -Guam
"Ngerulmud" "dedicated server" OR VPS OR hosting
"Melekeok" "data center" OR "cloud server"
```

## 6. Locality Search Recipes And Division Coverage

Universal state sweep:

```text
"{division}" Palau "data centre" OR "data center" OR datacenter
"{division}" Palau "server" OR "server room" OR hosting OR colocation
"{division}" Palau "cable landing" OR "submarine cable" OR fiber OR fibre OR POP
"{division}" Palau telecom OR telecommunications OR internet OR wifi
"{division}" Palau "power" OR "substation" OR "generator" OR "PPUC"
site:islandtimes.org "{division}" internet OR cable OR ICT OR telecommunications
site:palaugov.pw "{division}" communications OR ICT OR data
```

High-yield locality variants:

```text
"Koror" OR "Malakal" Palau "PNCC" OR "data center" OR "server room" OR telecom
"Airai" Palau "CAP-A" OR "airport" OR "fiber" OR "BSCC" OR "PNCC"
"Ngeremlengui" Palau "CAP-N" OR "Cable Landing Station" OR "BSCCnet"
"Ngardmau" Palau "PC2" OR "Echo" OR "DXN" OR "landing station"
"Ngerulmud" OR "Melekeok" Palau "government" "ICT" OR "server" OR procurement
"Aimeliik" OR "Ngatpang" Palau "fiber" OR "BSCC" OR "Ngeremlengui" OR "Airai"
"Angaur" OR "Kayangel" OR "Hatohobei" OR "Sonsorol" OR "Peleliu" Palau internet OR satellite OR PNCC
```

Coverage checklist:

| State | Industry likelihood | Notes for assignment |
|---|---|---|
| Aimeliik | Low | Fiber-route context between Ngeremlengui and Airai; no known DC. |
| Airai | Medium | CAP-A/airport access point, PNCC/retail telecom, industrial corridor; possible POP/server room. |
| Angaur | Very low | Remote island; expect access-network/satellite references only. |
| Hatohobei | Very low | Southwest Islands; administrative contact often Koror; no DC expectation. |
| Kayangel | Very low | Northern island; connectivity/service references only. |
| Koror | Medium | Business center, PNCC and enterprise/server-room leads; no confirmed commercial DC. |
| Melekeok | Low/medium | Ngerulmud government campus leads; no public DC evidence. |
| Ngaraard | Low | Rural Babeldaob; state/utility/PNCC checks only. |
| Ngarchelong | Low | Rural northern Babeldaob; no known DC. |
| Ngardmau | High for cable, low for DC | PC2/Echo branch landing station; do not call it commercial DC. |
| Ngatpang | Low | Fiber-route context; no known DC. |
| Ngchesar | Low | Rural Babeldaob; no known DC. |
| Ngeremlengui | High for cable, low for DC | PC1/CAP-N landing station; do not call it commercial DC. |
| Ngiwal | Low | Rural Babeldaob; no known DC. |
| Peleliu | Very low | Remote island; service/backhaul references only. |
| Sonsorol | Very low | Southwest Islands; service/backhaul references only. |

## 7. Capacity Extraction Guidance

- Commercial datacenter capacity: only the DC Alliance/PBC MOU provides datacenter numbers: 1 MW / 200 racks initial, 5 MW / 1,000 racks potential. Because it is a non-binding MOU with no verified build, store as proposal capacity only.
- Cable capacity: BSCC PC1/PC2 documents may describe wavelengths, branch systems, RFS dates, and wholesale bandwidth. Keep this as telecom capacity, not `capacity_mw`.
- Telecom/server-room facilities: if PNCC/BSCC/internal rooms are recorded, use `capacity_mw: null` unless a source gives UPS/generator/IT load/rack data.
- Power: PPUC/energy documents can explain feasibility constraints but should not be converted into datacenter capacity.

Capacity queries:

```text
"Palau" "data centre" "MW" OR "racks" OR "Tier III"
"DC Alliance" "Palau" "1MW" OR "200 racks" OR "5MW"
"BSCC" "rack" OR "UPS" OR "generator" OR "co-location"
"PNCC" "rack" OR "server room" OR "generator" OR "UPS"
"Palau" "data center" "power" OR "PPUC" OR "interconnection"
```

## 8. Expected Enumeration Outcome

Expect a very small, conservative census: PC1/CAP-N in Ngeremlengui, PC2/Echo branch infrastructure in Ngardmau, CAP-A in Airai, possible PNCC/internal telecom facilities in Koror/Airai if the target inventory includes telecom server rooms, and one stale/unverified MOU-stage commercial datacenter proposal. Anything else should remain a lead until primary evidence confirms a named operator, exact locality, operational status, and facility type.
