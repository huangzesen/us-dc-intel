# LI Explorer Official - Liechtenstein Datacenter Enumeration via AHR, Communes, LKW, AK, Registers, and Cloud-Region Controls

Date: 2026-08-12. Scope: Principality of Liechtenstein (LI), all 11 Gemeinden: Balzers, Eschen, Gamprin, Mauren, Planken, Ruggell, Schaan, Schellenberg, Triesen, Triesenberg, Vaduz. Purpose: official/regulatory workflow for finding, validating, and grading datacenter, colocation, telecom-room, and large server-room facilities. Reliability grades: **A** = official/primary government, commune, utility, regulator, legal, register, or operator-owned source; **B** = established press/trade/association source that still needs primary confirmation for facility facts; **C** = directory/aggregator/SEO/market-list source, usable only as a lead.

Final review note: Liechtenstein has no public national datacenter register and no single national building-permit search portal. Enumeration must be done by combining national AHR building authority records, each commune's Bauverwaltung/Baubewilligung surface, LKW energy/telecom infrastructure records, AK telecom colocation documents, company-register checks, geodata, and local press.

---

## 0. Structural facts

- Liechtenstein is a microstate with 11 communes. Complete division coverage is: **Balzers; Eschen; Gamprin; Mauren; Planken; Ruggell; Schaan; Schellenberg; Triesen; Triesenberg; Vaduz**. Do not omit smaller/rural communes; they are low-probability but required sweeps.
- Building-law execution is split: the national **Amt fuer Hochbau und Raumplanung (AHR)** is the building authority for building-law process, while communes participate through their own Bauverwaltung, Bauordnung, Zonenplan, Gemeinderat/commission minutes, and local consultation. Older pages may still say **Amt fuer Bau und Infrastruktur (ABI)**; current state authority is AHR.
- German is the working language. Use `Rechenzentrum`, `Datacenter`, `Data Center`, `Datenzentrum`, `Serverraum`, `Kollokation`, `Housing`, `Cloud`, `Baugesuch`, `Baubewilligung`, `Baufreigabe`, `Bauabnahme`, `Inbetriebnahme`, `Trafostation`, `Netzanschluss`, `USV`, `Notstrom`, `Kuehlung`, `Abwaerme`.
- Official permit strength: `Baugesuch` / `Auflage` = lead; `Baubewilligung` / `Bewilligungsbescheid` / `Baufreigabe` = permit evidence; `Bauabnahme`, `Inbetriebnahme`, `eroeffnet`, or active official/operator service page = operating evidence. Record the status word exactly.
- Energy/grid is a decisive corroboration channel. **Liechtensteinische Kraftwerke (LKW)** is the state-owned electricity and telecom network operator and publishes annual reports and telecom colocation documents. Large datacenter projects should create LKW grid, transformer, or customer-power traces even if permit notices are thin.
- Telecom regulator **Amt fuer Kommunikation (AK)** publishes market-regulation and colocation/unbundling material. AK colocation lists are official for network-access colocation points, but they are not a comprehensive commercial datacenter registry.
- No official AWS, Azure, Google Cloud, or Oracle region exists in Liechtenstein. Treat cloud-region pages as A only for the absence/presence and names of logical cloud regions, never as proof of a physical LI facility.

---

## 1. Official source backbone

