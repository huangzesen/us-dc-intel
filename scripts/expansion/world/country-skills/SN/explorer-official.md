# SN Explorer Official - Senegal Datacenter Enumeration via Permits, Environment, Energy, Telecom Regulation, and State Digital Programs

Date: 2026-08-12. Country: **SN Senegal**. Division model: **14 regions**: Dakar, Diourbel, Fatick, Kaffrine, Kaolack, Kedougou, Kolda, Louga, Matam, Saint-Louis, Sedhiou, Tambacounda, Thies, Ziguinchor. Angle: official/regulatory/state-digital discovery of data centers, colocation sites, telecom operator data centers, government data centers, and substantiated pipeline projects.

Reliability grades:

- **A** = primary/official evidence for the specific data point: commune or urbanism permit process; DEEC/DIREC environmental record; ARTP authorization/licence/sanction; Senelec/CRSE official material; Senegal Numerique SA page; APIX/investment PDF; Uptime Institute award record; official operator or cloud-provider page.
- **B** = strong secondary evidence: DCD, DCmag, Agence Ecofin, CIO Mag, RFI, Le Soleil/major local press, Africa50/project financier, operator press release mirrored by reputable wire/service.
- **C** = weak lead: DataCenterMap/Baxtel/Neocloud/market-report snippets, social posts, old MoUs, unattributed blogs, SEO pages, or any source whose capacity/location claim is not independently supported.

Use the grade per fact, not per facility. Example: an operator page can be **A** for existence and city, while a market aggregator is only **C** for rack count.

---

## 0. Senegal-specific structure facts

- Senegal does **not** publish a complete national datacenter planning register. Enumeration works by joining the approval and operations chain: commune **autorisation de construire** -> **DEEC/DIREC EIES or installations classees** -> **Senelec/CRSE** power evidence -> **ARTP** telecom/network authorization -> **APIX/ZES** investment evidence -> **Senegal Numerique SA / ministry** state program evidence -> operator/Uptime pages.
- Official and press discovery is primarily in French. Search all spellings: `centre de donnees`, `datacenter`, `data center`, `centre de traitement de donnees`, `salle de serveurs`, `hebergement`, `colocation`, `cloud souverain`, `souverainete numerique`, `station d'atterrissage`, `cable sous-marin`, `raccordement`, `poste`, `MW`, `MVA`, `groupe electrogene`, `cuve gasoil`, `installations classees`, `Tier III`, `Uptime`, `Diamniadio`, `Rufisque`, `Almadies`, `Les Mamelles`.
- Commercial and carrier-neutral activity is concentrated in **Dakar region**, especially Dakar department and Rufisque/Diamniadio. **Thies** is an adjacent airport/SEZ watchlist, not a confirmed commercial DC region in current evidence. **Kaolack** has old government-intent signals only; keep as planned/unverified until a current official source appears. The other 11 regions should be run as negative searches for telecom exchanges, government ICT rooms, university rooms, and energy/mining DR rooms.
- **Diamniadio attribution rule**: Diamniadio is a commune in Rufisque department, Dakar region. Press often says near Dakar or near Thies because the airport corridor is nearby; assign to Dakar/Rufisque/Diamniadio unless the source names a Thies-region parcel.
- **Cloud region rule**: official AWS/Azure/GCP/OCI region lists do not show a Senegal public cloud region as of this methodology date. AWS Wavelength/edge, Oracle/Orange planning, and local sovereign-cloud offers are leads only; do not count a hyperscaler region or facility without an official region/location page.

---

## 1. Official portals and regulatory sources

### 1.1 Building authorization / urbanism

Primary source:

- Ministere de l'Urbanisme official service page: https://www.urbanisme.gouv.sn/services-aux-usagers/demande-dune-autorisation-de-construire (**A for process**). The official page says the request is addressed to the mayor of the territorially competent commune and lists supporting documents such as title/property proof, information sheet, descriptive/cost estimate, architectural plans, wastewater/septic plan, cadastral extract, urbanism tax, and fiscal stamp.
- Main ministry portal: https://www.urbanisme.gouv.sn/ (**A for process and ministry context**).
- TeleDAC is the dematerialized building-authorization route. Current Senegal Numerique pages do not expose a clean stable TeleDAC project page, and the old `teledac.sec.gouv.sn` endpoint should not be treated as a reliable source URL. Use Senegal Numerique's main site plus Open Government Partnership documentation as **A/B for platform existence**, but **not** as a searchable permit database: https://www.senegalnumeriquesa.sn/ and https://www.opengovpartnership.org/members/senegal/commitments/SN0006/

