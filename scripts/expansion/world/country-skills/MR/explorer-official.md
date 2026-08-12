# MR Explorer Official - Mauritania Datacenter Enumeration

Date: 2026-08-12. Country: **MR Mauritania**. Division model: **15 manifest regions**: Eastern Basin, Western Basin, Assaba, Gorgol, Brakna, Trarza, Adrar, Nouadhibou Peninsula, Tagant, Guidimaka, Tiris Zemmour, Inchiri, West Nouakchott, North Nouakchott, South Nouakchott. Local wilaya aliases are listed below and must be kept in notes.

Scope: official, regulatory, donor, procurement, state-news, and official-operator evidence for datacenter, cloud-hosting, compute, and telecom-hosting infrastructure.

Reliability grades:

- **A** = primary source for the claimed fact: AMI state news; MTNIMA tender / contract / press page; ARE regulator publication; ARMP procurement notice or decision; EIB, EEAS / EU Global Gateway, World Bank project page or project document; Uptime Institute certification record; SDIN / IMT / official telecom operator page.
- **B** = strong secondary used as lead or context: DCD, DCmag.fr, Agence Ecofin, We Are Tech, CIO Mag, World Bank blog, reputable Mauritanian press when it quotes named officials or project documents.
- **C** = weak lead only: directories, generic market reports, consultant SEO pages, tender aggregators, social posts, LinkedIn claims, or operator service pages that do not identify a physical facility.

Grade discipline: A-grade is claim-specific. ARE confirms licence / interconnection status, not a datacenter. MTNIMA confirms a procurement stage, not completion, unless the page says commissioned. EIB / EEAS loan pages confirm funded scope, not MW. Uptime confirms certification award, not operator, rack count, or public colocation service.

---

## 0. Country-Specific Facts

- Mauritania has **no public national datacenter register** and no searchable national planning-permit portal comparable to US county permitting. Enumeration must join official news, procurement, regulator, donor, Uptime, operator, and targeted local searches.
- The public facility market is currently anchored by one A-grade national facility: **Nouakchott Data Hub / Centre d'hebergement de donnees numeriques de Nouakchott** in **West Nouakchott**. It was inaugurated on **8 May 2025**. AMI confirms 1,372 m2, 100 server racks expandable, national cloud / hosting / backup / continuity / AI-big-data services, and operation by IMT. EIB confirms the EUR 15m loan and WARCIP context. Uptime lists **Tier III Certification of Design Documents** and **Tier III Certification of Constructed Facility** for **Nouakchott Data Hub**.
- **SDIN** (Societe pour le Developpement des Infrastructures Numeriques) is a primary infrastructure owner seed. Its official site says SDIN owns WARCIP assets including the national fiber backbone, the Datacenter, and the IXP, under an asset-transfer convention.
- **IMT** (International Mauritania Telecom) is the operational telecom consortium seed. EIB says it brings together the government via Mauripost and the three telecom operators and would manage the data centre once operational. Do not create a second IMT facility record unless a source names another physical site.
- **No official hyperscaler public cloud region** is listed for Mauritania by AWS, Azure, Google Cloud, or OCI. Use the official region pages below as absence evidence; search for edge / partner / customer deployments separately.
- French is the most productive official search language. Arabic is necessary for MTNIMA and AMI mirrors. English is useful for EIB, EEAS, World Bank, DCD, and cable-sector sources.

Useful vocabulary:

```text
data center
data centre
datacenter
centre de donnees
centre d'hebergement de donnees
centre de donnees national
cloud gouvernemental
cloud souverain
hebergement cloud
salle serveur
salle informatique
salle blanche
centre de calcul
supercalculateur
systeme d'information
fibre optique
dorsale nationale
cable sous-marin
station d'atterrissement
point d'echange internet
مركز البيانات
مركز المعطيات
مركز البيانات الوطني
استضافة البيانات
الحوسبة السحابية
قاعة الخوادم
الألياف البصرية
الكابل البحري
مناقصة
```

---

## 1. Primary Official Routes

### 1.1 AMI - State News Agency

Primary URL: https://ami.mr/fr/ ; English mirror: https://ami.mr/en/

Confirmed A-grade anchor:

- AMI FR, 8 May 2025, **Le President de la Republique supervise l'inauguration du Data Center de Nouakchott**: https://ami.mr/fr/archives/270548
- AMI EN mirror: https://ami.mr/en/archives/24220

Facts to extract from AMI for the Nouakchott Data Hub:

- Physical region: **West Nouakchott** by current manifest mapping. Keep local note **Nouakchott-Ouest / Tevragh-Zeina area** when corroborated by local address sources.
- Date: inaugurated 8 May 2025.
- Scale: 1,372 m2 and 100 server racks, expandable.
- Services: national hosting / cloud, secure backup, business continuity / disaster recovery, AI and big-data environment.
- Operator: International Mauritania Telecom (IMT).
- Certification claim: Tier III / 99.982% availability. Use Uptime record below for certification-grade proof.

AMI query templates:

```text
site:ami.mr/fr "data center"
site:ami.mr/fr "centre de donnees"
site:ami.mr/fr "centre d'hebergement de donnees"
site:ami.mr/fr "cloud"
site:ami.mr/fr "cable sous-marin"
site:ami.mr/fr "fibre optique"
site:ami.mr/fr "point d'echange internet"
site:ami.mr/fr "{wilaya_fr}" "numerique"
site:ami.mr/fr "{locality}" "donnees"
site:ami.mr/ar "مركز البيانات"
site:ami.mr/ar "{wilaya_ar}" "الخوادم"
```

Use AMI for presidential inaugurations, foundation stones, and ministerial inspections. It can confirm a facility or project stage, but it rarely gives precise MW / MVA. Leave `capacity_mw` null unless the exact facility power is published.

### 1.2 MTNIMA - Digital Ministry

Primary URLs:

- Main site: https://mtnima.gov.mr/
- French section: https://mtnima.gov.mr/fr/
- EllaLink Nouadhibou landing announcement, 5 May 2026: https://mtnima.gov.mr/fr/ellalink-et-le-mtnima-posent-une-nouvelle-branche-de-cable-sous-marin-a-nouadhibou/
- Public contracts above thresholds, Aug 2024 to Aug 2025: https://mtnima.gov.mr/fr/marches-superieurs-aux-seuils-des-marches-publics-periode-daout-2024-a-aout-2025/
- National Digital Agenda 2022-2025 PDF: https://www.mtnima.gov.mr/sites/default/files/piecesjointes/Agenda_Num%C3%A9rique_2022-2025.pdf
- WARDIP migration-to-cloud notice PDF, July 2026: https://mtnima.gov.mr/wp-content/uploads/2026/07/AMI-45_Migration-Cloud.pdf
- Second submarine cable tender Q&A PDF: https://mtnima.gov.mr/sites/default/files/piecesjointes/R%C3%A9ponses%20liste%201.pdf

High-value MTNIMA signals:

- **Government Cloud**: the public contracts page lists WARDIP **Acquisition et mise en place d'un Cloud Gouvernemental**, contract 1320/F/011/CPMP/MTNIMA/WARDIP/2025, awarded to **HMN SMART CO LTD**, signed 24 Jun 2025, 12 months, MRU 103,611,370. This is A-grade for a government cloud project / platform procurement. It is not, by itself, a new physical datacenter beyond the Nouakchott Data Hub unless a source names a separate site.
- **Cloud migration support**: the July 2026 migration-cloud PDF is an A-grade procurement lead for migration services and should be linked to government cloud uptake, not counted as a facility.
- **EllaLink Nouadhibou**: the 5 May 2026 MTNIMA page confirms the cable landing at Nouadhibou and a neutral cable landing station. This is telecom infrastructure and connectivity context, not a datacenter unless later sources add compute / colocation facilities.
- **Digital Agenda**: confirms planned government cloud services and migration policy context; use as A-grade policy context.

MTNIMA query templates:

```text
site:mtnima.gov.mr/fr "Cloud Gouvernemental"
site:mtnima.gov.mr/fr "hebergement cloud"
site:mtnima.gov.mr/fr "data center"
site:mtnima.gov.mr/fr "datacenter"
site:mtnima.gov.mr/fr "centre de donnees"
site:mtnima.gov.mr/fr "salle serveur"
site:mtnima.gov.mr/fr "fibre optique"
site:mtnima.gov.mr/fr "dorsale"
site:mtnima.gov.mr/fr "cable sous-marin"
site:mtnima.gov.mr/fr "{wilaya_fr}"
site:mtnima.gov.mr "مركز البيانات"
site:mtnima.gov.mr "استضافة"
site:mtnima.gov.mr "{wilaya_ar}"
```

### 1.3 ARE - Telecommunications Regulator

Primary URLs:

- ARE main site: https://www.are.mr/ and https://are.mr/
- Publications route used by older pages: https://www.are.mr/index.php/l-autorite/189-publications
- BU-WAC 2026/2027 interconnection catalogue: https://are.mr/pdfs/IxBUWAC2026-2027.pdf
- Mattel 2026/2027 interconnection catalogue: https://are.mr/pdfs/IxMattel2026-2027.pdf
- Chinguitel 2026/2027 interconnection catalogue: https://are.mr/pdfs/IxChinguitel2026-2027.pdf
- Mauritel 2025/2026 interconnection catalogue: https://are.mr/pdfs/MauritelCatalogueInterco2025-2026.pdf
- ARE 2023 annual report: https://are.mr/pdfs/Rapport2023FR.pdf
- ARE 2022 annual report: https://are.mr/pdfs/RappAnnuel2022Fr.pdf

