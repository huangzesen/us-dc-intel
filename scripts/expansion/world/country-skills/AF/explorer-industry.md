# AF Explorer Industry - Afghanistan Datacenter Enumeration

Date: 2026-08-12. Scope: industry, operator, directory, trade-press, and local-news methodology for Afghanistan data-center discovery at **province, 34 provinces** level.

Reliability grades:
- **A** = operator-owned facility page, official procurement/agency page, regulator/license page, IFI/USAID/World Bank project page, Uptime certificate.
- **B** = credible trade/local press or contractor case study with named project/operator/location.
- **C** = directory, marketplace, PeeringDB/IXP-only record, market report, hosting blog, social post, inferred telecom core, or uncorroborated multi-city claim.

Promotion rule: a lead becomes a data-center record only when the source chain names a facility/site or directly states data-center/colocation/hosting infrastructure. Telecom coverage, fiber, towers, and cloud resale are not enough.

---

## 0. Market structure and current posture

- Afghanistan's public data-center market is **small and Kabul-centric**. Directory and trade coverage consistently resolve back to Kabul; national capacity estimates are low and should stay **C** unless primary capacity evidence is found.
- Verified or strong Kabul anchors: **ANDC**, **ALEF Technology**, **AryanICT**, **Asia Consultancy Group Kabul**, **NIXA**, **MoMP data center**, **DABS/Tarakhil DR plan**, and GTR-listed government/UNDP/AUAF/AFMIS data-center projects.
- ACG's own website confirms a **5,000 sq ft Kabul data center** at its HQ. DataCenterMap's ACG company profile claims additional ACG data centers in **Herat, Kandahar, Mazar-e-Sharif, Jalalabad, and Kunduz**, but live review found no independent operator pages for those cities. Keep those as **C leads**, not verified province records.
- MCIT states a second National Data Center would be created in **Nangarhar**. This is an official planned lead, not evidence of operation.
- No public hyperscaler region/local zone was found in Afghanistan on official AWS/Azure/GCP/OCI lists. Treat hyperscaler-partner or cloud-product pages as service evidence only.
- Internet shutdowns, power import dependence, and weak grid reliability materially affect status assessment. Prefer recent operating evidence over old directory entries.

Search languages:
- English: `data center`, `data centre`, `datacenter`, `colocation`, `co-location`, `hosting`, `managed hosting`, `cloud`, `disaster recovery`, `server farm`, `server room`, `Tier III`.
- Dari: `مرکز داده`, `مرکز معلوماتی`, `هاستینگ`, `سرور`, `ابر`.
- Pashto: `ډیټا مرکز`, `د معلوماتو مرکز`, `سرور`.

---

## 1. Industry and trade sources

### 1.1 International trade / analysis

| Source | URL / query | Use | Grade |
|---|---|---|---|
| Data Center Dynamics | https://www.datacenterdynamics.com/ and `site:datacenterdynamics.com Afghanistan data center` | DABS/Tarakhil DR data-center plan; Afghan telecom/DC-adjacent news. | B |
| Network World South Asia guide | https://www.networkworld.com/article/970978/south-asia-data-centre-guide-2022-country-by-country.html | Names ANDC, ACG, ALEF, Pamir Alpha, ANHDC; useful but verify with primary/operator pages. | B |
| APNIC Blog | https://blog.apnic.net/2022/05/20/ixp-seeks-to-sustainably-lower-the-cost-of-internet-in-afghanistan/ | NIXA context and IXP economics. | B |
| Internet Society IXP Tracker | https://pulse.internetsociety.org/en/ixp-tracker/country/AF/ | NIXA status/members; network evidence only. | B/C |
| PCH IXP directory | https://www.pch.net/ixp/details/1705 | NIXA cross-check. | B/C |
| Chatham House | https://www.chathamhouse.org/2024/08/internet-under-attack/03-internet-resilience-afghanistan | Internet resilience/shutdown context. | B |
| IMS / Digital Infrastructures report | https://www.mediasupport.org/publication/digital-infrastructures-in-afghanistan/ | Governance/ownership/connectivity context. | B |
| Mordor Intelligence | https://www.mordorintelligence.com/industry-reports/afghanistan-data-center-market | Market size/hotspots only; never facility proof. | C |