| Source | URL | Grade | How to use |
|---|---|---:|---|
| AHR eBaugesuch / Baubewilligung | https://www.llv.li/de/landesverwaltung/amt-fuer-hochbau-und-raumplanung/baurecht-und-brandschutz/ebaugesuch | A | Current national building-application/process surface. Use for process vocabulary and as the state contact route when commune records are incomplete. |
| AHR main page | https://www.llv.li/de/landesverwaltung/amt-fuer-hochbau-und-raumplanung | A | Confirms current authority name and contact context. |
| AHR Formserver Bauvorhaben | https://formulare.llv.li/hba/folders/HBA/forms/Bauvorhaben | A | Official e-form surface for building projects; useful for required data fields. |
| Building law | https://www.gesetze.li | A | Use for Baugesetz, Raumplanungsgesetz, Energiegesetz, Kommunikationsgesetz, Vergabegesetz. Legal context only, not facility evidence. |
| Statistikportal Bautätigkeit | https://www.statistikportal.li/de/themen/bauen-und-wohnen/bautaetigkeit | A | Aggregate construction activity. It reports AHR-issued Baubewilligungen/Baufreigaben, including industrial/services projects, but is not datacenter-specific. |
| Geodatenportal | https://www.llv.li/de/landesverwaltung/amt-fuer-tiefbau-und-geoinformation/geodateninfrastruktur/geodatenportal | A | Parcel, zoning, orthophoto, and address validation. Cross-check `Parzelle`, street, zone, and industrial area. |
| Open data | https://www.opendata.li and https://opendata.swiss/de/organization/amt-fuer-tiefbau-und-geoinformation-fl | A | Downloadable geodata/statistical data where available. |
| Handelsregister | https://handelsregister.li | A | Entity/SPV validation. Search operators and terms: `Rechenzentrum`, `Datacenter`, `Data Center`, `Kollokation`, `Cloud`, `Server`. |
| AK main page | https://www.llv.li/de/landesverwaltung/amt-fuer-kommunikation | A | Telecom regulator; use for operator/regulatory context. |
| AK/LKW colocation Standortliste | https://www.lkw.li/userdata/Alle-Download-Dokumente/Netze-Kommunikation/Kollokation/lkw-kollokation-standortliste-v1.4.pdf | A | Official LKW colocation-site list; includes access-network locations such as Eschen Hub 37. Extract all LI access-network colocation points, but do not count each as a commercial datacenter without extra evidence. |
| AK TAL copper unbundling locations | https://www.llv.li/serviceportal2/amtsstellen/amt-fuer-kommunikation/import/pdf-llv-ak-tal_kupfer_standorte_entbuendelung_v1.0.pdf | A | Official consultation/listing with colocation availability at access-network locations. Useful for telecom colocation leads in Balzers, Eschen, Schaan, Schaanwald, Mauren, etc. |
| LKW official site | https://www.lkw.li | A | State utility/operator site. Confirm HQ, downloads, energy/telecom network role, and annual reports. |
| LKW annual reports | https://www.lkw.li/hilfe-und-service/downloads/jahresbericht/ | A | Scan yearly for `Rechenzentrum`, `Kollokation`, `Netzausbau`, `Trafostation`, `Anschlussleistung`, `Grosskunde`, `Eschen`, `Schaan`, `Ruggell`, `Balzers`. |
| Energiefachstelle / AVW | https://www.llv.li/de/landesverwaltung/amt-fuer-volkswirtschaft/energie-energiefachstelle | A | Energy policy and efficiency context. No LI-specific datacenter energy-efficiency register identified. |
| energiebuendel.li | https://www.energiebuendel.li | B+ | State energy-information site; good context, not facility proof. |
| Public procurement | https://www.llv.li/de/landesverwaltung/stabsstelle-regierungskanzlei/fachstelle-oeffentliches-auftragswesen | A for office / B for discovery | Use for procurement rules and contacts. Search notices separately on llv.li, commune pages, and official/publication channels. |

---

## 2. Query patterns

Use German first; add English only after local sweeps.

### 2.1 Permit and commune records

```text
"{Gemeinde}" "Rechenzentrum" "Baugesuch"
"{Gemeinde}" "Rechenzentrum" "Baubewilligung"
"{Gemeinde}" "Datacenter" "Baugesuch"
"{Gemeinde}" "Kollokation" "Baubewilligung"
site:{gemeinde-domain} Rechenzentrum Baugesuch
site:{gemeinde-domain} Datacenter Baubewilligung
site:{gemeinde-domain} Serverraum Baugesuch
site:{gemeinde-domain} "Im alten Riet" Datacenter
site:{gemeinde-domain} "{Operator}" Baugesuch OR Baubewilligung OR Baufreigabe
filetype:pdf "{Gemeinde}" Rechenzentrum Baugesuch
filetype:pdf Liechtenstein Rechenzentrum Baubewilligung
site:llv.li Rechenzentrum Baubewilligung
site:llv.li Rechenzentrum Baufreigabe
site:llv.li "Baugesuch" "{Operator}"
```

