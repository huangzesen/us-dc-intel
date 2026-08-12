# MY Explorer Official - Malaysia Datacenter Enumeration Methodology

Date: 2026-08-12. Country: **MY Malaysia**. Scope: official / regulatory / cloud pipeline for enumerating Malaysian datacenter projects across **13 states and 3 federal territories**. Focus: planning and building approvals, energy and water trails, MCMC cloud-service licensing, MIDA / MDEC investment facilitation, official cloud-region pages, official operator facility pages, and trade-press query patterns.

Reliability grades:
- **A** = primary / legally accountable source: PLANMalaysia / KPKT guideline or circular, OSC / local authority planning record, state guideline, DOE / EIA record, utility agreement or regulator record, MCMC licence/register, MIDA / MDEC official release, official cloud-region page, official operator facility page, Bursa / annual-report disclosure.
- **B** = strong secondary source: Bernama, The Edge Malaysia, The Star, Data Center Dynamics, AP, FT, contractor press release, credible law-firm / engineering note that names the statutory process or project.
- **C** = weak lead: directories, broker pages, social posts, job ads, unverified maps, community objections without a matching application number.

---

## 0. Malaysia-Specific Structure Facts

- Malaysia has **no complete public national datacenter registry**. Build the census by joining planning approvals, utility commitments, MCMC / cloud licensing, investment facilitation, and operator disclosures.
- Planning approval is local-authority led. In Peninsular Malaysia, development applications are normally submitted through **OSC 3.0 Plus Online** under KPKT; Kuala Lumpur has a separate DBKL OSC portal; Penang has historically used local systems such as ILCS for council submissions; Johor also uses **Johor Fast Lane** and a state datacenter coordination process.
- PLANMalaysia's **Garis Panduan Perancangan Pusat Data / Planning Guideline for Data Centre** was approved by Cabinet on **2024-10-08** and applies as a uniform reference for datacenter development **above 1 MVA**, including new sites and existing buildings. Official pages: https://www.planmalaysia.gov.my/main/latest-news-details?id=garis-panduan-perancangan-gpp-pusat-data and circular page https://www.planmalaysia.gov.my/main/latest-news-details?id=pekeliling-ketua-pengarah-perancangan-bandar-dan-desa-planmalaysia-bilangan-4-tahun-2024.
- Johor has its own official state guideline: **Johor State Data Centre Development Planning Guidelines** from PLANMalaysia Johor / JPBD Johor. PDF: https://jpbd.johor.gov.my/wp-content/uploads/2025/02/81-GP-DATA-CENTRE-en.pdf. It explicitly routes datacenter applications through **PBT OSC / OSC 3.0 Plus or Johor Fast Lane**, with referral to the Johor State Data Centre Development Coordinating Committee for complex issues.
- Energy evidence is unusually strong in Peninsular Malaysia because TNB created a **Green Lane Pathway** for datacenters requiring high-voltage supply at **132/275 kV**, with a datacenter one-stop centre and a target connection period reduced from 36-48 months to about 12 months. TNB release: https://www.tnb.com.my/announcements/tnb-establishes-exclusive-green-lane-pathway.
- East Malaysia is different: **Sarawak Energy** and **Sabah Electricity** trails matter more than TNB for Sarawak / Sabah. Do not assume Peninsular TNB evidence applies to Kuching, Miri, Kota Kinabalu, or Labuan.

---

## 1. Core Search Terms

Use English, Malay, and mixed spellings. Malaysian sources often use British spelling.

```text
"data centre" "{operator}" "{state_or_city}"
"data center" "{operator}" "{state_or_city}"
"pusat data" "{operator}" "{state_or_city}"
"pusat data" "kebenaran merancang" "{PBT_or_state}"
"data centre" "OSC" "{PBT_or_state}"
"data centre" "pelan bangunan" "{PBT_or_state}"
"data centre" "pelan kerja tanah" "{PBT_or_state}"
"data centre" "CCC" "Malaysia"
"data centre" "Certificate of Completion and Compliance"
"data centre" "132kV" OR "275kV" Malaysia
"data centre" "MVA" "TNB"
"data centre" "water" "Johor" OR "Air Selangor" OR "SPAN"
"cloud region" Malaysia "{AWS|Microsoft|Google|Oracle}"
"ASP(C)" "cloud services" "MCMC"
"Malaysia Digital Status" "data centre"
```

Malay terms to rotate:

```text
"pusat data" "kebenaran merancang"
"pusat data" "pelan bangunan"
"pusat data" "pelan kerja tanah"
"pusat data" "pelan jalan dan parit"
"pusat data" "kelulusan perancangan"
"pusat data" "Jawatankuasa OSC"
"pusat data" "Mesyuarat OSC"
"pusat data" "bekalan elektrik"
"pusat data" "bekalan air"
"pusat data" "pencawang masuk utama"
"pusat data" "Laporan EIA"
```