### 1.2 Afghan / regional press

| Source | Query | Use | Grade |
|---|---|---|---|
| Pajhwok | `site:pajhwok.com "{province}" "data center"` | Provincial telecom/e-government announcements. | B |
| Bakhtar | `site:bakhtarnews.af "{province}" "data center"` | State-adjacent announcements; useful after 2021. | B |
| Ariana News | `site:ariananews.af Afghanistan fiber data center` | AWCC Kabul-Mazar-Hairatan fiber, MCIT/telecom announcements. | B |
| TOLOnews | `site:tolo.news Afghanistan telecom internet data` | Telecom, shutdowns, public-service centers. | B |
| Khaama | `site:khaama.com Afghanistan telecom internet` | Shutdown/fiber and governance leads. | B/C |
| Hasht-e Subh / 8am | `site:8am.media Afghanistan internet telecom` | Control/shutdown/governance leads. | B |
| Kabul Now | `site:kabulnow.org Afghanistan internet telecom` | Context leads; confirm elsewhere. | B/C |

### 1.3 Directories and network databases

Use only as lead sources unless corroborated:
- DataCenterMap Afghanistan: https://www.datacentermap.com/afghanistan/
- DataCenterMap Kabul: https://www.datacentermap.com/afghanistan/kabul/
- ACG DataCenterMap profile: https://www.datacentermap.com/c/asia-consultancy-group/
- ACG Kabul listing: https://www.datacentermap.com/afghanistan/kabul/acg-data-center/
- ANDC DataCenterMap listing: https://www.datacentermap.com/afghanistan/kabul/afghanistan-national-data-center/
- ALEF DataCenterMap listing: https://www.datacentermap.com/afghanistan/kabul/alef-technology/
- DataCenterCatalog Afghanistan: https://datacentercatalog.com/afghanistan
- datacenters.com Afghanistan/Kabul: https://www.datacenters.com/locations/afghanistan/kabul
- Uptime Institute Afghanistan page: https://uptimeinstitute.com/uptime-institute-awards/country/id/AF
- PeeringDB: https://www.peeringdb.com/
- Cloudscene: https://cloudscene.com/market/data-centers-in-afghanistan/all

Directory cautions:
- DataCenterMap currently lists Kabul facilities and may expose stale/self-submitted details. Use address and operator as leads.
- datacenters.com listings for Afghan Wireless Kabul data centers are **C** until AWCC names facilities or a stronger source confirms them.
- Uptime country page is a negative control; no visible Afghanistan award means local Tier claims remain uncertified.

---

## 2. Operator / project seed list

### 2.1 High-confidence Kabul and official/state projects

