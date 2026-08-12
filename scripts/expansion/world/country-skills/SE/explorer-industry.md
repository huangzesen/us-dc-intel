# SE Explorer — Industry/Vendor Enumeration for Swedish Datacenter Projects

Date: 2026-08-12. Scope: Sweden datacenter enumeration from industry, vendor, cloud-region, trade-press, association, and county-level query patterns. Reliability grades: **A** = official/primary (operator/cloud official pages, municipality planning/building-permit records, county administrative board/environment decisions, grid authority records), **B** = strong secondary (DCD, Baxtel, Datacenter Forum, SVT/local newspapers when they cite municipal files), **C** = weak/aggregate (market-report blurbs, generic directory pages, social posts).

---

## 0. Structural facts for Sweden

- Sweden has no single national public datacenter registry. Facility discovery works by joining **operator official portfolios**, **hyperscale cloud-region disclosures**, **municipal planning/building-permit files**, **county-level environmental/permitting records**, and **local/trade press**.
- Planning/building evidence is highly local. Under Sweden's Planning and Building Act system, **municipalities** publish detailed plans (`detaljplan`), consultations (`samråd`), reviews (`granskning`), building permits (`bygglov`), start notices (`startbesked`), meeting agendas/minutes, and project pages. Boverket's English planning guide confirms detailed-plan proposals are normally announced by the municipality and local newspaper: https://www.boverket.se/en/start/laws-and-regulations/planning-process2/detailed-planning-process/
- County administrative boards (`Länsstyrelsen`) matter for larger environmental/energy issues. Their "miljöfarlig verksamhet" pages explain that larger environmentally hazardous activities are handled by the county and decided by the Environmental Licensing Delegation (`Miljöprövningsdelegationen`): https://www.lansstyrelsen.se/stockholm/miljo-och-vatten/miljofarlig-verksamhet.html
- For large campuses, the strongest early signals are often **land sale/detailed-plan work**, **grid connection or substation planning**, and **backup generator/environmental cases**, not a datacenter-specific national permit.
- Swedish vocabulary is essential. Search all of: `datacenter`, `data center`, `datahall`, `datahallar`, `serverhall`, `serverhallar`, `datorhall`, `datorhallar`, `colocation`, `samlokalisering`, `molnregion`, `AI-kluster`, `HPC`, `högpresterande beräkning`, `elintensiv verksamhet`, `spillvärme`, `överskottsvärme`.

---

## 1. Core search patterns

### 1.1 English + Swedish discovery queries

Use Google/Bing for broad discovery; use Swedish exact terms for municipal/local results.

```text
"{kommun}" ("datacenter" OR "datahall" OR "serverhall" OR "datorhall")
"{kommun}" ("elintensiv verksamhet" OR "större industri") ("detaljplan" OR "samråd" OR "granskning")
"{kommun}" ("datahall" OR "serverhall") ("bygglov" OR "startbesked" OR "slutbesked" OR "VA-anmälan")
"{kommun}" ("datacenter" OR "datahall") ("ställverk" OR "nätanslutning" OR "fördelningsstation" OR "reservkraft")
"{operator}" "{kommun}" ("datacenter" OR "datahall" OR "campus" OR "MW" OR "megawatt")
site:{kommun-domain} ("datacenter" OR "datahall" OR "serverhall" OR "elintensiv")
site:lansstyrelsen.se "{county-or-city}" ("datahall" OR "serverhall" OR "datacenter" OR "reservkraft")
site:ei.se ("datahall" OR "datacenter" OR "serverhall" OR "nätkoncession")
site:svk.se ("datahall" OR "datacenter" OR "serverhall" OR "elintensiv")
```

### 1.2 Status/capacity extraction queries

```text
"{project}" ("MW" OR "megawatt" OR "MW el" OR "effekt" OR "anslutningseffekt")
"{project}" ("kvm" OR "m2" OR "hektar" OR "ha" OR "byggnad" OR "datahall")
"{project}" ("byggstart" OR "pågående markarbeten" OR "sprängningsarbeten" OR "öppnar" OR "i drift")
"{operator}" ("PUE" OR "rack" OR "kW per rack" OR "liquid cooling" OR "vätskekylning")
```

### 1.3 Municipal document terms

When a municipality has a meeting-document portal, search agenda PDFs and case text for:

```text
datacenter / data center
datahall / datahallar
serverhall / serverhallar
datorhall / datorhallar
elintensiv verksamhet
detaljplan
planbesked
samrådsredogörelse
granskningsutlåtande
bygglov
startbesked
markanvisning
markförsäljning
reservkraft
dieselaggregat
ställverk
fördelningsstation
spillvärme / överskottsvärme
```

---

## 2. Grade A/B source map

### 2.1 Industry association and national investment sources

- **Swedish Datacenter Industry Association / SweDCI** — association-level member universe and policy context; use to seed Swedish-entity operators/suppliers, then verify facilities elsewhere. Grade **B+** for sector universe, not facility inventory. https://www.sdia.se/
- **Business Sweden** — government/industry-backed investment promotion; useful for site-finder leads and national positioning, not enough for facility status. Grade **B** for market/site leads. https://www.business-sweden.com/industries/digital-technologies/ and https://www.business-sweden.com/invest-in-sweden/online-tools/site-finder/
- **Boverket** — official planning/building process reference; use to understand why municipal `detaljplan`/`bygglov` records are primary evidence. Grade **A** for process. https://www.boverket.se/en/start/laws-and-regulations/planning-process2/
- **Lantmäteriet / Geodataportalen** — official geodata and property/context layers; useful for parcel/county/municipality boundaries and site coordinates after a municipal record identifies a property. Grade **A** for geodata. https://www.lantmateriet.se/en/geodata/ and https://www.geodata.se/geodataportalen/

### 2.2 Operator official pages to seed facilities

Treat official operator pages as **A- for existence/location** and **B for marketed design capacity** unless they provide concrete live/opening evidence.

| Operator | Official source | Swedish enumeration notes |
|---|---|---|
| Tele2 | https://www.tele2.se/foretag/molntjanster/datacenter | Swedish carrier colo. Says Tele2 provides colocation in its datacenters; exact facility list may be less public, so pivot from Tele2 plus `datahall`, `colocation`, `Stockholm`, `Göteborg`, `Malmö`, `Kista`. |
| Bahnhof | https://bahnhof.se/foretag/colocation/ and https://bahnhof.se/foretag/colocation/our-data-centers/ | Explicitly lists Swedish facilities: Pionen, Thule, S:t Erik, Gullan/Kista, Sparven/Malmö, and upcoming Bahnhof Bunker/Göteborg. Facility pages can include address, MW/UPS/generator details, e.g. Pionen: https://bahnhof.se/foretag/colocation/datacenter/pionen/ |
| atNorth | https://www.atnorth.com/nordic-data-centers/sweden-data-centers/ | Stockholm SWE01/SWE02 and Sollefteå SWE04. SWE01 is in Kista; SWE02 in Akalla is scheduled Q4 2027; SWE04 Sollefteå is a planned 300 MW mega site. Key pages: https://www.atnorth.com/nordic-data-centers/sweden-data-centers/stockholm-metro-site/ , https://www.atnorth.com/nordic-data-centers/sweden-data-centers/stockholm-swe02/ , https://www.atnorth.com/nordic-data-centers/sweden-data-centers/solleftea-swe04/ |
| Conapto | https://www.conapto.com/ | Stockholm-focused colo. Official release says Stockholm 4 South opened in 2024 and combined Stockholm South campus has 5,200 m2 computer rooms / 24 MW: https://www.conapto.com/conapto-opens-stockholm-4-south-a-new-sustainable-data-center/ |
| Digital Realty / Interxion | https://www.digitalrealty.com/data-centers/emea/stockholm | Lists six Stockholm/Kista-Akalla facilities (STO1-STO6), total 25k m2 colocation, 115+ cloud/network providers. Strong official seed for Kista/Akalla. |
| EcoDataCenter | https://ecodatacenter.tech/data-center | Falun and Borlänge/Dalarna AI/HPC campuses. Falun EDC1 official page states 80 MW available power: https://ecodatacenter.tech/data-center/ecodatacenter-1 . Borlänge EDC2 page states up to 600 MW, construction start 2025: https://ecodatacenter.tech/data-center/ecodatacenter2 |
| Kolo DC | https://kolodc.com/ and https://kolodc.com/data-centers | CapMan-backed Nordic colo platform with Swedish sites; created from acquired EcoDataCenter edge facilities. Use official pages for current branding and DCD/Baxtel for transaction history. |
| GleSYS | https://glesys.com/locations/our-data-centers/stockholm/ | Stockholm/Västberga facility; also check Falkenberg/other Swedish locations via GleSYS official site. |
| Equinix | https://www.equinix.com/data-centers/europe-colocation/sweden-colocation | Officially states three Swedish data centers; useful for Stockholm interconnection inventory. |
| Tietoevry | Search official site + local directories | Large Nordic IT services operator; can be relevant as colocation/cloud infrastructure, but public facility details vary. Verify with official pages and PeeringDB/DataCenterMap. |
| Telia/Cygate, Telenor/GlobalConnect, Arelion | Search official pages | Network-carrier datacenter/colo may appear under enterprise IT, security, or edge pages; treat as operator seeds, then verify facility-level evidence. |

