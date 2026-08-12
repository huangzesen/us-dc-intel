# ZA Explorer Official — South Africa Datacenter Enumeration via Planning, Eskom/NERSA, Cloud, Colo, and ICASA

Date: 2026-08-12. Country: **ZA South Africa**. Scope: official/regulatory/cloud methodology for enumerating datacenter projects across South Africa's 9 provinces and municipalities. Angle: **official/regulatory/cloud first**, with trade press only as a lead source. Reliability grades: **A** = official/primary source (municipal land-use/building record, Municipal Planning Tribunal item, environmental authorisation, Eskom/NERSA/ICASA page, official cloud-region page, official operator page), **B** = strong secondary/trade press with named project/operator/location, **C** = weak aggregate, social, consultant, or unsupported announcement.

---

## 0. South Africa-specific structural facts

- South Africa does **not** have one national public datacenter register or one national planning-permit database. Enumeration is a **municipality-first land-use/building-control exercise**, backed by environmental, power, telecoms, cloud, and operator evidence.
- Land-use decisions are routed through municipal planning systems under the **Spatial Planning and Land Use Management Act (SPLUMA)** framework. SPLUMA requires municipalities to establish Municipal Planning Tribunals (MPTs) or equivalent decision structures for land-development applications. Grade **A** evidence is usually a municipal agenda item, tribunal report, decision notice, zoning approval, building-plan approval, Site Development Plan, or appeal record.
- The practical search unit is usually **metro/local municipality**, not province. Provinces matter for environmental competent authority, economic-development promotion, and grid constraints; municipalities hold the decisive land-use/building documents.
- Power is a core filter. South African datacenter projects often surface through Eskom transmission/distribution context, municipal electricity constraints, NERSA generation registrations/licences for dedicated supply, private power procurement, wheeling, or substation applications.
- Cloud regions are **metro seeds only**. AWS Cape Town, Azure South Africa, Google Johannesburg, OCI Johannesburg, and Huawei South Africa prove market presence and narrow the search to Cape Town/Johannesburg corridors, but they do not disclose exact facilities. Use operator/planning/environmental records for siting.
- ICASA is not a datacenter land-use regulator. Its value is telecoms/fibre infrastructure, electronic communications licensing, rapid-deployment/right-of-way records, spectrum/site context, and public consultations that may name infrastructure providers or GIS reporting requirements.

---

## 1. Grade A official/regulatory portals and how to use them

### 1.1 Municipal planning, land-use, and building-control records

Primary legal route:

- **SPLUMA / municipal planning by-laws**: use the municipality's planning portal, MPT meeting pages, council agendas, public participation notices, and building-control pages. Legal text/reference copies are available via SAFLII/Open By-laws/LawLibrary when the municipal site is hard to navigate, but the municipal decision document remains the preferred Grade **A** source.
- **City of Cape Town Planning Portal**: https://www.capetown.gov.za/Work%20and%20business/Planning-portal
- **City of Cape Town building-plan applications**: https://www.capetown.gov.za/City-Connect/Apply/Planning-building-and-development/Building-plan-applications
- **City of Cape Town MPT meeting details**: https://web1.capetown.gov.za/web1/councilhubonline/mptmeetingdetail
- **City of Cape Town planning by-law page**: https://www.capetown.gov.za/work%20and%20business/planning-portal/regulations-and-legislations/planning-by-law
- **City of Johannesburg eServices / building-plan progress**: https://eservices.joburg.org.za/pages/BuildingPlanProgress.aspx
- **City of Johannesburg municipal planning by-law reference**: https://openbylaws.org.za/akn/za-jhb/act/by-law/2024/municipal-planning/eng%402024-04-03
- **eThekwini Municipality**: https://www.durban.gov.za/ and planning/economic-development committee pages; also search council minutes and press statements for feasibility/MOA-stage projects.
- Other metros to sweep directly: Tshwane, Ekurhuleni, Nelson Mandela Bay, Mangaung, Buffalo City.

Municipal keyword searches:

```text
"data centre" +"Municipal Planning Tribunal"
"data center" +"Municipal Planning Tribunal"
"datacentre" +"land use application"
"data centre" +"rezoning"
"data centre" +"departure"
"data centre" +"site development plan"
"data centre" +"building plan"
"data centre" +"environmental impact assessment"
"data centre" +"public participation"
"data centre" +"appeal"
"data hall"
"server hall"
"hyperscale"
"colocation"
"co-location"
"standby generators"
"diesel storage"
"substation"
```

