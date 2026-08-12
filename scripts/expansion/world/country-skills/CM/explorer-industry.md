# CM Explorer Industry -- Cameroon Datacenter Enumeration

Date: 2026-08-12. Country: **CM / Cameroon**. Scope: operator, market, connectivity and trade-press methodology for finding commercial, telco, sovereign-cloud, institutional and edge data-centre facilities. Coverage model: **10 regions**: Adamaoua; Centre; Far North; East; Littoral; North; North-West; West; South; South-West.

## Reliability Grades

- **A** -- official operator facility/spec page, government/regulator page naming the facility, Uptime Institute record, PeeringDB facility record, official procurement/permit/EIES/power filing, company registry/RCCM record.
- **B** -- reputable trade or local press with named site/status: Data Center Dynamics, Capacity Media, Connecting Africa, The Tech Capital, Agence Ecofin, Business in Cameroon, Investir au Cameroun, EcoMatin, Cameroon Tribune, CRTV, Journal du Cameroun, CIO Mag, IT News Africa, TechAfrica News, CEMAC Eco Finance, Digital Business Africa, The Guardian Post Cameroon, Afrik.com, Actu Cameroun, Bougna, Le Big Data.
- **C** -- directories and lead sources: Datacenter Map, Baxtel, OCOLO, Datacenters.com, Data Center Platform, DCHub, Colomap, HostDir, WHtop, SEO blogs, LinkedIn/social, reseller pages, market reports and unsourced capacity tables.

Use source grades honestly. PeeringDB is A- for facility/interconnection metadata; directories are C even when useful. Uptime "Tier III Certification of Design Documents" is A for design-award status, not constructed facility or operational certification.

## Market Facts To Preserve

- Cameroon is now a small but real local-hosting market concentrated in **Centre (Yaoundé/Zamengoé)** and **Littoral (Douala)**.
- Strong facility seeds as of 2026-08-12:
  - **Camtel NBN II / Zamengoé Data Center** -- Centre region, marketed as Yaoundé; Uptime Tier III Design Documents award; Camtel services.
  - **Camtel Bepanda** -- Littoral / Douala; PeeringDB facility with CAMIX Douala.
  - **Orange Cameroun Data Center** -- Littoral / Douala 5e / Maképé; official Orange Business page with 340-rack / three-stage specs.
  - **ST Digital Data Center** -- Littoral / Douala port zone / Douala-Bonabéri; official ST Digital and MINPOSTEL evidence.
  - **CAMPOST Data Center Yaoundé** -- Centre / Yaoundé; CAMIX and PeeringDB facility.
  - **MTN Cameroon Yaoundé DC** -- Centre / Yaoundé lead; Uptime Tier III Design Documents award, operational/commercial status not proven.
- Region attribution matters: do not file Zamengoé as a generic Yaoundé city record without the Centre/Lékié note; do not file Orange or ST Digital outside Littoral/Douala.
- No AWS, Azure, Google Cloud, Oracle OCI or Huawei Cloud public cloud region is listed in Cameroon on official region/location pages as of this review. Track CDN/edge/PoP separately from cloud-region records.
- Pan-African colo entrants remain watchlist items. Raxio and Africa Data Centres do not list Cameroon facilities in current public footprints; ST Digital is already present and should no longer be treated as just a lead.
- Subsea and IX signals matter: Camtel markets four submarine cables and national backbone services; MINPOSTEL documents NCSCS; Kribi and Douala landing stations support demand but are not data centres by themselves. CAMIX has Yaoundé and Douala presence tied to CAMPOST and Camtel Bepanda/PeeringDB evidence.

## Operator Deep Dives

### Camtel -- NBN II / Zamengoé and Bepanda

Primary URLs:
- https://www.camtel.cm/ -- official state operator site.
- https://hosting.camtel.cm/ -- Camtel hosting/data-centre services portal.
- https://uptimeinstitute.com/uptime-institute-awards/country/id/CM -- Cameroon awards list; Camtel NBN II Data Center, Tier III Certification of Design Documents.
- https://uptimeinstitute.com/uptime-institute-awards/datacenter/camtel-nbn-ii-data-center/896 -- Camtel NBN II project page; also notes Camtel earth stations at Bepanda, Zamengoe and Garoua.
- https://www.peeringdb.com/fac/10585 -- Camtel Bepanda in Douala, 5 networks, 1 local exchange, coordinates.