Use ARE to seed licensed telecom entities and interconnection assets:

- ARE 2023 annual report says the regulator published 2023/2024 interconnection/access catalogues for **Mattel, Mauritel, Chinguitel, IMT, SNIM, IKASIRA, RIMATEL, and SOMELEC**.
- ARE 2022 annual report lists **Mattel, Mauritel, Chinguitel, IMT, SNIM, and IKASIRA** for 2022/2023.
- BU-WAC 2026/2027 catalogue says BU-WAC is a strategic Mauritel unit managing the Mauritanian branch of the WAC submarine cable and the landing point at the terminal station in Nouadhibou. Treat as cable / landing infrastructure, not a datacenter.

ARE query templates:

```text
site:are.mr "data center"
site:are.mr "centre de donnees"
site:are.mr "cloud"
site:are.mr "hebergement"
site:are.mr "catalogue d'interconnexion" "2026"
site:are.mr "{operator}" "catalogue"
site:are.mr "{operator}" "licence"
site:are.mr "5G" "adjudicataires"
site:are.mr "GMPCS"
site:are.mr "satellite"
```

### 1.4 EIB, EEAS, EU Global Gateway

Primary URLs:

- EIB EN, 9 May 2025: https://www.eib.org/en/press/all/2025-202-inauguration-du-centre-d-hebergement-de-donnees-numeriques-de-nouakchott
- EIB FR: https://www.eib.org/fr/press/all/2025-202-inauguration-du-centre-d-hebergement-de-donnees-numeriques-de-nouakchott
- EEAS EN project page: https://www.eeas.europa.eu/delegations/mauritania/construction-datacenter-nouakchott-mauritania_en
- EEAS FR project page: https://www.eeas.europa.eu/delegations/mauritanie/construction-d%E2%80%99un-datacenter-%C3%A0-nouakchott-mauritanie_fr
- EEAS FR inauguration page: https://www.eeas.europa.eu/delegations/mauritanie/inauguration-du-centre-d%E2%80%99h%C3%A9bergement-de-donn%C3%A9es-num%C3%A9riques-de-nouakchott_fr
- EU Global Gateway page covering Nouakchott datacenter and submarine cable: https://international-partnerships.ec.europa.eu/policies/global-gateway/construction-data-center-nouakchott-and-submarine-cable-mauritania_en

Facts:

- EIB confirms the national data centre was inaugurated on 8 May 2025, backed by a EUR 15m loan, and that the financing covered the building, construction supervision, and Tier III certification.
- EIB places the data centre inside WARCIP, co-financed with the World Bank, and says WARCIP built fiber backbone links in north-eastern, southern, and south-eastern Mauritania with international connection points near Senegal and Mali.
- EIB says IMT will manage the data centre and that IMT brings together government via Mauripost and the three telecom operators.
- EU Global Gateway confirms the paired datacenter + submarine cable policy package and says the submarine cable project includes the connection, wet station, terrestrial segment, and cable landing station.

Do not convert EUR loans into capacity. Use these pages for project scope, stage, financiers, and operator only.

### 1.5 World Bank WARCIP / WARDIP

Primary routes:

- Project search: https://projects.worldbank.org/
- Search query: `Mauritania WARCIP` and `Mauritania WARDIP`
- World Bank blog lead: https://blogs.worldbank.org/en/digital-development/mauritania-ramps-broadband-internet-stimulating-private-investment

Use World Bank project pages / PADs as A-grade when they name components, budgets, implementing agencies, and geographies. Use World Bank blogs as B-grade context unless they cite a formal project document.

Core interpretation:

- **WARCIP Mauritania**: official context for the national fiber backbone, ACE-related connectivity, SDIN assets, and the Nouakchott Data Hub.
- **WARDIP Mauritania**: official context for government cloud, NREN, digital payments, public e-services, cross-border integration, and backbone dissemination from new cable capacity. Cloud components are service/platform leads unless a physical facility is named.

World Bank query templates:

```text
site:projects.worldbank.org Mauritania WARCIP
site:projects.worldbank.org Mauritania WARDIP
site:projects.worldbank.org Mauritania "digital integration"
site:projects.worldbank.org Mauritania "cloud"
site:worldbank.org Mauritania "data center"
site:worldbank.org Mauritania "government cloud"
"WARCIP Mauritanie" "centre de donnees"
"WARDIP" Mauritanie "Cloud Gouvernemental"
```

