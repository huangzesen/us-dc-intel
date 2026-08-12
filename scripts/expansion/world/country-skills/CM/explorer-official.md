# CM Explorer Official -- Cameroon Datacenter Enumeration

Date: 2026-08-12. Country: **CM / Cameroon**. Scope: official, regulatory and primary-source methodology for enumerating commercial, telco, sovereign, institutional and edge data-centre facilities. Administrative coverage model: **10 regions**: Adamaoua; Centre; Far North (Extreme-Nord); East (Est); Littoral; North (Nord); North-West (Nord-Ouest); West (Ouest); South (Sud); South-West (Sud-Ouest).

## Reliability Grades

- **A** -- primary evidence naming a facility, project, licence, permit, certification or site: ministry/regulator pages (MINPOSTEL, ART, ANTIC, CENADI, MINHDU, MINEE, MINEPDED), official operator pages (Camtel, Orange Business Cameroun, ST Digital, MTN, CAMPOST), Uptime Institute award records, PeeringDB facility records, public procurement records, company registry/RCCM records, environmental filings, power/grid filings.
- **B** -- reputable trade or local press with named site/status: Data Center Dynamics, Capacity Media, Connecting Africa, The Tech Capital, Agence Ecofin, Business in Cameroon, Investir au Cameroun, EcoMatin, Cameroon Tribune, CRTV, Journal du Cameroun, CIO Mag, IT News Africa, TechAfrica News, CEMAC Eco Finance, Digital Business Africa, The Guardian Post Cameroon, Afrik.com, Actu Cameroun, Bougna, Le Big Data.
- **C** -- lead only: generic directories and SEO pages (Datacenter Map, Baxtel, OCOLO, Datacenters.com, Data Center Platform, HostDir, WHtop, DCHub, Colomap), LinkedIn/social posts, reseller claims, market reports, unsourced MW/rack tables, MoUs without named site/status.

Grade each fact separately. A page can be A for existence but C for an uncited MW/rack value. Uptime "Tier III Certification of Design Documents" is **not** the same as constructed-facility certification or operational sustainability. PeeringDB is A- for existence/location/interconnection metadata because it is user-maintained but operationally relied on.

## Ground Rules

- No verified national public register of Cameroon data centres was found. Build records by joining operator pages, ART telecom evidence, MINPOSTEL/ANTIC/CENADI digital-infrastructure evidence, MINHDU and commune permit evidence, MINEE/ARSEL/ENEO/SONATREL/EDC power evidence, MINEPDED environmental evidence, public procurement, Uptime, PeeringDB and trade press.
- Search in French first: `centre de données`, `data center`, `datacenter`, `centre d'hébergement`, `hébergement`, `colocation`, `baies`, `salle informatique`, `cloud souverain`, `Tier III`, `Tiers 3`, `mise en service`, `inauguration`, `raccordement`, `poste`, `MVA`, `MW`. Use English variants for North-West, South-West and international press: `data centre`, `colocation`, `Tier III`, `inaugurated`, `rack`, `landing station`.
- The market is **Centre + Littoral first**. Correct region attribution is mandatory:
  - Camtel NBN II / Zamengoé is a Centre-region record. Sources often market it as Yaoundé, but stronger local descriptions place Zamengoé in Lékié division / Okola area on the outskirts of Yaoundé.
  - Orange Cameroun's DC is Littoral / Douala 5e / Maképé.
  - ST Digital's Cameroon DC is Littoral / Douala port zone / Douala-Bonabéri.
  - CAMPOST Data Center Yaoundé and MTN Cameroon Yaoundé DC are Centre records.
- Treat telco switch rooms, cable landing stations, satellite earth stations and bank IT rooms as leads unless a service page, PeeringDB facility record, Uptime record, procurement, permit or official visit names a data centre.
- Hyperscaler public cloud regions are negative evidence as of 2026-08-12: AWS, Azure, Google Cloud, Oracle OCI and Huawei Cloud official region/location pages do not list a Cameroon public cloud region. Re-check official pages every run.
- Do not copy directory-only capacity values into final facility records without a stronger corroborating source.

## Verified Official and Primary Sources

### MINPOSTEL -- Ministry and Digital Strategy

