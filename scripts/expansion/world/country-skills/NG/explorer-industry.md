# NG Explorer Industry - Nigeria Datacenter Discovery from Operators, Trade Press, Cloud/IXP, and State Query Patterns

Date: 2026-08-12. Scope: Nigeria (NG) datacenter enumeration from operator/vendor pages, industry media, local business press, cloud/edge announcements, interconnection/subsea sources, and state-level search patterns. Reliability grades: **A** = official/primary source (operator facility page, government regulator, state permit, EAD/NERC/NCC, Uptime, official cloud page), **B** = strong secondary/trade press or reputable local business press with named project/location, **C** = aggregator, social post, old MoU, market-report snippet, or unverifiable local mention.

---

## 0. Nigeria-specific industry frame

- Nigeria's datacenter market is **Lagos-led**. Lagos discovery should start with named operators and localities: **Equinix/MainOne/MDXi Lekki**, **Rack Centre Oregun/Ikeja**, **Africa Data Centres LOS1/Eko Atlantic**, **Open Access Data Centres/WIOCC Lagos/Ikate-Lekki**, **Digital Realty/Medallion Victoria Island/Lekki**, **Kasi Cloud Lekki**, **MTN Ajao/Ojota/Ikoyi**, **Airtel/Nxtra Eko Atlantic**, **21st Century/ipNX/Cyberspace/inQ/NTT**.
- Strong non-Lagos leads exist in **FCT Abuja** and **Kano** through Galaxy Backbone; **Rivers/Port Harcourt** through Equinix/MainOne PR1 and subsea cable activity; **Akwa Ibom/Eket** through Kasi DNEK; **Ogun** through Sagamu/Atakobo energy-park leads; **Cross River/Calabar** and **Benue/Makurdi** through state/industry MoUs. Many other states have government ICT rooms or no confirmed projects.
- Press language matters. `announces`, `signs MoU`, `plans`, `seeks partners`, and `groundbreaking` are leads, not operational status. Upgrade only with official operator page, Uptime certificate, permit, NERC/NCC record, or commissioning page.
- Nigeria sources use both `data centre` and `data center`; use `datacentre`, `colo`, `colocation`, `carrier-neutral`, `cloud-neutral`, `interconnect`, `internet exchange`, `subsea cable`, `landing station`, `AI-ready`, `hyperscale`, `Tier III`, `Tier IV`, `Uptime`, `critical IT load`, `site load`, `MVA`, and `captive power`.

---

## 1. High-signal industry and press sources

Use press to discover names, timing, capacities, state/locality, financing, and construction stage; then verify through official operator/regulator sources.

| Source | URL / route | Use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com/en/news/ | Best trade feed for Nigeria: Rack Centre LGS2, MainOne/Equinix Lekki and Port Harcourt, Medallion/Digital Realty, OADC, Kasi Cloud, Galaxy Backbone, Benue, Cross River. | B; A only for linked/quoted primary docs |
| TechCabal / TechCabal Insights | https://techcabal.com/ and https://insights.techcabal.com/ | Strong Nigerian tech/business context, Lagos hyperscale/AI infrastructure, cloud and power constraints. | B |
| Technext | https://technext24.com/ | Useful Nigeria-focused explainer and project roundups; verify each entry because roundups mix A/B/C evidence. | B/C |
| TechAfrica News | https://techafricanews.com/ | Good for official/company announcement republication, Galaxy Backbone/state MoUs, Cross River, Airtel/Nxtra, MTN. | B |
| BusinessDay Nigeria / Guardian Nigeria / Punch / ThisDay / Premium Times / Vanguard | site-scoped search | Local business and government-investment leads, MoUs, groundbreakings, state data-centre initiatives. | B/C depending on specificity |
| Capacity Media / Data Centre Magazine / Dgtl Infra / W.Media | site-scoped search | Financing, operator strategy, subsea, hyperscale and capacity claims. Verify facility stage with operator/regulatory sources. | B/C |
| Africa Data Centres Association / Africa Data Centres ecosystem press | https://africadca.org/ and operator pages | Member/operator announcements and market context. | B |
| IXPN / PeeringDB / Packet Clearing House / LINX-style interconnect sources | https://www.ixp.net.ng/ , https://www.peeringdb.com/ , https://www.pch.net/ixp | Confirms interconnection locations and datacenter ecosystems, especially Lagos and Abuja. | B/C; not facility capacity |
| Subsea/cable sources | MainOne, WIOCC/Equiano, 2Africa, Glo1, ACE, WACS, SAT-3 pages | Cable landing and interconnect clues for Lagos/Port Harcourt. | A/B depending on source |
| Aggregators | Baxtel, DataCenterMap, OCOLO, Datacenters.com, Cloudscene | Useful address/name leads, especially smaller Lagos facilities. Never use alone for final capacity/status. | C/B- |

