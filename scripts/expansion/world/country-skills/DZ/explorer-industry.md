# DZ Explorer Industry - Algeria Datacenter Enumeration via Trade Press, Operator Pages, Colo Directories, and Wilaya Search Patterns

Date: 2026-08-12. Country: **DZ Algeria**. Scope: industry / press / vendor-led discovery for Algerian datacentres, with official verification routes for every lead. Reliability grades: **A** = official / primary source (operator page, ARPCE, ministry, BOMOP / ANEP, university, public-enterprise page, cloud provider page, Uptime record), **B** = strong secondary / trade press (DCD, APS via agency partners, Agence Ecofin / We Are Tech, Telecompaper, DC Magazine, Maghreb Emergent, El Watan when accessible, reputable vendor case study), **C** = weak lead (DataCenterMap, Baxtel, datacenters.com, Cloudscene, social media, generic market report, inaccessible snippets, directory-only address).

---

## 0. Algeria market frame

- Algeria's public data-center evidence is led by **government, telecom, university, and public-enterprise projects**, not by large international colo campuses. Commercial hosting exists, but public technical detail is sparse and many providers market cloud / hosting services without publishing facility-level specs.
- Highest-yield locations: **Alger / Mohammadia / Sidi Abdellah / Cheraga**, **Blida**, **Constantine**, **Oran**, **Ouargla / Hassi Messaoud**, **Tizi Ouzou**, **Djelfa**, and selected university / public-enterprise wilayas.
- Algeria sources mix spellings: `data center`, `datacenter`, `DataCenter`, `centre de donnees`, `centre national de donnees`, `centre de calcul`, `cloud souverain`, `hebergement`, `stockage`, `salle informatique`, `salle serveur`, `HPC`, `calcul intensif`.
- Treat directories as **lead indexes**. DataCenterMap, datacenters.com, Baxtel, and Cloudscene can expose facility names and addresses, but they often lack current status, source dates, and capacity proof. Raise a directory lead above C only when matched to an official operator / ARPCE / tender / press source.
- Cloud-provider pages are not facility sources for Algeria. AWS, Azure, Google Cloud, and OCI official region lists checked here do not show an Algeria public cloud region. Algeria's cloud story is currently sovereign / hosted cloud, telecom cloud, and government digital-services infrastructure.

Core national query set:

```text
Algeria ("data center" OR datacenter OR "data centre") ("Algiers" OR Oran OR Constantine OR Blida)
Algerie ("centre de donnees" OR "centre de calcul") ("Alger" OR Oran OR Constantine OR Blida)
"Algerie" "cloud souverain" "data center"
"Algerie" "centre national de donnees" Huawei
"Algerie Telecom" "data center" Constantine OR Lakhdaria
"Oran" "centre de calcul" "intelligence artificielle"
"Mohammadia" "Data Center National 1"
"Sidi Abdellah" "data center" hebergement
"Cheraga" "data center" ICOSNET
```

Arabic secondary checks:

```text
"الجزائر" "مركز البيانات"
"وهران" "مركز البيانات" "الذكاء الاصطناعي"
"قسنطينة" "اتصالات الجزائر" "مركز البيانات"
"المحمدية" "مركز البيانات الوطني"
```

---

## 1. High-signal trade and press sources

Use press to discover project names, dates, officials, integrators, and rough status. Then verify through an operator, ministry, ARPCE, BOMOP / ANEP, university, or power source.

| Source | URL / route | Use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD) | https://www.datacenterdynamics.com/en/news/ | Best global trade source for Algeria Telecom Constantine, Oran AI data center, parliament data center, Oman-Algeria data-center cooperation, and HCN/Huawei context. | B |
| APS / AMan Alliance | APS https://www.aps.dz/ and AMan Alliance APS mirror https://www.aman-alliance.org/Home/ContentDetail/100648 | Official / state-agency reporting for Mohammadia national DC Tier III Design certification and government digitalization milestones. | A/B depending host |
| Agence Ecofin / We Are Tech | https://www.wearetech.africa/ | Algeria digital-infrastructure coverage, including dual data-center infrastructure summaries and government digital services. | B |
| Telecompaper | https://www.telecompaper.com/ | Short telecom-regulatory / government approval leads, e.g. Huawei-built government data-center approval. | B |
| DC Magazine / DC Mag | https://dcmag.fr/ | French-language data-center industry coverage of Mohammadia / Huawei / Tier III and Algeria projects. | B |
| Maghreb Emergent / Algerie Eco / TSA / Algerie360 / El Watan / El Moudjahid | site-scoped searches | Local business and government-policy leads; useful for Oran, Blida, Ouargla, Mohammadia, national digital-services plan. Verify with official source. | B/C |
| Operator blogs / vendor case studies | Huawei, Schneider, Vertiv, ICE, AYRADE, ICOSNET, ISSAL, eBS/WebServices, Djezzy Cloud | Can identify integrator, site, and technical scope; often lacks exact capacity or public permit evidence. | A for operator service, B/C for facility detail |
| Directories | DataCenterMap, datacenters.com, Baxtel, Cloudscene, PeeringDB | Useful for Alger / Cheraga / Oran / Constantine facility names and addresses. Must be corroborated. | C unless corroborated |

