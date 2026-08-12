# FJ Explorer Industry - Fiji Datacenter Enumeration via Operators, Cable Infrastructure, Trade Press, Directories, and Locality Patterns

Date: 2026-08-12. Scope: Fiji (FJ), all 5 divisions/dependency from `world-manifest.jsonl`: Central, Eastern, Northern, Rotuma, Western. Angle: operator and industry discovery, with official verification required before promotion to facility inventory.

Reliability grades used by this explorer: **A** = official operator/provider page, public-sector owner page, regulator/registry record, official tender, official cloud/location page, stock-exchange/company filing, or official project document; **B** = reputable trade/local/regional press with named parties and dates; **C** = directory, marketplace, cable map/database, social repost, SEO hosting page, or unattributed aggregate.

## 0. Market Shape and Current Conclusion

- Fiji is one of the more active Pacific island datacenter markets, but it is still small. Expect a handful of telecom/operator facilities and cable/ICT projects, not a broad carrier-neutral or hyperscale cloud-region market.
- Verified industry tiers are: (1) operator-hosted services: TFL data-centre/colocation services and Vodafone Fiji's Fiji-based Hosted Cloud/IaaS; (2) cable and telecom hubs: FINTEL Vatuwaqa Communications Centre and Savusavu cable spur infrastructure; (3) hyperscaler cable/ICT infrastructure: Google's Natadola ICT facility and Tabua/Bulikula-related systems; (4) proposed commercial build: TFL NextGen Data Centre.
- Google's Natadola project is not a public Google Cloud region. Classify it as `hyperscaler_ict_facility` plus `cable_landing_station`; keep operational status conservative until Grade A commissioning appears.
- Fiji VPS, dedicated-server, VPN, and `.fj hosting` pages are often offshore SEO inventory. Treat them as Grade C false positives unless tied to a named Fiji operator facility with primary evidence.
- Division coverage must include low-yield Eastern and Rotuma. A negative sweep is valid only if the search route is recorded.

## 1. Operator and Vendor Sweep

| Operator / lead | Source URL | Division focus | Evidence use | Grade |
|---|---|---|---|---|
| Telecom Fiji Limited (TFL) | https://www.telecom.com.fj/ and https://www.telecom.com.fj/business/ict-solutions/ | Central likely; national service | Official page confirms cloud services, co-location for disaster recovery, data centres, hosted PABX. Main commercial-DC seed, but physical site/capacity not disclosed. | A for service |
| TFL-Google terrestrial fibre | https://www.telecom.com.fj/telecom-fiji-knowledge/telecom-fiji-and-google-announce-strategic-agreement-to-deliver-terrestrial-fiber-link-in-fiji/ | Central to Western | Officially ties FINTEL Vatuwaqa landing station to Google Natadola ICT facility via Queens Highway fibre. Fibre route evidence, not DC commissioning. | A |
| TFL NextGen Data Centre | https://www.tenderlink.com/tfl and https://portal.tenderlink.com/tfl/alltenders/; official TFL social post if tender has closed | Site not disclosed | EOI for Fiji's first next-generation, internationally accredited, sustainable data centre. Fiji Times says 24-month construction beginning in 2026. | A for EOI if preserved; B for schedule |
| Vodafone Fiji Hosted Cloud / IaaS | https://www.vodafone.com.fj/business/products-services/ict-cloud-solutions/infrustructure-as-a-service | Fiji-based; exact division not disclosed | Operator-hosted cloud service connected to Vodafone IPVPN. Use as internal/operator cloud lead; no MW/rack/site details. | A for service |
| Digicel Fiji | Verify current official Fiji pages | National | Telecom network POP/server-room lead only; no verified public DC page found. | Lead only |
| FINTEL | https://fintel.com.fj/our-facilities/ and https://fintel.com.fj/about-us/ | Central; Northern by cable spur context | Vatuwaqa cable hub; LEO/SAP colocation with UPS/cooling/backhaul. Datacenter-adjacent, not general commercial DC. | A |
| Google Pacific Connect systems | https://cloud.google.com/blog/products/infrastructure/honomoana-and-tabua-subsea-cables-connect-south-pacific and https://cloud.google.com/blog/products/infrastructure/introducing-bulikula-and-halaihai-subsea-cables-to-connect-the-central-pacific | Central/Western | Tabua/Bulikula/Honomoana/Halaihai cable context and partner evidence. Not cloud-region evidence. | A |
| Samoa Submarine Cable Company (SSCC) | https://www.ssccsamoa.com/ | Central/Northern | Tui-Samoa landing points include Suva and Savusavu. Cable infrastructure lead. | A for landing evidence |
| Southern Cross Cable Network | https://www.southerncrosscables.com/ | Central/Northern | Southern Cross/SX NEXT Fiji cable context; use cable owner where it states landing/RFS details. | A/B |
| Interchange | https://interchange.vu/ | Central | ICN1 Suva-Port Vila cable context. | A/B |
| Megaport / ecosystem pages | https://www.megaport.com/ecosystem/vendor/telecom-fiji-limited/ | Central lead | Interconnection/ecosystem lead only; not facility proof. | C unless primary corroborates |
| Staghorn Services / Natadola lease chain | ROC Public https://roc.digital.gov.fj/ and press such as Islands Business/PACNEWS | Western | Entity/lease lead for Google Natadola; must be verified through ROC/land records for Grade A. | B until primary record |
| USP/FNU/institutional ICT | https://www.usp.ac.fj/ and official institution pages | Central | Institutional server-room leads only unless procurement/facility record appears. | Lead only |

