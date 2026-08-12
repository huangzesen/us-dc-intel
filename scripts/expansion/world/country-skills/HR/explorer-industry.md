# HR Explorer Industry - Croatia Colo Providers, Cloud Signals, Trade Press, Associations, and County Query Patterns

Date: 2026-08-12. Scope: Croatia (HR), 20 counties plus Zagreb City. Angle: **industry/vendor-led datacenter enumeration**. Reliability grades: **A** = official operator, regulator, permit, government, certification, or procurement source; **B** = established trade press, industry association, contractor case study, stock-exchange/company disclosure, or reputable local business press; **C** = directories, market snippets, SEO hosting pages, social posts, or unverified aggregate data.

---

## 0. Croatia-specific market frame

- Croatia has no single public national registry of commercial datacenters. The practical enumeration path is: **operator/directories/trade lead -> operator page or certification -> eDozvola/ISPU/local permitting -> environmental and grid/energy checks -> HAKOM/e-procurement/press cross-check**.
- Expect a **Zagreb-led market** with smaller disaster-recovery, telecom, hosting, government, enterprise, and tourism/port/edge facilities elsewhere. Current public directories show most named commercial colo in Zagreb or the Zagreb belt, with higher-confidence non-Zagreb leads around Jastrebarsko, Kriz, Varazdin, Rijeka, Split, Osijek, and Pula only after verification.
- The newest large-project signal is **Pantheon AI / Pantheon Atlas near Topusko in Sisak-Moslavina County**. Treat it as a planned/prospective hyperscale AI campus until confirmed in county, eDozvola, environmental, grid, land, and construction records.
- Croatian sources use both English and local terms. Search first for `podatkovni centar`, `data centar`, `data center`, `kolokacija`, `smjestaj opreme`, `serverska soba`, `racunalni centar`, `oblak`, `virtualni podatkovni centar`, `agregat`, `UPS`, `trafostanica`, `prikljucak`, `gradevinska dozvola`, `uporabna dozvola`, `lokacijska dozvola`, `procjena utjecaja na okolis`, `studija utjecaja`, `sunčana elektrana`, `baterijski sustav`, and `dalekovod`.
- Watch false positives: `virtualni podatkovni centar` and cloud-service pages often do not name a physical facility; `centar podataka`, `podatkovni portal`, `data centar` in analytics/statistics contexts, call centers, and office/headquarters pages should not be counted without physical infrastructure evidence.

---

## 1. Priority industry, association, and trade-press sources

### 1.1 Associations, events, and market ecosystem

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| Croatian Data Centre Association / HRDCA | https://hrdca.hr/ and https://www.linkedin.com/company/hrdca | First domestic industry association; useful for member/operator ecosystem and official event claims. LinkedIn posts state HRDCA was founded in 2024 and cite government remarks about 22 active private data centers in Croatia, but verify facility-level claims elsewhere. | B/C |
| Croatia Data Center Summit | https://datacenterevent.eu/ and https://www.amcham.hr/en/news/croatian-data-center-summit-2026 | Event speakers/sponsors reveal active operators, engineers, grid/cooling vendors, investors, and policymakers. Not a facility register. | B/C |
| European Data Centre Association | https://www.eudca.org/ | Regional association context; use for Croatia market framing only unless Croatia-specific member/project evidence appears. | B/C |
| HAKOM operator search | https://www.hakom.hr/hr/operatori-i-usluge/162 and https://eoperator.hakom.hr/ | Confirms telecom/network operators that may own colo, fiber, or edge sites. HAKOM is not a datacenter registry. | A for telecom operator status; C for facility inference |
| Croatian Chamber / AmCham / ICT association surfaces | Queries: `site:amcham.hr "data center" Croatia`, `site:hup.hr "podatkovni centar"`, `site:hgk.hr "podatkovni centar"` | Useful for policy, investment and member leads. Verify facility data via operator/permit pages. | B/C |

