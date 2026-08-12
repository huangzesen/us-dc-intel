# MU Explorer Industry - Mauritius Datacenter Enumeration via Operators, Colocation, Connectivity, Directories, and Trade Press

Date: 2026-08-12. Country: **MU Mauritius**. Scope: operator-led and industry-source methodology across all 12 manifest divisions: Agalega Islands; Black River; Cargados Carajos Shoals; Flacq; Grand Port; Moka; Pamplemousses; Port Louis; Plaines Wilhems; Rodrigues Island; Riviere du Rempart; Savanne.

Reliability grades: **A** = operator, certification registry, regulator, government, cable/IXP primary, or official cloud-region page proves the exact claim. **B** = reputable trade/local press or vendor/designer source with named parties and locality. **C** = directory, marketplace, social page, SEO hosting page, or aggregate without primary facility evidence. Grade each attribute separately.

---

## 0. Market Shape and Verified Corrections

- Mauritius has a small but real colocation/government-DC market. The public inventory is concentrated in **Port Louis**, **Ebene/Reduit (Moka)**, **Arsenal/Terre Rouge (Pamplemousses)**, **Rose-Belle (Grand Port)**, and **Plaines Wilhems**. Low-yield divisions still require explicit negative sweeps.
- Corrected certification baseline:
  - **Emtel Data Centre**: EPI and TIA list ANSI/TIA-942-B Facility / Constructed Facility **Rated 3**, cert **TIA942MU230924001**, expiry **2026-09-23**.
  - **Mauritius Telecom Rose Belle Data Centre, Phase 1**: Uptime Institute Mauritius listing shows **Tier IV Certification of Design Documents** and **Tier IV Certification of Constructed Facility**.
  - **Bhumishq Teleserve LTD Cybercity Data Centre, Ebene**: Uptime Institute Mauritius listing shows **Tier IV Certification of Design Documents**.
- Operator capacity claims now have better primary support than the draft allowed:
  - Emtel primary page states **dual 1 MW transformers** and **N+1 backup generators**. Do not automatically convert transformer rating to IT load.
  - MT/my.t and rbdc.mu state Rose Belle has **1,500 sq m secured rack space**, **400+ racks**, and **3 MW power**.
- No official AWS, Azure, Google Cloud, or OCI Mauritius public cloud region was found on official region/location lists. Treat local cloud/sovereign-cloud offerings as local platforms unless a hyperscaler official page names Mauritius.
- Cable systems are industry leads, not datacentres. METISS is special because Emtel and press sources state the Mauritius landing point is Emtel's Arsenal data centre.

---

## 1. Priority Operator Sweep