---

## 2. Grade A Planning / Building Sources

### 2.1 KPKT / OSC 3.0 Plus / Local Authorities

Primary sources:
- OSC 3.0 Plus Online: https://osc3plus.kpkt.gov.my/
- MyGovernment OSC 3.0 Plus description: https://www.malaysia.gov.my/my-initiative/sistem-penyampaian-perkhidmatan-awam-dan-kerajaan-tempatan/local-e-government/sistem-osc-30-plus-online
- Older KPKT OSC landing page redirects users to OSC 3.0 Plus: https://portalosc.kpkt.gov.my/
- Example PBT page exposed through OSC 3.0 Plus, Kajang: https://osc3plus.kpkt.gov.my/pbt/MPKj
- DBKL OSC portal: https://osc.dbkl.gov.my/
- DBKL Department of City Planning: https://www.dbkl.gov.my/en/departments/jabatan-perancangan-bandaraya

Method:
1. Start from a project / operator / site lead, then identify the **PBT**: Sepang Municipal Council for Cyberjaya, Shah Alam City Council for Elmina / Shah Alam, Iskandar Puteri City Council for parts of Nusajaya / Iskandar Puteri, Kulai Municipal Council for Sedenak / Kulai, Johor Bahru City Council for Plentong / Johor Bahru, DBKL for Kuala Lumpur.
2. Search the PBT's OSC page, meeting agendas / minutes, announcement pages, and status search. OSC pages often expose meeting titles and application categories even when detailed plans require login.
3. Extract application number, applicant, owner, lot / mukim / district, proposal text, plan types, meeting date, decision, and attached public-notice material.
4. Treat **Kebenaran Merancang (planning permission)**, **Pelan Bangunan**, **Pelan Kerja Tanah**, **Pelan Jalan dan Parit**, **CCC / Certificate of Completion and Compliance**, and local council planning-committee decisions as the main construction-status trail.

Query templates:

```text
site:osc3plus.kpkt.gov.my/pbt "{operator}" "data centre"
site:osc3plus.kpkt.gov.my/pbt "pusat data" "{PBT}"
site:{pbt_domain}.gov.my "pusat data" "OSC"
site:{pbt_domain}.gov.my "data centre" "kebenaran merancang"
site:{pbt_domain}.gov.my "Mesyuarat OSC" "pusat data"
site:osc.dbkl.gov.my "data centre"
site:dbkl.gov.my "data centre" "planning permission"
```

Grade: **A** for local authority records and application status. Caveat: many detailed records are login-gated or searchable only by application number; use public meeting PDFs and local-news references to recover IDs.

### 2.2 PLANMalaysia / Datacenter Planning Guideline

Primary sources:
- GPP Pusat Data announcement: https://www.planmalaysia.gov.my/main/latest-news-details?id=garis-panduan-perancangan-gpp-pusat-data
- PLANMalaysia circular on adoption: https://www.planmalaysia.gov.my/main/latest-news-details?id=pekeliling-ketua-pengarah-perancangan-bandar-dan-desa-planmalaysia-bilangan-4-tahun-2024
- PLANMalaysia document-list page with BM / ENG GPP files: https://www.planmalaysia.gov.my/main/document-list?frontendpage=document-list&page=5&params=&per-page=12&q=%2Fmain%2Fdocument-list&type=garis-panduan-perancangan

Use:
1. Use the GPP to screen whether a candidate should be in industrial / commercial zoning, whether buffer requirements apply, and whether a project over 1 MVA should have gone through the datacenter-specific planning workflow.
2. Search state PLANMalaysia pages for local adoption circulars and local-plan publicity items, especially when a state is revising an industrial zone to host datacenters.
3. Do not count a project from the guideline alone; it is a permitting framework.

Grade: **A** for legal/planning requirements and adoption scope; **B/C** only for facility inference.

### 2.3 Johor Fast Lane / Johor Datacenter Guideline

Primary sources:
- Johor guideline PDF: https://jpbd.johor.gov.my/wp-content/uploads/2025/02/81-GP-DATA-CENTRE-en.pdf
- PLANMalaysia Johor guideline page: https://jpbd.johor.gov.my/?page_id=668
- MIDA news on Johor guideline drafting: https://www.mida.gov.my/mida-news/johor-to-streamline-coordination-of-data-centres-for-local-councils-and-agencies/

