# SE Explorer Official - Sweden Datacenter Enumeration via Planning, Environmental Permits, Grid, Cloud, Colo, and PTS Sources

Date: 2026-08-12. Scope: Sweden (SE), repo divisions are counties: Stockholm, Vasterbotten, Norrbotten, Uppsala, Sodermanland, Ostergotland, Jonkoping, Kronoberg, Kalmar, Gotland, Blekinge, Scania, Halland, Vastra Gotaland, Varmland, Orebro, Vastmanland, Dalarna, Gavleborg, Western Northland, Jamtland. Note: repo spellings are ASCII/English; map them to Swedish names for searching: `Vasterbotten = Västerbotten`, `Sodermanland = Södermanland`, `Ostergotland = Östergötland`, `Jonkoping = Jönköping`, `Scania = Skåne`, `Vastra Gotaland = Västra Götaland`, `Varmland = Värmland`, `Orebro = Örebro`, `Vastmanland = Västmanland`, `Gavleborg = Gävleborg`, `Western Northland = Västernorrland`, `Jamtland = Jämtland`.

Angle: **official/regulatory/cloud pipeline** for enumerating Swedish datacenter facilities and projects. Reliability grades: **A** = official/primary source (municipal planning/building record, county board environmental permit, court decision, regulator, grid operator, operator official page, official cloud region page); **B** = strong secondary/trade/association source with named project/operator/location; **C** = weak aggregate, scraped directory, social media, or unverified marketing.

---

## 0. Sweden-specific structural facts

- Sweden has **no complete national public datacenter facility register**. Enumeration is a join across municipal planning/building files (`detaljplan`, `bygglov`, `marklov`, `startbesked`, `slutbesked`), environmental permitting under `miljöbalken`, Svenska kraftnät grid/connection context, cloud-region official pages, operator site pages, and trade press.
- Swedish municipalities control land-use planning and building permits under the Planning and Building Act (`Plan- och bygglagen`, PBL). Boverket is the national planning/building guidance authority, but actual datacenter project files usually sit in **municipal plan/building portals** or municipal PDF archives.
- Use **Lantmäteriet's detailed-plan service / Nationella geodataplattformen (NGP)** as a plan-discovery layer, not as a full permit register. Lantmäteriet states the service shows selected information from adopted detailed plans uploaded to NGP: https://www.lantmateriet.se/sv/kartor/vara-karttjanster/detaljplaner/.
- Large datacenters often produce strong environmental evidence because reserve power, cooling, water discharge, chemicals/fuel storage, and noise can require `miljötillstånd`, `anmälan om miljöfarlig verksamhet`, or court/county-board proceedings. The best official examples are Naturvårdsverket-hosted decisions and Mark- och miljödomstolen pages.
- Sweden's power system is a gating screen. Svenska kraftnät says ongoing connection cases include large datacenter demand, and its public table showed roughly 7 GW of datacenter electricity-use requests in the queue in 2026. Use this as national/regional context, not as a project list: https://www.svk.se/aktorsportalen/anslut-till-transmissionsnatet/information-om-pagaende-anslutningsarenden/.
- `PTS` (Post- och telestyrelsen) is useful for telecom/cloud-service regulation and resilience context, not a facility census. PTS states it is Sweden's competent authority for the EU Data Act, which covers cloud service providers and switching/interoperability obligations: https://pts.se/internet-och-telefoni/dataforordningen/.
- `NIS2`/Sweden's Cybersecurity Act creates an operator-registration/security trail for digital infrastructure categories, but public facility-level data may be limited. MSB/NCSC states Sweden implements NIS2 through the `cybersäkerhetslagen` from 2026-01-15: https://www.msb.se/sv/amnesomraden/informationssakerhet-cybersakerhet-och-sakra-kommunikationer/krav-och-regler-inom-informationssakerhet-och-cybersakerhet/nis-direktivet/det-har-ar-nis2-direktivet/.
- Official cloud regions are **metro/county seeds only**. AWS `eu-north-1` is Europe (Stockholm), Azure lists Sweden Central/Sweden South, Google Cloud `europe-north2` is Stockholm, and OCI `eu-stockholm-1` is Sweden Central (Stockholm). Do not infer exact buildings from cloud-region names.