| Lead | Source route | Locality/division | Grade and action |
|---|---|---|---|
| Emtel Data Centre | https://www.epi-certification.com/sites/map/Mauritius ; https://tiaonline.org/942-datacenter/emtel-data-centre/ ; https://www.emtel.com/business/data-centre ; METISS press | B11 Plaine des Papayes Road, Arsenal, **Pamplemousses** | **A** for address/cert/operator service. Record METISS/SAFE/LION/LION2 connectivity. Use transformer/generator text as operator claim, not IT load. |
| MT Rose Belle Data Centre / RBDC | https://www.myt.mu/business/colocation/ ; https://rbdc.mu/ ; Uptime country/Rose Belle pages; MT annual reports/social/press | Rose-Belle, **Grand Port** | **A** for MT page capacity and Uptime Tier IV design+constructed. Track government-data hosting and expansion. |
| MT Rose Hill Tier III / RHDC | https://www.myt.mu/business/ict-bpo ; DatacenterPlanet seed | Rose Hill, **Plaines Wilhems** | **A** for MT claim that Rose Hill Tier III hosts ICT/BPO workloads; **C** for directory details until primary address page found. |
| Bhumishq / Cybercity Data Centre | Uptime Mauritius country page; DataCenterMap Bhumishq; Bhumishq/Facebook/company pages | Ebene/Cybercity, **Moka** | **A** for Uptime Tier IV design-cert in Ebene; **C** for Mindspace/45 Wall Street/500 sq m until primary confirms. |
| Rogers Capital Ebene DC | https://technology.rogerscapital.mu/services/cloud-and-data-centre-services/ ; MIXP; PeeringDB; ICTA | Ebene, **Moka** | **A/B**. Rogers states carrier-neutral DC in Ebene and MIXP hosted there. Verify Cyber Tower/MIXP node details with PeeringDB and planning records. |
| Rogers Capital La Tour Koenig DC | Rogers primary page; DataCenterMap/DataCenterPlatform | La Tour Koenig / Informatics Park; assign only after parcel check, likely **Port Louis market** | **A** for Rogers-stated La Tour Koenig data centre; **C** for directory address/detail. |
| Rogers Capital Port Louis DC | DataCenterMap; ICTA; Rogers pivot | 59 Mere Barthelemy St, **Port Louis** | **C** facility detail plus **A** licence/operator. Need Rogers primary or BLUP. |
| Rogers Capital Les Cascades DC | DataCenterMap; Rogers pivot | Les Cascades Bldg / Edith Cavell St, **Port Louis** | **C** facility detail plus **A** licence/operator. Need Rogers primary or BLUP. |
| Harel Mallac Technologies / MCS Datacenter 02 | DataCenterMap; hmtechnologies.mu; Telecom Review Africa | 18 Edith Cavell St, **Port Louis** | **B/C**. Primary company identity, but facility/address mostly directory/trade. |
| BIRGER Candos Recovery Centre / QB DC1 | https://www.birger.technology/ ; DataCenterMap; ColocationM | Candos/Quatre Bornes, **Plaines Wilhems** | **C/B**. BIRGER site proves technology/security/resiliency company; facility details need primary. |
| Aphelion DC3 | DataCenterMap/UPSTACK; Aphelion search; JinFei/Riche Terre status press | Noah Wealth Center, JinFei Smart City, Terre Rouge, **Pamplemousses** | **C** until operator primary/planning proof. Do not assign to Port Louis from directory market label. |
| Government Online Centre | MITCI GOC page; PeeringDB/MIXP | **Port Louis** | **A** state DC with 80-rack capacity and server co-location. |
| Government Data Centre / sovereign cloud / DR site | MITCI Blueprint material; public procurement RFI MITCI/RFI/01/2025-26 | TBD | **A** for policy/procurement lead; location null. |
| CEB DR centre | CEB/public procurement searches | TBD | **B lead** only; internal DR/procurement does not prove public colocation. |
| MIXP | https://www.mixp.org/ ; https://www.peeringdb.com/ix/1508 | Ebene + GOC node | **A** for IXP; not a datacentre. |

Operator queries:
```text
"Emtel" "data centre" Arsenal "TIA942MU230924001" OR "Rated 3"
"Emtel" "data centre" "dual 1MW transformers" OR METISS OR SAFE OR LION
"Rose Belle Data Centre" OR RBDC Mauritius Telecom "3 MW" OR "400 racks"
site:uptimeinstitute.com/uptime-institute-awards/country/id/MU Mauritius "Rose Belle" OR Bhumishq
"Mauritius Telecom" "Rose Hill Tier III" OR RHDC OR "ICT/BPO"
"Rogers Capital" "data centre" Ebene OR "La Tour Koenig" OR MIXP
"Bhumishq" "Cybercity Data Centre" OR "45 Wall Street" Mauritius
"Harel Mallac" "MCS Datacenter 02" OR "Edith Cavell"
"BIRGER" Candos "Recovery Centre" OR "Quatre Bornes" "data centre"
"Aphelion DC3" "Noah Wealth Center" OR "JinFei" OR "Terre Rouge"
"Government Online Centre" Mauritius "80-rack" OR "co-location"
```

---

## 2. Industry Source List

