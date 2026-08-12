# GA Explorer Official - Gabon Datacenter Enumeration

Date: 2026-08-12. Country: **GA - Gabon** (`Republique Gabonaise` / Gabonese Republic). Target division model for this explorer: **9 manifest provinces**: Estuary; Upper Ogooue; Middle Ogooue; Ngounie; Nyanga; Ogooue-Ivindo; Ogooue-Lolo; Maritime Ogooue; Woleu-Ntem. French administrative names used in sources: **Estuaire; Haut-Ogooue; Moyen-Ogooue; Ngounie; Nyanga; Ogooue-Ivindo; Ogooue-Lolo; Ogooue-Maritime; Woleu-Ntem**.

Yield honesty up front: Gabon has **no public national datacenter registry** and a very small public colocation market. This review found **two confirmed physical facilities** (ST Digital Nkok; Moov Africa Gabon Telecom DC1 in the Cenacom Building), **one major facility under development** (Cybastion/Gabon sovereign DC, reported at 20 MW), **one unresolved ANINF/state facility lead**, and a handful of directory-level leads. Expect a realistic country-wide inventory of **4-7 physical records at most**; 8 of the 9 manifest provinces are expected to return **no public colocation** (only connectivity, government server rooms, university labs, or private enterprise IT). Do not pad the inventory with policy statements, landing stations, IXP POPs, or labs.

Reliability grades used in this file:
- **A** = primary or official for the fact asserted: government/ministry/ANINF/ARCEP/APDPVP/SPIN page, official operator facility page, official cloud-region page, Uptime Institute record, company press release signed by officers.
- **B** = strong secondary: Agence Ecofin, DCD, Digital Business Africa, We Are Tech Africa, Gabon Review, L'Union, Gabon Actu, Gabon Media Time, AGP, Convergence Afrique, Le360, Euro-IX ixpdb, local press quoting named officials/operators.
- **C** = lead only: directories (DataCenterMap, colo.exchange, DataCenters.com, Inflect, Baxtel, Tracxn), aggregator news sites, social posts, unquoted vendor claims, ambiguous hosting/cloud claims, policy-only statements.

## 0. Ground Rules

- There is **no public national datacenter registry** for Gabon. Build the inventory by joining ministry/ANINF official pages, regulator records, operator facility pages, IXP evidence, energy/permit clues, donor project records, and trade press.
- Search in **French first**. High-yield terms: `centre de donnees`, `datacenter`, `data center`, `centre de stockage de donnees`, `hebergement`, `colocation`, `salle serveurs`, `cloud souverain`, `souverainete numerique`, `Tier III`, `Tier 3`, `GABIX`, `GAB-IX`, `point d'echange Internet`, `cable sous-marin`, `atterrissement`, `ACE`, `Medusa`, `SAT-3`, `LION2`, `backbone national gabonais` / `BNG`, `fibre optique`, `dorsale`, `poste electrique`, `MVA`, `MW`, `SEEG`, `centrale a gaz`, `ZES de Nkok`, `zone economique speciale`, `appel d'offres`, `permis de construire`.
- **Disambiguate aggressively.** Gabon evidence says Libreville, Port-Gentil, Franceville, Oyem, ANINF, ARCEP, APDPVP, SPIN, ACE Gabon, GABIX, SEEG, Moov Africa Gabon Telecom. Reject or re-check: Brazzaville/Pointe-Noire (Congo-Brazzaville), Kinshasa/Lubumbashi (DRC), Douala/Yaounde (Cameroon), Bata/Malabo (Equatorial Guinea), and any `Gabon` mention that is actually about `GABON TELECOM` brand history or unrelated sectors.
- Count **physical facilities**, not policy objectives, corporate offices, generic cloud services, tower sites, cable landing stations, or telco POPs. A facility record needs physical siting or facility language: data center, racks, white space, technical rooms, colocation, IXP host, Tier design/certification, launch, construction, or commissioning.
- **Dedupe trap of this market**: three distinct `Nkok`/`Libreville` storylines circulate in the press (ST Digital lbv01 operational; ANINF/Cybastion 20 MW under development; ANINF legacy Libreville DC). Do not merge them without an address/operator/ownership statement.
- **URL validation note, 2026-08-12**: the core official/operator pages were checked live. Most returned HTTP 200 to command-line probes; a few protected or intermittently proxied sites (for example ISOC Pulse/Uptime/news directories) may return 403/429/522 to curl while rendering through browser/search tooling. Keep protected secondary/directory sources as support, not sole facility proof. The old draft ministry short path `/aninf` returned 404 and has been replaced below.

