# TD Explorer Industry - Chad Datacenter Discovery from Operators, Trade Press, Vendors, Hosting, IXP, and Province Sweeps

Date: 2026-08-12. Scope: Chad (TD) datacenter enumeration from operator/vendor pages, trade press, local press, hosting/ISP pages, cloud/edge announcements, directories, and province-level search patterns. Reliability grades: **A** = official/primary source; **B** = strong trade/local press with named facts; **C** = directory, social, SEO, market-report, or unverifiable lead.

---

## 0. Chad-specific industry frame

- Chad is a **small, state-led data-center market**, not a zero-facility market. Verified industry leads are: the **PMICE National Data Center** in N'Djamena, a **2016 Tigo/Millicom modular communications/colocation data center** in N'Djamena, PMICE **micro data centers**, SOTEL/Airtel/Moov telecom cores, TCHADIX, and small ISP/hosting server rooms.
- The PMICE National Data Center should be staged carefully. 2026 sources show the building complete and equipment installed, but ADETIC/ANSICE/TECHSO audit/certification and final configuration/interconnection were still the gating steps before official exploitation.
- The **2016 Tigo facility matters**: DCD reported a Flexenclosure-built 374 m2 N'Djamena communications/colocation data center with 400 kW IT load, commissioned for Millicom subsidiary Tigo. Tigo Chad was sold to Maroc Telecom in 2019 and rebranded under Moov Africa in 2021, so current verification should follow Moov Africa Chad/Maroc Telecom and ARCEP records.
- French search is mandatory: `centre de données`, `data center`, `datacenter`, `salle serveurs`, `salle informatique`, `hébergement`, `colocation`, `micro Data Center`, `coeur du réseau`, `fibre optique`, `réception`, `certification`.
- Do not count cloud-service availability as a facility. AWS, Azure, Google Cloud, and Oracle have no official Chad region/local zone as of the current official lists; nearby public cloud regions are outside Chad.
- Power and connectivity are validation gates. Any real facility should have a credible N'Djamena/fiber/backhaul story and generator/solar/grid resilience; provincial claims without those details are usually telecom rooms or administrative IT rooms.

Core national query set:

```text
Tchad ("data center" OR "centre de données" OR datacenter) (PMICE OR Huawei OR TECHSO OR certification OR réception)
Chad ("data center" OR "data centre") ("N'Djamena" OR "Tigo" OR "Millicom" OR "Moov Africa" OR SOTEL)
"Tchad" ("micro Data Center" OR "site de backup" OR "site technique") ADETIC ANSICE
"Tchad" ("salle serveurs" OR hébergement OR colocation) "N'Djamena"
"TCHADIX" ("PeeringDB" OR "PCH" OR "point d'échange" OR "G.I.E")
```

---

## 1. High-signal press and industry sources

Use press for discovery, dates, scope, and stage language; then verify with official/operator pages.

| Source | URL / route | Use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD) | `https://www.datacenterdynamics.com/en/news/` | Chad 2016 Tigo/Flexenclosure DC; PMICE 2026 national DC/fiber investment summary. | B |
| Agence Ecofin / Ecofin Agency | `https://www.agenceecofin.com/actualites-numerique/`, `https://www.ecofinagency.com/news-digital/` | PMICE launch and milestones, telecom operator changes, ARCEP/market stories. Often cites ministries. | B |
| Digital Business Africa | `https://www.digitalbusiness.africa/tag/c169-tchad/` | PMICE May 2026 verification status, TCHADIX, data-governance stories. | B |
| WeAreTech.Africa | `https://www.wearetech.africa/` | ANSICE/ADETIC/TECHSO certification and 100 micro-DC report; digital-strategy context. | B |
| TechAfricaNews | `https://techafricanews.com/` | PMICE investment summaries, ADETIC/ANSICE partnership reposts, Maroc Telecom/Moov rebrand context. | B |
| Developing Telecoms | `https://developingtelecoms.com/` | PMICE launch summary, operator/network modernization, recent Moov/SOTEL pressure stories. | B |
| Alwihda Info | `https://www.alwihdainfo.com/` | Strong local source for TCHADIX, TchadElec, provincial announcements, telecom/power issues. | B/C |
| RFI / Financial Afrik / Sika Finance / TchadInfos | respective sites | Power-sector reform, SNE/TchadElec context, local infrastructure politics. | B/C |
| CybersecurityMag Africa | `https://cybersecuritymag.africa/` | ANSICE visits/audit/certification stories; use as lead to ADETIC/ANSICE. | B |
| PeeringDB / PCH / Internet Exchange Map | `https://www.peeringdb.com/`, `https://www.pch.net/ixp` | TCHADIX member/host evidence if/when listed. | B/C |
| Aggregators/directories | DataCenterMap, Baxtel, Cloudscene, datacenters.com, datacenterplatform.com | Discovery only. Expected sparse/empty for Chad; verify every listing. | C |