Trade-press scoped queries:

```text
site:datacenterdynamics.com/en/news/ Nigeria "data center" "MW"
site:datacenterdynamics.com/en/news/ Lagos "data center" "{operator}"
site:datacenterdynamics.com/en/news/ Nigeria "Rack Centre" OR "MainOne" OR "Equinix"
site:techcabal.com Nigeria "data centre" Lagos
site:insights.techcabal.com Nigeria "data centres" "AI"
site:technext24.com Nigeria "data centre" "MW"
site:techafricanews.com Nigeria "data centre" "{state}"
site:businessday.ng Nigeria "data centre" Lagos
site:guardian.ng Nigeria "data centre" "{state}"
site:punchng.com Nigeria "data centre" "{state}"
site:thisdaylive.com Nigeria "data centre" "{state}"
```

Capture exact stage language:
- **Intent/MoU**: `plans`, `to build`, `proposes`, `signs MoU`, `partners`, `seeks approval`.
- **Site/procurement**: `land acquired`, `groundbreaking`, `construction starts`, `tender`, `EIA disclosure`, `NERC/CPG`, `building permit`.
- **Delivery**: `commissioned`, `launched`, `opened`, `ready for service`, `Uptime constructed facility`, `customer live`.

---

## 2. Operator and developer sweep

Official operator pages are **A for marketed facility existence/current footprint**. Use them as seeds for official verification.

