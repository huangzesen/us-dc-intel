# DK Explorer Industry - Denmark Datacenter Discovery

Date: 2026-08-12. Scope: Denmark (DK). Repo divisions: North Denmark; Central Denmark; South Denmark; Region Zealand; Capital Region.

Purpose: discover Danish data-center leads from operators, industry associations, cloud providers, trade press, construction news, IXPs, subsea cable sources, and market directories. Reconcile every countable facility with the official methodology in `explorer-official.md`.

## Reliability Grades

Grades attach to the specific fact cited.

- Grade A: operator-owned facility page, official hyperscaler cloud-region page/newsroom, official association/company page for its own membership or statement, official IXP/operator page, or any official source also accepted by `explorer-official.md`.
- Grade B: credible trade press, investment-promotion case, stock-exchange/company release, construction contractor news, or association news with named operator, place, date, and project status.
- Grade C: directories, market reports, consultant lists, PeeringDB/user-maintained entries, aggregator maps, social posts, and unsourced local mentions. Leads only.
- Grade U: unverified, blocked, not reachable, or not enough evidence to use.

Industry evidence is a discovery layer. A Grade A operator page can justify that the operator markets a facility or region, but municipal permits, exact building status, grid capacity, and environmental approvals must come from official records unless the operator itself publishes the relevant primary detail.

## 0. Market Structure

### 0.1 National Association

Danish Data Center Industry (DDI) is the main national industry body.

- Home: https://www.datacenterindustrien.dk/ (A for association existence and own statements).
- Members: https://www.datacenterindustrien.dk/members (A for DDI-listed member status; not a facility census).
- Knowledge hub/market reports: https://www.datacenterindustrien.dk/knowledge-hub (B for sector estimates unless backed by named primary sources).
- Microsoft West Denmark DDI item: https://www.datacenterindustrien.dk/historic-investment-lands-in-west-denmark-as-microsoft-announces-new-datacenter-region (B; cites Microsoft announcement and names Esbjerg/Varde).
- Grid-capacity advocacy/news: treat as B unless backed by Energinet/Forsyningstilsynet primary documents.

### 0.2 Energy and ICT Associations

- Green Power Denmark: https://greenpowerdenmark.dk/ (A for own statements; B for market commentary). Example data-center article: https://greenpowerdenmark.dk/nyheder/dansk-energi-datacentre-danmark-er-godt-klimaet.
- IT-Branchen: https://www.itb.dk/ (A for association existence and own statements).
- Dansk Industri / DI Digital: https://www.di.dk/ (A for own statements).

### 0.3 Trade Press

Use trade press as B-grade evidence when it names operator, location, date, and status. Avoid paywalled snippets as sole evidence for exact capacities.

- Computerworld Danmark: https://www.computerworld.dk/ (B). Useful for Microsoft Denmark East locations and Danish grid constraints.
- Version2: https://www.version2.dk/ (B).
- ITWatch: https://www.itwatch.dk/ (B).
- EnergyWatch: https://energywatch.dk/ (B).
- Ingenioren: https://ing.dk/ (B).
- Borsen: https://borsen.dk/ and Finans: https://finans.dk/ (B).
- Data Center Dynamics: https://www.datacenterdynamics.com/ (B).
- DataCenterKnowledge: https://www.datacenterknowledge.com/ (B).
- DataCenterForum: https://www.datacenter-forum.com/ (B/C depending on sourcing).

### 0.4 Directories and Aggregators

These are useful for lead generation, not final counts.

- Data Center Map Denmark: https://www.datacentermap.com/denmark/ and Copenhagen: https://www.datacentermap.com/denmark/copenhagen/ (C).
- Data Center Map examples: GlobalConnect Taastrup https://www.datacentermap.com/denmark/copenhagen/global-connect-taastrup/ and Apple Tjele https://www.datacentermap.com/denmark/viborg/apple-tjele-data-center/ (C).
- Baxtel: https://baxtel.com/ (C).
- DatacenterHawk: https://datacenterhawk.com/ (C).
- DCSP Copenhagen: https://dcselectionpartners.com/data-centers/copenhagen (C).
- GeoCables Denmark: https://geocables.com/locations/dk (C for landing leads).
- RebootMonkey Denmark colocation page: https://www.rebootmonkey.com/en/colocation/denmark (C).
- PeeringDB: https://www.peeringdb.com/ (C+/B- depending on entry and maintainer; do not treat as official facility evidence).
- Uptime Institute certified list: https://uptimeinstitute.com/tier-certification/tier-certification-list (A for listed certifications only; not a full market list).

