# LS Explorer Official - Lesotho Data-Centre Enumeration Methodology

Date: 2026-08-12. Country: LS - Kingdom of Lesotho. Division model: 10 districts: Maseru; Berea; Butha-Buthe (also search Botha-Bothe); Leribe; Mafeteng; Mohale's Hoek; Mokhotlong; Qacha's Nek; Quthing; Thaba-Tseka.

This file is the official-source methodology for finding and grading Lesotho data-centre facilities and pipeline projects. Lesotho has no public national data-centre registry, so enumeration must join regulator, government ICT, land, EIA, energy, operator and cloud-region evidence.

## Reliability Grades

- A: primary/official evidence. Examples: LCA licence or consultation notice; gov.ls or communications.gov.ls project/tender material; Department of Environment EIA record; LEWA/LEC/LHDA/DoE power or generation record; LAA/council/LNDC land or building record; official operator page naming a data centre; official cloud-provider region list.
- B: strong secondary evidence. Examples: LENA state-news article, Lesotho Times, The Post, Public Eye, The Reporter, established trade press, ISOC/Af-IX material, vendor case study, Selibeng tender repost that reproduces official procurement text.
- C: weak lead only. Examples: data-centre directories, market-report snippets, social posts, unsupported MoU reposts, non-specific cloud/hosting marketing.

Grade rule: facility existence is A only when a primary source names the facility or site. Press can corroborate but cannot upgrade a record to A by itself.

## Current Verified Frame

- Operational/publicly evidenced facility seeds: Vodacom Lesotho data centres at Maseru West and Lekokoaneng (official operator page); LCA data centre in Maseru hosting LIXP (official LIXP page); Mohale's Hoek Government Data Centre and two additional government data centres (gov.ls article plus 2021 e-Gov EOI); ETL/Econet Telecom Lesotho data-centre lead in Maseru (operator/regulator confirmation still required for A site details; directories alone are C).
- Announced pipeline: Kobong Hydropower and AI Data Centre Project in the Mokhotlong/Kobong area. Convalt and U.S. Embassy material supports the announced agreement and scale; do not count it as a facility, construction start or IT-load capacity until feasibility, EIA, LEWA licence, land or construction evidence appears.
- Negative cloud finding: no AWS, Azure, Google Cloud or Oracle OCI public cloud region is listed for Lesotho. Nearest public cloud regions are in South Africa. Treat hyperscaler references in Lesotho as tenant, partner, cache or edge leads only.

## Official Sources and URL Status

### LCA / LTA - communications regulator

- LCA home: https://lca.org.ls/ - real. The LCA is the current Lesotho Communications Authority; older material may use Lesotho Telecommunications Authority or LTA.
- Telecommunications licensees: https://lca.org.ls/telecommunications-licensees/ - real. Use for network infrastructure, network services, internet services and value-added service licensees. Current named telecom/ISP players include Econet Telecom Lesotho, Vodacom Lesotho, LEC Communications, Comnet Lesotho, Starlink Lesotho, Jenny Lesotho and others.
- Application requirements: https://lca.org.ls/application-requirements/ - use for licence class definitions.
- Licensing Classification and Fees Rules 2025: https://lca.org.ls/download/lesotho-communications-authority-licensing-classification-and-fees-rules-2025/ - real.
- LCA public-consultation notices are posted as individual news/download items. Do not rely on wildcard URLs such as `public-consultation-notice-*`; instead use site search.

Queries:
```text
site:lca.org.ls "data centre" OR "data center" OR datacentre
site:lca.org.ls "PUBLIC CONSULTATION NOTICE" licence telecommunications
site:lca.org.ls "Telecommunications Licensees" "Econet" OR "Vodacom"
"Lesotho Communications Authority" "data centre" OR "data center"
"Lesotho Telecommunications Authority" "data centre" OR "data center"
"{operator}" "LCA" licence Lesotho
```

### Government ICT / MICSTI / e-Government

- Government portal: https://www.gov.ls/ - real.
- MICSTI site: https://communications.gov.ls/ - real, but coverage is uneven; also search gov.ls.
- Mohale's Hoek power-house article: https://www.gov.ls/uncategorized/power-house-for-data-centre-to-be-constructed/ - real. This is the corrected live URL; the draft `/government/` path should not be used. It confirms a data centre built in Mohale's Hoek, a two-roomed power house, e-Government Infrastructure Project components, and five towers at Senqunyane, Likhoele, Ha Ts'ilo, Malimong and Thamathu.
- EOI for Operationalisation of Mohale's Hoek Data Centre and Integration of the Three Government Data Centres: https://www.gov.ls/wp-content/uploads/2021/07/EXPRESSION-OF-INTEREST-Operationalisation-of-M_Hoek.pdf - real PDF. A-grade evidence for three government data centres and the Mohale's Hoek commissioning/integration scope.
- AfDB MapAfrica Phase I: https://mapafrica.afdb.org/en/projects/46002-P-LS-G00-001 - real. Confirms strengthening existing government data centers.
- AfDB Phase II implementation/progress documents: https://www.afdb.org/en/documents/lesotho-e-government-infrastructure-phase-ii-ipr-september-2024 - real.

