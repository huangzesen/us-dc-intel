# AE Explorer Official - UAE Datacenter Enumeration via Planning, Utility, Free-Zone, Cloud, Colo, and Regulator Sources

Date: 2026-08-12. Scope: United Arab Emirates (AE), repo divisions are 28 municipality/city areas: Abu Dhabi Municipality, Al Ain, Al Dhafra; Ajman/Manama/Masfut; Dubai Sectors 1-9; Fujairah/Dibba Al Fujairah; Ras Al Khaimah; Sharjah city and eastern/central towns; Umm Al Quwain. Angle: official/regulatory/cloud methodology. Reliability grades: **A** = official/primary source (municipal permit service/open data, utility/grid regulator, free-zone authority, cloud/operator official page), **B** = strong secondary/trade press or contractor page with named project details, **C** = weak aggregate/directory/social-only.

---

## 0. UAE-specific structural facts

- There is **no single public national registry of UAE datacenters or datacenter planning applications**. Enumeration should join emirate-level planning systems, free-zone authority permits, utility/NOC workflows, official open-data portals, cloud region pages, telecom/colo operator pages, internet-exchange pages, and trade press.
- Permitting is fragmented by **emirate and authority jurisdiction**. Dubai has Dubai Municipality / Build in Dubai, Dubai Development Authority (DDA) for TECOM/Dubai Internet City-type zones, Trakhees for certain special development/free-zone areas, Dubai Integrated Economic Zones and other free-zone authorities. Abu Dhabi uses DMT/TAMM/Binaa plus Abu Dhabi City Municipality, Al Ain Municipality, and Al Dhafra Municipality. Northern emirates use their municipality portals plus Etihad Water and Electricity for power/water service.
- For large projects, **power is often the best official lead**. In Dubai, use DEWA building NOC and electricity connection services. In Abu Dhabi, use Department of Energy (DoE), TAQA Distribution (ADDC/AADC legacy), EWEC planning/supply announcements, and any self-supply licences. In Ajman, Fujairah, Ras Al Khaimah, Umm Al Quwain and parts of Sharjah, use Etihad Water and Electricity / local authority signals. Keep grid capacity, self-supply generation, solar PPA capacity, and IT load as separate fields.
- Free zones and master developers matter because many UAE technology/data-center sites are inside **Dubai Internet City/TECOM, Dubai Production City/IMPZ, Dubai Silicon Oasis, Masdar City, KEZAD/KIZAD, Meydan, and Fujairah/Dubai SmartHub locations**. Their authority pages may identify development controls or operator presence before a normal municipal page does.
- Official cloud regions are **metro/emirate seeds, not physical addresses**. AWS discloses `me-central-1` Middle East (UAE) with 3 AZs. Microsoft lists UAE North/Dubai and UAE Central/Abu Dhabi, with UAE Central access-restricted. Google Cloud has Doha (`me-central1`) in Qatar, not a UAE region as of the checked official pages; use it only as a regional/Middle East latency comparison, not UAE facility evidence.
- Arabic and English both matter. Use `data center`, `data centre`, `datacenter`, `مركز بيانات`, `مراكز البيانات`, `مركز بيانات`, `الحوسبة السحابية`, `تصريح بناء`, `رخصة بناء`, `تصاريح البناء`, `شهادة إنجاز`, `عدم ممانعة`, `كهرباء`, `محطة فرعية`, and `ميغاواط`.

---

## 1. Grade A official planning and permit sources

### 1.1 Dubai planning and building permits

- **Dubai Municipality building permit procedures**: https://www.dm.gov.ae/municipality-business/building-permit-steps/. Official process source for building permits, completion certificates, inspections, soil tests, topographic maps, and industrial areas. Use for projects under Dubai Municipality jurisdiction.
- **Build in Dubai**: https://buildindubai.gov.ae/services and UAE/Dubai government explainer https://www.dubai.ae/living/property-housing/building-permit. Build in Dubai is the single-window building permit platform; service text says it enables planning permits and building permits through online submission/payment/issuance. It may not expose a public searchable application file, but it gives authoritative workflow terms and service names.
- **Dubai Municipality open data**: https://www.dm.gov.ae/open-data2/. The catalog lists building-permit, demolition-permit, building-usage, project-information, project-building, and application datasets. Also check the UAE open-data mirror for Dubai Municipality building permit datasets on Bayanat, e.g. https://bayanat.ae/en/Datasets/Dataset-info?id=E_YvtwUYLtv0LFKJqcXypirak_RHCxLUFJAK-iGZaD8. Treat as Grade A for structured municipal attributes when the dataset contains project/building/application fields.
- **Data.Dubai / Dubai Pulse**: https://www.digitaldubai.ae/apps-services/details/data.dubai and https://www.dubai.ae/open-data. Use to search public-sector datasets by entity (`Dubai Municipality`, `DEWA`, `Dubai Land Department`, `Dubai Development Authority`) and by terms such as `building permits`, `project information`, `land`, `utilities`, and `electricity`.
- **Dubai Land Department open data**: https://dubailand.gov.ae/en/open-data/real-estate-data/. Useful for parcel/developer/project corroboration after a candidate site is found; not a datacenter registry.