Lifecycle vocabulary:

`markanvisning` / `intentionsavtal` / `förstudie` < `samråd` / `granskning` / `detaljplan` < `antagen detaljplan` / `laga kraft` < `bygglov` / `marklov` < `startbesked` < `miljötillstånd` / `miljöprövning` / `dom` < `upphandling` / `byggstart` < `driftsättning` / `i drift` < `utbyggnad` / `ändringstillstånd`.

Count a facility/project as high-confidence only after `bygglov`, `startbesked`, `miljötillstånd`, court/county-board permit, confirmed construction, or official operator page. Treat site acquisition, cloud region, grid queue, or political announcements as leads until cross-checked.

---

## 1. Swedish and English query patterns

Use Swedish first for official portals and documents.

```text
datacenter
data center
datacentre
datorhall
serverhall
serverhallar
molnregion
molntjänster
kolokation OR colocation OR colocering
hyperscale
AI-datacenter
beräkningshall
HPC datacenter
```

Planning/building:

```text
"{kommun}" datacenter bygglov
"{kommun}" datacenter marklov
"{kommun}" datacenter detaljplan
"{kommun}" serverhall bygglov
"{kommun}" datorhall bygglov
"{kommun}" "startbesked" datacenter
"{kommun}" "slutbesked" datacenter
"{kommun}" "antagande" "detaljplan" datacenter
"{kommun}" "samråd" "detaljplan" datacenter
"{kommun}" "granskning" "detaljplan" datacenter
site:{kommun-domain} datacenter bygglov
site:{kommun-domain} datacenter detaljplan
site:{kommun-domain} serverhall OR datorhall
```

Environmental/court:

```text
site:naturvardsverket.se datacenter miljöbalken
site:naturvardsverket.se "Tillstånd enligt miljöbalken" datacenter
site:lansstyrelsen.se datacenter miljötillstånd
site:lansstyrelsen.se "miljöprövningsdelegationen" datacenter
site:domstol.se "Mark- och miljödomstolen" datacenter
"{operator}" "{kommun}" miljötillstånd
"{operator}" "{kommun}" reservkraft
"{operator}" "{kommun}" "9 kap. miljöbalken"
"{operator}" "{kommun}" "miljöprövningsförordningen"
"{operator}" "{kommun}" "dieselgenerator"
"{operator}" "{kommun}" "buller" datacenter
"{operator}" "{kommun}" "kylvatten" OR "processvatten"
```

Grid/energy:

```text
site:svk.se datacenter anslutningsärenden
site:svk.se datacenter nätutvecklingsplan
site:svk.se "{län}" "nätutvecklingsplan"
site:ei.se datacenter elnät
site:energimarknadsinspektionen.se datacenter
"{kommun}" datacenter "MW"
"{kommun}" datacenter "MVA"
"{kommun}" datacenter elanslutning
"{kommun}" datacenter nätkapacitet
"{kommun}" datacenter transformatorstation
"{kommun}" datacenter ställverk
"{kommun}" datacenter restvärme OR spillvärme
```

English discovery:

```text
"Sweden" "data center" "building permit"
"Sweden" "data center" "environmental permit"
"Sweden" "data center" "Land and Environment Court"
"Stockholm" "data center" "permit"
"Gävle" "data center" "Microsoft"
"Staffanstorp" "data center" "Microsoft"
"Luleå" "data center" "Meta"
"Avesta" "Horndal" "Google" "data center"
"Boden" "data center" "MW"
"Skellefteå" "data center"
"Västerås" "Amazon Data Services" "reserve power"
```

---

## 2. Grade A official/regulatory source backbone

### 2.1 Municipal planning and building permits

Core sources:

- **Municipal websites and e-services**. Search each municipality's planning/building pages for `detaljplaner`, `pågående detaljplaner`, `bygglov`, `diarium`, `anslagstavla`, `kungörelser`, `protokoll`, and planning PDFs. Grade A.
- **Boverket PBL Knowledge Bank / building permit guidance**: https://www.boverket.se/. Grade A process context. It explains planning/building rules, but it is not project-level.
- **Lantmäteriet detailed plans / NGP**: https://www.lantmateriet.se/sv/kartor/vara-karttjanster/detaljplaner/. Grade A for adopted detailed-plan geography and plan identifiers when uploaded.
- **Municipal council/building committee minutes** (`kommunstyrelsen`, `samhällsbyggnadsnämnden`, `byggnadsnämnden`, `miljö- och byggnämnden`). These often expose applicant names, decisions, addresses, and conditions before a searchable permit page is indexed. Grade A when hosted by the municipality.

Search pattern by municipality:

```text
site:{kommun-domain} "datacenter"
site:{kommun-domain} "serverhall"
site:{kommun-domain} "datorhall"
site:{kommun-domain} "bygglov" "datacenter"
site:{kommun-domain} "marklov" "datacenter"
site:{kommun-domain} "detaljplan" "datacenter"
site:{kommun-domain} "startbesked" "datacenter"
site:{kommun-domain} "protokoll" "datacenter"
```

Fields to extract: municipality, county, permit/planning reference, applicant/SPV, property designation (`fastighetsbeteckning`), address, detailed-plan title, land area, gross floor area, number of halls/buildings, reserve-power scope, cooling/water/discharge, `startbesked`, `slutbesked`, decision date, appeal status, and links to PDFs.

Official example leads:

- **Avesta/Horndal, Dalarna**: Avesta municipality confirms Google acquired 109 hectares in Horndal and later announced land/building-plan steps; use Avesta pages and Västmanland-Dalarna miljö- och byggförvaltning records as the municipal Grade A layer: https://avesta.se/-/nyheter/arbete-och-naringsliv/xxx-har-kopt-mark-i-avesta-kommun/ and https://avesta.se/-/nyheter/arbete-och-naringsliv/google-ansoker-om-nytt-marklov-for-datacenter-i-horndal/.
- **Horndal detailed-plan change**: Avesta page for amendment/repeal of part of the detailed plan for industrial land north of Horndal: https://avesta.se/bygga-bo-och-miljo/planering-byggande-och-boende/kommunens-planarbete/aktuella-planer-och-projekt/andring-och-upphavande-av-del-av--detaljplan-for-industrimark-norr-om-horndal-avesta-kommun/.

### 2.2 Environmental permits, county boards, and courts

Core sources:

- **County Administrative Boards / Länsstyrelsen**: https://www.lansstyrelsen.se/. Search the relevant county for `miljöprövningsdelegationen`, `kungörelse`, `miljötillstånd`, `datacenter`, `reservkraft`, and applicant/operator names. Grade A.
- **Naturvårdsverket public permit/case PDFs**: https://www.naturvardsverket.se/. Its search surfaces decisions from environmental review delegations and courts. Grade A when the PDF is an authority decision.
- **Swedish courts / Domstol.se**: https://www.domstol.se/. Search `Mark- och miljödomstolen datacenter`, `Nacka tingsrätt datacenter`, and operator names. Grade A.

Official examples:

- **Equinix SK2, Stockholm County**: Naturvårdsverket-hosted decision, `Tillstånd enligt miljöbalken till drift av datacenter, SK2...`, says the Environmental Review Delegation at the Stockholm County Administrative Board granted Equinix (Sweden) AB a permit under Chapter 9 of the Environmental Code for datacenter operation and reserve-power combustion installations. URL: https://www.naturvardsverket.se/497b37/contentassets/781859e933a341fab467a6212408a590/240418/2023-06-08-mpd-stockholm.pdf.
- **AWS Västerås, Västmanland**: Naturvårdsverket-hosted Nacka Land and Environment Court judgment for Amazon Data Services Sweden AB reserve-power expansion, with a total installed input effect up to 660 MW on `Kvastbruket 1` in Västerås municipality. URL: https://www.naturvardsverket.se/4926e0/contentassets/4eef28e4813b4c309697ffd56ae8165c/2022-09-29-mmd-nacka-vasteras.pdf.
- **Google Horndal, Dalarna**: Domstol.se news says the Land and Environment Court granted permission for a datacenter in Horndal, Avesta municipality, with conditions including renewable energy and heat availability; use the judgment as Grade A and trade press only for summaries. URL: https://www.domstol.se/nyheter/2021/06/mark--och-miljodomstolen-lamnar-tillstand-till-datacenter-i-horndal-avesta-kommun/.