| Facility / project | Province | Source anchors | Status use | Grade |
|---|---|---|---|---|
| Afghanistan National Data Center (ANDC) | Kabul | MCIT ANDC tenders/visit pages; DataCenterMap/Network World for directory/trade details | Government data center; the standalone ANDC site was returning a default/test page or 404 during URL validation, so use MCIT as the official source of record. | A |
| ANDC critical non-IT upgrade | Kabul | https://mcit.gov.af/en/invitation-bid-procurement-critical-upgrade-afghanistan-national-data-center-andc-non-it-equipment ; https://mcit.gov.af/en/contract-award-notice-1 | Modernization/procurement event; not a new site unless source says so. | A |
| Second data center in central Kabul | Kabul | https://mcit.gov.af/index.php/en/announcement-second-project-data-center-kabul-city ; https://mcit.gov.af/index.php/en/announcement-bid-create-second-datacenter-center-kabul-1 | Planned/tender-only until award/commissioning found. | A for tender |
| Ministry of Mines and Petroleum DC / MCRS | Kabul | https://mcit.gov.af/en/ministry-mines-and-petroleum-inaugurates-data-center-and-mcrs-system | Government DC; source states 160 TB and connection to ANDC. | A |
| NIXA Internet Exchange Point Center | Kabul | https://mcit.gov.af/en/node/7048 ; https://mcit.gov.af/en/nixa-national-internet-exchange-afghanistan-8 | Physical IXP/caches/root-DNS context; DC-adjacent, not commercial colo. | A |
| ALEF Technology Data Center | Kabul | https://www.aleftechnology.com/content/data-center-0 ; https://www.datacentermap.com/afghanistan/kabul/alef-technology/ | Operator page states dedicated enterprise-ready data center in Kabul with colo/managed hosting. | A |
| AryanICT Afghanistan Data Center | Kabul | https://www.aryanict.com/blog/aryanictcom-has-recently-launched-a-new-data-center-in-afghanistan ; https://www.aryanict.com/ | Company announced Afghanistan DC on 2024-05-09; address is Kabul; verify exact facility/address before adding capacity. | A/B |
| Asia Consultancy Group Kabul Data Center | Kabul | https://www.acgtelasia.com/ict-solution ; https://www.datacentermap.com/afghanistan/kabul/acg-data-center/ | ACG page confirms 5,000 sq ft data center and co-location; directory gives Shashdarak 2nd address/specs. | A/B |
| DABS existing DC / Tarakhil DR DC plan | Kabul | https://www.datacenterdynamics.com/en/news/usaid-plans-disaster-recovery-data-center-troubled-tarakhil-power-plant-afghanistan/ | Plan and existing DABS DC lead; find DABS/USAID completion before operational status. | B |
| GTR ANDC / WEPS DR / AUAF server farm / AFMIS DC | Kabul default unless exact city found | https://www.gtr.ae/major-projects-central-asia/ | Vendor case-study leads; promote when matched to government/client source. | B |
| Pamir Alpha Technologies DC | Kabul | Network World guide; search operator page | Trade-guide lead; no primary page found in this pass. | B/C |
| Afghanistan Natural Hazards Data Center / ASDC | Kabul | Network World guide; search iMMAP/ANDMA | Specialized data center, not commercial colo; verify current operator/status. | B/C |

### 2.2 Province or non-Kabul leads

| Lead | Province | Source anchors | Handling | Grade |
|---|---|---|---|---|
| Second National Data Center in Nangarhar | Nangarhar | MCIT MoMP/MCRS page | Official planned statement; search for later tender/commissioning. | A planned |
| ACG claimed city data centers | Balkh, Herat, Kandahar, Nangarhar, Kunduz | DataCenterMap ACG company profile | Treat as directory/profile leads only; ACG official ICT page confirms Kabul but not each city. | C |
| AWCC Kabul-Mazar-Hairatan fiber | Kabul, Balkh | https://www.ariananews.af/awcc-inaugurates-kabul-mazar-hairatan-fiber-optic-network/ | Connectivity/transit lead; not DC evidence. | B for fiber, C for DC |
| Afghan Telecom regional internet/fiber services | Multiple provinces | https://www.afghantelecom.af/en/service-list/internet/fttx | Operator coverage/NOC lead; not public facility proof. | A entity, C facility |
| e& / Etisalat Afghanistan Public Cloud RFP language | likely Kabul unless address found | Etisalat tender PDFs under https://www.etisalat.af/images/Tenders/ | Public Cloud setup hosted in Afghanistan; facility remains unnamed. | A/B service, C facility |
| Wasel / Herat Host / satellite ISP hubs | Balkh, Herat, Kabul | operator search required | ISP/server-room leads only. | C |

---

## 3. Operator-focused query patterns

### 3.1 Commercial / hosting

```text
"Afghanistan" "data center" "co-location"
"Kabul" "data center" "co-location"
"Kabul" "managed hosting" "data center"
"ACG" "data center" "Kabul"
"Asia Consultancy Group" "data center" Afghanistan
"ALEF" "data center" Kabul
"AryanICT" "data center" Afghanistan
"Pamir Alpha" "data center" Afghanistan
"Afghan Wireless" "data center" Kabul
"Roshan" "data center" Afghanistan
"Afghan Telecom" "data center" Kabul
"Etisalat Afghanistan" "Public Cloud data center"
```

