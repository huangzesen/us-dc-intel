# BI Explorer Industry - Burundi Press, Vendor, Interconnection, And Aggregator Discovery

Date verified: 2026-08-12. Scope: Burundi datacenter enumeration from local press, African/international trade press, operator/vendor pages, interconnection records, hosting directories, job posts, and province-level search patterns. Pair this file with `explorer-official.md`; official sources decide final facility status where conflicts exist.

Administrative correction: Burundi is **not** a 17-province country in 2026. Use the current **5-province** model for normalized records and the former **18-province** model for search recall. The former provinces are Bubanza, Bujumbura Mairie, Bujumbura Rural, Bururi, Cankuzo, Cibitoke, Gitega, Karuzi, Kayanza, Kirundo, Makamba, Muramvya, Muyinga, Mwaro, Ngozi, Rumonge, Rutana, and Ruyigi. Rumonge was created in 2015; omitting it while calling the set "17 provinces" is a data-quality error.

Reliability grades:
- **A** = primary/operator/official/donor: operator service pages or tenders, ARCT, SETIC, PAFEN, Primature/PDDSP, finance ministry, World Bank, official cloud-region lists.
- **B** = strong secondary: Iwacu, Burundi Eco, ABP, Le Renouveau, Agence Ecofin, WeAreTech Africa, CIO Mag, TechAfricaNews, Internet Society/African Union IXP releases, PeeringDB for IXP metadata.
- **C** = lead only: colo.exchange, datacenters.com, Baxtel, Inflect, Colomap, DataCenterMap, LinkedIn/social posts, unsourced blogs, old MoUs, vendor marketing without a named site.

---

## 0. Burundi Industry Frame

- Burundi has no hyperscale/large-colo market visible in public sources. The realistic discovery universe is: telecom cores and cloud-service nodes; SETIC/government hosting; PAFEN/CIU/BERNET project infrastructure; BBS hosting/backbone PoPs; BDIXP; CNI/NIC.BI registry infrastructure; small Bujumbura hosters.
- Bujumbura is the primary commercial cluster. Gitega is important for government and education-sector leads. Other locations are normally backbone PoPs, mobile-network sites, university labs, or negative searches.
- Treat marketing terms carefully. `Cloud server`, `hebergement serveur`, `data centre engineer`, or `colocation Bujumbura` are leads until a source identifies local infrastructure and location.
- Power is a major screen. REGIDESO/grid reliability and electricity-access constraints mean every serious facility claim should be cross-checked against power, generator, substation, or official project evidence where possible.
- French gives the highest recall: `centre de donnees`, `hebergement`, `serveurs`, `salle serveur`, `cloud`, `colocation`, `fibre optique`, `point de presence`, `appel d'offres`, `mise en service`, `inauguration`.

---

## 1. Local Press

| Source | URL / route | Use | Grade |
|---|---|---|---|
| Iwacu | https://www.iwacu-burundi.org/ | Highest-value independent source. Verified SETIC data-center/government-hosting article in 2021: https://www.iwacu-burundi.org/tic-les-institutions-etatiques-pas-tres-rassurees-par-le-setic/ | B; A only when linking/reproducing official document |
| Burundi Eco | https://burundi-eco.com/ | Economy/telecom/energy reporting, ONATEL and PAFEN context. | B |
| ABP / ABP Info | https://abp.bi/ and https://en.abpinfo.bi/ | State news agency; official launches. PAFEN launch coverage confirms World Bank USD 92M and 6-year project horizon: https://en.abpinfo.bi/official-launch-of-the-project-to-support-the-foundations-of-the-digital-economy-in-burundi/ | B |
| Le Renouveau | https://lerenouveau.bi/ | State-adjacent source for government digital projects and public-service systems. | B/C |
| SOS Medias Burundi | https://www.sosmediasburundi.org/ | Useful for procurement/public-sector risk, less likely for facility detail. | B/C |
| Itara Burundi | https://itaraburundi.com/ | Tech/economy leads including connectivity and Starlink. | C/B |
| Burundi AG News | https://burundi-agnews.org/ | Useful historical fibre/BBS/telecom leads; corroborate elsewhere. | C/B |
| RPA | https://rpa.bi/ | Local/provincial quick checks. | C/B |

