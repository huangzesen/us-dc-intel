# SO Explorer Official - Somalia Datacenter Enumeration via Regulator, Ministry, Identity, Investment, Energy, Cloud, and Operator Sources

Date: 2026-08-12. Country: **SO Somalia**. Division model: **18 regions** (manifest list: Awdal, Bakool, Banaadir, Bari, Bay, Galguduud, Gedo, Hiiraan, Middle Juba, Lower Juba, Mudug, Nugaal, Sanaag, Middle Shabelle, Lower Shabelle, Sool, Togdheer, Northwest). Angle: **official/regulatory/cloud pipeline** for finding government, telecom, and commercial data-centre facilities.

Reliability grades:
- **A** = primary/official/legal source: NCA licensing/regulation, MOCT ministry announcement or tender, NIRA/identity-programme pages, SOMINVEST sector study, World Bank/UNDP/IFC project documents, TaiwanICDF project page for Somaliland government works, official operator page or press release (Hormuud/Somtel/Telesom/Golis/Wingu/SomaliREN), official cloud-provider region list.
- **B** = strong secondary source: trade press quoting official announcements (DCD, SONNA, Goobjoog, Garowe Online, AllAfrica/Horn Diplomat reprints of government statements), credible vendor/development-partner release, PeeringDB/IXP record when used only for interconnection/address corroboration.
- **C** = weak lead: unsupported aggregator entry, social post, old MoU, market-report snippet, scraped directory, or local report without facility, owner, physical location, and status evidence.

---

## 0. Somalia-specific structure facts

- Somalia has **no public national data-centre planning register, no functional national planning-permit database, and no unified national electricity grid**. Electricity is fragmented by city/private electricity-service-provider networks, so there is **no NEMA/NCA-style national construction/environmental approval registry** searchable online for data centres. Enumeration therefore works by joining: telecom-regulator licensing evidence, ministry/government announcements, World Bank procurement, identity-programme infrastructure records, operator official pages, IXP/interconnection records, subsea landing stations, energy-sector records, development-partner (World Bank/UNDP/IFC/TaiwanICDF) documents, and aggregator listings.
- The datacenter market is **tiny and telecom-led**. The only confirmed commercial carrier-neutral colocation facility found is **Wingu Africa Berbera SL01** (Berbera, Somaliland), but Wingu's current homepage lists Djibouti/Ethiopia/Tanzania as active markets while the Berbera press release and PeeringDB facility page remain live; re-verify operating status directly with Wingu before using high-confidence current capacity/status fields. Main operator portfolios: **Hormuud Telecom** (stated 11 data centres, ~10 MW combined, mostly Banaadir/Mogadishu until site-level proof says otherwise), **Somtel FGC** (states 3 data centres and colocation services), **Telesom** (Hargeisa), **Golis Telecom** (Bosaso/Garowe/Puntland nodes), **NationLink** (Mogadishu). Government facilities: federal **National Data Center** (Mogadishu; tendered under SCALED-UP in 2023/2024, under construction in Apr 2024, nearing completion in May 2025, facility-engineer hiring in Apr 2025), **Somaliland Government Data and Cybersecurity Center / National Data Center** (Hargeisa; ground broken 22 Sep 2025), **NIRA** national-ID/DPI systems and ABIS (Mogadishu), **SomaliREN** research/education data-centre services (Hodan district, Mogadishu).
- Admin reality check: the manifest **"Northwest" division = Woqooyi Galbeed** (the official 18th region; the old British Somaliland capital region). Somaliland's own administration splits it into **Maroodi Jeex (Hargeisa)** and **Sahil (Berbera)**. Berbera data-centre activity (Wingu SL01) is physically in Sahil but is covered under the "Northwest" division in this manifest. **Togdheer** (Burao) and **Awdal** (Borama) are also Somaliland-administered; **Sanaag/Sool** are contested between Somaliland, Puntland and SSC-Khatumo; **Bari/Nugaal/Mudug** are Puntland-administered. Always state which administration's records you searched (federal vs Somaliland vs Puntland) and do not merge.
- English works for most official and trade material. Somali and Arabic appear on government sites and local press. Use both spellings: `data centre`, `data center`, `datacentre`, `server room`, `server farm`, `cloud`, `colocation`, `co-location`, `Tier III`, `hyperscale`, `substation`, `MW`, `MVA`, `racks`. Somali terms: `xarunta xogta` (data centre), `kaydinta xogta` (data storage), `seefar` (server), `xog-ballaarinta` (digitalisation), `maamulka isgaarsiinta` (communications authority), `wasaaradda isgaarsiinta` (ministry of communications). Arabic: `markaz al-bayanat` = centre of data.
- Treat **cloud-region evidence as seeds only**: no hyperscaler operates a Somalia region (AWS/Azure/GCP/OCI official region lists do not include Somalia as of this methodology date). Federal policy explicitly aims to reduce dependence on foreign data storage (data-sovereignty push around the National Data Center) - an incentive signal, not a facility record.
- Security context matters: Al-Shabab has attacked telecom infrastructure; Hormuud lost staff to attacks in 2024. Verify facility claims via official channels and current status.

