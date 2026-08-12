# ZA Explorer - Industry / Press / Vendor-Led Discovery for South Africa Datacentres

Date: 2026-08-12. Scope: how to enumerate South Africa (ZA) datacentre projects from industry/trade press, vendor/operator pages, municipal planning evidence, and province/district search patterns. Reliability grades: **A** = official/primary (operator facility page, cloud region docs, municipal planning/building/land-use record, environmental authorisation record, utility/power filing), **B** = strong secondary (DCD, MyBroadband, TechCentral, ITWeb, Daily Maverick/GroundUp, Business Day, W.Media, specialist property or legal notes), **C** = weak/aggregate (DataCenterMap, Baxtel, Cloudscene, DC Atlas, LinkedIn, conference pages, petitions/social posts).

---

## 0. South Africa-specific frame

- South Africa has no single public datacentre registry. Enumeration works by triangulating **operator pages**, **hyperscaler region pages**, **trade press**, **municipal land-use/building-plan systems**, **environmental/basic-assessment notices**, and **electricity/grid/renewable-power records**.
- The live and planned market is highly concentrated in **Gauteng** and the **Western Cape**. Priority clusters: **Johannesburg / Midrand / Isando / Bredell / Waterfall City / Samrand / Centurion / Pretoria**, **Cape Town / Rondebosch / Brackenfell / Diep River / King Air Industria / Airport Industria**, and **Durban / Riverhorse Valley / eThekwini south**. Secondary edge or telco sites appear in Bloemfontein, Gqeberha, East London, Klerksdorp, Polokwane, Nelspruit/Mbombela, Kimberley, and other metro/provincial nodes.
- South African sources usually use **data centre** and **datacentre**; US spelling **data center** is common in US vendor pages and DCD. Search all three. Also search **hyperscale**, **carrier-neutral**, **colocation**, **cloud region**, **server farm**, **AI data centre**, **data storage centre**, **technology hub**, **backup generators**, **diesel generators**, **substation**, **MVA**, **MW**, **critical IT load**, **rezoning**, **consent use**, **land-use application**, **site development plan**, and **Municipal Planning Tribunal**.
- Land-use verification is municipal under SPLUMA and municipal planning by-laws. For the biggest projects, planning evidence may be a **rezoning / subdivision / consolidation / consent-use / site-development-plan** record rather than a building permit visible in a public search page.
- Do not treat cloud-region pages as physical facility addresses. AWS, Azure, Google Cloud, and OCI prove metro/region presence; physical enumeration still needs operator/permit/press evidence.

Core national query set:

```text
South Africa ("data centre" OR "data center" OR datacentre) ("MW" OR "MVA" OR "critical IT load")
South Africa ("hyperscale" OR "colocation" OR "carrier-neutral") ("Johannesburg" OR "Cape Town" OR "Durban")
"South Africa" "data centre" ("rezoning" OR "land use application" OR "Municipal Planning Tribunal")
"South Africa" "data centre" ("environmental authorisation" OR "basic assessment" OR "scoping report")
"South Africa" "data centre" ("substation" OR "backup generators" OR "diesel generators" OR "PPA")
```

Afrikaans is rarely needed for commercial DC discovery, but can help with notices in rural municipalities:

```text
"datasentrum" "Suid-Afrika" "munisipaliteit"
"datasentrum" ("Kaapstad" OR "Johannesburg" OR "Pretoria")
"datasentrum" ("hersonering" OR "grondgebruik")
```

---

## 1. High-signal trade press and industry sources

Use these for discovery of project names, developer SPVs, location hints, MW claims, construction timing, and opposition/appeal context. Then verify through operator pages, municipal records, or environmental filings.

