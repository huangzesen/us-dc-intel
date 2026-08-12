# LT Explorer Official - Lithuania Datacenter Enumeration

Date: 2026-08-12. Scope: Lithuania (LT), all 10 county divisions used by `world-manifest.jsonl`: Alytus County, Kaunas County, Klaipeda County, Marijampole County, Panevezys County, Siauliai County, Taurage County, Telsiai County, Utena County, Vilnius County.

Purpose: enumerate datacenter facilities and projects from official, regulatory, municipal, energy, register, and operator-primary sources. Use this file for final verification; use `explorer-industry.md` for broader lead generation.

Reliability grades:

- **A**: official government/regulator/register source; municipal permit/planning/PAV source; operator-owned facility/project page or operator press release; official cloud infrastructure page.
- **B**: established business/trade/construction press, peering/interconnection sources, industry association or investment-promotion material where it reports market context.
- **C**: directories, aggregators, snippets, social media, unsourced market reports, or promotional capacity claims not tied to a named project.

## 0. Lithuania Structure And Caveats

Lithuania has no public datacenter registry and no reliable datacenter-specific permit category. Build the census by joining construction records, municipality records, environmental screening, power evidence, register evidence, operator pages, and trade leads.

Counties (`apskritys`) are the required output divisions, but practical research must be municipal. Lithuania has 10 counties and 60 municipalities; county administrations were abolished in 2010, while counties remain territorial/statistical units. Municipal administrations and national authorities are the useful permit/planning sources.

Do not count a facility from a grid map, investment offer, cloud customer, telecom POP, or directory alone. Strong facility evidence needs one of:

- operator-owned page or release saying the facility exists, opened, is under construction, or is available;
- Infostatyba construction permit/completion record;
- municipal planning, council, building, or PAV/`atranka` document tied to the site;
- Real Property/Register evidence tied to a non-residential technical building;
- regulator/energy document tied to the named project or address.

Lithuanian false positives are common. `duomenu centras` may refer to a data-processing agency or office, not a datacenter. Exclude ZUDC / `Zemes ukio duomenu centras`, `Valstybes duomenu agentura`, ID Vilnius, municipal GIS/statistics units, school/server rooms, and bank/ministry "data" teams unless a hosting/colocation/cloud/HPC/telecom-infrastructure facility is explicit.

## 1. Official Source Backbone

### Construction / Permits

Use these as Grade **A** sources:

- Infostatyba main system: https://infostatyba.lt/
- Public permit/search portal: https://infostatyba.planuojustatau.lt/
- Permit detail endpoint surface: https://infostatyba.planuojustatau.lt/eInfostatyba-external/accounting/accountingPermitDetails
- Open dataset for Infostatyba records: https://data.gov.lt/datasets/3740/
- State Territorial Planning and Construction Inspectorate (VTPSI) Infostatyba page: https://vtpsi.lrv.lt/lt/veiklos-sritys-1/statyba/infostatyba/

Extract:

- `statyba leidziantis dokumentas` / permit number;
- issuing authority (usually municipality; VTPSI for certain special buildings);
- applicant/developer/operator (`statytojas`, `uzsakovas`);
- project/building purpose and building group;
- address, cadastral number, parcel;
- dates: permit, construction start, completion/`statinio uzbaigimas`;
- utility works: transformer station, 10 kV / 110 kV cable, fiber duct, cooling, generator/fuel storage.

Infostatyba may not use the phrase `duomenu centras`. Search by operator legal names, addresses, cadastral parcels, and technical terms.

### Municipal Planning / EIA / Public Consultation

Municipality pages are Grade **A** for council decisions, planning documents, public-consultation notices, construction-proposal PDFs, and environmental screening notices.

Common surfaces:

- Vilnius city: https://vilnius.lt/
- Vilnius district: https://www.vrsa.lt/
- Kaunas city: https://www.kaunas.lt/
- Klaipeda city: https://www.klaipeda.lt/
- Siauliai city: https://www.siauliai.lt/
- Panevezys city: https://www.panevezys.lt/
- Marijampole PAV announcements: https://www.marijampole.lt/aplinkotvarka-ir-infrastruktura/pranesimai-del-poveikio-aplinkai-vertinimo/1805
- Taurage PAV page: https://taurage.lt/veiklos-sritys/aplinkos-apsauga/poveikio-aplinkai-vertinimas/
- Mazeikiai PAV page: https://www.mazeikiai.lt/savivalda/administracine-informacija/veiklos-sritys/aplinkosauga/poveikio-aplinkai-vertinimas
- Varena PAV notices: https://varena.lt/aktualijos/del-poveikio-aplinkai-vertinimo-atrankos/

Search municipal pages for:

```text
"duomenu centras" "projektiniai pasiulymai"
"duomenu centro" "statybos leidimas"
"duomenu centrui" "elektros tinklai"
"duomenu centras" "tarybos sprendimas"
"duomenu centras" "atranka" OR "PAV"
"dyzeliniai generatoriai" "duomenu centras"
"silumos atgavimas" "duomenu centras"
```

### Energy / Grid / Regulator

Use these as Grade **A** for process/context, and Grade **A** facility evidence only when tied to a named project, operator, address, or parcel:

- Litgrid (TSO): https://www.litgrid.eu/index.php?lang=2
- Litgrid/TSO-DSO hosting-capacity map for Lithuania: https://www.tsodsoplatform.eu/capacitypedia/lithuania
- ESO (distribution operator): https://www.eso.lt/web/
- VERT / National Energy Regulatory Council: https://vert.lt/

Energy terms:

```text
prisijungimas prie elektros tinklu
transformatoriu pastote
transformatorine
10 kV
110 kV
330 kV
galios rezervavimas
elektros energijos vartotojo prijungimas
rezervinis maitinimas
UPS
dyzeliniai generatoriai
```

Important caution: grid capacity at Kruonis, Vilnius, Kaunas, Klaipeda, Siauliai, or Panevezys is only siting context. It is not a datacenter unless the load is tied to a datacenter project.

### Communications Regulator

Use RRT as Grade **A** regulator context, not as a facility registry:

- RRT homepage: https://rrt.lt/
- RRT English about page: https://rrt.lt/en/about-rrt/
- RRT services: https://rrt.lt/paslaugos
- RRT numbering/provider self-service: https://numeracija.rrt.lt/savitarna/
- Electronic communications provider reporting dataset: https://data.gov.lt/datasets/2727/

RRT can help identify telecom and electronic-communications operators that may operate datacenter or colocation infrastructure. It does not license datacenters as such.

### Environment / PAV

Use as Grade **A**:

- Environmental Protection Agency (AAA): https://aaa.lrv.lt/
- AAA PAV section: https://aaa.lrv.lt/lt/veiklos-sritys/poveikio-aplinkai-vertinimas-pav/
- Ministry of Environment PAV framework: https://am.lrv.lt/lt/veiklos-sritys-1/tarsos-prevencija/planuojamos-ukines-veiklos-poveikio-aplinkai-vertinimas/
- Environmental data portal: https://gamta.lt/

Datacenters may surface through generator/fuel storage, cooling/noise, heat reuse, water use, or utility-corridor screening rather than a standalone datacenter category.

### Registers

Use Registru centras as Grade **A** for legal entity, real property, parcel, and registered-building evidence:

- https://www.registrucentras.lt/

Free lookup may be limited; paid extracts may be required for parcel/building confirmation.

### Official Cloud Region Absence

Use only official pages to determine whether a public cloud region/local zone exists:

- AWS Regions and AZs: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- AWS Local Zones: https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/
- Microsoft Azure global infrastructure: https://azure.microsoft.com/en-us/explore/global-infrastructure/
- Google Cloud locations: https://cloud.google.com/about/locations
- Google Compute regions/zones: https://cloud.google.com/compute/docs/regions-zones
- Oracle Cloud regions: https://www.oracle.com/cloud/public-cloud-regions/