Dubai permit/open-data queries:

```text
site:dm.gov.ae "data center" OR "data centre" OR datacenter
site:dm.gov.ae "مركز بيانات" OR "مراكز البيانات"
site:buildindubai.gov.ae "data center" OR "مركز بيانات"
site:dubai.ae "Building Permit" "Build in Dubai"
site:digitaldubai.ae "Dubai Municipality" "Building Permits"
site:bayanat.ae "Dubai Municipality" "Building Permits"
"Dubai Municipality" "data center" "building permit"
"Dubai" "data center" "completion certificate"
"Dubai" "data center" "Makani" OR "plot"
```

### 1.2 Dubai free-zone / special-zone permit authorities

- **Dubai Development Authority (DDA)**: https://dda.gov.ae/. DDA regulates master planning and construction within its jurisdiction, including master-plan reviews, design review, permits, inspections, and completion certificates. Its final building permit service is at https://dda.gov.ae/en/planning-development/construction/permits-nocs/final-building-permit and construction permits/NOCs page is https://dda.gov.ae/en/planning-development/construction/permits-nocs. High-priority for TECOM clusters such as Dubai Internet City and Dubai Production City/IMPZ where Equinix DX1/DX2 are described as located.
- **Dubai Internet City official site**: https://www.dic.ae/. Use as the official business-zone seed for technology-company tenancy and press releases. TECOM Group official press release on Khazna/Dubai Internet City: https://tecomgroup.ae/press-release/dubai-internet-city-and-khazna-data-centers-announce.
- **Dubai Silicon Oasis / DIEZ**: search official Dubai Integrated Economic Zones and Dubai Silicon Oasis pages for `data centre`, `data center`, `du`, `cloud`, `building permit`, `NOC`. Many project facts may be on tenant/operator or contractor pages, so use the free-zone source to confirm jurisdiction and the operator/municipality source for facility details.
- **Trakhees / Ports, Customs and Free Zone Corporation**: use for JAFZA, Dubai World Central-related and special development areas when a candidate lies in its jurisdiction. Search `site:pcfc.ae Trakhees data center`, `site:trakhees.ae "data center"`, and `Trakhees "building permit" "data center"`.

DDA/free-zone queries:

```text
site:dda.gov.ae ("data center" OR "data centre" OR datacenter OR "مركز بيانات")
site:dda.gov.ae ("Final Building Permit" OR "Construction Permits") "{operator}"
site:dic.ae ("data center" OR "data centre" OR Khazna OR Equinix OR cloud)
site:tecomgroup.ae "Khazna" "data"
site:pcfc.ae OR site:trakhees.ae ("data center" OR datacenter OR "مركز بيانات")
"Dubai Internet City" "data center" "permit"
"Dubai Production City" OR IMPZ "data center" "permit"
"Dubai Silicon Oasis" "data center" du
```

### 1.3 Abu Dhabi planning and building permits

- **DMT official site**: https://www.dmt.gov.ae/en. DMT exposes municipal services and links to building permit issuance. It is the institutional source for Abu Dhabi municipal planning/building workflows.
- **TAMM Request a Building Permit**: https://www.tamm.abudhabi/en/life-events/business/housing-construction/construction/RequestaNewBuildingPermit and building permit issuance page https://www.tamm.abudhabi/en/life-events/business/ManageyourPermitsMemberships/Constructions/RequestforBuildingPermitIssuance. Use these as official process evidence for Abu Dhabi, Al Ain, and Al Dhafra projects.
- **Binaa platform**: Abu Dhabi Media Office says DMT launched Binaa to enhance building permit processes: https://www.mediaoffice.abudhabi/en/infrastructure/department-of-municipalities-and-transport-launches-binaa-digital-platform-to-enhance-building-permit-processes-in-abu-dhabi/. Use `Binaa`, `MePS`, `DMT`, and `TAMM` terms when searching project records and news.
- **DMT open data / Abu Dhabi Open Data**: DMT open-data page https://www.dmt.gov.ae/en/adm/Open-Data and Abu Dhabi Open Data platform https://data.abudhabi/opendata/. Search for building permits, construction, land, facilities, and industrial-zone datasets. Coverage may be aggregate; verify against DMT/TAMM/operator records.
- **Masdar City**: https://masdarcity.ae/ is a critical Abu Dhabi free-zone/master-development seed. Masdar City official news confirms Khazna's second Masdar City facility and rooftop solar agreement: https://masdarcity.ae/news-and-media/news/2023/09/24/emerge-signs-agreement-to-develop-solar-plant-for-khazna-data-centers-facility-in-masdar-city.
- **KEZAD/KIZAD**: use official KEZAD/KIZAD and AD Ports pages for data center/industrial-zone land, especially around Taweelah/Khalifa Industrial Zone. Follow with DMT/TAMM and utility checks.