| Source | URL / route | Use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD) | `https://www.datacenterdynamics.com/en/news/?tag=south-africa`, tags `johannesburg`, `cape-town`, `teraco`, `vantage`, `africa-data-centres`, `equinix` | Best global DC trade feed for South Africa: Teraco expansions, Vantage Waterfall/Isando, Equinix JN1/Cape Town, Africa Data Centres Cape Town, Google/Azure/AWS/OCI regions. | B |
| MyBroadband | `https://mybroadband.co.za/news/cloud-hosting/` and site search | Strong local tech/business coverage; useful for SA-specific operator estate, water/power controversy, Microsoft/AWS/Google/Oracle cloud items, and local capacity claims. | B |
| TechCentral | `https://techcentral.co.za/` search `data centre` | Good on hyperscaler investment, legal challenges, market context, and South African policy concerns. | B |
| ITWeb | `https://www.itweb.co.za/` search `data centre` | Strong local enterprise/telecom coverage; useful for operator launches, expansions, and government/municipal ICT items. | B |
| Daily Maverick / GroundUp | `https://www.dailymaverick.co.za/`, `https://groundup.org.za/` | Especially useful for Cape Town land-use approvals, objections, environmental/power/water concerns, and tribunal dates. | B |
| W.Media / Data Centre Magazine / Capacity Media / Dgtl Infra | site-scoped searches | Useful APAC/EMEA industry feeds for financing, vendor announcements, and operator lists. Verify location and capacity. | B/C |
| Local business press | Business Day, Engineering News, Polity, IOL, Moneyweb, News24, Creamer Media | Good early leads on Cape Town/Gauteng land use, Durban AI DC proposals, renewable PPAs, and investment commitments. | B/C |
| Legal/environmental consultants | Pinsent Masons Out-Law, Clyde & Co, local EAP PDFs such as Enviroworks | Good for regulatory pathways, environmental notices, and site descriptions. | B for analysis; A when hosting actual EIA/BID notices |
| Aggregators/directories | DataCenterMap, Baxtel, Cloudscene, DC Atlas, datacenters.com, PeeringDB, Uptime Institute | Useful for legacy telco/edge facilities and addresses. Grade C unless matched by operator page or certification record. Uptime certificates are B/A for certified facility identity. | C/B |

Trade-press scoped searches:

```text
site:datacenterdynamics.com/en/news/ "South Africa" "data center" "MW"
site:datacenterdynamics.com/en/news/ "Teraco" "Johannesburg" "data center"
site:datacenterdynamics.com/en/news/ "Vantage" "Waterfall City" "data center"
site:datacenterdynamics.com/en/news/ "Equinix" "Cape Town" "data center"
site:mybroadband.co.za "data centre" "South Africa" "MW"
site:techcentral.co.za "data centre" "Cape Town" "Equinix"
site:itweb.co.za "data centre" "Teraco" OR "Africa Data Centres"
site:dailymaverick.co.za "data centres" "Cape Town" "Municipal Planning Tribunal"
site:w.media "South Africa" "data center" "Cape Town"
```

Stage language to capture:

- `announced`, `MoU`, `engagement`, `considering`, `plans` = lead only, usually **C/B-**.
- `land-use application`, `rezoning`, `tribunal approval`, `environmental authorisation`, `building plans submitted` = permitting stage, **A if municipal/EIA record**.
- `breaks ground`, `construction starts`, `site preparation`, `expansion under way` = construction, **B unless operator/municipality confirms**.
- `opened`, `launched`, `goes live`, `capacity now live`, `facility page` = operational, **A/B depending on source**.

---

## 2. Vendor/operator sweep

Official operator pages are **A for owned marketed locations** and **B for headline MW/buildout capacity** unless the page gives facility-level technical specs or is backed by permit/investor filings.

