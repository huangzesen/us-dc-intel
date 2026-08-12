# UG Explorer Official - Uganda Datacenter Enumeration via Regulator, Planning, Energy, e-Government, Procurement, and Cloud Sources

Final review: 2026-08-12. Country: **UG Uganda**. Division model: **geographical region**. Complete division coverage: **Central; Eastern; Northern; Western**. This file is the official/regulatory pipeline for finding and grading datacenter facilities in Uganda. Use `explorer-industry.md` for operator, press, IXP, and carrier discovery, then resolve leads back to the official sources below.

Reliability grades are per fact, not per row:
- **A** = primary/official source: regulator, law, government portal, NITA-U, PDPO, UCC, NEMA, PPDA/e-GP, ERA/UETCL/UEDCL, UIA, official cloud-region page, operator-owned facility page, Uptime Institute award page.
- **B** = strong secondary: established trade/local press, World Bank/MIGA/ITU documents, PeeringDB for interconnection facts, industry association materials.
- **C** = weak lead: directories/aggregators, social pages, uncorroborated market-report snippets.
- **U** = unresolved lead. Do not treat U-grade material as facility evidence.

## 0. Uganda-Specific Structure Facts

- Uganda has **no national public datacenter-facility register** and no single searchable national planning register. Enumeration requires joining sector regulators, district/city planning, NEMA environmental approvals, power records, government ICT procurement, operator pages, and industry evidence.
- Uganda's current top-level geographic division set is complete at **four regions: Central, Eastern, Northern, Western**. State House describes Uganda as 135 districts plus Kampala grouped into four administrative regions, and ISO 3166-2:UG defines four geographical regions plus district/city codes. Use UBOS publications for the current census/statistical names when a precise district list is needed: https://www.ubos.org/publications/statistical/ .
- Uganda is landlocked. There are **no submarine-cable landing stations in Uganda**; international connectivity arrives by terrestrial backhaul from coastal landing markets, especially Kenya/Mombasa and Tanzania/Dar es Salaam. Do not record any subsea landing station under a Uganda region.
- Public datacenter evidence is concentrated in **Central region, Kampala metro**: Kampala city, Wakiso/Namanve, Mukono corridor. Eastern, Northern, and Western should be searched seriously, but public evidence as of this review supports telecom/NBI/edge or government-service nodes rather than commercial colocation facilities.
- English dominates official records. Use both `data centre` and `data center`, plus `datacentre`, `server room`, `server farm`, `hosting`, `colocation`, `cloud`, `DR site`, `National Data Centre`, `NBI`, `Tier III`, `racks`, `MW`, `MVA`, `substation`, and named operators.

## 1. Search Vocabulary

Primary high-yield terms:
```text
data centre OR data center OR datacentre
colocation OR co-location OR carrier neutral OR carrier-neutral
cloud services OR government cloud OR IaaS OR PaaS OR managed services
server room OR server farm OR hosting OR disaster recovery OR DR site
National Data Centre OR NBI OR National Backbone Infrastructure OR UGHUB
Tier III OR Uptime Institute OR racks OR MW OR MVA OR 33kV OR 132kV
project brief OR ESIA OR environmental approval OR development permission
tender OR procurement OR e-GP OR PPDA OR ICT infrastructure
```

Secondary local-language checks have low yield. Swahili terms such as `kituo cha data`, `seva`, `wingu`, and `hifadhi ya data` can find outreach material; Luganda and other local-language technical terms are not standardized in facility records. Confirm any local-language lead against English/operator/official material before grading.

## 2. Official / Regulatory Pipeline

### 2.1 Uganda Communications Commission (UCC)

