# FI Explorer Official - Finland Datacenter Enumeration via Municipal Permits, YVA, Energy/Grid, Cloud, Colo, and Traficom

Date: 2026-08-12. Scope: Finland (FI), all regions/maakunnat and municipalities. Angle: **official/regulatory/cloud pipeline** for finding datacenter facilities and projects. Reliability grades: **A** = official/primary source, **B** = strong secondary/trade/association source, **C** = weak/aggregate/unverified.

---

## 0. Finland-specific structural facts

- Finland has **no single public national datacenter permit register**. Construction evidence is municipal: zoning (`kaavoitus`, `asemakaava`, `yleiskaava`), building supervision (`rakennusvalvonta`), building permits (`rakennuslupa` / from 2025 also `rakentamislupa`), council agendas, and municipal notices.
- The highest-yield national official discovery source is often **YVA**: the environmental impact assessment pages on `ymparisto.fi`. Large datacenter campuses appear there because backup generation, fuel storage, substations, cooling, earthworks, and electricity use can trigger assessment or screening. YVA pages often disclose project owner, municipality, region, land area, building count, IT load MW, total electrical load, backup-generator fuel power, ELY authority, and case status.
- Municipal planning usually precedes the building permit. Search for `datakeskus`, `konesali`, `pilvipalvelukeskus`, `palvelinkeskus`, `asemakaava`, `kaavamuutos`, `tontinluovutus`, `maankäyttösopimus`, and `rakentamislupa` in the target municipality.
- **Lupapiste** is the common electronic construction-permit platform, but it is not a complete open national search API for all application contents. Its public notice service (`julkipano.lupapiste.fi`) can expose municipal permit notices and decisions; detailed drawings often require municipality contact.
- Electricity grid evidence is central. Use **Fingrid** for main-grid development, transmission-map context, and connection-process rules; use regional distribution-network operators and municipal energy companies for local substations, district heating, and waste-heat projects.
- **Traficom / NCSC-FI** is relevant for cyber/NIS2 supervision of digital infrastructure, digital services, and ICT services. Treat it as a regulatory context and operator-registration lead, not as a public real-estate/facility census.
- Cloud-region pages are metro/region seeds only. Microsoft has an announced/building Finland cloud region in Southern Finland; Google has an official Hamina datacenter; AWS shows edge/local-zone signals rather than a Finnish AWS Region; OCI has no Finnish public cloud region in the official region list as of this research.

Finnish lifecycle vocabulary:

`selvitys` < `kaavoitusaloite` / `kaavahanke` < `osallistumis- ja arviointisuunnitelma` / `OAS` < `kaavaluonnos` < `kaavaehdotus` < `hyväksytty asemakaava` < `lainvoimainen kaava` < `rakennuslupa` / `rakentamislupa` < `aloittamisoikeus` < `rakentaminen alkaa` < `käyttöönotto` / `toiminnassa`

Only count `rakennuslupa`, `rakentamislupa`, `aloittamisoikeus`, construction start, or operation as hard build evidence. Treat zoning, land sale, YVA, and grid reservation as planned-project evidence until cross-checked.

---

## 1. Finnish and English query patterns

### 1.1 Core Finnish terms

Use Finnish first; English finds cloud/operator pages and trade press.

```
datakeskus
konesali
palvelinkeskus
pilvipalvelukeskus
data center OR data centre OR datacenter
hyperscale
tekoälydatakeskus OR AI-datakeskus
rakennuslupa datakeskus
rakentamislupa datakeskus
rakennusvalvonta datakeskus
asemakaava datakeskus
kaavamuutos datakeskus
kaavoitusaloite datakeskus
yleiskaava datakeskus
tontinluovutus datakeskus
maankäyttösopimus datakeskus
YVA datakeskus
ympäristövaikutusten arviointi datakeskus
ympäristölupa datakeskus
varavoimageneraattori datakeskus
polttoaineteho datakeskus
sähköasema datakeskus
verkkoliityntä datakeskus
kantaverkko datakeskus
hukkalämpö datakeskus
kaukolämpö datakeskus
```

