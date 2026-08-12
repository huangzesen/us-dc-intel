# ER Explorer Official - Eritrea Datacenter Enumeration

Date: 2026-08-12. Country: **ER Eritrea**. Repository division model: **6 regions** from `world-manifest.jsonl`: Anseba; Southern Red Sea; Southern; Gash-Barka; Central; Northern Red Sea.

Administrative caution: search both manifest and local/common names. Central = Maekel/Asmara; Southern = Debub/Mendefera; Northern Red Sea = Semienawi Keyih Bahri/Massawa; Southern Red Sea = Debubawi Keyih Bahri/Assab; Gash-Barka = Gash Barka/Barentu; Anseba = Keren.

Reliability grades:

- **A**: primary or official evidence for the exact fact being recorded. Eritrea A-grade routes include EriTel pages (`https://eritel.com.er`), Ministry of Information/Shabait (`https://shabait.com`), official gazette texts such as Library of Congress/FAO/UNEP records, US State Department Investment Climate Statements, AfDB/ITU/World Bank official data, and primary operator/vendor pages naming the facility/service.
- **B**: reputable industry, development, or press evidence that does not itself operate or regulate the asset. Examples: Submarine Networks, Carnegie, DataReportal, Internet Society Pulse, ICTworks, BuddeComm, East African Review, Developing Telecoms, Connecting Africa, energy/mining press.
- **C**: weak lead only. Examples: directories, forums, social posts, personal blogs, generic satellite marketing pages, aggregator-only listings, unsupported MoUs, and facility inferences from telecom/power/free-zone context.

## 0. Operating Facts

- Eritrea has no public datacenter registry, public planning-permit search, searchable telecom licence register, or public investment-permit database. Treat missing public records as expected, not as proof that no state/enterprise room exists.
- EriTel is the state telecom operator. The official history page says it was restructured in October 2003 to incorporate fixed telephony, mobile telephony, and internet services and that it operates end-to-end fibre core in **Asmara and Massawa**: `https://eritel.com.er/contents.php?id=1029`. Library of Congress hosts **Proclamation No. 134/2003**, which establishes Eritrea Telecommunication Services Corporation (EriTel): `https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-134-2003/eritrean-proc-134-2003.pdf`.
- EriTel is now the only verified official datacenter signal found in public sources. Its official **Private Cloud Services** page says EriTel Nextcloud is hosted in EriTel's datacenters and gives storage/user tiers, 10/5 Mbps committed direct connect in Asmara, 2/2 Mbps from remote cities, 90% uptime, and up to 6-day RTO: `https://eritel.com.er/contents.php?id=1046`. Its official **Email Hosting Services** page says email is hosted locally in EriTel's datacenters and lists Axigen, Barracuda gateway, VM replica, weekly backups, 99% uptime, and direct-connect terms: `https://eritel.com.er/contents.php?id=1045`.
- Do **not** over-locate EriTel datacenters. The official pages confirm EriTel datacenters and hosted services, but do not publish facility names, addresses, coordinates, rack counts, power, redundancy tier, or which city/cities host the platforms. Asmara/Central is the strongest locality inference because EriTel's contact page lists headquarters in Asmara and direct-connect service distinguishes Asmara from "remote cities"; keep the facility location as **Central, Asmara likely / exact site undisclosed** unless a primary source names another site.
- Eritrea has no public submarine cable landing. Submarine Networks says Eritrea is the lone exception among coastal African countries with at least one African subsea cable landing (`https://www.submarinenetworks.com/en/stations/africa`), and Carnegie repeats that Eritrea is the exception among 38 coastal African countries in a 2025 undersea-cable analysis. Do not use Wikipedia/EASSy snippets as evidence for Massawa; some search snippets conflict with stronger cable-station sources.
- Red Sea rerouting stories are future leads only. A June 2024 East African Review article reported that cable companies considered Eritrean waters during Red Sea/Yemen disruption risk, with no named landing commitment and no public cooperation commitment from Asmara: `https://eastafricanreview.com/2024/06/11/red-sea-internet-in-peril-cable-companies-turn-to-eritrea-amid-houthi-threats/`.
- Power evidence is context, not datacenter evidence. EEC is the national utility; Library of Congress hosts **Proclamation No. 142/2004** establishing the Eritrean Electric Corporation: `https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-142-2004/eritrean-proc-142-2004.pdf`. Africa Energy Portal reports about 232 MW installed capacity in 2023 and about 122 MW available capacity with a 54.4% national electricity access estimate: `https://africa-energy-portal.org/aep/country/eritrea`. AfDB's 2025 Desert to Power agreement funds a 12 MW mini-grid project for Teseney, Barentu, and Kerkebet: `https://www.afdb.org/en/news-and-events/press-releases/desert-power-african-development-bank-group-eritrea-sign-agreement-12-mw-mini-grid-project-81778`.
- Free-zone evidence is also context. The Eritrean Free Zones Proclamation No. 115/2001 establishes the Eritrean Free Zones Authority; usable legal-text routes include UNEP LEAP (`https://leap.unep.org/en/countries/er/national-legislation/eritrean-free-zones-proclamation-no-115-2001`) and FAO/FAOLEX PDF (`https://faolex.fao.org/docs/pdf/eri200706.pdf`). Public sources associate free-zone activity with Massawa and Assab, but no public tenant list or datacenter tenant evidence was found.
- Data protection and digital-market context: Data Protection Africa states Eritrea has no data protection legislation (`https://dataprotection.africa/eritrea/`). Internet Society Pulse reports about 27% internet-user penetration and very poor ISP choice (`https://pulse.internetsociety.org/en/reports/er/`). DataReportal Digital 2026 reports 726 thousand internet users at end-2025 and 859 thousand cellular mobile connections in late 2025 (`https://datareportal.com/reports/digital-2026-eritrea`). Use these as market context, not facility proof.
- Search spelling variants: `data center`, `data centre`, `datacentre`, `datacenter`; `Eritrea`, `Eritrean`; `Asmara`, `Asmera`; `Massawa`, `Mitsiwa`; `Assab`, `Aseb`; `Keren`, `Cheren`; `Mendefera`; `Barentu`; `Gash-Barka`, `Gash Barka`; `Maekel`, `Debub`, `Semienawi Keyih Bahri`, `Debubawi Keyih Bahri`; `colocation`, `hosting`, `server room`, `private cloud`, `email hosting`, `Nextcloud`, `gateway`, `earth station`, `VSAT`, `fibre`, `fiber`, `MPLS`, `direct connect`, `racks`, `MW`, `substation`, `free zone`.

