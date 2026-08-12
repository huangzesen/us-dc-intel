# FI Explorer - Industry, Vendors, Cloud Regions, Trade Press, and Region Query Patterns

Date: 2026-08-12. Scope: Finland datacenter enumeration methodology focused on Finnish colo/hyperscale providers, cloud regions, industry/trade sources, association sources, and repeatable region-level query patterns. Reliability grades: **A** = official/primary source or operator-owned current source; **B** = established trade press, association, municipal economic-development page, or legal analysis requiring project-level verification; **C** = directories, market databases, snippets, and weak secondary leads.

---

## 0. Finland-specific frame

- Finland does not have one complete public data-center register. Practical enumeration is: **operator/developer page or trade lead -> municipality/city project page or decision item -> building/zoning/environment permit evidence -> grid/energy/district-heating cross-check -> directory/PeeringDB only for residual colo/edge sites**.
- Use Finnish terms first. Product pages use English `data center`, but local decisions and planning pages usually use `datakeskus`, `palvelinkeskus`, `konesali`, `konesalirakennus`, `tekoälydatakeskus`, `tekoälytehdas`, `pilvipalvelu`, `kolokaatio`, `rakentamislupa`, `rakennuslupa`, `rakennusvalvonta`, `kaavoitus`, `asemakaava`, `kaavamuutos`, `tonttivaraus`, `maanvuokrasopimus`, `kiinteistökauppa`, `ympäristölupa`, `YVA`, `hukkalämpö`, `kaukolämpö`, `sähköasema`, `muuntamo`, `voimajohto`, `Fingrid`, `liittymisteho`, `MW`, `MVA`, `generaattori`.
- Since Finland's 2025 Building Act vocabulary, search both **`rakennuslupa`** and **`rakentamislupa`**. Older records and trade press still use `rakennuslupa`; newer municipal pages often say `rakentamislupa`.
- Municipalities are the key official layer for commercial projects. Many major projects have city pages or meeting items, e.g. Vaasa's FCDC Kuriiritie/GigaVaasa permit page, Lahti's DayOne Kiveriö permit page, Kouvola's Hyperco Koria permit-decision item, and Lappeenranta's Pajarila/Nebius project page.
- For early-stage projects, plot reservations and municipal economic-development releases are often the first public signal. Treat these as **planned/lead** until a building permit, zoning decision, construction start, or operator commitment appears.
- Cloud-region pages are **A for logical cloud-region/zone existence**, not for exact facility addresses. Do not map Azure/AWS/GCP/OCI logical regions to a physical building unless an operator, city, permit, or official community page names the municipality/site.

---

## 1. Industry, association, and trade-press sources

### 1.1 Association and market-ecosystem sources

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| Finnish Data Center Association (FDCA) | https://www.fdca.fi/ | National industry association. Good for ecosystem framing, members/events, policy priorities, and leads such as Google Hamina expansion coverage. Not a facility registry. | B |
| FDCA policy/news | `site:fdca.fi datakeskus OR "data center" Finland Google Microsoft` | Sector priorities, electricity tax/waste heat/regulatory advocacy, association event signals. | B |
| Business Finland / Invest in Finland | https://www.businessfinland.fi/ ; `site:businessfinland.fi data center Finland` | National investment-promotion context, ecosystem events, and market positioning. Use as context, not project proof unless a specific project is named. | B |
| Finnish government / Ministry pages | https://valtioneuvosto.fi/ ; `site:valtioneuvosto.fi data centres Finland high value added` | National data-centre policy, attraction principles, power-system and value-add criteria. | A/B context |
| Fingrid | https://www.fingrid.fi/en/grid/grid-connection-agreement-phases/ ; https://fingridlehti.fi/en/data-centres-want-to-be-in-finland/ | Grid-connection process, transmission constraints, and power-system context. Useful for cross-checking 100 MW+ projects, but individual customer connections may be non-public. | A/B |
| Ryhti built-environment system | https://ryhti.syke.fi/en/data-in-the-system/ | Emerging national built-environment data system; relevant for future permit/building data normalization. Not yet a complete historical DC enumeration surface. | A context |
| Lupapiste | https://www.lupapiste.fi/ and municipal permit pages | Common electronic construction-permit workflow used by many municipalities. Public visibility varies; use municipality decision pages for public evidence. | A process |
| DLA Piper Finland permit note | https://finland.dlapiper.com/en/news/permits-and-procedures-data-centre-projects | Good legal workflow summary: zoning, construction, environmental/water/joint procedures, foreign real-estate acquisition constraints. Use for vocabulary/process, not facility count. | B |