Method:
1. For every Johor lead, search **Kulai**, **Sedenak**, **Iskandar Puteri**, **Johor Bahru**, **Plentong**, **Gelang Patah**, **Nusajaya**, **Muar**, **Pasir Gudang**, **Senai**, and **Tanjung Langsat** with PBT names.
2. Use the guideline's process flow to require a PBT approval trail even when an operator announcement is strong.
3. Search for JPPPDNJ references where a project is large, near residential areas, requires unusual power / water, or has inter-agency issues.

Johor query templates:

```text
site:jpbd.johor.gov.my "data centre"
site:jpbd.johor.gov.my "pusat data"
"Johor Fast Lane" "data centre"
"JPPPDNJ" "pusat data"
"Sedenak Tech Park" "OSC" "data centre"
"Kulai" "pusat data" "kebenaran merancang"
"Iskandar Puteri" "data centre" "pelan bangunan"
"Plentong" "data centre" "OSC"
site:mbip.gov.my "data centre"
site:mpkulai.gov.my "pusat data"
site:mbjb.gov.my "data centre"
```

Grade: **A** for Johor state/PBT records; **B** for MIDA/Bernama descriptions of state process; **A** for operator pages only on named facility facts.

---

## 3. Environmental, Water, and Sustainability Trail

Primary sources:
- Department of Environment / Jabatan Alam Sekitar: https://www.doe.gov.my/en/utama-english/
- DOE online services / EIA links: https://www.doe.gov.my/perkhidmatan-dalam-talian/
- DOE Environmental Data Center page is not a datacenter facility source; it is only a DOE internal/environmental-data page: https://www.doe.gov.my/en/environmental-data-center/
- SPAN / water regulator: https://www.span.gov.my/
- Air Selangor: https://www.airselangor.com/
- Ranhill SAJ / Johor water utility: https://www.ranhillsaj.com.my/
- Sarawak Energy: https://www.sarawakenergy.com/
- Sabah Electricity: https://www.sabah-electricity.com.my/

Use:
1. Search DOE **EIA Report Status Review**, **Executive Summary List of EIA Reports**, and local DOE pages by operator, landowner, industrial estate, and power / generator terms. Datacenters are not always a clean prescribed-activity category; EIA may be triggered by land clearing, industrial development, power generation, backup-generator fuel storage, water abstraction, or other associated works.
2. For large campuses, search water-utility and state-water-agency pages because recent Malaysian scrutiny is focused on water consumption, recycled water, and potable-water constraints.
3. Capture water source, recycled-water agreements, cooling technology, discharge / wastewater conditions, backup generator fuel storage, and noise complaints if tied to a planning record.

Query templates:

```text
site:doe.gov.my "data centre" "EIA"
site:doe.gov.my "pusat data" "EIA"
site:doe.gov.my "data centre" "Executive Summary"
site:span.gov.my "data centre"
site:airselangor.com "data centre"
site:ranhillsaj.com.my "data centre"
"data centre" "recycled water" "Johor"
"pusat data" "bekalan air" "{state_or_city}"
"data centre" "backup generator" "EIA" Malaysia
```

Grade: **A** for DOE / SPAN / utility documents; **B** for law-firm or trade-press process analysis; **C** for unsupported environmental claims.

---

## 4. Energy and Grid Enumeration

### 4.1 Peninsular Malaysia - TNB / Suruhanjaya Tenaga

Primary sources:
- TNB Green Lane Pathway release: https://www.tnb.com.my/announcements/tnb-establishes-exclusive-green-lane-pathway
- TNB Green Lane PDF: https://www.tnb.com.my/assets/press_releases/2023080944_ENG.pdf
- TNB annual reports / investor pages: https://www.tnb.com.my/investors
- Suruhanjaya Tenaga / Energy Commission: https://www.st.gov.my/
- ST Annual Regulatory Review page: https://www.st.gov.my/partnership/suruhanjaya-tenaga-annual-regulatory-review
- Sustainable Energy Development Authority: https://www.seda.gov.my/

High-value evidence:
- Electricity Supply Agreement / ESA naming an operator or campus.
- TNB Green Lane Pathway participation, especially high-voltage 132/275 kV supply.
- MVA / MW capacity, substation names, PMU / pencawang masuk utama, feeder route works, grid-upgrade tender, energization date.
- Green Electricity Tariff (GET), CRESS / third-party access, solar / BESS / district cooling evidence tied to the facility.

Query workflow:

```text
site:tnb.com.my "{operator}" "data centre"
site:tnb.com.my "{operator}" "MVA"
site:tnb.com.my "{operator}" "Electricity Supply Agreement"
site:tnb.com.my "Green Lane Pathway" "data centre" "{operator}"
site:tnb.com.my "pencawang" "pusat data"
site:st.gov.my "data centre" "electricity demand"
site:seda.gov.my "data centre" "solar"
"{industrial_park}" "TNB" "data centre"
"{operator}" "132kV" "Malaysia"
"{operator}" "275kV" "Malaysia"
```

