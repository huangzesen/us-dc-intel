# EE Explorer Industry - Estonia Datacenter Enumeration

Date: 2026-08-12. Scope: Estonia (EE), all 15 counties: Harju, Hiiu, Ida-Viru, Jõgeva, Järva, Lääne, Lääne-Viru, Põlva, Pärnu, Rapla, Saare, Tartu, Valga, Viljandi, Võru. Angle: operators, developers, trade press, catalogs, interconnection data, contractor pages, and market signals that seed the official workflow.

Reliability grades in this industry explorer:

- **A**: first-party operator/developer page, first-party contractor release for its own scope, official company page, official cloud-region list, official IXP/association page.
- **B**: established trade press, local/regional press, public broadcaster, investment agency, association analysis, PCH/Euro-IX/Internet Society IXP data.
- **C**: DataCenterMap, Baxtel, Datacenters.com, ColoMap, Cloudscene, Inflect, DatacenterPlatform, social media, snippets, unsourced directories.

Industry evidence discovers leads. The official explorer decides whether a facility is countable through EHR, municipal planning/permits, environmental, grid, cadastral, or business-register evidence.

---

## 0. Market Shape

- Estonia is a small, Tallinn/Harju-centric colocation market. Catalogs commonly list around 9-10 Tallinn facilities, but catalog totals are **C** until every site is matched to an operator and official record. Useful catalog seeds: DataCenterMap Tallinn https://www.datacentermap.com/estonia/tallinn/ and Baxtel Estonia https://baxtel.com/data-center/estonia.
- Greenergy Data Centers / MCF Group Estonia at Hüüru, Saue vald, Harju county is the strongest large-scale live facility lead. Greenergy first-party pages advertise the largest EN 50600-certified facility in Tallinn/Baltics: https://www.greenergydatacenters.com and https://gdc.ee. Contact/address page: https://gdc.ee/est/kontaktid. DCD reports launch and 14,500 m2 / 31.5 MW build-out: https://www.datacenterdynamics.com/en/news/greenergy-launches-data-center-in-estonia/. Invest Estonia repeats the same scale claims: https://investinestonia.com/estonia-has-the-most-advanced-data-center-in-the-region/.
- The largest visible pipeline lead is Sunly's Risti Data Center Campus in Lääne-Nigula, Lääne county. First-party Sunly notice: https://sunly.ee/uudised/sunly-kavandab-eestisse-baltimaade-suurimat-andmekeskust. Municipal notice: https://www.laanenigula.ee/uudised/sunly-kavandab-eestisse-baltimaade-suurimat-andmekeskust. Project site: https://ristikampus.ai/. Treat as **planned**, not operating.
- Telco and hosting colo appears concentrated in Tallinn: Telia, Elisa, WaveCom, INFONET, and possible smaller DataHouse/Tele2-style sites from catalogs. These need de-duplication because catalog lists may mix legacy telephone exchanges, carrier PoPs, offices, and real data halls.
- Narva / Ida-Viru has a FairyHosting/Narva Datacenter catalog seed, but first-party FairyHosting currently points colocation to Telia Sõpruse/Tallinn and gives Narva as company/contact address: https://fairyhosting.com/colocation. Keep Narva as **candidate only** until official or first-party facility evidence is stronger.
- No AWS, Microsoft Azure, Google Cloud, or Oracle public cloud region is listed in Estonia on the providers' official region pages. Do not infer a hyperscale facility from customers, offices, jobs, CDN edge, Marketplace availability, or sovereign-cloud usage.
- Estonia's state ICT story (X-tee, Riigipilv, data embassies) is demand/context, not a commercial data-center inventory. RIA and Riigipilv are official context: https://www.ria.ee and https://riigipilv.ee.

---

## 1. Industry Search Patterns

### 1.1 English

```
"Estonia" "data center"
"Estonia" "data centre"
"Estonia" colocation
"Tallinn" "data center" MW
"Tallinn" "data centre" colocation
"Estonia" "data center" AI
"Estonia" "data center" investment
"Estonia" "data center" "district heating"
"Estonia" "data center" "heat reuse"
"Estonia" "data centre" permits
"Estonia" "data center" plan
"Sunly" "data center"
"Risti" "data center" Estonia
"Greenergy" "data center" Estonia
"MCF Group Estonia" "data center"
"Nebius" Estonia "data center"
site:datacenterdynamics.com Estonia "data center"
site:capacitymedia.com Estonia "data center"
site:news.err.ee "data center" Estonia
```

### 1.2 Estonian

