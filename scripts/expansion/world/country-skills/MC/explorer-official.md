# MC Explorer Official - Monaco Datacenter Enumeration via Government, Permits, Energy, Cybersecurity, and Public-Sector Sources

Date: 2026-08-12. Scope: Monaco (MC), covering all 17 repo divisions: La Colle, La Condamine, Fontvieille, La Gare, Jardin Exotique, Larvotto, Malbousquet, Monte-Carlo, Moneghetti, Monaco-Ville, Moulins, Port-Hercule, Sainte-Devote, La Source, Spelugues, Saint-Roman, Vallon de la Rousse.

Reliability grades: **A** = official/primary source (gouv.mc, monservicepublic.gouv.mc, Journal de Monaco, SMEG, AMSN, APDP, operator certificate or operator official page); **B** = named-party trade/local press; **C** = directory, marketplace, SEO page, or unverified aggregate. Use the grade of the source that proves the specific field. Do not promote a directory address to Grade A unless an official page, certificate, gazette notice, or operator filing confirms it.

---

## 0. Monaco-specific structure

- Monaco is a city-state with one commune. There are no provincial planning authorities to search. Building and development evidence is centralised through the Prince's Government, the **Département de l'Équipement, de l'Environnement et de l'Urbanisme (DEEU)**, the **Direction de la Prospective, de l'Urbanisme et de la Mobilité (DPUM)**, the **Direction des Travaux Publics**, and legal notices in the **Journal de Monaco**.
- The working divisions for this repo are 17 quarters. Assign a facility by its physical address, not by a head office, sales office, registered office, telecom POP, or customer site.
- Monaco's confirmed datacentre evidence is small and concentrated around official telecom/sovereign-cloud infrastructure:
  - **Monaco Telecom**: operator official page says the hosting platform is based on 3 data centers in the Principality. The current ISO/HDS certificate is the best official site-level evidence: `4-6 avenue Albert II - Zone F` (primary/head office and DC3), `25 boulevard de Suisse` (Centre de données n°1), and `Zone F, 4-6 avenue Albert II` (Centre de données n°6). Source: https://monaco-telecom.mc/en/data-center/ and certificate PDF https://monaco-telecom.mc/wp-content/uploads/2025/12/Certificats-MT_V2.pdf
  - **Monaco Telecom DC3**: Journal de Monaco created a protected zone for Data Center n°3 at the 4th floor of the Zone F building, `6 avenue Albert II`. Source: https://journaldemonaco.gouv.mc/fr/Journaux/2019/Journal-8435/Arrete-Ministeriel-n-2019-452-du-16-mai-2019-creant-une-zone-protegee-au-Data-Center-n-3-de-Monaco-Telecom
  - **Monaco Telecom Larvotto Supérieur project**: Journal de Monaco tender notice says the public housing project includes a Monaco Telecom data center of about 1,600 m2 on levels R-3/R-4, with works max 36 months. Treat as proposed/under-development until delivery is verified. Source: https://journaldemonaco.gouv.mc/switchlanguage/to/jdm_eng/Journaux/2023/Journal-8649/Avis-d-Appel-Public-a-Candidatures-Larvotto-Superieur-pour-la-Direction-des-Travaux-Publics-de-la-Principaute-de-Monaco
  - **Telis / MonacoDATACENTER**: Telis official pages state MonacoDATACENTER was created/opened in 2013 as Monaco's first green datacenter, located at `14 avenue de Grande-Bretagne`, ISO 27001/HDS certified, Tier III-designed, and seawater/thalassothermal cooled. Sources: https://www.telis.mc/digital-solutions/it-systems/ , https://www.telis.mc/development-and-innovation/ , https://www.telis.mc/labels-and-certifications/ , https://www.telis.mc/it-and-digital-transformation-partner-in-monaco/
  - **Monaco Cloud**: sovereign cloud operator, not a separate public colocation facility unless a site is separately evidenced. Monaco Cloud official page says it is state-majority, data under Monegasque law, AMSN-qualified (PINH Avancé and PSSI-E), multi-site, and headquartered at `9 avenue Albert II - Le Copori`. Source: https://www.monacocloud.mc/presentation and https://www.monacocloud.mc/
  - **Government DSI/DRSI**: Journal de Monaco created a protected zone for the DRSI computer room at `23 avenue Albert II`. Count only as a public-sector server room unless a facility-level hosting role is proven. Source: https://journaldemonaco.gouv.mc/Journaux/2019/Journal-8435/Arrete-Ministeriel-n-2019-453-du-16-mai-2019-creant-une-zone-protegee-au-sein-de-la-Direction-des-Reseaux-et-Systemes-d-Information