### 1.2 Discovery queries by municipality/region

Substitute `{kunta}`, `{maakunta}`, `{operator}`, `{site}`, `{DSO}`, and Swedish municipality names where applicable.

Planning/building:

```
"{kunta}" "datakeskus" "asemakaava"
"{kunta}" "datakeskus" "rakennuslupa"
"{kunta}" "datakeskus" "rakentamislupa"
"{kunta}" "konesali" "rakennuslupa"
"{kunta}" "datakeskus" "kaavamuutos"
"{kunta}" "datakeskus" "tontinluovutus"
"{kunta}" "datakeskus" "maankäyttösopimus"
"{kunta}" "datakeskus" "aloittamisoikeus"
site:{municipality-domain} datakeskus asemakaava
site:{municipality-domain} datakeskus rakennuslupa
site:{municipality-domain} datakeskus rakentamislupa
site:{municipality-domain} konesali
filetype:pdf "datakeskus" "asemakaavan selostus" "{kunta}"
filetype:pdf "datakeskus" "osallistumis- ja arviointisuunnitelma" "{kunta}"
filetype:pdf "datakeskus" "rakennuslupa" "{kunta}"
```

YVA/environment:

```
site:ymparisto.fi datakeskus "{kunta}"
site:ymparisto.fi datakeskus "{maakunta}"
site:ymparisto.fi "YVA" "datakeskus"
site:ymparisto.fi "varavoimageneraattoreiden" "datakeskus"
site:ymparisto.fi "IT-teho" "datakeskus"
site:ymparisto.fi "kokonaissähköteho" "datakeskus"
"{operator}" "datakeskus" "YVA"
"{kunta}" "datakeskus" "ympäristölupa"
"{kunta}" "datakeskus" "meluilmoitus"
```

Grid/energy:

```
"{kunta}" "datakeskus" "sähköasema"
"{kunta}" "datakeskus" "verkkoliityntä"
"{kunta}" "datakeskus" "kantaverkko"
"{kunta}" "datakeskus" "110 kV" OR "400 kV"
"{operator}" "{kunta}" "MW" "datakeskus"
"{operator}" "{kunta}" "hukkalämpö"
"{operator}" "{kunta}" "kaukolämpö"
site:fingrid.fi datakeskus
site:fingrid.fi "data centre" Finland
site:fingrid.fi "grid connection" "data centres"
site:{dso-domain} datakeskus sähköasema
```

English:

```
"Finland" "data center" "building permit"
"Finland" "data centre" "environmental impact assessment"
"Finland" "data center" "grid connection"
"Finland" "data center" "district heating"
"{municipality}" "data center" "zoning"
"{operator}" "{municipality}" "data center" "MW"
"Southern Finland" "Microsoft" "datacenter region"
"Hamina" "Google" "data center"
```

Swedish-language variants for bilingual municipalities:

```
datacenter
datacentral
serverhall
bygglov datacenter
detaljplan datacenter
miljökonsekvensbedömning datacenter
reservkraft datacenter
fjärrvärme datacenter
```

---

## 2. Grade A official/regulatory sources

### 2.1 Municipal planning and building permits

Primary rule: for each division, route to the **municipality** first. Finnish regions do not issue ordinary building permits; municipalities do. Regional councils (`maakuntaliitto`) matter for strategic land-use plans, but datacenter enumeration usually becomes concrete at municipal zoning/building-control level.

Core portals and routes:

- **Lupapiste**: https://www.lupapiste.fi/. Grade A for electronic permit handling context. Use the municipality's own guidance page to confirm whether it uses Lupapiste.
- **Lupapiste public notices / julkipano**: https://julkipano.lupapiste.fi/. Grade A when a public permit notice or decision is visible. Search by municipality/date/keywords where available; otherwise use web search `site:julkipano.lupapiste.fi datakeskus`.
- **Suomi.fi Lupapiste service page**: https://www.suomi.fi/palvelut/verkkoasiointi/lupapiste-cloudpermit-oy/2487b119-4121-48b8-b6ef-a64a80f2efe3. Grade A for official service description.
- **Suomi.fi construction overview**: https://www.suomi.fi/citizen/housing-and-construction/construction-and-properties. Grade A for the basic rule that building permits are municipal and municipalities draw up local master/detailed plans.
- **Helsinki building permits**: https://www.hel.fi/en/urban-environment-and-traffic/plots-and-building-permits/applying-for-a-building-permit/building-permit-and-other-permits. Grade A example: Helsinki states construction permits are submitted electronically in Lupapiste.

Municipal evidence to extract:

- permit/application ID, especially `LP-...` Lupapiste identifiers;
- applicant legal entity/SPV, parcel, district/neighborhood, and plan name;
- `asemakaava` status and legal force date (`lainvoimainen`);
- building count, gross floor area, data halls, ancillary buildings, substations, generator yards, fuel tanks;
- start permission (`aloittamisoikeus`), decision date, appeal period, construction start;
- waste-heat/district-heating counterparty, usually Fortum, Helen, Vantaa Energy, Lahti Energia, local municipal energy company, etc.

Known official examples that show the workflow:

- Espoo Hepokorvenkallio/Microsoft land sale and plan legal-force notice: https://www.espoo.fi/fi/uutiset/2023/12/espoo-myi-microsoftille-maata-hepokorvesta-datakeskusta-varten and https://www.espoo.fi/fi/uutiset/2023/11/hepokorvenkallion-asemakaava-lainvoimaiseksi-kho-ei-myontanyt-valituslupaa. Grade A.
- Kirkkonummi Microsoft construction-permit progress: https://kirkkonummi.fi/microsoftin-datakeskushanke-etenee-kirkkonummella/ and phase-two permit notice https://kirkkonummi.fi/microsoftin-datakeskushankkeen-toisen-vaiheen-rakentamislupa-on-vireilla/. Grade A. These show the useful terms `rakennuslupahakemus`, `rakentamislupahakemus`, `aloittamisoikeus`, environmental permit for crushing, and `meluilmoitus`.
- Microsoft Local project update page for Finland/Southern Finland: https://local.microsoft.com/communities/emea/suomidc/ and Kirkkonummi updates https://local.microsoft.com/blog/microsoft-aikoo-rakentaa-uuden-datakeskusalueen-etela-suomeen/. Grade A for Microsoft intent/project messaging; confirm permits on municipal/YVA pages.

### 2.2 YVA / ELY environmental assessment

Start here for large campuses:

- **Ymparisto.fi YVA pages**: https://www.ymparisto.fi/fi/osallistu-ja-vaikuta/ymparistovaikutusten-arviointi. Grade A. Search `datakeskus`, operator, municipality, and region.
- Example project pages:
  - Espoo datacenter area: https://www.ymparisto.fi/fi/osallistu-ja-vaikuta/ymparistovaikutusten-arviointi/espoon-datakeskusalue-espoo. Grade A; Microsoft 3465 Finland Oy, about 28 ha in Espoo.
  - Vihti datacenter: https://www.ymparisto.fi/fi/osallistu-ja-vaikuta/ymparistovaikutusten-arviointi/vihdin-datakeskus. Grade A; Microsoft 3465 Finland Oy, about 60 ha near Nummela.
  - Kirkkonummi datacenter: https://www.ymparisto.fi/fi/osallistu-ja-vaikuta/ymparistovaikutusten-arviointi/kirkkonummen-datakeskus. Grade A; project alternatives and backup-generator details.
  - Pyhäjoki datacenter: https://www.ymparisto.fi/fi/osallistu-ja-vaikuta/ymparistovaikutusten-arviointi/pyhajoen-datakeskus-pyhajoki. Grade A; example of very large disclosed loads, including IT power, total electrical power, and backup-generator fuel power.
  - Kouvola datacenter / Hyperco: https://www.ymparisto.fi/fi/osallistu-ja-vaikuta/ymparistovaikutusten-arviointi/kouvolan-datakeskus-hyperco-data-systems-oy-kouvola. Grade A.
  - Järvenpää datacenter YVA PDF: search `site:ymparisto.fi Järvenpään datakeskus Arviointiohjelma`. Grade A when hosted on `ymparisto.fi`.
