# NL Explorer Official - Netherlands Datacenter Enumeration via Permits, Grid, Cloud Regions, Colo Operators

Date: 2026-08-12. Scope: Netherlands, Kingdom of the (NL), including the European Netherlands provinces plus Aruba, Bonaire, Saba, Sint Eustatius, Curacao, and Sint Maarten as listed in `world-manifest.jsonl`. Focus angle: official/regulatory/cloud methodology for enumerating datacenter facilities and projects. Reliability grades: **A** = official/primary source, **B** = strong secondary/trade/association source, **C** = weak/aggregate/unverified.

---

## 0. Structural facts that shape Netherlands enumeration

- The Netherlands has no single public national datacenter facility register. Build the census by joining **Officiele Bekendmakingen permit notices**, **Omgevingsloket/DSO process clues**, **provincial and municipal spatial rules**, **omgevingsdienst environmental files**, **TenneT / regional grid evidence**, **ACM cloud and electricity-market materials**, and **official cloud/colo operator pages**.
- Since the **Omgevingswet** entered into force on 2024-01-01, new permits and environmental permissions are usually framed as **omgevingsvergunning**, **omgevingsplanactiviteit**, **bouwactiviteit**, and **milieubelastende activiteit**. Older records use **Wabo**, **bestemmingsplan**, **bouwvergunning**, and **milieuvergunning**.
- For project discovery, the strongest national source is **Officiele Bekendmakingen** (`zoek.officielebekendmakingen.nl`) because municipalities, provinces, water boards, and environmental agencies publish received applications, draft decisions, granted permits, amendments, and policy notices there. Example official hits include Lelystad/Flevokusthaven received application, Alphen aan den Rijn/Boerhaaveweg application, EdgeConneX AMS10 Schiphol-Rijk phase 2 granted permit, FalconConnect Amsterdam permit amendment, and Iron Mountain Haarlem granted environmental/building permit.
- Datacenters are often permitted by **province-backed environmental agencies** rather than only by the municipality in North Holland. The key body is **Omgevingsdienst Noordzeekanaalgebied (OD NZKG)**, which states that it grants building and environmental permits for datacenters in North Holland and supervises them; smaller datacenters usually fall under municipalities.
- Hyperscale projects have a separate national spatial-policy constraint. Official instruments under the **Besluit kwaliteit leefomgeving (Bkl)** and related government publications define hyperscale datacenters as very large facilities and restrict new hyperscale siting nationally, with exceptions around parts of **Het Hogeland (Groningen)** and **Hollands Kroon (North Holland)**. Treat non-exception hyperscale proposals as legally high-risk unless there is pre-2022/vested permit evidence.
- Grid capacity is a primary filter. TenneT is the national high-voltage grid operator in the Netherlands; regional grid operators such as Liander, Stedin, Enexis, Rendo, Westland Infra, and Coteq often publish capacity maps and congestion pages. North Holland, Haarlemmermeer/Schiphol, Amsterdam, Hollands Kroon/Middenmeer, and Groningen/Eemshaven require explicit grid-capacity validation.
- Official cloud region pages give city/region-level seeds but not buildings. Microsoft Azure has **West Europe = Netherlands**. Google Cloud has **europe-west4 = Eemshaven, Netherlands** and official Google datacenter locations at **Eemshaven**, **Middenmeer**, and **Winschoten**. Use cloud regions as seed records, then pivot to permits, grid, and operator evidence before counting facilities.
- The Dutch commercial market is highly clustered around **Amsterdam/Schiphol/Haarlemmermeer**, **Haarlem**, **Middenmeer/Hollands Kroon**, **Eemshaven/Het Hogeland**, **Almere/Lelystad/Flevoland**, **Rotterdam/Delft**, **Eindhoven**, and selected regional NorthC/telco locations.

Key lifecycle vocabulary:

`locatieonderzoek` < `vooraankondiging` / `ontvangen aanvraag` < `ontwerpbesluit` / `ter inzage` < `zienswijze` < `vergunning verleend` < `bezwaar` / `beroep` < `onherroepelijk` < `start bouw` < `in gebruik genomen` / `operationeel` < `wijziging vergunning` / `uitbreiding`