- Monaco has no public AWS, Azure, Google Cloud, or OCI region. Verify absence against the providers' own region pages before rejecting or accepting any "hyperscale Monaco" claim:
  - AWS: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html
  - Azure: https://learn.microsoft.com/en-us/azure/reliability/regions-list
  - Google Cloud: https://cloud.google.com/about/locations
  - Oracle OCI: https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm
- Cross-border trap: Cap-d'Ail, Beausoleil, Roquebrune-Cap-Martin, Nice, Sophia Antipolis, and CHPG Cap Fleuri are France, not Monaco. Do not assign French sites to MC divisions.

---

## 1. Grade A official/regulatory sources

### 1.1 Planning, works, and gazette

Use these first for development status:

- DEEU: https://www.gouv.mc/Gouvernement-et-Institutions/Le-Gouvernement/Departement-de-l-Equipement-de-l-Environnement-et-de-l-Urbanisme
- DEEU directory: https://monservicepublic.gouv.mc/annuaire-des-services-administratifs/departement-de-l-equipement-de-l-environnement-et-de-l-urbanisme
- DPUM: https://monservicepublic.gouv.mc/annuaire-des-services-administratifs/departement-de-l-equipement-de-l-environnement-et-de-l-urbanisme/direction-de-la-prospective-de-l-urbanisme-et-de-la-mobilite
- Building-permit procedure: https://monservicepublic.gouv.mc/thematiques/logement/domicile/travaux/demander-un-permis-de-construire
- Works/authorisation procedure hub: https://monservicepublic.gouv.mc/thematiques/logement/domicile/travaux
- Journal de Monaco: https://journaldemonaco.gouv.mc/
- Urbanism regulations and quarter plans: Journal de Monaco / MonServicePublic annexes to Ordonnance Souveraine n°4.482 and later updates, including the 2024 modification: https://journaldemonaco.gouv.mc/fr/Journaux/2024/Journal-8708/Ordonnance-Souveraine-n-10.743-du-5-aout-2024-modifiant-les-dispositions-de-l-Ordonnance-Souveraine-n-4.482-du-13-septembre-2013-portant-delimitation-et-reglement-d-urbanisme-du-secteur-des-quartiers-ordonnances-modifiee

Journal de Monaco high-confidence records already verified:

| Record | Evidence | Use |
|---|---|---|
| Arrêté Ministériel n°2019-452, Journal n°8435, 24/05/2019 | Protected zone for the computer room in Monaco Telecom Data Center n°3, 4th floor, Zone F building, `6 avenue Albert II` | Grade A physical site proof for MT DC3; map to Fontvieille unless local quarter geometry proves otherwise |
| Arrêté Ministériel n°2019-453, Journal n°8435, 24/05/2019 | Protected DRSI computer room, 1st floor, `23 avenue Albert II` | Grade A public-sector server-room proof; not commercial colo |
| Avis d'appel public à candidatures Larvotto Supérieur, Journal n°8649, 30/06/2023 | Project includes Monaco Telecom data center of about 1,600 m2 on levels R-3/R-4; 36-month maximum works period | Grade A proposed/under-development datacenter project; map to Larvotto/Saint-Roman only after address/quarter confirmation |
| Monaco Cloud S.A.M. constitution/statutes notices, 2020-2022 | Legal existence, capital/statutes, office evidence | Grade A entity proof; not a facility proof |

Gazette query templates:

```text
site:journaldemonaco.gouv.mc "data center" "Monaco Telecom"
site:journaldemonaco.gouv.mc "centre de données" Monaco
site:journaldemonaco.gouv.mc "salle informatique" "Monaco Telecom"
site:journaldemonaco.gouv.mc "zone protégée" "Data Center"
site:journaldemonaco.gouv.mc "Larvotto Supérieur" "data center"
site:journaldemonaco.gouv.mc "Monaco Cloud S.A.M."
site:journaldemonaco.gouv.mc "Telis" "MonacoDATACENTER"
site:journaldemonaco.gouv.mc "avenue Albert II" "salle informatique"
site:journaldemonaco.gouv.mc "boulevard de Suisse" "centre de données"
site:journaldemonaco.gouv.mc "avenue de Grande-Bretagne" "datacenter"
```

Extract from each official notice:

- document type, number, Journal issue, publication date, and URL;
- applicant / beneficiary / operator;
- exact address, building, floor/level, and quarter;
- project wording: data center, salle informatique, local technique, protected zone, substations, generators, cooling;
- disclosed size, racks, duration, works status, certifications, or security classification;
- whether the source proves an operational site, a proposed project, a server room, or only a company/legal entity.

### 1.2 Energy and grid

- **SMEG**: https://www.smeg.mc/ - sole Monaco electricity/gas distributor and a critical source for connection, transformer, power, backup-feed, and thalassothermal network evidence.
- **Direction de la Transition Énergétique**: https://transition-energetique.gouv.mc/ - official policy source for energy-transition constraints, thalassothermy/SeaWergie, and efficient-building context.
- Use Monaco Life / Monaco-Matin outage reporting only as Grade B unless backed by SMEG or Monaco Telecom. The 29 November 2022 Monaco Telecom outage identifies a Zone J Fontvieille data centre, maintenance disconnection from the SMEG grid, generator failure, and emergency reconnection to SMEG; useful resilience evidence, not official capacity evidence. Source: https://monacolife.net/what-caused-monaco-telecoms-worst-outage-in-25-years/

Energy queries:

```text
site:smeg.mc "data center"
site:smeg.mc "centre de données"
site:smeg.mc "Monaco Telecom" raccordement
site:smeg.mc "Larvotto Supérieur"
site:transition-energetique.gouv.mc thalassothermie Fontvieille
site:transition-energetique.gouv.mc SeaWergie Larvotto
"SMEG" "Monaco Telecom" "data centre"
"SMEG" "Zone J" "Monaco Telecom"
"SeaWergie" "data center" Monaco
```

### 1.3 Cybersecurity, protected zones, and data protection

- **AMSN**: https://amsn.gouv.mc/ - Monaco cybersecurity agency. Use for qualified products/services, OIV context, CERT-MC, PINH/PSSI-E references, and protected-zone context.
- **AMSN qualified services page**: https://amsn.gouv.mc/produits-et-services-qualifies/services-qualifies - confirms the PINH category and is the place to re-check qualified hosting/cloud services.
- **APDP**: https://apdp.mc/ - data-protection authority, successor to CCIN under Law n°1.565 of 3 December 2024. Use data-protection filings only as corroborating evidence for hosting/vendor choices; it is not normally a facility index.
- **Journal protected-zone records** are high-value security evidence: MT DC3 and DRSI have explicit 2019 protected-zone arrêtés.

Cyber/regulator queries:

```text
site:amsn.gouv.mc "Monaco Cloud" "PINH"
site:amsn.gouv.mc "PSSI-E" "Monaco Cloud"
site:amsn.gouv.mc "Monaco Telecom" "OIV"
site:amsn.gouv.mc "data center"
site:apdp.mc "Monaco Cloud"
site:apdp.mc "Monaco Telecom" hébergement
site:apdp.mc "Telis" hébergement
```

### 1.4 Public-sector digital infrastructure

- **Extended Monaco**: https://extendedmonaco.com/ - national digital strategy context.
- **Monaco Cloud**: https://www.monacocloud.mc/ and https://www.monacocloud.mc/presentation - Grade A for sovereign-cloud status, multi-site service wording, state-majority ownership, local legal governance, AMSN qualification, and office address `9 avenue Albert II - Le Copori`.
- **Data Monaco**: https://data.gouvernement.mc/ - official open-data portal. Useful for telecom-infrastructure context, addresses, and mapping; not a datacentre census.
- **DSI/DRSI**: use government directory and Journal de Monaco protected-zone records. Treat `23 avenue Albert II` as a government IT room unless a source proves public hosting/colo activity.

Queries:

```text
site:gouv.mc "Monaco Cloud" "Amazon"
site:gouv.mc "cloud souverain" Monaco
site:gouv.mc "Direction des Systèmes d'Information" "avenue Albert II"
site:gouv.mc "Direction des Réseaux et Systèmes d'Information"
site:data.gouvernement.mc antennes Monaco Telecom
site:monacocloud.mc "multi-site"
site:monacocloud.mc "PINH Avancé"
```

---

## 2. Quarter coverage workflow

Run the sweep for every one of the 17 divisions, even when the expected yield is zero.

| Division | Expected signal | Official-first method |
|---|---|---|
| Fontvieille | Highest yield: Avenue Albert II / Zone F, Le Copori, Les Terrasses de Fontvieille, Telis at Avenue de Grande-Bretagne, DSI/DRSI, Monaco Telecom HQ/DC3/DC6 evidence | Journal de Monaco protected-zone notices; Monaco Telecom certificate; Telis pages; Monaco Cloud pages; DEEU/DPUM works |
| Monte-Carlo | Monaco Telecom `25 boulevard de Suisse` is official certificate evidence for Centre de données n°1; also many head offices and hotel/bank server rooms | Monaco Telecom certificate first; verify address-to-quarter carefully; do not count bank/casino offices without facility evidence |
| Larvotto | Larvotto Supérieur project includes future/proposed Monaco Telecom data center | Journal n°8649 tender; construction updates; DPUM/DTP; DCD/local press as secondary |
| Saint-Roman | Adjacent to Boulevard du Larvotto upper/eastern area; possible mapping ambiguity for Larvotto Supérieur depending on repo geometry | Resolve using repo boundary data or authoritative Monaco map before assigning |
| Monaco-Ville | Government seat; no known commercial DC | Journal/gouv searches only; likely no record |
| La Condamine | Business/harbour adjacency; no known commercial DC | Gazette, SMEG, AMSN; reject head-office-only hits |
| Port-Hercule | Connectivity and event infrastructure; no known commercial DC | Gazette, SMEG, AMSN; reject event telecom rooms unless facility-level |
| Moulins / Spelugues | Casino/hotel/bank IT likely in-house; no public colo known | SBM/bank official records only if physical server-room evidence appears |
| La Colle, La Gare, Jardin Exotique, Malbousquet, Moneghetti, Sainte-Devote, La Source, Vallon de la Rousse | Low yield/residential/infrastructure-adjacent | Generic official search; require Grade A/B facility evidence before recording |

Quarter search template:

```text
"{quarter}" Monaco "data center"
"{quarter}" Monaco "centre de données"
"{quarter}" Monaco datacenter
"{quarter}" Monaco "salle informatique"
"{quarter}" Monaco "salle de serveurs"
"{quarter}" "Monaco Telecom"
"{quarter}" "Monaco Cloud"
"{quarter}" "SMEG" "raccordement"
site:journaldemonaco.gouv.mc "{quarter}" "data center"
site:journaldemonaco.gouv.mc "{quarter}" "salle informatique"
```

Address search template:

```text
"4-6 avenue Albert II" "Monaco Telecom"
"6 avenue Albert II" "Data Center n° 3"
"Zone F" "Monaco Telecom" "Data Center"
"25 boulevard de Suisse" "Monaco Telecom" "centre de données"
"19 boulevard du Larvotto" "data center"
"Larvotto Supérieur" "data center" "Monaco Telecom"
"14 avenue de Grande-Bretagne" "MonacoDATACENTER"
"23 avenue Albert II" "salle informatique" DRSI
"9 avenue Albert II" "Monaco Cloud"
```

---

## 3. Facility classification rules

Use these statuses consistently:

- **Operational colocation / hosting datacenter**: operator page or certificate proves live hosting/colocation, or legal/security record explicitly identifies an operational data center.
- **Proposed / under construction**: public tender, permit, council approval, or official project notice exists, but no commissioning source yet.
- **Sovereign cloud platform**: cloud service using local data centers; map its physical footprint only through separately evidenced hosting sites.
- **Public-sector server room**: official computer room / protected zone, but no public colocation or carrier-neutral service.
- **Directory-only lead**: keep as seed only; reliability C and no final facility acceptance without verification.