| Operator / developer | Official / useful URL | Priority locations | Notes |
|---|---|---|---|
| Equinix / MainOne / MDXi | MainOne https://mainone.net/ ; Equinix Lagos https://www.equinix.com/data-centers/europe-colocation/nigeria-colocation/lagos-data-centers ; Equinix PR1 release https://www.equinix.com/newsroom/press-releases/2025/04/equinix-to-open-first-data-center-in-port-harcourt-and-bring-2africa-subsea-cable-to-nigeria | Lagos/Lekki LG1/LG2/LG3; Rivers/Port Harcourt PR1; historic Ogun/Sagamu lead | Search `MDXi`, `MainData`, `MainOne`, `Equinix`, `LG1`, `LG2`, `LG3`, `PR1`, `Lekki II`, `2Africa`, `Sagamu`. |
| Rack Centre | https://rack-centre.com/ ; LGS2 https://rack-centre.com/lagos-data-centre-campus-expansion/data-centre-campus-lgs-2-expansion/ | Lagos Oregun/Ikeja | LGS2 official page gives 12 MW IT power and 25 MVA utility supply. Join to NERC CPG and Lagos permits. |
| Africa Data Centres / Cassava | https://www.africadatacentres.com/lagos/ | Lagos/Eko Atlantic | Official LOS1 page is primary for Lagos presence; industry coverage gives MW/white-space claims that need confirmation from current page or release. |
| Open Access Data Centres / WIOCC | https://www.openaccessdc.net/lagos | Lagos Ikate/Lekki; possible state MoU leads via WIOCC | Official OADC Lagos page gives 7,200 m2 technical space and 24 MW site load; Equiano landing-station role is a major interconnection clue. |
| Digital Realty / Medallion | Digital Realty Lagos https://www.digitalrealty.com/data-centers/emea/lagos ; Medallion opening/rebrand https://www.digitalrealty.com/about/newsroom/press-releases/123225/medallion-opens-new-data-centre-in-lagos-and-rebrands-to-digital-realty- | Lagos Victoria Island, Lekki | Search old name `Medallion Communications`, `MCL`, `Teleafrica`, `LOS1`, `LOS2`, `LKK1`, `LKK2`. |
| Galaxy Backbone | https://galaxybackbone.com.ng/ ; FAQ https://galaxybackbone.com.ng/ufaqs/does-galaxy-backbone-operate-a-datacentre/ | Abuja/FCT, Kano; state hosted-service partnerships | Government-owned backbone/cloud provider. Do not turn hosted-service MoUs into new state datacenters unless a physical build is named. |
| Kasi Cloud | https://www.kasicloud.com/ ; NSIA release https://nsia.com.ng/kasi-cloud-ltd-breaks-ground-in-lagos-nigeria-on-new-hyperscale-data-center/ | Lagos/Lekki LOS campus; Akwa Ibom/Eket DNEK campus | Official site lists DNEK coming soon in Eket; newsroom links to Lagos groundbreaking. Verify 2026 commissioning/operational claims with primary current source. |
| MTN Nigeria | https://www.mtn.ng/ plus NERC/NCC/Uptime | Lagos Ojota/Ajao/Ikoyi/Apapa; Abuja; Ibadan; Enugu; Kano; Kaduna; Uselu/Benin; Owerri | Many are telecom switch/data-centre sites. Count commercial colocation/cloud only when operator/service page supports it. |
| Airtel Africa / Nxtra | https://www.airtel.africa/data-centers | Lagos/Eko Atlantic lead | Search `Nxtra Lagos`, `Airtel Nigeria data centre`, `Eko Atlantic`, `34MW`, `38MW`; require official Airtel/Nxtra confirmation. |
| 21st Century Technologies | https://www.21ctl.com/ | Lagos Lekki and fibre routes | NCC shows telecom/fibre licences; aggregator entries may mention colo. Verify on operator page. |
| ipNX / Cyberspace / inq.Digital / NTT / Excelsimo / interconnectnigeria / Layer3 | own sites + NCC register + directories | Mostly Lagos, Abuja, Port Harcourt | Smaller enterprise/edge facilities. Treat directory-only capacity as C until corroborated. |
| Tetracore Energy / Huawei / energy-park projects | Tetracore/operator pages + energy press | Ogun/Atakobo/Ijebu East | Energy-linked datacenter claims need NERC/EIA/state planning proof. |
| UniCloud Africa / Benue Digital Infrastructure Company | https://unicloudafrica.africa/ and state/local press | Benue/Makurdi | MoU/state cloud lead. Confirm state procurement, parcel, and construction before operational status. |
| Nugi Group / 9mobile state partnerships | operator/local press | Cross River/Calabar | Good leads; typically early-stage. Search for land allocation, EIA, permit, or state budget follow-up. |

Operator query templates:

```text
"{operator}" Nigeria "data centre" "MW"
"{operator}" Nigeria "data center" "racks"
"{operator}" Lagos "data centre" ("opened" OR launched OR commissioned OR "ready for service")
"{operator}" "{state}" Nigeria ("data centre" OR "data center" OR datacentre)
"{operator}" "{town}" ("NERC/CPG" OR "captive power" OR MVA)
"{operator}" "{town}" ("EIA" OR "environmental impact assessment" OR "building permit")
"{facility}" "Uptime Institute" Nigeria
"{facility}" "NCC" "Collocation"
```

---

## 3. Cloud, edge, IXP, and subsea discovery

### 3.1 Hyperscaler and edge signals

- **AWS**: official AWS Local Zones docs list Nigeria (Lagos) Local Zone `af-south-1-los-1a`. This is a strong Lagos seed, not a full AWS Region. Search operator/colo hosts and AWS partner/customer announcements.
- **Azure**: official Azure regions list does not show Nigeria. NCC has a Microsoft/data-centre-infrastructure policy press release. Use as demand/policy lead only.
- **Google Cloud**: official region list does not show Nigeria. Google Equiano subsea cable and CDN/interconnect sources are useful Lagos/OADC/MainOne/WIOCC leads.
- **Oracle OCI**: official public-region pages do not show Nigeria. Use Oracle mentions as customer/partner leads, not facility evidence.