- UCC home: https://www.ucc.co.ug/ . UCC regulates communications under the Uganda Communications Act 2013. Grade **A** for regulator mandate and licensing process.
- Telecommunication licensing page: https://www.ucc.co.ug/telecommunication-licensing/ . The page states licensing communications service providers is one of UCC's responsibilities under section 5(1)(b) of the UCC Act 2013. Grade **A** for licensing framework.
- UCC eServices: https://eservices.ucc.co.ug/ and https://eservices.ucc.co.ug/applications . Account-gated but useful for application paths. Grade **A** for process, not for facility presence.
- Licensed telecom operators register: search UCC for the latest `LICENSED TELECOM OPERATORS` PDF. The 2024 register URL surfaced as https://www.ucc.co.ug/wp-content/uploads/2025/02/LICENSED-TELECOM-OPERATORS-AS-AT-30TH-DECEMBER-2024.pdf . Treat it as **A** for legal/operator names and licence classes when live; it is **not** facility evidence.
- Licence classes to search include National Telecom Operator, National Public Infrastructure Provider, National Public Service Provider, Regional Public Infrastructure Provider, and Regional Public Service Provider. A legal commentary summary of the 2020 framework is useful background only: https://www.mmaks.co.ug/articles/2020/06/10/new-licensing-framework-telecommunications-sector (**B**).

Queries:
```text
site:ucc.co.ug "data centre" OR "data center"
site:ucc.co.ug "Infrastructure Provider" "{operator}"
site:ucc.co.ug "Public Service Provider" "{operator}"
"LICENSED TELECOM OPERATORS" Uganda "{operator}"
"{operator}" "Uganda Communications Commission" licence
```

### 2.2 Planning and Environment

- Physical Planning Act, 2010: https://ulii.org/akn/ug/act/2010/8/eng@2023-12-31 . Section 35 requires development permission from a physical planning committee before development in a planning area. Grade **A** for planning-permission requirement.
- KCCA: https://www.kcca.go.ug/ . Use for Kampala planning/building-control routes and the Smart Permit process where available. Grade **A** for Kampala process; many records are not openly indexed.
- NEMA home: https://www.nema.go.ug/en/ . ESIA process: https://www.nema.go.ug/en/esia/ . The ESIA page points applicants to the Environmental Licensing and Management Information System (ELMIS) for Project Brief, ToR, and ESIA submission. Grade **A** for process.
- ELMIS portal surfaced at https://eservices.nema.go.ug/home and https://dev.nema.iras.go.ug/ . Use portal searches/status checks where accessible.

Extract from permits/ESIAs: applicant/SPV, district/city, ward/parish, plot/block, project description, floorspace, racks/IT load, transformer/MVA requirement, generator/fuel storage, water/cooling demand, NEMA certificate/reference, decision date, and local planning authority.

Queries:
```text
site:kcca.go.ug "data centre" OR "data center" OR "server room"
"{district}" "physical planning committee" "data centre"
site:nema.go.ug "data centre" OR "data center" OR "server room" OR "ICT"
"Environmental and Social Impact Assessment" Uganda "data centre"
"project brief" NEMA Uganda "{operator OR project}"
"{operator}" ESIA Uganda
```

### 2.3 Energy / Grid

- ERA: https://www.era.go.ug/ . Grade **A** for electricity-sector regulator materials.
- UETCL: https://uetcl.go.ug/ . Grade **A** for transmission projects, substations, and bulk-supply context.
- UEDCL: https://www.uedcl.co.ug/ . UEDCL states it owns/operates distribution networks below 33kV. Its history page states UEDCL took over Umeme on 2025-04-01 and resumed full operational control of the national distribution network. Grade **A** for current distributor role: https://www.uedcl.co.ug/history/ and https://www.uedcl.co.ug/mandate/ .
- ERA transition notice: https://www.era.go.ug/event/uedcl-take-over/ . Grade **A** for the 2025 transition.
- Legacy Umeme: https://www.umeme.co.ug/ . Use only for pre-April-2025 connection history.

