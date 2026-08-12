# BJ Explorer Official - Benin Datacenter Enumeration via Regulators, Permits, Power, Digital Government and Investment Records

Date: 2026-08-12. Country: **BJ Benin**. Division model: **12 departments** (`subnational_type = department`): Alibori, Atakora, Atlantique, Borgou, Collines, Donga, Kouffo, Littoral, Mono, Oueme/Ouémé, Plateau, Zou. Use ISO/French official spellings (`Atakora`, `Kouffo`, `Ouémé`) in final records; accept `Atacora`, `Couffo`, and `Oueme` as search aliases.

Scope: official and regulatory evidence for commercial, telecom, government, enterprise and pipeline data-centre facilities. Benin has no public national data-centre register, so official enumeration is a chain-of-evidence exercise.

Reliability grades:
- **A** = primary/official evidence: ministry or agency pages (`innovation.gouv.bj`, `asin.bj`, `gouv.bj`, `sgg.gouv.bj`), ARCEP decisions/pages, ABE or ministerial EIES/certificate records, commune permit records, SBEE/SBPE/CEB/ARE utility records, World Bank procurement records, official cloud-region pages, official operator pages naming a data-centre product or facility.
- **A-** = official operator or government announcement that proves a named facility/service or project but does not expose regulator/permit/utility details. Capacity, tier and commissioning claims still need source-specific grading.
- **B** = reputable secondary evidence with concrete parties/dates/site facts: DatacenterDynamics, Agence Ecofin, CIO Mag, La Nation, 24 Heures au Bénin, La Nouvelle Tribune, Banouto, OSIRIS, PeeringDB.
- **C** = lead only: directories, SEO listings, social posts, marketplace pages, market reports, unsourced rack/MW/area tables, Wikipedia.

Grade the specific claim, not the whole facility. A facility can be **A** for existence, **B** for a launch date, and **C** for area or rack count.

---

## 0. Benin-specific structure facts

- **No single official data-centre register was found.** Build records by moving from name/operator -> commune building permit -> environmental authorization -> power evidence -> telecom/connectivity licence -> data-protection/company/investment record -> ministry/operator confirmation.
- Benin is divided into **12 departments** and 77 communes. Department coverage is complete only when every department in the table in section 9 has either a positive/watch item or `no_projects: true` with dated query notes.
- Positive and watch geography is concentrated in:
  - **Atlantique**: national data centre at Abomey-Calavi; GDIZ/Glo-Djigbé watch item; Ouidah Sèmè City future campus watch item.
  - **Littoral**: Cotonou cluster: MTN Data Center product, Alink/ISOCEL directory leads, ACE/SAT-3 landing assets, BENIN-IX, telco HQs and hosting firms.
  - **Ouémé**: Porto-Novo/Sèmè-Kpodji historical Sèmè City/search alias and government/telco rooms; no official DC facility found there in current sources.
- French terms lead: `centre de données`, `datacenter`, `data center`, `salle de serveurs`, `hébergement`, `colocation`, `cloud`, `serveurs`, `permis de construire`, `étude d'impact environnemental`, `certificat de conformité environnementale`, `licence`, `autorisation`, `ARCEP`, `opérateur`, `fournisseur d'accès`, `GDIZ`, `zone industrielle`, `backbone`, `fibre optique`.
- Do not infer a public cloud region from hosting, CDN, cache, reseller or office presence. As of 2026-08-12, official AWS, Azure, Google Cloud and Oracle lists do **not** list a Benin public cloud region.
- Benin sources rarely publish MW. Prefer original units (`sqm`, racks, Tier/TIA wording, service launch wording). Do not convert building area or generator specs into operational IT load.

---

## 1. ARCEP Bénin - telecom regulator

Official site: https://arcep.bj/ . Decisions: https://arcep.bj/decisions/ . Related ARCEP services/maps visible from the official site include `e-services.arcep.bj`, `simulateur.arcep.bj`, `atlas.arcep.bj`, and legacy `web.arcep.bj`.