Cloud/edge queries:

```text
"AWS Local Zone" Lagos Nigeria "af-south-1-los-1a"
"AWS" Lagos Nigeria "Local Zone" "data center"
"Azure" Nigeria "data centre" Microsoft NCC
"Google Equiano" Nigeria "data centre" Lagos
"Oracle" Nigeria "data centre" Lagos
"cloud region" Nigeria Lagos "data centre"
```

### 3.2 Interconnection, IXP, and cable routes

Interconnection sources are good for identifying active datacenter ecosystems, but they do not prove MW/capacity.

High-yield terms:
- `IXPN`, `Internet Exchange Point of Nigeria`, `Lagos IX`, `Abuja IX`, `Kano IX`, `Port Harcourt IX`.
- `Equiano landing station`, `2Africa`, `MainOne cable`, `Glo1`, `ACE`, `WACS`, `SAT-3`.
- `meet-me room`, `carrier neutral`, `open access`, `peering`, `cross-connect`, `interconnect exchange`.

Queries:

```text
site:ixp.net.ng "data centre"
site:peeringdb.com "Lagos" "data center"
site:pch.net "Lagos" "Nigeria" "IXP"
"IXPN" "Rack Centre" OR "MainOne" OR "OADC" OR "Medallion"
"Equiano" "OADC Lagos" "data centre"
"2Africa" "Port Harcourt" "data center" Equinix
"MainOne cable landing station" "Lekki" "data centre"
"Glo1" Lagos "data centre"
```

---

## 4. State-level industry enumeration matrix

For every state/FCT, run:
1. `state + capital + data centre/data center/datacentre`.
2. `state + known operators`.
3. `state + NCC/NERC/EAD/Uptime`.
4. `state + fibre/subsea/IXP/power/industrial park`.
5. Local press and aggregator pass only after official/operator searches.

Universal query block:

```text
"{state}" Nigeria ("data centre" OR "data center" OR datacentre) ("MW" OR MVA OR racks OR "IT load")
"{state capital}" Nigeria ("data centre" OR "data center") ("opened" OR launched OR commissioned OR construction)
"{state}" Nigeria ("colocation" OR "carrier neutral" OR hyperscale OR "AI-ready")
"{state}" Nigeria ("cloud" OR "sovereign cloud" OR "state data centre")
"{state}" Nigeria ("Tier III" OR "Tier IV" OR "Uptime Institute")
"{state}" Nigeria ("captive power" OR "substation" OR "gas power" OR "solar") "data centre"
"{operator}" "{state OR town}" Nigeria "data centre"
site:datacenterdynamics.com/en/news/ Nigeria "{state}"
site:techcabal.com Nigeria "{state}" "data centre"
site:technext24.com Nigeria "{state}" "data centre"
site:techafricanews.com Nigeria "{state}" "data centre"
```

### 4.1 Priority states/FCT