Only count `vergunning verleend`, `onherroepelijk`, `start bouw`, or stronger as permit/construction evidence. Treat `ontvangen aanvraag`, policy capacity, or cloud-region presence as a lead until cross-checked.

---

## 1. Dutch and English query patterns

### 1.1 Core Dutch search terms

Use Dutch first for official records.

```text
datacenter
data center
datacentrum
rekencentrum
cloudregio OR cloud regio
colo OR colocatie
hyperscale datacenter OR hyperscale datacentrum
omgevingsvergunning datacenter
ontvangen aanvraag omgevingsvergunning datacenter
vergunning verleend datacenter
ontwerpbesluit datacenter
milieubelastende activiteit datacentrum
omgevingsplan datacenter
omgevingsplanactiviteit datacenter
buitenplanse omgevingsplanactiviteit datacenter OR BOPA datacenter
bestemmingsplan datacenter
parapluplan datacenters
omgevingsverordening datacenter
ontwikkelruimte datacenters
netcongestie datacenter
netaansluiting datacenter
aansluitvermogen datacenter
transportcapaciteit datacenter
hoogspanningsstation datacenter
koelwater datacenter
warmtevracht datacenter
restwarmte datacenter OR restwarmte datacentrum
noodstroomaggregaten datacenter
dieselgeneratoren datacenter
```

### 1.2 Official permit and planning queries

Substitute `{province}`, `{municipality}`, `{operator}`, `{address}`, `{site}`, and `{zaaknummer}`.

```text
site:zoek.officielebekendmakingen.nl datacenter omgevingsvergunning
site:zoek.officielebekendmakingen.nl datacentrum omgevingsvergunning
site:zoek.officielebekendmakingen.nl "het oprichten van een datacenter"
site:zoek.officielebekendmakingen.nl "het realiseren van een datacenter"
site:zoek.officielebekendmakingen.nl "vergunning verleend" "datacenter"
site:zoek.officielebekendmakingen.nl "ontwerpbesluit" "datacenter"
site:zoek.officielebekendmakingen.nl "{operator}" "datacenter"
site:zoek.officielebekendmakingen.nl "{address}" "datacenter"
site:lokaleregelgeving.overheid.nl datacenterbeleid
site:lokaleregelgeving.overheid.nl "parapluplan datacenters"
site:ruimtelijkeplannen.nl datacenter
site:omgevingswet.overheid.nl datacenter omgevingsplan
site:{municipality-domain} datacenter omgevingsvergunning
site:{municipality-domain} datacenter bestemmingsplan
site:{province-domain} datacenter omgevingsverordening
```

### 1.3 Energy, grid, and environmental queries

```text
site:tennet.eu datacenter netaansluiting Nederland
site:tennet.eu "datacenter" "transportcapaciteit"
site:tennet.eu "Noord-Holland" "netcongestie"
site:acm.nl TenneT investeringsplan net op land datacenter
site:acm.nl "transportcapaciteit" "datacenter"
site:liander.nl datacenter netcongestie
site:stedin.net datacenter netcongestie
site:enexis.nl datacenter netcongestie
site:odnzkg.nl datacenter omgevingsvergunning
site:iplo.nl datacentrum milieubelastende activiteit
"{municipality}" "datacenter" "hoogspanningsstation"
"{operator}" "{municipality}" "aansluitvermogen"
"{operator}" "{municipality}" "restwarmte"
"{operator}" "{municipality}" "koelwater"
"{operator}" "{municipality}" "noodstroomaggregaten"
```

### 1.4 English discovery patterns

```text
"Netherlands" "data center" "environmental permit"
"Netherlands" "data center" "building permit"
"Amsterdam" "data center" "omgevingsvergunning"
"Haarlemmermeer" "data center" "available development capacity"
"North Holland" "data center" "grid congestion"
"TenneT" "data center" "grid connection" Netherlands
"Google" "Eemshaven" "data center"
"Google" "Middenmeer" "data center"
"Azure" "West Europe" "Netherlands"
"Digital Realty" "Amsterdam" "AMS" "Netherlands"
```

