# SC Explorer Industry — Seychelles Datacenter Enumeration via Operators, Connectivity Infrastructure, Trade Press, and District Query Patterns

Date: 2026-08-12. Country: **SC Seychelles**. Scope: industry/operator-led datacentre discovery across the 27 `world-manifest.jsonl` districts. Reliability grades: **A** = operator/certification/cable/cloud/government primary source that proves the claim; **B** = reputable local or trade press with named parties, dates, and places; **C** = directory, marketplace, social, SEO hosting, or unverified aggregate evidence.

---

## 0. Market shape and verified facts

- The Seychelles datacentre market is very small and telecom-led. The two confirmed commercial/operator facilities are **Airtel Seychelles Limited at Airtel House, Perseverance** and **Cable & Wireless (Seychelles) Limited Data Center 1 - Bon Espoir**.
- Airtel facility existence/address is strongly verified by **TIA** and **EPI**: Airtel House, Josephine Cafrine Road, Perseverance, P.O. Box 1358, Mahé; ANSI/TIA-942-B Constructed Facility, Rating Level 3, certificate `TIA942SC221107001`, awarded 2022-11-07 with expiry shown as 2025-11-06. Because the expiry precedes the 2026-08-12 methodology date, recheck renewal/current status before calling the certification current. Ericsson announced the 2021 launch/modernisation project for Airtel Africa's Seychelles network and core services into a new data center.
- CWS Bon Espoir is strongly verified by **Uptime Institute**: client Cable & Wireless (Seychelles) Limited; data center **Data Center 1 - Bon Espoir**; location **Anse Boileau, Seychelles**. Local press reported the US$3m project announcement in 2023, launch on 2024-09-21, and inauguration on 2024-11-22; SBC describes the site as Bon Espoir, Montagne Posee.
- No public MW/rack/sqm figures were found for either confirmed facility. Set `capacity_mw: null` unless a primary source explicitly states a value.
- No independent colocation vendor and no AWS/Azure/GCP/OCI Seychelles region were confirmed in this pass. Local VPS, hosting, managed-IT, cloud reseller, and social-media posts are leads only.
- Cable systems are central to discovery: **SEAS** at Victoria/Beau Vallon history, **PEACE** at Perseverance, and **2Africa** at North East Point. They are connectivity sites unless there is separate hosting/datacentre evidence.

---

## 1. Priority operator and infrastructure sweep

| Lead | Source route | Locality/district handling | Evidence grade and action |
|---|---|---|---|
| Airtel Seychelles data centre | TIA: `tiaonline.org/942-datacenter/airtel-seychelles-limited/`; EPI: `epi-certification.com/sites/details/1053`; Airtel contact page; Ericsson 2021 press release; Nation/SNA/SBC public-opening articles | Airtel House, Josephine Cafrine Road, Perseverance. Assign to **Ile Perseverance I** only as provisional if parcel evidence does not distinguish I/II. | **A** for facility/address and historical certification. Recheck certificate renewal/current status before describing the certification as current. |
| CWS Data Center 1 - Bon Espoir | Uptime Institute data-center and client pages; CWS official site; Nation 19023/23523/24190; SBC Bon Espoir/Montagne Posee item | Uptime says **Anse Boileau**; press says Bon Espoir/Montagne Posee. Use Anse Boileau unless SPA parcel says otherwise. | **A** for Uptime facility/location; **B** for press dates/capex unless operator/filing confirms. |
| CWS legacy Victoria infrastructure | CWS site and filings, SCRA/DICT, SEAS/PEACE/SCS material, SPA/Gazette | Victoria CBD can map to English River, Saint Louis, Bel Air, or Mont Fleuri. | Lead only until address/facility source proves a server room/DC. |
| Intelvision | Intelvision official site, SCRA/SLA, 2Africa/IFC/Vodafone material, Nation/SNA | Providence/Roche Caiman search space; also Cascade/Plaisance/Pointe Larue boundary terms. | ISP/2Africa operator is verified; dedicated DC is unconfirmed. Keep as lead. |
| Seychelles Cable Systems / SEAS / PEACE | WIOCC, EIB/AfDB, Submarine Networks, Nation, DICT/SCS references | SEAS: Victoria CLS plus Beau Vallon shore approach history. PEACE: Perseverance. | Cable facts can be A/B; not a DC without hosting/server evidence. |
| 2Africa Seychelles branch | 2Africa, IFC, Submarine Networks, Intelvision/Vodafone, Nation | North East Point; Anse Etoile vs Glacis boundary requires parcel/boundary check. | Connectivity lead, not a DC unless new operator evidence appears. |
| Government/DICT hosting | DICT, eGov/monServis, National Tender Board, Gazette | Mostly Victoria districts. | Internal facility lead; count only with tender, facility, or planning proof. |
| Financial-sector server rooms | FSA-regulated entities, banks, official procurement/building records | Mostly Victoria CBD. | Demand signal only; C until primary facility evidence. |

