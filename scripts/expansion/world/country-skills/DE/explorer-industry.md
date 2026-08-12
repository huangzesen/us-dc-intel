# DE Explorer - Industry, Trade Press, Vendors, and Query Patterns

Date: 2026-08-12. Scope: Germany datacenter enumeration from industry/trade press, vendor pages, association material, market directories, and Land/Kreis search patterns. Reliability grades: **A** = official/primary or operator-owned current source; **B** = established trade press / association / market-intelligence source that should be verified; **C** = directories, aggregators, local promo, or stale articles useful mainly as leads.

---

## 0. Germany-specific frame

- Germany is not enumerated from a single public facility registry yet. The **BAFA/BfEE Energieeffizienzregister fuer Rechenzentren (RZReg)** exists and operators report to it under the Energy Efficiency Act, but as of recent public reporting the public data surface is delayed/not yet a practical open census. Use it as a coming A-grade channel, not today's discovery base. URLs: https://www.rechenzentrums-register.de/ , https://www.bfee-online.de/BfEE/DE/Effizienzpolitik/Energieeffizienzregister_Rechenzentren/energieeffizienzregister_rechenzentren_node.html , https://www.bafa.de/SharedDocs/Kurzmeldungen/DE/Bundesamt/20240703_bfee_rzreg_start_dateneingabe.html .
- The practical enumeration backbone is: **trade press lead -> vendor/operator page -> municipal Bauleitplanung/Bebauungsplan + council docs -> UVP/BImSchG docs -> grid/heat-reuse/local utility evidence**.
- Geography is highly clustered. Start with **Frankfurt/Rhein-Main (Hessen)**, then **Berlin-Brandenburg**, **Munich/Bavaria**, **Rheinland/Ruhr/Rheinisches Revier (NRW)**, **Hamburg**, then regional colocation/HPC sites in Saxony, Lower Saxony, Schleswig-Holstein, Saarland, Baden-Wuerttemberg, and Thuringia.
- Use German terms first. "Data center" misses many municipal files; **Rechenzentrum**, **RZ**, **Datacenter**, **Datenzentrum**, **Cloud-Region**, **KI-Rechenzentrum**, **Hyperscaler**, **Colocation**, **Bebauungsplan**, **B-Plan**, **Aenderung Flaechennutzungsplan**, **Sondergebiet Rechenzentrum**, **Netzersatzanlage**, **BImSchG**, **Abwaerme**, **Netzanschluss**, **Umspannwerk** are the productive terms.

---

## 1. Trade press and industry sources

### 1.1 German-language trade/IT press

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| Datacenter-Insider | https://www.datacenter-insider.de/ ; query `site:datacenter-insider.de Rechenzentrum Deutschland {Ort}` | Best German DC-sector trade source. Good for operator announcements, regional market commentary, interviews, and local project names. Example market frame articles mention Germany's active DC count and major clusters: Frankfurt, Berlin, Munich, Rheinland, Hamburg. | B |
| heise / heise online | https://www.heise.de/ ; query `site:heise.de Rechenzentrum {Ort|Betreiber}` | Broader IT press. Good for hyperscaler/cloud-region announcements, policy, energy constraints, and controversial projects; less complete for colo facility details. | B |
| Golem.de | https://www.golem.de/ ; query `site:golem.de Rechenzentrum Deutschland {Betreiber}` | Strong on policy, EnEfG, infrastructure politics, public opposition, and "who benefits" style explainers. Use as issue/context lead, not capacity authority. | B |
| Computerwoche | https://www.computerwoche.de/data-center/ ; query `site:computerwoche.de Rechenzentrum Deutschland Frankfurt Berlin Microsoft AWS Google` | Useful for cloud-provider regions, CIO-facing market constraints, and vendor interviews. Example: Microsoft Germany investment and Frankfurt/Rheinisches Revier coverage. | B |
| iX / c't / Telepolis via Heise Media | https://www.heise.de/ | Technical and public-policy supplements. Good when project has energy, heat, or social-conflict angle. | B-/C+ |
| t3n / IT-Business / e-commerce-magazin / Digital Business Magazin | `site:t3n.de Rechenzentrum Frankfurt Strom`, `site:it-business.de Rechenzentrum NRW Microsoft`, etc. | Fast secondary leads, especially for energy/grid headlines and vendor PR syndication. Verify before storing. | C+/B- |
| DCD / Data Center Dynamics | https://www.datacenterdynamics.com/ ; query `site:datacenterdynamics.com Germany data center {operator}` | International DC trade press; often names capacity, operator, address/municipality, status, and canceled projects. Excellent cross-check for German press. | B |