---

## 2. Official/regulatory source backbone

### 2.1 Officiele Bekendmakingen and open government notices

Primary portal: https://zoek.officielebekendmakingen.nl/. Grade A.

Use it as the national first-pass permit search. It exposes `Gemeenteblad`, `Provinciaal blad`, `Waterschapsblad`, `Staatscourant`, parliamentary records, and PDFs. Search the HTML and PDF forms because attachments can contain richer permit text.

High-value official examples:

- Lelystad/Flevokusthaven: `Gemeenteblad 2025, 534713`, received application for an omgevingsvergunning for establishing a datacenter at Flevokusthaven Lelystad. Grade A lead.
- Alphen aan den Rijn/Boerhaaveweg 10: `Gemeenteblad 2026, 135103`, received omgevingsvergunning application for realizing a datacenter. Grade A lead.
- Schiphol-Rijk/Koolhovenlaan 142: `Provinciaal blad 2026, 11662`, OD NZKG granted building activity permit phase 2 to EdgeConneX AMS10 B.V. Grade A permitted evidence.
- Haarlem/J.W. Lucasweg 35: `Provinciaal blad 2025, 5574` PDF and related `Provinciaal blad 2025, 2141`, OD NZKG granted/issued draft permit for Iron Mountain (Nederland) Data Centre B.V. to establish and operate the Haarlem datacenter. Grade A permitted evidence.
- Amsterdam/Plimsollweg 3, 13, 23: `Provinciaal blad 2025, 12791`, granted amendment to FalconConnect B.V. permit for a datacenter. Grade A expansion/amendment evidence.
- Haarlemmermeer development room: `Gemeenteblad 2025, 30669` PDF, official notice of available datacenter development capacity under the municipality's datacenter policy. Grade A planning-capacity context.

Extraction fields:

- `publication_type` (`Gemeenteblad`, `Provinciaal blad`, etc.);
- `publication_number` and date;
- `authority` and `omgevingsdienst`;
- `applicant` / `aanvrager`;
- `zaaknummer`, `OLO-nummer`, `DSO-nummer`, `kenmerk`;
- `address`, cadastral parcel, municipality, province;
- activity text (`bouwen`, `milieu`, `uitweg`, `strijdig gebruik`, `omgevingsplanactiviteit`);
- status (`ontvangen aanvraag`, `ontwerpbesluit`, `verleend`, `geweigerd`, `wijziging`, `bezwaar`);
- inspection window, appeal deadline, and whether `MER`/`m.e.r.-beoordeling` is required.

### 2.2 Omgevingsloket, IPLO, DSO, and environmental rules

Official process sources:

- Omgevingsloket / DSO: https://omgevingswet.overheid.nl/. Grade A for current permit workflow and permit-check logic.
- Technical building permit submission guidance: https://omgevingswet.overheid.nl/helpcentrum/aanvragen-melden/indienen-technische-bouwvergunning. Grade A process source.
- IPLO datacenter environmental activity page: https://iplo.nl/regelgeving/regels-voor-activiteiten/milieubelastende-activiteiten-hoofdstuk-3-bal/dienstverlening/datacentrum/. Grade A. It identifies `milieubelastende activiteit datacentrum` under Bal paragraph 3.7.3 and notes that an omgevingsvergunning is required when cooling-water discharge has a heat load above 50 MW to surface water; related Bal rules can apply to supporting activities.
- IPLO Omgevingswet business transition page: https://iplo.nl/regelgeving/regels-voor-activiteiten/overgangsrecht/omgevingswet-betekent-bedrijven/. Grade A for interpreting pre-2024 permits.

Use IPLO to classify permit types. A datacenter application may not need a single "datacenter permit" if it is split into:

- technical building activity;
- environmental activity;
- water discharge permit or notification;
- outside-plan activity / zoning deviation;
- backup generators, fuel tanks, batteries, ammonia cooling, or transformer infrastructure;
- demolition, tree removal, driveway/road access, and fire-safety activities.

