# GA Explorer Industry - Gabon Datacenter Enumeration

Date: 2026-08-12. Scope: industry/operator methodology for **GA - Gabon** (`Republique Gabonaise`). Target division model remains the requested **9 manifest provinces**: Estuary; Upper Ogooue; Middle Ogooue; Ngounie; Nyanga; Ogooue-Ivindo; Ogooue-Lolo; Maritime Ogooue; Woleu-Ntem (French: Estuaire; Haut-Ogooue; Moyen-Ogooue; Ngounie; Nyanga; Ogooue-Ivindo; Ogooue-Lolo; Ogooue-Maritime; Woleu-Ntem).

Reliability grades:
- **A** = official operator page, official cloud-region page, regulator/ministry/agency/donor/IXP primary page, Uptime Institute record, signed company press release.
- **B** = credible trade press, industry association, Euro-IX ixpdb, local press quoting named officials/operators.
- **C** = directory, marketplace, market report, aggregator, social post, generic vendor claim, ambiguous POP/hosting/cloud lead.

## 0. Market Assumptions

- The active public datacenter market is concentrated in **Estuary province**: **Libreville** (Moov Africa Gabon Telecom Cenacom DC1, Airtel Gabon lead, ANINF legacy state DC, GABIX POPs) and the **Nkok Special Economic Zone** (~30 km from Libreville; ST Digital lbv01 operational since Jul 2026; ANINF/Cybastion 20 MW project under development).
- **Yield honesty**: expect **2-4 confirmed physical facilities country-wide** and at most 4-7 records including leads. Every other province is expected to return no public colocation; record them with explicit `no public colocation expected` coverage rather than padding.
- Strongest facility seeds: ST Digital Nkok lbv01 (official page + Jul 2026 opening); Moov Africa Gabon Telecom DC1 Cenacom (Uptime Institute record); Cybastion/Gabon/ANINF sovereign DC project reported at 20 MW (company PR + DCD); ANINF/state national-DC programme lead (agency project/article pages); Airtel Gabon Libreville (directory C).
- Official public-cloud pages show **no AWS/Azure/GCP/OCI region in GA**. Treat global-cloud references as reseller, CDN, on-ramp, or tenant leads unless an official region/facility page names Gabon.
- Telco POPs, tower shelters, cable landing stations (ACE Libreville; Medusa Port-Gentil 2026-27), IXP POPs, university labs, and enterprise server rooms are **not datacenters** unless the source names colocation, racks, white space, datacenter rooms, Tier design/certification, or a significant sovereign/enterprise hosting function.
- **URL validation note, 2026-08-12**: core operator/official pages were checked live. Most returned HTTP 200 to command-line probes; protected or intermittently proxied sites (for example ISOC Pulse/Uptime/news directories) may return 403/429/522 to curl while rendering through browser/search tooling. The old draft ministry short path `/aninf` returned 404 and is not used here. Use protected directory/news pages as B/C support, not sole proof.

## 1. Operator and Facility Seeds

