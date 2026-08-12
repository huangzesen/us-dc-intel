# FM Explorer Industry - Federated States of Micronesia Datacenter Methodology

Date verified: 2026-08-12

Scope: Federated States of Micronesia (FM/FSM). Division coverage required by `world-manifest.jsonl`: Kosrae, Pohnpei, Chuuk, Yap.

Use this file for the industry/vendor pass: telecom operators, wholesale cable operator, satellite providers, cloud/CDN providers, trade press, peering/network directories, and data-center directories. Pair with `explorer-official.md` before creating or rejecting any facility record.

## Industry Conclusion

No industry source verified a live carrier-neutral or commercial colocation data center in FSM. The market is primarily telecom infrastructure:

- FSMTC: incumbent retail operator with Pohnpei international gateway/HANTRU-1 facilities and FTTP in Pohnpei, Weno/Chuuk, and Yap Proper.
- FSMTCC/CableCorp/OAE: wholesale cable and open-access fiber operator with landing stations/central-office facilities in the states and an explicit wholesale colocation/backhaul product design.
- iBoom/Boom: Yap competitor with licensed terrestrial cable, international gateway, and satellite earth-station facilities.
- Kacific, MCS Pohnpei, Starlink, CPUC, iSolutions, FSMtech: connectivity/service-provider leads; do not count as data centers unless a facility-specific primary source appears.
- Digital FSM: official project pathway for a government data center/FSM-Cloud and for private-sector-operated green data-center hosted digital services by 2027. Treat as project leads unless implementation records name a location/operator.

The best near-term watch items are CableCorp/OAE colocation becoming live, Digital FSM/FSM-Cloud procurement or commissioning records, and any private-sector green data center named under World Bank P170718.

## Grading for Industry Pass

- Grade A: operator/vendor official pages and PDFs; TRA register/market pages; World Bank project documents; FCC/US government records; cloud-provider official infrastructure pages.
- Grade B: NEC/AIFFP/East Micronesia Cable project pages for EMC, Submarine Networks, Data Center Dynamics, Pacific Island Times, RNZ Pacific, APNIC, World Teleport Association.
- Grade C: PeeringDB and BGP directories for routing context, data-center directories, web-hosting directories, LinkedIn, job posts, social posts not from the operator, and reseller marketing.

Downgrade aggressively. A "communications facility", "gateway", "earth station", or "central office" is not a data center unless the source says colocation, hosting, data center, cloud, racks, power/cooling for third-party equipment, or comparable facility language.

## Operator and Vendor Leads

### FSMTC

- Official site: https://fsmtc.fm/
- HANTRU-1 upgrade: https://www.fsmtc.fm/news/fsmtc-announces-completion-hantru-1-upgrade
- Chuuk-Pohnpei outage: https://www.fsmtc.fm/news/outage-chuuk-pohnpei-submarine-cable-system
- TRA register entry: https://tra.fm/public-register-of-licences/
- PeeringDB lead: https://www.peeringdb.com/org/36890

Industry use:

- Grade A for FSMTC as a licensed operator of cable landing station and international gateway facilities.
- Grade A for the 2021 HANTRU-1 upgrade between Pohnpei and Guam.
- Grade C/B only for PeeringDB routing/ASN context; never use it alone as a facility source.
- No verified FSMTC public colocation product was found. "Dedicated Internet Access", domain registration, mail, or web-hosting directory listings are service leads, not data-center proof.

Queries:

```text
site:fsmtc.fm "colocation" OR "hosting" OR "data center" OR "server"
site:fsmtc.fm "HANTRU-1" "Pohnpei" "Guam"
"FSMTC" "international gateway" "Pohnpei"
"FSMTC" "PeeringDB" OR "ASN"
```

### FSMTCC / CableCorp / OAE

- Official site: https://fsmcable.com/
- State pages: https://fsmcable.com/states/
- Wholesale overview PDF: https://fsmcable.com/wp-content/uploads/2020/11/High-level-OAE-overview-for-RSP-2020.pdf
- Interstate/international services PDF: https://fsmcable.com/wp-content/uploads/2020/11/OAE-Interstate-and-International-Connectivity-Services-November-2020.pdf
- TRA market page: https://tra.fm/market-entry-and-information-2/
- NEC EMCS completion: https://www.nec.com/en/press/202605/global_20260515_02.html

Industry use:

- Grade A for OAE/FSMTCC wholesale facilities, central-office exchange design, and colocation/backhaul product intent.
- Grade A for FSMTCC headquarters: Ocean View Plaza (East Wing), Suite 15, Pohnpei, FM 96941.
- Grade A for per-state cable/fiber progress on FSMTCC state pages where the claim is about FSMTCC's own network.
- Grade A/B for NEC and EMC project pages confirming EMCS completion, handover, route, and cable-landing-station purpose.
- Treat "colocation" as wholesale telecom colocation at exchanges/central offices until a live tariff or service order confirms availability.