Municipal site-scoped templates:

```text
site:capetown.gov.za "data centre"
site:capetown.gov.za "data center" "Municipal Planning Tribunal"
site:web1.capetown.gov.za "data centre"
site:joburg.org.za "data centre"
site:durban.gov.za "data centre"
site:tshwane.gov.za "data centre"
site:ekurhuleni.gov.za "data centre"
site:nelsonmandelabay.gov.za "data centre"
site:mangaung.co.za "data centre"
site:buffalocity.gov.za "data centre"
```

Data to extract from municipal packs: application/reference number, erf/farm/portion, street/precinct, zoning requested, applicant and land owner, operator if disclosed, floor area, number of buildings/data halls, MVA/MW electricity demand, backup generation and diesel storage, water/cooling statement, stormwater/wastewater, traffic, environmental triggers, objections/appeals, decision date, conditions, and next-stage building-plan requirements.

Known high-yield example pattern: in 2026, Cape Town MPT/trade coverage reported approval of land-use applications for two proposed hyperscale datacenters at **King Air Industria near Cape Town International Airport** associated in reports with Equinix. Treat municipal MPT records as Grade **A**; trade reports such as GroundUp/Business Day/News24/IOL are **B** leads until the MPT agenda/report and decision are opened.

### 1.2 Environmental authorisation and EIA records

Datacenters may trigger environmental review through land transformation, water, listed activities, diesel storage, backup generation, fuel handling, roads/services, or sensitive-site impacts rather than a "datacenter" category.

- **DFFE Environmental Impact Assessment / Environmental Authorisation pages**: https://www.dffe.gov.za/
- **National Environmental Authorisation System (NEAS)**: https://neas.environment.gov.za/dea_neas/
- **DFFE Environmental GIS (EGIS)**: https://www.dffe.gov.za/egis
- Provincial environmental departments: Western Cape DEA&DP, Gauteng Department of Agriculture, Rural Development and Environment, KwaZulu-Natal EDTEA, Eastern Cape DEDEAT, Free State DESTEA, Mpumalanga DARDLEA, Limpopo LEDET, North West DEDECT, Northern Cape DENC.
- Environmental Assessment Practitioner public-participation pages are useful **B+ leads** when they host Basic Assessment Reports, EIA reports, specialist studies, and authorisation letters. Grade them **A** only when the document is a signed government authorisation or official municipal/government-hosted file.

Environmental query templates:

```text
"data centre" "environmental authorisation" "South Africa"
"data center" "Basic Assessment Report" "South Africa"
"data centre" "NEMA" "EIA"
"data centre" "diesel" "environmental authorisation"
"data centre" "public participation" "Basic Assessment"
site:dffe.gov.za "data centre"
site:westerncape.gov.za "data centre" "environmental authorisation"
site:gauteng.gov.za "data centre" "environmental authorisation"
site:kznedtea.gov.za "data centre"
```

Extract: DFFE/provincial reference number, listed activities, project proponent, coordinates/erf, diesel storage volumes, generator count/rating, water source, wastewater plan, biodiversity constraints, mitigation commitments, appeal status, and whether the authorisation is for new build, expansion, or rectification.

### 1.3 Power, grid, wheeling, and private generation

- **Eskom main site**: https://www.eskom.co.za/
- **Eskom Data Portal**: https://www.eskom.co.za/dataportal/
- **Eskom company/network context**: https://www.eskom.co.za/about-eskom/company-information/
- **Eskom Transmission Development Plan PDFs**: search Eskom for `Transmission Development Plan` / `TDP`; useful for substation and regional capacity context, not a datacenter list.
- **NERSA electricity overview**: https://www.nersa.org.za/electricity/overview
- **NERSA notices/media statements/files**: https://www.nersa.org.za/ ; search for generation registrations, licences, wheeling/open access, embedded generation, and tariff determinations.
- Municipal electricity departments are critical in metros: City Power Johannesburg, Cape Town Electricity Generation and Distribution, eThekwini Electricity, Ekurhuleni Energy, Tshwane electricity pages.

Power-query templates:

```text
"{operator}" "Eskom" "data centre"
"{project}" "Eskom" "MVA"
"{project}" "substation" "data centre"
"{project}" "wheeling" "data centre"
"{operator}" "NERSA" "generation registration"
"{operator}" "solar" "data centre" "NERSA"
"data centre" "132kV" "South Africa"
"data centre" "88kV" "South Africa"
"data centre" "MVA" "Cape Town"
"data centre" "MVA" "Johannesburg"
site:eskom.co.za "data centre"
site:nersa.org.za "data centre"
site:nersa.org.za "{operator}" "generation"
site:capetown.gov.za "data centre" "electricity"
site:joburg.org.za "data centre" "electricity"
```

Grade **A** when a NERSA decision/registration, Eskom document, municipal electricity report, tariff/connection record, or official tender names the project/operator. Grade **B** when a renewable-power press release says a project will supply a cloud region but the NERSA/Eskom evidence has not been opened.

### 1.4 Telecoms/regulator evidence: ICASA and related records

- **ICASA mandate**: https://www.icasa.org.za/pages/our-mandate
- **ICASA telecommunications page**: https://www.icasa.org.za/pages/telecommunications
- **ICASA public consultations and uploads**: https://www.icasa.org.za/
- ICASA regulates electronic communications, postal services, broadcasting, and spectrum. It can identify telecom licensees, passive infrastructure/right-of-way disputes, fibre deployment, and rapid-deployment regulations, but it is **not** a complete datacenter register.
- The 2026 Draft Rapid Deployment Regulations consultation is a useful telecom infrastructure lead. Submissions mention GIS data on passive infrastructure location/capacity/ownership; treat consultation documents as Grade **A** for regulatory context and Grade **B** for operator claims unless backed by filings.

ICASA query templates:

```text
site:icasa.org.za "data centre"
site:icasa.org.za "data center"
site:icasa.org.za "rapid deployment" "data centre"
site:icasa.org.za "GIS" "passive physical infrastructure"
site:icasa.org.za "{operator}" "Electronic Communications Service"
site:icasa.org.za "{operator}" "Electronic Communications Network Service"
```

Use ICASA to pivot to fibre/network providers around datacenter campuses: Openserve/Telkom, DFA, Liquid, Vodacom Business, MTN, Frogfoot, Vumatel/Dark Fibre Africa, Seacom, WIOCC/OADC.

---

## 2. Official cloud-region pages as metro seeds

Cloud region evidence is Grade **A** for region existence and geography, but **not** exact facility evidence.

| Provider | Official source | South Africa signal | Enumeration use |
|---|---|---|---|
| AWS | AWS Africa page https://aws.amazon.com/local/africa/ ; AWS Cape Town page https://aws.amazon.com/local/africa/cape-town/ ; AWS launch blog https://aws.amazon.com/blogs/aws/now-open-aws-africa-cape-town-region/ ; AWS global infrastructure https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | Africa (Cape Town), API `af-south-1`, launched 2020 | Seed Cape Town/Western Cape searches for Amazon Data Services/AWS, power procurement, land-use records, substations, renewable wheeling. |
| Microsoft Azure | Azure regions list https://learn.microsoft.com/en-us/azure/reliability/regions-list ; Azure geographies https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies ; paired regions https://learn.microsoft.com/en-us/azure/reliability/regions-paired | South Africa North (Johannesburg); South Africa West (Cape Town) appears as paired/restricted-access region in official docs | Seed Johannesburg/Gauteng and Cape Town/Western Cape; verify exact sites via Teraco/BCX/NTT/operator/planning evidence, not Azure page alone. |
| Google Cloud | Cloud locations https://cloud.google.com/about/locations ; Compute regions/zones https://docs.cloud.google.com/compute/docs/regions-zones ; Johannesburg launch blog https://cloud.google.com/blog/products/infrastructure/heita-south-africa-new-cloud-region | `africa-south1` Johannesburg with zones `a/b/c` | Seed Johannesburg/Gauteng searches; cross-check with hyperscale campuses and environmental/power records. |
| Oracle OCI | Johannesburg launch https://www.oracle.com/news/announcement/oracle-cloud-johannesburg-region-2022-01-19/ ; OCI release note https://docs.oracle.com/iaas/releasenotes/changes/8b70bb98-9542-4dae-92d9-8d3f05cc8417/index.htm ; region page https://www.oracle.com/za/cloud/cloud-regions/johannesburg/ | South Africa Central (Johannesburg), `af-johannesburg-1`, region key `JNB` | Seed Johannesburg/Gauteng, enterprise colo, and Oracle partner/operator searches. |
| Huawei Cloud | Huawei official 2018 South Africa announcement https://www.huawei.com/en/news/2018/11/huawei-cloud-south-africa-connected-intelligent ; Huawei Cloud global infrastructure https://www.huaweicloud.com/intl/en-us/ | South Africa region announced for service availability from end-2018; later official Huawei Cloud local updates | Seed Johannesburg/Gauteng and operator/partner searches; exact sites require independent confirmation. |
| Alibaba Cloud / BCX | Use Alibaba official region docs if available plus BCX/Telkom official pages; trade reports say BCX launched/hosted local Alibaba region | South Africa/Cape Town lead, but official public detail varies | Treat as **B** until verified by Alibaba/BCX official region or facility page. |

