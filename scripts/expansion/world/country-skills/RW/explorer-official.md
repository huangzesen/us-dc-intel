# RW Explorer Official - Rwanda Datacenter Enumeration

Date verified: 2026-08-12. Country: **RW - Rwanda**. Angle: official/regulatory/government sources for identifying datacenter facilities, telco core rooms, government hosting infrastructure, planned national data infrastructure, and regulatory/licensing signals.

Reliability grades:
- **A** = official or primary source: RURA licences/statistics/decrees, MINICT/RISA/NCSA/NDPB documents and tenders, RPPA (UMUCYO) e-procurement notices, RDB investment materials, government-owned operator pages, official cloud-region lists, verified primary news from government channels.
- **B** = strong secondary: established trade press (Data Centre Dynamics, Connecting Africa, Agence Ecofin, The Stack, Datacentre Magazine), The New Times/IGIHE/KT Press quoting official material, PeeringDB for interconnection metadata, Internet Society IXP tracker, World Bank/UNECA project documents.
- **C** = lead only: aggregator listings (DataCenterMap, datacenters.com, datacenterplanet, Baxtel, Inflect), vendor marketing without a named site, old MoUs, LinkedIn/social posts, unsourced blogs.
- **U** = unverified: anything seen only in aggregators or single weak sources; re-check before grading up.

Rule: an entry's grade covers only the fact actually supported. A verified MoU (B) does not make the facility operational; a verified service page (A) does not prove a physical site address.

---

## 0. Structure Facts

### 0.1 Administrative divisions (world-manifest model)

Rwanda's subnational model in `world-manifest.jsonl` is **city/province** with exactly 5 divisions: **City of Kigali, Eastern, Northern, Western, Southern**. This matches the official structure of Kigali City plus 4 provinces. District names are the natural second layer for searches and address resolution:

| Division | Districts (akarere) | Notes |
|---|---|---|
| City of Kigali | Gasabo, Kicukiro, Nyarugenge | The only commercial/telecom cluster; Kacyiru (Gasabo) hosts Telecom House, RINEX, NCSA, TrAC |
| Eastern | Bugesera, Gatsibo, Kayonza, Kirehe, Ngoma, Nyagatare, Rwamagana | Hosts Rwanda Space Agency teleport at Mwulire (Rwamagana); Bugesera International Airport under construction; Tanzania-border fibre corridor |
| Northern | Burera, Gakenke, Gicumbi, Musanze, Rulindo | Musanze/Rubavu tourism corridor; low datacenter yield |
| Western | Karongi, Ngororero, Nyabihu, Nyamasheke, Rubavu, Rusizi, Rutsiro | Lake Kivu methane-gas power plants (energy context); Goma/Rubavu border; low datacenter yield |
| Southern | Gisagara, Huye, Kamonyi, Muhanga, Nyamagabe, Nyanza, Nyaruguru, Ruhango | Huye (UR campus) and Kamonyi (MTN 5G expansion sites per IGIHE); otherwise low yield |

Kinyarwanda names for search recall: Umujyi wa Kigali; Intara y'Iburasirazuba (Eastern); Intara y'Amajyaruguru (Northern); Intara y'Iburengerazuba (Western); Intara y'Amajyepfo (Southern). Administrative verification: official government local-government directory https://www.gov.rw/government/directory/local-government and City of Kigali overview https://www.kigalicity.gov.rw/about/overview ; NISR census/maps portal https://statistics.gov.rw/node

### 0.2 Registries: what exists and what does not

- **No public national datacenter registry.** No single government page lists operating or planned datacenters.
- **No reliable online construction-permit search.** City of Kigali and districts publish planning material, but no consolidated national construction/EIA permit database is reliably machine-searchable for datacenter projects. REMA (Rwanda Environment Management Authority) is the environmental authority: https://rema.gov.rw/
- The closest thing to a census is the combination of: RURA ICT market statistics and licensing, RPPA UMUCYO e-procurement notices, RDB investment announcements, and RISA project pages.
- **Cloud-region official lists are negative evidence** for hyperscale facilities (see section 3).

### 0.3 Legal and regulatory basis