### 1.2 Trade press, business press, and project-news sources

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com/ ; query `site:datacenterdynamics.com Croatia "data center"` | Best international DC trade source. Confirmed A1 Zagreb opening and DataBox/Digital Realty cloud-service transaction; also tracks Pantheon/Topusko. Verify with operator and public records. | B |
| Bug / Mreza | https://www.bug.hr/ and https://mreza.bug.hr/ ; query `site:bug.hr "podatkovni centar" Hrvatska`, `site:mreza.bug.hr "data centar"` | Croatian IT press; strong for Pantheon, HRDCA, local operator announcements, and terminology. | B |
| Poslovni dnevnik | https://www.poslovni.hr/ ; query `site:poslovni.hr "podatkovni centar"` | Business/investment press; useful for HRDCA summit, Pantheon, and local investment claims. | B |
| Forbes Hrvatska / Dnevnik | https://forbes.dnevnik.hr/ ; query `site:forbes.dnevnik.hr "data centar" OR "podatkovni centar"` | Current business reporting; useful for HRDCA summit and the "22 private data centers" claim, but not facility-level proof. | B |
| Hina | https://www.hina.hr/ ; query `site:hina.hr "podatkovni centar" "Hrvatska udruga"` | National wire. Often paywalled but strong for association/government statements. | B |
| Index / Vecernji / Jutarnji / Lider / Telegram | Queries: `site:index.hr Pantheon "podatkovni centar"`, `site:vecernji.hr "podatkovni centar"`, `site:jutarnji.hr "podatkovni centar" Topusko`, `site:lider.media "data centar"` | Good for local project visibility and political/land/energy details. Cross-check carefully; many Pantheon stories are announcement-led. | B/C |
| Balkan Insight / BusinessWire / WSJ / Enlit / OIE Hrvatska | Queries around `Pantheon AI Topusko Croatia data centre` | Useful for the Topusko hyperscale/energy project. BusinessWire is issuer-controlled; OIE is useful for energy-industry remarks; WSJ is opinion/announcement context. | B/C |
| Contractor/vendor references | Vertiv, Schneider Electric, ABB, Siemens, Koncar, HEP/HOPS contractors, HVAC/fire/security firms; query `"podatkovni centar" "referenca" "{vendor}"` | Can reveal build partners, generator permits, grid connections, cooling upgrades, or facility retrofits. Verify facility/operator before counting. | B |

### 1.3 Directories and market aggregators

| Source | URL | Use | Grade |
|---|---|---|---|
| Baxtel Croatia | https://baxtel.com/data-center/croatia | Strong lead list; currently indicates 19 Croatian facilities and highlights PCK-DataCross, DC North Varazdin, Croatian Web Hosting, and A1. Use as a seed, not source-of-record. | C+ |
| DataCenterMap Croatia/Zagreb | https://www.datacentermap.com/croatia/ and https://www.datacentermap.com/croatia/zagreb/ | Useful for older colo names, addresses, and provider aliases. Free view limits and stale data require primary checks. | C+ |
| Datacenters.com Croatia | https://www.datacenters.com/locations/croatia | Provider/facility marketplace; useful for A1, Digital Realty, PCK and smaller hosts. | C |
| Cloudscene Zagreb/Croatia | https://cloudscene.com/market/data-centers-in-croatia/zagreb | Market ecosystem, network fabrics, and cloud-service-provider counts. Facility addresses need confirmation. | C |
| Data Center Catalog | https://datacentercatalog.com/croatia-hrvatska | Certification/capacity snippets and directory aliases. Verify with operator/certifier. | C |
| PeeringDB | https://www.peeringdb.com/ | Interconnection evidence for CIX/facilities and network presence. Grade B for active peering/facility signal, C for completeness. | B/C |

---

## 2. Official and semi-official verification surfaces

| Channel | URL / pattern | What it confirms | Grade |
|---|---|---|---|
| eDozvola / eGrađevinska dozvola | https://mpgi.gov.hr/edozvola-8144/8144 | Construction, use, location, and other building-permit proceedings. The ministry page says applications and status for construction/use permits can be handled electronically. | A |
| eDozvola notice board / Oglasna ploca | https://mpgi.gov.hr/oglasna-ploca-13818/13818 | Publicly posted permits/notices from the eDozvola system; search by investor, county, municipality, parcel, and keywords. | A |
| ISPU portal / Geoportal | https://mpgi.gov.hr/ispu-portal/8994 and https://mpgi.gov.hr/eu-sufinanciranja/ispu-i-razvoj-e-usluga/e-usluge/geoportal-ispu-i-interoperabilnost/8417 | Spatial plans, zoning layers, cadastral context, and planning constraints after a lead is known. | A |
| Ministry of Environmental Protection and Green Transition | https://mzozt.gov.hr/ | Environmental assessment, screening, nature-protection and SEA/EIA documents. Search for `procjena utjecaja na okolis`, `ocjena o potrebi procjene`, `studija utjecaja`, project name, and county. | A |
| HOPS / HEP ODS / energy ministry | https://www.hops.hr/ , https://www.hep.hr/ods/ , https://mingo.gov.hr/ | Grid-connection, transmission, substation, renewable/BESS and high-load project context. Most individual connection details may not be public; use press and procurement as secondary evidence. | A/B |
| EOJN public procurement | https://eojn.hr/ and https://ted.europa.eu/ | Government, municipal, hospital, university, and telecom/utility procurements for data center buildouts, server rooms, UPS, generators, cooling, and design/build works. | A/B |
| County/city official sites and BIP-style notices | `site:{county/city-domain} "podatkovni centar"` | Local plans, development-agency investment pages, council decisions, environmental notices, and building acts. | A/B |
| Uptime Institute and EN 50600/Tier certifiers | https://uptimeinstitute.com/uptime-institute-awards/ | Facility certification evidence; A1 Zagreb appears in Uptime Institute awards. Certification confirms the named facility, not current operator status or exact capacity. | A/B |