As of this review date, these official pages do not show a public AWS, Azure, Google Cloud, or OCI region/local zone in Lithuania. This is Grade **A** evidence for absence from public cloud-region lists; it is not evidence that these companies have no leased/network presence.

### Investment Promotion

Invest Lithuania is official and Grade **A** for what Lithuania is marketing, but realized datacenter capacity remains **C** until an operator/project/permit is found:

- Data centers page: https://investlithuania.com/data-centers/
- Kruonis article: https://investlithuania.com/news/kruonis-the-perfect-fit-for-data-centers/

Current verified use: Kruonis Technology Park in Kaisiadorys District, Kaunas County is a state-promoted greenfield datacenter location. Invest Lithuania describes 75 ha, near-term power availability around 200 MW, long-term power potential, redundant 110 kV/330 kV context, and proximity to Kruonis pumped-storage. Do not count Kruonis as an operating or committed datacenter without a named tenant plus permit/construction evidence.

## 2. Core Query Templates

Use Lithuanian without accents and with accents where possible.

```text
"duomenu centras"
"duomenu centrai"
"duomenu centro"
"duomenu centrui"
"serverine"
"serveriu talpinimas"
"serveriu kolokacija"
"kolokacija"
"hostingas"
"debesijos kompiuterija"
"kritine IT infrastruktura"
"rezervinis maitinimas"
"dyzeliniai generatoriai"
"UPS"
"transformatoriu pastote"
"10 kV" OR "110 kV" OR "330 kV"
"statybos leidimas"
"statyba leidziantis dokumentas"
"statinio uzbaigimas"
"projektiniai pasiulymai"
"atranka del poveikio aplinkai vertinimo"
"poveikio aplinkai vertinimas"
```

Permit/municipal:

```text
site:infostatyba.lt "duomenu centras"
site:infostatyba.planuojustatau.lt "duomenu"
site:data.gov.lt/datasets/3740 "duomenu"
"{operator}" "statyba leidziantis dokumentas"
"{operator}" "{address}" "statybos leidimas"
"{municipality}" "duomenu centras" "projektiniai pasiulymai"
"{municipality}" "duomenu centras" "tarybos sprendimas"
site:{municipality-domain} "duomenu centras"
site:{municipality-domain} "duomenu centro" "elektros tinklai"
filetype:pdf "duomenu centras" "statybos leidimas"
filetype:pdf "duomenu centro" "PAV"
```

Energy/environment:

```text
site:litgrid.eu "data centre" OR "duomenu centras"
site:eso.lt "duomenu centras"
site:vert.lt "duomenu centras"
site:aaa.lrv.lt "duomenu centras" OR "atranka"
"{operator}" "{municipality}" "110 kV"
"{operator}" "pastote" "duomenu centras"
"duomenu centras" "dyzeliniai generatoriai" "PAV"
"duomenu centras" "silumos atgavimas"
```

English:

```text
"Lithuania" "data center" "building permit"
"Lithuania" "data centre" "commissioned" OR "opened"
"Vilnius" "data center" "Infostatyba" OR "building permit"
"Kaunas" "data centre" "MW"
"Siauliai" "data center" "Bacloud"
"Lithuania" "data center" "110 kV" OR "grid connection"
"Kruonis" "data center" "200 MW"
"Telia" "Raisteniskes" "data center"
"Telecentras" "data center" "Vilnius"
"Delska" "Vilnius" "LT DC1"
```

## 3. Primary Facility Seeds To Verify Officially

Operator-owned sources are Grade **A** for advertised facility existence/status. Capacity and certification claims stay Grade **A** only when the operator states them directly; directory capacity remains **C**.