## 1. Official Sources

### 1.1 EriTel - Eritrea Telecommunication Services Corporation

Primary URLs:

- Home/about: `https://eritel.com.er/`, `https://eritel.com.er/contents.php?id=1028`
- History/fibre core: `https://eritel.com.er/contents.php?id=1029`
- Internet services and 2021 rollout item: `https://eritel.com.er/contents.php?id=1020`
- Enterprise index: `https://eritel.com.er/contents.php?id=1044`
- SiteConnect MPLS VPN: `https://eritel.com.er/contents.php?id=1032`
- Email hosting: `https://eritel.com.er/contents.php?id=1045`
- Private cloud: `https://eritel.com.er/contents.php?id=1046`

What to extract:

- **A**: EriTel existence, headquarters city (Asmara), service categories, fibre core in Asmara/Massawa, hosted email/private-cloud service being hosted in EriTel datacenters, direct-connect speeds, published SLA/RTO, ADSL rollout towns and dates.
- **B/C**: exact exchange/datacenter address, national gateway details, satellite-earth-station location, or ASN footprint unless confirmed by a primary source. PeeringDB/IP registry evidence for AS30987 is useful interconnection context but not a facility record.

Queries:

```text
site:eritel.com.er "Datacenters" OR "Data Centers" OR "data center" OR "data centre"
site:eritel.com.er "Private Cloud Services" OR Nextcloud
site:eritel.com.er "Email Hosting Services" OR Axigen OR Barracuda
site:eritel.com.er "Direct Connect" "Asmara" "remote cities"
site:eritel.com.er "MPLS" OR "SiteConnect"
site:eritel.com.er "fibre core" OR "Massawa" OR "Asmara"
site:eritel.com.er "Debaruwa" OR "Adi Quala" OR "Segenetti" OR "Nakfa" OR "Serjeka"
"EriTel" "datacenters" Eritrea
"EriTel" "data center" OR "data centre" OR colocation
"AS30987" EriTel PeeringDB OR AFRINIC
```

### 1.2 Ministry of Information / Shabait