Verified official role:
- ARCEP is the national electronic-communications and postal regulator. The SGG page for Decree No. 2019-209 cites Law No. 2014-14 of 9 July 2014 and the ARCEP framework: https://sgg.gouv.bj/upload/files/documentheque/0298673001530263350.pdf . **Grade A**.
- The current digital/legal framework is the Code du numérique, Law No. 2017-20 of 20 April 2018 as amended by Law No. 2020-35 of 6 January 2021. Use SGG/official legal copies when a claim depends on the statute. **Grade A**.
- ARCEP is **not** a data-centre construction-permit authority. Use ARCEP for network operators, fibre authorizations, satellite/VSAT/radio authorizations, SVA declarations, interconnection, numbering, QoS and infrastructure-map leads.

What to extract:
- licensee/SPV, licence or authorization class, decision number/date, service scope, expiry/effective dates, station/site wording, commune/department, and whether the record names fibre, backbone, landing station, VSAT/satellite, colocation/hosting, or operator infrastructure.

ARCEP queries:
```text
site:arcep.bj "{operator}" licence OR autorisation OR décision
site:arcep.bj "centre de données" OR "data center" OR hébergement OR colocation
site:arcep.bj "station d'atterrissement" OR "câble sous-marin" OR "fibre optique"
site:arcep.bj "Décision" "{operator}" "{year}"
"ARCEP Bénin" "{operator}" licence OR autorisation OR décision
"ARCEP Bénin" satellite OR VSAT OR "Wifi Zone" autorisation
site:atlas.arcep.bj Cotonou OR Abomey-Calavi OR Parakou
```

Grade guidance: **A** for ARCEP pages/downloads; **B** for reputable press quoting an ARCEP decision; **C** for generic licence lists without an ARCEP URL.

---

## 2. Digital-government chain

### 2.1 Ministère du Numérique / Portail du Numérique

Official portal: https://innovation.gouv.bj/ . Government portal: https://www.gouv.bj/ . State legal repository: https://sgg.gouv.bj/ .

Verified facility/project evidence:
- **Data centre national, Abomey-Calavi (Atlantique)**. Ministry page dated 2021-06-01 states ministers visited the national datacenter site in Abomey-Calavi for progressive powering/testing, describes secure electric supply, dual fibre, fire/access controls, and Tier 3 ANSI/TIA-942 certification process: https://innovation.gouv.bj/publications/actualites/datacenter-national-demarrage-des-premiers-tests-techniques-sous-le-regard-de-la-ministre-du-numerique-et-de-la-digitalisation . **Grade A** for existence, commune, testing milestone and infrastructure features.
- La Nation article dated 2019-02-08 describes the construction site at Abomey-Calavi, a two-hectare property, a 500 sqm technical block, national hosting mission for state systems and semi-public/private capacity, and project management by ASSI: https://lanation.bj/actualites/pour-booster-le-potentiel-numerique-au-benin-le-menc-a-pied-doeuvre-pour-un-data-center . Treat La Nation as **B+**, or **A-** where it directly reports an official ministerial site visit and named officials.
- Operational status call: count the national DC as a confirmed government facility in Abomey-Calavi with commissioning/testing proven in 2021. Mark `status = operational_or_commissioning_confirmed_by_2021`; do **not** mark commercial colocation as proven unless ASIN/SBIN/ministry publishes a commercial service page.
- **WARDIP secondary/redundancy DC feasibility study**. World Bank procurement detail OP00432980 is the primary source: https://projects.worldbank.org/en/projects-operations/procurement-detail/OP00432980 . DCD summarized the notice and reported submissions due 2026-03-27 and a six-month study: https://www.datacenterdynamics.com/en/news/benin-wants-to-establish-a-secondary-national-data-center/ . The WARDIP concept/PID document landing page is at https://documents.worldbank.org/en/publication/documents-reports/documentdetail/966521635044503175 . Grade **A** for the World Bank procurement/document landing page and **B** for DCD details. Pipeline only; no facility record until a site is selected.