Core official-query templates:

```text
site:mpgi.gov.hr "podatkovni centar" "eDozvola"
site:mpgi.gov.hr "data centar" "oglasna ploča"
site:mpgi.gov.hr "podatkovni centar" "građevinska dozvola"
site:mzozt.gov.hr "podatkovni centar" "procjena utjecaja na okoliš"
site:mzozt.gov.hr "data centar" "ocjena o potrebi procjene"
site:eojn.hr "podatkovni centar" OR "serverska soba" OR "kolokacija"
site:ted.europa.eu Croatia "data centre" OR "data center" OR "server room"
site:hakom.hr "{operator}" "operatori i usluge"
site:hops.hr "podatkovni centar" OR "Topusko" OR "trafostanica"
site:hep.hr "podatkovni centar" OR "priključenje" OR "trafostanica"
```

---

## 3. Operator, cloud, and vendor seed list

Operator pages are **A for self-reported facility/service existence**, but not by themselves proof of construction status, full capacity, or exact permit boundary. Pair each with eDozvola/ISPU/certification/local records where possible.

### 3.1 High-priority commercial and telecom operators

| Operator / project | Official / useful URL | Geography | Evidence use |
|---|---|---|---|
| Digital Realty / former Altus IT / ZAG1 | https://www.digitalrealty.com/data-centers/emea/zagreb | Zagreb City, Selska cesta 93 | Official page lists Zagreb ZAG1, 1,330 sqm colocation, 50+ cloud/network service providers, ISO/PCI certifications. Grade A for current Digital Realty facility. PRNewswire acquisition: https://www.prnewswire.com/news-releases/interxion-a-digital-realty-company-establishes-presence-in-croatia-with-acquisition-of-altus-it-301126856.html . |
| A1 Hrvatska data center | https://www.a1.hr/poslovni/ict-rjesenja/datacentar-usluge and A1 opening release https://www.a1.hr/tko-smo-mi/objave-za-medije/-/objave/clanak/otvoren-najmoderniji-podatkovni-centar-u-regiji-vrijedan-11-milijuna-eura/1961821 | Zagreb City; intersection of Avenija Većeslava Holjevca and Nežićeva ulica; older Vrtni put facility lead | A1 official page confirms datacenter services. A1/DCD opening reports give EUR 11m, 2,000 sqm, Tier III, Vertiv build, two 2 MW power branches, 300 IT cabinets. Uptime Institute listing: https://uptimeinstitute.com/uptime-institute-awards/datacenter/a1-hrvatska-podatkovni-centar-zagreb-level-2-zone-1-and-zone-2/1510 . Grade A/B. |
| Podatkovni centar Križ / PCK-DataCross | https://pck.hr/en/ , https://pck.hr/en/pocetna/data-centar-jastrebarsko/ , https://pck.hr/en/pocetna/svecano-otvorenje-datacross-jastrebarsko/ | Zagreb County: Jastrebarsko/Jalševac; Križ | Official pages identify Jastrebarsko in industrial zone Jalsevac near Zagreb-Karlovac highway and a Križ disaster-recovery/business-continuity platform. Directory pages list separate Križ and Jastrebarsko sites; verify current footprint and capacity with operator and county/city records. Grade A/C. |
| DataBox | https://databox.hr/data-centar/ | Zagreb lead | Official page offers colocated IT equipment in its data center. DCD reported DataBox took over Digital Realty's cloud-service business in Croatia while DataBox offers colocation/cloud and has a Zagreb DC: https://www.datacenterdynamics.com/en/news/databox-takes-over-digital-realtys-cloud-service-in-croatia/ . Verify physical address before counting as distinct from Digital Realty ecosystem. Grade A/B. |
| Croatian Web Hosting / CROWEB.HOST | https://www.croweb.host/datacenter | Zagreb City / Zagreb Airport-side lead | Official page says strategically located in Zagreb, 15 km from Zagreb Airport, Tier 3-designed and N+1. DCD says it was the other Tier III Croatian facility when A1 opened. Verify address and certification. Grade A/B. |
| Hrvatski Telekom / T-HT | https://www.hrvatskitelekom.hr/poslovni/ict/cloud and related official domain searches | Zagreb and possible regional telecom facilities | Strong telecom/cloud pivot. Do not count generic cloud/virtual datacenter services without a named physical datacenter, address, certification, procurement, or PeeringDB/facility record. Grade B/C until facility evidence. |
| Telemach Hrvatska / United Group | https://telemach.hr/ and official domain searches | Zagreb and regional telecom nodes | Telecom operator lead; search for colocation, cloud, server rooms, and network facilities. Count only when a named facility/address appears. Grade B/C. |
| Iskon / Terrakom / Optima / regional ISPs | Official domains plus HAKOM operator search | Zagreb, Split, Rijeka, Osijek, Pula and county seats | Use as lead pivots for small colo, hosting, CIX presence, and edge sites. Most service pages are not facility proof. Grade C until primary confirmation. |
| Plus Hosting Grupa / DHH | Digital Realty partner page https://www.digitalrealty.com/partners/partner-directory/plus-hosting-grupa | Zagreb/service-provider ecosystem | Digital Realty calls Plus Hosting Croatia's largest hosting provider and a partner. Use for customer/provider ecosystem and possible historic hosting-facility leads; verify physical sites. Grade B/C. |
| DC North / Varazdin lead | Directory and local searches: `DC North Varazdin data center`, `"DC North" "Varaždin"` | Varazdin County | Baxtel lists a DC North Varazdin lead. Treat as C until operator, address, permit, or local press confirms. |

