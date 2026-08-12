# TN Explorer Official - Tunisia Datacenter Enumeration via INTT, MTC, ANCS, CNI/ATI, INPDP, TIA, Urbanism, STEG, and Official Operators

Date: 2026-08-12. Country: **TN Tunisia**. Division model: **24 governorates**. Angle: **official / regulatory / public-sector / investment / utility routes** for finding operational, planned, under-construction, public-institutional, and connectivity-adjacent data-center assets.

Reliability grades:
- **A** = primary / official evidence for the specific claim: INTT page, telecom licence or decision, MTC / ANCS / CNI / ATI / INPDP / TIA / ministry / governorate / commune page, official procurement notice, STEG / ANME source, operator facility page, official ISO / PCI / Uptime certificate or certifier record, official public-cloud region list.
- **B** = strong secondary evidence: DCD, Agence Ecofin / We Are Tech Africa, Webmanagercenter, THD, Tekiano, ilboursa, African Manager, La Presse, Business News, Leaders, L'Economiste Maghrebin, TAP carried by a non-official host, or a named vendor / integrator article with project details.
- **C** = weak lead: DataCenterMap, Baxtel, datacenters.com, Cloudscene, WHTop, social posts, inaccessible snippets, generic market reports, or directory-only addresses.

---

## 0. Tunisia-specific structural facts

- Tunisia has **no public national data-center register** and no complete open planning-permit search. Enumeration works by joining telecom/legal status, ministry cloud policy, public-sector hosting, investment files, operator facility pages, certification records, utility context, and local press.
- Tunisia is divided into **24 governorates / gouvernorats / wilayat**. Use the ISO / government spelling set: Ariana, Beja, Ben Arous, Bizerte, Gabes, Gafsa, Jendouba, Kairouan, Kasserine, Kebili, Le Kef, Mahdia, Manouba, Medenine, Monastir, Nabeul, Sfax, Sidi Bouzid, Siliana, Sousse, Tataouine, Tozeur, Tunis, Zaghouan. ISO's entry for Tunisia and Tunisia's industry portal both list 24 first-level governorates.
- The highest-yield language is **French**. Arabic is useful on public pages and local press. English is useful for DCD, vendor pages, cloud-region pages, and international cable coverage.
- Product vocabulary is inconsistent. Search all forms: `data center`, `datacenter`, `data centre`, `centre de donnees`, `centre de données`, `centre de calcul`, `cloud`, `cloud souverain`, `cloud national`, `hebergement`, `hébergement`, `colocation`, `housing`, `salle serveur`, `salle informatique`, `HPC`, `calcul haute performance`.
- The market is **telecom-led, public-sector-led, and small private-colo-led**. Confirmed physical / institutional anchors include Tunisie Telecom Data Center Carthage in Tunis, Ooredoo Tunisie's La Charguia data center in Tunis, Orange Tunisie's Kalaa Kebira data center in Sousse governorate, EO Data Center / Meninx in Enfidha, ATI data centers in Tunis, and CNI's public-sector private-cloud project. SoleCrypt's Bizerte AI data-center plan is a **planned lead**, not an operational facility unless later construction / commissioning evidence appears.
- Submarine-cable landing stations are **connectivity assets, not data centers**. Bizerte is important because Orange Tunisie / Medusa evidence places a cable landing there, and SoleCrypt links its planned Bizerte site to landing-point geography.
- No official AWS, Microsoft Azure, Google Cloud, or Oracle OCI public-cloud region list shows a Tunisia public cloud region as of 2026-08-12. Treat Tunisia as a sovereign / hosted-cloud and telecom-cloud market unless an official provider region page changes.
- Capacity discipline: record MW / MVA / kVA / racks / square meters only when tied to a named site by the source. Do not derive MW from national electricity statistics or a solar plant unless the source explicitly ties it to a data-center project.

Core vocabulary:

```text
centre de donnees / centre de données
data center / datacenter / data centre
centre de calcul / calcul haute performance / HPC
cloud souverain / cloud national / cloud computing
hebergement / hébergement / housing / colocation
salle serveur / salle informatique / salle blanche
onduleur / UPS / groupe electrogene
climatisation de precision / refroidissement liquide
poste electrique / transformateur / raccordement
fibre optique / cable sous-marin / station d'atterrissement
permis de construire / autorisation d'urbanisme / etude d'impact
appel d'offres / consultation / marche public / attribution
autorisation / licence / cahier des charges / services a valeur ajoutee
```

Arabic terms for secondary checks:

```text
مركز البيانات
مركز الحوسبة
مركز الحساب
الاستضافة
السحابة السيادية
السحابة الوطنية
رخصة البناء
شركة الكهرباء والغاز
هيئة الاتصالات
```

---

## 1. Grade A official / regulatory routes

### 1.1 INTT - Instance Nationale des Telecommunications

Primary source: **INTT**, https://www.intt.tn/. INTT is the telecom regulator created under Tunisia's telecommunications code. Its site is the main official route for operator / ISP / SVA status, annual sector reporting, interconnection, fibre, and decisions.

High-value pages verified:

| Route | URL | Use |
|---|---|---|
| INTT homepage | https://www.intt.tn/ | News, notices, operator context, SVA declaration references. |
| E-services portal | https://intt.tn/eservices/index.php | SVA / operator filing route. |
| Annual reports | https://www.intt.tn/fr/index-rapports-annuels-266-402.html and https://www.intt.tn/fr/index-rapports-annuels-264-333.html | Operator market context and sector statistics. |
| Fibre optique dossier | https://www.intt.tn/fr/index-fibre-optique-265-404.html | Fibre / wholesale infrastructure context. |
| Location de capacites excedentaires | https://www.intt.tn/fr/index-location-de-capacites-excedentaires-265-395.html | Excess-capacity / wholesale-route context. |
| QoS Internet fixe | https://www.intt.tn/fr/index-qos-internet-265-398.html | ISP list and fixed-Internet performance context. |
| Textes de reference | https://www.intt.tn/fr/index-les-lois-263-331.html, https://www.intt.tn/fr/index-les-decrets-263-356.html, https://www.intt.tn/fr/index-les-arretes-263-332.html | Legal basis / cahiers des charges. |
| Decisions | https://www.intt.tn/fr/index-les-decisions-274-334.html | Regulatory decisions and market rules. |

How to use:

- INTT evidence is **A for legal / telecom / SVA status**, not automatic facility evidence. A telecom operator, ISP, or SVA declarant may host in its own data center, leased space, or another provider's facility.
- Pull legal names and licence / authorisation classes first, then pivot to operator facility pages, MTC announcements, certificates, tenders, and local permits.
- Search current and historical spellings: `Tunisie Telecom`, `Tunisie Télécom`, `Ooredoo Tunisie`, `Orange Tunisie`, `Topnet`, `TopNet`, `GlobalNet`, `HexaByte`, `Tunet`, `ATI`, `Meninx`, `EO Data Center`.

INTT query templates:

```text
site:intt.tn "licence" "Tunisie Telecom"
site:intt.tn "licence" "Ooredoo Tunisie"
site:intt.tn "licence" "Orange Tunisie"
site:intt.tn "services a valeur ajoutee"
site:intt.tn "services à valeur ajoutée"
site:intt.tn "SVA" "declaration"
site:intt.tn "hebergement"
site:intt.tn "hébergement"
site:intt.tn "cloud"
site:intt.tn "centre de donnees"
site:intt.tn "data center"
site:intt.tn "capacites excedentaires"
site:intt.tn "fibre optique"
site:intt.tn "{operator}" "decision"
site:intt.tn "rapport annuel" "{year}"
"INTT" "{operator}" "autorisation"
```

Extract: legal name, licence class, service class, decision / declaration date, address, and any disclosed network, storage, interconnection, or wholesale detail.

### 1.2 MTC - Ministere des Technologies de la Communication

Primary source: **MTC**, https://www.mtc.gov.tn/. Use it for ministerial data-center inaugurations, national cloud policy, public digital projects, and procurement notices.

Verified official anchors:

- MTC published the **2015-01-15 inauguration of Tunisie Telecom's new data center in Tunis**: https://www.mtc.gov.tn/index.php?cHash=4ae7c8470a22c49f7b2bf96a4e9baa7d&id=119&tx_ttnews%5Btt_news%5D=2707. This is **A for a Tunisie Telecom data center in Tunis** and for its business-hosting purpose. It does not publish MW capacity.
- MTC published tender / postponement pages for the **CNI private-cloud project**, including "Mise en place d'un Cloud prive pour le Centre National de l'informatique": https://www.mtc.gov.tn/index.php?cHash=ad3205d1b0a984049ba3e497c442a3f4&id=291&tx_ttnews%5Btt_news%5D=4935.

MTC query templates:

```text
site:mtc.gov.tn "centre de donnees"
site:mtc.gov.tn "centre de données"
site:mtc.gov.tn "data center"
site:mtc.gov.tn "cloud prive"
site:mtc.gov.tn "Cloud First"
site:mtc.gov.tn "Tunisie Digitale"
site:mtc.gov.tn "{operator}" "data center"
site:mtc.gov.tn "{governorate}" "data center"
site:mtc.gov.tn "{governorate}" "centre de donnees"
site:mtc.gov.tn "appel d'offres" "cloud"
```

Grade **A** for the named project / governorate / date when the MTC page names the facility or procurement. Leave `capacity_mw` null unless MTC or another primary source gives capacity.

### 1.3 ANCS - Agence Nationale de la Cybersecurite

Primary source: **ANCS**, https://ancs.tn/. ANCS succeeds / continues national cybersecurity functions and sits under the MTC ecosystem.

Why it matters:

- ANCS is a cloud-governance and cybersecurity route. Secondary policy reporting says Tunisia's national cloud strategy assigns ANCS a role in **labelling hosting-service providers**. Treat any ANCS-published provider list as **A for approved-provider status**, but still verify the physical facility separately.
- ANCS pages are useful for security obligations, incident / hosting governance, and government-cloud policy. They are not a complete facility registry.

ANCS query templates:

```text
site:ancs.tn "hebergement"
site:ancs.tn "hébergement"
site:ancs.tn "cloud"
site:ancs.tn "labellisation"
site:ancs.tn "data center"
site:ancs.tn "centre de donnees"
site:ancs.tn "{provider}"
"Agence Nationale de la Cybersecurite" "hebergement" "{provider}"
"ANCS" Tunisie "cloud" "fournisseur"
```

### 1.4 CNI and ATI - public-sector hosting

Primary sources:

| Entity | URL | Verified use |
|---|---|---|
| CNI - Centre National de l'Informatique | https://www.cni.tn/ | Public IT agency under MTC. Its address is in El Omrane, Tunis; facility location must be verified separately. |
| AfDB CNI private-cloud procurement | https://www.afdb.org/fr/documents/aoi-tunisie-mise-en-place-dun-cloud-prive-pour-le-centre-national-de-linformatique-tunisie-digitale-2020 and https://www.afdb.org/en/documents/attribution-de-marches-tunisie-mise-en-place-dun-cloud-prive-pour-le-centre-national-de-linformatique-tunisie-digitale-2020 | **A for a CNI private-cloud project** under Tunisie Digitale 2020; use buyer documents for award / stage and search for the implementation site. |
| ATI - Tunisie Internet | https://www.ati.tn/ and https://www.ati.tn/housing/ | ATI states that products and data are hosted in ATI data centers and markets housing / colocation in Tunisian datacenters. **A for ATI hosting / DC service existence**, not exact addresses or capacity unless published. |
| .tn registry | https://www.registre.tn/ | .tn registry / DNS context, often linked to ATI infrastructure. |

Queries:

```text
site:cni.tn "cloud"
site:cni.tn "data center"
site:cni.tn "centre de donnees"
site:cni.tn "hebergement"
site:afdb.org "Centre National de l'Informatique" "Cloud prive"
site:mtc.gov.tn "Centre National de l'informatique" "Cloud prive"
site:ati.tn "data centers"
site:ati.tn "datacenters"
site:ati.tn "housing"
site:ati.tn "hebergement"
site:registre.tn "data center"
"ATI" "Meninx" "Enfidha"
"TunIXP" "Meninx"
```

