# DK Explorer Official - Denmark Datacenter Enumeration

Date: 2026-08-12. Scope: Denmark (DK). Repo divisions: North Denmark; Central Denmark; South Denmark; Region Zealand; Capital Region.

Purpose: enumerate Danish data centers from official and regulatory evidence. Use industry sources only to discover leads, then confirm the facility through planning, building, environmental, grid, business-register, procurement, or operator-owned primary records.

## Reliability Grades

Grades attach to the specific fact cited, not to a whole row.

- Grade A: primary evidence for the specific fact: municipal lokalplan, kommuneplan amendment, building permit, EIA/VVM screening, environmental approval, Plandata.dk record, BBR record, CVR/Virk record, Energinet/DSO/Forsyningstilsynet record, Retsinformation/Lovtidende law text, EU/agency page, public procurement notice, or operator-owned page for that operator's own facility.
- Grade B: credible secondary evidence with named operator, municipality/place, date, and status, including trade press, stock-exchange/company release, association news, construction contractor news, or official investment-promotion case study where the underlying permit is not linked.
- Grade C: directories, market reports, map aggregators, PeeringDB/user-maintained entries, consultant lists, social posts, or unsourced press. Use only as leads.
- Grade U: unverified or not reachable in the current run. Do not use for counting until upgraded.

An operator page is Grade A for "operator markets facility/location/status as stated on that page." It is not Grade A for permits, exact legal property boundaries, grid capacity, tenants, or completion unless the page explicitly proves those facts. Cloud-region pages prove cloud-region availability and geography, not physical campus addresses unless the page names them.

## 0. Denmark Structure

### 0.1 Division Coverage

Denmark has five current regions and 98 municipalities. Municipalities are the practical planning and building authorities for data-center enumeration. The five repo divisions are complete as follows:

| Repo division | Official Danish region | Official regional domain | Municipality pivots for DC work |
|---|---|---|---|
| North Denmark | Region Nordjylland / North Denmark Region | https://rn.dk/ | Aalborg, Hjorring, Frederikshavn, Thisted, Jammerbugt, Vesthimmerland |
| Central Denmark | Region Midtjylland / Central Denmark Region | https://rm.dk/ | Viborg/Tjele/Foulum, Silkeborg, Aarhus, Horsens, Herning, Randers, Skanderborg |
| South Denmark | Region Syddanmark / Region of Southern Denmark | https://rsyd.dk/ | Odense, Esbjerg, Varde/Blaabjerg, Fredericia, Kolding, Sonderborg, Aabenraa |
| Region Zealand | Region Sjalland / Region Zealand | https://regionsjaelland.dk/ | Roskilde/Gadstrup, Koge/Lille Skensved, Kalundborg, Naestved, Slagelse, Ringsted, Holbaek, Lolland, Guldborgsund, Vordingborg, Faxe/Rodvig |
| Capital Region | Region Hovedstaden / Capital Region of Denmark | https://regionh.dk/ | Kobenhavn, Hoje-Taastrup, Ballerup, Glostrup, Lyngby-Taarbaek, Frederiksberg, Bornholm |

Cross-check the five-region structure against Danske Regioner: https://www.regioner.dk/services/in-english/regional-denmark/ (A). Note: Denmark has approved a future merger of the Capital Region and Region Zealand from 2027, but this repo's DK division model remains the five-region model above for 2026 enumeration.

### 0.2 No National Data-Center Register

Denmark has no national data-center licensing register or official data-center census. Build the facility list bottom-up from:

1. CVR/Virk business register: https://datacvr.virk.dk/ and https://virk.dk/ (A for legal entity, CVR number, production units, registered addresses, and activity codes). The Danish Business Authority describes CVR as the government master register for Denmark and Greenland: https://danishbusinessauthority.dk/ (A). Search DB07/NACE 63.11.00 for "Databehandling, hosting og lignende aktiviteter" as a candidate universe, then confirm facilities elsewhere.
2. Plandata.dk: https://www.plst.dk/ and https://kort.plandata.dk/ (A for nationwide planning records). Plan- og Landdistriktsstyrelsen states Plandata.dk is the national digital register for physical planning and contains plans produced under Planloven.
3. Municipal planning/building archives: A for local plans, building permits, public consultation pages, council decisions, and VVM/environmental decisions. There is no single national building-permit database.
4. BBR: https://bbr.dk/ and borger.dk BBR self-service (A for building/property attributes where accessible). BBR is useful for confirming a known address, but building-use categories do not reliably expose data centers.
5. Environmental records: municipal miljogodkendelse, VVM-screening/miljovurdering, Miljostyrelsen pages, and Miljoeportalen where relevant. Data centers often trigger noise, backup-generator, fuel-storage, cooling, stormwater, and heat-reuse documents.
6. Grid records: Energinet https://www.energinet.dk/, Forsyningstilsynet https://forsyningstilsynet.dk/, DSOs and capacity maps. Large-consumer connection records are strong evidence for planned hyperscale facilities when named.
7. Public procurement: udbud.dk https://udbud.dk/, TED https://ted.europa.eu/, SKI https://www.ski.dk/, and KOMBIT https://kombit.dk/ for hosting, colocation, cloud, and disaster-recovery awards.