| Operator / project | Verified primary / strong source | Current official-method signal | Official verification action |
|---|---|---|---|
| Telia Lietuva, Raisteniskes / Vilnius district new DC | Telia project page https://www.telia.lt/ndc ; Telia company release mirrored by GlobeNewswire https://www.globenewswire.com/de/news-release/2022/01/07/2362941/0/lt/telia-lietuva-investuos-10-mln-eur%C5%B3-%C4%AF-did%C5%BEiausio-duomen%C5%B3-centro-lietuvoje-statybas.html ; LRT/BNS construction update https://www.lrt.lt/naujienos/verslas/4/2790105/telia-pradeda-26-mln-euru-vertes-duomenu-centro-statybas ; construction press https://www.statybunaujienos.lt/naujiena/Vilniaus-rajone-prasideda-26-mln-euru-vertes-duomenu-centro-statybos/25809 | Under construction in Raisteniskes, Vilnius District; planned service from 2027; investment updated from earlier EUR 10M plan to EUR 26M construction-stage reporting. | Search Infostatyba/Vilnius district for `Telia`, `Raisteniskes`, `Ukmerges g. 449`, `duomenu centras`, `Conres LT`. |
| Telecentras / AB Lietuvos radijo ir televizijos centras | https://telecentras.lt/ ; colocation https://telecentras.lt/paslaugos/kolokacijos-paslaugos/ ; state DC project https://telecentras.lt/projektai/vdc/ ; Vilnius municipal TV-tower planning note https://vilnius.lt/lt/miesto-pletra/salia-televizijos-boksto-iskils-duomenu-centras-teks-persodinti-medzius/ | Operator markets Tier III colocation/hosting and a state-datacenter program. VDC project says four state datacenters under Telecentras development. | Verify each public location through Vilnius city, Infostatyba, and Telecentras annual/project documents. Avoid inferring undisclosed secure locations. |
| Delska Lithuania / ex-DLC / Data Inn | Delska facility page https://delska.com/data-centers/ ; legal rename https://delska.com/about/news-resources/delska-newsroom/dlc-legally-becomes-delska-lithuania/ | Delska lists Vilnius LT DC1 at J. Tiskeviciaus g. 72, LT DC2 at T. Sevcenkos g. 16J, and LT DC3 at A. Juozapaviciaus g. 13. | Search Infostatyba and Vilnius for `Delska`, `Duomenu logistikos centras`, `Data Inn`, each address. |
| Bite Lietuva | Operator release https://www.bite.lt/naujienos/BITE-atidaro-isskirtinio-saugumo-duomenu-centra ; LRT/BNS https://www.lrt.lt/naujienos/verslas/4/1781109/bite-lietuva-prie-vilniaus-atidare-duomenu-centra ; DCD https://www.datacenterdynamics.com/en/news/bite-lithuania-opens-data-center-outside-vilnius/ | Bite opened a Tier III customer environment near Vilnius in 2022 inside Data Inn, operated by DLC. This is a tenant/service deployment inside an existing DC, not necessarily a separate building. | Count as Bite-operated/service footprint only if the schema allows tenant DCs; otherwise attach as tenant evidence to Delska/Data Inn. Verify existing Bite Kaunas/Vilnius DC claims via operator pages or municipal/Infostatyba before counting separate facilities. |
| Baltneta | Operator colocation page https://www.balt.net/colocation ; construction press https://www.statybunaujienos.lt/naujiena/Vilniuje-statomas-didziausias-Lietuvoje-duomenu-centras/11545 | Operator markets a dedicated Tier 3 datacenter in Vilnius with 96 cabinets; historical construction press covers a large Vilnius/Liepkalnis build. | Verify Paneriu/Liepkalnis addresses and building records through Infostatyba/Vilnius. Directory-only extra sites stay Grade C. |
| Bacloud | https://www.bacloud.com/en/our-datacenter/lithuania | Operator states its main Lithuania datacenter is in Siauliai and has operated since 2006. | Search Siauliai municipality/Infostatyba and company legal address for building proof. |
| Hostline | https://hostline.lt/duomenu-centrai/ ; https://hostline.lt/kolokacija/ | Operator states it has two Vilnius DCs / private Vilnius DC plus partner DCs. | Count only with public location/address or operator detail; otherwise use as Vilnius operator lead. |
| RackRay / Delska LT DC2 | Delska page lists T. Sevcenkos g. 16J as LT DC2; RackRay page https://www.rackray.com/ | RackRay appears to have become part of the Delska Vilnius platform; avoid double-counting RackRay separately from Delska LT DC2 unless source model tracks brands. | Verify legal/operator transition and address in Delska/RackRay sources. |
| VPSnet | https://www.vpsnet.com/lt/paslaugos/kolokacija | Operator offers colocation/Tier III service in Lithuania. | Requires address or facility owner/source before counting as separate site. |
| Cherry Servers | https://www.cherryservers.com/ | Lithuanian bare-metal/cloud operator; public pages are service evidence. | Count facility only if a Lithuanian physical site/address is documented. |
| LETAS / Serveroffer / Host Baltic | LETAS https://letas.lt/ ; Serveroffer https://serveroffer.lt/lt/serveriu-kolokacija-duomenu-centre ; Host Baltic registry lead https://rekvizitai.vz.lt/imone/host_baltic/ | Kaunas-area hosting/colocation leads. | Verify addresses, building status, and whether the "own DC" is a standalone facility through Kaunas/Kaunas district and Infostatyba. |
| Kruonis Technology Park | Invest Lithuania https://investlithuania.com/data-centers/ ; https://investlithuania.com/news/kruonis-the-perfect-fit-for-data-centers/ | Official pipeline/siting offer, not a datacenter facility. | Monitor Kaisiadorys municipality and Infostatyba for first tenant/project permit. |

