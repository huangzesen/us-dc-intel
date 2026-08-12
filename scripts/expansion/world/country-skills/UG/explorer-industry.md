# UG Explorer Industry - Uganda Datacenter Discovery via Trade Press, Operators, IXP/Subsea, and Hyperscaler/Partner Signals

Final review: 2026-08-12. Country: **UG Uganda**. Division model: **geographical region**. Complete division coverage: **Central; Eastern; Northern; Western**. This file is the industry/vendor discovery layer. Facility leads must be resolved through the official pipeline in `explorer-official.md` before being treated as A-grade facility records.

Reliability grades are per fact:
- **A** = operator-owned page, regulator/government page, official cloud-region list, or Uptime Institute record.
- **B** = established trade/local press, World Bank/MIGA/ITU document, PeeringDB for interconnection facts, industry association.
- **C** = directory/aggregator, social page, market-report snippet, uncorroborated local listing.
- **U** = unresolved lead; do not use as facility evidence.

## 0. Uganda Industry Frame

- Uganda's public datacenter market is a **Kampala-metro market** in Central region. Raxio UG1, MTN's Mutundwe evidence, UiXP, and government NITA-U NDC services are the strongest public signals.
- Eastern, Northern, and Western are not empty of digital infrastructure; they have NBI fibre, district/border connectivity, telco exchanges, service centres, bank branches, and oil/gas demand drivers. Those are watchlist signals, not datacenter records unless a source describes hosting/colo/cloud/server infrastructure.
- Uganda is landlocked. Treat subsea cable material as connectivity context only. Relevant commercial routes connect inland Uganda to coastal landing ecosystems, especially Mombasa and Dar es Salaam.
- Search both `data centre` and `data center`, and include `datacentre`, `colocation`, `carrier-neutral`, `Tier III`, `Uptime`, `racks`, `MW`, `cloud`, `hosting`, `IXP`, `peering`, `NBI`, and `DR site`.

## 1. Industry Search Vocabulary

```text
operator names: Raxio, MTN Uganda, Airtel Uganda, Roke Telkom, Roke Cloud, Liquid Intelligent Technologies Uganda, SimbaNET, Simba Fiber, Zuku, Baasa Cloud, Hostalite, Computer Point, Datanet, CSG, WIOCC, Seacom, Bayobab
facility terms: data centre, data center, datacentre, colocation, co-location, carrier neutral, cloud neutral, Tier III, Uptime Institute, racks, white space, IT power, MW, MVA
lifecycle verbs: announced, launched, opened, commissioned, certified, operational, migrated, hosted, broke ground, construction, expansion, market study
interconnection terms: UiXP, IXP, peering, PeeringDB, Communications House, Raxio Data Center, Namanve, cross-border fibre, Nairobi-Kampala, Kampala-Mombasa, Mombasa, Dar es Salaam
```

Local-language terms such as Swahili `kituo cha data`, `seva`, and `wingu` are low-yield. Use them only for supplementary outreach searches and confirm in English/operator sources.

## 2. Press and Research Sources

| Source | URL / route | Use | Grade |
|---|---|---|---|
| Data Center Dynamics | https://www.datacenterdynamics.com/en/news/ ; Uganda searches | Raxio, Equity Bank migration, Liquid Azure Stack, new DC announcements | B |
| Connecting Africa | https://www.connectingafrica.com/ | Telecom regulation, fibre, market and operator announcements | B |
| Capacity Media | https://www.capacitymedia.com/ | Carrier and fibre-route announcements | B |
| ITWeb Africa | https://itweb.africa/ | Operator appointments, Liquid/Raxio/ICT market signals | B |
| TechAfrica News | https://techafricanews.com/ | NITA-U, government ICT strategy, cloud/data-centre policy | B |
| African Business | https://african.business/ | Raxio construction/economy coverage | B |
| Daily Monitor | https://www.monitor.co.ug/ | Local policy, business, procurement and energy coverage | B/C |
| New Vision | https://www.newvision.co.ug/ | Local business and Raxio Tier III coverage | B/C |
| The Independent | https://www.independent.co.ug/ | Local telecom/energy/business coverage | B/C |
| CEO East Africa | https://www.ceo.co.ug/ | NITA-U/NBI long-form infrastructure pieces | B |
| Techjaja / PC Tech Magazine | https://techjaja.com/ ; https://pctechmag.com/ | Uganda tech press; useful for early Raxio/UCC coverage | B/C |
| MIGA | https://www.miga.org/project/raxio-data-centers-0 | Investor/ESRS context for Raxio Africa platform | B |
| ITU | https://www.itu.int/hub/publication/d-uga-nagrdg2-2025/ | Uganda National Green Data Center Strategy and Guidelines | B/A for publication existence |
| D4D Hub market brief | https://cms.d4dhub.eu/assets/Initiatives/Data-Governance-in-Africa/Digital-Investment-Facility/2507_Country-Market-Briefs/Data-Center-Market-Brief-Uganda.pdf | Market-demand context, not facility proof | B |