### 0.3 Legal and Regulatory Basis

Use Retsinformation https://www.retsinformation.dk/ as the official law source (A). Current law IDs must be re-checked on each refresh, but these instruments are the correct legal hooks:

- Planning: Planloven. Municipalities adopt kommuneplaner and lokalplaner; Plandata.dk carries official planning data.
- Building: Byggeloven and Bygningsreglementet BR18. Municipalities issue building permits.
- Environment: Miljovurderingsloven, Miljobeskyttelsesloven, and Godkendelsesbekendtgorelsen. Check VVM/miljovurdering, generators, cooling, fuel storage, and noise.
- Electricity: Elforsyningsloven. Use Energinet, DSOs, and Forsyningstilsynet for grid connection and tariff evidence.
- Data protection: GDPR and Databeskyttelsesloven. Datatilsynet https://www.datatilsynet.dk/ is the Danish supervisory authority.
- Cybersecurity: Lov nr. 434 af 06/05/2025, "Lov om foranstaltninger til sikring af et hojt cybersikkerhedsniveau (NIS 2-loven)", enters into force 2025-07-01 per Retsinformation (A): https://www.retsinformation.dk/eli/lta/2025/434.
- Telecom: Digitaliseringsstyrelsen holds telecom policy/regulatory pages, including https://digst.dk/tele/ and https://digst.dk/tele/love-og-regler-paa-teleomraadet/ (A).

### 0.4 Telecom and Digital Government

There is no Danish telecom-regulator data-center facility list. Use telecom sources for connectivity and critical-infrastructure context only.

- Digitaliseringsstyrelsen: https://digst.dk/tele/ (A) for telecom policy, numbering, broadband, spectrum, and telecom-law guidance.
- Styrelsen for Samfundssikkerhed: https://samsik.dk/tele/ (A where reachable) for telecom resilience/security responsibilities.
- Konkurrence- og Forbrugerstyrelsen: https://www.kfst.dk/ (A) for competition/consumer aspects.
- EU national regulatory authority list: https://digital-strategy.ec.europa.eu/da/policies/telecommunications-national-regulatory-authorities (A).
- CFCS: https://www.cfcs.dk/ (A) for cyber threat and NIS context.

## 1. Search Vocabulary

Use Danish spellings with and without Danish characters because many sources normalize them differently.

```text
datacenter
datacentre
data center
serverpark
serverhus
serverhotel
serverlokale
kolokation
colocation
hosting
webhotel
cloud
skyen
digital infrastruktur
internetudveksling
peering
internetknudepunkt
soekabel
undersoisk kabel
landstation
lokalplan
kommuneplan
byggetilladelse
byggeansoegning
VVM-screening
miljovurdering
miljogodkendelse
nettilslutning
eltilslutning
tilslutningsaftale
reserveret effekt
transformatorstation
overskudsvarme
fjernvarme
noedstroem
dieselgenerator
koeling
```

English:

```text
data center
data centre
server farm
colocation
hosting
cloud region
digital infrastructure
internet exchange point
submarine cable
landing station
building permit
environmental assessment
EIA
grid connection
waste heat
district heating
backup generator
```

## 2. Official Enumeration Pipeline

### 2.1 Confirm the Legal Entity

Start with CVR/Virk when an operator or SPV is known.

```text
site:datacvr.virk.dk "{operator}"
site:datacvr.virk.dk "{SPV name}"
site:virk.dk "{operator}" "Databehandling, hosting"
"{operator}" "CVR" "63.11"
"{operator}" "P-nummer" "{kommune}"
```