- **YVA decisions by region**: example page for Etelä-Pohjanmaa, Keski-Pohjanmaa and Pohjanmaa decisions: https://www.ymparisto.fi/fi/osallistu-ja-vaikuta/ymparistovaikutusten-arviointi/hankkeiden-ymparistovaikutusten-arviointimenettely-yva/yva-paatokset/yva-paatokset-etela-pohjanmaa-keski-pohjanmaa-ja-pohjanmaa. Grade A. Use the regional YVA decision pages to find screening decisions where the main project page is missed.

YVA extraction checklist:

- `Hankkeesta vastaava` / project owner, business ID if present;
- `Hankealue`, municipality, parcel/industrial area, hectares;
- alternatives (`VE0`, `VE1`, `VE2`), building count, phased capacity;
- `IT-teho`, `kokonaissähköteho`, transformer/substation needs;
- `varavoimageneraattorit`, total fuel power, fuel-tank volume;
- water/cooling, noise, traffic, blasting/crushing, biodiversity constraints;
- ELY centre or permit authority, docket number (`Dnro`), status (`vireillä`, `päättynyt`, `perusteltu päätelmä annettu`).

### 2.3 Energy, grid, and district heating

Official/high-confidence sources:

- **Fingrid connection process**: https://www.fingrid.fi/en/grid/grid-connection-agreement-phases/. Grade A for main-grid connection phases and guarantee of transmission capability at connection points.
- **Fingrid grid-scope map for grid connectivity estimates and planned routes/substations**: https://www.fingrid.fi/en/grid/grid-connection-agreement-phases/grid-scope/. Grade A for map context; not a named datacenter queue.
- **Fingrid main grid development plan 2026-2035**: https://www.fingrid.fi/en/grid/development/Main-grid-development-plan/. Grade A for transmission-investment geography.
- **Fingrid electricity system / network facts**: https://www.fingrid.fi/en/grid/development/electricity-system-of-finland/ and https://www.fingrid.fi/en/grid/development/power-transmission-grid-of-fingrid/. Grade A for main-grid lines/substations context.
- **Fingrid news on 2026-2035 plan**: https://www.fingrid.fi/en/news/news/2025/main-grid-development-plan-investments-in-electricity-transmission-links-continue-to-grow/. Grade A.
- **Government roadmap/news**: https://valtioneuvosto.fi/en/-/finland-sets-out-measures-to-attract-data-centres-with-high-value-added and energy-system column https://valtioneuvosto.fi/en/-/1410877/column-data-centres-are-an-integral-part-of-a-developing-energy-system-and-economy. Grade A for policy; not project enumeration.
- **Metsähallitus roadmap page**: https://www.metsa.fi/en/responsible-business/sale-rental-and-usage-rights-of-properties/industrial-sites-for-energy-intensive-operators/roadmap-for-finnish-data-centres/. Grade A-/B+ for state land/site-selection context.
- **Energiavirasto / Energy Authority**: https://energiavirasto.fi/. Grade A for energy-market regulation and DSO regulatory materials. Use for network-company identity and regulation, but expect limited project-level datacenter disclosure.

Grid workflow:

1. From YVA/municipal documents, identify nearest substation, voltage level (`110 kV`, `220 kV`, `400 kV`), connection power, and network company.
2. Check Fingrid maps/development plan for planned substations, north-south and west-south transmission reinforcements, and project completion dates.
3. Search the local DSO and city energy company for `sähköasema`, `verkkoliityntä`, `kaukolämpö`, and `hukkalämpö`.
4. Treat grid reservations/connection discussions as leads; only count the datacenter when backed by municipal/YVA/operator evidence.

Common energy-company pivots:

- Uusimaa: Fortum, Helen, Vantaan Energia, Caruna/Espoo-related networks, local DSOs.
- Päijät-Häme: Lahti Energia.
- Kymenlaakso: KSS Energia/Kouvola, Haminan Energia.
- Pirkanmaa: Tampereen Energia/Sähkölaitos, Elenia.
- Northern/west coast wind areas: Fingrid plus local municipal energy companies and DSOs.

### 2.4 Traficom, NCSC-FI, and digital-infrastructure regulation

- **Traficom / NCSC-FI digital infrastructure, digital services and ICT services**: https://kyberturvallisuuskeskus.fi/en/our-activities/regulation-and-supervision/digital-infrastructure-digital-services-and-ict-services. Grade A. Use for NIS2/Cybersecurity Act context; the page says NCSC-FI at Traficom supervises the majority of digital infrastructure entities, digital service providers, managed service providers, managed security service providers, research organisations and public administration entities.
- **Register for Traficom's list of NIS2 entities**: https://kyberturvallisuuskeskus.fi/en/register-traficoms-list-nis-2-entities. Grade A for registration obligations; not necessarily public facility locations.
- **Traficom Cybersecurity Act news**: https://traficom.fi/en/news/cybersecurity-act-passed-parliament-obligations-under-nis-2-directive-enter-force-8-april-2025. Grade A.
- **Traficom telecom operator register**: https://traficom.fi/fi/yleispalveluyritykset/teletoimintarekisteri. Grade A for telecom-company leads; useful when a datacenter is tied to a telco/IXP, but not a datacenter register.

Use Traficom leads to validate legal/operator names, telecom ties, and critical-infrastructure context. Do not infer datacenter addresses from NIS2 registration alone.

---

## 3. Cloud and operator seed lists

### 3.1 Hyperscale cloud sources

| Provider | Official URL | Finland signal | Enumeration use |
|---|---|---|---|
| Microsoft Azure | https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies and https://learn.microsoft.com/en-us/azure/reliability/regions-list | Microsoft announces/builds a new datacenter region in Southern Finland; Microsoft Local confirms Finland community/project pages. | Seed Espoo, Kirkkonummi, Vihti, broader Uusimaa searches; confirm with municipal and YVA evidence. |
| Google | https://datacenters.google/locations/hamina-finland and https://cloud.google.com/about/locations | Official Google datacenter in Hamina; Google Cloud region list may not equal facility address. | Seed Hamina/Kymenlaakso, heat-recovery and expansion searches. |
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ and https://docs.aws.amazon.com/local-zones/latest/ug/available-local-zones.html | No Finnish AWS Region found in official region list; AWS Local Zone/edge references can seed Helsinki only. | Do not count as Finnish AWS datacenter without local permit/operator evidence. |
| Oracle OCI | https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm and https://www.oracle.com/cloud/public-cloud-regions/ | No Finnish OCI public cloud region found in official region list. | Use only as negative/nearest-region context unless a Finnish facility/operator page appears. |

### 3.2 Colo/operator official pages and pivots

Use operator pages as Grade A for owned/marketed facility existence, but still pivot to municipal/YVA evidence for expansions and new builds.