## 1. Official and Regulatory Sources

### 1.1 Ministry of Digital Economy, Digitalization and New Technologies

Use first for the national datacenter programme, the 2025-2026 sovereign-DC push, and official operator context.

Verified URLs:
- Ministry homepage: https://economie-numerique.gouv.ga/
- Ministry ANINF page: https://economie-numerique.gouv.ga/agence-nationale-des-infrastructures-numerique-et-des-frequences/
- Ministry contact page listing supervised entities including ANINF, SPIN, and ARCEP: https://economie-numerique.gouv.ga/contact/
- Ministry is co-signatory (with ST Digital and APDPVP) of the Nkok sovereign-cloud partnership: https://st.digital/blog/nos-actualites-1/datacenter-de-nkok-st-digital-lapdpvp-et-le-ministere-de-leconomie-numerique-scellent-un-partenariat-pour-une-infrastructure-cloud-souveraine-et-conforme-544

Use as **A** for ministry statements, government programme status, and official project descriptions. Do not use it alone to infer commercial colocation unless it names a facility or service.

Queries:

```text
site:economie-numerique.gouv.ga "data center"
site:economie-numerique.gouv.ga "centre de donnees"
site:economie-numerique.gouv.ga datacenter
site:economie-numerique.gouv.ga Nkok
site:economie-numerique.gouv.ga ANINF
site:economie-numerique.gouv.ga Cybastion
site:economie-numerique.gouv.ga "ST Digital"
"Ministere de l'Economie Numerique" Gabon datacenter Nkok
"Mark Alexandre Doumba" OR "Bonjean Rodrigue Mbanza" Gabon "data center"
```

Extract: project name, province/city, build status, opening target, contractor, operator, intended tenants, funding, and whether the page proves a facility or only policy.

### 1.2 ANINF - national digital infrastructure agency (key source)

Verified URLs:
- ANINF homepage: https://aninf.ga/
- ANINF project page, Data Center national: https://aninf.ga/projet/data-center-national-garantir-la-souverainete-des-donnees/
- ANINF article on the sovereign DC launch: https://aninf.ga/souverainete-numerique-le-gabon-lance-son-data-center-national-et-affirme-son-independance-technologique/
- ANINF GAB-IX project page (FR): https://aninf.ga/projet/point-dechange-internet-gab-ix-le-hub-internet-gabonais/
- ANINF GAB-IX project page (EN): https://aninf.ga/en/projet/internet-exchange-area-gab-ix-gabons-internet-hub/

ANINF is the State's technical arm for shared digital infrastructure: it operates/anchors national digital infrastructure, appears as a 10 Gbps GABIX member in current IXP data, and is the State co-contractor of the 28 June 2025 Cybastion agreement for sovereign digital infrastructure. Treat ANINF's older `Data Center National` page as programme evidence unless it gives a current address/operator for a physical room.

Use ANINF pages as **A** for agency statements, GABIX facts, backbone facts, and the national-DC programme. Resolve explicitly which facility ANINF pages mean (Libreville legacy vs Nkok new) before counting a record.

Queries:

```text
site:aninf.ga "data center"
site:aninf.ga "centre de donnees"
site:aninf.ga datacenter
site:aninf.ga Nkok
site:aninf.ga Libreville "centre de donnees"
site:aninf.ga GABIX OR GAB-IX
site:aninf.ga BNG OR backbone
site:aninf.ga Cybastion
"ANINF" "data center" Gabon 2025 OR 2026
```

Extract: facility host, city/province, IXP members, launch dates, backbone segments, service scope, and whether the record proves a physical facility or only programme intent.