Count CNI / ATI / ministry systems as **institutional / government hosting** unless a page clearly markets commercial colocation.

### 1.5 INPDP - data protection context

Primary source: **INPDP**, https://www.inpdp.tn/.

Use INPDP for compliance context, not as a facility register. Tunisia's data-protection framework affects cloud / hosting buyers and operators; investment-policy sources also point to GDPR alignment as a data-center investment condition.

Queries:

```text
site:inpdp.tn "hebergement"
site:inpdp.tn "hébergement"
site:inpdp.tn "centre de donnees"
site:inpdp.tn "cloud"
site:inpdp.tn "2022-34"
"Instance Nationale de Protection des Donnees Personnelles" "cloud"
"loi organique 2022-34" Tunisie "donnees personnelles"
```

### 1.6 TIA - Tunisia Investment Authority

Primary source: **TIA**, https://tia.gov.tn/.

Verified official anchor:

- TIA's page "Data Center Sector: Emerging Strategic Growth Pillar for Tunisia" reports that during the **22nd Strategic Council meeting on 2025-10-14**, TIA presented data-center trends, Tunisia's advantages, and investment opportunities: https://tia.gov.tn/news-details/data-center-sector-emerging-strategic-growth-pillar-tunisia. This is **A for TIA policy / investment-priority status**, not evidence of any individual facility unless the page names one.

Why it matters:

- TIA can surface large-project declarations, investment conventions, incentive files, and special-zone discussions for cloud / data centers.
- Use TIA to discover promoters and governorates, then verify through company pages, construction / urbanism, grid, and environmental sources.

TIA query templates:

```text
site:tia.gov.tn "data center"
site:tia.gov.tn "centres de donnees"
site:tia.gov.tn "cloud"
site:tia.gov.tn "convention d'investissement"
site:tia.gov.tn "zone economique" "data center"
"Tunisia Investment Authority" "data center" Tunisie
"Instance Tunisienne de l'Investissement" "centre de donnees"
```

### 1.7 Urbanism, environment, industrial land

Primary routes:

- **Permis de construire** are local / municipal matters, coordinated with governorate and regional equipment / housing services. There is no complete national public search comparable to a US county permit system.
- National administrative-services portal: https://www.tunisie.gov.tn/.
- Governorate portals often use `{name}.gov.tn` and contain local announcements, land / industrial-zone information, and public-works notices.
- **ANPE** / Ministry of Environment routes can expose environmental-impact studies for large installations. Search data-center project names with `etude d'impact`, `EIE`, `ANPE`, and `consultation publique`.
- Industrial land and business parks: AFI / industrial zones and named parks. SoleCrypt sources point to Bizerte business-park / cable-landing geography; verify exact parcel and permit before upgrading from planned.

Urbanism query templates:

```text
"{project}" "permis de construire" Tunisie
"{operator}" "{governorate}" "permis de construire"
"{project}" "autorisation d'urbanisme"
"{project}" "etude d'impact"
"{project}" "ANPE"
"{project}" "zone industrielle"
"{project}" "parc d'activites"
site:tunisie.gov.tn "permis de construire"
site:{governorate-domain} "data center"
site:{governorate-domain} "centre de donnees"
"Agence Fonciere Industrielle" "data center"
"Parc d'activites economiques de Bizerte" "SoleCrypt"
```

Extract: commune, governorate, proponent, land / parcel / industrial zone, permit or EIA status, floorspace, utility connections, and stage.

### 1.8 Energy and grid: STEG / ANME

Primary routes:

| Entity | URL | Use |
|---|---|---|
| STEG | https://www.steg.com.tn/ | Grid / connection / transformer / substation context. |
| ANME | https://www.anme.tn/ | Energy-efficiency, renewables, self-production framework. |

How to use:

- STEG / ANME evidence is usually **context or utility confirmation**, not a data-center registry.
- Search named projects for substations, grid connection, transformers, backup generators, solar self-production, and wheeling. Do not infer facility capacity from a site's solar project unless the data-center source states it.

Energy query templates:

```text
site:steg.com.tn "data center"
site:steg.com.tn "centre de donnees"
site:anme.tn "data center"
site:anme.tn "autoproduction" "solaire"
"{project}" "STEG" "poste electrique"
"{project}" "STEG" "transformateur"
"{project}" "groupe electrogene"
"{project}" "onduleur"
"{project}" "MW" Tunisie "data center"
"SoleCrypt" "Tozeur" "60MW"
"SoleCrypt" "T60"
```

### 1.9 Official cloud-region pages

Use official pages to prevent false positives:

| Provider | Official source | Tunisia signal as of 2026-08-12 | Enumeration use |
|---|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ and https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | No Tunisia public region listed. | A for absence of AWS Tunisia public region. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No Tunisia Azure public region listed. | A for absence; do not treat Microsoft partnerships as a region. |
| Google Cloud | https://cloud.google.com/about/locations | No Tunisia Google Cloud region listed. | A for absence; partner / customer leads only. |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ and https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | No Tunisia OCI public region listed. | A for absence; partner / customer leads only. |

### 1.10 Official operator facility anchors

| Operator / entity | Official source | Known Tunisia signal | Grade / handling |
|---|---|---|---|
| Tunisie Telecom | https://www.tunisietelecom.tn/particulier/actualite/ttdatacentercarthage/ and MTC 2015 page | Data Center Carthage / Tunis data center; TUV Rheinland certification page also identifies "Tunisie Telecom Carthage Data Center". | **A** for facility and certifications. Address from directories is **C** unless TT / MTC confirms it. |
| Ooredoo Tunisie | https://www.ooredoo.tn/ and https://host.ooredoo.tn/ | Ooredoo hosting says data are stored in Ooredoo Tunisia data centers; WMC press visit places a data center at La Charguia 1. | **A** for service claim; **B** for La Charguia facility from press; capacity unknown. |
| Orange Tunisie | https://www.orange.tn/actualites/actus/orange-tunisie-inaugure-un-nouveau-data-center-a-sousse-pour-repondre-aux-enjeux-numeriques-de-demain | Kalaa Kebira, Sousse data center inaugurated with MTC minister present. | **A** for facility, locality, inauguration; operator claims Tier III-quality / 1,000 m2 when present on page. |
| ATI | https://www.ati.tn/ and https://www.ati.tn/housing/ | ATI data centers / housing in Tunisia. | **A** for service existence; exact sites require separate proof. |
| CNI | https://www.cni.tn/ + AfDB / MTC procurement | CNI private-cloud platform under Tunisie Digitale 2020. | **A** for public project; physical hosting site / stage needs award details. |
| EO Data Center | https://www.eodatacenter.com/ | Carrier-neutral / sovereign-cloud data center in Zone Industrielle d'Enfidha, Sousse governorate. | **A** for current operator claim and location; B for historical first-private claims from press. |
| SoleCrypt | https://www.solecrypt.com/post/solecrypt-schneider-electric-mou-sustainable-ai-data-centres-in-tunisia | MoU with Schneider Electric, signed 2026-02-02, to study / co-develop next-generation AI data centers in Tunisia. | **A** for MoU existence; **B/C** for exact Bizerte 20 MW details unless company / permit pages name them. Stage planned. |

---

## 2. Official seed list

