# LK Explorer Official - Sri Lanka Datacenter Enumeration

Date reviewed: 2026-08-12. Country: **LK - Sri Lanka**. Division model: **9 provinces**: Western; Central; Southern; Northern; Eastern; North Western; North Central; Uva; Sabaragamuwa.

This file is the official-source methodology for finding operational and planned data centers, colocation sites, government cloud facilities, cable landing stations, and data-center-like critical facilities in Sri Lanka. Sri Lanka has no national public data-center registry, so evidence must be assembled from telecom regulation, government ICT programs, operator pages, planning/procurement routes, cable records, certification registries, and investment-promotion records.

## Reliability Grades

- **A**: primary source for the exact fact claimed: TRCSL, ICTA, Ministry of Digital Economy, DPA, BOI, UDA/OSU/local-authority records, CEB/LECO, Treasury/NPC procurement, official operator pages, Uptime Institute certification directory, official cloud-region lists, eROC/RIPE records for entity facts.
- **B**: reputable secondary or regulator-adjacent source: DCD, TeleGeography/Submarine Cable Map, Submarine Networks, Daily FT, EconomyNext, Daily Mirror, Sunday Times, ITU/UNCTAD/UNESCAP/World Bank documents, vendor case studies naming a site.
- **C**: weak lead or pivot: DataCenterMap, datacenters.com, Cloudscene, Baxtel, Inflect, PeeringDB-only facility inference, market-report snippets, Wikipedia, social posts, tender aggregators without original documents.
- **U**: unsupported or unreachable source, or the source does not support the stated facility fact.

Grade each fact separately. Example: an operator page can be A for service existence, while a rack count from press remains B and an aggregator-only MW value remains C/U.

## 0. National Official Context

- **Regulator**: Telecommunications Regulatory Commission of Sri Lanka (TRCSL), https://www.trc.gov.lk/ . TRCSL is the telecom regulator under the Sri Lanka Telecommunications Act. It is A for operator/licensing/regulatory facts, but it is not a data-center registry.
- **Government ICT**: Information and Communication Technology Agency of Sri Lanka (ICTA), https://www.icta.lk/ . The Ministry of Digital Economy institution page confirms ICTA as the apex government ICT institution under the ICT Act No. 27 of 2003, as amended by Act No. 33 of 2008: https://mode.gov.lk/docs/institutions/ICTA . ICTA is A for LGN, Lanka Government Cloud, NDX, policy, and e-government program facts.
- **Parent ministry / institution map**: Ministry of Digital Economy, https://mode.gov.lk/ . Its institution pages list ICTA, SLCERT, SLTMobitel, TRCSL, DPA, and DRP. Re-check ministry name/scope each batch because Sri Lankan ministry portfolios change.
- **Data protection**: Data Protection Authority of Sri Lanka, https://dpa.gov.lk/ . The DPA page confirms the Personal Data Protection Act No. 9 of 2022, the 2025 amendment, and DPA establishment in August 2023. Use this for cloud/data-controller compliance context, not facility discovery.
- **Investment promotion**: Board of Investment of Sri Lanka, https://investsrilanka.com/ . BOI is A for approved investment announcements and zones. Large data-center FDI should be checked here and on project-specific SEZ pages.
- **Port City Colombo**: https://www.portcitycolombo.lk/ . A for SEZ/business-center facts. No official data-center-specific project was verified in this review; any Port City DC claim remains C/U until named by the commission, BOI, a developer, or a permit source.
- **Planning and permits**: Urban Development Authority, https://www.uda.gov.lk/ ; One Stop Unit for Development Approvals, https://osu.uda.lk/ ; Colombo Municipal Council building applications, https://www.colombo.mc.gov.lk/building-application.php . Sri Lanka does not expose a simple national searchable permit database; use these as verification routes for named projects and addresses.
- **Environment**: Central Environmental Authority, https://www.cea.lk/ . Use for EIA/IEE screening only when a named site/project appears.
- **Energy**: Ceylon Electricity Board, https://www.ceb.lk/ ; Lanka Electricity Company, https://www.leco.lk/ . A for grid/distribution context. They do not publish a public DC list. Record MW/kVA only when a site-named source supports it.
- **Procurement**: Ministry of Finance/Treasury procurement notices, https://www.treasury.gov.lk/procurement/procurement-notices ; National Procurement Commission, https://nprocom.gov.lk/ ; ePMS, https://epms.nprocom.gov.lk/ . Use UNGM and World Bank documents for donor-funded ICT projects. Treat `procurement.gov.lk` and `etenders.lk` as unverified unless the original buyer document is opened.
- **Company registry**: Department of Registrar of Companies / eROC, https://eroc.drc.gov.lk/ . A for legal-entity registration and registered addresses; not proof of a facility.
- **Cybersecurity**: Sri Lanka CERT|CC, https://www.cert.gov.lk/ . A for national CERT role and incident/procurement context; not a facility source.

