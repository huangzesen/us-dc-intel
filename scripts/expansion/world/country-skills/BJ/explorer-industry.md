# BJ Explorer Industry - Benin Datacenter Enumeration via Operators, Connectivity, Peering, Trade Press and Directories

Date: 2026-08-12. Country: **BJ Benin**. Division model: **12 departments**: Alibori, Atakora, Atlantique, Borgou, Collines, Donga, Kouffo, Littoral, Mono, Oueme/Ouémé, Plateau, Zou. Search aliases: `Atacora`, `Couffo`, `Oueme`, `Sèmè-Podji`, `Sèmè-Kpodji`.

Scope: industry and market evidence complementing `explorer-official.md`: operator pages, colocation products, government-DC records, directories, subsea/IXP sources, trade press and Benin business media.

Reliability grades:
- **A** = official operator/government facility page, official operator service page, official cloud-region page, Uptime Institute award page, regulator record, official IXP/subsea/operator page.
- **A-** = official operator/government announcement proving a project/service or named site but without permit, energy, regulator or commissioning details.
- **B** = established trade press or reputable local/pan-African business press with specific parties, dates, locations and status. PeeringDB is **B** for peering/exchange facts.
- **C** = directories, marketplace pages, SEO lists, social posts, Wikipedia, unsourced market reports and capacity tables. Discovery only unless corroborated.

Grade claims separately. Example: MTN Bénin has **A** evidence for a current official `Data Center` business product, **B** for the June 2019 launch date from CIO Mag, and **C** for any unverified rack/MW count.

---

## 0. Benin market facts

- Benin is a small, Cotonou/Abomey-Calavi-led market. Verified positives are the **national data centre in Abomey-Calavi** and **MTN Bénin Data Center** business product. Alink and ISOCEL appear in data-centre directories but need operator/permit confirmation before being counted as verified colocation facilities.
- The national DC is the flagship state facility: Abomey-Calavi, ministry-confirmed testing from 2021-06-01, dual fibre/secure power, Tier 3 ANSI/TIA-942 certification process, and 2019 La Nation reporting of a two-hectare site and 500 sqm technical block.
- Connectivity assets are strong but DC-adjacent: ACE cable lands at Cotonou/Fidjrossè; SAT-3/WASC has Cotonou station references; BENIN-IX is in Cotonou; SBIN/Celtiis operates national infrastructure. Do not count these as commercial DCs unless a facility/colocation source says so.
- No AWS, Azure, Google Cloud or Oracle public cloud region in Benin was verified on official region pages as of 2026-08-12.
- Pipeline: World Bank WARDIP procurement OP00432980 for a secondary/redundancy national DC feasibility study. The site is TBD and may be outside Benin; do not create a facility until a selected site is published.
- Announced MW is rare. Keep source units (`sqm`, racks, product wording, Tier/TIA) and leave `capacity_mw = null` unless an official/operator source publishes MW.

---

## 1. Facility and lead census

