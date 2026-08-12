# MG Explorer Industry - Madagascar Datacenter Enumeration via Operators, Connectivity, Trade Press, and Province Query Patterns

Date: 2026-08-12. Country: **MG Madagascar**. Division model: **province** (`faritany`): **Antananarivo; Antsiranana; Fianarantsoa; Mahajanga; Toamasina; Toliara**. Scope: industry/operator-side datacenter discovery: commercial colocation, hosting/cloud providers, telco and IXP facilities, cable landing pivots, directories, trade press, and per-province query templates. Official/regulatory pipeline lives in `explorer-official.md`.

Reliability grades are per fact:
- **A** = operator-owned, certification-registry, cable-system official, cloud-provider official, regulator/government, or other primary source that proves the specific claim.
- **B** = reputable trade/local press or named vendor source with date/place/operator details.
- **C** = directory, marketplace, self-reported PeeringDB/Inflect/OCOLO/DataCenterMap lead, social profile, Wikipedia, market-report snippet.
- **U** = unresolved after this pass; keep as a lead only.

## 0. Market shape and verified facts

- Madagascar is a small, telecom-led datacenter market concentrated in **Antananarivo province**. ISOC Pulse reports **1 active data center**, **1 IXP**, and 5 active networks in Madagascar for 2026 (https://pulse.internetsociety.org/en/reports/mg/). This is a B-grade market indicator, not a definitive facility registry.
- **STELLARIX** is the clearest commercial datacenter operator lead. Its own site describes STELLARIX as a data-hosting and infrastructure-management company in Africa and says it offers colocation, cloud, virtualization, and interconnection services (https://www.stellar-ix.com/en/). Its about page names two Madagascar data centers: **TNR1 Analakely, Lalana Paul Dussac, Antananarivo 101** and **TNR2 Galaxy, Building KUBE D 2nd floor Galaxy Andraharo, BP 763 Antananarivo 101** (https://stellar-ix.com/en/a-propos-de-stellarix/). Grade **A for operator facility/address/service claims**.
- STELLARIX “TIER III ready” wording is an operator claim, not proof of Uptime/TIA certification. Uptime search surfaced a **STELLARIX Tanzania** award, not a Madagascar award (https://uptimeinstitute.com/uptime-institute-awards/client/stellarix-tanzania-limited/1277). TIA/EPI searches did not surface a Madagascar STELLARIX certificate. Grade Madagascar certification as **U** until registry evidence appears.
- PeeringDB lists **MGIX** and the **Bâtiment Sirius / Zone Galaxy Andraharo** facility in Antananarivo (https://www.peeringdb.com/org/14435 and https://www.peeringdb.com/fac/2993). Grade **C/A-by-source** because PeeringDB is self-reported but specific and useful.
- DataCenterMap lists **2 Antananarivo data centers** and a **STELLARIX Antananarivo TNR01** record (https://www.datacentermap.com/madagascar/antananarivo/ and https://www.datacentermap.com/madagascar/antananarivo/tnr011/). Grade **C** until reconciled to STELLARIX's own addresses.
- Connectivity is distributed outside Antananarivo but is not datacenter evidence by itself: **LION/LION2** at Toamasina, **2Africa** at Mahajanga, and **METISS** at Fort Dauphin/Taolagnaro lead. Treat cable landing stations as connectivity facilities unless hosting/compute/colo evidence is explicit.

## 1. Search vocabulary

Use French first, English second, and Malagasy only as a low-yield discovery layer.

```text
French: centre de données | datacenter | data center | hébergement | hébergement de données | hébergement de serveurs | colocation | salle serveur | cloud | infrastructure numérique | point d'échange Internet | IXP | peering | point de présence | PoP | station d'atterrissement | câble sous-marin | site de secours | PRA | reprise d'activité | groupe électrogène | délestage | licence | appel d'offres
English: data center | data centre | datacenter | colocation | colo | hosting | cloud | server room | NOC | disaster recovery | DR site | internet exchange | cable landing station | submarine cable | satellite gateway | ground station | Tier III | Uptime Institute | TIA-942
Malagasy discovery: foibe data | foiben-drakitra | rahona | mpampiantrano | tambajotra | tariby amban-dranomasina | herinaratra
Brands/entities: STELLARIX | Stellar-IX | Telma | Yas | Orange Madagascar | Airtel Madagascar | Gulfsat | Blueline | BIP | Axian | MGIX | iRENALA | NIC.MG | GOTICOM | LION | LION2 | METISS | 2Africa | Africa-1 | Starlink | OneWeb | O3b | PRODIGY | UGD | ARTEC | JIRAMA
```

## 2. Priority operator and infrastructure sweep

| Lead | Source route | Province/locality handling | Grade and action |
|---|---|---|---|
| STELLARIX TNR1 Analakely | Operator about page: https://stellar-ix.com/en/a-propos-de-stellarix/ ; home/services: https://www.stellar-ix.com/en/ | Antananarivo province; Lalana Paul Dussac, Antananarivo 101 | **A** for operator-named DC/address and service family. Verify parcel, power, certification, and current commercial availability separately. |
| STELLARIX TNR2 Galaxy | Same operator page | Antananarivo province; Building KUBE D, 2nd floor, Galaxy Andraharo, BP 763, Antananarivo 101 | **A** for operator-named DC/address. Cross-check with MGIX/PeeringDB Galaxy/Andraharo records. |
| MGIX / Bâtiment Sirius | PeeringDB org/facility; ISOC Pulse IXP tracker; ISOC Foundation MGIX grant page https://www.isocfoundation.org/project/restart-mgix-madagascar-global-internet-exchange/ | Antananarivo, Zone Galaxy Andraharo / Bâtiment Sirius | **B/C** for IXP and interconnection facility. Count as DC only with hosting/colo/data-hall evidence. |
| DataCenterMap / OCOLO / Inflect directory entries | DataCenterMap Antananarivo and TNR01; OCOLO Antananarivo; Inflect MGIX | Mostly Antananarivo | **C** seed only. Reconcile every address against STELLARIX/operator pages or local filings. |
| Telma/Yas / AXIAN | https://www.yas.mg/ or https://services.yas.mg/ ; old corporate PDF https://services.yas.mg/data/corporate/2011_en.pdf ; DCD Axian financing articles | Antananarivo HQ/NOC; national network; cable landings at Mahajanga and Toamasina via consortium context | **A** for operator-owned statements, **B** for trade financing. The 2011 NOC/DR-centre statement is historical; current facility status needs fresh operator proof. |
| Orange Madagascar | https://www.orange.mg/ plus LION/LION2 consortium sources | Antananarivo operator, Toamasina cable context | **A** for operator existence/services; **U** for Madagascar DC unless a facility page appears. |
| Airtel Madagascar | https://www.africa.airtel.com/madagascar | Antananarivo/operator network; national mobile services | **A** for operator existence/services; **U** for dedicated DC evidence. |
| Gulfsat Madagascar | https://gulfsat.mg/ ; O3b press (Satellite Today) | Antananarivo/satellite ISP | **A/B** for operator/connectivity; **U** for VSAT head-end as DC unless source names facility. |
| Starlink Madagascar | Starlink service pages; ARTEC 2024 report; 2424.mg and Agence Ecofin | National; gateway not public | **A/B** for licence/service availability. **U** for ground gateway/DC. |
| Government/UGD/PRODIGY compute | https://digital.gov.mg/ and World Bank P169413 | Mostly Antananarivo; pilots in Toamasina and other provinces | **A** for project/tenders. Facility address/hosting site remains U unless named. |
| Banks/mining/enterprise server rooms | Bank sites; Ambatovy/QMM; tenders and press | Antananarivo, Toamasina, Toliara | Demand/enterprise-IT leads only; **C/U** unless they offer third-party hosting or name a DR/DC site. |

Operator queries:
```text
site:stellar-ix.com Madagascar TNR1 OR TNR2 OR Analakely OR Galaxy OR Andraharo
"STELLARIX" Madagascar (colocation OR cloud OR datacenter OR "data center" OR "centre de données")
"TNR1" "Antananarivo" STELLARIX OR Stellar-IX
"TNR2" "Galaxy" "Andraharo" STELLARIX OR Stellar-IX
"Bâtiment Sirius" MGIX OR "Zone Galaxy" MGIX OR Andraharo
"Telma" OR "Yas" Madagascar ("disaster recovery" OR NOC OR "centre de données" OR datacenter OR hébergement)
site:orange.mg Madagascar (hébergement OR cloud OR "centre de données" OR datacenter)
site:africa.airtel.com/madagascar (business OR cloud OR hosting OR "data center")
site:gulfsat.mg (hosting OR cloud OR gateway OR VSAT OR datacenter)
```

## 3. Connectivity pivots

### 3.1 IXP and peering

- **MGIX - Madagascar Global Internet eXchange** is the national IXP in Antananarivo. ISOC Pulse reports one IXP in Madagascar and PeeringDB places MGIX at Bâtiment Sirius / Zone Galaxy Andraharo with 5 exchange networks in the facility view. Sources: https://pulse.internetsociety.org/en/reports/mg/ , https://www.peeringdb.com/org/14435 , https://www.peeringdb.com/fac/2993 .
- The ISOC Foundation funds a 2024-07-01 to 2026-06-30 **Restart MGIX** grant to iRENALA for sustainable peering infrastructure (https://www.isocfoundation.org/project/restart-mgix-madagascar-global-internet-exchange/). Use it as a modernization lead, not a DC record.

Queries:
```text
"MGIX" OR "Madagascar Global Internet eXchange" Antananarivo peering members
site:peeringdb.com MGIX Madagascar Antananarivo facility
"Bâtiment Sirius" "Zone Galaxy" Andraharo "data center" OR MGIX
"iRENALA" MGIX Madagascar peering infrastructure
```

### 3.2 Submarine cables and landing stations

| Cable | Madagascar locality/province | Evidence | Grade | Handling |
|---|---|---|---|---|
| LION / LION2 | Toamasina, Toamasina province | LION official site snippet lists Madagascar cable landing station Toamasina; Submarine Networks says LION connects Madagascar, Reunion, Mauritius and was RFS March 2010; LION2 extends to Mayotte/Kenya | A/B | Connectivity site. Seek Orange/Telma/ARTEC/local permit evidence before any facility record. |
| 2Africa | Mahajanga, Mahajanga province | Connecting Africa says 2Africa reached Madagascar in Feb 2023 with Telma/Vodafone at the Mahajanga landing site; 2Africa official site says the core system is complete and ready in most landing countries | B for Madagascar landing; A for official system status | Important correction: do not place this in Toamasina. CLS is not a DC. |
| METISS | Fort Dauphin/Taolagnaro lead, Toliara province | Submarine Networks says METISS has been in service since March 2021 and connects Mauritius, Reunion, Madagascar, and South Africa; multiple trade reports say Madagascar landing at Fort Dauphin | B | Important correction: do not default METISS to Toamasina. Confirm exact local CLS and operator. |
| Africa-1 | Madagascar lead unresolved | Submarine Networks tracks Africa-1 progress elsewhere; no strong Madagascar operational landing proof found in this pass | U/C | Keep as planned/rumored until cable-system or operator source names Madagascar landing and status. |
| EASSy/SEACOM | No Madagascar landing confirmed | Searches mostly route via regional backhaul/stubs | U/negative lead | Do not include as MG landing without primary map/source. |

Cable queries:
```text
"LION" "LION2" Madagascar Toamasina "cable landing station"
site:lion-submarinesystem.com Madagascar Toamasina LION2
"2Africa" Madagascar Mahajanga Telma Vodafone landing
site:2africacable.net Madagascar Mahajanga
"METISS" Madagascar "Fort Dauphin" OR Taolagnaro OR "landing station"
"Africa-1" Madagascar "landing station" OR "cable landing"
```

### 3.3 Satellite / LEO / VSAT

- ARTEC's 2024 report snippet and press confirm Starlink Madagascar licensing in 2024; Ecofin reported commercial launch in June 2024. Use as satellite ISP evidence only.
- Gulfsat/O3b and OneWeb-style claims are edge-connectivity leads. A gateway/ground-station record requires a named site, licence, construction, or operator statement.

Queries:
```text
"Starlink" Madagascar gateway OR "ground station" OR passerelle OR ARTEC
"Gulfsat" Madagascar O3b gateway OR VSAT OR "station terrienne"
"OneWeb" Madagascar gateway OR "station terrienne" OR licence
site:artec.mg satellite Madagascar licence Starlink OneWeb Gulfsat
```

## 4. Industry, press, and directory source map

| Source | URL / route | Use | Grade rule |
|---|---|---|---|
| STELLARIX | https://www.stellar-ix.com/en/ and `/en/a-propos-de-stellarix/` | Primary commercial DC/operator evidence | A for STELLARIX claims; certification separate |
| PeeringDB | https://www.peeringdb.com/ | MGIX, facilities, interconnection addresses | C/A-by-source; self-reported |
| ISOC Pulse | https://pulse.internetsociety.org/en/reports/mg/ | Market baseline, IXP count, active DC count | B indicator |
| ISOC Foundation | https://www.isocfoundation.org/project/restart-mgix-madagascar-global-internet-exchange/ | MGIX restart grant | B/A for grant page, not facility proof |
| DataCenterMap | https://www.datacentermap.com/madagascar/antananarivo/ | Directory leads | C |
| Inflect / OCOLO / datacenters.com | Search STELLARIX/Madagascar/Antananarivo | Marketplace/directory leads | C |
| Uptime Institute | https://uptimeinstitute.com/uptime-institute-awards/list | Certification check | A for awards found; absence requires refresh |
| TIA/EPI | https://tiaonline.org/products-and-services/tia942certification/tia-942-certifications-ratings/ and https://www.epi-certification.com/sites/list | Certification check | A for certificates found |
| Data Center Dynamics | https://www.datacenterdynamics.com/ | Axian financing, regional DC/cable context | B |
| Connecting Africa | https://www.connectingafrica.com/ | 2Africa Madagascar landing | B |
| Submarine Networks / SubTel Forum | https://www.submarinenetworks.com/ , https://subtelforum.com/ | LION, METISS, 2Africa, Africa-1 | B unless operator primary |
| Agence Ecofin / 2424.mg | https://www.agenceecofin.com/ , https://2424.mg/ | Telecom licences, Starlink, local regulation | B |
| L'Express / Midi / NewsMada | local press | Energy, telecom, business signals | B/C depending detail |
| trade.gov | https://www.trade.gov/country-commercial-guides/madagascar-information-and-telecommunications-technology and `/madagascar-digital-economy` | Market/digital-economy context | A/B |
| GOTICOM | https://goticom.org.mg/ | ICT association/member leads | B/C for leads |
| NIC.MG / IANA | https://nic.mg/ , https://www.iana.org/domains/root/db/mg.html | ccTLD/cache/DNS context | A for registry/delegation |

Press/directory queries:
```text
site:datacenterdynamics.com Madagascar STELLARIX OR Axian OR Telma OR "data center"
site:connectingafrica.com Madagascar 2Africa Mahajanga
site:submarinenetworks.com Madagascar LION OR METISS OR 2Africa OR Africa-1
site:subtelforum.com Madagascar 2Africa OR METISS OR LION
site:agenceecofin.com Madagascar (Starlink OR Telma OR Orange OR Airtel OR datacenter OR "centre de données")
site:2424.mg Madagascar (Starlink OR ARTEC OR datacenter OR "centre de données" OR STELLARIX)
site:datacentermap.com Madagascar Antananarivo STELLARIX
site:ocolo.io Madagascar STELLARIX Antananarivo
site:datacenters.com STELLARIX Madagascar TNR01 OR TNR02
```

## 5. Province recipes

Use the exact province names in output records. The region list is included to prevent accidental omissions in province sweeps.

| Province | Regions | Expected yield | Industry recipe |
|---|---|---|---|
| Antananarivo | Analamanga, Vakinankaratra, Itasy, Bongolava | Confirmed commercial/operator DC evidence: STELLARIX TNR1/TNR2. MGIX and telco NOC/DR leads. | Search STELLARIX, Galaxy/Andraharo, Analakely, MGIX, Telma/Yas, Orange, Airtel, Gulfsat, banks, government tenders, JIRAMA power terms. |
| Antsiranana | Diana, Sava | No public commercial DC found; expect telecom PoPs, tourism/free-zone IT, satellite leads. | Search Antsiranana/Diego-Suarez, Nosy Be, Sambava with hosting/DC/IXP/gateway terms; require operator or permit proof. |
| Fianarantsoa | Amoron'i Mania, Haute Matsiatra, Ihorombe, Atsimo-Atsinanana, Vatovavy, Fitovinany | No public commercial DC found; possible university/government server rooms. | Search Fianarantsoa, Ambositra, Manakara, Mananjary, Ihosy with PRODIGY, civil status, server, JIRAMA, university terms. |
| Mahajanga | Boeny, Betsiboka, Melaky, Sofia | 2Africa landing at Mahajanga; no commercial DC confirmed. | Search Mahajanga/Majunga + 2Africa/Telma/Vodafone/CLS. Do not count landing as DC without hosting/colo evidence. |
| Toamasina | Atsinanana, Analanjirofo, Ambatosoa, Alaotra-Mangoro | LION/LION2 Toamasina landing and port/industrial ICT; no commercial DC confirmed. | Search Toamasina/Tamatave + LION/LION2/Orange/Telma/landing station, port, Ambatovy, JIRAMA. |
| Toliara | Atsimo-Andrefana, Androy, Anosy, Menabe | METISS Fort Dauphin/Taolagnaro landing lead; mining enterprise IT; no commercial DC confirmed. | Search Toliara/Tulear, Taolagnaro/Fort Dauphin, QMM, METISS, landing station, energy/permit terms. |

Universal province query:
```text
"{province}" OR "{city}" Madagascar (datacenter OR "data center" OR "centre de données" OR colocation OR hébergement OR cloud)
"{city}" Madagascar ("cable landing station" OR "station d'atterrissement" OR "câble sous-marin" OR IXP OR peering)
"{city}" Madagascar ("server room" OR "salle serveur" OR "disaster recovery" OR PRA OR NOC)
"{city}" Madagascar (JIRAMA OR délestage OR "groupe électrogène" OR UPS OR refroidissement)
"{city}" Madagascar ("permis de construire" OR EIE OR "étude d'impact") (datacenter OR télécommunications OR fibre)
```

## 6. Seed records to validate during enumeration

| Seed | Status | Capacity | Operator/developer | Province | Grade | Sources to use |
|---|---|---:|---|---|---|---|
| STELLARIX TNR1 Analakely | Operator-confirmed lead / likely operational service | null | STELLARIX / AXIAN group context | Antananarivo | A for operator claim | STELLARIX about page, services page, local permits/power/certification refresh |
| STELLARIX TNR2 Galaxy | Operator-confirmed lead / likely operational service | null | STELLARIX | Antananarivo | A for operator claim | STELLARIX about page; PeeringDB Galaxy/Andraharo; DataCenterMap/OCOLO as C cross-checks |
| MGIX / Bâtiment Sirius | Active IXP/interconnection facility | null | Madagascar Global Internet eXchange / iRENALA context | Antananarivo | B/C | ISOC Pulse, PeeringDB, ISOC Foundation grant |
| Telma/Yas NOC and disaster recovery centre | Historical lead; current status unresolved | null | Telma/Yas / AXIAN | Antananarivo | A historical, U current | 2011 Yas/Telma PDF, Yas current site, ARTEC, STELLARIX relationship checks |
| PRODIGY government compute | Project/tender lead | null | Government/UGD/World Bank | Antananarivo plus provincial pilots | A for project | digital.gov.mg, World Bank P169413, ARMP |
| LION/LION2 Toamasina CLS | Connectivity site | null | Orange Madagascar/Mauritius Telecom/France Telecom consortium | Toamasina | A/B cable fact | LION official site, Submarine Networks, Orange/Telma/local permits |
| 2Africa Mahajanga CLS | Connectivity site | null | Telma/Vodafone/2Africa consortium | Mahajanga | B landing fact; A for official system status | Connecting Africa, 2Africa official site, Telma/Vodafone/ARTEC |
| METISS Fort Dauphin/Taolagnaro CLS | Connectivity site | null | METISS consortium / Telma-related connectivity | Toliara | B | Submarine Networks, SubTel Forum, Telma/METISS operator pages, local permits |
| Starlink Madagascar | Licensed satellite ISP | null | Starlink Madagascar / SpaceX | National | A/B licence/service | ARTEC 2024 report, 2424.mg, Ecofin, Starlink availability; gateway searches |
| Orange/Airtel/Gulfsat enterprise/network sites | Operator leads | null | Operators | Mostly Antananarivo | A for operator, U for DC | Operator pages, ARTEC, PeeringDB, tenders, press |

## 7. Capacity, certification, and status extraction

Capture these fields when a source provides them: facility name, operator legal name, address, province, region/city, status, service type, launch date, customer eligibility, racks, MW/kW/kVA/MVA, gross sqm, power redundancy, generator/fuel permits, cooling system, carrier list, IXP presence, cloud on-ramps, certification body, certificate ID, certificate date/expiry, and source URL.

Do not infer capacity from:
- Cable design capacity or landing status.
- Market share, ISP rank, or fibre footprint.
- “Tier III ready”, “state of the art”, or “carrier neutral” wording without registry or technical detail.
- Investment totals, EIB/AfDB financing, or government project budgets.

Certification queries:
```text
site:uptimeinstitute.com/uptime-institute-awards Madagascar STELLARIX OR Antananarivo
site:tiaonline.org/942-datacenter Madagascar OR STELLARIX
site:epi-certification.com/sites Madagascar OR STELLARIX
"STELLARIX" Madagascar "TIA-942" OR "Uptime Institute" OR "Tier III Facility" OR "Tier III Design"
"TNR1" OR "TNR2" racks OR MW OR kVA OR "TIA-942" OR Uptime
```

## 8. Pitfalls and decision rules

- **STELLARIX is the primary commercial target.** Start there, then reconcile DataCenterMap/OCOLO/Inflect/datacenters.com records to STELLARIX's named TNR1/TNR2 sites.
- **Keep TNR1/TNR2 separate unless a source proves they are the same physical site.** The operator names two data centers at different Antananarivo addresses.
- **Do not merge MGIX with STELLARIX automatically.** Both involve Antananarivo/Galaxy/Andraharo search space, but MGIX/Batiment Sirius and STELLARIX TNR2/KUBE D need address reconciliation.
- **Cable landings are not datacenters.** LION/LION2, 2Africa, and METISS are important for edge/CLS leads but should remain connectivity records unless facility evidence appears.
- **Use province, not region, as the output division.** Regions are search aids. Province assignment must be one of the six requested names.
- **Treat historical Telma PDF evidence carefully.** The old Antananarivo NOC/DR-centre statement is useful, but it is not current commercial-colo proof in 2026.
- **No hyperscaler region by reseller inference.** Partner pages, CDN caches, Starlink service, or local cloud products do not equal AWS/Azure/GCP/OCI Madagascar regions.

## 9. Refresh cadence

- **Quarterly:** STELLARIX site/about/services/jobs; PeeringDB MGIX/facility; ISOC Pulse; DataCenterMap/OCOLO/Inflect/datacenters.com; ARTEC reports/licences; Starlink/gateway searches; cable status for 2Africa/LION/METISS/Africa-1; local press for power and telecom incidents.
- **Semi-annual:** Uptime/TIA/EPI certification lists; hyperscaler region lists; Yas/Telma, Orange, Airtel, Gulfsat enterprise pages; GOTICOM membership; trade.gov digital economy and ICT guides; EDBM/Choose Digital Madagascar.
- **Annual:** province/region mapping, data-protection authority status, telecom law changes, State Department investment climate statement, World Bank/PRODIGY procurement and project status.

## 10. Validation log - 2026-08-12

Live web checks confirmed: STELLARIX home/about pages and TNR1/TNR2 addresses; PeeringDB MGIX/Batiment Sirius records; ISOC Pulse MG report; DataCenterMap Antananarivo/STELLARIX pages; Uptime search result for STELLARIX Tanzania only; TIA/EPI certification list routes; 2Africa official site; Connecting Africa 2Africa Madagascar/Mahajanga; Submarine Networks LION and METISS; LION official site snippet; ARTEC Starlink report snippet; 2424.mg and Agence Ecofin Starlink coverage; World Bank PRODIGY P169413; trade.gov ICT/digital-economy pages; JIRAMA/IMF power context; ONE/Ivotoro official planning/environment routes. Unresolved facts are retained as leads with U or C grades rather than asserted as confirmed facilities.