Environmental extraction terms:

```text
verksamhetskod
tillståndsplikt B
miljöfarlig verksamhet
reservkraftsanläggning
förbränningsanläggning
installerad tillförd effekt
dieselgeneratorer
bränsleförbrukning
kylvatten
processvatten
dagvatten
buller
luftutsläpp
miljörapport
kontrollprogram
igångsättningstid
```

### 2.3 Grid, energy, and district heat

Primary sources:

- **Svenska kraftnät** (transmission system operator): https://www.svk.se/. Use `nätutvecklingsplan`, regional county pages, `Kapacitetskarta`, transmission projects, and connection-process pages. Grade A for grid context and aggregate queue data.
- **Svenska kraftnät ongoing connection cases**: https://www.svk.se/aktorsportalen/anslut-till-transmissionsnatet/information-om-pagaende-anslutningsarenden/. Grade A aggregate signal; it separates `Datacenter` electricity use but normally does not name facilities.
- **Svenska kraftnät Nätutvecklingsplan 2026-2035**: https://www.svk.se/om-oss/rapporter-och-remissvar/natutvecklingsplan/. Grade A for national/regional network constraints.
- **Svenska kraftnät regional pages** such as Västra Götaland: https://www.svk.se/utveckling-av-kraftsystemet/transmissionsnatet/Sa-planerar-vi-elnatet-for-framtiden/vastra-gotalands-lan/. Grade A for county power-system context.
- **Energimarknadsinspektionen (Ei)**: https://ei.se/ and https://www.energimarknadsinspektionen.se/. Grade A for electricity-network regulation, connection/queue policy, and tariff context.
- **Local/regional grid companies**. High-yield examples: Ellevio (Stockholm, Dalarna, Värmland, Gävleborg), E.ON Energidistribution (Skåne/South), Vattenfall Eldistribution (many regions), Göteborg Energi Nät, Jämtkraft, Skellefteå Kraft, Luleå Energi, Borlänge Energi, Falu Energi & Vatten, Gavle Energi. Use grid-company project pages and consultation PDFs as A/B depending on source.
- **District-heating companies**. Stockholm Exergi, Göteborg Energi, Kraftringen, E.ON, Vattenfall, Falu Energi & Vatten, Borlänge Energi, Jämtkraft, and local municipal energy companies can expose `spillvärme/restvärme` agreements tied to datacenters.

Do not equate grid-connection queue MW with facility IT load. Keep `ansökt effekt`, `abonnerad effekt`, `installerad tillförd effekt` for reserve generators, `IT load`, and `gross power` as separate fields.

### 2.4 PTS, Data Act, NIS2, and digital-infrastructure regulation

Use these as regulator/context sources, not as a facility census:

- **PTS Data Act page**: https://pts.se/internet-och-telefoni/dataforordningen/. Grade A. It says PTS has been appointed competent authority for the EU Data Act and that the regulation covers cloud service providers within the EU.
- **PTS digital infrastructure / CEF Digital**: https://pts.se/om-oss/internationellt-arbete/sok-pengar-fran-EU-for-digital-infrastruktur/. Grade A for EU-funded digital infrastructure context.
- **MSB/NCSC Cybersecurity Act/NIS2 page**: https://www.msb.se/sv/amnesomraden/informationssakerhet-cybersakerhet-och-sakra-kommunikationer/krav-och-regler-inom-informationssakerhet-och-cybersakerhet/nis-direktivet/det-har-ar-nis2-direktivet/. Grade A for NIS2 implementation status.
- **Länsstyrelsen security-protection and protected-object pages** can matter for critical facilities, but public detail may be intentionally limited. Treat absence of location details as expected, not as evidence the site does not exist.