- RURA: Law N 09/2013 of 08/04/2013 establishing the Rwanda Utilities Regulatory Authority; mission, powers, organisation: https://rwandalii.org/akn/rw/act/law/2013/9/eng@2013-04-08 ; ICT sector overview: https://www.rura.rw/sectors/ict/overview
- ICT sector policy leadership: Ministry of ICT and Innovation (MINICT), https://www.minict.gov.rw/ and https://www.minict.gov.rw/about
- Implementation agency: Rwanda Information Society Authority (RISA), established 2017, coordinates Smart Rwanda Master Plan and digital infrastructure: https://www.risa.gov.rw/ and https://www.risa.gov.rw/about/overview
- Cybersecurity / data protection supervision: National Cyber Security Authority (NCSA), established 2017, operational 2020; site is https://cyber.gov.rw/ (NOT ncsa.gov.rw); address: Telecom House, 5th Floor, 8 KG 7 St, Kacyiru, Kigali: https://cyber.gov.rw/contact-us/ ; National Cybersecurity Strategy 2024-2029 lead: https://dig.watch/resource/national-cybersecurity-strategy-of-the-republic-of-rwanda-2024-2029
- Data protection: Law No 058/2021 of 13/10/2021 relating to the protection of personal data and privacy, gazetted 15/10/2021: https://rwandalii.org/akn/rw/act/law/2021/58/eng@2021-10-15 ; RISA summary page: https://www.risa.gov.rw/data-protection-and-privacy-law ; Data Protection and Privacy Office: https://dpo.gov.rw/ ; NCSA launch notice for the Data Protection Office: https://cyber.gov.rw/updates/article/ncsa-officially-launches-its-data-protection-office/ . Treat the law as regulatory/demand context, not facility evidence. Rwanda does not have a blanket localization rule for all data; some public-sector or sensitive personal-data handling may require local hosting/certification depending on circumstance.
- Digital economy programs: Smart Rwanda Master Plan; Rwanda Digital Acceleration Project (RDAP, USD 200M, World Bank + AIIB, launched 2022, 5 years, implemented via RISA) - RISA site: https://www.risa.gov.rw/ ; RISA National Data Sharing Policy notice: https://www.risa.gov.rw/news-detail/national-data-sharing-policy-approved ; RDAP context incl. USD 100M biometric authentication (AMBAS) tender coverage: https://idtechwire.com/rwanda-launches-100m-tender-for-national-biometric-authentication-system/ and https://www.biometricupdate.com/202504/rwanda-seeks-supplier-for-automated-multimodal-biometric-authentication-system ; World Bank project detail page: https://projects.worldbank.org/en/projects-operations/project-detail/P175437
- Market structure: use RURA ICT statistics for current counts and shares; secondary overviews can seed searches but should not override RURA. Rwanda is a landlocked market with MTN Rwanda and Airtel Rwanda as the mobile operators, a national fibre backbone, and MTN 5G launched in Kigali in June 2025 per local press.

---

## 1. Search Vocabulary

Rwanda is trilingual (Kinyarwanda, English, French). English and French give the best recall; Kinyarwanda is low yield but useful for district-level government posts.

English: data center, data centre, datacenter, server farm, colocation, hosting, cloud, digital infrastructure, internet exchange point, IXP, submarine cable, fibre, point of presence, tier III, rack space, disaster recovery, sovereign cloud.
French: centre de donnees, centre de traitement de donnees, datacenter, centre d'hebergement, hebergement web, hebergement de serveurs, colocation, cloud, infrastructure numerique, point de presence, fibre optique, salle des serveurs, serveurs, appel d'offres, mise en service, inauguration, centre informatique.
Kinyarwanda (low yield, verify any hits): ikigo cy'imyirondoro (data centre), ububiko bw'amakuru (data storage), itsinda rya serveurs (server room), ikoranabuhanga (ICT), umuyoboro wa fibre optique (fibre).

Lifecycle verbs to capture in French/English sources: projet / etude / MoU (intent), appel d'offres / AMI / tender / awarded (procurement), construction / travaux / breaking ground (under construction), mise en service / operationnel / inaugurated / go-live (operational).

---

## 2. Official And Regulatory Pipeline

### 2.1 RURA - Rwanda Utilities Regulatory Authority (telecom/ICT regulator)

RURA is the licence census and market-statistics source, not a facility registry. A telecom licence alone is NOT a datacenter facility.

- Site: https://www.rura.rw/ ; ICT sector overview: https://www.rura.rw/sectors/ict/overview
- ICT statistics reports (subscribers, ISPs, market structure): Q2 2025 report PDF: https://www.rura.rw/index.php?eID=dumpFile&t=f&f=147480&token=f5d6725743614952f9dde682f06c2369ea137f0c ; mobile subscriptions Sep 2024: https://www.rura.rw/index.php?eID=dumpFile&t=f&f=121592&token=db85c1a4a710b1c024f53931326e883347a2c092
- Energy regulation (RURA also regulates electricity tariffs): https://www.rura.rw/sectors/energy/sub-sectors-and-services/electricity
- Licenced ISP structure (2025): 2 MNOs, 4 ISPs, 1 wholesaler network service provider, 2 network facility providers, 23 retail ISPs (per RURA Q2 2025 report as summarised in Wikipedia). Use RURA lists to seed operator and hosting-provider discovery.
- RURA set up RINEX (Rwanda Internet Exchange) in 2009; ISPs can connect via RINEX; ~15 members late 2025: https://pulse.internetsociety.org/en/ixp-tracker/country/RW/ (Internet Society Pulse IXP tracker).

Queries:
```text
site:rura.rw licence internet OR operator OR "service provider" Rwanda
site:rura.rw statistiques OR statistics OR observatoire ICT Rwanda
site:rura.rw "centre de donnees" OR "data center" OR hebergement OR cloud
site:rura.rw RINEX OR "internet exchange"
site:rura.rw decision OR sanction OR compliance MTN OR Airtel OR licence
"RURA" Rwanda "data center" OR "centre de donnees" OR colocation
```