| Facility / platform | Governorate | Locality | Type | Stage | Evidence grade | Notes |
|---|---|---|---|---|---|---|
| Tunisie Telecom Data Center Carthage / Tunis data center | Tunis | Tunis / Carthage-area naming; directory address needs confirmation | Telecom data center / hosting / cloud | Operational | A | MTC 2015 inauguration; TT / TUV certification evidence. Capacity unknown. |
| Ooredoo Tunisie data center | Tunis | La Charguia 1 | Telecom data center / network operations / hosting | Operational | B for site, A for service | WMC visit names La Charguia 1; Ooredoo hosting pages support Tunisia DC service. Capacity unknown. |
| Orange Tunisie Kalaa Kebira data center | Sousse | Kalaa Kebira | Telecom / enterprise hosting / cloud / backup / DR | Operational | A | Orange official 2025 announcement; DCD / ilboursa corroborate 1,000 m2 and Tier III-quality language. |
| EO Data Center / Meninx | Sousse | Zone Industrielle d'Enfidha | Neutral colo / sovereign cloud | Operational | A/B | EO official page for current location and service; press for 2013 launch / first-private history. |
| ATI data centers | Tunis | ATI / Tunis area; exact facility addresses not public in opened source | Public ISP / housing / .tn / TunIXP support | Operational | A for service | ATI page says data centers and housing in Tunisia; address / capacity not published. |
| CNI private cloud | Tunis likely, verify implementation site | CNI / public-sector hosting | Awarded / implementation lead | A | AfDB / MTC procurement route; do not infer facility address from CNI office address. |
| CCK / Centre de Calcul El-Khawarizmi | Tunis | MESRS / research network context | Institutional HPC / compute | Operational / institutional | A/B | Count as institutional compute, not commercial colocation. |
| SoleCrypt AI data center | Bizerte planned; Tozeur solar asset | Bizerte DC; Tozeur T60 solar | Planned AI data center + captive renewables concept | Planned | A for MoU, B/C for specific site / capacity until primary project page confirms | Keep 20 MW / 10 MW phase as press/company-claim notes; verify construction, permit, grid, and environmental record before operational count. |
| Orange / Medusa landing station | Bizerte | Bizerte | Cable landing station / connectivity | In service / connectivity asset | B/A depending operator source | Record as connectivity asset only, not DC. |

---

## 3. Governorate coverage strategy

### 3.1 National workflow

Run five passes for every governorate:

1. **Regulatory / legal pass**: INTT licences, SVA, decisions, annual reports; ANCS hosting-provider labelling if available.
2. **Public-sector pass**: MTC, CNI, ATI, CCK, ministry / university / AfDB / World Bank / AFD procurement pages.
3. **Operator pass**: Tunisie Telecom, Ooredoo, Orange, EO, ATI, CNI, local ISPs / hosters.
4. **Urbanism / energy pass**: commune / governorate portals, industrial zones, ANPE, STEG, ANME.
5. **Secondary confirmation pass**: DCD, WMC, THD, Tekiano, Agence Ecofin / We Are Tech, ilboursa, African Manager, La Presse; directories only as leads.

Universal governorate templates:

```text
"{governorate}" "centre de donnees"
"{governorate}" "centre de données"
"{governorate}" "data center"
"{governorate}" datacenter Tunisie
"{governorate}" "cloud" "hebergement"
"{governorate}" "cloud" "hébergement"
"{governorate}" "salle serveur"
"{governorate}" "salle informatique"
"{governorate}" "universite" "HPC"
"{governorate}" "centre de calcul"
"{governorate}" "Tunisie Telecom" "data center"
"{governorate}" "Ooredoo" "data center"
"{governorate}" "Orange" "data center"
"{governorate}" "STEG" "data center"
site:intt.tn "{governorate}"
site:mtc.gov.tn "{governorate}" "data center"
site:ati.tn "{governorate}" "hebergement"
```

### 3.2 Governorate matrix