Abu Dhabi planning queries:

```text
site:tamm.abudhabi "data center" OR "data centre" OR datacenter OR "مركز بيانات"
site:dmt.gov.ae ("data center" OR "data centre" OR datacenter OR "مركز بيانات")
site:mediaoffice.abudhabi "data center" "DMT" OR "Binaa"
site:data.abudhabi "building permit" OR "construction permit"
"Binaa" "data center" "Abu Dhabi"
"MePS" "data center" "Abu Dhabi"
"Masdar City" "Khazna" "data center"
site:masdarcity.ae Khazna "data center"
site:kezadgroup.com OR site:adports.ae ("data center" OR datacenter OR "AI")
```

### 1.4 Northern emirates and Sharjah municipal sources

- **Sharjah Municipality services**: https://shjmun.gov.ae/servicedirectory/subServices/10 lists ordinary building permits, permit modifications, completion certificates, construction signage, tower crane permits, and utility completion/connection certificates. Search Sharjah Municipality plus free zones such as Hamriyah Free Zone and SAIF Zone for candidate sites.
- **Ajman government / Municipality & Planning Department**: building permit service https://www.ajman.ae/en/servicecatalog/services/3278 and service category https://www.ajman.ae/en/servicecatalog/service_categories/municipality-planning-department. Use for Ajman, Manama, and Masfut candidate buildings.
- **Ras Al Khaimah Municipality / SANAD**: building permit documentation starts at https://sanad.mun.rak.ae/docs/en/building-permits. Use for Ras Al Khaimah city/industrial-zone projects; cross-check RAKEZ if relevant.
- **Fujairah Municipality**: https://www.fujmun.gov.ae/default.aspx?lang=en and Rukhsati business licensing system. Bayanat has Fujairah building-permit-by-type datasets, e.g. https://bayanat.ae/Datasets/Dataset-info/visualization?id=KDYAuMzIP035N-TZzdF2JrJDZtql_q6eaWLLOe6KBBo&rid=vrThf4woO80AqTTceSmemOmC9lAyNQNz1FLzSqNc778. Fujairah is important because e&/SmartHub/DE-CIX references geo-redundant SmartHub sites in Fujairah and Dubai.
- **Umm Al Quwain Municipality**: search official UAQ portal/municipality pages for `building permit`, `تصريح بناء`, `data center`, and industrial/free-zone candidate names. Expect lower density but do not skip because EtihadWE and free-zone industrial projects may surface there.

Northern-emirates queries:

```text
site:shjmun.gov.ae ("data center" OR datacenter OR "مركز بيانات")
site:shjmun.gov.ae ("building permit" OR "ordinary building permit" OR "utility completion")
site:ajman.ae ("data center" OR datacenter OR "مركز بيانات")
site:sanad.mun.rak.ae ("data center" OR datacenter OR "building permit")
site:fujmun.gov.ae ("data center" OR datacenter OR "مركز بيانات")
site:bayanat.ae Fujairah "Building Permits"
"Hamriyah Free Zone" "data center" OR datacenter
"SAIF Zone" "data center" OR datacenter
"RAKEZ" "data center" OR datacenter
"Umm Al Quwain" "data center" "building permit"
```

---

## 2. Utility, grid, energy, and environmental evidence

### 2.1 Dubai power/water - DEWA

- **DEWA building NOC**: https://crm.dewa.gov.ae/irj/portal/anonymous?NavigationTarget=ROLES%3A%2F%2Fportal_content%2Fcom.dewa.portal.crm.F_Dewa_CRM%2Fcom.dewa.portal.crm.F_Pages_CRM%2Fcom.dewa.portal.crm.P_Building_NOC_Page. Lists Building NOC, infrastructure NOCs, electricity permits/connections, fit-out connections, network modification, solar permits, and cost calculator routes.
- **DEWA infrastructure project services**: https://www.dewa.gov.ae/en/builder/general-technical-services/infrastructure-projects-services. Official process source for road/network/general-project NOCs processed by DEWA Infrastructure Information and Permits Department.
- **DEWA getting electricity permits and connections**: https://dewa.gov.ae/en/builder/electricity-network-services/getting-electricity-connection. Use workflow terms like HV inspection, LV design approval, substation readiness, building NOC, fit-out connection, and load thresholds.
- **DEWA media/service pages**: official news confirms building NOCs for free zones and other licensing entities, including Trakhees, DDA, and Dubai Integrated Economic Zones. Search DEWA news for project/operator names plus `NOC`, `substation`, `renewable`, `solar`, `district cooling`, and `data center`.

DEWA queries:

```text
site:dewa.gov.ae ("data center" OR "data centre" OR datacenter OR "مركز بيانات")
site:dewa.gov.ae "{operator}" ("NOC" OR "Building NOC" OR "electricity connection")
site:dewa.gov.ae ("substation" OR "HV Inspection" OR "LV Design Approval") "data center"
"DEWA" "data center" "MW"
"Dubai" "data center" "DEWA" "substation"
"Dubai" "data center" "solar permits" "DEWA"
```