Primary URLs:
- https://www.minpostel.gov.cm/ -- official ministry site; live and listing current news, tenders and institutional links.
- https://www.minpostel.gov.cm/index.php/en/les-grands-chantiers/138-cameroon-digital-strategic-plan-2020 -- "Strategic Plan for a Digital Cameroon by 2020"; A for national digital-infrastructure strategy.
- https://www.minpostel.gov.cm/index.php/en/structure-a-la-une/91-in-the-spotlight/293-nigeria-cameroon-submarine-cable-system-ncscs-provides-quality-service-for-electronic-communication-networks -- official NCSCS submarine-cable page; A for state cable evidence.
- https://www.minpostel.gov.cm/index.php/fr/actualites/515-data-center-de-st-digital -- 2025-07-21 ministry article on the ST Digital Data Center after a 2025-07-14 ministerial visit; A for official recognition, Douala port-zone location and local hosting role.

Use MINPOSTEL as A-grade evidence for strategy, state broadband/subsea programmes, official site visits and state-hosting policy signals. Ministry articles that quote operator claims remain A for the visit/location and B/A- for technical claims unless a technical certificate is linked.

Queries:
```text
site:minpostel.gov.cm "centre de données" OR "data center" OR "datacenter"
site:minpostel.gov.cm "ST Digital" "Data Center" OR "Douala"
site:minpostel.gov.cm "NCSCS" OR "câble sous-marin" OR "submarine"
site:minpostel.gov.cm "Camtel" "Zamengoé" OR "NBN II"
site:minpostel.gov.cm "MTN" "Yaoundé DC" OR "data center"
```

### ART -- Telecom Regulator

Primary URLs:
- https://art.cm/ -- Agence de Régulation des Télécommunications.
- https://art.cm/fr/operateurs -- licensed operators list.
- https://art.cm/fr/procedures-formulaires -- procedures/forms.
- https://art.cm/fr/reglementation/dao -- tenders / DAO.

Use ART as A-grade evidence for operator status, licences and regulator actions. It is not a facility registry unless the specific decision or article names a facility. Join ART operator records to Camtel, MTN, Orange, Nexttel/Viettel, Yoomee, ISP and IXP names before accepting a commercial-services claim.

Queries:
```text
site:art.cm "centre de données" OR "data center" OR "datacenter" OR "hébergement"
site:art.cm "licence" OR "décision" "{operator}"
site:art.cm "Camtel" "Zamengoé" OR "NBN II" OR "Data Center"
site:art.cm "Orange Cameroun" "data center" OR "Maképé"
site:art.cm "MTN Cameroon" "Yaoundé DC" OR "data center"
```

### Camtel -- State Operator

Primary URLs:
- https://www.camtel.cm/ -- official site; A for current operator identity and marketed state connectivity/hosting offers.
- https://hosting.camtel.cm/ -- official hosting/data-centre services portal; A for customer-facing hosting, cloud, backup and related services.
- https://uptimeinstitute.com/uptime-institute-awards/country/id/CM -- lists Cameroon Telecommunications / Camtel NBN II Data Center / Yaounde with **Tier III Certification of Design Documents**.
- https://uptimeinstitute.com/uptime-institute-awards/datacenter/camtel-nbn-ii-data-center/896 -- Camtel NBN II project page; A for Uptime record and satellite-earth-station context.
- https://www.peeringdb.com/fac/10585 -- Camtel Bepanda, Douala; networks, CAMIX Douala exchange, coordinates.

Facility seeds:
- **Camtel NBN II Data Center / Zamengoé** -- Centre region; use Lékié / Okola / Zamengoé when source-supported and "Yaoundé" only as marketed metro. Status: operational/marketed. A for official service existence and Uptime design-award record; B for trade-press size/cost/rack numbers. Record certification as "Tier III Certification of Design Documents listed by Uptime" unless a constructed-facility certificate is isolated.
- **Camtel Bepanda** -- Littoral region, Wouri division, Douala/Bepanda. A- for PeeringDB facility record and CAMIX Douala presence. Classify as interconnection/telco/colo lead unless Camtel page proves commercial colocation at this site.
- **Camtel Garoua earth station** -- North region, Benoué division, Garoua. C lead only unless a data-centre page, Uptime record, PeeringDB facility or procurement names a DC.