| Facility / operator | Department / location | Status handling | Best current evidence | Grade |
|---|---|---|---|---|
| **Data centre national (Abomey-Calavi)** | Atlantique - Abomey-Calavi | Confirmed state facility. Ministry page proves site/testing on 2021-06-01, secure power, dual fibre and Tier 3 certification process. La Nation 2019 gives two-hectare site and 500 sqm technical block. Treat commercial colo as unconfirmed. | https://innovation.gouv.bj/publications/actualites/datacenter-national-demarrage-des-premiers-tests-techniques-sous-le-regard-de-la-ministre-du-numerique-et-de-la-digitalisation ; https://lanation.bj/actualites/pour-booster-le-potentiel-numerique-au-benin-le-menc-a-pied-doeuvre-pour-un-data-center | A for existence/location/testing; A-/B+ for 2019 site details |
| **MTN Bénin Data Center / MTN Data Center Collocation Pro** | Littoral - Cotonou (MTN Bénin HQ/service base) | Confirmed official enterprise data-centre/colocation product. CIO Mag reports launch on 2019-06-14 for startups and enterprises. No official MW/rack/site technical specs found. | https://www.mtn.bj/business/connectivite/data-center/ ; https://www.mtn.bj/mtn-data-center-pro/ ; https://cio-mag.com/mtn-benin-lance-son-service-data-center/ | A for current official product; B for 2019 launch date |
| **Alink Telecom Cotonou Datacenter** | Littoral - Cotonou (Guinkomey/Rue des Dako Donou aliases) | Directory-listed data centre/colocation lead. Alink ISP/company presence is corroborated by ISP directories, but no official Alink DC page, permit or regulator DC record was verified. | https://datacenterplatform.com/data-centers/alink-telecom/alink-telecom-cotonou-datacenter/ ; https://www.africa-internet.com/en/provider/benin/alink-telecom/ ; https://www.goafricaonline.com/bj/108693-alink-telecom-telecommunication-cotonou-benin | C for DC; B/C for ISP/company presence |
| **ISOCEL Telecom / ISOCEL SA Cotonou** | Littoral - Cotonou; network presence also Porto-Novo | Directory-listed Cotonou data-centre lead. ISOCEL official site confirms telecom/ISP activity and ACE news, but no official DC service page was verified. | https://isoceltelecom.com/ ; https://isoceltelecom.com/isonews/le-benin-desormais-dote-de-son-second-cable-sous-marin/ ; https://datacenterplatform.com/data-centers/isocel-telecom/ ; https://www.datacenterslist.com/data-centers/isocel-sa-cotonou | B for operator/connectivity; C for DC |
| **SBIN / Celtiis** | National; HQ/service base Cotonou | State infrastructure/operator lead. Official Celtiis/Sonatel pages support SBIN/Celtiis telecom role; directory/social claims of the Abomey-Calavi DC operator require official confirmation. | https://celtiis.bj/a-propos ; https://sonatel.sn/sonatel-nouveau-partenaire-strategique-de-la-sbin-au-benin/ ; https://www.datacentermap.com/benin/abomey-calavi/benin-national-data-center/ | A/B for telecom role; C for directory-only DC operator attribution |
| **Bénin Télécoms SA / legacy telecom rooms** | Littoral - Cotonou | Legacy operator/server-room lead only. No public colocation/DC facility verified. | https://www.globenin.com/annuaire/benin-telecoms-sa-benin-1318 ; https://fr.wikipedia.org/wiki/Bénin_Télécoms_SA | C lead |
| **Moov Africa Bénin** | Littoral - Cotonou; national network | Telecom/operator lead only. No Benin DC facility or product page verified in this pass. | Search operator site and ARCEP decisions each batch; avoid using unrelated Maroc Telecom group DC news as Benin proof. | C lead |
| **Open BJ / local hosting firms** | Littoral - Cotonou | Hosting/cloud-service lead. Do not create physical DC record without infrastructure/location proof. | https://www.open.bj/ | C/B service lead |
| **Sèmè One / Sèmè City data-centre mention** | Current official main campus: Atlantique - Ouidah; historical/search aliases: Ouémé - Sèmè-Kpodji | Watch item only. Current Sèmè City site confirms Ouidah campus, and third-party pages mention a Sèmè One data centre. No official Sèmè City DC page/location/capacity was verified. | https://semecity.bj/ ; https://semecity.bj/fr/campus/campus-ouidah/ ; https://www.wearetech.africa/en/fils-uk/tech-stars/seme-city-benin-s-innovation-and-knowledge-city | A for Ouidah campus; C/B for data-centre mention |
| **ACE landing station** | Littoral - Cotonou/Fidjrossè | Connectivity asset, not commercial DC. Official ACE route includes Cotonou; press reports service in 2015 and Fidjrossè/SAT-3 visits. | https://ace-submarinecable.com/le-cable-sous-marin/ ; https://www.agenceecofin.com/infrastructures/1610-33176-le-benin-a-mis-en-service-le-cable-sous-marin-de-fibre-optique-ace ; https://lanation.bj/actualites/visite-du-mctic-dans-les-stations-ace-et-sat-3-etienne-kossi-senquiert-de-letat-davancement-des-deux-sites | A for cable landing; B for press details |
| **SAT-3/WASC Cotonou station** | Littoral - Cotonou/Fidjrossè | Connectivity asset. Verify against official/operator sources before facility creation. | https://geocables.com/location/cotonou-benin?lang=fr ; https://fr.slideshare.net/slideshow/sation-de-cable-sous-marin-sat3-cotonou/69587201 | C/B lead |
| **BENIN-IX** | Littoral - Cotonou | IXP/peering asset; use member and facility records to pivot to operators. | https://www.peeringdb.com/ix/1017 ; https://www.peeringdb.com/org/10706 | B |
| **WARDIP secondary national DC** | TBD | Pipeline feasibility study only; submissions due 2026-03-27 per DCD, with World Bank procurement OP00432980 as primary source. | https://projects.worldbank.org/en/projects-operations/procurement-detail/OP00432980 ; https://documents.worldbank.org/en/publication/documents-reports/documentdetail/966521635044503175 ; https://www.datacenterdynamics.com/en/news/benin-wants-to-establish-a-secondary-national-data-center/ | A for procurement/document landing page; B for trade-press summary |
| **GDIZ / Glo-Djigbé Industrial Zone** | Atlantique - Glo-Djigbé/Abomey-Calavi | Strategic watch zone only. No DC project verified inside GDIZ. | https://gdiz-benin.com/ ; https://www.ariseiip.com/project/gdiz/ ; https://www.gouv.bj/article/1567/amenagement-zone-industrielle-djigbe-gdiz-vaste-projet-veut-etre-industriel-sous-region/ | A for zone; no DC grade |

