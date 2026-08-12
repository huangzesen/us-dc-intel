# LT Explorer Industry - Lithuania Datacenter Lead Generation

Date: 2026-08-12. Scope: Lithuania (LT), all 10 county divisions: Alytus, Kaunas, Klaipeda, Marijampole, Panevezys, Siauliai, Taurage, Telsiai, Utena, Vilnius.

Purpose: find operator, trade-press, directory, peering, and market leads for datacenter enumeration, then send each candidate to `explorer-official.md` for official verification.

Reliability grades:

- **A**: operator-owned current facility/project page or operator press release; official investment-promotion page only for the promoted offer, not realized facility capacity.
- **B**: established trade/business/construction press, PeeringDB/interconnection evidence, company annual/project reports.
- **C**: directories, aggregators, social media, business-register snippets, vendor/market-report fragments.

## 0. Market Frame

Lithuania is a Vilnius-first datacenter market. Most public commercial colocation evidence is in Vilnius city or Vilnius district. Kaunas has hosting/colocation leads and telecom operator references; Siauliai has a directly advertised Bacloud facility. Klaipeda, Panevezys, Alytus, Marijampole, Taurage, Telsiai, and Utena are mostly low-yield unless an industrial, power, or municipality-specific lead appears.

No public AWS, Azure, Google Cloud, or Oracle Cloud region/local zone in Lithuania was found in the official infrastructure lists reviewed for `explorer-official.md`. Do not infer hyperscale facilities from cloud customers, offices, or MSP/reseller pages.

The national hyperscale/AI siting story is Kruonis Technology Park in Kaisiadorys District, Kaunas County, promoted by Invest Lithuania. It is a pipeline/siting lead until a named tenant plus permit/construction evidence appears.

Discovery chain:

```text
operator/trade lead
-> operator-owned page or release
-> address/legal entity aliases
-> Infostatyba / municipal / PAV verification
-> Litgrid / ESO / VERT power-context check
-> directory and peering cross-check
-> final grade and lifecycle status
```

## 1. Strong Industry And Trade Sources

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| Operator pages/releases | Telia https://www.telia.lt/ndc ; Telecentras https://telecentras.lt/ ; Delska https://delska.com/data-centers/ ; Bite https://www.bite.lt/naujienos/BITE-atidaro-isskirtinio-saugumo-duomenu-centra ; Baltneta https://www.balt.net/colocation ; Bacloud https://www.bacloud.com/en/our-datacenter/lithuania | Best non-government source for current facility existence/status. | A |
| Data Center Dynamics | https://www.datacenterdynamics.com/ ; query `site:datacenterdynamics.com Lithuania data center` and `site:datacenterdynamics.com Vilnius` | International trade coverage, including Bite/Data Inn and Telia construction. | B |
| LRT / BNS | https://www.lrt.lt/ ; query `site:lrt.lt "duomenų centras" Telia` and `site:lrt.lt "duomenų centras" Bite` | National business reporting. Verified examples: Bite 2022 Data Inn opening; Telia 2025/2026 Raisteniskes construction reports. | B |
| Verslo Zinios | https://www.vz.lt/ ; query `site:vz.lt "duomenų centras"` | Business press; useful for DLC/Data Inn, Telia, Bite, market context. | B |
| Construction press | https://www.statybunaujienos.lt/ ; https://sa.lt/ ; https://structum.lt/ | Construction-stage reporting. Verified examples: Baltneta Vilnius build; Telia Raisteniskes construction. | B |
| Made in Vilnius | https://madeinvilnius.lt/ ; query `site:madeinvilnius.lt "duomenų centras"` | Local/regional Vilnius business coverage. Good for leads; verify with operator/municipality. | B |
| Ignitis Group history | https://ignitisgrupe.lt/naujienos/itin-efektyvus-data-inn-duomenu-centras-lietuvai-pades-konkuruoti-tarptautineje-rinkoje ; https://www.vz.lt/paslaugos/2021/08/16/duomenu-logistikos-centras-plecia-duomenu-centra-data-inn--investicija-sieks-3-mln-euru | Data Inn / DLC history and ownership aliases. | B |
| Invest Lithuania | https://investlithuania.com/data-centers/ ; https://investlithuania.com/news/kruonis-the-perfect-fit-for-data-centers/ | Official FDI promotion and Kruonis siting facts. Promotional realized-capacity claims must be verified. | A for offer, C for uncommitted facility capacity |
| PeeringDB | https://www.peeringdb.com/ | Interconnection and network-presence signal. | B for peering, C for facility census |