| Governorate | Priority | Known / likely signals | Required checks |
|---|---:|---|---|
| Tunis | Very high | TT Carthage / Tunis DC, Ooredoo La Charguia 1, ATI DCs, CNI private cloud, CCK HPC, ministries, BCT / banks, hoster HQs. | Verify exact communes / addresses; distinguish facility from HQ and service. |
| Ariana | High | El Ghazala technopark, Topnet / ISP-hosting lead, Greater Tunis ICT estate. | Require current operator or permit evidence before counting. |
| Ben Arous | Medium | Greater Tunis industrial zones, Borj Cedria, bank / DR possibilities. | Search permits, industrial zones, banks, operators; likely sparse. |
| Manouba | Low-medium | Greater Tunis edge / institutional server rooms. | Negative checklist plus university / public tenders. |
| Nabeul | Medium | Cap Bon industrial / tourism ICT; active governorate pages. | Search governorate / commune / industrial-zone leads; likely no major DC. |
| Zaghouan | Low | Industrial zones and proximity to Tunis. | Negative checklist; watch backup / DR and utility projects. |
| Bizerte | Very high | Medusa landing, Orange landing station, SoleCrypt planned Bizerte AI DC corridor. | Do not count landing station as DC; verify SoleCrypt permit / construction / grid. |
| Beja | Low | Interior public-sector / telecom nodes. | Negative checklist. |
| Jendouba | Low | University / public server-room leads only. | Negative checklist. |
| Le Kef | Low | University / public server-room leads only. | Negative checklist. |
| Siliana | Low | Public / telecom local nodes. | Negative checklist. |
| Kairouan | Low | Interior institutional / university leads. | Negative checklist. |
| Kasserine | Low | Interior public-sector nodes. | Negative checklist. |
| Sidi Bouzid | Low-medium | 60 MW solar in broader renewables context from separate Scatec project; not a DC lead by itself. | Avoid confusing solar generation with DC location. |
| Sousse | Very high | Orange Kalaa Kebira DC; EO / Meninx Enfidha; Sousse technopole. | Confirm Enfidha and Kalaa Kebira localities; verify any technopole server rooms separately. |
| Monastir | Medium | Technopole / airport corridor, university / health IT. | Negative checklist; watch DR / hosting providers. |
| Mahdia | Low | University / public sector. | Negative checklist. |
| Sfax | High | Second economic city, Sfax technopole, universities; no confirmed major DC in opened sources. | Search deeply but mark negative if no named physical facility. |
| Gafsa | Low-medium | Mining / industrial systems, university. | Count only named institutional compute / server rooms. |
| Tozeur | High for energy, not DC | SoleCrypt / Tozeur T60 solar claim; Scatec 60 MW solar in Tozeur is separate energy context. | Record as energy asset only unless a DC site is named in Tozeur. |
| Kebili | Low | Southern / energy context. | Negative checklist. |
| Gabes | Low-medium | Industrial / port / chemical sector IT. | Negative checklist; watch internal industrial compute. |
| Medenine | Low-medium | Southern corridor / tourism / oil-gas support. | Negative checklist. |
| Tataouine | Low | Energy / oil-gas fields; sparse DC evidence. | Negative checklist. |

### 3.3 Negative-search standard

For a governorate with no obvious signal, do not mark `no_projects` until these have been checked:

```text
"{governorate}" "centre de donnees"
"{governorate}" "data center"
"{governorate}" datacenter
"{governorate}" "cloud"
"{governorate}" "hebergement"
"{governorate}" "colocation"
"{governorate}" "salle serveur"
"{governorate}" "universite" "centre de calcul"
"{governorate}" "Tunisie Telecom" "data center"
"{governorate}" "Ooredoo" "data center"
"{governorate}" "Orange" "data center"
site:mtc.gov.tn "{governorate}" "data center"
site:intt.tn "{governorate}"
site:datacentermap.com/tunisia "{governorate}"
```

Assign the facility to the governorate containing the physical commune / locality. Example: Enfidha is in Sousse governorate; La Charguia 1 is in Tunis governorate.

---

## 4. Data extraction rules

For every candidate, capture:

- governorate and exact commune / locality / technopark / industrial zone;
- facility name and aliases in French, English, and Arabic where useful;
- owner, operator, developer, public buyer, integrator, and legal entity;
- source route: INTT, MTC, ANCS, CNI, ATI, INPDP, TIA, permit, STEG / ANME, operator page, certificate, or press;
- stage: planned, MoU / study, tendered, awarded, under construction, inaugurated, operational, maintenance-only, inactive / decommissioned;
- evidence date and URL;
- capacity fields only when tied to the named data-center site;
- type: physical data center, telecom data center, commercial colo, sovereign cloud, government hosting, institutional HPC, DR site, server room, or cable landing station;
- confidence caveats, especially where a directory gives an address without operator confirmation.

Do **not** count:

- generic cloud / VPS / hosting pages with no physical facility evidence;
- office addresses from INTT, CNI, ATI, or directories as data-center addresses without facility support;
- telecom central offices, network POPs, or cable landing stations unless described as data centers;
- cybersecurity labs, call centers, training centers, and software platforms unless a physical DC / server room / HPC cluster is named;
- solar farms as data centers;
- university HPC / CCK records as commercial colocation;
- hyperscaler partner announcements as AWS / Azure / Google / OCI regions.