### 1.2 Finnish and Nordic trade press

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com/ ; `site:datacenterdynamics.com Finland data center {operator|municipality}` | Best international DC trade source for Finland. Strong for new campuses, capacity, status, M&A, and hyperscale announcements; verify with operator/city where possible. | B |
| Data Center Forum / Nordic pages | https://www.datacenter-forum.com/ ; `site:datacenter-forum.com Finland datacenter {operator}` | Nordic trade/event source. Useful for Hyperco, AWS Local Zones, Microsoft/Google land/permit leads, and smaller project echoes. Verify with primary records. | B-/C+ |
| Yle | https://yle.fi/ ; `site:yle.fi datakeskus {kunta|operator}` | Strong Finnish public-broadcaster source for local controversy, land reservations, named investors, and project scale. Use especially where operator pages are thin. | B |
| Rakennuslehti | https://www.rakennuslehti.fi/ ; `site:rakennuslehti.fi datakeskus rakennuslupa` | Construction-sector source. Good for permit/application timing and contractor/contract leads, often paywalled. Verify with municipal permit decisions. | B-/C+ |
| Kauppalehti / Talouselämä / Tekniikka & Talous | `site:kauppalehti.fi datakeskus Suomi`, `site:tekniikkatalous.fi datakeskus` | Business and technology leads, company names, land transactions, financing context. Often paywalled; snippets are leads only. | C+/B- |
| Municipal economic-development sites | `Business Pori`, `Miksei Mikkeli`, `Invest in Kainuu`, `GigaVaasa`, local development companies | Often first public source for plot reservations and investment announcements. Grade A/B when city-owned or city development company; still verify permits. | A/B |
| DC Byte / Data Center Knowledge / Data Centre Magazine | `Finland data center market 2026`, `Finland data centre boom` | Market trend and pipeline context. Useful for names and scale, not final project evidence. | C+/B- |

### 1.3 Directories and interconnection sources

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| Data Center Map Finland | https://www.datacentermap.com/finland/ | Broad seed list for legacy colo/edge locations: Helsinki, Vantaa, Pori, Tampere, Turku/Raisio, etc. Verify status and ownership. | C+ |
| Baxtel Finland | https://baxtel.com/data-center/finland | Useful for hyperscale campuses, construction status, facility aliases, and coordinates; verify with operator/city. | C+ |
| Datacenters.com / DC Atlas / Cloudscene / Inflect | Queries by operator/city | Secondary address/spec leads for Equinix HE sites, Telia, Elisa, Ficolo/Verne legacy, small colos. | C |
| PeeringDB | https://www.peeringdb.com/ | Confirms interconnection presence/active facilities. Good for Helsinki colo records and IXPs, but incomplete for hyperscale. | B/C |

---

## 2. Core Finnish query patterns

### 2.1 National discovery

```text
("datakeskus" OR "palvelinkeskus" OR "data center" OR "data centre" OR "konesali") (Suomi OR Finland) (MW OR MVA OR "hukkalämpö" OR "kaukolämpö")
("tekoälydatakeskus" OR "tekoälytehdas" OR "AI factory") Finland datakeskus
site:fdca.fi ("data center" OR datakeskus) Finland
site:datacenterdynamics.com Finland "data center" {operator|city}
site:datacenter-forum.com Finland datacenter {operator|city}
site:yle.fi datakeskus {kunta|maakunta|operator}
site:rakennuslehti.fi datakeskus rakennuslupa OR rakentamislupa
site:businessfinland.fi "data center" Finland
site:fingridlehti.fi "data centres" Finland
```

