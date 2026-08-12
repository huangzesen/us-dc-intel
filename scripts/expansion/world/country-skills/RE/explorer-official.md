# RE Explorer Official - 留尼汪（La Reunion）数据中心官方源枚举方法

Date: 2026-08-12. Country: **RE Reunion / 留尼汪**. Manifest entry verified from `world-manifest.jsonl`: `{"country_code":"RE","country_name":"Reunion","subnational_type":"country","divisions":["Reunion"]}`. This is a **single-division model / 单分区模型**: every record must use division `Reunion`; locality work is done by commune.

Scope: official and first-party routes for discovering operating, construction, planned, institutional, and lead-stage data-center facilities in Reunion. Primary emphasis is operator/government evidence, procurement, planning/ICPE, power, cable-landing context, certification registries, and official cloud-region negative checks.

Reliability grades / 可信度分级：**A** = official/first-party source directly supports the specific field: operator page, government/local authority page, regulatory decision, public procurement, planning/ICPE file, utility record, certification registry, official cloud-region page, or first-party cable/IXP evidence. **B** = reliable industry/local media or vendor source with named party, date, and location. **C** = directory, SEO hosting page, social page, aggregator, or unattributed market claim. Grade by field: a facility can have A-grade existence, B-grade launch details, and C-grade capacity.

---

## 0. Verified Baseline / 已核验基线

- Reunion is a French overseas department/region (DROM) in the Indian Ocean. The manifest has exactly one division, `Reunion`; do not create province/region subdivisions.
- **Confirmed local data-center facility / 已确认本地数据中心**: **Omega 1 / Omega One**, built by the **Groupe Oceinde** ecosystem and located in **Le Port**. Official/local-authority evidence from Territoire de l'Ouest says the first stone was presented on 2023-05-04, the article was published on 2023-05-05, Omega 1 is installed in Le Port, and it provides data-hosting, connectivity, and services for local/international enterprises and public/government bodies. Operator site `https://www.omegaone.re/` is live and describes Omega 1 as the first equivalent Tier 3 data center in Reunion/Indian Ocean, with ISO 27001 and HDS badges. Treat "equivalent Tier 3" as an operator claim unless a registry certificate is found.
- **Other hosting/colocation activity / 其他托管活动**:
  - **SFR Business Reunion** has a live first-party hosting page (`https://www.sfrbusiness.re/entreprises-et-collectivites/hebergement/`) describing secure datacenter hosting, NETCENTER, dedicated/shared space, cloud/PRA/PCA, and virtual datacenter services. This proves SFR's Reunion business hosting offer exists, but not public facility address/capacity by itself.
  - **Zeop Entreprise** (`https://entreprise.zeop.re/`) states business services are 100% in Reunion and references `data-center`; it also has an `Hébergement` service path. Because Zeop is part of the Oceinde ecosystem, cross-check whether current hosting is Omega 1, legacy Reunicable/Zeop hosting, or a separate facility before creating duplicate assets.
  - **Orange Reunion / Orange Business** is a telecom/operator pivot, but no current first-party Reunion-specific datacenter facility page was verified in this pass. Keep Orange as an operator/procurement/regulatory lead, not a confirmed facility seed unless a facility page or permit appears.
- **ARCEP telecom context**: ARCEP records and annual reports verify the Reunion telecom market and operators such as Orange Reunion, SRR/SFR, Outremer Telecom, Zeop/Oceinde, Idom, and Mediaserv/Canalbox. ARCEP operator/frequency evidence is A-grade for telecom authorization or market context only; it is not a facility registry.
- **Cable landing context / 海缆背景**: SAFE and LION/LION2 are verified through Submarine Networks; SAFE lands at St. Paul, La Reunion. LION connects Madagascar, Reunion, and Mauritius; LION2 extends the system toward Mayotte/Kenya. TeleGeography's Submarine Cable Map is usable but may be JavaScript/bot-protected; use search snippets/API-visible metadata and cross-check with Submarine Networks or operator releases. Cable landing stations are connectivity records, not data centers.
- **IXP context**: Internet Society Pulse reports 1 active IXP in Reunion as of August 2026; PeeringDB search should still be checked for REUNIX/Reunion entries. IXP facts support interconnection context only.
- **Hyperscaler negative**: AWS, Azure, Google Cloud, and OCI official region/location pages list no Reunion cloud region. Azure France South is Marseille/mainland France, not Reunion.
- **Certification negative / caveat**: Uptime Institute and EPI/TIA-942 searches did not surface a Reunion facility certificate in this pass. EPI's country selector includes "Reunion" as a possible country value, which is not evidence of a certified site. Omega 1's ISO 27001/HDS badges are operator claims unless the certificate issuer/register and certificate numbers are captured.