| Operator / developer | Priority geographies | Official / useful URL | Notes |
|---|---|---|---|
| Teraco, a Digital Realty company | Gauteng: Isando, Bredell, Ekurhuleni/Johannesburg metro edge; Western Cape: Rondebosch, Brackenfell; KwaZulu-Natal: Riverhorse Valley/Durban | `https://www.teraco.co.za/data-centre-locations/`, Johannesburg `https://www.teraco.co.za/data-centre-locations/johannesburg/`, Cape Town `https://www.teraco.co.za/data-centre-locations/cape-town/`, Durban `https://www.teraco.co.za/data-centre-locations/durban/` | Primary anchor operator. Teraco pages list Johannesburg, Cape Town, Durban and named JB/CT/DB facilities. DCD and Teraco news track CT1/CT2/JB expansions and renewable PPAs. |
| Africa Data Centres / Cassava Technologies | Midrand/Samrand Johannesburg, Cape Town, possible other SA sites inherited/edge | `https://www.africadatacentres.com/`, Midrand `https://www.africadatacentres.com/midrand/`, Samrand `https://www.africadatacentres.com/samrand-2/`, Cape Town category `https://www.africadatacentres.com/category/capetown/` | Official pages/news confirm Johannesburg and Cape Town estate; ADC Cape Town additional 6MW live in 2024 and second Cape Town facility were reported by official/news channels. |
| Vantage Data Centers | Waterfall City/Midrand and Isando/Ekurhuleni/Johannesburg region | `https://vantage-dc.com/data-center-locations/emea/johannesburg-i-south-africa/` | Official JNB1 page states Waterfall City campus and full buildout scale; DCD reported Attacq JV Phase II and new Johannesburg campus activity. Verify exact municipal jurisdiction: Waterfall/Midrand may map to City of Johannesburg; Isando maps to Ekurhuleni. |
| Equinix | JN1 Germiston/Isando, Gauteng; Cape Town King Air Industria proposal | JN1 `https://www.equinix.com/data-centers/europe-colocation/south-africa-colocation/johannesburg-data-centers/jn1`, Equinix newsroom `https://newsroom.equinix.com/2024-10-24-Equinix-opens-its-first-data-center-in-Johannesburg-enhancing-digital-infrastructure-and-connectivity-in-the-region` | Official page gives JN1 address at 308 Brollo Road, Germiston/Isando, Gauteng. Cape Town proposal needs City of Cape Town DAMS/MPT and press verification; July 2026 tribunal approval was widely reported. |
| Open Access Data Centres (OADC) / WIOCC | Johannesburg Parklands, Bryanston, Isando; Cape Town; Bloemfontein and edge network | `https://openaccessdc.net/`, Parklands `https://openaccessdc.net/parklands`, Bryanston `https://www.openaccessdc.net/bryanston`, Isando `https://openaccessdc.net/isando` | Official pages confirm Johannesburg core sites and South African footprint; OADC announced/acquired seven NTT SA data centres. Use site pages plus DataCenterMap/Baxtel cautiously for edge nodes. |
| NTT DATA / former Dimension Data / Internet Solutions estate | Johannesburg, Cape Town, Durban, regional edge | `https://services.global.ntt/en/services/data-centers` plus OADC acquisition news | Some former NTT/IS facilities may now be OADC. Verify current owner before counting. |
| Digital Parks Africa | Samrand/Centurion/Midrand region | `https://www.digitalparksafrica.com/` | Important Gauteng specialist operator; verify facility pages and local press. |
| BCX / Telkom | Centurion, Johannesburg, Cape Town, Durban, telco nodes | `https://www.bcx.co.za/` | Enterprise/telco estate; many facilities are private or legacy. Use Uptime certificates, tenders, and operator disclosures. |
| MTN / Vodacom | Roodepoort/Fairland/Johannesburg, Midrand, Cape Town, Durban, regional remote hubs | `https://www.mtn.com/`, `https://www.vodacom.co.za/` | Telco DCs and remote hubs appear in Uptime certificates and directories. Distinguish commercial colocation from internal network facilities. |
| xneelo / Hetzner SA, RSAWEB, Dimension Data legacy hosting | Cape Town and Johannesburg | `https://xneelo.co.za/`, `https://www.rsaweb.co.za/` | Smaller hosting/enterprise DCs; usually no public MW. Use as operational facility leads. |
| Microsoft / AWS / Google / Oracle | Cloud regions: Cape Town and Johannesburg | official cloud pages below | Region pages are primary for cloud-region existence, not exact campus/facility identity. |

Vendor query templates:

```text
"{operator}" "South Africa" ("data centre" OR "data center") ("Johannesburg" OR "Cape Town" OR "Durban")
site:{operator-domain} "South Africa" "data centre" "{city}"
"{operator}" "{municipality}" ("MW" OR "MVA" OR "critical IT load" OR "racks")
"{operator}" "{township/suburb}" ("data centre" OR "data center")
"{operator}" "rezoning" "data centre"
"{operator}" "environmental authorisation" "data centre"
"{operator}" "backup generators" "data centre" "South Africa"
```

---

## 3. Official hyperscale cloud region pages

Use cloud-provider pages as **A for region presence**. They rarely identify owned versus leased buildings or exact addresses.