### 2.3 Hyperscale/cloud official pages

Cloud pages are **A for region existence and public city/country geography**, but they rarely reveal exact buildings. Use them as anchor points for municipal and operator pivots.

| Cloud/platform | Official source | Swedish inference use |
|---|---|---|
| AWS | AWS Europe (Stockholm), `eu-north-1`, opened with 3 AZs: https://aws.amazon.com/blogs/aws/now-open-aws-europe-stockholm-region/ ; current AWS region table: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | Search Stockholm-region municipalities and AWS SPVs/contractors. Municipal records can reveal building permits/VA/environment details; example Swedish municipal PDFs mention AWS datahall works. |
| Microsoft Azure/M365 | Microsoft says it operates datacenters in **Gävle, Sandviken, and Staffanstorp**: https://local.microsoft.com/communities/emea/sweden/ . Launch release: https://news.microsoft.com/europe/2021/11/16/microsoft-opens-its-sustainable-datacenter-region-in-sweden-creating-new-opportunities-for-a-cloud-first-sweden/ | Primary county targets: Gävleborg and Scania. Search municipal permit files for `Microsoft`, `datorhall`, `datahall`, `reservkraft`, `Ersbo`, `Stackbo`, `Staffanstorp`. |
| Google Cloud | Stockholm `europe-north2`, launched 2025: https://cloud.google.com/blog/products/infrastructure/google-cloud-launches-42nd-cloud-region-in-sweden ; zones listed in docs: https://docs.cloud.google.com/compute/docs/regions-zones | Also search Dalarna/Avesta/Horndal because Google has long-held land there; do not infer operational status without municipal or Google evidence. |
| Oracle Cloud | Oracle public-region table lists **Sweden Central (Stockholm)** live: https://www.oracle.com/cloud/public-cloud-regions/ | Use as Stockholm-region cloud anchor; exact sites are not public. |
| Meta | Meta official locations list has **Luleå** with 8.7B+ SEK investment and operational/job facts: https://datacenters.atmeta.com/all-locations/ ; Luleå go-live post: https://datacenters.atmeta.com/2013/06/lulea-goes-live/ | Primary Norrbotten seed; search Luleå municipality planning/building records for expansion phases and backup/power details. |
| CoreWeave | https://www.coreweave.com/ai-data-centers and EcoDataCenter press | CoreWeave is a workload/customer clue in Falun/Dalarna via EcoDataCenter; verify through EcoDataCenter official releases and local permits. |

---

## 3. Trade press and secondary sources

- **Data Center Dynamics (DCD)** — strongest free trade press for Swedish campus announcements, land acquisitions, Microsoft/Vantage/EcoDataCenter/atNorth updates. Grade **B**; capacity may repeat vendor claims. https://www.datacenterdynamics.com/
- **Baxtel** — practical facility-level aggregator with addresses/news links. Grade **B-/C+**; use as lead generator, then verify with official/municipal sources. https://baxtel.com/
- **DataCenterMap / DataCenters.com / OCOLO** — useful for colo inventory and addresses, especially Stockholm. Grade **C+** unless source links are provided. https://www.datacentermap.com/sweden/ and https://www.ocolo.io/data-centers/sweden/
- **Datacenter Forum / DataCentre Magazine / Data Centre Dynamics / DCNN** — good for industry announcements in Nordics. Grade **B** for dated news; re-check operator official pages.
- **SVT Nyheter and local newspapers** (`GD`, `Arbetarbladet`, `Nya Tierps-Posten`, `Dagens Nyheter`, regional papers) — often break municipal planning/building-permit cases. Grade **B** if the article cites council/committee files; use it to find the underlying municipal docket.
- **TED EU / Swedish procurement portals** — useful for public-sector datacenter/IT infrastructure tenders, but many are enterprise IT refreshes rather than new facilities. TED is official for notices: https://ted.europa.eu/en/ . Search `datacenter`, `datahall`, `driftmiljö`, `serverhall`, CPV 452/453/725 terms plus place `SE`.

