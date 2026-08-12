# ZW Explorer Industry - Zimbabwe Datacenter Enumeration via Operators, Colo, Telco, IXP, and Trade Press

Date: 2026-08-12. Country: **ZW Zimbabwe**. Division model: **10 provinces**: Bulawayo; Harare; Manicaland; Mashonaland Central; Mashonaland East; Mashonaland West; Matabeleland North; Matabeleland South; Midlands; Masvingo. Angle: **industry/operator-first discovery**, reconciled against official records in `explorer-official.md`.

Reliability grades are field-level:
- **A** = operator-owned page, official government/regulator/council/procurement/power/investment record, official cloud-region page, or signed government/operator announcement for the exact claim.
- **B** = strong named secondary/trade source: DCD, Ecofin Agency, Techzim, 263Chat, The Herald, The Chronicle, Bulawayo24, NewZimbabwe.com, TechnoMag, Mbare Times, ITWeb Africa, Developing Telecoms, Connecting Africa, Capacity, vendor case study, PeeringDB/PCH/IX-F for network presence.
- **C** = lead only: directories, social posts, aggregator pages, generic market reports, unsupported addresses/capacity, and regional expansion articles with no Zimbabwe site evidence.
- **U** = not verified in this review. Re-check before use.

Use industry sources to find candidates, then promote only the exact fields confirmed by operator or official evidence. A single candidate can have A-grade operator existence, B-grade capacity, and C-grade address.

---

## 0. Market Structure

Zimbabwe is a small, early-stage, **Harare-centred** datacenter market. Confirmed or high-confidence facility evidence clusters in Harare, with a confirmed TelOne node in Bulawayo and a TelOne satellite facility at Mazowe in Mashonaland Central.

Operational / high-confidence seeds:
- **TelOne**: official pages list Data Centre & Cloud Services, Data Centre & Hosted Services, Colocation, Disaster Recovery as a Service, and Rack Space Rental. The TelOne page describes its data centre as a `Tier 3 Data Centre Environment`; the hosted-services pages show Runhare House, 107 Kwame Nkrumah Avenue, Causeway, Harare. This is A-grade for TelOne's Harare datacenter service and address, but not Uptime certification. Techzim reported the March 2017 Harare launch as the first phase of the National Data Centre.
- **TelOne Mazowe Earth Station Data Centre**: DCD reported the March 2022 launch at Mazowe Earth Station as TelOne's fourth data center, 34 racks, 1,300 sqm. TechnoMag and other local press report the same launch as a US$1m expansion. Grade B for rack/area/cost/count unless TelOne official documents confirm. Map Mazowe to **Mashonaland Central**, not Harare.
- **TelOne Bulawayo Data Centre**: DCD, Ecofin, Techzim, 263Chat, and Herald/Zimpapers coverage report an April 2022 launch, 120 racks, 400 kVA or 400 kW depending on publisher wording, and `Tier 3 Designed`/`Tier 3 by design`. Grade B for rack/power/tier wording; directory address is C unless confirmed by TelOne/council.
- **Econet Wireless Zimbabwe / Econet Data Centre (EDC)**: The Herald, TechnoMag, Bulawayo24, and Mbare Times reported a new 5 MW Harare data centre with corporate onboarding from late June 2025, designed/built with Africa Data Centres as a sister-company capability, and plans to double to 10 MW for AI demand. Grade B for 5 MW/date/status until an Econet-owned page or official filing is found.
- **Liquid Intelligent Technologies Zimbabwe**: official country page confirms Zimbabwe presence at Block B, Stand 45 and 47, Sam Levy Office Park, Piers Road, Borrowdale, Harare, and describes Liquid as a large data, voice and IP provider in Zimbabwe. Grade A for operator presence/services and address; directory claims for a `Liquid Zimbabwe DC`, Tier 3, and PUE are C unless a Liquid/Africa Data Centres facility page confirms.
- **Dandemutande / Utande**: operator existence is A via its website; industry history includes a 2011 Techzim interview about Harare datacenter/SEACOM connectivity and C-grade colo.exchange/directory entries. DCD reported in February 2025 that Dandemutande planned a US$15m Tier III carrier-neutral data center under ITU Partner2Connect, expected live by June 2026, with location/specs not disclosed. Grade B for the plan; completion was not confirmed in this review.
- **Government National Data Centre**: Techzim ties TelOne's 2017 Harare launch to the first phase; Bulawayo24 reported February 2021 commissioning by the President; Ministry ICT pages reference the National Data Centre project. Grade A for Ministry project context, B for commissioning/date details unless an official project page gives specifics.
- **ZOL Zimbabwe / Liquid Home Zimbabwe**: former ZOL broadband brand now routes publicly to Liquid Home Zimbabwe (`zw.liquidhome.tech`); use it as a legacy ISP/hosting/colocation lead in Harare. Treat old ZOL datacenter claims as B/U until a current Liquid/ZOL-owned page explicitly claims a datacenter or colocation in its own facility.