Operator census queries:
```text
"Bénin" "data center" OR datacenter OR "centre de données" "{operator}" lancement OR inauguration OR opérationnel OR "Tier III"
"Cotonou" "data center" colocation OR hébergement OR "carrier-neutral" -Nigeria -Kenya
"{operator}" Bénin "centre de données" OR "salle de serveurs" OR datacenter OR racks
"{operator}" Bénin "Uptime Institute" OR "TIA-942"
"{operator}" Bénin "permis de construire" OR "étude d'impact" OR "certificat de conformité"
site:mtn.bj "Data Center" OR datacenter OR colocation
site:isoceltelecom.com datacenter OR "data center" OR hébergement
site:alinktelecom.bj datacenter OR "data center" OR hébergement OR colocation
```

Alias rules:
- National DC = `data center national`, `datacenter national`, `centre de données national`, Abomey-Calavi.
- SBIN is correct; `SBIM` in some DCD/directory text is likely a typo and must not be normalized without a note.
- Alink Benin must not be confused with Alink entities in other African countries.
- ISOCEL Telecom / ISOCEL SA are likely same operator context; dedupe carefully.
- Sèmè City originally/historically used Sèmè-Kpodji/Sèmè-Podji associations, but the current main campus page says Ouidah.

---

## 2. Hyperscaler and cloud-provider status

Official pages to check every run:
- AWS: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- Azure: https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies/ and https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud: https://cloud.google.com/about/locations
- Oracle Cloud: https://www.oracle.com/cloud/public-cloud-regions/ and https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm

As of 2026-08-12, none lists a Benin public cloud region. Do not create a Benin hyperscale/cloud-region facility from:
- CDN/cache/edge nodes;
- local managed hosting or resellers;
- offices, partner pages or customer references;
- “data residency” marketing without an official region/location page.

Cloud queries:
```text
site:aws.amazon.com Benin "Region" "Availability Zone"
site:learn.microsoft.com/azure Benin "region"
site:cloud.google.com/about/locations Benin "region"
site:oracle.com/cloud Benin "cloud region"
"Benin" "AWS region" OR "Azure region" OR "Google Cloud region" OR "Oracle Cloud region"
```

---

## 3. Connectivity, subsea and IXP evidence

Connectivity evidence is useful for facility discovery but not sufficient for facility creation.