Scoped searches:

```text
site:datacenterdynamics.com Chad "data center" OR "data centre"
site:agenceecofin.com Tchad "PMICE" OR "data center"
site:ecofinagency.com Chad "data center" OR "PMICE"
site:digitalbusiness.africa Tchad ("PMICE" OR "Data Center" OR TCHADIX)
site:wearetech.africa Chad "national data center" OR "micro data centers"
site:techafricanews.com Chad "data center" OR "Moov Africa Chad"
site:developingtelecoms.com Chad "data centre" OR "network modernisation"
site:alwihdainfo.com TCHADIX OR TCHADELEC OR PMICE
```

Stage language:
- `annonce`, `prévoit`, `MoU`, `ambition`, `plan` = lead only.
- `construction`, `travaux`, `bâtiment achevé`, `équipements installés` = construction/installation, not necessarily operational.
- `audit`, `certification`, `tests`, `interconnexion`, `configuration finale` = pre-operational readiness.
- `réception provisoire`, `inauguré`, `mis en exploitation`, `opérationnel`, `héberge` = stronger status; require A/B source and exact facility.

---

## 2. Operator, vendor, and hosting sweep

| Operator / developer | Official / useful URL | Priority location | Notes |
|---|---|---|---|
| ADETIC / PMICE | `https://adetic.td/`, `https://adetic.td/category/data-center/` | N'Djamena and government institutions | National DC, backup site, micro DCs, TCHADIX. ADETIC is the best official industry-adjacent source. |
| ANSICE | `https://ansice.td/` | N'Djamena | Audit/certification, personal data, cybersecurity resilience. |
| Huawei | `https://www.huawei.com/` | PMICE sites | Delivery contractor for PMICE national DC and telecom infrastructure; verify local claims via ministry/ADETIC. |
| Gulf/GOLF Consultancy | company/press searches | PMICE | Control/supervision office named in 2026 PMICE reporting. |
| TECHSO-GROUP | company/press searches | National DC | Audit/certification partner with ADETIC/ANSICE. |
| Flexenclosure / eCentre | DCD 2016, archive/company pages | N'Djamena | Built Tigo/Millicom modular DC: 374 m2, 400 kW IT load; follow current Moov lineage. |
| Moov Africa Chad / Maroc Telecom | `https://www.iam.ma/` group pages; local Moov pages when live | N'Djamena | Successor to Tigo Chad. Verify whether the 2016 Tigo data center remains active and whether any hosting/colo is public. |
| Airtel Chad | `https://www.airtel.africa/` | N'Djamena | Mobile core/switching rooms; not commercial colo without disclosure. |
| SOTEL / Salam | `https://www.sotel-tchad.td/` | N'Djamena and PMICE sites | State incumbent; core-network modernization under PMICE. |
| ARCEP-authorized ISPs | `https://arcep.td/fournisseurs_acces_internet.html` | Mostly N'Djamena | Candidate small server rooms/hosting nodes; verify each operator page for physical hosting. |
| TCHADIX | ADETIC/press; PeeringDB/PCH searches | N'Djamena likely | IXP equipment host is a high-value facility lead. |
| TIC Tchad | `https://www.tictchad.com/hebergement-web/` | International cloud, not necessarily Chad | States hosting is on cloud/shared/hybrid servers across data centers worldwide; useful negative evidence for local colo scarcity. |
| Afriregister Tchad / local registrars | `https://afriregister.td/`, registry ecosystem | N'Djamena / foreign | Domain/hosting providers; verify if physical servers are in Chad. |