Do not count these as datacenters without named facility evidence: NetOne, Telecel, Powertel, IMC/Starlink, ZINX/HIX, CDN/cache nodes, fibre nodes, POTRAZ Digital Centres, cloud resellers, bank server rooms, mining control rooms, or university server rooms.

No official AWS, Azure, Google Cloud, or Oracle OCI public cloud region is listed in Zimbabwe as of 2026-08-12. Nearest official public cloud regions are in South Africa. No Uptime Institute Zimbabwe Tier-certified facility was found in searched official results. Re-check annually.

---

## 1. Search Vocabulary

Industry discovery is English-first. Run Shona/Ndebele sweeps only to document completeness.

```text
data centre / data center / datacentre
server farm / server room / server hosting
colocation / colo / co-location / carrier-neutral
hosting / managed hosting / dedicated servers / web hosting
cloud / cloud computing / local cloud / sovereign cloud / IaaS / PaaS / SaaS / Azure Stack
Tier III / Tier 3 / Tier III by design / Uptime Institute
network operations centre / NOC / internet exchange point / IXP / peering / ZINX / HIX
submarine cable / landing station / backhaul / international gateway / SEACOM / EASSy / WACS
fibre / fibre-optic / backbone / dark fibre / bandwidth
data sovereignty / data localisation / disaster recovery / DR / business continuity
power / solar / generator / UPS / captive power / PPA / ZESA / load-shedding
```

Local-language sweep:
```text
"data centre" Zimbabwe Shona OR Ndebele
indaneti maseva kombuta
"nzvimbo yekuchengetedza data" OR "isikhungo sedatha"
```

---

## 2. Operator and Facility Seed List