### 1.3 ARCEP Gabon - telecom regulator

Verified URLs:
- ARCEP Gabon homepage: https://www.arcep.ga/
- ARCEP context (Africa Internet Summit 2026 hosted in Gabon, June 2026): https://www.arcep.ga/

ARCEP (Autorite de Regulation des Communications Electroniques et des Postes) regulates telecom operators including Moov Africa Gabon Telecom and Airtel Gabon. **No datacenter registry or dedicated datacenter licence category was found** in this review; check the licence framework (electronic-communications licences may or may not cover hosting/colocation) before asserting a regulatory category.

Use ARCEP as **A** for operator existence, licensing, and telecom-market facts; **B/C** for any hosting/DC implication unless a licence text names facilities.

Queries:

```text
site:arcep.ga "centre de donnees"
site:arcep.ga "data center"
site:arcep.ga datacenter
site:arcep.ga GABIX OR "point d'echange"
site:arcep.ga licence operateur hebergement
site:arcep.ga "Africa Internet Summit"
"ARCEP" Gabon datacenter OR "centre de donnees"
```

Extract: operator legal name, licence category, service scope, IXP involvement, and whether a source proves network service only or a physical facility.

### 1.4 APDPVP - data protection authority (sovereign-hosting driver)

Verified URLs:
- APDPVP homepage: https://www.apdpvp.ga/
- APDPVP accompanied the Nkok DC project for compliance: https://www.gabonreview.com/hebergement-des-donnees-le-gabon-met-fin-a-sa-dependance-aux-serveurs-etrangers-avec-son-premier-datacenter/
- ST Digital/APDPVP/Ministry partnership (10 Jun 2026): https://st.digital/blog/nos-actualites-1/datacenter-de-nkok-st-digital-lapdpvp-et-le-ministere-de-leconomie-numerique-scellent-un-partenariat-pour-une-infrastructure-cloud-souveraine-et-conforme-544
- APDPVP inspections outside Libreville (e.g., Lambarene, Moyen-Ogooue): https://www.union.sonapresse.com/fr/donnees-personnelles-lapdpvp-en-mission-dinspection-lambarene

APDPVP is useful for local-hosting and personal-data-compliance signals and can surface provincial server-room/hosting compliance leads through inspection activity. Use as **A** for compliance/authorization facts on APDPVP pages; it is **not** a datacenter register.

Queries:

```text
site:apdpvp.ga "data center"
site:apdpvp.ga hebergement
site:apdpvp.ga "transfert de donnees"
site:apdpvp.ga cloud
"APDPVP" Nkok datacenter
"APDPVP" hebergement Gabon agrement
"loi 001/2011" Gabon hebergement donnees
```

### 1.5 SPIN and subsea-cable official sources

Verified URLs:
- SPIN (Societe de Patrimoine des Infrastructures Numeriques) homepage: https://spin.ga/
- ACE Gabon landing-station page: https://spin.ga/nos-activites/ace-gabon/
- Medusa official C&MA release for Port-Gentil landing: https://medusascs.com/news/ace-gabon-and-medusa-africa-sign-construction-and-maintenance-agreement-for-medusa-submarine-cable-landing-in-port-gentil/
- ACE Gabon / Medusa local coverage (Port-Gentil landing, 2026-2027 build, Ndjole extension to BNG): https://gabonactu.com/blog/2025/03/17/resilience-numerique-au-gabon-bientot-un-nouveau-cable-sous-marin-medusa/ and https://gabonmediatime.com/gabon-vers-la-construction-du-cable-sous-marin-optique-medusa-afrique/

SPIN holds Gabon's digital infrastructure patrimony; its subsidiary ACE Gabon owns/operates the **Libreville ACE landing station** and is the landing party for **Medusa Africa** at **Port-Gentil, Ogooue-Maritime**. Landing stations are **connectivity, not datacenters**; use them as anchors for adjacent carrier rooms, GABIX POP ACE, and backhaul facilities only when rack/colo evidence appears.

Queries:

```text
site:spin.ga "data center" OR "centre de donnees" OR datacenter
site:spin.ga ACE "Libreville"
site:spin.ga Medusa Port-Gentil
"ACE Gabon" Libreville datacenter OR "salle serveurs"
"Medusa" Gabon "Port-Gentil" datacenter OR "point de presence"
"atterrissement" Gabon "data center" OR racks
```

### 1.6 Energy, grid, and environmental/permit sources

Verified URLs:
- SEEG (Societe d'Energie et d'Eau du Gabon), concessionaire since 1997: https://www.seeg-gabon.com/
- Ministry of Energy and Hydraulic Resources: https://www.energie.gouv.ga/
- SEEG restructuring (2026 split into a future `Electricite du Gabon` + water entity): https://www.agenceecofin.com/actualites-industries/2906-139717-gabon-restructuration-de-la-societe-d-energie-et-d-eau-face-a-ses-difficultes
- Nkok power context: ST Digital's operator page says the Nkok DC is operational with 1 MW of power and green/solar design; DCD and Le360 report the Cybastion project with a **20 MW gas power plant**: https://afrique.le360.ma/economie/gabon-un-futur-data-center-national-concu-par-lamericain-cybastion-le-modele-america-first-a-loeuvre_UZQ5ZK7ZLBHY3KMVQMF4JYEDMA/ and https://www.datacenterdynamics.com/en/news/cybastion-to-build-20mw-data-center-in-gabon/

Hydro assets relevant for power-anchored searches: Kinguele (Estuaire), Tchimbele (Estuaire), Grand Poubara (Haut-Ogooue), Bongolo (Ngounie); gas/diesel thermal around Port-Gentil and Alenakiri. No searchable national building-permit registry was found; permits are expected at commune/urbanism level and EIES studies may surface through donors/consultants. Treat named permits/EIES as **A/B** depending on issuer; generic construction mentions remain leads.

Queries:

```text
site:seeg-gabon.com "data center" OR "centre de donnees"
site:energie.gouv.ga datacenter OR "centre de donnees"
"Nkok" "centrale a gaz" MW datacenter
"Port-Gentil" centrale electrique datacenter OR "salle serveurs"
"Grand Poubara" OR "Kinguélé" OR "Kinguélé" datacenter
"permis de construire" datacenter Gabon
"EIES" OR "etude d'impact" "centre de donnees" Gabon
"ZES de Nkok" datacenter electricite OR MW
```

Extract exact power meaning: grid connection, substation, site load, IT load, MVA/MW, generator/gas plant, cooling/water, permit dates, commissioning.

### 1.7 Donor and procurement projects

Verified URLs:
- AfDB grant to ANINF (2018) covering CAB fibre feasibility + **national data center** + alert platform: https://gabonactu.com/blog/2018/12/07/laninf-beneficie-dun-don-additionnel-de-bad-de-800-000-dollars-projets-plan-national-strategique-gabon-digital-2025/
- World Bank Gabon project search: https://projects.worldbank.org/en/projects-operations/projects-list?countrycode_exact=GA
- Cybastion/ANINF convention press release (28 Jun 2025, with Cisco/Citibank/EXIM): https://www.cybastiontech.com/cybastion-government-of-gabon-and-aninf-sign-historic-digital-infrastructure-agreement/

Use donor pages as **A** for financing/project scope. Use procurement notices as **B** for planned facilities until award/site/construction evidence is found.

Queries:

```text
site:afdb.org Gabon datacenter OR "centre de donnees"
site:documents.worldbank.org Gabon digital economy datacenter
site:projects.worldbank.org Gabon digital
"Gabon" "appel d'offres" datacenter OR "centre de donnees"
"BAD" OR "AfDB" Gabon "centre de donnees" ANINF
"Gabon Digital 2025" datacenter
EXIM Gabon datacenter Cybastion
```

### 1.8 Official cloud-region negative controls

Use these as **A** only for cloud-region existence/non-existence. **No AWS, Azure, Google Cloud, or Oracle OCI public cloud region exists in GA** in the checked public lists; the nearest public regions are South Africa (AWS Cape Town; Azure South Africa North/West; GCP `africa-south1` Johannesburg; OCI `af-johannesburg-1`).