Trade-press queries:

```text
site:datacenterdynamics.com/en/news/ Algeria "data center"
site:datacenterdynamics.com/en/news/ "Algeria Telecom" "Constantine"
site:datacenterdynamics.com/en/news/ Algeria Oran "AI data center"
site:datacenterdynamics.com/en/news/ Algeria Huawei "data center"
site:datacenterdynamics.com/en/news/ Algeria Oman "data centers"
site:wearetech.africa Algeria "data center"
site:telecompaper.com Algeria "data centre" Huawei
site:dcmag.fr Algerie "datacenter" Mohammadia
site:maghrebemergent.news "Mohammadia" "datacenter"
site:elwatan.dz "centre de donnees" "Ouargla"
site:elmoudjahid.dz "Data Center" "Mohammadia"
```

Status-language interpretation:

- `accord`, `partenariat`, `protocole`, `MoU`, `approuve`, `decision du conseil des ministres` = lead / planned. Verify site and stage.
- `appel d'offres`, `consultation`, `attribution`, `signature du contrat` = procurement. Stronger when BOMOP / ministry source is opened.
- `pose de la premiere pierre`, `lancement des travaux`, `construction` = construction lead. Verify with official visit / tender / contractor.
- `inaugure`, `mis en service`, `operationnel`, `obtient la certification`, `launched` = operational / commissioned signal. Verify with official operator / ministry / Uptime.
- `solution cloud`, `hebergement`, `VPS`, `bare metal`, `souverain cloud` = service evidence only unless physical data-center location is named.

---

## 2. Operator and vendor sweep

Official operator pages are **A for current marketed services and self-claimed facilities**. They are not always A for exact physical location or capacity unless the page publishes site details.

| Operator / provider | Main URL | Likely geography | Search / verification notes |
|---|---|---|---|
| Algerie Telecom | https://www.algerietelecom.dz/ | Constantine confirmed; Lakhdaria / Bouira historical plan; national business services | Official Constantine announcement is A. Search business posts cautiously because modular / containerized DC solutions may be customer products, not Algerie Telecom-owned sites. |
| High Commission for Digitalization / Huawei | HCN / APS / BOMOP / Huawei coverage | Mohammadia, Alger; Blida; possible DR site | Use HCN / APS / BOMOP before accepting directory or social claims. Huawei is integrator/vendor unless operator role is explicit. |
| Djezzy Cloud | https://www.djezzycloud.dz/english/ | Sovereign cloud; Bejaia / Amizour directory lead; telecom estate | Official page is A for service claim. Search ARPCE and Djezzy documents for facility location. |
| AYRADE | https://www.ayrade.com/ and ARPCE authorisation page https://www.ayrade.com/autorisation-general-hebergement-et-cloud/ | Sidi Abdellah / Alger directory lead; Algerian cloud host | AYRADE says it is ARPCE-authorized since 2024 under authorisation no. 01/RM/ARPCE/2024. Verify facility via operator page / DataCenterMap / ARPCE. |
| ICOSNET | https://www.icosnet.com.dz/ | Cheraga / Algiers and possible Oran private ISP / hosting | Search `Algiers DATA CENTER`, `Centre commercial El-Qods`, `Cheraga`, `Oran`, ARPCE FAI list. Directory-only locations are C until official page confirms. |
| ISSAL NET / Flex Cloud | https://issal.dz/ | Oran data-center directory lead | Operator markets FlexHosting / FlexCompute. Cloudscene says it operates its own data center; DataCenterMap lists an Oran address. Verify with official technical page / ARPCE. |
| eBS / WebServices | https://www.ebs.dz/ and https://webservices.dz/ | Sidi Abdellah Cyber Parc, Alger | eBS / WebServices page and DataCenterMap lead mention an 85 sqm data center; verify operator ownership and power figures before using capacity. |
| ADEXCLOUD | https://adexcloud.dz/data-center | Algeria-hosted data center, location not always specific | Official page describes data-center security, fire suppression, cooling, and 99.9% SLA; site location needs ARPCE / company / address corroboration. |
| Syntys Algeria | company / directory pages | Constantine lead at 33 Rue Belouizdad | Directory lead only unless operator page or ARPCE confirms. |
| MAHLIATOV | https://cloud.mahliatov.com/ | Annaba dedicated-server lead | Product page lists Annaba server inventory; count only as small hosting / server location unless facility details emerge. |
| Sonatrach | https://sonatrach.com/ | Ouargla / Hassi Messaoud / industrial telemetry | Official / university visit pages may mention production data center and telemetry center. Treat as internal industrial compute. |
| Sonelgaz / ELIT | https://www.sonelgaz.dz/ | Alger, Blida, Constantine, Oran platform context | Sonelgaz pages mention ELIT data centers; search ELIT and Sonelgaz subsidiaries for exact sites. |
| Algerie Poste | https://www.poste.dz/ | Alger HQ and regional postal complexes such as Tiaret | Usually institutional data centers / postal IT, not commercial colocation. |