Queries:
```text
site:iwacu-burundi.org Burundi "data center" OR "centre de donnees" OR SETIC OR hebergement
site:burundi-eco.com ONATEL OR PAFEN OR "fibre optique" OR numerique
site:abp.bi PAFEN OR "centre de donnees" OR numerique OR "mise en service"
site:en.abpinfo.bi Burundi PAFEN OR digital OR "data center"
site:lerenouveau.bi PAFEN OR e-gouvernement OR "centre de donnees"
site:sosmediasburundi.org REGIDESO OR fibre OR numerique OR "data center"
```

Lifecycle verbs to capture:
- `projet`, `etude`, `strategie`, `MoU`: intent or planning only.
- `appel d'offres`, `AMI`, `DAO`, `marche attribue`: procurement/pipeline.
- `construction`, `travaux`, `installation`: under construction/deployment.
- `mise en service`, `operationnel`, `inaugure`, `lance`: operational, but still verify with primary source where possible.

---

## 2. African And International Trade Press

| Source | URL / route | Use | Grade |
|---|---|---|---|
| Agence Ecofin | https://www.agenceecofin.com/ | Telecom and infrastructure finance. Verified BBS USD 11.5M fibre loan article: https://www.agenceecofin.com/equipement/2705-11223-burundi-backbone-system-recoit-un-pret-de-11-5-millions-pour-un-reseau-national-de-fibre-optique | B |
| WeAreTech Africa | https://www.wearetech.africa/ | Digital-economy policy and PAFEN/SNGD updates. PAFEN mid-term review coverage: https://www.wearetech.africa/en/fils-uk/news/tech/world-bank-reviews-burundi-s-pafen-reform-program | B |
| CIO Mag | https://cio-mag.com/ | ARCT internet/telecom statistics, Starlink/market reporting. | B |
| TechAfricaNews | https://techafricanews.com/ | PAFEN/Lumitel broadband rollout; useful for operator-project leads. | B/C |
| Digital Business Africa | https://www.digitalbusiness.africa/ | PAFEN progress and regional data-centre context; corroborate primary documents. | B/C |
| Data Center Dynamics | https://www.datacenterdynamics.com/en/regions/africa/ | Watch for any first confirmed Burundi commercial DC; currently low recall. | B for sourced articles |
| IT News Africa | https://www.itnewsafrica.com/ | Pan-African ICT lead generation. | B/C |
| Africa Data Centres Association | https://africadca.org/ | Regional market context; no Burundi facility membership expected. | B for reports, C for unsourced facility claims |

Queries:
```text
site:agenceecofin.com Burundi BBS OR fibre OR telecom OR numerique
site:wearetech.africa Burundi PAFEN OR "data center" OR "data centre" OR gouvernance
site:cio-mag.com Burundi ARCT OR Starlink OR internet
site:techafricanews.com Burundi PAFEN OR Lumitel OR "data center"
site:datacenterdynamics.com Burundi OR Bujumbura
```

---

## 3. Operators, Hosters, And Vendors