- AWS Regions: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html
- Microsoft Azure regions: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud locations: https://cloud.google.com/about/locations
- Oracle OCI regions: https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm

Queries:

```text
"Libreville" "AWS Direct Connect" OR ExpressRoute OR "Cloud Interconnect" OR FastConnect
"Port-Gentil" AWS Azure "Google Cloud" Oracle datacenter
"Gabon" "cloud region"
"ST Digital" Libreville cloud colocation
```

### 1.9 Uptime Institute

Verified URL (record found):
- Moov Africa Gabon Telecom - **DC1, Cenacom Building, Libreville**: https://uptimeinstitute.com/component/tierachievement/datacenter/dc1-cenacom-building-libreville/2003
- Certification list to confirm tier level/date: https://uptimeinstitute.com/tier-certification/tier-certification-list
- Awards list: https://uptimeinstitute.com/uptime-institute-awards/list

The Cenacom DC1 record is the only Uptime Institute record located for Gabon in this review; the static page rendered client/project details but **not the tier level/date** - confirm the tier and certification date on the list before writing a tier value. ST Digital's Nkok DC claims `Tier 3 Certified` on its operator page and press repeats `certifie Tier III`, but **no Uptime record for the Nkok site was located** in this review - treat that as an operator claim until the Uptime list names lbv01/Nkok.

Queries:

```text
site:uptimeinstitute.com Gabon Libreville
site:uptimeinstitute.com "Cenacom"
site:uptimeinstitute.com "ST Digital" Gabon
site:uptimeinstitute.com "Moov Africa Gabon Telecom"
site:uptimeinstitute.com "Port-Gentil"
```

## 2. Verified Facility and Lead Seeds

