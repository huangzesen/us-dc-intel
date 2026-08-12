# LV Explorer Industry - Latvia Datacenter Enumeration via Operators, Trade Press, Directories, and Municipality Query Patterns

Date: 2026-08-12. Scope: Latvia (LV), 43 municipality/state-city divisions. Focus angle: industry/trade/operator-led discovery, then official verification. Reliability grades: **A** = official/primary source or operator-owned current page, **B** = strong secondary/trade/association source, **C** = weak/aggregate/unverified.

---

## 0. Latvia-specific market frame

- Latvia is a **Riga-first** data-center market with a small number of strongly visible operators: **Delska/DEAC**, **Tet/Tet Cloud**, and **LVRTC**. The second layer is project/developer leads in **Salaspils**, **Liepaja**, **Jekabpils**, **Kurzeme**, and older/smaller enterprise facilities such as **C.T.Co in Valdlauci**.
- There is no official cloud hyperscale region publicly listed in Latvia by AWS, Azure, Google Cloud, or Oracle as of 2026-08-12. Do not infer an AWS/Azure/GCP/OCI datacenter from cloud customers, local offices, or managed-service providers.
- The practical discovery chain is: **operator/trade lead -> operator page -> municipal/BIS construction evidence -> power/fiber/heating evidence -> directory cross-check**.
- Latvian-language searches matter. Trade pages often use English `data center`, while municipalities and construction/utility documents use `datu centrs`, `datu centra`, `buvatlauja`, `nodosana ekspluatacija`, `elektroapgade`, `20 kV`, `110 kV`, `optiskais pieslegums`, and `atlikumsiltums`.
- Be careful with Latvian words `datu` and `centrs`: many false positives are statistical data centers, geospatial portals, library/database centers, school IT rooms, or generic "data" services. A valid facility needs a hosting/colocation/cloud/HPC/telecom-infrastructure signal.

---

## 1. Industry, trade press, and directory sources

### 1.1 Strong industry/trade sources

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com/ ; queries `site:datacenterdynamics.com Latvia Tet Delska DEAC LVRTC data center`, `site:datacenterdynamics.com Latvia DC7 Salaspils` | Best international trade feed for Latvia project announcements and follow-up status. DCD reported Tet DC7 completion/operations in 2026 and earlier DEAC/Delska developments. | B |
| Latvian Public Media / LSM English | https://eng.lsm.lv/ ; query `site:eng.lsm.lv Tet data center Salaspils Latvia` | Public-media confirmation for large national projects, especially Tet DC7 investment and Salaspils context. | B |
| Labs of Latvia | https://labsoflatvia.com/en/ ; query `site:labsoflatvia.com data center Latvia DEAC Tet LVRTC` | Latvian startup/investment press; useful for innovation, cloud, cybersecurity, and investment leads. | B/C |
| Baltic Times / BNN / regional business press | Queries: `site:baltictimes.com Latvia data center Tet`, `site:bnn-news.com Tet data center Latvia`, `Latvia data center investment Salaspils` | Context on Tet strategy, export/cloud/cybersecurity business, and major Latvian ICT investments. Verify facts with operator/municipal pages. | B/C |
| Datacenter Forum | https://www.datacenter-forum.com/ ; query `Latvia Tet Delska data center` | Reposts/industry summaries of operator releases; useful for discovering dates and alternate project names. | B/C |
| Contractor / integrator pages | Citrus Solutions: https://www.citrus.lv/en/projects/data-centers/constrution-works-of-the-data-centre-of-c-t-co/ | Can identify completed enterprise/telecom projects not marketed as commercial colo. Verify with operator/BIS if possible. | B |