Current facts:
- **Zamengoé / NBN II**: Centre region; likely Lékié / Okola / Zamengoé even when marketed as Yaounde. Status: operational/marketed. Uptime lists Tier III Certification of Design Documents; do not assert constructed-facility certification unless a separate Uptime certificate appears. B-grade press reports discuss Huawei/Chinese consortium, area, cost and launch/visit chronology; use those only with source-specific qualifiers.
- **Bepanda**: Littoral / Douala / Bepanda. PeeringDB identifies it as a facility with CAMIX Douala and networks; treat as operational interconnection/telco facility. Commercial colocation at that exact site needs Camtel/operator corroboration.
- **Garoua**: Uptime background mentions an earth station. It remains a North-region telco lead, not a DC.

Queries:
```text
site:camtel.cm "Zamengoé" OR "Zamengoe" OR "NBN II" OR "datacentre" OR "data center"
site:hosting.camtel.cm "colocation" OR "hébergement" OR "cloud" OR "backup"
"Camtel NBN II Data Center" "Tier III Certification of Design Documents"
"Camtel" "Zamengoé" "130 baies" OR "3 000 m2" OR "Huawei"
site:peeringdb.com/fac "Camtel Bepanda" OR "Camtel Datacenter Zamengoe"
```

### Orange Cameroun -- Maképé Data Center

Primary URLs:
- https://business.orange.cm/fr/mieux-nous-connaitre.html -- official Orange Business Cameroun page; A for DC existence and specs.
- https://www.datacenterdynamics.com/en/news/orange-opens-data-center-in-cameroon/ -- B for 2017 launch/trade context.
- https://www.afrik.com/cameroun-le-premier-ministre-inaugure-le-data-center-de-orange-cameroun-a-douala -- B for Maképé / Douala 5e location and inauguration.
- https://cio-mag.com/le-plus-grand-et-gros-data-center-hub-de-orange-dafrique-centrale-et-de-louest-inaugure-a-douala/ -- B for inauguration narrative and 12,880 m2 complex context.

Current facts:
- **Orange Cameroun Data Center**: Littoral / Wouri / Douala 5e / Maképé. Operational since May 2017. Official Orange Business page says one Tier III+ data center, three 1,050 m2 stages, 340 racks across two white rooms, 24/7 operation, 99.82% availability statement, two separate MV public-grid sources, two fibre landing points, IP Fabric, biometric access, 49 cameras, IG55 fire suppression and 24/7 monitoring.
- Treat the Orange Business official page as A for specs, but record "Tier III+" as Orange wording unless a Uptime award/certificate is found. Use press for 16 bn FCFA / $27m and Maképé location when the final record needs ceremony context.

Queries:
```text
site:business.orange.cm "data center" OR "tiers III+" OR "340 baies"
"Orange Cameroun" "Maképé" OR "Douala 5" "data center"
"Orange Cameroun" "16 milliards" OR "$27m" OR "12 880 m2"
"Orange Business" "Cameroun" "hébergement" OR "cloud" OR "colocation"
```

### ST Digital -- Douala Port-Zone Data Center

Primary URLs:
- https://st.digital/ -- official ST Digital site; says datacenters in Douala, Grand-Bassam and Nkok.
- https://st.digital/en/cameroun -- official Cameroon page; cloud, cybersecurity, certified infrastructure, Douala address.
- https://st.digital/datacenters and https://st.digital/en/datacenters -- official datacenter pages; verify reachability each run.
- https://www.minpostel.gov.cm/index.php/fr/actualites/515-data-center-de-st-digital -- MINPOSTEL 2025-07-21 official visit article; locates the facility in the Douala port zone and says it hosts data for public and private structures.
- https://st.digital/zh_CN/blog/stds-blog-presse-3/technology-cloudstoreafrica-the-first-100-african-cloud-service-platform-made-in-cameroon-342 -- ST Digital repost/press page stating CloudStore services use servers in Cameroon in a Tier 3 datacenter installed in Douala; B/C+ for exact wording because it is a blog/press repost.

Current facts:
- **ST Digital Data Center**: Littoral / Wouri / Douala port zone / Douala-Bonabéri. Status: operational/marketed. A evidence now exists, so no longer leave this as merely "presence since 2021".
- Official materials support cloud, hosting, cybersecurity and local data-sovereignty positioning. Keep "certified" tied to ST Digital's own ISO 27001/TIA-942/HDS statements unless an independent certificate page is isolated. Do not label it Uptime Tier III without Uptime evidence.

