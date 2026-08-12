# NE Explorer Official - Niger Datacenter Enumeration (official/regulatory methodology)

Date verified: 2026-08-12. Country: NE - Niger. Primary angle: official, regulatory, public-procurement, power, interconnection, and cloud-provider evidence for datacenter enumeration.

Division model: **region / capital urban community**. Niger's first-level coverage set is complete at 8 divisions: **Niamey** (capital urban community), **Agadez**, **Diffa**, **Dosso**, **Maradi**, **Tahoua**, **Tillabéri/Tillaberi**, and **Zinder**. The government presentation page states that Niger is divided into 8 regions: Agadez, Dosso, Maradi, Tahoua, Tillabéri, Zinder, Diffa and Niamey (communauté urbaine): https://www.gouv.ne/index.php/lenigerpresentation/presentation . ANP's region menu independently exposes the same coverage set: https://www.anp.ne/region/niamey/ plus /region/agadez/, /region/diffa/, /region/dosso/, /region/maradi/, /region/tahoua/, /region/tillabery/, /region/zinder/.

Political context: Niger has been under a transition regime since the 2023-07-26 coup and is part of the AES with Mali and Burkina Faso. Ministry names and officeholders change; for 2026 checks, use MCNTI as the active ministry name and confirm the named minister on current pages before citing.

## 0. Structure Facts

- **Administrative divisions:** use the 8-division model above for coverage. Do not stop at Niamey-only searches, but expect real datacenter evidence to be Niamey-centered.
- **No public datacenter registry found:** Niger has no official public registry of datacenters, no public building-permit registry suitable for facility enumeration, and no Uptime Institute-certified Niger facility was found in the 2026-08-12 check. Treat Uptime/Tier claims as unproven unless the certification directory names a Niger facility: https://uptimeinstitute.com/tier-certification .
- **Telecom regulator:** ARCEP is the regulator for electronic communications and postal services: https://arcep.ne/ . Its 2024 annual report page is live and lists operators including CELTEL/Airtel, MOOV, ZAMANI COM and NIGER TELECOMS: https://arcep.ne/ova_doc/rapport-annuel-2024/ . ARCEP facts are A-grade for licences/regulation, but a licence is not a datacenter record.
- **Digital ministry:** the active ministry website is MCNTI, Ministère de la Communication et des Nouvelles Technologies de l'Information: https://mcnti.gouv.ne/ . Current 2026 ministry pages name Adji Ali Salatou as minister in MCNTI/government communications; older 2025 national-DC articles name Sidi Mohamed Raliou under the prior portfolio wording.
- **State digital agency:** ANSI remains the state digital-agency seed source for Niger 2.0, e-government and possible government-hosting leads: https://ansi.ne/ . Use ANSI only for official program evidence unless it names a physical facility.
- **Data protection:** HAPDP is live at https://www.hapdp.ne/ . Its legislation page lists Law No. 2022-59 of 16 December 2022, amendments including Law No. 2023-31 and ordinances in 2024, and the consolidated personal-data framework: https://www.hapdp.ne/legislation-nationale . This supports sovereign-data demand but does not prove a facility.
- **Power:** NIGELEC's official site is live at https://www.nigelec.ne/ and states it handles production, transmission and distribution; its site gives the head office at Avenue du Général De Gaulle, Plateau I, Niamey. ARSE's electricity page says the national public electricity network is dominated by NIGELEC and that NIGELEC is present in all eight regions: https://arse.ne/electricite/ . Power documents are A-grade for utility facts and should be checked for any DC-class load claim.
- **Procurement:** the Portail des Marchés Publics du Niger is live and searchable: https://www.marchespublics.ne/ . It is the best official source for tenders/awards. ARMP/JMP remains useful for journals and older tender notices; its search-visible route is https://www.armp-niger.org/documentation/journal-des-marches-publics-jmp but it returned Cloudflare 522 to raw curl in this pass.
- **Interconnection:** Niger is landlocked; no in-country submarine landing station should be accepted. The official/reliable connectivity sources are DTS/AfDB, ARCEP, operator pages, PCH and PeeringDB.

## 1. Search Vocabulary

Run French first, English second. Niger's administrative and technical publications are overwhelmingly in French.