### 1.2 Directories and aggregators

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| DataCenterMap Latvia/Riga | https://www.datacentermap.com/latvia/ and https://www.datacentermap.com/latvia/riga/ | Seed list for Riga facilities and older colo addresses. Coverage can lag and status/capacity may be inconsistent. | C+ |
| Baxtel Latvia | https://baxtel.com/data-center/latvia | Good for quick list of Delska/Tet/LVRTC/Telia-style entries and visual market context. Verify everything. | C+ |
| Datacenters.com Latvia | https://www.datacenters.com/locations/latvia | Commercial marketplace pages can expose addresses and aliases. Treat as lead only unless mirrored by operator source. | C |
| Cloudscene | https://cloudscene.com/ | Useful for long-tail regional Tet/LVRTC entries, but many facility pages require verification. | C |
| PeeringDB | https://www.peeringdb.com/ | Strong for active interconnection and facility/network relationship. Grade **B** for peering signal, **C** for complete facility census. |
| ColoMap / Inflect | https://colomap.com/ , https://inflect.com/datacenters/emea/latvia | Helpful for regional LVRTC/Telia addresses and edge sites. Verify with operator or municipal pages. | C |

Use directories for aliases, addresses, and operator names, not as final proof of current operations or MW.

---

## 2. Operator and project seed list

Operator pages are **A** for current marketed footprint; capacity/status should be cross-checked where possible.

### 2.1 Delska / DEAC

Primary pages:

- Delska homepage / portfolio: https://delska.com/
- EU North Riga LV DC1: https://delska.com/data-centers/eu-north-riga-lv-dc1/
- Data-center portfolio: https://delska.com/data-centers/

Known Latvia signals to seed searches:

- EU North Riga LV DC1: 10 MW, 1,000 racks, Tier III/LEED messaging, Riga, AI/HPC positioning.
- EU North Riga LV DC2: portfolio lists 2 MW and 240 racks at Cuibes Street 17 in Riga.
- EU North Riga LV DC3: portfolio lists 1 MW and 80 racks, underground data center, Jana Asara Street 24 in Riga.
- Brand/entity aliases: `Delska`, `DEAC`, `DEAC European Data Center Operator`, `Data Logistics Center` only for group context.

Queries:

```text
Delska Riga "10 MW" "data center"
DEAC Riga "Cuibes" "data center"
"Cuibes iela 17" "datu centrs"
"Jana Asara iela 24" DEAC "datu centrs"
site:bis.gov.lv Delska OR DEAC
site:riga.lv Delska OR DEAC OR "datu centrs"
```

### 2.2 Tet / Tet Cloud

Primary pages:

- Tet Cloud data centers: https://tetcloud.com/data-centers
- Tet DC7 first phase official news: https://www.tet.lv/par-mums/jaunumi/tet-datu-centra-dc7-pirma-karta-nodota-ekspluatacija-novembri-planota-sviniga-atklasana
- Tet DC7 foundation/time-capsule official news: https://www.tet.lv/par-mums/jaunumi/jauna-tet-datu-centra-dc7-pamatos-iemureta-laika-kapsula
- Salaspils official DC7 pages: https://salaspils.lv/lv/node/3751 and https://salaspils.lv/lv/node/3972

Seed facilities:

- Riga: `Dattum` (1.4 MW, 100 racks), `Brivibas` (0.7 MW, 50 racks), `Kleistu` (1.2 MW, 122 racks), `Perses` (0.7 MW, 80 racks), `Atlasa` (40 cabinets, up to 15 kW/rack), `Tet DC 6` at Kleistu Street 5 (0.3 MW, 60 racks).
- Salaspils: `DC7`, EUR30m+ investment, first phase completed/put into operation in 2026, planned full completion by 2028, liquid cooling/AI readiness and waste-heat reuse with `Salaspils Siltums`.
- Possible weak/regional entries: Rezekne and partner/DR facilities appear in directories; require operator confirmation.

Queries:

```text
Tet "Dattum" "1.4 MW"
Tet "DC7" Salaspils "datu centrs"
"Tet datu centrs DC7" "nodosana ekspluatacija"
"Krasta iela 2/1" "DC7" OR "Tet"
"Salaspils Siltums" "datu centrs"
"Tet DC 6" "Kleistu Street 5"
site:salaspils.lv "DC7" "datu centrs"
site:salaspils.lv "datu centram" "20kV"
site:bis.gov.lv "DC7" "Salaspils"
```

### 2.3 LVRTC / Baltic Data Hub

Primary pages:

- LVRTC data centers / Baltic Data Hub: https://www.lvrtc.lv/en/baltic-data-hub/data-centers/
- LVRTC Positron announcement: https://www.lvrtc.lv/en/news/datu-centri/lvrtc-most-physically-secure-data-center-baltics/
- LVRTC Positron project page: https://www.lvrtc.lv/projekti/datu-centrs-pozitrons/