| Operator / facility | Province | Evidence | Grade | Action |
|---|---|---|---|---|
| **ST Digital Data Center Services - Nkok DC (lbv01)** | Estuary | Official datacenter page: https://st.digital/datacenter/lbv01 (operational, 1 MW, Tier 3 certified claim, solar/green design, water-free cooling, colocation/IaaS/SaaS); datacenters index: https://st.digital/en/datacenters; colocation: https://st.digital/en/colocation; sovereign-cloud partnership blog: https://st.digital/blog/nos-actualites-1/datacenter-de-nkok-st-digital-lapdpvp-et-le-ministere-de-leconomie-numerique-scellent-un-partenariat-pour-une-infrastructure-cloud-souveraine-et-conforme-544; DCD opening report: https://www.datacenterdynamics.com/en/news/cameroons-st-digital-opens-data-center-in-gabon/; We Are Tech capacity/cost report: https://www.wearetech.africa/en/fils-uk/news/tech/gabon-launches-14-million-tier-iii-data-center-in-digital-sovereignty-push | A for service/location; B for published capacity/cost; Uptime certification unverified | **Record as operator-confirmed operational facility**. DCD reports opening on 3 Jul 2026 after Aug 2025 groundbreaking; ST Digital page proves current operational status and services. Search for exact address/parcel in Nkok SEZ, APDPVP filings, PeeringDB facility, customers, and operator-confirmed capacity. Keep Tier III as claim until Uptime lists lbv01. |
| **Cybastion / Government of Gabon / ANINF sovereign data center project (reported 20 MW)** | Estuary / Libreville-Nkok corridor; exact site unresolved | Cybastion PR: https://www.cybastiontech.com/cybastion-government-of-gabon-and-aninf-sign-historic-digital-infrastructure-agreement/; DCD: https://www.datacenterdynamics.com/en/news/cybastion-to-build-20mw-data-center-in-gabon/; w.media (Porteo Group/gas plant context): https://w.media/st-digital-opens-gabons-first-sovereign-tier-iii-data-center/; Le360: https://afrique.le360.ma/economie/gabon-un-futur-data-center-national-concu-par-lamericain-cybastion-le-modele-america-first-a-loeuvre_UZQ5ZK7ZLBHY3KMVQMF4JYEDMA/ | A for agreement/scope; B for 20 MW, site, contractor, power details | Treat as separate planned/development project. Cybastion's official release proves the sovereign-DC agreement; DCD/Le360 supply the 20 MW and gas-plant details. Confirm whether later official pages place it at Nkok or elsewhere in Libreville before assigning final site/address. |
| **Moov Africa Gabon Telecom - DC1, Cenacom Building, Libreville** | Estuary | Uptime Institute: https://uptimeinstitute.com/component/tierachievement/datacenter/dc1-cenacom-building-libreville/2003; operator: https://www.moov-africa.ga/; GABIX POP CT-1 adjacency: https://ixpdb.euro-ix.net/en/explore/ixp/807/pops/ | A for existence; tier level/date to confirm | Legacy operator DC (ex-Gabon Telecom, Maroc Telecom group). Confirm tier level/date on Uptime list, exact address (Cenacom building), capacity, and whether third-party colocation is offered. GABIX CT-1 shows Moov and ST Digital network presence, but the POP itself is not a separate DC. |
| **ANINF / state national data-center programme lead - Libreville** | Estuary | ANINF project page: https://aninf.ga/projet/data-center-national-garantir-la-souverainete-des-donnees/; ANINF launch/current narrative: https://aninf.ga/souverainete-numerique-le-gabon-lance-son-data-center-national-et-affirme-son-independance-technologique/; reinforcement press: https://www.nouvelles-du-monde.com/gabon-renforce-son-centre-de-donnees-national-pour-assurer-la-souverainete-numerique/ | A for programme; C for unresolved facility identity | State programme/facility lead; address/identity unresolved. Search ANINF official pages, L'Union/Gabon Review, and APDPVP compliance notes for a physical Libreville site. Keep separate from ST Digital Nkok and the Cybastion agreement unless official ownership/address evidence merges them. |
| **Airtel Gabon S.A. - Libreville** | Estuary | colo.exchange: https://colo.exchange/data-centers/airtel-gabon-sa-airtel-gabon; market page: https://colo.exchange/locations/ga/estuaire/libreville; GABIX member: https://ixpdb.euro-ix.net/en/explore/ixp/807/pops/ | C until operator/PeeringDB confirmation | Lead for an Airtel-operated facility. Verify with Airtel Gabon official pages, PeeringDB facility/ASN records, ARCEP licence, or customer references before counting. |
| **GABIX (GAB-IX) - Libreville** | Estuary | Official: https://www.gabix.ga/ (GIE since 2014, Ancienne RTG - Libreville); ANINF: https://aninf.ga/projet/point-dechange-internet-gab-ix-le-hub-internet-gabonais/; Euro-IX ixpdb: https://ixpdb.euro-ix.net/en/explore/ixp/807/pops/ (POP ACE + POP CT-1; ANINF 10G, Airtel, GVA, Moov, ST Digital, PCH, iPi9, GBM/TLDC depending on POP); ISOC Pulse: https://pulse.internetsociety.org/fr/ixp-tracker/ixp/555/; relaunch: https://lefinancierdafrique.com/open/2026/05/15/numerique-le-gabon-relance-son-point-dechange-internet/ | A/B | IXP, not a DC. Use POP locations to locate carrier rooms: POP ACE at the ACE landing station; POP CT-1 at/near Cenacom building. Do not accept directory claims that GABIX POP CT-1 is a standalone 3 MW datacenter without host/operator proof. |
| **SPIN / ACE Gabon - Libreville landing station; Medusa - Port-Gentil** | Estuary; Maritime Ogooue | SPIN: https://spin.ga/nos-activites/ace-gabon/; Medusa official C&MA release: https://medusascs.com/news/ace-gabon-and-medusa-africa-sign-construction-and-maintenance-agreement-for-medusa-submarine-cable-landing-in-port-gentil/; Medusa local coverage: https://gabonactu.com/blog/2025/03/17/resilience-numerique-au-gabon-bientot-un-nouveau-cable-sous-marin-medusa/ and https://gabonmediatime.com/gabon-vers-la-construction-du-cable-sous-marin-optique-medusa-afrique/ | A for ACE station; A/B for Medusa agreement; B for local build details | Landing stations are connectivity. Medusa Port-Gentil is a future adjacency lead for Maritime Ogooue. Count only adjacent rack/colo facilities. |
| **Shapoorji Pallonji MoU - national data center** | n/a | Baxtel: https://baxtel.com/news/shapoorji-pallonji-signs-mou-to-build-data-center-in-gabon | C | Historical lead; likely superseded. Search for award/termination news; do not count without official evidence. |
| **GVA, iPi9, Packet Clearing House, General Business Machines, TLDC, ST Digital-AS and other GABIX members** | Estuary | GABIX/Euro-IX/ISOC membership: https://ixpdb.euro-ix.net/en/explore/ixp/807/pops/ and https://pulse.internetsociety.org/fr/ixp-tracker/ixp/555/ | B for network presence | Pivot each into POP/cache/hosting searches. Most are network leads only; require facility language for DC inventory. |
| **Azur Telecom (ex-operator)** | n/a | Agence Ecofin: https://www.agenceecofin.com/dossier/2311-52310-radiographie-d-azur-telecom-l-operateur-en-danger-au-gabon-au-congo-et-en-centrafrique | B for market context | Defunct/declining regional operator; historical infrastructure only. |
| **Enterprise/private IT (TotalEnergies, Perenco, VAALCO, Eramet/Comilog, SETRAG, BGFI, Ecobank, UBA)** | Maritime Ogooue; Upper Ogooue; Estuary; multi | Company sites + trade press | B/C | Private server rooms/DR sites. Do not count as public colocation unless a colocation/DC service is offered publicly. |