Regulator-adjacent facts worth keeping: in 2017 RURA fined MTN Rwanda ~USD 8.5M for running IT services outside the country in breach of licence (CNBC Africa: https://www.cnbcafrica.com/2017/rwanda-utilities-regulatory-authority-fines-mtn-us-85m-non-compliance/ ). This is historical evidence that (a) operators have kept core/IT hosting offshore in the past and (b) RURA enforces in-country obligations - useful context when grading telco 'core in Kigali' claims.

### 2.2 MINICT, RISA, NCSA - policy, implementation, cybersecurity

Primary route (all live as of 2026-08):
- MINICT: https://www.minict.gov.rw/ ; about page https://www.minict.gov.rw/about ; Smart Rwanda / Connect Rwanda 2.0 digital-infrastructure status page: https://www.minict.gov.rw/news-detail/what-you-should-know-about-connect-rwanda-campaign
- RISA: https://www.risa.gov.rw/ ; overview https://www.risa.gov.rw/about/overview ; projects incl. RDAP and digital certificate programmes (homepage); data-protection-law page https://www.risa.gov.rw/data-protection-and-privacy-law ; RISA is the implementing agency for government ICT infrastructure and the Smart Rwanda Master Plan (per Wikipedia overview and RISA About).
- NCSA: https://cyber.gov.rw/ ; about https://cyber.gov.rw/about/ ; Rw-CSIRT incident response; contact (Telecom House 5th floor): https://cyber.gov.rw/contact-us/

Verified signals:
- RISA is active and publishes national digital-government/data notices from https://www.risa.gov.rw/ ; keep RISA as the canonical agency source instead of social mirrors.
- RDAP (USD 200M, World Bank + AIIB, launched 2022, ~5-year) is a RISA-implemented project; it includes digital ID/biometric (AMBAS) procurement and digital-infrastructure components; use the World Bank project page plus UMUCYO/RPPA for tenders.
- Government e-services run through IremboGov: https://irembo.gov.rw/ (portal) and Irembo Ltd: https://irembo.com/ . IremboGov is evidence of government platform operation, NOT of a specific datacenter; hosting location remains unverified unless a tender, operator page, or government statement names the facility.

Queries:
```text
site:minict.gov.rw "data centre" OR "data center" OR "centre de donnees" OR hosting OR infrastructure
site:minict.gov.rw RDAP OR "digital acceleration" OR "Smart Rwanda"
site:risa.gov.rw RDAP OR "data centre" OR hosting OR infrastructure OR tenders
site:risa.gov.rw "appel d'offres" OR procurement OR AMBAS OR "digital ID"
site:cyber.gov.rw "data centre" OR "data center" OR hosting OR critical infrastructure
site:cyber.gov.rw standards OR directives OR "critical information infrastructure"
"RDAP" Rwanda tender "data center" OR hosting OR serveurs
"Irembo" hosting OR "data centre" OR cloud OR infrastructure Rwanda
```

### 2.3 RPPA UMUCYO - e-procurement (tenders)

RPPA (Rwanda Public Procurement Authority) runs UMUCYO, the national e-procurement system. All government ICT/digital tenders flow through it or through ministry portals.

- RPPA: https://www.rppa.gov.rw/ (homepage states UMUCYO is the e-procurement system for Rwanda)
- UMUCYO portal: https://www.umucyo.gov.rw/ . RPPA's e-procurement page links directly to this portal: https://www.rppa.gov.rw/e-procurement . Do not use `umuganda.rdb.rw`; that is not the official e-procurement route for this task.
- Trade.gov guidance on selling to the Rwandan public sector: https://www.trade.gov/country-commercial-guides/rwanda-selling-public-sector
- OCDS open-contracting data publication for RPPA: https://data.open-contracting.org/en/publication/145

Queries:
```text
site:rppa.gov.rw tender OR "avis d'appel d'offres" OR UMUCYO ICT OR "data center"
"UMUCYO" Rwanda tender "data centre" OR "data center" OR serveurs OR hebergement OR cloud
"RPPA" Rwanda "centre de donnees" OR hosting OR fibre OR digital
"Rwanda" "appel d'offres" "data center" OR "centre de donnees" OR "hebergement des donnees"
```

### 2.4 RDB - investment promotion, KIC, special economic zones

- RDB: https://rdb.rw/ ; e-services: https://rdb.rw/e-services/ ; Kigali Innovation City ground-breaking announcement (GoR + Africa50 + BADEA, 60 ha): https://rdb.rw/the-government-of-rwanda-africa50-and-badea-break-ground-on-the-construction-of-kigali-innovation-city/ ; KIC funding for basic infrastructure: https://www.minecofin.gov.rw/news-detail/kigali-innovation-city-project-secures-us-20-million-to-finance-basic-infrastructure
- KIC official/project sources: RDB ground-breaking notice above; Africa50 project page https://www.africa50.com/our-funds/projects/kigali-innovation-city/ ; MINECOFIN financing notice https://www.minecofin.gov.rw/news-detail/kigali-innovation-city-project-secures-us-20-million-to-finance-basic-infrastructure . KIC is the designated innovation estate where a PAIX data centre is reported by aggregators (see section 4); that does not prove PAIX is operational.
- RDB is also the one-stop shop for business/investor licences and incentives; datacenter developers (Raxio, ADC, Otech, PAIX) would interact with RDB for investment status.

Queries:
```text
site:rdb.rw "data centre" OR "data center" OR KIC OR "innovation city" OR SEZ
site:rdb.rw investment "digital infrastructure" OR "data centre" OR cloud
"Kigali Innovation City" data centre OR datacenter OR "data center"
"Kigali Special Economic Zone" OR "special economic zone" Rwanda "data center"
```

### 2.5 Energy, planning, and environmental evidence

Use for power-feasibility and permitting corroboration of any serious facility claim.

- Rwanda Energy Group (REG) Ltd, government holding (established July 2014) with subsidiaries EUCL and EDCL): official site https://www.reg.rw/ ; RURA electricity page describes REG structure: https://www.rura.rw/sectors/energy/sub-sectors-and-services/electricity
- Grid context: national electricity access reached 84.6% by end-July 2025 (59.6% grid + ~25% off-grid) per REG reporting: https://africasustainabilitymatters.com/rwanda-weighs-net-metering-policy-to-unlock-household-solar-power-and-accelerate-universal-electricity-access/ ; generation mix includes hydro (incl. Rusumo, Nyabarongo), Lake Kivu methane gas, peat, solar, and imports (regional power pools). Grid reliability in Kigali is better than the regional norm but diesel/genset backup is standard for any DC claim; cross-check large power claims against REG/EUCL connection or substation evidence.
- Trade.gov Rwanda energy overview: https://www.trade.gov/country-commercial-guides/rwanda-energy
- REMA (Rwanda Environment Management Authority) for environmental authority context: https://rema.gov.rw/
- Ministry of Infrastructure (MININFRA) urban/ICT-adjacent projects (e.g., Rwanda Urban Development Project): https://www.mininfra.gov.rw/updates/news-details/transforming-lives-and-connecting-communities-celebrating-the-success-of-rwandas-urban-development-project
- City of Kigali: https://www.kigalicity.gov.rw/ ; use it for administrative/location context, but do not assume permit-search completeness.