| Operator / investor | Official URL | High-yield municipalities/regions |
|---|---|---|
| Equinix | https://www.equinix.com/data-centers/europe-colocation/finland-colocation and Helsinki page https://www.equinix.com/data-centers/europe-colocation/finland-colocation/helsinki-data-centers | Helsinki, Espoo, Vantaa/Uusimaa. Facility pages include HE3/HE4/HE5/HE6/HE7 addresses. |
| Telia | https://www.telia.fi/business/data-center-services/data-center/helsinki-data-center | Helsinki Pitäjänmäki/Uusimaa. Search heat recovery, permit changes, expansion. |
| Elisa | https://elisa.com/carrierservices/Co-location_services_and_solutions/data-center-services/ | Finland and Estonia service page; pivot to Espoo, Turku/Raisio, Helsinki-area facilities through municipal/permit sources. |
| Digita Data Centers | https://datacenter.digita.fi/ and https://datacenter.digita.fi/our-data-centers/ | Pasila/Helsinki; strong connectivity/IXP lead. |
| Hetzner Finland | https://www.hetznerfinland.com/ and https://www.hetzner.com/pressroom/five-years-helsinki/ | Tuusula/Uusimaa; Data Center Park Helsinki. |
| Verne | https://www.verne.co/finland | Helsinki/Vantaa and Finnish campus services; also search Kajaani legacy/HPC ecosystem depending on current operator references. |
| atNorth | https://www.atnorth.com/nordic-data-centers/finland-data-centers/ | Helsinki-area sites; FIN02/FIN04 style facility names, capacity claims; verify with municipal permits. |
| Finnish Data Center Association | https://www.fdca.fi/ | Grade B+/A- association ecosystem lead; useful for member/operator discovery, not a complete official census. |
| Business Finland datacenters map | https://www.businessfinland.com/explore-business-opportunities/data-centers/map/ | Grade A-/B+ investment-promotion map; use as a seed list and confirm facilities with primary sources. |
| DayOne / Hyperco | https://dayonedc.com/market/finland and Hyperco-related YVA pages | Lahti/Päijät-Häme, Kouvola/Kymenlaakso, Nurmijärvi/Uusimaa leads; YVA/municipal documents are primary. |

Operator-pivot workflow:

1. Record exact official facility/campus name, address, city, and legal entity.
2. Search exact facility and entity names in the municipality domain, YVA pages, `julkipano.lupapiste.fi`, and council minutes.
3. Search `ytj.fi` / Finnish Patent and Registration Office business information when legal-entity identity matters: https://www.ytj.fi/ and https://www.prh.fi/.
4. For new announcements, require at least one of: YVA page, municipal zoning/permit page, land sale, council decision, environmental permit, or grid/energy agreement.

---

## 4. Per-region enumeration routing

Finland's repo divisions should be handled as regions and municipalities. For every region, first search `ymparisto.fi datakeskus "{maakunta}"`, then the largest municipalities, then local energy/grid names. The table below gives priority municipalities and special query pivots.