### 2.2 Permit, zoning, and city-decision confirmation

```text
site:{municipality}.fi datakeskus "{kunta}" ("rakentamislupa" OR "rakennuslupa" OR "rakennusvalvonta")
site:{municipality}.fi datakeskus ("kaavoitus" OR "asemakaava" OR "kaavamuutos" OR "tonttivaraus")
site:{municipality}.fi datakeskus ("kaupunginhallitus" OR "tekninen lautakunta" OR "rakennus- ja ympäristölautakunta")
site:{municipality}.fi datakeskus ("maanvuokrasopimus" OR "kiinteistökauppa" OR "tontti")
site:{municipality}.fi ("konesalirakennus" OR "palvelinkeskus") ("sähköasema" OR "muuntamo" OR "generaattori")
site:{municipality}.fi datakeskus ("YVA" OR "ympäristölupa" OR "melu" OR "pöly" OR "louhinta")
"datakeskus" "{address OR industrial park}" "{municipality}"
"rakennuslupapäätös" datakeskus "{municipality}"
"rakentamislupa" datakeskus "{address}"
```

### 2.3 Power, heat, and grid cross-checks

```text
datakeskus "{municipality}" ("hukkalämpö" OR "kaukolämpö" OR "lämmöntalteenotto")
datakeskus "{municipality}" ("Fingrid" OR "sähköasema" OR "voimajohto" OR "liittymisteho")
datakeskus "{municipality}" ("110 kV" OR "400 kV" OR MVA OR MW)
site:fingrid.fi datakeskus OR "data center"
site:{district-heating-company-domain} datakeskus hukkalämpö {municipality}
site:fortum.com data centres Helsinki region Microsoft Espoo Kirkkonummi
```

### 2.4 Lifecycle/status vocabulary

- **Lead only**: `tonttivaraus`, `esisopimus`, `aiesopimus`, `yhteistoimintasopimus`, `selvitysvaihe`, `suunnittelee`, `valmistelee`, `alustava`, `mahdollinen`, `neuvottelut`.
- **Planning evidence**: `kaavoitus`, `asemakaava`, `kaavamuutos`, `osallistumis- ja arviointisuunnitelma`, `OAS`, `kaavaselostus`, `rakennusoikeus`, `teollisuusalue`.
- **Permit evidence**: `rakentamislupa`, `rakennuslupa`, `lupapäätös`, `rakennusvalvonta`, `teknisen lautakunnan lupajaosto`, `rakennus- ja ympäristölautakunta`, `aloittamisoikeus`.
- **Construction/operation**: `maanrakennustyöt alkavat`, `louhinta`, `rakentaminen alkaa`, `rakennustyöt`, `harjannostajaiset`, `käyttöönotto`, `toiminnassa`, operator live page, PeeringDB active facility.
- **Risk/rejected/canceled**: `valitus`, `hallinto-oikeus`, `peruttu`, `keskeytetty`, `rauennut`, `hylätty`, `muistutus`, `lausunto`, `naapurien kuuleminen`.

---

## 3. Operator, developer, and cloud pivots

Official operator pages are **A for current marketed existence/status**, **B for capacity unless exact specs are published**, and **C for exact hyperscaler physical mapping when only a cloud region or tenant relationship is known.