| State/FCT | Main towns/localities | Industry seeds | Query notes |
|---|---|---|---|
| Lagos | Lekki, Victoria Island, Ikoyi, Ikeja, Oregun, Eko Atlantic, Ikate Elegushi, Yaba, Apapa, Ojota, Gbagada, Ajao Road | Equinix/MainOne/MDXi, Rack Centre, ADC, OADC/WIOCC, Digital Realty/Medallion, Kasi, MTN, Airtel/Nxtra, 21st Century, ipNX, Cyberspace, NTT/inQ, Excelsimo, AWS Local Zone | Highest-recall pass. Run each operator plus locality. Separate Lekki/Eko Atlantic/Victoria Island/Oregun/Ojota to avoid duplicate Lagos-only records. |
| Abuja Federal Capital Territory | CBD, Maitama, Garki, Wuse, Utako, Gwarinpa | Galaxy Backbone, federal government cloud, NCC/NITDA, MTN Abuja switch, Layer3/enterprise DCs | Government/shared-services focus. Search hosted-state partnerships carefully; many use Abuja/Kano GBB facilities rather than new state sites. |
| Kano | Kano city, Ahmadu Bello Way, Challawa | Galaxy Backbone Tier IV, MTN Kano Switch, North West Infraco/fibre | Uptime + Galaxy official first. Check if any commercial colo exists beyond government/telco. |
| Rivers | Port Harcourt, Bonny, Onne, Trans Amadi, Rumuolumeni | Equinix/MainOne PR1, 2Africa, interconnectnigeria, oil/gas captive power, IXPN/edge | Search `Port Harcourt data center PR1`, `2Africa landing`, `Rivers State ICT`, `Bonny data centre`; distinguish oil/gas comms rooms from colo. |
| Ogun | Sagamu, Flowergate Industrial Park, Atakobo, Ijebu East, Ota | MainOne Sagamu historic project, Tetracore/Huawei Atakobo energy-park lead, industrial estates | Old Sagamu announcement may be stale/unbuilt. Require recent operator/permit/NERC proof. |
| Akwa Ibom | Eket, Uyo, Qua Iboe | Kasi DNEK campus, oil/gas power, state ICT | Search `Kasi Cloud DNEK`, `Eket data centre`, `Akwa Ibom data center`; verify DNEK status. |
| Cross River | Calabar, Tinapa/free-trade zone | Nugi Group Tier 4 plan, 9mobile government proposal | Early-stage leads. Search state government, land/permit/EIA, hydro/solar/gas claims. |
| Benue | Makurdi | Benue Digital Infrastructure Company, UniCloud Africa, Africa Data Centres DR references | MoU likely; confirm procurement/site/construction before counting. |
| Abia | Aba, Umuahia, Ohafia, Owaza River | WIOCC/OADC state broadband/connectivity/data-centres MoU | Search WIOCC duct infrastructure and state official releases; no site-level facility unless a build is named. |
| Enugu | Enugu city | MTN Enugu Switch, NCC collocation licensee addresses, state digital-government initiatives | Use NERC/NCC to confirm telco switch; watch for server rooms mislabelled as data centres. |
| Oyo | Ibadan | MTN Ibadan Switch, FarmKonnect precision-farming data centre, state ICT | FarmKonnect is agri/data operations, not commercial colo. |
| Kaduna | Kaduna city, Kakuri | MTN Kaduna Switch, Kaduna Bureau of Statistics/state data centre, North West fibre | Mostly government/statistics/telco; verify function. |
| Edo | Benin City, Uselu | MTN Uselu, Edo government data centre/digital state programme | Search Edo state official + NERC/NCC. |
| Borno | Maiduguri | Borno State Data Center, eHealth Africa/World Bank support | Public-sector/humanitarian data-management facility. |
| Bayelsa | Yenagoa, ICT Village, oil/gas creek sites | Bayelsa ICT Village secure data center; off-grid/flare-gas data-center/mining leads | Official state source for ICT Village. Treat off-grid social leads as C unless NERC/EIA/operator proof exists. |

Priority-cluster templates:

```text
"Lagos" Nigeria ("Rack Centre" OR "MainOne" OR Equinix OR OADC OR "Africa Data Centres" OR Kasi OR Nxtra OR Medallion) "data centre"
"Lekki" Nigeria ("data centre" OR "data center") ("MainOne" OR Equinix OR OADC OR Kasi)
"Oregun" Lagos "Rack Centre" "NERC/CPG"
"Eko Atlantic" Lagos ("data centre" OR "data center") ("Africa Data Centres" OR Nxtra)
"Port Harcourt" Nigeria Equinix PR1 "data center"
"Kano" "Galaxy Backbone" "Tier IV" "data centre"
"Abuja" "Galaxy Backbone" "Tier III" "data centre"
"Eket" "Kasi Cloud" "data centre"
"Atakobo" Ogun "data centre" Huawei Tetracore
"Makurdi" Benue "data centre" UniCloud
"Calabar" "data centre" "Nugi" OR "9mobile"
```