## 2. Directories And Aggregators

Use these for aliases, addresses, and seed lists only. Do not final-count a directory entry without operator or official corroboration.

| Source | URL | Use | Grade |
|---|---|---|---|
| DataCenterMap | https://www.datacentermap.com/lithuania/ ; https://www.datacentermap.com/lithuania/vilnius/ | Vilnius facility seed list and older aliases. | C+ |
| Baxtel | https://baxtel.com/data-center/lithuania | Quick market/project leads. | C+ |
| Datacenters.com | https://www.datacenters.com/locations/lithuania | Address and provider leads. | C |
| Cloudscene | https://cloudscene.com/ | Long-tail colo/telecom leads. | C |
| ColoMap | https://colomap.com/ | Long-tail directory leads. | C |
| DataCenterCatalog | https://datacentercatalog.com/lithuania | Generic catalog. | C |
| DatacenterPlatform | https://datacenterplatform.com/data-centers/baltneta/ | Useful for Baltneta/Delska aliases; verify independently. | C |
| Inflect | https://inflect.com/ | Useful for address leads; not final proof. | C |

## 3. Operator And Project Seeds

### 3.1 Telia Lietuva

Primary sources:

- New datacenter page: https://www.telia.lt/ndc
- 2022 company release mirrored by GlobeNewswire: https://www.globenewswire.com/de/news-release/2022/01/07/2362941/0/lt/telia-lietuva-investuos-10-mln-eur%C5%B3-%C4%AF-did%C5%BEiausio-duomen%C5%B3-centro-lietuvoje-statybas.html
- LRT/BNS construction-stage article: https://www.lrt.lt/naujienos/verslas/4/2790105/telia-pradeda-26-mln-euru-vertes-duomenu-centro-statybas
- Construction press: https://www.statybunaujienos.lt/naujiena/Vilniaus-rajone-prasideda-26-mln-euru-vertes-duomenu-centro-statybos/25809
- Sweco engineering article: https://www.sweco.lt/pranesimai/naujienos/statomas-telia-duomenu-centras-bus-pirmasis-toks-baltijos-salyse/

Current signal:

- Raisteniskes / Ukmerges g. 449, Vilnius District.
- Originally announced in 2022 as a EUR 10M plan; later construction-stage reporting says EUR 26M and service expected in 2027.
- Designed to connect with two existing Telia Vilnius datacenters.

Queries:

```text
Telia "Raisteniskes" "duomenu centras"
Telia "Ukmerges g. 449"
Telia "duomenu centro statybos" "Conres LT"
site:telia.lt "duomenu centras"
site:lrt.lt "Telia" "duomenu centro statybas"
site:infostatyba.planuojustatau.lt "Telia"
```

Grade: **A** for Telia-owned project page/release; **B** for LRT/BNS/construction press; official permit still required for construction-record grade.

### 3.2 Telecentras

Primary sources:

- Homepage: https://telecentras.lt/
- Colocation: https://telecentras.lt/paslaugos/kolokacijos-paslaugos/
- State datacenter project: https://telecentras.lt/projektai/vdc/
- Vilnius municipal TV-tower planning note: https://vilnius.lt/lt/miesto-pletra/salia-televizijos-boksto-iskils-duomenu-centras-teks-persodinti-medzius/

Current signal:

- Telecentras markets Tier III colocation and hosting.
- Public project page says Telecentras is building four state datacenters (`valstybes duomenu centrai`) to Tier III availability requirements.
- TV-tower area / Sausio 13-osios g. 10 is a public location pivot; secure state sites may not disclose exact location.