### 2.2 Energy/grid/environment

```text
site:lkw.li Rechenzentrum OR Datacenter OR Kollokation
site:lkw.li Jahresbericht Rechenzentrum
site:lkw.li Netzausbau Trafostation "{Gemeinde}"
"Liechtensteinische Kraftwerke" Rechenzentrum Netzanschluss
"LKW" "{Gemeinde}" Rechenzentrum Trafostation
"LKW" "{Operator}" Anschlussleistung
"Liechtenstein" Rechenzentrum Stromverbrauch MW
site:energiebuendel.li Rechenzentrum OR Serverraum OR Abwaerme
site:llv.li Rechenzentrum Energieeffizienz OR Energie
```

### 2.3 AK/telecom

```text
site:llv.li "Amt fuer Kommunikation" Kollokation
site:llv.li "Kollokation" "Standortliste"
site:lkw.li "Kollokation" "Standortliste"
site:llv.li "TAL Kupfer" "Standorte Entbuendelung"
"Hub 37" Eschen Kollokation
"Hubstrasse 37" Eschen Kollokation
"Schaanwald" "Kollokation fuer alternative Betreiber"
```

### 2.4 Register, geodata, procurement, press

```text
site:handelsregister.li Rechenzentrum OR Datacenter OR "Data Center" OR Kollokation
site:geodaten.llv.li "{Strasse}" "{Gemeinde}"
site:opendata.li Bauzone "{Gemeinde}" OR Zonenplan
site:llv.li Ausschreibung Rechenzentrum OR Datacenter OR Kollokation OR Cloud
site:{gemeinde-domain} Ausschreibung Rechenzentrum OR Cloud OR Server
site:vaterland.li "{Gemeinde}" Rechenzentrum OR Datacenter
site:eliechtensteinensia.li "{Gemeinde}" Rechenzentrum OR Datacenter
site:lie-zeit.li "{Gemeinde}" Rechenzentrum OR Datacenter OR Baugesuch
```

### 2.5 English pivots

```text
"Liechtenstein" "data center" "building permit"
"Liechtenstein" "colocation" "Hub 37"
"Vaduz" OR "Schaan" OR "Eschen" OR "Balzers" "data center" permit
"Liechtenstein" "data center" "grid connection" OR "power" OR "MW"
"AWS" OR "Azure" OR "Google Cloud" OR "Oracle" "Liechtenstein" region
```

---

## 3. Commune-by-commune official strategy

Run every commune as: **known operator/address seed -> Bauverwaltung/Baubewilligung page -> commune site/PDF search -> Gemeinderat/Kundmachungen -> AHR/LLV search -> LKW/AK grid/telecom cross-check -> local press**.

