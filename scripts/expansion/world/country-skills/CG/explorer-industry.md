# CG Explorer Industry - Republic of the Congo Datacenter Enumeration

Date: 2026-08-12. Scope: industry/operator methodology for **CG - Republic of the Congo / Congo-Brazzaville**. Target division model remains the requested **12 legacy/manifest departments**: Bouenza; Brazzaville; Cuvette; Cuvette-Ouest / West Cuvette; Kouilou; Lekoumou; Likouala; Niari; Plateaux; Pointe-Noire / Black Point; Pool; Sangha.

Note for search coverage: Congo government sources now use a 15-department frame after the 2024 reform. Keep the output keyed to the 12 requested divisions, but add current-name queries for **Nkeni-Alima**, **Djoue-Lefini**, and **Congo-Oubangui** so newer news is not missed.

Reliability grades:
- **A** = official operator page, official cloud-region page, regulator/ministry/donor/IXP primary page, Uptime Institute record.
- **B** = credible trade press, industry association, French Treasury market note, local press quoting named officials/operators.
- **C** = directory, marketplace, market report, social post, generic vendor claim, ambiguous POP/hosting/cloud lead.

## 0. Market Assumptions

- The active public datacenter market is concentrated in **Brazzaville** and **Pointe-Noire**. Oyo in Cuvette is a planned/tendered secondary national-datacenter and IXP lead, not confirmed operational.
- Strongest facility seeds: ST Digital Brazzaville official service page; ARPCE Pointe-Noire Tier 3+ data center and CGIX-PN host; AfDB/ministry Bacongo national datacenter project; ARPCE Brazzaville 2021 lead; Congo Telecom Pointe-Noire carrier/landing ecosystem.
- Official public-cloud pages show no AWS/Azure/GCP/OCI region in CG. Treat global-cloud references as reseller, CDN, on-ramp, or tenant leads unless an official region/facility page names Congo-Brazzaville.
- Telco POPs, tower shelters, cable landing stations, and offices are not datacenters unless the source names colocation, racks, white space, datacenter rooms, Tier design/certification, or a significant sovereign/enterprise hosting function.

## 1. Operator and Facility Seeds