### 2.2 Abu Dhabi power/water - DoE, TAQA Distribution, EWEC

- **Abu Dhabi Department of Energy (DoE)**: https://www.doe.gov.ae/. DoE regulates energy sector legislation, secure supply, and licences service providers/suppliers. Use for official licences, policy, and regulated-asset context.
- **Khazna self-supply licence**: DoE PDF result for `Khazna Data Center Limited - SS Licence`: https://www.doe.gov.ae/-/media/Project/DOE/Department-Of-Energy/Media-Center-Publications/EDL08007-Khazna-Data-Center-Limited--SS-Licence.pdf. This is a high-value Grade A lead because it ties a data-center operator to electricity generation/self-supply licensing terms.
- **TAQA Distribution**: https://taqadistribution.com/ and legacy ADDC/AADC connection page https://www.addc.ae/en-US/distribution/Pages/ConnectionCharges.aspx. TAQA announced ADDC and AADC would be unified under TAQA Distribution; use current TAQA plus legacy ADDC/AADC terms in searches.
- **EWEC**: https://ewec.ae/ states EWEC is the sole procurer of water and power in Abu Dhabi and succeeded Abu Dhabi Water and Electricity Company/ADWEC. Search EWEC/TAQA/Masdar announcements for AI data-center power supply, grid investment, BESS/solar, and campus power agreements.
- **TAQA Transmission / EWEC / Masdar AI power announcements**: official TAQA Transmission page https://taqatransmission.com/node/121 says Abu Dhabi energy supply infrastructure investment will support AI and data centers. ADX PDF for TAQA/EWEC Al Dhafra financing says a 1 GW plant will provide power to data centre projects and advance the UAE AI Strategy.

Abu Dhabi utility queries:

```text
site:doe.gov.ae ("data center" OR "data centre" OR Khazna OR "self-supply")
site:doe.gov.ae filetype:pdf Khazna "Data Center" "Licence"
site:taqadistribution.com ("data center" OR datacenter OR "connection")
site:addc.ae ("data center" OR datacenter OR "connection charges")
site:ewec.ae ("data center" OR "data centre" OR "AI" OR "MW")
site:taqatransmission.com ("data center" OR "AI" OR "grid infrastructure")
"Abu Dhabi" "data center" "TAQA Distribution" OR ADDC OR AADC
"Abu Dhabi" "data center" "substation" "MW"
"Khazna" "self-supply licence" "Department of Energy"
```

### 2.3 Northern emirates utilities - EtihadWE and local services

- **UAE Government public utilities page**: https://u.ae/en/information-and-services/housing/public-utilities routes electricity/water service by emirate and says Etihad Water and Electricity handles service activation for its coverage areas.
- **Etihad Water and Electricity (EtihadWE / legacy FEWA)**: use for Ajman, Umm Al Quwain, Ras Al Khaimah, Fujairah, and relevant northern coverage. Search official EtihadWE service pages, e-services, tender pages, and connection/NOC terms.
- **Sharjah utility**: Sharjah has separate utility authority context (SEWA/Sharjah Electricity, Water and Gas Authority). Search official SEWA pages for high-load connection, substations, and NOCs if a Sharjah candidate appears.

Northern utility queries:

```text
site:etihadwe.ae ("data center" OR datacenter OR "connection" OR "substation")
site:u.ae "Etihad WE" "electricity and water service"
site:sewa.gov.ae ("data center" OR datacenter OR "substation" OR "connection")
"Ras Al Khaimah" "data center" "EtihadWE"
"Fujairah" "data center" "EtihadWE" OR "FEWA"
"Sharjah" "data center" "SEWA" OR "substation"
```

### 2.4 Environmental and sustainability signals

- **MOCCAE**: UAE government environment page https://www.dubai.ae/environment-sustainability identifies the Ministry of Climate Change and Environment as the federal environmental authority. MOCCAE certificate/permit verification hub: https://eservices.moccae.gov.ae/digitalcertificates/certificateverification.aspx?lang=en-US. Useful when a permit/certificate number is known; not a public datacenter list.
- **Local environmental authorities**: Abu Dhabi Environment Agency (EAD), Dubai Municipality environment department, Sharjah environment authority and free-zone EHS departments may hold EIA, air-quality, diesel generator, fuel tank, cooling, and wastewater evidence. Search by operator/project rather than generic `data center`.
- **Solar/clean-power PPAs**: Masdar City/Emerge official news on Khazna rooftop solar is Grade A for energy integration but not proof of full IT load. Use solar MWp separately from facility IT MW.

Environmental queries:

```text
site:moccae.gov.ae ("data center" OR "data centre" OR datacenter)
site:ead.gov.ae ("data center" OR datacenter OR Khazna OR "generator")
site:dm.gov.ae ("data center" OR datacenter) ("environment" OR "generator" OR "diesel")
"Khazna" "solar" "Masdar City" "MWp"
"data center" "UAE" "generator" "environmental permit"
"مركز بيانات" "تقييم الأثر البيئي" الإمارات
```