### 2.5 Trade/investment/association sources

- **Business Sweden / Data Centers by Sweden**: https://www.business-sweden.com/. Grade B+/A- depending on content. It is government/industry-backed investment promotion, useful for site-finder leads and AWS/Microsoft/Google establishment context, but still verify facility records in permits.
- **Business Sweden site finder**: https://www.business-sweden.com/invest-in-sweden/online-tools/site-finder/. Grade B lead source for industrial/datacenter-ready sites, not facility evidence.
- **Swedish Data Center Industry Association (SweDCI)**: https://www.sdia.se/. Grade B for member/operator ecosystem and policy positions.
- **Data Center Dynamics (DCD)** Sweden tag: https://www.datacenterdynamics.com/en/tags/sweden/. Grade B trade press for recent announcements; pivot every project to municipal/environmental/operator primary sources.
- **Datacenter Forum Sweden**: https://www.datacenter-forum.com/. Grade B trade/event/operator directory; useful for local announcements and operator names.
- **DatacenterMap/Baxtel/DataCenters.com**: Grade C/B-. Use only to seed legacy colo addresses and operator names; verify against operator official pages or permits.

---

## 3. Official cloud and operator seed list

### 3.1 Hyperscale cloud regions (Grade A for region existence only)

| Provider | Official source | Sweden signal | Method use |
|---|---|---|---|
| AWS | AWS region docs https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html and AWS launch blog https://aws.amazon.com/blogs/aws/now-open-aws-europe-stockholm-region/ | `eu-north-1`, Europe (Stockholm), 3 AZs | Seed Stockholm/Mälardalen searches; AWS Sweden facility evidence is stronger in Västerås/Eskilstuna/Katrineholm-style municipal/environmental records than in cloud docs. |
| Microsoft Azure | Azure region list https://learn.microsoft.com/en-us/azure/reliability/regions-list and Azure geography page https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies | Sweden Central and Sweden South; public reporting places presence around Gävle/Sandviken and Staffanstorp/Malmö | Seed Gävleborg, Dalarna/Gävle-Sandviken area, and Skåne/Staffanstorp/Malmö queries; use municipal permits and Microsoft official sustainability/local pages for confirmation. |
| Google Cloud | Locations https://cloud.google.com/about/locations, Compute zones https://docs.cloud.google.com/compute/docs/regions-zones, launch blog https://cloud.google.com/blog/products/infrastructure/google-cloud-launches-42nd-cloud-region-in-sweden | `europe-north2`, Stockholm, 3 zones | Seed Stockholm cloud-region search; separately track Google-owned Horndal/Avesta project as Dalarna facility evidence. |
| Oracle OCI | OCI release note https://docs.oracle.com/iaas/releasenotes/changes/74484749-00f3-46bf-b9b5-d77419b72446/index.htm and Oracle announcement https://www.oracle.com/news/announcement/oracle-cloud-stockholm-region-2021-12-15/ | Sweden Central (Stockholm), `eu-stockholm-1`, 1 availability domain | Seed Stockholm/colocation searches; do not infer exact building. |

### 3.2 Priority colo/operator official pages