Ministry queries:
```text
site:innovation.gouv.bj datacenter OR "data center" OR "centre de données"
site:innovation.gouv.bj "Abomey-Calavi" "datacenter national"
site:gouv.bj "data center" OR datacenter OR "centre de données" OR "cloud souverain"
site:sgg.gouv.bj "centre de données" OR datacenter OR "numérique"
"ASSI" Bénin "data center national" "Abomey-Calavi"
"ASIN" Bénin "data center national" OR "cloud souverain"
```

### 2.2 ASIN

Official site: https://asin.bj/ . ASIN is the state execution agency for digital systems and infrastructure and the successor/continuation of earlier digital execution functions such as ASSI/ADN/ANSSI in public reporting.

Use ASIN to verify:
- operator/manager attribution for the national DC;
- state-cloud or hosting service pages;
- procurement/maintenance notices for power, cooling, security, fibre or cloud platforms;
- references to disaster recovery or secondary DC planning.

ASIN queries:
```text
site:asin.bj "data center" OR datacenter OR "centre de données" OR hébergement OR cloud
site:asin.bj "Abomey-Calavi" OR "datacenter national"
site:asin.bj marchés OR "appel d'offres" OR infrastructure OR "salle serveur"
"ASIN" "Abomey-Calavi" datacenter OR "centre de données"
"ASIN" "SBIN" datacenter OR hébergement
```

Grade **A** for ASIN pages/procurements; **B** for press quoting ASIN; **C** for social-only attribution.

### 2.3 APDP - data protection

Use APDP and Code du numérique records to identify data controllers/processors, not facilities. APDP registration proves a legal/compliance relationship; it does not prove a physical DC.

Queries:
```text
"APDP" Bénin "{operator}" hébergement OR cloud OR traitement
site:apdp.bj "{operator}" OR hébergement OR cloud
site:sgg.gouv.bj "Code du numérique" "données à caractère personnel"
```

Grade **A** for official law/APDP pages; **B** for reputable press on APDP actions; **C** for company privacy pages.

### 2.4 E-government portals

- Public-service portal: https://www.service-public.bj/public/services/e-services .
- Building permit service PS00141: https://www.service-public.bj/public/services/service/PS00141 .
- CatIS/X-Road service catalogue: https://catis.xroad.bj/ .
- APIEx company window: https://monentreprise.bj/ .

Grade **A** for service existence and process; facility evidence requires a project/operator-specific record.

---

## 3. Planning and building permits - communes/mairies

Building permits (`permis de construire`) are commune/mairie records. The verified official online service is PS00141. The Ministry of Living Environment/Cadre de Vie permit information page was found at https://cadredevie.gouv.bj/permis-de-construire/ . The current SGG decree page for construction/demolition permits is https://sgg.gouv.bj/doc/decret-2023-617/ .

For DC-scale projects, seek:
- applicant/SPV/operator;
- plot/parcel/title reference;
- commune and department;
- use description (`centre de données`, `salle informatique`, `local technique`, `bâtiment technique`, `groupe électrogène`, `poste`);
- permit number/date;
- floor area, technical block size, generator/fuel/battery/cooling room descriptions.

Permit queries:
```text
site:service-public.bj "permis de construire" "{commune}"
"permis de construire" site:service-public.bj "{operator}" OR "{commune}"
"permis de construire" "{commune}" Bénin "{operator}" OR "centre de données" OR datacenter
"Mairie de {commune}" "permis de construire" "centre de données"
"Abomey-Calavi" "permis de construire" datacenter OR "centre de données"
"Cotonou" "permis de construire" MTN OR ISOCEL OR Alink OR datacenter
```

Grade **A** only for commune/portal/official permit records; **B** for a ministry or press report of a granted permit; **C** for real-estate or directory claims.

---

## 4. Environment - ABE and environmental compliance