### 1.2 Associations and policy/market bodies

| Source | URL | Use | Grade |
|---|---|---|---|
| eco Verband / Allianz zur Staerkung digitaler Infrastrukturen | https://www.eco.de/ , https://digitale-infrastrukturen.net/ | Policy positions, studies, operator coalition, heat reuse and Standortpolitik. Good for market-wide claims and operator ecosystem, not individual facility registry. | B |
| German Datacenter Association (GDA) | https://www.germandatacenters.com/en/ | Industry association headquartered in Frankfurt; member/partner pages identify active operators, suppliers, and municipalities. GDA reports/position papers are useful for Germany-specific policy and market context. | B |
| Bitkom | https://www.bitkom.org/ ; example market press `Rechenzentren in Deutschland: KI treibt das Wachstum` | National aggregate capacity, power, AI-capacity estimates, operator investment environment. Use for country totals and cluster ranking. | B |
| Borderstep Institut | https://www.borderstep.de/ | Research institute behind many German DC energy/market studies; often cited by eco/Bitkom/GDA. Good for methodology, energy consumption, and market sizing. | B+ |
| GTAI / U.S. International Trade Administration | https://www.gtai.de/en/invest/industries/digital-economy/data-center , https://www.trade.gov/market-intelligence/germany-information-technology-data-centers | Investor-oriented summaries; useful for market geography and vendor landscape, not facility evidence. | B- |
| JLL / CBRE / DC Byte / Structure Research reports | Example JLL: https://www.jll.com/de-de/insights/die-neue-geografie-des-deutschen-rechenzentrumsmarktes | Metro capacity and pipeline estimates. Treat as market intelligence, not source-of-record; cite when explaining clusters. | B |

### 1.3 Directories / maps

| Source | URL | Use | Grade |
|---|---|---|---|
| Data Center Map | https://www.datacentermap.com/germany/ | Fast city/operator seed list. Current crawl shows hundreds of German facilities and city counts such as Frankfurt, Berlin, Munich, Hamburg, Duesseldorf, Nuremberg, Stuttgart. Verify each facility with operator page or local filings. | C+ |
| Datacenters.com | https://www.datacenters.com/locations/germany | Commercial listing with provider/facility pages; useful for addresses and aliases, but coverage/commercial bias varies. | C+ |
| Baxtel | https://baxtel.com/data-centers/germany | Good for hyperscale/campus pages and neighboring-facility graph; use as lead and cross-check, not final evidence. | C+ |
| Datacenterplatform | https://datacenterplatform.com/data-centers/ | Often exposes German facility address lists for NTT, Digital Realty, etc.; verify via operator. | C |

Note on "geoDC": search results are noisy because "GEODE" is also an energy-distribution association. If the intended source is an internal "geoDC" industry map, treat it like Data Center Map/Baxtel: **C+ lead source** until confirmed by operator or municipal filings.

---

## 2. Vendor/operator seed list by region

Operator official pages are **A for existence/current marketed site**, **B for capacity** unless they provide a formal spec sheet. Capacity should be cross-checked against planning docs, grid/heat-network filings, press releases, or DCD/Datacenter-Insider.

### 2.1 Hessen: Frankfurt/Rhein-Main, Hanau, Offenbach, Hattersheim, Liederbach, Raunheim, Eschborn, Gross-Gerau, Karben

Primary cluster; query by municipality and Landkreis because projects sit outside Frankfurt city limits.