| Operator / facility | Department | Evidence | Grade | Action |
|---|---|---|---|---|
| **ST Digital Brazzaville** | Brazzaville | Official datacenter page: https://st.digital/en/datacenters and https://st.digital/datacenters; colocation page: https://st.digital/en/colocation; cloud marketplace: https://cloudstore.africa/ | A for service/location; Uptime certification unverified | Record as an operator-confirmed Brazzaville datacenter/colocation/cloud facility. Search for address, ARPCE/ANSSI compliance, PeeringDB facility, customer references, and exact capacity. |
| **Datacenter national du Congo - Bacongo** | Brazzaville | AfDB official: https://www.afdb.org/fr/news-and-events/congo-le-nouveau-datacenter-finance-par-la-banque-africaine-de-developpement-va-consacrer-la-souverainete-numerique-du-pays-et-de-la-sous-region-70845; ministry: https://postetelecom.gouv.cg/congo-vers-une-revolution-numerique-avec-le-lancement-imminent-du-data-center-national/; latest status press: https://www.digitalbusiness.africa/congo-le-datacenter-national-operationnel-dici-mai-2026-selon-le-president-de-la-bad/ | A for project/finance; B for May 2026 status | Treat as confirmed project under construction/near commissioning unless a newer official inauguration appears. Do not mark operational from old target-date articles alone. |
| **ARPCE Data Center Pointe-Noire** | Pointe-Noire | DCD: https://www.datacenterdynamics.com/en/news/republic-of-congo-launches-data-center-in-pointe-noire-for-2africa-cable/; Agence Ecofin: https://www.agenceecofin.com/equipement/2902-116638-le-congo-renforce-son-infrastructure-numerique-avec-la-mise-en-service-d-un-nouveau-centre-de-donnees-de-6-3-millions-nbsp; ADIAC CGIX-PN host: https://www.adiac-congo.com/content/technologie-lancement-du-deuxieme-point-cgix-de-larpce-pointe-noire-159992; directory: https://www.datacenters.com/arpce-arpce-pointe-noire-tier-3 | B; directory C | Operational/commissioned facility. Use 54 racks/156 sqm/3.8bn FCFA figures only as B/C until ARPCE datasheet confirms. Confirm exact address and operator access model. |
| **ARPCE Brazzaville 2021 datacenter** | Brazzaville | DCD/Telecompaper quote ARPCE DG on a Brazzaville datacenter built in 2021: https://www.datacenterdynamics.com/en/news/republic-of-congo-launches-data-center-in-pointe-noire-for-2africa-cable/; https://www.telecompaper.com/news/congo-launches-facility-to-store-sovereign-data-in-pointe-noire--1494296 | B lead | Resolve identity. Keep separate from ST Digital and the AfDB Bacongo national DC until address/operator evidence proves a merge. |
| **Data center national secondaire - Oyo** | Cuvette | Tender: https://www.agenceecofin.com/breves-telecom/2502-95380-congo-12-societes-se-disputent-le-marche-de-construction-des-deux-centres-de-donnees-nationaux | B tender | Planned only. Search for award, Sumec or alternate contractor, site works, E2C connection, inauguration, or CGIX Oyo deployment. |
| **Congo Telecom PNR1 / carrier facility** | Pointe-Noire | Directories: https://colo.exchange/data-centers/congo-telecom-congo-telecom-carrier-facility-pnr1; https://www.datacenterslist.com/data-centers/congo-telecom-carrier-facility-pnr1-pointe-noire; Congo Telecom: https://congotelecom.cg/; ministry organ: https://postetelecom.gouv.cg/organes/congo-telecom/ | C until operator/PeeringDB confirmation | Lead for carrier facility near cable ecosystem. Verify with Congo Telecom pages, PeeringDB, customer ASN/facility references, or ARPCE records before counting. |
| **WACS Matombi / 2Africa Pointe-Noire landing ecosystem** | Kouilou / Pointe-Noire | French Treasury sector note: https://www.tresor.economie.gouv.fr/Pays/CG/le-secteur-du-numerique; DCD 2Africa/DC article above | B for connectivity | Landing stations are not datacenters. Use to find adjacent carrier rooms, backhaul PoPs, and Congo Telecom/Congo Cables facilities. |
| **CEC Telecom / Congo Electronic Center** | Brazzaville service lead | https://congoelectronicenter.com/ | C | Integrator/vendor lead. Do not count unless a Congo-Brazzaville facility/address and colocation/hosting evidence appears. |
| **SOFIA, GVA/Canal Box, MTN, Airtel, Alink, AMC, PI Service/Sky TIC, Silicone Connect, Mambs Services** | Multi-department | French Treasury market note: https://www.tresor.economie.gouv.fr/Pays/CG/le-secteur-du-numerique; ministry operator pages; ARPCE records | B for market/operator existence | Pivot each into POP/datacenter/hosting searches. Most are network leads only. Require facility language for DC inventory. |

## 2. Cloud, CDN, and On-Ramp Checks

Official public-region sources, used as A-grade negative controls:

| Provider | Official URL | Current CG finding |
|---|---|---|
| AWS | https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | No Republic of Congo region. Africa public region is South Africa/Cape Town. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No Republic of Congo region. South Africa North/West are the Africa public regions. |
| Google Cloud | https://cloud.google.com/about/locations and https://docs.cloud.google.com/compute/docs/regions-zones | No Republic of Congo region. `africa-south1` is Johannesburg, South Africa. |
| Oracle OCI | https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm | No Republic of Congo region. `af-johannesburg-1` is South Africa Central. |

On-ramp/CDN searches:

```text
"Brazzaville" ("AWS Direct Connect" OR ExpressRoute OR "Cloud Interconnect" OR FastConnect OR CDN OR edge)
"Pointe-Noire" ("AWS" OR Azure OR "Google Cloud" OR Oracle OR Cloudflare OR Akamai) (datacenter OR "data center" OR POP)
"ST Digital" Brazzaville (cloud OR colocation OR peering OR souverain)
"Congo Telecom" (cloud OR hebergement OR datacenter OR colocation OR "centre de donnees")
"CGIX" (Cloudflare OR Google OR Meta OR Akamai OR CDN OR membres)
```

