# QA Explorer Industry - Qatar Datacenter Discovery via Operators, Press, Directories, IXPs, and Cable Records

Date: 2026-08-12. Scope: State of Qatar (QA). Division model: **municipality (baladiyah)**. Required divisions: **Doha; Al Khor; Ash Shamal; Al Rayyan; Al Shahaniya; Umm Salal; Al Wakrah; Al Daayen**.

Reliability grades: **A** = operator-owned, official cloud/provider, regulator/government, Uptime/certifier record, or official IXP page for the exact fact; **B** = high-signal trade press, contractor case study, recognized industry source, or local media with named facts; **C** = directory, social, market-report, SEO listing, or unattributed address/capacity lead; **U** = unresolved after review. A facility should not be created from a cloud region, IXP, cable landing station, investment vehicle, or MoU unless a separate source confirms a physical datacenter.

---

## 0. Qatar market frame

- Qatar is small, state-driven, and Doha-metro-centric, but not every "Doha" datacenter lead belongs to Doha municipality. Education City/QSTP maps to **Al Rayyan**; Umm Qarn maps to **Al Daayen**; Umm Alhoul/Hamad Port/Mesaieed map to **Al Wakrah**; Lusail maps to **Al Daayen**.
- There is no public national datacenter registry. Discovery works by triangulating operator pages, Syntys/Ooredoo announcements, MEEZA news, QFZ pages, MCIT government-hosting pages, cloud-region pages, IXP pages, Submarine Networks, PeeringDB, DCD, local press, and directories.
- Fixed-network and connectivity anchors: Ooredoo, Vodafone Qatar, QNBN, GBI, QIX, and Doha IX. Submarine cable landing evidence is connectivity evidence, not a datacenter record by itself.
- Status wording matters. **Operational/launched/handed over** can support a facility when the source names the operator/project. **MoU/partnership/investment/JV/fund** is context unless it includes land, power, construction, or an operational facility.

---

## 1. Search vocabulary

English:

```text
"data center" OR "data centre" OR datacenter OR datacentre
"colocation" OR "co-location" OR hosting OR "data hall" OR "hyperscale"
"cloud region" OR "AI cloud" OR "AI infrastructure" OR GPU
"internet exchange" OR IXP OR peering OR "cable landing station"
"MW" OR "IT load" OR "gross power" OR "ready for service"
```

Arabic:

```text
"مركز بيانات" OR "مراكز البيانات" OR "مركز البيانات"
"استضافة" OR "استضافة مشتركة" OR "الحوسبة السحابية" OR "خدمات سحابية"
"نقطة تبادل الإنترنت" OR "الكابلات البحرية" OR "محطة الهبوط"
"تدشين" OR "افتتاح" OR "دخل الخدمة" OR "وضع حجر الأساس"
"مذكرة تفاهم" OR "اتفاقية" OR "شراكة"
```

Municipality/location anchors:

```text
Doha / الدوحة; Al Rayyan / الريان / Education City / QSTP;
Al Daayen / الضعاين / Umm Qarn / Lusail; Al Wakrah / الوكرة / Umm Alhoul / Hamad Port / Mesaieed;
Al Khor / الخور / Ras Laffan; Ash Shamal / الشمال / Al Ruwais;
Al Shahaniya / الشحانية / Dukhan; Umm Salal / أم صلال
```

---

## 2. High-signal source pipeline

### 2.1 Operators and primary commercial sources

