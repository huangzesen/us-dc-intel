# TN Explorer Industry - Tunisia Datacenter Enumeration via Trade Press, Operator Pages, Directories, and Governorate Search Patterns

Date: 2026-08-12. Country: **TN Tunisia**. Scope: industry / press / vendor-led discovery for Tunisian data centers, with official verification routes for every lead. Reliability grades: **A** = official / primary source for the fact claimed; **B** = strong secondary / trade press; **C** = weak lead or directory-only evidence.

Grade calibration:
- **A**: operator facility page, INTT / MTC / ANCS / CNI / ATI / TIA / ministry / governorate page, official procurement, TUV / ISO / PCI / Uptime source, official hyperscaler region list.
- **B**: DCD, Agence Ecofin / We Are Tech Africa, Webmanagercenter, THD, Tekiano, ilboursa, African Manager, La Presse, Business News, Leaders, L'Economiste Maghrebin, TAP reposts, reputable vendor / integrator pages with named project details.
- **C**: DataCenterMap, Baxtel, datacenters.com, Cloudscene, WHTop, social posts, snippets, inaccessible reports, generic provider directories, unverified addresses.

---

## 0. Tunisia market frame

- Tunisia is a **small but active data-center market** led by telecom operators, public-sector hosting, and one established neutral private colo. The confirmed commercial / institutional geography is concentrated in **Tunis / Greater Tunis** and **Sousse governorate**, with **Bizerte** emerging as a cable-landing / planned-AI-DC corridor.
- Confirmed or high-confidence facility anchors: **Tunisie Telecom Data Center Carthage / Tunis DC**, **Ooredoo Tunisie La Charguia 1 data center**, **Orange Tunisie Kalaa Kebira data center**, **EO Data Center / Meninx Enfidha**, **ATI data centers**, and **CNI private cloud**. **SoleCrypt Bizerte** is planned / MoU-stage until primary construction, permit, power, or commissioning proof appears.
- Recent market signals to track:
  - Orange Tunisie inaugurated a data center at **Kalaa Kebira, Sousse** in May 2025; Orange's own page is A for the facility and date, while DCD / ilboursa / We Are Tech are B for corroborating Tier III-quality and 1,000 m2 details.
  - TIA's 22nd Strategic Council on **2025-10-14** made data centers a strategic investment topic; TIA's own page is A for policy status, not for any facility.
  - The Medusa / ViaTunisia submarine system gives **Bizerte** strong connectivity relevance. Treat the Bizerte landing station as a connectivity asset, not a data center.
  - SoleCrypt and Schneider Electric signed a **2026-02-02 MoU** to study / co-develop AI data centers in Tunisia; DCD / African Manager report Bizerte, 20 MW, and Tozeur solar details. Keep stage `planned` unless later official evidence confirms construction.
- Energy and water constraints matter for large projects. Do not turn national renewable targets, STEG grid context, or solar-plant capacity into data-center IT load unless the source explicitly ties capacity to the named data-center site.
- No AWS, Azure, Google Cloud, or Oracle OCI official public-region list shows Tunisia as a public cloud region as of 2026-08-12. Search for partner / edge / reseller evidence separately, but do not count it as a hyperscaler region.

Core national query set:

```text
Tunisia "data center" Tunis
Tunisia datacenter Sousse
Tunisie "centre de donnees" Tunis
Tunisie "centre de données" Sousse
"Tunisie Telecom" "Data Center Carthage"
"Ooredoo Tunisie" "La Charguia" "data center"
"Orange Tunisie" "Kalaa Kebira" "data center"
"EO Data Center" Enfidha
"Meninx" Enfidha "data center"
"ATI" "data centers" Tunisie
"CNI" "Cloud prive" "Tunisie Digitale"
"SoleCrypt" Bizerte "data center"
"Medusa" Bizerte "landing station"
```

Arabic secondary checks:

```text
"تونس" "مركز البيانات"
"سوسة" "مركز البيانات"
"بنزرت" "مركز البيانات"
"صفاقس" "مركز البيانات"
"مركز البيانات" "الاستضافة" "تونس"
```

---

## 1. High-signal trade and press sources

Use press to discover project names, dates, officials, integrators, technical terms, and localities. Then upgrade or hold the grade based on primary evidence.

| Source | URL / route | Use | Default grade |
|---|---|---|---|
| Data Center Dynamics | https://www.datacenterdynamics.com/en/news/ | Orange Sousse launch; SoleCrypt Bizerte / Schneider / solar-backed AI DC lead. | B |
| We Are Tech Africa | https://www.wearetech.africa/ | Tunisia digital-infrastructure coverage; Orange Sousse article. | B |
| Agence Ecofin | https://www.agenceecofin.com/ | Telecom / digital-sector news; ATI-Meninx IPv6 / DNS partnership. | B |
| Webmanagercenter | https://www.webmanagercenter.com/ | Ooredoo La Charguia visit; TIA data-center strategy; ATI-Meninx coverage. | B |
| THD - Tunisie Haut Debit | https://www.thd.tn/ | Historical TT data-center inauguration mirror; Huawei modular DC / energy-sector leads; EO / Oxabox partnership. | B |
| Tekiano | https://www.tekiano.com/ | Meninx / first private data center history; TT ISO news. | B |
| ilboursa | https://www.ilboursa.com/ | Orange Kalaa Kebira 2025 launch with locality / area details. | B |
| African Manager / en.africanmanager.com | https://africanmanager.com/ and https://en.africanmanager.com/ | TIA strategy analysis; SoleCrypt Bizerte / Tozeur lead; water / energy constraints. | B |
| La Presse | https://www.lapresse.tn/ | National cloud / ANCS labelling context; CCK supercomputer / public digital context. | B |
| Business News / Leaders / L'Economiste Maghrebin | site-scoped searches | Certifications, policy sessions, corporate announcements. | B |
| TAP | https://www.tap.info.tn/ | Official-agency government / operator announcements where accessible. | A/B depending host and directness. |
| Operator / vendor pages | orange.tn, tunisietelecom.tn, ooredoo.tn, eodatacenter.com, solecrypt.com, Schneider Electric | Facility launches, service claims, MoUs, certifications. | A for self-claimed facility / service facts; B/C for unverifiable specs. |
| Directories | DataCenterMap, datacenters.com, Baxtel, Cloudscene, WHTop | Facility names, localities, addresses, rough capacity leads. | C unless corroborated. |

Trade-press query templates:

```text
site:datacenterdynamics.com/en/news/ Tunisia "data center"
site:datacenterdynamics.com/en/news/ "SoleCrypt"
site:datacenterdynamics.com/en/news/ "Orange" "Sousse"
site:wearetech.africa Tunisia "data center"
site:wearetech.africa Tunisie "centre de donnees"
site:agenceecofin.com Tunisie "data center"
site:agenceecofin.com Tunisie "centre de donnees"
site:webmanagercenter.com Tunisie "data center"
site:webmanagercenter.com "La Charguia" "data center"
site:tekiano.com Tunisie "data center"
site:thd.tn "data center" Tunisie
site:ilboursa.com "data center" "Sousse"
site:africanmanager.com "data center" Tunisie
site:en.africanmanager.com Tunisia "data center"
site:lapresse.tn "centre de donnees"
site:tap.info.tn "data center" Tunisie
```

Status-language interpretation:

- `protocole d'accord`, `MoU`, `etudier`, `co-develop`, `annonce`, `projet`, `convention` = planned / study lead. Do not mark under construction.
- `appel d'offres`, `consultation`, `attribution`, `signature du contrat` = procurement / award. Verify buyer and site.
- `pose de la premiere pierre`, `lancement des travaux`, `construction`, `chantier` = construction lead. Confirm with official / contractor page.
- `inaugure`, `lance`, `mis en service`, `operationnel`, `certifie`, `obtient la certification` = commissioned / operational signal, subject to source grade.
- `cloud`, `VPS`, `hebergement`, `housing`, `SaaS`, `backup`, `PRA` = service evidence only unless physical facility is named.

