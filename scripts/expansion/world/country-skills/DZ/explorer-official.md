# DZ Explorer Official - Algeria Datacenter Enumeration via ARPCE, Ministries, Tenders, Urbanism, Energy, and Official Operators

Date: 2026-08-12. Country: **DZ Algeria**. Division model: **58 wilayas**. Angle: **official / regulatory / public-procurement / cloud-authorisation pipeline** for enumerating operational, under-construction, planned, and institutional data-center facilities.

Reliability grades:
- **A** = official / primary source: ARPCE authorisation or operator list, ministry / wilaya / commune / university / public-enterprise page, BOMOP / ANEP tender, official public procurement page, AAPI / urbanism procedure, Sonelgaz / CREG evidence, official cloud-region page, official operator facility page, Uptime certification record.
- **B** = strong secondary source: APS carried by an official agency partner, DCD, Agence Ecofin / We Are Tech, Telecompaper, reputable Algerian national press, vendor / integrator project page with named client and site.
- **C** = weak lead: tender aggregators, DataCenterMap / Baxtel / datacenters.com, social posts, market reports, inaccessible snippets, directory pages, unverified local press.

---

## 0. Algeria-specific structural facts

- Algeria has **no single public national data-center register** and no complete public planning-permit search equivalent to a US county database. Enumeration works by joining **ARPCE service authorisations**, **ministry / public-enterprise announcements**, **BOMOP / ANEP public tenders**, **AAPI / APC / wilaya urbanism routes**, **Sonelgaz / CREG power context**, and **operator pages**.
- The most productive official language is **French**. Arabic is useful for APS, ministry reposts, wilaya pages, and local press. English is useful for DCD, cloud-provider pages, and vendor pages. Search all variants: `data center`, `datacenter`, `centre de donnees`, `centre national de donnees`, `centre de calcul`, `cloud`, `hebergement`, `stockage`, `salle informatique`, `salle serveur`, `cloud computing`.
- Algeria's largest public-sector data-center activity is **state-led**: High Commission for Digitalization / Huawei national digital services centers, Ministry of Post and Telecommunications projects, Algerie Telecom facilities, Algerie Poste, ministry / OPGI secondary data centers, university HPC / cloud projects, and Sonatrach / Sonelgaz internal data centers.
- Commercial colocation is thinner and concentrated around **Alger / Cheraga / Sidi Abdellah**, **Oran**, **Constantine**, and some operator / mobile-cloud leads in **Bejaia** and **Ouargla**. Treat most other wilaya searches as negative unless a public entity, university, port, oil/gas operator, cyberpark, call center, or telecom operator appears.
- Cloud-provider global-region pages are **A for absence / presence of a named public cloud region**, but Algeria currently appears as a **local sovereign / hosted-cloud market**, not a hyperscaler public cloud region market. Use AWS / Azure / Google / OCI official lists to avoid falsely converting edge or partner services into physical cloud regions.

Core French and English vocabulary:

```text
centre de donnees
centre national de donnees
centre de donnees national
data center
datacenter
centre de calcul
centre de calcul IA
calcul intensif
HPC
cloud national
cloud souverain
cloud computing
hebergement et stockage
hebergement web
colocation
co-location
salle informatique
salle serveur
salle blanche
onduleur / UPS
groupe electrogene
climatisation de precision
poste electrique
transformateur
fibre optique
permis de construire
certificat de conformite
actes d'urbanisme
appel d'offres
BOMOP
ANEP
consultation nationale
```

Useful Arabic terms for secondary checks:

```text
مركز البيانات
مركز معطيات
مركز وطني للبيانات
مركز حساب
الحوسبة السحابية
استضافة
الألياف البصرية
رخصة البناء
سونلغاز
اتصالات الجزائر
```

---

## 1. Grade A official / regulatory routes

### 1.1 ARPCE - telecom and cloud authorisation

Primary source: **Autorite de regulation de la poste et des communications electroniques (ARPCE)**, https://www.arpce.dz/.

High-value pages:

- Cloud / hosting authorisation service: https://www.arpce.dz/fr/service/cloud and English page https://www.arpce.dz/en/service/cloud
- ISP service operator list: https://www.arpce.dz/fr/service/fai
- Audiotex / service lists sometimes expose data-center legal names: https://www.arpce.dz/fr/service/audiotex
- ARPCE news / notices: https://www.arpce.dz/fr/news
- ARPCE regulation files / cahier des charges PDFs under `https://www.arpce.dz/fr/file/...`

Why it matters:

- ARPCE is the main official route for **hosting and storage in cloud computing** authorisations. Its cloud service page describes the technical file required for authorisation, including detailed service description, infrastructure architecture, connection mode, equipment type, storage capacity, backup capacity, and data-security systems.
- ARPCE records are **operator/service evidence**, not automatically facility evidence. A legal entity may offer cloud using its own facility, leased space, or partner infrastructure. Use ARPCE to discover legal names, then pivot to facility, permit, power, and operator-page evidence.
- ARPCE notices can also show withdrawals / sanctions / list changes. A withdrawn authorisation should not be used as current operational evidence without later renewal.

ARPCE query templates:

```text
site:arpce.dz "hebergement et stockage" "cloud computing"
site:arpce.dz "Hébergement et Stockage en Cloud Computing"
site:arpce.dz "centre de donnees"
site:arpce.dz "data center"
site:arpce.dz "{operator}" "cloud"
site:arpce.dz "{operator}" "autorisation"
site:arpce.dz "{operator}" "hebergement"
site:arpce.dz "Liste des Operateurs" "cloud"
site:arpce.dz "retrait definitif" "cloud computing"
```

Operator names to search in ARPCE and its PDFs: `Algerie Telecom`, `Mobilis`, `Djezzy`, `Ooredoo`, `ICOSNET`, `AYRADE`, `ISSAL`, `eBS`, `WebServices`, `ADEXCLOUD`, `Djezzy Cloud`, `Beyte Datacenters`, `Syntys`, `MAHLIATOV`, `TDA`, `Connexis`, `BringCom Algerie`, `Airband`.

Extract: legal name, authorisation number, service class, address, decision date, whether the company is an ISP / cloud host / call-center provider / postal provider, and any disclosed storage, backup, security, or network architecture.

### 1.2 Ministry of Post and Telecommunications / national digital infrastructure

Primary source: **Ministere de la Poste et des Telecommunications**, https://www.mpt.gov.dz/.

High-value routes:

- MPT news and project pages for `centre de donnees`, `data center`, `centre de calcul`, `IA`, `fibre optique`, `Algerie Telecom`, `Oran`, `Ouargla`, `Tiaret`, `Algerie Poste`.
- Example official page: MPT Oran visit, https://www.mpt.gov.dz/visite-de-travail-a-oran-renforcer-linfrastructure-numerique-et-soutenir-leconomie-numerique/, which states that the minister laid the foundation stone for an advanced data center and AI computing center in Oran.
- Example official page: Algerie Poste / postal complex visit, https://www.mpt.gov.dz/commemoration-de-la-journee-mondiale-de-la-poste/, which mentions the Algerie Poste data center at its general management headquarters.
- Example official page: Tiaret visit, https://www.mpt.gov.dz/visite-de-travail-et-dinspection-a-la-wilaya-de-tiaret/, which mentions a postal complex with a data center.

MPT query templates:

```text
site:mpt.gov.dz "centre de donnees"
site:mpt.gov.dz "data center"
site:mpt.gov.dz "centre de calcul"
site:mpt.gov.dz "intelligence artificielle" "centre de donnees"
site:mpt.gov.dz "Algerie Telecom" "data center"
site:mpt.gov.dz "{wilaya}" "centre de donnees"
site:mpt.gov.dz "{wilaya}" "fibre optique" "data center"
site:mpt.gov.dz "Algerie Poste" "centre de donnees"
```

Grade **A** for the project fact and wilaya when an MPT page names the facility / visit / work. Capacity is usually absent; leave `capacity_mw` null unless an official source provides MW / kVA / MVA.

### 1.3 High Commission for Digitalization / national digital services centers

Primary route: **Haut-Commissariat a la Numerisation (HCN)** and official government / APS coverage. Search official HCN domains if available, plus APS and BOMOP / ANEP.