---

## 1. Grade A official portals and regulatory sources

### 1.1 National Communications Authority (NCA) - telecom regulator

- **NCA website**: https://nca.gov.so/
  - Established under the **National Communications Law of 2017** (Communications Act 2017). Mandate: spectrum management, operator licensing, cybersecurity (SOMCERT), consumer protection, IXP facilitation, subsea-cable regulation.
  - NCA is the primary licence-issuer for telecom operators in the Federal Republic. Use it to confirm which operators hold national licences (Hormuud was awarded Somalia's first radio-spectrum licence in Nov 2022: https://www.hormuud.com/Updates/HORMUUD-AWARDED-SOMALIA%E2%80%99S-FIRST-RADIO-SPECTRUM-LICENSE ) and to find policy statements relevant to data-centre/cloud services.
- **NCA-IFC subsea-cable framework** (Sep 2024, covered by DCD/SONNA): https://www.datacenterdynamics.com/en/news/nca-and-ifc-agree-framework-for-somalian-subsea-cables/ ; https://sonna.so/en/article/national-communications-authority-of-somalia-and-ifc-host-workshop-on-critical-telecommunications-regulations . Use as a regulator-backed seed for landing-station searches and environmental/licensing context; grade A for an NCA/IFC primary page if found, B for press coverage.
- **Submarine Cable Landing Regulation consultation** (NCA, 2025): https://nca.gov.so/nca-holds-consultation-meeting-on-submarine-cable-landing-regulation/ - strengthens landing-station/licensing context; not data-centre evidence.
- **Somali Internet Exchange Point (SoIXP / earlier MogIX)**: MOCT announcement May 2018 https://moct.gov.so/en/somalia-to-establish-first-internet-exchange-point/ ; PCH record https://www.pch.net/ixp/details/2072 lists SoIXP in Mogadishu, active, managed by National Communications Authority Somalia, established 20 Nov 2018. The IXP is an interconnection anchor only; do not record it as a data-centre facility.

NCA/MOCT query templates:
```text
site:nca.gov.so "data centre" OR "data center" OR datacentre
site:nca.gov.so licence "{operator}"
site:nca.gov.so "IXP" OR "internet exchange"
site:nca.gov.so "subsea" OR "cable landing"
site:moct.gov.so "data centre" OR "data center" OR "National Data Center"
site:moct.gov.so "cloud" "government"
"{operator}" "NCA" Somalia licence
"SOMCERT" "{operator}" data
```

### 1.2 Ministry of Communications and Technology (MOCT) - federal government

- **MOCT**: https://moct.gov.so/en/ (Somali: https://moct.gov.so/ )
  - Federal ICT ministry. Primary owner of the **National Data Center** project and e-government agenda.
  - **Procurement trail (Dec 2023-Feb 2024)**: Ministry of Finance/SCALED-UP request for bids for "Supply, Installation, Commissioning and Support for Data Center for Ministry of Communication and Technology", Project ID P168115, RFB SO-MOF-374369-GO-RFB, posted on SomaliJobs with a MOCT-hosted bidding-document link: https://somalijobs.com/tenders/somalia/16504385293277024/amendment-to-submision-deadline-and-response%3A-request-for-bids-for-supply%2C-installation%2C-commissioning-of-data-centre-for-ministry-of-communications-and-technology . Grade A for the underlying FGS/World Bank procurement when the MOCT/MoF PDF is accessible, B for the SomaliJobs mirror.
  - **National Data Center article (Apr 28, 2024)**: https://moct.gov.so/en/the-minister-of-communications-and-technology-toured-the-national-data-center/ - Minister Mohamed Adam Moalim Ali toured the facility under construction; stated it will centralise government data, eliminate dependence on foreign data storage, and support data sovereignty. Accompanied by NCA Director General Mustafa Yasin Sheikh. Grade **A** for existence/status of the project.
  - **Near-completion status (May 6, 2025)**: MOCT primary status update https://moct.gov.so/en/h-e-minister-mohamed-adam-moalim-ali-inspects-progress-of-the-national-data-center-construction/ and SONNA mirror https://sonna.so/en/article/minister-of-communications-inspects-final-stages-of-national-data-center-construction - minister's second site visit; MOCT says construction was "nearing completion" and engineers briefed the minister on projected completion timing. Grade A via MOCT, B/A via SONNA.
  - **Operations hiring (Apr 2025)**: Data Center Facility Engineer REOI, Mogadishu, SCALED-UP Project, SO-MOF-425074-CS-INDV, says MoCT is implementing a centralized national Data Center to consolidate scattered FGS hosting infrastructure and seeks an engineer for operations/maintenance: https://somalijobs.com/jobs/mogadishu/9974656767534180/data-center-%28dc%29-facility-engineer-%28individual-consultant%29 . Grade B mirror of official procurement; useful operational-readiness signal.
  - **Aug 7, 2026 planning statement**: State Minister Ahmed Osman Dirie at the launch of Garad.ai by Arkaan AI Centre said the government is developing plans for a National Data Centre to strengthen digital infrastructure (Dawan): https://www.dawan.africa/news/somalia-plans-national-data-centre-to-strengthen-digital-infrastructure . Because this conflicts with the 2024-2025 construction/near-completion record, treat it as either a generic reference to the same programme, a next-phase/expansion plan, or a parallel planned facility; do not downgrade the earlier physical-site evidence without a primary MOCT clarification. Grade B/C.
  - Extract: location (Mogadishu/Banaadir, district if named), stage verbs (`under construction`, `nearing completion`, `plans`), partner agencies (NCA, ministry), capacity if ever published (none found yet), commissioning dates.

Federal e-government/government-portal context:
- **Federal Republic of Somalia portal**: https://www.somalia.gov.so/ (About page https://www.somalia.gov.so/about-somalia ). General government information; no DC facility register.
- There is no federal e-permitting portal for buildings/data centres. Municipal building permits are issued by Banadir Regional Administration (Mogadishu) and district offices; these are **not reliably published online** - treat any online permit record as a rare bonus, grade B if web-indexed from an official source.

### 1.3 NIRA - national identity / biometric infrastructure

- **NIRA**: https://nira.gov.so/ - National Identification and Registration Authority. Runs the biometric national ID programme, HUBIYE verifier platform, Certificate Delivery System, and eAqoonsi digital ID app.
- Infrastructure relevance: NIRA's official DPI launch page says the World Bank Scaled-UP Project supported the infrastructure and technical capacity for HUBIYE/CDS/eAqoonsi (https://nira.gov.so/news/nira-launches-key-digital-public-infrastructure-for-national-id-system). World Bank's Sep 17, 2025 blog says the mass-registration pilot launched on Aug 18, 2025 in Shangani and Boondheer districts and is planned to scale across Banadir and nationally by 2029: https://blogs.worldbank.org/en/nasikiliza/federal-republic-of-somalia-launches-mass-registration-drive-for-its-digital-id .
- The ABIS is a separate law-enforcement biometric infrastructure lead. Biometric Update/HigherGov summarize the FBI RFI for operations and maintenance of Somalia ABIS, including a secure facility at Aden Adde International Airport, Mogadishu, database capacity of 2,000,000 ten-print records and 50,000 latent records, and a secondary secure backup server: https://www.biometricupdate.com/202501/fbi-seeks-vendors-for-its-somalia-abis ; https://www.highergov.com/contract-opportunity/cjis-somalia-abis-rfi-fy-2025-djf-25-rfi-01102025-r-78ef3/ . Grade B/C unless the SAM.gov primary notice or Somali authority document is retrieved.
- **Do not convert identity data centres into commercial datacenter records**; record them in a government/identity category.

### 1.4 Somaliland official sources (for Awdal, Togdheer, Sanaag, Sool, Northwest/Woqooyi Galbeed divisions)

- **Somaliland government portal**: https://govsomaliland.org/ (portal availability is unstable - if down, use ministry pages, TaiwanICDF, and web cache).
- **Ministry of Information and ICT Development / Ministry of Information and Communication Technology**: https://moiid.govsomaliland.org/ and related MICT references. The old MOIID Wingu page may 404; prefer Wingu's own press release and PeeringDB for Berbera.
- **Somaliland Government Data and Cybersecurity Center / National Data Center**: TaiwanICDF primary page confirms that the Taiwan Technical Mission and Somaliland MICT held a groundbreaking ceremony on **22 Sep 2025 at the MICT in Hargeisa**; it describes Somaliland's first government data center, server facilities, cybersecurity management systems, S-Road/e-governance linkage, and planned ISO/IEC 27001 support: https://www.icdf.org.tw/wSite/ct?ctNode=31572&mp=2&xItem=74053 . AllAfrica/Horn Diplomat mirror the same event and cite an over-USD-1M project: https://allafrica.com/stories/202509230049.html ; https://www.horndiplomat.com/somaliland-breaks-ground-on-national-data-center-with-taiwans-support/ . Grade A for TaiwanICDF project facts, B for press reprints.
- **Somaliland Ministry of Telecommunications and Technology** - search its pages for data-centre/e-government statements.
- Somaliland has its own regulatory/administrative environment; federal NCA licensing is not uniformly applied in Somaliland, so do not assume federal NCA records cover Somaliland operators (Telesom, Somtel, Somcable).

Somaliland query templates:
```text
site:govsomaliland.org "data centre" OR "data center" OR datacentre OR "National Data Center"
site:moiid.govsomaliland.org "data" "centre" OR "center"
"Somaliland" "National Data Center" Hargeisa
"Somaliland" "data centre" Telesom OR Somtel OR Wingu OR Somcable
"Electronic Government Services" Somaliland "data centre"
"Hargeisa" "data center" "e-government"
```

### 1.5 Puntland official sources (Bari, Nugaal, Mudug and contested parts of Sool/Sanaag)

- No strong online e-permitting or ICT-regulator portal was found for Puntland. Use:
  - **Puntland Ministry of Finance**: https://mof.pl.so/ (government zone, Garowe) - tender notices can surface ICT/data-centre procurement.
  - **Garowe Online** (https://www.garoweonline.com/) - main Puntland press; frequently carries Puntland government ICT/e-government statements.
  - Search terms: `Puntland Ministry of Posts and Telecommunications`, `Puntland e-government`, `Garowe data centre`, `Bosaso data centre`, `Puntland ICT policy`. Verify any claimed facility with an operator page (Golis Telecom) or Puntland government release.

### 1.6 Investment promotion and development-partner records

- **SOMINVEST - Somalia Investment Promotion Office** (under the Ministry of Planning, Investment and Economic Development; statutory body per the Foreign Investment Law of 2015): https://sominvest.gov.so/ - has an official **ICT Sector Study**: https://sominvest.gov.so/ict-sector-study/ - grade A for the study itself; use for market framing, not facility inventory.
- **World Bank - Somalia Digital Economy Diagnostic (2022)**: https://thedocs.worldbank.org/en/doc/61714f214ed04bcd6e9623ad0e215897-0400012021/related/IDU105f167fa1085214f8b1919f141249b1e8fae.pdf - authoritative context on connectivity, regulation, and digital infrastructure gaps. Grade A.
- **World Bank digital ID blog** (mass registration drive): https://blogs.worldbank.org/en/nasikiliza/federal-republic-of-somalia-launches-mass-registration-drive-for-its-digital-id
- **World Bank / SCALED-UP procurement trail for federal NDC**: use World Bank project ID P168115 and the FGS/MoF tender mirrors above; search World Bank procurement and contract-award datasets for `SO-MOF-374369-GO-RFB`, `SO-MOF-425074-CS-INDV`, and `Data Centre for Ministry of Communications and Technology`.
- **UNDP Somalia digital transformation**: https://www.undp.org/somalia/stories/driving-digital-transformation-somalia-2025-highlights - DPI/NIRA framing; grade B/A.
- **Somalia National Transformation Plan / digital economy strategy** - search `Somalia National Transformation Plan digital` and `Somalia digital economy strategy`; strategy PDFs can name planned data-centre/government-cloud investments.

Investment/donor query templates:
```text
site:sominvest.gov.so "data centre" OR "data center" OR ICT
site:worldbank.org Somalia "data centre" OR "data center" OR "digital ID" OR ABIS
site:undp.org/somalia "data centre" OR "data center" OR DPI
"Somalia" "digital economy" strategy "data centre"
"Somalia" "National Data Centre" tender OR procurement
"SO-MOF-374369-GO-RFB" OR "SO-MOF-425074-CS-INDV"
"P168115" "Data Centre" Somalia
```

---

## 2. Power, grid, and energy evidence

- **Fragmented grid/private ESP model**: electricity is provided by private utility companies per city. Mogadishu: **BECO** (https://beco.so/ - Tarabun Street, Hodan, Mogadishu; covers much of Banaadir and nearby South-Central load) plus other city ESPs that must be verified case by case. BECO installed an 8 MWp solar PV plant; treat the planned 100 MW expansion and installed-capacity figures as dated unless a current utility source confirms them (Green Building Africa: https://www.greenbuildingafrica.co.za/somalia-beco-commissions-8mw-solar-pv-plant-in-mogadishu/ ).
- **Ministry of Energy and Water Resources (MOEWR)** implements the **Somali Electricity Sector Recovery Project (SESRP)**: https://sesrp.moewr.gov.so/ - tenders/addenda include 55 MWp AC solar PV + 160 MWh BESS for BECO at Daynile/Jazeera power-plant sites in Mogadishu and 3.5 MWp + 7 MWh BESS for GECO in Galkayo. Use SESRP tender pages for power-infrastructure signals near potential DC sites; grade A for official tenders, but do not infer a datacenter from power capacity alone.
- Data centres in Somalia realistically run on **diesel + solar + battery** behind-the-meter or on private utility supply. Hormuud states several of its data centres run up to 95% solar during daylight (DCD/Bloomberg, Dec 2024: https://www.datacenterdynamics.com/en/news/hormuud-ceo-announces-plans-for-more-green-data-centers/ ). Record energy claims separately from IT load.

Energy query templates:
```text
site:beco.so "data centre" OR "data center" OR "large customer" OR MW
site:sesrp.moewr.gov.so tender "power plant" OR substation
"{town}" Somalia electricity utility "{operator}" "data centre"
"{operator}" Somalia solar "data centre" MW
"Mogadishu" electricity "MW" "data centre"
```

---

## 3. Official cloud-region and edge signals

| Provider | Official source | Somalia signal | How to use |
|---|---|---|---|
| AWS | AWS global infrastructure: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | No Somalia region, no Local Zone listed as of this methodology date. | Tenant/partner/edge lead only; do not infer a Somalia AWS facility. |
| Microsoft Azure | Azure regions: https://learn.microsoft.com/en-us/azure/reliability/regions-list | No Somalia region listed. | Tenant/edge lead only. |
| Google Cloud | Google locations: https://cloud.google.com/about/locations | No Somalia region listed. | Tenant/edge lead only. |
| Oracle OCI | OCI regions: https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | No Somalia region listed (Africa operational regions are Johannesburg/Casablanca etc.). | Tenant lead only. |
| Sovereign/government cloud | moct.gov.so, NIRA, govsomaliland.org | Federal data-sovereignty push (National Data Center) and Somaliland e-government modernisation; NIRA eAqoonsi/ABIS. | Government infrastructure projects, not hyperscaler regions; record separately. |

Cloud query templates:
```text
site:aws.amazon.com Somalia region OR "Local Zone"
"Somalia" "cloud region" OR "public cloud" hyperscaler
"Somalia" "data sovereignty" "data centre"
"Somaliland" "data centre" Telesom OR Somtel cloud
```

---

## 4. Official/operator facility seed list

Operator pages are primary statements for marketed facility existence and city. They are not substitutes for commissioning/construction evidence when classifying status.

| Operator / project | Official source | Somalia footprint signal | Follow-up joins |
|---|---|---|---|
| Federal National Data Center (MOCT/NCA) | MOCT Apr 2024: https://moct.gov.so/en/the-minister-of-communications-and-technology-toured-the-national-data-center/ ; MOCT May 2025: https://moct.gov.so/en/h-e-minister-mohamed-adam-moalim-ali-inspects-progress-of-the-national-data-center-construction/ ; procurement mirror: https://somalijobs.com/tenders/somalia/16504385293277024/amendment-to-submision-deadline-and-response%3A-request-for-bids-for-supply%2C-installation%2C-commissioning-of-data-centre-for-ministry-of-communications-and-technology | Mogadishu (Banaadir); procurement 2023/2024; under construction Apr 2024; nearing completion May 2025; facility-engineer hiring Apr 2025; government data-sovereignty hub; capacity not published. | Search MOCT/NCA/MoF/World Bank procurement, project-manager/facility-engineer TORs, district permits. Treat Aug 2026 "plans" coverage as an expansion/phase lead until MOCT clarifies. |
| Somaliland Government Data and Cybersecurity Center / National Data Center | TaiwanICDF: https://www.icdf.org.tw/wSite/ct?ctNode=31572&mp=2&xItem=74053 ; AllAfrica: https://allafrica.com/stories/202509230049.html | Hargeisa (Northwest/Woqooyi Galbeed); ground broken 22 Sep 2025 at MICT; first government data center for Somaliland; server facilities + cybersecurity management systems; e-government/S-Road linkage; ~USD 1M reported by press. | Search Somaliland MICT/MOIID releases, TaiwanICDF project pages, S-Road/e-government docs, Somaliland budget docs. |
| Wingu Africa Berbera SL01 | Wingu official news: https://www.wingu.africa/latest-news/wingu-opens-carrier-neutral-data-centre-in-berbera-somaliland ; PeeringDB https://www.peeringdb.com/fac/13450 ; Baxtel https://baxtel.com/data-center/wingu-africa-berbera-sl01 | Berbera (Sahil, within "Northwest" division); first phase commissioned 13 Feb 2021 and ready for service per Wingu Feb 2022 release; first/only commercial carrier-neutral DC in Somaliland at that time; PeeringDB lists Batalaale Beach, Zone 20 / Beach Road and Somcable ASN 37425. | Verify current status/capacity directly because Wingu's current homepage omits Somaliland from active market cards; join Somcable 2Africa landing and Berbera port/SEZ plans. |
| Hormuud Telecom portfolio | Hormuud: https://hormuud.com/ ; jobs page for DC ops: https://hormuud.com/Jobs/12 ; DCD/Bloomberg Dec 2024: https://www.datacenterdynamics.com/en/news/hormuud-ceo-announces-plans-for-more-green-data-centers/ | 11 data centres, ~10 MW combined (CEO statement); some up to 95% solar by day; DARE1 cable landing station in Mogadishu completed Nov 2022 (DCD: https://www.datacenterdynamics.com/en/news/hormuud-telecom-cable-landing-station-construction-completed-in-somalia/ ); first national spectrum licence Nov 2022. | Facility-level records need per-site evidence (address, MW, racks); do not create 11 records from the aggregate claim. |
| Somtel FGC / Somtel (Dahabshiil group) | Somtel FGC: https://somtelfgc.com/about/ ; Somtel network page: https://www.somtelnetwork.net/Submarrine-cable ; first 5G in Somalia Jan 2024 (DCD: https://www.datacenterdynamics.com/en/news/somtel-launches-first-5g-network-in-somalia/ ) | Hargeisa-headquartered FGC page offers colocation services; Somtel network page states "3 Data Centers" and landing points at Mogadishu, Bosaso, Wajaale, Djibouti, Mombasa plus planned Berbera (2025). | Operator claim proves portfolio/service category, not three individual facilities. Verify physical sites via operator, PeeringDB, cable-landing docs, or customer interconnect pages before creating records. |
| Telesom | https://www.telesom.com/ ; 5G launch 1 Jan 2024 Hargeisa (SomalilandCurrent: https://www.somalilandcurrent.com/telesom-leads-somalilands-5g-future-amidst-adversity/ ) | Hargeisa (Northwest); Telesom group includes Somgas (gas), TEC (electricity), Dara Salaam Bank; e-government service delivery partner for Somaliland. | DC-specific evidence is thin; search `Telesom "data centre"`, Telesom enterprise/EGS pages, Somaliland MOIID releases. |
| Golis Telecom | https://golistelecom.com/ (HQ Biyo Kulule road, Bosaso); GSMA mobile-money certification with Hormuud: https://www.garoweonline.com/en/news/somalia/hormuud-and-golis-telecom-achieve-gsma-certification-as-mobile-money-providers | Bosaso (Bari), Garowe (Nugaal), Galkayo (Mudug), Qardho and other Puntland towns; fibre/microwave backbone Bosaso-Galkayo (~750 km). | DC-specific evidence is thin; search `Golis Telecom "data centre"`, Puntland e-gov, Golis enterprise services. |
| NationLink Telecom | https://en.wikipedia.org/wiki/NationLink_Telecom (founded 1997, Mogadishu; ~16% market share 2022 per industry sources) | Mogadishu (Banaadir) and southern cities incl. Kismayo (Lower Juba). | DC-specific evidence thin; search `NationLink "data centre"`, NationLink enterprise/internet services, NCA licence records. |
| SomaliREN data centre | https://somaliren.org/ ("To our Data Center"; 33 member institutions by 2026; 50+ sites) | TCC Building, Taleh Road, Hodan District, Mogadishu (Banaadir); academic research/education network DC; AS327764; eduroam via UbuntuNet (https://ubuntunet.net/members/somaliren-succeeds-in-implementing-the-international-service-of-eduroam/ ). | Record as education-network DC (not commercial colo); join SomaliREN reports and SORER repository pages. |
| NIRA identity infrastructure | https://nira.gov.so/ ; NADRA cooperation (Biometric Update Mar 2025); ABIS (FBI vendor solicitation Jan 2025 via Hiiraan) | Mogadishu (Banaadir) core systems; registration centres across FMS. | Government/identity category; do not merge with commercial DCs. |

Operator query templates:
```text
"{operator}" Somalia "data centre" OR "data center" MW
"{operator}" "{town}" "data centre" racks
site:{operator-domain} "data centre" OR "data center"
"{operator}" "landing station" OR "IXP" OR "peering"
"{operator}" "Uptime" OR "Tier" Somalia
```

---

## 5. Regional enumeration strategy for 18 regions

There is no per-region planning portal. For each region, run: (1) named-operator sweep, (2) official-domain search (NCA/MOCT for federal areas; govsomaliland/moiid for Somaliland; Garowe Online for Puntland), (3) local press, (4) aggregator/PeeringDB check. Most regions will be negative or government-ICT only.

| Region (manifest) | Capital / main towns | Administration | Expected yield and seeds |
|---|---|---|---|
| Banaadir | Mogadishu | Federal | **Highest density**: federal National Data Center (procurement/construction/near-completion), Hormuud DC portfolio (incl. DARE1 landing station as interconnect), NationLink, SomaliREN DC/contact address, NIRA/HUBIYE/eAqoonsi and ABIS, SoIXP/MogIX, Hormuud/Somtel 5G, enterprise/server rooms. |
| Northwest (Woqooyi Galbeed) | Hargeisa (+Berbera/Sahil) | Somaliland | **Second cluster**: Somaliland Government Data and Cybersecurity Center (Hargeisa), Wingu Berbera SL01 (Berbera/Sahil), Telesom, Somtel/FGC, Somcable 2Africa landing station (Berbera), EGS/S-Road e-government services. |
| Awdal | Borama | Somaliland | Low: Telesom/Somtel network nodes, university ICT; expect negative unless e-gov or university DC surfaces. |
| Togdheer | Burao | Somaliland | Low: Telesom/Somtel coverage, Somtel contact-page "Togdheer" wording - flag, verify physical sites. |
| Bari | Bosaso, Qardho | Puntland | Low-medium: Golis Telecom HQ (Bosaso), telecom core nodes, DARE1/G2A/Somtel landing-point leads. No confirmed commercial DC found; treat Bosaso cable landing as interconnect, not DC, unless a facility record names racks/colo/hosting. |
| Nugaal | Garowe | Puntland | Low-medium: Golis Telecom, Puntland government e-services (mof.pl.so tenders), Garowe Online coverage. No confirmed DC found in official/industry sweeps. |
| Mudug | Galkayo | Puntland/Galmudug boundary | Low: Golis Telecom nodes, Hormuud 5G city, GECO/SESRP power project lead in Galkayo. No confirmed DC found. |
| Lower Juba | Kismayo | Jubaland | Low: NationLink/Hormuud presence, port/ICT chatter; no confirmed commercial DC. |
| Middle Juba | Bu'aale | Jubaland | Very low: expect negative. |
| Bay | Baidoa | Southwest | Very low: government/ATMIS ICT, UN agencies; expect negative for commercial DC. |
| Bakool | Hudur | Southwest | Very low: negative expected. |
| Gedo | Garbahaarey | Jubaland | Very low: negative expected. |
| Hiiraan | Beledweyne | Hirshabelle | Very low: negative expected; telecom nodes only. |
| Middle Shabelle | Jowhar | Hirshabelle | Very low: negative expected. |
| Lower Shabelle | Afgooye, Merca | Southwest/Federal | Very low: negative expected. |
| Sanaag | Erigavo | Contested (Somaliland/Puntland/SSC-Khatumo) | Very low: Golis nodes (Erigavo per Devex); expect negative for DCs. |
| Sool | Las Anod | Contested | Very low: conflict-affected; expect negative. |
| Galguduud | Dhusamareb | Galmudug | Very low: government ICT; expect negative. |

Region query templates:
```text
"{region}" Somalia "data centre" OR "data center" OR datacentre
"{region}" Somalia "server room" OR "server farm" OR colocation
"{capital}" Somalia "{operator}" "data centre"
"{capital}" Somalia "e-government" OR "ICT centre"
site:garoweonline.com "{capital}" "data centre"
```

---

## 6. Practical grading and de-duplication rules

- **A facility exists (A)** when an official government/operator page names the facility and location (federal National Data Center via MOCT; Wingu Berbera via Wingu; SomaliREN via somaliren.org), or when a regulator/ministry document identifies it.
- **Under construction (A/B)** only with official evidence: MOCT tours/procurement for the federal NDC; TaiwanICDF/MICT for the Somaliland Government Data and Cybersecurity Center.
- **Portfolio claims are not facility records**: Hormuud's "11 data centres / 10 MW" (CEO statement via Bloomberg/DCD, B) proves a portfolio, not 11 individually verified sites. Somtel's "3 Data Centers" claim proves a portfolio/service claim only; require per-site confirmation.
- **Capacity**: no public facility-level IT-load figures found for Somali facilities. Record any MW/MVA/MWh with unit and source; flag the common Hormuud "10MW" and "95% solar" figures as portfolio/energy-mix claims, not per-facility IT load. Do not confuse MWp/MWh energy projects with data-centre capacity.
- **Cloud region != facility**; hyperscaler presence = none. Do not record AWS/Azure/GCP/OCI as Somali facilities.
- **Somaliland vs federal split**: keep separate attribution. Federal NCA records do not cover Somaliland licensing cleanly; Wingu/Telesom/Somtel/Somcable are Somaliland-context. "Northwest" in this manifest = Woqooyi Galbeed; Wingu's Berbera site is in Sahil - assign to Northwest with a Sahil note to avoid a second bogus region.
- **Landing stations and IXPs are not data centres** (DARE1 landing station Mogadishu; Somcable 2Africa Berbera; SIXP) - record as interconnect anchors only.
- **Government "data centre" ambiguity**: e-government server rooms, university labs, NGO data-collection offices, and biometric enrolment centres are not commercial datacenters. Grade cautiously and categorise.
- **Stale/aspirational items**: old MoUs, "plans", and feasibility chatter (incl. the Aug 2026 NDC "plans" statement) are intent, not facilities - require a physical-site/status source to upgrade.

---

## 7. Source priority checklist

1. NCA (nca.gov.so) licensing/regulation and MOCT (moct.gov.so) ministry statements.
2. Official government project pages: federal National Data Center, Somaliland National Data Center (govsomaliland.org/moiid), NIRA identity programme.
3. Operator official pages: Hormuud, Somtel, Telesom, Golis, NationLink, Wingu, SomaliREN.
4. Energy: BECO/SESRP/MOEWR tenders and power-plant records.
5. Development-partner documents: World Bank (Digital Economy Diagnostic 2022, digital ID), UNDP, IFC subsea framework.
6. Interconnection records: SIXP/MogIX, landing stations, PeeringDB.
7. Local/state press (SONNA, Goobjoog, Garowe Online, Somaliland press) as B-grade verification.
8. Aggregators (datacentermap, Baxtel, OCOLO, datacenters.com, DataCenterPlanet) as C-grade leads only.