Press lifecycle grading: `plans` or `MoU` is intent; `construction` is pipeline; `opened`, `operational`, `certified`, or `migrated` is stronger but still needs operator/government/Uptime confirmation for A-grade facility status.

## 3. Operators and Facility Leads

| Operator / lead | Primary URL | Uganda signal | Grade and handling |
|---|---|---|---|
| Raxio UG1 | https://www.raxiogroup.com/data-centres/uganda/ ; launch release https://www.raxiogroup.com/raxio-uganda-launches-first-enterprise-grade-tier-iii-certified-carrier-neutral-data-centre/ | Enterprise-grade data centre in Namanve; opened 2021; carrier/cloud neutral; up to 400 racks and 1.5 MW IT power in operator release | **A** for existence/location/operator claims; capacity **A/B** as operator claim; reconcile any 250-rack press figure separately |
| Uptime Institute Raxio UG1 | https://uptimeinstitute.com/uptime-institute-awards/country/id/UG | Raxio Data Centre SMC Limited, Kampala, Raxio UG1, Tier III Certification of Design Documents | **A** for award listing and certification type |
| NITA-U National Data Centre | https://www.nita.go.ug/services/technical-services/nita-u-national-data-centre | Government NDC with IaaS/PaaS/managed services; 99.98% SLA claim | **A** for service existence; location unresolved unless official source found |
| NITA-U third NDC study | https://www.nita.go.ug/news-updates/nita-u-launches-data-center-market-study-report-guide-expansion-national-ict | 2025 study to guide expansion and a Third National Data Centre | **A** watchlist; not a built facility |
| MTN Uganda | https://www.mtn.co.ug/businesssolutions/data-centre/ ; archive https://www.mtn.co.ug/tag/data-centre/ | MTN markets data-centre services; MTN archive states Mutundwe switch and data center was commissioned in 2012 and houses MTN data servers | **A** for MTN service and Mutundwe existence/function; Mbuya address/name remains **C/U** if only directory-sourced |
| UiXP | https://www.uixp.co.ug/contact ; https://www.peeringdb.com/ix/422 | Peering facility #1 Communications House, 1 Colville Street, Kampala; facility #2 Raxio Data Center, Plot 781 Block 113, Namanve Industrial Park | **A** from UiXP for contact/facility locations; **B** from PeeringDB for IX/facility/peer data |
| Roke Telkom / Roke Cloud | https://business.roketelkom.co.ug/it-and-data-center-services ; https://www.roke.cloud/ | Operator markets IT/data-center services, hosting, cloud. Directory entries claim a Roke data centre at Kulubya Close, but operator pages reviewed do not clearly publish that facility record | Service claims **A**; named physical data-centre facility/address **C/U** pending primary source |
| Liquid Intelligent Technologies Uganda | https://liquid.tech/local-offices/country/uganda/ | Official Uganda office and ISP/service presence. DCD reported Liquid launched Microsoft Azure Stack in Uganda in 2024 | Company/service presence **A**; Azure Stack local cloud signal **B** from DCD unless Liquid primary release is found; physical DC location **U** |
| Airtel Uganda | https://www.airtel.africa/data-centers | Airtel Africa group markets data centres; no dedicated Uganda facility page found | Group capability **B/A at group level**; Uganda facility **U** |
| SimbaNET / Simba Fiber / Zuku | https://www.simbanet.net/ ; https://www.simbafiber.ug/ ; search current Zuku Uganda URL | ISP/fibre leads | ISP presence **B/C**; datacenter facility negative unless primary evidence found |
| Baasa Cloud | https://baasacloud.com/ plus social/contact listings | Local hosting/cloud provider; social results list 1 Water Lane, Naguru | Hosting lead **C**; datacenter facility **U/C** until primary page states facility details |
| Hostalite | https://www.hostalite.com/ | Uganda hosting/web/software provider | Hosting lead **C**; no facility evidence |
| Computer Point / Datanet / CSG | Search operator pages and URSB/UCC | Local IT/cloud/hosting leads | **U/C** until source names a data centre and location |