Operator search templates:

```text
"{operator}" Fiji ("data centre" OR "data center" OR datacenter)
"{operator}" Fiji (colocation OR "co-location" OR hosting OR "server room")
"{operator}" Fiji (rack OR MW OR "Tier III" OR "Tier 3" OR Uptime)
"{operator}" Fiji ("cable landing" OR "landing station" OR POP OR Vatuwaqa)
"{operator}" "{division}" Fiji
"{operator}" Fiji (construction OR commissioned OR operational OR "ready for service")
```

## 2. Google Natadola Project Handling

Primary facts to preserve:

- Fiji Government, 30 Nov 2024: PM Sitiveni Rabuka officiated the groundbreaking at Natadola, Nadroga Province. The facility will hold a new cable landing station and house data transmission servers/racks and power generating equipment for Google's international fibre optic cables. This is Grade A for scope and location.
- PM Office, 27 Oct 2023: the South Pacific Connect initiative includes new subsea cables linking the United States, Fiji, Australia, and French Polynesia and physically diverse Fiji landing stations. This is Grade A for initiative scope.
- Google official blogs: Tabua will connect the US/Australia/Fiji; Bulikula will connect Guam/Fiji as part of Central Pacific Connect; use the Google pages for system names and partners.
- TFL, 9 Jun 2025: Telecom Fiji and Google agreed that TFL would design, build, and maintain the terrestrial fibre link between FINTEL's Vatuwaqa international cable landing station and Google's Natadola ICT facility. This is Grade A for the route and endpoints.

Secondary facts to treat carefully:

- Data Center Dynamics, 16 Aug 2024, reported a FJ$200 million / about US$89.4 million Google data center based on Deputy PM remarks. Grade B for public reporting; do not use for capacity.
- Data Center Dynamics, 2 Dec 2024, and Fiji Times/FBC coverage reported the groundbreaking and investment figures. Grade B unless they reproduce or link primary statements.
- Fiji Times, 17 Nov 2025, reported TFL's separate NextGen data-centre construction plan; do not conflate it with Google Natadola.
- Press and regional reports about Natadola lease, community consultation, power, and water should remain Grade B until ROC, iTLTB, EFL, WAF, Google, or FNPF primary records are verified.

Status rule:

- Use `under_construction` or `near_completion_unverified` for Natadola unless Grade A commissioning appears.
- Use `capacity_mw: null`, `racks: null`, and no tier claim unless a primary spec states it. APNIC or press references to "Tier 3" are leads, not sufficient for certification.
- Use `project_value` only with source-specific currency and date; do not average FJ$200M, US$250M, or other reported figures.

Negative-control queries:

```text
Google Natadola Fiji (commissioned OR operational OR "ready for service" OR RFS)
Google Fiji "data centre" (capacity OR MW OR racks OR "Tier III" OR "Tier 3")
site:cloud.google.com Fiji ("cloud region" OR "Google Cloud region")
site:datacenters.google (Fiji OR Natadola)
Natadola Fiji "data centre" (EFL OR power OR water OR substation)
```

## 3. Cable and Telecom Infrastructure Leads

| Lead | Division | Interpretation | Evidence path | Reliability |
|---|---|---|---|---|
| FINTEL Vatuwaqa Communications Centre | Central | International gateway/cable landing station; LEO/SAP colocation environment | FINTEL facilities page | A |
| Southern Cross Cable Network / Southern Cross NEXT | Central; Northern where Savusavu spur is documented | Operational cable landing infrastructure; not DC by default | FINTEL, Southern Cross, cable databases | A/B |
| Tonga Cable | Central | Fiji-Tonga submarine cable landing context | FINTEL, Tonga Cable | A/B |
| Interchange Cable Network 1 | Central | Suva-Port Vila cable context | FINTEL, Interchange, cable databases | A/B |
| Tui-Samoa | Central (Suva), Northern (Savusavu) | Cable landing/spur infrastructure | SSCC and FINTEL; reconcile RFS/date discrepancies by source | A for existence |
| Gondwana 2 | Central | New Caledonia-Fiji redundancy context | FINTEL and cable/trade sources | A/B |
| Google Tabua/Bulikula | Central/Western | Google-owned cable systems; Natadola and existing Fiji landing context | Google blogs, FINTEL, TFL route release, trade/cable sources | A/B |
| TFL domestic fibre / Vanua Levu fibre leads | Northern/Western/Central | Connectivity/backhaul projects; not DC unless facility named | TFL official releases, reputable local press | A/B |
| Vodafone 5G/network infrastructure | Central/Western and national | Network POP lead; not DC evidence | Vodafone official releases and local press | A/B |