```text
French core:
"datacenter" OR "data center" OR "centre de données" OR "centre de traitement des données"
"salle serveur" OR "salle informatique" OR hébergement OR colocation OR cloud OR "cloud souverain"
"infrastructure numérique" OR "infrastructures de télécommunication" OR "dorsale" OR "fibre optique"
"point d'échange Internet" OR IXP OR peering OR "centre de supervision" OR NOC
"groupe électrogène" OR onduleur OR climatisation OR kVA OR MVA OR MW OR "poste de transformation"

English support:
"data center" OR "data centre" OR datacenter OR colocation OR hosting OR cloud
"digital infrastructure" OR IXP OR peering OR "terrestrial fibre" OR backbone OR "Tier III"
```

Use accents and plain-ASCII variants: Tillabéri/Tillaberi, Niamey/Niame, centre de données/centre de donnees.

## 2. Official/Regulatory Pipeline

| Source | Verified URL | Use | Grade and cautions |
|---|---|---|---|
| MCNTI | https://mcnti.gouv.ne/ ; government ministry page https://www.gouv.ne/index.php/les-ministeres/178-ministere-de-la-communication-et-des-nouvelles-technologies-de-l-information | Digital policy, national Data Center program, DTS reception, e-government, AES digital cooperation. | A for live MCNTI/government pages. Reconfirm current minister before citing. |
| ARCEP | https://arcep.ne/ ; annual reports https://arcep.ne/cat_doc/rapport-annuels/ ; 2024 report page https://arcep.ne/ova_doc/rapport-annuel-2024/ | Operator universe, licences, QoS decisions, reports, telecom market facts. | A for regulator facts; not facility proof by itself. |
| ANSI | https://ansi.ne/ | Niger 2.0, e-government, cyber/digital platforms, government-cloud leads. | A for pages it publishes; use as lead unless a physical site is named. |
| HAPDP | https://www.hapdp.ne/ ; https://www.hapdp.ne/legislation-nationale | Personal-data law, cross-border transfer/data-localization pressure, data-controller lists. | A for legal/authority facts; not facility proof. |
| Portail des Marchés Publics | https://www.marchespublics.ne/ | Tender plans and awards for datacenter works, cabling, power, NOC, fibre and server procurement. | A for tender/award records. Dynamic pages may need portal search rather than direct URL. |
| ARMP / JMP | https://www.armp-niger.org/documentation/journal-des-marches-publics-jmp | Weekly procurement journal and corroboration of procurement items. | A when the journal notice is opened; B/C for snippets/search-only evidence. Raw curl returned Cloudflare 522 on 2026-08-12. |
| NIGELEC / ARSE | https://www.nigelec.ne/ ; https://arse.ne/electricite/ ; https://arse.ne/sous-secteur-electricite-nigelec/ | Utility footprint, concessions, grid constraints, substations, large-load plausibility. | A for utility/regulator facts. |
| gouv.ne / ANP / Le Sahel | https://www.gouv.ne/ ; https://anp.ne/ ; https://www.lesahel.org/ | Council communiqués, state announcements, official interviews and regional feeds. | A for government pages; B+ for ANP/Le Sahel relays of named officials. |
| AfDB DTS | Project page https://www.afdb.org/en/projects-and-operations/p-z1-gb0-024 ; EER https://www.afdb.org/en/documents/niger-dorsale-transsaharienne-fibre-optique-dts-eer-octobre-2024 ; procurement plan https://www.afdb.org/en/documents/ppm-niger-dorsale-transsaharienne-fibre-optique-dts-simplifie ; E&S docs page https://www.afdb.org/ar/documents/niger-projet-de-la-dorsale-transsaharienne-fibre-optique-dts-p-z1-gb0-024 | DTS backbone, national data center scope, EIES/PAR documents, procurement plans. | A for AfDB documents. AfDB pages may show Cloudflare to curl; browser/search access still confirmed content. |
| PCH IXP directory | https://www.pch.net/ixp/details/1921 | Niger IXP status in Niamey; PCH showed a live page and the historical record. | A for PCH record. On-hold/no-facility evidence weakens commercial colo claims. |
| Official cloud region lists | AWS https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ ; Azure https://learn.microsoft.com/en-us/azure/reliability/regions-list ; Google https://cloud.google.com/about/locations ; Oracle https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm | Negative verification for hyperscaler regions/local zones. | A for the official lists. No Niger public cloud region was found on 2026-08-12. |

## 3. Official Query Templates