- **Digital Realty / Interxion** - Frankfurt and Duesseldorf. Official: https://www.digitalrealty.com/data-centers/emea/frankfurt , https://www.digitalrealty.com/data-centers/emea/dusseldorf . Also Digital Realty FRA20 press: https://www.digitalrealty.com/about/newsroom/press-releases/19811/digital-realty-begins-construction-of-its-latest-state-of-the-art-data-center-in-frankfurt . Grade A/B.
- **NTT Global Data Centers (ex-e-shelter)** - Frankfurt, Berlin, Hamburg, Munich, Bonn. Official EMEA page states it is one of/largest in Germany and lists German metro pages: https://services.global.ntt/en-us/services-and-products/global-data-centers/global-locations/emea . Frankfurt page: https://services.global.ntt/en-us/services-and-products/global-data-centers/global-locations/emea/frankfurt-data-centers . Grade A/B.
- **Equinix** - Frankfurt and Munich; official Germany page: https://www.equinix.com/data-centers/europe-colocation/germany-colocation . Grade A/B.
- **Vantage Data Centers** - Frankfurt and Berlin campuses. EMEA locations page lists Berlin total 88 MW and Frankfurt total 112 MW: https://vantage-dc.com/data-center-locations/emea/ . Frankfurt I: https://vantage-dc.com/data-center-locations/emea/frankfurt-i-germany/ . Grade A/B. Watch canceled/denied proposals: Gross-Gerau 2026 via DCD/Hessenschau is a "rejected" lead, not active.
- **CyrusOne** - Frankfurt/Hanau/Frankfurt Westside. FRA5 official: https://www.cyrusone.com/data-centers/emea/frankfurt-germany-fra5 . DCD covers FRA7 groundbreaking and status. Grade A/B.
- **STACK Infrastructure** - Frankfurt/Liederbach campus. Official: https://www.stackinfra.com/locations/emea/frankfurt/ and https://www.stackinfra.com/locations/emea/frankfurt/fra01/ . Grade A/B. Watch Babenhausen cancellation (DCD 2026).
- **Iron Mountain** - Frankfurt FRA-1/FRA-2. Official: https://www.ironmountain.com/data-centers/locations/frankfurt-data-center . Grade A/B.
- **Telehouse** - Frankfurt carrier hotel/colo. Official: https://www.telehouse.net/data-centres/frankfurt/ . Grade A/B.
- **maincubes** - Frankfurt FRA01 plus Berlin/Nauen pipeline. Official: https://www.maincubes.com/en/data-centers/ . Grade A/B.
- **Google** - Hanau own facility and Frankfurt cloud region. Official Hanau page: https://datacenters.google/intl/de_ALL/locations/hanau-germany/ . Grade A for existence.
- **AWS commercial cloud** - Europe (Frankfurt) region, `eu-central-1`; official global infrastructure pages should confirm availability zones. Grade A for region, C for exact facility inference.
- **Microsoft Azure** - Germany West Central (Frankfurt) and Germany North (Berlin) region pairing; official Azure geography page: https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies . Grade A for region, C for exact facility inference.

Hessen local search templates:
```
site:frankfurt.de Rechenzentrum Bebauungsplan
site:stadtplanungsamt-frankfurt.de Rechenzentrum Bebauungsplan "Begruendung"
site:offenbach.de Rechenzentrum Bebauungsplan Vantage
site:hanau.de Rechenzentrum Google EdgeConneX CyrusOne Bebauungsplan
site:hattersheim.de Rechenzentrum Abwaerme NTT
site:liederbach.eu Rechenzentrum STACK Bebauungsplan
site:raunheim.de Rechenzentrum Vantage Bebauungsplan
site:gross-gerau.de Rechenzentrum Vantage Stadtverordnetenversammlung
site:rim.ekom21.de Rechenzentrum "{Kommune}" Beschlussvorlage
site:uvp-verbund.de Rechenzentrum Hessen Netzersatzanlage
"{Kommune}" "Sondergebiet Rechenzentrum" OR "SO Rechenzentrum"
```

### 2.2 Berlin and Brandenburg: Berlin, Teltow-Flaming, Havelland/Nauen, Ludwigsfelde, Brandenburg AWS sovereign cloud