---

## 1. Official Source Routes / 官方源路径

### 1.1 Government, Planning, and ICPE

Primary URLs verified/usable:
- Prefecture / state services: `https://www.reunion.gouv.fr/`
- Region Reunion: `https://www.regionreunion.com/` (reachable but can return Cloudflare/bot protection)
- Departement de La Reunion: `https://www.departement974.fr/`
- Territoire de l'Ouest (TCO): `https://www.tco.re/`
- Saint-Denis mairie: `https://www.saintdenis.re/`
- National digital policy / DINUM: `https://www.numerique.gouv.fr/`

Use local-government and planning records to prove commune, land parcel, permit, construction date, generator/UPS/cooling scope, and public-sector use. For data centers with generators or fuel storage, check DREAL/ICPE records under French `Installations classees` categories, especially combustion/generator references.

High-value verified source:
- TCO article: `https://www.tco.re/actualite-du-tco/lancement-de-la-construction-du-1er-data-center-de-lile-au-port-53046.html`
- TCO/Oceinde press dossier PDF: `https://www.tco.re/wp-content/uploads/2023/05/dp-omega1-04-05-2023.pdf`

Planning query templates:
```text
site:reunion.gouv.fr "centre de données" OR datacenter OR "salle de serveurs" OR "Omega 1"
site:reunion.gouv.fr ICPE "centre de données" OR datacenter OR "groupe électrogène"
site:tco.re "Omega 1" OR datacenter OR "centre de données"
site:regionreunion.com "datacenter" OR "centre de données" OR "cloud souverain"
site:departement974.fr "centre de données" OR "hébergement" OR "salle serveurs"
"permis de construire" "La Réunion" "centre de données" OR datacenter OR "Omega 1"
"enquête publique" Réunion datacenter OR "centre de traitement de données"
```

Extract: permit/application number, applicant, corporate entity, address/parcel, commune, project description, floor area, electrical/generator/cooling detail, decision/status/date, authority, URL, and access date.

### 1.2 Telecom Regulator - ARCEP

Primary URL: `https://www.arcep.fr/`

Use ARCEP to verify operators and market context: Orange Reunion, SRR/SFR, Outremer Telecom/Mobius, Zeop/Oceinde, Idom, Mediaserv/Canalbox, frequency awards, and overseas-observatory material. Do not infer a data center from telecom authorization.

Query templates:
```text
site:arcep.fr Réunion Orange SFR Zeop Océinde "cahier des charges" OR autorisation
site:arcep.fr "La Réunion" "Outremer Telecom" OR "SRR" OR "Zeop"
site:arcep.fr "Observatoire" "outre-mer" Réunion "haut débit" OR fibre OR mobile
site:arcep.fr Réunion datacenter OR "centre de données" OR hébergement
```

### 1.3 Power and Energy - EDF SEI / CRE

Primary URLs:
- EDF SEI / island energy systems: `https://www.edf-sei.fr/`
- CRE: `https://www.cre.fr/`

Use EDF SEI/CRE/PPE documents to support grid connection, electrical constraints, tariff/regulatory context, renewable supply, generators, UPS, transformer size, and island-grid constraints. Power files alone never create a data-center record.

Query templates:
```text
site:edf-sei.fr Réunion "centre de données" OR datacenter OR "Omega 1" OR "poste source"
site:edf.fr Réunion "centre de données" OR "groupe électrogène" OR "poste source"
site:cre.fr Réunion "programmation pluriannuelle" OR PPE OR réseau OR tarif
"Omega 1" "La Réunion" MW OR kVA OR "groupe électrogène" OR "photovoltaïque"
```

### 1.4 Procurement - BOAMP / PLACE / Local Portals

Primary URLs:
- BOAMP: `https://www.boamp.fr/`
- PLACE: `https://www.marches-publics.gouv.fr/`
- TCO procurement: `https://www.tco.re/` > Marches publics
- Region/Departement/mairie procurement pages via their official sites