### 2.3 National hyperscale spatial rules

Official sources:

- Staatsblad 2023, 492: https://zoek.officielebekendmakingen.nl/stb-2023-492.html. Grade A. This establishes national rules for hyperscale datacenter siting through the Barro/Bkl transition.
- Bkl consolidated text at IPLO: https://iplo.nl/publish/pages/191119/besluit-kwaliteit-leefomgeving-tekst-bij-inwerkingtreding-.pdf. Grade A.
- Staatscourant 2022, 5276: https://zoek.officielebekendmakingen.nl/stcrt-2022-5276.pdf. Grade A for the temporary/preparatory prohibition context.
- Parliamentary explanation around thresholds and exception areas: https://zoek.officielebekendmakingen.nl/kst-32813-AO.html and https://zoek.officielebekendmakingen.nl/h-tk-20252026-35-3.html. Grade A policy context.

Operational rule:

- Treat `>10 hectares` and `>=70 MW aansluitvermogen` as the hyperscale threshold to test in Dutch sources.
- For new hyperscale proposals outside the named exception areas, require extra scrutiny: check the application date relative to 2022-02-16, existing permit rights, Bkl exception, and municipal/provincial plan conformity.
- Do not discard smaller colocation or enterprise datacenters under this rule; the national hyperscale restriction is not a general datacenter ban.

### 2.4 Provincial and municipal planning sources

Primary national planning/legal portals:

- Local regulations: https://lokaleregelgeving.overheid.nl/. Grade A. Use for municipal `Datacenterbeleid`, `parapluplan datacenters`, and provincial `Omgevingsverordening`.
- Spatial plans archive: https://www.ruimtelijkeplannen.nl/. Grade A for pre-Omgevingswet `bestemmingsplan`, `parapluplan`, and plan rules.
- Current Omgevingsloket plan viewer route: https://omgevingswet.overheid.nl/regels-op-de-kaart/. Grade A for omgevingsplan rules.

Important official policy examples:

- Haarlemmermeer datacenter policy: https://lokaleregelgeving.overheid.nl/CVDR646404. Grade A. It states that Haarlemmermeer maintains an overview of available development room and that datacenter policy is being legally embedded through planning instruments.
- Noord-Holland datacenter strategy / Omgevingsverordening materials: https://www.noord-holland.nl/ and related official PDFs. Grade A. Use for clustering/instruction rules in Amsterdam/Haarlemmermeer/Hollands Kroon and for unused plan-capacity restrictions through 2026.
- OD NZKG datacenter dossier: https://odnzkg.nl/aandachtsdossiers/datacenters/. Grade A. Use as the North Holland environmental and building-permit hub.

Per project, search both the policy instrument and the permit notice. A plan that allows datacenters is not itself a facility; it becomes a facility record only after an operator, address, permit, construction, or operational source is attached.

### 2.5 TenneT, regional grid operators, and ACM

Grid sources:

- TenneT main site: https://www.tennet.eu/. Grade A for high-voltage operator identity, investment plans, project pages, and congestion publications.
- TenneT / RVO North Holland North 380 kV expansion materials: example RVO PDF `380 kV-Netuitbreiding Noord-Holland Noord | Notitie Nut en Noodzaak`, https://www.rvo.nl/sites/default/files/2025-10/Notitie-nut-en-noodzaak-%28oktober-2025%29-380-kV-Netuitbreiding-Noord-Holland-Noord.pdf. Grade A for grid-capacity context around North Holland.
- ACM TenneT investment-plan review letters, e.g. `Eindbrief toetsing investeringsplan TenneT net op land 2026`: https://www.acm.nl/system/files/documents/eindbrief-toetsing-investeringsplan-tennet-net-op-land-2026.pdf. Grade A for regulatory review of grid investment plans.
- Liander regional capacity pages, e.g. https://www.liander.nl/grootzakelijk/capaciteit-op-het-net/capaciteit-per-regio/tennet. Grade A for distribution-grid constraints; the page notes TenneT reached maximum delivery capacity in North Holland.
- Stedin congestion pages, e.g. https://www.stedin.net/zakelijk/energietransitie/beschikbare-netcapaciteit/congestie-en-congestiemanagement/provincie-noord-holland. Grade A for regional distribution constraints.
- Enexis capacity pages: https://www.enexis.nl/zakelijk/duurzaam-bezig/capaciteit-op-het-net. Grade A for southern/eastern provinces.