Verified/usable sources:
- ACE cable official route page includes **Cotonou, Benin**: https://ace-submarinecable.com/le-cable-sous-marin/ . **A**.
- Agence Ecofin reported the ACE cable service in Benin in 2015: https://www.agenceecofin.com/infrastructures/1610-33176-le-benin-a-mis-en-service-le-cable-sous-marin-de-fibre-optique-ace . **B**.
- La Nation reported ministerial visits to ACE and SAT-3 stations: https://lanation.bj/actualites/visite-du-mctic-dans-les-stations-ace-et-sat-3-etienne-kossi-senquiert-de-letat-davancement-des-deux-sites . **B+**.
- BENIN-IX PeeringDB exchange page: https://www.peeringdb.com/ix/1017 and org page https://www.peeringdb.com/org/10706 . **B**.
- PeeringDB network pivots: MTN BENIN `AS37424`, ISOCEL SA `AS37090`, BENIN-IX. Use to find operator facility/peering metadata, not as DC proof.
- GeoCables Cotonou page: https://geocables.com/location/cotonou-benin?lang=fr . **C/B-** discovery source. The “third cable” claim must be resolved with operator/landing-party evidence before ingesting.

Connectivity queries:
```text
"landing station" Cotonou Bénin submarine ACE OR SAT-3
site:ace-submarinecable.com Cotonou Benin
site:isoceltelecom.com ACE OR "câble sous-marin" OR Fidjrossè
site:arcep.bj "câble sous-marin" OR "fibre optique" OR "station d'atterrissement"
"BENIN-IX" OR "Bénin Internet Exchange" Cotonou peering members
"Cotonou" "câble sous-marin" 2Africa OR MainOne OR Equiano OR WACS
site:peeringdb.com Benin OR Bénin Cotonou facility
```

---

## 4. Trade press and market feeds

| Source | URL | Use | Grade |
|---|---|---|---|
| DatacenterDynamics | https://www.datacenterdynamics.com/ | Benin national DC, WARDIP secondary DC, regional DC context | B+ |
| Agence Ecofin | https://www.agenceecofin.com/ | Telecom/infra, ACE, ARCEP, operators | B+ |
| CIO Mag | https://cio-mag.com/ | MTN launch and digital government service coverage | B |
| La Nation | https://lanation.bj/ | National daily; official visits/projects, ACE/SAT-3, public infrastructure | B+ / A- when reporting ministerial site visits |
| 24 Heures au Bénin | https://www.24haubenin.bj/ | Local launches and regulator/government news | B-/C+ |
| OSIRIS | https://www.osiris.sn/ | Senegalese/francophone mirror of MTN launch and telecom news | C+/B- |
| La Nouvelle Tribune | https://lanouvelletribune.info/ | Benin economy/GDIZ/ICT leads | B-/C+ |
| Banouto, Bénin Intelligent, Fraternité, Le Matinal, Matin Libre | outlet domains | Local ICT/project leads requiring official confirmation | C+/B- |
| PeeringDB | https://www.peeringdb.com/ | IXP and ASN peering facts | B |
| Directories | DataCenterMap, DataCenterPlatform, DataCenters.com, DataCentersList, GoAfricaOnline, Globenin, Africa Internet | Facility/operator leads and aliases | C unless linked to operator evidence |
| Market reports | Arizton, Mordor, Xalam, Africa DCA, generic SEO pages | Macro sizing only | C |

Feed queries:
```text
site:datacenterdynamics.com Benin "data center" OR "national data center"
site:agenceecofin.com Bénin "data center" OR "centre de données" OR câble OR numérique
site:cio-mag.com Bénin "data center" OR datacenter OR numérique
site:lanation.bj "data center" OR datacenter OR "centre de données" OR numérique
site:24haubenin.bj "data center" OR datacenter OR "centre de données" OR MTN
"Bénin" "data center" OR datacenter OR "centre de données" annonce OR inauguration OR lancement OR construction
"Bénin" "data center" MW OR racks OR "Tier III" OR colocation
```

---

## 5. Directories and use limits

Directory pages are allowed for discovery but not final proof.

Directory queries:
```text
site:datacentermap.com/benin "data center" OR "data centre"
site:datacenterplatform.com Benin OR Cotonou data center
site:datacenters.com/benin Cotonou "data center"
site:datacenterslist.com Benin OR Cotonou
site:peeringdb.com Benin OR Bénin facility OR ix
site:goafricaonline.com/bj "data center" OR télécommunications
site:africa-internet.com/en/provider/benin "{operator}"
```

