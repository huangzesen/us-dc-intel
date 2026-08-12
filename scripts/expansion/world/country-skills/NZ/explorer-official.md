# NZ Explorer Official - New Zealand Datacenter Enumeration via Resource Consents, Transpower, Cloud Regions, Colo, and Regulators

Date: 2026-08-12. Scope: New Zealand (NZ), 17 repo divisions: Auckland, Bay of Plenty, Canterbury, Chatham Islands Territory, Gisborne, Hawke's Bay, Marlborough, Manawatu-Whanganui, Nelson, Northland, Otago, Southland, Tasman, Taranaki, Greater Wellington, Waikato, West Coast. Angle: **official/regulatory/cloud pipeline**. Reliability grades: **A** = official/primary source (council consent file, EPA/MfE fast-track file, Transpower/GCDO/regulator page, operator official page), **B** = strong secondary/trade press or industry report with named sources, **C** = weak directory, social, aggregate, or unverified marketing.

---

## 0. Structural facts for New Zealand

- New Zealand has **no single national datacenter permit registry**. Facility and project enumeration is mainly a **Resource Management Act (RMA) resource-consent search** plus **building-consent/property-file follow-up** at council level. Large projects may also appear in **EPA fast-track consenting** and **Ministry for the Environment fast-track project pages**.
- The planning unit is usually the **territorial authority / unitary authority**, not just the repo's regional division. For each region, map likely sites to city/district councils and regional councils. Example: Auckland is a unitary authority; Southland projects can require Southland District Council land-use consent plus Environment Southland regional consents plus Invercargill City Council approvals for related works.
- Resource-consent files may use broad planning language rather than "data centre" as the application category. Search for `data centre`, `data center`, `datacentre`, `server hall`, `hyperscale`, `GXP substation`, `substation`, `diesel generators`, `backup generators`, `cooling`, `industrial or trade activity`, `discharge of contaminants`, and named operators/SPVs.
- Public visibility is uneven. Ministry for the Environment guidance says notified consents are publicly available for submissions, but many datacenter applications can be **non-notified**. Use council open-data/property portals, LGOIMA requests, property files, and meeting minutes when a consent is known but the full file is not indexed.
- Power is a high-yield independent signal. Transpower publishes connection-process pages and a public **New Connection Enquiries** dashboard for generation, storage, and load. Transpower's Te Kanapu data-centre insights and dashboard are Grade A for grid context and aggregated/enquiry-stage signals; they are not proof of built datacenters.
- Official cloud sources are now unusually useful in NZ. Microsoft opened **New Zealand North** in December 2024, Azure lists `newzealandnorth` in Auckland, AWS opened **Asia Pacific (New Zealand)** `ap-southeast-6` with 3 AZs in September 2025, and NZ Digital Government's **Public Cloud Data Centre Certification (PCDCC)** page names certified facilities/areas.
- Most currently visible hyperscale/colo activity clusters around **Auckland**; **Waikato/Hamilton** has Datacom Kapua; **Southland/Invercargill-Makarewa** has the Datagrid hyperscale/AI campus consent trail; **Canterbury/Christchurch** and **Greater Wellington** have telco/enterprise/edge leads.

Key lifecycle vocabulary:

`site selection` < `pre-application meeting` < `fast-track referral / listed project` < `resource consent lodged` < `publicly notified / limited notified / non-notified` < `decision / consent conditions` < `building consent` < `earthworks / enabling works` < `grid investigation / connection agreement` < `commissioning` < `certified / operational`

Count status conservatively:

- **Operational**: operator official facility page, GCDO certified facility, council completion/compliance, or strong operator announcement.
- **Approved/permitted**: council/EPA resource-consent decision, consent conditions, or fast-track approval.
- **Proposed/planned**: lodged consent, fast-track application, operator development page, Transpower enquiry, or official council proposal page.
- **Lead only**: cloud region, Transpower aggregate pipeline, overseas-investment approval, industry directory, or press without primary documents.

---

## 1. Official planning and consenting backbone

### 1.1 National RMA / consent process sources

- **Ministry for the Environment - What is a resource consent?**: https://environment.govt.nz/publications/information-for-affected-persons/what-is-a-resource-consent/. Grade A for process. It confirms applications can be publicly notified, limited notified, or non-notified.
- **Ministry for the Environment - When you need a resource consent**: https://environment.govt.nz/publications/understanding-the-rma-and-how-to-get-involved/when-you-need-a-resource-consent/. Grade A for public-submission pathway.
- **Ministry for the Environment - applying for a resource consent guide**: https://environment.govt.nz/assets/Publications/Files/2.1-applying-for-a-resource-consent_0.pdf. Grade A for statutory processing stages/timing.
- **Environment Court**: https://www.environmentcourt.govt.nz/. Grade A for appeals/plan cases. Search decisions for consent appeals, plan changes, or judicially visible disputes around large projects.
- **EPA fast-track consenting**: https://www.epa.govt.nz/fast-track-consenting/. Grade A for COVID-19 Recovery fast-track projects and related decision reports.
- **MfE Fast-track projects**: https://environment.govt.nz/acts-and-regulations/acts/fast-track-approvals/fast-track-projects/. Grade A for listed/unlisted Fast-track Approvals projects and supporting documents.