ACM sources:

- ACM cloud services market study: https://www.acm.nl/en/publications/market-study-cloud-services. Grade A policy/market source, not facility-level.
- ACM Data Act authority note: https://www.acm.nl/en/publications/acm-now-authorized-enforce-data-act. Grade A for cloud-service regulatory context.
- ACM cloud/DMA cooperation and provisional cloud-gatekeeper publications: https://www.acm.nl/en/publications/acm-collaborates-european-commission-market-investigation-cloud-services and https://www.acm.nl/en/publications/european-commissions-provisional-position-market-investigation-acm-microsoft-and-amazon-cloud-services-fall-under-dma. Grade A for market oversight; not a datacenter list.

Grid extraction cautions:

- Keep `aansluitvermogen`, `transportcapaciteit`, `gecontracteerd vermogen`, `netcongestie`, `hoogspanningsstation`, `transformatorvermogen`, and `IT load` as separate fields.
- A grid-connection dispute or waitlist is evidence of a project lead, but not proof of construction.
- For large North Holland and Groningen/Eemshaven projects, absence of grid capacity may explain stalled status even where plan or permit evidence exists.

---

## 3. Official cloud-region and operator seed lists

### 3.1 Hyperscaler cloud and datacenter seeds

| Provider | Netherlands signal | Official source | Reliability |
|---|---|---|---|
| Microsoft Azure | `West Europe`, physical location Netherlands, availability-zone region | https://learn.microsoft.com/en-us/azure/reliability/regions-list and https://datacenters.microsoft.com/globe/explore/?info=region_westeurope | A for region/country; not facility-level |
| Google Cloud | `europe-west4`, Netherlands; GPU/TPU docs expose Eemshaven zones and De Kooy AI zone | https://cloud.google.com/about/locations and https://docs.cloud.google.com/compute/docs/regions-zones | A for cloud-region/city; not every facility |
| Google datacenter locations | Eemshaven, Middenmeer, and Winschoten official datacenter-location pages | https://datacenters.google/locations/eemshaven-netherlands-var, https://datacenters.google/locations/middenmeer-netherlands, and https://datacenters.google/locations/winschoten/ | A for facility/campus city; exact parcel still needs permit cross-check |
| AWS | No public Netherlands AWS region as of this research; use Direct Connect/on-ramp pages only for network presence | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ and AWS Direct Connect locations | A for absence/presence in official region list; not a Dutch facility list |
| Oracle Cloud / IBM / other clouds | Check current official region/location tables; Netherlands may appear as interconnect/on-ramp rather than full region | vendor official docs | A for vendor-stated cloud presence; C for inferred building |

Extraction rule: create a cloud seed record only at the geography stated by the official source. For Azure `West Europe`, use `Netherlands` and pivot to Amsterdam/Schiphol/Haarlemmermeer/Middenmeer only if permit/operator evidence supports it. For Google `europe-west4`, use Eemshaven/Het Hogeland and Google official datacenter pages, then validate with Groningen municipal/provincial planning and TenneT grid material.

### 3.2 Colocation/operator official seeds

Official operator pages are Grade A for operator-stated facility existence and broad location, but use permits and official notices for construction status, legal applicant, and expansions.