---

## 2. Operator and provider sweep

Official operator pages are **A for current service or self-claimed facility existence**. They are not automatically A for exact address, power, racks, or certification unless those details appear on the official page or certificate.

| Operator / provider | Main route | Likely geography | Verification notes |
|---|---|---|---|
| Tunisie Telecom | https://www.tunisietelecom.tn/ and https://www.tunisietelecom.tn/particulier/actualite/ttdatacentercarthage/ | Tunis | TT official / TUV evidence supports Data Center Carthage certification. MTC supports 2015 inauguration of a new TT data center in Tunis. Directories give Carthage / Rue Tirons / Avenue de Carthage address leads; keep address C unless primary source confirms. |
| Ooredoo Tunisie | https://www.ooredoo.tn/ and https://host.ooredoo.tn/ | Tunis / La Charguia 1 | Ooredoo hosting pages are A for service / Tunisia DC storage claims. WMC 2016 visit is B for La Charguia 1 physical site. Specs and capacity remain unknown. |
| Orange Tunisie | https://www.orange.tn/ | Sousse / Kalaa Kebira; Bizerte landing station | Orange official 2025 article is A for the Kalaa Kebira DC. DCD / ilboursa / We Are Tech are B for area and Tier III-quality details. Bizerte is a cable-landing station unless a DC facility is separately identified. |
| ATI - Tunisie Internet | https://www.ati.tn/ and https://www.ati.tn/housing/ | Tunis | ATI says it hosts data in ATI data centers and offers housing in Tunisian datacenters. A for service / existence; exact site and capacity need further confirmation. |
| CNI | https://www.cni.tn/ + AfDB / MTC procurement | Tunis likely, but verify | CNI private-cloud project is A via AfDB / MTC procurement; do not use CNI office address as facility address without implementation evidence. |
| EO Data Center / Meninx | https://www.eodatacenter.com/ | Enfidha, Sousse governorate | EO official page states its main infrastructure is in Zone Industrielle d'Enfidha and is carrier-neutral / sovereign cloud. Press supports first-private / neutral history and 2013 launch. |
| Topnet | https://www.topnet.tn/ | Ariana / El Ghazala lead | Historical hosting-DC claims are B/C. Require current Topnet page, INTT / MTC source, or directory corroboration before counting as active facility. |
| GlobalNet / HexaByte / Tunet | official ISP / hoster domains | Greater Tunis / ISP offices | Provider leads only. Search for physical facility, housing, ISO, or named DC before counting. |
| Novahoster and small hosters | provider domains + WHTop / directories | Tunis-area leads | C unless the provider publishes facility details or a primary source corroborates. |
| NeoLedge | company / press | Tunis-area cloud-service lead | Market-recognition lead only; physical hosting site must be separately verified. |
| CCK - Centre de Calcul El-Khawarizmi | https://cck.rnu.tn/ | Tunis | Institutional HPC / research compute. Count as institutional compute, not commercial colocation. |
| BCT / banks / insurers | official pages, tenders, local press | Tunis + possible DR outside Tunis | Internal DC / DR leads only; require named project, procurement, or permit evidence. |
| SoleCrypt | https://www.solecrypt.com/ | Bizerte planned DC; Tozeur solar asset | Official MoU page is A for Schneider MoU. Bizerte / 20 MW / Tozeur T60 details are B unless company or permit sources confirm each detail. Stage planned until construction evidence. |

Operator / provider queries:

```text
"{operator}" Tunisie "data center"
"{operator}" Tunisie "centre de donnees"
"{operator}" "ISO 27001" "data center"
"{operator}" "Tier III" Tunisie
"{operator}" "PCI-DSS" Tunisie
"{operator}" "{governorate}" "data center"
"{operator}" "cloud" "hebergement" Tunisie
"{operator}" "housing" Tunisie
"{operator}" "inauguration" "data center"
"{operator}" "certification" "data center"
```

Facility-address pivots:

```text
"Data Center Carthage" Tunis
"Tunisie Telecom Carthage Data Center"
"Avenue de Carthage" "data center"
"Rue Tirons" "Data Center Carthage"
"La Charguia 1" "Ooredoo" "data center"
"Kalaa Kebira" "Orange Tunisie" "data center"
"El Kalaa El Kebira" "data center" "Orange"
"Enfidha" "EO Data Center"
"Zone Industrielle Enfidha" "datacenter"
"Parc d'activites economiques de Bizerte" "data center"
"SoleCrypt" "Bizerte" "20MW"
"El Ghazala" "Topnet" "data center"
```

---

## 3. Directory and aggregator handling

Directories are useful in Tunisia because operator pages can be sparse, but they are never enough for high-confidence facility enumeration.

| Directory / lead source | What it can provide | Caveats |
|---|---|---|
| DataCenterMap Tunisia | https://www.datacentermap.com/tunisia/ | Tunis / Sousse / Bizerte market pages; TT Carthage, Orange Sousse, EO Enfidha, SoleCrypt-style leads. | C by default. Verify status, address, and capacity. |
| datacenters.com Tunisia | https://www.datacenters.com/locations/tunisia | Provider / location index and contact pages. | C; sometimes sales-oriented and sparse. |
| Baxtel | https://baxtel.com/ | News summary for large planned projects such as SoleCrypt. | B for sourced news summary; C for directory data. |
| Cloudscene | https://cloudscene.com/ | Provider profiles and market listings. | C/B-; verify with operator / INTT. |
| WHTop / ma-tunisie.com | hosting-provider lists | Provider names, service categories, hosting claims. | C; useful for discovery only. |
| PeeringDB / bgp.tools | ASNs, IX / interconnection clues. | Network presence only; not facility proof. |

Directory upgrade workflow:

1. Capture exact facility name, address, market, operator, status, and any capacity from the directory.
2. Search the exact name on the operator's domain.
3. Search INTT / MTC / ANCS / TIA for the legal entity or project name.
4. Search certifier / Uptime / PCI / ISO records and local permits for the site.
5. If no primary or strong secondary source appears, keep the lead at **C** with a caveat.

Directory query templates:

```text
site:datacentermap.com/tunisia "Tunisie Telecom"
site:datacentermap.com/tunisia "Ooredoo"
site:datacentermap.com/tunisia "Orange"
site:datacentermap.com/tunisia "EO Data Center"
site:datacentermap.com/tunisia "SoleCrypt"
site:datacenters.com/locations/tunisia "{operator}"
site:baxtel.com Tunisia "data center"
site:cloudscene.com Tunisia "{operator}"
site:whtop.com Tunisia "data center"
site:peeringdb.com Tunisia "{operator}"
```

---

## 4. Official verification routes for industry leads

Every industry lead should be checked against the official routes below before it is promoted above B/C.

| Route | URL | What to verify |
|---|---|---|
| INTT | https://www.intt.tn/ and https://intt.tn/eservices/index.php | Operator / ISP / SVA legal status, decisions, annual-report references, fibre / interconnection context. |
| MTC | https://www.mtc.gov.tn/ | Ministerial launches, procurement, cloud strategy, public digital projects. |
| ANCS | https://ancs.tn/ | Hosting-provider labelling and cloud / cybersecurity governance. |
| CNI | https://www.cni.tn/ | Government IT / CNI project context. |
| ATI | https://www.ati.tn/ and https://www.ati.tn/housing/ | ATI data centers, housing, .tn / TunIXP support. |
| INPDP | https://www.inpdp.tn/ | Data-protection / hosting obligations; context only. |
| TIA | https://tia.gov.tn/ | Investment-priority status, conventions, large-project leads, special-zone discussion. |
| STEG / ANME | https://www.steg.com.tn/ and https://www.anme.tn/ | Power, grid, transformer, self-production, renewables context. |
| Certifier / standards | TUV Rheinland Certipedia, PCI / Uptime pages | Named facility certification claims. |
| Official cloud regions | AWS, Azure, Google Cloud, Oracle official pages | Confirm no Tunisia public hyperscaler region. |