Core planning queries:

```text
"{division}" "data centre" "resource consent"
"{division}" "data center" "resource consent"
"{division}" datacentre consent
"{city/district council}" "data centre" "resource consent"
site:{council-domain} "data centre"
site:{council-domain} "data center"
site:{council-domain} datacentre
site:{council-domain} "hyperscale" "resource consent"
site:{council-domain} "GXP substation" "data centre"
site:{council-domain} "backup generators" "data centre"
site:{council-domain} "diesel generators" "data centre"
site:{council-domain} "industrial or trade activity" "data centre"
```

Document and decision queries:

```text
filetype:pdf "data centre" "assessment of environmental effects" "New Zealand"
filetype:pdf "data centre" "resource consent decision"
filetype:pdf "data centre" "consent conditions"
filetype:pdf "data centre" "AEE" "{division}"
filetype:pdf "data centre" "air quality" "{division}"
filetype:pdf "data centre" "noise assessment" "{division}"
filetype:pdf "data centre" "traffic assessment" "{division}"
filetype:pdf "data centre" "stormwater" "{division}"
filetype:pdf "data centre" "substation" "{division}"
```

What to extract from consent packs: application/reference number, consent authority, consent holder/applicant/SPV, site address and legal description, activity status, notification status, decision date, lapse date, conditions, floor area, site area, data halls, IT load MW, total utility/load MW, GXP/substation details, generator count/rating, cooling/water demand, discharge permits, stormwater, earthworks volume, construction phasing, and related building-consent/property-file references.

### 1.2 Council portals and how to use them

New Zealand councils vary in how much they expose online. The minimum workflow for every hit is:

1. Search council website and notified-consent pages.
2. Search public GIS/open-data layers for resource consents, property, zoning, hazards, and infrastructure.
3. Search council agendas/minutes for land sales, plan changes, private plan changes, development agreements, road stopping, easements, and submissions.
4. If the primary file is not posted, request property file/resource-consent documents under LGOIMA or use the council's paid property-file channel.

High-yield official examples:

- **Auckland Council GeoMaps**: https://geomapspublic.aucklandcouncil.govt.nz/. Grade A for council GIS/property/resource-consent layers. Use parcel/address search around known clusters such as Hobsonville, Westgate, Silverdale/Millwater/Dairy Flat, Takanini/Papakura, Auckland CBD, Albany/North Shore, East Tamaki, and airport/industrial precincts.
- **Auckland Council Open Data**: https://data-aucklandcouncil.opendata.arcgis.com/. Grade A for downloadable GIS layers where available.
- **Auckland Unitary Plan**: https://unitaryplan.aucklandcouncil.govt.nz/. Grade A for zoning/precinct rules. Search `data centre` and `industrial or trade activity`; the Auckland Surf Park/Dairy Flat documents are a useful template for how datacenters appear under Unitary Plan rules.
- **Christchurch City Council resource consents**: https://ccc.govt.nz/consents-and-licences/resource-consents and received/issued search page https://ccc.govt.nz/consents-and-licences/resource-consents/resource-consent-process/resource-consents-received-and-issued. Grade A. Search by RMA number, address, name, and application type.
- **Christchurch City Council Open Data**: https://opendata-christchurchcity.hub.arcgis.com/. Grade A for spatial context.
- **Environment Canterbury consent search**: https://www.ecan.govt.nz/data/consent-search. Grade A for regional water/discharge consents; search operator/applicant names and activity keywords.
- **Canterbury Maps resource consents active**: https://opendata.canterburymaps.govt.nz/maps/resource-consents-active. Grade A for regional consent locations/applications.
- **Environment Southland Datagrid page**: https://www.es.govt.nz/datagrid. Grade A example of a regional council public-notice page with consent decision PDFs and application appendices.
- **Southland District Council proposals of public interest**: https://www.southlanddc.govt.nz/home-and-property/resource-consents/proposals-of-public-interest/. Grade A example of a district council proposal page for Datagrid.

Council-scoped query templates:

```text
site:aucklandcouncil.govt.nz ("data centre" OR datacentre OR "data center")
site:geomapspublic.aucklandcouncil.govt.nz "data centre"
site:ccc.govt.nz ("data centre" OR datacentre)
site:ecan.govt.nz ("data centre" OR datacentre)
site:es.govt.nz ("data centre" OR datacentre OR Datagrid)
site:southlanddc.govt.nz ("data centre" OR datacentre OR Datagrid)
site:wellington.govt.nz ("data centre" OR datacentre)
site:hcc.govt.nz ("data centre" OR datacentre OR Datacom OR Kapua)
site:waikatoregion.govt.nz ("data centre" OR datacentre)
```

### 1.3 Fast-track and official project examples

Use these as templates for expected document depth and fields.

- **Auckland Surf Park Community - EPA**: https://www.epa.govt.nz/fast-track-consenting/referred-projects/auckland-surf-park-community/. Grade A. The project includes a data centre and solar farm at 1350 Dairy Flat Highway, Silverdale/Auckland. EPA pages link application material and decision documents.
- **EPA latest-news decision note for Auckland Surf Park**: https://www.epa.govt.nz/news-and-alerts/latest-news/surfs-up-at-dairy-flat/. Grade A. Confirms consent decision and that conditions sit in the decision report.
- **Auckland Surf Park AEE PDF**: https://www.epa.govt.nz/assets/Uploads/Documents/Fast-track-consenting/Auckland-Surf-Park-/Revised-application/Auckland-Surf-Park-assessment-of-environmental-effects.pdf. Grade A. Search inside for `data centre`, `industrial or trade activity`, `discharge of contaminants`, cooling, solar, and heat reuse.
- **Datagrid Sustainable Data Centre Park - MfE**: https://environment.govt.nz/acts-and-regulations/acts/fast-track-approvals/fast-track-projects/datagrid-sustainable-data-centre-park/. Grade A for fast-track application/supporting material.
- **Datagrid official site**: https://www.datagrid.nz/. Grade A for operator/project claims; validate against council/EPA/MfE documents.
- **Datagrid resource-consent announcement**: https://www.datagrid.nz/pr1-rc/resourceconsent. Grade A/B: official operator announcement; use Environment Southland/Southland District Council decisions as the primary source for approval and conditions.

Fast-track query templates:

```text
site:epa.govt.nz "data centre" "fast-track"
site:epa.govt.nz "data center" "resource consent"
site:environment.govt.nz "data centre" "Fast-track"
site:environment.govt.nz "Datagrid Sustainable Data Centre Park"
site:environment.govt.nz "data centre" "unlisted project"
site:environment.govt.nz "data centre" "listed project"
```

---

## 2. Energy, grid, and utility evidence

### 2.1 Transpower and national grid sources

- **Transpower Connections hub**: https://www.transpower.co.nz/connections. Grade A process source for new generation, storage, and load connections.
- **Transpower - What's the latest with grid connections?**: https://www.transpower.co.nz/connections/whats-latest-grid-connections. Grade A route into progress/dashboard material for new load, generation, and storage.
- **Transpower New Connection Enquiries dashboard**: https://experience.arcgis.com/experience/97d4604079b545448280423f9269b9ea. Grade A for aggregated/public enquiry-stage connection data. It includes "load or demand" categories; use as lead evidence only until project identity is confirmed.
- **Transpower New Connection Enquiries - About the data**: https://experience.arcgis.com/experience/97d4604079b545448280423f9269b9ea/page/About-the-data. Grade A for data definitions/limitations.
- **Transpower grid connection process**: https://www.transpower.co.nz/connections/our-grid-connection-process. Grade A. It states small/simple connections can be under 18 months while large complex connections may take longer than three years.
- **Transpower customer information**: https://www.transpower.co.nz/connections/customer-information. Grade A for required information on new connection enquiries and investigation applications.
- **Transpower Te Kanapu data centres insights PDF**: https://static.transpower.co.nz/public/uncontrolled_docs/Te%20Kanapu%20insights%20-%20data%20centres.pdf?VersionId=F4jVwV0JTAXqG4eq3c45JmLJb4_tlzJR. Grade A for official data-centre demand methodology and aggregate scenario context.
- **Transpower proposed new load and other connections process consultation PDF**: https://static.transpower.co.nz/public/uncontrolled_docs/New-load-and-other-connections-proposed-application-process-consultation-document.pdf?VersionId=z5qo4mC7yNgHMJET5Tl72j_ei4SzlBYV. Grade A for current load-connection process reform context.

Grid query templates:

```text
site:transpower.co.nz "data centres"
site:transpower.co.nz "data centre" "load"
site:transpower.co.nz "data centre" "connection"
site:transpower.co.nz "new load" "data centre"
site:experience.arcgis.com "Transpower" "load" "data centre"
"{project}" "Transpower" "GXP"
"{project}" "grid exit point"
"{project}" "220kV" "data centre"
"{project}" "substation" "Transpower"
"{division}" "data centre" "GXP substation"
"{division}" "data centre" "MVA"
"{division}" "data centre" "MW" "grid connection"
```

### 2.2 Electricity regulators and distribution companies

- **Electricity Authority**: https://www.ea.govt.nz/. Grade A for electricity-market regulation, connection/process reform, and industry-code context. Not a datacenter registry.
- **Commerce Commission - electricity lines**: https://comcom.govt.nz/regulated-industries/electricity-lines. Grade A for regulated lines-business context and information disclosures; useful when datacenters connect to local distribution networks rather than Transpower directly.
- **Commerce Commission - telecommunications**: https://www.comcom.govt.nz/regulated-industries/telecommunications/. Grade A for telecom-market regulation, not facility enumeration.
- **MBIE communications markets regulatory system**: https://www.mbie.govt.nz/cross-government-functions/regulatory-stewardship/regulatory-systems/communications-markets-regulatory-system. Grade A for communications-market regulatory context.

Distribution companies to pivot by region:

| Region/division | Likely electricity distribution leads | Search terms |
|---|---|---|
| Auckland | Vector, Counties Energy, Northpower in northern fringe | `data centre Vector`, `data centre Counties Energy`, `Silverdale substation`, `Hobsonville`, `Westgate`, `Takanini` |
| Waikato | WEL Networks, Waipa Networks, Powerco | `Kapua Datacom WEL Networks`, `Hamilton data centre substation` |
| Greater Wellington | Wellington Electricity, Electra, Powerco | `Wellington data centre substation`, `Porirua data centre`, `Hutt data centre` |
| Canterbury | Orion, MainPower, Alpine Energy, Electricity Ashburton | `Christchurch data centre Orion`, `Canterbury data centre substation` |
| Southland | PowerNet, Electricity Invercargill, Transpower | `Datagrid GXP`, `Makarewa substation`, `Invercargill data centre 220kV` |
| Bay of Plenty / Taranaki / Hawke's Bay / Manawatu-Whanganui / Otago / Nelson-Tasman / Marlborough / West Coast / Northland | Local EDBs plus Transpower if load is large | combine operator/project with `substation`, `GXP`, `MW`, `MVA`, and EDB name |

Energy caution: separate `grid/enquiry MW`, `contracted connection capacity`, `building electrical load`, `IT load`, `generator backup capacity`, and `actual annual consumption`. Do not convert one to another without a primary-source statement.

---

## 3. Official cloud and government certification sources

### 3.1 Public cloud regions (Grade A for region existence; not exact addresses)

| Provider | Official source | NZ signal | Enumeration use |
|---|---|---|---|
| Microsoft Azure | Azure regions list: https://learn.microsoft.com/en-us/azure/reliability/regions-list; Microsoft NZ launch: https://news.microsoft.com/en-nz/2024/12/12/new-zealands-first-hyperscale-cloud-is-open-for-business/; NZ datacenter region microsite: https://news.microsoft.com/aotearoa-datacenter | `New Zealand North`, physical location Auckland, programmatic name `newzealandnorth`; region opened 2024-12-12 | Seed Auckland/Hobsonville/Silverdale/Westgate/Millwater searches. Use GCDO PCDCC and council consents to confirm facility-level evidence. |
| AWS | AWS NZ local page: https://aws.amazon.com/local/new-zealand/; AWS launch blog: https://aws.amazon.com/blogs/aws/now-open-aws-asia-pacific-new-zealand-region/; AWS regions docs: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | Asia Pacific (New Zealand), `ap-southeast-6`, 3 AZs, opened 2025-09-01 | Seed Auckland-area provider/lease searches. AWS region evidence is metro/region-level only unless a primary consent/operator facility is found. |
| Google Cloud | Global locations: https://cloud.google.com/about/locations; Compute regions/zones: https://docs.cloud.google.com/compute/docs/regions-zones | No NZ cloud region observed in official locations as of this file date | Use as negative check; do not infer a Google NZ facility from edge/PoP or partner hosting. |
| Oracle OCI | Regions docs: https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm; public cloud regions: https://www.oracle.com/cloud/public-cloud-regions/ | No NZ public OCI region observed in official region list as of this file date | Use only for cloud-market context unless an official NZ facility/region appears. |

Cloud query templates:

```text
"Azure" "New Zealand North" Auckland datacenter
"Microsoft" "New Zealand North" "GCDO" "data centre"
"Microsoft" "AKL02" "data centre"
"AWS" "ap-southeast-6" "New Zealand"
"AWS Asia Pacific (New Zealand) Region" "Availability Zones"
"Amazon Data Services" "Auckland" "resource consent"
"Google Cloud" "New Zealand" "region" "locations"
"Oracle Cloud" "New Zealand" "region"
```

### 3.2 NZ Government public cloud certification

- **NZ Digital Government - Certified PCDC facilities and areas**: https://www.digital.govt.nz/products-and-services/products-and-services-a-z/public-cloud-data-centre-certification-pcdcc/certified-pcdc-facilities-and-areas. Grade A and unusually high-value facility lead. At the time checked, it lists:
  - CDC Data Centres NZ Limited - Silverdale 1, certified 2025-03-19.
  - CDC Data Centres NZ Limited - Hobsonville 1, certified 2025-03-19.
  - Microsoft - AKL02, certified 2025-07-02.
- **NZ Digital Government - Cloud Jurisdictional Risk guidance**: https://www.digital.govt.nz/standards-and-guidance/technology-and-architecture/cloud-services/assess-the-risks/cloud-jurisdictional-risk-guidance. Grade A for public-sector cloud governance context, not a facility census.
- **NZ Digital Government - Cloud First policy**: https://www.dns.govt.nz/standards-and-guidance/technology-and-architecture/cloud-services/cloud-adoption-policy-and-strategy/cabinet-requirement. Grade A for demand/procurement context.

Use PCDCC as a validation source, not a full inventory. It only covers certified public cloud data-centre facilities/areas for government use and can omit private colo, enterprise, telco, and uncertified hyperscale/lease facilities.

---

## 4. Operator and colocation seed list

Use operator official pages as Grade A for facility existence/marketing claims, then confirm capacity/status with council, GCDO, Transpower, or property records.

| Operator / platform | Official source | NZ facility/project seed | Notes |
|---|---|---|---|
| CDC Data Centres | Auckland page: https://cdc.com/locations/auckland/ | Auckland campuses; page states 220 MW+ capacity; GCDO certifies Silverdale 1 and Hobsonville 1 | High-priority Auckland hyperscale seed. Search `CDC Data Centres NZ Limited`, `Silverdale`, `Hobsonville`, `resource consent`, `AKL`. |
| Datacom | Data centres overview: https://datacom.com/nz/en/products/data-centres; Kapua Hamilton: https://datacom.com/nz/en/products/data-centres/locations/kapua-hamilton; Kapua decade article: https://datacom.com/nz/en/discover/articles/datacom-marks-kapua-s-decade-of-data-in-hamilton | Kapua, Hamilton/Waikato; official article says expandable to 1,500+ racks and 14 MW | Search Hamilton City Council/Waikato Regional Council and WEL Networks for consent/grid history and expansions. |
| Spark / Spark Wholesale / Spark Data Centres | Spark Wholesale colocation: https://www.sparkwholesale.co.nz/products/layerzero/colocation/ | Spark says it deploys assets in data centres and exchanges across NZ; known official/press leads include Takanini, Auckland CBD, North Shore/Dairy Flat | Spark official social/announcements may be B if not on corporate site. Confirm with Auckland Council/EPA. Qrious is Spark-owned but mainly a data/AI services brand; treat it as an entity pivot, not a facility list. |
| Digital Island | https://digitalisland.co.nz/ | Telecom/cloud-services provider seed | Official site is useful for provider identity but does not expose a strong public datacenter inventory. Treat facility claims as unconfirmed until a council/operator facility source is found. |
| Qrious | https://www.qrious.co.nz/ and Spark ownership context | Spark data/AI services brand | Search `Qrious Spark data centre`, but do not count Qrious as a separate DC operator without primary facility evidence. |
| NEXTDC | NZ page: https://www.nextdc.com/data-centres/new-zealand-data-centres-colocation | AK1 Auckland in development | Operator official development lead. Confirm through Auckland Council consent/property records and Transpower/Vector/Counties Energy if available. |
| Datagrid | https://www.datagrid.nz/ and resource-consent announcement https://www.datagrid.nz/pr1-rc/resourceconsent | Southland/Makarewa sustainable data centre / AI factory campus | Primary approval evidence sits with Environment Southland and Southland District Council. |
| Equinix | Global/APAC page: https://www.equinix.com/data-centers/asia-pacific-colocation and global data centers: https://www.equinix.com/data-centers | No official New Zealand facility page identified in checked Equinix pages | Include as a negative/monitoring seed because the brief names Equinix NZ. Do not count an Equinix NZ site unless an official Equinix location page, acquisition, or council file is found. |
| Catalyst Cloud | https://catalystcloud.nz/about/data-sovereignty/ | NZ sovereign cloud/provider lead | Good sovereign cloud/operator lead; validate physical facilities via official/council evidence before counting. |
| Datacentre220 / Data Vault / Plan B / local telco-hosting operators | Operator pages and directories; use official pages first | Auckland/Wellington/Christchurch edge/colo leads | Often visible in directories before council files. Grade B/C until official operator or council evidence confirms facility. |