Cloud pivot queries:

```text
"Amazon Data Services South Africa" "data centre"
"AWS" "Cape Town" "data centre" "Eskom"
"Microsoft" "South Africa North" "data centre"
"Google Cloud" "africa-south1" "Johannesburg" "data centre"
"Oracle" "af-johannesburg-1" "data centre"
"Huawei Cloud" "South Africa region" "data centre"
"Alibaba Cloud" "South Africa" "BCX" "data centre"
```

---

## 3. Official colo/operator seed list

Operator pages are Grade **A** for a facility/campus claim and broad city/metro presence. Exact address, permit status, capacity, and expansion state still need municipal/environmental/power confirmation.

| Operator | Official URL | South Africa footprint signal | High-yield divisions/municipalities |
|---|---|---|---|
| Teraco / Digital Realty | https://www.teraco.co.za/ ; locations https://www.teraco.co.za/data-centre-locations/ | Official locations in Johannesburg, Cape Town, Durban; NAPAfrica/ACX ecosystem | Gauteng: Ekurhuleni/Isando/Bredell, Johannesburg area; Western Cape: Cape Town/Rondebosch/Brackenfell; KwaZulu-Natal: Durban/Riverhorse/Umhlanga area |
| Africa Data Centres / Cassava / Liquid | https://www.africadatacentres.com/ ; Samrand page https://www.africadatacentres.com/samrand-2/ ; Liquid DC page https://liquid.tech/data-centres/ | ADC/Liquid carrier-neutral data centres, including Johannesburg/Samrand and Cape Town; Cassava official expansion news | Gauteng: Midrand/Samrand/Centurion; Western Cape: Cape Town; also operator group links to Liquid fibre |
| Liquid Intelligent Technologies | https://liquid.tech/ ; https://liquid.tech/data-centres/ | Fibre + data-centre provider, part of Cassava ecosystem | Gauteng/Midrand, Cape Town, fibre routes nationally |
| BCX / Telkom | https://www.bcx.co.za/solutions/services/managed-infrastructure-and-cloud-services/ | BCX says it operates from its own 12 data centres; Telkom/Openserve links are important | Gauteng: Midrand/Centurion/Johannesburg; Western Cape: Bellville/Century City; KZN; confirm with official pages/filings |
| NTT DATA / Dimension Data / Internet Solutions | https://services.global.ntt/en-us/services-and-products/global-data-centers/global-locations/emea/south-africa-data-centers | Official NTT page lists South African data centres in Gauteng, KZN, Western Cape, Eastern Cape, and Free State: Parklands, Bryanston, Umhlanga, Bloemfontein, East London, Port Elizabeth/Gqeberha, Bree, Belville | Gauteng, KwaZulu-Natal, Western Cape, Eastern Cape, Free State |
| Equinix | South Africa page https://www.equinix.com/data-centers/europe-colocation/south-africa-colocation ; Johannesburg page https://www.equinix.com/data-centers/europe-colocation/south-africa-colocation/johannesburg-data-centers ; JN1 https://www.equinix.com/data-centers/europe-colocation/south-africa-colocation/johannesburg-data-centers/jn1 | Official JN1 in Isando/Germiston; 2026 Cape Town hyperscale proposal appears in municipal/trade records | Gauteng: Ekurhuleni/Isando/Germiston; Western Cape: Cape Town/King Air Industria lead |
| Vantage Data Centers | Johannesburg I https://vantage-dc.com/data-center-locations/emea/johannesburg-i-south-africa/ ; Johannesburg II https://vantage-dc.com/data-center-locations/emea/johannesburg-ii-south-africa/ | Official Waterfall City/Johannesburg campuses; JNB1 fully developed signal up to 120 MW critical load | Gauteng: Midrand/Waterfall City, City of Johannesburg/City of Ekurhuleni boundary checks |
| Open Access Data Centres / WIOCC | https://www.openaccessdc.net/ and WIOCC/Cassava announcements | Edge/core datacenter footprint in South Africa; trade reports say OADC buying NTT SA facilities in 2026 | Johannesburg, Durban, Cape Town, plus NTT facility cities if transaction confirmed |
| Digital Parks Africa | https://www.dpa.host/ | Official carrier-neutral facilities, flagship Samrand, plus Cape Town/Pretoria/Johannesburg service footprint | Gauteng: Samrand/Centurion/Pretoria/Johannesburg; Western Cape: Cape Town |
| xneelo | https://xneelo.co.za/ | Hosting provider with South African infrastructure; useful for smaller enterprise DCs | Western Cape and Gauteng; verify exact sites with official technical pages and local records |