Queries:
```text
site:era.go.ug "data centre" OR "data center"
site:uetcl.go.ug "Namanve" OR "KIBP" OR "substation" OR "MVA"
site:uedcl.co.ug "data centre" OR "data center" OR "{operator}"
site:umeme.co.ug "data centre" OR "{operator}"
"{project}" "power supply" Uganda "data centre"
"{operator}" Uganda "33kV" OR "MVA" OR "substation"
```

### 2.4 NITA-U, MoICT, and PDPO

- NITA-U home: https://www.nita.go.ug/ . Grade **A** for government ICT agency mandate.
- NITA-U National Data Centre: https://www.nita.go.ug/services/technical-services/nita-u-national-data-centre . The page describes the National Data Centre as government hosting infrastructure and lists IaaS/PaaS/managed services and a 99.98% SLA. Grade **A** for NDC existence/services; exact physical location is not published on that page.
- NITA-U co-location service: https://www.nita.go.ug/services/technical-services/co-location-tx-sites-mancenter . Grade **A** for government co-location service existence; verify the specific site before treating any location as a datacenter.
- NITA-U NBI project: https://www.nita.go.ug/projects/national-backbone-infrastructure-project-nbiegi . Grade **A** for NBI project scope. NBI nodes/fibre are not datacenters unless server-hosting evidence is present.
- NBI Phase V launch in Karamoja/Moroto: https://www.nita.go.ug/news-updates/president-yoweri-k-museveni-launches-nbi-phase-v-karamoja . NITA-U reports phases 1-4 laid 4,387 km of fibre connecting 53 district HQs, 11 border stations, and 1,480 MDAs. Grade **A** for NBI expansion; not datacenter evidence.
- NITA-U Data Center Market Study / Third National Data Centre watchlist: https://www.nita.go.ug/news-updates/nita-u-launches-data-center-market-study-report-guide-expansion-national-ict . Grade **A** for policy/project-study existence; it is not proof that the third NDC is built.
- Ministry of ICT & National Guidance: https://ict.go.ug/ . Grade **A** for policy and government-digital announcements.
- PDPO: NITA-U service page https://www.nita.go.ug/services/personal-data-protection-office and registration portal https://pdpo.go.ug/register . Data Protection and Privacy Act 2019: https://ulii.org/akn/ug/act/2019/9/eng@2019-05-03 . Grade **A** for data-protection register/process; **C** at most for facility inference.

Queries:
```text
site:nita.go.ug "National Data Centre" OR "data centre" OR "DR site" OR "cloud"
site:nita.go.ug "Third National Data Centre" OR "Data Center Market Study"
site:ict.go.ug "data centre" OR "National Backbone Infrastructure"
site:pdpo.go.ug register "{operator OR hosting company}"
"National Data Centre" Uganda "{district OR town}"
"NITA-U" "disaster recovery" Uganda
```

### 2.5 Investment and Industrial Parks

- Uganda Investment Authority: https://ugandainvest.go.ug/ . Grade **A** for investment-promotion and park materials.
- Industrial and Business Parks: https://ugandainvest.go.ug/parks/ . UIA identifies Kampala Industrial and Business Park (KIBP), Namanve, among government-owned industrial parks in the Kampala-Mukono region. Grade **A** for park existence/location; not facility evidence by itself.
- State House Investment Unit Namanve investor event: https://statehouseinvest.go.ug/news/shipu-head-graces-investors-baraza-namanve-industrial-park . Grade **A/B** for park activity.

Queries:
```text
site:ugandainvest.go.ug "data centre" OR "data center" OR "ICT"
site:ugandainvest.go.ug "Namanve" "{operator}"
"Kampala Industrial and Business Park" "data centre"
"KIBP" OR "Namanve" "Raxio" OR "cloud"
```

### 2.6 Procurement

- PPDA: https://www.ppda.go.ug/ . PPDA states it is the procurement regulator under the PPDA Act (Cap 205). Grade **A**.
- e-GP portal: https://egpuganda.go.ug/ . Grade **A** for current electronic procurement portal and supplier route.
- Search e-GP/GPP and entity procurement pages for server rooms, NDC expansion, DR sites, cloud hosting, ICT infrastructure, UPS/generator packages, and NBI works.