Known official / strong sources:

- APS / AMan Alliance: https://www.aman-alliance.org/Home/ContentDetail/100648 reports Algeria's first national data center in Mohammadia, Algiers, received Uptime Institute Tier III Design certification.
- APS page: https://www.aps.dz/fr/algerie/education-et-technologie/mlxxic0p-le-premier-data-center-national-obtient-une-certification-refletant-sa-maturite-technique-et-son-operationnalite
- HCN-Huawei agreement repost with locations: https://webservices.dz/faq-ssl/219-signature-dun-accord-entre-le-haut-commissariat-a-la-numerisation-et-huawei-consortium states the first national data center is in Mohammadia, Alger, and the second in Blida.
- BOMOP / ANEP tender page: https://bomop.anep.dz/representation-et-assistance-au-maitre-douvrage-pour-le-suivi-le-controle-et-la-valisation-des-livrables-et-des-travaux-de-realisation-it-et-data-center-facilites-dcf-du-centre-de-donnees-natio/ references owner's-assistance for IT and Data Center Facilities works for the national digital services data center.
- DZtenders lead for HCN disaster-recovery data center: https://www.dztenders.com/fr/archive/509473/etude-realisation-equipement-et-mise-en-service-dun-centre-de-donnees-national-de-reprise-dactivite-apres-sinistre-dr-en-02-lots/

Queries:

```text
"Haut Commissariat a la Numerisation" "centre de donnees"
"Haut-Commissariat a la Numerisation" "data center"
"HCN" "centre de donnees national" "Algerie"
"Mohammadia" "Data Center National 1"
"Blida" "centre de donnees national" "Huawei"
site:aps.dz "data center national" "Mohammadia"
site:aps.dz "centre de donnees national" "Blida"
site:bomop.anep.dz "centre de donnees national"
site:bomop.anep.dz "data center facilites"
```

Handling:

- Count **Mohammadia / Alger** as a separate national data center when official / APS / Uptime evidence identifies it.
- Count **Blida** as planned / under development only when tender, HCN, or official government evidence names the Blida site.
- If new DR / reprise d'activite national data-center tenders do not name the wilaya, keep them as national leads until a site is disclosed.

### 1.4 Algerie Telecom and public telecom operators

Primary source: **Algerie Telecom**, https://www.algerietelecom.dz/.

Known official source:

- Constantine data center official announcement: https://www.algerietelecom.dz/en/espace-presse/algeria-telecom-inaugurates-a-new-data-center-art2528 and French version https://www.algerietelecom.dz/fr/espace-presse/algerie-telecom-inaugure-son-data-center-art2528. It states Algerie Telecom inaugurated a new data center in Constantine on 2023-02-23, with a cloud platform to collect, process, and store company / enterprise data.

Use Algerie Telecom as both:

- **A-grade operator evidence** when its pages identify a facility / service.
- **lead source** for modular, containerized, and managed data-center solutions; these posts may describe services rather than fixed facilities.

Queries:

```text
site:algerietelecom.dz "data center"
site:algerietelecom.dz "centre de donnees"
site:algerietelecom.dz "cloud" "Constantine"
site:algerietelecom.dz "{wilaya}" "data center"
"Algerie Telecom" "Lakhdaria" "centre de donnees"
"Algerie Telecom" "Bouira" "data center"
"Algerie Telecom Business" "Data Center Solutions"
```

Other official telecom operator pivots:

- **Djezzy Cloud**: https://www.djezzycloud.dz/english/ describes Djezzy Cloud as a sovereign cloud platform. Use as A for service claim, B/C for facility location until an official facility page or permit confirms the physical data center.
- **Mobilis / Ooredoo**: search official pages and ARPCE authorisations for data-center, cloud, and hosting services; most public records will be telecom-service evidence, not facility evidence.

### 1.5 Public procurement: BOMOP, ANEP, ministry tenders, universities, and public entities

Official / semi-official procurement is often the best way to find Algeria's small institutional data centers, server rooms, HPC rooms, disaster-recovery sites, and data-center equipment projects.

Primary routes:

- **BOMOP / ANEP**: https://bomop.anep.dz/
- **MPT tender pages**: https://www.mpt.gov.dz/
- **Ministry of Housing tender page**: https://www.mhuv.gov.dz/?lang=fr&p=5167
- **Ministry of Defence tender page**: https://www.mdn.dz/site_principal/sommaire/appels/appels_fr.php
- University tender pages, e.g. UMMTO Tizi Ouzou official tender: https://www.ummto.dz/avis-dappel-doffres-national-ouvert-avec-exigence-de-capacites-minimales-n-01-ummto-vrdpo-2024/

Examples to model:

- MHUv official tender page lists `Acquisition, installation et configuration de deux firewalls au Data Center secondaire sis a l'OPGI de Djelfa` and Veeam renewals for the ministry data center. Grade **A** for the Djelfa secondary data-center existence.
- UMMTO Tizi Ouzou official material covers a `Data Center HPC/AI et Cloud Prive` acquisition / installation and later official visit to future data-center premises.
- Ministry of Defence tenders include `amenagement de l'environnement technique d'un centre de donnees sis a Alger`; treat site as Alger if the official page gives `sis a Alger`.

Procurement queries:

```text
site:bomop.anep.dz "data center"
site:bomop.anep.dz "datacenter"
site:bomop.anep.dz "centre de donnees"
site:bomop.anep.dz "salle informatique"
site:bomop.anep.dz "salle serveur"
site:bomop.anep.dz "cloud prive"
site:bomop.anep.dz "{wilaya}" "data center"
site:mhuv.gov.dz "Data Center"
site:mhuv.gov.dz "OPGI" "Data Center"
site:mdn.dz "centre de donnees"
site:{university-domain} "data center"
site:{university-domain} "centre de donnees"
site:{university-domain} "HPC" "cloud"
```

Tender aggregators such as DZtenders, Algerie Marches, AlgeriaTenders, RhinoTenders, and DzairTenders are **C leads** unless the original public buyer document is opened. They are still useful because BOMOP pages may be access-limited.

Extract: buyer, wilaya, site wording (`sis a`), object, lot numbers, tender / consultation number, ANEP number, award date, contractor, whether it is a new build, equipment acquisition, maintenance, firewall / Veeam / UPS renewal, or simple server-room work.

### 1.6 Urbanism, building permits, and investment one-stop shop

Primary routes:

- **AAPI building permit application file**: https://aapi.dz/en/permis-de-construire-en/
- **Ministry of Interior downloadable forms**: https://interieur.gov.dz/formulaires-telechargeables/
- **Ministry of Housing / Urbanism services**: https://www.mhuv.gov.dz/?lang=fr&page_id=5458
- Commune / APC and wilaya urbanism pages where available.

Practical reality:

- Algeria's building-permit evidence is usually **not openly searchable by project**, especially for private projects. Use AAPI and ministry pages to understand the route, then search commune / wilaya / local press / tender documents for named projects.
- AAPI says building-permit applicants should contact the urban-planning representative at the AAPI one-stop shop. This is useful for investment-zone / large commercial project routing.
- Ministry of Interior forms include `Demande de permis de construire`, `permis de lotir`, and `permis de demolir`; these prove the administrative workflow, not a facility.

Urbanism queries:

```text
"{operator}" "{wilaya}" "permis de construire"
"{operator}" "{commune}" "permis de construire"
"{project}" "permis de construire"
"{project}" "certificat de conformite"
"{project}" "actes d'urbanisme"
"{project}" "AAPI" "data center"
"{project}" "APC" "centre de donnees"
site:{wilaya-domain} "centre de donnees"
site:{wilaya-domain} "data center"
site:{commune-domain} "permis de construire" "data center"
```

Extract: commune, wilaya, investor / proponent, land parcel if present, zone / cyberpark / industrial estate, permit or conformity certificate number, floorspace, generator / HVAC / fire-suppression clues, utility connection, and stage.

### 1.7 Energy and grid evidence: Sonelgaz / CREG / ELIT

Primary routes:

- **Sonelgaz**: https://www.sonelgaz.dz/
- **CREG**: https://creg.gov.dz/en/home/ and electricity / gas distribution page https://creg.gov.dz/en/electricity-and-gas-distribution/
- **Ministry of Energy / renewable-energy pages** when a project claims captive solar or large grid connection.

How to use:

- Sonelgaz / CREG are usually **context and utility-confirmation sources**, not data-center registries.
- CREG states electricity and gas distribution is subject to the concession regime under Law No. 02-01. Use CREG for regulatory context, concessions, tariffs, and grid-market structure.
- Sonelgaz pages can identify internal data centers and ELIT-hosted platforms. Example: Sonelgaz customer-contact-center material says the platform is centralized at ELIT data centers and has call platforms in Alger, Constantine, Blida, and Oran.
- For MW-scale projects, search for substations, transformers, connection capacity, backup generators, diesel storage, and renewable energy around the named site.

Energy queries:

```text
site:sonelgaz.dz "data center"
site:sonelgaz.dz "Data Centers d'ELIT"
site:sonelgaz.dz "centre de donnees"
site:sonelgaz.dz "{operator}" "MW"
site:sonelgaz.dz "{wilaya}" "poste electrique" "data center"
site:creg.gov.dz "data center"
site:creg.gov.dz "centre de donnees"
"{project}" "Sonelgaz" "data center"
"{project}" "poste electrique"
"{project}" "transformateur" "centre de donnees"
"{project}" "groupe electrogene" "data center"
"{project}" "MVA" "Algerie"
```

Do not convert national electricity statistics into facility capacity. Record kVA / MVA / MW only when tied to a named data-center site.

### 1.8 Official public cloud region pages

Use these official pages to prevent false positives:

| Provider | Official source | Algeria signal | Enumeration use |
|---|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ and docs https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | No Algeria public AWS region shown in official region list checked here. | Search only for edge / partner / customer leads; do not count as physical AWS region. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list and https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies | No Algeria Azure public region found in official region list checked here. | Use as absence evidence; search local Microsoft partner / sovereign-cloud references separately. |
| Google Cloud | https://cloud.google.com/about/locations and https://docs.cloud.google.com/compute/docs/regions-zones | No Algeria GCP region found in official locations checked here. | Use only for partner / customer / edge leads. |
| Oracle OCI | https://www.oracle.com/cloud/public-cloud-regions/ and https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | No Algeria OCI public region found in official region list checked here. | Use only for partner / customer leads. |
| Huawei / Huawei Cloud Stack | https://e.huawei.com/en/solutions/data-center and Huawei Algeria / HCN project coverage | Huawei is a vendor / integrator for national data-center projects, not necessarily a public Huawei Cloud region. | Verify through HCN / ministry / BOMOP / APS before counting physical sites. |

---

## 2. Official operator / public-sector seed list

| Operator / entity | Official source | Algeria footprint signal | Follow-up |
|---|---|---|---|
| High Commission for Digitalization / Huawei consortium | APS / HCN / BOMOP / Huawei-related government coverage | Mohammadia national data center in Alger; second national data center in Blida; possible DR center tenders | Verify HCN / APS / BOMOP / Uptime; assign wilaya only when site named. |
| Algerie Telecom | https://www.algerietelecom.dz/ | Official Constantine data center inaugurated 2023-02-23; possible Lakhdaria / Bouira historical plan; business data-center services | Search official site, MPT, DCD, Ecofin, ARPCE, Sonelgaz. |
| Algerie Poste | https://www.poste.dz/ plus MPT posts | Data center at general management headquarters; postal complexes may include data-center components | Search MPT / Algerie Poste / tenders; distinguish small postal IT rooms from commercial DC. |
| Ministry of Housing / OPGI | https://www.mhuv.gov.dz/ | Official secondary data center at OPGI Djelfa; primary ministry data center implied by maintenance / Veeam / firewall tenders | Use MHUv tender page and OPGI wilaya terms. |
| Universities / MESRS | university domains and ministry pages | Tizi Ouzou UMMTO Data Center HPC/AI; Batna-2 HPC; Laghouat / Guelma / Khenchela and other institutional projects | Count as institutional compute/data-center only, not commercial colo. |
| Sonatrach / oil-gas entities | https://sonatrach.com/ and university / official visit pages | Industrial telemetry / production data centers, especially Ouargla / Hassi Messaoud corridor | Search official Sonatrach, universities, tenders, and wilaya pages. |
| Sonelgaz / ELIT | https://www.sonelgaz.dz/ | ELIT data centers supporting centralized platforms; call platforms in Alger, Constantine, Blida, Oran | Use as internal enterprise DC evidence unless commercial service is shown. |
| Djezzy Cloud / Mobilis / Ooredoo | official sites + ARPCE | Sovereign cloud / telecom hosting leads; possible Bejaia / Algiers / Oran facilities | Require official facility page, ARPCE authorisation, or permit before precise site count. |
| AYRADE, ICOSNET, ISSAL, eBS/WebServices, ADEXCLOUD | operator pages + ARPCE + directories | Commercial cloud / hosting providers mainly in Alger / Cheraga / Sidi Abdellah / Oran | Operator page is A for service; facility details need corroboration. |