Primary URL: `https://shabait.com/`

Shabait is the state Ministry of Information outlet and is the best government-announcement source for telecom, power, ports, and infrastructure. Use it to corroborate EriTel rollouts, power projects, port/free-zone activity, and any future cable or government-cloud announcement. A useful telecom-background article route is: `https://shabait.com/2021/05/05/communications-service-way-forward-from-microwave-to-broadband/`.

Queries:

```text
site:shabait.com "data center" OR "data centre" OR datacenter OR "datacentre"
site:shabait.com EriTel "private cloud" OR "email hosting" OR "server"
site:shabait.com EriTel internet OR broadband OR ADSL OR fibre OR fiber
site:shabait.com "VSAT" OR "satellite" OR "gateway" OR "earth station"
site:shabait.com "free zone" Massawa OR Assab
site:shabait.com "Eritrean Electric Corporation" OR EEC OR "mini-grid" OR "Dekemhare"
```

Grade: **A** for named state announcements; **B** for background articles that do not identify a facility.

### 1.3 Legal, Investment, And Regulatory Checks

- Telecom: LOC Proclamation No. 134/2003 is an A-grade legal route for EriTel establishment: `https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-134-2003/eritrean-proc-134-2003.pdf`.
- Electricity: LOC Proclamation No. 142/2004 is an A-grade EEC route: `https://tile.loc.gov/storage-services/service/ll/lleritrea/eritrean-proc-142-2004/eritrean-proc-142-2004.pdf`.
- Free zones: UNEP LEAP and FAOLEX provide A/B legal-text routes for Proclamation No. 115/2001: `https://leap.unep.org/en/countries/er/national-legislation/eritrean-free-zones-proclamation-no-115-2001`, `https://faolex.fao.org/docs/pdf/eri200706.pdf`.
- Investment climate: US State Department ICS route: `https://www.state.gov/reports/2025-investment-climate-statements/eritrea`. The site can block automated fetches; if blocked, retry with browser/manual access and record access date.
- Investment law: UNCTAD route: `https://investmentpolicy.unctad.org/investment-laws/laws/255/eritrea-investment-proclamation-`.

Queries:

```text
"Proclamation No. 134/2003" Eritrea EriTel
"Proclamation No. 142/2004" "Eritrean Electric Corporation"
"Proclamation No. 115/2001" "Eritrean Free Zones"
"Eritrean Investment Center" "data center" OR ICT OR telecom
site:state.gov/reports/2025-investment-climate-statements/eritrea EriTel OR telecom OR investment
site:investmentpolicy.unctad.org Eritrea investment proclamation ICT telecom
```

Grade only the source's exact fact. A legal proclamation can establish an entity or authority; it does not prove a datacenter unless the datacenter is named.

### 1.4 Power, Ports, Banking, Universities, And Procurement

- Power routes: EEC legal text, Africa Energy Portal, AfDB MapAfrica/project pages, AfDB press releases, Shabait power articles.
- Port/free-zone routes: EFZA legal text, Shabait, Massawa/Assab port news. No public tenant list has been verified.
- Government/banks/universities: National Bank of Eritrea, Commercial Bank of Eritrea, Housing and Commerce Bank of Eritrea, ministries, Eritrea Institute of Technology (Mai Nefhi), and Asmara education/health institutions may have server rooms, but public evidence is generally **C** unless a primary page names a datacenter-scale facility.
- Procurement: no public e-procurement portal was verified. Use broad web search and donor procurement portals for ICT equipment only; ICT tenders are not datacenter evidence without a named site.

Queries:

```text
"Eritrean Electric Corporation" "data center" OR server OR substation OR MW
site:afdb.org Eritrea "mini-grid" OR "Dekemhare" OR "Barentu" OR "Teseney"
"Massawa free zone" Eritrea "data center" OR ICT OR server OR tenant
"Assab free zone" Eritrea "data center" OR ICT OR server OR tenant
"National Bank of Eritrea" "data center" OR "server room" OR "core banking"
"Commercial Bank of Eritrea" "data center" OR "server room" OR "core banking"
"Eritrea Institute of Technology" "data center" OR "server room" OR ICT
Eritrea procurement ICT "server" OR "data center"
```

## 2. Official/Primary Facility Seeds

As of this review, there is **one verified official datacenter-class signal** and no verified commercial third-party colocation campus.