Procurement is an A-grade lead source for government hosting, cloud, disaster recovery, server-room moves, and managed infrastructure. Unless a tender or award names a facility/address, keep location null and status `lead/procurement`.

Query templates:
```text
site:boamp.fr "La Réunion" "centre de données" OR hébergement OR "cloud" OR infogérance
site:boamp.fr "La Réunion" datacenter OR "data center" OR "sauvegarde" OR PRA OR PCA
site:marches-publics.gouv.fr Réunion "centre de données" OR hébergement OR "salle serveurs"
site:tco.re OR site:regionreunion.com OR site:departement974.fr "marché public" "hébergement" OR "cloud" OR "datacenter"
"La Réunion" "appel d'offres" "cloud souverain" OR "centre de données"
```

### 1.5 Cable Landing and Interconnection

| Asset | Verified source route | Reunion signal | Handling |
|---|---|---|---|
| SAFE | `https://www.submarinenetworks.com/en/systems/asia-europe-africa/safe` | St. Paul, La Reunion landing point | Connectivity only; no DC inference |
| LION / LION2 | `https://www.submarinenetworks.com/en/systems/asia-europe-africa/lion-2` | Connects Madagascar, Reunion, Mauritius; LION2 extension | Connectivity only |
| METISS | `https://www.submarinecablemap.com/submarine-cable/meltingpot-indianoceanic-submarine-system-metiss` plus operator/news cross-check | Reunion landing visible in TeleGeography metadata; exact locality requires cross-check | Connectivity only |
| IXP / REUNIX | PeeringDB search; Internet Society Pulse `https://pulse.internetsociety.org/en/ixp-tracker/country/RE/` | 1 active IXP reported in RE in Aug 2026 | IXP context only |

Cable query templates:
```text
"Saint-Paul" Réunion SAFE OR METISS "landing station" OR "station d'atterrissement"
"La Réunion" SAFE OR METISS OR LION "câble sous-marin"
"Le Port" OR "Saint-Paul" Réunion "câble sous-marin" OR "landing station"
site:submarinenetworks.com Réunion OR "La Reunion" SAFE OR METISS OR LION
"REUNIX" OR "Réunion IX" OR "Reunion Internet Exchange" PeeringDB
```

### 1.6 Certification Registries

Primary URLs:
- Uptime Institute awards/certification search: `https://uptimeinstitute.com/uptime-institute-awards`
- Uptime tier methodology: `https://uptimeinstitute.com/tiers`
- EPI/TIA-942 certified sites: `https://www.epi-certification.com/sites/list`
- TIA: `https://tiaonline.org/`

Rules:
- "Tier 3 equivalent" or "equivalent Tier 3" is not the same as Uptime Tier III certified.
- ISO 27001 and HDS claims must include issuer/register/certificate number before being stored as certification facts; otherwise store as operator claim.
- Country selectors listing "Reunion" are not certified-site evidence.

### 1.7 Hyperscaler Absence Checks

Official pages to recheck each refresh:
- AWS: `https://aws.amazon.com/about-aws/global-infrastructure/regions_az/`
- Azure: `https://learn.microsoft.com/en-us/azure/reliability/regions-list`
- Google Cloud: `https://cloud.google.com/about/locations`
- OCI: `https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm`

Current conclusion: no official Reunion region for AWS/Azure/GCP/OCI. Do not treat reseller hosting, CDN edge, local partner pages, "France South", or mainland France cloud regions as Reunion region evidence.

---

## 2. Per-Division Strategy / 单分区按市镇策略

Division is always `Reunion`. Required commune sweep:

```text
"{commune}" Réunion "centre de données" OR datacenter OR "salle de serveurs" OR hébergement OR colocation
"{commune}" Réunion "groupe électrogène" OR "poste source" OR onduleur OR climatisation
site:reunion.gouv.fr "{commune}" datacenter OR "centre de données" OR telecom
site:boamp.fr "{commune}" "centre de données" OR hébergement OR PRA OR PCA
site:edf-sei.fr "{commune}" "poste source" OR datacenter
"{commune}" "data center" "permis de construire" OR "building permit"
```