### 3.2 Planned/prospective hyperscale and energy-linked project

- **Pantheon AI / Pantheon Atlas / Project Pantheon - Topusko** - issuer-controlled page https://pantheonai.com/ and BusinessWire release https://www.businesswire.com/news/home/20260427904479/en/Transatlantic-Investment-Group-Announces-%E2%82%AC50-Billion-AI-Data-Center-and-Innovation-Campus-in-Croatia-the-Largest-Investment-in-Croatian-History-and-Among-the-Largest-Private-U.S.-Investments-in-Europe . DCD writeup: https://www.datacenterdynamics.com/en/news/pantheon-eyes-large-scale-behind-the-meter-data-center-campus-in-croatia/ . Local searches point to Topusko / Banovina / Pecka-Katinovac-Crni Potok area in Sisak-Moslavina County, with claimed 1 GW total capacity, 800 MW usable IT load, 500 MW solar, 2 GW/8 GWh BESS, and 2027-2029 timeline. Grade B/C until government permitting, environmental, grid, and land records confirm.

Pantheon verification queries:

```text
"Pantheon" "Topusko" "podatkovni centar"
"Pantheon AI" "Sisačko-moslavačka županija"
"AI razvojni i podatkovni centar Topusko"
"Topusko" "građevinska dozvola" "Pantheon"
"Topusko" "procjena utjecaja na okoliš" "Pantheon"
"Topusko" "studija utjecaja" "podatkovni centar"
"Pecka" "Katinovac" "Crni Potok" "Pantheon"
"Pantheon" "trafostanica" OR "dalekovod" OR "HOPS"
"Pantheon" "sunčana elektrana" OR "baterijski sustav"
site:smz.hr Pantheon Topusko
site:topusko.hr Pantheon "podatkovni centar"
site:mzozt.gov.hr Pantheon Topusko
site:mpgi.gov.hr Pantheon Topusko
```

### 3.3 Hyperscale cloud region handling