```
andmekeskus
andmekeskus Eesti
andmekeskus Tallinn
andmekeskus Harjumaa
andmekeskus investeering
andmekeskus laienemine
andmekeskus tehisintellekt
andmekeskus AI
andmekeskus jääksoojus
andmekeskus kaugküte
andmekeskus ehitusluba
andmekeskus detailplaneering
andmekeskus "{operator}"
site:aripaev.ee andmekeskus
site:err.ee andmekeskus
site:arileht.delfi.ee andmekeskus
site:postimees.ee andmekeskus
site:le.ee andmekeskus Risti
```

### 1.3 Catalog, IXP, and Network Seeds

```
site:datacentermap.com estonia tallinn data center
site:baxtel.com "Estonia" "data center"
site:datacenters.com/locations/estonia
site:colomap.com/facilities "Estonia"
site:inflect.com Tallinn Estonia datacenter
site:peeringdb.com Tallinn Estonia
"TIX" Tallinn peering members
"Tallinn Internet Exchange" Estonia
"Estonia" IXP data center
```

---

## 2. Source List by Grade

### 2.1 Grade A in This Industry File

- Greenergy Data Centers: https://www.greenergydatacenters.com and https://gdc.ee. First-party for marketed services/status; capacity still best cross-checked with permits and contractor documents.
- Greenergy contact/address: https://gdc.ee/est/kontaktid. First-party for address and MCF legal entity.
- Sunly Risti announcement: https://sunly.ee/uudised/sunly-kavandab-eestisse-baltimaade-suurimat-andmekeskust. First-party for developer intent.
- Risti campus project site: https://ristikampus.ai/. First-party/project marketing for campus concept, secured-power claim, modules, and contact.
- Elisa carrier data-center services: https://elisa.com/carrierservices/Co-location_services_and_solutions/data-center-services/. First-party for Estonia service availability, not for a public address.
- WaveCom data-center page: https://wavecom.ee/en/andmekeskus and news/contact page https://wavecom.ee/en/news/wavecom-opened-innovative-data-center-tallinn. First-party.
- INFONET DC data-center page: https://infonetdc.com/en/data-center/ and contacts page https://infonetdc.com/en/contacts/. First-party.
- FairyHosting colocation page: https://fairyhosting.com/colocation. First-party for services offered; currently not enough to prove the Narva catalog facility.
- Telia Company data centers and colocation: https://www.teliacompany.com/en/solutions/global/data-centers-and-colocation. First-party group-level service page; local Estonia facility evidence still needs Telia Eesti/ERR/EHR.
- Official cloud-region lists for negative hyperscale checks: AWS https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ and Local Zones https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/; Azure https://azure.microsoft.com/en-us/explore/global-infrastructure/; Google Cloud https://cloud.google.com/about/locations; Google data-center locations https://datacenters.google/locations; Oracle https://www.oracle.com/cloud/public-cloud-regions/.

### 2.2 Grade B

- ERR / ERR News: https://www.err.ee and https://news.err.ee. Key URLs: Telia Tallinn project https://www.err.ee/951199/telia-ehitab-utilitase-elektrijaama-korvale-10-miljoniga-andmekeskuse; Sunly English https://news.err.ee/1609962983/renewable-energy-company-wants-to-build-baltics-largest-data-center-in-estonia; Sunly Estonian https://www.err.ee/1609962965/sunly-kavandab-laanemaale-ule-1-7-miljardi-eurost-andmekeskust; Nebius speculation https://news.err.ee/1610099740/tech-firm-nebius-hiring-push-fuels-speculation-over-estonia-data-center-plans.
- Data Centre Dynamics: https://www.datacenterdynamics.com. Key URLs: Greenergy launch https://www.datacenterdynamics.com/en/news/greenergy-launches-data-center-in-estonia/; Sunly Risti https://www.datacenterdynamics.com/en/news/sunly-plans-to-build-baltic-regions-largest-data-center-in-estonia/; older MCF groundbreaking https://www.datacenterdynamics.com/en/news/mcf-breaks-ground-estonian-data-center-campus-largest-baltics/.
- Lääne-Nigula municipal news for Sunly planning: https://www.laanenigula.ee/uudised/sunly-kavandab-eestisse-baltimaade-suurimat-andmekeskust. This is Grade A in the official file, but it is used here as a strong industry/planning news lead.
- Lääne Elu local press for Sunly: https://online.le.ee/2026/03/09/sunly-kavandab-risti-lahedale-ule-17-miljardi-eurost-andmekeskust-taiendatud-18-55/.
- Invest Estonia / Trade with Estonia: https://investinestonia.com and https://tradewithestonia.com. Useful for FDI and government-promotion context; cross-check claims.
- Caverion contractor release on MCF/Greenergy expansion: https://www.caverion.com/newsroom/releases/2026/mcf-group-estonia-chooses-caverion-as-main-contractor-for-a-eur-50-million-project-the-largest-high-security-data-centre-in-the-baltics-is-expanding/.
- Siemens Greenergy case study: https://www.siemens.com/en-us/content/greenergy-data-center/.
- Merko construction project page for MCF stage I: https://group.merko.ee/en/project/mcf-group-estonia-s-data-center-stage-i/.
- Delta Power Solutions Greenergy case study: https://www.deltapowersolutions.com/en/mcis/success-story-multiple-delta-ups-help-greenergy-data-centers-complete-prestigious-project-in-the-baltics.php.
- ITL (Estonian ICT association): https://itl.ee. Market context/member discovery only.
- Internet Society IXP tracker Estonia: https://pulse.internetsociety.org/en/ixp-tracker/country/EE/.
- PCH Tallinn Internet Exchange page: https://www.pch.net/ixp/details/68.
- Euro-IX IXPDB Tallinn Internet Exchange: https://ixpdb.euro-ix.net/en/explore/ixp/76/.
- IVIA Ida-Viru investment agency: https://ivia.ee.