| Provider | Official URL | South Africa signal |
|---|---|---|
| AWS | Region docs `https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html`; launch blog `https://aws.amazon.com/blogs/aws/now-open-aws-africa-cape-town-region/` | `af-south-1` Africa (Cape Town), 3 Availability Zones. Launched April 2020. |
| Microsoft Azure | `https://learn.microsoft.com/en-us/azure/reliability/regions-list`; South Africa AZ release `https://news.microsoft.com/en-xm/2021/10/13/azure-availability-zones-to-enable-competitiveness-of-sa-businesses/` | South Africa North = Johannesburg with AZ support; South Africa West = Cape Town paired/restricted access on current region list. |
| Google Cloud | Locations `https://cloud.google.com/about/locations`; compute regions `https://docs.cloud.google.com/compute/docs/regions-zones`; Cloud Run locations `https://docs.cloud.google.com/run/docs/locations` | `africa-south1` Johannesburg appears in official product/location docs. DCD reported first African Google Cloud region launch in Johannesburg. |
| Oracle Cloud Infrastructure | Public regions `https://www.oracle.com/cloud/public-cloud-regions/`; Johannesburg launch `https://www.oracle.com/news/announcement/oracle-cloud-johannesburg-region-2022-01-19/`; release note `https://docs.oracle.com/iaas/releasenotes/changes/8b70bb98-9542-4dae-92d9-8d3f05cc8417/index.htm` | South Africa Central / Johannesburg region, identifier `af-johannesburg-1`, region key `JNB`, launched January 2022. |
| Huawei Cloud / Alibaba Cloud / local cloud platforms | provider pages + BCX/Telkom press | Usually partner/colo-backed. Use for demand signal, not facility owner unless facility is disclosed. |

Hyperscaler pivot queries:

```text
"AWS" "Cape Town" "data centre" "availability zones"
"Microsoft" "South Africa North" "Johannesburg" "data centre"
"Google Cloud" "africa-south1" "Johannesburg" "data center"
"Oracle" "af-johannesburg-1" "Johannesburg" "cloud region"
"{cloud provider}" "{operator}" "South Africa" "data centre"
```

---

## 4. Municipal planning and permitting workflow

### 4.1 National/legal frame

South African land-use control is municipal. For datacentre enumeration, search by **province -> district/metropolitan municipality -> local municipality/metro planning route -> suburb/erf/operator**.

Primary record types to capture:

- municipality and portal/manual route;
- application number/reference, erf/portion/farm number, township/suburb, street address;
- applicant/owner/developer/SPV and planning consultant;
- application type: rezoning, subdivision, consolidation, consent use, township establishment, site development plan, building plan, departure, environmental authorisation/basic assessment;
- decision body/status: Municipal Planning Tribunal, authorised official, appeal authority, council committee, approved/refused/appealed;
- capacity evidence: MW/critical IT load, MVA/grid connection, number of data halls, gross floor area, backup generator count, cooling/water requirement, substation rating, phasing.

Core planning queries:

```text
site:{municipal-domain} "data centre" "Municipal Planning Tribunal"
site:{municipal-domain} "data center" "Municipal Planning Tribunal"
site:{municipal-domain} "datacentre" "land use"
site:{municipal-domain} "hyperscale" "rezoning"
site:{municipal-domain} "data centre" "rezoning"
site:{municipal-domain} "data centre" "site development plan"
site:{municipal-domain} "data centre" "building plan"
site:{municipal-domain} "backup generators" "data centre"
```

Environmental and power queries:

```text
"data centre" "environmental authorisation" "{province}"
"data centre" "basic assessment report" "{municipality}"
"data storage centre" "environmental authorisation" Gauteng
"data centre" "diesel generators" "basic assessment"
site:enviroworks.co.za "data centre" "Gauteng"
site:sahris.sahra.org.za "data centre" "{province}"
site:nersa.org.za "data centre" "generation"
site:eskom.co.za "data centre" "MVA" OR "substation"
"{operator}" "PPA" "South Africa" "data centre"
```

### 4.2 High-value municipal portals/routes