Seed signals:

- LVRTC says it operates strategically located data centers: two in Riga and one regional hub about 150 km from Riga, plus a nationwide colocation network with facilities every 100 km.
- Regional LVRTC entries appear in PeeringDB/ColoMap/other directories for Riga TV Tower, Talejas iela 1, Ventspils RTS, Valmiera RTS, Daugavpils RTS, Liepaja RTS. Treat these as interconnection/colo leads unless LVRTC or municipal evidence confirms address/status.
- `Positron` is a high-security data center under construction in Kurzeme with commissioning targeted for early 2027 in official releases; exact location may be intentionally nonspecific.

Queries:

```text
LVRTC "datu centri" "Riga"
LVRTC "Baltic Data Hub" "data centers"
LVRTC "Pozitrons" "datu centrs"
"datu centrs Pozitrons" "Kurzeme"
site:lvrtc.lv "datu centrs" "Ventspils"
site:lvrtc.lv "datu centrs" "Liepaja"
site:peeringdb.com LVRTC "Riga TV Tower"
```

### 2.4 Northern Energy / large power-ready campuses

Primary page:

- Northern Energy projects: https://northernenergy.eu/projects

Seed projects:

- Liepaja Data Centre: developer states a next-generation AI-ready campus in Liepaja Special Economic Zone, 120 MW operational capacity by 2029, 110 kV/33 kV connectivity, renewable power/N-1 redundancy.
- Jekabpils Old Airport Data Centre: developer states 114 MW available today, scalable to 400 MW by 2030, secure land, robust 110 kV grid connections, renewable backup strategy.

These are high-capacity leads but should remain `planned` unless a municipal/BIS/AST/operator commissioning record confirms later lifecycle status.

Queries:

```text
"Liepaja Data Centre" "120 MW"
"Liepaja Special Economic Zone" "data centre" "Northern Energy"
"Jekabpils Old Airport" "data centre" "114 MW"
"Jekabpils" "datu centrs" "110 kV"
site:liepaja-sez.lv "data centre" OR "datu centrs"
site:liepaja.lv "datu centrs" "Northern Energy"
site:jekabpils.lv "datu centrs" "lidosta"
site:ast.lv "Jekabpils" "data centre"
```

### 2.5 Other long-tail leads

- **C.T.Co / Valdlauci / Kekavas novads**: Citrus Solutions project page records completed data-centre construction works for C.T.Co at Meistaru Street 33, Valdlauci, 20 racks: https://www.citrus.lv/en/projects/data-centers/constrution-works-of-the-data-centre-of-c-t-co/. Grade **B**.
- **Telia / Liepaja**: aggregator-only entries list a Liepaja facility. Treat as **C** until Telia or municipal evidence is found.
- **Eway / Ogre**: business-register/directory snippets may mention a historical `DATU CENTRS` department. Treat as **C/historical** unless an operator page proves current facility.
- Local ISP/server-room pages can be useful for edge/hosting census, but do not mix ordinary hosting resellers with physical datacenter operators without address/infrastructure proof.

---

## 3. National query patterns

### 3.1 Industry sweep

```text
"Latvia" "data center" Delska DEAC Tet LVRTC
"Latvia" "data centre" "MW" "Riga" "Salaspils"
"Riga" "data center" "Delska" OR "DEAC"
"Tet" "DC7" "Salaspils" "data center"
"LVRTC" "Positron" "data center"
"Latvia" "AI data center" "MW"
"Liepaja" "data center" "120 MW"
"Jekabpils" "data center" "114 MW"
site:datacenterdynamics.com Latvia "data center"
site:eng.lsm.lv "data center" Latvia Tet
site:labsoflatvia.com "data center" Latvia
site:baltictimes.com "data center" Latvia
```

### 3.2 Latvian-language sweep