Datacenter use:

- New or modified datacenter buildings should leave a commune authorization trail. The public web may only expose notices, council minutes, public-procurement files, or press references; there is no comprehensive public permit search.
- Extract: commune, department, lot/title number, applicant, use description, gross area, height/floors, generator/fuel/storage notes, authorization date/reference, mayor/commune authority.

Usable official/permit queries:

```text
site:urbanisme.gouv.sn ("centre de donnees" OR datacenter OR "data center" OR "centre de traitement")
site:urbanisme.gouv.sn "autorisation de construire" "{operator}"
"TeleDAC" ("{operator}" OR "centre de donnees" OR datacenter OR "autorisation de construire")
"{commune}" "autorisation de construire" (datacenter OR "centre de donnees")
"{commune}" "permis de construire" (datacenter OR "centre de donnees")
"{operator}" "autorisation de construire" (Dakar OR Rufisque OR Diamniadio OR "Les Mamelles" OR Almadies)
"arrete" "{commune}" (datacenter OR "centre de donnees")
```

### 1.2 Environment: DEEC / DIREC / EIES / installations classees

Primary source:

- Direction de la Reglementation Environnementale et du Controle / DEEC portal: https://www.denv.gouv.sn/ (**A**). The portal lists the **Division des Etudes d'Impact Environnemental (DEIE)** and **Division des Installations Classees (DIC)**.
- DIREC/DEEC pages for EIA process: https://www.denv.gouv.sn/avis-de-projet/ and https://www.denv.gouv.sn/division-des-etudes-dimpact-environnemental-deie/ (**A for process**).
- Regulatory instruments on the portal include Arrete ministeriel n 9471 MJEHP-DEEC (terms of reference) and n 9472 MJEHP-DEEC (EIES report content): https://www.denv.gouv.sn/decrets/ (**A for process**).

Datacenter use:

- Datacenters surface through construction EIES, generator/fuel-tank ICPE, substations, cooling/water systems, and larger SEZ/industrial-park EIES documents.
- Extract: project title, promoter, commune/department, parcel or coordinates, power demand, generator size, fuel storage, cooling/water, wastewater, noise/air impacts, public consultation, decision/reference.

Queries:

```text
site:denv.gouv.sn ("centre de donnees" OR datacenter OR "data center")
site:denv.gouv.sn "{operator}" "etude d'impact"
site:denv.gouv.sn Diamniadio EIES
site:denv.gouv.sn "installations classees" "{operator}"
"{project}" "etude d'impact environnemental" Senegal
"{project}" "groupe electrogene" "installations classees" Senegal
"EIES" "Diamniadio" (datacenter OR "centre de donnees")
```

### 1.3 ARTP telecom and network regulation

Primary source:

- ARTP portal: https://artp.sn/ and English portal https://artp.sn/en (**A**).
- Authorization/procedure index: https://artp.sn/liste-des-types-de-demandes-dautorisation-et-procedures (**A for available authorization types**).
- Private independent networks: https://artp.sn/la-regulation/radiocommunications/reseaux-prives-independants (**A**). Relevant for private links/radio systems at DCs or satellite gateways.

Datacenter use:

- ARTP is not a facility register. Use it to verify telecom/operator status, ISP/agrement status, private-network authorizations, satellite gateway authorizations, sanctions, and equipment homologation.
- Strong verified lead: Avanti/Free Senegal. AXIAN/Free announced that Free would build and operate Avanti's gateway from Free's Tier III data centre facility in Diamniadio: https://www.axian-telecom.com/2022/05/23/avanti-communications-and-free-in-senegal-sign-landmark-agreement-to-build-and-host-new-hylas-4-satellite-gateway-in-senegal/ (**A/B: operator-group press release for Free facility and gateway plan**). Avanti later announced HYLAS 4 gateway authorization in Diamniadio: https://www.avanti.space/news/avanti-secures-authorisation-for-hylas-4-satellite-gateway-in-senegal/ (**A for Avanti claim if reachable; otherwise B via reputable telecom press**). Do **not** describe this as an ARTP sanction unless the ARTP decision is retrieved.

Queries:

```text
site:artp.sn ("centre de donnees" OR datacenter OR "data center")
site:artp.sn "{operator}" (licence OR agrement OR autorisation OR sanction)
site:artp.sn "reseaux prives independants" "{operator}"
site:artp.sn Diamniadio (gateway OR passerelle OR antenne OR datacenter)
"ARTP" "{operator}" (datacenter OR "centre de donnees" OR Diamniadio)
"Avanti" "Diamniadio" "autorisation" Senegal
```

### 1.4 Energy: Senelec and CRSE

Primary source:

- Senelec: https://www.senelec.sn/ (**A** for utility material).
- CRSE: https://www.crse.sn/ (**A** for sector regulation/tariffs). CRSE tariff and sector documents are context unless they name a facility or customer connection.
- Uptime has a distinct **Senelec Datacenter Diamniadio** record: https://uptimeinstitute.com/uptime-institute-awards/datacenter/senelec-datacenter-diamniadio-/1245 (**A for certification/location record**). Treat this as a separate Senelec/internal-utility data-center record, not as the Senegal Numerique national DC unless corroborated.

Datacenter use:

- Search for `raccordement`, `poste`, `MVA`, `MW`, `HT`, `MT`, `alimentation electrique`, tenders, and substation work near named DC localities.
- Capture whether power numbers are utility import, transformer capacity, critical power, or IT load.

Queries:

```text
site:senelec.sn (datacenter OR "centre de donnees" OR "data center")
site:senelec.sn "{operator}" (raccordement OR poste OR MVA OR MW OR "haute tension")
site:crse.sn (datacenter OR "centre de donnees" OR "grande consommation")
"{operator}" Senelec (MW OR MVA OR raccordement OR poste) Senegal
"{project}" "alimentation electrique" (Dakar OR Diamniadio OR Rufisque)
```

### 1.5 State digital programs: Senegal Numerique SA / Smart Senegal

Primary source:

- Senegal Numerique SA: https://www.senegalnumeriquesa.sn/ (**A**). Current page states SENUM succeeds ADIE, operates public digital infrastructure, has more than 5,000 km of fiber, and lists **three operational datacenters: Orana, Technopole, Diamniadio**: https://senegalnumeriquesa.sn/fr/senegal-numerique-moteur-de-la-transformation-digitale-de-letat (**A for state operator claim**).
- National Diamniadio DC inauguration/capacity is well supported by 2021 government/press coverage; where official pages are unavailable, use RFI/CIO Mag/Financial Afrik/DCD as **B** for the 22 June 2021 inauguration, 500-1,000 sqm technical/hosting figures, and 1.4 MW claims. Keep exact capacity fields source-specific.
- CDP data protection authority: https://www.cdp.sn/ (**A for law/compliance context, not facility registry**).

Datacenter use:

- The Senegal Numerique page creates two additional official state leads that the draft did not handle enough: **Orana** and **Technopole**. Investigate whether these are full hosting datacenters, government server rooms, disaster-recovery sites, or campus rooms before assigning commercial facility class.
- Treat `cloud national`, `SEN Cloud`, `Smart Senegal`, `JOJ Dakar 2026`, `souverainete numerique`, and `intranet administratif` as state facility pivots.

Queries:

```text
site:senegalnumeriquesa.sn (datacenter OR "centre de donnees" OR cloud OR Diamniadio OR Orana OR Technopole)
site:senegalnumeriquesa.sn "trois datacenters" OR "cloud national"
"SENUM" (Orana OR Technopole OR Diamniadio) datacenter
"ADIE" "Orana" datacenter
"ADIE" "Technopole" datacenter
"Smart Senegal" (datacenter OR "centre de donnees" OR "cloud national")
site:cdp.sn (hebergement OR cloud OR datacenter OR "centre de donnees")
```

### 1.6 Investment and special economic zones: APIX

Primary source:

- APIX / Invest in Senegal: https://investinsenegal.sn/ (**A**).
- APIX digital-economy PDF: https://investinsenegal.sn/wp-content/uploads/2023/10/FR-Secteur-porteur-Economie-Numerique.pdf (**A/B for investment-promotion claims**). It describes a data-center project with work begun in July 2022, expected operational Q2 2024, project amount about USD 12m. Use this as a lead requiring operator identification and current status verification.
- APIX investor guide: https://investinsenegal.sn/wp-content/uploads/2026/01/LeGuideDeLInvestisseurAuSENEGAL_FR_Janv2026.pdf (**A/B for investment context**); mentions data centers/AI/cloud and Diamniadio Tier III context.

Queries:

```text
site:investinsenegal.sn (datacenter OR "data center" OR "centre de donnees")
site:investinsenegal.sn "Economie Numerique" datacenter
site:investinsenegal.sn Diamniadio (datacenter OR "zone economique speciale" OR cloud)
"APIX" (datacenter OR "centre de donnees") Senegal
"ZES Diamniadio" (datacenter OR "centre de donnees" OR cloud)
"Code des Investissements" "{operator}" Senegal
```

---

## 2. Official cloud-region checks

No public hyperscaler cloud region is confirmed in Senegal by official region lists as of 2026-08-12.

| Provider | Official URL | Senegal handling |
|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ and https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | No Senegal region. AWS Wavelength with Orange/Sonatel is an edge/service lead only; map to operator facility only if AWS/Orange/Sonatel names the site. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No Senegal region. Edge/partner claims only. |
| Google Cloud | https://cloud.google.com/about/locations | No Senegal region. Partner/edge claims only. |
| Oracle OCI | https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm and https://www.oracle.com/cloud/public-cloud-regions/ | No Senegal public region. Historical Oracle/Orange West Africa planning is not operational evidence. |

---

## 3. Official/source-graded facility seed list

| Facility/operator | Best verified source(s) | Region assignment | Grade and handling |
|---|---|---|---|
| Senegal Numerique SA / ADIE **Datacenter national de Diamniadio** | Senegal Numerique SA general infrastructure page: https://senegalnumeriquesa.sn/fr/senegal-numerique-moteur-de-la-transformation-digitale-de-letat ; 2021 DCD/Financial Afrik/CIO Mag/RFI inauguration coverage | Diamniadio commune, Rufisque department, Dakar region | **A** for SENUM operating state datacenter infrastructure and Diamniadio being one of three operational state DCs; **B** for older capacity figures unless an official SENUM technical sheet is found. |
| Senegal Numerique SA **Orana** datacenter | Same SENUM page lists Orana among three operational datacenters | Locality to verify, likely Dakar metro | **A lead for state-operated DC name**; facility class/location/capacity require follow-up. |
| Senegal Numerique SA **Technopole** datacenter | Same SENUM page; SENUM contact address is Technopole, Pikine | Technopole/Pikine, Dakar region if confirmed | **A lead for state-operated DC name**; verify whether this is public hosting, internal state DC, or campus/server room. |
| **Senelec Datacenter Diamniadio** | Uptime record: https://uptimeinstitute.com/uptime-institute-awards/datacenter/senelec-datacenter-diamniadio-/1245 | Diamniadio, Dakar region | **A** for Uptime award/location. Separate from SENUM national DC until a primary source links them. |
| **Douanes, BdM Datacenter** | Uptime record: https://uptimeinstitute.com/uptime-institute-awards/list/datacenter/douanes-bdm-datacenter-/1202 | Dakar, Dakar region | **A** for Uptime award/location. Likely government/customs internal DC; not commercial colo unless official service evidence appears. |
| **Sonatel Rufisque Data Center** | Orange Business Senegal page: https://www.orangebusiness.sn/digitaliser/datacenter ; Uptime record: https://uptimeinstitute.com/uptime-institute-awards/datacenter/data-center-sonatel-rufisque/984 | Rufisque, Dakar region | **A** for operator page and Uptime record. Use press for expansions only when dated and corroborated. |
| **Millicom/Tigo/SenConnect Dakar DC Phase-1A / Yas legacy lead** | Uptime record: https://uptimeinstitute.com/uptime-institute-awards/list/datacenter/tigo-senegal-dakar-dc-phase1a/767 ; DCD 2017 article | Dakar/Diamniadio needs source-specific attribution | **A** for Uptime record naming Dakar; **B** for DCD's Diamniadio/SenConnect narrative. Do not rely on DataCenterMap alone for Yas branding. |
| **Free Senegal Diamniadio data centre** | AXIAN/Free press release: https://www.axian-telecom.com/2022/05/23/avanti-communications-and-free-in-senegal-sign-landmark-agreement-to-build-and-host-new-hylas-4-satellite-gateway-in-senegal/ | Diamniadio, Rufisque department, Dakar region | **A/B** for operator-group statement that Free has a Tier III data centre facility in Diamniadio; verify Uptime under current legal entity and exact address. |
| **Avanti HYLAS 4 gateway hosted at Free DC** | AXIAN/Free 2022 release and Avanti 2024 authorization page | Diamniadio, Dakar region | Treat as satellite gateway/tenant evidence, not a separate datacenter unless permits show a separate facility. |
| **Onix Data Centre Senegal** | Onix official update: https://onixdatacentres.com/2023/05/11/tier-3-facility-in-dakar-2023-completion/ ; contact page: https://onixdatacentres.com/o-home/senegal/contact-us/ | Almadies, Dakar department, Dakar region | **A** for operator-claimed facility/location; status after Q4 2023 should be rechecked before marking operational if only older construction/update page is used. |
| **PAIX Dakar** | PAIX press release mirror: https://newswire.telecomramblings.com/2025/01/paix-data-centres-announces-the-construction-of-a-new-ultra-modern-data-centre-in-dakar-senegal/ ; DCD: https://www.datacenterdynamics.com/en/news/paix-data-centres-breaks-ground-on-facility-in-dakar-senegal/ | Les Mamelles, Dakar department, Dakar region | **B/A-** for PAIX announcement via wire and trade press; status is under construction with first phase planned for 2026 unless PAIX posts go-live. |
| **StellarIX Senegal** | https://www.stellar-ix.com/senegal/ | Diamniadio, Dakar region | **A** for operator claim of colocation in a Tier III Design & Facility-certified Diamniadio datacenter; verify Uptime record under owner/client name before making certification fields authoritative. |
| **Jokko / Dariss Consulting sovereign cloud** | https://jokko.africa/ | Dakar, Dakar region | **A** for provider claim of Senegal-hosted cloud in a Tier III+ Dakar datacenter; **C/B** for Tier III+ until Uptime/operator site is identified. |
| **APIX unnamed 2022 data-center project** | APIX digital-economy PDF | Locality/operator to identify | **A/B lead**. Do not count as separate facility until operator, site, and current status are resolved. |
| **Kaolack planned national datacenter** | 2021 press/government-intent references only | Kaolack region | **C lead**. Do not mark active/under construction without current ministry/SENUM/APIX evidence. |