Cable/telecom queries:

```text
site:fintel.com.fj ("landing station" OR cable OR colocation OR LEO OR Vatuwaqa)
site:ssccsamoa.com ("Tui Samoa" OR "Tui-Samoa") (Suva OR Savusavu)
site:submarinenetworks.com Fiji (Tabua OR Bulikula OR "SX-Next" OR Savusavu OR "Tui Samoa")
site:geocables.com Fiji cable (RFS OR Savusavu OR Suva)
FINTEL Fiji ("data centre" OR "data center" OR colocation OR "ground station")
(Savusavu OR "Vanua Levu") Fiji ("cable landing" OR fibre OR "Telecom Fiji")
```

## 4. Trade Press and Secondary Sources

| Source | URL | Fiji use | Grade |
|---|---|---|---|
| Fiji Times | https://www.fijitimes.com.fj/ | TFL NextGen construction timeline, Google/Natadola local coverage, telecom business coverage. | B |
| FBC News | https://www.fbcnews.com.fj/ | Google investment and government-facing project coverage. | B |
| Fiji Sun | https://fijisun.com.fj/ | Local business/telecom coverage. | B |
| fijivillage | https://www.fijivillage.com/ | Local telecom, digital economy, and 5G coverage. | B |
| Fiji Global News | https://fijiglobalnews.com/ | Telecom and Natadola community/consultation reporting. | B |
| Islands Business / PACNEWS | https://islandsbusiness.com/ | Regional reporting on Natadola lease, power/water/community questions. | B |
| Data Center Dynamics | https://www.datacenterdynamics.com/en/news/ | Google Fiji data-center/cable project reporting and Pacific cable context. | B |
| APNIC Blog | https://blog.apnic.net/ | Technical/regional internet-infrastructure context; treat facility/tier details as leads unless primary source linked. | B/C depending claim |
| Submarine Networks | https://www.submarinenetworks.com/ | Cable system pages and RFS dates; useful but secondary to cable owner. | B/C |
| GeoCables | https://geocables.com/ | Cable landing/RFS cross-checks; not facility proof. | C/B depending citation needs |
| SubTel Forum | https://subtelforum.com/ | Cable maps and regional context. | C/B |
| Baxtel / DataCenterMap / DataCenterPlanet / Cloudscene / WHTop | respective sites | Directory leads and negative controls only. | C |

Trade query examples:

```text
site:fijitimes.com.fj Fiji ("data centre" OR "data center" OR datacenter OR Natadola OR NextGen)
site:fbcnews.com.fj Google Fiji (data OR ICT OR cable OR Natadola)
site:islandsbusiness.com Fiji ("data centre" OR Google OR Natadola OR cable)
site:datacenterdynamics.com/en/news Fiji ("data center" OR Tabua OR Bulikula OR Natadola)
site:blog.apnic.net Fiji ("data centre" OR "cable landing" OR Natadola)
site:fijiglobalnews.com Fiji ("data centre" OR Natadola OR "Telecom Fiji")
```

## 5. Directory-to-Primary Verification Workflow

1. Use directories after the official/operator sweep, not before.
2. If a directory claims a Fiji facility, require an official operator page, facility address, permit, registry record, utility/interconnection record, or reputable press with named parties before creating inventory.
3. TFL directory entries can support a Suva locality lead only at Grade C; TFL's official page supports service existence but not the directory's address/capacity claims.
4. Check whether the advertised "Fiji" host is actually in Australia, New Zealand, Singapore, the United States, or a generic worldwide VPS platform.
5. Record SEO-only hosting pages as `seo_false_positive` with missing evidence noted.
6. Do not create a facility from IP geolocation, CDN presence, DNS, VPN endpoint, country selector, or `.fj` domain registration.

Directory/false-positive queries:

```text
site:datacentermap.com Fiji ("data center" OR colocation)
site:datacenterplanet.com Fiji ("data centre" OR "data center" OR Suva)
site:baxtel.com Fiji ("data center" OR colocation)
site:cloudscene.com Fiji ("data center" OR colocation)
site:whtop.com Fiji (hosting OR "data centre")
Fiji ("dedicated server" OR VPS OR "cloud server") -Samoa -Guam
(Suva OR Nadi) ("dedicated server" OR VPS OR hosting) -reseller
(Natadola OR Savusavu) ("data center" OR "cloud server")
```

## 6. Locality Search Recipes and Division Coverage

Universal division sweep:

```text
"{division}" Fiji ("data centre" OR "data center" OR datacenter)
"{division}" Fiji ("server" OR "server room" OR hosting OR colocation)
"{division}" Fiji ("cable landing" OR "submarine cable" OR fiber OR fibre OR POP OR "landing station")
"{division}" Fiji (telecom OR telecommunications OR internet OR wifi OR 5G)
"{division}" Fiji (power OR EFL OR substation OR generator OR hydro)
"{division}" Fiji (Google OR Natadola OR TFL OR Vodafone OR FINTEL)
```

Locality variants:

```text
(Suva OR Vatuwaqa OR Nasinu OR Nausori) Fiji (FINTEL OR "data centre" OR "Telecom Fiji" OR colocation)
(Natadola OR Sigatoka OR "Coral Coast" OR Nadroga) Fiji (Google OR "data centre" OR "data center" OR "landing station")
(Nadi OR Lautoka OR Ba OR Denarau) Fiji ("data centre" OR server OR Vodafone OR 5G OR airport)
(Savusavu OR Labasa OR "Vanua Levu") Fiji (cable OR landing OR fibre OR "Telecom Fiji")
(Levuka OR Ovalau OR Kadavu OR Lau) Fiji (internet OR satellite OR telecom)
Rotuma Fiji (satellite OR internet OR telecom OR backhaul)
```

Coverage checklist:

| Division | Industry likelihood | Assignment notes |
|---|---|---|
| Central | High | Suva/Vatuwaqa: FINTEL VCC, TFL service lead, Vodafone cloud lead, government ICT, TAF/ROC, banks and USP. Most commercial/operator DC leads start here. |
| Eastern | Low | Levuka/Ovalau, Kadavu, Lau, Lomaiviti. Expect access network, maritime/satellite, and public-service ICT references only. |
| Northern | Low/medium | Savusavu cable spur and Labasa/Vanua Levu fibre/telecom leads. Cable infrastructure, not commercial DC. |
| Rotuma | Very low | Remote dependency; expect satellite/backhaul and telecom-service references only. |
| Western | High | Natadola Google ICT facility; Nadi/Lautoka/Denarau/Sigatoka telecom and airport/tourism network leads; monitor for TFL NextGen site selection. |

## 7. Capacity Extraction Guidance

- TFL data-centre/colocation: no verified public MW, rack count, tier certificate, or floor area. Use null capacity unless TFL discloses it.
- Vodafone Fiji Hosted Cloud: no verified physical site or capacity. Use null capacity.
- FINTEL VCC: cable bandwidth, satellite gateways, UPS, cooling, and backhaul are not datacenter IT load. Do not convert them to MW.
- Google Natadola: no official IT-load figure or rack count was verified. Use source-specific project values only, not capacity.
- TFL NextGen: EOI/press do not disclose MW/racks/site in verified public snippets. Keep proposed capacity null.
- Certification/tier: do not record Tier III/Tier 3 unless Uptime Institute, operator certification, tender specs, or another primary technical document supports it.

Capacity queries:

```text
Fiji "data centre" (MW OR racks OR "Tier III" OR "Tier 3" OR Uptime)
"Telecom Fiji" "data centre" (capacity OR MW OR racks OR square OR tier)
"Vodafone Fiji" "data centre" (capacity OR MW OR racks)
Google Natadola (MW OR capacity OR racks OR "Tier III" OR "Tier 3")
TFL NextGen "data centre" (MW OR racks OR investment OR partners OR site)
Fiji "data centre" (EFL OR power OR interconnection OR grid)
```

## 8. Expected Enumeration Outcome

Expect a modest census: TFL data-centre/colocation service (operational service, exact site/capacity undisclosed), Vodafone Fiji Hosted Cloud/IaaS (operational Fiji-based cloud service, site/capacity undisclosed), FINTEL VCC cable hub and LEO/SAP colocation environment (Central), cable infrastructure at Suva/Vatuwaqa and Savusavu, Google Tabua/Bulikula/South Pacific/Central Pacific cable assets, Google Natadola ICT facility (Western, under construction or commissioning-unverified until Grade A evidence), and TFL NextGen Data Centre (proposed/EOI-stage). Digicel, USP/FNU, government server rooms, and SEO hosting pages remain leads or negatives unless primary facility evidence appears.