| Operator / platform | URLs | Zimbabwe signal | Likely locations | Grade discipline |
|---|---|---|---|---|
| **TelOne Harare** | https://www.telone.co.zw/ ; https://www.telone.co.zw/products/details/data-centre-cloud-services ; https://www.telone.co.zw/Products/Details/data-centre--hosted-services ; https://www.telone.co.zw/Products/Details/colocation | Official data-centre/cloud/colo/DR/rack services; `Tier 3 Data Centre Environment`; Runhare House, 107 Kwame Nkrumah Avenue, Causeway | Harare | A for service/address/operator wording; B for 2017 launch/National Data Centre first-phase press; no Uptime certification found |
| **TelOne Mazowe Earth Station DC** | https://www.datacenterdynamics.com/en/news/telone-opens-data-center-at-mazowe-earth-station-zimbabwe/ ; https://technomag.co.zw/telone-launches-us1m-mazowe-data-centre-expansion-project/ | March 2022 launch at Mazowe Earth Station; DCD says fourth TelOne DC, 34 racks, 1,300 sqm | Mazowe, Mashonaland Central | B for rack/area/cost/count; C for directory entries; official facility page still needed |
| **TelOne Bulawayo DC** | https://www.datacenterdynamics.com/en/news/telone-launches-data-center-in-bulawayo-zimbabwe/ ; https://www.ecofinagency.com/telecom/0305-43573-zimbabwe-telone-inaugurates-bulawayo-data-center-for-enhanced-internet ; https://www.techzim.co.zw/2022/04/telone-officially-opens-its-first-matabeleland-data-centre/ | April 2022 launch; 120 racks; 400 kVA/kW depending on report; Tier 3 designed/by design | Bulawayo | B for capacity and tier wording; C for directory address until operator/council confirms |
| **Econet Data Centre (EDC)** | https://www.heraldonline.co.zw/econet-unveils-5-mw-data-centre/ ; https://technomag.co.zw/econet-launches-5-megawatt-data-centre-to-power-zimbabwes-digital-future/ ; https://bulawayo24.com/index-id-news-sc-national-byo-253712.html | 5 MW Harare data centre; corporate onboarding late June 2025; possible 10 MW expansion | Harare | B for 5 MW/status/date; A only after Econet-owned confirmation or official filing |
| **Econet InfraCo airport industrial/IT park** | https://itweb.africa/article/econet-approves-ambitious-harare-it-park-data-centre/RgeVDMPRgo1vKJN3 | 300 ha park near Harare airport, 100 MW solar, large-scale data centre concept | Harare airport corridor | B/C planned/MoU-intent; no permit, site, power licence, or construction evidence found |
| **Liquid Intelligent Technologies Zimbabwe** | https://liquid.tech/local-offices/country/zimbabwe/ ; https://liquid.tech/data-centres/ | Official Zimbabwe office and wholesale data/voice/IP services; directories list a Harare DC | Harare, Borrowdale/Sam Levy area | A for office/operator/services; C for DC specs until Liquid/ADC facility page confirms |
| **Dandemutande / Utande** | https://www.dandemutande.co.zw/ ; https://www.datacenterdynamics.com/en/news/zimbabwean-it-provider-dandemutande-plans-15m-data-center/ ; https://colo.exchange/data-centers/utande-internet-services-utande-internet-services | Existing Harare colo lead; US$15m Tier III carrier-neutral P2C project expected by June 2026 | Harare likely, site undisclosed | A for operator; B for plan; C for directory/social claims; completion unconfirmed |
| **ZOL Zimbabwe / Liquid Home Zimbabwe** | https://zw.liquidhome.tech/ ; https://zw.myliquidhome.tech/knowledgebase/sme-migration-from-zol-to-liquid-business/283/what-changes-should-i-expect-to-see-with-the-migration-from-zol-zimbabwe-to-liquid-business | Legacy ZOL ISP/hosting/colo lead; current Liquid Home pages document migration from `zol.co.zw` to `zw.liquidhome.tech` | Harare | U/B for old colo/DC claim until a current owned page confirms it |
| **National Data Centre** | https://www.ictministry.gov.zw/pages/projects ; https://www.techzim.co.zw/2017/03/telone-launch-new-data-centre/ ; https://bulawayo24.com/index-id-news-sc-national-byo-199954.html | Ministry project context; press-reported commissioning and TelOne first phase | Harare expected | A for Ministry project context; B for launch/date/location details |
| **ZINX / Zimbabwe Internet Exchange** | https://zispa.org.zw/ ; https://www.pch.net/ixp/details/364 ; https://www.peeringdb.com/org/21434 | IXP/network-presence signal | Harare | B for network evidence; not facility proof |
| **NetOne / Telecel / Powertel / IMC-Starlink** | https://www.netone.co.zw/ ; https://www.telecel.co.zw/ ; https://www.energy.gov.zw/?page_id=1855 | Telecom/connectivity operators | National | Lead only unless a physical datacenter is named |

Operator queries:
```text
"{operator}" Zimbabwe "data centre" OR "data center" OR "colocation"
"{operator}" Zimbabwe "Tier III" OR "Tier 3" OR "by design"
"{operator}" Zimbabwe "MW" OR "MVA" OR "kVA" OR "racks" OR "cabinets"
"{operator}" Zimbabwe "local cloud" OR "sovereign cloud" OR "IaaS" OR "DRaaS"
"{operator}" "POTRAZ" OR "ZERA" OR "ZIDA" OR "EMA" OR "PRAZ" Zimbabwe
"{operator}" "Harare" OR "Bulawayo" OR "Mazowe" "data centre"
"{operator}" "MoU" OR "Partnership" "data centre" Zimbabwe
```

---

## 3. Trade Press and Industry Media

Use trade press for discovery, dates, capacities, and pipeline leads. Reconcile each field against operator/official records.