```text
"datu centrs" Latvija "MW"
"datu centrs" Riga Tet Delska DEAC LVRTC
"datu centrs" Salaspils Tet DC7
"datu centrs" Liepaja "120 MW"
"datu centrs" Jekabpils "110 kV"
"datu centrs" Kurzeme LVRTC Pozitrons
"datu centrs" "nodosana ekspluatacija"
"datu centra" "pirma karta" "ekspluatacija"
"datu centram" "siltumapgade" OR "atlikumsiltums"
"datu centram" "20kV" OR "110kV"
"serveru telpa" "kolokacija" Latvija
```

### 3.3 Official-verification sweep

```text
site:bis.gov.lv "datu centrs"
site:bis.gov.lv "datu centra"
site:bis.gov.lv "serveru"
site:bis.gov.lv "DEAC" OR "Delska" OR "Tet" OR "LVRTC"
site:sprk.gov.lv "datu centrs"
site:ast.lv "datu centrs" OR "data centre"
site:sadalestikls.lv "datu centrs"
site:vpvb.gov.lv "datu centrs"
filetype:pdf "datu centrs" "buvatlauja"
filetype:pdf "datu centram" "elektroapgade"
```

---

## 4. Division query strategy

Latvia divisions in the manifest are municipalities/state cities. Use a tiered pass:

### 4.1 Tier 1: known/high-probability divisions

**Riga**

```text
"Riga" "datu centrs" Tet Delska DEAC LVRTC
"Riga" "data center" Delska DEAC Tet LVRTC
"Cuibes iela 17" OR "Čuibes iela 17"
"Jana Asara iela 24" OR "Jāņa Asara iela 24"
"Kleistu iela 5" "datu centrs"
"Talejas iela 1" LVRTC
site:riga.lv "datu centrs"
site:bis.gov.lv "Riga" "datu centrs"
```

**Salaspils novads**

```text
"Salaspils" "DC7" "datu centrs"
"Tet datu centra DC7" "Salaspili"
"Krasta iela 2/1" "DC7"
"Salaspils Siltums" "datu centrs"
site:salaspils.lv "DC7"
site:salaspils.lv "datu centram" "20kV"
site:bis.gov.lv "Salaspils" "DC7"
```

**Liepaja**

```text
"Liepaja Data Centre" "120 MW"
"Liepaja" "datu centrs" "120 MW"
"Liepajas Speciala ekonomiska zona" "datu centrs"
"Liepaja SEZ" "data centre" "110 kV"
site:liepaja.lv "datu centrs"
site:liepaja-sez.lv "data centre" OR "datu centrs"
```

**Jekabpils novads**

```text
"Jekabpils Old Airport" "data centre"
"Jekabpils" "datu centrs" "114 MW"
"Jekabpils" "datu centrs" "lidosta"
"Jekabpils" "110 kV" "data centre"
site:jekabpils.lv "datu centrs"
site:bis.gov.lv "Jekabpils" "datu centrs"
```

**Kekavas novads**

```text
"Valdlauci" "datu centrs"
"Meistaru Street 33" "data centre"
"Meistaru iela 33" "datu centrs"
"C.T.Co" "Valdlauci" "data centre"
site:kekava.lv "datu centrs"
```

**Ventspils / Kurzeme / Dienvidkurzemes novads / Kuldigas novads / Talsu novads**

```text
"LVRTC" "Pozitrons" "Kurzeme"
"datu centrs Pozitrons" "Kurzeme"
"LVRTC" "Ventspils RTS"
"Ventspils" "datu centrs" LVRTC
site:ventspils.lv "datu centrs"
site:kurzemeplanning.lv "datu centrs"
site:bis.gov.lv "Pozitrons"
```

### 4.2 Tier 2: regional-city / LVRTC / telecom-edge checks

Run these for **Daugavpils, Valmieras Novads, Rezekne, Jelgava, Jurmala, Ventspils, Liepaja**:

```text
"{division}" "LVRTC" "RTS"
"{division}" "datu centrs" "LVRTC"
"{division}" "data center" "Tet" OR "Telia" OR "LVRTC"
"{division}" "kolokacija"
"{division}" "serveru telpa"
site:peeringdb.com "{division}" "LVRTC"
site:colomap.com "{division}" "LVRTC"
site:datacentermap.com "{division}" "Latvia"
```

Treat LVRTC regional radio/TV station entries as possible colocation/edge data-center nodes. Capture them only when a source explicitly describes colocation/data-center service or interconnection facility.