## 1. Query Templates

Use quoted names for operators, municipalities, and site names. Avoid ungrouped `OR` queries; search engines often interpret them loosely.

### 1.1 Operator and Facility Discovery

```text
"{operator}" Danmark datacenter
"{operator}" Denmark "data center"
"{operator}" "{kommune}" datacenter
"{operator}" "{by}" MW datacenter
"{operator}" "{by}" PUE
"{operator}" "{by}" (overskudsvarme OR fjernvarme)
"{operator}" "{by}" nettilslutning
site:{operator-domain} (Danmark OR Denmark) datacenter
site:datacenterindustrien.dk "{operator}"
"datacenter" "{by}" ("under opførelse" OR "under construction" OR "indviet" OR "i drift")
```

### 1.2 Status and Construction

```text
"{site}" datacenter "under construction" Denmark
"{site}" datacenter byggetilladelse
"{site}" datacenter lokalplan
"{site}" datacenter ("i drift" OR operational)
"{site}" datacenter (VVM OR miljogodkendelse)
"{operator}" "{kommune}" byggeplads
"{operator}" "{kommune}" entreprenør datacenter
```

### 1.3 Cloud and Hyperscale

```text
site:learn.microsoft.com/azure "Denmark East"
site:azure.microsoft.com "Denmark East"
site:news.microsoft.com Denmark datacenter region Microsoft
site:local.microsoft.com Danmark datacenter Microsoft
site:docs.aws.amazon.com/global-infrastructure Denmark Region
site:cloud.google.com/about/locations Denmark
site:oracle.com/cloud Denmark region
"Microsoft" "West Denmark" datacenter Esbjerg Varde
"Microsoft" "Høje-Taastrup" datacenter
"Microsoft" Gadstrup datacenter
"Microsoft" "Lille Skensved" datacenter
"Apple" Viborg Foulum datacenter
"Meta" Odense data centre
```

### 1.4 Connectivity

```text
Denmark submarine cable landing Blaabjerg
Blaabjerg landing point AC-1
Havhingsten Denmark landing
Denmark IXP Copenhagen PeeringDB
"Copenhagen Internet Exchange" CIX
```

## 2. Operator and Platform Map

