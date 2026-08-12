# NL Explorer - Industry, Trade Press, Vendors, and Province Query Patterns

Date: 2026-08-12. Scope: Netherlands, Kingdom of the datacenter enumeration from industry/trade press, vendor/operator pages, DDA material, public announcement surfaces, and repeatable province/special-municipality search patterns. Reliability grades: **A** = official/primary source or operator-owned current source; **B** = established trade press, association, or strong secondary source requiring verification; **C** = directory/aggregator/weak secondary lead.

---

## 0. Netherlands-specific frame

- Do not enumerate the Netherlands from one registry. The practical workflow is: **DDA/operator/directories seed -> Dutch trade press lead -> official operator page -> Officiele Bekendmakingen / local omgevingsvergunning / omgevingsplan / municipal policy evidence -> grid or environmental cross-check**.
- The mainland market is clustered in **Noord-Holland / Amsterdam-MRA / Schiphol / Haarlemmermeer / Hollands Kroon**, then **Groningen/Eemshaven**, **Zuid-Holland/Rotterdam-Delft-Alphen**, **Noord-Brabant/Eindhoven-Roosendaal-Steenbergen-Rijen**, **Utrecht/Nieuwegein-Groenekan**, **Overijssel/Enschede-Hengelo-Zwolle**, and smaller regional/edge sites elsewhere.
- Use Dutch terms first. Productive terms: `datacenter`, `datacentrum`, `datacentra`, `rekencentrum`, `computercentrum`, `serverruimte`, `colocatie`, `housing`, `cloud regio`, `hyperscale datacenter`, `omgevingsvergunning`, `milieubelastende activiteit`, `bouwactiviteit`, `bestemmingsplan`, `omgevingsplan`, `paraplubestemmingsplan`, `beheersverordening`, `voorbereidingsbesluit`, `aansluitvermogen`, `MVA`, `noodstroomaggregaten`, `restwarmte`, `netcongestie`.
- Current policy matters. A national hyperscale restriction entered Dutch planning law from 2024: hyperscale projects, generally over 10 ha and 70 MW, are heavily restricted, with exceptions for areas such as **Het Hogeland/Eemshaven** and **Hollands Kroon/Agriport A7**. Treat legal/policy articles as context, then verify individual projects through permits. Sources: Greenberg Traurig summary https://www.gtlaw.com/en/insights/2024/3/challenges-in-the-dutch-data-center-market ; draft/official documents surfaced via `open.overheid.nl` / `wetgevingskalender.overheid.nl` / `lokaleregelgeving.overheid.nl`.
- Permit notices are often in Dutch official publications rather than a friendly planning portal. Search `zoek.officielebekendmakingen.nl` and local/provincial `omgevingsdienst` sites for `omgevingsvergunning`, `vergunning verleend`, `ontwerpbeschikking`, `aanvraag`, and exact addresses.

---

## 1. Industry and trade-press sources

### 1.1 Dutch sector association and maps

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| Dutch Data Center Association (DDA) | https://www.dutchdatacenters.nl/en/ ; participants https://www.dutchdatacenters.nl/en/participants/ ; map https://www.dutchdatacenters.nl/en/map/ | Best national sector starting point. Participant pages and the Datacenter Guide 2026 are strong seeds for operators, addresses, and market coverage; the guide claims broad coverage of Dutch capacity. Not a government registry. | B |
| DDA Dutch pages | `site:dutchdatacenters.nl/deelnemers/ {operator}` and `site:dutchdatacenters.nl datacenter {plaats}` | Dutch-language participant pages sometimes expose more precise local names/addresses than English pages. | B |
| Datacenter Platform Netherlands | https://datacenterplatform.com/countries/netherlands/ | Market/directory view; useful for supplier and facility seeds. Verify via operator or official notice. | C+ |
| Data Center Map Netherlands | https://www.datacentermap.com/the-netherlands/ | Broad city/operator seed list; useful for small regional sites and Caribbean dependencies when official pages are thin. | C |
| Baxtel / Datacenters.com / Inflect / PeeringDB | `baxtel.com/data-center/netherlands`, `datacenters.com/locations/netherlands`, `peeringdb.com` | Good cross-check for addresses, facility aliases, IXP presence, and capacity snippets. Never final evidence alone for status or MW. | C/C+ |