### 2.3 Grade C

- DataCenterMap Estonia/Tallinn/Narva pages: https://www.datacentermap.com/estonia/tallinn/; https://www.datacentermap.com/estonia/narva/; Narva Datacenter https://www.datacentermap.com/estonia/narva/narva-datacenter/; Elisa Tallinn https://www.datacentermap.com/estonia/tallinn/elisa-tallinn/.
- Baxtel Estonia: https://baxtel.com/data-center/estonia; Greenergy page https://baxtel.com/data-center/greenergy-tallinn-dc1; Sunly Risti page https://baxtel.com/data-center/sunly-risti-estonia.
- Datacenters.com Estonia and individual listings: https://www.datacenters.com/locations/estonia.
- ColoMap Narva and Elisa pages: https://colomap.com/facilities/narva-datacenter/; https://colomap.com/facilities/elisa-tallinn/.
- DatacenterPlatform and Inflect pages for Estonia/Tallinn/Narva. Use only as address/name seeds.
- PeeringDB-only facility or network presence. Good for interconnection leads, not a facility census.

---

## 3. Player and Facility Lead Inventory

| Lead | County / municipality | Status from industry sources | Source grade | Official follow-up |
|---|---|---|---|---|
| Greenergy Data Centers / MCF Group Estonia GRE DC1 | Harju / Saue vald, Hüüru, Alajaama tee 1 | Operating large-scale colo/build-to-suite facility; commonly cited at 14,500 m2 and 31.5 MW build-out | A/B | Verify EHR, Saue permits, Äriregister reg. 14069314, cadastre. Count only once even if catalog labels it Tallinn/Harku/Saue. |
| Greenergy / MCF expansion | Harju / Saue vald | 2026 expansion/AI infrastructure lead; Caverion says technical systems expansion due autumn 2026 | B | Verify new/modified EHR building permits and Saue municipal proceedings. |
| Sunly Risti Data Center Campus | Lääne / Lääne-Nigula vald, Risti area | Planned 180 MW/184.5 MW campus, 36 ha, six modules/buildings; planning application filed | A/B | Track Lääne-Nigula detail plan, EHR permit, KOTKAS/KMH, Elering connection. Do not count as live. |
| Telia Eesti | Harju / Tallinn/Tallinn edge | Telco DC estate; ERR reported a 10m EUR facility next to Utilitas, expected H2 2021; catalogs list Sõpruse pst, Pärnu mnt, Sõle, etc. | B/C | Treat each address as a separate candidate requiring Telia/EHR/TPR confirmation. De-duplicate carrier PoPs and legacy exchanges. |
| Elisa Eesti | Harju / Tallinn, catalog address Adala/Ädala 4 | Elisa first-party offers data-center services in Estonia; catalog gives Tallinn address | A/C | Verify address and building in EHR/TPR before counting. |
| WaveCom | Harju / Tallinn, Endla 16 | First-party data-center service and opening/news/contact evidence | A | Confirm legal entity/address in Äriregister and EHR; capacity likely not public. |
| INFONET DC | Harju / Tallinn | First-party Tier-3-style standalone DC claim | A | Pull address from first-party/contact or catalogs, then EHR/TPR. |
| FairyHosting / Narva Datacenter | Ida-Viru / Narva | Catalogs list Narva DC at Mihail/Ak. Maslovi 1; FairyHosting first-party advertises colocation but references Telia Sõpruse/Tallinn and Narva contact address | C with partial A | Candidate only. Needs EHR/Narva/first-party facility confirmation. |
| Telia Valga / other legacy telco sites | Valga or other counties in catalogs | Catalog-only legacy carrier/telephone-exchange style entries | C | Do not count without current Telia first-party service page and EHR/use evidence. |
| University of Tartu / academic HPC / EENet | Tartu / national | Research/academic compute and network infrastructure | A/B context | Do not count as commercial DC unless marketed as colocation or explicitly public facility. |
| RIA / Riigipilv | Not public | State ICT infrastructure | A context | Do not enumerate non-public state facilities. |
| Nebius Estonia | No confirmed site | Hiring/speculation only | B | Watchlist only. Require operator or official site before assigning county. |

