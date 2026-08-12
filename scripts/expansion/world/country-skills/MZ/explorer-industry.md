# MZ Explorer Industry - Mozambique Datacenter Enumeration

Date: 2026-08-12. Country: MZ Mozambique. Scope: operator pages, trade press, directories, vendor/project leads and province search patterns, with official verification routes for every lead. Manifest divisions: Niassa; Manica; Gaza; Inhambane; Maputo; Nampula; Cabo Delgado; Zambezia; Sofala; Tete.

Maputo caveat: the manifest has one `Maputo` division. Map both Maputo City and Maputo Province to it, and keep the exact locality in notes.

## Reliability Grades

- A = official/primary: operator facility page or release; Uptime Institute record; INTIC, INCM, UEM, CEDSIF, APIEX, BAU, ARENE, EDM, MIREME or HCB page; official cloud-provider region list.
- B = strong secondary/trade/local press: DCD, Club of Mozambique, AIM, Jornal Noticias, Carta de Mocambique, Diario Economico, O Pais, TechCentral, TechAfrica News, The Tech Capital, Capacity, Developing Telecoms, Total Telecom, Agence Ecofin/We Are Tech Africa, Macauhub, reputable legal alerts.
- C = lead only: DataCenterMap, Datacenters.com, Baxtel, Cloudscene, OCOLO, colo.exchange, Inflect, HostDir, PeeringDB, SubmarineNetworks, LinkedIn/social, market reports, broker pages.

## 0. Market Frame

- Mozambique is Maputo-centric for commercial colocation. Confirmed commercial/operator facilities: iColo/Digital Realty MPM1, Raxio MZ1 and Vodacom Business Matola Data Center.
- Raxio official page confirms MZ1 can house up to 400 racks, provides 3 MW IT power and is located inside Beluluane Industrial Park/Matola, about 20 km from downtown Maputo: https://www.raxiogroup.com/data-centres/mozambique/
- Uptime Institute country record lists two Mozambique Tier III facilities as of this run: Raxio MZ1 and Vodacom Business Matola Data Center, both with Tier III Certification of Design Documents and Tier III Certification of Constructed Facility: https://uptimeinstitute.com/uptime-institute-awards/country/id/MZ
- iColo official pages confirm Maputo One MPM1, 80 rack capacity, 350 sqm IT space and 9,500 sqm campus; iColo announced opening on 2023-02-07: https://www.icolo.io/location/mpm1/ and https://www.icolo.io/news/icolo-announces-opening-of-mpm1-data-center-in-maputo/
- Digital Realty lists MPM1 as its Maputo data center: https://www.digitalrealty.com/data-centers/emea/maputo/mpm1
- DCD reports Vodacom launched the Tchumene/Matola data center in March 2025, with USD 25m investment, construction from October 2023, carrier-neutral access and direct 2Africa access hosted in Vodacom's Matola equipment room: https://www.datacenterdynamics.com/en/news/vodacom-opens-data-center-in-maputo-mozambique/
- Club of Mozambique/AIM reports Prime Minister Benvinda Levi opened Vodacom's facility and said Mozambique had 17 data centers including the Vodacom facility: https://clubofmozambique.com/news/mozambique-prime-minister-opens-vodacom-data-centre-photos/ . DCD quotes 18; record this as a contextual statement, not a facility list.
- UEM officially announced an August 2026 institutional data center at Eduardo Mondlane University/CIUEM in Maputo, supporting UEM services, research, `.mz` and MOZIX: https://uem.mz/uem-inaugura-centro-de-dados/
- INTIC licensing began in June 2026 and should be checked on every run: https://intic.gov.mz/intic-atribui-primeiras-licencas-a-provedores-intermediarios-de-servicos-electronicos-operadores-de-plataformas-digitais-e-centros-de-dados/
- Bubble Cloud is a licensed cloud/data-residency lead, but do not count physical facilities until operator/INTIC/AIM evidence identifies named sites. Carta reports the INTIC cloud license and local infrastructure: https://cartamz.com/empresas-marcas-e-pessoas/51499/novo-regime-bubble-e-a-primeira-provedora-de-servicos-cloud-a-receber-licenciamento/
- No hyperscaler public cloud region is in Mozambique. Always verify against AWS, Azure, Google Cloud and OCI official region pages before accepting any region claim.

Core national queries:

```text
Mozambique OR Mocambique ("data center" OR "data centre" OR datacenter OR "centro de dados")
"Raxio MZ1" Mozambique OR Mocambique
"iColo" OR "Digital Realty" "MPM1" Maputo
"Vodacom Business Matola Data Center"
"Vodacom" Tchumene Matola "data center"
"Uptime Institute" Mozambique "Vodacom Business Matola Data Center"
"Uptime Institute" Mozambique "Raxio MZ1"
"UEM" OR "CIUEM" "centro de dados"
"Bubble Cloud" Mocambique "centros de dados" OR "licenca"
"EDM" "National Control Center" "data center" Mozambique
"INTIC" "Operadores de Centros de Dados"
```