Grade: **A** when TNB/ST names the customer, load, agreement, grid project, or regulatory fact. **B** for operator-stated power arrangements if TNB is not cited.

### 4.2 Sarawak / Sabah / Labuan

Primary sources:
- Sarawak Energy: https://www.sarawakenergy.com/
- Sabah Electricity: https://www.sabah-electricity.com.my/
- Energy Commission for Labuan / Peninsular regulatory context: https://www.st.gov.my/
- MIDA / state investment agencies for project facilitation.

Query templates:

```text
site:sarawakenergy.com "data centre"
site:sarawakenergy.com "pusat data"
"Sarawak" "data centre" "MVA"
"Kuching" "data centre" "Sarawak Energy"
"Miri" "data centre" "Sarawak Energy"
site:sabah-electricity.com.my "data centre"
"Kota Kinabalu" "data centre" "electricity"
"Labuan" "data centre" "Suruhanjaya Tenaga"
```

Grade: **A** for utility/regulator statements; **B/C** for speculative cheap-hydro / AI hub articles unless joined to an operator, land, or permit.

---

## 5. MCMC / Cloud-Service Licensing Trail

Primary sources:
- MCMC: https://www.mcmc.gov.my/
- Ministry of Communications official MCMC cloud-regulation news: https://www.komunikasi.gov.my/en/public/news/20492-light-touch-regulation-on-cloud-services-to-enhance-data-protection-mcmc-2
- MCMC ReCPro for cabling/provider discovery: https://recpro.mcmc.gov.my/

Use:
1. Cloud service providers with Malaysian local presence, or providing cloud services through a Malaysian local datacenter, fall under MCMC's light-touch **Applications Service Provider Class Licence / ASP(C)** cloud-service licensing framework.
2. Use MCMC licensing as a **legal-entity and regulated-service seed**, not as physical-facility proof. It is useful for cloud providers, hosting companies, local CSPs, and datacenter operators offering cloud services.
3. Search ReCPro and MCMC pages for cabling providers, network facility/service providers, fibre buildouts, and telecom infrastructure associated with new campuses.

Query templates:

```text
site:mcmc.gov.my "cloud services" "ASP(C)"
site:mcmc.gov.my "cloud service provider" "class licence"
site:komunikasi.gov.my "cloud services" "MCMC" "ASP"
site:recpro.mcmc.gov.my "{operator}"
"Applications Service Provider Class" "cloud" "Malaysia" "{operator}"
"ASP(C)" "{operator}" Malaysia
"Network Facilities Provider" "{operator}" "data centre" Malaysia
```

Grade: **A** for licence / regulatory status; **B/C** for facility inference unless joined to planning, utility, or official facility page.

---

## 6. MIDA / MDEC / Digital Investment Office

Primary sources:
- MIDA: https://www.mida.gov.my/
- MDEC: https://mdec.my/
- MDEC Digital Investment Office page: https://www.mdec.my/programmes/digital-investment-office-dio
- DIO datacenter/cloud page: https://mydigitalinvestment.gov.my/data-centre-cloud
- MIDA data-centre investment examples: https://www.mida.gov.my/media-release/mida-powers-up-malaysias-digital-future-at-data-centre-nexus/ and https://www.mida.gov.my/mida-news/malaysia-approved-rm114-7-bln-investments-in-data-centres-cloud-services-from-2021-to-2023/

Use:
1. MIDA/MDEC/DIO are strong seeds for approved investment, Malaysia Digital Status, project facilitation, investment value, and sometimes state / site.
2. MIDA has reported large approved investment totals for datacenter and cloud projects, but many totals are aggregate. Do not count aggregate statistics as individual facilities.
3. Search MIDA by operator and state because MIDA frequently mirrors / republishes operator project announcements with government quotes.

Query templates:

```text
site:mida.gov.my "data centre" "{operator}"
site:mida.gov.my "data centre" "Johor"
site:mida.gov.my "data centre" "Selangor"
site:mida.gov.my "cloud" "Malaysia" "{operator}"
site:mdec.my "Malaysia Digital Status" "data centre"
site:mydigitalinvestment.gov.my "data centre"
"Digital Investment Office" "data centre" Malaysia
```

Grade: **A** for MIDA/MDEC official investment approval / status facts; **B** for project status unless construction, utility, or facility details are primary.

---

## 7. Official Cloud Region Seeds

Cloud pages are **A** for region existence, city/state label, region code, and availability-zone count when disclosed. They do not identify every physical building.