---

## 3. Regulator and policy sources

- **TDRA**: https://tdra.gov.ae/en/. TDRA regulates telecom/digital government and is useful for cloud policy, telecom licensee context, and official statements, but it is not a public facility registry. TDRA welcomed AWS's UAE data-center decision: https://tdra.gov.ae/en/media/press-release/2021/tdra-welcomes-awss-decision-to-open-data-centers-in-the-uae. TDRA cloud-security/accreditation blog: https://tdra.gov.ae/en/Participation/blogs/info?id=929.
- **UAE official portal**: https://u.ae/ for federal service routing, public utilities, environmental authorities, cloud/digital-government policy, and open-data entry points.
- **Digital Dubai / Dubai Data Law ecosystem**: use Digital Dubai for Dubai public datasets and cloud/data policies; it is a discovery aid, not facility confirmation by itself.
- **Abu Dhabi Media Office / Dubai Media Office**: official government announcements can confirm strategic projects, infrastructure initiatives, DMT/Binaa changes, and major AI/cloud campus announcements. Treat as Grade A for announcement facts and Grade A-/B+ for facility status unless tied to permit/utility records.

Policy queries:

```text
site:tdra.gov.ae ("data center" OR "data centre" OR datacenter OR AWS OR cloud)
site:u.ae ("data center" OR "cloud computing" OR "public utilities")
site:mediaoffice.abudhabi ("data center" OR "AI campus" OR "Khazna" OR "G42")
site:mediaoffice.ae ("data center" OR "cloud" OR "Microsoft" OR "du")
site:digitaldubai.ae ("data center" OR "cloud" OR "Data.Dubai")
```

---

## 4. Official cloud and operator seed lists

### 4.1 Hyperscale cloud regions - Grade A for region existence, not exact building

| Provider | Official source | UAE / nearby signal | How to use |
|---|---|---|---|
| AWS | Region docs https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html and launch blog https://aws.amazon.com/blogs/aws/now-open-aws-region-in-the-united-arab-emirates-uae/ | `me-central-1`, Middle East (UAE), 3 AZs, opt-in required | Seed Dubai/Abu Dhabi/UAE-wide searches for `Amazon Data Services`, `AWS UAE`, DEWA/DMT/TDRA references; never infer exact sites from AZs. |
| Microsoft Azure | Regions list https://learn.microsoft.com/en-us/azure/reliability/regions-list and global infrastructure geography page https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies | UAE North = Dubai (`uaenorth`); UAE Central = Abu Dhabi (`uaecentral`, access-restricted on current list) | Seed Dubai/Abu Dhabi planning and utility searches; check Microsoft official news and du/e&/Khazna ties. |
| Google Cloud | Locations https://cloud.google.com/about/locations and Compute zones docs https://docs.cloud.google.com/compute/docs/regions-zones | No UAE region on checked official pages; nearby Middle East region `me-central1` is Doha, Qatar | Do not count as UAE. Use only for regional cloud-latency context and to avoid false UAE attribution. |
| Oracle OCI | Region docs https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm and public cloud regions https://www.oracle.com/cloud/public-cloud-regions/ | Check current Oracle docs for UAE commercial/sovereign availability; do not rely on secondary lists | If a UAE Oracle region/partner claim appears, verify directly in OCI docs and then pivot to Abu Dhabi/Dubai operator records. |

Cloud query templates:

```text
"AWS" "me-central-1" "UAE" "data centers"
"Amazon Data Services" "UAE" ("permit" OR "DEWA" OR "DMT" OR "Khazna")
"Microsoft" "UAE North" "Dubai" "data center"
"Microsoft" "UAE Central" "Abu Dhabi" "data center"
"Google Cloud" "Doha" "me-central1" "UAE"
"Oracle Cloud" "UAE" "region" "official"
```

### 4.2 Major colo, telecom, interconnection, and AI infrastructure operators