## 2. Cloud, CDN, and On-Ramp Checks

Official public-region sources, used as A-grade negative controls:

| Provider | Official URL | Current GA finding |
|---|---|---|
| AWS | https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | No Gabon region. Africa public region is South Africa/Cape Town. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No Gabon region. South Africa North/West are the Africa public regions. |
| Google Cloud | https://cloud.google.com/about/locations | No Gabon region. `africa-south1` is Johannesburg, South Africa. |
| Oracle OCI | https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm | No Gabon region. `af-johannesburg-1` is South Africa Central. |

On-ramp/CDN searches:

```text
"Libreville" ("AWS Direct Connect" OR ExpressRoute OR "Cloud Interconnect" OR FastConnect OR CDN OR edge)
"Port-Gentil" ("AWS" OR Azure OR "Google Cloud" OR Oracle OR Cloudflare OR Akamai) (datacenter OR "data center" OR POP)
"ST Digital" Nkok (cloud OR colocation OR peering OR souverain)
"Moov Africa Gabon Telecom" (cloud OR hebergement OR datacenter OR colocation OR "centre de donnees")
"GABIX" (Cloudflare OR Google OR Meta OR Facebook OR Akamai OR CDN OR membres)
"ACE Gabon" (POP OR "salle serveurs" OR datacenter OR racks)
```

## 3. Industry Sources by Type