### 1.6 Uptime Institute

Primary URLs:

- Mauritania country awards: https://uptimeinstitute.com/uptime-institute-awards/country/id/MR
- Nouakchott Data Hub award page: https://uptimeinstitute.com/component/tierachievement/datacenter/nouakchott-data-hub-/1291

Current confirmed certification signal:

- Client: **Societe pour le Developpement des Infrastructures Numeriques (SDIN)**.
- Project: **Nouakchott Data Hub**.
- Location: **Nouakchott, Mauritania**.
- Awards: **Tier III Certification of Design Documents** and **Tier III Certification of Constructed Facility**.

Uptime query templates:

```text
site:uptimeinstitute.com/uptime-institute-awards Mauritania
site:uptimeinstitute.com "Nouakchott Data Hub"
site:uptimeinstitute.com "Mauritania" "Tier III"
site:uptimeinstitute.com "SDIN" "Nouakchott"
```

### 1.7 SDIN, IMT, Mauripost, Telecom Operators

Primary URLs:

- SDIN: https://sdin.mr/
- Mauripost: https://www.mauripost.mr/
- Mauritel / Moov Mauritel: https://www.mauritel.mr/
- Mattel: http://www.mattel.mr/
- Chinguitel: https://chinguitel.mr/

Interpretation:

- SDIN is A-grade for asset ownership and WARCIP asset context. Its site currently contains older wording saying Nouakchott Data Hub is in construction; reconcile with AMI / EIB / Uptime, which show it was inaugurated and certified in May 2025.
- IMT lacks a consistently discoverable public site in this pass. Use EIB / AMI / ARE / SDIN for IMT facts.
- Mauritel, Mattel, Chinguitel, Rimatel, SNIM, IKASIRA, BU-WAC, and SOMELEC are telecom/network seeds. Operator catalogues and service pages do not prove commercial datacenter sites. Search for named server rooms, core network centres, cloud platforms, and facility addresses.

Operator query templates:

```text
site:sdin.mr "Datacenter"
site:sdin.mr "Nouakchott Data Hub"
site:mauripost.mr "data center"
site:mauripost.mr "centre de donnees"
site:mauritel.mr "cloud"
site:mauritel.mr "hebergement"
site:mattel.mr "cloud"
site:chinguitel.mr "data center"
"International Mauritania Telecom" "Nouakchott Data Hub"
"IMT" "Mauritanie" "centre de donnees"
"SNIM" "data center" "Mauritanie"
"SNIM" "centre de donnees" "Zouerate"
```

### 1.8 ARMP and Public Procurement

Primary URL: https://armp.mr/

Use ARMP for public-procurement decisions when MTNIMA pages do not expose the notice / award. Search all central ministries and public enterprises as buyers, especially MTNIMA, Interior, Finance, Health, Higher Education, Defence, BCM, SNIM, SOMELEC, PANPA, TCN, airports, and port authorities.

Procurement query templates:

```text
site:armp.mr "data center"
site:armp.mr "datacenter"
site:armp.mr "centre de donnees"
site:armp.mr "cloud"
site:armp.mr "Cloud Gouvernemental"
site:armp.mr "hebergement"
site:armp.mr "salle serveur"
site:armp.mr "systeme d'information"
site:armp.mr "centre d'operations de cyber-securite"
site:armp.mr "CSIRT"
site:armp.mr "{buyer}" "{locality}"
```

Extract buyer, contract number, awardee, date, stage, object, region, site if named, and whether the contract is facility construction, equipment supply, hosting service, cloud migration, maintenance, or cybersecurity operations.

### 1.9 Official Cloud Region Absence Checks

Official URLs:

- AWS Regions and AZs: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- Azure geographies: https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies
- Google Cloud locations: https://cloud.google.com/about/locations
- Oracle Cloud regions: https://www.oracle.com/cloud/public-cloud-regions/

As of this methodology pass, none lists a Mauritania public cloud region. Record this only as absence evidence for hyperscaler regions. It does not disprove private cloud, government cloud, edge cache, CDN, partner hosting, or enterprise server rooms.

---

## 2. Confirmed Official Seeds and Current Interpretation