Operator pivot workflow:

1. Record official facility/campus name, city, address if published, capacity if published, and certifications.
2. Search exact facility/campus name plus municipality and `MPT`, `building plan`, `environmental authorisation`, `substation`, `diesel`, `Eskom`, `NERSA`.
3. Search legal entity/SPV names in CIPC/BizPortal and tender records when needed; use operator parent names and prior brands (Dimension Data, Internet Solutions, Telkom/BCX, Liquid, ADC, Teraco/Digital Realty).
4. Use Baxtel/DataCenterMap/Datacenters.com only as **C/B leads**; do not accept their address/capacity without operator or government corroboration.

---

## 4. Province and municipality enumeration strategy

### 4.1 National workflow

For each repo division/province:

1. Identify the metro/local municipalities in the division. For a province-wide target, start with metros and known industrial/logistics corridors.
2. Search municipal MPT/council agenda pages and planning portals using `data centre`, `data center`, `datacentre`, `data hall`, `server hall`, `hyperscale`, `colocation`, `substation`, `diesel`, and operator names.
3. Search environmental public-participation/authorisation records by operator, erf/farm/industrial park, and province.
4. Search Eskom/NERSA/municipal electricity evidence for MVA/MW, substations, wheeling, backup/self-generation, and grid constraints.
5. Cross-check official cloud and operator seed lists for facility names and metros.
6. Use trade press (Data Center Dynamics, MyBroadband, TechCentral, ITWeb, Engineering News, GroundUp, News24, Business Day, IOL) to identify leads; then open primary records.
7. Record uncertainty explicitly: announced/MOA, land-use approved, building-plan approved, environmental authorised, under construction, operational, expansion.

### 4.2 High-yield provincial clusters