## 4. Interconnection and Carrier Context

- UiXP official contact page confirms two peering facilities: Communications House, 1 Colville Street, Kampala, and Raxio Data Center, Plot 781 Block 113, Namanve Industrial Park: https://www.uixp.co.ug/contact .
- PeeringDB IX 422 lists UiXP facilities including Communications House and Raxio UG1: https://www.peeringdb.com/ix/422 . Treat peer counts and port speeds as time-variable **B** data.
- Communications House PeeringDB facility page: https://www.peeringdb.com/fac/3962 . Useful for coordinates/address; grade **B** unless corroborated by UiXP/UCC.
- Seacom official newsroom listed a 2026-06-16 new high-capacity Nairobi-Kampala route: https://seacom.com/newsroom and Seacom home also surfaced the launch: https://seacom.com/ . This is **A/B** carrier evidence, not a datacenter.
- WIOCC TEAMS page states TEAMS connects Mombasa to Fujairah and extends capacity to Uganda and other East African countries through cross-border connectivity: https://www.wiocc.net/teams . Grade **B** for carrier context.
- WIOCC diversity/network page references EASSy, SEACOM, TEAMS, 2Africa, Equiano and other cable connectivity: https://www.wiocc.net/diversity . Grade **B** for subsea ecosystem context.
- Connecting Africa reported Bayobab's Kampala-Tororo-Kenya/Mombasa route signal: https://www.connectingafrica.com/fiber-networking/bayobab-connects-uganda-kenya-with-new-fiber-route . Grade **B** for fibre route; not facility evidence.

Queries:
```text
site:uixp.co.ug peering OR facility OR members
site:peeringdb.com/ix/422 Uganda OR Raxio OR Communications House
"UiXP" "Raxio" OR "Communications House"
"Uganda" "peering" "data centre"
"Nairobi-Kampala" OR "Kampala-Mombasa" fibre OR route OR capacity
"Uganda" EASSy OR TEAMS OR SEACOM OR 2Africa OR Bayobab
```

## 5. Hyperscaler / Cloud-Partner Checks

No AWS, Azure, Google Cloud, or Oracle OCI public cloud region in Uganda was present on official region lists checked on 2026-08-12:

- AWS regions: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- Azure regions: https://learn.microsoft.com/en-us/azure/reliability/regions-list and https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies
- Google Cloud locations: https://cloud.google.com/about/locations
- Oracle OCI regions: https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm and https://www.oracle.com/cloud/public-cloud-regions/

Industry rule: a local Azure Stack, partner, reseller, CDN edge, or cloud marketplace listing is a service/tenant lead only. It is not a hyperscaler cloud region and not a standalone facility record unless a source names the local facility.

Queries:
```text
"AWS" Uganda "Local Zone" OR "edge" OR "cloud region"
"Azure" Uganda "region" OR "Azure Stack" OR "edge"
"Google Cloud" Uganda "region" OR "partner"
"Oracle Cloud" Uganda "region" OR "Kenya" OR "Johannesburg"
"{hyperscaler}" Uganda partner "{operator}"
```

## 6. Per-Division Industry Approach

### Central

- Search operator pages and press for Kampala, Wakiso, Namanve/KIBP, Mukono, Entebbe, Mbuya, Mutundwe, Naguru, Bugolobi, Nakawa, Colville Street, Communications House.
- Strong public records: Raxio UG1, MTN Mutundwe, MTN data-centre services, NITA-U NDC services, UiXP facilities.
- Weak leads needing primary confirmation: Roke physical data-centre address, Liquid physical facility/Azure Stack hosting site, Baasa Cloud facility, Hostalite/Computer Point/Datanet/CSG facilities, MTN Mbuya.

### Eastern

- Search Jinja, Tororo, Mbale, Soroti, Busia, Malaba, Bujagali, border fibre, NBI, Service Uganda, telco exchange.
- Expected result: fibre/backhaul, hydro/industry, government service, and telco exchange leads. Do not mark commercial DC unless facility source says hosting/colo/cloud/server infrastructure.

### Northern

- Search Gulu, Lira, Arua, Moroto, Karamoja, West Nile, Acholi, NBI Phase V, district information centre, NGO/UN ICT, telco exchange.
- Verified signal: NITA-U Phase V/Moroto connectivity expansion; not datacenter evidence.