---

## 4. County-by-county enumeration approach

For every county, run three passes:

1. **Operator/cloud seed pass**: known operators + county municipalities.
2. **Municipal planning pass**: municipality domains and meeting portals for `detaljplan`, `planbesked`, `bygglov`, `datahall`, `elintensiv`.
3. **Power/environment pass**: `lansstyrelsen.se`, local grid companies, `ei.se`, `svk.se`, and district-heating utilities for `reservkraft`, `ställverk`, `nätanslutning`, `spillvärme`.

| Manifest county | Swedish county name | Priority and query notes |
|---|---|---|
| Stockholm | Stockholms län | Highest density. Operators: Digital Realty/Interxion Kista-Akalla, atNorth SWE01/SWE02, Conapto Stockholm South, Bahnhof, Tele2, Equinix, GleSYS, Oracle/Google/AWS region anchors. Query municipalities: Stockholm, Solna, Sollentuna, Järfälla, Upplands Väsby, Sigtuna, Botkyrka, Huddinge. Use `site:stockholm.se datahall`, `site:vaxer.stockholm serverhall`, `Akalla 4:8`, `Kista`, `Brista`, `Stockholm Data Parks`. Official example: Stockholm city project page for Akalla server halls / atNorth: https://vaxer.stockholm/projekt/akalla/serverhallar-med-atervinning-av-overskottsvarme/ |
| Vasterbotten | Västerbottens län | Lower known colo density but strong power/cold-climate candidate area. Query Umeå, Skellefteå, Lycksele for `elintensiv verksamhet`, `datahall`, `serverhall`, `industripark`, `ställverk`. Treat green-industry power competition as context, not facility proof. |
| Norrbotten | Norrbottens län | Meta Luleå is the anchor; also Node Pole/Boden/Luleå industrial sites and mining/HPC facilities. Query `Luleå datacenter bygglov`, `Porsön datahall detaljplan`, `Boden datacenter`, `serverhall reservkraft`. Verify with Meta official pages and Luleå municipal plans. RISE Luleå testbed can be a research/edge lead: https://www.ri.se/en/data-center-testbed-for-the-whole-world-in-lulea |
| Uppsala | Uppsala län | Watch Tierp/Mehedeby and Stockholm-north land deals. Search `Tierp Mehedeby datacenter`, `Vantage datacenter Tierp`, `Dragon Gate datahall`, `detaljplan Mehedeby datacenter`. Local press reported a major Mehedeby project; use that only as a lead until Tierp municipal planning/building files appear. |
| Sodermanland | Södermanlands län | Stockholm-adjacent overflow. Query Eskilstuna, Strängnäs, Nyköping, Katrineholm for `datahall`, `elintensiv`, `logistik`, `ställverk`. AWS-related municipal snippets have appeared in Katrineholm building committee documents; search PDFs for `AWS` and `datahall`. |
| Ostergotland | Östergötlands län | Query Linköping/Norrköping/Mjölby/Motala, local energy companies, and university/SAAB-tech ecosystem. Use `serverhall`, `datorhall`, `reservkraft`, `fjärrvärme`. |
| Jonkoping | Jönköpings län | Query Jönköping/Nässjö/Värnamo plus logistics/power corridors. Länsstyrelsen electrification documents discuss large loads generally; facility proof still needs municipality/operator records. |
| Kronoberg | Kronobergs län | Query Växjö/Alvesta/Ljungby for `datahall`, `serverhall`, `fjärrvärme`, `elintensiv`. Expect few large public leads; use local planning portals. |
| Kalmar | Kalmar län | Query Kalmar/Oskarshamn/Västervik/Nybro; add `kraft`, `industrimark`, `reservkraft`. Watch coastal/industrial power sites. |
| Gotland | Gotlands län | Low probability for hyperscale due island grid constraints. Query `Region Gotland datahall`, `serverhall`, `fiber`, `reservkraft`; count only firm municipal/operator evidence. |
| Blekinge | Blekinge län | Query Karlskrona/Karlshamn/Ronneby. Add `NKT`, `fiber`, `undervattenskabel`, `serverhall`, `datacenter`. |
| Scania | Skåne län | Microsoft Staffanstorp is the anchor; also Malmö/Lund/Helsingborg carrier colo. Search `Staffanstorp Microsoft datorhall`, `reservkraft`, `70MW`, `Malmö colocation`, `Bahnhof Sparven`. Microsoft official page confirms Staffanstorp. Länsstyrelsen Skåne electrification material notes datacenter loads can affect local grid: https://www.lansstyrelsen.se/download/18.5e789f8a19e49fa9dce8d9e/1779431950628/Handlingsplan%20f%C3%B6r%20elektrifiering%20i%20Sk%C3%A5ne.pdf |
| Halland | Hallands län | GleSYS/Falkenberg is an operator lead; query Falkenberg/Halmstad/Kungsbacka/Varberg for `GleSYS`, `datahall`, `serverhall`, `colocation`, `spillvärme`. |
| Vastra Gotaland | Västra Götalands län | Gothenburg/Borås/Trollhättan/Skövde/Alingsås. Bahnhof has upcoming Göteborg Bunker; carrier colo likely around Gothenburg. Search `Göteborg datacenter bygglov`, `Bahnhof Bunker`, `datahall Göteborg`, `serverhall fjärrvärme`, `GlobalConnect`, `Tele2 datacenter`. |
| Varmland | Värmlands län | Query Karlstad/Grums/Arvika/Kristinehamn for `datahall`, `serverhall`, `elintensiv`, `industrimark`. Expect local government/energy-company leads before operator announcements. |
| Orebro | Örebro län | Query Örebro/Kumla/Hallsberg for logistics/power corridor `datahall`, `elintensiv`, `detaljplan`, `ställverk`. |
| Vastmanland | Västmanlands län | Query Västerås/Köping/Fagersta/Arboga. Search with `ABB`, `elintensiv`, `serverhall`, `datahall`, `nätanslutning`. |
| Dalarna | Dalarnas län | EcoDataCenter Falun and Borlänge are anchors; Google land/Horndal/Avesta is a planning-watch item. Search `EcoDataCenter Falun bygglov`, `Borlänge Kvarnsveden datacenter`, `CoreWeave Falun`, `Horndal Google datacenter`, `Avesta bygglov datacenter`. Official EcoDataCenter pages are strong seeds. |
| Gavleborg | Gävleborgs län | Microsoft Gävle/Sandviken and Ockelbo/Lingbo planning are anchors. Search `Gävle Microsoft datahall bygglov`, `Sandviken datahall VA-anmälan`, `Stackbo`, `Ersbo`, `Ockelbo Valhalla industriområde datacenter`. Ockelbo official detailed-plan article: https://ockelbo.se/nyheter/nyheter/2025-02-24-detaljplan-for-valhalla-industriomrade-ute-pa-samrad |
| Western Northland | Västernorrlands län | atNorth Sollefteå SWE04 is the anchor. Search `Sollefteå Hamre Industripark datacenter`, `Långsele datahall`, `SWE04`, `300MW`, `detaljplan Hamre`. Official atNorth page/release provides planned capacity and timing. Also monitor Länsstyrelsen Västernorrland "aktuella större etableringar": https://www.lansstyrelsen.se/vasternorrland/miljo-och-vatten/miljofarlig-verksamhet/aktuella-storre-etableringar-i-lanet.html |
| Jamtland | Jämtlands län | Östersund/Verksmon project has had contested planning. Search `Östersund Verksmon datacenter`, `serverhallar Verksmon`, `miljötillstånd`, `detaljplan`, `Jämtkraft`. SVT is a useful lead but confirm with Östersund municipal records: https://www.svt.se/nyheter/lokalt/jamtland/tjanstemannen-sager-nej-till-detaljplan-for-datacenter-i-ostersund |