Search engines handle `site:` more reliably when each domain is queried separately. Use these as copy/paste lines, not as a single block.

```text
site:gouv.ne Niger "centre de données"
site:gouv.ne Niger datacenter
site:gouv.ne Niger "data center"
site:gouv.ne Niger "infrastructures numériques"
site:mcnti.gouv.ne "centre de données"
site:mcnti.gouv.ne datacenter
site:mcnti.gouv.ne "data center national"
site:mcnti.gouv.ne "Dorsale Transsaharienne"
site:ansi.ne Niger "centre de données"
site:ansi.ne Niger datacenter
site:ansi.ne Niger "cloud gouvernemental"
site:arcep.ne Niger "rapport annuel" opérateurs
site:arcep.ne Niger licence "Niger Telecoms"
site:arcep.ne Niger licence Airtel Zamani Moov
site:hapdp.ne "Loi-N°2022-59"
site:marchespublics.ne "data center"
site:marchespublics.ne "centre de données"
site:marchespublics.ne datacenter
site:marchespublics.ne "salle pilote"
site:armp-niger.org "data center" Niger
site:armp-niger.org "centre de données" Niger
site:nigelec.ne datacenter Niamey
site:nigelec.ne "poste de transformation" Niamey
site:arse.ne NIGELEC Niamey MW
site:afdb.org Niger DTS "data centre"
site:afdb.org Niger "centre de données" DTS
site:afdb.org "P-Z1-GB0-024" datacenter
```

For each project/operator:

```text
"{operator}" Niger "centre de données"
"{operator}" Niger datacenter
"{operator}" Niger hébergement colocation cloud
"{operator}" Niger "salle serveur"
"{operator}" Niamey NIGELEC
"{operator}" Niamey ARSE
"{operator}" Niger site:marchespublics.ne
```

## 4. Per-Division Enumeration Approach

| Division | Search aliases | Expected yield | Required strategy |
|---|---|---|---|
| Niamey | Niamey; Communauté Urbaine de Niamey; Plateau; Yantala; Gamkalley; Kouara Kano; PK5; Arrondissement Communal Niamey V | High by Niger standards | Exhaustive official sweep. Known leads: national Data Center / DTS data center at PK5-Niamey, Ministry of Finance data center procurement, MCNTI/ANSI/ARCEP/HAPDP, Niger Telecoms HQ/core, Airtel/Zamani/Moov cores, banks and government DR rooms. Count only named hosting/colo/cloud/compute facilities. |
| Agadez | Agadez; Arlit; Tchirozérine; mining corridor; Algeria route | Low | Negative sweep plus DTS/Algeria fibre route and mining telecom leads. Do not convert mine ICT rooms, towers or security posts into DC records. |
| Diffa | Diffa; N'Guigmi; Lake Chad corridor; Chad route | Lowest | Negative sweep. DTS route and government service buildings may appear; require official facility evidence. |
| Dosso | Dosso; Gaya; Benin/Cotonou route | Low | Negative sweep; look for Benin-border fibre, tax/customs systems, regional government server rooms. Count only if facility function is explicit. |
| Maradi | Maradi; Nigeria/Katsina/Kano corridor | Low | Negative sweep; watch Niger Telecoms mobile-site expansion and cross-border connectivity. Towers and PoPs are not datacenters. |
| Tahoua | Tahoua; Madaoua; Konni; Algeria/Nigeria corridors | Low | Negative sweep; power/fibre corridor evidence only unless a named hosting facility appears. |
| Tillabéri | Tillabéri; Tillabery; Téra; Burkina/Mali corridors | Low | Negative sweep; security context and border fibre only. Require strong official evidence for any site. |
| Zinder | Zinder; Magaria; Nigeria/Kano corridor | Low-medium | Search for legacy telecom exchange/core rooms, university/bank IT rooms and border fibre. Count only named hosting/colo/cloud facilities. |

Universal per-division sweep:

```text
"{division}" Niger "centre de données"
"{division}" Niger datacenter
"{division}" Niger "data center"
"{division}" Niger "salle serveur"
"{capital}" Niger "Niger Telecoms" "centre de données"
"{capital}" Niger Airtel Zamani Moov datacenter
site:anp.ne "{division}" "centre de données"
site:anp.ne "{division}" datacenter
site:marchespublics.ne "{division}" datacenter
site:marchespublics.ne "{division}" "fibre optique"
```