### 1.2 Dutch and international trade press

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| Dutch IT Channel | https://www.dutchitchannel.nl/ ; `site:dutchitchannel.nl datacenter Nederland {operator|plaats}` | Required Dutch trade-press pass. Good for operator expansions, energy/transparency controversy, partner ecosystem, and reposted vendor announcements. Example topics include Google/Microsoft energy disclosure and Equinix Amsterdam expansion. | B |
| Computable | https://www.computable.nl/ ; `site:computable.nl datacenter {plaats|operator}` | Dutch IT/business press. Good for cloud-region and vendor market context. | B- |
| Tweakers / Tweakers Pro | https://tweakers.net/ ; `site:tweakers.net datacenter Nederland Microsoft Google Zeewolde` | Strong for public controversy, hyperscale policy, energy, and local-government debate. Verify facility details elsewhere. | B- |
| Techzine | https://www.techzine.eu/ ; `site:techzine.eu Netherlands hyperscale data center permits` | English-language Dutch tech press. Useful for current summaries such as permitted hyperscale pipeline claims; verify every project individually. | B-/C+ |
| NL Times / DutchNews / NRC-derived reports | `site:nltimes.nl datacenter Amsterdam vergunning`, `site:dutchnews.nl datacenter Microsoft Google` | English-accessible leads from Dutch mainstream/local reporting. Good for recent permits and political conflict; verify via official notice. | B-/C+ |
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com/ ; `site:datacenterdynamics.com Netherlands data center {operator|plaats}` | Best international DC trade source for Dutch hyperscale, Amsterdam moratorium, vendor expansions, and exact project status. | B |
| Telecompaper | https://www.telecompaper.com/ ; `site:telecompaper.com Dutch data centre hyperscale` | Telecom/ICT trade press; often paywalled but snippets are useful leads. | C+/B- |

### 1.3 Official/public-record surfaces to pair with press leads

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| Officiele Bekendmakingen | https://zoek.officielebekendmakingen.nl/ ; `site:zoek.officielebekendmakingen.nl datacenter omgevingsvergunning {plaats}` | Core public notice search. Finds municipal/provincial notices, PDFs, environmental permits, objections, applications, and decisions. Examples include Haarlem/J.W. Lucasweg, Halfweg/CyrusOne, Plimsollweg Amsterdam, Alphen aan den Rijn/Boerhaaveweg. | A |
| Lokale wet- en regelgeving | https://lokaleregelgeving.overheid.nl/ ; `site:lokaleregelgeving.overheid.nl datacenters {gemeente}` | Local datacenter policy, parapluplan, beheersverordening, preparatory decisions. Example Haarlemmermeer datacenter rules. | A |
| Omgevingswet / Omgevingsloket | https://omgevingswet.overheid.nl/ | National permitting framework. Public search is less convenient for historical enumeration, but vocabulary and activity categories help decode notices. | A context |
| Ruimtelijkeplannen legacy searches | `site:ruimtelijkeplannen.nl datacenter {gemeente}` | Useful for older bestemmingsplan documents and plan IDs such as Haarlemmermeer/Zeewolde-era files. | A/B depending on document |
| Provincial and municipal sites | `site:{gemeente}.nl datacenter omgevingsvergunning`, `site:{provincie}.nl datacenter`, `site:{omgevingsdienst}.nl datacenter` | Confirm local policy, council decisions, environmental-permit PDFs, and public participation pages. | A |
| Parliamentary/open government | https://open.overheid.nl/ ; `site:open.overheid.nl datacenter Zeewolde Microsoft Google` | National policy letters, parliamentary answers, and ministerial context. Good for hyperscale restrictions and controversial cases. | A |