Queries:
```text
site:camtel.cm "Zamengoé" OR "Zamengoe" OR "NBN II" OR "data center" OR "datacentre"
site:hosting.camtel.cm "colocation" OR "hébergement" OR "cloud" OR "backup"
site:camtel.cm "Bepanda" "data center" OR "colocation" OR "station terrienne"
site:camtel.cm "Garoua" "station" OR "data center"
"Camtel NBN II Data Center" "Tier III Certification of Design Documents"
```

### Orange Cameroun

Primary URLs:
- https://business.orange.cm/fr/mieux-nous-connaitre.html -- official Orange Business Cameroun page; A for "1 data center tiers III+", inaugurated since May 2017, three 1,050 m2 stages, 340 racks in two white rooms, 24/7 operation, two separated MV feeds, two fibre landing points and security/fire controls.
- https://www.orange.cm/ -- consumer/operator portal; use for operator identity and cross-links.

Facility seed:
- **Orange Cameroun Data Center, Maképé, Douala 5e** -- Littoral region, Wouri division. Status: operational since May 2017. A for official Orange Business page and specs; B for location/inauguration details from Afrik/DCD/CIO Mag if Orange page does not name Maképé.

Queries:
```text
site:business.orange.cm "data center" OR "tiers III" OR "baies" OR "hébergement"
site:orange.cm "data center" OR "centre de données" OR "hébergement" OR "cloud"
"Orange Cameroun" "Maképé" OR "Douala 5" "data center"
"Orange Cameroun" "340 baies" OR "1050 m²" OR "16 milliards"
```

### ST Digital

Primary URLs:
- https://st.digital/ -- official ST Digital site; states datacenters in Douala (Cameroon), Grand-Bassam and Nkok and certifications including ISO 27001/TIA-942/HDS.
- https://st.digital/en/cameroun -- official Cameroon page; A for Douala presence, certified infrastructure and cloud/cybersecurity service offer.
- https://st.digital/datacenters and https://st.digital/en/datacenters -- official datacenter pages; use if reachable in the run. Search result confirms a Douala next-generation datacenter and local/international customer positioning.
- https://www.minpostel.gov.cm/index.php/fr/actualites/515-data-center-de-st-digital -- official ministry visit to the port-zone Douala data center, published 2025-07-21.

Facility seed:
- **ST Digital Data Center, Douala port zone / Douala-Bonabéri** -- Littoral region, Wouri division. Status: operational/marketed. A for ST Digital official presence/services and MINPOSTEL official visit/location. Keep exact Tier/certification wording tied to source: ST Digital says certified infrastructure; do not translate this into Uptime Tier certification unless an Uptime record is found.

Queries:
```text
site:st.digital "Cameroun" OR "Cameroon" "datacenter" OR "data center" OR "Douala"
site:st.digital "Douala" "colocation" OR "cloud souverain" OR "CloudStore"
site:minpostel.gov.cm "Data Center de ST Digital"
"ST Digital" "zone portuaire" OR "Douala-Bonabéri" "data center"
```

### CAMPOST, CAMIX and Interconnection

Primary URLs:
- https://camix.cm/ and https://www.camix.cm/membres -- CAMIX official site/member page; A for IXP identity and contact address "Immeuble Data Center CAMPOST, BP 788 Yaoundé". Browser/search access works; automated HEAD checks may time out.
- https://www.peeringdb.com/fac/10586 -- CAMPOST Data Center Yaoundé; A- for facility existence, address Ave Konrad Adenauer, coordinates, CAMIX Yaounde exchange and network list.
- https://armp.cm/details?id_publication=4844&type_publication=AMI -- 2024 ARMP/CAMPOST AMI; A for EPOST infrastructure containing a datacenter for hosting platforms/servers, current datacenter rehabilitation/extension, and a planned secondary datacenter in Douala. A stale CAMPOST deep link is still visible in PeeringDB but returned 404 in this run.
- https://www.pch.net/ixp/details/1952 -- PCH CAMIX-Yaoundé entry naming the CAMPOST Data Center building.

Facility seed:
- **CAMPOST Data Center Yaoundé** -- Centre region, Mfoundi division, Yaoundé. Status: operational interconnection/institutional facility. A- for PeeringDB and CAMIX; classify commercial colocation only if CAMPOST service pages or customer materials support that.