| Operator/developer | Official URL / lead URL | Region/city pivots | Notes |
|---|---|---|---|
| Verne / Ficolo legacy | https://www.verne.co/finland | Uusimaa/Vantaa-Helsinki, Satakunta/Pori, Pirkanmaa/Tampere | Verne says Finnish operations were previously Ficolo. Use for legacy Ficolo sites `The Air`, `The Rock`, Tampere/Pori/Vantaa; DCD reported Verne sold Tampere and Pori facilities to Glesys. |
| Glesys | https://glesys.com/locations/our-data-centers/tampere/ and Pori page | Pirkanmaa/Tampere, Satakunta/Pori | Official pages confirm operational Tampere/Pori colocation/cloud sites. |
| Equinix | https://www.equinix.com/data-centers/europe-colocation/finland-colocation ; Helsinki page https://www.equinix.com/data-centers/europe-colocation/finland-colocation/helsinki-data-centers | Uusimaa/Helsinki metro | Official page says five Finland data centers and about 7,750 sqm colocation space. Search HE1-HE7 PDFs/pages and PeeringDB for facility-level details. |
| Telia Helsinki Data Center | https://www.telia.fi/business/data-center-services/data-center/helsinki-data-center | Uusimaa/Helsinki/Pitäjänmäki-Valimotie | Official page gives Valimotie 3-5, 15,000 sqm data hall and 24 MW IT power. |
| Elisa / corporate telco facilities | https://elisa.fi/yrityksille/ and directory leads | Uusimaa, Southwest Finland/Raisio-Turku | Use Data Center Map/Baxtel/Inflect leads, then verify through Elisa, PeeringDB, and municipal/address records. |
| Google | https://datacenters.google/locations/hamina-finland ; https://cloud.google.com/about/locations | Kymenlaakso/Hamina, Kainuu/North Ostrobothnia land leads | Official Hamina campus and Google Cloud Finland region (`europe-north1`) are A. Treat Kajaani/Muhos/Vaala land reports as planned leads until city/operator confirmation. |
| Microsoft Azure | https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies ; https://local.microsoft.com/communities/emea/suomidc/ | Uusimaa/Espoo-Kirkkonummi-Vihti; Ostrobothnia/Vaasa-Mustasaari potential | Official Microsoft pages confirm intent to build Southern Finland datacenter region and community updates; Fortum identifies Espoo/Kirkkonummi heat-reuse locations. Vaasa/Mustasaari land is potential development until permits. |
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ ; Local Zones https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/ | Helsinki logical local-zone signal | AWS Local Zone is logical edge infrastructure. Do not create a physical facility record without a partner/operator/address source. |
| Oracle Cloud | https://www.oracle.com/cloud/public-cloud-regions/ | No confirmed Finnish OCI region as of this pass; Stockholm/Nordics may serve Finland | Use official region list only; do not infer Finnish facilities. |
| Nebius | https://nebius.com/newsroom/nebius-to-triple-capacity-at-finland-data-center-to-75-mw ; https://nebius.com/newsroom/nebius-to-construct-310-mw-ai-factory-in-finland | Uusimaa/Mäntsälä, South Karelia/Lappeenranta | Official pages confirm Mäntsälä expansion to 75 MW and 310 MW Lappeenranta AI factory. Pair Lappeenranta with city Pajarila project page. |
| Hyperco | https://www.hyperco.com/ plus city/TikTok pages | Kymenlaakso/Kouvola-Koria; Uusimaa/Espoo leads | Kouvola official permit and city pages are strong primary evidence for Koria/TikTok. Search Hyperco + `Hiivuri`, `Vilppulantie 96`, `Koria`. |
| DayOne | https://dayonedc.com/market/finland ; Lahti/Kouvola pages | Paijat-Hame/Lahti, Kymenlaakso/Kouvola, Uusimaa/Nurmijärvi | DayOne official Finland platform says 281 MW across Lahti/Kouvola; Lahti city and SRV verify Kiveriö construction. Nurmijärvi is early-stage until approvals. |
| Polarnode | https://www.polarnode.fi/projects/ | South Karelia/Lappeenranta, North Savo/Kuopio, Paijat-Hame/Heinola, Satakunta/Pori, Pirkanmaa/Nokia, Lapland/Keminmaa | Finnish developer with multiple municipal-stage projects. Official project pages are A for developer intent; verify permits/land with cities. |
| FCDC Corp Oy | https://fcdc.fi/ and city pages | Ostrobothnia/Vaasa, Paijat-Hame/Lahti, Pirkanmaa/Valkeakoski, Lapland/Rovaniemi | FCDC official site is general; Vaasa city permit page is A. Other FCDC projects often need city/DCD/directory triangulation. |
| Pure DC / SDC Ventures | https://puredc.com/finland | South Ostrobothnia/Seinäjoki | Official page confirms SJK01 large campus. Check Seinäjoki city land/permit pages and Microsoft tenant press carefully. |
| QTS / Blackstone | https://q.com/data-centers/forssa-en/ | Kanta-Hame/Forssa | Official QTS Forssa page confirms first Finland campus on 150 ha site; check Forssa city decisions for permits/zoning. |
| XTX Markets | official/company releases plus Invest in Kainuu | Kainuu/Kajaani | Invest in Kainuu and DCD confirm EUR 1bn+ campus/first phase; verify construction through Kajaani city and contractors. |
| CSC - IT Center for Science | https://csc.fi/en/our-expertise/data-center-ecosystem/ | Kainuu/Kajaani | Primary for public/research HPC and LUMI/LUMI-AI expansion. Enumerate separately from commercial colo if scope requires. |
| YIT | https://www.yitgroup.com/ | North Savo/Kuopio, North Karelia/Kontiolahti, North Ostrobothnia/Liminka | Developer for multiple regional site-development projects. Treat as planned until city approvals/permits. |
| AmpTank / Data Tank Nordic | https://amptank.energy/ | North Ostrobothnia/Utajärvi | Official 100 MW hyperscale + battery-storage project lead. Verify with Utajärvi/Oulu regional records. |
| ASP DC | https://www.aspdatacenter.no/ | Satakunta/Pori | Official/city pages describe Pori campus acquisition and 300-400 MW potential. Verify with Business Pori and Pori city decisions. |
| Compute Nordic / Regant / Aurora Core / Orka | Mikkeli/Miksei project pages | South Savo/Mikkeli | Mikkeli has several city-development announced projects; verify each lease/building permit separately to avoid double-counting Visulahti/Pellos/EcoSairila. |