| Entity | Primary or lead URL | Industry signal | Grade and handling |
|---|---|---|---|
| BBS | https://www.bbs.bi/ ; hosting page https://www.bbs.bi/fr/sb25/ | Official site lists `Hebergement Web`, `Hebergement Serveur`, and pricing. | A for marketed server/web hosting; require site/facility details before rack/MW/address claims. |
| Lumitel / Viettel Burundi | https://lumitel.bi/ ; cloud-server tab https://lumitel.bi/package-vas?tab=Cloud+server | Official page exposes cloud-server service surface and Bujumbura address. PAFEN rollout covered by trade press. | A for service; physical facility remains unproven until operator/tender evidence names it. |
| ONATEL | https://onatel.bi/ | State incumbent; ARCT confirms operator status. | A for operator, B/C for data-centre facility unless hosting/cloud/core evidence is named. |
| Econet Leo | ARCT + Econet group release: https://www.econetafrica.com/press-release/econet-wireless-group-announces-the-end-of-the-merger-econet-leo ; domain lead `econet.bi` | ARCT confirms operator; LinkedIn posts mention Data Centre Engineer roles in 2026. | C lead for data-centre staffing unless captured on official career page/tender; do not count as facility alone. |
| CNI / NIC.BI | https://www.cni.bi/ and https://nic.bi/ | .bi registry and legacy computing/hosting lead. | B/C until a primary page names server/hosting infrastructure and location. |
| Buja Online and small hosters | datacenters.com and web-hosting searches | Possible Bujumbura VPS/hosting. | C unless own site proves local infrastructure. Many small providers resell abroad. |
| Huawei/ZTE/Ericsson | vendor pages and operator tenders | Network, fibre, 4G/core equipment leads. | B/C; vendor case studies can corroborate telecom infrastructure but rarely facility status. |

Operator queries:
```text
site:bbs.bi hebergement OR serveur OR colocation OR "data center"
site:lumitel.bi cloud OR "Cloud server" OR entreprise OR hebergement
site:onatel.bi cloud OR hebergement OR "data center" OR "appel d'offres"
site:econet.bi "data centre" OR "data center" OR cloud OR "appel d'offres"
site:cni.bi hebergement OR serveur OR infrastructure
site:nic.bi serveur OR infrastructure OR DNS OR registry
"Econet Leo" Burundi "Data Centre Engineer"
"Viettel Burundi" cloud OR "data center" OR Bujumbura
"Huawei" Burundi ONATEL OR BBS OR fibre OR "data center"
```

---

## 4. Interconnection, IXP, And Aggregators

| Channel | URL | Use | Grade |
|---|---|---|---|
| BurundiX / BDIXP launch | https://www.internetsociety.org/news/press-releases/2014/internet-exchange-point-launched-on-21-march-2014-in-bujumbura-burundi/ | Confirms IXP launch in Bujumbura on 21 March 2014. | B/A for launch fact; not DC capacity. |
| African Union launch notice | https://au.int/en/newsevents/20140317/launching-internet-exchange-point-burundi | Official regional corroboration of launch. | B |
| BDIXP current site | https://bdixp.org.bi/en/home/ | Current IXP organization/site lead. | B for IXP presence. |
| PeeringDB | https://www.peeringdb.com/ix/2552 | Metadata: Burundi Internet Exchange Point, Bujumbura, 26G listed total capacity in captured page. | B/C; use for IXP metadata, not facility count. |
| colo.exchange | https://colo.exchange/locations/bi/bujumbura-mairie/bujumbura | Bujumbura/BBS colocation lead. | C; now corroborate BBS hosting via BBS official pages. |
| datacenters.com | https://www.datacenters.com/providers/buja-online | Buja Online lead. | C until operator page confirms local facility. |
| Baxtel / Inflect / Colomap / DataCenterMap | Search Bujumbura/Burundi pages | Lead discovery only. | C |

IXP/aggregator queries:
```text
"BDIXP" OR "Burundi Internet Exchange" Bujumbura members facilities
"BurundiX" IXP Bujumbura
site:peeringdb.com Burundi Bujumbura
site:colo.exchange Burundi Bujumbura colocation
site:datacenters.com Burundi Bujumbura hosting
"Buja Online" Burundi data center OR VPS OR hosting
```

---

## 5. Search Templates

### 5.1 French discovery templates

```text
"Burundi" "centre de donnees" OR "data center" OR datacenter OR "centre informatique"
"Burundi" "hebergement serveur" OR "hebergement web" OR colocation OR cloud
"Bujumbura" ("centre de donnees" OR "data center" OR hebergement OR colocation OR "cloud server")
"Gitega" ("centre de donnees" OR "data center" OR PAFEN OR CIU OR BERNET OR CDIN)
"Burundi" "centre de donnees national" OR "Centre de Donnees Integre National"
"Burundi" "appel d'offres" "hebergement des donnees" OR "serveurs"
filetype:pdf Burundi "hebergement des donnees" OR "centre de donnees" OR "data center"
```