## 4. Complete County And Municipality Strategy

Run every county at county level, then municipality level. Store result division as the county, and `municipality` as the operational geography.

### Alytus County

Municipalities: Alytus city, Alytus district, Druskininkai, Lazdijai district, Varena district.

Expected yield: low. No verified commercial datacenter seed found in this review.

Queries:

```text
"Alytus" "duomenu centras"
"Alytaus rajonas" "duomenu centras"
"Druskininkai" "duomenu centras" OR "serverine"
"Lazdijai" "kolokacija" OR "duomenu centras"
"Varena" "atranka" "duomenu"
site:alytus.lt "duomenu centras"
site:arsa.lt "duomenu centras"
site:druskininkusavivaldybe.lt "duomenu centras"
site:lazdijai.lt "duomenu centras"
site:varena.lt "duomenu centras" OR "atranka"
```

Mark `no_projects: true` only after checking municipality pages, Infostatyba, and PAV notices.

### Kaunas County

Municipalities: Kaunas city, Kaunas district, Birstonas, Jonava district, Kaisiadorys district, Kedainiai district, Prienai district, Raseiniai district.

Expected yield: medium. Kaunas city/district has hosting/colo leads; Kaisiadorys district contains Kruonis Technology Park pipeline.

Queries:

```text
"Kaunas" OR "Kaune" "duomenu centras"
"Kauno rajone" "duomenu centras"
Serveroffer Kaunas "duomenu centras"
LETAS Kaunas kolokacija
"Host Baltic" "Kaunas" "duomenu centras"
"Bite" "duomenu centras" "Kaunas"
"Kruonis" OR "Kruonio technologiju parkas" "duomenu centras" OR "data center"
site:kaunas.lt "duomenu centras"
site:krs.lt "duomenu centras"
site:kaisiadorys.lt "duomenu centras"
site:infostatyba.planuojustatau.lt "Kruonis"
```

Kruonis is Kaunas County but Kaisiadorys District, not Kaunas city. Keep as `planned/siting lead` until an anchor tenant and permit appear.

### Klaipeda County

Municipalities: Klaipeda city, Klaipeda district, Kretinga district, Neringa, Palanga city, Skuodas district, Silute district.