| Provider | Official source | Malaysia signal | Enumeration use |
|---|---|---|---|
| AWS | AWS Malaysia page https://aws.amazon.com/local/malaysia/ and launch blog https://aws.amazon.com/blogs/aws/now-open-aws-asia-pacific-malaysia-region/ plus AWS region table https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | **Asia Pacific (Malaysia)**, `ap-southeast-5`, opened 2024-08-21 with **3 Availability Zones** | Search Amazon / AWS legal entities, Greater Kuala Lumpur, Selangor, TNB Green Lane, MIDA, OSC. |
| Microsoft Azure | Malaysia West GA: https://news.microsoft.com/source/asia/features/microsoft-announces-its-first-cloud-region-in-malaysia-empowering-more-malaysian-organizations-to-accelerate-ai-innovation/ and Azure geography page https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies | **Malaysia West** in Greater Kuala Lumpur, 3 AZs; Microsoft has also announced intent for **Southeast Asia 3** in Johor Bahru | Search Microsoft / Azure, Malaysia West, Greater KL, Johor Bahru, TNB, local PBT records. |
| Google | Google press release https://www.googlecloudpresscorner.com/2024-05-30-Advancing-Malaysia-Together-Google-Announces-US-2-Billion-Investment-in-Malaysia%2C-Including-First-Google-Data-Center-and-Google-Cloud-Region and data-center locations https://datacenters.google/locations | First Google datacenter and Google Cloud region in Malaysia; Google location page lists **Selangor, Malaysia (in development)** | Search Google, Pearl Computing Malaysia, Elmina Business Park, Sime Darby Property, Shah Alam / Selangor OSC, TNB, contractors. |
| Oracle OCI | Oracle Malaysia investment announcement https://www.oracle.com/news/announcement/oracle-to-invest-in-ai-and-cloud-computing-in-malaysia-2024-10-02/ and OCI release note https://docs.oracle.com/iaas/releasenotes/oci/new-region-malaya-2.htm | Oracle announced a Malaysia cloud region; OCI release note lists **Malaysia West 2 (Kulai)**, `ap-kulai-2`, release date 2026-02-02 | Search Oracle, Kulai, Johor, Sedenak / Iskandar, TNB, PBT records. |

Cloud query templates:

```text
"ap-southeast-5" Malaysia "Availability Zones"
"Malaysia West" "Greater Kuala Lumpur" "availability zones"
"Southeast Asia 3" "Johor Bahru" Microsoft
"Google data center" "Elmina Business Park" "Selangor"
"Pearl Computing Malaysia" "data centre"
"ap-kulai-2" "Kulai" Oracle
```

---

## 8. Official Operator / Colo Seeds

Use these as seed lists, then verify with OSC / TNB / state evidence.