High-value sources:
- **Operator official pages (A)**: ST Digital (https://st.digital/en/datacenters, https://st.digital/datacenter/lbv01), Moov Africa Gabon Telecom (https://www.moov-africa.ga/), SPIN/ACE Gabon (https://spin.ga/), ANINF (https://aninf.ga/), Cybastion (https://www.cybastiontech.com/), Medusa (https://medusascs.com/).
- **IXP/peering sources (A/B)**: GABIX (https://www.gabix.ga/); Euro-IX ixpdb GABIX (https://ixpdb.euro-ix.net/en/explore/ixp/807/pops/); PeeringDB (https://www.peeringdb.com/); ISOC Pulse GABIX page (https://pulse.internetsociety.org/fr/ixp-tracker/ixp/555/); TeleGeography Internet Exchange Map (https://www.internetexchangemap.com/).
- **Donor/government project pages (A/B)**: Cybastion PR (28 Jun 2025); AfDB Gabon pages; World Bank Gabon project list (https://projects.worldbank.org/en/projects-operations/projects-list?countrycode_exact=GA); ministry/ANINF pages.
- **Trade press (B)**: Agence Ecofin, DCD (Data Center Dynamics), Digital Business Africa, We Are Tech Africa, Gabon Review, L'Union (sonapresse), Gabon Actu, Gabon Media Time, AGP, Convergence Afrique, Le360 Afrique, Ogooue News, Infos Gabon, Le Financier d'Afrique, OSIRIS, Tech in Africa, Pouvoirs Afrique, Kongossa News, Finances A.O., Digital Magazine (BF).
- **Directories (C)**: DataCenterMap (https://www.datacentermap.com/gabon/ and /gabon/libreville/), colo.exchange (https://colo.exchange/locations/ga/estuaire/libreville), DataCenters.com (https://www.datacenters.com/locations/gabon/estuaire/libreville), Inflect (https://inflect.com/datacenters/emea/gabon/), Baxtel (https://baxtel.com/), DataCenterPlatform (https://datacenterplatform.com/data-centers/gabon-internet-exchange-gabix/), DataCenterJournal (https://www.datacenterjournal.com/data-centers/gabon/libreville/gabix-pop-ct-1/), Tracxn. Use for aliases and addresses only until joined.

Directory URLs to check as leads:

```text
https://www.datacentermap.com/gabon/
https://www.datacentermap.com/gabon/libreville/
https://colo.exchange/locations/ga/estuaire/libreville
https://colo.exchange/data-centers/airtel-gabon-sa-airtel-gabon
https://www.datacenters.com/st-digital-st-digital-gabon-nkok
https://www.datacenters.com/locations/gabon/estuaire/libreville
https://inflect.com/datacenters/emea/gabon
https://datacenterplatform.com/data-centers/gabon-internet-exchange-gabix/
https://www.datacenterjournal.com/data-centers/gabon/libreville/gabix-pop-ct-1/
```

## 4. Query Library

Core disambiguated queries:

```text
(Gabon OR Libreville OR "Port-Gentil") (datacenter OR "data center" OR "centre de donnees" OR colocation) -Congo -Brazzaville -Kinshasa -Douala
(Gabon OR Libreville) ("Tier III" OR "Tier 3" OR "Tier 3+" OR "Uptime Institute")
(Gabon OR Libreville) ("cloud souverain" OR "souverainete numerique" OR "coffre-fort numerique")
(Gabon OR Libreville OR Nkok) (GABIX OR GAB-IX OR "point d'echange Internet")
"data center national" Gabon Nkok OR ANINF OR Cybastion OR "ST Digital"
```

Vendor pivots:

```text
"ST Digital" Nkok datacenter OR colocation OR "Tier III" OR lbv01
"ST Digital" Gabon "Data Center Services"
"Cybastion" Gabon datacenter OR "20 MW" OR ANINF
"ANINF" Nkok OR Libreville datacenter OR "centre de donnees"
"Moov Africa Gabon Telecom" Cenacom OR datacenter OR "salle serveurs"
"Airtel Gabon" datacenter OR colocation OR hebergement Libreville
"ACE Gabon" station OR datacenter OR POP Libreville
"Medusa" Gabon "Port-Gentil" cable OR datacenter
"GABIX" membres OR peering OR POP OR CT-1
"Gabon Telecom" datacenter USTM OR Franceville OR hebergement
"Shapoorji Pallonji" Gabon datacenter
```

Trade-source scoped queries:

```text
site:agenceecofin.com Gabon datacenter OR "centre de donnees"
site:datacenterdynamics.com Gabon "data center"
site:digitalbusiness.africa Gabon datacenter
site:gabonreview.com datacenter OR "data center"
site:union.sonapresse.com "data center" OR datacenter
site:gabonactu.com datacenter OR "data center"
site:gabonmediatime.com datacenter OR "data center"
site:wearetech.africa Gabon "data center"
site:le360.ma Gabon datacenter
site:agpgabon.ga datacenter OR "centre de donnees"
site:ogoouenews.com datacenter OR "data center"
```

## 5. Province-by-Province Industry Pattern

For each province use:

```text
("{province}" OR "{city}" OR "{alias}") (datacenter OR "data center" OR "centre de donnees" OR colocation OR hebergement OR "salle serveurs") Gabon -Congo
("{city}" OR "{province}") ("fibre optique" OR backbone OR BNG OR POP OR "point de presence" OR IXP OR GABIX OR "station d'atterrissage" OR "atterrissement") ("{operator}" OR datacenter OR hebergement)
("{operator}") ("{city}" OR "{province}") (datacenter OR colocation OR hebergement OR POP OR "salle serveurs")
```

| Manifest province | Industry aliases | Priority | Industry strategy |
|---|---|---:|---|
| Estuary / Estuaire | Libreville (Batterie IV, Oloumi, Mont-Bouet, Nzeng-Ayong, Glass, Akanda, Owendo, Ancienne RTG, Cenacom, Tour ANINF), Nkok SEZ, Ntoum, Kango, Cocobeach | Very high | Seed ST Digital lbv01, Cybastion/Gabon sovereign DC project, Moov Africa Gabon Telecom Cenacom DC1, ANINF/state programme lead, Airtel Gabon, GABIX POP ACE + CT-1, ACE station. Dedupe Nkok/Libreville storylines by operator, address, and date. |
| Upper Ogooue / Haut-Ogooue | Franceville, Moanda, Mounana, Okondja, Akieni, Lekoni, USTM/Masuku | Medium | USTM labs are education-only. Search Comilog/Moanda mining IT rooms (private), Grand Poubara power, BNG fibre. No public colocation expected. |
| Middle Ogooue / Moyen-Ogooue | Lambarene, Ndjole, Bifoun | Low/medium | Ndjole = future Medusa/BNG junction. Hospital/administration rooms; APDPVP inspection leads. No public colocation expected. |
| Ngounie | Mouila, Fougamou, Mbigou, Mimongo, Ndende, Lebamba, Bongolo | Low | Bongolo power and government rooms. No public colocation expected. |
| Nyanga | Tchibanga, Mayumba, Moabi, Mabanda | Low | Mayumba port/oil adjacency, border connectivity. No public colocation expected. |
| Ogooue-Ivindo | Makokou, Booue, Mekambo, Ovan | Low | BNG/VSAT and forestry-town rooms. No public colocation expected. |
| Ogooue-Lolo | Koulamoutou, Lastoursville, Iboundji | Low | BNG corridor rooms; avoid power-only false positives. No public colocation expected. |
| Maritime Ogooue / Ogooue-Maritime | Port-Gentil, Omboue, Gamba, Sette Cama, Cap Lopez | Medium | Oil-company private IT (TotalEnergies, Perenco, VAALCO) - private only; gas thermal power; **Medusa landing (2026-27)** as future adjacency. No public colocation today. |
| Woleu-Ntem | Oyem, Bitam, Minvoul, Mitzic, Medouneu | Low/medium | Cameroon border corridor, government/health IT rooms. No public colocation expected. |

## 6. Verification and Dedupe Rules

1. **Operator page beats directory.** If ST Digital/Moov Africa Gabon Telecom/ANINF confirms a facility, grade only the confirmed facts A; keep directory-only capacity/address as C until matched.
2. **Separate the three Nkok/Libreville leads.** ST Digital lbv01 (operational), Cybastion/Gabon/ANINF sovereign DC project (planned/development, reported 20 MW), and ANINF/state programme or legacy-facility lead may be conflated in `data center national` headlines. Merge only on exact address/operator/ownership evidence from ANINF, the ministry, ST Digital, or Cybastion.
3. **Uptime records.** The only Uptime record found for GA is Moov Africa Gabon Telecom DC1, Cenacom Building, Libreville (tier level/date to confirm on the list). ST Digital's `Tier 3 Certified` claim for Nkok is not yet on the located Uptime record set - keep it as an operator claim.
4. **Landing stations are connectivity, not colocation.** ACE Libreville and Medusa Port-Gentil are strong network-adjacency leads but must not be counted as datacenters by themselves.
5. **GABIX POPs are IXP colocation, not DCs.** POP ACE and POP CT-1 identify carrier rooms at the ACE station and the Cenacom building respectively; only count a host as a DC when rack/colo evidence exists.
6. **USTM Franceville labs are donations, not commercial DCs.** Exclude university data-center labs from the inventory.
7. **Do not upgrade MoU/leads without new evidence.** Shapoorji Pallonji MoU and Airtel Gabon directory entries stay C/lead-only until operator or PeeringDB confirmation.
8. **Attribute the ~8 bn FCFA figure to its exact source.** Some outlets tie it to the ST Digital-inaugurated DC, others to the national-DC convention; record cost figures with the source URL and date.
9. **Mind ST Digital page copy.** ST Digital group pages can mix country-market content; verify any Cote d'Ivoire/Cameroon/Togo/Congo claim against the Gabon Nkok facility before recording.
10. **Keep status dates explicit.** Examples: Cybastion strategic agreement reported 28 Jan 2025; State/ANINF/Cybastion agreement 28 Jun 2025; ST Digital Nkok groundbreaking reported Aug 2025 and opening 3 Jul 2026; GABIX relaunch reported May 2026; Medusa C&MA signed 19 Mar 2025 with Port-Gentil landing as connectivity adjacency.