High-yield reviewed sources:
- DCD: TelOne Mazowe launch; TelOne Bulawayo launch; Dandemutande US$15m plan; older TelOne/Huawei two-data-centre coverage. Grade B.
- Ecofin Agency: TelOne Bulawayo, 120 racks, 400 kVA, Tier 3 designed. Grade B.
- Techzim: TelOne 2017 Harare/National Data Centre first phase; TelOne Bulawayo; POTRAZ IXP; Starlink licence. Grade B.
- The Herald / HeraldOnline: Econet 5 MW Harare data centre; TelOne Bulawayo. Grade B.
- Bulawayo24 / Mbare Times / TechnoMag: Econet EDC onboarding and 5 MW; local operator launches. Grade B, with care for republication.
- NewZimbabwe.com / 263Chat: TelOne Mazowe/National Data Centre context. Grade B.
- ITWeb Africa: Econet InfraCo Harare airport industrial/IT park, 300 ha and 100 MW solar. Grade B for reported plan only.
- Telecoms Chamber / Structure & Design Zimbabwe / Telecompaper: Dandemutande P2C project. Grade B/C depending on source chain; do not treat as completion.
- Directories: datacentermap, Baxtel, colo.exchange, GoDataCenters, DatacenterPlanet. Grade C until matched to operator/official evidence.

Press queries:
```text
site:techzim.co.zw "data centre" OR "data center" OR "colocation" OR "cloud" Zimbabwe
site:heraldonline.co.zw "data centre" OR "data center" "Econet" OR "TelOne"
site:chronicle.co.zw "data centre" OR "data center" "Bulawayo" OR "Matabeleland"
site:newzimbabwe.com "data centre" OR "data center" "TelOne" OR "Econet" OR "Dandemutande"
site:bulawayo24.com "data centre" OR "data center" "Zimbabwe"
site:datacenterdynamics.com Zimbabwe "data center" OR "data centre"
site:itweb.africa Zimbabwe "data centre" OR "data center" OR "IT park"
site:developingtelecoms.com Zimbabwe "data centre" OR "AI" OR "cloud"
"Zimbabwe" "first Tier III" OR "Tier 3" "data centre"
"Zimbabwe" "new data centre" "2025" OR "2026"
```

---

## 4. Network, Peering, and CDN Evidence

Network evidence identifies where to look; it rarely proves a datacenter.

- **ZINX/ZISPA**: ZISPA operates the Zimbabwe Internet Exchange and `.zw` ecosystem; PCH IXP 364 and PeeringDB org 21434 provide network evidence. Grade B for network/IXP facts, not facility proof.
- **POTRAZ-launched IXP**: Techzim reported a 2017 Zimbabwe Internet Exchange Point launch by POTRAZ. Treat as network presence unless a facility/address/operator record is found.
- **PeeringDB**: use the API/search where the web SPA is incomplete. Record ASN, organisation, IXP, and facility fields separately.
- **Directories**: use datacentermap, Baxtel, colo.exchange, GoDataCenters, and DatacenterPlanet only as C-grade leads. Directory misclassification is known for Mazowe under Harare; correct the province in the record.
- **CDN/cache**: Google Global Cache, Akamai, Netflix OCA, Meta cache, and similar clues are edge/network evidence only unless a named hosting facility is given.
- **International connectivity**: landlocked Zimbabwe depends on terrestrial fibre via Mozambique/South Africa corridors. Do not count routes as facilities.

Queries:
```text
"ZINX" OR "Zimbabwe Internet Exchange" members OR peers OR peering
site:zispa.org.zw "ZINX" OR "data centre" OR "hosting"
site:peeringdb.com Zimbabwe "Harare" OR "ZINX"
site:pch.net Zimbabwe IXP
"Google Global Cache" OR "Akamai" OR "Netflix OCA" OR "Meta CDN" Zimbabwe Harare
datacentermap Zimbabwe Harare Bulawayo TelOne Liquid Dandemutande
"Somabhula" Dandemutande fibre node data centre
```

---

## 5. Enterprise, Financial, Government, and Mining Leads

These sectors reveal demand, closed server rooms, and DR requirements. Count only with public physical-facility evidence.