Queries:
```text
site:ppda.go.ug "data centre" OR "data center" OR "server" OR "cloud"
site:egpuganda.go.ug "data centre" OR "data center" OR "server" OR "NITA-U"
"{entity}" Uganda procurement "data centre" OR "disaster recovery"
"PPDA" "NITA-U" "server" OR "cloud" OR "NBI"
```

### 2.7 Registries

- URSB: https://ursb.go.ug/ . Grade **A** for company-registration processes and legal-name checks; paid/accounted searches may be required. Use https://ursb.go.ug/business-company-and-document-registration-fees/ for process context.
- OpenCorporates Uganda knowledge page: https://knowledge.opencorporates.com/knowledge-base/ug/ . Grade **C** only; use as a pointer to URSB-sourced company data, not as facility evidence.

Queries:
```text
site:ursb.go.ug "{operator legal name}"
"{operator}" "Uganda Registration Services Bureau"
"{operator}" Uganda "company number" OR "registered office"
```

### 2.8 Cloud-Region Official Checks

Rule: a hyperscaler cloud region is a Uganda facility record only if the provider's official region list shows a Uganda region and separate local facility evidence exists. As of 2026-08-12, official lists checked show **no AWS, Azure, Google Cloud, or Oracle OCI public cloud region in Uganda**.

| Provider | Official page | Uganda result | Grade |
|---|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ | No Uganda region; Africa region footprint is South Africa on the official regions page | A |
| Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list and https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies | No Uganda region; Africa geography lists South Africa North/West | A |
| Google Cloud | https://cloud.google.com/about/locations | No Uganda region; Africa public cloud region is Johannesburg (`africa-south1`) | A |
| Oracle OCI | https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm and https://www.oracle.com/cloud/public-cloud-regions/ | No Uganda region; Africa footprint includes Johannesburg and other non-UG regions/plans | A |

Queries:
```text
site:aws.amazon.com/about-aws/global-infrastructure Uganda
site:learn.microsoft.com/en-us/azure/reliability/regions-list Uganda
site:cloud.google.com/about/locations Uganda
site:docs.oracle.com/iaas/Content/General/Concepts/regions.htm Uganda
"{hyperscaler}" Uganda "cloud region" OR "availability zone" OR "Local Zone"
```

## 3. Per-Division Enumeration Approach

Use this workflow for each region: official-domain sweep, operator sweep, English spelling variants, anchor-town searches, NEMA/planning/power searches, procurement searches, then industry corroboration. Record negatives only after the sources searched are named.

### 3.1 Central

- Coverage: Kampala, Wakiso/Namanve/Entebbe/Kira, Mukono, Mpigi, Mityana, Mubende, Luwero, Nakaseke, Nakasongola, Kayunga, Kiboga, Kyankwanzi, Masaka, Kalungu, Lwengo, Lyantonde, Rakai, Kyotera, Sembabule, Gomba, Bukomansimbi, Butambala, Kalangala, Kasanda, Buikwe, Buvuma and other current Central districts/city units per UBOS/ISO.
- Expectation: **major hub**. Confirmed facility-level evidence is in Kampala metro: Raxio UG1 in Namanve/KIBP, MTN Mutundwe data center, MTN data-centre services, UiXP at Communications House and Raxio, NITA-U NDC services, plus weaker local hosting leads.
- Anchors: `Kampala`, `Wakiso`, `Namanve`, `KIBP`, `Mukono`, `Entebbe`, `Mbuya`, `Mutundwe`, `Naguru`, `Bugolobi`, `Nakawa`, `Colville Street`, `Communications House`, `Raxio`, `MTN`, `NITA-U`, `UiXP`, `Roke`, `Liquid`.

