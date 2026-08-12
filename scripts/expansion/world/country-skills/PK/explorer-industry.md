# PK Explorer Industry - Pakistan Datacenter Enumeration Methodology

Country: **PK Pakistan**. Review status: **finalized 2026-08-12** after live URL/API checks and reliability-grade tightening. This file covers the industry/operator path: telcos, colo, cloud, IXPs, subsea landings, directories and trade press.

Division model for this expansion manifest: **7 first-level units**: Punjab; Sindh; Khyber Pakhtunkhwa; Balochistan; Islamabad ICT; Gilgit-Baltistan; Azad Kashmir.

## Reliability Grades

- **A** = operator-owned page, official regulator/government page, Uptime Institute award page, official cloud-region page, official cable/IXP page, PeeringDB API for interconnection presence only.
- **B** = credible trade/press source: DCD, Developing Telecoms, Capacity, TeleGeography/Submarine Cable Map, APNIC, Dawn, Business Recorder, Express Tribune, ProPakistani, TechJuice, APP/PID when no underlying operator page is reachable.
- **C** = directories/aggregators and weak secondary sources: DataCenterMap, DataCenterCatalog, datacenters.com, OCOLO, Cloudscene, social reposts, unaudited market blogs.
- **U** = unverified. Do not populate facility capacity, certification, address, or status from U-grade claims.

PeeringDB and IXPs identify network presence; they do not, by themselves, prove a commercial colocation facility or customer-accessible data center.

## Market Shape

Pakistan's data-center inventory is concentrated in **Karachi, Lahore/Rawalpindi and Islamabad**. Karachi is the commercial and international-connectivity hub; Islamabad is the federal/telco/cloud hub; Lahore is the second commercial/government hub. KP, Balochistan, Gilgit-Baltistan and Azad Kashmir mostly yield institutional/public-sector facilities and cloud-policy signals rather than commercial colo.

No AWS, Azure, Google Cloud, Oracle Cloud or Huawei Cloud public region in Pakistan was found on official region pages on 2026-08-12. Treat Data Vault, Khazana, Zong, Jazz, PTCL, Sky47 and Telenor-style claims as local/sovereign/partner cloud unless a hyperscaler official region page names Pakistan.

## Industry Search Vocabulary

```text
"data center" OR "data centre" OR datacenter
colocation OR "co-location" OR hosting OR "server farm"
"Tier III" OR "Tier 3" OR "TIA-942" OR Uptime
"AI data center" OR "AI data centre" OR "sovereign cloud" OR "government cloud"
"landing station" OR "submarine cable" OR IXP OR "internet exchange"
"Karachi" OR "Lahore" OR "Islamabad" OR "Rawalpindi" plus operator name
"ڈیٹا سینٹر" OR "سرور روم" OR "کلاؤڈ" OR "کولوکیشن"
```

## Operator Query Templates

```text
"{operator}" Pakistan ("data center" OR "data centre" OR colocation OR hosting)
"{operator}" ("Tier III" OR "Tier 3" OR "TIA-942" OR Uptime) Pakistan
"{operator}" (Karachi OR Lahore OR Islamabad OR Rawalpindi) (racks OR MW OR kVA OR "power infrastructure")
"{operator}" ("cloud" OR "sovereign cloud" OR "AI cloud" OR "government cloud") Pakistan
"{operator}" ("landing station" OR "submarine cable" OR IXP) Pakistan
site:uptimeinstitute.com/uptime-institute-awards/country/id/PK "{operator}"
site:peeringdb.com "{operator}" Pakistan
```

## Operator and Facility Seeds