Queries:
```text
site:camix.cm "CAMPOST" OR "Data Center" OR "Yaoundé"
site:campost.cm "hébergement" OR "serveurs" OR "applications" OR "data center"
"CAMPOST Data Center Yaoundé" OR "Immeuble Data Center CAMPOST"
site:peeringdb.com/fac "CAMPOST Data Center Yaoundé"
```

### MTN Cameroon

Primary URLs:
- https://uptimeinstitute.com/uptime-institute-awards/country/id/CM -- lists **MTN Cameroon / Yaoundé DC / Tier III Certification of Design Documents**.
- https://uptimeinstitute.com/component/tierachievement/client/mtn-cameroon/1314 -- MTN Cameroon client page.
- https://fr.uptimeinstitute.com/uptime-institute-awards/list/datacenter/yaound-dc/2228 -- French project page for Yaoundé DC.
- https://mtn.cm/ and https://www.mtn.com/ -- operator identity and service pages.

Facility seed:
- **MTN Cameroon Yaoundé DC** -- Centre region, Yaoundé; division/site details unknown. Status: at least designed/projected facility with Uptime Tier III Design Documents award; do not mark operational or commercial unless MTN or regulator evidence proves launch/customer services.

Queries:
```text
site:uptimeinstitute.com "MTN Cameroon" "Yaoundé DC"
site:mtn.cm "data center" OR "centre de données" OR "cloud" OR "hébergement"
"MTN Cameroon" "Yaoundé DC" OR "Tier III Certification of Design Documents"
"MTN Business" "Cameroun" "cloud" OR "hosting" OR "colocation"
```

### ANTIC, CENADI and State IT

Primary URLs:
- https://www.antic.cm/ -- National Agency for ICT; live.
- https://www.cenadi.cm/ -- CENADI under MINFI; live.
- https://camgovca.cm/ -- CamGovCA e-government/PKI portal; verify reachability each run.

Use these as A-grade evidence for state IT/cybersecurity responsibilities and data-sovereignty demand, but not as facility proof unless a named site is given.

Queries:
```text
site:antic.cm "hébergement" OR "cloud" OR "centre de données" OR "certification"
site:cenadi.cm "data center" OR "centre de calcul" OR "hébergement" OR "serveurs"
site:camgovca.cm "données" OR "hébergement" OR "infrastructure" OR "PKI"
"CENADI" OR "ANTIC" "data center" "Cameroun"
```

### Energy, Grid and Environment

Primary URLs:
- https://minee.cm/ -- Ministry of Water and Energy.
- https://arsel-cm.org/ -- ARSEL electricity regulator; verify current status/renaming each run.
- https://eneocameroon.cm/ -- ENEO distribution utility; ownership/status should be rechecked each run.
- https://minee.cm/category/sonatrel/ -- MINEE SONATREL category; use as official fallback when SONATREL's standalone site is unreachable.
- https://edc.cm/ -- EDC generation/hydro developer; `www.edc-cameroon.org` did not respond in this run and should not be used as a primary URL.
- https://minepded.gov.cm/ -- MINEPDED environment ministry. `https://www.minepded.gov.cm/` did not resolve in this run; no-www host responded with an expired certificate, so verify manually before citing.

Energy/environment facts are high value but sparse. A-grade power evidence requires a named operator/facility, connection request, substation, MV feed, generator/fuel filing, tariff, EIES or official technical sheet.

Queries:
```text
site:minee.cm "data center" OR "centre de données" OR "raccordement"
site:arsel-cm.org "data center" OR "raccordement" OR "grand consommateur"
site:eneocameroon.cm "data center" OR "raccordement" OR "moyenne tension"
site:sonatrel.cm OR site:edc-cameroon.org "data center" OR "MW" OR "poste"
site:minepded.gov.cm OR site:minepded.gov.cm "EIES" OR "étude d'impact" "data center"
"{facility}" "MVA" OR "MW" OR "moyenne tension" "Cameroun"
```

### Planning, Building Permits, Registry and Procurement

Primary URLs:
- https://www.minhdu.gov.cm/demarche-construire/ -- MINHDU "Démarche Construire"; A for permit process.
- https://www.minhdu.gov.cm/ -- Ministry of Housing and Urban Development.
- https://www.minmap.cm/ -- MINMAP; live and redirects to `index.php?lang=fr`.
- https://www.armp.cm/ -- ARMP; live.
- https://marchespublics.cm/ -- COLEPS/public procurement platform; no `www` host. `https://www.marches-publics.cm/` did not resolve in this run.
- https://www.investincameroon.net/ -- investment-promotion/official-adjacent site; live.
- CFCE: `cfce.cm` and `www.cfce.cm` did not resolve in this run. Prefer official MINFI/greffe/CFCE pages located by search before citing RCCM/company formation facts.