| Commune | Official priority | Expected handling |
|---|---|---|
| Le Port | TCO, mairie, planning/ICPE, EDF SEI, operator pages | **Highest priority** because Omega 1 is verified here; also validate SFR Le Port directory lead against first-party/permit evidence |
| Saint-Denis / Sainte-Clotilde / Le Chaudron | Prefecture, mairie, ARCEP, BOAMP/PLACE, operators | Operator offices, SFR/Orange/Zeop/Oceinde leads, possible REUNIX; require facility proof |
| Saint-Paul | mairie, cable sources, EDF SEI | SAFE/METISS landing context; no upgrade to DC without hosting/server evidence |
| La Possession | mairie, industrial planning | Low-output permit/procurement scan |
| Saint-Pierre | mairie, department/local procurement | Southern administrative/economic center; low-medium scan |
| Le Tampon, Saint-Louis, Saint-André, Saint-Benoît, Sainte-Marie, Sainte-Suzanne | mairie, BOAMP/PLACE, EDF SEI | Low-output explicit negative scan |

---

## 3. Seed Records / 种子记录

| Seed | Commune | Status | Capacity | Grade | Best evidence path |
|---|---|---|---|---|---|
| Omega 1 / Omega One data center | Le Port | Operating / inaugurated by Nov 2024; construction launched May 2023 | 1 MW / 120 racks are B unless found in operator/press dossier as first-party; operator claims ISO 27001/HDS and equivalent Tier 3 | A for existence/location from TCO + operator site; B/C for capacity depending source; certification claim pending registry | `omegaone.re`, TCO article/PDF, DCD/local media, certificate registries |
| SFR Business Reunion NETCENTER / hosting | Le Port or unknown; directory says 3 avenue Theodore Drouhet, Le Port | Operating service | null | A for SFR hosting service; C for directory-only address/capacity | `sfrbusiness.re/entreprises-et-collectivites/hebergement/`, DataCenterMap seed, ARCEP |
| Zeop Entreprise hosting/data-center service | Le Port / Saint-Denis / Omega 1 relationship TBD | Operating service / possible Omega 1 tie | null | A for service page; facility identity TBD | `entreprise.zeop.re`, Omega 1, ARCEP |
| Orange Reunion / Orange Business hosting lead | Saint-Denis or unknown | Lead | null | A only for operator/regulatory context; facility not verified | `reunion.orange.fr`, Orange Business, ARCEP, procurement |
| Government hosting/cloud/procurement | TBD | Lead | null | A for tender; location null until award/site evidence | BOAMP, PLACE, Region/Departement/TCO/mairie pages |
| SAFE landing station | Saint-Paul | Connectivity | n/a | B | Submarine Networks, TeleGeography |
| METISS landing | Saint-Paul/Reunion locality to confirm | Connectivity | n/a | B | TeleGeography/Submarine Cable Map, operator releases |
| LION/LION2 landing/context | Reunion locality to confirm | Connectivity | n/a | B | Submarine Networks, Orange/consortium releases |
| REUNIX / local IXP | Saint-Denis likely; verify in PeeringDB | IXP context | n/a | B/A for IXP fact after PeeringDB confirmation | PeeringDB, ISOC Pulse |
| Uptime/TIA/EPI Reunion entries | All communes | Negative in this pass | n/a | A negative after registry search | Uptime, EPI/TIA |

---

## 4. Decision Rules and Pitfalls / 决策规则与陷阱

- **Single division only**: all records use `division = "Reunion"`. Commune/locality is a separate field.
- **Do not duplicate Omega 1**: Zeop and Oceinde belong to the same ecosystem; verify whether Zeop hosting references Omega 1 before adding a separate Zeop facility.
- **Cable landing station is not DC**: SAFE/METISS/LION assets remain connectivity records unless a source explicitly ties the landing station to colocation/server hosting.
- **Telecom license is not a facility**: ARCEP is a pivot, not a DC registry.
- **Power is corroboration**: EDF SEI/CRE/PPE evidence can support power fields but cannot create a DC record alone.
- **Certification precision**: store "equivalent Tier 3" as an operator design/resilience claim unless Uptime/TIA/EPI registry evidence exists.
- **Capacity stays sourced**: do not derive MW, racks, area, or redundancy from cable bandwidth, transformer size, marketing adjectives, or island market size.
- **Bot-protected pages**: if a page is reachable only through search snippets or returns Cloudflare/Vercel checks, record that access limitation and cross-check with another primary or reliable source.