Operator pivot queries:

```text
"CDC Data Centres NZ Limited" "resource consent"
"CDC" "Silverdale" "data centre" "Auckland Council"
"CDC" "Hobsonville" "data centre" "Auckland Council"
"Microsoft" "AKL02" "CDC" OR "Silverdale" OR "Hobsonville"
"Datacom" "Kapua" "resource consent"
"Datacom" "Hamilton" "data centre" "14MW"
"Spark" "Takanini" "data centre" "resource consent"
"Spark" "Dairy Flat" "data centre" "resource consent"
"Spark" "North Shore" "data centre" "resource consent"
"Digital Island" "data centre" "New Zealand"
"Qrious" "data centre" "Spark"
"Equinix" "New Zealand" "data center"
"NEXTDC" "AK1" "Auckland" "resource consent"
"Datagrid" "Makarewa" "resource consent"
```

---

## 5. Per-division enumeration strategy

### 5.1 Priority divisions

| Repo division | Priority | Official route | Operator/cloud seeds |
|---|---:|---|---|
| Auckland | Very high | Auckland Council GeoMaps/Open Data/Unitary Plan, EPA fast-track, GCDO PCDCC, Transpower dashboard, Vector/Counties Energy/Northpower | Microsoft NZ North, AWS NZ region, CDC Silverdale/Hobsonville, Spark Takanini/CBD/North Shore, NEXTDC AK1, Digital Island/Qrious/Spark pivots |
| Waikato | High | Hamilton City Council, Waikato Regional Council, WEL Networks, Transpower | Datacom Kapua Hamilton, industrial/HPC expansion leads |
| Southland | High | Environment Southland, Southland District Council, Invercargill City Council, MfE fast-track, Transpower/PowerNet | Datagrid Makarewa, subsea cable/GXP substation leads |
| Canterbury | Medium-high | Christchurch City Council received/issued search, CCC Open Data, Environment Canterbury consent search, Canterbury Maps, Orion | Christchurch edge/colo/telco leads, disaster-recovery/enterprise facilities |
| Greater Wellington | Medium-high | Wellington City Council, Hutt City, Porirua, Wellington Regional Council, Wellington Electricity/Electra | Government/enterprise/telco facilities, Spark/Datacentre220/Catalyst-style sovereign leads |
| Bay of Plenty | Medium | Tauranga City, Western Bay of Plenty, Bay of Plenty Regional Council, Powerco/Unison/Horizon | Edge/industrial/coastal fiber leads; search Tauranga/Whakatane/Rotorua |
| Northland | Medium | Northland Regional Council, Whangarei/Far North/Kaipara district councils, Northpower/Top Energy | Auckland-north fringe overlap, cable/renewable-power-adjacent leads |
| Otago | Medium | Dunedin City, Queenstown Lakes, Otago Regional Council, Aurora/Network Waitaki | University/HPC, edge/DR, cold-climate/renewables leads |
| Taranaki | Medium | New Plymouth District, Taranaki Regional Council, Powerco, Transpower | Industrial energy/hydrogen/AI leads; verify carefully |
| Manawatu-Whanganui | Low-medium | Palmerston North, Whanganui, Horizons Regional Council, Powerco | Edge/DR, central North Island network routes |
| Hawke's Bay | Low-medium | Napier/Hastings, Hawke's Bay Regional Council, Unison | Edge and disaster-recovery leads |
| Nelson / Tasman / Marlborough | Low-medium | Nelson City, Tasman District, Marlborough District, Network Tasman/Marlborough Lines | Small edge, subsea/fiber, local sovereign/cloud leads |
| West Coast | Low | West Coast Regional Council and district councils, Westpower | Low-density but check energy/industrial proposals |
| Gisborne | Low | Gisborne District Council/unitary authority, Eastland Network | Edge/resilience leads |
| Chatham Islands Territory | Very low | Chatham Islands Council, central government infrastructure pages | Count only explicit facility evidence; likely no commercial DC lead |

### 5.2 Regional query templates

For each `{division}`, run:

```text
"{division}" "data centre" "resource consent"
"{division}" "data center" "resource consent"
"{division}" datacentre "council"
"{division}" "hyperscale" "data centre"
"{division}" "AI factory" "data centre"
"{division}" "GXP substation" "data centre"
"{division}" "Transpower" "data centre"
"{division}" "data centre" "MW"
"{division}" "data centre" "MVA"
"{division}" "data centre" "diesel generators"
"{division}" "data centre" "cooling"
"{division}" "data centre" "water take"
"{division}" "data centre" "discharge permit"
```

For every city/district council in the division, run:

```text
site:{council-domain} ("data centre" OR "data center" OR datacentre)
site:{council-domain} ("server hall" OR hyperscale OR "AI factory")
site:{council-domain} ("GXP" OR substation OR "backup generators") "data centre"
site:{council-domain} ("resource consent decision" OR "consent conditions") "data centre"
site:{council-domain} ("notified consent" OR "proposals of public interest") "data centre"
```

For regional councils:

```text
site:{regional-council-domain} ("data centre" OR datacentre)
site:{regional-council-domain} ("water take" OR groundwater OR discharge OR stormwater) "data centre"
site:{regional-council-domain} ("industrial or trade activity" OR "air discharge") "data centre"
site:{regional-council-domain} "{operator}" consent
```

### 5.3 Auckland deep-dive workflow

Auckland needs extra care because it contains the major hyperscale cluster and several cloud-region/AZ claims.

1. Start with GCDO PCDCC certified facilities: CDC Silverdale 1, CDC Hobsonville 1, Microsoft AKL02.
2. Open Auckland Council GeoMaps and search parcels/addresses around `Silverdale`, `Millwater`, `Dairy Flat`, `Hobsonville`, `Westgate`, `Takanini`, `Papakura`, `Auckland CBD`, `Albany`, `East Tamaki`, `Mangere`, and `Airport`.
3. Search EPA Auckland Surf Park files for Spark/North Shore/Dairy Flat data-centre details and heat-reuse/solar conditions.
4. Search operator pivots: CDC, Microsoft, AWS/Amazon Data Services, Spark, NEXTDC AK1, Datacom, Digital Island, Qrious, Catalyst, Plan B, Data Vault, Datacentre220.
5. Cross-check with Transpower New Connection Enquiries and local EDBs. Auckland projects may connect through Vector, Counties Energy, Northpower, or directly/indirectly through Transpower upgrades.
6. Use council meeting minutes and property files when consent documents are not indexed by public search.

Auckland-specific queries:

```text
"Auckland" "data centre" "resource consent" "Silverdale"
"Auckland" "data centre" "resource consent" "Hobsonville"
"Auckland" "data centre" "resource consent" "Westgate"
"Auckland" "data centre" "resource consent" "Dairy Flat"
"Auckland" "data centre" "resource consent" "Takanini"
"Auckland Surf Park" "data centre" "decision report"
"CDC Data Centres" "Silverdale" "Auckland Council"
"CDC Data Centres" "Hobsonville" "Auckland Council"
"NEXTDC AK1" "Auckland Council"
"Amazon Data Services" "Auckland" "resource consent"
```

### 5.4 Southland / Datagrid workflow

1. Open Environment Southland Datagrid page and download decision/application appendices.
2. Open Southland District Council proposals of public interest and collect the land-use consent record.
3. Search MfE fast-track project page for Datagrid supporting documents, including location plans, title records, cable-route plans, and agency advice.
4. Search Invercargill City Council for cable/road approvals and related works.
5. Search Transpower for GXP/substation connection references and use the Transpower dashboard for load-enquiry context.
6. Record Datagrid as approved/permitted only to the extent supported by consent decisions; record operator capacity claims separately.

Southland-specific queries:

```text
"Datagrid NZ Partnership Limited" "Resource Consent Decision"
"Datagrid" "APP-20252550"
"Datagrid" "GXP substation"
"Datagrid" "Makarewa" "Southland District Council"
"Datagrid" "Environment Southland" "water take"
"Datagrid" "Invercargill City Council" "cable"
"Datagrid Sustainable Data Centre Park" "Transpower"
```

---

## 6. Regulator, privacy, procurement, and validation sources

Use these for context and validation, not as first-pass facility lists unless they name facilities.