- **Vantage** - Berlin I/II campuses; official EMEA page lists Berlin total 88 MW: https://vantage-dc.com/data-center-locations/emea/ . Grade A/B.
- **NTT** - Berlin 1/2. Official: https://services.global.ntt/en-us/services-and-products/global-data-centers/global-locations/emea/berlin-data-centers . Grade A/B.
- **maincubes** - BER02/mainHub Nauen. Official BER02: https://www.maincubes.com/en/data-centers/berlin-cloud-ai-provider-campus-ber02/ ; zoning/grid press: https://www.maincubes.com/en/press/zoning-plan-approved-and-grid-connection-agreement-signed-maincubes-to-begin-development-of-mainhub-berlin-data-centre-campus-in-nauen/ . Grade A/B.
- **Google Cloud** - Berlin-Brandenburg region opened in 2023. Official: https://cloud.google.com/blog/products/infrastructure/berlin-brandenburg-google-cloud-region-is-now-open . Grade A for region.
- **AWS European Sovereign Cloud** - first AWS European Sovereign Cloud region in Brandenburg, generally available/opened in 2026. Official: https://aws.amazon.com/blogs/aws/opening-the-aws-european-sovereign-cloud/ and https://aws.eu/ . Grade A for region/state, C for exact site until local filings identify municipality.
- **NorthC** - acquired Colt European DCs and lists German sites in Berlin/Hamburg/Duesseldorf/Frankfurt/Nuremberg/Munich. Official: https://www.northcdatacenters.com/de/northc-datacenters/ . Grade A/B.

Berlin/Brandenburg query templates:
```
site:berlin.de Rechenzentrum Bebauungsplan BImSchG Netzersatzanlage
site:uvp-verbund.de Rechenzentrum Berlin Netzersatzanlage
site:bb.beteiligung.diplanung.de Rechenzentrum
site:brandenburg.de Rechenzentrum Bebauungsplan
site:nauen.de Rechenzentrum maincubes "Bebauungsplan" OR "Sondergebiet"
"Bebauungsplan" "Rechenzentrum 2" Nauen
"AWS" "Brandenburg" "Rechenzentrum" "Bebauungsplan"
"European Sovereign Cloud" Brandenburg Rechenzentrum Gemeinde
```

### 2.3 Nordrhein-Westfalen: Rheinland/Ruhr/Rheinisches Revier, Duesseldorf, Cologne, Bonn, Aachen, Bergheim, Bedburg, Elsdorf, Grevenbroich

- **Microsoft** - 3.2bn EUR Germany investment focused on Frankfurt expansion and Rheinisches Revier. Official Microsoft Germany: https://news.microsoft.com/de-de/ki-rechenzentren-fuer-das-rheinische-revier-und-ganz-deutschland-microsoft-stellt-plaene-in-nrw-vor-und-startet-qualifizierungsoffensive/ . NRW government: https://www.land.nrw/pressemitteilung/von-der-kohle-zur-ki-plaene-fuer-ki-rechenzentren-von-microsoft-im-rheinischen . Construction/start updates: https://www.wirtschaft.nrw/spatenstich-fuer-die-microsoft-rechenzentren-im-rheinischen-revier-nordrhein-westfalen-wird . Grade A for announcement/status, still verify each site via municipal permits.
- **Digital Realty** - Duesseldorf. Official: https://www.digitalrealty.com/data-centers/emea/dusseldorf . Grade A/B.
- **NTT** - Bonn campus historically important; check NTT EMEA/Germany pages. Grade A/B.
- **NorthC** - Duesseldorf and other acquired Colt assets. Official German locations page above. Grade A/B.
- Regional/smaller: PlusServer (Cologne), myLoc (Duesseldorf), 23M, q.beyond, regio iT Aachen, municipal IT service providers; search local providers and RZ terms.