| Operator | Official URL | High-yield counties/municipalities | Notes |
|---|---|---|---|
| Equinix | https://www.equinix.com/data-centers/europe-colocation/sweden-colocation and Stockholm page https://www.equinix.com/data-centers/europe-colocation/sweden-colocation/stockholm-data-centers | Stockholm | Official page says Equinix operates three data centers in Sweden; verify SK1/SK2/SK3 against Stockholm municipal and environmental records. |
| atNorth | https://www.atnorth.com/nordic-data-centers/sweden-data-centers/ | Stockholm/Kista, Norrland expansion leads | Official page lists Sweden sites such as SWE01 Stockholm metro; trade press reports SWE02 and Sollefteå/mega-site leads require permit checks. |
| EcoDataCenter | https://ecodatacenter.tech/ and sites page https://ecodatacenter.tech/data-center | Dalarna: Falun, Borlänge; Jämtland/Östersund legacy/development leads | Official pages list Falun/Borlänge assets and power figures; verify expansion via Falun/Borlänge municipal records and environmental permits. |
| Bahnhof | https://www.bahnhof.se/ | Stockholm and other Swedish metros | Official pages plus PTS filings can identify operator activity; facility detail may require municipal and press cross-check. |
| Conapto | https://www.conapto.com/ | Stockholm | Official operator for Stockholm colocation; use municipal permits and DCD for expansion leads. |
| Digital Realty | https://www.digitalrealty.com/ | Stockholm legacy/interconnection market leads | Verify Sweden assets via official locations and local records. |
| GleSYS | https://glesys.se/ | Halland/Falkenberg, Stockholm, Malmö | Official pages are useful for smaller colo/hosting facilities. |
| GlobalConnect | https://www.globalconnect.se/ | Stockholm, Malmö, Gothenburg, Nordic fiber/DC footprint | Operator/fiber backbone lead. |
| Meta | https://datacenters.atmeta.com/ | Norrbotten/Luleå | Official Meta datacenter page plus Luleå/Norrbotten permits and energy records. |
| Microsoft | https://datacenters.microsoft.com/ and Azure pages | Gävle/Sandviken, Staffanstorp/Skåne | Use official cloud/local datacenter pages, then municipal/environmental permits. |
| Google | https://www.google.com/about/datacenters/ and Google Cloud locations | Stockholm cloud region; Avesta/Horndal owned project | Avesta/Domstol pages are stronger facility evidence than cloud-region pages. |
| AWS / Amazon Data Services Sweden AB | https://aws.amazon.com/about-aws/global-infrastructure/ | Stockholm region; Västerås environmental permit example | Search the legal entity and property names in municipal/court records. |
| Vantage Data Centers | https://vantage-dc.com/ | Swedish leads via Svenska kraftnät consultation response | Treat as lead until operator/permit source confirms specific Swedish sites. |
| Hive Digital / AI/HPC operators | operator official pages plus DCD | Boden/Norrbotten and Stockholm leads | Verify against municipal permit/building records. |

Operator workflow:

1. Record official facility/campus/site name and metro/county.
2. Search Swedish legal entity names in municipal and environmental sources: `"Amazon Data Services Sweden AB"`, `"Equinix (Sweden) AB"`, `"DSC International AB"`, `"Microsoft Sweden"`, `"EcoDataCenter"`, `"Conapto"`, `"atNorth"`.
3. Search `fastighetsbeteckning` and address from permits.
4. Attach a Grade A planning/environmental/operator URL before counting the facility as confirmed.

---

## 4. County-by-county enumeration strategy

General county method:

1. Start with the biggest municipalities and known datacenter clusters in the county.
2. Search county/municipal Swedish terms first (`län`, `kommun`, `bygglov`, `detaljplan`, `miljötillstånd`, `serverhall`, `reservkraft`).
3. Search Länsstyrelsen and Naturvårdsverket for environmental permits and public notices.
4. Search Svenska kraftnät county/regional grid pages plus local DSO pages for connection constraints.
5. Add official cloud/operator seeds; then use DCD/Datacenter Forum as freshness checks.