Verification query templates:

```text
site:intt.tn "{operator}"
site:intt.tn "{project}"
site:mtc.gov.tn "{project}"
site:mtc.gov.tn "{governorate}" "data center"
site:ancs.tn "{provider}" "hebergement"
site:cni.tn "{project}"
site:ati.tn "{provider}"
site:tia.gov.tn "data center"
site:steg.com.tn "{project}"
site:anme.tn "{project}"
site:tunisietelecom.tn "Data Center Carthage"
site:orange.tn "Kalaa Kebira" "data center"
site:eodatacenter.com "Enfidha"
site:solecrypt.com "Schneider" "Tunisia"
```

---

## 5. Governorate-by-governorate industry search matrix

Use all 24 governorates from the manifest. For high-priority locations, run French, English, and Arabic searches. For low-priority locations, run the negative checklist and only count named physical facilities, institutional compute, or server rooms.

### 5.1 Highest priority

| Governorate | Localities / terms | Industry / operator seeds |
|---|---|---|
| **Tunis** | Carthage, Avenue de Carthage, Rue Tirons, La Charguia 1, Mutuelleville, Belvedere, El Omrane, Cite El Khadra, Berges du Lac | Tunisie Telecom Carthage / Tunis DC, Ooredoo La Charguia, ATI DCs, CNI private cloud, CCK HPC, ministry and BCT / bank DC or DR leads, GlobalNet / HexaByte / Tunet / NeoLedge leads. |
| **Ariana** | El Ghazala, Technopark, Raoued, Charguia-adjacent ambiguity | Topnet historical DC / hoster lead; ISP offices and technopark companies. Verify whether any "Charguia" result is Tunis or Ariana before assigning. |
| **Sousse** | Kalaa Kebira, Enfidha, Sahloul, Sousse technopole | Orange Kalaa Kebira DC; EO Data Center / Meninx Enfidha; technopole server-room / cloud leads. |
| **Bizerte** | Bizerte city, Menzel Bourguiba, Parc d'activites economiques de Bizerte, cable landing | SoleCrypt planned AI DC, Medusa / Orange landing station, Schneider / renewables leads. Landing station is not a DC. |
| **Sfax** | Sfax city, Sakiet Ezzit, Technopole de Sfax, University of Sfax | Second economic city and ICT technopole; no confirmed major DC in opened sources. Search deeply, then mark negative if no named facility appears. |

### 5.2 Medium priority

| Governorate | Search focus |
|---|---|
| Ben Arous | Industrial zones, Borj Cedria, bank / DR sites, Greater Tunis overflow. |
| Manouba | Greater Tunis institutional / university server-room leads. |
| Nabeul | Cap Bon industrial / tourism ICT; governorate and commune sites. |
| Zaghouan | Industrial zones and Tunis-adjacent DR / utility leads. |
| Monastir | Technopole, university, airport corridor, health / textile IT. |
| Mahdia | University / public-sector server-room leads. |
| Tozeur | SoleCrypt / T60 solar and other solar projects. Treat as energy asset unless a DC is physically named in Tozeur. |
| Sidi Bouzid | Renewable-energy context, including solar projects; not a DC lead without site evidence. |
| Gabes | Industrial / port / chemical sector internal compute. |
| Medenine | Southern corridor, oil-gas support, university / public-sector IT. |
| Gafsa | Mining / phosphate / university internal compute. |
| Kebili | Energy and public-sector IT; likely sparse. |