| Operator / source | URL | What it supports | Grade |
|---|---|---|---|
| Ooredoo Qatar Data Centre | https://www.ooredoo.qa/web/en/business/ict-solutions/qatar-data-centre/ | Five Qatar facilities, about 60,000 sq ft, hosting/colo/cloud/DR portfolio. Individual addresses are not published. | A for portfolio; C/U for directory addresses |
| Ooredoo Government Data Centre | https://www.ooredoo.qa/web/en/business/ict-solutions/government-data-centre/ | GDC2 hosting for government entities, connected to Government Network, Tier III wording. | A for service; U for site |
| Syntys | https://syntys.com/newsroom | Ooredoo/Syntys acquisition of Q Data QFZ, 5 MW live + 7.5 MW under development; regional Syntys platform. | A for own release facts |
| Ooredoo Group Syntys/Q Data release | find via Ooredoo Group newsroom search for `Syntys acquisition Q Data facilities in Qatar`; the same release is mirrored at https://syntys.com/newsroom | Q Data QFZ operates hyperscale facilities in Qatar Free Zones; acquisition/capacity. | A for acquisition/capacity; U for exact zone |
| MEEZA | https://www.meeza.net/services/data-centre-services/ and https://www.meeza.net/about-meeza/about-us/ | M-VAULT datacenter services, Tier III/ISO/LEED claims, portfolio. | A for operator claims |
| MEEZA M-VAULT 4 release | https://www.meeza.net/meeza-reveals-the-launch-of-its-4th-m-vault-4-data-center-building-in-concurrence-with-its-13th-anniversary-celebrations/ | M-VAULT 4 launch; biggest data-center building in Qatar per MEEZA. | A |
| MEEZA M-VAULT 5 release | https://www.meeza.net/meeza-launches-the-5th-m-vault-data-center-building-to-boost-cloud-services-in-qatar-and-region/ | M-VAULT 5 launched at QSTP. | A |
| Vodafone Qatar | https://www.vodafone.qa/ | Enterprise telecom/cloud context. No strong public page found that enumerates a Qatar DC facility. | U for DC; A/B for telecom facts only |
| QNBN | CRA individual-license page confirms Qnbn passive fixed telecommunications licensing; use QNBN's own site only as a supplemental lead if reachable. | A for licensing context, not DC operator |
| QSTP directory | https://qstp.qa/directory/meeza-qstp-llc/ | MEEZA as QSTP tenant with M-VAULT network. | A for tenant/profile |
| QIX | https://www.qix.qa/ and https://www.qix.qa/contactus.html | Qatar Internet Exchange and point location: MEEZA (MV2) Datacenter, Umm Qarn. | A |
| Doha IX | https://www.doha-ix.com/about/news-and-events/ | Doha IX announcement history. | A for IXP |
| DE-CIX Doha IX release | https://www.de-cix.net/en/about-de-cix/media/press-releases/ooredoo-and-de-cix-bring-world-class-internet-exchange-to-qatar-with-doha-ix | Doha IX powered by DE-CIX, hosted on Ooredoo data centers. | A |

Operator queries:

```text
site:ooredoo.qa ("Qatar Data Centre" OR "Government Data Centre" OR GDC2)
site:syntys.com Qatar "Q Data QFZ" OR "data centre"
site:ooredoo.com "Syntys" "Q Data QFZ" Qatar
site:meeza.net ("M-VAULT" OR "data centre" OR "hyperscaler")
site:qix.qa ("MV2" OR "Umm Qarn" OR "participants")
site:de-cix.net "Doha IX"
```

### 2.2 Trade press and industry databases

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| Data Center Dynamics | use site search for `site:datacenterdynamics.com/en/news/ Qatar "data center"` | Best feed for MEEZA expansions, Ooredoo/Syntys, Microsoft region, Nvidia/Ooredoo, Qai, and historical Energy City Qatar items; the tag index can block automated fetches. | B |
| DCD: MEEZA 4 MW expansion | https://www.datacenterdynamics.com/en/news/meeza-completes-data-center-expansion-project-for-major-hyperscaler/ | 2026 completion/hand-over of 4 MW expansion for undisclosed hyperscaler. | B |
| DCD: Syntys spin-out | https://www.datacenterdynamics.com/en/news/ooredoo-spins-out-data-center-unit-rebrands-mena-digital-hub-to-syntys/ | Syntys platform background, financing, regional scale. | B |
| DCD: Syntys/Q Data acquisition | https://www.datacenterdynamics.com/en/news/ooredoos-syntys-acquires-two-data-centers-in-qatar/ | Two Q Data facilities and 5 MW live + 7.5 MW under development. | B, upgraded by Ooredoo/Syntys release |
| DCD: MEEZA financing | https://www.datacenterdynamics.com/en/news/qatari-data-center-firm-meeza-secures-219m-funding-to-fuel-44mw-expansion/ | MEEZA five data centers, QSTP details, 44 MW expansion plan. | B |
| Submarine Networks Qatar | https://www.submarinenetworks.com/en/stations/asia/qatar | Cable landing station list and Ooredoo/Vodafone landing-party context. | B |
| Data Center Map | search `Data Center Map M-VAULT 2 Umm Qarn` | M-VAULT 2 address/capacity lead at Umm Qarn; directory may rate-limit automated fetches. | C |
| PeeringDB | https://www.peeringdb.com/ix/4715 and https://www.peeringdb.com/fac/13248 | Doha IX/QDC5 leads; community-maintained. | C unless corroborated |
| ISOC Pulse IXP tracker | https://pulse.internetsociety.org/en/ixp-tracker/ixp/796/ | QIX participant/AS leads. | B/C |
| Uptime Institute | search certificate directory | A only if a current public certificate record names the facility. Operator Tier claims alone remain operator claims. | A when direct |

Trade queries:

```text
site:datacenterdynamics.com/en/news/ Qatar "data center" OR "data centre"
site:datacenterdynamics.com/en/news/ ("MEEZA" OR "Syntys" OR "Ooredoo") Qatar
site:datacentermap.com/qatar/ ("M-VAULT" OR "Ooredoo" OR "Q Data")
site:peeringdb.com Qatar ("QDC" OR "Doha IX" OR "QIX")
site:uptimeinstitute.com Qatar ("MEEZA" OR "Ooredoo" OR "Tier III")
```

### 2.3 Cloud providers

| Provider | Official URL | Qatar status | Use |
|---|---|---|---|
| Google Cloud | https://docs.cloud.google.com/compute/docs/regions-zones and https://cloud.google.com/blog/products/infrastructure/new-google-cloud-region-now-open-in-qatar | `me-central1-a/b/c` in Doha, Qatar. | A for cloud region only. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | Qatar Central, `qatarcentral`, physical location Doha, availability-zone support. | A for cloud region only. |
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | No Qatar Region listed. | A for absence of public Region. |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ | No Qatar public OCI Region listed. | A for absence of public Region. |

Cloud pivot queries:

```text
"Google Cloud" "Doha" "me-central1" ("MEEZA" OR "QFZ" OR "Ooredoo")
"Azure" "Qatar Central" ("MEEZA" OR "QSTP" OR "Microsoft cloud data centre")
"AWS" Qatar ("CloudFront" OR "edge location" OR Outposts)
"Oracle" Qatar ("dedicated cloud" OR "public cloud region")
```

---

## 3. Connectivity and interconnection

### 3.1 Submarine cable landing stations

Submarine Networks lists only Ooredoo and Vodafone Qatar as operators of submarine cable landing stations in Qatar. GBI is Qatar-based but contracts Ooredoo/Vodafone as landing parties. Source: https://www.submarinenetworks.com/en/stations/asia/qatar (B).

Records to capture as connectivity, not DC buildings:

- Ooredoo Doha Cable Landing Station: AAE-1, FALCON, FOG, GBI, Qatar-UAE, TGN-Gulf.
- Ooredoo Halul Island Cable Landing Station: Qatar-UAE.
- Vodafone Qatar North Doha Cable Landing Station: GBI.
- Qatar-UAE system lands at Doha and Halul Island; cross-check: https://www.submarinenetworks.com/en/systems/intra-asia/qatar-uae (B).
- Do not attribute 2Africa to Qatar unless a current landing-station source is found; Ooredoo's 2Africa announcement checked here is for Oman: https://www.ooredoo.com/en/media/news_view/ooredoo-to-land-worlds-largest-subsea-cable-system-2africa-comes-to-oman/ (A for Oman-only release).

Queries:

```text
"Doha Cable Landing Station" Ooredoo
"Halul Island" "cable landing"
"Vodafone Qatar" "North Doha" "landing station"
"AAE-1" "Qatar" Ooredoo
"GBI" "Qatar" "landing station"
"2Africa" Qatar "landing" -Oman
```

### 3.2 IXPs

- **QIX / Qatar Internet Exchange**: official site https://www.qix.qa/ says QIX is an internet exchange in Qatar. Contact page https://www.qix.qa/contactus.html names the QIX point location as MEEZA (MV2) Datacenter, Umm Qarn. This maps the IXP point to **Al Daayen** with high confidence, while facility details still need MEEZA/operator corroboration.
- **Doha IX**: Ooredoo + DE-CIX, announced 2025-02-04 and subsequently marketed at https://www.doha-ix.com/. DE-CIX says it is built on Ooredoo's data centers. Treat as **Doha/Ooredoo-hosted IXP** unless an exact facility is named.

Queries:

```text
"QIX" OR "Qatar Internet Exchange" "Umm Qarn" OR "MV2"
"Doha IX" Ooredoo DE-CIX "data centers"
"Doha IX" "PeeringDB" OR "IX 4715"
"QIX" "participants" "MEEZA"
```

---

## 4. Division-by-division industry workflow

### 4.1 Doha

Targets: Ooredoo Qatar Data Centres portfolio, Ooredoo GDC2, Doha IX, Vodafone Qatar enterprise/CLS leads, Microsoft/Google cloud-region metro references, Ras Bufontas/HIA free-zone leads, West Bay enterprise hosting, ministry data rooms.

```text
"Doha" "data centre" (Ooredoo OR Vodafone OR "Doha IX" OR "GDC2")
"Ooredoo" "Qatar Data Centre" "five facilities"
"Ooredoo" "Government Data Centre" GDC2
"Vodafone Qatar" "data centre" OR "hosting" OR "cloud"
"Ras Bufontas" ("data centre" OR "cloud data services" OR ICT)
"الدوحة" "مركز بيانات"
```