| Repo county | Swedish county | Priority municipalities / clusters | Official-first query focus |
|---|---|---|---|
| Stockholm | Stockholms län | Stockholm, Solna, Sollentuna, Järfälla, Upplands Väsby, Sigtuna/Arlanda, Kista, Sköndal, Bromma | Equinix, atNorth SWE01/SWE02, Conapto, Bahnhof, Oracle/Google/AWS Stockholm region seeds; search Stockholm County MPD permits, municipal building records, Stockholm Exergi rest-heat. |
| Vasterbotten | Västerbottens län | Umeå, Skellefteå, Lycksele | Search Skellefteå Kraft, Umeå Energi, industrial park/site-selection records, `AI-datacenter`, `serverhall`, hydropower/low-carbon power leads. |
| Norrbotten | Norrbottens län | Luleå, Boden, Piteå, Gällivare, Kiruna | Meta Luleå, Boden AI/HPC/large-load projects, Node Pole/Business Sweden leads; search Luleå/Boden permits, Länsstyrelsen Norrbotten, Svenska kraftnät northern grid plans. |
| Uppsala | Uppsala län | Uppsala, Enköping, Tierp | Search `datacenter bygglov`, `reservkraft`, E4/Mälardalen logistics/industrial plans; check Uppsala County MPD if reserve-power permits appear. |
| Sodermanland | Södermanlands län | Eskilstuna, Katrineholm, Strängnäs, Nyköping | AWS/Mälardalen-style cloud-region support leads, Eskilstuna/Katrineholm municipal planning, `Amazon Data Services Sweden AB`, grid/substation terms. |
| Ostergotland | Östergötlands län | Linköping, Norrköping, Mjölby | Search university/defense/enterprise datacenters, industrial plans, Tekniska verken rest-heat, E.ON/Vattenfall grid projects. |
| Jonkoping | Jönköpings län | Jönköping, Nässjö, Värnamo | Search logistics corridor/datacenter planning, municipal minutes, `serverhall`, local energy/grid pages. |
| Kronoberg | Kronobergs län | Växjö, Ljungby, Älmhult | Lower expected hyperscale density; search municipal building records and regional energy/industrial parks. |
| Kalmar | Kalmar län | Kalmar, Oskarshamn, Västervik | Search industrial power/port-adjacent leads, municipal planning, `datorhall`, backup-power permits. |
| Gotland | Gotlands län | Visby/Region Gotland | Search Region Gotland planning, telecom/edge facilities, power constraints; expect smaller edge/enterprise records. |
| Blekinge | Blekinge län | Karlskrona, Ronneby, Karlshamn | Search telecom/defense/port/fiber routes, municipal planning and environmental records. |
| Scania | Skåne län | Malmö, Lund, Staffanstorp, Helsingborg, Landskrona | Azure Sweden South / Staffanstorp-Malmö seed, Kraftringen/E.ON regional grid context, municipal `bygglov datacenter`, Länsstyrelsen Skåne environmental permits. |
| Halland | Hallands län | Falkenberg, Halmstad, Varberg | GleSYS/Falkenberg and smaller colo/hosting leads; search municipal permits, Falkenberg Energi, local press. |
| Vastra Gotaland | Västra Götalands län | Göteborg, Borås, Mölndal, Trollhättan, Skövde | Strong grid constraint angle; search Göteborg Energi, Svenska kraftnät Västra Götaland page, municipal `serverhall`/`datacenter`, port/industrial estates, Conapto/GlobalConnect/operator leads. |
| Varmland | Värmlands län | Karlstad, Kristinehamn, Arvika | Search Ellevio/Vattenfall capacity, municipal planning, Nordic fiber/edge. |
| Orebro | Örebro län | Örebro, Kumla, Hallsberg | Search logistics corridor, municipal plans, reserve-power and substations. |
| Vastmanland | Västmanlands län | Västerås, Enköping border area, Köping | High priority: AWS/Amazon Data Services Sweden AB and `Kvastbruket 1`; search Nacka MMD/Naturvårdsverket decisions, Västerås municipal permits, Mälarenergi rest heat. |
| Dalarna | Dalarnas län | Avesta/Horndal, Falun, Borlänge | High priority: Google Horndal and EcoDataCenter Falun/Borlänge; search Avesta, V-Dala miljö- och byggförvaltning, Falu/Borlänge permits, local energy/rest heat. |
| Gavleborg | Gävleborgs län | Gävle, Sandviken, Söderhamn | High priority: Microsoft/Gävle-Sandviken cloud-region presence; search Gävle/Sandviken municipal records, Gavle Energi, Svenska kraftnät regional pages. |
| Western Northland | Västernorrlands län | Sundsvall, Sollefteå, Härnösand, Örnsköldsvik | Search atNorth/Sollefteå leads, hydropower/industrial land, `datacenter detaljplan`, local grid/energy. |
| Jamtland | Jämtlands län | Östersund, Åre, Krokom | Search EcoDataCenter/Östersund legacy/development leads, Jämtkraft, municipal planning, cold-climate/HPC marketing cross-checks. |