Vendor / operator queries:

```text
"{operator}" "Algerie" "data center"
"{operator}" "Algerie" "centre de donnees"
"{operator}" "Algerie" "cloud" "ARPCE"
"{operator}" "autorisation" "ARPCE" "cloud"
"{operator}" "{wilaya}" "data center"
"{operator}" "{commune}" "hebergement"
"{operator}" "Tier III" "Algerie"
"{operator}" "Uptime Institute" "Algerie"
"{operator}" "groupe electrogene" "data center"
"{operator}" "onduleur" "centre de donnees"
```

Facility-address pivots:

```text
"Sidi Abdellah Cyber Parc" "data center"
"Centre des affaires Cyber Parc Sidi Abdellah" "AYRADE"
"Centre commercial El-Qods" "data center" ICOSNET
"Rue Belouizdad" Constantine "data center"
"Rue N 6" "Cite Jourdain" Oran "data center"
"Amizour" "Djezzy Cloud"
"Bekri Bouguerra" Mohammadia "data center"
```

---

## 3. Directory and aggregator handling

Directories are useful in Algeria because private operator pages are often sparse, but they are not enough for final high-confidence enumeration.

| Directory / lead source | What it can provide | Caveats |
|---|---|---|
| DataCenterMap Algeria: https://www.datacentermap.com/algeria/ | Lists Algeria markets and facilities; current snapshot shows Algiers, Oran, Cheraga, Constantine leads. | C by default. Addresses and capacities must be verified. May list inactive or unconfirmed facilities. |
| DataCenterMap facility pages | Facility names such as Huawei Mohammadia, WebServices Data Center, AYRADE DC 1, ICOSNET Algiers, APN Parliament Data Center, ISSAL NET Oran, Syntys Constantine. | Do not accept marketing specs without operator / official source. |
| datacenters.com Algeria: https://www.datacenters.com/locations/algeria | Provider/location index, including Djezzy Cloud / Bejaia-type leads. | C; sometimes sparse and quote-oriented. |
| Baxtel | Trade directory / news, e.g. Algeria Telecom Constantine summary. | B for news summary when sourced, C for directory data alone. |
| Cloudscene | Provider profile, e.g. ISSAL claims. | C/B-; verify with operator and ARPCE. |
| PeeringDB / IX records | Interconnection nodes and facility names. | Proves network presence only; not MW / construction status. |

Directory upgrade workflow:

1. Capture exact name, address, market, operator, and any capacity from directory.
2. Search exact name plus operator official domain.
3. Search ARPCE for legal entity and cloud / ISP authorisation.
4. Search BOMOP / ministry / urbanism / Uptime for site or operator.
5. If no primary support appears, keep as **C** and write a caveat.

Directory query templates:

```text
site:datacentermap.com/algeria "{operator}"
site:datacentermap.com/algeria "Algeria" "data center"
site:datacenters.com/locations/algeria "{operator}"
site:baxtel.com Algeria "data center"
site:cloudscene.com Algeria "{operator}"
site:peeringdb.com "{operator}" "Algeria"
```

---

## 4. Official verification routes for press/operator leads

Every industry lead should be checked against these primary routes:

| Route | URL | What to verify |
|---|---|---|
| ARPCE cloud / hosting authorisation | https://www.arpce.dz/fr/service/cloud | Legal authorisation for cloud hosting / storage; technical dossier requirements; operator status. |
| ARPCE ISP / other operator lists | https://www.arpce.dz/fr/service/fai and ARPCE service pages | Legal entity, address, ISP / telecom status, authorisation category. |
| MPT | https://www.mpt.gov.dz/ | Ministerial visits, foundation stones, telecom / Algerie Telecom / Algerie Poste data-center projects. |
| Algerie Telecom | https://www.algerietelecom.dz/ | Official facility announcements and business services. |
| BOMOP / ANEP | https://bomop.anep.dz/ | Public tenders and award notices for national, ministry, university, and wilaya data centers. |
| AAPI building permit workflow | https://aapi.dz/en/permis-de-construire-en/ | Investment one-stop-shop / urbanism routing for large private or industrial projects. |
| Ministry of Housing tenders | https://www.mhuv.gov.dz/?lang=fr&p=5167 | OPGI and ministry data-center maintenance / secondary-site evidence. |
| Sonelgaz / CREG | https://www.sonelgaz.dz/ and https://creg.gov.dz/en/home/ | Power / utility context, internal data centers, substations, concessions. |
| Uptime Institute awards / certificates | https://uptimeinstitute.com/uptime-institute-awards/ | Tier certification of named facilities such as Mohammadia. |
| Official cloud regions | AWS / Azure / Google / OCI official region pages | Confirm no Algeria public hyperscaler region before accepting cloud-region claims. |

Verification templates:

```text
site:arpce.dz "{operator}" "cloud"
site:arpce.dz "{operator}" "autorisation"
site:mpt.gov.dz "{project}" OR "{wilaya}" "data center"
site:bomop.anep.dz "{project}" OR "{operator}" "data center"
site:mhuv.gov.dz "{project}" OR "{wilaya}" "Data Center"
site:sonelgaz.dz "{project}" OR "{operator}" "data center"
site:uptimeinstitute.com "Algeria" "{facility}"
```

---

## 5. Wilaya-by-wilaya industry search matrix

Use the 58 wilaya names from `world-manifest.jsonl`. For each wilaya, run the universal templates with French, English, and at least one Arabic pass for high-priority locations.

### 5.1 Highest priority

| Wilaya | Localities / terms | Industry/operator seeds |
|---|---|---|
| **Alger** | Mohammadia, Sidi Abdellah, Cyber Parc, Cheraga, Dely Ibrahim, Bir Mourad Rais, El Harrach, APN | HCN / Huawei Mohammadia, WebServices / eBS, AYRADE, ICOSNET, ADEXCLOUD, APN Parliament DC, Algerie Poste HQ, ministry data centers, ARPCE operators. |
| **Blida** | Blida, Boufarik, Beni Mered, industrial zones | HCN / Huawei second national data center, Sonelgaz / ELIT platform leads, possible disaster-recovery / national services follow-up. |
| **Constantine** | Constantine city, Rue Belouizdad, regional telecom nodes | Algerie Telecom official data center, Syntys directory lead, Sonelgaz / ELIT, university / public tenders. |
| **Oran** | Akid Lotfi, Cite Jourdain, Hai Chouhada, Bir El Djir, Es Senia | MPT AI data center / centre de calcul IA, ISSAL NET / Flex Cloud, ICOSNET social / directory leads, Algerie Telecom, Sonelgaz / fiber. |
| **Ouargla** | Ouargla, Hassi Messaoud, Sonatrach Production Division, Kasdi Merbah University | Sonatrach data center and telemetry center, IMS Cloud report, oil/gas industrial compute, university / AI visits. |
| **Tizi Ouzou** | UMMTO, Hasnaoua, Tamda | UMMTO Data Center HPC/AI and private cloud official project. |
| **Djelfa** | OPGI Djelfa, ministry secondary data center | MHUv / OPGI Data Center secondaire, firewall and backup tenders. |
| **Bouira** | Lakhdaria, satellite hub | Algerie Telecom planned international-class DC lead from DCD / Ecofin; requires fresh official confirmation. |
| **Bejaia** | Amizour, Afra | Djezzy Cloud directory lead; verify with Djezzy official / ARPCE. |
| **Tiaret** | postal complex | MPT page says postal complex includes a data center; likely institutional. |

### 5.2 Medium priority institutional / industrial checks

| Wilaya | Search focus |
|---|---|
| Batna | University Batna-2 data center / HPC; search APS/local reports, university, MESRS. |
| Laghouat | University / ICE HPC computer-room references; verify with university / tender pages. |
| Guelma | University / ICE HPC project references; institutional only unless new source appears. |
| Khenchela | University Abbes Laghrour data-center acquisition / installation tenders; verify through official university or BOMOP. |
| Medea | University pole data center references; verify official university / MESRS page. |
| Annaba | MAHLIATOV dedicated server / hosting lead; port / university / industrial server-room checks. |
| Skikda | Port enterprise digitalization / centre de donnees newsletter lead; search port PDFs and tenders. |
| Setif | University / industrial / telecom edge searches; also operator POPs. |
| Tlemcen | University / telecom / border interconnection searches; low-to-medium. |
| Chlef | OPGI data-center and structure-interconnection tender lead; verify original tender if possible. |