### 5.2 English discovery templates

```text
"Burundi" ("data centre" OR "data center" OR datacentre OR colocation) (Bujumbura OR Gitega)
"Burundi" ("national data centre" OR "sovereign cloud" OR "data hosting")
"Burundi" (PAFEN OR "World Bank" OR BERNET OR CDIN) "data"
"Burundi" (BBS OR ONATEL OR Lumitel OR "Econet Leo") ("cloud" OR "server hosting" OR "data centre")
```

### 5.3 Kirundi/local low-yield checks

Use only as a recall aid for provincial government posts; verify all positive results with French/official sources.

```text
Burundi data serveurs ikigo itumanaho
"Bujumbura" OR "Gitega" data serveurs itumanaho
```

---

## 6. Province Enumeration

Normalize to current 5 provinces, but search all legacy names.

| Current province | High-yield legacy names | Seeds |
|---|---|---|
| Bujumbura | Bujumbura Mairie, Bujumbura Rural, Bubanza, Cibitoke, parts of Rumonge and Muramvya | SETIC, BBS hosting, BDIXP, ONATEL, Lumitel, Econet, CNI/NIC.BI, banks, small hosters. |
| Gitega | Gitega, Karuzi, Mwaro, parts of Muramvya | Political capital, CIU at Universite Polytechnique de Gitega, PAFEN/BERNET, possible CDIN lead. |
| Butanyerera | Ngozi, Kayanza, Kirundo, parts of Muramvya | BBS and mobile regional network leads; mostly PoPs/edge rooms. |
| Buhumuza | Cankuzo, Muyinga, Ruyigi | Broadband rollout and backbone/mobile leads; negative commercial search expected. |
| Burunga | Bururi, Makamba, Rutana, parts of Rumonge | Border/backbone/power/donor leads; negative commercial search expected. |

Current-province query block:
```text
Bujumbura Burundi (BBS OR SETIC OR ONATEL OR Lumitel OR Econet OR CNI OR BDIXP) ("data center" OR hebergement OR colocation OR cloud)
Gitega Burundi (PAFEN OR CIU OR BERNET OR CDIN OR "centre de donnees")
Butanyerera OR Ngozi OR Kayanza OR Kirundo Burundi (BBS OR fibre OR "point de presence" OR "data center")
Buhumuza OR Cankuzo OR Muyinga OR Ruyigi Burundi (fibre OR telecom OR "centre de donnees")
Burunga OR Bururi OR Makamba OR Rutana OR Rumonge Burundi (fibre OR telecom OR "centre de donnees")
```

Legacy exhaustive query block:
```text
Bubanza Burundi "data center" OR "centre de donnees" OR datacenter OR colocation OR fibre
"Bujumbura Mairie" Burundi (BBS OR ONATEL OR Lumitel OR SETIC OR CNI OR BDIXP) "data center" OR colocation OR cloud OR hebergement
"Bujumbura Rural" Burundi "data center" OR "centre de donnees" OR fibre
Bururi Burundi "data center" OR "centre de donnees" OR fibre
Cankuzo Burundi "data center" OR "centre de donnees" OR fibre
Cibitoke Burundi "data center" OR "centre de donnees" OR fibre
Gitega Burundi ("data center" OR "centre de donnees" OR BERNET OR PAFEN OR CIU OR CDIN)
Karuzi Burundi "data center" OR "centre de donnees" OR fibre
Kayanza Burundi "data center" OR "centre de donnees" OR fibre
Kirundo Burundi "data center" OR "centre de donnees" OR fibre
Makamba Burundi "data center" OR "centre de donnees" OR fibre
Muramvya Burundi "data center" OR "centre de donnees" OR fibre
Muyinga Burundi "data center" OR "centre de donnees" OR fibre
Mwaro Burundi "data center" OR "centre de donnees" OR fibre
Ngozi Burundi (Econet OR ONATEL OR Lumitel OR BBS) "data center" OR fibre
Rumonge Burundi "data center" OR "centre de donnees" OR fibre
Rutana Burundi "data center" OR "centre de donnees" OR fibre
Ruyigi Burundi "data center" OR "centre de donnees" OR fibre
```