Queries:
```text
site:gov.ls "data centre" OR "data center" OR datacentre
site:gov.ls "Mohale's Hoek" "data centre"
site:gov.ls "Government Data Centres" OR "Government Data Centers"
site:communications.gov.ls "data centre" OR "cloud" OR "e-Government"
"Operationalisation of Mohale's Hoek Data Centre"
"e-Government Infrastructure" Lesotho "data centres" tender OR EOI
```

### Land, planning and investment land

- Land Administration Authority: https://laa.org.ls/ - real. Authoritative source for leases, cadastre and land administration; the online Landfolio portal is https://portal.laa.landfolio.com/ .
- LNDC property: https://lndc.org.ls/services/property/ - real. Use for industrial-property leads including Maseru/Tikoe, Maputsoe, Butha-Buthe and Mafeteng.
- LNDC EIA guidance: https://lndc.org.ls/knowledge-base/health-and-environmental-regulations-in-lesotho/ - real. Confirms EIA Clearance Certificate as part of the investment process.
- LNDC LAA guide: https://lndc.org.ls/knowledge-base/land-administration-authority-laa/ - real.

Queries:
```text
site:laa.org.ls "data centre" OR "data center" OR lease
site:lndc.org.ls "data centre" OR "data center" OR "industrial estate"
"{operator}" "plot" "Maseru" Lesotho
"Maseru City Council" "building permit" "data centre"
"{district}" "development permit" "data centre" Lesotho
```

### Environment / EIA

- Department of Environment: https://environment.gov.ls/ - real.
- Environment Act 2008 download: https://environment.gov.ls/download/environment-act-2008/ - real.
- LesothoLII Environment Act text: https://lesotholii.org/akn/ls/act/2008/10/eng@2008-12-05 - real.

Use this route for large builds, substations, fuel storage, generator compounds, water/cooling infrastructure and hydropower/solar components.

Queries:
```text
site:environment.gov.ls "data centre" OR "data center" OR datacentre OR EIA
"{project}" "environmental impact" Lesotho
"{operator}" "EIA Clearance" Lesotho
"Kobong" "Environment Act" OR "EIA" Lesotho
```

### Energy and grid

- LEC: https://lec.co.ls/ - real.
- LEWA: https://www.lewa.org.ls/ - real.
- LEWA Electricity Supply Industry page: https://www.lewa.org.ls/electricity-ector/ - real despite the misspelled path. It lists regulated electricity activity and licensees including LEC, LHDA for 'Muela Hydro-Power Station, LEGCO and solar/minigrid entities.
- LEGCO: https://www.legco.co.ls/ - real.
- Ministry of Energy: https://www.gov.ls/government-ministries/energy/ - real.
- Department of Energy: https://doe.gov.ls/ - real.
- LHDA: https://www.lhda.org.ls/ - use for Lesotho Highlands Water Project context, especially 'Muela, Katse, Mohale and Polihali.

Queries:
```text
site:lec.co.ls "data centre" OR "data center" OR "large power" OR substation
site:lewa.org.ls "Kobong" OR "generation licence" OR "data centre"
site:doe.gov.ls "Kobong" OR "data centre" OR "AI"
site:lhda.org.ls "Polihali" OR "Muela" OR "hydro-power"
"{project}" "Lesotho Electricity Company" OR LEC
"{project}" LEWA "licence" Lesotho
```

### Cloud regions and edge checks

- AWS regions: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ - no Lesotho region; AWS Africa is Cape Town.
- Azure regions: https://learn.microsoft.com/en-us/azure/reliability/regions-list - no Lesotho region; South Africa North/West are listed.
- Google Cloud locations: https://cloud.google.com/about/locations - no Lesotho region; Johannesburg is the regional anchor to check.
- Oracle OCI regions: https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm - no Lesotho region; Johannesburg/South Africa Central is listed.
- LIXP: https://lixp.org.ls/about/ - real. Confirms LIXP migration from NUL to the LCA data centre and hosted caches/root server.
- PeeringDB LIXP: https://www.peeringdb.com/ix/5015 - real. Use as B-grade interconnection evidence.

## Facility Seed List