Rules:
- Never ingest directory-only MW/racks/sqm as operational capacity.
- Directory-only facilities (`Alink`, `ISOCEL`, possible `MTN Bohicon`) require operator/regulator/permit confirmation before production records.
- DataCenterMap says national DC is 300 sqm and operated by SBIN; La Nation says 500 sqm technical block and ASSI project-side role. Keep both source-tagged; prefer ministry/official records for final core facts.
- Treat marketplace descriptions with generic “redundant power/cooling” text as boilerplate unless backed by operator documentation.

---

## 6. Industry bodies, certification and events

- Uptime Institute search: https://uptimeinstitute.com/ . No Benin award record was verified in this pass. Use `site:uptimeinstitute.com Benin "Data Center"` and `site:uptimeinstitute.com "Bénin" "Tier"` each batch.
- TIA-942/Tier claims for the national DC come from ministry/La Nation wording about certification process; do not record an awarded certificate unless a certificate issuer/official award page is found.
- No dedicated Benin data-centre association was verified. Use ISP/telco associations, CCI Bénin and AfPIF/Datacloud Africa materials only as leads.

Queries:
```text
site:uptimeinstitute.com Benin "Data Center"
"Bénin" "Uptime Institute" "Tier III" OR "Tier IV"
"Bénin" "ANSI/TIA-942" datacenter OR "centre de données"
"AfPIF" Cotonou OR Bénin peering
"Datacloud Africa" Bénin data centre
"CCI Bénin" numérique OR "data center"
```

---

## 7. Per-department industry discovery map

| Department | Search set | Expected result / coding guidance |
|---|---|---|
| **Alibori** | `"Kandi" Bénin "data center" OR "salle de serveurs"`; `"Alibori" numérique OR ICT OR fibre`; `site:arcep.bj Kandi fibre` | Expected negative for commercial DC; store `no_projects: true` unless telco/government room evidence is unusually strong. |
| **Atakora** | `"Natitingou" "centre de données" OR "salle de serveurs"`; `"Atacora" OR "Atakora" Bénin numérique OR fibre` | Expected negative. |
| **Atlantique** | `"Abomey-Calavi" data center OR datacenter`; `"GDIZ" OR "Glo-Djigbé" "data center" OR datacenter`; `"Ouidah" "Sèmè City" "data center"`; `site:semecity.bj Ouidah "Sèmè One"` | Positive national DC. Watch GDIZ and Sèmè City/Ouidah. |
| **Borgou** | `"Parakou" "data center" OR "centre de données" OR "salle de serveurs"`; `"UP Parakou" serveurs`; `"Borgou" numérique OR fibre` | Expected negative; possible university/government/server-room leads only. |
| **Collines** | `"Savalou" OR "Dassa-Zoumé" "centre de données" OR serveurs`; `"Collines" Bénin numérique` | Expected negative. |
| **Donga** | `"Djougou" "centre de données" OR "salle de serveurs"`; `"Donga" Bénin numérique OR fibre` | Expected negative. |
| **Kouffo** | `"Dogbo" OR "Aplahoué" "salle de serveurs" OR "centre de données"`; `"Kouffo" OR "Couffo" Bénin numérique` | Expected negative. |
| **Littoral** | `"Cotonou" "data center" OR datacenter OR "centre de données" colocation OR hébergement`; `"MTN" Bénin "data center"`; `"Fidjrossè" "câble sous-marin"`; `"Alink" OR "ISOCEL" Cotonou datacenter`; `"BENIN-IX" Cotonou` | Positive cluster: MTN product, landing stations, IXP; directory leads Alink/ISOCEL. Dedupe before counting. |
| **Mono** | `"Lokossa" "centre de données" OR "salle de serveurs"`; `"Mono" Bénin numérique OR fibre` | Expected negative. |
| **Ouémé** | `"Porto-Novo" "data center" OR "salle de serveurs"`; `"Sèmè-Kpodji" OR "Sèmè-Podji" "data center"`; `"Sèmè One" data center`; `ISOCEL Porto-Novo` | Watch only; current Sèmè City main campus is Ouidah/Atlantique, not proof of Ouémé DC. |
| **Plateau** | `"Pobè" OR "Sakété" "centre de données" OR serveurs`; `"Plateau" Bénin "zone industrielle" OR numérique` | Expected negative; watch SEZ/park announcements. |
| **Zou** | `"Abomey" OR "Bohicon" "centre de données" OR "salle de serveurs"`; `"MTN Bohicon" datacenter`; `"Zou" Bénin numérique OR fibre` | Expected negative for commercial DC. Treat `MTN Bohicon` directory entries as telco/network leads until official DC evidence appears. |