Known Monaco official-grade facility/project evidence:

| Facility / project | Physical evidence | Division handling | Status | Grade |
|---|---|---|---|---|
| Monaco Telecom DC3 | Journal n°8435 protected zone at Zone F, `6 avenue Albert II`; operator certificate includes `4-6 avenue Albert II - Zone F` and DC3 | Usually Fontvieille; verify against repo geometry | Operational | A |
| Monaco Telecom Centre de données n°1 | Monaco Telecom ISO/HDS certificate lists `25 boulevard de Suisse` | Likely Monte-Carlo/Sainte-Devote edge; verify repo geometry | Operational | A |
| Monaco Telecom Centre de données n°6 | Monaco Telecom ISO/HDS certificate lists `Zone F, 4-6 avenue Albert II` | Usually Fontvieille; verify against repo geometry | Operational | A |
| Monaco Telecom platform | Official product page says 3 data centers, 12 kW/rack, 2N power, ISO 27001:2022, HDS/no transfer of health data outside EEA | Do not use as address proof by itself | Operational platform | A |
| Larvotto Supérieur Monaco Telecom DC | Journal n°8649 says about 1,600 m2 data center for Monaco Telecom on R-3/R-4 | Larvotto/Saint-Roman boundary check required | Proposed / under development | A |
| Telis MonacoDATACENTER | Telis pages: first Monaco green datacenter, since 2013, `14 avenue de Grande-Bretagne`, ISO 27001/HDS, Tier III-designed, seawater cooling | Fontvieille | Operational | A |
| Monaco Cloud | Official Monaco Cloud: state sovereign cloud, multi-site, data stored/managed under Monaco law, AMSN-qualified, `9 avenue Albert II` office | Do not count office as DC; map through MT/Telis hosting evidence | Operational platform | A |
| DRSI computer room | Journal n°8435 protected zone, `23 avenue Albert II` | Fontvieille unless repo geometry differs | Public-sector server room | A |

---

## 4. Query and evidence pitfalls

- Monaco Telecom's **current certificate is more precise than older press**. Prefer the certificate for site addresses and naming; use older 2014/2015 articles for historical rack/floor-area context.
- Older articles describe a Fontvieille Zone F DC3 project of around 1,000 m2 / 200 racks and older existing sites; do not assume those historical names still match today's three certified centers without certificate/gazette support.
- The 2022 outage article identifies **Zone J under the Fontvieille shopping centre** as a main data centre and says a generator failed during maintenance. Treat as Grade B resilience/location evidence unless Monaco Telecom, SMEG, or Journal de Monaco confirms the same site.
- Monaco Cloud's official language says data is stored in Monaco and services are multi-site. It does not, by itself, disclose the exact physical data halls. Use Monaco Cloud as a platform/tenant signal, not a standalone facility count.
- `AWS technology`, `AWS Outposts`, or cloud-provider partnership language does not equal an AWS/Azure/GCP/OCI Monaco region. Always verify against official provider region lists.
- Do not convert `12 kW/rack`, racks, or floor area into MW without an explicit source. Set `capacity_mw: null` and store the proxy metrics.
- French query terms matter: `centre de données`, `data center`, `datacenter`, `salle informatique`, `salle de serveurs`, `hébergement`, `cloud souverain`, `zone protégée`, `raccordement`, `groupe électrogène`, `thalassothermie`, `SeaWergie`.

---

## 5. Final validation checklist

Before finalising MC enumeration:

- All 17 divisions were searched and either have a candidate, a negative result, or a "no facility-level evidence found" note.
- Every accepted facility has an address-level source and a quarter assignment.
- Every proposed site has a status date and is not mixed with operational capacity.
- Monaco Telecom sites are reconciled against the 2025 certificate and Journal protected-zone notice.
- Larvotto Supérieur is tracked as a future/proposed Monaco Telecom facility until a commissioning source appears.
- MonacoDATACENTER is verified against Telis/MonacoDATACENTER official pages, not directory-only listings.
- Monaco Cloud is counted as a sovereign cloud platform and mapped only through confirmed hosting data centers.
- Cap-d'Ail, Beausoleil, Nice, Sophia Antipolis, and other French results are excluded.