---

## 2. Dutch search patterns

### 2.1 Broad discovery

```text
("datacenter" OR "datacentrum" OR "datacentra" OR "rekencentrum") ("Nederland" OR "{provincie}" OR "{gemeente}") ("MW" OR MVA OR "aansluitvermogen" OR "vierkante meter")
site:dutchitchannel.nl ("datacenter" OR "datacentrum") ({operator} OR {gemeente} OR {provincie})
site:datacenterdynamics.com Netherlands "data center" ({operator} OR {municipality})
site:dutchdatacenters.nl/en/participants/ {operator}
site:dutchdatacenters.nl/deelnemers/ {operator}
site:datacentermap.com/the-netherlands/ {plaats} datacenter
site:baxtel.com/data-center/netherlands {operator} {plaats}
```

### 2.2 Permit/status confirmation

```text
site:zoek.officielebekendmakingen.nl ("datacenter" OR "datacentrum" OR "rekencentrum") "{gemeente}"
site:zoek.officielebekendmakingen.nl ("omgevingsvergunning" OR "vergunning verleend" OR "aanvraag vergunning" OR "ontwerpbeschikking") "datacenter" "{plaats}"
site:zoek.officielebekendmakingen.nl ("milieubelastende activiteit" OR "milieu, bouw" OR "noodstroomaggregaten") "datacenter"
site:lokaleregelgeving.overheid.nl ("datacenter" OR "datacentra") "{gemeente}"
site:{gemeente}.nl ("datacenter" OR "datacentrum") ("omgevingsvergunning" OR "bestemmingsplan" OR "omgevingsplan" OR "raad")
site:{provincie-domain} ("datacenter" OR "datacentrum") ("omgevingsvergunning" OR "bezwaar" OR "zienswijze")
```

### 2.3 Policy, power, and opposition

```text
"hyperscale datacenter" "Nederland" ("verbod" OR "beperking" OR "Besluit kwaliteit leefomgeving")
"datacenter" "netcongestie" "{provincie}" OR "{gemeente}"
"datacenter" "restwarmte" "{gemeente}"
"datacenter" "stroomverbruik" Google Microsoft Nederland
"datacenter" "waterschap" "{gemeente}" OR "{provincie}"
"datacenter" "stikstof" "omgevingsvergunning"
```

### 2.4 Lifecycle/status vocabulary

- **Lead only**: `plan`, `voornemen`, `beoogd`, `locatieonderzoek`, `grondpositie`, `intentieovereenkomst`, `MOU`, `ontwikkelruimte`.
- **Permit evidence**: `aanvraag omgevingsvergunning`, `ontwerpbeschikking`, `vergunning verleend`, `zaaknummer`, `OLO-nummer`, `bouwactiviteit`, `milieubelastende activiteit`, `handelen in strijd met regels ruimtelijke ordening`.
- **Planning evidence**: `bestemmingsplan`, `omgevingsplan`, `paraplubestemmingsplan`, `beheersverordening`, `voorbereidingsbesluit`, `planidentificatie NL.IMRO`.
- **Construction/operation**: `start bouw`, `eerste paal`, `oplevering`, `ingebruikname`, `operationeel`, operator facility page live, IXP/facility active in PeeringDB.
- **Rejected/canceled**: `ingetrokken`, `vernietigd`, `afgewezen`, `geschorst`, `Raad van State`, `beroepsprocedure`, `voorbereidingsbesluit`.

---

## 3. Major operators and developers to pivot

Official operator pages are **A for current marketed existence/location**, **B for capacity unless facility specs are explicit**, and **C for exact hyperscaler physical mapping when only a cloud region is known.