Queries:
```text
site:st.digital "Cameroun" OR "Cameroon" "datacenter" OR "data center" OR "Douala"
site:st.digital "CloudStore" OR "cloud souverain" OR "colocation" "Cameroun"
site:minpostel.gov.cm "Data Center de ST Digital"
"ST Digital" "zone portuaire de Douala" OR "Douala-Bonabéri" "data center"
"ST Digital" "TIA-942" "Douala" OR "ISO 27001"
```

### CAMPOST and CAMIX

Primary URLs:
- https://camix.cm/ and https://www.camix.cm/membres -- CAMIX official site/member page; contact address at "Immeuble Data Center CAMPOST, BP 788 Yaoundé". Browser/search access works; automated HEAD checks may time out.
- https://www.peeringdb.com/fac/10586 -- CAMPOST Data Center Yaoundé; 3 networks, 1 local exchange, Ave Konrad Adenauer, coordinates.
- https://www.pch.net/ixp/details/1952 -- PCH CAMIX-Yaoundé record naming CAMPOST Data Center Building.
- https://armp.cm/details?id_publication=4844&type_publication=AMI -- 2024 ARMP/CAMPOST AMI; A for EPOST infrastructure containing a datacenter for hosting platforms/servers, current datacenter rehabilitation/extension, and a planned secondary datacenter in Douala. A stale CAMPOST deep link is still visible in PeeringDB but returned 404 in this run.

Current facts:
- **CAMPOST Data Center Yaoundé**: Centre / Mfoundi / Yaoundé. Operational interconnection/institutional facility. PeeringDB networks include CAMIX route-server/services and ST Digital. Classify as commercial colocation only when a live CAMPOST service page proves customer-facing colocation/hosting.

Queries:
```text
site:camix.cm "CAMPOST" OR "Data Center" OR "Yaoundé"
site:campost.cm "hébergement" OR "serveurs" OR "applications" OR "data center"
"CAMPOST Data Center Yaoundé" OR "Ave Konrad Adenauer" "PeeringDB"
```

### MTN Cameroon -- Yaoundé DC

Primary URLs:
- https://uptimeinstitute.com/uptime-institute-awards/country/id/CM -- Cameroon awards list; MTN Cameroon / Yaoundé DC / Tier III Certification of Design Documents.
- https://uptimeinstitute.com/component/tierachievement/client/mtn-cameroon/1314 -- MTN Cameroon Uptime client page.
- https://fr.uptimeinstitute.com/uptime-institute-awards/list/datacenter/yaound-dc/2228 -- French Uptime project page.
- https://mtn.cm/ and https://www.mtn.com/ -- operator identity/service context.

Current facts:
- **MTN Cameroon Yaoundé DC**: Centre / Yaoundé, exact site unknown. Status: design-awarded/project lead. A for Uptime design-award existence; C for operational/commercial status until MTN, ART, PeeringDB, procurement or press proves launch and site details.
- This is an important correction to older drafts that treated MTN only as a generic telco-internal lead.

Queries:
```text
site:uptimeinstitute.com "MTN Cameroon" "Yaoundé DC"
site:mtn.cm "data center" OR "centre de données" OR "cloud" OR "hébergement"
"MTN Cameroon" "Yaoundé DC" OR "Tier III Certification of Design Documents"
"MTN Business" "Cameroon" OR "Cameroun" "cloud" OR "hosting" OR "colocation"
```

### Nexttel/Viettel, ISPs, Banks and Enterprise Leads

- Nexttel/Viettel Cameroun: no verified public DC facility page isolated. Keep as C lead unless ART, operator pages, PeeringDB or procurement names a site.
- Yoomee, Connection Cameroon, AVS Telecom and ISPs: PeeringDB/Data Center Platform may expose network presence; only create facility records when the facility itself is named by A/B evidence.
- Banks and fintechs likely operate internal rooms in Centre/Littoral, but public facility evidence is usually absent. Use procurement, EIES, building permits and Uptime records.

Queries:
```text
"Nexttel" OR "Viettel Cameroun" "data center" OR "centre de données" OR "serveurs"
"Yoomee" OR "Connection Cameroon" OR "AVS Telecom" "data center" OR "PeeringDB"
"banque" OR "microfinance" "centre de données" "Cameroun" "Yaoundé" OR "Douala"
site:uptimeinstitute.com "Cameroon" "Data Center" -Camtel -MTN
```

## Connectivity and Interconnection Feeds

Use connectivity as demand-side and corroborating evidence, not standalone proof of a commercial data centre unless a facility is named.