### 3.2 Eastern

- Coverage anchors: Jinja, Iganga, Bugiri, Mayuge, Namayingo, Busia, Tororo, Mbale, Sironko, Bududa, Manafwa, Namisindwa, Bulambuli, Kapchorwa, Kween, Bukwo, Kumi, Ngora, Serere, Soroti, Katakwi, Amuria, Kapelebyong, Kaberamaido, Dokolo, Kalaki, Pallisa, Kibuku, Budaka, Butaleja, Butebo, Luuka, Kamuli, Kaliro, Namutumba, Buyende, Bugweri and current Eastern districts per UBOS/ISO.
- Expectation: **low activity**. Search for telco exchanges, NBI nodes, border fibre, and government service hubs; do not grade them as datacenters without hosting/colo/server evidence.
- Anchors: `Jinja`, `Tororo`, `Mbale`, `Soroti`, `Busia`, `Malaba`, `Bujagali`, `NBI`, `Service Uganda`, `border fibre`.

### 3.3 Northern

- Coverage anchors: Gulu, Amuru, Nwoya, Omoro, Lamwo, Kitgum, Agago, Pader, Lira, Alebtong, Otuke, Oyam, Kole, Apac, Kwania, Arua, Maracha, Koboko, Yumbe, Moyo, Adjumani, Nebbi, Pakwach, Zombo, Madi-Okollo, Obongi, Moroto, Nakapiripirit, Napak, Amudat, Kotido, Kaabong, Karenga, Nabilatuk, Abim and current Northern districts per UBOS/ISO.
- Expectation: **very low activity**. NBI Phase V/Moroto is verified connectivity evidence, not datacenter evidence. Search Gulu/Lira/Arua/Moroto for telco exchanges, NBI nodes, UN/NGO ICT rooms, and procurement.
- Anchors: `Gulu`, `Lira`, `Arua`, `Moroto`, `Karamoja`, `Acholi`, `West Nile`, `NBI Phase V`, `district information centre`.

### 3.4 Western

- Coverage anchors: Mbarara, Rwampara, Isingiro, Kiruhura, Kazo, Ibanda, Bushenyi, Sheema, Mitooma, Rubirizi, Buhweju, Ntungamo, Kabale, Rubanda, Rukiga, Kisoro, Kanungu, Rukungiri, Kasese, Bundibugyo, Ntoroko, Fort Portal/Kabarole, Kyenjojo, Kamwenge, Kyegegwa, Hoima, Kikuube, Buliisa, Masindi, Kiryandongo, Kagadi, Kakumiro, Kibaale and current Western districts per UBOS/ISO.
- Expectation: **low activity, watchlist**. Search oil/gas growth around Hoima/Kabaale, bank/DR in Mbarara, and NBI nodes. Do not infer datacenters from oil, bank branch, or connectivity evidence alone.
- Anchors: `Mbarara`, `Hoima`, `Kabaale`, `Kikuube`, `Fort Portal`, `Kasese`, `Kabale`, `EACOP`, `refinery`, `bank disaster recovery`, `NBI`.

## 4. Known Officially Resolved Facilities / Projects