Exact 8-division quick sweep:

```text
Niamey Niger "centre de données"
Niamey Niger datacenter
Niamey Niger colocation
Agadez Niger "centre de données"
Agadez Niger datacenter
Diffa Niger "centre de données"
Diffa Niger datacenter
Dosso Niger "centre de données"
Dosso Niger datacenter
Maradi Niger "centre de données"
Maradi Niger datacenter
Tahoua Niger "centre de données"
Tahoua Niger datacenter
Tillabéri Niger "centre de données"
Tillabéri Niger datacenter
Tillaberi Niger "centre de données"
Tillaberi Niger datacenter
Zinder Niger "centre de données"
Zinder Niger datacenter
```

## 5. Reliability Grades

- **A:** primary official/operator record: government communiqué, ministry page, ARCEP report/decision, HAPDP legal text, ARMP/JMP/Portail tender or award, NIGELEC/ARSE document, AfDB project/procurement/E&S document, official operator facility page, official cloud-provider region page, PCH/PeeringDB network record.
- **B:** strong secondary: ANP or Le Sahel relaying a named official, Agence Ecofin/Ecofin Agency, Data Center Dynamics, Connecting Africa, Developing Telecoms, Telecom Review Africa, TechAfrica News, WeAreTech, credible vendor case study.
- **C:** discovery lead only: commercial directory, marketplace, social post, paid market report teaser, VPS reseller, old MoU, launch claim without site/power/operator evidence, generic server-room mention.
- **U:** no usable source, dead URL, unverifiable social claim, or claim unsupported by the cited page.

Grade each field separately. A-grade proof of a project does not make its Tier level, capacity, power, commissioning status or address A-grade unless those fields are directly supported. A "Tier III" marketing or ministerial phrase remains C/U until Uptime or an equivalent certification source names the facility.

## 6. Known Facilities / Projects and Evidence Status

| Project/operator | Location signal | Evidence | Grade | Treatment/status |
|---|---|---|---|---|
| National Data Center / DTS data center | Niamey; AfDB E&S search result identifies the EIES subproject as a national datacenter at PK5, Arrondissement Communal Niamey V; ANP gives Niamey article context but not street address. | ANP 2025-02-27 states the minister announced a national Data Center supported by AfDB for more than 9 billion FCFA, 13% execution, and planned reception by 2025-09-30: https://anp.ne/le-niger-entend-se-doter-dun-data-center-et-1000-km-de-fibre-optique-sur-axes-et-troncons-du-pays-ministre/ . AfDB project records for P-Z1-GB0-024 and E&S documents cover the DTS national datacenter scope: https://www.afdb.org/en/projects-and-operations/p-z1-gb0-024 and https://www.afdb.org/ar/documents/niger-projet-de-la-dorsale-transsaharienne-fibre-optique-dts-p-z1-gb0-024 . AfDB later reported provisional handover of more than 1,000 km of DTS fibre on 2025-11-14 and describes the project as 1,031 km of fibre plus a Tier III national data centre: https://www.afdb.org/en/news-and-events/press-releases/niger-takes-major-step-towards-high-speed-connectivity-handover-over-1000-km-fibre-optic-cable-88768 . | A for AfDB project scope; B+ for ANP ministerial status; C/U for Tier III certification and final commissioning until an official acceptance/certification document is found. | Treat all "national DC", "DTS Niamey DC" and ANSI/government-cloud references as the same physical program unless a source proves a distinct site. Do not create multiple records. |
| Ministry of Finance data center / DGMG procurement | Likely Niamey because it is Ministry of Finance central procurement, but the portal page does not expose a full address in the visible record. | Public procurement plan P_MF_2022_5 lists multiple data-center items: construction of datacenter enclosure/parking/guardhouse/toilet, finalization of internal cabling and interconnection, IT equipment for DataCenter and pilot room, telephone equipment and furniture: https://www.marchespublics.ne/marches-publics/572 . The provisional-award page includes "Construction et câblage d'un data centre", authority MINISTERE DES FINANCES, Avis TR_DGMG_034, date 2021-07-27, awardee Groupe BASSID SERVICES: https://www.marchespublics.ne/avis-dattribution-provisoire . | A for procurement existence; U for operational status, exact address, hosting role and whether it is the same as/older than the national DC. | Keep as a separate **government internal data-center lead** until deduped. Do not classify as commercial colocation. |
| DTS fibre backbone | National/cross-border: Algeria, Chad, Benin, Burkina Faso, Mali border; likely crosses/serves multiple regions. | ANP 2025 article states 1,031 km and 97% execution; AfDB 2025 press release reports provisional handover of more than 1,000 km on 2025-11-14. | A/B for backbone project; not a datacenter. | Use as connectivity context for regional sweeps, never as facility evidence. |
| Niger Telecoms | Niamey HQ plus regional telecom exchanges/backbone. | Operator seed from ARCEP 2024 report page and official site https://www.nigertelecoms.ne/ . | A for operator existence/licensing; C/U for DC classification. | Do not count exchanges, towers or backbone PoPs unless Niger Telecoms publishes a datacenter/hosting facility page or procurement/permit source names one. |
| Airtel Niger, Zamani Telecom, Moov Africa Niger | Niamey mobile/core infrastructure plus national networks. | ARCEP 2024 report page lists operator categories. Airtel Africa has official data-center activity in Lagos, Nigeria, not Niger: https://www.airtel.africa/data-centers . | A for operator/licence facts; U for Niger DC facilities. | Search each operator every cycle; do not import Nigeria or group-level data-center assets into Niger. |
| Niger IXP | Niamey. | PCH record https://www.pch.net/ixp/details/1921 . | A for PCH record. | Historical/on-hold interconnection lead, not an active colo facility. |
| Atal Networks "Niamey VPS" | Niamey claimed. | https://atalnetworks.com/niamey-niger-vps-server/ . | C/U. | Treat as reseller marketing unless it names a physical Niger facility/operator and that claim is corroborated. |
| Hyperscaler regions | None in Niger. | AWS, Azure, Google Cloud and Oracle official region lists checked 2026-08-12; none shows Niger. | A for negative list check. | Edge/CDN/customer presence is not a datacenter record. |