### 3.2 Local-language facility queries

```text
"کابل" "مرکز داده"
"کابل" "مرکز معلوماتی"
"کابل" "د معلوماتو مرکز"
"{province_dari}" "مرکز داده"
"{province_pashto}" "د معلوماتو مرکز"
"هاستینگ" "کابل" "سرور"
"سرور" "کابل" "دیتا سنتر"
```

### 3.3 Trade/local press scoped queries

```text
site:datacenterdynamics.com Afghanistan "data center"
site:networkworld.com Afghanistan "data centre"
site:pajhwok.com Afghanistan "data center"
site:bakhtarnews.af Afghanistan "data center"
site:ariananews.af Afghanistan "fiber" OR "data center"
site:tolo.news Afghanistan "internet" "data"
site:apnic.net Afghanistan NIXA
site:mediasupport.org Afghanistan "digital infrastructure"
```

### 3.4 Directory checks

```text
site:datacentermap.com/afghanistan Kabul "Data Center"
site:datacentermap.com/c/asia-consultancy-group "Herat" OR "Kunduz"
site:datacentercatalog.com Afghanistan "ACG"
site:datacenters.com Afghanistan "Afghan Wireless"
site:cloudscene.com Afghanistan "data centers"
site:uptimeinstitute.com "Afghanistan" "Tier"
site:peeringdb.com "Kabul" "facility"
```

---

## 4. Per-province industry workflow, all 34 provinces

| Province | Industry sweep |
|---|---|
| Balkh | Search `Mazar-e-Sharif`, `Mazar-i-Sharif`, `بلخ`, `مزارشریف`, `Wasel`, `Hairatan`, AWCC fiber, ACG profile. Current status: C leads only, no verified facility. |
| Bamyan | Compact negative sweep; filter out tourism/cultural center and solar-power hits. |
| Badghis | Compact negative sweep; filter out provincial access/power stories. |
| Badakhshan | Compact negative sweep; watch generic "data" and disaster/humanitarian datasets. |
| Baghlan | Search `Pul-e-Khumri`, Afghan Telecom, DABS, ISP hosting; no verified facility. |
| Daykundi | Search `Daikundi`, `Daykundi`, `دایکندی`; no verified facility. |
| Farah | Search `Farah`, `فراه`, border/transit; no verified facility. |
| Faryab | Search `Maymana`, `Faryab`, `فاریاب`; no verified facility. |
| Ghazni | Search `Ghazni`, `غزنی`, Afghan Telecom/fiber; no verified facility. |
| Ghor | Search `Ghor`, `Chaghcharan`, `غور`; no verified facility. |
| Helmand | Search `Lashkargah`, `Helmand`, `هلمند`; separate telecom/security false positives. |
| Herat | Search `Herat Host`, `Herat ISP`, `Islam Qala`, ACG profile, `هرات مرکز داده`; no verified facility found in current review. |
| Jowzjan | Search `Jawzjan`, `Jowzjan`, `Sheberghan`; no verified facility. |
| Kabul | Exhaustive operator sweep: ACG, ALEF, AryanICT, Afghan Wireless, Afghan Telecom, Roshan, e&, M1/MTN, Pamir Alpha, GTR, ANDC, NIXA, DABS. |
| Kandahar | Search `Spin Boldak`, e&/AWCC launches, ACG profile, `قندهار مرکز داده`; current status C leads only. |
| Kapisa | Compact negative sweep; no verified facility. |
| Kunduz | Search `Kunduz`, `Konduz`, ACG profile, Afghan Telecom; current status C leads only. |
| Khost | Search `Khost`, `Ghulam Khan`, Asan Khedmat, ISP/server; no verified facility. |
| Kunar | Compact negative sweep; no verified facility. |
| Laghman | Compact negative sweep; no verified facility. |
| Logar | Compact negative sweep; no verified facility. |
| Nangarhar | Search `Jalalabad`, `Torkham`, ACG profile, MCIT second NDC statement, `جلال آباد مرکز داده`; keep MCIT planned lead separate from ACG C lead. |
| Nimruz | Search `Zaranj`, Chabahar corridor; no verified facility. |
| Nuristan | Compact negative sweep; power constraints make large facility unlikely, but still search generator-backed terms. |
| Panjshir | Compact negative sweep; no verified facility. |
| Parwan | Search `Charikar`, `Bagram`, ISP/server; no verified facility. |
| Paktia | Search `Gardez`, Asan Khedmat, Afghan Telecom; no verified facility. |
| Paktika | Search `Sharana`, power/telecom terms; no verified facility. |
| Samangan | Search `Aybak`, `Samangan`; no verified facility. |
| Sar-e Pol | Search `Sar-e Pol`, `Sari Pul`, `سرپل`; no verified facility. |
| Takhar | Search `Taloqan`, `Takhar`; no verified facility. |
| Urozgan | Search `Uruzgan`, `Urozgan`, `Tarin Kot`; no verified facility. |
| Maidan Wardak | Search `Wardak`, `Maidan Shahr`, `میدان وردک`; no verified facility. |
| Zabul | Search `Qalat`, `Zabul`, `زابل`; no verified facility. |