| Operator/project | Main URLs | Evidence and use | Grade discipline |
|---|---|---|---|
| PTCL | `https://ptcl.com.pk/`; cloud page `https://ptcl.com.pk/home/pagedetail?itemid=424&linkid=1004`; Uptime PK page | PTCL Smart Cloud/DC service; Uptime lists Commercial Data Center-1 Lahore and Commercial Data Center-2 Karachi with Tier III Design Documents awards | A for PTCL service and Uptime awards; C for directory addresses unless matched to PTCL/Uptime |
| Jazz Digital Park | VEON PR `https://www.veon.com/newsroom/press-releases/veon-group-ceo-kaan-terzioglu-inaugurates-us8-million-jazz-digital-park`; Jazz media page `https://jazz.com.pk/business/insights/media-room/jazz-digital-park-pakistans-largest-data-center` | Islamabad facility; VEON/Jazz state 300+ racks expandable to 450 and 3MW power infrastructure, with TIA Tier-III wording | A for operator claim; not Uptime unless Uptime lists it |
| Zong CICC | `https://www.zong.com.pk/press-release/zong-inaugurates-its-new-stateoftheart-cloud-intelligent-computing-center-in-islamabad-with-federal-minister-for-it--telecommunication`; `https://www.zong.com.pk/business/z-saiscloud` | Islamabad Cloud Intelligent Computing Center; company says Tier-III Certified Data Center | A for launch and company wording; Uptime registry not found under Zong in PK list |
| NTC / Government Cloud | `https://cloud.gov.pk/`; `https://ntc.net.pk/`; PID release `https://pid.gov.pk/site/press_detail/15554` | Government NDC/cloud; Lahore DRC/full-fledged data center for NDC backup and cloud services | A/B for official wording; specs/capacity U |
| NADRA | `https://www.nadra.gov.pk/`; CGD NADRA Story `https://www.cgdev.org/publication/ft/technology-service-development-nadra-story`; Uptime PK page | Large identity-platform DC estate; Uptime lists Islamabad ICT Safe City Data Center under NADRA; CGD says two DCs 150 miles apart and a third planned | A for entity/Uptime award; B for CGD count/distance |
| Data Vault Pakistan | `https://datavault.com.pk/`; SIFC item `https://sifc.gov.pk/news/636` | Karachi AI-focused data centre launch per SIFC/operator context | A for official launch/company; GPU/solar/first/largest claims only when primary source says exactly that |
| Quantum Global Data Center | `https://quantumdc.com/`; `https://quantumdc.com/about-us/`; Dawn `https://www.dawn.com/news/2005546`; Business Recorder `https://www.brecorder.com/news/40424274/pakistans-largest-data-centre-planned-as-qgdc-announces-230mn-investment` | Gul Ahmed Energy venture; Karachi project announced with Huawei partnership and $230m initial investment | A for company; B for project economics/timeline until official construction/commissioning source appears |
| Transworld Associates | `https://www.transworld.com.pk/`; Uptime PK page; DCD/ProPakistani/press for SEA-ME-WE 6 and DC | Cable operator; Uptime lists Transworld KR1 in Karachi with Tier III Design Documents; Tier III DC launch timing from press | A for company and Uptime award; B for launch schedule unless TWA page confirms |
| Sky47 Karakoram 1 | Uptime PK page; ZTE/Sky47/operator/official press where reachable | Uptime lists Karakoram 1 in Islamabad with Tier III Design Documents; launch and AI-cloud claims require separate source | A for award; B/A for launch depending on source; largest/Tier IV claims U unless certified |
| NASTP / Khazana Cloud | `https://nastp.pk/`; `https://khazanacloud.com/`; ProPakistani coverage of NASTP/Khazana launch | Local cloud/hyperscale marketing; Khazana states PTCL Karachi co-location and Tier 3 facility at Lahore NASTP in its own content | A for operator content; B for launch coverage; “hyperscaler” label U |
| Multinet | `https://multinet.com.pk/`; `https://multinet.com.pk/data-center/`; PeeringDB fac 3447 | Karachi data-center service; PeeringDB lists Multinet Pakistan Karachi facility | A for operator page and PeeringDB presence; specs C/U unless operator states |
| CubeXS Weatherly | `https://www.cubexsweatherly.com`; PeeringDB fac 6728 | Karachi/Clifton facility candidate | A for company and PeeringDB facility presence; commercial DC specs U |
| Nova / The Professional Communications | `https://www.nova.net.pk/`; PeeringDB fac 8210 | Islamabad facility candidate | A for company and PeeringDB presence; specs U |
| KK Networks / Infinity | PeeringDB facs 8264 and 9130; PeeringDB-listed operator URLs `http://www.kknetworks.com.pk` and `http://www.infinitybroadband.net` were not usable in curl validation | Lahore interconnection/facility candidates | A for PeeringDB presence only; do not use the operator URLs as source evidence until reachable |
| Wateen, Cybernet, Supernet, Nexlinx, CIS, Chapal, NetSat, Logon, Getlinks, Usman ISP and others | Operator sites plus PeeringDB/directories | Candidate operators from directories/API | A only for operator/PeeringDB facts; C for DataCenterMap/DataCenterCatalog candidate claims |