Extract CVR number, production-unit address, activity code, status, ownership, registered management, and historical names. CVR alone does not prove a data-center building.

### 2.2 Planning and Building Records

Search Plandata.dk and municipality sites first; then use search-engine fallbacks.

```text
site:{kommune}.dk (datacenter OR "data center" OR serverpark)
site:{kommune}.dk lokalplan datacenter
site:{kommune}.dk lokalplan "{operator}"
site:{kommune}.dk byggetilladelse datacenter
site:{kommune}.dk kommuneplan datacenter
site:{kommune}.dk VVM datacenter
site:{kommune}.dk miljogodkendelse datacenter
"lokalplan" "{operator}" "{kommune}"
"lokalplan nr." "{adresse}" datacenter
"{operator}" "{kommune}" "byggetilladelse"
```

Extract municipality, plan number, plan title, legal status, decision date, appeal deadline/status, applicant/SPV, matrikel/property, address, permitted use, gross floor area, building heights, generator/cooling language, heat-reuse provisions, and PDF URLs.

Examples of high-yield confirmed planning pivots:

- Viborg Kommune council item for Apple/Foulum: search result confirms "lokalplan nr. 460 for et erhvervsomraade ved Foulum", VVM permit for datacenter/high-voltage station, and environmental approval for emergency-power plant (A when opened from Viborg Kommune records).
- Odense Kommune planning/VVM records for Meta/Facebook in Tietgenbyen: search for "Lokalplan 6-1096" and "Udvidelse af datacenter i Tietgenbyen" (A when sourced from odense.dk or dkplan/NIRAS municipal viewer).
- Roskilde Kommune planning archive: https://www.roskilde.dk/da-dk/service-og-selvbetjening/borger/bolig-og-byggeri/dit-hus-og-din-grund/find-lokalplaner-og-kommuneplan/ (A for portal). Search "Microsoft", "Gadstrup", and "Finervej".

### 2.3 Environmental and Heat-Reuse Records

Use the municipality, Miljostyrelsen, and district-heating utilities. Query both operator and technical triggers.

```text
site:{kommune}.dk "{operator}" VVM
site:{kommune}.dk "{operator}" miljogodkendelse
site:{kommune}.dk datacenter noedstroem
site:{kommune}.dk datacenter dieselgenerator
site:{kommune}.dk datacenter overskudsvarme
site:mst.dk datacenter "{kommune}"
"{operator}" "{kommune}" "miljoerapport"
"{operator}" "{kommune}" fjernvarme
```

Environmental approvals and VVM screenings are Grade A for scoped environmental decisions and technical attributes. They do not by themselves prove the facility is operational unless completion/use is stated.

### 2.4 Grid and Energy Records

Grid capacity is a binding constraint for Danish hyperscale projects. Use Energinet and DSO records where available.

```text
site:energinet.dk datacenter
site:energinet.dk "store forbrugere"
site:energinet.dk nettilslutning datacenter
site:forsyningstilsynet.dk datacenter
site:forsyningstilsynet.dk nettilslutning
site:ens.dk datacenter elforbrug
"{operator}" "{kommune}" nettilslutning
"{operator}" "{kommune}" transformatorstation
"{kommune}" datacenter "132 kV"
"{kommune}" datacenter "150 kV"
"{operator}" "{kommune}" "tilslutningsaftale"
```

Energinet's "Net til tiden" material is useful context, but named connection records are stronger. Treat general trade-press statements about grid bottlenecks as Grade B unless backed by Energinet/Forsyningstilsynet documents.

### 2.5 Procurement and Public-Sector IT

Procurement rarely proves a physical data-center building, but it can reveal incumbent colocation/hosting providers and DR sites.

```text
site:udbud.dk datacenter
site:udbud.dk kolokation
site:udbud.dk hosting "{kommune}"
site:ted.europa.eu Denmark datacenter hosting
site:ski.dk cloud hosting datacenter
site:kombit.dk hosting datacenter
```

Extract buyer, supplier, lot, contract period, service location if stated, and CPV codes. Grade A for the procurement award facts; facility existence still needs facility evidence.

## 3. Cloud-Region Official Checks

Cloud-region lists are volatile and must be checked before every run.