Official ABE site: https://abe.bj/ . SGG decree page for environmental-assessment procedures: https://sgg.gouv.bj/doc/decret-2017-332/ and download https://sgg.gouv.bj/doc/decret-2017-332/download . A 2022 Council of Ministers record says the 2017 decree was replaced/updated by a new environmental and social evaluation procedure: https://sgg.gouv.bj/cm/2022-07-13/ . Check the current decree in each batch.

Why DCs matter for ABE: standby diesel generation, fuel storage, UPS batteries, cooling and water use, noise, construction impact and e-waste. Public EIES/certificate records can reveal generator count, kVA/MW, fuel volumes, site plan and phase descriptions.

ABE queries:
```text
site:abe.bj "data center" OR datacenter OR "centre de données" OR "salle de serveurs"
site:abe.bj "{operator}" OR "{SPV}" OR "{commune}"
site:abe.bj "certificat de conformité" "{operator}" OR datacenter
"Agence Béninoise pour l'Environnement" "{operator}" "étude d'impact"
"certificat de conformité environnementale" Bénin "{operator}" OR datacenter
filetype:pdf EIES Bénin "{commune}" datacenter OR "centre de données"
```

Grade **A** for ABE/ministerial permits or EIES records; **B** for official project announcements saying a certificate was granted; **C** for unsupported compliance claims.

---

## 5. Power and energy evidence

Current/commonly cited sector actors:
- SBEE - distribution: https://sbee.bj/ .
- SBPE - production/bulk procurement: https://sbpe.bj/ .
- CEB - Benin-Togo transmission/generation utility: https://www.cebnet.org/ .
- ARE - electricity regulator: https://are.bj/ .

Use power evidence to confirm scale and readiness. Benin DC sources usually mention secure power, UPS/generators and dual fibre, not MW.

Energy queries:
```text
site:sbee.bj "data center" OR datacenter OR "centre de données" OR "grand client" OR raccordement
site:sbpe.bj "{operator}" OR "Abomey-Calavi" OR "Cotonou" OR centrale OR solaire
site:are.bj "{operator}" OR tarif OR décision OR raccordement
site:cebnet.org "{site}" poste OR transport OR MVA
"SBEE" Bénin "{commune}" raccordement OR "poste électrique" "{operator}"
"{operator}" Bénin "groupe électrogène" OR générateur OR onduleur OR "salle informatique"
```

Grade **A** for official utility/regulator documents; **B** for utility/project press; **C** for reported MW without source.

---

## 6. Investment promotion and special economic zones

- APIEx investor portal: https://investbenin.bj/ and APIEx profile page https://investbenin.bj/about/apiex . Company formalities: https://monentreprise.bj/ .
- GDIZ/Glo-Djigbé Industrial Zone: official site https://gdiz-benin.com/ ; ARISE IIP project page https://www.ariseiip.com/project/gdiz/ ; government article https://www.gouv.bj/article/1567/amenagement-zone-industrielle-djigbe-gdiz-vaste-projet-veut-etre-industriel-sous-region/ .

Current handling:
- GDIZ is in **Atlantique** (Glo-Djigbé/Abomey-Calavi area). It is a strategic watch zone for industrial ICT infrastructure, but **no verified data-centre project inside GDIZ was found**. Mark `watch_only`, not facility.
- Sèmè City’s current official site says the main campus is in **Ouidah** (Atlantique): https://semecity.bj/fr/campus/campus-ouidah/ . Treat Sèmè One/data-centre mentions as industry leads, not official facility proof unless a Sèmè City page explicitly names a data centre and its current address.

Investment queries:
```text
site:apiex.bj "data center" OR datacenter OR "centre de données" OR ICT OR numérique
site:investbenin.bj "data center" OR datacenter OR "digital" OR "zone économique spéciale"
site:gdiz-benin.com "data center" OR datacenter OR "centre de données" OR digital OR infrastructure
"SIPI-Bénin" OR "ARISE IIP" Bénin "data center" OR datacenter OR numérique
"GDIZ" Bénin "data center" OR datacenter OR "centre de données"
site:semecity.bj "data center" OR datacenter OR "centre de données" OR "Sèmè One"
```