- **CAMIX**: official site and PeeringDB/PCH records support Yaoundé (CAMPOST Data Center) and Douala (Camtel Bepanda/CAMIX Douala) interconnection.
- **Subsea**: SAT-3/WASC, ACE, NCSCS and SAIL are core leads. MINPOSTEL's NCSCS page is A for the state Kribi-Lagos system; trade press can support SAIL and outage context.
- **Kribi**: South-region landing/port/industrial zone potential. Treat landing stations as DC leads only.
- **Douala**: SAT-3/WASC, CAMIX Douala, Orange, ST Digital and Camtel Bepanda make Littoral the strongest commercial market.

Queries:
```text
"ACE cable" "Kribi" OR "Cameroun" "landing"
"NCSCS" "Kribi" OR "Lagos" "Cameroun"
site:minpostel.gov.cm "NCSCS" OR "submarine"
"SAIL" "Kribi" "Fortaleza" "Cameroun" OR "câble"
"SAT-3" OR "WASC" "Douala" "Cameroun"
"Medusa Africa" OR "AFR-IX" "Cameroun" OR "Kribi"
site:peeringdb.com "Cameroon" OR "Cameroun" "Facility" OR "Yaounde" OR "Douala"
site:camix.cm "CAMPOST" OR "Camtel" OR "noeud" OR "node"
```

## Hyperscaler and Cloud Region Tracking

Official pages to re-check each batch:
- AWS regions: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- AWS Local Zones: https://docs.aws.amazon.com/local-zones/latest/ug/available-local-zones.html
- Azure regions: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud locations: https://cloud.google.com/about/locations
- Oracle regions: https://www.oracle.com/africa/cloud/public-cloud-regions/ and https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm
- Huawei Cloud: https://www.huaweicloud.com/global/global_region.html

Record a negative result only as of the run date and with the official URL checked. Do not confuse partner cloud resale, CDN edges, ExpressRoute/Direct Connect partner access, or Microsoft/Orange/ST Digital partnerships with a hyperscaler public cloud region.

Queries:
```text
site:aws.amazon.com "Cameroon" "region" OR "Local Zone"
site:learn.microsoft.com "Cameroon" "Azure region"
site:cloud.google.com "Cameroon" "locations"
site:oracle.com "Cameroon" "cloud region"
site:huaweicloud.com "Cameroon" OR "Yaoundé" OR "Douala"
"AWS" OR "Azure" OR "Google Cloud" "Douala" OR "Yaoundé" "edge" OR "PoP"
```

## Trade Press and Aggregators

| Source | Grade | Use |
|---|---:|---|
| datacenterdynamics.com | B | Orange launch, Camtel/Zamengoé build context, market context. |
| capacitymedia.com / datacenterknowledge.com / connectingafrica.com / thetechcapital.com | B | African infrastructure expansion and investment stories. |
| agenceecofin.com / ecofinagency.com | B | Orange Douala, SAIL cable, telco/regulatory coverage. |
| businessincameroon.com / investiraucameroun.com | B | Official-adjacent investment, procurement and regulatory stories. |
| cameroon-tribune.cm / crtv.cm / ecomatin.net / journalducameroun.com | B-/C+ | Ceremony and policy context; verify technical specs elsewhere. |
| actucameroun.com / afrik.com / bougna.net / CIO Mag | B-/C+ | Orange/ST Digital/Douala location context; verify exact technical numbers. |
| CEMAC Eco Finance / Digital Business Africa / Le Big Data / africaneyereport | B-/C+ | Camtel/Zamengoé and sovereignty narrative; check against official/Uptime. |
| The Guardian Post Cameroon | B- | English-language regulator/operator visit coverage. |
| kamer-android.com | B-/C+ | Local detail and certification debate; never final source for Tier/rack values alone. |
| PeeringDB | A- | Facility existence, coordinates, networks and IXP presence. |
| Datacenter Map / Baxtel / OCOLO / Datacenters.com / Data Center Platform / DCHub / Colomap / HostDir / WHtop | C | Lead discovery only; never final capacity/status without stronger source. |

## Per-Region Industry Sweep