## PeeringDB Live Snapshot

Live API pulls on 2026-08-12:

- `https://www.peeringdb.com/api/fac?country=PK` returned facilities including Multinet Pakistan Karachi, CubeXS Weatherly Karachi, The Professional Communications/NOVA Islamabad, KK Networks Lahore, Infinity Broadband Lahore, Logon Broadband Karachi, Getlinks Multan, Usman ISP Bhalwal, Tzee's Multi Services Karachi, Nexlinx Lahore, Homenet Lahore and more.
- `https://www.peeringdb.com/api/ix?country=PK` returned PKIX Lahore, Pakistan Internet Exchange (PIE) Karachi powered by DE-CIX/PTCL, and MyNet Broadband Karachi.

Use the API as candidate discovery. Re-pull before every enumeration run because PeeringDB entries can be user-maintained and change quickly.

## IXPs and Interconnection

| IXP/source | Location | Use | Grade |
|---|---|---|---|
| PKIX official `https://pkix.pk/` | Islamabad origin; Lahore node in PeeringDB/APNIC; Karachi referenced by APNIC | Participant list and local traffic exchange clue | A for official PKIX facts; B for APNIC historical expansion |
| PIE Karachi powered by DE-CIX/PTCL | Karachi | Carrier-neutral IX lead and PTCL/DC adjacency clue | A for DE-CIX/PTCL/PeeringDB facts; not DC proof |
| MyNet Broadband Karachi | Karachi | Candidate network/IXP clue | A for PeeringDB fact only |

## Subsea and Cable-Landing Discovery

Karachi/Sindh is Pakistan's international cable-landing hub. Use TeleGeography/Submarine Cable Map and consortium/operator pages first, then trade press for landing/RFS status.

Search templates:

```text
site:submarinecablemap.com/landing-point/karachi-pakistan
"{cable}" Karachi Pakistan landing station
"Transworld" "SEA-ME-WE 6" Karachi "data center"
"PTCL" "Africa-1" Karachi landing
"2Africa" Pakistan Karachi Transworld
```

Candidate cables to track: SEA-ME-WE 3/4/5/6, I-ME-WE, AAE-1, TW1, PEACE, 2Africa, Africa-1 and Africa-2. Cable landing stations are physical telecom facilities but should not be counted as commercial data centers unless a source says they provide DC/colo/cloud service.

## Division Strategy

| Division | Industry anchors | Enumeration strategy |
|---|---|---|
| **Sindh** | Karachi: PTCL DC-2, Data Vault, QGDC, Transworld KR1/TWA DC, SBP MDC, Government of Sindh Board of Revenue DC, Multinet, CubeXS, Cybernet/Wateen candidates, PIE Karachi, cable landings | Start with Uptime, SIFC, PTCL/TWA/QGDC/Data Vault, PeeringDB and cable map; use directories only to widen the candidate list |
| **Punjab** | Lahore: PTCL DC-1, NTC Main Data Centre/DRC, Multinet LDC candidates, KK/Infinity/Nexlinx, PSCA; Rawalpindi/Lahore claims around Sky47 only if source places them there | Run Lahore/Rawalpindi/Faisalabad/Multan sweeps; separate ICT from Rawalpindi carefully |
| **Khyber Pakhtunkhwa** | KP Government Data Centre from KP strategy; KPITB STPs; KP Safe City/university candidates | Institutional sweep only; no commercial colo hub confirmed in reliable industry sources |
| **Balochistan** | Balochistan Police D3C Quetta; University of Turbat DC; possible Quetta/Gwadar directory candidates | Treat as institutional/minimal; do not promote directory entries without operator confirmation |
| **Islamabad ICT** | Zong CICC, Jazz Digital Park, Sky47 Karakoram 1, NTC/NITB/NADRA, ICT Safe City DC, PKIX/PERN, NOVA | Federal/telco cluster; cross-check every “Islamabad/Rawalpindi” source for legal division |
| **Gilgit-Baltistan** | GBIT, GB Cloud First Policy 2024 | Negative-search default; cloud policy does not imply local DC build |
| **Azad Kashmir** | AJK IT Board/e-government | Negative-search default; no confirmed industry DC project found |

## Known Facilities and Projects

