# NC Explorer — 行业 / 媒体 / 供应商 勘探方法
# New Caledonia Industry / Trade-Press / Vendor Discovery Methodology

Date: 2026-08-12. Scope: New Caledonia datacenter enumeration methodology focused on industry sources, local media, vendor footprints, network-infrastructure signals, and repeatable French/English query patterns. Use with `explorer-official.md`; official sources remain the acceptance authority.

Manifest coverage: NC has one manifest division, **New Caledonia**. Industry research should still scan Province Sud, Province Nord, Province des Îles Loyauté, and all communes as an internal completeness grid because facilities and permits are local.

Reliability grades: **A** = official/primary source; **B** = strong secondary (established media, trade press, association, validated vendor page); **C** = aggregator, scraped database, social media, self-published commentary, or unverified lead.

---

## 0. 行业框架（industry frame）

- NC does not have a comprehensive public datacenter registry. The realistic inventory is a small set of Nouméa-area commercial hosting/colocation sites, OPT-NC telecom/datacenter history, government DINUM infrastructure, and private enterprise/server rooms.
- The phrase `data center` in NC can mean anything from a true colocation facility to a government server room. Count only records with facility-level evidence: named operator, physical site/commune, service or permit evidence, status, and source URL.
- Large global colocation/hyperscale brands should be treated as negative/remote evidence unless there is a specific NC facility filing. Sydney, Melbourne, Auckland, Singapore, or mainland France regions are not NC facilities.
- Industry leads are useful for discovery but not final counting. Promote B/C leads only after checking official pages, JONC/Juridoc, procurement, Enercal/EEC, or owner filings.

---

## 1. 已验证行业种子（verified industry seeds）

| Entity/source | URL | Verified signal | Grade and use |
|---|---|---|---:|
| DSP / Data Services Pacific | https://dsp.nc | Official site describes DSP as a 100% private hosting company in Nouméa and says it has 2 data centers | A for existence/operator claim; B for marketing language; capacity/address needs confirmation |
| CIPAC article on DSP expansion | https://www.cipac.nc/dsp-extension-data-center-nouvelle-caledonie/ | 2025 article says DSP is extending its second data center in New Caledonia | B lead; verify via DSP/permit/procurement before counting expansion capacity |
| DataCenterMap | https://www.datacentermap.com/new-caledonia/noumea/ | Lists DSP DC1/DC2 and OPT-NC DC Nouville with addresses/rack claims | C/B lead only; scrape cautiously and cross-check |
| Inflect | https://inflect.com/datacenters/apac/new-caledonia | Lists Data Services Pacific DC1 in Nouméa | C/B lead only; not enough for capacity acceptance |
| OPT-NC | https://office.opt.nc and https://www.opt.nc | Official telecom/cable/datacenter history and enterprise services | A where official page/PDF directly states fact |
| Autorité de la concurrence NC | https://autorite-concurrence.nc | Competition case files mention OPT, Offratel, CITIUS and connectivity market structure | A for legal/market facts |
| PITA | https://www.pita.org.fj/about-us/membership/full-members/ | Membership list includes OPT - Office des Postes et Telecommunications - NC - New Caledonia | B for association/member clue |
| APNIC Whois | https://wq.apnic.net | ASNs/addresses for OPT-NC and other NC networks | A network evidence; C facility evidence |
| bgp.tools / PeeringDB | https://bgp.tools and https://www.peeringdb.com | ASN, peering, facility hints | B/C, never facility acceptance alone |

DSP handling:

- Treat `dsp.nc` as the strongest private-sector seed because it is the operator's own site.
- Treat DataCenterMap/Inflect rack, address, and power values as B/C until confirmed by DSP brochure, permit, lease, customer contract, or local official record.
- Search both `DSP`, `Data Services Pacific`, `Le Cube`, `210 rue Gervolino`, `34 rue du général Gallieni`, `Nouméa`, and `Magenta`.

---

## 2. 本地媒体与经济 sources

| Source | URL | Use | Grade |
|---|---|---|---:|
| Les Nouvelles Calédoniennes (LNC) | https://www.lnc.nc | telecom, cable, energy, business projects | B |
| NC La 1ère | https://la1ere.francetvinfo.fr/nouvellecaledonie/ | public-service news, social/economic context | B |
| CCI Nouvelle-Calédonie | https://www.cci.nc | business directory, local IT firms, economic magazine PDFs | B |
| ADECAL | https://www.adecal.nc | investment/economic development leads | B |
| Technopole NC | https://www.technopole.nc | innovation and digital ecosystem leads | B |
| Choose New Caledonia | https://choosenewcaledonia.nc | investment promotion, telecom/economic background | B |
| LinkedIn/Facebook/company social | platform URLs | hiring, photos, expansion hints | C unless official company account and cross-verified |

Local media queries:

```text
site:lnc.nc (datacenter OR "data center" OR "centre de données" OR "câble sous-marin" OR "fibre optique")
site:la1ere.francetvinfo.fr/nouvellecaledonie (datacenter OR "centre de données" OR numérique OR "câble sous-marin" OR cybersécurité)
site:cci.nc ("data center" OR datacenter OR hébergement OR infogérance OR cloud OR "Data Services Pacific")
site:adecal.nc (numérique OR datacenter OR "centre de données" OR cloud)
site:technopole.nc (numérique OR cloud OR hébergement OR cybersécurité)
"Data Services Pacific" "Nouvelle-Calédonie"
"DSP" "data center" Nouméa
```

---

## 3. 全球 / 区域 trade press

| Source | URL | Use | Grade |
|---|---|---|---:|
| Data Center Dynamics | https://www.datacenterdynamics.com | Pacific datacenter/cable announcements; Hawaiki Nui context | B |
| Capacity Media | https://www.capacitymedia.com | subsea and carrier market | B |
| Submarine Cable Networks | https://www.submarinenetworks.com | cable systems and landing routes | B |
| TeleGeography Submarine Cable Map | https://www.submarinecablemap.com | cable map, RFS, landing points | A/B route evidence |
| Telecompaper | https://www.telecompaper.com | telecom/cable announcements | B |
| BW Group / BW Digital | https://bw-group.com | Hawaiki Nui owner/developer announcements | A for owner announcement; B/C for NC facility unless NC landing confirmed |

Trade queries:

```text
site:datacenterdynamics.com ("New Caledonia" OR "Nouvelle-Calédonie" OR Hawaiki OR Gondwana)
site:capacitymedia.com ("New Caledonia" OR Gondwana OR Hawaiki)
site:submarinenetworks.com (Gondwana OR "New Caledonia" OR "Nouvelle-Calédonie")
site:telecompaper.com ("New Caledonia" OR "OPT-NC" OR Hawaiki)
site:bw-group.com Hawaiki Nui ("New Caledonia" OR Pacific)
"Gondwana-1" "New Caledonia" "ready for service"
"Gondwana-2" "Nouméa" Suva
```

---

## 4. 查询词库（French-first discovery terms）

Facility and service:

```text
"centre de données" "Nouvelle-Calédonie"
"data center" "Nouvelle-Calédonie"
datacenter Nouméa (hébergement OR colocation OR cloud OR "salle informatique")
"hébergement de données" "Nouvelle-Calédonie"
"hébergement informatique" Nouméa
"salle serveurs" (banque OR administration OR université OR mine) "Nouvelle-Calédonie"
"centre informatique" (OPT-NC OR DINUM OR DSP OR "Data Services Pacific")
```

Lifecycle/status:

```text
"permis de construire" ("centre de données" OR datacenter OR "salle informatique") "Nouvelle-Calédonie"
"enquête publique" (datacenter OR "centre de données" OR "groupe électrogène")
"appel d'offres" (datacenter OR hébergement OR "système d'information" OR "infrastructures numériques")
"mise en service" ("data center" OR "centre de données" OR "câble sous-marin")
"extension" "data center" Nouméa
```

Power/cooling:

```text
"groupe électrogène" (datacenter OR "salle informatique" OR "centre de données") Nouméa
"onduleurs" "salle informatique" "Nouvelle-Calédonie"
"climatisation" "salle informatique" Nouméa
"puissance souscrite" (DSP OR DINUM OR OPT-NC OR datacenter)
"poste source" Nouméa Enercal
```

Network/cable:

```text
"câble sous-marin" "Nouvelle-Calédonie" (atterrage OR atterrissement OR débarquement)
"GONDWANA-1" Nouméa Sydney
"GONDWANA-2" Nouméa Suva Fidji
"PICOT-2" (Ouémo OR "Mont-Dore" OR Nouville OR Yaté OR Maré OR Lifou)
"station d'atterrissement" Nouméa OR Ouémo OR Nouville
```

---

## 5. Vendor / owner pivot list

Use each name with facility, procurement, legal, and power terms:

| Category | Pivot names |
|---|---|
| Telecom/incumbent | `OPT-NC`, `OPT`, `Office des Postes et Télécommunications de Nouvelle-Calédonie`, `Helia by OPT-NC`, `CITIUS`, `Offratel` |
| Private hosting | `DSP`, `Data Services Pacific`, `Le Cube`, `Nouméa data center`, `Magenta data center` |
| Government | `DINUM`, `Direction du Numérique et de la Modernisation`, `Amadéo`, `Service des infrastructures numériques`, `section réseau et datacenter` |
| Finance | `BCAL`, `Banque Calédonienne d'Investissement`, `BNP Paribas Nouvelle-Calédonie`, `Société Générale Calédonienne de Banque`, `Banque de Nouvelle-Calédonie` |
| Mining/industry | `SLN`, `ERAMET`, `Koniambo Nickel SAS`, `KNS`, `Prony Resources New Caledonia`, `Goro`, `Doniambo`, `Vavouto` |
| Education/research | `Université de la Nouvelle-Calédonie`, `UNC`, `IRD Nouvelle-Calédonie`, `CRESICA` |
| Power | `Enercal`, `EEC-Engie`, `poste source`, `raccordement`, `puissance souscrite` |

Pivot templates:

```text
"{entity}" (datacenter OR "data center" OR "centre de données" OR "salle informatique") "Nouvelle-Calédonie"
"{entity}" (hébergement OR cloud OR infogérance OR cybersécurité) Nouméa
"{entity}" ("RCS Nouméa" OR RIDET OR "registre du commerce") 
"{entity}" ("permis de construire" OR arrêté OR délibération OR "marché public")
"{entity}" (Enercal OR EEC OR "poste source" OR raccordement OR "groupe électrogène")
```

---

## 6. 枚举矩阵（source x evidence）

| # | Source type | Evidence produced | Typical grade | Acceptance rule |
|---|---|---|---:|---|
| 1 | Operator official page | service existence, owner claim, sometimes sites | A/B | Accept existence if specific; verify capacity elsewhere |
| 2 | Procurement | tender/award, scope, buyer, dates | A | Strong for government/regulated projects |
| 3 | JONC/Juridoc/Congrès | legal act, authorization, budget | A | Strong for status and legal owner |
| 4 | Province/commune records | permit, land, environment, council minutes | A | Strongest local location/status evidence |
| 5 | Enercal/EEC | grid/power/raccordement | A | Required for MW claims |
| 6 | Local media | project narrative, dates, quotes | B | Lead unless paired with A source |
| 7 | Trade press | cable/project announcements | B | Lead; cable routes can support official evidence |
| 8 | Industry association | membership, event presentations | B | Entity seed only |
| 9 | APNIC/BGP/PeeringDB | ASN, peering, network presence | A/B network; C facility | Never enough for facility count alone |
| 10 | Aggregators | address/racks/MW | C/B | Use only as clue until confirmed |
| 11 | Social/recruiting | hiring, photos, staff roles | C | Lead only |

---

## 7. Record acceptance and grading

Existence:

- **A**: official owner page names a datacenter/site/service, procurement/permit/JONC record, or official government/authority filing.
- **B**: established media/trade report or association source names the facility/operator.
- **C**: aggregator, scraped listing, LinkedIn/social, unsourced market report.

Capacity:

- **A**: permit, energy/raccordement document, technical appendix, official spec sheet.
- **B**: operator brochure or reputable trade article.
- **C**: aggregator values, sales database, unsourced market estimate.

Status:

- Use exact dates where available.
- `operational` requires current service/official listing or equivalent operational evidence.
- `expansion` must preserve the base facility status and separately grade extension evidence.
- Historical CITIUS/OPT datacenter references should be reconciled against current OPT/DSP/DINUM evidence to avoid double counting merged or retired assets.

Required fields:

```text
name
operator
legal_entity
status
status_date
province
commune
address_or_area
source_urls
evidence_grade_existence
evidence_grade_capacity
it_mw
grid_mw
generator_mw
rack_count
notes
```

---

## 8. 快速优先顺序（fast priority order）

1. `dsp.nc` plus DSP brochure/downloads; then verify DSP DC1/DC2 addresses and expansion through permits, procurement, or local records.
2. `office.opt.nc` annual reports and board PDFs for CITIUS/OPT datacenter history; reconcile current status.
3. `gouv.nc`, `data.gouv.nc`, and JONC/Juridoc for DINUM `réseau et datacenter`, cloud/internal infrastructure, and Ouémo references.
4. `marchespublics.nc` and province procurement rooms for hosting, cloud, cyber, infrastructure, UPS/generator/cooling tenders.
5. Enercal/EEC for any power or MW field.
6. Cable route sweep: OPT GONDWANA/PICOT pages first; TeleGeography/SCN/DCD second.
7. Local media and social/recruiting only to discover names, dates, and terminology.

---

## 9. Source index

- DSP / Data Services Pacific: https://dsp.nc
- CIPAC DSP expansion article: https://www.cipac.nc/dsp-extension-data-center-nouvelle-caledonie/
- DataCenterMap NC/Nouméa: https://www.datacentermap.com/new-caledonia/noumea/
- Inflect New Caledonia: https://inflect.com/datacenters/apac/new-caledonia
- OPT-NC: https://www.opt.nc and https://office.opt.nc
- Autorité de la concurrence NC: https://autorite-concurrence.nc
- Marchés publics NC: https://marchespublics.nc
- LNC: https://www.lnc.nc
- NC La 1ère: https://la1ere.francetvinfo.fr/nouvellecaledonie/
- CCI NC: https://www.cci.nc
- ADECAL: https://www.adecal.nc
- Technopole NC: https://www.technopole.nc
- PITA members: https://www.pita.org.fj/about-us/membership/full-members/
- APNIC Whois: https://wq.apnic.net
- bgp.tools: https://bgp.tools
- PeeringDB: https://www.peeringdb.com
- Data Center Dynamics: https://www.datacenterdynamics.com
- Capacity Media: https://www.capacitymedia.com
- Submarine Cable Networks: https://www.submarinenetworks.com
- TeleGeography Submarine Cable Map: https://www.submarinecablemap.com
- Telecompaper: https://www.telecompaper.com
- BW Group / BW Digital: https://bw-group.com