Operator query templates:
```text
"Airtel Seychelles" "Airtel House" "data center" OR "data centre" OR "TIA-942"
"AIRTEL Seychelles Limited" "TIA942SC221107001" OR "Rated 3"
"Ericsson" "Airtel Africa" "data center" "Seychelles"
"Cable & Wireless" "Bon Espoir" "data centre" OR "Data Center 1"
"Cable & Wireless (Seychelles) Limited" "Uptime Institute" "Bon Espoir"
"CWS" "Seychelles" "Tier IV" OR "Uptime" OR "Bon Espoir"
"Intelvision" "Providence" hosting OR server OR "data centre"
"Intelvision" "2Africa" "North East Point" OR Vodafone OR IFC
"Seychelles Cable Systems" SEAS OR PEACE "landing station"
```

---

## 2. Industry and press sources

| Source | URL | Use | Grade rule |
|---|---|---|---|
| TIA-942 registry | https://tiaonline.org/942-datacenter/airtel-seychelles-limited/ | Airtel facility/certification/address | A |
| EPI certified clients | https://www.epi-certification.com/sites/details/1053 | Airtel certificate dates, address, and renewal-status check | A |
| Uptime Institute awards | https://uptimeinstitute.com/uptime-institute-awards/datacenter/data-center-1--bon-espoir/2230 | CWS Bon Espoir facility/client/location | A |
| Ericsson | https://www.ericsson.com/en/press-releases/1/2021/airtel-africa-and-ericsson-launch-data-center-in-seychelles | Airtel data-center launch/modernisation | A for vendor-client project statement; verify address with TIA/EPI/Airtel |
| Cable & Wireless Seychelles | https://www.cwseychelles.com/ | Operator identity, services, current claims | A for company claims; still seek facility-specific pages/filings |
| Airtel Seychelles | https://www.airtel.sc/ | Address and current commercial services | A for address/operator facts |
| Intelvision | https://intelvision.sc/ | Operator identity/services and 2Africa pivots | A for company facts; C/B for inferred DC unless facility proof appears |
| WIOCC SEAS | https://www.wiocc.net/seas | SEAS cable length and Victoria CLS | A for SEAS facts |
| 2Africa official | https://www.2africacable.net/ | Consortium/system context | A for official system facts; may not name every local facility |
| IFC | https://www.ifc.org/ | 2Africa Seychelles branch financing leads | A for financing/project facts |
| Seychelles Nation | https://www.nation.sc/ | CWS dates/capex, Airtel certification story, PEACE/2Africa landings | B+; use with primary registry/operator page where possible |
| SBC | https://www.sbc.sc/ | Local TV/radio confirmation, especially CWS Bon Espoir/Montagne Posee | B |
| Seychelles News Agency | https://www.seychellesnewsagency.com/ | English wire and local ICT coverage | B |
| Submarine Networks | https://www.submarinenetworks.com/ | Cable landing timelines and operator summaries | B for article/reporting; A only if citing an operator/system primary page it hosts or quotes |
| DCD / Developing Telecoms / TechAfrica News / The Tech Capital | Industry sites | Airtel/Ericsson, regional telecom DC context | B |
| DataCenterMap / Baxtel / Cloudscene / datacenters.com | Directories | Seed discovery only | C until matched to primary |
| Social media | Facebook/Instagram/LinkedIn | Change feed for operator marketing claims | C unless the official account links to a primary document |

Press/trade query templates:
```text
site:nation.sc "Airtel" "data centre" "Seychelles"
site:nation.sc "Cable & Wireless" "Bon Espoir" "data centre"
site:sbc.sc "Bon Espoir" "data centre"
site:seychellesnewsagency.com "data centre" Seychelles Airtel OR "Cable & Wireless"
site:datacenterdynamics.com Seychelles "data center"
site:developingtelecoms.com Seychelles "data centre" OR "data center"
site:submarinenetworks.com Seychelles PEACE OR SEAS OR 2Africa
```