---

## 4. Division-by-Division Industry Workflow

| County | Industry sweep focus | Current lead posture |
|---|---|---|
| Harju | Tallinn, Saue, Harku, Rae, Maardu, Saku, Lääne-Harju. Search Greenergy/MCF, Telia, Elisa, WaveCom, INFONET, DataHouse, Tele2, `Tallinn data center MW`, `Harjumaa andmekeskus`, heat reuse and Utilitas terms. | Highest yield. Several operating candidates, but require official de-duplication. |
| Hiiu | Hiiumaa hosting/server-room terms, local municipality pages, small MSPs. | No confirmed commercial DC lead found in this review. |
| Ida-Viru | Narva/FairyHosting, IVIA, Narva/Sillamäe/Jõhvi industrial sites, power-zone stories, `Ida-Viru data center`, `Narva andmekeskus`. | One catalog candidate; keep C until official/first-party confirmation. |
| Jõgeva | Jõgeva, Mustvee, Põltsamaa `andmekeskus`, `serveriruum`, hosting/MSP searches. | No confirmed lead found. |
| Järva | Paide, Türi, Järva industrial and hosting searches. | No confirmed lead found. |
| Lääne | Sunly, Risti, Lääne-Nigula, Haapsalu, `Risti andmekeskus`, `Läänemaa data center`. | High-priority planned lead: Sunly Risti. |
| Lääne-Viru | Rakvere/Tapa/Viru-Nigula industrial and hosting searches. | No confirmed lead found; industrial-grid watchlist. |
| Põlva | Põlva/Räpina/Kanepi hosting and municipal references. | No confirmed lead found. |
| Pärnu | Pärnu city MSP/hosting, port/industrial areas, environmental-permit press; exclude Keskkonnaamet HQ as non-DC. | No confirmed commercial DC lead found. |
| Rapla | Kohila/Märjamaa/Rapla industrial land near Tallinn, `Raplamaa andmekeskus`. | No confirmed lead found; proximity watchlist. |
| Saare | Kuressaare/Saaremaa hosting, island grid and telecom terms. | No confirmed lead found; grid projects are context only. |
| Tartu | Tartu city/vald, University of Tartu HPC, science park, Zone/hosting/MSPs, `Tartu data center`. | Research/enterprise compute likely; no confirmed commercial colo lead in this review. |
| Valga | Valga/Tõrva/Otepää, old Telia/catalog entries, cross-border energy/heat terms. | Catalog legacy leads require strong verification; no confirmed live commercial DC. |
| Viljandi | Viljandi/Mulgi/Põhja-Sakala hosting and industrial searches. | No confirmed lead found. |
| Võru | Võru/Antsla/Rõuge/Setomaa hosting and municipal searches. | No confirmed lead found. |

Low-yield sweep:

```
"{maakond}" "andmekeskus"
"{maakond}" "data center"
"{maakond}" "serveriruum"
"{main town}" "andmekeskus"
"{main town}" "data center" colocation
"{main town}" hosting colocation
site:err.ee "{maakond}" "andmekeskus"
site:postimees.ee "{maakond}" "andmekeskus"
```

---

## 5. Watchlist and False-Positive Rules

Re-check quarterly:

- Sunly Risti: detail-plan milestones, EHR permit/start notice, KOTKAS/KMH, Elering connection, project-site capacity changes.
- Greenergy/MCF: expansion permits, contractor milestones, AI/HPC customer announcements, capacity changes.
- Nebius: any first-party or municipal confirmation. Hiring alone is not a site.
- Harju industrial municipalities: Rae, Saue, Harku, Lääne-Harju, Maardu for new high-power detailed plans.
- Ida-Viru industrial zones: Narva, Sillamäe, Jõhvi, Enefit/IVIA leads.
- Hyperscale region pages: AWS/Azure/GCP/OCI official lists only.

Common false positives:

- `andmekeskus` used for a statistical, municipal, geospatial, education, or customer-service information center.
- Enterprise server rooms in ordinary offices.
- University/research HPC not marketed as commercial colo.
- Internet exchange members or CDN/cache nodes without a facility.
- Telecom central offices/PoPs listed by catalogs but not currently marketed as data centers.
- Registered office addresses of hosting companies.

Recommended fields:

```
name
country
county
municipality
address
operator_or_developer
legal_entity
registry_code
status
capacity_mw
white_space_m2
racks
operator_evidence_url
trade_press_url
catalog_seed_url
official_followup_url
evidence_date
evidence_grade
candidate_or_countable
notes
```