| Facility / project | Province | Evidence and grade | Status and handling |
|---|---|---|---|
| **ST Digital Data Center Services - Nkok DC (lbv01)** | Estuary (Nkok SEZ, near Libreville) | Official operator page **A**: https://st.digital/datacenter/lbv01 (100% operational, 1 MW, Tier 3 certified claim, solar/green design, water-free cooling, colocation/IaaS/SaaS); partner blog **A**: https://st.digital/blog/nos-actualites-1/datacenter-de-nkok-st-digital-lapdpvp-et-le-ministere-de-leconomie-numerique-scellent-un-partenariat-pour-une-infrastructure-cloud-souveraine-et-conforme-544; press **B**: https://www.datacenterdynamics.com/en/news/cameroons-st-digital-opens-data-center-in-gabon/, https://www.union.sonapresse.com/fr/data-center-le-gabon-sur-les-pas-des-geants-africains, https://convergenceafrique.net/2026/07/03/gabon-avec-son-premier-data-center-souverain-libreville-accelere-sa-revolution-numerique/, https://www.agenceecofin.com/actualites-numerique/2907-130498-gabon-st-digital-lance-la-construction-d-un-data-center-100-africain-a-nkok, https://w.media/st-digital-opens-gabons-first-sovereign-tier-iii-data-center/, https://gabonactu.com/blog/2026/07/04/gabon-inauguration-du-premier-data-center-souverain-a-nkok/, https://www.wearetech.africa/en/fils-uk/news/tech/gabon-launches-14-million-tier-iii-data-center-in-digital-sovereignty-push; directory **C**: https://www.datacenters.com/st-digital-st-digital-gabon-nkok | **Operational.** Opening/inauguration reported 30 Jun/3 Jul 2026; DCD says the facility opened 3 Jul 2026 after breaking ground in Aug 2025. We Are Tech reports 8 bn FCFA, >3,000 sqm, 92 racks, 1 MW, and cloud/colocation/private-hosting rooms; keep those as **B** unless ST Digital publishes the same detail. Tier III is operator/press claim; keep `Uptime certification` as **unverified** until the Uptime list names the site. |
| **Cybastion / Government of Gabon / ANINF sovereign data center project (reported 20 MW)** | Estuary / Libreville-Nkok corridor; exact site unresolved | Company PR **A**: https://www.cybastiontech.com/cybastion-government-of-gabon-and-aninf-sign-historic-digital-infrastructure-agreement/ (28 Jun 2025 agreement, Cisco/Citibank/EXIM, sovereign data center + cybersecurity + digital ID); trade **B**: https://www.datacenterdynamics.com/en/news/cybastion-to-build-20mw-data-center-in-gabon/ (20 MW, strategic agreement signed 28 Jan 2025, Libreville site, Porteo, gas plant), https://w.media/st-digital-opens-gabons-first-sovereign-tier-iii-data-center/, https://afrique.le360.ma/economie/gabon-un-futur-data-center-national-concu-par-lamericain-cybastion-le-modele-america-first-a-loeuvre_UZQ5ZK7ZLBHY3KMVQMF4JYEDMA/; local press **C**: https://gaboninfos.com/digitalisation-gabon-dote-data-center-national/, https://fr.infosgabon.com/le-gabon-signe-une-convention-avec-cybastion-pour-la-creation-du-data-center-de-laninf/ | **Under development / planned.** Keep **separate** from ST Digital lbv01 unless ANINF/ministry/Cybastion states that they are the same building. The official Cybastion release proves the agreement and sovereign-DC scope; DCD/Le360 supply the 20 MW, site, contractor, and gas-plant details. |
| **Moov Africa Gabon Telecom - DC1, Cenacom Building, Libreville** | Estuary | Uptime Institute record **A** (client/project/location, tier/date not rendered): https://uptimeinstitute.com/component/tierachievement/datacenter/dc1-cenacom-building-libreville/2003; operator portal **A** for company: https://www.moov-africa.ga/; IXP adjacency **B** (GABIX POP CT-1 has Moov Africa Gabon Telecom and ST Digital connections): https://ixpdb.euro-ix.net/en/explore/ixp/807/pops/ | **Operational legacy telco DC.** Real physical facility (Uptime record). Confirm exact street address, capacity, tier level/date, and whether third-party colocation is offered before listing as public colocation. |
| **ANINF / state national data-center lead - Libreville** | Estuary | ANINF project page **A** for programme: https://aninf.ga/projet/data-center-national-garantir-la-souverainete-des-donnees/; ANINF launch/article page **A** for current state narrative: https://aninf.ga/souverainete-numerique-le-gabon-lance-son-data-center-national-et-affirme-son-independance-technologique/; press on reinforcement **C**: https://www.nouvelles-du-monde.com/gabon-renforce-son-centre-de-donnees-national-pour-assurer-la-souverainete-numerique/; AfDB-funded feasibility context **B**: https://gabonactu.com/blog/2018/12/07/laninf-beneficie-dun-don-additionnel-de-bad-de-800-000-dollars-projets-plan-national-strategique-gabon-digital-2025/ | **Lead / programme record.** Do not double count this against the Cybastion agreement or ST Digital Nkok without an address/operator match. Use it to search for ANINF HQ/Tour ANINF, legacy government hosting, and state migration plans. |
| **Airtel Gabon S.A. - Libreville data center** | Estuary | Directory **C**: https://colo.exchange/data-centers/airtel-gabon-sa-airtel-gabon and https://colo.exchange/locations/ga/estuaire/libreville; GABIX member evidence **B**: https://ixpdb.euro-ix.net/en/explore/ixp/807/pops/ (Airtel Gabon 1 Gbps link) | **C-grade lead.** Verify with Airtel official pages, PeeringDB facility record, or ARCEP licence before counting. GABIX membership alone is network evidence, not a DC. |
| **GABIX / GAB-IX (IXP)** | Estuary | Official IXP **A**: https://www.gabix.ga/ (GIE since 2014, address Ancienne RTG - Libreville); ANINF project page **A**: https://aninf.ga/projet/point-dechange-internet-gab-ix-le-hub-internet-gabonais/; Euro-IX ixpdb **B**: https://ixpdb.euro-ix.net/en/explore/ixp/807/pops/ (POP ACE + POP CT-1; ANINF 10G, Airtel, GVA, Moov, ST Digital, PCH, iPi9, GBM/TLDC depending on POP); ISOC Pulse **B**: https://pulse.internetsociety.org/fr/ixp-tracker/ixp/555/ | **IXP, not a datacenter.** Use GABIX POP locations (ACE landing station; CT-1/Cenacom carrier room) to find facility hosts. Do not count GABIX as a DC just because directories label POP CT-1 as a datacenter. |
| **SPIN / ACE Gabon landing station - Libreville; Medusa - Port-Gentil** | Estuary; Maritime Ogooue | Official **A**: https://spin.ga/nos-activites/ace-gabon/ (Libreville ACE station); Medusa official **A/B**: https://medusascs.com/news/ace-gabon-and-medusa-africa-sign-construction-and-maintenance-agreement-for-medusa-submarine-cable-landing-in-port-gentil/; local coverage **B**: https://gabonactu.com/blog/2025/03/17/resilience-numerique-au-gabon-bientot-un-nouveau-cable-sous-marin-medusa/ and https://gabonmediatime.com/gabon-vers-la-construction-du-cable-sous-marin-optique-medusa-afrique/ | **Connectivity infrastructure, not DCs.** Do not count landing stations as datacenters unless rack/colo facility evidence appears at the station. Medusa Port-Gentil is a Maritime Ogooue adjacency lead. |
| **Shapoorji Pallonji MoU - national data center** | n/a | Directory/news lead **C**: https://baxtel.com/news/shapoorji-pallonji-signs-mou-to-build-data-center-in-gabon (MoU with Gabonese state; company visits since Mar 2023) | **Historical lead.** No award/construction evidence found in this review; may have been superseded by the Cybastion/ANINF convention or the ST Digital build. Require official evidence before counting. |
| **USTM data center labs - Franceville** | Upper Ogooue | Operator donation coverage **B**: https://gabonactu.com/blog/2021/07/14/gabon-telecom-offre-un-puissant-data-center-pour-revolutionner-lapprentissage-a-lustm/ and https://gabonmediatime.com/ustm-moov-africa-gabon-telecom-deploie-deux-laboratoires-data-center/ | **Rejected as commercial DC.** University teaching labs at Universite des Sciences et Techniques de Masuku (Franceville). Useful only to explain why Haut-Ogooue has no public colocation. |