NRW query templates:
```
site:land.nrw Rechenzentrum Microsoft Rheinisches Revier
site:wirtschaft.nrw Rechenzentrum Microsoft Bergheim Bedburg Elsdorf
site:bergheim.de Microsoft Rechenzentrum Bebauungsplan
site:bedburg.de Microsoft Rechenzentrum Bebauungsplan
site:elsdorf.de Microsoft Rechenzentrum Bebauungsplan
site:grevenbroich.de Microsoft Rechenzentrum Grundstueck Baugenehmigung
site:duesseldorf.de Rechenzentrum Bebauungsplan Digital Realty NorthC
site:koeln.de Rechenzentrum Bebauungsplan Colocation
site:uvp-verbund.de Rechenzentrum Nordrhein-Westfalen Netzersatzanlage
"Rheinisches Revier" "KI-Rechenzentrum" Microsoft "Baugenehmigung"
```

### 2.4 Bayern: Munich/Aschheim, Nuremberg, Augsburg, Regensburg, Erlangen, Garching

- **Equinix** - Munich MU sites, including Aschheim/Landkreis Muenchen; Datacenter-Insider article on MU4 has rack/space numbers. Official Germany page above. Grade A/B.
- **NTT** - Munich data centers. Official NTT EMEA page links Munich. Grade A/B.
- **NorthC** - Munich/Nuremberg German sites. Official German locations page above. Grade A/B.
- **Hetzner** - Nuremberg/Falkenstein and other German facilities; official data center parks: https://www.hetzner.com/unternehmen/rechenzentrum/ . Grade A/B.
- **LEW TelNet / LEW Green Data Center** - Augsburg regional facility; search Datacenter-Insider and local press. Grade B until official/spec.
- **HPC/AI** - Leibniz Supercomputing Centre (LRZ, Garching) and planned/announced AI factories in Munich/Bavaria; use official Bavarian government/HPC pages for non-colo research DCs. Grade A.

Bayern query templates:
```
site:bayern.de Rechenzentrum KI-Fabrik Muenchen
site:muenchen.de Rechenzentrum Bebauungsplan
site:aschheim.de Rechenzentrum Equinix Bebauungsplan
site:nuernberg.de Rechenzentrum Hetzner NorthC Bebauungsplan
site:augsburg.de "Green Data Center" LEW Rechenzentrum
site:uvp-verbund.de Rechenzentrum Bayern Netzersatzanlage
"Landkreis Muenchen" Rechenzentrum Aschheim Equinix
"Falkenstein" Hetzner Rechenzentrum Bebauungsplan
```

### 2.5 Hamburg, Schleswig-Holstein, Lower Saxony, Bremen

- **NTT** - Hamburg 1. Official NTT EMEA page. Grade A/B.
- **NorthC** - Hamburg German site. Grade A/B.
- **GlobalConnect / wilhelm.tel / municipal and regional providers** - search by city/operator. Grade B/C until official.
- **Hannover legacy hosting** - Hostway/Ionos-style regional DCs; older Computerwoche articles can seed, but verify because operators and brands changed.
- **Northern Germany edge/green DCs** - query industrial parks, wind-power PPAs, district-heating projects.

Northern query templates:
```
site:hamburg.de Rechenzentrum Bebauungsplan Abwaerme
site:uvp-verbund.de Rechenzentrum Hamburg Netzersatzanlage
site:schleswig-holstein.de Rechenzentrum Bebauungsplan
site:niedersachsen.de Rechenzentrum UVP Netzersatzanlage
site:hannover.de Rechenzentrum Bebauungsplan
site:bremen.de Rechenzentrum Bebauungsplan
"Rechenzentrum" "Abwaerme" Hamburg
"Rechenzentrum" "Windstrom" Schleswig-Holstein
```

### 2.6 Baden-Wuerttemberg, Saxony, Saxony-Anhalt, Thuringia, Saarland, Rheinland-Pfalz, Mecklenburg-Vorpommern