## 1. High-Signal Sources

| Source | URL / route | Use | Grade |
|---|---|---|---:|
| Raxio Group | https://www.raxiogroup.com/data-centres/mozambique/ | MZ1 specs, location, operator claims, partner ecosystem | A |
| Uptime Institute | https://uptimeinstitute.com/uptime-institute-awards/country/id/MZ | Tier certification for Raxio MZ1 and Vodacom Business Matola Data Center | A |
| iColo | https://www.icolo.io/location/mpm1/ ; https://www.icolo.io/news/icolo-announces-opening-of-mpm1-data-center-in-maputo/ | MPM1 opening and specs | A |
| Digital Realty | https://www.digitalrealty.com/data-centers/emea/maputo/mpm1 | MPM1 official global operator page | A |
| Vodacom Mozambique | https://www.vm.co.mz/ or https://www.vodacom.co.mz/ as current redirect | Operator verification; search for Matola/DC release | A when official |
| INTIC | https://intic.gov.mz/ | Licensing, data-center/cloud regulation, licensees | A |
| UEM | https://uem.mz/uem-inaugura-centro-de-dados/ | UEM/CIUEM data-center facility | A |
| CEDSIF | https://www.cedsif.gov.mz/ | e-SISTAFE/state finance IT platform leads | A for institution/platform, C until physical site named |
| INCM | https://www.incm.gov.mz/ | Licensed telecom/ISP universe | A for operator authority |
| EDM | https://www.edm.co.mz/ | Utility/control-center data-center leads and large-consumer context | A |
| ARENE | https://arene.org.mz/ | Energy regulation, electricity licensing and tariff context | A |
| MIREME | https://mireme.gov.mz/ | Energy ministry context; correct acronym is MIREME | A |
| DCD | https://www.datacenterdynamics.com/en/news/ | Vodacom/Raxio/iColo market coverage | B |
| Club of Mozambique / AIM | https://clubofmozambique.com/ ; https://aimnews.org/ | Official ceremonies and local reporting | B, A only for directly official facts |
| Jornal Noticias | https://jornalnoticias.co.mz/ | Local official-adjacent reports | B |
| Carta de Mocambique | https://cartamz.com/ | Bubble/INTIC and market leads | B |
| Diario Economico / O Pais | https://www.diarioeconomico.co.mz/ ; https://opais.co.mz/ | Investment/project reporting | B |
| DataCenterMap / Datacenters.com / Baxtel / Cloudscene | directory domains | Addresses, duplicate discovery, capacity leads | C |
| SubmarineNetworks / PeeringDB | submarine cable and peering routes | Cable/IX/network context only | C |

Trade queries:

```text
site:datacenterdynamics.com/en/news/ Mozambique "data center"
site:clubofmozambique.com Mozambique "data centre" OR "data center"
site:aimnews.org "centro de dados" Mocambique
site:jornalnoticias.co.mz "centro de dados"
site:cartamz.com "centro de dados" OR "Bubble"
site:diarioeconomico.co.mz "centro de dados" OR "data center"
site:opais.co.mz "centro de dados" OR "data center"
site:techafricanews.com Mozambique "data center"
site:developingtelecoms.com Mozambique "data centre"
site:thetechcapital.com Mozambique "data centre"
```

## 2. Operator and Vendor Sweep

| Operator / provider | Geography | How to handle |
|---|---|---|
| Raxio Group | Beluluane Industrial Park / Matola-Boane, Maputo | Count MZ1 as operational commercial colo with A source and Uptime certification. |
| iColo / Digital Realty | Maputo City | Count MPM1 as operational commercial colo with A source. Preserve iColo capacity values; do not replace with directory estimates. |
| Vodacom Business Mozambique | Tchumene/Matola, Maputo | Count Vodacom Business Matola DC as operational. Use Uptime for Tier III. Use DCD/Club for launch, investment and location unless official Vodacom release is found. |
| Vodacom legacy modular DC | Matola, Maputo | B lead from DCD historical reference. Count separately only if facility inventory wants legacy modular sites. |
| UEM / CIUEM | Maputo City | Count as institutional/university DC, operational August 2026, A source. Not commercial colo unless official service terms appear. |
| CEDSIF | Maputo | State finance-system IT lead. Needs physical facility evidence before counting. |
| Bubble Cloud Mozambique | Maputo, exact sites unknown | Licensed cloud/data-residency lead. AIM reports two data centers; verify named facilities before counting two physical DCs. |
| EDM | Matalane/CTM Maputo; Chibata; Nampula | Utility SCADA/control-center data-center leads from EDM-branded slides. Verify tenders/commissioning before counting as operational. |
| Tmcel | Maputo HQ plus national network | Hosting/colo ecosystem lead. Count only if a named DC, INTIC DC license or tender appears. |
| Movitel / Viettel | Maputo plus provincial network | Network/operator lead only. Count named DCs only. |
| TV Cabo, Webmasters, Moztel, TeleData, AbariCom, ClubNet, Netclix | Mostly Maputo | Hosting/ISP leads seen in Raxio/iColo ecosystems and directories. Count only named facilities. |
| Dimension Data / BCX, Paratus, WIOCC, SEACOM, Liquid | Maputo and cables | Connectivity/cloud/integrator leads, not physical DC evidence by themselves. |
| Banks, mining, LNG, ports, universities | Maputo, Tete, Cabo Delgado, Inhambane, Sofala, Nampula | Enterprise/internal leads. Require named site/tender. |