---

## 3. Wilaya enumeration strategy

### 3.1 National workflow for each wilaya

Run five passes:

1. **Official telecom/cloud pass**: ARPCE + Algerie Telecom + MPT + operator name.
2. **Public procurement pass**: BOMOP / ANEP + ministry / university / wilaya / commune tender pages.
3. **Urbanism pass**: AAPI / APC / wilaya / commune searches for permits and conformity certificates around named projects.
4. **Energy pass**: Sonelgaz / CREG / substation / generator / UPS terms around named site.
5. **Operator and trade-confirmation pass**: official operator pages first; DCD / APS / Ecofin / We Are Tech / directories only as leads.

Universal wilaya templates:

```text
"{wilaya}" "centre de donnees"
"{wilaya}" "data center"
"{wilaya}" datacenter
"{wilaya}" "centre de calcul"
"{wilaya}" "cloud" "hebergement"
"{wilaya}" "salle informatique" "onduleur"
"{wilaya}" "salle serveur" "appel d'offres"
"{wilaya}" "HPC" "universite"
"{wilaya}" "Algerie Telecom" "data center"
"{wilaya}" "Sonelgaz" "data center"
"{wilaya}" "OPGI" "Data Center"
site:bomop.anep.dz "{wilaya}" "data center"
site:bomop.anep.dz "{wilaya}" "centre de donnees"
site:arpce.dz "{wilaya}" "cloud"
site:mpt.gov.dz "{wilaya}" "centre de donnees"
site:aps.dz "{wilaya}" "data center"
```

Arabic secondary templates:

```text
"{wilaya_ar}" "مركز البيانات"
"{wilaya_ar}" "مركز معطيات"
"{wilaya_ar}" "مركز حساب" "الذكاء الاصطناعي"
"{wilaya_ar}" "رخصة البناء" "مركز البيانات"
```

### 3.2 Priority wilaya clusters