## 3. Industry Sources by Type

High-value sources:
- **Operator official pages (A)**: ST Digital, Congo Telecom, ARPCE/ministry operator pages, cloud provider region pages.
- **IXP/peering sources (A/B)**: ARPCE IXP page https://www.arpce.cg/point-echange-internet; ISOC Pulse country tracker https://pulse.internetsociety.org/fr/ixp-tracker/country/CG/; PeeringDB facility and IXP records.
- **Donor/government project pages (A)**: AfDB national datacenter/CAB pages; World Bank PATN pages; government/ministry pages.
- **Trade press (B)**: Agence Ecofin, DCD, Digital Business Africa, Telecompaper, We Are Tech Africa, ADIAC, ACI, Vox.cg, Tribune-Eco, Pages Afrik, Journal de Brazza, Les Depeches de Brazzaville.
- **Directories (C)**: DataCenterMap, DataCenters.com, DataCentersList, colo.exchange, Inflect, Neocloud. Use for aliases and addresses only until joined.

Directory URLs to check as leads:

```text
https://www.datacentermap.com/congo-brazzaville/
https://www.datacenters.com/arpce-arpce-pointe-noire-tier-3
https://www.datacenterslist.com/data-centers/country/cg
https://colo.exchange/data-centers/congo-telecom-congo-telecom-carrier-facility-pnr1
https://inflect.com/datacenters/emea/congo-brazzaville
```

## 4. Query Library

Core disambiguated queries:

```text
("Republique du Congo" OR "Congo-Brazzaville" OR Brazzaville OR "Pointe-Noire") (datacenter OR "data center" OR "centre de donnees" OR colocation)
("Congo-Brazzaville" OR "Republic of Congo") ("Tier III" OR "Tier 3" OR "Tier 3+" OR "Uptime Institute")
("Congo-Brazzaville" OR Brazzaville) ("cloud souverain" OR "souverainete numerique" OR "coffre-fort numerique")
("Congo-Brazzaville" OR "Pointe-Noire") (IXP OR CGIX OR "CGIX-PN" OR "point d'echange Internet")
"Congo" datacenter -RDC -Kinshasa -Lubumbashi -ARPTC
```

Vendor pivots:

```text
"ST Digital" Brazzaville datacenter OR colocation OR "Tier III"
"ARPCE" "Pointe-Noire" datacenter OR "Tier 3+"
"ARPCE" Brazzaville datacenter 2021
"datacenter national" Congo Bacongo OR Brazzaville OR Sumec OR BAD OR AfDB
"Oyo" "datacenter" Congo OR "centre de donnees"
"Congo Telecom" PNR1 OR datacenter OR hebergement OR Matombi
"Congo Cables" "2Africa" Pointe-Noire OR Matombi
"SOFIA" "Pointe-Noire" fibre OR hebergement OR datacenter
"Silicone Connect" fibre E2C Congo datacenter OR POP
"Mambs Services" CAB Congo fibre POP
```

Trade-source scoped queries:

```text
site:agenceecofin.com Congo datacenter OR "centre de donnees"
site:datacenterdynamics.com "Republic of Congo" "data center"
site:digitalbusiness.africa Congo datacenter
site:adiac-congo.com datacenter Congo
site:aci.cg CGIX Pointe-Noire
site:wearetech.africa Congo "data center"
site:telecompaper.com Congo "data centre" ARPCE
site:lesdepechesdebrazzaville.fr datacenter
site:lejournalducongo.com "data center" OR datacenter
```

## 5. Department-by-Department Industry Pattern

For each department use:

```text
("{department}" OR "{city}" OR "{alias}") (datacenter OR "data center" OR "centre de donnees" OR colocation OR hebergement OR "salle serveurs") Congo -RDC
("{city}" OR "{department}") ("fibre optique" OR backbone OR POP OR "point de presence" OR IXP OR CGIX OR "station d'atterrage") ("{operator}" OR datacenter OR hebergement)
("{operator}") ("{city}" OR "{department}") (datacenter OR colocation OR hebergement OR POP OR "salle serveurs")
```