---

## 5. Verification rules and source grading

### 5.1 Evidence hierarchy

1. **A — official project/legal evidence**: municipality detailed-plan/building-permit files, county environmental decisions, operator official facility pages, hyperscaler official region/location pages, official geodata/property records, official TED/procurement notices where the subject is facility construction/operation.
2. **A- — operator marketing pages**: good for facility existence, city, services, and designed capacity; weaker for built/live capacity unless the page states opened/in operation.
3. **B — trade/local press with named municipality/operator facts**: DCD, Baxtel news, SVT, established local newspapers. Use as a lead and cite if official docs are not public.
4. **C — generic directories/market reports/social posts**: use only to discover names/locations; do not count capacity or status without stronger evidence.

### 5.2 Status mapping

- `markförvärv`, `markanvisning`, `planbesked`, `samråd`, `granskning` = planned/proposed.
- `antagen detaljplan`, `lagakraftvunnen detaljplan` = zoning/planning approved, still not built.
- `bygglov`, `startbesked`, `pågående markarbeten`, `sprängningsarbeten` = construction-enabling or under construction.
- `öppnar`, `i drift`, `go live`, `opened`, `operational`, `slutbesked` = operational/open; still separate shell completion from actual IT load where possible.
- Capacity terms: distinguish `site power`, `available power`, `IT capacity`, `anslutningseffekt`, `reservkraft`, and long-term `potential to scale`. Swedish press often reports total campus power even when only phase 1 is under construction.