Queries:
```text
site:minhdu.gov.cm "permis de construire" "data center" OR "centre de données"
site:minmap.cm OR site:armp.cm OR site:marchespublics.cm "data center" OR "centre de données" OR "hébergement" OR "serveurs"
site:minfi.gov.cm "CFCE" OR "RCCM" "{operator}"
"{operator}" "RCCM" "Cameroun" "objet"
"{facility}" "convention d'établissement" OR "investissement" "Cameroun"
"Douala" "permis de construire" "ST Digital" OR "Orange Cameroun"
```

## Facility Seeds With Correct Region Attribution

| Facility / project | Region / division | Status | Best source grade | Evidence and cautions |
|---|---|---:|---:|---|
| Camtel NBN II Data Center / Zamengoé | Centre / Lékié lead; marketed as Yaoundé | Operational/marketed | A for Uptime design award and Camtel services; B for trade size/cost | Uptime lists Camtel NBN II Data Center in Yaounde with Tier III Certification of Design Documents. Use Camtel/hosting pages for services; use DCD/CEMAC/press only for cost, area and ceremony details. |
| Camtel Bepanda | Littoral / Wouri / Douala-Bepanda | Operational interconnection/telco facility | A- | PeeringDB fac/10585: Camtel, Bepanda address, Douala, coordinates, 5 networks, CAMIX Douala. Commercial colocation requires Camtel service corroboration. |
| Orange Cameroun Data Center | Littoral / Wouri / Douala 5e / Maképé | Operational since May 2017 | A | Orange Business official page gives Tier III+ wording, 3 x 1050 m2 stages, 340 racks, 24/7, MV feeds, fibre and security specs. Afrik/DCD/CIO Mag support Maképé and inauguration context. |
| ST Digital Data Center | Littoral / Wouri / Douala port zone / Douala-Bonabéri | Operational/marketed | A | ST Digital official site and Cameroon page identify Douala datacenter/services; MINPOSTEL 2025 visit names port-zone location and local public/private hosting. Verify exact address/certifications. |
| CAMPOST Data Center Yaoundé | Centre / Mfoundi / Yaoundé | Operational interconnection/institutional facility | A- | CAMIX official contact and PeeringDB fac/10586 identify CAMPOST DC, Ave Konrad Adenauer, networks and CAMIX Yaounde. |
| MTN Cameroon Yaoundé DC | Centre / Yaoundé; division/site unknown | Design-awarded/project lead | A for Uptime design award; C until operational evidence | Uptime lists MTN Cameroon Yaoundé DC with Tier III Certification of Design Documents. Do not infer constructed/operational/commercial status. |
| Camtel Garoua earth station | North / Benoué / Garoua | Telco site lead | C | Uptime Camtel client background names Garoua earth station, but not a DC. |
| Kribi cable landing infrastructure | South / Ocean / Kribi | Landing stations, not DCs | A for landing evidence | MINPOSTEL NCSCS and subsea sources support cable infrastructure. Treat as demand/edge lead only. |
| CENADI / CamGovCA state hosting | Centre / Yaoundé lead | State IT workload lead | C for facility | Official portals prove institutions, not a named DC beyond Camtel/CAMPOST. |
| Nexttel/Viettel, banks, universities, ISPs | Centre/Littoral likely | Internal leads | C | Search before creating facility records; do not classify switch/IT rooms as DCs without named evidence. |

## Per-Region Official Sweep

Run this exact 10-region sweep before setting `no_projects: true`. Search both French and English region names, local capitals and divisions/departments.