### 4.3 Tier 3: all remaining municipalities

For lower-yield municipalities such as Aizkraukles, Aluksnes, Adazu, Balvu, Bauskas, Cesu, Dobeles, Gulbenes, Kraslavas, Kuldigas, Limbazu, Livanu, Ludzas, Madonas, Marupes, Ogres, Olaines, Preilu, Rezeknes novads, Ropazu, Saldus, Saulkrastu, Siguldas, Smiltenes, Talsu, Tukuma, Valkas, Varaklanu, Ventspils novads, Augsdaugavas, and others, run a compact pass:

```text
"{division}" "datu centrs"
"{division}" "datucentrs"
"{division}" "serveru ferma"
"{division}" "kolokacija"
"{division}" "datu centram" "elektroapgade"
"{division}" "110 kV" "datu centrs"
site:{municipality-domain} "datu centrs"
site:{municipality-domain} "datu centram"
site:bis.gov.lv "{division}" "datu centrs"
```

If no project appears after this pass and no operator/directory seed exists, `no_projects` is usually appropriate. Keep a note that Latvia hits are concentrated in Riga/Salaspils/Liepaja/Jekabpils/Kurzeme.

---

## 5. Operator/entity aliases

Use aliases aggressively because Latvian public records may use legal names, brand names, or Latvian forms.

```text
Delska
DEAC
DEAC European Data Center Operator
Data Logistics Center
Tet
Tet Cloud
Lattelecom
SIA Tet
DC7
Dattum
LVRTC
Latvijas Valsts radio un televizijas centrs
Baltic Data Hub
Pozitrons
Northern Energy
Northern Europe Energy Group
Liepaja Data Centre
Jekabpils Old Airport
C.T.Co
Fraternitas
Citrus Solutions
Telia
Eway
```

Address aliases:

```text
Cuibes iela 17 / Čuibes iela 17
Jana Asara iela 24 / Jāņa Asara iela 24
Kleistu iela 5
Krasta iela 2/1, Salaspils
Meistaru iela 33, Valdlauci
Talejas iela 1
Riga TV Tower / Rigas radio un televizijas tornis
```

---

## 6. Evidence grading and false-positive handling

### Grade A

- Operator-owned facility pages: Delska, Tet Cloud, LVRTC, Northern Energy.
- BIS construction/operation records.
- Municipal/council/construction-board documents.
- SPRK, AST, Sadales tikls official pages.
- Official cloud-region lists proving presence/absence of public cloud regions.

### Grade B

- Data Center Dynamics, LSM/Latvian Radio, Baltic Times, Labs of Latvia, Datacenter Forum.
- Contractor pages such as Citrus Solutions when they describe completed data-center works.
- PeeringDB for active interconnection signal.

### Grade C

- DataCenterMap, Baxtel, Datacenters.com, Cloudscene, ColoMap, Inflect, Lursoft snippets, social media posts, market-report snippets.

### Common false positives

- Government "data centers" that are information portals, not physical infrastructure.
- `serveru telpa` in an office/school/municipal building with no hosting/colo function.
- Telecom POPs without rack/hosting/colocation evidence.
- Cloud service providers/resellers without physical facility claims.
- Sensitive public-sector/security sites where location is not disclosed: keep only the public geography and do not infer exact municipality.

---

## 7. Recommended data capture

For each candidate:

```text
name
division
city_or_municipality
address_or_public_location
operator
developer
legal_entity_aliases
status
capacity_mw
racks_or_white_space
power_connection_kv
heat_reuse_or_cooling_notes
source_urls
evidence_date
evidence_grade
verification_needed
notes
```

Suggested status rules:

- `operational`: operator says launched/available, municipal source says commissioned/put into operation, or strong current facility page exists.
- `construction`: building works underway, topping-out/foundation/permit evidence, not yet launched.
- `planned`: developer/municipality announces project and site/capacity, but no public construction/commissioning proof.
- `unknown/historical`: only directory, business-register, or old contractor evidence.

Latvia-specific final rule: large claimed MW projects in Liepaja and Jekabpils are important but should not be mixed with operating Riga/Tet/Delska/LVRTC facilities unless their lifecycle stage is separately captured.