### 5.3 Lower priority / negative-search governorates

Lower-yield governorates: Beja, Jendouba, Le Kef, Siliana, Kairouan, Kasserine, Tataouine, plus any medium-priority governorate with no initial signals.

Negative-search checklist:

```text
"{governorate}" "centre de donnees"
"{governorate}" "centre de données"
"{governorate}" "data center"
"{governorate}" datacenter
"{governorate}" "cloud"
"{governorate}" "hebergement"
"{governorate}" "hébergement"
"{governorate}" "colocation"
"{governorate}" "salle serveur"
"{governorate}" "salle informatique"
"{governorate}" "universite" "HPC"
"{governorate}" "centre de calcul"
"{governorate}" "Tunisie Telecom" "data center"
"{governorate}" "Ooredoo" "data center"
"{governorate}" "Orange" "data center"
site:datacenterdynamics.com/en/news/ Tunisia "{governorate}"
site:wearetech.africa Tunisie "{governorate}" "data center"
site:webmanagercenter.com "{governorate}" "data center"
site:datacentermap.com/tunisia "{governorate}"
```

Do not over-count generic ICT centers, training centers, cyber labs, call centers, or telecom POPs.

---

## 6. Candidate handling examples

Use these examples to calibrate final records:

| Candidate | Handling |
|---|---|
| Tunisie Telecom Data Center Carthage / Tunis data center | **A** for facility and certification via Tunisie Telecom / TUV / MTC. Operational. Capacity null unless published. Directory address remains **C**. |
| Ooredoo Tunisie La Charguia 1 | **B** for physical La Charguia site via WMC press visit; **A** for Ooredoo-hosted service claim on Ooredoo pages. Operational but specs / capacity unknown. |
| Orange Tunisie Kalaa Kebira | **A** for facility / date / locality via Orange official page. **B** for secondary 1,000 m2 / Tier III-quality corroboration if not explicit on official page. Operational from 2025-05-05. |
| EO Data Center / Meninx Enfidha | **A** for current operator page and Enfidha location; **B** for historical first-private / neutral DC and older size / Tier III+ design claims. Operational. |
| ATI data centers | **A** for ATI data-center / housing service existence. Exact addresses, number of halls, racks, and power need separate evidence. |
| CNI private cloud | **A** for public procurement / AfDB project. Treat as government-hosting platform; verify implementation site before assigning an exact facility address. |
| CCK / Centre de Calcul El-Khawarizmi | Institutional HPC / research compute, not colocation. Count only if the schema supports institutional compute. |
| SoleCrypt Bizerte | **A** for the SoleCrypt-Schneider MoU, **B** for DCD / African Manager details such as Bizerte, 20 MW, Tozeur solar. Stage planned / study until construction or permit evidence appears. |
| Orange / Medusa Bizerte landing station | Connectivity asset. Do not count as a data center. Useful for Bizerte corridor scoring. |
| Topnet / GlobalNet / HexaByte / Tunet / Novahoster | Provider leads. Count only if a current physical data center / housing facility is named by operator, regulator, certificate, permit, or strong press. |

---

## 7. Output discipline

For each final project record:

- Normalize the governorate to the 24-governorate manifest spelling.
- Preserve the exact commune / locality / industrial zone in notes.
- Use French source names and add English aliases only when a source uses them.
- Put MW in `capacity_mw` only when the source ties MW to that named data-center facility.
- Put sqm, racks, kVA, MVA, generators, UPS, and cooling claims in notes unless the schema has a separate field.
- Use `evidence_grade=A` only for the specific facts proven by primary evidence.
- Keep planned / MoU / cable / solar records out of the operational facility count.
- Mark `no_projects` only after official, operator, press, and directory checks have run and national projects physically located elsewhere have been excluded.