---

## 3. Directory-to-primary workflow

1. Seed only from directories/marketplaces: DataCenterMap, Baxtel, Cloudscene, datacenters.com, PeeringDB, CDN PoP lists, and hosting-provider pages.
2. Search exact facility/operator/address against primary domains: `tiaonline.org`, `epi-certification.com`, `uptimeinstitute.com`, `airtel.sc`, `cwseychelles.com`, `intelvision.sc`, `scra.sc`, `spa.gov.sc`, `gazette.sc`.
3. Verify district through SPA/ePlanning, parcel/address, certification registry location, or an official operator address. If only a broad locality is available, use the manifest district with an uncertainty note.
4. Verify status with launch/inauguration/certification/operational service evidence. Use `announced` or `lead` if only a planned project or press statement exists.
5. Keep directory-only entries as Grade C; do not merge them into confirmed facilities unless name/address/operator line up.

Negative-control queries:
```text
"Seychelles" colocation OR "co-location" provider
"Seychelles" "cloud hosting" OR VPS OR "dedicated server"
"Seychelles" "AWS" OR Azure OR "Google Cloud" OR OCI "data centre"
"Seychelles" "Starlink" "data center" OR gateway
"SC" "data center" -Seychelles
```

---

## 4. District recipes for all 27 divisions

Use the exact manifest spellings in records. Add accented/local variants only in queries.

Universal district query:
```text
"{district}" "Seychelles" "data centre" OR "data center" OR datacentre OR "server room" OR colocation
"{district}" "Seychelles" "network operations" OR telecom OR "landing station" OR "cable station"
"{district}" "Seychelles" generator OR UPS OR cooling OR substation OR "backup power"
site:nation.sc "{district}" "data centre" OR telecom OR server
site:sbc.sc "{district}" "data centre" OR telecom OR server
site:spa.gov.sc "{district}" server OR data OR telecom OR generator
site:gazette.sc "{district}" server OR telecom OR "data centre" OR substation
```

High-yield district variants:
```text
"Ile Perseverance" OR Perseverance "Airtel House" OR "TIA-942" OR PEACE
"Anse Boileau" "Bon Espoir" OR "Montagne Posee" "Cable & Wireless"
"Bon Espoir" "data centre" Seychelles
"Anse Etoile" OR Glacis "North East Point" "2Africa" OR Intelvision
"Roche Caiman" OR Cascade OR Plaisance OR Providence Intelvision OR hosting OR server
"English River" OR Victoria OR "Ile du Port" OR "New Port" "landing station" OR CWS OR SEAS
"Mont Fleuri" "Centre for Excellence in ICT" OR "data centre" OR UniSey
"Baie Sainte Anne" OR "Grand Anse Praslin" OR "La Digue" fibre OR "Cable & Wireless" OR Airtel OR Intelvision
```

District checklist and expected handling:

| District | Expected yield | Notes |
|---|---|---|
| Anse aux Pins | Low/medium | Bon Espoir boundary false positives; require parcel proof. |
| Anse Boileau | High | CWS Bon Espoir is currently assigned here by Uptime. |
| Anse Etoile | High | North East Point / 2Africa search space. |
| Au Cap | Medium | Bon Espoir boundary false positives; verify against Anse Boileau/Anse aux Pins. |
| Anse Royale | Low | Generic sweep only. |
| Baie Lazare | Low | Generic sweep only. |
| Baie Sainte Anne | Medium | Praslin PoPs/fibre/cable centres only unless DC proof appears. |
| Beau Vallon | Medium | SEAS shore approach history; not a DC. |
| Bel Air | Medium | Victoria CBD banking/government/CWS leads. |
| Bel Ombre | Low | Generic sweep only. |
| Cascade | Medium | Providence/industrial boundary searches. |
| Glacis | High | North East Point / 2Africa search space. |
| Grand Anse Mahe | Low | Generic sweep only. |
| Grand Anse Praslin | Medium | Praslin PoPs/fibre; no DC without primary proof. |
| La Digue | Medium | Fibre/PoP references; no DC without primary proof. |
| English River | High | Victoria/New Port/Ile du Port, SEAS/CWS/SCS leads. |
| Mont Buxton | Low | Greater Victoria fringe. |
| Mont Fleuri | Medium | UniSey/ISCEICT historical data-centre lead; current status needs proof. |
| Plaisance | Medium | Providence and Greater Victoria boundary searches. |
| Pointe Larue | Medium | Airport/industrial telecom and power leads. |
| Port Glaud | Low | Generic sweep only. |
| Saint Louis | Medium | Victoria CBD/CWS/banks/government leads. |
| Takamaka | Low | Generic sweep only. |
| Les Mamelles | Low | Greater Victoria fringe. |
| Roche Caiman | High | Providence Industrial Estate and Intelvision lead. |
| Ile Perseverance I | High | Airtel DC, TIA/EPI renewal check, and PEACE landing; avoid duplicate with district II. |
| Ile Perseverance II | High | Airtel/PEACE boundary check; use only if parcel proves district II. |