---

## 4. Per-region official enumeration strategy

Run every region even when expected yield is low. Senegal's confirmed public evidence is Dakar-heavy, so non-Dakar passes are mainly for negative coverage and unexpected government/telecom rooms.

| Region | Official strategy | Expected result / caution |
|---|---|---|
| **Dakar** | Search Dakar, Plateau, Almadies, Ouakam, Les Mamelles, Fann, Mermoz, Pikine, Technopole, Guediawaye, Keur Massar, Rufisque, Route de Rufisque, Diamniadio, Bargny across urbanisme, denv, ARTP, Senelec, SENUM, APIX, Uptime. | Highest yield: Sonatel, Onix, PAIX, Senegal Numerique, Senelec, Douanes, Millicom/Tigo/Yas lead, Free, StellarIX, Jokko, cable-landing/edge leads. Keep Diamniadio in Rufisque/Dakar. |
| **Diourbel** | Search Diourbel, Touba, Mbacke plus Sonatel/Free/Expresso, `salle de serveurs`, `intranet administratif`, `EIES`, `poste`. | Low yield. Count only compute/hosting evidence, not telecom shops or ordinary exchanges. |
| **Fatick** | Search Fatick, Foundiougne, Sokone, Saloum, fisheries/admin ICT, Senelec/ARTP. | Low yield; likely government ICT rooms only. |
| **Kaffrine** | Search Kaffrine, Birkelane, Koungheul, Malem Hoddar plus agropole/digitalization and Senelec projects. | Low yield; watch rural connectivity technical rooms. |
| **Kaolack** | Search Kaolack city, Medina Baye, `datacenter de Kaolack`, SENUM/ministry/APIX, `pose premiere pierre`, `mise en service`. | Only old planned national-DC lead is known; keep **C** unless refreshed by official evidence. |
| **Kedougou** | Search Kedougou, Saraya, Salemata, gold/mining operators, `centre de donnees`, `salle serveurs`, `data room`, EIES. | Mining/industrial DR rooms possible; require datacenter-specific function and location. |
| **Kolda** | Search Kolda, Velingara, Medina Yoro Foulah, Casamance ICT, SENUM, university/admin rooms. | Low yield. |
| **Louga** | Search Louga, Linguere, Kebemer, Dahra, agropole, `projet numerique`, telecom rooms. | Low yield. |
| **Matam** | Search Matam, Ourossogui, Kanel, Ranerou, Ogo, border/rural connectivity and Senelec/ARTP. | Low yield; Ogo appears in rural connectivity/satellite coverage contexts, not necessarily DC. |
| **Saint-Louis** | Search Saint-Louis, UGB/Gaston Berger, Richard Toll, Dagana, Podor, university `salle serveurs`, fisheries/admin systems. | Possible university/government server-room leads; avoid counting ordinary IT rooms as DCs. |
| **Sedhiou** | Search Sedhiou, Bounkiling, Goudomp, Casamance digital services and SENUM regional service points. | Low yield. |
| **Tambacounda** | Search Tambacounda, Bakel, Goudiry, Koumpentoum, east corridor, Senelec/ARTP. | Low yield; corridor telecom sites only unless hosting function is named. |
| **Thies** | Search Thies city, Mbour, Saly, Tivaouane, Diass, Ndiass, Blaise Diagne airport, airport/SEZ/industrial park, `autorisation de construire`, `EIES`. | Watchlist region adjacent to Dakar; no confirmed commercial DC in current verified set. Do not misassign Diamniadio to Thies. |
| **Ziguinchor** | Search Ziguinchor, Bignona, Oussouye, Casamance, university/admin ICT and SENUM. | Low yield; possible government/university rooms. |