## 3. Province Coverage and Strategy

Run both exact province and city/anchor terms (French and English spellings).

Generic query block:

```text
("{province}" OR "{capital}" OR "{alias}") (datacenter OR "data center" OR "centre de donnees" OR "salle serveurs" OR colocation OR hebergement) Gabon -Congo -Brazzaville -Kinshasa -Douala
("{city}") ("fibre optique" OR backbone OR dorsale OR BNG OR IXP OR GABIX OR "point d'echange Internet" OR "poste electrique") (datacenter OR "centre de donnees" OR "{operator}")
site:aninf.ga "{city}"
site:economie-numerique.gouv.ga "{city}"
site:spin.ga "{city}"
"{operator}" "{city}" (datacenter OR colocation OR hebergement OR POP OR "point de presence")
```

| Manifest province | Search aliases and anchors | Priority | Concrete strategy |
|---|---|---:|---|
| Estuary / Estuaire | Libreville (Batterie IV, Oloumi, Mont-Bouet, Nzeng-Ayong, Glass, Akanda, Ancienne RTG, Cenacom, Tour ANINF), Nkok (ZES, zone economique speciale), Owendo, Ntoum, Kango, Cocobeach | Very high | Seed ST Digital Nkok (operational), Cybastion/Gabon sovereign DC project (development/planned), Moov Africa Gabon Telecom Cenacom DC1, ANINF/state programme lead, Airtel Gabon lead, GABIX POP ACE + POP CT-1, ACE station. Dedupe Nkok/Libreville storylines by operator/address/date. |
| Upper Ogooue / Haut-Ogooue | Franceville, Moanda, Mounana, Okondja, Akieni, Lekoni, USTM (Masuku) | Medium | Search USTM data-center labs (reject as commercial), Eramet/Comilog manganese IT rooms (private), BNG fibre, Grand Poubara power. Expect no public colocation. |
| Middle Ogooue / Moyen-Ogooue | Lambarene, Ndjole, Bifoun, Ogooue-et-Lacs | Low/medium | Ndjole is the BNG junction for the future Medusa extension. Search government/health (Albert Schweitzer) server rooms, APDPVP inspection mentions, fibre/POP evidence. Expect no public colocation. |
| Ngounie | Mouila, Fougamou, Mbigou, Mimongo, Ndende, Lebamba, Bongolo | Low | Search Bongolo dam power, government service rooms, VSAT/fibre. Treat any Bongolo/health IT room as enterprise private unless colocation offered. |
| Nyanga | Tchibanga, Mayumba, Moabi, Mabanda | Low | Coastal/oil and Mayumba port leads; search border connectivity, VSAT, oil camp IT rooms. Expect no public colocation. |
| Ogooue-Ivindo | Makokou, Booue, Mekambo, Ovan | Low | Northern forestry/mining corridor. Search BNG/VSAT and government intranet; expect no public colocation. |
| Ogooue-Lolo | Koulamoutou, Lastoursville, Iboundji | Low | BNG backbone corridor and government rooms. Avoid power-only false positives. |
| Maritime Ogooue / Ogooue-Maritime | Port-Gentil, Omboue, Gamba, Sette Cama, Cap Lopez | Medium | Oil capital: private enterprise IT rooms (TotalEnergies, Perenco, VAALCO - private only), gas thermal power, and the **Medusa cable landing at Port-Gentil (2026-27)** as a future adjacency lead. Do not count oil-company server rooms as public colocation. |
| Woleu-Ntem | Oyem, Bitam, Minvoul, Mitzic, Medouneu | Low/medium | Cameroon border corridor (BNG/CAB extensions), government services, Oyem health/education IT rooms. Expect no public colocation. |