| Seed | Region | Source URLs | Grade | Enumeration treatment |
|---|---:|---|---|---|
| Nouakchott Data Hub / Centre d'hebergement de donnees numeriques de Nouakchott | West Nouakchott | https://ami.mr/fr/archives/270548 ; https://www.eib.org/en/press/all/2025-202-inauguration-du-centre-d-hebergement-de-donnees-numeriques-de-nouakchott ; https://uptimeinstitute.com/uptime-institute-awards/country/id/MR ; https://sdin.mr/ | A | Operational national datacenter. Use one facility record. `capacity_mw=null`; notes should include 1,372 m2, 100 racks expandable, Tier III design + constructed facility certifications, SDIN / IMT roles. |
| WARDIP Government Cloud | National; likely hosted from West Nouakchott unless a source names otherwise | https://mtnima.gov.mr/fr/marches-superieurs-aux-seuils-des-marches-publics-periode-daout-2024-a-aout-2025/ ; https://mtnima.gov.mr/wp-content/uploads/2026/07/AMI-45_Migration-Cloud.pdf | A | Platform / service procurement. Do not count as a second facility without a named physical site. |
| SDIN WARCIP assets: national backbone, Datacenter, IXP | National backbone; datacenter in West Nouakchott | https://sdin.mr/ | A | Asset owner / infrastructure context. Use to support SDIN developer/owner fields, not to infer extra regional DCs. |
| EllaLink second submarine cable / Nouadhibou landing station | Nouadhibou Peninsula | https://mtnima.gov.mr/fr/ellalink-et-le-mtnima-posent-une-nouvelle-branche-de-cable-sous-marin-a-nouadhibou/ ; https://international-partnerships.ec.europa.eu/policies/global-gateway/construction-data-center-nouakchott-and-submarine-cable-mauritania_en | A | Cable landing / neutral landing station; connectivity context only. Not a datacenter unless later official sources name compute / racks / colocation. |
| BU-WAC / WAC landing at Nouadhibou terminal station | Nouadhibou Peninsula | https://are.mr/pdfs/IxBUWAC2026-2027.pdf | A | Cable landing / telecom station context. Not a datacenter. |
| University of Nouakchott Al Aasriya Centre de Calcul | West Nouakchott | https://mtnima.gov.mr/wp-content/uploads/2024/05/Rapport-Phase-2-Etat-des-lieux-Clean-1.pdf ; https://www.inhea.org/ahen/mauritania/ | B | Institutional compute / HPC lead. Count only if project scope includes research compute/server-room enumeration; do not classify as commercial colocation. No public MW. |

---

## 3. Division Mapping and Coverage

Use manifest English division names in result records. Keep local aliases in notes and search terms.

| Manifest division | Local wilaya / alias | Arabic search name | Priority | Official strategy |
|---|---|---|---:|---|
| Eastern Basin | Hodh Ech Chargui / Hodh Charghi; Nema, Oualata, Bassikounou | الحوض الشرقي / النعمة | Medium | WARCIP south-east backbone and Mali-border routes. Search Nema and border interconnection terms; expect fiber / admin IT, not datacenters. |
| Western Basin | Hodh El Gharbi; Aioun, Tintane, Kobenni | الحوض الغربي / العيون | Medium | WARCIP south-east route and energy corridor. Search Aioun / Tintane plus fiber, cloud, server-room terms. |
| Assaba | Assaba; Kiffa, Guerou | لعصابة / كيفة | Medium | Regional administration and transmission corridor context. Search Kiffa plus MTNIMA / AMI / ARMP IT procurement terms. |
| Gorgol | Gorgol; Kaedi, M'Bout | كوركول / كيهيدي | Medium | Southern backbone, government services, health / education IT. Search Kaedi / Kaedi variants and ARMP. |
| Brakna | Brakna; Aleg, Boghe | لبراكنة / ألاك | Medium | Southern backbone and government-service nodes. Search Aleg / Boghe for fiber and server-room notices. |
| Trarza | Trarza; Rosso, R'Kiz, Boutilimit | اترارزة / روصو | Medium-high | Senegal-border connectivity / Rosso crossing. Search WARCIP, backbone, Rosso, border interconnection; no DC unless site named. |
| Adrar | Adrar; Atar, Chinguetti | آدرار / أطار | Low | Sparse official leads. Search tourism/admin IT, fiber, server-room terms; expect negative. |
| Nouadhibou Peninsula | Dakhlet Nouadhibou; Nouadhibou, Zone Franche, Port, Cansado | داخلت نواذيبو / نواذيبو | High | EllaLink landing, WAC/BU-WAC landing station, SNIM / port / zone-franche IT. Treat cable stations separately from DCs. |
| Tagant | Tagant; Tidjikja, Moudjeria | تكانت / تجكجة | Low | Run universal negative workflow; monitor regional admin digitization and fiber. |
| Guidimaka | Guidimaka; Selibaby, Ould Yenge | كيدي ماغه / سيلبابي | Medium | Southern / Mali-Senegal border connectivity and health/admin IT. Search Selibaby plus fiber, data, cloud. |
| Tiris Zemmour | Tiris Zemmour; Zouerate, F'Derick, Bir Moghrein | تيرس زمور / ازويرات | Medium | SNIM mining corridor and possible mine IT/server rooms. Search SNIM, Zouerate, fibre, centre de calcul; current public evidence often negative. |
| Inchiri | Inchiri; Akjoujt, Benichab, Tasiast | إينشيري / أكجوجت | Medium-low | Mining (Akjoujt / Tasiast / MCM / Kinross) and telecom power contexts. Treat mine server-room leads as C until official evidence. |
| West Nouakchott | Nouakchott-Ouest; Tevragh-Zeina, Ksar, Sebkha boundary checks | نواكشوط الغربية / تفرغ زينة | Highest | National Data Hub, SDIN, ministries, university compute, bank HQs, telecom HQs. Avoid duplicate "Nouakchott" records by locality. |
| North Nouakchott | Nouakchott-Nord; Dar Naim, Toujounine, Teyarett | نواكشوط الشمالية / توجنين | Medium | New energy and public-building projects; check Toujounine, ANAC, public agencies. No separate DC currently confirmed. |
| South Nouakchott | Nouakchott-Sud; Arafat, El Mina, Riyad | نواكشوط الجنوبية / عرفات | Medium | Dense urban / logistics / public services. Search localities plus data/cloud/server-room terms; no separate DC currently confirmed. |