Regional query block:

```text
"{region}" Senegal ("centre de donnees" OR datacenter OR "data center" OR "salle de serveurs" OR colocation OR hebergement OR cloud)
"{main town}" (Sonatel OR Free OR Expresso OR "Senegal Numerique" OR SENUM) (datacenter OR "centre de donnees" OR "salle de serveurs")
site:urbanisme.gouv.sn "{region}" (datacenter OR "centre de donnees" OR "autorisation de construire")
site:denv.gouv.sn "{region}" (EIES OR "installations classees" OR datacenter)
site:artp.sn "{region}" (licence OR agrement OR autorisation OR sanction)
site:senelec.sn "{region}" (datacenter OR "poste" OR raccordement OR MVA OR MW)
site:senegalnumeriquesa.sn "{region}" (datacenter OR cloud OR "intranet administratif")
site:uptimeinstitute.com/uptime-institute-awards Senegal "{region}"
```

Exact 14-region copy/paste seeds:

```text
Dakar Senegal (Onix OR PAIX OR Sonatel OR Free OR StellarIX OR Jokko OR SENUM OR Senelec OR Douanes) datacenter
Diourbel Senegal ("centre de donnees" OR datacenter OR "salle de serveurs")
Fatick Senegal ("centre de donnees" OR datacenter OR "salle de serveurs")
Kaffrine Senegal ("centre de donnees" OR datacenter OR "salle de serveurs")
Kaolack Senegal (datacenter OR "centre de donnees") (projet OR SENUM OR APIX)
Kedougou Senegal (mine OR or OR Saraya) (datacenter OR "salle de serveurs" OR "data room")
Kolda Senegal ("centre de donnees" OR datacenter OR "salle de serveurs")
Louga Senegal ("centre de donnees" OR datacenter OR "salle de serveurs")
Matam Senegal ("centre de donnees" OR datacenter OR "salle de serveurs" OR Ogo)
Saint-Louis Senegal (UGB OR universite OR administration) (datacenter OR "salle de serveurs")
Sedhiou Senegal ("centre de donnees" OR datacenter OR "salle de serveurs")
Tambacounda Senegal ("centre de donnees" OR datacenter OR "salle de serveurs")
Thies Senegal (Diass OR Mbour OR Saly OR "Blaise Diagne") (datacenter OR "centre de donnees" OR "zone economique")
Ziguinchor Senegal (universite OR administration OR Casamance) (datacenter OR "salle de serveurs")
```

---

## 5. Deduplication and final grading rules

- One physical facility per operator/site. Diamniadio has multiple facility leads; do not merge Senegal Numerique, Senelec, Free, StellarIX, Millicom/Tigo/Yas, and Avanti gateway evidence.
- Uptime records are authoritative for certification/location names but do not prove the business model. A customs or utility DC may be internal only.
- Operator marketing is authoritative for a claimed service/location, but permits, power, and environmental approvals are needed for construction history and parcel-level confidence.
- Aggregators can start a lead but cannot upgrade a facility above **C/B-** without operator, Uptime, permit, regulator, energy, or credible press corroboration.
- Planned/under construction/operational must follow source verbs. `announces`, `plans`, `will build`, `purchased land` = planned/under construction; `inaugurated`, `operational`, `go-live`, Uptime constructed-facility certification, or current service order pages = stronger operational evidence.
- Keep negative coverage logs for all 14 regions so future researchers know low-yield regions were checked.