- **Government/parastatal**: National Data Centre, OPC/eGP `DATACENTR` procurement, Ministry of ICT, ZIMRA, NSSA, RBZ, Registrar-General, health/education systems. Parliament/Auditor-General reports may mention backup/DR failures.
- **Financial sector**: RBZ, CBZ, Stanbic, Standard Chartered, First Capital, NMB, Steward Bank, EcoCash, OneMoney. Grade DR/server-room mentions as C unless a facility, address, or operator is named.
- **Mining/industry**: ZCDC, Zimasco, Unki, Mimosa, Blanket, lithium operators. Look for OT rooms, substations, captive power, and EMA/ZERA records; do not count operations control rooms as datacenters unless the source says so.
- **Universities/research**: University of Zimbabwe, NUST, HIT, Chinhoyi University of Technology, Midlands State University. Treat HPC/server rooms as institutional IT unless commercial datacenter services are explicit.
- **AI pipeline**: Econet AI and government AI strategy coverage may increase demand; only count data-centre construction with site/power/operator evidence.

Queries:
```text
"Reserve Bank of Zimbabwe" OR "RBZ" "data centre" OR "disaster recovery" OR "server room"
"{bank}" Zimbabwe "data centre" OR "DR site" OR "business continuity"
"EcoCash" OR "Steward Bank" "data centre" OR "hosting"
site:parlzim.gov.zw "data centre" OR "National Data Centre" OR "server"
"{mine}" Zimbabwe "data centre" OR "ICT infrastructure" OR "control room"
"Zimbabwe" "AI data centre" OR "AI factory" OR "GPU" 2025 OR 2026
"{province}" "server room" OR "ICT infrastructure" Zimbabwe
```

---

## 6. Associations and Events

- **ZISPA**: https://zispa.org.zw/ - use for IXP, member, and `.zw` leads. Grade B for association/network evidence.
- **Africa Data Centres Association**: members page lists Africa Data Centres and TelOne as active in Zimbabwe; useful as an industry lead, not facility-specific proof.
- **ZITF**: Bulawayo trade fair; monitor annual ICT/digital infrastructure announcements and TelOne/ZIDA/Econet exhibits.
- **Techzim events, POTRAZ briefings, Ministry ICT events**: useful for MoU-stage and product-launch leads.

Queries:
```text
site:zispa.org.zw "ZINX" OR "members" OR "hosting"
"ZISPA" "internet exchange" Zimbabwe members
"Africa Data Centres Association" Zimbabwe TelOne
"ZITF" "data centre" OR "ICT" OR "digital" Bulawayo
"Computer Society of Zimbabwe" "data centre" OR "ICT"
```

---

## 7. Per-Province Industry Strategy

| Province | Capital / seat | Industry anchors | Strategy and expected yield |
|---|---|---|---|
| **Harare** | Harare | TelOne Runhare House; Econet EDC; Econet InfraCo park; Liquid; Dandemutande; ZOL; National Data Centre; ZINX/HIX; telco HQs; banks | **Primary cluster.** Start with operator pages, then DCD/Ecofin/Techzim/Herald/Bulawayo24, directories, IXP members, and official confirmation. Track Econet 10 MW expansion, Dandemutande completion, OPC `DATACENTR` tender, and airport park approvals. |
| **Bulawayo** | Bulawayo | TelOne Bulawayo DC; ZITF; NUST; regional telco cores | **Second node.** Confirm TelOne details and address; watch Chronicle/ZITF/council records and bank DR. |
| **Mashonaland Central** | Bindura | TelOne Mazowe Earth Station DC | **Low but confirmed lead.** Search Mazowe/Glendale/Concession and TelOne; correct directory Harare misclassification. |
| **Manicaland** | Mutare | Harare-Beira corridor, border trade, provincial ICT | **Very low watch.** Connectivity/PoP evidence only unless a facility appears. |
| **Mashonaland East** | Marondera | Ruwa/Sunway City, provincial government, agriculture ICT | **Very low watch.** Search Sunway/Ruwa/Marondera ICT and server rooms. |
| **Mashonaland West** | Chinhoyi | Kariba power context, provincial government | **Very low watch.** Search Chinhoyi/Kariba government ICT/power-sector systems. |
| **Matabeleland North** | Lupane; Victoria Falls | Victoria Falls tourism/finance, Hwange power | **Very low watch.** Search Victoria Falls/Hwange for power-backed or finance ICT leads. |
| **Matabeleland South** | Gwanda | Beitbridge corridor | **Very low watch.** Border logistics ICT only. |
| **Midlands** | Gweru | Somabhula fibre node, mining, MSU | **Very low watch.** Dandemutande Somabhula is a fibre node, not a DC. Search Gweru/Kwekwe/mining DR. |
| **Masvingo** | Masvingo | POTRAZ Digital Centres and Starlink upgrades | **Very low watch.** Digital Centres are connectivity/public-access sites, not datacenters. |