- **Baden-Wuerttemberg** - Stuttgart/Leinfelden/Heidelberg/Mannheim, plus HLRS Stuttgart (research/HPC). Query local IT providers, university/HPC centers, Bosch/Daimler industrial cloud projects. Grade mixed.
- **Saxony** - Leipzig/Dresden; look for cloud/semiconductor supply-chain DCs and university/HPC. Grade mixed.
- **Saxony-Anhalt** - Magdeburg: historical Microsoft Germany trustee cloud was Frankfurt + Magdeburg, but that sovereign model is legacy/stale; verify current status before counting. Grade C until current official.
- **Thuringia** - Erfurt/Jena regional IT and government DCs. Grade mixed.
- **Saarland** - Saarlouis/Saarbruecken small colo/enterprise sites; use Data Center Map as seed and local permits. Grade C/B.
- **Rheinland-Pfalz** - Nierstein/Mainz edge of Rhein-Main, possible NTT project leads; use municipal council docs and local press. Grade B once permits found.
- **Mecklenburg-Vorpommern** - low density; query renewable/edge/public-sector DCs.

Broad query templates:
```
site:{land-or-city-domain} Rechenzentrum Bebauungsplan
site:{land-or-city-domain} Rechenzentrum Baugenehmigung
site:{land-or-city-domain} Rechenzentrum Netzersatzanlage BImSchG
site:uvp-verbund.de Rechenzentrum "{Land}"
site:ratsinfo.* Rechenzentrum "{Kommune}"
site:rim.ekom21.de Rechenzentrum "{Kommune}"
"{Landkreis}" "Rechenzentrum" "Bebauungsplan"
"{Kommune}" "Sondergebiet Rechenzentrum"
"{Kommune}" "Aenderung des Flaechennutzungsplans" Rechenzentrum
```

---

## 3. Hyperscaler/cloud official pages

Cloud region pages are **A for operational logical region/state/metro**, not for physical facility address. Germany's exact hyperscaler sites are often leased, multi-AZ, or intentionally obscured.

| Provider | German region signal | URL | Grade |
|---|---|---|---|
| AWS | Europe (Frankfurt) commercial region; AWS European Sovereign Cloud first region in Brandenburg, opened/GA in 2026 | https://aws.amazon.com/about-aws/global-infrastructure/ , https://aws.amazon.com/blogs/aws/opening-the-aws-european-sovereign-cloud/ , https://aws.eu/ | A region / C facility |
| Microsoft Azure | Germany West Central (Frankfurt), Germany North (Berlin); 2024-2026 Germany investment in Frankfurt and Rheinisches Revier | https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies , https://news.microsoft.com/de-de/ki-rechenzentren-fuer-das-rheinische-revier-und-ganz-deutschland-microsoft-stellt-plaene-in-nrw-vor-und-startet-qualifizierungsoffensive/ | A region / B project / C facility |
| Google Cloud | Frankfurt region and Berlin-Brandenburg region; Hanau own data center | https://cloud.google.com/about/locations , https://cloud.google.com/blog/products/infrastructure/berlin-brandenburg-google-cloud-region-is-now-open , https://datacenters.google/intl/de_ALL/locations/hanau-germany/ | A region/site |
| Oracle Cloud | Frankfurt region `eu-frankfurt-1`; cross-check Oracle official regions | https://www.oracle.com/cloud/cloud-regions/ | A region / C facility |
| SAP / Schwarz Digits / IONOS / Open Telekom Cloud | German sovereign/enterprise cloud providers; often use own or partner DCs in Germany | Query provider official pages plus `Rechenzentrum Standort` | A/B |

Cloud pivot queries:
```
"{provider}" "Deutschland" "Rechenzentrum" "Region"
"{provider}" "Germany West Central" Frankfurt Rechenzentrum
"{provider}" "Berlin-Brandenburg" "cloud region" Rechenzentrum
"{provider}" "Brandenburg" "Bebauungsplan" "Rechenzentrum"
"{provider}" "Rheinisches Revier" Microsoft Rechenzentrum Baugenehmigung
```

---

## 4. Municipal / Land / Kreis discovery method

### 4.1 Why Kreis-level search matters

German hyperscale projects usually surface first as **Bauleitplanung** or **Stadtverordnetenversammlung/Gemeinderat** items, not as a national filing. The owner may be a property SPV or a developer, not the final cloud tenant. Search all aliases:

- project type: `Rechenzentrum`, `Datacenter`, `Datenzentrum`, `Hyperscale-Rechenzentrum`, `KI-Rechenzentrum`
- planning instruments: `Bebauungsplan`, `B-Plan`, `Flaechennutzungsplan`, `Regionaler Flaechennutzungsplan`, `Sondergebiet`, `Gewerbegebiet`
- procedure terms: `fruehzeitige Beteiligung`, `Offenlage`, `Abwaegung`, `Satzungsbeschluss`, `Baugenehmigung`, `Beschlussvorlage`
- environmental/technical: `UVP`, `BImSchG`, `Netzersatzanlage`, `Dieselgenerator`, `Kuehlanlage`, `Umspannwerk`, `Netzanschluss`, `Abwaerme`, `Fernwaerme`
- systems: `Ratsinformationssystem`, `RIS`, `sdnetrim`, `SessionNet`, `Allris`, `Buergerinfo`, `DiPlanung`

### 4.2 A-grade confirmation portals

| Channel | URL / pattern | What it confirms | Grade |
|---|---|---|---|
| Municipal planning pages | `site:{kommune}.de Rechenzentrum Bebauungsplan` | Land-use approval, parcel/location, owner/developer, status. | A |
| Council/RIS docs | `site:rim.ekom21.de Rechenzentrum`, `site:ris.{kommune}.de Rechenzentrum`, `site:buergerinfo.{kommune}.de Rechenzentrum` | Political decisions, rejection/approval, development agreements, staff reports. | A |
| DiPlanung participation portal | https://bb.beteiligung.diplanung.de/ for Brandenburg/Berlin planning participation | Public planning procedures, especially Nauen/Berlin-Brandenburg projects. | A |
| UVP-Verbund / UVP portals | https://www.uvp-verbund.de/ , https://www.uvp-portal.de/de | Environmental assessment and authority docs for generators/cooling/industrial facilities. | A |
| BAFA/BfEE RZReg | https://www.rechenzentrums-register.de/ | Future energy-efficiency register; when public data appears, should confirm operator/site specs. | A |
| Land-level press/ministries | `site:{land}.de Rechenzentrum Microsoft AWS Google` | Major projects with political announcements, permits, funding, or economic-development status. | A/B |

### 4.3 Per-Land sweep starter list

Use these as first-pass queries, then pivot to Kreis/Kommune names found in results.

```
site:hessen.de Rechenzentrum
site:frankfurt.de OR site:stadtplanungsamt-frankfurt.de Rechenzentrum Bebauungsplan
site:berlin.de Rechenzentrum
site:brandenburg.de OR site:bb.beteiligung.diplanung.de Rechenzentrum
site:land.nrw Rechenzentrum OR site:wirtschaft.nrw Rechenzentrum
site:bayern.de Rechenzentrum
site:hamburg.de Rechenzentrum
site:niedersachsen.de Rechenzentrum
site:schleswig-holstein.de Rechenzentrum
site:baden-wuerttemberg.de Rechenzentrum
site:sachsen.de Rechenzentrum
site:sachsen-anhalt.de Rechenzentrum
site:thueringen.de Rechenzentrum
site:rlp.de Rechenzentrum
site:saarland.de Rechenzentrum
site:mv-regierung.de Rechenzentrum
site:bremen.de Rechenzentrum
```

Preferred search-engine form:
```
("{Land}" OR "{Kreis}" OR "{Kommune}") ("Rechenzentrum" OR "Datacenter" OR "KI-Rechenzentrum") ("Bebauungsplan" OR "Baugenehmigung" OR "BImSchG" OR "UVP" OR "Netzanschluss" OR "Abwaerme")
```

---

## 5. Reliability grading rules