- **AWS** - official global infrastructure page (https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) lists current regions and explains regions/AZs; no Croatia region was found on the official page during this pass. Use only as negative cloud-region evidence unless AWS later announces a Croatia region/local zone.
- **Microsoft Azure** - official geographies page (https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/) lists Azure geographies/regions and, as of review, names nearby European regions such as Austria East, Italy North, Poland Central, Greece, North/West Europe etc.; Croatia is not listed. Use as negative public-region evidence.
- **Google Cloud** - official locations page (https://cloud.google.com/about/locations) says Google Cloud has 43 regions and 130 zones as of July 23, 2026; no Croatia region was found by page search. Use only for latency/data-residency context.
- **Oracle Cloud Infrastructure** - official public cloud regions page (https://www.oracle.com/cloud/public-cloud-regions/) lists European commercial regions including Germany, Italy, Netherlands, Serbia, Spain, Sweden, Switzerland, UK, etc.; Croatia is not listed. The Serbia Central region may influence Croatian latency/residency discussions but is not a Croatian facility.
- Cloud marketplace/product pages, `virtualni podatkovni centar`, sovereign cloud and partner-hosted offers should be treated as **service leads**, not datacenter sites, unless a physical Croatian facility is identified.

Cloud-region query templates:

```text
"Croatia" "AWS Local Zone" OR "AWS Region"
"Croatia" "Azure region" OR "Microsoft datacenter region"
"Croatia" "Google Cloud region" OR "Cloud Interconnect" Zagreb
"Croatia" "Oracle Cloud region" OR OCI
"Hrvatska" "cloud regija" Microsoft OR Google OR AWS OR Oracle
"Zagreb" "direct connect" OR "cloud on-ramp" OR "Cloud Interconnect"
site:digitalrealty.com Zagreb AWS Google Microsoft Oracle
site:peeringdb.com Zagreb "Digital Realty" OR "CIX"
```

---

## 4. National query playbook

### 4.1 Croatian and English national sweep

```text
"podatkovni centar" Hrvatska kolokacija
"data centar" Hrvatska "kolokacija"
"data center" Croatia colocation Zagreb
"data centre" Croatia "Zagreb" "Tier III"
"podatkovni centar" Hrvatska "MW" OR "MVA" OR "kVA"
"podatkovni centar" Hrvatska "agregat" OR "UPS" OR "hlađenje"
"podatkovni centar" Hrvatska "trafostanica" OR "priključenje"
"podatkovni centar" Hrvatska "građevinska dozvola" OR "uporabna dozvola"
"podatkovni centar" Hrvatska "procjena utjecaja na okoliš"
"serverska soba" Hrvatska "agregat" "UPS"
"računalni centar" Hrvatska "kolokacija" OR "smještaj opreme"
"smještaj opreme" "podatkovni centar" Hrvatska
"virtualni podatkovni centar" Hrvatska "fizička lokacija"
```

### 4.2 Trade and local-press sweep

```text
site:datacenterdynamics.com Croatia "data center"
site:bug.hr "podatkovni centar" OR "data centar"
site:mreza.bug.hr "podatkovni centar" OR "data centar"
site:poslovni.hr "podatkovni centar" OR "data centar"
site:forbes.dnevnik.hr "data centar" OR "podatkovni centar"
site:hina.hr "podatkovni centar" Hrvatska
site:index.hr "podatkovni centar" Topusko OR Zagreb
site:vecernji.hr "podatkovni centar" "Hrvatska"
site:jutarnji.hr "podatkovni centar" Topusko OR Zagreb
site:lider.media "podatkovni centar" OR "data centar"
site:balkaninsight.com Croatia "data centre" Pantheon
```

### 4.3 Operator and contractor sweep

```text
"{operator}" "podatkovni centar" Hrvatska
"{operator}" "data centar" Zagreb
"{operator}" "kolokacija" "smještaj opreme"
"{operator}" "Tier III" "Hrvatska"
"{operator}" "ISO 27001" "podatkovni centar"
"{operator}" "referenca" "podatkovni centar"
"{operator}" "agregat" "podatkovni centar"
"{operator}" "hlađenje" "data centar"
site:{operator-domain} "podatkovni centar"
site:{operator-domain} "kolokacija"
site:{operator-domain} "data center"
```

High-yield operator strings:

```text
"Digital Realty" Zagreb "Selska cesta 93"
"Altus IT" Zagreb "data center"
"A1 Hrvatska" "podatkovni centar Zagreb"
"Avenija Većeslava Holjevca" "Nežićeva" "podatkovni centar"
"Vrtni put" "A1" "podatkovni centar"
"Podatkovni centar Križ" OR "PCK-DataCross"
"DataCross" Jastrebarsko Jalševac
"DataBox" Zagreb "data centar"
"Croatian Web Hosting" Zagreb "Tier 3"
"CROWEB.HOST" "data center"
"DC North" Varaždin "data center"
"Hrvatski Telekom" "podatkovni centar"
"Telemach" Hrvatska "podatkovni centar"
"Plus Hosting" Hrvatska "data center"
```

### 4.4 Negative filters and downgrade triggers

Downgrade or exclude:

```text
"podatkovni portal"
"baza podataka" without physical facility
"virtualni podatkovni centar" without address/facility
"cloud usluge" only
"hosting" only with no facility/location
"call centar" OR "kontakt centar"
"data center" as product category only
"ured" OR "poslovnica" only
"edge" marketing without equipment-room evidence
```

---

## 5. County-by-county industry query patterns

Use the English manifest name, the Croatian county name, county seat, and largest cities. When a source uses diacritics, also search ASCII fallback forms (`Varaždin/Varazdin`, `Križevci/Krizevci`, `Međimurje/Medimurje`, `Šibenik/Sibenik`, `Požega/Pozega`, `Čakovec/Cakovec`).

Universal county template:

```text
"{county Croatian name}" "podatkovni centar"
"{county English name}" Croatia "data center"
"{county seat}" "podatkovni centar" OR "data centar"
"{county seat}" "kolokacija" OR "smještaj opreme"
"{county seat}" "serverska soba" "agregat" OR "UPS"
"{county seat}" "trafostanica" "podatkovni centar"
"{county seat}" "građevinska dozvola" "podatkovni centar"
site:{county-domain} "podatkovni centar" OR "data centar"
site:{city-domain} "podatkovni centar" OR "serverska soba"
site:mzozt.gov.hr "{county seat}" "podatkovni centar"
site:mpgi.gov.hr "{county seat}" "podatkovni centar"
```

### 5.1 Zagreb City / Grad Zagreb

Highest-yield market. Seed operators: Digital Realty/Altus, A1, DataBox, Croatian Web Hosting, Hrvatski Telekom, Telemach, Plus Hosting, CIX/IXP ecosystem, public-sector IT, banks and insurers.

```text
"Grad Zagreb" "podatkovni centar"
"Zagreb" "data center" colocation Croatia
"Zagreb" "kolokacija" "podatkovni centar"
"Selska cesta 93" "Digital Realty" OR "Altus IT"
"Avenija Većeslava Holjevca" "Nežićeva" A1
"Vrtni put" A1 "podatkovni centar"
"DataBox" Zagreb "podatkovni centar"
"Croatian Web Hosting" Zagreb "data center"
"Zagreb" CIX "data center" OR "podatkovni centar"
site:zagreb.hr "podatkovni centar" OR "data centar"
site:zagreb.hr "serverska soba" "agregat"
site:mpgi.gov.hr Zagreb "podatkovni centar" "eDozvola"
```

### 5.2 Zagreb County / Zagrebačka županija

High-yield belt for disaster recovery and industrial-zone sites. Seed operators: PCK-DataCross Jastrebarsko/Jalševac and Križ; look also at Velika Gorica, Samobor, Sveta Nedelja, Zaprešić, Dugo Selo, and airport/logistics corridors.

```text
"Zagrebačka županija" "podatkovni centar"
"Jastrebarsko" "DataCross" OR "PCK"
"Jalševac" "podatkovni centar" Jastrebarsko
"Križ" "Podatkovni centar Križ"
"Velika Gorica" "data centar" OR "podatkovni centar"
"Samobor" "podatkovni centar" OR "serverska soba"
"Sveta Nedelja" "podatkovni centar"
site:zagrebacka-zupanija.hr "podatkovni centar"
site:jastrebarsko.hr "podatkovni centar" OR "DataCross"
site:opcina-kriz.hr "podatkovni centar" OR "PCK"
```

### 5.3 Sisak-Moslavina / Sisačko-moslavačka županija

High-yield because of Pantheon/Topusko. Also search Sisak, Petrinja, Kutina, Glina, Novska and energy/industrial land.

```text
"Sisačko-moslavačka županija" "podatkovni centar"
"Topusko" "podatkovni centar" Pantheon
"AI razvojni i podatkovni centar Topusko"
"Pecka" "Katinovac" "Crni Potok" Pantheon
"Sisak" "data centar" OR "podatkovni centar"
"Petrinja" "podatkovni centar" OR "serverska soba"
"Kutina" "podatkovni centar" OR "trafostanica"
site:smz.hr "Pantheon" OR "podatkovni centar"
site:topusko.hr "Pantheon" OR "podatkovni centar"
site:sisak.hr "podatkovni centar" OR "serverska soba"
```

### 5.4 Varazdin / Varaždinska županija

Directory lead: DC North Varazdin. Also search Varazdin tech/industry parks and regional ISP facilities.

```text
"Varaždinska županija" "podatkovni centar"
"Varaždin" "data center" OR "data centar"
"Varaždin" "podatkovni centar" OR "kolokacija"
"DC North" "Varaždin" "data center"
"Varaždin" "serverska soba" "agregat"
site:vzz.hr "podatkovni centar"
site:varazdin.hr "podatkovni centar" OR "serverska soba"
```

### 5.5 Primorje-Gorski Kotar / Primorsko-goranska županija

Likely Rijeka port, telecom, university, and subsea/connectivity edge leads. Verify any hosting/office claims.

```text
"Primorsko-goranska županija" "podatkovni centar"
"Rijeka" "data center" OR "data centar"
"Rijeka" "kolokacija" "podatkovni centar"
"Luka Rijeka" "podatkovni centar" OR "serverska soba"
"Sveučilište u Rijeci" "podatkovni centar" OR "računalni centar"
"Opatija" "podatkovni centar" OR "data center"
site:pgz.hr "podatkovni centar"
site:rijeka.hr "podatkovni centar" OR "serverska soba"
```

### 5.6 Split-Dalmatia / Splitsko-dalmatinska županija

Likely Split telecom/tourism/public-sector edge facilities and university computing; search also Dugopolje industrial/logistics.

```text
"Splitsko-dalmatinska županija" "podatkovni centar"
"Split" "data center" OR "data centar"
"Split" "kolokacija" OR "smještaj opreme"
"Dugopolje" "podatkovni centar" OR "data center"
"Sveučilište u Splitu" "podatkovni centar" OR "računalni centar"
"Luka Split" "serverska soba" OR "podatkovni centar"
site:dalmatia.hr "podatkovni centar"
site:split.hr "podatkovni centar" OR "serverska soba"
```

### 5.7 Osijek-Baranja / Osječko-baranjska županija

Search Osijek tech park/IT cluster, university/HPC, telecom, and public-sector projects.

```text
"Osječko-baranjska županija" "podatkovni centar"
"Osijek" "data center" OR "data centar"
"Osijek" "kolokacija" OR "podatkovni centar"
"Osijek" "serverska soba" "UPS" OR "agregat"
"Sveučilište Josipa Jurja Strossmayera" "podatkovni centar"
"Čepin" "podatkovni centar" OR "data center"
site:obz.hr "podatkovni centar"
site:osijek.hr "podatkovni centar" OR "serverska soba"
```

### 5.8 Istria / Istarska županija

Search Pula, Pazin, Rovinj, Porec, Labin and tourism/municipal/ISP facilities. Distinguish real infrastructure from web-hosting brands.

```text
"Istarska županija" "podatkovni centar"
"Pula" "data center" OR "data centar"
"Pula" "kolokacija" OR "smještaj opreme"
"Pazin" "podatkovni centar" OR "serverska soba"
"Rovinj" "podatkovni centar" OR "data center"
"Poreč" "podatkovni centar" OR "data center"
site:istra-istria.hr "podatkovni centar"
site:pula.hr "podatkovni centar" OR "serverska soba"
```

### 5.9 Dubrovnik-Neretva / Dubrovačko-neretvanska županija

Tourism, port/airport, cable/edge and public-sector resilience leads; low expected commercial colo density.

```text
"Dubrovačko-neretvanska županija" "podatkovni centar"
"Dubrovnik" "data center" OR "data centar"
"Dubrovnik" "kolokacija" OR "smještaj opreme"
"Dubrovnik" "serverska soba" "agregat"
"Luka Dubrovnik" "podatkovni centar" OR "serverska soba"
"Zračna luka Dubrovnik" "podatkovni centar" OR "serverska soba"
site:dnz.hr "podatkovni centar"
site:dubrovnik.hr "podatkovni centar" OR "serverska soba"
```

### 5.10 Medimurje / Međimurska županija

Search Cakovec/industrial SMEs, cross-border fiber and regional ISP/hosting.

```text
"Međimurska županija" "podatkovni centar"
"Medimurje" "data center" OR "data centar"
"Čakovec" "podatkovni centar" OR "kolokacija"
"Cakovec" "data center" Croatia
"Prelog" "podatkovni centar" OR "serverska soba"
site:medjimurska-zupanija.hr "podatkovni centar"
site:cakovec.hr "podatkovni centar" OR "serverska soba"
```

### 5.11 Remaining county sweeps

Use these for lower-density areas, public-sector server rooms, telecom edge nodes, industrial parks, and energy-led sites:

```text
# Krapina-Zagorje / Krapinsko-zagorska
"Krapinsko-zagorska županija" "podatkovni centar"
"Krapina" "data centar" OR "serverska soba"
site:kzz.hr "podatkovni centar" OR "serverska soba"

# Karlovac / Karlovačka
"Karlovačka županija" "podatkovni centar"
"Karlovac" "data center" OR "podatkovni centar"
"Ogulin" "podatkovni centar" OR "serverska soba"
site:kazup.hr "podatkovni centar" OR "serverska soba"
site:karlovac.hr "podatkovni centar"

# Koprivnica-Krizevci / Koprivničko-križevačka
"Koprivničko-križevačka županija" "podatkovni centar"
"Koprivnica" "data centar" OR "serverska soba"
"Križevci" "podatkovni centar" OR "kolokacija"
site:kckzz.hr "podatkovni centar"

# Bjelovar-Bilogora / Bjelovarsko-bilogorska
"Bjelovarsko-bilogorska županija" "podatkovni centar"
"Bjelovar" "data centar" OR "serverska soba"
site:bbz.hr "podatkovni centar" OR "serverska soba"

# Lika-Senj / Ličko-senjska
"Ličko-senjska županija" "podatkovni centar"
"Gospić" "data centar" OR "serverska soba"
"Senj" "podatkovni centar" OR "trafostanica"
site:licko-senjska.hr "podatkovni centar"

# Virovitica-Podravina / Virovitičko-podravska
"Virovitičko-podravska županija" "podatkovni centar"
"Virovitica" "data centar" OR "serverska soba"
site:vpz.hr "podatkovni centar" OR "serverska soba"

# Pozega-Slavonia / Požeško-slavonska
"Požeško-slavonska županija" "podatkovni centar"
"Požega" "data centar" OR "serverska soba"
site:pszupanija.hr "podatkovni centar" OR "serverska soba"

# Brod-Posavina / Brodsko-posavska
"Brodsko-posavska županija" "podatkovni centar"
"Slavonski Brod" "data centar" OR "serverska soba"
site:bpz.hr "podatkovni centar"
site:slavonski-brod.hr "podatkovni centar"

# Zadar / Zadarska
"Zadarska županija" "podatkovni centar"
"Zadar" "data center" OR "data centar"
"Zadar" "serverska soba" "agregat"
site:zadarska-zupanija.hr "podatkovni centar"
site:grad-zadar.hr "podatkovni centar"

# Sibenik-Knin / Šibensko-kninska
"Šibensko-kninska županija" "podatkovni centar"
"Šibenik" "data centar" OR "serverska soba"
"Knin" "podatkovni centar" OR "data center"
site:sibensko-kninska-zupanija.hr "podatkovni centar"
site:sibenik.hr "podatkovni centar"

# Vukovar-Srijem / Vukovarsko-srijemska
"Vukovarsko-srijemska županija" "podatkovni centar"
"Vukovar" "data centar" OR "serverska soba"
"Vinkovci" "podatkovni centar" OR "kolokacija"
site:vusz.hr "podatkovni centar"
site:vukovar.hr "podatkovni centar"
```

---

## 6. Enumeration workflow and grading guidance

1. Start with **A/B operator and association seeds**: Digital Realty, A1, PCK-DataCross, DataBox, Croatian Web Hosting, HRDCA summit/member ecosystem, and HAKOM telecom operators.
2. Add **C-grade directory leads** from Baxtel, DataCenterMap, Datacenters.com, Cloudscene, Data Center Catalog and PeeringDB; normalize aliases before counting (`Altus IT` vs `Digital Realty`, `Vipnet` vs `A1`, `PCK` vs `DataCross`).
3. For each facility/project, search exact operator + address + county/city + `podatkovni centar`, then verify with eDozvola/ISPU, local government, environmental, Uptime/EN50600 certification, procurement, or contractor case study.
4. Assign county by physical site, not sales office or headquarters. Zagreb-market directory pages often place belt facilities under "Zagreb"; reassign Jastrebarsko/Križ to Zagreb County and Topusko to Sisak-Moslavina.
5. Record capacity as stated by source type: IT load MW/MVA, total power, racks, white space sqm, certification/Tier, number of technical rooms, or investment value. Do not infer IT load from generator/substation values unless explicitly stated.
6. Treat Pantheon/Topusko as **prospective** until there is a public permit/environment/grid construction trail. Its announcement volume is high, but facility enumeration should separate "announced mega-campus" from operational Croatian colo stock.

Minimum evidence fields for final enumeration:

```text
facility_name
operator_legal_name
county
municipality/city
address_or_parcel_if_public
status: operational / under construction / planned / abandoned / directory-only
evidence_grade
best_source_url
secondary_source_url
capacity_fields_with_units
notes_on_aliases_and_uncertainties
```