| Facility/project | District | Status | Best evidence | Grade | Collection action |
|---|---:|---|---|---:|---|
| Vodacom Lesotho Maseru West data centre | Maseru | Operational/operator-marketed | https://www.vodacom.co.ls/business/fixed-solutions/ says services are hosted in two data centres at Maseru West and Lekokoaneng and advertises colocation | A | Search LCA licence, LEC connection, Vodacom annual reports, council/land records. |
| Vodacom Lesotho Lekokoaneng data centre | Berea | Operational/operator-marketed | Same Vodacom page; Lekokoaneng is on the Maseru-Teyateyaneng/Berea side | A for name/location, verify district in parcel records | Do not merge with Maseru West; search Lekokoaneng, TY, Berea. |
| LCA data centre / LIXP host | Maseru | Operational institutional/interconnection facility | https://lixp.org.ls/about/ states LIXP moved to LCA data centre in 2017 | A for existence; B for technical specs unless LCA source found | Search LCA reports, LIXP/PeeringDB peers, Google/Akamai/cache mentions. |
| Mohale's Hoek Government Data Centre | Mohale's Hoek | Built/commissioning/integration evidence | gov.ls power-house article; 2021 EOI PDF | A | Search Phase II deliverables, tender awards, LEC/LEWA connection, council/LAA records. |
| Two additional Government Data Centres | Location not public in verified docs, likely Maseru candidates | Existing government DCs to integrate | 2021 EOI names three Government Data Centres but does not publish all site locations | A for existence as government programme assets; location unresolved | Do not assign district without primary site evidence. |
| Econet Telecom Lesotho / ETL data-centre lead | Maseru likely | Commercial/telco lead | ETL official site plus LCA licence; directories list Maseru but are C | B/C until an ETL page or official record names the facility | Search ETL business hosting/colo pages, LIXP peer docs, LEC/LAA/council evidence. |
| Kobong Hydropower and AI Data Centre Project | Mokhotlong | Announced/approved MoA; not a facility | https://convalt.com/press_releases plus DCD/Investment Monitor/TechAfricaNews coverage | B for announcement; C for facility details | Track feasibility, EIA, LEWA generation licence, land, construction procurement. |

## Per-District Official Strategy

Use the same base query set in every district, then add local anchors. Base set:
```text
"{district}" "data centre" OR "data center" OR datacentre Lesotho
"{district}" "server room" OR "server farm" OR colocation OR hosting Lesotho
"{district}" LCA OR LTA licence ISP Lesotho
"{district}" EIA OR "environmental impact" substation OR UPS OR generator Lesotho
"{district}" LEC OR LEWA "substation" OR "large power" Lesotho
```

- Maseru: highest priority. Anchors: Vodacom Maseru West, LCA data centre, LIXP, ETL, MICSTI/e-Gov offices, Kingsway Road, Old Europa, Mabille Road, Thetsane, Ha Tikoe/Tikoe, Maseru West, LNDC industrial land. Verify any commercial lead through operator/LCA plus land or power records.
- Berea: medium priority. Anchors: Vodacom Lekokoaneng data centre, Teyateyaneng/TY, Malimong e-Gov tower. Run both Berea and Lekokoaneng queries; verify parcel/district because names near Maseru can be misassigned.
- Leribe: medium priority. Anchors: Hlotse, Maputsoe, Ha Nyenye, Peka, LNDC industrial estate and border-fibre routes. No verified DC seed; search industrial-power and telco-hosting records.
- Butha-Buthe / Botha-Bothe: low-medium. Always search both spellings. Anchors: Butha-Buthe town, Belo industrial site, LNDC property, 'Muela hydropower/LHDA. Treat energy anchors as future leads, not facility evidence.
- Mafeteng: low. Anchors: Mafeteng town, LNDC estate, Likhoele e-Gov tower, Ha Ramarothole solar/LEGCO/LEWA power context. Require facility-specific wording before recording.
- Mohale's Hoek: high for government. Anchor: Mohale's Hoek Government Data Centre and power house. Search tender awards, commissioning, LEC connection, LAA/council and Phase II integration material.
- Mokhotlong: high for pipeline, low for current operations. Anchors: Kobong, Polihali, Senqunyane e-Gov tower, Letseng mining-power context. Do not upgrade Kobong beyond announced until official permits/licences appear.
- Qacha's Nek: low. Anchor: Thamathu e-Gov tower. Search official EIA/council/LCA records; negative-search likely.
- Quthing: low. Anchors: Quthing/Moyeni and southern border connectivity. No verified seed; apply negative-search protocol.
- Thaba-Tseka: low. Anchors: Thaba-Tseka town, Katse-area adjacency and public-sector connectivity. No verified seed; apply negative-search protocol.

## De-Duplication and Recording Rules

- LTA and LCA refer to the same regulator across older/newer material; deduplicate by legal entity and facility address.
- IXP presence is not a standalone data centre. Record LIXP as evidence for the LCA data centre and interconnection ecosystem.
- Telco exchanges, bank server rooms, cyber cafes, schools, labs and council ICT rooms are not data centres unless the source says hosting, colocation, cloud, data centre or equivalent facility service.
- For every facility record capture: operator, legal entity, district, town/site, address/plot if available, source URL, source grade, operational status, claimed capacity with units, power source/connection, confidence note and unresolved checks.
- Never convert MVA/kVA to MW unless the source does so. Kobong generation capacity is not data-centre IT load.