Queries:
```text
site:reg.rw ("data centre" OR "data center" OR serveurs OR "grand client")
site:eucl.rw ("data centre" OR "data center" OR serveurs OR "grand client")
site:rura.rw electricity OR tarif OR licence OR interconnection Rwanda
site:rema.gov.rw EIA OR EIES "centre de donnees" OR telecom OR fibre OR substation
site:kigalicity.gov.rw construction OR permit OR development OR telecom [verify domain]
"REG" OR "EUCL" Rwanda "data center" OR "centre de donnees" OR "critical power"
"Rwanda" "etude d'impact" "centre de donnees" OR "data center" OR telecom
```

---

## 3. Cloud, Edge, And Interconnection Signals (negative evidence where applicable)

| Signal | Source | Rwanda interpretation |
|---|---|---|
| AWS regions | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | No Rwanda region. Africa regions (Cape Town, Johannesburg) are outside Rwanda; negative evidence for local hyperscale. |
| Azure regions | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No Rwanda region. South Africa North/West are outside Rwanda. |
| Google Cloud locations | https://cloud.google.com/about/locations | No Rwanda region. Johannesburg is the nearest region. |
| Oracle OCI regions | https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | No Rwanda region; Johannesburg and other Africa/Middle East regions outside Rwanda. |
| RINEX / RIXP | Set up by RURA 2009: https://pulse.internetsociety.org/en/ixp-tracker/country/RW/ ; AS329521 'Rwanda Internet Exchange Point (RINEX) c/o RICTA', Telecom House, KG 7, Kacyiru, Gasabo, Kigali: https://whois.ipip.net/AS329521 | Operating IXP in Kigali (Telecom House). Interconnection infrastructure, NOT datacenter capacity by itself; can be a colocation-adjacent lead. |
| .rw registry / RICTA | RICTA manages .rw and RINEX: http://www.ricta.org.rw/ | Registry infrastructure; Kigali-based; C/B for facility claims unless hosting site proven. |
| International connectivity | Landlocked; terrestrial fibre to EASSy, TEAMS, SEACOM via Kenya and Tanzania: https://en.wikipedia.org/wiki/Telecommunications_in_Rwanda ; ISOC 2024 East Africa cable outage report includes Rwanda/Tanzania/DRC dependency: https://www.internetsociety.org/resources/doc/2024/2024-east-africa-submarine-cable-outage-report/ ; UN Africa Renewal 'Big dreams for Rwanda's ICT sector': https://africarenewal-un-org.nproxy.org/en/magazine/big-dreams-rwandas-ict-sector | No submarine landing in Rwanda. International PoPs in Kigali are connectivity context; do not count as DC. |
| Starlink | Operating in Rwanda since Feb 2023: https://www.cnbcafrica.com/media/6320977012112/rwanda-launches-starlink-satellite-internet | Connectivity, not a facility. Gateway/ground-station claims need SpaceX/RURA confirmation. |
| Rwanda Space Agency ground segment | Teleport/ground station at Mwulire, Rwamagana District (Eastern Province); commercial antenna activated July 2025 (COSMIC-2/NOAA): https://www.satellitetoday.com/technology/2025/07/16/atlas-space-operations-adds-to-ground-network-with-rwanda-antenna/ ; RSA: https://space.gov.rw/ ; brochure: https://space.gov.rw/Rwanda_Space_Agency_Brochure.pdf | Operational satellite ground station in Eastern Province; an edge/telecom facility record, not a commercial datacenter. |