- **Gauteng**: highest-yield province. Focus City of Johannesburg, Ekurhuleni, Tshwane, Midvaal/Emfuleni, Mogale City, and Midrand/Waterfall/Samrand/Isando/Bredell/Bryanston/Parklands/Centurion. Operators: Teraco, Africa Data Centres/Liquid, Equinix JN1, Vantage JNB1/JNB2, NTT/Dimension Data, BCX/Telkom, Digital Parks Africa. Cloud seeds: Azure South Africa North, Google `africa-south1`, OCI `af-johannesburg-1`, Huawei South Africa.
- **Western Cape**: focus City of Cape Town, Stellenbosch, Drakenstein, Saldanha Bay, and Cape Winelands industrial corridors. Operators/seeds: AWS Cape Town region, Azure South Africa West, Teraco CT, Africa Data Centres Cape Town, NTT Belville/Bree, BCX/Telkom Bellville/Century City, Equinix King Air Industria proposal. Use Cape Town MPT and building-plan sources heavily.
- **KwaZulu-Natal**: focus eThekwini/Durban, Umhlanga, Riverhorse Valley, Amanzimtoti/Lovu/Ocean View leads, Richards Bay and Dube TradePort. Operators/seeds: Teraco Durban, NTT Umhlanga, Liquid/ADC, eThekwini 2026 Korean AI datacenter MOA lead. Treat MOAs as **C** until land, environmental, power, or planning records appear.
- **Eastern Cape**: focus Nelson Mandela Bay/Gqeberha and Buffalo City/East London. Operators/seeds: NTT East London and Port Elizabeth/Gqeberha official listings; smaller enterprise/government DCs likely.
- **Free State**: focus Mangaung/Bloemfontein. Operator seed: NTT Bloemfontein official listing; government/enterprise DCs more likely than hyperscale.
- **Northern Cape**: low direct colocation density but high renewable-power/wheeling relevance. Search Amazon/AWS renewable procurement, solar PV, NERSA registrations, Eskom grid, and data-centre offtake links; do not classify renewable sites as datacenters unless a facility is present.
- **Mpumalanga**: search power-station redevelopment, high-voltage substations, industrial parks, and renewable/hydrogen corridors; likely power-led future proposals rather than current colo.
- **Limpopo**: search Musina/Makhado SEZ, Polokwane, mining/industrial power users, and fibre corridors; expect low recall from cloud/operator pages.
- **North West**: search Rustenburg, Bojanala, mining/industrial parks, renewable/offtake, and municipal planning; likely low direct DC density.

---

## 5. Query playbook

### 5.1 English and South African variants

```text
"{municipality}" "data centre"
"{municipality}" "data center"
"{municipality}" datacentre
"{municipality}" "hyperscale"
"{municipality}" "data hall"
"{municipality}" "server hall"
"{municipality}" "colocation"
"{municipality}" "co-location"
"{municipality}" "Municipal Planning Tribunal" "data centre"
"{municipality}" "land use application" "data centre"
"{municipality}" "rezoning" "data centre"
"{municipality}" "site development plan" "data centre"
"{municipality}" "building plan" "data centre"
"{municipality}" "data centre" "substation"
"{municipality}" "data centre" "MVA"
"{municipality}" "data centre" "MW"
```

### 5.2 Afrikaans/local government variants

Most official records are in English, but Afrikaans terms help in Western Cape/Northern Cape/local notices:

```text
"datasentrum"
"data sentrum"
"datacentrum"
"grondgebruik aansoek" "datasentrum"
"hersonering" "datasentrum"
"bouplan" "datasentrum"
"munisipale beplanningstribunaal" "datasentrum"
```

### 5.3 Document-focused searches

```text
filetype:pdf "data centre" "Municipal Planning Tribunal"
filetype:pdf "data center" "Municipal Planning Tribunal"
filetype:pdf "data centre" "Basic Assessment Report"
filetype:pdf "data centre" "environmental authorisation"
filetype:pdf "data centre" "site development plan"
filetype:pdf "data centre" "traffic impact assessment"
filetype:pdf "data centre" "noise impact assessment"
filetype:pdf "data centre" "air quality"
filetype:pdf "data centre" "diesel storage"
filetype:pdf "data centre" "Eskom"
```

### 5.4 Operator/company aliases

```text
"Amazon Data Services South Africa"
"Amazon Web Services South Africa" "data centre"
"Microsoft South Africa" "data centre"
"Google Cloud" "Johannesburg" "data centre"
"Oracle" "Johannesburg" "cloud region"
"Teraco" "Municipal Planning Tribunal"
"Africa Data Centres" "environmental authorisation"
"Liquid Intelligent Technologies" "data centre" "South Africa"
"BCX" "data centre" "South Africa"
"Telkom" "data centre" "South Africa"
"Dimension Data" "data centre" "South Africa"
"Internet Solutions" "data centre" "South Africa"
"NTT" "South Africa Data Centers"
"Equinix" "King Air Industria"
"Vantage" "Waterfall City" "data center"
"Digital Parks Africa" "Samrand"
```

---

## 6. Reliability and extraction rules