| Evidence item | Grade | Notes |
|---|---|---|
| Operator official location/spec page | A for existence/current marketed location; B for capacity | Operator pages can round MW and include future phases. |
| Hyperscaler official region page | A for logical region/metro/state | Does not identify physical DCs/AZs. Do not infer exact facility without other evidence. |
| Municipal Bebauungsplan / council decision / Baugenehmigung | A | Best source for proposed/rejected/approved status and parcel. |
| UVP/BImSchG docs | A | Best source for generators, environmental procedure, sometimes thermal/electrical details. |
| BAFA/BfEE RZReg public data, if/when accessible | A | Treat current site as proof of reporting framework, not an open census until data is actually visible. |
| DCD, Datacenter-Insider, heise, Golem, Computerwoche | B | Strong leads; store article URL and verify with A source before marking operational or approved. |
| eco/GDA/Bitkom/Borderstep/JLL/GTAI/ITA | B | Good market/association context; generally not facility registry. |
| Data Center Map, Datacenters.com, Baxtel, Datacenterplatform | C+ | Useful seed lists/addresses. Verify all rows; can be stale, commercial, duplicated, or projected. |
| Local newspaper article | B-/C+ | Good for council vote and public conflict; poor for technical specs unless quoting official docs. |
| Vendor LinkedIn/social posts | C+ | Useful milestone leads; verify with official press or municipal docs. |

Status semantics:

- `announced` / `investment planned`: do not count as built.
- `Bebauungsplan in Aufstellung`, `fruehzeitige Beteiligung`: proposed.
- `Satzungsbeschluss`, `Baugenehmigung erteilt`, `grid connection signed`: approved/enabled, not necessarily started.
- `Spatenstich`, `Baubeginn`, `Richtfest`: under construction.
- `in Betrieb`, `opened`, `customer ready`, `live`, `GA region`: operational, but still distinguish shell, fitted IT load, and leased capacity.
- `abgelehnt`, `zurueckgezogen`, `aufgegeben`: rejected/canceled; preserve as negative evidence to avoid re-adding from stale directory pages.

---

## 6. Recommended enumeration workflow

1. Seed metro/operator table from Data Center Map + Datacenters.com + Baxtel + vendor pages for NTT, Digital Realty, Equinix, Vantage, CyrusOne, STACK, Iron Mountain, Telehouse, maincubes, NorthC, Hetzner, Google, AWS, Microsoft, Oracle.
2. For each seed, normalize to `(ultimate operator, campus name, municipality, Kreis, Land, status, capacity type, evidence URL)`.
3. Run trade press queries by operator and municipality:
   ```
   site:datacenter-insider.de "{operator}" "{Ort}" Rechenzentrum
   site:datacenterdynamics.com "{operator}" Germany "{Ort}"
   site:heise.de "{Ort}" Rechenzentrum
   site:golem.de "{Ort}" Rechenzentrum
   site:computerwoche.de "{operator}" Deutschland Rechenzentrum
   ```
4. For every non-operational or large-capacity claim, pivot to official local docs:
   ```
   "{Ort}" "{operator}" Bebauungsplan Rechenzentrum
   "{Ort}" "{campus}" "Sondergebiet Rechenzentrum"
   site:uvp-verbund.de "{Ort}" Rechenzentrum
   site:rim.ekom21.de "{Ort}" Rechenzentrum
   ```
5. Add national/association context only after facility evidence is captured: eco/GDA/Bitkom/Borderstep/JLL for cluster totals and policy constraints.
6. Re-run cancellation/rejection queries for pipeline items:
   ```
   "{operator}" "{Ort}" Rechenzentrum abgelehnt
   "{operator}" "{Ort}" Rechenzentrum zurueckgezogen
   "{operator}" "{Ort}" Rechenzentrum gestoppt
   "{operator}" "{Ort}" Rechenzentrum Babenhausen Gross-Gerau Karben
   ```

Key pitfalls:

- Frankfurt market data often includes adjacent municipalities in Main-Taunus-Kreis, Offenbach, Gross-Gerau, Wetteraukreis, Hanau/Main-Kinzig-Kreis, and Darmstadt-Dieburg. Store the actual municipality, not just "Frankfurt".
- Cloud-region existence is not a facility census. One region has multiple AZs; one AZ can use multiple buildings; exact sites can be leased.
- Directories duplicate campus buildings and list planned shells as facilities. Dedupe on address/campus/phase.
- "Rheinisches Revier" Microsoft items refer to multiple NRW municipalities; track Bergheim, Bedburg, Elsdorf, and newer Grevenbroich separately.
- Legacy "Microsoft Germany Cloud" Frankfurt + Magdeburg articles from 2015-2018 are historical. Do not count Magdeburg as current Microsoft cloud capacity without current official confirmation.