Data-localization context: Law No 058/2021 restricts transfer of personal data outside Rwanda (authorisation required) - rwandalii link in 0.3. This increases the strategic value of in-country hosting but must not be recorded as a facility.

---

## 4. Facility And Project Seed List (evidence status as of 2026-08)

| Candidate | Status | Grade | Location handling | Why it matters / evidence |
|---|---|---|---|---|
| TrAC Kigali Data Centre (TransAfrica Communications) | Operating marketed colocation/hosting service | A for service marketing (trac.africa), C for physical facility details; U for Uptime Tier III certification | Telecom House, 8 KG 7 Ave, Kacyiru, Gasabo, Kigali | Operator site markets cloud and tier 3 data centre hosting: https://trac.africa/ ; aggregator listing gives Telecom House address: https://www.datacentermap.com/rwanda/kigali/trac-kigali/ ; PeeringDB org: https://www.peeringdb.com/org/29956 . No independent Uptime certification, rack count, MW, or MEP detail found in this pass. |
| PAIX Kigali (PAIX Data Centres) | Listed, status unverified | C aggregator; U for operational status | Within Kigali Innovation City (Gasabo), exact site not public | 3 MW carrier-neutral listing: https://www.datacentermap.com/rwanda/kigali/paix-kigali/ and https://www.datacenters.com/paix-paix-kigali ; PAIX official homepage/contact and Africa50 profile emphasize existing Ghana/Kenya assets rather than Rwanda: https://www.paix.io/ , https://www.paix.io/contact-us , https://www.africa50.com/our-funds/projects/paix-data-centers/ . Keep as lead until PAIX, RDB, RURA, KIC, or trade press confirms construction/go-live. |
| AOS LTD Kigali | Listed colocation | C aggregator | Kigali Business Centre, KN 5 Rd, Kigali | Local IT-service provider colocation listing, not carrier neutral, last updated 2023-06-22: https://www.datacentermap.com/rwanda/kigali/aos/ ; DCD names AOS as one of three existing Kigali operators in its 2026 Rwanda article: https://www.datacenterdynamics.com/en/news/omantels-otech-signs-mou-to-build-data-center-in-rwanda/ . Keep as C until AOS/operator evidence confirms current services. |
| Raxio RW1 Kigali | Aggregator-only; status unverified | U/C | Gasabo District, Kigali (per aggregator) | Listed as 'Raxio RW1 - Rwanda's first carrier-neutral Tier III-designed data centre': https://datacenterplanet.com/listings/raxio-rw1-kigali-rwanda . Raxio's official data-centres page lists Angola, Cote d'Ivoire, DRC, Ethiopia, Mozambique, Tanzania, and Uganda - NOT Rwanda: https://www.raxiogroup.com/data-centres/ . Treat RW1 as unconfirmed until Raxio/RURA/primary press confirms. |
| Africa Data Centres (ADC) Kigali | Announced 2022; status unclear | B for announcement; U for current status | Kigali; precise location never disclosed | DCD 2022-11-28: 2 MW purpose-built facility, ground break Q1 2023: https://www.datacenterdynamics.com/en/news/africa-data-centres-to-build-first-data-center-in-kigali-rwanda/ ; Cassava Technologies release: https://www.cassavatechnologies.com/africa-data-centres-to-build-its-first-data-centre-in-kigali/ ; DCD 2026-06 states project status unclear: https://www.datacenterdynamics.com/en/news/omantels-otech-signs-mou-to-build-data-center-in-rwanda/ ; aggregator listing: https://inflect.com/building/kigali-kigali/africa-data-centres/datacenter/kigali . Verify: ADC Rwanda page or construction evidence. |
| Otech (Omantel) x Broadband Systems Corporation DC | MoU announced 2026-06-03 | B for MoU; U for site/construction | Rwanda (location not disclosed) | AI-ready, Tier III-standards, co-investment MoU: https://www.datacenterdynamics.com/en/news/omantels-otech-signs-mou-to-build-data-center-in-rwanda/ ; BSC is described there as a Kigali ISP. Requires follow-up tender/construction/inauguration evidence. |
| MTN Rwanda core / 5G | Operational network; core rooms are telco leads | B for network; C for DC claim | Kigali (MTN Centre); 5G rollout Kigali + Kamonyi (Southern) | MTN Centre Kigali facility on PeeringDB: https://www.peeringdb.com/fac/11839 ; 5G launch June 2025 (IGIHE): https://en.igihe.com/business-62/article/mtn-rwanda-launches-5g-network ; MTN case study (solar, MTN Rwanda): https://www.mtn.com/case-study/partnerships-for-the-planet-clean-energy-solutions-mtn-rwanda/ . Count as datacenter only if source names hosting/cloud/core infrastructure. |
| Airtel Rwanda | Operational MNO | B for operator; C for DC | Kigali HQ | 4G launch/operators: https://www.ecofinagency.com/telecom/2607-44768-rwanda-airtel-and-mtn-launch-4g-networks ; no public DC claim verified. |
| Liquid Intelligent Technologies Rwanda | Fibre/ISP operation (ex-Rwandatel assets, 2013); cloud services marketed | B for fibre presence; U for local DC | Kigali office; national backbone | New Times: 'Liquid Intelligent Technologies at the forefront of Africa's data sovereignty' (AFPIF 2022 Kigali): https://www.newtimes.co.rw/article/561/news/featured/liquid-intelligent-technologies-at-the-forefront-of-africas-data-sovereignty ; Liquid acquired Rwandatel assets 2013: https://www.newtimes.co.rw/article/93378/National/liquid-telecom-acquires-rwandatel-assets . No verified Liquid-owned colocation DC in Rwanda as of 2026-08. |
| RINEX / RICTA registry | Operational IXP/registry | B | Telecom House, Kacyiru, Kigali | Section 3 sources. Interconnection, not DC. |
| RISA government hosting / IremboGov | Operational platform; hosting location unverified | A for platform; U for facility | Kigali (presumed); verify | https://irembo.gov.rw/ ; https://www.risa.gov.rw/ . Do not convert platform operation into a facility record. |
| Rwanda Space Agency teleport (Mwulire) | Operational ground station | B | Rwamagana District, Eastern Province | https://www.satellitetoday.com/technology/2025/07/16/atlas-space-operations-adds-to-ground-network-with-rwanda-antenna/ ; edge/telecom facility. |
| Broadband Systems Corporation (BSC) | Operational ISP | B | Kigali | MoU partner for Otech DC; nationwide fibre: DCD article above. |
| Paratus Rwanda | Connectivity presence; DC listing unverified | B for Rwanda fibre presence; C/U for DC listing | Kigali route/PoP, facility unknown | Aggregator listing 'Paratus Rwanda Data Centre Kigali': https://datacenterplanet.com/listings/paratus-rwanda-data-centre-kigali . Paratus official 2026 Goma-Mombasa route announcement says the protected route runs via Kigali and that Paratus Rwanda is licensed, while its data-centre menu lists Angola/Namibia/Zambia rather than Rwanda: https://paratus.africa/blog/paratus-lights-up-new-east-africa-fiber-highway-linking-goma-to-mombasa/ . Treat as connectivity/PoP lead, not a confirmed DC. |
| Starlink Rwanda | Operational since Feb 2023 | B for service | n/a | Connectivity only: https://www.cnbcafrica.com/media/6320977012112/rwanda-launches-starlink-satellite-internet |