| Operator | Official source | Netherlands facility seeds / notes |
|---|---|---|
| Equinix | https://www.equinix.com/data-centers/europe-colocation/netherlands-colocation and https://www.equinix.com/data-centers/europe-colocation/netherlands-colocation/amsterdam-data-centers | Amsterdam metro / AM-series IBX facilities. Search AM3, AM4, AM5, AM7, AM11 and Science Park / Schepenbergweg / Lemelerbergweg addresses in official permits. |
| Digital Realty / Interxion | https://www.digitalrealty.com/data-centers/emea/amsterdam | Official page states 12 Amsterdam data centers and direct access to AMS-IX, NL-IX, and DE-CIX. Search AMS1-AMS18 style facility pages, Science Park, Cessnalaan, Pudongweg, Amsterdam Data Tower, and Interxion legacy names. |
| NorthC | https://www.northcdatacenters.com/en/northc-datacenters/ | Official locations include Aalsmeer, Almere, Amsterdam, Amsterdam 2, Oude Meer, Delft, Rotterdam Waalhaven, Rotterdam Zestienhoven, Eindhoven 1/2, Groningen, Nieuwegein, and others depending current page. Use exact addresses from official location pages. |
| Iron Mountain | https://www.ironmountain.com/data-centers/locations/amsterdam-data-center | AMS-1 at J.W. Lucasweg 35, Haarlem; official page states current and planned power/campus buildout. Cross-check with OD NZKG/Provinciaal blad permits. |
| EdgeConneX | https://www.edgeconnex.com/locations/europe/amsterdam/ | Amsterdam/Schiphol-Rijk campus seeds; official permit notices identify AMS10 B.V. and Koolhovenlaan 142. |
| NTT Global Data Centers | https://services.global.ntt/en/services/global-data-centers | Check Amsterdam facility pages and operator legal names; verify against local permits. |
| CyrusOne / Colt DCS / Global Switch / Switch Datacenters / QTS/Goodman-style developers | Official operator/developer pages plus permit notices | Treat as leads until official Dutch permit or operational page confirms address/status. |
| Dutch Datacenter Association members | https://www.dutchdatacenters.nl/en/ | Grade B+ association lead list. Useful for identifying operators, but facility-level claims still need official/operator validation. |

Operator pivot queries:

```text
"Equinix" ("AM3" OR "AM4" OR "AM11") "Amsterdam" "omgevingsvergunning"
"Digital Realty" ("AMS9" OR "AMS17" OR "Science Park") "omgevingsvergunning"
"Interxion" "Amsterdam" "datacenter" "vergunning"
"NorthC" "{location}" "datacenter" "omgevingsvergunning"
"Iron Mountain" "J.W. Lucasweg 35" "omgevingsvergunning"
"EdgeConneX" "Koolhovenlaan 142" "omgevingsvergunning"
"FalconConnect" "Plimsollweg" "datacenter"
"Google" "Middenmeer" "omgevingsvergunning"
"Google" "Eemshaven" "datacenter" "bestemmingsplan"
"Microsoft" "Middenmeer" "datacenter" "vergunning"
```

---

## 4. Per-division enumeration workflow

Use the manifest divisions as the top-level sweep units, but in the European Netherlands the operational unit is usually the **municipality** and sometimes the **omgevingsdienst**. For the Caribbean countries/special municipalities, use local government planning and telecom/cloud-edge sources; do not assume European Netherlands portals cover them.

### 4.1 European Netherlands province routing