| Operator / platform | Official source | UAE facility/geography seed | Method notes |
|---|---|---|---|
| Khazna Data Centers | https://khaznadatacenters.com/ | Official homepage says 30 live data centers across the UAE. G42/Khazna pages identify Masdar, Mafraq, AUH4/AUH8, and UAE-wide expansion. | Priority operator. Official pages are Grade A for operator existence/count but often hide addresses. Pivot to DoE self-supply licence, DMT/TAMM, Masdar City, DEWA, DDA, contractor pages, and press releases for site-specific evidence. |
| G42 / Stargate UAE | https://www.g42.ai/resources/news/global-tech-alliance-launches-stargate-uae and https://www.g42.ai/resources/news/g42-lead-consortium-us-partners-build-5gw-uae-us-ai-campus | Abu Dhabi 5 GW UAE-US AI Campus; Stargate UAE cluster with OpenAI/Oracle/NVIDIA/SoftBank/Cisco; Khazna as data-center developer in later G42 updates. | Treat official announcement as Grade A project lead. Facility enumeration still needs DMT/DoE/EWEC/TAQA and parcel/permit confirmation. |
| Equinix | Dubai overview https://www.equinix.com/data-centers/europe-colocation/united-arab-emirates-colocation/dubai-data-centers; DX1 https://www.equinix.com/data-centers/europe-colocation/united-arab-emirates-colocation/dubai-data-centers/dx1; DX2 https://www.equinix.com/data-centers/europe-colocation/united-arab-emirates-colocation/dubai-data-centers/dx2 | Dubai DX1, DX2, DX3. Equinix page says DX1/DX2 at IMPZ and Dubai facilities host UAE-IX powered by DE-CIX. | Official pages Grade A for IBX names/metro/location strings. Search DDA/Dubai Production City/IMPZ and DEWA for underlying permits and power. |
| e& / Etisalat SmartHub | e& SmartHub page https://www.eand.com/en/whoweare/carrier-and-wholesale/services/data-services/smart-hub/interconnected-communities.html | SmartHub ecosystem; DE-CIX says SmartHub IX is in geo-redundant SmartHub data centers in Fujairah and Dubai. | Search `SmartHub Fujairah`, `SmartHub Dubai`, `Etisalat SmartHub`, submarine cable and Fujairah municipality/EtihadWE/DEWA records. |
| du / datamena | du data-center solutions https://www.du.ae/business/digital-platform/digital-infrastructure/data-centres-solutions | du says its UAE data centers are growing to five facilities from Abu Dhabi to Dubai. datamena/UAE-IX ties make Dubai a key interconnection seed. | Official page Grade A for portfolio footprint; verify individual KIZAD/Dubai Silicon Oasis/hyperscale sites through DMT/DDA/free-zone/utility sources. |
| UAE-IX / DE-CIX | UAE-IX https://www.uae-ix.net/; DE-CIX Dubai page https://www.de-cix.net/en/locations/dubai; DE-CIX locations https://www.de-cix.net/en/locations | UAE-IX in Dubai; SmartHub IX in Fujairah and Dubai; carrier/data-center-neutral IX. | IX points identify high-probability carrier hotels and SmartHub/Equinix locations; not all IX member networks are facility operators. |
| Masdar City / Emerge | Masdar City news on Khazna solar https://masdarcity.ae/news-and-media/news/2023/09/24/emerge-signs-agreement-to-develop-solar-plant-for-khazna-data-centers-facility-in-masdar-city | Khazna second Masdar City facility, scheduled operational 2023; solar plant and Abu Dhabi portfolio >25 MWp. | Combine with DMT/TAMM and DoE/TAQA records for actual facility status and electrical facts. |
| e&/G42 Khazna merger | G42 announcement https://www.g42.ai/resources/news/g42-etisalat-to-establish-uaes-largest-data-center-provider | Twelve Etisalat/G42 data centers merged into Khazna, creating UAE's largest provider. | Use as ownership/operator consolidation evidence; then de-duplicate legacy e&/Etisalat and Khazna facilities. |

Operator queries:

```text
"Khazna" ("AUH1" OR "AUH4" OR "AUH6" OR "AUH8" OR "Masdar" OR "Mafraq" OR "Meydan")
"Khazna Data Centers" "Department of Energy" "licence"
"Khazna" "DMT" OR "TAMM" OR "Binaa"
"Equinix" ("DX1" OR "DX2" OR "DX3") "Dubai"
"Equinix" "IMPZ" "DDA" OR "Dubai Production City"
"e&" "SmartHub" "Fujairah" "data center"
"SmartHub IX" "Fujairah" "Dubai"
"du" "data centres" "KIZAD" OR "Dubai Silicon Oasis" OR "Microsoft"
"datamena" "UAE-IX" "data center"
"G42" "UAE-US AI Campus" "Abu Dhabi" "5GW"
```

---

## 5. Per-division enumeration workflow

Use the repo's municipality/city-area divisions as a routing layer, but do not assume permit authority boundaries match the GeoNames divisions exactly. For each candidate, record `emirate`, `division`, `authority jurisdiction`, `free zone/master developer`, `operator`, `source grade`, and `evidence type`.