Queries:

```text
Telecentras "duomenu centras" "Sausio 13-osios"
Telecentras "VDC" "duomenu centrai"
"Valstybes duomenu centru pletros projektas" Telecentras
"Saugusis duomenu perdavimo tinklas" "duomenu centras"
site:telecentras.lt "duomenu centrai"
site:vilnius.lt Telecentras "duomenu centras"
```

Grade: **A** for Telecentras-owned pages and Vilnius municipal source; do not infer undisclosed addresses.

### 3.3 Delska / DEAC / DLC / Data Inn

Primary sources:

- Delska data centers: https://delska.com/data-centers/
- DLC legally becomes Delska Lithuania: https://delska.com/about/news-resources/delska-newsroom/dlc-legally-becomes-delska-lithuania/
- Data Inn history from Ignitis Group: https://ignitisgrupe.lt/naujienos/itin-efektyvus-data-inn-duomenu-centras-lietuvai-pades-konkuruoti-tarptautineje-rinkoje
- DLC expansion press: https://www.vz.lt/paslaugos/2021/08/16/duomenu-logistikos-centras-plecia-duomenu-centra-data-inn--investicija-sieks-3-mln-euru

Current Delska-listed Vilnius sites:

- EU North Vilnius LT DC1: J. Tiskeviciaus street 72, Vilnius; 2 MW; 220 racks; Tier III certification.
- EU North Vilnius LT DC2: T. Sevcenkos street 16J, Vilnius; 2 MW; 140 racks; Tier III certification.
- EU North Vilnius LT DC3: A. Juozapaviciaus street 13, Vilnius; 2 MW; 180 racks; designed to EN 50600-2.

Queries:

```text
Delska Vilnius "LT DC1"
"J. Tiskeviciaus" "duomenu centras"
"T. Sevcenkos g. 16J" Delska OR RackRay
"A. Juozapaviciaus g. 13" "duomenu centras"
"Duomenu logistikos centras" Delska
"Data Inn" "duomenu centras" "Vilnius"
site:delska.com Lithuania Vilnius
site:infostatyba.planuojustatau.lt "Duomenu logistikos centras"
```

Grade: **A** for Delska-owned current facility page and legal rename; **B** for Ignitis/VZ historical expansion context.

### 3.4 Bite Lietuva

Primary sources:

- Operator release: https://www.bite.lt/naujienos/BITE-atidaro-isskirtinio-saugumo-duomenu-centra
- LRT/BNS: https://www.lrt.lt/naujienos/verslas/4/1781109/bite-lietuva-prie-vilniaus-atidare-duomenu-centra
- DCD: https://www.datacenterdynamics.com/en/news/bite-lithuania-opens-data-center-outside-vilnius/

Current signal:

- In September 2022 Bite opened a Tier III datacenter service footprint near Vilnius in Data Inn, operated by DLC.
- The release says it complements existing Bite datacenters in Kaunas, Riga, and Vilnius, but separate physical facilities need independent verification before counting.

Queries:

```text
Bite "Data Inn" "duomenu centras"
"Bite Lietuva" "Tier III" "duomenu centras"
"Bite" "duomenu centrai" Kaunas Vilnius Ryga
site:bite.lt "duomenu centras"
site:lrt.lt "Bite" "Data Inn"
```

Grade: **A** for operator release; **B** for LRT/DCD. Treat as tenant/service footprint unless schema counts operator footprints separately from buildings.

### 3.5 Baltneta

Primary sources:

- Colocation page: https://www.balt.net/colocation
- News page: https://www.balt.net/naujienos
- Construction press: https://www.statybunaujienos.lt/naujiena/Vilniuje-statomas-didziausias-Lietuvoje-duomenu-centras/11545

Current signal:

- Baltneta advertises a dedicated Tier 3 datacenter in Vilnius with 96 switchboard cabinets.
- Historical/construction sources point to Liepkalnis and directory sources point to Paneriu g. 26; these addresses require official/operator confirmation before final counting.

Queries:

```text
Baltneta "duomenu centras" Vilnius
Baltneta "Liepkalnio" "duomenu centras"
Baltneta "Paneriu g. 26"
site:balt.net "duomenu centras"
site:vilnius.lt Baltneta "duomenu centras"
site:infostatyba.planuojustatau.lt Baltneta
```

Grade: **A** for operator colocation claims; **B** for construction press; **C** for directory-only extra locations.

### 3.6 Bacloud

Primary sources:

- Lithuania datacenter page: https://www.bacloud.com/en/our-datacenter/lithuania
- Lithuanian site: https://www.bacloud.com/lt

Current signal:

- Bacloud states its main Lithuania datacenter is in Siauliai and has run since 2006.

Queries:

```text
Bacloud Siauliai "duomenu centras"
"Siauliai" "Bacloud" "data center"
site:bacloud.com Siauliai
site:siauliai.lt Bacloud OR "duomenu centras"
site:infostatyba.planuojustatau.lt Bacloud
```

Grade: **A** for operator page; municipal/building evidence still useful for precise address/status.

### 3.7 Kaunas-Area Hosting / Colocation Leads

Primary/lead sources:

- LETAS: https://letas.lt/
- Serveroffer colocation: https://serveroffer.lt/lt/serveriu-kolokacija-duomenu-centre
- Host Baltic business-register lead: https://rekvizitai.vz.lt/imone/host_baltic/

Current signal:

- Serveroffer states it offers colocation in its own datacenter in Kaunas.
- LETAS/Host Baltic are Kaunas-area hosting/colocation leads, but public physical-facility detail is limited.

Queries:

```text
"duomenu centras" Kaune kolokacija
"serveriu kolokacija" Kaunas
Serveroffer Kaunas "nuosavame duomenu centre"
LETAS Kaunas "duomenu centras"
"Host Baltic" "Kauno rajone" "duomenu centras"
site:kaunas.lt "duomenu centras" "kolokacija"
site:krs.lt "duomenu centras"
```

Grade: **A** if operator page clearly states own DC; **C** for registry snippets until address/building evidence is found.

### 3.8 Vilnius Small / Medium Operators

Sources:

- Hostline: https://hostline.lt/duomenu-centrai/ and https://hostline.lt/kolokacija/
- RackRay: https://www.rackray.com/
- VPSnet colocation: https://www.vpsnet.com/lt/paslaugos/kolokacija
- Cherry Servers: https://www.cherryservers.com/
- CSC Telecom DC service: https://csc.lt/verslui/it-centras/duomenu-centras/

Use:

- Hostline says it operates a private Vilnius DC and works with another large Lithuanian DC.
- RackRay should be checked against Delska LT DC2 to avoid double-counting.
- VPSnet, Cherry Servers, and CSC Telecom are service/operator leads until a public physical facility or host datacenter is identified.

Queries:

```text
Hostline "du duomenu centrai Vilniuje"
RackRay "T. Sevcenkos" OR Delska
VPSnet "kolokacija" "Tier III"
Cherry Servers Vilnius "data center"
CSC Telecom "duomenu centras"
site:vilnius.lt Hostline OR RackRay OR VPSnet OR Cherry
```

## 4. National Query Sweeps

English sweep:

```text
"Lithuania" "data center" Telia Telecentras Delska Bite Baltneta Bacloud
"Lithuania" "data centre" "MW" Vilnius
"Vilnius" "data center" "Tier III"
"Siauliai" "data center" Bacloud
"Lithuania" "AI data center" OR "hyperscale"
"Kruonis" "data center" "200 MW"
"Delska" "Vilnius" "LT DC1"
"Telecentras" "state data centers" Lithuania
site:datacenterdynamics.com Lithuania "data center"
```

Lithuanian sweep:

```text
"duomenu centras" Lietuva "MW"
"duomenu centras" Vilnius Telia Telecentras Delska Bite Baltneta
"duomenu centras" Kaunas kolokacija
"duomenu centras" Siauliai Bacloud
"duomenu centras" "statybos leidimas"
"duomenu centras" "statinio uzbaigimas" OR "atidarytas"
"duomenu centrui" "110 kV" OR "330 kV"
"duomenu centro" "poveikio aplinkai"
"Tier III" "duomenu centras" Vilnius
```