Operator query templates:

```text
"Moov Africa Chad" OR "Tigo Tchad" "data center" OR "centre de données"
"Millicom" "Tigo Chad" "Flexenclosure" "400kW"
"Airtel Tchad" "data center" OR "coeur du réseau" OR "NOC"
"SOTEL Tchad" "coeur du réseau" OR "data center" OR "PMICE"
"Huawei" "PMICE" "Data Center" "Tchad"
"TECHSO-GROUP" ADETIC ANSICE "Data Center"
"{ISP name}" Tchad (hébergement OR serveurs OR colocation OR "salle serveurs")
```

---

## 3. Known industry leads and grading

| Lead | Location | Industry interpretation | Grade |
|---|---|---|---|
| PMICE National Data Center | N'Djamena | New sovereign/government DC. Use "building/equipment installed; audit/certification pending" unless a later A-grade commissioning source is found. | A/B |
| ADETIC backup site | Unpublished | DR/continuity lead inspected during the 2026 TECHSO/ADETIC/ANSICE process; needs location/capacity. | A lead |
| PMICE micro data centers | Government institutions | Distributed micro-DC estate intended to interconnect with the National DC; final configuration/interconnection pending in May 2026 reporting. | A/B |
| Tigo/Millicom Flexenclosure DC | N'Djamena | 2016 modular communications/colocation DC, 374 m2 and 400 kW IT load. Verify current operation through Moov Africa Chad/Maroc Telecom and ARCEP. | B |
| TCHADIX | N'Djamena likely | National IXP/G.I.E. If PeeringDB/PCH or ADETIC publishes host facility, this can identify Chad's first neutral interconnection node. | B |
| SOTEL/Salam core modernization | N'Djamena + national network | Telco core and wireless-site modernization under PMICE; count as telco infrastructure, not public colo. | A/B |
| Airtel and Moov core/switching facilities | N'Djamena | Private telco DC/NOC/server rooms; only count named facilities if official/operator or high-quality press identifies them. | C/B |
| Local ISP hosting rooms | N'Djamena | Possible small server rooms; hosting pages usually prove service, not facility. | C/B |
| Hyperscaler regions | None in Chad | Confirm absence using official cloud pages. | A absence |

---

## 4. Cloud, edge, and directory checks

Cloud:

```text
site:docs.aws.amazon.com "Chad" "AWS Region" OR "Local Zone"
site:learn.microsoft.com/azure "Chad" "region"
site:cloud.google.com/about/locations Chad
site:oracle.com/cloud "Chad" "cloud region"
```

Directories and edge:

```text
site:datacentermap.com/datacenters/chad Chad OR N'Djamena
site:baxtel.com Chad OR N'Djamena
site:cloudscene.com Chad OR N'Djamena
site:peeringdb.com TCHADIX OR "N'Djamena"
site:pch.net TCHADIX OR Chad IXP
site:datacenters.com Chad OR "N'Djamena"
```

Rules:
- Use directories for alternate names, legacy ownership, and coordinates only.
- Never accept directory MW, status, or service type without operator/official confirmation.
- Avoid double-counting: PMICE National DC, ADETIC backup site, micro DCs, SOTEL core, TCHADIX, and Moov/Tigo DC may be related but are separate records only when sources distinguish them.
- Generic pages such as "data center construction management in N'Djamena" are **C/ignore** unless they name a real project, owner, address, and status.