| Region | Key city/division terms | Official-first strategy | Expected result as of 2026-08-12 |
|---|---|---|---|
| Adamaoua | Ngaoundéré; Vina; Mbéré; Faro-et-Déo; Mayo-Banyo; Djérem | MINHDU/commune permits, ENEO/ARSEL/MINEE, MINPOSTEL, Camtel/MTN/Orange local POPs, University of Ngaoundéré. | No verified DC. |
| Centre | Yaoundé; Mfoundi; Lékié; Okola; Zamengoé; Mbankomo; Nsimalen; Obala | Camtel NBN II/Zamengoé, CAMPOST/CAMIX, MTN Yaoundé DC Uptime, ANTIC/CENADI/CamGovCA, MINHDU/CUY permits, ENEO/SONATREL. | Positive: Camtel NBN II, CAMPOST DC, MTN Yaoundé DC design-awarded lead, state IT leads. |
| Far North | Maroua; Diamaré; Kousséri; Logone-et-Chari; Mayo-Sava; Mayo-Tsanaga | Commune permits, MINEE/ENEO, telco POPs, university/state projects; verify security-context impact. | No verified DC. |
| East | Bertoua; Lom-et-Djérem; Kadey; Boumba-et-Ngoko; Haut-Nyong | Backbone/mining/logistics corridors, commune permits, ENEO/SONATREL, telco POPs. | No verified DC. |
| Littoral | Douala; Wouri; Bepanda; Maképé; Douala 5e; Douala-Bonabéri; Akwa; Bonanjo; Bonabéri; Yassa; Bassa; Nkongsamba; Moungo | Orange Business, ST Digital, Camtel Bepanda PeeringDB, CAMIX Douala, ART operator records, CUD/commune permits, ENEO/ARSEL, port/industrial records. | Positive: Orange Maképé, ST Digital Douala, Camtel Bepanda, telco/ISP leads. |
| North | Garoua; Benoué; Lagdo; Guider; Mayo-Louti; Mayo-Rey | Camtel Garoua earth station lead, MINEE/ENEO, commune permits, telco POPs, university/state infrastructure. | No verified DC; Garoua satellite station only. |
| North-West | Bamenda; Mezam; Kumbo; Bui; Wum; Menchum; Ndop; Ngoketunjia | English + French searches, council permits, telco POPs, University of Bamenda, conflict-context status checks. | No verified DC. |
| West | Bafoussam; Mifi; Dschang; Menoua; Foumban; Noun; Mbouda; Bamboutos | Commune permits, ENEO, university/state IT, telco POPs and potential DR/edge sites. | No verified DC. |
| South | Ebolowa; Kribi; Ocean; Sangmélima; Dja-et-Lobo; Vallée-du-Ntem | Port de Kribi, ZES/industrial zone, MINPOSTEL NCSCS, ACE/SAIL landing evidence, ENEO/SONATREL, commune permits. | No verified DC; strongest non-Centre/Littoral future lead. |
| South-West | Buea; Fako; Limbe; Tiko; Kumba; Meme; Mamfe; Manyu | English + French searches, Buea/Limbe/Tiko councils, port/industrial and university leads, telco POPs, conflict-context status checks. | No verified DC. |

Universal region queries:
```text
"{region}" "centre de données" OR "data center" "Cameroun"
"{capital}" "centre de données" OR "data center" OR "datacenter" "Cameroun"
"{division}" "hébergement" OR "colocation" OR "cloud" "Cameroun"
site:gouv.cm "{region}" "numérique" OR "TIC" OR "fibre"
site:minhdu.gov.cm "{capital}" "permis de construire" OR "certificat d'urbanisme"
"{capital}" "Orange" OR "MTN" OR "Camtel" OR "Nexttel" "data center" OR "centre de données"
"{region}" "MVA" OR "MW" "data center" OR "centre de données"
"{region}" "data centre" OR "colocation" OR "Tier III"
```

## Record Extraction Checklist

For each candidate, capture:

- `facility_name`, `aliases`, `operator`, `owner/SPV`, `source_name`, `source_url`, `source_grade`, `fact_grade`.
- `region`, `division/departement`, `arrondissement/commune`, `locality`, address and coordinates if source-grade supports them.
- `status`: lead, announced, financed, permitted, first stone, under construction, inaugurated/launched, operational, decommissioned.
- `service_class`: commercial colocation/cloud, telco internal, interconnection/IXP, state/institutional, landing station, satellite/POP lead.
- Capacity facts with qualifiers: racks current vs max, building area vs white space, MW utility vs IT load, availability SLA vs measured uptime, Uptime design vs constructed vs operational certificate.
- Negative evidence date and official URL checked for hyperscalers and pan-African entrants.