---

## 4. Region-by-region enumeration patterns

Use the manifest region names for storage, but search Finnish region/city names and municipalities. For each region run: **operator/developer seeds -> Finnish local press/Yle -> municipal project/meeting search -> building/zoning/environment evidence -> grid/heat cross-check -> directories for small colo**.

| Region | Finnish/local search pivots | Known operator/city pivots | Query templates |
|---|---|---|---|
| Aland | `Ahvenanmaa`, `Åland`, `Maarianhamina`, `Mariehamn` | Likely telecom/server-room scale; check Ålcom/government/municipal IT rather than hyperscale. | `"datacenter" Åland`; `"datakeskus" Ahvenanmaa`; `site:alcom.ax data center`; `site:regeringen.ax datacenter OR serverhall`; `"Mariehamn" colocation`. |
| South Karelia | `Etelä-Karjala`, `Lappeenranta`, `Pajarila`, `Kettukuja`, `Imatra` | Nebius/Polarnode 310 MW Pajarila AI factory; local heat/permit pages. | `site:lappeenranta.fi Pajarila datakeskus`; `site:lappeenranta.fi Nebius datakeskus rakennuslupa`; `"Pajarilan datakeskus" Kettukuja`; `site:yle.fi Lappeenranta datakeskus Nebius`; `datakeskus Imatra Etelä-Karjala`. |
| South Ostrobothnia | `Etelä-Pohjanmaa`, `Seinäjoki`, `SJK01`, `Isojoki`, `Pettenkangas` | Pure DC/SJK01, Isojoki project lead. | `site:seinajoki.fi datakeskus Pure DC`; `site:puredc.com Finland Seinäjoki`; `"SJK01" datakeskus`; `site:isojoki.fi datakeskus Pettenkangas`; `site:yle.fi datakeskus Isojoki`. |
| South Savo | `Etelä-Savo`, `Mikkeli`, `Visulahti`, `Pellos`, `EcoSairila` | Miksei/Mikkeli cluster: Compute Nordic, Regant, Aurora Core, Orka. | `site:mikseimikkeli.fi datakeskus Mikkeli`; `site:mikkeli.fi datakeskus Visulahti`; `"Pellos" "datakeskus"`; `"EcoSairila" Orka datakeskus`; `site:mikkeli.fi rakentamislupa datakeskus`. |
| Kainuu | `Kainuu`, `Kajaani`, `Renforsin Ranta`, `Vaala`, `Kuhmo` | XTX Markets Kajaani, CSC/LUMI, Google land leads, Kuhmo feasibility. | `site:investinkainuu.fi data centre Kajaani`; `site:kajaani.fi datakeskus rakennuslupa`; `site:csc.fi Kajaani data center LUMI`; `site:yle.fi datakeskus Kajaani Google`; `"Kuhmo" datakeskus 40 MW`; `"Vaala" Google datakeskus`. |
| Kanta-Hame | `Kanta-Häme`, `Forssa`, `Hämeenlinna`, `MORE`, `Janakkala`, `Riihimäki` | QTS/Blackstone Forssa, Hämeenlinna MORE 120 MW lead. | `site:forssa.fi datakeskus QTS`; `site:q.com/data-centers/forssa-en`; `site:hameenlinna.fi datakeskus MORE`; `"Hämeenlinna" "120MW" datakeskus`; `site:yle.fi datakeskus Forssa`. |
| Central Ostrobothnia | `Keski-Pohjanmaa`, `Kokkola`, `Kaustinen`, `Kruunupyy` | No strong project found in current pass; monitor industrial power/port/renewables. | `site:kokkola.fi datakeskus`; `"Keski-Pohjanmaa" datakeskus`; `"Kokkola" "data center"`; `site:yle.fi datakeskus Kokkola`; `"Kokkola Industrial Park" datakeskus`. |
| Central Finland | `Keski-Suomi`, `Jyväskylä`, `Seppälänkangas`, `Jämsä`, `Äänekoski` | Fortum/City of Jyväskylä Seppälänkangas campus lead. | `site:jyvaskyla.fi datakeskus Seppälänkangas`; `"Fortum" Jyväskylä datakeskus`; `site:jyvaskyla.fi kaavoitus datakeskus`; `site:yle.fi datakeskus Jyväskylä`; `"Seppälänkangas" "data center"`. |
| Kymenlaakso | `Kymenlaakso`, `Hamina`, `Kouvola`, `Koria`, `Hiivuri`, `Vilppulantie`, `Kotka` | Google Hamina, Hyperco/TikTok Koria, DayOne/Hyperco Kouvola. | `site:datacenters.google Hamina Finland`; `site:kouvola.fi Hyperco datakeskus Koria`; `site:kouvola.fi rakennuslupapäätös datakeskus Vilppulantie`; `"Vilppulantie 96" datakeskus`; `site:hamina.fi Google datakeskus`; `"Koria" "second data center" Hyperco`. |
| Lapland | `Lappi`, `Rovaniemi`, `Hietavaara`, `Keminmaa`, `Kemi`, `Tornio` | FCDC Rovaniemi/Hietavaara, Polarnode Keminmaa. | `site:rovaniemi.fi datakeskus Hietavaara`; `"500MW" datakeskus Rovaniemi FCDC`; `site:polarnode.fi Keminmaa datakeskus`; `site:keminmaa.fi datakeskus`; `site:yle.fi datakeskus Lappi`. |
| Pirkanmaa | `Pirkanmaa`, `Tampere`, `Nokia`, `Valkeakoski`, `Mahlianmaa` | Glesys Tampere, Polarnode Nokia, FCDC Valkeakoski lead. | `site:glesys.com Tampere data center`; `site:nokiankaupunki.fi datakeskus Polarnode`; `site:polarnode.fi Nokia data center`; `site:valkeakoski.fi datakeskus FCDC`; `"Mahlianmaa" datakeskus`; `site:tampere.fi datakeskus konesali`. |
| Ostrobothnia | `Pohjanmaa`, `Vaasa`, `Mustasaari`, `Korsholm`, `GigaVaasa`, `Laajametsä`, `Kuriiritie` | FCDC Vaasa approved permit, Microsoft Vaasa/Mustasaari preliminary land acquisition. | `site:vaasa.fi datakeskus Kuriiritie rakentamislupa`; `site:vaasa.fi FCDC datakeskus`; `site:vaasa.fi Microsoft datakeskus Mustasaari`; `"GigaVaasa" datakeskus`; `site:mustasaari.fi datakeskus Microsoft`; `site:yle.fi datakeskus Vaasa Microsoft`. |
| North Karelia | `Pohjois-Karjala`, `Kontiolahti`, `Lehmo`, `Vellamo`, `Joensuu` | YIT/Kontiolahti Vellamo lead. | `site:kontiolahti.fi datakeskus YIT Vellamo`; `"Vellamo" Kontiolahti datakeskus`; `site:joensuu.fi datakeskus`; `site:yle.fi datakeskus Kontiolahti`; `"Lehmo" "data center"`. |
| North Ostrobothnia | `Pohjois-Pohjanmaa`, `Oulu`, `Utajärvi`, `Mustikkakangas`, `Liminka`, `Muhos`, `Ii` | Glesys/Trevian Oulu up to 300 MW, AmpTank Utajärvi 100 MW, YIT Liminka, Google Muhos land leads. | `site:ouka.fi datakeskus Oulu`; `site:trevian.fi Glesys Oulu data center`; `site:utajarvi.fi datakeskus AmpTank`; `"Mustikkakangas" datakeskus`; `site:liminka.fi datakeskus Kivimäki`; `"Muhos" Google datakeskus`; `site:yle.fi datakeskus Oulu`. |
| North Savo | `Pohjois-Savo`, `Kuopio`, `Hepomäki`, `Mustakorpi`, `Iisalmi`, `Tervamäki` | YIT Kuopio Hepomäki, Polarnode Kuopio Mustakorpi, Helios Iisalmi. | `site:kuopio.fi datakeskus Hepomäki YIT`; `site:kuopio.fi Mustakorpi datakeskus Polarnode`; `site:polarnode.fi Kuopio Mustakorpi`; `site:iisalmi.fi Helios datakeskus Tervamäki`; `site:yle.fi datakeskus Iisalmi`. |
| Paijat-Hame | `Päijät-Häme`, `Lahti`, `Kiveriö`, `Ilmarisentie`, `Väinämöisentie`, `Heinola`, `Vierumäki` | DayOne Lahti, Polarnode Heinola, FCDC Lahti. | `site:lahti.fi datakeskus Kiveriö rakentamislupa`; `site:lahti.fi Ilmarisentie datakeskus`; `"Väinämöisentie 2" datakeskus`; `site:polarnode.fi Heinola datakeskus`; `site:heinola.fi datakeskus Vierumäki`; `site:rakennuslehti.fi Lahden Kiveriö datakeskus`. |
| Satakunta | `Satakunta`, `Pori`, `Honkaluoto`, `Kivipellontie`, `Ulvila`, `Rauma` | ASP DC Pori/Ecogrid, Polarnode Pori divestment, Glesys/Verne Pori. | `site:businesspori.fi datakeskus Pori ASP DC`; `site:businesspori.fi Polarnode Honkaluoto`; `site:pori.fi datakeskus rakennuslupa`; `site:glesys.com Pori data center`; `"Kivipellontie" Pori datakeskus`; `site:yle.fi datakeskus Pori`. |
| Uusimaa | `Uusimaa`, `Helsinki`, `Espoo`, `Kirkkonummi`, `Vihti`, `Mäntsälä`, `Nurmijärvi`, `Vantaa`, `Pitäjänmäki`, `Valimotie`, `Hepokorpi`, `Kolabacken`, `Kapuli` | Microsoft Southern Finland region, Equinix Helsinki, Telia HDC, Nebius/Verne Mäntsälä, DayOne Nurmijärvi, Verne/Ficolo Vantaa. | `site:local.microsoft.com Finland datacenter Espoo Kirkkonummi Vihti`; `site:fortum.com Microsoft data centres Helsinki region`; `site:espoo.fi Microsoft datakeskus Hepokorpi`; `site:kirkkonummi.fi datakeskus Kolabacken`; `site:vihti.fi Microsoft datakeskus`; `site:mantsala.fi Nebius datakeskus Kapuli`; `site:nurmijarvi.fi DayOne datakeskus`; `site:telia.fi Helsinki Data Center Valimotie`; `site:equinix.com Finland Helsinki data centers`. |
| Southwest Finland | `Varsinais-Suomi`, `Turku`, `Raisio`, `Salo`, `Loimaa`, `Naantali` | Elisa/Raisio-Turku directory lead; monitor port/industrial and telco colos. | `site:turku.fi datakeskus rakennuslupa`; `site:raisio.fi datakeskus Elisa`; `"Elisa" Raisio Turku datakeskus`; `"Varsinais-Suomi" datakeskus`; `site:yle.fi datakeskus Turku`; `site:datacentermap.com/finland/turku datacenter`. |