---

## 4. Official Enumeration Workflow

Run this sequence per division:

1. **Anchor exact-facility search**: exact known facility / project names in AMI, MTNIMA, EIB, EEAS, Uptime, SDIN, and ARMP.
2. **Wilaya official news pass**: AMI + MTNIMA with manifest name, French wilaya name, Arabic wilaya name, and major localities.
3. **Regulator pass**: ARE for operator catalogues, landing points, licence changes, and interconnection points.
4. **Procurement pass**: MTNIMA, ARMP, and public-enterprise sites for cloud, hosting, servers, SOC/CSIRT, hyperconverged infrastructure, and building works.
5. **Donor pass**: EIB / EEAS / World Bank for WARCIP, WARDIP, cable, backbone, NREN, and digital-government components.
6. **Facility test**: only create a datacenter / compute record when a source names a physical facility, centre de calcul, server room, rack hall, data centre building, or equivalent. Keep cable landing stations, IXP, fiber nodes, and cloud platforms as context unless compute infrastructure is explicit.

Universal official query templates:

```text
"{division}" "data center" Mauritania
"{wilaya_fr}" "centre de donnees" Mauritanie
"{locality}" "datacenter" Mauritanie
"{locality}" "centre d'hebergement de donnees"
"{locality}" "cloud gouvernemental"
"{locality}" "salle serveur"
"{locality}" "salle informatique"
"{locality}" "centre de calcul"
"{locality}" "fibre optique" "Mauritanie"
"{locality}" "cable sous-marin"
site:ami.mr/fr "{wilaya_fr}" "numerique"
site:ami.mr/fr "{locality}" "donnees"
site:mtnima.gov.mr/fr "{wilaya_fr}" "cloud"
site:mtnima.gov.mr/fr "{locality}" "fibre"
site:are.mr "{operator}" "{locality}"
site:armp.mr "{locality}" "salle serveur"
"{wilaya_ar}" "مركز البيانات"
"{locality_ar}" "قاعة الخوادم"
```

Negative-search handling:

- Mark `no_projects=true` only after checking official news (AMI / MTNIMA), procurement (ARMP / MTNIMA), regulator (ARE), and exact locality searches.
- For Nouakchott, disambiguate **West**, **North**, and **South** by moughataa / commune. If a source says only "Nouakchott", assign only when another source gives locality; otherwise note `division_uncertain` rather than duplicating across all three.
- For Nouadhibou Peninsula, do not confuse cable landing stations or port telecom rooms with datacenters.
- For mining regions, do not infer a datacenter from mine automation, private LTE, SCADA, dispatch centres, or telecom licences without a named server-room / data-centre source.

---

## 5. Region-Specific Official Playbook

### Eastern Basin

Local alias: Hodh Ech Chargui / Hodh Charghi. Main localities: Nema, Oualata, Bassikounou, Adel Bagrou, Amourj.

Official focus:

- WARCIP south-eastern backbone routes and Mali-border connection points.
- Regional administration / health / education IT tenders.
- Humanitarian and border digital systems can produce server-room references, but are usually service deployments.

Queries:

```text
"Hodh Ech Chargui" "centre de donnees"
"Hodh Charghi" "fibre optique" "WARCIP"
"Nema" "salle serveur" Mauritanie
site:ami.mr/fr "Nema" "numerique"
site:mtnima.gov.mr/fr "Hodh Ech Chargui"
"النعمة" "مركز البيانات"
```

### Western Basin