| Division | First official route | Second route | Notes |
|---|---|---|---|
| North Holland | Officiele Bekendmakingen + OD NZKG + Noord-Holland Omgevingsverordening | Amsterdam, Haarlemmermeer, Hollands Kroon, Haarlem, Aalsmeer, Oude Meer municipal policies; Liander/Stedin/TenneT | Highest priority. Search Amsterdam/Schiphol-Rijk/Haarlemmermeer, Haarlem, Middenmeer, Oude Meer, Science Park, Plimsollweg, Koolhovenlaan, J.W. Lucasweg. |
| Groningen | Het Hogeland/Eemshaven municipal planning + Groningen province + TenneT/RVO grid expansion | Google official Eemshaven pages, local water/port authority | Hyperscale exception area around Het Hogeland; search Eemshaven, Eemsdelta, Het Hogeland, Groningen Seaports, TenneT stations. |
| Flevoland | Lelystad and Almere municipal notices + province | Flevokusthaven, Almere NorthC, Liander/TenneT | Search Flevokusthaven application and any "fourth cluster" policy references. |
| South Holland | Rotterdam, Delft, The Hague, Alphen aan den Rijn, Westland municipal notices | Stedin/Westland Infra, port/industrial heat networks | Search NorthC Delft/Rotterdam, Boerhaaveweg 10 Alphen, Rotterdam Waalhaven/Zestienhoven. |
| North Brabant | Eindhoven, Tilburg, Breda, Den Bosch, High Tech Campus | Enexis, Brabantse omgevingsdiensten | Search NorthC Eindhoven, HTC, ASML/supplier campuses, `rekencentrum`. |
| Utrecht | Nieuwegein, Utrecht, Amersfoort municipal notices | Stedin/Liander; provincial omgevingsverordening | Search NorthC Nieuwegein and enterprise/telco facilities. |
| Gelderland | Arnhem/Nijmegen/Apeldoorn/Ede municipal notices | Liander/TenneT | Lower density but important grid and government/enterprise facilities. |
| Overijssel | Zwolle/Enschede/Deventer municipal notices | Enexis/Coteq/Rendo | Search regional colo, university/HPC, and telco sites. |
| Friesland | Leeuwarden/Heerenveen municipal notices | Liander/TenneT | Lower density; include water/energy and provincial planning terms. |
| Drenthe | Assen/Emmen municipal notices | Enexis/Rendo | Lower density; search industrial parks and government ICT. |
| Limburg | Maastricht/Venlo/Heerlen/Sittard-Geleen | Enexis/TenneT | Search cross-border colo/enterprise and logistics parks. |
| Zeeland | Middelburg/Vlissingen/Terneuzen industrial sites | Stedin/Enduris/TDTR capacity context | Search port/industrial-energy sites; distinguish industrial electrification from datacenters. |

### 4.2 Caribbean divisions

| Division | Route | Notes |
|---|---|---|
| Aruba | Government of Aruba planning/building permit pages, telecom operators, local utility | Search `datacenter Aruba`, `data center Aruba`, `bouwvergunning datacenter`, `SETAR`, `Digicel`, `WEB Aruba`. |
| Curacao | Government of Curacao permitting, telecom/utility operators | Search `datacenter Curacao`, `data center Curacao`, `vergunning datacenter`, `Blue NAP`, `Curoil/utility` where relevant. |
| Sint Maarten | Government of Sint Maarten planning permits, telecom operators | Search `data center Sint Maarten`, `datacenter Sint Maarten`, `building permit data center`. |
| Bonaire | Rijksdienst Caribisch Nederland / openbaar lichaam Bonaire permits, telecom/utility | Search `datacenter Bonaire`, `omgevingsvergunning Bonaire datacenter`, `TELBO`, `WEB Bonaire`. |
| Saba | Openbaar lichaam Saba planning/building permits and telecom | Likely edge/server-room scale; require facility-grade evidence before counting. |
| Sint Eustatius | Openbaar lichaam Sint Eustatius planning/building permits and telecom | Likely edge/server-room scale; require facility-grade evidence before counting. |

### 4.3 Step-by-step enumeration loop

1. **National notice sweep**: run Officiele Bekendmakingen queries for `datacenter`, `datacentrum`, `rekencentrum`, and named operators. Export publication URL, authority, status, applicant, address, and dates.
2. **Province filter**: assign each hit to province/division and check provincial omgevingsverordening or municipal datacenter policy for allowed/blocked siting.
3. **Municipality drill-down**: search municipality pages, council information systems (`raadsinformatie`, `RIS`, `besluitenlijst`, `collegebesluit`), and plan viewers for the address/operator.
4. **Omgevingsdienst/environment drill-down**: especially in North Holland, search OD NZKG and other regional environmental services for draft decisions, final permits, generator/cooling/water files, and MER determinations.
5. **Grid validation**: query TenneT, ACM investment-plan materials, Liander/Stedin/Enexis capacity pages, and local council minutes for `netaansluiting`, `transportcapaciteit`, `hoogspanningsstation`, and congestion.
6. **Cloud/operator reconciliation**: join official Azure/GCP/Google datacenter pages and operator location pages to the permit list. Avoid inferring exact facilities from cloud regions alone.
7. **Status and capacity normalization**: store permit status, operational status, gross floor area, campus area, grid MW/MVA, IT MW, generator capacity, water/heat discharge, and waste-heat commitments separately.