| Municipality / route | URL / portal | How to use | Grade |
|---|---|---|---|
| City of Cape Town Planning Portal / DAMS | Planning portal `https://www.capetown.gov.za/Work%20and%20business/Planning-portal`; DAMS `https://www.capetown.gov.za/work%20and%20business/planning-portal/online-planning-and-building-resources/dams`; e-services `https://eservices.capetown.gov.za/irj/portal/` | Search DAMS, council online MPT reports, and City document centre by `data centre`, `Equinix`, `King Air`, `Airport Industria`, `Brackenfell`, `Rondebosch`, `Diep River`, erf numbers. | A |
| City of Johannesburg Development Planning / eServices | Land-use forms `https://www.joburg.org.za/departments_/Pages/City%20directorates%20including%20departmental%20sub-directorates/Development%20Planning/Land-Use-Management-Forms.aspx`; eServices maps/building plans `https://eservices.joburg.org.za/onlinemaps` | Search Joburg site/PDF notices for Midrand, Waterfall, Chartwell, Roodepoort, Bryanston, Randburg, Parktown, Rosebank. Use eServices maps/building-plan search when property details are known. | A/B |
| City of Ekurhuleni City Planning | `https://www.ekurhuleni.gov.za/departments/1-2/city-planning/`; digital building-plan notice `https://www.ekurhuleni.gov.za/press-releases/service-delivery/digital-submission-of-building-plans-in-ekurhuleni/` | Critical for Isando, Germiston, Bredell, Kempton Park, Jet Park, OR Tambo corridor, Vantage/Equinix/Teraco sites. Search city PDFs/budget/IDP plus local planning notices. | A/B |
| City of Tshwane Land Use / NAPS | Land Use Management `https://www.tshwane.gov.za/?page_id=15464`; NAPS launch `https://www.tshwane.gov.za/?p=82100` | Check Centurion, Samrand, Pretoria, Menlyn, Rosslyn, Silverton, and government/BCX/Telkom facilities. NAPS began online building-plan submissions in Dec 2024. | A/B |
| eThekwini / Durban Development Planning, Environment and Management | `https://www.durban.gov.za/page/development-planning-environment-and-management`; LUMS adverts `https://www.durban.gov.za/page/lums-adverts`; media `https://www.durban.gov.za/pages/government/media` | Search LUMS adverts, council decisions, electricity annual reports, and press statements for Riverhorse Valley, Umhlanga, Cornubia, Dube TradePort, Shongweni, south Durban AI DC proposals. | A/B |
| Nelson Mandela Bay / Buffalo City / Mangaung / other metros | municipal planning pages, IDP/budget PDFs, local notices | Mostly edge/telco/enterprise leads. Search building-plan and tender pages plus Uptime/DataCenterMap. | B/C unless direct municipal record found |

---

## 5. Province and district/metro enumeration matrix

The ZA manifest uses **district/metropolitan municipalities (GeoNames admin2)**. For every division, run the universal templates with: province, district/metro name, major towns, local municipalities inside the district, operator names, and common suburbs/industrial nodes.

### 5.1 Gauteng - highest priority

Known concentration: Johannesburg, Ekurhuleni, Tshwane, Midrand/Samrand/Centurion, Isando/Germiston/Bredell, Waterfall City, Roodepoort/Fairland, Bryanston/Parklands.

| Manifest division | Query approach |
|---|---|
| City of Johannesburg Metropolitan Municipality | Search `Johannesburg`, `Midrand`, `Waterfall City`, `Bryanston`, `Parklands`, `Roodepoort`, `Randburg`, `Chartwell`, `Rosebank`, `Sandton` with Vantage, OADC, Microsoft, Google, BCX, MTN, xneelo. Check Joburg Development Planning PDFs, eServices Online Maps/building plans, and council/media statements. |
| Ekurhuleni Metropolitan Municipality | Search `Ekurhuleni`, `Isando`, `Germiston`, `Bredell`, `Kempton Park`, `Jet Park`, `OR Tambo`, `Brollo Road` with Teraco, Equinix JN1, Vantage JNB2, OADC Isando. Ekurhuleni is critical because many "Johannesburg" facilities are actually in Ekurhuleni. |
| City of Tshwane Metropolitan Municipality | Search `Tshwane`, `Pretoria`, `Centurion`, `Samrand`, `Menlyn`, `Rosslyn`, `Silverton`, `Highveld`, `Route 21` with BCX, Telkom, Digital Parks Africa, Teraco, Africa Data Centres. Use Tshwane NAPS/Land Use pages and local notices. |
| Sedibeng District Municipality | Lower probability; search `Vereeniging`, `Vanderbijlpark`, `Meyerton`, `Sasolburg` with `data centre`, `server farm`, `industrial park`, `substation`, `renewable PPA`. Verify no-project carefully. |
| West Rand District Municipality | Search `Krugersdorp`, `Mogale City`, `Randfontein`, `Westonaria`, `Carletonville`, plus telco/operator edge terms. |

Gauteng templates:

```text
"Gauteng" "data centre" ("Midrand" OR "Isando" OR "Centurion" OR "Waterfall City")
"City of Johannesburg" "data centre" "land use"
site:joburg.org.za "data centre" "Midrand"
site:ekurhuleni.gov.za "data centre" "Isando" OR "Bredell"
site:tshwane.gov.za "data centre" "Centurion" OR "Samrand"
"Brollo Road" "data center" "Germiston"
"Waterfall City" "data center" "Vantage"
```

### 5.2 Western Cape - highest priority

Known concentration: Cape Town, Rondebosch, Brackenfell, Diep River, Airport Industria/King Air Industria, Bellville, Foreshore, Cape Town cloud regions.

| Manifest division | Query approach |
|---|---|
| City of Cape Town | Highest priority after Gauteng. Search DAMS/MPT/council online for `data centre`, `Equinix`, `King Air Industria`, `Pallotti`, `Airport Industria`, `Brackenfell`, `Rondebosch`, `Diep River`, `De Waal Road`, `Foreshore`, `AWS`, `Teraco`, `Africa Data Centres`, `OADC`, `Vodacom`, `xneelo`. |
| Cape Winelands District Municipality | Search Stellenbosch, Paarl, Worcester, Wellington, Klapmuts, Techno Park. Expect university/HPC/enterprise leads, not hyperscale. Check local municipalities if a lead appears. |
| West Coast District Municipality | Search Saldanha Bay, Atlantis, Malmesbury, Vredenburg, renewables/freeport/industrial park terms. Possible future energy-driven leads; verify with Saldanha Bay/Swartland planning. |
| Overberg District Municipality | Search Hermanus, Grabouw, Caledon, Bredasdorp; likely no commercial projects. |
| Eden / Garden Route District Municipality | Search George, Mossel Bay, Knysna, Plettenberg Bay, `Garden Route data centre`; mostly telecom/edge leads. |
| Central Karoo District Municipality | Search Beaufort West and renewable-energy plus data-centre terms; low probability. |

Western Cape templates:

```text
"Cape Town" ("data centre" OR "data center") ("DAMS" OR "Municipal Planning Tribunal")
site:capetown.gov.za "data centre" "Municipal Planning Tribunal"
site:capetown.gov.za "Equinix" "King Air"
"King Air Industria" "data centre" "Cape Town"
"Brackenfell" "Teraco" "data centre"
"Diep River" "Africa Data Centres" "Cape Town"
"AWS Africa (Cape Town) Region" "Availability Zones"
```

### 5.3 KwaZulu-Natal - priority for Durban/eThekwini

Known concentration: Durban/Riverhorse Valley and potential eThekwini AI/data-centre proposals; Dube TradePort and Cornubia/Umhlanga are plausible industrial nodes.

| Manifest division | Query approach |
|---|---|
| eThekwini Metropolitan Municipality | Search `Durban`, `Riverhorse Valley`, `Umhlanga`, `Cornubia`, `Dube TradePort`, `Shongweni`, `south of Durban`, `Ward 97`, `AI Data Centre`, Teraco DB1. Check eThekwini LUMS adverts, media statements, council decisions, electricity annual reports for MVA/load references. |
| iLembe District Municipality | Search Ballito, KwaDukuza, Dube TradePort spillover, Tinley Manor, Salt Rock; low/medium probability from airport/logistics growth. |
| uMgungundlovu District Municipality | Search Pietermaritzburg, Hilton, Mkondeni, local government ICT/telco nodes. |
| Amajuba / Ugu / uMkhanyakude / uMzinyathi / uThukela / uThungulu / Zululand / Sisonke | Search major towns plus `data centre`, `server room`, `telco exchange`, `industrial park`; expect no-project or small edge/telco only. Note `uThungulu` may now be King Cetshwayo in current local naming, but manifest uses old name. |

KwaZulu-Natal templates:

```text
"Durban" "data centre" "Teraco"
site:durban.gov.za "data centre" "LUMS"
site:durban.gov.za "AI Data Centre"
site:durban.gov.za "data centre" "MVA"
"Riverhorse Valley" "data centre"
"Dube TradePort" ("data centre" OR "data center" OR "AI")
```

### 5.4 Free State

Known leads are mainly edge/renewable support: Bloemfontein/OADC-type edge, and renewable generation tied to operators' national PPAs/solar farms.