| Source | URL | Use | Grade rule |
|---|---|---|---|
| EPI TIA-942 Mauritius map | https://www.epi-certification.com/sites/map/Mauritius | Emtel address, rating, expiry | A |
| TIA Online Emtel | https://tiaonline.org/942-datacenter/emtel-data-centre/ | Emtel certificate ID/status/dates | A |
| Uptime Mauritius | https://uptimeinstitute.com/uptime-institute-awards/country/id/MU | MT Rose Belle and Bhumishq certification entries | A |
| Uptime Rose Belle | https://uptimeinstitute.com/uptime-institute-awards/datacenter/rose-belle-data-centre-phase-1/784 | MT Rose Belle project evidence | A |
| Emtel business DC | https://www.emtel.com/business/data-centre | Arsenal service, connectivity, power redundancy claims | A for operator claims |
| MT/my.t colocation | https://www.myt.mu/business/colocation/ | RBDC capacity/services | A for operator claims |
| RBDC | https://rbdc.mu/ | Rose Belle facility capacity/services | A/B; verify ownership linkage to MT |
| MT/my.t ICT/BPO | https://www.myt.mu/business/ict-bpo | Rose Belle Tier IV and Rose Hill Tier III mention | A for MT claim |
| Rogers Capital tech | https://technology.rogerscapital.mu/services/cloud-and-data-centre-services/ | Ebene and La Tour Koenig DCs; MIXP hosting | A for operator claims |
| ICTA Commercial Licensees | https://www.icta.mu/licences-issued/ | Operator telecom licence pivots | A for licence only |
| MITCI GOC | https://mitci.govmu.org/mitci/government-online-centre/ | Government Online Centre state DC | A |
| Public Procurement RFI | https://publicprocurement.govmu.org/publicprocurement/?p=4897 | Sovereign cloud RFI | A for procurement notice |
| MIXP | https://www.mixp.org/ | Mauritius Internet Exchange | A for IXP |
| PeeringDB MIXP | https://www.peeringdb.com/ix/1508 | IXP node/member validation | A/B |
| DataCenterMap Mauritius | https://www.datacentermap.com/mauritius/ | Seed inventory and addresses | C until primary matched |
| DataCenterPlatform / ColocationM / UPSTACK / ColoMap / DC Hub | various | Discovery, ecosystem, capacity clues | C unless independently confirmed |
| Telecom Review Africa | https://www.telecomreviewafrica.com/articles/features/12397-sublime-seas-to-storage-sphere-mauritius-expands-hyperscale-data-hub/ | Market inventory/trade context | B |
| DCD | https://www.datacenterdynamics.com/ | MT T3/T4 and cable reporting | B |
| Submarine Networks | https://www.submarinenetworks.com/ | T3/METISS/cable reporting | B, A only when quoting operator announcement |
| TeleGeography Submarine Cable Map | https://www.submarinecablemap.com/ | Landing points | B |
| L'Express / Le Mauricien / Defi Media | local press | MT/government/JinFei/local project context | B when named/date/locality present |
| AWS/Azure/GCP/OCI official region pages | official provider URLs | Negative control for hyperscaler regions | A |

Press/trade queries:
```text
site:telecomreviewafrica.com Mauritius "data centre" OR "data hub" OR "Rose Belle"
site:datacenterdynamics.com Mauritius "data centre" OR T3 OR T4 OR SAFE
site:lexpress.mu "Rose-Belle" "data centre" OR "cloud souverain"
site:lemauricien.com JinFei OR "Terre Rouge" "data centre" OR "smart city"
site:defimedia.info Mauritius "data centre" OR "sovereign cloud"
"Mauritius" "hyperscale" "data centre" "Ebene" OR "Port Louis"
```

---

## 3. Directory-to-Primary Workflow

1. Seed from directories only when they provide operator/name/address: DataCenterMap, DataCenterPlatform, ColocationM, UPSTACK, ColoMap, DC Hub, Baxtel, Cloudscene.
2. Match exact operator and address to primary domains: `emtel.com`, `myt.mu`, `telecom.mu`, `rbdc.mu`, `technology.rogerscapital.mu`, `birger.technology`, `hmtechnologies.mu`, `icta.mu`, `mitci.govmu.org`, `epi-certification.com`, `tiaonline.org`, `uptimeinstitute.com`.
3. Assign division by physical location:
   - Ebene/Reduit/Cybercity = **Moka**
   - Arsenal/Terre Rouge/Riche Terre/JinFei = **Pamplemousses**
   - Rose-Belle/Gros Billot = **Grand Port**
   - Rose Hill/Candos/Quatre Bornes = **Plaines Wilhems**
   - Edith Cavell/Mere Barthelemy/GOC central Port Louis = **Port Louis**
   - Baie Jacotet/Bel Ombre cable station = **Savanne**