---

## 5. Cloud-region handling

| Provider | Finland signal | URL | Handling |
|---|---|---|---|
| Google Cloud | Finland region `europe-north1`; Google official Hamina data center campus. | https://cloud.google.com/about/locations ; https://datacenters.google/locations/hamina-finland | A for logical region and Hamina campus. Do not use cloud-region page to infer exact buildings beyond official Hamina/location pages. |
| Microsoft Azure | Announced Southern Finland datacenter region with Availability Zones; community pages and Fortum identify Espoo/Kirkkonummi/Vihti program elements. | https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies ; https://news.microsoft.com/europe/2022/03/17/microsoft-announces-intent-to-build-a-new-datacenter-region-in-finland-accelerating-sustainable-digital-transformation-and-enabling-large-scale-carbon-free-district-heating/ ; https://local.microsoft.com/communities/emea/suomidc/ ; https://www.fortum.com/services/heating-cooling/data-centres-helsinki-region | A for region/program; verify each physical facility via municipality/permit/land pages. |
| AWS | No Finland AWS Region identified in official region list during this pass; Helsinki appears as Local Zone/edge infrastructure on AWS Local Zones pages. | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ ; https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/ | A for Local Zone logical availability only. Facility mapping remains C unless a host/operator source is found. |
| Oracle Cloud | Official OCI public regions list should be checked for current state; Nordic service often maps to Stockholm rather than Finland. | https://www.oracle.com/cloud/public-cloud-regions/ | A for official regions only; do not infer Finnish physical facilities. |
| Local/hybrid clouds | Telia, Elisa, Verne/Ficolo, Glesys, Equinix, Nebius, CSC, Hetzner/Helsinki network presence leads | Operator pages and PeeringDB | Treat operator pages as A for marketed services; directories/PeeringDB fill in facility aliases. |

---

## 6. Fast validation checklist

1. **Normalize region** to the manifest division, but search by Finnish region/city/industrial-park names.
2. **Confirm operator/developer** with an official page, city page, or signed municipal decision.
3. **Confirm physical site** with a municipality page, meeting item, building permit (`rakennuslupa`/`rakentamislupa`), zoning document, address, or land/lease decision.
4. **Classify lifecycle**: plot reservation/LOI, zoning, permit application, permit granted, construction, operational, canceled/appealed.
5. **Capacity discipline**: prefer operator/city MW; distinguish IT load from grid/electrical power. Treat directory MW and inferred campus totals as C unless primary source confirms.
6. **Power/heat cross-check** for 50 MW+ sites: search Fingrid, local DSO, district-heating company, `hukkalämpö`, `kaukolämpö`, `sähköasema`, `110 kV`, `MVA`.
7. **Avoid double-counting**: Microsoft Southern Finland region may span Espoo/Kirkkonummi/Vihti; DayOne Finland platform spans Lahti/Kouvola; Verne/Ficolo/Glesys ownership changed for Tampere/Pori; Hyperco Koria/TikTok/DayOne-related Kouvola leads may refer to adjacent phases.