Official verification sweep:

```text
site:infostatyba.lt "duomenu centras"
site:infostatyba.planuojustatau.lt "duomenu"
site:litgrid.eu "data centre" OR "duomenu centras"
site:eso.lt "duomenu centras"
site:vert.lt "duomenu centras"
site:rrt.lt "duomenu centras"
site:aaa.lrv.lt "atranka" "duomenu"
filetype:pdf "duomenu centras" "statybos leidimas"
filetype:pdf "duomenu centro" "elektros tinklai"
```

## 5. Complete County Query Strategy

### Tier 1 Counties

**Vilnius County**: Vilnius city, Vilnius district, Elektrenai, Salcininkai district, Sirvintos district, Svencionys district, Trakai district, Ukmerge district.

```text
"Vilnius" "duomenu centras" Telia Telecentras Delska Bite Baltneta Hostline RackRay
"J. Tiskeviciaus g. 72" OR "Sausio 13-osios g. 10" "duomenu centras"
"T. Sevcenkos g. 16J" OR "A. Juozapaviciaus g. 13" "duomenu centras"
"Raisteniskes" OR "Ukmerges g. 449" "duomenu centras"
"Liepkalnis" OR "Paneriu g. 26" Baltneta "duomenu centras"
site:vilnius.lt "duomenu centras"
site:vrsa.lt "duomenu centras"
site:infostatyba.planuojustatau.lt Vilnius "duomenu"
```

**Kaunas County**: Kaunas city, Kaunas district, Birstonas, Jonava district, Kaisiadorys district, Kedainiai district, Prienai district, Raseiniai district.

```text
"Kaunas" OR "Kaune" "duomenu centras"
"Kauno rajone" "duomenu centras"
Serveroffer OR LETAS OR "Host Baltic" Kaunas
"Kruonis" OR "Kruonio technologiju parkas" "duomenu centras" OR "data center"
site:kaunas.lt "duomenu centras"
site:krs.lt "duomenu centras"
site:kaisiadorys.lt "duomenu centras"
```

**Siauliai County**: Siauliai city, Siauliai district, Akmene district, Joniskis district, Kelme district, Pakruojis district, Radviliskis district.

```text
"Siauliai" "duomenu centras" Bacloud
"Bacloud" "Lithuania" "data center"
site:bacloud.com Siauliai
site:siauliai.lt "duomenu centras"
site:siauliuraj.lt "duomenu centras"
```

### Tier 2 Counties

**Klaipeda County**: Klaipeda city, Klaipeda district, Kretinga district, Neringa, Palanga city, Skuodas district, Silute district.

```text
"Klaipeda" "duomenu centras"
"Klaipedos LEZ" OR "Klaipeda FEZ" "data center" OR "duomenu centras"
"Klaipedos uostas" "duomenu centras"
"Palanga" "serverine" OR "duomenu centras"
site:klaipeda.lt "duomenu centras"
site:palanga.lt "duomenu centras"
site:silute.lt "duomenu centras"
```

**Panevezys County**: Panevezys city, Panevezys district, Birzai district, Kupiskis district, Pasvalys district, Rokiskis district.

```text
"Panevezys" "duomenu centras"
"Panevezio rajonas" "duomenu centras"
"Panevezys" Telia OR Tele2 OR Bite "duomenu centras"
site:panevezys.lt "duomenu centras"
site:panrs.lt "duomenu centras"
site:birzai.lt "duomenu centras"
site:rokiskis.lt "duomenu centras"
```

Watch false positives from ZUDC/agricultural data offices.

### Tier 3 Counties

Run this compact pass for every municipality in Alytus, Marijampole, Taurage, Telsiai, and Utena counties:

```text
"{municipality}" "duomenu centras"
"{municipality}" "serverine"
"{municipality}" "kolokacija"
"{municipality}" "duomenu centras" "statybos leidimas"
"{municipality}" "atranka" "duomenu"
site:{municipality-domain} "duomenu centras"
site:{municipality-domain} "atranka" OR "PAV"
site:infostatyba.planuojustatau.lt "{municipality}" "duomenu"
```