---

## 5. Province-level industry enumeration matrix

Commercial discovery outside N'Djamena is unlikely; provincial sweeps are for PMICE micro DCs, fiber/transmission sites, ADETIC telecentres, telco NOCs, and institutional server rooms.

Universal province query block:

```text
"{province}" Tchad ("data center" OR "centre de données" OR datacenter OR "micro Data Center")
"{capital}" Tchad ("PMICE" OR "fibre optique" OR "site technique" OR "salle serveurs")
site:alwihdainfo.com "{capital}" (PMICE OR numérique OR internet OR fibre)
site:digitalbusiness.africa "{capital}" Tchad
"{capital}" Tchad (Airtel OR Moov OR SOTEL OR ADETIC OR ARCEP)
```

| Province | Capital / main locality | Sweep priority | Industry notes |
|---|---|---|---|
| N'Djamena | N'Djamena | Critical | National DC, ADETIC backup, TCHADIX, Moov/Tigo 2016 DC, telco cores, ISP hosting. |
| Barh El Gazel | Moussoro | Low | Transmission/fiber and telco site sweeps. |
| Batha | Ati | Low | PMICE/site-technique searches; no commercial DC expected. |
| Borkou | Faya-Largeau | Low | Satellite/telecom rooms only unless named. |
| Chari-Baguirmi | Massenya | Low/medium | Capital-adjacent power/fiber/telco support sites. |
| Ennedi Est | Amdjarass | Medium | ADETIC telecentre precedent; institutional ICT rooms. |
| Ennedi Ouest | Fada | Low | Telecom/satellite support only. |
| Guera | Mongo | Medium | ADETIC telecentre precedent; PMICE/fiber leads. |
| Hadjer-Lamis | Massakory | Low/medium | Capital-adjacent transmission and power infrastructure. |
| Kanem | Mao | Low | Telecom/fiber support searches. |
| Lac | Bol | Low | Connectivity/resilience and humanitarian/NGO ICT rooms. |
| Logone Occidental | Moundou | Medium | Second-city telco/ISP rooms and fiber endpoint leads. |
| Logone Oriental | Doba | Medium | PMICE route includes Doba; oil-region telecom/power rooms. |
| Mandoul | Koumra | Medium | PMICE route includes Koumra; micro-DC/fiber sweeps. |
| Mayo-Kebbi Est | Bongor | Medium | ADETIC telecentre precedent and Cameroon-route checks. |
| Mayo-Kebbi Ouest | Pala | Low | Telco/power/institutional rooms only. |
| Moyen-Chari | Sarh | High | PMICE ceremony/reception and route evidence; watch Sarh local press. |
| Ouaddai | Abeche | Medium/high | PMICE route includes Abeche; eastern corridor and ADETIC leads. |
| Salamat | Am Timan | Medium | PMICE route includes Am Timan; transmission/fiber searches. |
| Sila | Goz Beida | Low | Telecom/satellite/public ICT rooms. |
| Tandjile | Lai | Low | Telco/power sweeps. |
| Tibesti | Bardai | Low | Satellite/telecom support only. |
| Wadi Fira | Biltine | Medium | ADETIC telecentre precedent; PMICE route localities Am Zoer/Guereda/Iriba. |

---

## 6. Open gaps to resolve during enumeration

- Pin the PMICE National Data Center's exact address/arrondissement and final commissioning date from ADETIC/ministry/ANSICE.
- Confirm whether the 2016 Tigo/Millicom Flexenclosure facility remains active under Moov Africa Chad, and whether any colocation service is still sold.
- Identify TCHADIX's physical host facility through ADETIC, PeeringDB, PCH, or operator statements.
- Obtain the PMICE inventory list for the micro data centers and 200 transmission sites.
- Separate "micro data center", "institutional server room", and "telecom transmission site" in provincial records; do not merge them into a single DC category.
- Re-check official cloud-region pages quarterly; a Chad region/local zone would be a major new market event.