4. Upgrade to Grade A only when primary/certification/operator evidence proves the same facility or claim. Keep directory-only capacity, racks, coordinates, tenants, and services as Grade C.
5. Retain every unresolved lead. Downgrade and annotate missing evidence instead of deleting.

Negative-control queries:
```text
"Mauritius" "AWS region" OR "Azure region" OR "Google Cloud region" OR "OCI region"
"Mauritius" VPS OR "dedicated server" OR "cloud hosting" -datacentre -datacenter
"Mauritius" Starlink "data center" OR gateway
"Mauritius" 2Africa OR Equiano OR LION3 landing
"Port Louis" "data center" -Mauritius
"MU" "data center" -Mauritius
```

---

## 4. Division Recipes

Universal division query:
```text
"{division}" Mauritius "data centre" OR "data center" OR datacentre OR "server room" OR colocation
"{division}" Mauritius "network operations" OR telecom OR "landing station" OR "cable station"
"{division}" Mauritius generator OR UPS OR cooling OR substation OR "backup power"
site:datacentermap.com/mauritius "{division}" OR "{locality}"
site:lexpress.mu "{division}" "data centre" OR telecom OR server
site:lemauricien.com "{division}" "data centre" OR telecom OR server
site:icta.mu "{division}" licence OR "data centre" OR telecom
"{division}" "centre de donnees" OR "salle de serveurs"
```

| Division | Expected yield | Industry handling |
|---|---|---|
| Agalega Islands | None | Search MT/Emtel coverage, island projects, and government communications only; no public DC evidence. |
| Black River | Low | Cap Tamarin, Tamarin, Flic en Flac, Black River smart/office projects; no confirmed DC. |
| Cargados Carajos Shoals | None | St Brandon/Cargados/Saint Brandon telecom sweep; no public DC evidence. |
| Flacq | Low | Centre de Flacq, Deep River Beau Champ/solar, telecom exchanges; no confirmed DC. |
| Grand Port | High | **MT Rose Belle/RBDC**; airport/Plaine Magnien/Mon Tresor leads; government-data hosting. |
| Moka | High | **Bhumishq Cybercity**, **Rogers Ebene DC/MIXP**, Cyber Tower 1, Mindspace, Wall Street, MITCI/CEB/EDB offices. |
| Pamplemousses | High | **Emtel Arsenal**, **Aphelion DC3** lead, METISS/Terre Rouge, Baie du Tombeau, Riche Terre/JinFei/Beau Plan. |
| Port Louis | High | **GOC**, Rogers Port Louis/Les Cascades, Harel Mallac/MCS, MIXP GOC node, downtown telecom facilities. |
| Plaines Wilhems | Medium/high | **MT Rose Hill Tier III/RHDC**, **BIRGER Candos**, Quatre Bornes/Rose Hill/Beau Bassin/Curepipe/Vacoas exchanges. |
| Rodrigues Island | Medium | MARS landing at Grand Baie; Port Mathurin PoPs; no public DC without hosting/server evidence. |
| Riviere du Rempart | Low | Grand Baie business/tourism corridor; no confirmed DC. |
| Savanne | Medium | Baie Jacotet SAFE/MARS/T3 cable cluster; connectivity only, not DC. |

High-yield locality queries:
```text
Ebene OR Reduit OR Cybercity "data centre" OR Bhumishq OR MIXP OR "Cyber Tower"
"Rose Belle" OR "Rose-Belle" RBDC "data centre" OR "Tier IV" OR "3 MW"
Arsenal OR "Plaine des Papayes" Emtel "data centre" OR METISS
"Terre Rouge" OR "Riche Terre" Aphelion OR JinFei OR "Noah Wealth"
"Rose Hill" "Tier III" "Mauritius Telecom" OR RHDC
"Quatre Bornes" OR Candos BIRGER OR "recovery centre" OR "data centre"
"Port Louis" "Mere Barthelemy" OR "La Tour Koenig" OR "Les Cascades" OR "Edith Cavell"
"Baie Jacotet" "landing station" OR SAFE OR MARS OR T3
Rodrigues "Grand Baie" MARS OR "Port Mathurin" fibre
```