Compact province query set:
```text
"{province}" "data center" Afghanistan
"{province}" "datacenter" Afghanistan
"{province}" "co-location" OR colocation
"{province}" "managed hosting" Afghanistan
"{province}" "server farm" OR "server room"
"{province_dari}" "مرکز داده"
"{province_pashto}" "د معلوماتو مرکز" OR "ډیټا مرکز"
site:datacentermap.com/afghanistan "{province}"
site:pajhwok.com "{province}" "data center"
site:bakhtarnews.af "{province}" "data center"
site:mcit.gov.af "{province}" "data center"
```

---

## 5. Extraction schema and grading

For each candidate extract:
- Facility name exactly as written.
- Operator, customer, contractor, and legal entity.
- Province and locality/address; do not assign province from national wording unless justified.
- Status: operational, construction, planned, tender-only, service-only, directory-only, unknown.
- Facility type: commercial colo, managed hosting/cloud, government DC, DR site, ministry/enterprise server farm, IXP/cache/root-DNS, telco core, satellite hub, or false positive.
- Capacity only when stated with units: MW, kW, racks, sqm, sq ft, TB storage. Never infer MW from generator/transformer/power-plant numbers.
- Source chain: operator/official first; trade/local press second; directories/market reports last.

Grade examples:
- ALEF operator page naming a dedicated Kabul data center = **A**.
- AryanICT company blog announcing an Afghanistan data center = **A/B**; Kabul assignment depends on company address unless facility address found.
- ACG own ICT page + directory address = **A/B for Kabul**.
- MCIT Nangarhar second-NDC statement = **A planned**, no operational status.
- ACG Herat/Kandahar/Mazar/Jalalabad/Kunduz from DataCenterMap profile only = **C**.
- Afghan Wireless datacenters.com listing only = **C**.
- NIXA member/caches/root DNS = **A/B network infrastructure**, not member DC.
- Mordor market figures = **C** and never facility/capacity evidence for a named site.

---

## 6. False positives

- Telecom towers, 4G/5G trials, BTS construction, microwave rings, and fiber routes.
- NIXA/PeeringDB/CDN/cache/root-DNS records without a host facility.
- Cloud resale, Google Workspace, D365, VMware, Oracle Linux, firewall, or support-renewal RFPs unless they name an in-country data-center site.
- "Tier III", "N+1", "state of the art", or "world-class" claims without certification.
- Open-data/statistics/humanitarian datasets.
- E-Tazkira printing centers, card-printing rooms, and small server rooms unless the source calls them a data center or server farm.
- Generic "Afghanistan data center market" pages that list Kabul providers but do not provide province-specific facility evidence.