| Operator | Official source | Seed facts / query hooks |
|---|---|---|
| AirTrunk | Malaysia location https://airtrunk.com/location/malaysia/, JHB1 https://airtrunk.com/location/jhb1-johor/, JHB2 https://airtrunk.com/location/jhb2-johor/, JHB3/JHB4 announcement https://airtrunk.com/airtrunk-doubles-down-in-malaysia-with-two-new-hyperscale-campuses-in-johor-bahru/ | Johor Bahru campuses; JHB1 150+ MW, JHB2 270+ MW, JHB3/JHB4 add 280 MW. Search `AirTrunk JHB`, Johor Bahru, recycled water, 132kV, TNB, OSC. |
| YTL Data Centers | Malaysia page https://ytldatacenters.com/locations/malaysia/ and Johor park release https://ytldatacenters.com/pr/ytl-green-data-center-park-launches-in-johor-the-first-integrated-data-center-park-powered-by-solar-energy-in-malaysia/ | YTL Green Data Center Park in Kulai / Iskandar region, 275 acres, 500 MW total park concept, individual Johor Data Center pages. Search YTL, Kulai, Sedenak, GDS, NVIDIA, Oracle, TNB. |
| Princeton Digital Group | Malaysia page https://princetondg.com/locations/malaysia/ and JH1 delivery https://princetondg.com/newsroom/princeton-digital-group-delivers-phase-one-of-its-150mw-ai-ready-jh1-campus-in-sedenak-tech-park-johor/ | JH1 in Sedenak Tech Park / Kulai and JH2 nearby; official page discloses 200 MW and 300 MW site concepts; PDG release names TNB ESA for JH1. |
| Bridge Data Centres | Malaysia page https://www.bridgedatacentres.com/locations/malaysia/ and MIDA MY06 release https://www.mida.gov.my/media-release/bridge-data-centres-announces-construction-of-its-fourth-hyperscale-data-centre-campus-in-johor-malaysia/ | MY06 in Sedenak / Johor, Cyberjaya/MRANTI expansion leads. Search BDC, MY03, MY06, MRANTI, Sedenak, Plentong. |
| Vantage Data Centers | Johor campus https://vantage-dc.com/data-center-locations/apac/johor-malaysia and Cyberjaya II https://vantage-dc.com/data-center-locations/apac/cyberjaya-ii-malaysia/ | Johor JHB1 300MW+ critical IT load; KUL2 Cyberjaya with TNB and 500MVA on-campus substation; also Cyberjaya I. |
| NTT Global Data Centers | Cyberjaya overview https://services.global.ntt/en-us/services-and-products/global-data-centers/global-locations/asia-pacific/cyberjaya-data-centers and Cyberjaya 5 https://services.global.ntt/en-us/services-and-products/global-data-centers/global-locations/asia-pacific/cyberjaya-5-data-center | Cyberjaya facilities; Cyberjaya 5 lists 12 MW critical IT load. Search NTT MSC, Cyberjaya 1-6, MPSepang, TNB. |
| Keppel Data Centres / Basis Bay | Malaysia page https://www.keppeldatacentres.com/locations/asia-pacific/malaysia/, Basis Bay https://www.keppeldatacentres.com/locations/asia-pacific/malaysia/basis-bay-data-centre/, Johor 1 https://www.keppeldatacentres.com/locations/asia-pacific/malaysia/keppel-dc-johor-1/ | Basis Bay in Cyberjaya; Keppel DC Johor 1 built-to-suit in Johor industrial park. |
| AIMS | DigitalBridge portfolio https://www.digitalbridge.com/portfolio/aims and AIMS official pages when available | Menara AIMS Kuala Lumpur carrier hotel; Cyberjaya expansion / Block 3. Search AIMS, Menara Aik Hua, Cyberjaya, MyIX. |
| TM / TM Global / Nxera | TM / TM Global official channels and Singtel Nxera releases; cross-check TNB ESA | Klang Valley Data Centre / Cyberjaya and Iskandar Puteri Data Centre / Johor. Search `TM Nxera`, `IPDC`, `KVDC`, `Iskandar Puteri`, `280MW TNB`. |
| EdgeConneX, STT GDC, Equinix, NEXTDC, MyTelehaus, DayOne, GDS | Use official location / newsroom pages plus MIDA / state announcements | Treat as project leads unless an official facility page gives location and status. Search exact company + Malaysia + state + TNB + OSC. |

---

## 9. Division-by-Division Enumeration Strategy

### Tier 1 - Selangor

Priority clusters: **Cyberjaya / Sepang**, **Elmina Business Park / Shah Alam**, **Petaling Jaya / Kota Damansara**, **Kajang / Bangi / Semenyih**, **Subang / Klang Valley industrial parks**, **MRANTI Park / Bukit Jalil boundary checks**.

Workflow:
1. Determine PBT: MPSepang for Cyberjaya, MBSA for Shah Alam / Elmina, MBPJ for Petaling Jaya / Kota Damansara, MPKj for Kajang/Bangi, MBSJ for Subang / Puchong, MPKlang for Klang.
2. Search OSC 3.0 Plus PBT pages and PBT meeting documents by `pusat data`, operator, lot, business park, and contractor.
3. Cross-check TNB Green Lane / substation references and Air Selangor / SPAN for water.
4. Use official operator pages for NTT, Vantage, Bridge, Keppel/Basis Bay, AIMS, Google / Pearl Computing, and contractors such as Gamuda / IJM where they name the site.

Queries:

```text
"Cyberjaya" "data centre" "OSC"
site:mpsepang.gov.my "pusat data"
site:osc3plus.kpkt.gov.my/pbt "Cyberjaya" "pusat data"
"Elmina Business Park" "data centre" "MBSA"
"Pearl Computing Malaysia" "Elmina"
"Kota Damansara" "pusat data" "MBPJ"
"MRANTI Park" "data centre" "Bridge"
"Air Selangor" "data centre" "Selangor"
```

### Tier 1 - Johor

Priority clusters: **Sedenak Tech Park / Kulai**, **Iskandar Puteri / Nusajaya**, **Johor Bahru**, **Plentong**, **Gelang Patah**, **Senai**, **Pasir Gudang**, **Tanjung Langsat**, **Muar**.

Workflow:
1. Start with PLANMalaysia Johor guideline and PBT responsibility. Use Johor Fast Lane terms and JPPPDNJ terms for state-level coordination.
2. Search operator campus names: AirTrunk JHB1-4, YTL Johor Data Center 1/2/3/6, PDG JH1/JH2, Bridge MY06 / Plentong, Vantage JHB1, Keppel DC Johor 1, Microsoft Southeast Asia 3, Oracle `ap-kulai-2`, TM Nxera IPDC.
3. Verify with TNB ESA / MVA, Johor water evidence, and PBT OSC records.