---

## 5. Seed Records to Validate

| Seed | Status | Capacity | Operator | Grade | Source route |
|---|---|---|---|---|---|
| Emtel Data Centre | Operational | null IT load; dual 1 MW transformers claimed | Emtel Ltd | A | EPI, TIA, Emtel, METISS |
| MT Rose Belle Data Centre / RBDC | Operational | 1,500 sq m, 400+ racks, 3 MW claimed by MT/RBDC | Mauritius Telecom | A | myt.mu, rbdc.mu, Uptime |
| MT Rose Hill Tier III / RHDC | Operational/lead | null | Mauritius Telecom | A/C | myt.mu ICT/BPO, directory seed |
| Bhumishq Cybercity Data Centre | Operational/verify | null; 500 sq m directory claim | Bhumishq Teleserve/Technologies | A/C | Uptime, DataCenterMap |
| Rogers Capital Ebene DC | Operational | null | Rogers Capital Technology Services | A/B | Rogers, MIXP, PeeringDB, ICTA |
| Rogers Capital La Tour Koenig DC | Operational/verify | null | Rogers Capital Technology Services | A/C | Rogers, DataCenterMap |
| Rogers Capital Port Louis DC | Operational/verify | null | Rogers Capital Technology Services | C + A licence | DataCenterMap, ICTA |
| Rogers Capital Les Cascades DC | Operational/verify | null | Rogers Capital Technology Services | C + A licence | DataCenterMap, ICTA |
| Harel Mallac / MCS Datacenter 02 | Operational/verify | null | Harel Mallac Technologies | B/C | DataCenterMap, trade press |
| BIRGER Candos Recovery Centre | Operational/verify | null | BIRGER / Blanche Birger Ltd | C/B | DataCenterMap, ColocationM, BIRGER |
| Aphelion DC3 | Operational/verify | null | Aphelion Limited | C | DataCenterMap, UPSTACK |
| Government Online Centre | Operational state DC | 80 racks | MITCI/GOC | A | MITCI GOC |
| New Government Data Centre / sovereign cloud / DR | Planned/procurement | null | Government of Mauritius | A policy/procurement | MITCI, public procurement |
| CEB DR centre | Lead | null | CEB | B lead | CEB/procurement queries |
| MIXP | Operational IXP | n/a | MIXP | A | MIXP, PeeringDB |

---

## 6. Capacity and Reliability Rules

Record certification body, certification type, tier/rating, certificate ID, awarded/expiry dates, exact address, division, operator, launch/operational date, rack count, floorspace, MW/MVA/kVA, redundancy, cable/IXP adjacency, and whether the source is operator/registry/directory.

Do **not** derive capacity from:
- Tier or rating certification.
- Transformer capacity unless the field explicitly allows power-infrastructure rating.
- Rack count without stated power.
- Cable bandwidth or cable capex.
- Market forecasts from Mordor, DC Hub, or similar reports.
- Marketing terms such as "hyperscale", "world-class", "sovereign", or "state-of-the-art".

Reliability grading:
- **A**: registry/operator/government source proves the facility, certification, address, status, or named capacity claim.
- **B**: press/trade/vendor source supports a date, project, capex, status, or named-party statement.
- **C**: directory/social/SEO/aggregate only, or service page that does not prove physical facility ownership/location.

Final pitfalls: Uptime entries exist and must be used; DataCenterMap's Port Louis market label must not override Terre Rouge/Pamplemousses or Ebene/Moka; cable landings are not DCs except where explicitly linked to Emtel; ICTA licences prove telecom authority only; all 12 divisions need a positive lead or explicit "no public DC evidence" note on every enumeration run.