1. **National/emirate seed pass**: collect operator official pages (Khazna, Equinix, du, e&, DE-CIX/UAE-IX), cloud-region pages (AWS/Azure/GCP/OCI), TDRA announcements, UAE open data/Bayanat, and UAE/Dubai/Abu Dhabi official portals.
2. **Emirate planning pass**: route Dubai candidates to Dubai Municipality/Build in Dubai or DDA/Trakhees/DIEZ; route Abu Dhabi candidates to DMT/TAMM/Binaa and municipality/free-zone pages; route Northern Emirates to each municipality portal and relevant free zone.
3. **Utility pass**: Dubai -> DEWA; Abu Dhabi/Al Ain/Al Dhafra -> DoE/TAQA Distribution/EWEC; Ajman/RAK/Fujairah/UAQ -> EtihadWE plus municipality; Sharjah -> SEWA plus municipality/free-zone. Search operator/project/site names with `NOC`, `connection`, `substation`, `MW`, `MVA`, `self-supply`, `solar`, and Arabic equivalents.
4. **Free-zone/master-developer pass**: search DDA/DIC/TECOM, Masdar City, KEZAD/KIZAD, Dubai Silicon Oasis/DIEZ, Meydan, Hamriyah, SAIF Zone, RAKEZ, Fujairah free-zone/port and SmartHub-related pages.
5. **De-duplicate**: UAE operators may describe campuses, data-center pods, legacy Etisalat facilities, cloud AZs, and IX sites separately. Keep a single facility/campus record when official pages show the same operator/site, but preserve aliases such as `DX1`, `DX2`, `SmartHub`, `AUH8`, `Mafraq`, `Masdar`, `Meydan`.
6. **Capacity extraction**: record IT load, total facility power, grid import, self-supply generation, solar PPA MWp, and announced campus GW separately. Do not convert or merge these numbers unless a source explicitly defines them.

### 5.1 Abu Dhabi - Abu Dhabi Municipality

Priority zone for Khazna, G42/Stargate, Masdar City, Mafraq, government/sovereign cloud, and hyperscale AI projects.

```text
"Abu Dhabi Municipality" "data center" OR "مركز بيانات"
"Masdar City" "Khazna" ("data center" OR "solar")
"Mafraq" "Khazna" "data center"
"Abu Dhabi" "UAE-US AI Campus" "DMT" OR "Department of Energy"
site:doe.gov.ae Khazna "Data Center" "Licence"
site:ewec.ae "data center" "Abu Dhabi"
```

### 5.2 Abu Dhabi - Al Ain Municipality

Lower known density, but use the same DMT/TAMM/Binaa path and TAQA Distribution. Search for government cloud, university/HPC, industrial AI, and large-load/substation clues.

```text
"Al Ain" "data center" OR datacenter OR "مركز بيانات"
"Al Ain Municipality" "data center"
site:tamm.abudhabi "Al Ain" "Building Permit" "data"
site:taqadistribution.com "Al Ain" "data center"
```

### 5.3 Abu Dhabi - Al Dhafra

Important for energy-side AI/datacenter infrastructure, renewable/baseload power, and large land parcels. Do not count power plants as datacenters unless tied to a named facility/campus.

```text
"Al Dhafra" "data center" OR "AI data centre"
"Al Dhafra" "EWEC" "data centre"
"Al Dhafra" "TAQA" "AI" "data centers"
site:ewec.ae "Al Dhafra" "data center"
site:taqatransmission.com "Al Dhafra" "data center"
```

### 5.4 Dubai - Sectors 1-9

Dubai sector boundaries require post-geocoding. Start with named zones/sites, then map to the sector: Dubai Internet City/TECOM, Dubai Production City/IMPZ, Dubai Silicon Oasis, Meydan, JAFZA/Trakhees areas, Business Bay/DIFC enterprise facilities, and SmartHub/Dubai IX sites.

```text
"Dubai" "data center" "Build in Dubai"
"Dubai" "data center" "DEWA" "NOC"
"Dubai Internet City" "Khazna Data Centers"
"Dubai Production City" OR IMPZ "Equinix" "DX1"
"Dubai Silicon Oasis" "du data center"
"Meydan" "Khazna" "data center"
"JAFZA" OR "Trakhees" "data center"
site:dda.gov.ae ("Equinix" OR "Khazna" OR "data center")
```

### 5.5 Sharjah divisions - Sharjah, Hamriyah, Dhaid, Kalba, Khor Fakkan, Dibba Al Hesn, Al Madam, Milehah, Al Batayih

Search Sharjah Municipality, SEWA, Hamriyah Free Zone, SAIF Zone, and eastern-region municipality pages. Expect enterprise/telco/edge rather than hyperscale unless a free-zone industrial project appears.

```text
"Sharjah" "data center" OR datacenter OR "مركز بيانات"
site:shjmun.gov.ae "data center"
"Hamriyah Free Zone" "data center"
"SAIF Zone" "data center"
"Khor Fakkan" "data center" OR "مركز بيانات"
"Kalba" "data center" OR "مركز بيانات"
"Dhaid" "data center" OR "مركز بيانات"
site:sewa.gov.ae ("data center" OR "substation" OR "large load")
```

### 5.6 Ajman - Ajman, Manama, Masfut

Use Ajman Municipality & Planning Department, Ajman Digital service catalog, EtihadWE, and Ajman Free Zone. Most leads are likely small colo, government IT, telecom edge, or enterprise sites.

```text
site:ajman.ae "data center" OR datacenter OR "مركز بيانات"
"Ajman Free Zone" "data center"
"Ajman" "EtihadWE" "data center"
"Manama Ajman" "data center"
"Masfut" "data center"
```