Operator queries:

```text
"{operator}" Mocambique "data center" OR "centro de dados"
"{operator}" Mozambique colocation OR alojamento OR cloud
"{operator}" "Uptime" OR "Tier III" Mozambique
"{operator}" "grupo electrogeneo" OR UPS "centro de dados"
"Viettel" OR "Movitel" "data center" Mozambique
"Tmcel" "hosting" "colocation" Mocambique
"Webmasters" Maputo "data center" OR colocation
"Bubble Cloud" "infra-estruturas localizadas em Mocambique"
```

Address pivots:

```text
"Beluluane" OR "MozParks" Raxio
"Matola" OR "Tchumene" Vodacom "data center"
"Avenida Lenine" OR "Av. Vladimir Lenine" iColo MPM1
"Matalane" "data center" EDM
"CTM" "data center" EDM Maputo
"Chibata" "Data Collection Centre" EDM
"Nampula" "Regional Control Center" EDM
"CIUEM" "centro de dados" UEM
```

## 3. Directory Handling

Directories are lead generators only.

| Directory | Use | Caveat |
|---|---|---|
| DataCenterMap Mozambique | May list Vodacom, iColo, Raxio and addresses | C; use only after A/B corroboration. Its Vodacom capacity/address claims need official support. |
| Datacenters.com | Sales/provider index | C; may conflict with operator page. |
| Baxtel | Raxio/Vodacom summaries and linked news | B only for linked sourced news; C for profile data. |
| Cloudscene/OCOLO/colo.exchange/Inflect/HostDir | Facility discovery | C; reconcile with operator/Uptime. |
| SubmarineNetworks | Cable landing context, MPM1/2Africa relationship | C for facility enumeration. Count iColo because iColo is a named DC, not because it is a cable station. |
| PeeringDB | ASN/interconnection context | C; never sufficient for a DC count. |

Upgrade workflow:

1. Capture exact claimed name, address, operator, power/racks/sqm and source date.
2. Search exact name plus operator domain.
3. Search Uptime Institute by country and facility name.
4. Search INTIC license pages and INCM operator pages.
5. Search DCD, AIM/Club, Jornal Noticias, Carta, Diario Economico and O Pais for opening/tender evidence.
6. If no A/B source appears, keep as C lead or exclude from inventory.

## 4. Known Lead Grading

| Lead | Initial grade | Final handling |
|---|---:|---|
| Raxio MZ1 | A | Operational commercial colo. Use Raxio specs and Uptime Tier III record. |
| iColo/Digital Realty MPM1 | A | Operational commercial colo. Use iColo specs and opening date. |
| Vodacom Business Matola Data Center | A/B | Operational telecom/operator DC. Use Uptime for Tier III; DCD/Club for Tchumene, USD 25m, launch and 2Africa access unless Vodacom page is found. |
| UEM/CIUEM data center | A | Operational institutional/university DC. Maputo. |
| EDM Matalane/CTM data-center components | A/B | Planned/under-procurement utility/control-center leads. Count as utility/institutional only when inventory scope includes SCADA/control data centers. |
| EDM Chibata/Nampula regional control/data collection | A/B | Non-commercial utility leads. Verify exact geography and explicit DC component before counting. |
| Bubble Cloud | B/C | Licensed cloud/data-residency provider. Do not count one or two physical DCs until sites are named by Bubble, INTIC or strong press. |
| CEDSIF/e-SISTAFE | A/C | Important state IT platform. Count only with physical DC/source. |
| Tmcel/Movitel/TV Cabo/Webmasters/TeleData/etc. | C to B | Hosting/network leads. Require named facility or INTIC DC license. |
| Banks, LNG, mining, ports, universities outside UEM | C | Internal IT leads only; require named facility/tender. |

## 5. Province-by-Province Strategy

### Maputo