## 1. Official Search Vocabulary

Run English first, then Sinhala/Tamil for local media and government notices.

```text
EN: data center; data centre; datacenter; colocation; co-location; hosting; cloud;
    internet data centre; IDC; server room; disaster recovery; DR site; cable landing station;
    submarine cable; internet exchange; IXP; national data centre; sovereign cloud

SI: "දත්ත මධ්‍යස්ථානය"; "දත්ත මධ්‍යස්ථාන"; "වලාකුළු පරිගණනය";
    "සේවාදායක"; "මුහුදු යට කේබලය"; "අන්තර්ජාල හුවමාරු"

TA: "தரவு மையம்"; "தரவு மையங்கள்"; "மேகக் கணிமை";
    "சேவையகம்"; "கடலடி கேபிள்"; "இணைய பரிமாற்றம்"
```

Use Unicode strings exactly as search strings; transliteration is less reliable than native script.

## 2. Official Source Routes and Query Templates

### 2.1 TRCSL

Use TRCSL for license/operator context, telecom infrastructure announcements, numbering/spectrum, annual reports, and interconnection policy. Do not infer a data center solely from a telecom license.

```text
site:trc.gov.lk "data centre"
site:trc.gov.lk "data center"
site:trc.gov.lk "IDC"
site:trc.gov.lk "cloud"
site:trc.gov.lk "internet service provider"
"TRCSL" "data centre" "Sri Lanka"
"Telecommunications Regulatory Commission of Sri Lanka" "data center"
```

### 2.2 ICTA / Government Cloud

Use ICTA for LGN, Lanka Government Cloud, NDX, sovereign-cloud policy, and digital-government infrastructure. The Ministry page confirms ICTA's mandate; SLT's LGN 2.0 page confirms SLT was selected as total communication and infrastructure provider for LGN 2.0, but it does not by itself prove the physical data hall for all government workloads.

```text
site:icta.lk "data centre"
site:icta.lk "data center"
site:icta.lk "Lanka Government Cloud"
site:icta.lk "LGN 2.0"
site:icta.lk "sovereign cloud"
"Lanka Government Cloud" "data centre"
"ICTA" "National Data Exchange" "Sri Lanka"
```

### 2.3 BOI / SEZ / Port City

Use BOI and Port City for new-project discovery. A claim is facility-grade only if the announcement names a data center, operator/developer, site, and stage.

```text
site:investsrilanka.com "data centre"
site:investsrilanka.com "data center"
site:investsrilanka.com "digital infrastructure"
site:portcitycolombo.lk "data centre"
site:portcitycolombo.lk "data center"
"BOI Sri Lanka" "data centre"
"Sri Lanka Investment Forum" "data center"
```

### 2.4 Planning / Environment / Energy

Planning sources are low-discovery but useful for verifying a known project address.