- **A**: municipal MPT/council/building-plan record; official signed environmental authorisation; Eskom/NERSA/municipal electricity document; ICASA consultation/regulatory document; official cloud-region page for region existence; official operator facility page for claimed facility existence.
- **B**: Data Center Dynamics, MyBroadband, TechCentral, ITWeb, Engineering News, GroundUp, News24, Business Day, IOL, company press releases hosted by parent companies, engineering-consultant project pages. Use as leads and corroboration, not as final proof where official records exist.
- **C**: DataCenterMap, Baxtel, Datacenters.com, LinkedIn, social media, petitions, marketing claims with no facility details, MOU/signing-ceremony articles, consultant speculation.

Do not over-read cloud regions. A cloud region in Cape Town/Johannesburg proves the provider has regional infrastructure and likely leased/built capacity, but exact buildings remain hidden unless confirmed by planning, operator, environmental, or power records.

Do not over-read power projects. A solar/wind/NERSA registration supplying a cloud provider is strong evidence of datacenter energy procurement, but the renewable plant itself is not a datacenter.

Minimum record fields for ZA expansion:

```text
country=ZA
province
municipality
place/precinct
facility_or_project_name
operator/developer/land_owner
source_grade
source_url
planning_reference
environmental_reference
power_reference_or_MVA_MW
cloud_or_colo_seed
status
evidence_notes
last_checked_date
```

---

## 7. Starter source list

Official/regulatory:

- City of Cape Town Planning Portal: https://www.capetown.gov.za/Work%20and%20business/Planning-portal
- City of Cape Town building-plan applications: https://www.capetown.gov.za/City-Connect/Apply/Planning-building-and-development/Building-plan-applications
- City of Cape Town MPT meeting details: https://web1.capetown.gov.za/web1/councilhubonline/mptmeetingdetail
- City of Johannesburg building-plan progress/eServices: https://eservices.joburg.org.za/pages/BuildingPlanProgress.aspx
- eThekwini Municipality: https://www.durban.gov.za/
- Eskom: https://www.eskom.co.za/
- Eskom Data Portal: https://www.eskom.co.za/dataportal/
- NERSA electricity overview: https://www.nersa.org.za/electricity/overview
- ICASA mandate: https://www.icasa.org.za/pages/our-mandate
- ICASA telecommunications: https://www.icasa.org.za/pages/telecommunications
- NEAS: https://neas.environment.gov.za/dea_neas/
- DFFE EGIS: https://www.dffe.gov.za/egis

Official cloud/operator:

- AWS Africa/Cape Town: https://aws.amazon.com/local/africa/ ; https://aws.amazon.com/local/africa/cape-town/ ; https://aws.amazon.com/blogs/aws/now-open-aws-africa-cape-town-region/
- Azure regions: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud locations / Johannesburg: https://cloud.google.com/about/locations ; https://docs.cloud.google.com/compute/docs/regions-zones ; https://cloud.google.com/blog/products/infrastructure/heita-south-africa-new-cloud-region
- Oracle Johannesburg: https://www.oracle.com/news/announcement/oracle-cloud-johannesburg-region-2022-01-19/ ; https://docs.oracle.com/iaas/releasenotes/changes/8b70bb98-9542-4dae-92d9-8d3f05cc8417/index.htm
- Huawei South Africa region announcement: https://www.huawei.com/en/news/2018/11/huawei-cloud-south-africa-connected-intelligent
- Teraco: https://www.teraco.co.za/ ; https://www.teraco.co.za/data-centre-locations/
- Africa Data Centres: https://www.africadatacentres.com/ ; https://www.africadatacentres.com/samrand-2/
- Liquid data centres: https://liquid.tech/data-centres/
- BCX managed infrastructure: https://www.bcx.co.za/solutions/services/managed-infrastructure-and-cloud-services/
- NTT DATA South Africa data centers: https://services.global.ntt/en-us/services-and-products/global-data-centers/global-locations/emea/south-africa-data-centers
- Equinix South Africa/Johannesburg/JN1: https://www.equinix.com/data-centers/europe-colocation/south-africa-colocation ; https://www.equinix.com/data-centers/europe-colocation/south-africa-colocation/johannesburg-data-centers ; https://www.equinix.com/data-centers/europe-colocation/south-africa-colocation/johannesburg-data-centers/jn1
- Vantage Johannesburg I/II: https://vantage-dc.com/data-center-locations/emea/johannesburg-i-south-africa/ ; https://vantage-dc.com/data-center-locations/emea/johannesburg-ii-south-africa/
- Digital Parks Africa: https://www.dpa.host/