| Operator/developer | Official URL / lead URL | Province/cluster pivots | Notes |
|---|---|---|---|
| Digital Realty | https://www.digitalrealty.com/data-centers/emea/amsterdam | Noord-Holland/Amsterdam, Schiphol area | Official page lists 12 Amsterdam data centers and colocation ecosystem. DCD reported AMS11 27 MW and Dutch footprint increase to about 159 MW: https://www.datacenterdynamics.com/en/news/digital-realty-opens-new-27mw-data-center-campus-in-amsterdam-the-netherlands/ . |
| Equinix | https://www.equinix.com/data-centers/europe-colocation/netherlands-colocation | Noord-Holland/Amsterdam, Overijssel/Enschede, Overijssel/Zwolle | Official page says 11 Dutch data centers across Amsterdam, Enschede, and Zwolle. Search AM/EN/ZW site pages individually. |
| NorthC Datacenters | https://www.northcdatacenters.com/en/northc-datacenters/ | Noord-Holland, Flevoland, Groningen, Utrecht, Zuid-Holland, Noord-Brabant | Best regional operator seed. Official page lists Aalsmeer, Almere, Amsterdam, Delft, Rotterdam, Eindhoven, Groningen, Nieuwegein, etc. DCD article on 4.5 MW Amsterdam expansion lists Dutch footprint across 13 facilities. |
| Google | Eemshaven https://datacenters.google/locations/eemshaven-netherlands-var ; Middenmeer https://datacenters.google/locations/middenmeer-netherlands | Groningen, Noord-Holland | Official pages confirm Eemshaven and Middenmeer. Also search Oldambt/Oostpolder leads; verify via province/gemeente notices before counting new build. |
| Microsoft | Community page https://local.microsoft.com/communities/emea/north-holland/ ; Azure geography https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies | Noord-Holland/Hollands Kroon/Middenmeer, Amsterdam/Westpoort | Official community page confirms Middenmeer datacenter. Use permits and press for expansions/leased campuses; exact Azure region physical sites remain non-public. |
| Iron Mountain Data Centers | https://www.ironmountain.com/data-centers/locations/amsterdam-data-center | Noord-Holland/Haarlem/Amsterdam region | Official AMS-1 page gives expansion status/capacity; verify permits at Haarlem/J.W. Lucasweg in Officiele Bekendmakingen. |
| CyrusOne | https://cyrusone.com/locations/europe/amsterdam-netherlands/ or official regional pages; permit notices | Noord-Holland/Halfweg/Haarlemmermeer | Search `CyrusOne AMS3`, `Linieweg 3 Halfweg`, and official notices. |
| Global Switch | https://www.globalswitch.com/data-centres/amsterdam/ | Noord-Holland/Amsterdam | Carrier hotel/hyperscale host; official page for existence, DDA/PeeringDB for ecosystem. |
| Colt DCS | https://www.coltdatacentres.net/en-GB/our-locations/data-centre-locations-europe/rotterdam | Noord-Brabant/Roosendaal despite Rotterdam marketing name | Official page places Rotterdam DC in Roosendaal and gives 15 MW potential max IT power. |
| QTS | https://q.com/data-centers/netherlands-groningen/ | Groningen | Official Groningen page; verify exact local permits if expanding. |
| Penta Infra | https://penta-infra.com/data-centers/ | Friesland/Leeuwarden, Limburg/Geleen | Official pages list LEE01/LEE02 and GLN01. |
| Eurofiber Cloud Infra / Nedzone | https://www.eurofiber.com/en-nl/services/our-data-centers | Utrecht/Groenekan, Zuid-Holland/Rotterdam, Noord-Brabant/Steenbergen | Operator pages useful for regional Tier 3 facilities. |
| InterDC / InterRacks | https://www.interdc.nl/ | Gelderland/Doetinchem, Overijssel/Enschede/Hengelo | Official pages disclose regional Tier 3-designed sites and rack counts. |
| Kolo / Serverius | https://kolodc.com/ | Flevoland/Dronten, Drenthe/Meppel | Kolo/Serverius pages seed northern/eastern regional sites. |
| Cellnex Netherlands edge datacentres | https://www.cellnex.com/nl-en/technology/edge-datacentres/ | Drenthe, Flevoland, Friesland, Gelderland, Zeeland, other tower locations | Official page lists multiple tower-based edge datacentres with surface/kVA for some sites. |
| Previder | https://previder.com/services/datacenter | Overijssel/Hengelo, Noord-Brabant/Rijen | Official page references four Dutch datacenters in Hengelo and Rijen. |
| Smartdc | https://www.smartdc.net/data-centers/locations/rotterdam/ | Zuid-Holland/Rotterdam | Official page confirms Rotterdam facility and power/network details. |
| Switch Datacenters | https://www.switchdatacenters.com/ | Noord-Holland/Amsterdam/Diemen | Search AMS site codes, DDA page, and Amsterdam permits. |
| Interconnect | https://www.interconnect.nl/ | Noord-Brabant/'s-Hertogenbosch/Eindhoven region | Regional operator; use official pages/DDA and local searches. |
| Aruba, Curacao, Sint Maarten operators | SETAR https://www.setar.aw/business/cloud-hosting/data-center-services/ ; Blue NAP Americas https://www.bluenapamericas.com/ ; PeeringDB OCIX https://www.peeringdb.com/fac/641 | Aruba, Curacao, Sint Maarten | Use official telecom/operator pages where possible; Caribbean directories are often necessary but lower grade. |