| Region | Search focus | Current expectation |
|---|---|---|
| Adamaoua | Ngaoundéré, Vina, University of Ngaoundéré, telco POPs, backbone routes, public permits. | No verified DC. |
| Centre | Yaoundé, Mfoundi, Zamengoé, Okola, Lékié, CAMPOST/CAMIX, Camtel NBN II, MTN Yaoundé DC, CENADI/CamGovCA, banks/government. | Positive and highest priority. |
| Far North | Maroua, Kousséri, Mokolo, Diamaré, Logone-et-Chari, security-context checks. | No verified DC. |
| East | Bertoua, Lom-et-Djérem, Kadey, Boumba-et-Ngoko, mining/logging corridors, backbone. | No verified DC. |
| Littoral | Douala, Wouri, Bepanda, Maképé, Douala 5e, Akwa, Bonabéri, Douala-Bonabéri, port zone, Yassa, Bassa, Nkongsamba/Moungo. | Positive: Orange, ST Digital, Camtel Bepanda, telco/ISP leads. |
| North | Garoua, Benoué, Lagdo, Guider, Mayo-Louti, Mayo-Rey. | No verified DC; Camtel Garoua earth station is a C lead. |
| North-West | Bamenda, Mezam, Kumbo, Bui, Wum, Menchum, English-language `data centre`, conflict status. | No verified DC. |
| West | Bafoussam, Mifi, Dschang, Menoua, Foumban, Noun, Mbouda, universities and DR/edge leads. | No verified DC. |
| South | Ebolowa, Kribi, Ocean, Sangmélima, Port de Kribi, ZES Kribi, NCSCS/ACE/SAIL landings. | No verified DC; highest-potential emerging zone. |
| South-West | Buea, Fako, Limbe, Tiko, Kumba, Meme, Mamfe, English-language `data centre`, port/university/telco leads. | No verified DC. |

Universal industry queries:
```text
"{region}" OR "{capital}" "data center" OR "centre de données" "Cameroun"
"{capital}" "hébergement" OR "colocation" OR "cloud" OR "serveur dédié"
"{operator}" "{region}" OR "{capital}" "Cameroun"
"{capital}" "Orange" OR "MTN" OR "Camtel" OR "Nexttel" OR "ST Digital" "cloud" OR "data center"
"{region}" "Tier III" OR "Tiers 3" OR "baies" OR "MW"
site:peeringdb.com "{capital}" OR "{region}" "CM"
"{capital}" "data centre" OR "colocation" OR "Tier III"
```

## Verification Pipeline

1. Seed from A/A- sources: Camtel/hosting pages, Orange Business page, ST Digital official pages, MINPOSTEL ST Digital visit, Uptime Cameroon list, PeeringDB fac/10585 and fac/10586, CAMIX, ART operators, MINPOSTEL NCSCS.
2. Add B-grade trade press for launch dates, location context and announced capacities: Orange 2017, Camtel/Zamengoé launch and build, ST Digital Douala port-zone context. Keep source-specific qualifiers.
3. Join official records: ART licences, MINHDU/commune permits, MINEPDED/EIES, ARSEL/ENEO/SONATREL power, MINMAP/ARMP/COLEPS procurement, RCCM/company records, Uptime, PeeringDB.
4. Run the 10-region sweep. Only mark `no_projects: true` for non-Centre/Littoral regions after French and English terms plus operator-name queries fail.
5. Normalize status: lead < announced/MoU < financed < permitted < first stone < under construction < inaugurated/launched < operational. Design-awarded is not operational.
6. De-duplicate aliases: "Camtel NBN II", "Zamengoé Data Center", "Camtel Datacenter Zamengoe-Yaounde"; "Orange DC", "Orange Business Data Center", "Maképé"; "ST Digital Douala", "CloudStore Cameroon", "Douala-Bonabéri".
7. Re-check pan-African entrants and hyperscaler pages each run because Cameroon announcements may change quickly.

## Common Pitfalls

- Treating the Zamengoé NBN II DC as Yaoundé city without a Centre/Lékié note.
- Treating Uptime design awards as constructed-facility or operational certifications.
- Leaving ST Digital as a weak 2021 lead; official/ministry evidence now supports an operational Douala data center.
- Missing MTN Cameroon Yaoundé DC because it appears in Uptime rather than MTN marketing pages.
- Copying directory rack/MW values into final records without operator/Uptime/procurement corroboration.
- Treating cable landings (Kribi, Douala), satellite earth stations (Bepanda, Zamengoé, Garoua), telco switch rooms or bank IT rooms as commercial colocation without service evidence.
- Using dead hosts as primary URLs: `cfce.cm`, `www.cfce.cm`, `www.marches-publics.cm` and `www.minepded.gov.cm` failed in this run; use `marchespublics.cm` and `minepded.gov.cm` with verification notes.