Local alias: Hodh El Gharbi. Main localities: Aioun / Ayoun el-Atrous, Tintane, Kobenni, Tamchekett.

Official focus:

- WARCIP / WARDIP backbone dissemination, Mali-border routes.
- Energy corridor projects may support telecom reliability but are not DC evidence.

Queries:

```text
"Hodh El Gharbi" "centre de donnees"
"Aioun" "fibre optique" Mauritanie
"Tintane" "salle informatique"
site:ami.mr/fr "Aioun" "donnees"
site:mtnima.gov.mr/fr "Hodh El Gharbi"
"العيون" "خوادم" "موريتانيا"
```

### Assaba

Local alias: Assaba. Main localities: Kiffa, Guerou, Barkewol, Boumdeid.

Official focus:

- Kiffa regional administration and university / hospital IT.
- Transmission corridor and backbone context; do not treat power projects as DC capacity.

Queries:

```text
"Assaba" "centre de donnees"
"Kiffa" "data center" Mauritania
"Kiffa" "salle serveur"
site:armp.mr "Kiffa" "systeme d'information"
site:ami.mr/fr "Kiffa" "numerique"
"كيفة" "مركز البيانات"
```

### Gorgol

Local alias: Gorgol. Main localities: Kaedi / Kaedi, M'Bout, Maghama.

Official focus:

- Southern backbone and regional public-service digitization.
- Health and education systems can name server rooms.

Queries:

```text
"Gorgol" "centre de donnees"
"Kaedi" "salle serveur"
"Kaedi" "fibre optique" Mauritanie
site:ami.mr/fr "Gorgol" "numerique"
site:mtnima.gov.mr/fr "Kaedi"
"كيهيدي" "خوادم"
```

### Brakna

Local alias: Brakna. Main localities: Aleg, Boghe / Boghe, Bababe.

Official focus:

- Southern fiber route, regional administration, agriculture and river-valley systems.

Queries:

```text
"Brakna" "centre de donnees"
"Aleg" "salle serveur" Mauritanie
"Boghe" "fibre optique"
site:ami.mr/fr "Brakna" "donnees"
site:armp.mr "Aleg" "informatique"
"ألاك" "مركز البيانات"
```

### Trarza

Local alias: Trarza. Main localities: Rosso, R'Kiz, Boutilimit, Keur Macene.

Official focus:

- Rosso / Senegal border connectivity; WARCIP international connection point candidates.
- Agriculture, port / river logistics, and customs IT systems.

Queries:

```text
"Trarza" "centre de donnees"
"Rosso" "fibre optique" "WARCIP"
"Rosso" "salle serveur"
site:ami.mr/fr "Rosso" "numerique"
site:mtnima.gov.mr/fr "Trarza"
"روصو" "مركز البيانات"
```

### Adrar

Local alias: Adrar. Main localities: Atar, Chinguetti, Ouadane.

Official focus:

- Regional administration, tourism systems, military / airport IT references.
- Expect negative results unless a local institution names a server room.

Queries:

```text
"Adrar" "centre de donnees" Mauritanie
"Atar" "data center" Mauritania
"Atar" "salle serveur"
site:ami.mr/fr "Atar" "numerique"
site:mtnima.gov.mr/fr "Adrar"
"أطار" "خوادم"
```

### Nouadhibou Peninsula

Local alias: Dakhlet Nouadhibou. Main localities: Nouadhibou, Cansado, Zone Franche, Port Autonome de Nouadhibou.

Official focus:

- EllaLink 2026 landing and neutral cable landing station.
- BU-WAC / WAC landing point at the Nouadhibou terminal station.
- SNIM, port, fisheries, free-zone, and customs IT.

Queries:

```text
"Dakhlet Nouadhibou" "centre de donnees"
"Nouadhibou" "data center" Mauritania
"Nouadhibou" "station d'atterrissement"
"Nouadhibou" "salle serveur"
site:mtnima.gov.mr/fr "Nouadhibou" "cable sous-marin"
site:are.mr "Nouadhibou" "atterrissement"
site:snim.com "Nouadhibou" "data center"
"نواذيبو" "محطة إنزال" "الكابل البحري"
```

### Tagant

Local alias: Tagant. Main localities: Tidjikja, Moudjeria, Tichit.

Official focus:

- Low-density negative workflow, regional administration, education / health systems.

Queries:

```text
"Tagant" "centre de donnees"
"Tidjikja" "salle serveur"
"Tidjikja" "fibre optique"
site:ami.mr/fr "Tagant" "numerique"
site:mtnima.gov.mr/fr "Tidjikja"
"تجكجة" "مركز البيانات"
```

### Guidimaka

Local alias: Guidimaka. Main localities: Selibaby, Ould Yenge, Ghabou.