```text
site:osu.uda.lk "data centre"
site:uda.gov.lk "data centre"
site:colombo.mc.gov.lk "data centre"
site:cea.lk "data centre" "EIA"
site:ceb.lk "data centre"
site:leco.lk "data centre"
"building approval" "data centre" "Sri Lanka"
"grid connection" "data centre" "Sri Lanka"
```

### 2.5 Procurement and Donor Projects

Procurement is important for government cloud upgrades, disaster recovery, server rooms, and network/data-center services.

```text
site:treasury.gov.lk/procurement "data centre"
site:treasury.gov.lk/procurement "cloud"
site:nprocom.gov.lk "data centre"
site:epms.nprocom.gov.lk "ICT"
site:ungm.org "Sri Lanka" "data centre"
site:documents.worldbank.org "Sri Lanka" "digital"
site:documents.worldbank.org "Sri Lanka" "data center"
```

### 2.6 Official Cloud-Region Absence

Official public-cloud region lists checked 2026-08-12 show **no Sri Lanka public cloud region** for AWS, Microsoft Azure, Google Cloud, or Oracle OCI. This is A-grade absence evidence only for the checked provider pages:

| Provider | Official source | Sri Lanka signal |
|---|---|---|
| AWS | https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | No Sri Lanka region; nearby India regions include Mumbai and Hyderabad |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No Sri Lanka region; India regions listed include Central India, South India, and India South Central |
| Google Cloud | https://cloud.google.com/about/locations | No Sri Lanka region visible in official locations list; re-check interactive Region Picker per batch |
| Oracle OCI | https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm | No Sri Lanka region |

Local "cloud" in Sri Lanka normally means SLT Akaza, Dialog cloud/colocation, Lankacom hosting, or ICTA Lanka Government Cloud, not a hyperscaler region.

## 3. Cable and Connectivity Anchors

Submarine Networks' Sri Lanka station page, https://www.submarinenetworks.com/en/stations/asia/sri-lanka , was live in this review and states that Sri Lanka has five cable landing stations owned by Sri Lanka Telecom, Lanka Bell, and Dialog Axiata. It also states that SLT is the sole National Backbone Network provider and connects its cable landing stations to the international backhaul hub at the SLT Welikada premises.

| Cable / station | Province | Owner / locality | Use |
|---|---|---|---|
| SMW4 and Dhiraagu-SLT | Western | SLT Colombo CLS | Critical facility / connectivity anchor |
| SMW3 and Bharat Lanka Cable System | Western | SLT Mount Lavinia CLS | Critical facility / India route |
| SMW5 | Southern | SLT Matara CLS | Only verified non-Western cable landing station |
| FALCON | Western | Lanka Bell Colombo CLS | Critical facility; operational status should be rechecked |
| BBG and Maldives Sri Lanka Cable | Western | Dialog Mount Lavinia CLS | Critical facility; MSC status should be rechecked |

Cable landing stations are not large commercial data centers by default. Count them as cable/critical facilities unless a data-center function is separately sourced.

## 4. Official / Primary Facility Seed List