Queries:

```text
"Sedenak Tech Park" "data centre" "Kulai"
"Kulai" "pusat data" "OSC"
"Jalan Digital" "Sedenak" "data centre"
"Iskandar Puteri" "data centre" "OSC"
"Gelang Patah" "data centre" "bekalan air"
"Plentong" "Bridge Data Centres"
"Johor Fast Lane" "pusat data"
"JPPPDNJ" "data centre"
```

### Tier 1 - Kuala Lumpur Federal Territory

Priority clusters: **Menara AIMS / Jalan Aik Hua**, **Bukit Jalil / MRANTI border**, **CBD carrier hotels**, enterprise retrofit sites.

Workflow:
1. Search DBKL OSC public portal and DBKL City Planning for planning-permission and building-plan records.
2. Use MCMC / MyIX / AIMS / telecom licences to identify carrier hotels and network-heavy sites.
3. Because KL sites are often retrofits, search CCC, renovation, change-of-use, generator, and noise complaints.

Queries:

```text
site:osc.dbkl.gov.my "data centre"
site:dbkl.gov.my "pusat data"
"Menara AIMS" "DBKL" OR "planning"
"Jalan Aik Hua" "data centre"
"Kuala Lumpur" "data centre" "CCC"
"Bukit Jalil" "data centre" "MRANTI"
```

### Tier 1 - Penang

Priority clusters: **Bayan Lepas**, **Batu Kawan**, **Perai / Seberang Perai**, **George Town enterprise sites**, semiconductor / cloud-adjacent industrial estates.

Workflow:
1. Search PLANMalaysia Pulau Pinang and council systems. Penang has used local digital planning systems such as ILCS, so do not rely only on OSC 3.0 Plus indexing.
2. Search MBPP / MBSP council pages for planning permission, building plan, and industrial-estate records.
3. Cross-check TNB Penang high-load evidence and InvestPenang announcements.

Queries:

```text
site:jpbd.penang.gov.my "GPP Pusat Data"
site:mbpp.gov.my "data centre"
site:mbsp.gov.my "pusat data"
"Bayan Lepas" "data centre" "planning"
"Batu Kawan" "data centre" "TNB"
"Penang" "data centre" "ILCS"
site:investpenang.gov.my "data centre"
```

### Tier 2 - Sarawak

Priority clusters: **Kuching**, **Samarahan**, **Miri**, **Bintulu**, energy-intensive industrial corridors and hydro-powered AI / cloud proposals.

Workflow:
1. Search Sarawak Energy first for power availability and customer agreements, then state investment pages and local councils.
2. Use Sarawak planning and land-development pages rather than Peninsular OSC assumptions.
3. Treat cheap hydropower / green AI hub articles as leads until an operator, power agreement, or local approval appears.

Queries:

```text
site:sarawakenergy.com "data centre"
"Sarawak" "data centre" "Kuching"
"Kuching" "pusat data" "Majlis"
"Samarahan" "data centre"
"Bintulu" "data centre" "power"
"Miri" "data centre" "Sarawak Energy"
```

### Tier 2 - Putrajaya and Labuan Federal Territories

Use mainly for government / disaster recovery / financial or offshore connectivity sites. Search federal procurement, MCMC, DOE, and local authority portals.

```text
"Putrajaya" "data centre" "kerajaan"
"Putrajaya" "pusat data" "tender"
"Labuan" "data centre" "MCMC"
"Labuan" "data centre" "electricity"
```

### Tier 2 - Negeri Sembilan, Melaka, Perak, Kedah

These are spillover states for land / power-constrained Klang Valley and Penang growth.

Workflow:
1. Search state investment agencies and industrial parks before broad web search.
2. Use OSC 3.0 Plus PBT pages for Seremban / Nilai, Melaka / Ayer Keroh, Ipoh / Kinta, Kulim / Kedah, and Sungai Petani.
3. Cross-check TNB high-voltage and state water-utility capacity.

Queries:

```text
"Nilai" "data centre" "OSC"
"Seremban" "pusat data" "kebenaran merancang"
"Ayer Keroh" "data centre" "Melaka"
"Ipoh" "data centre" "TNB"
"Kulim" "data centre" "Kedah"
"Sungai Petani" "pusat data"
```

### Tier 3 - Sabah, Pahang, Terengganu, Kelantan, Perlis

Lower probability for hyperscale but relevant for government, telecom, edge, disaster recovery, and energy-led proposals.

Queries:

```text
"Kota Kinabalu" "data centre" "Sabah Electricity"
"Sabah" "pusat data" "MCMC"
"Pahang" "data centre" "industrial park"
"Terengganu" "pusat data" "kerajaan"
"Kelantan" "data centre" "tender"
"Perlis" "pusat data"
```

---

## 10. Trade Press / Secondary Pipeline

Use trade press to discover leads, then backfill primary evidence.

High-value sources:
- Data Center Dynamics: https://www.datacenterdynamics.com/
- The Edge Malaysia: https://theedgemalaysia.com/
- The Star: https://www.thestar.com.my/
- Bernama / BernamaBiz: https://www.bernama.com/ and https://bernamabiz.com/
- AP / FT for hyperscaler and resource-conflict context.
- Contractor / developer releases: Gamuda, IJM, Sime Darby Property, Johor Corporation / JLand, Mah Sing, Paragon Globe, Ranhill SAJ.

Secondary query patterns:

```text
site:datacenterdynamics.com "Malaysia" "data center" "Johor"
site:theedgemalaysia.com "data centre" "Selangor"
site:thestar.com.my "data centre" "Johor" "TNB"
site:bernama.com "data centre" "Malaysia"
site:gamuda.com "data centre" "Elmina"
site:ijm.com "hyperscale data centre" "Elmina"
site:simedarbyproperty.com "data centre" "Elmina"
site:jcorp.com.my "Sedenak Tech Park" "data centre"
site:mahsing.com.my "data centre"
site:paragonglobe.com.my "data centre"
```

Grade: **B** for credible reporting and listed-company / contractor releases; upgrade to **A** only where the source is the operator, regulator, utility, PBT, or statutory filing.

---

## 11. Practical Enumeration Workflow

1. **Seed operators and cloud regions** from official cloud/operator pages: AWS, Microsoft, Google, Oracle, AirTrunk, YTL, PDG, Bridge, Vantage, NTT, Keppel/Basis Bay, AIMS, TM/Nxera, Equinix, STT GDC, EdgeConneX, NEXTDC.
2. **Normalize entity names**: Malaysian SPVs often differ from global brand names. Search corporate/legal names from operator releases, Bursa filings, MIDA/MDEC, and contractor contracts.
3. **Assign state, district, PBT, mukim, and industrial park**. Malaysian planning evidence is often PBT-specific; a "Kuala Lumpur" cloud label may mean Greater KL / Selangor.
4. **Pull planning trail**: OSC 3.0 Plus / DBKL / council pages; search `kebenaran merancang`, `pelan bangunan`, `pelan kerja tanah`, `pelan jalan dan parit`, `Mesyuarat OSC`, and `CCC`.
5. **Pull energy trail**: TNB Green Lane / ESA / MVA / 132kV / 275kV / substation; Sarawak Energy and Sabah Electricity outside Peninsular Malaysia.
6. **Pull water / environment trail**: DOE EIA status, water utilities, SPAN, recycled-water agreements, cooling and generator details.
7. **Pull regulator / service trail**: MCMC ASP(C), network licences, ReCPro cabling/network ecosystem, MDEC Malaysia Digital Status.
8. **Use trade press only to fill gaps**, then downgrade if no primary corroboration is found.

Minimum record fields:

```text
facility_name
operator_brand
legal_entity / applicant / landowner
state
district / city / PBT
mukim / industrial park / street
source_status: planned | approved | under construction | energized | operating | cancelled
planning_evidence: application_no, approval_type, date, URL
power_evidence: TNB/Sarawak/Sabah, MVA/MW, voltage, ESA/connection, date, URL
water_environment_evidence: DOE/EIA/SPAN/water utility, date, URL
cloud_or_operator_evidence: official page/release, URL
confidence_grade
notes / unresolved conflicts
```

---

## 12. Red Flags and Caveats

- **"Greater Kuala Lumpur" is not necessarily Kuala Lumpur Federal Territory**. Most hyperscale land is in Selangor or adjacent states.
- **Cloud region != physical site list**. Treat AZ count and region labels as official, but do not infer coordinates without planning / power / operator evidence.
- **MIDA aggregate investment totals are not facility counts**. Use them for macro context and individual releases only.
- **OSC detail may be login-gated**. Public meeting titles, PBT announcements, councillor reports, and trade press may provide application numbers that unlock status searches.
- **Johor capacity claims change quickly**. Re-check official operator pages and TNB/utility evidence before using MW values.
- **Environmental evidence is uneven**. Absence from DOE search is not proof of no project or no environmental obligations.
- **Datacenters may be permitted as industrial, commercial, utility, ICT, warehouse, office, or mixed infrastructure**, not always under `pusat data`.