### 4.2 Secondary-state sweep

These states usually surface as government ICT/data rooms, telecom switches, fibre MoUs, or negative searches. Use state capital plus operator terms, then official verification.

| State group | States | Main additions |
|---|---|---|
| South East | Abia, Anambra, Ebonyi, Enugu, Imo | Add `Aba`, `Umuahia`, `Awka`, `Abakaliki`, `Enugu`, `Owerri`, `Zinox Infraco`, `South East Infraco`, `state data centre`, `MTN switch`, `Galaxy Backbone partnership`. |
| South South | Akwa Ibom, Bayelsa, Cross River, Delta, Edo, Rivers | Add `Eket`, `Uyo`, `Yenagoa`, `Calabar`, `Asaba`, `Benin`, `Port Harcourt`, `oil and gas`, `captive power`, `Raeanna Infraco`, `subsea`, `landing station`. |
| South West excluding Lagos | Ekiti, Ogun, Ondo, Osun, Oyo | Add `Ado-Ekiti`, `Abeokuta`, `Sagamu`, `Atakobo`, `Akure`, `Osogbo`, `Ibadan`, `Oodua Infraco`, `industrial park`, `free zone`, `farm data centre`. |
| North Central | Benue, Kogi, Kwara, Nasarawa, Niger, Plateau, FCT | Add `Makurdi`, `Lokoja`, `Ilorin`, `Lafia`, `Minna`, `Jos`, `Abuja`, `Broadbased Infraco`, `innovation hub`, `state ICT`, `development control`. |
| North West | Jigawa, Kaduna, Kano, Katsina, Kebbi, Sokoto, Zamfara | Add `Dutse`, `Kaduna`, `Kano`, `Katsina`, `Birnin Kebbi`, `Sokoto`, `Gusau`, `Fleek Infraco`, `Galaxy Backbone Kano`, `MTN switch`, `mini data centre`. |
| North East | Adamawa, Bauchi, Borno, Gombe, Taraba, Yobe | Add `Yola`, `Bauchi`, `Maiduguri`, `Gombe`, `Jalingo`, `Damaturu`, `Brinks Infraco`, `humanitarian data centre`, `Galaxy Backbone partnership`, `ICT hub`. |

---

## 5. Aggregator and directory handling

Useful aggregator routes:

```text
site:baxtel.com Nigeria "data center" "{operator}"
site:datacentermap.com/nigeria "Lagos" "data center"
site:ocolo.io/data-centers/nigeria "{operator}"
site:datacenters.com Nigeria "{operator}" "data center"
site:cloudscene.com Nigeria "data centre"
```

Rules:
- Use aggregators to find alternate facility names, addresses, coordinates, and legacy operators.
- Never accept aggregator MW/status without operator, Uptime, NERC, NCC, EAD, or permit corroboration.
- Be cautious with parent/subsidiary changes: `MDXi -> MainOne -> Equinix`, `Medallion -> Digital Realty/Teleafrica`, `WIOCC -> OADC`, `Dimension Data/Internet Solutions -> NTT/inQ/OADC depending transaction`.
- Avoid double-counting a campus and individual buildings unless the target schema wants facility-level units.

---

## 6. Final validation checklist

Before emitting a Nigeria facility record:
- Has the source identified a **physical location** at least to state + city/locality?
- Is the project a real datacenter/colo/cloud facility, not just a government statistics database, call centre, training hub, telecom mast, office server room, or fibre route?
- Is the status supported by stage language and date?
- Are capacity fields separated into IT load, site load, MVA import, captive generation MW, racks, and white space?
- Is there a primary source for A grade? If only DCD/local press, keep B. If only aggregator/social, keep C or U.
- For Lagos, deduplicate by operator + campus: Lekki/MainOne-Equinix, Oregun/Rack Centre, Eko Atlantic/ADC-Nxtra, Ikate/OADC, Victoria Island/Medallion-Digital Realty, Lekki/Kasi.
- For FCT/Kano, do not duplicate Galaxy Backbone hosted-service partnerships as new facilities in partner states.