---

## 4. Province and special-municipality enumeration

Run every province as: **operator seed -> DDA/directories -> Dutch trade press -> official publication search -> local municipality/omgevingsdienst search**. Use Dutch province names in queries even when storing English division names.

| Division | Dutch/local query names | Major developers / places to pivot | Query templates |
|---|---|---|---|
| Drenthe | `Drenthe`, `Meppel`, `Hoogersmilde` | Kolo NL2 Meppel; Cellnex Hoogersmilde; smaller regional hosting. | `site:zoek.officielebekendmakingen.nl datacenter Drenthe`; `site:meppel.nl datacenter omgevingsvergunning`; `site:drenthe.nl datacenter`; `"Kolo" Meppel datacenter`; `"Hoogersmilde" Cellnex datacenter`. |
| Flevoland | `Flevoland`, `Dronten`, `Almere`, `Lelystad`, `Zeewolde`, `Flevokusthaven` | Kolo/Serverius Dronten; NorthC Almere; Cellnex Lelystad; Zeewolde Meta rejected lead; new Flevokusthaven application leads need verification. | `site:zoek.officielebekendmakingen.nl datacenter Flevoland`; `site:zoek.officielebekendmakingen.nl datacenter Flevokusthaven`; `site:lelystad.nl datacenter omgevingsvergunning`; `site:almere.nl datacenter NorthC`; `Zeewolde Meta datacenter Raad van State`; `site:open.overheid.nl Zeewolde hyperscale datacenter`. |
| Friesland | `Friesland`, `Fryslan`, `Leeuwarden`, `Tjerkgaast`, `Spannenburg` | Penta Infra LEE01/LEE02; Cellnex Tjerkgaast/Spannenburg; ViaData-style regional edge. | `site:zoek.officielebekendmakingen.nl datacenter Friesland OR Fryslan`; `site:leeuwarden.nl datacenter`; `"Penta Infra" Leeuwarden datacenter`; `"Tjerkgaast" datacenter Cellnex`; `"Spannenburg" datacenter`. |
| Gelderland | `Gelderland`, `Doetinchem`, `Ugchelen`, `Apeldoorn`, `Arnhem`, `Nijmegen` | InterDC Doetinchem; Cellnex Ugchelen; regional enterprise/public-sector sites. | `site:zoek.officielebekendmakingen.nl datacenter Gelderland`; `site:doetinchem.nl datacenter omgevingsvergunning`; `site:gelderland.nl datacenter`; `"InterDC" Doetinchem`; `"Ugchelen" Cellnex datacenter`; `"Arnhem" "rekencentrum"`. |
| Groningen | `Groningen`, `Eemshaven`, `Het Hogeland`, `Delfzijl`, `Oldambt`, `Oostpolder`, `Westpoort Groningen` | Google Eemshaven; Google/Oldambt leads; NorthC Groningen 1/2; QTS Groningen; Eemshaven hyperscale exception zone. | `site:zoek.officielebekendmakingen.nl datacenter Groningen Eemshaven`; `site:hethogeland.nl datacenter Eemshaven`; `site:provinciegroningen.nl datacenter`; `site:omgevingsdienstgroningen.nl datacenter`; `"Google" Oldambt datacenter vergunning`; `"QTS" Groningen datacenter`; `"NorthC" Groningen Westpoort`. |
| Limburg | `Limburg`, `Geleen`, `Chemelot`, `Venlo`, `Sittard`, `Ittervoort`, `Leudal` | Penta Infra GLN01 Geleen/Chemelot; Systemec Venlo; Cellnex Ittervoort; Dustin/Unilogic Sittard leads. | `site:zoek.officielebekendmakingen.nl datacenter Limburg`; `site:chemelot.nl datacenter`; `site:geleen.nl datacenter`; `site:venlo.nl datacenter Systemec`; `"Penta Infra" Geleen datacenter`; `"Ittervoort" Cellnex datacenter`. |
| North Brabant | `Noord-Brabant`, `Eindhoven`, `Roosendaal`, `Steenbergen`, `Rijen`, `'s-Hertogenbosch`, `Breda`, `Tilburg` | NorthC Eindhoven 1/2; Colt DCS Rotterdam/Roosendaal; Eurofiber/Nedzone Steenbergen; Previder Rijen; Interconnect. | `site:zoek.officielebekendmakingen.nl datacenter "Noord-Brabant"`; `site:eindhoven.nl datacenter omgevingsvergunning`; `site:roosendaal.nl datacenter Colt`; `site:steenbergen.nl datacenter Nedzone Eurofiber`; `site:gilzerijen.nl datacenter Previder`; `"Koolhovenlaan 142" datacenter`; `"Colt" Roosendaal "15MW"`. |
| North Holland | `Noord-Holland`, `Amsterdam`, `Haarlemmermeer`, `Schiphol`, `Aalsmeer`, `Oude Meer`, `Halfweg`, `Haarlem`, `Middenmeer`, `Hollands Kroon`, `Agriport`, `Diemen`, `De Kwakel`, `Westpoort`, `Plimsollweg`, `Linieweg` | Digital Realty; Equinix; Global Switch; Iron Mountain; CyrusOne; NorthC; Switch; Microsoft Middenmeer/Amsterdam; Google Middenmeer; hyperscale exception in Hollands Kroon. | `site:zoek.officielebekendmakingen.nl datacenter "Noord-Holland"`; `site:zoek.officielebekendmakingen.nl datacenter Amsterdam Plimsollweg`; `site:zoek.officielebekendmakingen.nl datacenter Halfweg Linieweg CyrusOne`; `site:lokaleregelgeving.overheid.nl datacenters Haarlemmermeer`; `site:haarlemmermeer.nl datacenter ontwikkelruimte`; `site:amsterdam.nl datacenter vestigingsbeleid`; `site:hollandskroon.nl datacenter Microsoft Google`; `"J.W. Lucasweg 35" datacenter Haarlem`; `"De Kwakel" datacenter "Noord-Holland"`. |
| Overijssel | `Overijssel`, `Enschede`, `Hengelo`, `Zwolle` | Equinix EN1 Enschede; Equinix ZW1 Zwolle; Previder Hengelo; InterDC Enschede/Hengelo. | `site:zoek.officielebekendmakingen.nl datacenter Overijssel`; `site:enschede.nl datacenter Equinix`; `site:hengelo.nl datacenter Previder InterDC`; `site:zwolle.nl datacenter Equinix`; `"Auke Vleerstraat" datacenter`; `"Expolaan 50" datacenter`. |
| Utrecht | `Utrecht`, `Nieuwegein`, `Groenekan`, `De Bilt`, `Amersfoort` | NorthC Nieuwegein; Eurofiber Utrecht 1 Groenekan; BT Nieuwegein; regional government/health IT. | `site:zoek.officielebekendmakingen.nl datacenter Utrecht Nieuwegein`; `site:nieuwegein.nl datacenter`; `site:debilt.nl datacenter Groenekan`; `"Koningin Wilhelminaweg 471" datacenter`; `"BT" Nieuwegein datacenter`; `"NorthC" Nieuwegein datacenter`. |
| Zeeland | `Zeeland`, `Goes`, `Middelburg`, `Vlissingen`, `Terneuzen` | Cellnex Goes; small Zeeland/Goes operators from directories; port/industrial edge leads. | `site:zoek.officielebekendmakingen.nl datacenter Zeeland`; `site:goes.nl datacenter Cellnex`; `site:zeeland.nl datacenter`; `site:vlissingen.nl datacenter`; `"Goes" datacenter Cellnex`; `site:datacentermap.com/the-netherlands/goes datacenter`. |
| South Holland | `Zuid-Holland`, `Rotterdam`, `Delft`, `Waalhaven`, `Zestienhoven`, `Alphen aan den Rijn`, `Den Haag`, `Leiden`, `Dordrecht` | NorthC Rotterdam Zestienhoven/Waalhaven/Delft; Smartdc Rotterdam; Eurofiber Rotterdam 1; new Alphen aan den Rijn notice; port/IXP ecosystem. | `site:zoek.officielebekendmakingen.nl datacenter "Zuid-Holland"`; `site:zoek.officielebekendmakingen.nl datacenter "Alphen aan den Rijn"`; `site:rotterdam.nl datacenter omgevingsvergunning`; `site:delft.nl datacenter NorthC`; `site:alphenaandenrijn.nl datacenter Boerhaaveweg`; `"Boerhaaveweg 10" datacenter`; `"Smartdc" Rotterdam datacenter`; `"NorthC" Zestienhoven datacenter`. |
| Aruba | `Aruba`, `Oranjestad`, `SETAR` | SETAR Colocation Datacenter; telecom/government DR leads. | `site:setar.aw datacenter colocation`; `site:overheid.aw datacenter`; `site:aruba.com datacenter`; `"SETAR" "Data Center Services"`; `"Aruba" "colocation datacenter"`. |
| Bonaire | `Bonaire`, `Kralendijk`, `Caribisch Nederland` | Government datacenter recommendation/modernized government facility; telecom/server-room leads. | `"Bonaire" "government data center"`; `"Caribisch Nederland" datacenter Bonaire`; `site:rijksdienstcn.com datacenter`; `site:bonairegov.com datacenter`; `"Bonaire" "rekencentrum"`. |
| Saba | `Saba`, `The Bottom`, `Caribisch Nederland` | Candidate secondary government datacenter in resilience reports; likely small server rooms unless official procurement appears. | `"Saba" "government data center"`; `"Caribisch Nederland" datacenter Saba`; `site:sabagov.com datacenter`; `site:rijksdienstcn.com Saba datacenter`; `"Saba" "server room" government`. |
| Sint Eustatius | `Sint Eustatius`, `Statia`, `Oranjestad`, `Caribisch Nederland` | Candidate secondary government datacenter; small government/telecom rooms. | `"Sint Eustatius" datacenter`; `"Statia" "government data center"`; `site:statiagovernment.com datacenter`; `site:rijksdienstcn.com "Sint Eustatius" datacenter`; `"Statia" "server room"`. |
| Curacao | `Curacao`, `Willemstad`, `Blue NAP`, `DataPlanet`, `CORE`, `E-Commerce Park` | Blue NAP Americas/DataPlanet; CORE; E-Commerce Park; AMS-IX Caribbean PoP. | `site:bluenapamericas.com datacenter Curacao`; `site:ams-ix.net Curacao "data centre"`; `"Blue NAP Americas" Willemstad`; `"CORE Datacenter" Curacao`; `"E-Commerce Park" Curacao datacenter`; `site:datacentermap.com/curacao Willemstad datacenter`. |
| Sint Maarten | `Sint Maarten`, `St Maarten`, `Philipsburg`, `OCIX`, `Habour View`, `Harbour View` | OCIX / Open Caribbean Internet Exchange facility; SD Datacenter/PeeringDB leads. | `"OCIX" "Sint Maarten" datacenter`; `site:peeringdb.com/fac Sint Maarten OCIX`; `"3 Habour View" Philipsburg datacenter`; `"Open Caribbean Internet Exchange" Sint Maarten`; `site:sintmaartengov.org datacenter`. |