Province query block:
```text
"{capital}" "data centre" OR "data center" OR "server room" OR "hosting" Zimbabwe
"{province}" "cloud" OR "ICT" OR "digital" OR "disaster recovery" Zimbabwe
"{capital}" "TelOne" OR "Econet" OR "NetOne" OR "Liquid" OR "Dandemutande" OR "ZOL"
site:techzim.co.zw "{province}" OR "{capital}" ICT OR data
site:bulawayo24.com "{capital}" OR "{province}" "data centre" OR ICT
site:heraldonline.co.zw "{province}" "ICT" OR "digital" OR "data"
site:chronicle.co.zw "{province}" OR "{capital}" "data centre" OR ICT
"{capital}" "substation" OR "solar" "data" Zimbabwe
```

---

## 8. Known Facilities / Projects and Evidence Status

| Facility / project | Province | Status | Evidence and grade | Re-check item |
|---|---|---|---|---|
| TelOne Harare Data Centre / Runhare House | Harare | Operational | TelOne official service/address pages (A); Techzim 2017 launch (B); 263Chat national-hub coverage (B) | Capacity and any formal certification; no Uptime listing found |
| TelOne Mazowe Earth Station Data Centre | Mashonaland Central | Operational; opened Mar 2022 | DCD (B: fourth DC, 34 racks, 1,300 sqm); TechnoMag (B: US$1m expansion); directories (C) | Official TelOne facility page; total TelOne DC count |
| TelOne Bulawayo Data Centre | Bulawayo | Operational; launched Apr 2022 | DCD/Ecofin/Techzim/263Chat/Herald (B: 120 racks, 400 kVA/kW, Tier 3 designed); datacentermap address (C) | Official rack/power/address confirmation |
| Econet Data Centre (EDC) | Harare | Operational per 2025 press; onboarding clients | Herald/TechnoMag/Bulawayo24/Mbare Times (B: 5 MW, onboarding late Jun 2025, 10 MW expansion intent) | Econet-owned page, exact address, power/certifications |
| Econet InfraCo airport industrial/IT park + data centre | Harare | Planned / MoU-intent | ITWeb Africa and related reports (B/C: 300 ha, 100 MW solar, airport area) | ZIDA, ZERA, ZETDC, council, EMA, or construction evidence before counting |
| Liquid Zimbabwe DC lead | Harare | Lead / possible operational facility | Liquid country page (A for office/services); directory claims (C) | Liquid/Africa Data Centres official facility page and specs |
| Dandemutande / Utande existing colo | Harare | Operational lead | Operator site (A for company); Techzim 2011 (B); colo.exchange/social/directory (C) | Current official colo page and facility address |
| Dandemutande US$15m Tier III carrier-neutral DC | Site not disclosed, likely Harare | Planned/under construction; target Jun 2026 not confirmed | DCD/Telecoms Chamber/Telecompaper/Structure & Design (B/C) | Completion/opening, site, power, permits |
| Government National Data Centre | Harare expected | Operational/project context | Ministry project page and Broadband Plan (A context); Techzim/Bulawayo24 (B launch details) | Exact operator, address, capacity, public/private service scope |
| ZOL / Liquid Home colocation-data-centre legacy claim | Harare | Lead | Current Liquid Home pages document the ZOL-to-Liquid migration; old ZOL DC/colo claims are not current facility proof | Find a current Liquid/ZOL-owned datacenter or colocation product page |
| ZINX / Zimbabwe Internet Exchange | Harare | Network/IXP, not DC | ZISPA/PCH/PeeringDB/Techzim (B) | Current members/facility field; do not count as DC |
| NetOne / Telecel / Powertel core infrastructure | National | Lead only | Operator/government existence (A); no DC evidence | Any named DR/data-centre records |
| Hyperscaler public regions | n/a | None in Zimbabwe | Official AWS/Azure/GCP/OCI pages (A) | Annual re-check |
| Uptime Institute Tier-certified facilities | n/a | None found | Uptime certification list surface (A); no ZW result found | Annual re-check and on any Tier claim |