| Operator/platform | Best industry source(s) | Facility notes and grading |
|---|---|---|
| Microsoft Azure Denmark East | Launch page: https://news.microsoft.com/source/emea/features/microsoft-aabner-denmark-east/?lang=da ; English launch page: https://news.microsoft.com/source/emea/features/microsoft-announces-the-opening-of-its-new-datacenter-region-in-denmark-strengthening-digital-resilience-innovation-and-economic-growth/ ; Azure region list: https://learn.microsoft.com/en-us/azure/reliability/regions-list ; Microsoft Local: https://local.microsoft.com/communities/emea/danmark/ | A for Denmark East launch on 2026-03-26 and municipality locations Høje-Taastrup, Køge, Roskilde. Use municipal records for exact buildings. |
| Microsoft Høje-Taastrup | https://local.microsoft.com/blog/microsoft-will-start-building-its-datacenter-in-hoje-taastrup/ | A for Microsoft-stated construction start; Capital Region. |
| Microsoft Roskilde/Gadstrup | https://local.microsoft.com/blog/byggeriet-er-startet-i-roskilde/ | A for Microsoft-stated construction start; Region Zealand. |
| Microsoft Køge/Lille Skensved | Microsoft Denmark East launch page; Computerworld location article | A for Køge municipality from Microsoft; B/C for exact Lille Skensved/site details unless municipal/operator source is attached. |
| Microsoft West Denmark | https://news.microsoft.com/source/emea/features/accelerating-europes-digital-future-microsoft-announces-plans-for-a-new-datacenter-region-in-west-denmark ; DDI item above | A for Microsoft announcement and Esbjerg/Varde municipalities; not operational unless later sources say so. |
| Apple Viborg/Foulum/Tjele | https://www.apple.com/ma/newsroom/2020/09/apple-expands-renewable-energy-footprint-in-europe/ | A for Apple-stated operational 45,000 m2 Viborg data centre. Use Viborg Kommune for local plan/VVM and emergency-power approvals. |
| Meta Odense | https://datacenters.atmeta.com/asset/odense-data-center-info-sheet/ ; https://datacenters.atmeta.com/ | A for Meta-stated Odense data centre facts. DCD/DCK are B for 2022 expansion cancellation: https://www.datacenterdynamics.com/en/news/meta-terminates-contractor-on-danish-data-centers-kills-expansion-project/ and https://www.datacenterknowledge.com/hyperscalers/meta-stops-planned-342-million-data-center-expansion-in-denmark. |
| Bulk Infrastructure DK01 Esbjerg | https://bulkinfrastructure.com/data-centers/locations/dk01 ; https://investindk.com/insights/bulk-infrastructure-breaks-ground-for-data-centre-in-denmark/ | A for Bulk-marketed DK01 Esbjerg campus; B for Invest in Denmark ground-breaking narrative. |
| GlobalConnect | https://globalconnectcarrier.com/services/data-center-and-colocation/ | A for operator-marketed Nordic/Danish colocation offering. Exact Taastrup address is C if sourced only from aggregators; confirm with operator or municipal records. |
| Equinix Copenhagen | https://www.equinix.com/data-centers/europe-colocation | A for accessible Equinix operator facts. A specific Copenhagen URL returned 403 to curl on 2026-08-12; manual/browser verification may be required for CP facility names. |
| Digital Realty Copenhagen | https://www.digitalrealty.com/data-centers/emea/copenhagen | A for operator-owned Copenhagen marketing page; verify current facility ownership after Interxion/GlobalConnect changes before counting sites. |
| itm8/Sotea Silkeborg | Data Center Map/Sotea audit leads; itm8 direct confirmation needed | C/B lead for Silkeborg colocation. `frostcore.net` was not reachable on 2026-08-12 and should not be treated as an operator source. |
| atNorth Denmark | https://www.atnorth.com/nordic-data-centers/denmark-data-centers/ | A only for atNorth's own Denmark marketing statements. Do not count a Danish facility unless the page names an actual site. |
| KMD/NEC | Company pages and municipal records needed | B/C lead for Ballerup enterprise data centers; not final without primary facility evidence. |
| TDC/Nuuday/TDC NET | Company pages and municipal records needed | Legacy telecom/colo lead; not final without current operator facility page or municipal evidence. |
| Atea, One.com, Simply.com, UnoEuro, Fiberby | Company pages and CVR/procurement records | Usually hosting/service providers; verify whether they own a facility or rent colocation before counting. |

## 3. Cloud-Region Facts

| Platform | Official source | Denmark treatment as of 2026-08-12 |
|---|---|---|
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list ; https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies ; Microsoft Denmark East launch page | Denmark East launched 2026-03-26. Microsoft names Høje-Taastrup, Køge, and Roskilde. West Denmark is announced for Esbjerg/Varde but must be treated as planned unless later official sources prove operation. |
| AWS | https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | No Denmark AWS Region found in checked official sources. Copenhagen edge/connectivity does not equal a region or facility count. |
| Google Cloud | https://cloud.google.com/about/locations/ | No Denmark Google Cloud region found in checked official sources. DDI/Google innovation-hub items are ecosystem evidence, not data-center evidence. |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ | No Denmark OCI public cloud region found in checked official sources. |

## 4. Per-Division Leads

### 4.1 North Denmark

Status: low to moderate. No hyperscaler campus confirmed by reviewed official or primary industry sources as of 2026-08-12.

Likely leads: Aalborg regional hosting/colo, telecom rooms, Aalborg University research compute, and energy-adjacent industrial sites. These should not be counted as commercial DCs without operator or municipal proof.