| Region / maakunta | Priority municipalities and known clusters | Official route | Query emphasis |
|---|---|---|---|
| Uusimaa | Helsinki, Espoo, Vantaa, Kirkkonummi, Vihti, Tuusula, Järvenpää, Nurmijärvi, Hanko/ports if cable/edge leads appear | Municipal planning/building control, Lupapiste notices, YVA, Fortum/Helen/Vantaa Energy, Fingrid, operator pages | Highest priority. Search Microsoft, Equinix, Telia, Elisa, Digita, Hetzner, Verne, atNorth, DayOne; `Hepokorpi`, `Kolabacken`, `Nummela`, `Pitäjänmäki`, `Pasila`, `Sinimäentie`, `Huurrekuja`. |
| Pirkanmaa | Tampere, Nokia, Ylöjärvi, Lempäälä, Pirkkala, Valkeakoski | Tampere/Nokia planning portals, Lupapiste, Tampereen Energia, Elenia, Fingrid | `Tampere datakeskus asemakaava`, `konesali`, `kaukolämpö`, `sähköasema`, industrial sites and AI/HPC announcements. |
| Päijät-Häme | Lahti, Hollola, Orimattila | Municipal planning, Lahti Energia, YVA, Business Finland/DayOne leads | `Lahti datakeskus`, `Lahti Energia hukkalämpö`, `DayOne Lahti`, `Hyperco`. |
| Kymenlaakso | Hamina, Kouvola, Kotka | Hamina/Kouvola planning, YVA, Haminan Energia, KSS Energia, port/fiber leads | Google Hamina official page; Kouvola Hyperco YVA; search `Ensontie`, `Koria`, `Hiivuri`, `hukkalämpö`. |
| Northern Ostrobothnia / Pohjois-Pohjanmaa | Oulu, Pyhäjoki, Raahe, Kalajoki, Ii | YVA, municipal planning, Fingrid wind/transmission corridors, Oulun Energia | High-growth power/wind area. Search `Pyhäjoen datakeskus`, `IT-teho`, `kokonaissähköteho`, `varavoimageneraattorit`, `400 kV`. |
| Lapland / Lappi | Rovaniemi, Kemi, Tornio, Kemijärvi, Sodankylä, Inari | Municipal planning, Lapland ELY/YVA, Fingrid north-south grid plans, industrial/energy sites | Use local Finnish plus Swedish/Northern names when relevant. Search `datakeskus Lappi`, `konesali Rovaniemi`, `sähköasema`, `tuulivoima`, `teollisuusalue`, `kantaverkko`. Treat cold-climate marketing as a lead only. |
| Southwest Finland / Varsinais-Suomi | Turku, Raisio, Salo, Kaarina, Naantali | Municipal planning, Turku/Raisio building control, local energy, port/cable infrastructure | Search Elisa/Raisio, `Turku datakeskus rakennuslupa`, `Salo datakeskus`, `kaukolämpö`. |
| Satakunta | Pori, Rauma, Harjavalta, Ulvila | Municipal planning, YVA, industrial energy/grid, port/industrial parks | Search `Pori datakeskus`, `Rauma datakeskus`, `sähköasema`, `teollisuuspuisto`, `hukkalämpö`. |
| Kanta-Häme | Hämeenlinna, Riihimäki, Forssa, Janakkala | Municipal planning, Elenia/Fingrid, industrial zones | Search `datakeskus Hämeenlinna`, `Riihimäki konesali`, `asemakaava datakeskus`. |
| South Karelia / Etelä-Karjala | Lappeenranta, Imatra | Municipal planning, LUT/industrial energy, local energy companies, Fingrid | Search `Lappeenranta datakeskus`, `Imatra datakeskus`, `hukkalämpö`, industrial redevelopments. |
| South Savo / Etelä-Savo | Mikkeli, Savonlinna, Pieksämäki | Municipal planning, local energy, YVA | Lower expected volume; query `konesali` and municipal agendas. |
| North Savo / Pohjois-Savo | Kuopio, Iisalmi, Varkaus | Municipal planning, Kuopion Energia, YVA | Search `Kuopio datakeskus`, `Varkaus teollisuusalue datakeskus`, `kaukolämpö`. |
| North Karelia / Pohjois-Karjala | Joensuu, Kontiolahti, Lieksa | Municipal planning, local energy, YVA | Search `Joensuu datakeskus`, `konesali`, `sähköasema`. |
| Central Finland / Keski-Suomi | Jyväskylä, Jämsä, Äänekoski | Municipal planning, Fingrid Lowlands/west-south routes, local energy | Search `Jyväskylä datakeskus`, `Jämsä datakeskus`, `sähköasema`, `kantaverkko`. |
| South Ostrobothnia / Etelä-Pohjanmaa | Seinäjoki, Kauhava, Kurikka, Alavus | YVA regional decisions, municipal planning, wind/grid corridors | Search `Seinäjoki datakeskus`, `Etelä-Pohjanmaa datakeskus`, `tuulivoima` plus `sähköasema`. |
| Ostrobothnia / Pohjanmaa | Vaasa, Mustasaari, Pietarsaari/Jakobstad, Närpes | Municipal planning, energy cluster, coastal wind/grid, YVA | Search `Vaasa datakeskus`, `Pohjanmaa datakeskus`, `serverhall`, Swedish variants `datacenter bygglov`. |
| Central Ostrobothnia / Keski-Pohjanmaa | Kokkola, Kannus, Kaustinen | YVA, municipal planning, industrial/port energy | Search `Kokkola datakeskus`, `teollisuuspuisto`, `sähköasema`, `hukkalämpö`. |
| Kainuu | Kajaani, Sotkamo, Kuhmo | Municipal planning, local energy, legacy HPC/datacenter ecosystem, YVA | Search `Kajaani datakeskus`, `konesali`, `entinen paperitehdas`, `HPC`, `kaukolämpö`. |
| Åland / Ahvenanmaa | Mariehamn, Jomala | Municipal/Åland planning, Swedish terms, local energy/telecom | Use Swedish first: `datacenter`, `serverhall`, `bygglov`, `detaljplan`, `fjärrvärme`, plus `Åland`. |