## 7. Per-Division Status Snapshot

| Division | Status as of 2026-08-12 | Action |
|---|---|---|
| Niamey | Only division with confirmed datacenter-project evidence. National/DTS data center is the primary record; Ministry of Finance data-center procurement is a separate internal-government lead pending dedup/status. | Exhaustive official/procurement/power follow-up. |
| Agadez | No facility record found; DTS/Algeria corridor and mining telecom only. | Negative sweep and power/fibre check. |
| Diffa | No facility record found; DTS Chad corridor/security-affected. | Negative sweep only; require A/B evidence. |
| Dosso | No facility record found; Benin corridor context only. | Negative sweep and procurement search. |
| Maradi | No facility record found; Nigeria corridor and mobile-site activity only. | Negative sweep; do not count towers. |
| Tahoua | No facility record found. | Negative sweep and power/fibre check. |
| Tillabéri | No facility record found; border/security context. | Negative sweep; require official source. |
| Zinder | No facility record found; possible legacy telecom exchange/core leads only. | Search telecom/bank/university terms but count only facility proof. |

## 8. Update / Re-check Cadence

- **Monthly:** MCNTI, gouv.ne council communiqués, ANP, Le Sahel, marchespublics.ne, ARMP/JMP, ARCEP notices, AfDB P-Z1-GB0-024 procurement/project pages.
- **Quarterly:** NIGELEC/ARSE, HAPDP lists, PCH and PeeringDB, DataCenterMap/Baxtel/DataCenterPlatform/Inflect, DCD, Agence Ecofin, WeAreTech, Connecting Africa, TechAfrica News, Telecom Review Africa.
- **Semi-annual:** AWS/Azure/GCP/OCI region lists, Uptime Institute certification directory, submarine-cable maps for the negative landlocked check.
- **Event-driven:** national-DC reception/inauguration, publication of an EIES/acceptance certificate, Zamani/Niger Telecoms merger actions, AES regional digital-infrastructure announcements, ARCEP licence changes or major power-grid events.

## 9. Exclusion Rules

Do not create datacenter records from cybercafes, ordinary web-hosting resellers, offshore VPS pages, university labs, ministry server rooms, bank DR rooms, tower sites, fibre shelters, NOCs, digital hubs, incubators, smart-city offices, or ARCEP licences unless the source proves a physical hosting/colo/cloud/compute facility in Niger. Keep a separate lead note when a source may later mature into facility evidence.