| Facility/project | Division | Status | Best grade |
|---|---|---|---|
| PTCL Commercial Data Center-1 Lahore | Punjab | Operational; Uptime Design Documents award | A |
| PTCL Commercial Data Center-2 Karachi | Sindh | Operational; Uptime Design Documents award | A |
| SBP Main Data Center | Sindh | Operational institutional DC; Uptime Design Documents + Constructed Facility awards | A |
| Board of Revenue Data Center | Sindh | Government DC; Uptime Design Documents award | A |
| Transworld KR1 / TWA DC | Sindh | Uptime Design Documents award; launch/construction status needs operator/press reconciliation | A for award; B for schedule |
| Data Vault AI data centre | Sindh | Launched in Karachi per SIFC/operator context | A for launch statement; B/U for detailed claims |
| QGDC Karachi | Sindh | Announced/planned; not operational by default | A company; B project |
| Multinet Karachi facility | Sindh | Operational candidate/operator DC | A for operator/PeeringDB; specs U |
| CubeXS Weatherly Karachi | Sindh | PeeringDB facility candidate | A for PeeringDB; specs U |
| Jazz Digital Park | Islamabad ICT | Operational; operator states TIA Tier-III, 300+ racks, 3MW | A operator |
| Zong CICC | Islamabad ICT | Inaugurated; operator states Tier-III Certified Data Center | A operator |
| Sky47 Karakoram 1 | Islamabad ICT | Uptime Design Documents award; launch claims must be verified separately | A for award |
| ICT Safe City Data Center | Islamabad ICT | Uptime Design Documents award under NADRA | A for award |
| NTC/NDC and Lahore DRC | Islamabad ICT/Punjab | Government cloud/NDC/DRC | A/B official |
| NOVA/The Professional Communications | Islamabad ICT | PeeringDB facility candidate | A for PeeringDB; specs U |
| KP Government Data Centre | Khyber Pakhtunkhwa | Stated by KP digital strategy | A for statement; specs U |
| Balochistan Police D3C | Balochistan | Operational institutional command/data center | A |
| University of Turbat DC | Balochistan | Operational institutional DC | B |
| GB Cloud First Policy | Gilgit-Baltistan | Policy signal only | A |
| AJK IT Board | Azad Kashmir | E-government signal only | A for entity; no DC confirmed |

## Grade Discipline

- Capacity fields stay null unless a named source states MW/kW/kVA/racks for the exact facility. Jazz's 3MW/300+ rack claim is usable because VEON/Jazz state it; QGDC's capex is not facility MW.
- Directory counts are not census totals. Record them only as discovery notes.
- “Largest”, “first”, “hyperscale” and “AI-ready” are marketing claims unless independently defined and sourced.
- Keep cable landing stations, IXPs, telecom exchanges and server rooms out of commercial DC inventory unless the source explicitly offers colocation/cloud/hosting or the methodology needs them as separate infrastructure nodes.
- Pakistan city placement matters: Islamabad ICT and Rawalpindi/Punjab are separate manifest divisions.

## Recheck Cadence

- Monthly for active projects: QGDC, Data Vault, Transworld KR1/TWA DC, Sky47, Khazana/NASTP, Zong/Jazz cloud offers.
- Quarterly: PeeringDB `fac` and `ix` APIs for PK, Uptime Pakistan awards, cloud-region pages, DataCenterMap/DataCenterCatalog candidate lists, ProPakistani/TechJuice/DCD/DevelopingTelecoms queries.
- Semiannual: full 7-division negative sweep, including Urdu searches for KP, Balochistan, GB and AJK.
- Annual: operator ownership changes, PTCL/Ufone/Telenor consolidation, SIFC/BOI changes, PTA licensing changes and cable status.

## Source Status Log

Validation status on 2026-08-12: Uptime PK, PeeringDB PK `fac`/`ix`, Jazz/VEON, Zong, NADRA, PID, SIFC, QGDC, Transworld, Nova, PKIX, DE-CIX, Submarine Cable Map, KPITB/digital KP, GBIT and official AWS/Azure/GCP/OCI/Huawei region pages returned usable HTTP results. Data Vault, Dawn, Business Recorder, CGD and Express Tribune were bot-blocked but search-indexed. PTCL, Multinet, Cloud.gov.pk, CubeXS Weatherly, Balochistan Police and Infinity timed out from curl and should be opened in browser/search before extracting new facts. KK Networks returned 404 from the PeeringDB-listed URL; use PeeringDB only until a current operator URL is found.