For negative departments, output dated query notes. Do not omit a department because no facility is found.

---

## 8. Verification workflow

1. Seed only from **A/A-** and strong **B** sources: ministry national-DC pages, MTN official product pages, World Bank WARDIP procurement, ACE official page, BENIN-IX PeeringDB, SBIN/Celtiis official pages.
2. Dedupe aliases before counting: national DC/ASSI/ASIN/SBIN; ISOCEL/ISOCEL SA; Alink Benin vs other countries; MTN service pages vs directory entries.
3. Assign `division` by physical facility location, not headquarters. When location is uncertain, mark `division_unverified` and keep as lead.
4. Split status and capacity fields: `status`, `operational_capacity_mw`, `announced_capacity_mw`, `racks`, `area_sqm`, `tier`, `source_date`, `source_grade`.
5. Escalate each industry lead through `explorer-official.md`: commune permit -> ABE/EIES -> energy -> ARCEP -> APDP/company -> ASIN/ministry/operator.
6. Run cloud-region and subsea checks each batch. Do not ingest unverified Equiano/2Africa/MainOne Benin landing claims.
7. Sweep all 12 departments and explicitly output `no_projects: true` where appropriate.

Recommended output schema:
```json
{
  "country_code": "BJ",
  "country_name": "Benin",
  "division": "Littoral",
  "commune": "Cotonou",
  "name": "MTN Bénin Data Center",
  "status": "service_offered",
  "operator": "MTN Bénin / SPACETEL BENIN",
  "capacity_mw": null,
  "announced_capacity_mw": null,
  "racks": null,
  "area_sqm": null,
  "tier": null,
  "source_urls": [
    "https://www.mtn.bj/business/connectivite/data-center/",
    "https://www.mtn.bj/mtn-data-center-pro/",
    "https://cio-mag.com/mtn-benin-lance-son-service-data-center/"
  ],
  "evidence_date": "2026-08-12",
  "evidence_grade": "A for current official product; B for 2019 launch date",
  "notes": "No public MW/rack/site technical specs verified."
}
```

---

## 9. Common false positives

- Directory counts listing four Benin data centers without primary/operator evidence.
- `SBIM` as a supposed operator name; keep note that the likely intended state company is **SBIN**, but do not silently correct source text.
- Sèmè City location confusion: current official main campus page says Ouidah/Atlantique; historical Sèmè-Kpodji/Ouémé references are search aliases.
- Equiano, 2Africa, MainOne or WACS Benin landing claims from maps/directories without landing-party evidence.
- Telco switching rooms, mobile core sites and branches represented as “data centers” by directories.
- Hosting/VPS/cloud companies treated as physical colocation facilities without a site/infrastructure source.
- MTN Data Center product treated as a large hyperscale facility; no public MW/rack/certification source was found.
- National DC 300 sqm vs 500 sqm conflict; source-tag both until an ASIN/SBIN official technical sheet resolves it.
- GDIZ digital-industrial promotion treated as an active DC project; no DC in GDIZ was verified.

## Final confidence notes

- **High confidence (A)**: national data centre exists at Abomey-Calavi; MTN Bénin has an official Data Center/Collocation Pro product; ACE lands at Cotonou; no Benin hyperscaler region; WARDIP secondary-DC feasibility procurement exists.
- **Medium confidence (B)**: MTN launch date in June 2019; BENIN-IX Cotonou peering record; ISOCEL/Alink as real telecom/ISP actors; SAT-3 Cotonou station from secondary/technical sources.
- **Low confidence (C)**: Alink and ISOCEL physical DC details/capacity; Sèmè One data-centre claim; Moov/Bénin Télécoms/Celtiis standalone DC products; third cable identity at Cotonou.