Municipality lists:

- Alytus County: Alytus city, Alytus district, Druskininkai, Lazdijai district, Varena district.
- Marijampole County: Marijampole, Kalvarija, Kazlu Ruda, Sakiai district, Vilkaviskis district.
- Taurage County: Taurage district, Jurbarkas district, Pagegiai, Silale district.
- Telsiai County: Telsiai district, Mazeikiai district, Plunge district, Rietavas.
- Utena County: Utena district, Anyksciai district, Ignalina district, Moletai district, Visaginas, Zarasai district.

Watch items:

- Utena County / Visaginas and Ignalina: grid/land narratives only; require permits before counting.
- Telsiai County / Mazeikiai: industrial-power context only; require datacenter-specific evidence.
- Marijampole, Taurage, Alytus: municipal PAV pages are the main discovery surface; expect `no_projects` unless a local operator lead appears.

## 6. Aliases

Operator/legal aliases:

```text
Telia / Telia Lietuva / TeliaSonera
Telecentras / LRTC / Lietuvos radijo ir televizijos centras / AB Lietuvos radijo ir televizijos centras
Delska / Delska.DEAC / DEAC / DLC / Duomenu logistikos centras / Data Logistics Center / UAB DELSKA Lithuania
Data Inn
Bite / Bite Lietuva
Baltneta / Baltnetos komunikacijos
Bacloud
Hostline / RackRay / VPSnet / Cherry Servers / CSC Telecom
Host Baltic / LETAS / Serveroffer
Saugusis duomenu perdavimo tinklas
Kruonis Technology Park / Kruonio technologiju parkas
```

Address aliases:

```text
J. Tiskeviciaus g. 72, Vilnius - Delska LT DC1 / Data Inn area
T. Sevcenkos g. 16J, Vilnius - Delska LT DC2 / RackRay legacy
A. Juozapaviciaus g. 13, Vilnius - Delska LT DC3
Sausio 13-osios g. 10, Vilnius - Telecentras TV-tower area
Ukmerges g. 449 / Raisteniskes / Avizieniai area, Vilnius District - Telia new DC
Paneriu g. 26 and Liepkalnio g. 160C, Vilnius - Baltneta directory/construction pivots; verify before final counting
```

## 7. Evidence Handling

Use these status labels consistently:

- `operational`: current operator page/release or official opened/commissioned evidence.
- `tenant/service footprint`: branded operator deployment inside another operator's facility, e.g. Bite inside Data Inn.
- `construction`: construction start, permit, contractor, or municipal evidence, e.g. Telia Raisteniskes.
- `planned`: named project/site without construction proof.
- `siting lead`: Invest Lithuania/Kruonis, FEZ, grid, or land offer.
- `unknown/historical`: only old press or directory evidence.

Common false positives:

- ZUDC / `Zemes ukio duomenu centras`.
- `Valstybes duomenu agentura`.
- ID Vilnius or municipal data/GIS units.
- `duomenu centras` used for a data-processing office.
- Office/server rooms with no hosting/colo/customer infrastructure.
- Telecom POPs without colocation/rack/hosting claims.
- Cloud MSP/reseller pages without physical facility claims.
- Directory entries for Telia/Tele2/Bite regional nodes without operator confirmation.
- Secure/state sites where exact locations are intentionally not public.

Recommended capture:

```text
name
division_county
municipality
city_or_settlement
address_or_public_location
operator
developer
legal_entity_aliases
status
capacity_mw
racks_or_white_space
power_connection_kv
tier_or_certification
source_urls
evidence_date
evidence_grade
official_verification_needed
notes
```

Final Lithuania-specific rule: separate physical buildings from operator/tenant service footprints. Delska/Data Inn and Bite are the key example: Bite's 2022 facility signal is a Bite service deployment inside Data Inn/DLC, so do not double-count it as an additional building unless the target database explicitly tracks tenant deployments.