## 4. Evidence Capture Rules

For every candidate record capture:

```text
facility_name:
operator_or_owner:
province_manifest_9:
city_quartier_address:
status: operational | commissioned | under construction | planned | tender | lead-only | rejected
source_grade_by_fact:
source_urls:
physical_evidence: racks | rooms | MW/MVA | Tier | IXP host | landing station | POP | office | university lab
capacity:
power_cooling:
connectivity:
tenant_or_service_scope:
dedupe_notes:
country_disambiguation:
```

Status hierarchy: official/operator operational page or inauguration > commissioning coverage > under-construction official/donor page > contract award > convention/MoU > tender > policy/strategy. Capacity hierarchy: official datasheet > operator statement > trade press quoting operator > directory. Do not promote a C-grade directory lead without a non-directory join.

## 5. Rejection Patterns

- Congo-Brazzaville (Brazzaville/Pointe-Noire), DRC (Kinshasa/Lubumbashi), Cameroon (Douala/Yaounde), or Equatorial Guinea (Bata/Malabo) sources unless they explicitly describe a cross-border GA facility.
- Hyperscale region claims for AWS/Azure/GCP/OCI in Gabon unless the provider region page names GA (none do as of 2026-08-12).
- ACE/SAT-3/LION2/Medusa landing stations counted as datacenters without adjacent facility evidence.
- `cloud`, `hebergement`, or `hosting` services with no Gabon physical site.
- USTM Franceville data-center labs and other university/CSR donations - education facilities, not commercial DCs.
- Oil, mining, and bank server rooms (TotalEnergies, Perenco, VAALCO, Eramet/Comilog, BGFI, Ecobank) unless named as a significant data center, disaster-recovery site, or colocation offer.
- Ministry or agency server rooms unless named as a significant data center, DR site, or colocation facility.
- ST Digital group copy that mixes country-market claims across Gabon, Cote d'Ivoire, Cameroon, Togo, and Congo - verify any non-Gabon claim against the Gabon Nkok facility before recording.
- `Data center national` headlines that conflate the ST Digital Nkok DC (operational), the ANINF/Cybastion 20 MW Nkok project (development), and the ANINF legacy Libreville DC - resolve ownership before merging records.