---

## 5. Seed records to validate during enumeration

| Seed | Status | Capacity | Developer/operator | Grade | Sources to use |
|---|---|---|---|---|---|
| Airtel Seychelles Data Centre | Operational | null | AIRTEL Seychelles Limited / Airtel Africa; Ericsson turnkey partner | A | TIA, EPI renewal status, Ericsson, Airtel contact page, Nation/SNA/SBC |
| CWS Data Center 1 - Bon Espoir | Operational | null | Cable & Wireless (Seychelles) Limited | A | Uptime Institute, CWS, Nation, SBC, SPA/ePlanning |
| CWS Victoria legacy exchange/server rooms | Lead | null | Cable & Wireless (Seychelles) Limited / Seychelles Cable Systems | B/C | CWS docs, SCRA/DICT, SEAS/PEACE material, SPA/Gazette |
| Intelvision Providence hosting/network site | Lead | null | Intelvision | B/C | Intelvision official site, SLA/SCRA, 2Africa/IFC, SPA Providence |
| SEAS Victoria CLS / Beau Vallon shore approach | Connectivity site | null | SCS/CWS/WIOCC consortium context | A for cable | WIOCC, EIB/AfDB, Nation historical records |
| PEACE landing at Perseverance | Connectivity site | null | Seychelles Cable Systems / CWS context | A/B for cable | Submarine Networks, AfDB/EIB, Nation, DICT/SCS |
| 2Africa North East Point landing | Connectivity site | null | Intelvision/Vodafone; IFC-financed branch | A/B for cable | 2Africa, IFC, Submarine Networks, Nation/SNA |
| India-Seychelles Centre for Excellence in ICT data centre | Historical institutional lead | null | University of Seychelles / ISCEICT | B until current proof | Nation 2011, UniSey/NTB/DICT follow-up |

---

## 6. Capacity and reliability extraction

Record these fields when available: certification body, tier/rating level, certificate ID, awarded/expiry dates, capex, launch/inauguration date, address, district, operator, customer type, public services offered, and connectivity/cable adjacency.

Do not derive capacity from:
- TIA/Uptime tier or rating.
- CWS US$3m Bon Espoir capex or R1.1bn five-year programme.
- SEAS/PEACE/2Africa cable bandwidth or cable capex.
- Claims such as "world-class", "state-of-the-art", "Tier 3", or "Tier IV" without a registry entry.

Capacity query templates:
```text
"Airtel Seychelles" "data centre" rack OR racks OR sqm OR MW OR MVA OR kVA
"Bon Espoir" "data centre" rack OR racks OR sqm OR MW OR MVA OR kVA
"Data Center 1 - Bon Espoir" "Uptime" "Tier" OR "constructed facility"
"AIRTEL Seychelles Limited" "TIA-942" "certificate" OR "Rated 3"
"Seychelles" "data centre" generator OR UPS OR cooling OR redundancy
```

Reliability grading rules:
- **A**: TIA/EPI/Uptime/operator/government source proves facility, address, status, or certification.
- **B**: press/trade source supports dates, capex, launch, public remarks, or cable event but does not independently prove a certified facility/address.
- **C**: directory/social/hosting page only, or a service page that does not show physical facility ownership/location.

Pitfalls: do not duplicate Perseverance I/II; do not let CWS "first data centre" marketing override Airtel's earlier primary evidence; do not count cable landings as datacentres; keep all 27 districts in the sweep even where prior batches found no projects; always include `Seychelles` in searches to avoid South Carolina false positives.