Negative-search rule: do not count ICT offices, cybercafes, computer labs, NGO server rooms, generic data-collection projects, GIS rooms, or software platforms unless a source describes hosting/colo/compute infrastructure with a named operator and location.

---

## 7. Grading And Verification Rules

- **A operating facility**: official/operator/donor source names a site or facility with location and infrastructure function.
- **B operating facility**: strong press names a site/location and gives enough detail to distinguish a facility, preferably quoting an official.
- **C lead**: aggregator listing, social/job post, reseller page, unsourced vendor claim, or service page with no local physical evidence.
- **Provider-level service**: official hosting/cloud/server offer without a named facility. Examples: BBS hosting/server hosting, Lumitel cloud-server surface.
- **Planned/pipeline**: PDDSP/CDIN/PAFEN study, AMI, or tender without award or site commissioning.
- **Interconnection**: BDIXP/IXP records prove traffic-exchange infrastructure, not datacenter capacity.
- **Telco core**: ONATEL/Lumitel/Econet sites count only if the source describes core/network/server/hosting infrastructure, not merely mobile coverage.
- **Capacity**: leave null unless kW/MW/racks/floor area are stated by official/operator/tender source.
- **Power**: cross-check large claimed facilities with REGIDESO, AREEN, OBPE, World Bank power-project context, or generator/substation procurement.
- **Cloud**: AWS/Azure/GCP/OCI official region pages are negative evidence for Burundi; do not infer local hyperscaler facilities.
- **De-dup**: keep one canonical physical record for overlapping SETIC/eNama/PAFEN/CDIN evidence only when sources prove the same site; otherwise keep separate project records.

---

## 8. Verified Source Anchors

- ARCT: https://arct.gov.bi/
- ARCT equipment authorization portal announcement: https://arct.gov.bi/2025/10/24/lancement-de-la-plateforme-numerique-de-gestion-des-autorisations-des-materiels-de-communications-electroniques/
- ARCT Q2 2025 market observatory: https://arct.gov.bi/2025/12/29/observatoire-du-marche-des-services-de-communications-voix-sms-internet-et-services-financiers-mobiles-au-burundi-deuxieme-trimestre-2025/
- SETIC: https://setic.gov.bi/
- SETIC PAFEN mid-term page: https://setic.gov.bi/evaluation-a-mi-parcours-du-projet-pafen-2023-2028/
- SETIC/PAFEN data-hosting study AMI: https://setic.gov.bi/wp-content/uploads/2024/03/AMI_hebergement-des-donnees_0001.pdf
- PAFEN: https://pafen.gov.bi/
- PAFEN tenders: https://pafen.gov.bi/appels-doffres/
- Finance ministry PAFEN mid-term review: https://finances.gov.bi/index.php/2026/03/23/pafen-une-evaluation-a-mi-parcours-pour-accelerer-la-transformation-numerique/
- Primature PDDSP page: https://primature.gov.bi/plan-directeur-de-digitalisation-des-services-publics-du-burundi-pddsp-2023-2033/
- BBS official site: https://www.bbs.bi/
- BBS hosting page: https://www.bbs.bi/fr/sb25/
- Lumitel: https://lumitel.bi/
- ONATEL: https://onatel.bi/
- BDIXP: https://bdixp.org.bi/en/home/
- Internet Society IXP launch: https://www.internetsociety.org/news/press-releases/2014/internet-exchange-point-launched-on-21-march-2014-in-bujumbura-burundi/
- PeeringDB BDIXP: https://www.peeringdb.com/ix/2552
- REGIDESO: https://regideso.bi/
- AREEN: https://www.areen.bi/
- AWS regions: https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- Azure regions: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud locations: https://cloud.google.com/about/locations
- OCI regions: https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm

Final note: aggregator results are useful in Burundi because primary reporting is sparse, but they should only open an investigation. The final record should be grounded in ARCT, SETIC/PAFEN/PDDSP, operator pages, donor documents, or strong local/regional press.