---

## 5. Per-Division Enumeration Approach (realistic expectations)

Run every enumeration cycle across all 5 divisions; record negatives as `no_projects: true` where a division genuinely has no activity. Expect a heavily Kigali-centred market with a handful of planned projects and mostly negative yields in the four provinces.

1. **City of Kigali** (Gasabo, Kicukiro, Nyarugenge): the ONLY credible cluster. All currently identified candidates sit here: Telecom House (Kacyiru/Gasabo) hosts TrAC, RINEX, NCSA; PAIX Kigali is listed within Kigali Innovation City (Gasabo); MTN Centre and Airtel HQ are in Kigali; ADC/Otech/Raxio-RW1/Paratus targets are all Kigali-pending or Rwanda-pending. Expected yield: facility-level records/leads (TrAC, PAIX, AOS, ADC-pending, Otech-pending, MTN core) plus IXP and government-hosting context.
2. **Eastern Province**: one verified edge/telecom asset - Rwanda Space Agency teleport at Mwulire, Rwamagana District (operational 2025). Search Bugesera (new international airport, digital infrastructure), Rwamagana (teleport, UR campus), Nyagatare (agriculture/energy), Kayonza/Kirehe (Tanzania border fibre corridor). Expect mostly negative commercial searches.
3. **Northern Province**: search Musanze, Gicumbi, Rulindo for university labs, tourism-tech, and backbone PoPs. Expect negative for commercial datacenters.
4. **Western Province**: search Rubavu (Gisenyi, DRC border), Rusizi (Goma crossing), Karongi, Nyamasheke for fibre/backbone and Lake Kivu methane-gas power (energy context only). Expect negative for commercial datacenters.
5. **Southern Province**: search Huye (University of Rwanda), Nyanza, Muhanga, Kamonyi (MTN 5G expansion sites per IGIHE), Ruhango for university computing rooms and telecom edge. Expect negative for commercial datacenters.