Note: Päijät-Häme is intentionally prominent because current market signals are strong around Lahti/DayOne.

---

## 5. Trade press and secondary validation

Use these as Grade B leads, then backfill with official pages:

- Data Center Dynamics: https://www.datacenterdynamics.com/; query `site:datacenterdynamics.com Finland data center Microsoft Google Hyperco DayOne`.
- Data Center Knowledge: https://www.datacenterknowledge.com/; useful for market trend and named project leads.
- Datacenter Forum: https://www.datacenter-forum.com/; Nordic/Finland project announcements and FDCA directory leads.
- Capacity Media, Telecoms.com, local Finnish business press (`Yle`, `Kauppalehti`, `Tekniikka & Talous`, `Rakennuslehti`) for land sales and council decisions.
- Business-wire/ResearchAndMarkets-style market reports are Grade C/B- for operator lists; use only as prompts for primary-source searches.
- Baxtel, DataCenters.com, DataCenterMap, OCOLO and similar directories are Grade C/B- depending on source disclosure; useful for address seeds, never sufficient alone for new-project enumeration.

Trade-to-official backfill query:

```
"{project name}" "asemakaava"
"{project name}" "YVA"
"{project name}" "rakennuslupa"
"{operator}" "{kunta}" site:ymparisto.fi
"{operator}" "{kunta}" site:{municipality-domain}
"{operator legal entity}" "Dnro"
```

---

## 6. Record schema and confidence rules

For each candidate facility/project, capture:

- country/region/municipality and exact address or parcel;
- project/facility name and operator/applicant/SPV;
- source type: operator page, municipal zoning, building permit, YVA, grid/energy, Traficom/NIS2, trade press;
- status: operating, under construction, permitted, zoning approved, YVA, announced/land option;
- dates: zoning approval/legal force, permit decision, YVA status date, construction start, operation date;
- capacity fields: IT MW, total electrical MW/MVA, backup-generator fuel MW, building count, land hectares, gross floor area;
- power/heat fields: substation, voltage, DSO/TSO, district-heating partner, heat-recovery capacity if disclosed;
- primary-source URL and archived/source title.

Confidence grading:

- **A**: municipal permit/decision, `ymparisto.fi` YVA, Fingrid/government/regulator page, official operator facility page.
- **B**: FDCA/Business Finland map, credible trade press with named operator/site, contractor case study with location/capacity.
- **C**: directory listing, market-report excerpt, LinkedIn/social post, unsourced blog.

Counting rules:

- Count operating facilities from official operator pages even if building permits are old/non-public.
- Count planned projects only when an official planning/YVA/land/permit source identifies municipality and project owner, or when a hyperscaler/operator official page is backed by municipal geography.
- Do not count a cloud region as multiple facilities unless official/local permits identify the separate sites.
- Do not count grid queue, energy-site marketing, or Business Finland land/site listings as datacenter projects without an operator or permit/YVA record.