High-yield county query template:

```text
"{Swedish county}" datacenter
"{Swedish county}" "serverhall"
"{municipality}" "datacenter" "bygglov"
"{municipality}" "datacenter" "detaljplan"
"{municipality}" "datacenter" "miljötillstånd"
"{municipality}" "serverhall" "reservkraft"
site:lansstyrelsen.se "{Swedish county}" datacenter
site:naturvardsverket.se "{municipality}" datacenter
site:domstol.se "{municipality}" datacenter
site:svk.se "{Swedish county}" datacenter
```

---

## 5. Validation and de-duplication rules

- **Cloud region vs facility**: AWS/Azure/GCP/OCI region pages prove a cloud service region, not a specific address. Count as cloud-region seed unless a permit/operator source identifies a facility.
- **Municipal plan vs facility**: an adopted `detaljplan` allowing industrial/datacenter use is a site-capacity record; count as facility only when attached to a named operator/applicant, building permit, environmental permit, construction, or operation.
- **Environmental permit vs building permit**: a `miljötillstånd` for reserve-power/datacenter operation is strong facility evidence even if building documents are hard to find. Still search municipal `bygglov/startbesked` to capture size and phasing.
- **Reserve-power MW**: Swedish environmental documents may state installed input effect for backup combustion (`installerad tillförd effekt`) that is much larger than IT load. Do not store it as IT MW.
- **Protected/security-sensitive sites**: telecom/public-sector facilities may hide exact location. Use operator/county-level evidence and mark coordinates/address confidence low when public sources are intentionally vague.
- **Name variants**: search both English and Swedish spelling, and both legal and marketing names: `data center/datacenter/datacentre`, `serverhall/datorhall`, `Amazon Data Services Sweden AB/AWS`, `Google/DSC International AB`, `Equinix (Sweden) AB`, `Microsoft/Microsoft Sweden`.
- **Trade press freshness**: DCD and Datacenter Forum are excellent for 2025-2026 changes (Google Horndal construction, Conapto/CoreWeave, Boden/Hive, atNorth SWE02), but every fresh lead should be reconciled to a municipal, court, county-board, operator, or official cloud page before final confidence.

Minimum evidence packet per confirmed record:

```text
country=SE
county repo name + Swedish county name
municipality
facility/campus name
operator and legal entity/SPV
address or fastighetsbeteckning
evidence type: bygglov / marklov / detaljplan / miljötillstånd / court judgment / operator official / cloud region / construction
permit/case/reference number when available
capacity fields separated: IT MW, grid MW/MVA, reserve-power installed input MW, floorspace sqm
status and date
source URL + reliability grade
notes on uncertainty
```

---

## 6. Source reliability quick guide

- **A**: municipal building/planning portal or PDF; Länsstyrelsen/MPD environmental decision; Domstol.se/Mark- och miljödomstolen judgment; Naturvårdsverket-hosted authority decision; Svenska kraftnät/Ei/PTS/MSB official pages; operator official facility page; official AWS/Azure/GCP/OCI cloud-region documentation.
- **B**: Business Sweden/Data Centers by Sweden investment pages, SweDCI, DCD, Datacenter Forum, named local news with official quotes/documents.
- **C**: DatacenterMap, Baxtel, DataCenters.com, CloudInfrastructureMap, LinkedIn posts, social media, scraped directories, market-report snippets. Use these only as search seeds unless corroborated.