| Manifest department | Industry aliases | Priority | Industry strategy |
|---|---|---:|---|
| Bouenza | Madingou, Nkayi, Moukoukoulou | Medium | Search energy/fibre operators and E2C aerial-fibre corridor. Possible enterprise/server-room leads only. |
| Brazzaville | Bacongo, Makelekele/Makélékélé, Poto-Poto, Moungali, Ouenze/Ouenzé, Talangai/Talangaï, Mfilou, Madibou, Djiri, Mpila | Very high | Start with ST Digital, national DC, ARPCE 2021, CGIX-BZV, Congo Telecom, MTN/Airtel. Dedupe by date and owner. |
| Cuvette | Owando, Oyo, Boundji, Mossaka/Congo-Oubangui overlay | High planned | Oyo secondary national DC and planned third CGIX. Search award/construction and operator references. |
| Cuvette-Ouest / West Cuvette | Ewo, Kelle, Mbomo, Etoumbi, Okoyo | Low | Only run broad operator/POP and government-intranet searches; expect no public colo. |
| Kouilou | Loango, Hinda, Matombi, Djeno | High infrastructure | WACS landing and industrial connectivity. Count only adjacent carrier/rack facilities, not the landing station itself. |
| Lekoumou | Sibiti, Zanaga, Komono | Low/medium | Mining/enterprise IT room checks; likely private non-colo. |
| Likouala | Impfondo, Betou, Liranga, Congo-Oubangui overlay | Low | Border/river connectivity and VSAT/fibre; no confirmed DC expected. |
| Niari | Dolisie, Mossendjo, Loubomo | Medium | Backbone corridor POP checks, especially Congo Telecom/Mambs/Silicone Connect. |
| Plateaux | Djambala, Gamboma, Imboulou, Nkeni-Alima overlay | Low/medium | Power/fibre corridor and new-department label search. Avoid power-only false positives. |
| Pointe-Noire / Black Point | Pointe-Noire, Black Point, Loandjili, Tie-Tie/Tié-Tié, Mvoumvou, Port autonome, Ngoyo, Lumumba | Very high | ARPCE DC, CGIX-PN, Congo Telecom PNR1, SOFIA, WACS/2Africa adjacency, port/enterprise connectivity. |
| Pool | Kinkala, Mindouli, Mayama, Djoue/Djoué, Kintélé, Djoue-Lefini/Odziba overlay | Medium | Hinterland fibre and hydro corridor; low colo probability outside Brazzaville spillover. |
| Sangha | Ouesso/Ouésso, Pokola, Kabo, Ngombe/Ngombé, Sembé | Medium | CAB/Cameroon/CAR corridor and logging-town operator rooms. Require facility wording. |

## 6. Verification and Dedupe Rules

1. **Operator page beats directory.** If ST Digital/Congo Telecom/ARPCE confirms a facility, grade only the confirmed facts A; keep directory-only capacity/address as C until matched.
2. **IXP host is facility evidence only when host is named.** CGIX-PN host is ARPCE Pointe-Noire DC. CGIX-BZV host remains unresolved unless ARPCE/PeeringDB names it.
3. **Landing station is connectivity, not colocation.** WACS Matombi and 2Africa Pointe-Noire are strong network-adjacency leads but should not be counted as datacenters by themselves.
4. **Separate the three Brazzaville leads.** ST Digital Brazzaville, AfDB Bacongo national DC, and ARPCE 2021 Brazzaville DC may be distinct. Merge only on exact address/operator/project evidence.
5. **Do not upgrade Oyo from tender to build without new evidence.** Search Oyo/Cuvette/CGIX/third exchange, but record as planned until award or physical construction appears.
6. **Tier language needs certification proof.** `Tier III compliant`, `Tier 3 standards`, and `Tier 3+` are not Uptime certification unless the Uptime awards list names the exact site.
7. **Keep status dates explicit.** Example: ARPCE Pointe-Noire commissioned 28 Feb 2024; CGIX-PN launched 20 Sep 2024; Bacongo national DC last reliable public status found was near-completion/target May 2026, not proven operational in this review.