Grade guidance: Ooredoo portfolio = A; individual sites from Datacenters.com/Waze/PeeringDB = C until operator-confirmed. Cloud regions = A region facts, not facilities.

### 4.2 Al Rayyan

Targets: QSTP/Education City MEEZA M-VAULT 4 and 5, MEEZA/Qatar Foundation IT, GBI/QSTP company leads, research/HPC infrastructure.

```text
"QSTP" OR "Qatar Science and Technology Park" ("M-VAULT" OR MEEZA OR "data centre")
"M-VAULT 4" "QSTP"
"M-VAULT 5" "QSTP"
"Education City" "data centre"
"الريان" "مركز بيانات" "ميزة"
```

Grade guidance: MEEZA operator pages = A; DCD/local press = B; do not map MV2 here unless evidence says QSTP, because QIX and directories place MV2 at Umm Qarn/Al Daayen.

### 4.3 Al Daayen

Targets: QIX point at MEEZA MV2 in Umm Qarn, MEEZA M-VAULT 2 directory/capacity lead, Lusail smart-city/edge infrastructure, Energy City Qatar historical MoU.

```text
"Umm Qarn" "MEEZA" OR "M-VAULT 2" OR QIX
"MEEZA MV2" "Umm Qarn"
"Al Daayen" "data centre" OR "data center"
"Lusail" ("data centre" OR "ICT infrastructure" OR "smart city")
"Energy City Qatar" "data centre"
"الضعاين" "مركز بيانات"
```

Grade guidance: QIX point location = A. MV2 capacity/address from Data Center Map = C. Energy City Qatar 2007 MoU = C/U historical and should not create an active facility without current proof.

### 4.4 Al Wakrah

Targets: Umm Alhoul Free Zone, Hamad Port, Mesaieed Industrial City, QatarEnergy/industrial edge, Q Data QFZ zone-resolution searches.

```text
"Umm Alhoul" ("data centre" OR "cloud data services" OR ICT)
"Hamad Port" ("data centre" OR ICT OR "digital")
"Mesaieed" ("data centre" OR ICT)
"Q Data QFZ" "Umm Alhoul"
"Qatar Free Zones" "data centre" "Umm Alhoul"
"الوكرة" "مركز بيانات"
```

Grade guidance: QFZ location pages = A for zone geography; Q Data QFZ acquisition = A for Qatar Free Zones and capacity, U for exact zone.

### 4.5 Al Khor

Targets: Ras Laffan industrial digital/edge systems, QatarEnergy ICT, telecom nodes. Expected negative for commercial colocation.

```text
"Ras Laffan" ("data centre" OR "data center" OR ICT OR "control room")
"QatarEnergy" "Ras Laffan" ("data" OR ICT OR "digital")
"Al Khor" "data centre"
"الخور" "مركز بيانات"
```

### 4.6 Ash Shamal

Expected negative; document search date and terms. Look for Al Ruwais/Madinat ash Shamal telecom or government edge only.

```text
"Ash Shamal" Qatar "data center"
"Madinat ash Shamal" OR "Al Ruwais" ("data centre" OR ICT)
"الشمال" "قطر" "مركز بيانات"
```

### 4.7 Al Shahaniya

Expected negative; search Dukhan and industrial/oilfield ICT separately from datacenter facilities.

```text
"Al Shahaniya" "data centre" OR "data center"
"Dukhan" ("data centre" OR ICT OR "digital")
"الشحانية" "مركز بيانات"
```

### 4.8 Umm Salal

Expected negative; watch for fibre/telecom/government edge leads.

```text
"Umm Salal" "data centre" OR "data center"
"Umm Slal" ICT Qatar
"أم صلال" "مركز بيانات"
```

---

## 5. Known facilities, projects, and non-facility signals