| Facility / project | Province | Evidence status | Grade |
|---|---|---|---|
| SLT-Mobitel National Data Center, Pitipana-Homagama | Western | SLT official data-center page names Pitipana and Tier III services; SLT opening page says the facility opened at Pitipana-Homagama on 2018-01-16, cost more than Rs. 2.4bn, has 500 racks, and is 24 km from the SLT HQ Data Centre; Uptime country page lists SLT National Data Center, Pitipana-Homagama, with Tier III Design and Constructed Facility certifications. | A for existence, operator services, location, and Uptime certification; A/B for operator-stated rack/cost details |
| SLT HQ Data Centre / Welikada backhaul hub | Western | SLT Pitipana opening page references the SLT HQ Data Centre in Colombo; Submarine Networks names Welikada SLT premises as the international backhaul hub. | B for facility/backhaul lead unless SLT page naming HQ DC is used for the exact fact; capacity U |
| Dialog Broadband Networks Malabe Data Center #2 | Western | Uptime country page lists Dialog Broadband Networks, Malabe, Western Province, with Tier III Design and Constructed Facility certifications; Dialog 2017 official news says its Tier III Data Centre and Media Hub is at Malabe and offers hosting, colocation, and cloud services. | A for certification/location and operator-stated services |
| Dialog Data Centre, Piliyandala | Western | Dialog 2021 official news announces a fully owned data centre in Piliyandala offering hosting, co-location, and cloud services; DCD corroborates. Uptime page does not list a separate Piliyandala award in the fetched country view. | A for launch/location/operator services; U/B for any facility-specific Tier claim unless certification entry is found |
| Lankacom data center / hosting services, Colombo 07 | Western | Lankacom official pages list datacenter/cloud hosting services and company address at 65C Dharmapala Mawatha, Colombo 07. They do not publish capacity or certification. | A for service and company address; C/U for capacity/certification |
| ICTA LGN / Lanka Government Cloud estate | Western likely, with national service coverage | ICTA/ministry sources support program role; SLT LGN 2.0 page supports SLT as LGN infrastructure provider. Physical data hall mapping to SLT Pitipana is plausible but must be sourced per entry. | A for program; B/U for specific data-hall location unless primary source names it |
| National Savings Bank Production Data Center | Western / Colombo | Uptime country page lists National Savings Bank Production Data Center, Colombo, with Tier III Design Documents certification. Treat as institutional/bank facility, not public colo. | A for certification and city-level location; capacity U |
| MillenniumIT / LSEG Malabe data centre | Western | LSEG official page confirms Malabe campus address. Daily FT and Sunday Times report a privately held Tier 3 data centre at MillenniumIT in Malabe in 2015. Uptime country page fetched in this review did not list MillenniumIT by name. | A for LSEG campus; B for data-centre/Tier claim |
| Matara Cable Landing Station | Southern | Submarine Networks station page names Matara CLS for SMW5. | B/A for cable facility existence; not a commercial DC |
| Port City Colombo Business Centre | Western | Port City official site supports SEZ/development facts. No official DC-specific project verified. | A for SEZ/business centre; U for data-center claim |
| Hambantota data-center rumors | Southern | No official source found in this review. | U |

## 5. Province Coverage Matrix

Use this matrix to ensure all 9 provinces are searched. Do not mark `no_projects` until the five-pass workflow below is complete.

| Province | Districts / pivots | Official expectation |
|---|---|---|
| **Western** | Colombo, Gampaha, Kalutara; Welikada, Colombo 07, Mount Lavinia, Malabe, Piliyandala, Pitipana/Homagama, Port City | Highest-yield province. Verified operator DCs, Uptime-certified facilities, cable landings, likely government cloud hosting, IXPs, and investment-zone leads. |
| **Central** | Kandy, Matale, Nuwara Eliya | No verified commercial DC found in this review. Search universities, banks, telco POPs, BOI/ICTA programs, and cool-climate DC proposals; keep market-report growth claims at C. |
| **Southern** | Galle, Matara, Hambantota | Matara CLS is verified as a cable facility. No verified Hambantota DC project found. Search BOI/Hambantota port/energy and submarine-cable routes. |
| **Northern** | Jaffna, Kilinochchi, Mannar, Mullaitivu, Vavuniya | No verified commercial DC found. Search Jaffna university/government ICT, telco network nodes, procurement, and Tamil terms. |
| **Eastern** | Trincomalee, Batticaloa, Ampara | No verified commercial DC found. Search port/BOI/energy leads and Tamil terms. |
| **North Western** | Kurunegala, Puttalam | No verified commercial DC found. Search backbone, power, BOI zones, and institutional server rooms. |
| **North Central** | Anuradhapura, Polonnaruwa | No verified commercial DC found. Search government ICT, backbone nodes, and institutional leads. |
| **Uva** | Badulla, Moneragala | No verified commercial DC found. Negative-search default after full pass. |
| **Sabaragamuwa** | Ratnapura, Kegalle | No verified commercial DC found. Negative-search default after full pass. |