---

## 7. Connectivity official hooks

- SBIN/Celtiis official brand page: https://celtiis.bj/a-propos . Sonatel delegation announcement: https://sonatel.sn/sonatel-nouveau-partenaire-strategique-de-la-sbin-au-benin/ . Use these for SBIN/Celtiis corporate/backbone context, but do not treat them as DC-facility proof unless they name a DC.
- ACE official cable page lists Cotonou, Benin: https://ace-submarinecable.com/le-cable-sous-marin/ . Agence Ecofin reported ACE service in Benin in October 2015: https://www.agenceecofin.com/infrastructures/1610-33176-le-benin-a-mis-en-service-le-cable-sous-marin-de-fibre-optique-ace . La Nation covered ministerial visits to ACE and SAT-3 stations: https://lanation.bj/actualites/visite-du-mctic-dans-les-stations-ace-et-sat-3-etienne-kossi-senquiert-de-letat-davancement-des-deux-sites . Grade **A** for ACE official route, **B** for press site details.
- BENIN-IX PeeringDB exchange page: https://www.peeringdb.com/ix/1017 and organization page https://www.peeringdb.com/org/10706 . Grade **B**; use as network/peering lead, not standalone facility proof.
- GeoCables Cotonou page: https://geocables.com/location/cotonou-benin?lang=fr . Grade **C/B-**; use to discover cable aliases and verify elsewhere before creating records.

Connectivity queries:
```text
site:gouv.bj "câble sous-marin" OR ACE OR SAT-3 OR "station d'atterrissement"
site:innovation.gouv.bj "câble sous-marin" OR ACE OR SAT-3
site:arcep.bj "câble sous-marin" OR "station d'atterrissement" OR "fibre optique"
site:celtiis.bj backbone OR "fibre optique" OR wholesale OR "datacenter"
"ACE" "Cotonou" Bénin "station" OR atterrissement OR Fidjrossè
"BENIN-IX" OR "Bénin Internet Exchange" Cotonou peering
site:peeringdb.com Benin OR Bénin Cotonou
```

---

## 8. Official cloud-region check

Run every batch against official pages:
- AWS Regions/AZs: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- Azure geographies and region list: https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/ and https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud locations: https://cloud.google.com/about/locations
- Oracle Cloud regions: https://www.oracle.com/cloud/public-cloud-regions/ and https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm

Templates:
```text
site:aws.amazon.com Benin "Region" "Availability Zone"
site:learn.microsoft.com/azure Benin "region"
site:cloud.google.com/about/locations Benin "region"
site:oracle.com/cloud Benin "cloud region"
```

As of 2026-08-12, no Benin public cloud region was verified. Grade **A** for absence from the official provider lists checked on that date.

---

## 9. Per-department official coverage map

Capitals/hubs and spellings: Alibori/Kandi; Atakora/Natitingou; Atlantique/Ouidah, Abomey-Calavi, Allada, Glo-Djigbé; Borgou/Parakou; Collines/Savalou, Dassa-Zoumé; Donga/Djougou; Kouffo/Dogbo, Aplahoué; Littoral/Cotonou; Mono/Lokossa; Ouémé/Porto-Novo, Sèmè-Kpodji; Plateau/Sakété, Pobè; Zou/Abomey, Bohicon.