---

## 5. Hyperscaler/cloud region handling

Cloud region pages are **A for logical region existence**, not for exact facility addresses. Dutch hyperscaler physical sites are often owned campuses in Eemshaven/Middenmeer or leased/partner campuses near Amsterdam/Schiphol; never infer a facility record only from an Azure/AWS/GCP/OCI logical region.

| Provider | Netherlands signal | URL | Grade |
|---|---|---|---|
| Microsoft Azure | Netherlands geography/West Europe region; Microsoft-operated datacenter in Middenmeer; multiple North Holland permit/press leads | https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies ; https://local.microsoft.com/communities/emea/north-holland/ | A region/site, C facility mapping for leased sites |
| Google | Official data centers at Eemshaven and Middenmeer; Google Cloud Netherlands region should be checked via current GCP locations page | https://datacenters.google/locations/eemshaven-netherlands-var ; https://datacenters.google/locations/middenmeer-netherlands ; https://cloud.google.com/about/locations | A |
| AWS | No public AWS owned Dutch region comparable to Frankfurt/Paris; may appear as edge/CloudFront/partner colo leads | https://aws.amazon.com/about-aws/global-infrastructure/ | A for official region/edge statements only |
| Oracle Cloud | Check OCI public regions/current docs for Netherlands-related region/edge claims; do not infer Amsterdam facility without operator evidence | https://www.oracle.com/cloud/public-cloud-regions/ | A for official region only |
| Local/cloud providers | Leaseweb, Eurofiber, Previder, Interconnect, KPN/NorthC legacy, Smartdc, DCspine ecosystem | Operator/DDA pages | A/B depending on source |

---

## 6. Fast validation checklist for each candidate

1. **Normalize province/municipality**: store English division from manifest, but search Dutch names and municipalities.
2. **Confirm operator existence**: official operator page, DDA participant page, or telecom/government page for Caribbean sites.
3. **Confirm address/status**: Officiele Bekendmakingen notice, municipal page, DDA page, PeeringDB facility, or operator spec sheet.
4. **Classify lifecycle**: application, draft permit, permit granted, construction, operational, rejected/canceled.
5. **Capacity discipline**: prefer operator MW/kW/MVA; convert kVA/MVA only when clearly electrical capacity and note apparent-power caveat. Directory-only MW remains C.
6. **Policy filter**: if over 10 ha / 70 MW, check hyperscale restrictions, exceptions, and whether application predates relevant cutoff.
7. **Avoid double-counting**: Amsterdam-branded facilities may sit in Haarlem, Haarlemmermeer, Aalsmeer, Oude Meer, Halfweg, or Diemen; Rotterdam-branded Colt is in Roosendaal, North Brabant.