### 5.3 Lower priority / negative-search wilayas

For Adrar, Oum el Bouaghi, Biskra, Bechar, Tamanrasset, Tebessa, Tiaret beyond postal complex, Jijel, Saida, Sidi Bel Abbes, Mostaganem, M'sila, Mascara, El Bayadh, Illizi, Bordj Bou Arreridj, Boumerdes, El Tarf, Tindouf, Tissemsilt, El Oued, Souk Ahras, Tipaza, Mila, Ain Defla, Naama, Ain Temouchent, Ghardaia, Relizane, Timimoun, Bordj Badji Mokhtar, Ouled Djellal, Beni Abbes, In Salah, In Guezzam, Touggourt, Djanet, El Meghaier, and El Meniaa:

- Search for `centre de donnees`, `data center`, `cloud`, `salle serveur`, `universite HPC`, `Algerie Telecom`, `Sonelgaz`, `OPGI`, `port`, `zone industrielle`, and `BOMOP`.
- Do not over-count generic ICT training centers, call centers, cybersecurity labs, or university websites unless the text identifies a physical data center / server room / HPC facility.
- New wilayas created from older parent wilayas need locality checks. For example, a result under old `Ouargla` may physically be in current Touggourt or El Meniaa only if the commune supports it.

Universal wilaya query set:

```text
"{wilaya}" "centre de donnees" Algerie
"{wilaya}" "data center" Algeria
"{wilaya}" datacenter Algerie
"{wilaya}" "cloud souverain"
"{wilaya}" "hebergement web" "data center"
"{wilaya}" "salle serveur" "appel d'offres"
"{wilaya}" "salle informatique" "onduleur"
"{wilaya}" "universite" "HPC"
"{wilaya}" "centre de calcul"
"{wilaya}" "OPGI" "data center"
"{wilaya}" "Algerie Telecom" "data center"
"{wilaya}" "Sonelgaz" "data center"
site:datacenterdynamics.com/en/news/ Algeria "{wilaya}"
site:wearetech.africa Algeria "{wilaya}" "data center"
site:datacentermap.com/algeria "{wilaya}"
site:bomop.anep.dz "{wilaya}" "centre de donnees"
```

---

## 6. Candidate handling examples

Use these examples as calibration for future enumeration:

- **Algerie Telecom Constantine Data Center**: official Algerie Telecom announcement is **A**; DCD / Baxtel are **B** corroboration. Stage operational; capacity null unless official MW / kVA appears.
- **Mohammadia National Data Center / Data Center National 1**: APS / AMan + HCN / Uptime + BOMOP / Huawei context gives **A** for facility existence and certification; directories can add address clues but should not override official data.
- **Blida national digital services data center**: HCN-Huawei agreement and BOMOP references are **A/B** for planned / works context; do not mark operational without commissioning or certification source.
- **Oran AI data center / advanced data center**: MPT page is **A** for foundation stone and wilaya; DCD / DzairAI are **B**. Stage construction unless later official inauguration appears.
- **AYRADE DC 1 / TASSILI**: AYRADE ARPCE authorisation page is **A** for cloud authorisation; DataCenterMap is **C** for facility address until official facility page confirms.
- **ISSAL NET Oran**: ISSAL official page is **A** for service; Cloudscene / DataCenterMap are **C/B-** for own-DC / address claims until official facility proof is found.
- **Djezzy Cloud Amizour / Bejaia**: Djezzy Cloud official page is **A** for sovereign cloud service; datacenters.com location is **C** for Amizour facility unless Djezzy / ARPCE / permit confirms.
- **University / OPGI data centers**: count as institutional data centers when official tender / university page says `data center`, `Data Center HPC/AI`, or `salle informatique (datacenter)`. Do not compare them to commercial colo campuses.

---

## 7. Output discipline

For each final project record:

- Prefer French project names from official sources; include English alias if trade press uses one.
- Normalize wilaya to the manifest name, but keep exact commune / locality in notes.
- Put capacity in `capacity_mw` only when the source gives MW / IT load for that exact facility. For kVA / MVA / generators / sqm / racks, record in notes unless schema supports separate fields.
- Use `evidence_grade=A` only when the source is official / primary for the fact being claimed.
- Mark `no_projects` only after checking official / industry / operator / tender terms and after excluding national projects physically located elsewhere.