Expected yield: low-to-medium for telecom/industrial leads, no verified standalone colocation facility in this review.

Queries:

```text
"Klaipeda" "duomenu centras"
"Klaipedos LEZ" OR "Klaipeda FEZ" "data center" OR "duomenu centras"
"Klaipedos uostas" "duomenu centras"
"Palanga" "serverine" OR "duomenu centras"
site:klaipeda.lt "duomenu centras"
site:sendvaris.lt "duomenu centras"
site:kretinga.lt "duomenu centras"
site:palanga.lt "duomenu centras"
site:silute.lt "duomenu centras"
```

Treat port, FEZ, telecom regional-node, and office branches as leads only.

### Marijampole County

Municipalities: Marijampole, Kalvarija, Kazlu Ruda, Sakiai district, Vilkaviskis district.

Expected yield: low. Use PAV pages and Infostatyba.

Queries:

```text
"Marijampole" "duomenu centras"
"Kazlu Ruda" "duomenu centras"
"Sakiai" "kolokacija" OR "serverine"
"Vilkaviskis" "duomenu centras"
site:marijampole.lt "duomenu centras" OR "poveikio aplinkai"
site:kalvarija.lt "duomenu centras"
site:kazluruda.lt "duomenu centras"
site:sakiai.lt "duomenu centras"
site:vilkaviskis.lt "duomenu centras"
```

### Panevezys County

Municipalities: Panevezys city, Panevezys district, Birzai district, Kupiskis district, Pasvalys district, Rokiskis district.

Expected yield: low. Industrial/grid leads possible; beware ZUDC/agricultural-data false positives.

Queries:

```text
"Panevezys" "duomenu centras"
"Panevezio rajonas" "duomenu centras"
"Birzai" "serverine" OR "duomenu centras"
"Kupiskis" "duomenu centras"
"Pasvalys" "duomenu centras"
"Rokiskis" "duomenu centras"
site:panevezys.lt "duomenu centras"
site:panrs.lt "duomenu centras"
site:birzai.lt "duomenu centras"
site:rokiskis.lt "duomenu centras"
```

### Siauliai County

Municipalities: Siauliai city, Siauliai district, Akmene district, Joniskis district, Kelme district, Pakruojis district, Radviliskis district.

Expected yield: confirmed Bacloud in Siauliai city; otherwise low.

Queries:

```text
"Siauliai" "duomenu centras" Bacloud
"Bacloud" "Siauliai" "data center"
site:bacloud.com Siauliai data center
site:siauliai.lt "duomenu centras"
site:siauliuraj.lt "duomenu centras"
site:akmene.lt "duomenu centras"
site:joniskis.lt "duomenu centras"
site:kelme.lt "duomenu centras"
site:pakruojis.lt "duomenu centras"
site:radviliskis.lt "duomenu centras"
```

### Taurage County

Municipalities: Taurage district, Jurbarkas district, Pagegiai, Silale district.

Expected yield: low. Use municipal PAV pages.

Queries:

```text
"Taurage" "duomenu centras"
"Jurbarkas" "duomenu centras"
"Pagegiai" "serverine" OR "duomenu centras"
"Silale" "duomenu centras"
site:taurage.lt "duomenu centras" OR "poveikio aplinkai"
site:jurbarkas.lt "duomenu centras"
site:pagegiai.lt "duomenu centras"
site:silale.lt "duomenu centras"
```

### Telsiai County

Municipalities: Telsiai district, Mazeikiai district, Plunge district, Rietavas.

Expected yield: low, with industrial-power context around Mazeikiai. No facility should be counted from power/industrial context alone.

Queries:

```text
"Telsiai" "duomenu centras"
"Mazeikiai" "duomenu centras" OR "serverine"
"Mazeikiai" "PAV" "duomenu"
"Plunge" "kolokacija" OR "duomenu centras"
"Rietavas" "duomenu centras"
site:telsiai.lt "duomenu centras"
site:mazeikiai.lt "duomenu centras" OR "poveikio aplinkai"
site:plunge.lt "duomenu centras"
site:rietavas.lt "duomenu centras"
```