| Department | Official strategy | Current expected outcome |
|---|---|---|
| **Alibori** | Search Kandi, Malanville, Banikoara with ARCEP/SBEE/commune terms. | `no_projects_expected`; telco/government rooms only unless permit/utility evidence appears. |
| **Atakora** | Search Natitingou and Atakora aliases (`Atacora`) with fibre, mairie and EIES terms. | `no_projects_expected`. |
| **Atlantique** | Search Abomey-Calavi national DC, Ouidah/Sèmè City, GDIZ/Glo-Djigbé, Allada/Ouidah permits. | Positive: national DC at Abomey-Calavi. Watch: GDIZ and Sèmè City Ouidah campus; no GDIZ DC verified. |
| **Borgou** | Search Parakou, University of Parakou, SBEE/ARCEP regional infrastructure. | `no_projects_expected`; possible government/university/server-room leads. |
| **Collines** | Search Savalou, Dassa-Zoumé, Glazoué, Savè; check commune permits and fibre/backbone. | `no_projects_expected`. |
| **Donga** | Search Djougou, Bassila, Ouaké, Copargo. | `no_projects_expected`. |
| **Kouffo** | Search Dogbo, Aplahoué, Klouékanmè with `Kouffo/Couffo` spellings. | `no_projects_expected`. |
| **Littoral** | Search Cotonou, Fidjrossè, Ganhi, Guinkomey, MTN, ISOCEL, Alink, BENIN-IX, ACE/SAT-3, permits/EIES. | Positive/operator evidence: MTN Data Center service. Connectivity assets: ACE/SAT-3/BENIN-IX. Directory leads: Alink/ISOCEL. |
| **Mono** | Search Lokossa, Comè, Grand-Popo with mairie/EIES/ARCEP terms. | `no_projects_expected`. |
| **Ouémé** | Search Porto-Novo, Sèmè-Kpodji, Adjarra, Sèmè City historical aliases. | Watch only. Current Sèmè City official main campus is Ouidah/Atlantique; no Ouémé DC facility verified. |
| **Plateau** | Search Sakété, Pobè, Kétou and industrial-zone terms. | `no_projects_expected`; watch industrial announcements. |
| **Zou** | Search Abomey, Bohicon, Covè, Zogbodomey; note MTN directory false positives such as “MTN Bohicon”. | `no_projects_expected`; verify telco-switching rooms before facility creation. |

Generic sweep for every department:
```text
"{department}" Bénin "data center" OR datacenter OR "centre de données" OR "salle de serveurs"
"{capital_or_hub}" "data center" OR datacenter OR "centre de données" OR "salle de serveurs"
"{capital_or_hub}" "permis de construire" "{operator}" OR datacenter
"{capital_or_hub}" "étude d'impact" OR "certificat de conformité" datacenter
site:arcep.bj "{capital_or_hub}" fibre OR licence OR autorisation
site:sbee.bj "{capital_or_hub}" raccordement OR "poste"
```

---

## 10. Official output guidance

Minimum record fields:
```json
{
  "country_code": "BJ",
  "division": "Atlantique",
  "commune": "Abomey-Calavi",
  "name": "Data centre national (Abomey-Calavi)",
  "operator": "ASIN / state digital agencies; SBIN attribution requires official confirmation",
  "status": "operational_or_commissioning_confirmed_by_2021",
  "capacity_mw": null,
  "area_sqm": 500,
  "tier": "Tier 3 / ANSI-TIA-942 certification process reported in 2021",
  "source_urls": [
    "https://innovation.gouv.bj/publications/actualites/datacenter-national-demarrage-des-premiers-tests-techniques-sous-le-regard-de-la-ministre-du-numerique-et-de-la-digitalisation",
    "https://lanation.bj/actualites/pour-booster-le-potentiel-numerique-au-benin-le-menc-a-pied-doeuvre-pour-un-data-center"
  ],
  "evidence_grade": "A for existence/location/testing; A-/B+ for 2019 area/mission details",
  "evidence_date": "2026-08-12"
}
```

Rules:
- Do not create Benin records from directory-only sources unless a second source verifies operator/site existence.
- Treat landing stations, IXPs and telco exchanges as connectivity assets unless a source names data-centre/colocation functionality.
- Store negative department sweeps with date and queries, not silent omissions.
- Preserve aliases in notes: `Atacora/Atakora`, `Couffo/Kouffo`, `Oueme/Ouémé`, `SBIM/SBIN`, `Sèmè-Podji/Sèmè-Kpodji`, `data center/datacenter/centre de données`.