- **Government Chief Digital Office / NZ Digital Government PCDCC**: facility-grade for certified public cloud facilities/areas. https://www.digital.govt.nz/products-and-services/products-and-services-a-z/public-cloud-data-centre-certification-pcdcc/certified-pcdc-facilities-and-areas.
- **Commerce Commission telecommunications**: https://www.comcom.govt.nz/regulated-industries/telecommunications/. Grade A for telecom regulation/market monitoring; useful for telco operator identity and wholesale context.
- **Commerce Commission electricity lines**: https://comcom.govt.nz/regulated-industries/electricity-lines. Grade A for EDB information-disclosure context.
- **Electricity Authority**: https://www.ea.govt.nz/. Grade A for electricity-market and connection-code context.
- **MBIE communications markets regulatory system**: https://www.mbie.govt.nz/cross-government-functions/regulatory-stewardship/regulatory-systems/communications-markets-regulatory-system. Grade A for communications-market framework.
- **Office of the Privacy Commissioner**: https://www.privacy.org.nz/. Grade A for privacy-law context; generally not a datacenter registry.
- **NZTE data and AI infrastructure investment page**: https://www.nzte.govt.nz/page/data-and-ai-infrastructure. Grade A/B for official investment promotion and industry reports; use linked reports as context, not facility proof.
- **Tech New Zealand data-centre infrastructure report**: https://technewzealand.org.nz/reports/empowering-aotearoa-new-zealands-digital-future-our-national-data-centre-infrastructure/. Grade B+ industry/association source; useful for market sizing and operator leads, but confirm facilities with official/operator sources.

Regulatory/context queries:

```text
site:digital.govt.nz "Public Cloud Data Centre Certification"
site:digital.govt.nz "data centre" "certified"
site:comcom.govt.nz "data centre" telecommunications
site:ea.govt.nz "data centre" electricity
site:mbie.govt.nz "data centre" "New Zealand"
site:nzte.govt.nz "data centre" "New Zealand"
site:privacy.org.nz "cloud" "New Zealand" "data centre"
```

---

## 7. Reliability rules and extraction schema

### 7.1 Grading

- **A**: council/EPA/MfE consent application, decision report, consent conditions, council GIS/property record, Transpower dashboard/process/source document, NZ Digital Government PCDCC listing, official cloud-region documentation, operator official facility page.
- **B**: specialist trade press (DCD, Capacity, W.Media, Reseller/IDG, BusinessDesk) citing official documents; NZTech/BCG/NZTE reports; law-firm planning/grid explainers when used for process rather than facility facts.
- **C**: datacenter directories, map sites, LinkedIn posts, social posts, community claims, property speculation, uncited summaries.

### 7.2 Required fields per candidate

```text
country_code: NZ
division: Auckland | Waikato | Southland | ...
territorial_authority:
regional_council:
facility_or_project_name:
operator:
consent_holder_or_applicant:
site_address:
legal_description:
coordinates:
status: operational | approved | lodged | proposed | lead
evidence_grade:
primary_urls:
resource_consent_refs:
building_consent_refs:
notification_status:
decision_date:
lapse_date:
facility_type: hyperscale | colo | telco | enterprise | cloud region | edge | AI/HPC
site_area_ha:
building_gfa_sqm:
data_halls:
it_load_mw:
grid_or_connection_mw:
backup_generation_mw:
water_take_or_cooling:
substation_or_gxp:
cloud_region_or_certification:
notes:
last_checked:
```

### 7.3 Common false positives

- Generic "data centre" references inside career pages, IT services pages, or "contact centre" pages.
- Cloud regions and AZs without facility-level evidence. Count as cloud-region seeds, not physical addresses.
- Transpower load enquiries without named project/customer. Count as grid lead only.
- Qrious/Digital Island service pages that do not name a facility.
- Equinix global/APAC pages that do not list New Zealand.
- University/server-room/HPC pages that are not commercial datacenter projects unless the scope is explicitly intended to include institutional datacenters.

---

## 8. Recommended first-pass sweep order

1. **Auckland official sweep**: GCDO PCDCC -> Auckland Council GeoMaps/Open Data -> EPA Auckland Surf Park -> operator pivots for CDC, Microsoft, AWS, Spark, NEXTDC, Datacom, Digital Island, Qrious.
2. **Southland official sweep**: Environment Southland Datagrid -> Southland District Council proposals -> MfE Datagrid fast-track -> Invercargill City Council -> Transpower/GXP searches.
3. **Waikato/Hamilton sweep**: Datacom Kapua official page -> Hamilton City Council -> Waikato Regional Council -> WEL Networks/Transpower.
4. **Canterbury and Greater Wellington sweep**: council consent portals/open data -> regional consent searches -> telco/enterprise operator pivots.
5. **Remaining regions**: council-by-council keyword search plus Transpower dashboard leads; promote to detailed review only when a consent/operator/grid hit appears.

Minimum validation standard before counting a site: one Grade A facility/project source, or one operator official facility page plus a second independent Grade A/B source. For planned hyperscale projects, require a council/EPA/MfE consent record or Transpower/named grid document before recording MW as more than a lead.