Official focus:

- Southern border connectivity and public-service digitization.
- Health / education / humanitarian IT may create institutional server-room leads.

Queries:

```text
"Guidimaka" "centre de donnees"
"Selibaby" "data center" Mauritania
"Selibaby" "salle serveur"
site:ami.mr/fr "Guidimaka" "donnees"
site:mtnima.gov.mr/fr "Selibaby"
"سيلبابي" "خوادم"
```

### Tiris Zemmour

Local alias: Tiris Zemmour. Main localities: Zouerate, F'Derick, Bir Moghrein.

Official focus:

- SNIM rail-mining corridor, mine telecom licences, Zouerate institutional IT.
- Current batch evidence found no public datacenter project; keep searching SNIM / procurement / ARE for upgrades.

Queries:

```text
"Tiris Zemmour" "centre de donnees"
"Zouerate" "data center" Mauritania
"Zouerate" "centre de calcul"
"SNIM" "Zouerate" "salle serveur"
site:snim.com "Zouerate" "informatique"
site:are.mr "SNIM" "catalogue"
"ازويرات" "مركز البيانات"
```

### Inchiri

Local alias: Inchiri. Main localities: Akjoujt, Benichab, Tasiast.

Official focus:

- Mining and industrial systems: MCM / First Quantum, Kinross Tasiast, water / energy sites.
- Treat mine IT rooms as C until official mine, EIA, or tender evidence names them.

Queries:

```text
"Inchiri" "centre de donnees"
"Akjoujt" "data center" Mauritania
"Tasiast" "salle serveur"
"Kinross" "Tasiast" "data center"
site:ami.mr/fr "Akjoujt" "numerique"
site:armp.mr "Inchiri" "informatique"
"أكجوجت" "خوادم"
```

### West Nouakchott

Local alias: Nouakchott-Ouest. Main localities: Tevragh-Zeina, Ksar, central government / embassies, university campus.

Official focus:

- Nouakchott Data Hub / SDIN / IMT.
- University of Nouakchott Centre de Calcul.
- Ministries, central bank, telecom HQs, and national SOC / CSIRT procurements.

Queries:

```text
"Nouakchott Data Hub"
"Centre d'hebergement de donnees numeriques de Nouakchott"
"Nouakchott-Ouest" "data center"
"Tevragh-Zeina" "centre de donnees"
"Ksar" "salle serveur" Nouakchott
site:ami.mr/fr "Data Center de Nouakchott"
site:mtnima.gov.mr/fr "Cloud Gouvernemental"
site:uptimeinstitute.com "Nouakchott Data Hub"
"نواكشوط الغربية" "مركز البيانات"
```

### North Nouakchott

Local alias: Nouakchott-Nord. Main localities: Dar Naim, Toujounine, Teyarett.

Official focus:

- New public buildings, telecom infrastructure, Toujounine energy projects as power context.
- No separate confirmed datacenter currently; avoid assigning generic "Nouakchott" records here without locality evidence.

Queries:

```text
"Nouakchott-Nord" "centre de donnees"
"Toujounine" "data center"
"Dar Naim" "salle serveur"
site:ami.mr/fr "Toujounine" "numerique"
site:mtnima.gov.mr/fr "Nouakchott-Nord"
"نواكشوط الشمالية" "خوادم"
```

### South Nouakchott

Local alias: Nouakchott-Sud. Main localities: Arafat, El Mina, Riyad.

Official focus:

- Dense public-service districts, logistics, banking branches, urban digital services.
- No separate confirmed datacenter currently; do not duplicate West Nouakchott Data Hub.

Queries:

```text
"Nouakchott-Sud" "centre de donnees"
"El Mina" "data center" Nouakchott
"Riyad" "salle serveur" Nouakchott
site:ami.mr/fr "Nouakchott-Sud" "numerique"
site:armp.mr "Arafat" "informatique"
"نواكشوط الجنوبية" "مركز البيانات"
```

---

## 6. Output Rules

For each final record:

- Use `division` exactly as one of the 15 manifest names.
- Prefer official French project names, with English aliases in `notes`.
- Use `status=operational` only when commissioned / inaugurated / certified / operator-live evidence exists. Use `planned`, `construction`, `procurement`, or `announced` for earlier stages.
- `capacity_mw` stays null unless a source gives kW / MW / MVA tied to that exact facility.
- Put rack count, floor area, certification, owner, operator, and non-MW power details in `notes`.
- Keep cable landing stations, IXP, fiber backbone, cloud service procurement, SOC/CSIRT, and NREN as context unless the source names a physical compute / server facility.
- Use A-grade only for facts directly supported by A-grade sources; otherwise downgrade the record or split the claim in notes.