- Microsoft Azure regions list: https://learn.microsoft.com/en-us/azure/reliability/regions-list (A for live Azure public-cloud regions).
- Microsoft Azure geography page: https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies (A; search page text showed Denmark East).
- Microsoft official Denmark East launch: https://news.microsoft.com/source/emea/features/microsoft-aabner-denmark-east/?lang=da and English page https://news.microsoft.com/source/emea/features/microsoft-announces-the-opening-of-its-new-datacenter-region-in-denmark-strengthening-digital-resilience-innovation-and-economic-growth/ (A). The Danish page names Høje-Taastrup, Køge, and Roskilde and is dated 2026-03-26.
- Microsoft datacenter community page: https://local.microsoft.com/communities/emea/danmark/ (A for Microsoft's community/construction statements).
- Microsoft Høje-Taastrup construction update: https://local.microsoft.com/blog/microsoft-will-start-building-its-datacenter-in-hoje-taastrup/ (A).
- Microsoft Roskilde construction update: https://local.microsoft.com/blog/byggeriet-er-startet-i-roskilde/ (A).
- Microsoft West Denmark announcement: https://news.microsoft.com/source/emea/features/accelerating-europes-digital-future-microsoft-announces-plans-for-a-new-datacenter-region-in-west-denmark (A for announcement). It states the planned region spans Esbjerg and Varde municipalities.
- AWS regions: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html (A). No Danish AWS region was found in the checked sources as of 2026-08-12.
- Google Cloud locations: https://cloud.google.com/about/locations/ (A). No Danish Google Cloud region was found in the checked sources as of 2026-08-12.
- Oracle OCI regions: https://www.oracle.com/cloud/public-cloud-regions/ (A). No Danish OCI public region was found in the checked sources as of 2026-08-12.

## 4. Per-Division Official Method

### 4.1 North Denmark

Expected activity: low to moderate. No hyperscaler campus confirmed in reviewed official/primary sources as of 2026-08-12.

Primary authorities: Aalborg, Hjorring, Frederikshavn, Thisted, Jammerbugt, Vesthimmerland municipalities; CVR; local DSOs; Aalborg University for non-commercial research compute.

```text
site:aalborg.dk datacenter
site:aalborg.dk serverpark
site:aalborg.dk lokalplan hosting
"Aalborg" datacenter byggetilladelse
"Nordjylland" datacenter lokalplan
"North Denmark" data center municipality
```

Count only facilities with operator pages or municipal records. Treat regional hosting and university compute as separate from commercial colocation unless the source states public colocation services.

### 4.2 Central Denmark

Expected activity: secondary hub, anchored by Apple Foulum/Viborg and regional colocation.

Primary authorities: Viborg, Silkeborg, Aarhus, Horsens, Herning, Randers, Skanderborg municipalities; Energinet/Tjele grid context.

Known official/primary pivots:

- Apple Viborg/Foulum/Tjele: Apple newsroom states the Viborg data centre is operational, 45,000 square meters, and supports European Apple services: https://www.apple.com/ma/newsroom/2020/09/apple-expands-renewable-energy-footprint-in-europe/ (A). Use Viborg Kommune records for local-plan, VVM, emergency-power, and high-voltage-station details; Viborg search results identify local plan no. 460 and related VVM/environment decisions (A once opened from Viborg Kommune).
- itm8/Sotea Silkeborg: current open evidence is mostly aggregator and older Sotea audit material, not a clean operator facility page. Treat as a C/B lead until itm8 or Silkeborg Kommune confirms the facility directly. The former `frostcore.net` lead was not reachable on 2026-08-12 and should not be used as A-grade evidence.

```text
site:viborg.dk Apple datacenter Foulum
site:viborg.dk "lokalplan nr. 460"
site:viborg.dk datacenter "noedstroemsanlaeg"
site:silkeborg.dk itm8 datacenter
site:silkeborg.dk Sotea datacenter
"itm8" "Silkeborg" datacenter
"Sotea" "Vejlsøvej 51" datacenter
```

### 4.3 South Denmark

Expected activity: secondary hub, anchored by Meta Odense, Bulk Esbjerg, Microsoft West Denmark, and Blaabjerg connectivity.

Primary authorities: Odense, Esbjerg, Varde, Fredericia, Kolding, Sonderborg, Aabenraa municipalities; Energinet/DSO records; Varde for Blaabjerg cable landing context.

Known official/primary pivots:

- Meta Odense: official Meta info sheet at https://datacenters.atmeta.com/asset/odense-data-center-info-sheet/ (A for Meta-stated Odense data-centre facts). Search Odense Kommune for Tietgenbyen, "Lokalplan 6-1096", "Udvidelse af datacenter", VVM/miljoerapport, and heat-reuse records.
- Bulk DK01 Esbjerg: https://bulkinfrastructure.com/data-centers/locations/dk01 (A for Bulk's own marketed campus; automated curl may receive 403, so check in browser/manual mode). Invest in Denmark case study is B for ground-breaking/project narrative: https://investindk.com/insights/bulk-infrastructure-breaks-ground-for-data-centre-in-denmark/.
- Microsoft West Denmark: official Microsoft announcement above (A for plan and municipalities; permits/construction require Esbjerg/Varde records).
- Blaabjerg landing point: https://www.submarinecablemap.com/landing-point/blaabjerg-denmark (C+/B lead; TeleGeography map page is authoritative as an industry map but not a Danish permit record). Confirm with cable-operator pages where counting cable landings.

```text
site:odense.dk Meta datacenter
site:odense.dk Facebook datacenter Tietgenbyen
site:odense.dk "Lokalplan 6-1096"
site:esbjerg.dk Bulk datacenter
site:esbjerg.dk Microsoft datacenter
site:varde.dk Microsoft datacenter
site:varde.dk Blaabjerg kabel
```

### 4.4 Region Zealand

Expected activity: rising because two Denmark East Microsoft locations are in Zealand; otherwise thin commercial colocation.

Primary authorities: Roskilde, Koge, Kalundborg, Naestved, Slagelse, Ringsted, Holbaek, Lolland, Guldborgsund, Vordingborg, Faxe municipalities.

Known official/primary pivots:

- Microsoft Roskilde/Gadstrup: Microsoft Local states construction started in Roskilde: https://local.microsoft.com/blog/byggeriet-er-startet-i-roskilde/ (A for Microsoft statement). Use Roskilde Kommune local-plan portal and search Finervej/Gadstrup/Microsoft for permits.
- Microsoft Koge/Lille Skensved: Microsoft Denmark East launch page names Køge as one of the three locations (A for location at municipality level). Use Koge Kommune for exact plan/permit evidence.

```text
site:roskilde.dk Microsoft datacenter Gadstrup
site:roskilde.dk Finervej Microsoft
site:koge.dk Microsoft datacenter
site:koge.dk "Lille Skensved" datacenter
site:kalundborg.dk datacenter
site:naestved.dk datacenter
site:slagelse.dk datacenter
site:ringsted.dk datacenter
site:holbaek.dk datacenter
site:lolland.dk datacenter
site:guldborgsund.dk datacenter
site:vordingborg.dk datacenter
site:faxe.dk datacenter OR soekabel
```

### 4.5 Capital Region

Expected activity: major hub for Copenhagen-area colocation, Microsoft Denmark East, enterprise IT, and IXP/connectivity.

Primary authorities: Hoje-Taastrup, Kobenhavn, Ballerup, Glostrup, Lyngby-Taarbaek, Frederiksberg, Bornholm municipalities; CVR; building/property records.

Known official/primary pivots:

- Microsoft Høje-Taastrup: Microsoft Local construction page (A for Microsoft statement): https://local.microsoft.com/blog/microsoft-will-start-building-its-datacenter-in-hoje-taastrup/. Confirm with Høje-Taastrup Kommune planning/building records.
- GlobalConnect: https://globalconnectcarrier.com/services/data-center-and-colocation/ (A for GlobalConnect's own Nordic colocation offering; exact Taastrup address needs operator-specific or municipal confirmation if not stated on the page).
- Equinix Copenhagen: https://www.equinix.com/data-centers/europe-colocation (A for Equinix European/Copenhagen presence if the page is accessible; curl returned 403 on a specific Copenhagen URL, so browser/manual verification may be required).
- Digital Realty Copenhagen: https://www.digitalrealty.com/data-centers/emea/copenhagen (A for operator-owned marketed Copenhagen page; verify current post-Interxion/GlobalConnect ownership before counting facilities).
- KMD/NEC Ballerup and TDC/Nuuday legacy colocation are leads until company pages or municipal records confirm facility details.
- CIX/Copenhagen Internet Exchange: `copenhagenix.net` did not resolve on 2026-08-12; use PeeringDB only as a C-grade lead and confirm against current IXP/operator sources.
- Bornholm: include as a negative-control municipality within the Capital Region.