### Utena County

Municipalities: Utena district, Anyksciai district, Ignalina district, Moletai district, Visaginas, Zarasai district.

Expected yield: low. Visaginas/Ignalina grid-rich narratives are siting leads only.

Queries:

```text
"Utena" "duomenu centras"
"Visaginas" "duomenu centras" OR "data center"
"Ignalina" "duomenu centras"
"Moletai" "serverine"
"Anyksciai" "duomenu centras"
"Zarasai" "duomenu centras"
site:utena.lt "duomenu centras"
site:visaginas.lt "duomenu centras"
site:ignalina.lt "duomenu centras"
site:moletai.lt "duomenu centras"
site:anyksciai.lt "duomenu centras"
site:zarasai.lt "duomenu centras"
```

### Vilnius County

Municipalities: Vilnius city, Vilnius district, Elektrenai, Salcininkai district, Sirvintos district, Svencionys district, Trakai district, Ukmerge district.

Expected yield: highest. Most confirmed Lithuanian commercial colocation/operator footprint is in Vilnius city or Vilnius district.

Queries:

```text
"Vilnius" "duomenu centras" Telia Telecentras Delska Bite Baltneta Hostline RackRay VPSnet
"J. Tiskeviciaus g. 72" "duomenu centras"
"T. Sevcenkos g. 16J" "duomenu centras"
"A. Juozapaviciaus g. 13" "duomenu centras"
"Sausio 13-osios g. 10" "duomenu centras"
"Raisteniskes" "Telia" "duomenu centras"
"Ukmerges g. 449" "Telia"
"Liepkalnio" "duomenu centras" Baltneta
site:vilnius.lt "duomenu centras"
site:vrsa.lt "duomenu centras"
site:elektrenai.lt "duomenu centras"
site:trakai.lt "duomenu centras"
site:ukmerge.lt "duomenu centras"
site:infostatyba.planuojustatau.lt "Vilnius" "duomenu"
```

Known public-address pivots:

- Delska LT DC1 / Data Inn: J. Tiskeviciaus g. 72, Vilnius.
- Delska LT DC2 / RackRay legacy: T. Sevcenkos g. 16J, Vilnius.
- Delska LT DC3: A. Juozapaviciaus g. 13, Vilnius.
- Telecentras TV-tower area: Sausio 13-osios g. 10, Vilnius.
- Telia new DC: Ukmerges g. 449 / Raisteniskes, Avižieniai area, Vilnius District.
- Baltneta: verify Paneriu / Liepkalnio sites via operator/Infostatyba before final counting.

## 5. Record Fields And Status Rules

Recommended fields:

```text
name
division_county
municipality
settlement_or_city
address_or_public_location
cadastral_or_parcel_id
developer_operator
legal_entity
status
capacity_mw
racks_or_white_space
power_connection_kv
tier_or_certification
construction_evidence_url
operator_evidence_url
energy_evidence_url
register_evidence_url
evidence_date
evidence_grade
notes
```

Status rules:

- `operational`: operator says facility/service is live, municipal source says opened/commissioned, or a current facility page exists.
- `tenant/service footprint`: operator offers a branded environment inside another operator's datacenter; do not double-count as a separate building.
- `construction`: permit, construction start, groundbreaking, or contractor evidence exists, but no launch yet.
- `planned`: named site/project announced; no permit/construction evidence yet.
- `siting lead`: grid, land, FEZ, investment-promotion, or policy offer only.
- `unknown/historical`: old directory, business-register, or press lead without current operator or official evidence.

Final rule: preserve lifecycle separation. Lithuania currently has confirmed commercial/operator concentration in Vilnius, smaller verified Siauliai evidence via Bacloud, Kaunas-area hosting leads that require official verification, and a Kruonis hyperscale siting pipeline with no public anchor facility found in this review.