| Facility / operator | Division and locality | Strongest URL | What is verified | Grade guidance |
|---|---|---|---|---|
| EriTel hosted email and private-cloud platform, hosted in EriTel datacenters | **Central, Asmara likely; exact site undisclosed** | `https://eritel.com.er/contents.php?id=1045`, `https://eritel.com.er/contents.php?id=1046`, `https://eritel.com.er/contents.php?id=1044` | EriTel officially sells local email hosting and private-cloud/Nextcloud services hosted in EriTel datacenters; headquarters contact is Asmara; direct-connect terms distinguish Asmara from remote cities. | **A** for hosted service and existence of EriTel datacenters; **C** for exact address/site and any claim that all infrastructure is in Asmara. |
| EriTel fibre core cities | Central (Asmara); Northern Red Sea (Massawa) | `https://eritel.com.er/contents.php?id=1029` | Official history page confirms end-to-end fibre core in Asmara and Massawa. | **A** for fibre-core fact; not a datacenter unless joined to a hosting/datacenter page or facility record. |
| EriTel internet rollout towns | Southern (Debaruwa, Adi Quala, Segenetti); Northern Red Sea (Nakfa); Central (Serjeka/Serejaka) | `https://eritel.com.er/contents.php?id=1020` | Official news item dated 2021-10-01 says internet services were introduced in those towns. | **A** for rollout existence; **C** for server-room/DC inference. |
| EriTel regional telecom nodes | Anseba (Keren); Southern (Mendefera); Gash-Barka (Barentu); Southern Red Sea (Assab) | EriTel service pages; Shabait joins | Nationwide telecom operations imply regional telecom equipment. | **B/C** only; do not enumerate as datacenters. |
| Massawa and Assab free zones | Northern Red Sea (Massawa); Southern Red Sea (Assab) | Proclamation No. 115/2001 legal-text routes; Shabait/free-zone press | EFZA legal framework and free-zone context. | **A/B** for legal/free-zone existence; **C** or negative for datacenter tenant absent source. |
| AfDB 12 MW mini-grids | Gash-Barka (Teseney, Barentu) and Anseba (Kerkebet) | `https://www.afdb.org/en/news-and-events/press-releases/desert-power-african-development-bank-group-eritrea-sign-agreement-12-mw-mini-grid-project-81778` | Donor-backed power access project. | **A** for power project; not datacenter evidence. |

## 3. Hyperscaler And Certification Guardrails

Recheck official pages at every refresh:

```text
site:aws.amazon.com/about-aws/global-infrastructure/regions_az Eritrea
site:learn.microsoft.com/en-us/azure/reliability/regions-list Eritrea
site:cloud.google.com/about/locations Eritrea
site:oracle.com/cloud/public-cloud-regions Eritrea
site:uptimeinstitute.com Eritrea "EriTel" OR "Eritrea"
```

None of AWS, Azure, Google Cloud, Oracle Cloud, or Uptime Institute public-awards routes list an Eritrean region/facility in verified public evidence. EriTel private cloud is a local operator service, not a hyperscaler region. Do not classify GlobalTT/VSAT/Starlink availability pages as datacenters.

## 4. Per-Division Official Strategy

Run all six rows; record negative searches explicitly.

| Manifest division | Priority towns/sites | Official routes | Expected yield and cautions |
|---|---|---|---|
| Central | Asmara, Ghala Nefhi, Serejaka/Serjeka, airport/industrial areas | EriTel HQ, email hosting, private cloud, MPLS/direct connect, Shabait, banks, ministries, EEC | **Low-medium / national hub.** Strongest seed is EriTel datacenters-hosted services. Exact facility is undisclosed; avoid invented address/coordinates. |
| Northern Red Sea | Massawa, Hirgigo, Nakfa, Ghinda, Foro, Afabet | EriTel Massawa fibre core; EriTel Nakfa rollout; Shabait; EFZA; EEC/Hirgigo; cable-station negative checks | **Low.** Fibre/port/free-zone context; no verified cable landing or datacenter tenant. |
| Southern | Mendefera, Debaruwa, Adi Quala, Segenetti, Dekemhare, Adi Keyh, Mai Nefhi/EIT | EriTel rollout towns; EIT; Dekemhare solar/power; Shabait | **Negative/low.** ADSL and campus ICT only unless a primary source names a server-hosting facility. |
| Anseba | Keren, Hamelmalo, Elabered, Kerkebet | EriTel regional service evidence; AfDB Kerkebet mini-grid; Shabait | **Negative.** Telecom and power context only. |
| Gash-Barka | Barentu, Teseney/Tessenei, Agordat, Bisha mine area | EriTel regional service evidence; AfDB Barentu/Teseney mini-grids; mining power/ICT searches | **Negative/low.** Mining enterprise IT is C-level context and not a datacenter without primary disclosure. |
| Southern Red Sea | Assab/Aseb, Beilul, Denkalia plain | EriTel regional service evidence; EFZA Assab; Assab wind/port searches; Shabait | **Negative.** Free-zone and wind/port context only. |