Copy/paste query block (official angle; keep each domain-restricted query separate because search engines often mishandle multiple `site:` operators in one line):
```text
"Kigali" ("data centre" OR "data center" OR colocation OR hebergement OR RINEX OR "Tier III")
site:rura.rw ("data centre" OR "data center" OR hosting OR colocation)
site:minict.gov.rw ("data centre" OR "data center" OR hosting OR colocation)
site:risa.gov.rw ("data centre" OR "data center" OR hosting OR colocation)
site:cyber.gov.rw ("data centre" OR "data center" OR hosting OR colocation)
site:rdb.rw ("data centre" OR "data center" OR hosting OR colocation)
site:rppa.gov.rw ("data centre" OR "data center" OR hosting OR colocation)
site:umucyo.gov.rw ("data centre" OR "data center" OR hosting OR colocation OR servers OR cloud)
"Gasabo" OR Kacyiru OR "Telecom House" Rwanda ("data centre" OR "data center" OR serveurs OR colocation)
"Kigali Innovation City" data centre OR datacenter
"Rwamagana" OR Mwulire Rwanda (teleport OR ground station OR satellite OR "data centre")
"Bugesera" Rwanda ("data centre" OR "data center" OR airport OR digital OR fibre)
"Musanze" OR "Rubavu" OR "Huye" OR "Kamonyi" Rwanda ("data centre" OR "data center" OR serveurs OR fibre OR "point de presence")
"Eastern Province" OR "Northern Province" OR "Western Province" OR "Southern Province" Rwanda ("data centre" OR "data center")
```

---

## 6. Counting, Grading, And De-Dup Rules (official angle)