| Facility / project | Region / location | Evidence | Grades |
|---|---|---|---|
| Raxio UG1 Data Centre | Central - Namanve Industrial Park / KIBP, Kampala metro (Wakiso/Mukono attribution varies by source) | Operator page: https://www.raxiogroup.com/data-centres/uganda/ ; launch release: https://www.raxiogroup.com/raxio-uganda-launches-first-enterprise-grade-tier-iii-certified-carrier-neutral-data-centre/ ; Uptime country awards: https://uptimeinstitute.com/uptime-institute-awards/country/id/UG | Existence/location/carrier-neutral/Tier III claim **A** from operator; Uptime Tier III Design Documents award **A** from Uptime; 1.5 MW and up to 400 racks **A/B** from operator; any 250-rack figure from press/directories **B/C** and should be recorded separately |
| NITA-U National Data Centre | Central - Uganda government NDC; public page does not disclose exact facility address | https://www.nita.go.ug/services/technical-services/nita-u-national-data-centre ; co-location page: https://www.nita.go.ug/services/technical-services/co-location-tx-sites-mancenter | Existence/services **A**; physical site/address **U** unless another primary source is found; SLA/managed-service claims **A** as NITA-U claims |
| NITA-U Third National Data Centre study | Location not yet resolved | https://www.nita.go.ug/news-updates/nita-u-launches-data-center-market-study-report-guide-expansion-national-ict | Study/project-planning signal **A**; built facility **not established** |
| MTN Mutundwe switch and data center | Central - Mutundwe, Kampala | MTN tag/archive page: https://www.mtn.co.ug/tag/data-centre/ ; MTN services page: https://www.mtn.co.ug/businesssolutions/data-centre/ | Mutundwe data center existence/function **A** from MTN; address details from directories only **C** unless confirmed by MTN/planning records; enterprise DC services **A** |
| MTN Mbuya data centre | Central - Mbuya/Kampala | MTN services page confirms MTN Uganda data-centre services; named Mbuya facility is directory-sourced (e.g. DataCenterMap) | Service existence **A**; Mbuya named facility/address **C/U** until primary confirmation |
| UiXP | Central - Communications House, 1 Colville Street, Kampala; second peering facility at Raxio Data Center, Plot 781 Block 113, Namanve | UiXP contact page: https://www.uixp.co.ug/contact ; PeeringDB IX: https://www.peeringdb.com/ix/422 ; PeeringDB facility: https://www.peeringdb.com/fac/3962 | IX and facility locations **A/B**; peer counts **B** and time-variable; not a commercial colocation datacenter unless separately evidenced |
| NBI fibre nodes / border points / district HQ connections | All regions | https://www.nita.go.ug/projects/national-backbone-infrastructure-project-nbiegi ; https://www.nita.go.ug/news-updates/president-yoweri-k-museveni-launches-nbi-phase-v-karamoja | National fibre/connectivity **A**; not datacenter evidence |
| Roke, Liquid, Airtel, Baasa, Hostalite, local hosting leads | Primarily Central | See industry file for operator pages and directory leads | Treat as **A** only for official company/service claims; facility existence requires primary/operator facility page or official records |

## 5. Negative and Watchlist Rules

- Eastern, Northern, and Western currently have no verified commercial colocation facility in public evidence reviewed here. Record a negative only after searching official sources plus operator/press terms.
- NBI nodes, Service Uganda centres, telecom exchanges, bank IT rooms, university labs, school server rooms, and cyber cafes are **not datacenters** unless the source says they provide hosting, colocation, cloud, or substantial server/data-centre infrastructure.
- Cloud partners/resellers do not imply a hyperscaler region or local hyperscaler facility.
- Capacity must be quoted exactly as sourced. Do not convert MVA to MW. Do not merge conflicting rack counts.
- If a new facility announcement appears, immediately search UCC, NEMA/ELMIS, district/KCCA planning, ERA/UETCL/UEDCL, UIA, PPDA/e-GP, and URSB for primary corroboration.

## 6. Update Cadence

| Cadence | Action |
|---|---|
| Monthly | UCC licence register/news; NITA-U/MoICT news; PeeringDB UiXP; UiXP contact/facilities; DCD/Capacity/Connecting Africa Uganda searches |
| Quarterly | NEMA/ELMIS and KCCA/district planning searches; UEDCL/UETCL/ERA searches; PPDA/e-GP procurement terms; UIA park/investor news |
| Semi-annual | Hyperscaler region pages; Uptime Institute Uganda awards; PDPO register searches for hosting/cloud processors; URSB legal-name checks |
| Annual | Refresh UBOS/ISO district-region coverage; re-run all query templates; update known-facility and negative-division notes |