## 5. Per-Division Query Templates

Use the manifest division plus local names and towns. Keep OR groups small enough for search engines to execute.

```text
"{division}" Eritrea "data center"
"{division}" Eritrea "data centre"
"{division}" Eritrea datacenter OR datacentre
"{town}" Eritrea "server room" OR hosting OR colocation
"{town}" Eritrea "private cloud" OR "email hosting" OR Nextcloud
"{town}" Eritrea "VSAT" OR "earth station" OR gateway OR satellite
"{town}" Eritrea "fibre" OR fiber OR ADSL OR broadband OR exchange
"{town}" Eritrea "MW" OR substation OR "free zone" OR port
site:eritel.com.er "{town}" OR "{division}"
site:shabait.com "{town}" internet OR telecom OR electricity OR data
```

High-yield national queries:

```text
"EriTel" "Datacenters" OR "Private Cloud Services" OR "Email Hosting Services"
"Eritel Nextcloud" Eritrea
"EriTel" Axigen Barracuda "VM Replica"
"EriTel" "Direct Connect" Asmara "remote cities"
"EriTel" "fibre core" Asmara Massawa
"Eritrea" "submarine cable landing station" Massawa
"Eritrea" "no submarine cable landing"
"Massawa" Eritrea "landing station" EriTel
"Assab" Eritrea "data center" OR "data centre"
```

Tigrinya secondary queries may help discovery but should not carry a grade without corroboration:

```text
"{town}" "መረጃ ማእከል" OR "ሰርቨር" OR "ኣገልግሎት ኢንተርነት"
site:shabait.com "ሰርቨር" OR "መረጃ"
```

## 6. Extraction Fields

For every candidate, capture:

```text
division; city/town; exact locality or "undisclosed";
operator/SPV legal name; parent/state link; sector (telco/government/enterprise/banking/mining/satellite);
source URL; source date/access date; source grade; exact sourced claim;
lifecycle stage; public service offered; customer class;
floorspace; rack count; storage/users if service tier is the only metric; IT load MW; utility import MVA; voltage; substation/feeder;
power source; backup/generator evidence; fibre/satellite/backhaul evidence; direct-connect terms;
certification/SLA/RTO; caveats; contradictions; negative joins tried.
```

## 7. Confidence Rules

- Upgrade to **A** only for exact facts stated by a primary/official source. EriTel pages support "hosted in EriTel datacenters"; they do not support a street address, MW, racks, Tier III, or a public colocation campus.
- Keep **B** for reputable context such as Submarine Networks/Carnegie no-landing evidence, DataReportal/Pulse market figures, ICTworks connectivity constraints, East African Review future cable-routing discussion, and energy press.
- Keep **C** for directories, aggregators, social posts, generic VSAT offers, and all physical-location inferences not named by a primary source.
- Do not count a fibre core, telecom exchange, ADSL town, MPLS service, free zone, power plant, mine, university ICT room, or port system as a datacenter without a source naming a hosting/datacenter/server-room facility.
- Do not convert cable-routing interest into a cable landing station. Do not convert EriTel private cloud into a hyperscaler cloud region.
- Expected national yield is **one A-grade operator/service seed with undisclosed facility details**, plus mostly negative regional records. It is acceptable and preferred to mark divisions as `no_projects: true` rather than pad with telecom/power context.
- Re-verify quarterly: EriTel email/private-cloud/enterprise pages, Shabait telecom/power announcements, Submarine Networks/cable news, Starlink/LEO licensing, EEC/AfDB power additions, EFZA tenant evidence, hyperscaler region pages, and data-protection/telecom legislation.