- A facility exists only when a source names infrastructure AND location with enough specificity to distinguish a physical site. A marketed hosting/cloud service without a named site is a provider-level service lead (keep separate).
- Keep `facility_type` precise: `commercial_colocation`, `telco_core`, `ixp`, `government_hosting`, `planned_commercial_dc`, `edge_ground_station`, `registry_infrastructure`, `lead_only`.
- Keep status precise: `operational`, `marketed_service`, `announced`, `mou`, `procurement`, `under_construction`, `unknown`, `negative`.
- ADC Kigali and Otech/BSC remain `announced/mou` until an official tender, construction notice, EIA, or inauguration names a site. Do not promote on the strength of the 2022/2026 announcements alone.
- Raxio RW1 and Paratus Rwanda: aggregator-only. Keep as `lead_only`/U until Raxio/Paratus/RURA/primary press confirm.
- TrAC 'only tier 3' is a marketing claim (A for the claim's existence on their site); Tier III certification, rack count, MW and address-level power need independent confirmation.
- MTN/Airtel network rollouts and 5G sites are NOT datacenters. Count cores only with hosting/cloud/DC evidence (PeeringDB facility entry is interconnection metadata, grade B/C).
- RINEX/IXP and the Mwulire ground station are interconnection/edge facilities - record separately, never as commercial datacenter capacity.
- Capacity fields (MW/racks) stay null unless stated by an official/operator/tender source. PAIX 3 MW and ADC 2 MW come from listings/announcements - cite as such.
- De-dup: if TrAC, RINEX, and NCSA all sit in Telecom House, that is ONE building with separate operators - record per operator, do not merge.
- Negative searches: ICT offices, cybercafes, computer labs, NGO server rooms, GIS rooms, and software platforms do not count unless the source describes hosting/colo/compute infrastructure with a named operator and location.

---

## 7. Source Priority Checklist (official angle)

1. RURA licences, ICT statistics, decisions, and RINEX records.
2. MINICT policy (Smart Rwanda, Connect Rwanda, National AI/digital strategies) and MINECOFIN budget documents.
3. RISA project pages and RDAP procurement (digital ID, biometrics, digital infrastructure components).
4. NCSA directives, standards, and Rw-CSIRT incident reporting; NDPB/DPO data-protection determinations.
5. RPPA UMUCYO e-procurement notices and award decisions.
6. RDB investment announcements (KIC, SEZ, datacenter developers) and US Trade.gov country guides.
7. REG/EUCL/EDCL and RURA energy evidence; REMA EIA records; City of Kigali permits.
8. World Bank project documents (RDAP; energy/connectivity programs), UNECA digital-trade profile: https://www.uneca.org/sites/default/files/ATPC/cp/Digital%20trade%20regulatory%20integration%20-%20Country%20profile%20-%20Rwanda-%20ENG.pdf , and D4D Hub Rwanda Data Center Market Brief: https://cms.d4dhub.eu/assets/Initiatives/Data-Governance-in-Africa/Digital-Investment-Facility/2507_Country-Market-Briefs/Data-Center-Market-Brief-Rwanda.pdf
9. Operator official pages (MTN, Airtel, Liquid, BSC, TrAC) and their tenders.
10. Internet Society/PeeringDB for IXP and interconnection metadata.
11. Trade press (DCD, Connecting Africa, Agence Ecofin, The Stack, Datacentre Magazine) as B-grade corroboration.
12. Aggregators (DataCenterMap, datacenters.com, datacenterplanet, Baxtel, Inflect) as C/U discovery only.

---

## 8. Update / Re-Check Cadence

- **Quarterly**: RURA ICT statistics and licensing pages; RPPA UMUCYO tender scan for 'data centre', 'hosting', 'serveurs', 'cloud'.
- **Quarterly**: re-check ADC Kigali, Otech/BSC, PAIX Kigali, Raxio RW1, Paratus Rwanda status on operator sites and DCD Africa tag (https://www.datacenterdynamics.com/en/tags/rwanda/).
- **Semi-annual**: MINICT/RISA/NCSA policy and project pages (RDAP milestones, cybersecurity strategy actions, data-protection rules); REG grid/energy reports for power-feasibility changes.
- **Annual**: re-verify all U-grade aggregator listings (TrAC Tier III claim, PAIX 3 MW, AOS, Raxio RW1, Paratus); confirm Uptime Institute certification status for Rwanda (none verified as of 2026-08) at https://uptimeinstitute.com/ .
- **Event-driven**: any announcement of a Rwanda cloud region (AWS/Azure/GCP/OCI) would be the single biggest change; watch official region pages (section 3).

## 9. Verified Source Anchors (as of 2026-08)

- gov.rw portal: https://www.gov.rw/
- RURA: https://www.rura.rw/ ; ICT overview https://www.rura.rw/sectors/ict/overview ; Q2 2025 ICT stats PDF: https://www.rura.rw/index.php?eID=dumpFile&t=f&f=147480&token=f5d6725743614952f9dde682f06c2369ea137f0c ; RURA law: https://rwandalii.org/akn/rw/act/law/2013/9/eng@2013-04-08
- MINICT: https://www.minict.gov.rw/ ; Connect Rwanda: https://www.minict.gov.rw/news-detail/what-you-should-know-about-connect-rwanda-campaign
- RISA: https://www.risa.gov.rw/ ; overview https://www.risa.gov.rw/about/overview ; data-protection page https://www.risa.gov.rw/data-protection-and-privacy-law
- NCSA: https://cyber.gov.rw/ ; contact https://cyber.gov.rw/contact-us/
- Data protection law 058/2021: https://rwandalii.org/akn/rw/act/law/2021/58/eng@2021-10-15 ; DPO: https://dpo.gov.rw/
- RPPA/UMUCYO: https://www.rppa.gov.rw/ ; OCDS: https://data.open-contracting.org/en/publication/145
- RDB: https://rdb.rw/ ; e-services https://rdb.rw/e-services/ ; KIC ground-breaking https://rdb.rw/the-government-of-rwanda-africa50-and-badea-break-ground-on-the-construction-of-kigali-innovation-city/
- REG: https://www.reg.rw/ ; RURA energy https://www.rura.rw/sectors/energy/sub-sectors-and-services/electricity
- REMA: https://rema.gov.rw/
- City of Kigali: https://www.kigalicity.gov.rw/
- Internet Society IXP tracker Rwanda: https://pulse.internetsociety.org/en/ixp-tracker/country/RW/
- RINEX AS329521 (IPIP whois): https://whois.ipip.net/AS329521
- RICTA: http://www.ricta.org.rw/
- MTN Centre Kigali (PeeringDB): https://www.peeringdb.com/fac/11839 ; TrAC (PeeringDB): https://www.peeringdb.com/org/29956
- IremboGov: https://irembo.gov.rw/ ; Irembo Ltd: https://irembo.com/
- Wikipedia Telecommunications in Rwanda: https://en.wikipedia.org/wiki/Telecommunications_in_Rwanda
- DCD Rwanda tag: https://www.datacenterdynamics.com/en/tags/rwanda/
- Trade.gov ICT guide: https://www.trade.gov/country-commercial-guides/rwanda-ict-and-space-technologies ; energy guide: https://www.trade.gov/country-commercial-guides/rwanda-energy

Final note: Rwanda is a small but policy-ambitious market. As of 2026-08 the operating colocation evidence is thin (TrAC marketing claim plus aggregator listings); the credible pipeline/leads are PAIX Kigali (KIC listing), ADC Kigali (announced 2022, status unclear), Otech/BSC (2026 MoU), and aggregator-only Raxio RW1/Paratus. Everything beyond RURA/MINICT/RISA/NCSA/RPPA/RDB primary evidence and strong trade press should stay graded U/C until re-verified.