| Wilaya / cluster | Why high priority | Official query notes |
|---|---|---|
| **Alger** | National government, Mohammadia national DC, Sidi Abdellah Cyber Parc, ministries, APN, private cloud hosts, telecom HQs | Search `Mohammadia`, `Sidi Abdellah`, `Cyber Parc`, `Cheraga`, `Bir Mourad Rais`, `Dely Ibrahim`, `APN`, `ministere`, `Huawei`, `HCN`, `WebServices`, `AYRADE`, `ICOSNET`, `ADEXCLOUD`, `Algerie Poste`. |
| **Blida** | Second national digital-services data center and Sonelgaz / ELIT / platform leads | Search `Blida` + `HCN`, `Huawei`, `centre de donnees national`, `Data Center Facilities`, `Sonelgaz`, `ELIT`. |
| **Constantine** | Official Algerie Telecom data center; Sonelgaz / regional platform leads | Search Algerie Telecom official announcement, `Syntys`, `33 Rue Belouizdad`, `ELIT`, `Cloud`, university / public tenders. |
| **Oran** | MPT official AI data center / advanced data center foundation stone; ISSAL NET / ICOSNET / regional telecom activity | Search `Akid Lotfi`, `centre de calcul IA`, `ISSAL`, `Algerie Telecom`, MPT Oran visit, Sonelgaz / fiber completion. |
| **Bouira / Lakhdaria** | Historical Algerie Telecom international-class data-center plan near satellite hub | Search `Lakhdaria`, `centre satellitaire`, `Algerie Telecom`, `Bouira`, Ecofin / DCD follow-up. Treat as planned unless official commissioning found. |
| **Ouargla / Hassi Messaoud corridor** | Oil/gas compute, Sonatrach data center / telemetry center, IMS Cloud report, new-town logistics projects | Search `Sonatrach`, `Division Production`, `Hassi Messaoud`, `IMS Cloud`, `Kasdi Merbah`, `telemetrie`, `centre de donnees`, MHUv logistics tenders. |
| **Tizi Ouzou** | UMMTO official Data Center HPC/AI and private cloud tender / works | Search UMMTO official pages, `Data Center HPC/AI`, `Cloud Prive`, ministry visit. |
| **Djelfa** | Ministry of Housing secondary data center at OPGI Djelfa | Search MHUv tenders, `OPGI Djelfa`, `Data Center secondaire`, `firewall`, `Veeam`. |
| **Tiaret** | MPT official postal complex includes data center | Search MPT Tiaret visit, `complexe postal`, `data center`, Algerie Poste. |
| **Bejaia** | Djezzy Cloud / Amizour directory lead; mobile / sovereign cloud angle | Search Djezzy Cloud official, ARPCE, `Amizour`, `Afra`, Bejaia telecom infrastructure. |
| **Annaba / Skikda** | Port / hosting / industrial leads; weaker evidence but strategic ports | Search port enterprise PDFs, `MAHLIATOV`, `port`, `data center`, `numerisation`, `server room`. |
| **Batna, Laghouat, Guelma, Khenchela, Medea** | University / institutional HPC and data-center leads | Search university pages, MESRS, procurement, `HPC`, `calcul intensif`, `salle informatique`, `data center`. |

### 3.3 Lower-yield wilaya handling

For wilayas without obvious telecom / university / oil-gas / government data-center leads, run a negative-search checklist and record `no_projects` only after checking:

```text
"{wilaya}" "centre de donnees"
"{wilaya}" "data center"
"{wilaya}" "datacenter"
"{wilaya}" "cloud"
"{wilaya}" "hebergement"
"{wilaya}" "salle serveur"
"{wilaya}" "universite" "HPC"
"{wilaya}" "Algerie Telecom" "cloud"
"{wilaya}" "Sonelgaz" "Data Centers d'ELIT"
site:bomop.anep.dz "{wilaya}" "data center"
site:mpt.gov.dz "{wilaya}" "data center"
site:aps.dz "{wilaya}" "centre de donnees"
```

Be careful with new 2019 wilayas such as Timimoun, Bordj Badji Mokhtar, Ouled Djellal, Beni Abbes, In Salah, In Guezzam, Touggourt, Djanet, El Meghaier, and El Meniaa. Searches may return records under the former parent wilaya. Assign a facility to the current wilaya only when the physical commune / locality supports it.

---

## 4. Data extraction rules

For every candidate, capture:

- wilaya and commune / locality / cyberpark / industrial zone;
- facility name and alternate names in French / English / Arabic;
- developer / owner / operator / public buyer / integrator;
- legal source: ARPCE authorisation, tender number, ministry announcement, permit, official operator page, Uptime record;
- project stage: planned, tendered, awarded, under construction, inaugurated, operational, maintenance-only, decommissioned / inactive;
- evidence date and source URL;
- capacity fields: MW / MVA / kVA / generators / racks / sqm only when explicitly tied to that site;
- whether the record is a physical data center, cloud service, server room, HPC cluster, telemetry center, disaster-recovery site, or call-center platform;
- confidence caveats, especially when an aggregator gives an address but no operator page confirms it.

Do **not** count:

- generic `cloud` service pages with no physical facility evidence;
- call centers unless the source says they run on or include a data center;
- office addresses from ARPCE as data-center addresses without facility support;
- UPS / firewall / software renewal tenders unless they name a data center or server room;
- national cloud-region absence / presence as a physical facility address.