| Manifest division | Query approach |
|---|---|
| Mangaung Metropolitan Municipality | Search Bloemfontein, `BFN1`, OADC, MTN, Vodacom, Telkom, municipal ICT/tenders. |
| Fezile Dabi / Lejweleputswa / Thabo Mofutsanyana / Xhariep | Search Sasolburg, Welkom, Bethlehem, Harrismith, Kroonstad, renewable-energy and industrial-park terms. Treat Teraco/ADC solar farms as energy infrastructure, not datacentres, unless a compute facility is present. |

Templates:

```text
"Bloemfontein" ("data centre" OR "data center" OR "colocation")
"OADC" "Bloemfontein" "data centre"
"Free State" "data centre" "solar" "Teraco"
```

### 5.5 Eastern Cape

Potential nodes: Gqeberha/Port Elizabeth, East London/Buffalo City, Coega SEZ, ELIDZ, university/HPC, telco/edge facilities.

| Manifest division | Query approach |
|---|---|
| Nelson Mandela Bay Metropolitan Municipality | Search `Gqeberha`, `Port Elizabeth`, `Coega`, `data centre`, `server farm`, `colocation`, `SEZ`, `telco`. |
| Buffalo City Metropolitan Municipality | Search East London, ELIDZ, Mdantsane, Bhisho government ICT. |
| Alfred Nzo / Amathole / Chris Hani / Joe Gqabi / OR Tambo / Sarah Baartman | Search district name plus major towns and telco/municipal ICT terms; likely no-project outside small government/server-room facilities. |

Templates:

```text
"Gqeberha" OR "Port Elizabeth" "data centre"
"Coega" "data centre" OR "cloud" OR "AI"
"East London" "data centre" "South Africa"
"ELIDZ" "data centre"
```

### 5.6 Limpopo, Mpumalanga, North West, Northern Cape

These are mostly low-probability for hyperscale datacentres but important for false negatives, telco edge, mining/industrial HPC, and renewables-powered proposals.

| Province/divisions | Query approach |
|---|---|
| Limpopo: Capricorn, Mopani, Sekhukhune, Vhembe, Waterberg | Search Polokwane, Tzaneen, Phalaborwa, Thohoyandou, Lephalale, mining/industrial parks, government ICT, MTN/Vodacom/Telkom remote hubs. |
| Mpumalanga: Ehlanzeni, Gert Sibande, Nkangala | Search Mbombela/Nelspruit, Witbank/eMalahleni, Middelburg, Secunda, coal/energy transition, industrial parks, telco edge. |
| North West: Bojanala Platinum, Dr Kenneth Kaunda, Dr Ruth Segomotsi Mompati, Ngaka Modiri Molema | Search Rustenburg, Klerksdorp, Potchefstroom, Mahikeng, mining campuses, MTN remote hubs, Uptime certificates. |
| Northern Cape: Frances Baard, John Taolo Gaetsewe, Namakwa, Pixley ka Seme, Siyanda/ZF Mgcawu | Search Kimberley, Upington, Springbok, De Aar, Kuruman, solar/wind, `green data centre`, `AI`, `substation`, `renewable PPA`. Avoid counting solar farms as DCs. |

Templates:

```text
"Polokwane" ("data centre" OR "data center" OR "server farm")
"Mbombela" OR "Nelspruit" "data centre"
"Klerksdorp" "data centre" "MTN"
"Kimberley" "data centre" "South Africa"
"Upington" "green data centre" OR "AI data centre"
"Northern Cape" "data centre" "renewable energy"
site:uptimeinstitute.com "South Africa" "{town}" "Tier Certification"
```

---

## 6. District-level workflow

For each manifest division:

1. Split the division into `province`, `district/metro`, and key local municipalities/towns.
2. Run broad web queries with both spellings:

```text
"{division}" ("data centre" OR "data center" OR datacentre)
"{major town}" ("data centre" OR "data center" OR "colocation" OR "cloud region")
"{major town}" ("server farm" OR "AI data centre" OR "data storage centre")
"{province}" "{major town}" ("MW" OR "MVA" OR "substation") "data centre"
```

3. Run operator pivots:

```text
"{operator}" "{major town}" "data centre"
"{operator}" "{district}" "South Africa"
site:{operator-domain} "{major town}" "South Africa"
```

4. Run planning/environment pivots only where a lead exists or the division is high priority:

```text
site:{municipal-domain} "{operator}" "data centre"
site:{municipal-domain} "data centre" "rezoning"
site:{municipal-domain} "data centre" "building plan"
"{major town}" "data centre" "environmental authorisation"
"{major town}" "data centre" "basic assessment report"
```

5. Run directory/certification backstops for operational edge sites:

```text
site:uptimeinstitute.com "South Africa" "{major town}"
site:datacentermap.com "South Africa" "{major town}"
site:baxtel.com "South Africa" "{major town}"
site:peeringdb.com "{major town}" "South Africa"
```

6. Grade conservatively:

- **A**: operator facility page, official cloud-region page, municipal planning/building/environmental record, formal certificate naming facility/address.
- **B**: DCD/MyBroadband/ITWeb/TechCentral/Business Day/Daily Maverick article with named developer/location/status; operator press release without facility page; credible legal/EIA summary.
- **C**: directories, social posts, LinkedIn, petitions, unsourced market reports, local rumours, MoU-only announcements.

---

## 7. Known high-priority leads to verify first

Use these as seed tests for the methodology, not as a complete inventory.

| Lead | Division | Evidence route |
|---|---|---|
| Teraco Johannesburg JB facilities / Isando and Bredell | Gauteng - Ekurhuleni / Johannesburg edge | Teraco Johannesburg page; DCD/Teraco expansion news; Ekurhuleni planning/power docs for expansions. |
| Vantage JNB1 Waterfall City | Gauteng - City of Johannesburg Metropolitan Municipality | Vantage official Johannesburg I page; DCD reports; Attacq/Waterfall/municipal planning docs. |
| Vantage/Equinix/OADC Isando/Germiston facilities | Gauteng - Ekurhuleni Metropolitan Municipality | Equinix JN1 official address; OADC Isando page; Ekurhuleni planning/building-plan evidence. |
| Africa Data Centres Midrand/Samrand | Gauteng - Johannesburg/Tshwane boundary area | ADC official Midrand/Samrand pages; environmental documents such as `data storage centre` expansion notices; municipal jurisdiction check. |
| AWS Africa (Cape Town) Region | Western Cape - City of Cape Town | AWS official region docs and launch blog; do not infer exact addresses. |
| Teraco CT1/CT2 | Western Cape - City of Cape Town | Teraco Cape Town official page/news; Cape Town DAMS/MPT if expansion requires land-use/building records. |
| Africa Data Centres CPT1/CPT2 | Western Cape - City of Cape Town | ADC official news/pages; DCD/ITWeb; Cape Town planning/environment records. |
| Equinix Cape Town / King Air Industria | Western Cape - City of Cape Town | City of Cape Town DAMS/Municipal Planning Tribunal record; Daily Maverick/GroundUp/IOL/W.Media reports; appeal/environmental follow-up. |
| Teraco DB1 Riverhorse Valley | KwaZulu-Natal - eThekwini Metropolitan Municipality | Teraco Durban official page/news; eThekwini LUMS/electricity documents. |
| Proposed Korean/AI data centre engagement in Durban | KwaZulu-Natal - eThekwini Metropolitan Municipality | eThekwini official press/council decisions first; treat as MoU/lead until land-use/building record. |
| OADC Bloemfontein and telco remote hubs | Free State - Mangaung / other regional divisions | OADC/directories/Uptime certificates; usually edge/low-MW, verify address and current owner. |

---

## 8. Common pitfalls

- **Johannesburg naming mismatch**: vendors often market any Gauteng facility as Johannesburg. Map exact addresses to **City of Johannesburg**, **Ekurhuleni**, or **Tshwane** before assigning a manifest division.
- **Cape Town approvals are staged**: rezoning/subdivision/MPT approval is not the same as full environmental/building approval or operational status.
- **Power capacity vs IT load**: press may quote grid import, campus buildout, or IT load. Preserve the label exactly (`MW critical IT load`, `MVA`, `power demand`, `full buildout`).
- **Renewable projects are not datacentres**: Teraco/ADC PPAs and solar farms may sit in Free State/Northern Cape but power facilities elsewhere. Count only compute/storage facilities in the target division.
- **Directories overstate or duplicate**: DataCenterMap/Baxtel/Cloudscene may list old NTT/IS/OADC names separately. Confirm current operator and avoid double-counting acquired facilities.
- **Telco/server rooms**: municipal or telecom "data centre" can mean internal IT/server rooms. Include only facilities that meet the project scope; otherwise mark as internal/edge and capacity unknown.