Known high-priority facilities and leads: Raxio MZ1; iColo/Digital Realty MPM1; Vodacom Business Matola Data Center; UEM/CIUEM data center; possible CEDSIF/e-SISTAFE infrastructure; Bubble Cloud; EDM Matalane/CTM; Tmcel and other ISP/operator sites.

```text
"Maputo" "data center" OR "centro de dados" colocation
"Matola" "data center" Vodacom OR Raxio
"Tchumene" Vodacom "data center"
"Beluluane" OR "Boane" Raxio
"MPM1" "Maputo" iColo
"CIUEM" "centro de dados"
"Matalane" OR "CTM" "data center" EDM
"Maputo" INTIC "Operadores de Centros de Dados"
```

### Nampula

Baseline: no confirmed commercial DC. Watch EDM northern regional control/data-collection project, Nacala corridor, UniLurio, ports/logistics and telecom cores.

```text
"Nampula" "centro de dados" OR "data center"
"Nacala" "data center" OR servidores
"EDM" Nampula "Regional Control Center"
"UniLurio" "centro de dados" OR servidores
"Nampula" Movitel OR Vodacom "servidores"
```

### Sofala

Baseline: no confirmed commercial DC. Watch Beira port/rail, universities and possible Chibata central control-center geography.

```text
"Sofala" OR "Beira" "centro de dados" OR "data center"
"CFM" Beira servidores OR "centro de dados"
"UniZambeze" Beira servidores
"Chibata" EDM "Data Collection Centre"
"Beira Corridor" servidores digital
```

### Manica

Baseline: no confirmed commercial DC. Watch Chibata/Chimoio utility and corridor leads.

```text
"Manica" OR "Chimoio" "centro de dados" OR "data center"
"Chibata" "data center" OR "Data Collection Centre"
"EDM" "Chibata" SCADA OR servidores
"Beira Corridor" Chimoio digital servidores
```

### Tete

Baseline: no confirmed commercial DC. Watch Cahora Bassa/HCB, Moatize mining and Mphanda Nkuwa project IT.

```text
"Tete" OR "Moatize" "centro de dados" OR "data center"
"HCB" OR "Cahora Bassa" servidores OR "centro de dados"
"Mphanda Nkuwa" TIC OR servidores
"Vulcan" OR "Jindal" Moatize servidores
```

### Cabo Delgado

Baseline: no confirmed commercial DC. Watch LNG, Afungi/Palma/Pemba and security/telecom projects.

```text
"Cabo Delgado" OR "Pemba" OR "Palma" "centro de dados" OR "data center"
"Afungi" servidores OR "data center"
"TotalEnergies" OR "ExxonMobil" OR ENI Palma servidores
"Cabo Delgado" fibra optica servidores
```

### Inhambane

Baseline: no confirmed commercial DC. Watch Pande/Temane/Sasol and energy SCADA.

```text
"Inhambane" OR "Maxixe" OR "Vilankulo" "centro de dados" OR "data center"
"Temane" servidores OR SCADA
"Sasol" Pande Temane TIC servidores
"Central Termica de Temane" "data center" OR servidores
```

### Niassa

Baseline: no confirmed commercial DC. Watch public ICT/resource centers and off-grid/anchor-load projects only as context.

```text
"Niassa" OR "Lichinga" OR "Cuamba" "centro de dados" OR "data center"
"Niassa" servidores TIC governo provincial
"Lichinga" "sala de servidores"
"Chimbonila" servidores
```

### Gaza

Baseline: no confirmed commercial DC. Watch Chokwe/Xai-Xai public-sector IT and energy projects.

```text
"Gaza" OR "Xai-Xai" OR "Chokwe" "centro de dados" OR "data center"
"Gaza" servidores TIC
"Kuvaninga" SCADA servidores
```

### Zambezia

Baseline: no confirmed commercial DC. Search both accentless and accented forms.

```text
"Zambezia" OR "Zambézia" OR "Quelimane" "centro de dados" OR "data center"
"Quelimane" servidores TIC
"Mocuba" SCADA servidores
"UniZambeze" Quelimane servidores
```

## 6. Honesty Rules

- Do not count a service as a facility. Cloud, VPS, hosting, backup, IaaS, CDN, IX and cable words need a named physical data center or license category.
- Do not count every telecom exchange, POP or provincial node.
- Treat `Tier III` carefully. Uptime Institute is A; trade/operator language without Uptime is a claim.
- Keep capacity null unless the operator, Uptime, government procurement or a strong source states it. Raxio and iColo have source-supported figures; Vodacom capacity should stay null unless Vodacom/Uptime publishes it.
- Use the PM 17/18 data-center statement only as context. It is not a list and the number differs across reports.
- Maputo is the only division with confirmed commercial colocation in current evidence. Nampula, Sofala/Manica and Maputo have utility/institutional leads; the rest are negative-by-default.