| Facility / signal | Municipality | Evidence status | Grade |
|---|---|---|---|
| Ooredoo Qatar Data Centres portfolio | Doha/Qatar; sites unpublished | Five facilities, about 60,000 sq ft from Ooredoo official page | A portfolio; C/U individual addresses |
| Ooredoo GDC2 / Government Data Centre | Site not public | Ooredoo/MCIT/Hukoomi support government-hosting service | A service; U site |
| Syntys / Q Data QFZ acquisition | Qatar Free Zones; exact zone unresolved | Ooredoo/Syntys: Q Data QFZ, 5 MW live + 7.5 MW under development; Syntys H1 2026 materials add Qatar operational IT capacity context | A capacity/acquisition; U zone |
| MEEZA M-VAULT 4 | Al Rayyan, QSTP | MEEZA official launch page | A |
| MEEZA M-VAULT 5 | Al Rayyan, QSTP | MEEZA official launch page | A |
| MEEZA 4 MW hyperscaler expansion | Qatar/MEEZA facilities; exact building/hyperscaler undisclosed | DCD and MEEZA news category report completion/hand-over in 2026 | B; U building/customer |
| MEEZA M-VAULT 2 / QIX point | Al Daayen, Umm Qarn | qix.qa contact page names MEEZA MV2 Datacenter, Umm Qarn; Data Center Map provides MV2 details | A QIX location; C facility capacity/address |
| MEEZA M-VAULT 3 | Qatar; precise public mapping needs corroboration | MEEZA says M-VAULT 3 is Tier III and LEED Gold; directories place it in Doha/QSTP-type listings | A operator claim; C location/capacity |
| Google Cloud Doha `me-central1` | Doha metro | Google official docs/blog | A region only |
| Microsoft Azure Qatar Central `qatarcentral` | Doha metro | Microsoft Learn/geographies | A region only |
| Doha IX | Doha/Ooredoo facilities | Ooredoo and DE-CIX official releases | A IXP; no building address |
| QIX | Al Daayen via MV2/Umm Qarn point | qix.qa official | A IXP/location |
| Ooredoo Doha CLS, Ooredoo Halul CLS, Vodafone North Doha CLS | Doha / Halul offshore | Submarine Networks Qatar page | B connectivity |
| Vodafone Qatar datacenter services | Unknown | Public facility evidence remains weak; use only as lead unless an operator page or customer case study names a facility | U |
| GBI | QSTP/company lead; landing via Ooredoo/Vodafone | Submarine Networks for landings; company/HQ sources for business presence | B context |
| Energy City Qatar / NavLink datacenter MoU | Al Daayen/Lusail | Historical DCD-era MoU; no current build evidence found in this review | C/U historical |
| AWS Qatar public Region | None | AWS official region list has no Qatar Region | A absence |
| Oracle OCI Qatar public Region | None | Oracle public-region list has no Qatar public Region | A absence |
| Qai/Brookfield, Blue Owl/QIA, Nvidia/Ooredoo | Investment/technology context | Trade press indicates AI/data-center investment or technology partnerships; no Qatar facility by itself | B context only |

---

## 6. Evidence and normalization rules

- Minimum positive facility evidence: operator page naming facility, official announcement, certification record, contractor case study, utility/power evidence, or two strong independent press sources naming status and location.
- Directory-only records are leads. Use them for addresses, capacity, and aliases only with `evidence_grade=C` until confirmed.
- Do not merge Ooredoo Qatar Data Centres, Syntys/Q Data QFZ, and MEEZA M-VAULTs unless a source explicitly links assets.
- Do not infer physical buildings from Google/Azure regions, AWS/Oracle absence, QIX/Doha IX, cable landing stations, or AI investment platforms.
- Always record municipality mapping confidence. "Doha" in marketing copy may mean country/metro, not Doha municipality.
- Keep capacity fields separate: IT load MW, installed/gross MW, reserved MW, square footage, and financial investment.

Recommended record fields:

```text
facility_name
aliases
operator_current
operator_legacy
municipality
district_or_landmark
source_status_word
evidence_grade
evidence_type
evidence_urls
it_load_mw
gross_or_installed_mw
space_sq_ft
cloud_region_or_ix_role
mapping_confidence
notes_on_uncertainty
```

---

## 7. Re-check sequence

1. Operator pass: Ooredoo, Syntys, MEEZA, Vodafone Qatar, QNBN, GBI.
2. Official pass: CRA, MCIT/Hukoomi GDC, QFZ, Invest Qatar, Kahramaa, Ashghal, Ministry of Municipality/open data, QNA/GCO.
3. Trade pass: DCD Qatar tag, Gulf Times, The Peninsula, Qatar Tribune, Zawya, The Fast Mode, Telecom Review, W.Media, Middle East AI News.
4. Connectivity pass: qix.qa, doha-ix.com, DE-CIX, PeeringDB, Submarine Networks, TeleGeography.
5. Directory/certification pass: Uptime Institute, Data Center Map, Baxtel, Datacenters.com, Cloudscene, DatacenterHawk.
6. Division negatives: rerun Al Khor, Ash Shamal, Al Shahaniya, Umm Salal searches in English and Arabic and save absence notes.
7. Zone-resolution pass: specifically search whether Q Data QFZ facilities are in Ras Bufontas or Umm Alhoul before assigning a municipality.