```text
Aalborg datacenter hosting
"North Denmark" "data center"
"Nordjylland" datacenter
site:aalborg.dk datacenter
site:datacenterindustrien.dk Aalborg datacenter
site:datacentermap.com Aalborg Denmark data center
```

### 4.2 Central Denmark

Status: secondary hub.

Confirmed/strong leads:

- Apple Viborg/Foulum/Tjele: operational per Apple (A); municipal records needed for plan/VVM packet.
- itm8/Sotea Silkeborg: current open evidence is a lead, not an A-grade operator confirmation.
- Aarhus: likely hosting/research compute leads, but no hyperscaler campus found in checked sources.

```text
"Apple" Foulum Tjele Viborg datacenter
"Apple" Viborg datacenter overskudsvarme
"itm8" Silkeborg datacenter
"Sotea" "Vejlsøvej 51" datacenter
"Aarhus" datacenter hosting serverpark
site:viborg.dk Apple datacenter
site:silkeborg.dk itm8 datacenter
site:silkeborg.dk Sotea datacenter
```

### 4.3 South Denmark

Status: secondary hub with hyperscale and connectivity concentration.

Confirmed/strong leads:

- Meta Odense: official Meta source (A); DCD/DCK for expansion cancellation (B).
- Bulk DK01 Esbjerg: operator page (A); Invest in Denmark ground-breaking (B).
- Microsoft West Denmark: official announcement for Esbjerg/Varde (A for announcement; not operational unless later official source says so).
- Blaabjerg/Varde: subsea landing connectivity lead, not a data-center count.
- DDI HQ in Fredericia: association presence, not a facility.

```text
"Meta" Odense data center
"Facebook" Odense Tietgenbyen datacenter
"Bulk Infrastructure" Esbjerg DK01
"Microsoft" Esbjerg Varde datacenter
Blaabjerg landing station AC-1
site:odense.dk datacenter
site:esbjerg.dk datacenter
site:varde.dk datacenter
```

### 4.4 Region Zealand

Status: low but rising because Microsoft Denmark East includes Roskilde and Køge.

Confirmed/strong leads:

- Microsoft Roskilde/Gadstrup: Microsoft Local construction page (A).
- Microsoft Køge/Lille Skensved: Microsoft launch page names Køge (A for municipality); exact site details need municipal records or Microsoft Local/operator source.
- Other commercial colocation density appears thin; use negative searches and document results.

```text
"Microsoft" Roskilde Gadstrup datacenter
"Microsoft" Koge "Lille Skensved" datacenter
site:roskilde.dk Microsoft datacenter
site:koge.dk Microsoft datacenter
site:kalundborg.dk datacenter
site:naestved.dk datacenter
site:slagelse.dk datacenter
site:ringsted.dk datacenter
site:holbaek.dk datacenter
```

### 4.5 Capital Region

Status: major Copenhagen-metro hub.

Confirmed/strong leads:

- Microsoft Høje-Taastrup: construction page (A).
- GlobalConnect Copenhagen/Taastrup: operator-marketed colocation (A); exact address can be C if only from aggregators.
- Equinix Copenhagen: operator presence (A when accessible); specific CP details need manual page verification due 403 in curl.
- Digital Realty Copenhagen: operator-owned page (A for its page statements); verify current facility ownership.
- KMD/NEC Ballerup and TDC/Nuuday legacy data centers: B/C leads pending primary evidence.
- CIX/Copenhagen Internet Exchange: `copenhagenix.net` failed DNS on 2026-08-12; use PeeringDB only as a C-grade lead until current official IXP source is found.
- Bornholm: negative-control municipality; no commercial colocation found in reviewed sources.

```text
"Microsoft" "Høje-Taastrup" datacenter
"GlobalConnect" Taastrup datacenter Hørskætten
"Equinix" Copenhagen CP1 CP2
"Digital Realty" Copenhagen Denmark
"KMD" Ballerup datacenter
"Copenhagen Internet Exchange" CIX
site:peeringdb.com Copenhagen CIX
site:brk.dk datacenter Bornholm
```