### 5.3 Common pitfalls

- Do not double count Stockholm Kista/Akalla facilities across Interxion/Digital Realty legacy names, Stockholm Data Parks, operator brands, and individual STO/SWE labels.
- Do not treat cloud region city names as exact campus addresses. AWS/Google/Oracle publish Stockholm region names; municipal/operator evidence is needed for physical sites.
- Do not count `elintensiv verksamhet` as a datacenter unless the same document/article says `datacenter`, `datahall`, `serverhall`, or identifies a known operator/hyperscaler.
- Swedish local news may identify a project before the municipality publishes searchable documents; revisit the municipality portal after council meetings.
- Backup-generator permits and VA/stormwater records can reveal true building counts and MW, but the applicant name may be a construction/SPV name rather than the cloud brand.

---

## 6. Recommended Swedish enumeration pipeline

1. **Seed known operators and cloud regions** from §2.2 and §2.3; create initial records for Stockholm, Gävleborg, Skåne, Norrbotten, Dalarna, Västernorrland, Uppsala.
2. **For every manifest county**, list municipalities and run the query bundle in §1.1 against municipal domains plus `lansstyrelsen.se`.
3. **For every hit**, capture the strongest project lifecycle document: official facility page, detailed plan, building permit, environmental decision, grid/substation record, or dated opening release.
4. **Cross-check capacity** against at least one independent source: operator page + municipal doc, or trade press + official planning/building/environment record.
5. **Normalize aliases**: operator ultimate parent, Swedish SPV/applicant name, campus name, facility code (SWE01/STO6/etc.), municipality, county.
6. **Grade per data point**. Example: atNorth SWE04 existence/planned 300 MW from official atNorth = A-/B; operational timing H1 2028 from same release = B until municipal/construction evidence confirms progress.

---

## 7. High-value source URLs captured

- SweDCI: https://www.sdia.se/
- Boverket planning process: https://www.boverket.se/en/start/laws-and-regulations/planning-process2/
- Länsstyrelsen environmental permitting example: https://www.lansstyrelsen.se/stockholm/miljo-och-vatten/miljofarlig-verksamhet.html
- Business Sweden digital technologies/site finder: https://www.business-sweden.com/industries/digital-technologies/ and https://www.business-sweden.com/invest-in-sweden/online-tools/site-finder/
- Tele2 datacenter: https://www.tele2.se/foretag/molntjanster/datacenter
- Bahnhof colocation/facilities: https://bahnhof.se/foretag/colocation/ and https://bahnhof.se/foretag/colocation/our-data-centers/
- atNorth Sweden: https://www.atnorth.com/nordic-data-centers/sweden-data-centers/
- Conapto: https://www.conapto.com/
- Digital Realty Stockholm: https://www.digitalrealty.com/data-centers/emea/stockholm
- EcoDataCenter: https://ecodatacenter.tech/data-center
- Kolo DC: https://kolodc.com/data-centers
- AWS Stockholm: https://aws.amazon.com/blogs/aws/now-open-aws-europe-stockholm-region/
- Microsoft Sweden datacenters: https://local.microsoft.com/communities/emea/sweden/
- Google Cloud Stockholm: https://cloud.google.com/blog/products/infrastructure/google-cloud-launches-42nd-cloud-region-in-sweden
- Oracle cloud regions: https://www.oracle.com/cloud/public-cloud-regions/
- Meta Luleå: https://datacenters.atmeta.com/all-locations/ and https://datacenters.atmeta.com/2013/06/lulea-goes-live/
- Stockholm Akalla/Stockholm Data Parks project: https://vaxer.stockholm/projekt/akalla/serverhallar-med-atervinning-av-overskottsvarme/
- Ockelbo Valhalla plan lead: https://ockelbo.se/nyheter/nyheter/2025-02-24-detaljplan-for-valhalla-industriomrade-ute-pa-samrad
- TED official procurement portal: https://ted.europa.eu/en/