### Western

- Search Mbarara, Hoima, Kabaale, Kikuube, Fort Portal, Kasese, Kabale, oil, EACOP, refinery, bank DR, NBI.
- Expected result: oil/gas and regional-service watchlist; no verified commercial colocation facility in public evidence reviewed.

## 7. Query Templates

### Press Sweep
```text
site:datacenterdynamics.com/en/news Uganda "data centre" OR "data center" OR Raxio OR Liquid
site:connectingafrica.com Uganda "data centre" OR fibre OR Bayobab
site:capacitymedia.com Uganda "data centre" OR cable OR fibre
site:itweb.africa Uganda Raxio OR Liquid OR "data centre"
site:techafricanews.com Uganda "NITA-U" OR "National Data Centre"
site:african.business Uganda Raxio "data centre"
site:monitor.co.ug "data centre" OR "data center" Uganda
site:newvision.co.ug "data centre" OR Raxio
site:techjaja.com Uganda "data centre" OR UCC OR Raxio
site:pctechmag.com Uganda "data centre" OR Uptime
"Uganda" "data centre" "{operator OR town}" launched OR opened OR commissioned
```

### Operator Sweep
```text
"{operator}" Uganda "data centre" OR "data center" OR colocation OR hosting
site:{operator-domain} Uganda "data centre" OR "data center" OR cloud
"{operator}" "Uptime Institute" OR "Tier III" Uganda
"{operator}" Namanve OR KIBP OR Kampala OR Mutundwe OR Mbuya
"{operator}" "Uganda Communications Commission" licence
```

### Facilities and Directories
```text
site:datacentermap.com/uganda Kampala "data centre"
site:datacenters.com Uganda Raxio OR MTN OR Roke
site:inflect.com Kampala Uganda "data center"
site:ocolo.io "Uganda" "data centers"
```

Use directory results as **C** leads only. Resolve through operator, UCC, NEMA/planning, power, or procurement records.

## 8. Known Industry Evidence Summary

| Facility / project | Region | Industry evidence status |
|---|---|---|
| Raxio UG1 | Central | Official operator and Uptime records are strong; press corroborates launch and enterprise migrations. Best current commercial colocation record in Uganda. |
| NITA-U National Data Centre | Central | Official government NDC service page; exact physical location unresolved publicly. |
| NITA-U Third National Data Centre | Unresolved | Official 2025 market-study/watchlist item; not a built facility. |
| MTN Mutundwe | Central | MTN archive confirms switch/data center function and commissioning; directories add address details. |
| MTN Mbuya | Central | Directory lead plus MTN general DC services; needs primary facility confirmation. |
| UiXP | Central | Official two-facility peering footprint and PeeringDB corroboration; IX, not standalone colo unless separately evidenced. |
| Roke Data Centre | Central | Operator service page supports IT/data-center services; physical facility/address remains directory-led. |
| Liquid Uganda / Azure Stack | Central | Official Uganda office/service presence and DCD 2024 Azure Stack report; physical hosting site unresolved. |
| Airtel Uganda | Central/national | Group data-centre capability but no public Uganda facility page found. |
| Baasa / Hostalite / Computer Point / Datanet / CSG | Central | Local hosting/cloud leads; facility claims need primary confirmation. |
| Eastern / Northern / Western facilities | Eastern/Northern/Western | No verified commercial colocation facility found in reviewed public evidence; continue periodic negative searches. |
| Subsea landing stations | None | Uganda has no in-country landings; route evidence is terrestrial backhaul only. |

## 9. Update Cadence

| Cadence | Action |
|---|---|
| Monthly | PeeringDB UiXP and UiXP contact page; DCD/Connecting Africa/Capacity Uganda searches; Seacom/WIOCC/Bayobab route news |
| Quarterly | Operator sweeps for Raxio, MTN, Roke, Liquid, Airtel, Baasa, Hostalite, Computer Point, Datanet, CSG; local press sweeps |
| Semi-annual | Uptime Institute Uganda awards; hyperscaler region pages; ITU/D4D/World Bank market publications; UCC licensed-operator register |
| Annual | Refresh division/district coverage from UBOS/ISO; re-run all templates; re-grade C/U leads and negative regions |
| On new signal | For any launch/construction/migration claim, pivot immediately to official file: UCC, NEMA/ELMIS, KCCA/district planning, ERA/UETCL/UEDCL, UIA, PPDA/e-GP, URSB |