### 5.7 Ras Al Khaimah

Use RAK Municipality/SANAD, RAKEZ, EtihadWE/FEWA, and industrial-zone queries. Watch for logistics/industrial projects misclassified as digital infrastructure.

```text
site:sanad.mun.rak.ae "data center"
"Ras Al Khaimah" "data center" OR datacenter
"RAKEZ" "data center"
"Ras Al Khaimah" "EtihadWE" "substation" "data"
```

### 5.8 Fujairah - Fujairah Municipality and Dibba Al Fujairah

Fujairah is higher priority than population would suggest because of subsea/SmartHub connectivity. Use Fujairah Municipality, Fujairah free-zone/port, EtihadWE, e& SmartHub, and DE-CIX SmartHub IX references.

```text
"Fujairah" "SmartHub" "data center"
"Fujairah" "DE-CIX" "SmartHub IX"
site:fujmun.gov.ae "data center"
site:etihadwe.ae "Fujairah" "data center"
"Dibba Al Fujairah" "data center"
```

### 5.9 Umm Al Quwain

Lower density, but sweep municipality/free-zone/EtihadWE for industrial park or edge deployments.

```text
"Umm Al Quwain" "data center" OR datacenter
"Umm Al Quwain Free Trade Zone" "data center"
"UAQ" "EtihadWE" "data center"
"Umm Al Quwain" "substation" "data center"
```

---

## 6. Search pattern library

### 6.1 English discovery

```text
"United Arab Emirates" "data center" "building permit"
"UAE" "data centre" "planning permit"
"UAE" datacenter "NOC" "electricity"
"UAE" "data center" "substation" "MW"
"UAE" "hyperscale data center" "permit"
"UAE" "data center campus" "free zone"
"UAE" "data center" "completion certificate"
"Dubai" OR "Abu Dhabi" "data center" "plot"
"data center" "UAE" "self-supply licence"
"data center" "UAE" "solar" "MWp"
```

### 6.2 Arabic discovery

```text
"مركز بيانات" "الإمارات" "تصريح بناء"
"مراكز البيانات" "دبي" "تصاريح البناء"
"مركز بيانات" "أبوظبي" "دائرة الطاقة"
"مركز بيانات" "ديوا" OR "هيئة كهرباء ومياه دبي"
"مركز بيانات" "عدم ممانعة" "كهرباء"
"مركز بيانات" "محطة فرعية"
"مركز بيانات" "مدينة مصدر"
"مركز بيانات" "الفجيرة" "سمارت هب"
```

### 6.3 Document and data extraction

```text
filetype:pdf "data center" "UAE" "licence"
filetype:pdf "Khazna" "Data Center" "Licence"
filetype:pdf "data center" "Dubai" "NOC"
filetype:pdf "data center" "Abu Dhabi" "MW"
site:bayanat.ae "Building Permits" "Dubai Municipality"
site:bayanat.ae "Building Permits" "Fujairah"
site:data.abudhabi "building permit"
site:digitaldubai.ae "Building Permits"
```

---

## 7. Reliability and normalization rules

- **Grade A facility evidence**: municipal/free-zone building permit or completion certificate; utility NOC/connection/licence; official operator facility page naming a site/campus; official government/media-office project announcement; official cloud region docs for region existence only.
- **Grade B facility evidence**: contractor/project manager pages with named operator/location/capacity (e.g. EPC pages), trade press quoting official announcements, specialist datacenter press, reputable construction databases with project names. Upgrade only after matching to A-grade sources.
- **Grade C evidence**: generic datacenter directories, SEO approval guides, social posts, market reports without primary links, address guesses for cloud AZs. Use only as leads.
- **Do not count**: cloud regions/AZs as separate physical facilities; IX member lists as datacenters; power plants as datacenters unless linked to a named data-center project; telco network exchanges unless there is facility-grade hosting/colo evidence.
- **Normalize operator aliases**: `e&`, `Etisalat`, `Etisalat Group`, `e& Carrier & Wholesale`, and legacy data centers may now map into Khazna or SmartHub depending on the source date. Record source date and ownership status.
- **Normalize place aliases**: `IMPZ` = Dubai Production City; `DIC` = Dubai Internet City; `DDA` jurisdiction may cover TECOM clusters; `KIZAD` legacy branding may appear under `KEZAD`; `ADWEA/ADWEC/ADDC/AADC` are legacy Abu Dhabi energy terms now often represented by DoE/EWEC/TAQA Distribution.

Recommended facility record fields:

```text
facility_name
aliases
operator_current
operator_legacy
emirate
repo_division
free_zone_or_master_developer
planning_authority
utility_authority
evidence_grade
evidence_urls
permit_or_licence_refs
address_or_zone
makani_or_plot_if_available
status
it_load_mw
grid_import_mw_or_mva
self_supply_mw
renewable_ppa_or_solar_mwp
cloud_region_or_ix_role
notes_on_uncertainty
```