---

## 9. Confirmation Workflow

1. Seed from operator pages: TelOne, Econet, Liquid, Dandemutande, ZOL, National Data Centre, NetOne, Telecel, Powertel.
2. Add B/C leads from trade press, directories, PeeringDB/PCH/IX-F, and associations.
3. Reconcile each candidate against official trails in `explorer-official.md`: POTRAZ/DPA, ZERA/ZETDC/ZESA, ZIDA, PRAZ/eGP, EMA, councils, Ministry ICT.
4. Run the full ten-province sweep and explicitly record `no confirmed facility found` for provinces without evidence.
5. Grade each field independently and preserve exact source units/wording.
6. Never upgrade `Tier 3`, `Tier III`, `Tier 3 Designed`, or `Tier 3 Data Centre Environment` to Uptime-certified Tier III without Uptime evidence.

Master query bank:
```text
"Zimbabwe" "data centre" "Harare" "Tier"
"Zimbabwe" "data center" "MW" OR "racks" OR "kVA"
"TelOne" "data centre" Mazowe OR Bulawayo OR Harare
"Econet Data Centre" OR "EDC" Harare 5MW OR 10MW
"Dandemutande" "data centre" "Tier 3" OR "carrier-neutral" OR "$15"
"Liquid" OR "Africa Data Centres" Zimbabwe "data centre"
"National Data Centre" Zimbabwe e-government Huawei TelOne
"ZINX" OR "Zimbabwe Internet Exchange" members facility
"Zimbabwe" "AI data centre" OR "AI factory" 2026
"{operator}" "POTRAZ" OR "ZERA" OR "ZIDA" OR "EMA" OR "PRAZ" Zimbabwe
```

---

## 10. Source Notes From This Review

Verified A-grade URLs used in this methodology include TelOne service pages, Liquid Zimbabwe country page, POTRAZ pages and DPA portal, ZimLII/Veritas data-protection law and S.I. 155 of 2024, ZERA, ZETDC, ZIDA/eRegulations, PRAZ/eGP, Ministry of ICT projects page, Government of Zimbabwe province pages, EMA, Harare and Bulawayo council sites, official cloud-region pages, Uptime certification list, ZISPA/PCH/PeeringDB for network evidence.

Honest downgrades retained:
- Econet EDC 5 MW and 10 MW expansion are B until Econet or official records confirm.
- Econet InfraCo airport park is B/C `planned` or `MoU/intent`, not a counted facility.
- Dandemutande US$15m facility completion by June 2026 is unconfirmed as of this review.
- Liquid Zimbabwe datacenter specs are C directory evidence.
- ZOL/Liquid Home legacy colo/DC claim remains U/B until a current Liquid/ZOL-owned datacenter or colocation page is found.
- TelOne Bulawayo and Mazowe capacity values are B unless official TelOne facility pages provide the same fields.
- No Uptime-certified Zimbabwe facility and no hyperscaler Zimbabwe public region were found; re-check annually.

---

## 11. Update Cadence

- Operator pages: quarterly; monthly for Econet EDC, Econet InfraCo, and Dandemutande until project statuses settle.
- Press: Techzim/NewZimbabwe/Bulawayo24/263Chat/Herald weekly; DCD/ITWeb Africa/Developing Telecoms/Connecting Africa/Capacity monthly.
- Directories: quarterly, always reconciled against operator/official pages.
- PeeringDB/PCH/IX-F/ZISPA: quarterly.
- Official trails: monthly eGP/PRAZ and Ministry ICT; quarterly POTRAZ/ZIDA/ZERA/ZETDC; monthly EMA/council for Harare and Bulawayo.
- Cloud region and Uptime certification: annually and on any public claim.