## 5. Connectivity and Subsea Leads

Connectivity assets are useful siting signals but should not be counted as data centers.

- Blaabjerg, Varde Kommune: https://www.submarinecablemap.com/landing-point/blaabjerg-denmark (C+/B lead for cable landing). Confirm current cable inventory with cable operators or TeleGeography.
- Havhingsten: https://www.submarinenetworks.com/en/systems/intra-europe/havhingsten (B for Submarine Networks system summary; confirm exact Danish landings from operator documents).
- Aqua Comms AEC pages: https://www.aquacomms.com/network/aec-1 (A for Aqua Comms' own network statements; verify Denmark relevance before using).
- GeoCables Denmark: https://geocables.com/locations/dk (C lead list only).

## 6. Known Facility/Project Matrix

| Facility/project | Division | Status treatment | Best industry evidence | Grade notes |
|---|---|---|---|---|
| Apple Viborg/Foulum/Tjele | Central Denmark | Operational hyperscale facility | Apple newsroom | A for operational 45,000 m2 Viborg facility; municipal records for permits |
| Meta Odense | South Denmark | Operational hyperscale campus | Meta info sheet; DCD/DCK for cancellation | A for Meta-stated facility facts; B for expansion cancellation |
| Microsoft Denmark East | Capital Region; Region Zealand | Launched cloud region; physical facilities need site-level evidence | Microsoft launch and Local pages | A for cloud region and named municipalities |
| Microsoft West Denmark | South Denmark | Planned/announced | Microsoft newsroom; DDI | A for announcement and Esbjerg/Varde; not operational by default |
| Bulk DK01 Esbjerg | South Denmark | Operator-marketed colocation campus | Bulk page; Invest in Denmark | A for Bulk page facts; B for investment-promotion narrative |
| GlobalConnect Taastrup/Copenhagen | Capital Region | Operator-marketed colocation | GlobalConnect page; aggregators | A for operator offering; C for aggregator-only address/site details |
| Equinix Copenhagen | Capital Region | Operator presence; details require verification | Equinix page | A for accessible operator facts; U for blocked/unopened details |
| Digital Realty Copenhagen | Capital Region | Operator-marketed page; ownership needs verification | Digital Realty page | A for page facts; verify current facility inventory |
| itm8/Sotea Silkeborg | Central Denmark | Lead only until primary confirmation | Data Center Map/Sotea audit lead | C/B lead; permits and direct operator evidence still needed |
| CIX/Copenhagen Internet Exchange | Capital Region | Connectivity lead | PeeringDB; former domain unresolved | C/U until current official IXP source is found |
| Blaabjerg landing | South Denmark | Connectivity asset | Submarine Cable Map/TeleGeography, cable operators | C+/B lead; not a data-center facility |

## 7. Industry-to-Official Reconciliation

For every lead, create one row with:

```text
operator | facility/site name | municipality | repo division | lead source URL | lead grade | claimed status | official source needed | official source URL | final count decision
```

Final count rules:

1. Count only if an operator-owned page or official record names the facility/location.
2. Upgrade to high confidence when a municipal planning/building/environmental record or operator page names the site.
3. Keep region-launch, land-purchase, grid-reservation, investment-announcement, IXP, and cable-landing items out of facility counts unless facility evidence exists.
4. Record negative searches for North Denmark and Bornholm/low-density municipalities so later runs know coverage was attempted.

## 8. Refresh Cadence

- Before every run: Microsoft/AWS/GCP/Oracle region pages; Microsoft Local Denmark; Apple, Meta, Bulk, GlobalConnect, Equinix, Digital Realty, and the current Silkeborg operator lead.
- Monthly: DDI, Computerworld, Version2, ITWatch, EnergyWatch, Ingenioren, Borsen, DCD, DataCenterKnowledge.
- Quarterly: Data Center Map, Baxtel, DatacenterHawk, PeeringDB, Uptime Institute, TeleGeography/Submarine Cable Map, GeoCables.
- Semi-annually: reconcile all industry leads against CVR, Plandata.dk, municipality portals, environmental records, and grid/procurement sources.