| Commune | Official building URL | Grade | Known official/permit priority | Required local queries |
|---|---|---:|---|---|
| Balzers | https://www.balzers.li/de/gemeinde/verwaltung/bauverwaltung/tblid/299 | A | Kyberna lead at Fabrikstrasse 4; industrial zone. Confirm any Baugesuch/Baubewilligung and later changes with Bauverwaltung. | `site:balzers.li Rechenzentrum`; `site:balzers.li Kyberna Baugesuch`; `"Fabrikstrasse 4" Balzers Baubewilligung`; `site:balzers.li Datacenter` |
| Eschen | https://www.eschen.li/verwaltung-service/service/dienstleistung/baubewilligung/ and https://www.eschen.li/bereich/bauwesen/ | A | Highest priority. LKW colocation at Hub/Hubstrasse 37; vestra Eschen lead; SupraNet/QualityNet Eschen lead; Nendeln included in commune. | `site:eschen.li Rechenzentrum Baugesuch`; `"Hub 37" Eschen Kollokation`; `"Hubstrasse 37" Eschen`; `"Wirtschaftspark 65" Eschen Rechenzentrum`; `"vestra" Eschen Rechenzentrum` |
| Gamprin | https://www.gamprin.li/verwaltung-politik/verwaltung/bauverwaltung | A | No verified commercial DC lead. Include Bendern/Unterbendern industrial and telecom locations as possible infrastructure leads. | `site:gamprin.li Rechenzentrum`; `site:gamprin.li Datacenter`; `"Bendern" Kollokation LKW`; `"Gamprin" Serverraum Baugesuch` |
| Mauren | https://www.mauren.li/planen-bauen and https://www.mauren.li/bauverwaltung | A | No verified commercial DC lead. Schaanwald is part of commune; AK/LKW lists show telecom colocation leads in Schaanwald/Mauren access-network context. | `site:mauren.li Rechenzentrum`; `"Schaanwald" Datacenter`; `"Schaanwald" Kollokation`; `"Weiherring 10" Mauren Kollokation`; `"Saegenstrasse 11" Schaanwald Kollokation` |
| Planken | https://www.planken.li/service/planen-und-bauen/baubewilligung | A | No known facility; smallest/rural commune. Sweep for server rooms in municipal/public buildings only. | `site:planken.li Rechenzentrum`; `site:planken.li Datacenter`; `"Planken" Serverraum`; `"Planken" Baugesuch Rechenzentrum` |
| Ruggell | https://www.ruggell.li/baubewilligung and https://www.ruggell.li/bauverwaltung | A | No verified commercial DC lead, but industrial/logistics area makes it a required grid/permit sweep. | `site:ruggell.li Rechenzentrum`; `site:ruggell.li Datacenter`; `"Ruggell" Rechenzentrum Baugesuch`; `"Ruggell" Trafostation Rechenzentrum` |
| Schaan | https://www.schaan.li/gemeinde-politik/verwaltung-abteilungen/gemeindebauverwaltung and https://www.schaan.li/leben-soziales/bauen-und-immobilien/baugesetz | A | Very high priority. SpeedCom official site says two datacenters in Liechtenstein; directory seed at Im alten Riet 153. SupraNet official page also says Schaan and Eschen DCs. LKW HQ at Im alten Riet 17. | `site:schaan.li Rechenzentrum Baugesuch`; `"Im alten Riet 153" Datacenter`; `"Im alten Riet 121" SupraNet`; `"SpeedCom" Schaan Datacenter`; `"SupraNet" Schaan Rechenzentrum`; `"newsnet" Schaan Datacenter` |
| Schellenberg | https://www.schellenberg.li/service | A | No known facility. Use service page, Bauverwaltung contact, Gemeinderat PDFs, and zoning/industrial terms. | `site:schellenberg.li Rechenzentrum`; `site:schellenberg.li Datacenter`; `"Schellenberg" Baugesuch Serverraum`; `"Schellenberg" Kollokation` |
| Triesen | https://www.triesen.li/baugesuch-baubewilligung and https://www.triesen.li/bauverwaltung | A | No verified commercial DC lead. Industrial/service permits and power infrastructure still relevant. | `site:triesen.li Rechenzentrum`; `site:triesen.li Datacenter`; `"Triesen" Serverraum Baugesuch`; `"Triesen" Trafostation Rechenzentrum` |
| Triesenberg | https://www.triesenberg.li/gemeinde/bauen-planen/baubewilligungen/ | A | No known facility; mountain commune. Sweep for municipal/server-room upgrades, telecom shelters, and Malbun-related infrastructure. | `site:triesenberg.li Rechenzentrum`; `site:triesenberg.li Datacenter`; `"Triesenberg" Serverraum`; `"Malbun" Serverraum OR Kollokation` |
| Vaduz | https://www.vaduz.li/wohnen-umwelt/wohnen-bauen/planen-bauen and https://www.vaduz.li/politik-verwaltung/verwaltung/abteilungen/bau-und-infrastruktur | A | High priority. ICT-Center Vaduz at Schwefelstrasse 5A (directory/operator lead), vestra Vaduz at Landstrasse 107 (operator says Vaduz DC), FL1/Telecom Liechtenstein HQ at Schaanerstrasse 1 but do not count without facility evidence. | `site:vaduz.li Rechenzentrum Baugesuch`; `"Schwefelstrasse 5A" Rechenzentrum`; `"Landstrasse 107" vestra Rechenzentrum`; `"ICT-Center" Vaduz Baubewilligung`; `"FL1" Vaduz Rechenzentrum` |

State-wide commune sweeps for each division:

```text
"{Gemeinde}" Rechenzentrum Baugesuch OR Baubewilligung OR Baufreigabe
site:llv.li "{Gemeinde}" Rechenzentrum
site:statistikportal.li "{Gemeinde}" Bautätigkeit
site:vaterland.li "{Gemeinde}" Rechenzentrum OR Datacenter
site:eliechtensteinensia.li "{Gemeinde}" Rechenzentrum OR Datacenter
site:lie-zeit.li "{Gemeinde}" Rechenzentrum OR Datacenter
```

---

## 4. Extraction fields and evidence rules

For every candidate, extract:

```text
country=LI
division={one of the 11 communes}
settlement/locality={e.g. Nendeln, Schaanwald, Bendern, Malbun}
operator/legal_entity
facility_aliases
street_address
parcel/Grundstueck/Parzelle
source_url
source_grade=A/B/C
evidence_type=permit|operation|telecom_colocation|grid|directory|press|register|cloud_region
status_word_original
status_normalized=lead|permit|construction|operating|rejected|retired|unknown
permit_authority=AHR|commune|unknown
permit_number/date if available
power_fields=IT load|connection capacity|annual consumption|substation/transformer|UPS|diesel|cooling|waste heat
last_verified_date
```

Evidence rules:

- Count a physical datacenter only with A/B evidence for **location + operator + operating/permit status**.
- An official AK/LKW telecom colocation point is A for network-access colocation but not automatically a commercial datacenter.
- Operator pages are A for what the operator states about its own services/sites, but grade capacity, redundancy, and opening dates only as A when backed by operator datasheets or permits; otherwise B.
- Directories such as Data Center Map, Data Center Catalog, Inflect, colo.exchange, PQ.hosting, DCHub, and PeeringDB are C or B-/C leads depending on user-maintained status. They can seed addresses, but do not use them alone for final facility records.
- Negative claims for rural communes are never A unless the commune/AHR directly confirms no records. Otherwise record as "no public evidence found in sweep date".

---

## 5. Cloud-region proximity

Use cloud pages only to prevent false positives. Official region pages checked in this review:

| Provider | Official source | Nearest official regions | LI handling |
|---|---|---|---|
| AWS | https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | Europe (Zurich) `eu-central-2`; Frankfurt `eu-central-1`; Milan `eu-south-1` | No listed Liechtenstein region. No AWS Austria/Vienna region listed in the official regions table at review time; remove stale `eu-central-3` assumptions unless a future official page confirms it. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | Switzerland North; Switzerland West; Austria East `austriaeast` in Vienna | No LI region. Azure Austria East is real and official, but it is not LI. |
| Google Cloud | https://cloud.google.com/about/locations | Zurich `europe-west6`; Milan `europe-west8`; Frankfurt `europe-west3` | No LI region. |
| Oracle Cloud | https://www.oracle.com/cloud/public-cloud-regions/ and https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | Zurich `eu-zurich-1`; Frankfurt `eu-frankfurt-1` | No LI region. |

Quarterly control query:

```text
("Liechtenstein" OR "Vaduz") ("AWS" OR Azure OR "Google Cloud" OR Oracle) ("region" OR "availability zone" OR Rechenzentrum OR Datacenter)
site:aws.amazon.com Liechtenstein region
site:learn.microsoft.com azure Liechtenstein region
site:cloud.google.com Liechtenstein region
site:oracle.com Liechtenstein cloud region
```

---

## 6. Final reliability posture

- **High confidence (A/B)**: all 11 commune coverage and domains; AHR/AK/LKW/statistics/legal/register backbone; lack of national public DC registry; need for per-commune permit search; no official LI hyperscale cloud region.
- **Medium confidence (B)**: likely concentration of commercial datacenter/colo facilities in Vaduz, Schaan, Eschen, and Balzers; rural commune negatives are public-web negatives only.
- **Low confidence without follow-up (C)**: directory facility counts, MW/square-foot figures, rack counts, and exact site addresses not repeated on official/operator pages.

Operational conclusion: a final LI facility inventory should be built from operator/AK/directory seeds, then individually reconciled against AHR/commune permits, Handelsregister entities, LKW/grid traces, geodata parcels, and local press. Treat every uncorroborated directory entry as a lead.