## 6. Province Workflow

For each province:

1. Run English, Sinhala, and Tamil queries for data center/data centre/cloud/hosting/colocation/server room/cable landing station.
2. Run operator queries for SLT-Mobitel, Dialog, Lankacom, Lanka Bell, Hutch, Airtel, and major banks/universities where relevant.
3. Check ICTA, Ministry of Digital Economy, BOI, Port City/Hambantota zone sources, Treasury/NPC/ePMS, UNGM, and World Bank.
4. Check cable and connectivity sources: Submarine Networks, Submarine Cable Map, TRCSL, PeeringDB/IX records as pivots.
5. Check planning/energy/environment routes for named projects: UDA, OSU, local authority, CEA, CEB, LECO.

Negative results are evidence only when the above workflow is recorded. Do not count ICT training centers, call centers, cyber labs, university e-learning platforms, ordinary telecom exchanges, or bank DR references as data centers unless the source names a facility.

## 7. Output Rules

- Use official operator names: Sri Lanka Telecom PLC / SLT-Mobitel; Dialog Axiata PLC / Dialog Broadband Networks; Lanka Communication Services (Pvt) Ltd; Lanka Bell.
- Split facts into separate evidence fields when grades differ.
- `capacity_mw` requires a source naming MW or IT load for that exact facility. Rack counts, sqm, UPS, and generator details belong in notes unless the schema has explicit fields.
- Facility addresses from aggregators are C until corroborated by operator, permit, registry, or credible press.
- Cable landing stations should be tagged as cable/critical infrastructure, not commercial colocation, unless a colocation/data-center service is separately sourced.
- Re-check volatile facts each batch: cloud-region absence, Uptime certification directory, ministry name, cable status, BOI/Port City announcements, procurement portals, and operator pages.

## 8. Verified URL Ledger

Opened and usable in this review: https://www.trc.gov.lk/ ; https://www.icta.lk/ ; https://mode.gov.lk/docs/institutions/ICTA ; https://dpa.gov.lk/ ; https://investsrilanka.com/ ; https://www.uda.gov.lk/ ; https://osu.uda.lk/ ; https://www.colombo.mc.gov.lk/building-application.php ; https://www.ceb.lk/ ; https://www.leco.lk/ ; https://www.treasury.gov.lk/procurement/procurement-notices ; https://nprocom.gov.lk/ ; https://epms.nprocom.gov.lk/ ; https://www.cert.gov.lk/ ; https://www.slt.lk/en/business/data-center ; https://www.slt.lk/en/content/slt-announces-grand-opening-state-art-tier-3-%25E2%2580%259Cnational-data-center%25E2%2580%259D-sri-lanka ; https://www.slt.lk/en/content/slt-power-lanka-government-network-lgn-20 ; https://business.dialog.lk/products-services/cloud-co-location/co-location/ ; https://dialog.lk/news/Dialog-Launches-Sri-Lankas-first-TIER-III-Certified-Data-Center-and-Media-Hub?language=en ; https://dialog.lk/news/dialog-axiata-launches-its-latest-data-centre-built-to-global-standards-in-piliyandala?language=en ; https://www.lankacom.net/ ; https://www.lankacom.net/datacenter-services/ ; https://www.submarinenetworks.com/en/stations/asia/sri-lanka ; https://uptimeinstitute.com/uptime-institute-awards/country/id/LK ; https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html ; https://learn.microsoft.com/en-us/azure/reliability/regions-list ; https://cloud.google.com/about/locations ; https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm ; https://www.portcitycolombo.lk/ ; https://www.lseg.com/en/locations/details/malabe ; https://www.ft.lk/IT-Telecom-Tech/millenniumit-launches-sri-lankas-first-privately-held-tier-3-data-centre/50-505901 .