Queries:

```text
"FSMTCC" OR "CableCorp" OR "OAE" "colocation"
site:fsmcable.com "central office" OR "exchange" OR "co-location"
site:fsmcable.com "landing station" "Pohnpei" OR "Chuuk" OR "Yap" OR "Kosrae"
site:nec.com "East Micronesia Cable System" "FSMTCC"
```

### iBoom / Boom

- Official site: https://www.iboom.io/
- TRA register: https://tra.fm/public-register-of-licences/
- Pacific Island Times lead: https://www.pacificislandtimes.com/post/same-slogan-new-cable-why-economic-development-promises-keep-falling-short-in-micronesia

Industry use:

- Grade A for Boom! Inc. licensing from TRA: P.O. Box 215, Colonia Yap, FM 96943; licensed for terrestrial cable, international gateway, and satellite earth-station facilities; mobile/fixed wireless spectrum in Yap.
- Grade A for iBoom official services if the current site documents FTTH/mobile service.
- Grade B for Pacific Island Times context about Yap market competition.
- No verified data-center or colocation product. Record as a Yap telecom facility lead only.

Queries:

```text
site:iboom.io Yap "fiber" OR "FTTH" OR "mobile"
"Boom! Inc." "Colonia Yap" "international gateway"
"iBoom" "data center" OR colocation OR "server"
```

### Satellite and Wireless Providers

| Provider | Verified FM role | Industry handling |
|---|---|---|
| Starlink Pacific Islands LLC | TRA operating license effective 2024-03-19; mobile satellite frequency license FL-MS-001 effective 2025-10-01 | Connectivity only. The TRA menu's S-band announcement URL is broken; use the register. |
| Kacific Broadband Satellite(s) International Ltd. | TRA individual operating license effective 2020-07-01; satellite/service-provider role | Connectivity only unless a local gateway/earth-station facility is named. |
| MCS Pohnpei, Inc. | TRA class operating license effective 2020-09-16; not authorized to construct/own/operate a specified communications network | Service lead only; not a facility. |
| CPUC | TRA individual operating license in Chuuk; terrestrial cable/gateway/satellite earth-station facility authorization | Telecom lead in Chuuk; verify any actual facility with CPUC/source documents. |
| iSolutions Micronesia Ltd. | TRA individual and spectrum licenses in Weno, Chuuk | Telecom lead in Chuuk; Facebook-only site is Grade C unless source is an official operator post. |
| FSMtech, Inc. | TRA class operating license in Kolonia/Pohnpei; not authorized to construct/own/operate a specified communications network | Service lead only; not a facility. |

Satellite/wireless queries:

```text
site:tra.fm Starlink "FL-MS-001" OR "Mobile Satellite"
"Starlink Pacific Islands" "Federated States of Micronesia" "gateway"
"Kacific" "Pohnpei" OR "Kosrae" OR "Chuuk" OR "Yap"
"MCS Pohnpei" "satellite" "Micronesia"
"iSolutions Micronesia" Weno Chuuk "data center" OR "server"
```

### Hyperscaler and CDN Absence

Official pages to re-check:

- AWS regions: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html
- Azure regions: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud locations: https://cloud.google.com/about/locations
- Oracle OCI regions: https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm
- Cloudflare network: https://www.cloudflare.com/network/
- Akamai connected cloud/global locations: https://www.akamai.com/site/en/locations.jsp

Current result: no verified FM cloud region, local zone, or CDN PoP. Do not infer a PoP from global service availability, DNS, latency tests, or customer routing.

Queries:

```text
site:aws.amazon.com OR site:docs.aws.amazon.com "Micronesia" "region" "AWS"
site:learn.microsoft.com/azure "Micronesia" "Azure region"
site:cloud.google.com "Micronesia" "Google Cloud" "locations"
site:docs.oracle.com/iaas "Micronesia" "region"
site:cloudflare.com/network "Micronesia" OR "Pohnpei"
site:akamai.com "Micronesia" OR "Pohnpei"
```

## Trade Press and Directories

Use these for lead generation and dates, then backfill with official/operator evidence:

- NEC official EMCS completion: https://www.nec.com/en/press/202605/global_20260515_02.html
- East Micronesia Cable project: https://www.eastmicronesiacable.com/
- AIFFP EMC pages: https://www.aiffp.gov.au/
- Submarine Networks: https://www.submarinenetworks.com/
- Data Center Dynamics: https://www.datacenterdynamics.com/
- Pacific Island Times: https://www.pacificislandtimes.com/
- RNZ Pacific: https://www.rnz.co.nz/international/pacific-news
- Submarine Cable Map: https://www.submarinecablemap.com/
- PeeringDB: https://www.peeringdb.com/
- DataCenterMap: https://www.datacentermap.com/
- Cloudscene: https://cloudscene.com/
- WHTop FM directory: https://www.whtop.com/directory/country/fm

Directory rule: absence from DataCenterMap/Cloudscene is only a weak negative signal. Presence in WHTop or hosting directories is Grade C and usually identifies a web-hosting brand, not a physical data center.

Trade/directory queries:

```text
"Federated States of Micronesia" "data center" OR "datacenter" OR colocation -ship -registry
"Pohnpei" "data center" OR "colocation" OR "server hosting"
"Weno" "Chuuk" "data center" OR "colocation" OR "server"
"Colonia" "Yap" "data center" OR "colocation" OR "gateway"
"Kosrae" "East Micronesia Cable" "landing station" OR "data center"
site:datacenterdynamics.com "Federated States of Micronesia" OR "East Micronesia Cable"
site:submarinenetworks.com "East Micronesia Cable" OR "EMCS"
site:datacentermap.com Micronesia OR Pohnpei OR Yap OR Chuuk OR Kosrae
site:cloudscene.com Micronesia OR Pohnpei OR Yap OR Chuuk OR Kosrae
```

## Per-State Industry Workflow

| State | Industry yield | Vendor route | Record guidance |
|---|---|---|---|
| Kosrae | Medium and rising after EMCS | East Micronesia Cable, NEC, AIFFP, FSMTCC Kosrae page, Kacific/Starlink only as connectivity context, KUA power | Record EMCS cable landing station as telecom infrastructure. Record Digital FSM/green-DC leads only if tied to Kosrae by a later primary source. No verified commercial DC. |
| Pohnpei | High relative to FSM | FSMTC, FSMTCC/OAE, TRA, World Bank P170718, DFO/DTCI, PeeringDB for network context | Record HANTRU-1/gateway, C-P/EMCS landing, OAE central-office colocation lead, and Digital FSM government data-center/FSM-Cloud lead. Distinguish Kolonia telecom facilities from Palikir government facilities. |
| Chuuk | Medium, Weno-focused | FSMTCC Chuuk page, FSMTC outage notices, TRA register for CPUC/iSolutions, CPUC site | Record C-P cable landing/operations and Weno FTTP/head-end telecom infrastructure. CPUC/iSolutions are telecom leads only. No verified commercial DC. |
| Yap | Medium | FSMTCC Yap page, TRA register, iBoom site, Pacific Island Times, YSPSC | Record Yap Spur/SEA-US landing and iBoom licensed network/gateway/earth-station facilities. Treat iBoom as ISP/mobile competition, not colocation. No verified commercial DC. |

State query template:

```text
"{State}" "Federated States of Micronesia" "data center" OR "datacenter" OR "colocation" OR "server hosting"
"{State}" "FSMTCC" OR "CableCorp" OR "OAE" "landing station" OR "central office"
"{State}" "FSMTC" "gateway" OR "FTTP" OR "submarine cable"
"{State}" "Starlink" OR "Kacific" OR "earth station"
```

## Facility Classification

- `operational_telecom`: cable landing station, international gateway, central office, FTTP head-end, satellite earth station, or licensed communications facility with official/operator evidence.
- `planned_telecom_colocation`: OAE/CableCorp central-office colocation/backhaul where evidence is design, pricing, or market-entry material but no live service order is found.
- `planned_government_dc`: Digital FSM government data center/FSM-Cloud where source is ESMP/project documentation but no commissioned facility is named.
- `planned_private_green_dc`: World Bank P170718 private-sector-operated green-data-center hosting target, only until providers/sites are named.
- `no_projects`: use for a state when searches find only connectivity services or unsourced server-room inference.

## Watch List

Re-run these before final project extraction:

```text
site:dofa.gov.fm "green data centers" OR "FSM-Cloud" OR "data center"
site:tci.gov.fm "FSM-Cloud" OR "Secure Government Network" OR "Data Center"
site:fsmcable.com "co-location products" OR "colocation products" OR "service provider operations manual"
site:tra.fm "Notice of New Infrastructure" "CableCorp" OR "data center"
"Digital Federated States of Micronesia Project" "green data centers" "operator"
"East Micronesia Cable System" "ready for service" "FSMTCC"
```

If a future result names a private operator, site, tariff, rack/power specification, or commissioning date, promote it only with primary evidence and assign it to one of the four FSM states.