---

## 5. Evidence hierarchy and extraction rules

### 5.1 Reliability hierarchy

| Source | Grade | Use |
|---|---:|---|
| Officiele Bekendmakingen permit notices and PDFs | A | Application, draft/final decision, applicant, address, official status, appeal window. |
| Omgevingsloket / IPLO / Bkl / Staatsblad / Staatscourant | A | Legal categories, permit process, hyperscale restrictions, environmental triggers. |
| Provincial/municipal omgevingsverordening, datacenter policy, plan viewer | A | Allowed areas, excluded areas, development capacity, zoning/planning status. |
| Omgevingsdienst files, especially OD NZKG | A | Environmental/building permits, MER decisions, supervision, technical attachments. |
| TenneT, ACM investment-plan reviews, regional grid-operator capacity pages | A | Grid capacity/congestion context and connection constraints; rarely facility-complete. |
| Official cloud-region pages | A for region/country/city, C for exact facility | Seed cloud demand and rough geography; exact buildings hidden. |
| Official operator location pages | A- for active facility/location, B for capacity | Operator-stated sites and capacities; verify expansions with permits. |
| Dutch Datacenter Association | B+ | Operator/member leads; not a full official facility register. |
| Trade press, legal updates, local newspapers | B | Discovery and narrative; verify with official filings. |
| Generic DC maps, broker listings, forums, social media | C | Lead generation only. |

### 5.2 Status model

Use these lifecycle labels:

- `lead`: only cloud/operator/trade signal, no Dutch permit or local official evidence.
- `policy-enabled`: municipal/provincial plan or datacenter development room exists, but no named facility.
- `application-received`: `ontvangen aanvraag` notice exists.
- `under-review`: draft decision, consultation, MER review, or `ter inzage`.
- `permitted`: `vergunning verleend` or equivalent final decision.
- `appealed/contested`: objection/court/grid dispute affects status.
- `grid-constrained`: permit or project exists but TenneT/regional operator capacity blocks or delays connection.
- `under-construction`: permit plus works announcement, tender, contractor notice, or official construction start.
- `operational`: operator page, cloud availability, inspection/supervision record, or official commissioning.
- `expansion/amendment`: amendment to existing permit or new phase/building.

### 5.3 Capacity fields to keep separate

- `site_area_ha`: relevant for hyperscale threshold and zoning.
- `gross_floor_area_m2`: permit/operator building area.
- `white_space_m2` or `colo_space_m2`: operator-stated technical/customer space.
- `aansluitvermogen_mw_mva`: grid connection power; do not treat as IT load.
- `transportcapaciteit_mw_mva`: grid transport rights/capacity; can be constrained.
- `it_load_mw`: only when explicitly labeled IT power/load.
- `generator_mw`: backup generation, often found in environmental permits.
- `cooling_water_heat_load_mw`: important because IPLO/Bal permit trigger mentions cooling-water discharge above 50 MW heat load to surface water.
- `restwarmte_mw`: waste-heat recovery commitment; not facility load.

### 5.4 Count rules

- Count a specific address/operator as one facility unless official documents clearly split independent campuses or phases.
- For Equinix/Digital Realty AM-series facilities, use operator IDs as facility IDs, then verify addresses and expansions with Dutch permit notices.
- For Google/Microsoft hyperscale campuses, count official datacenter campuses and permitted buildings/phases separately only when permit/project documents support the split.
- Do not count a cloud region (`West Europe`, `europe-west4`) as a facility. It is a seed that must be reconciled to official datacenter/campus or permit evidence.
- Do not count a municipal "development room" notice as a project without a named operator/address/application.