```text
site:htk.dk Microsoft datacenter
site:htk.dk "Høje-Taastrup" datacenter
site:ballerup.dk KMD datacenter
site:glostrup.dk datacenter
site:kk.dk datacenter
"GlobalConnect" Taastrup datacenter
"Equinix" Copenhagen CP1 OR CP2
"Digital Realty" Copenhagen Denmark
site:peeringdb.com Copenhagen "CIX"
site:brk.dk datacenter Bornholm
```

## 5. Facility Evidence Matrix

| Facility/project | Division(s) | Count status | Current best evidence | Grade notes |
|---|---|---|---|---|
| Apple Viborg/Foulum/Tjele | Central Denmark | Count as operational hyperscale facility | Apple newsroom, Viborg municipal planning/VVM records to attach | A for Apple-stated operational 45,000 m2 Viborg facility; A for municipal plan facts once linked; B/C for claims not in those sources |
| Meta Odense | South Denmark | Count as operational hyperscale campus | Meta official info sheet; Odense planning/VVM records | A for Meta-stated Odense data centre; A for municipal planning facts; B for expansion-cancellation trade press |
| Microsoft Denmark East | Capital Region; Region Zealand | Count as launched cloud region; count individual physical facilities only with Microsoft/municipal evidence | Microsoft 2026-03-26 launch page; Microsoft Local Høje-Taastrup/Roskilde; municipal records | A for Denmark East launch and Høje-Taastrup/Køge/Roskilde municipality locations; A for Microsoft construction statements; municipal permits still needed for exact facility boundaries |
| Microsoft West Denmark | South Denmark | Planned/announced; do not count as operational | Microsoft West Denmark announcement; Esbjerg/Varde municipal records pending | A for Microsoft announcement and municipalities; B/U for construction or permit status until official local records are attached |
| Bulk DK01 Esbjerg | South Denmark | Count if operator-marketed active campus; confirm permit status | Bulk operator page; Invest in Denmark case | A for Bulk's own campus statements; B for Invest in Denmark ground-breaking narrative |
| GlobalConnect Taastrup/Copenhagen metro | Capital Region | Count operator-marketed colocation; facility-level count requires operator/address records | GlobalConnect operator page; municipal/address records | A for operator offering; C for exact address if sourced only from aggregators |
| Equinix Copenhagen | Capital Region | Count only after accessible Equinix Copenhagen page/manual verification | Equinix operator pages | A for operator page facts; U where access blocked or details missing |
| Digital Realty Copenhagen | Capital Region | Count only after current facility ownership check | Digital Realty Copenhagen page | A for operator page facts; verify against GlobalConnect/Interxion transaction history |
| itm8/Sotea Silkeborg | Central Denmark | Lead only until primary confirmation | Data Center Map/older Sotea audit lead; Silkeborg Kommune records needed | C/B lead; not A-grade from current open operator evidence |
| Blaabjerg cable landing | South Denmark | Connectivity asset, not a data center unless facility source appears | Submarine Cable Map/TeleGeography and cable-operator sources | C+/B for landing lead; not a DC count |

## 6. Validation Rules

1. Do not count a facility from a cloud-region name alone.
2. Do not count a facility from a directory row alone.
3. Split multi-campus cloud regions by municipality only when the source names municipalities or sites.
4. Keep commercial colocation, hyperscale self-build, enterprise/private IT, research HPC, IXP, and cable landing assets separate.
5. For every counted facility, store at least one facility-level source URL, access date, source grade, operator, municipality, repo division, status, and any uncertainty.
6. When source access is blocked by 403/JS/paywall, keep the URL but downgrade the unsupported facts and add an access note.

## 7. Refresh Cadence

- Before every run: Microsoft/AWS/GCP/Oracle region lists; Microsoft Local Denmark; operator pages for Apple, Meta, Bulk, GlobalConnect, Equinix, Digital Realty, and the current Silkeborg operator lead.
- Monthly: DDI, Computerworld, Version2, ITWatch, EnergyWatch, Ingenioren, Borsen, Data Center Dynamics, DataCenterKnowledge.
- Quarterly: Plandata.dk searches for "datacenter"; municipality searches for the five divisions; Energinet/Forsyningstilsynet grid status; CVR 63.11 universe.
- Semi-annually: BBR/address checks for counted sites; procurement searches; Uptime Institute tier list; cable landing maps.
