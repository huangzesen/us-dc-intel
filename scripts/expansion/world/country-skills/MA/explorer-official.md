# MA Explorer Official - Morocco Datacenter Enumeration

Date: 2026-08-12. Country: **MA Morocco**. Division model: **12 regions** under the 2015 territorial reform / ISO 3166-2:MA. Scope: official, regulatory, public-procurement, utility, investment, hyperscaler, certification, and operator-primary routes for discovering operational, planned, under-construction, public-sector, and connectivity-adjacent data-center assets.

Reliability grades used in this file:

- **A** = primary evidence for the exact fact claimed: official regulator/ministry/CRI/procurement/utility page, operator facility page, Oracle/OCI region page, Uptime Institute award page, official company press release, official zone-authority page.
- **B** = strong secondary evidence: Data Center Dynamics, Reuters-carried coverage, Agence Ecofin, Medias24, Le360, TelQuel, LesEco, L'Economiste, Le Matin, La Vie Eco, Moroccan World News, Le Desk, MAP reposts, reputable vendor/integrator article.
- **C** = lead only: directories, marketplaces, generic market reports, social posts, snippets, inaccessible reports, unsourced capacity claims.

Do not upgrade a source grade because a claim is plausible. Upgrade only when the cited page itself supports the facility, status, location, or capacity.

---

## 0. Morocco Operating Facts

Morocco has no public national data-center register and no open national planning-permit search engine. Enumeration requires joining these official surfaces:

1. Telecom/legal context: ANRT.
2. National digital policy: Ministry of Digital Transition and ADD.
3. Investment/permit route: CRI-Invest plus the relevant regional CRI / CRUI.
4. Energy/grid route: ONEE, ANRE, MASEN, municipal distributors, self-production law.
5. Data-protection route: CNDP.
6. Procurement route: Portail National des Marches Publics.
7. Primary facility evidence: operator pages, Oracle/OCI pages, Uptime Institute awards.
8. Secondary discovery: industry and regional press, held at B unless official documents are found.

Administrative coverage must include all **12 regions**:

| ISO | Region | CRI-Invest route |
|---|---|---|
| MA-01 | Tanger-Tetouan-Al Hoceima | https://www.cri-invest.ma/map/my-cri/5 ; CRI portal https://investangier.com/ |
| MA-02 | L'Oriental | https://www.cri-invest.ma/map/my-cri/12 ; CRI portal https://orientalinvest.ma/ |
| MA-03 | Fes-Meknes | https://www.cri-invest.ma/map/my-cri/6 ; CRI portal https://fesmeknesinvest.ma/ |
| MA-04 | Rabat-Sale-Kenitra | https://www.cri-invest.ma/map/my-cri/1 ; CRI portal https://www.rabatinvest.ma/ |
| MA-05 | Beni Mellal-Khenifra | https://www.cri-invest.ma/map/my-cri/7 |
| MA-06 | Casablanca-Settat | https://www.casainvest.ma/ ; find CRI-Invest map route from the national map if needed |
| MA-07 | Marrakech-Safi | https://www.cri-invest.ma/map/my-cri/10 ; CRI portal https://www.marrakechinvest.ma/ |
| MA-08 | Draa-Tafilalet | use https://www.cri-invest.ma/ map and regional CRI search |
| MA-09 | Souss-Massa | https://www.cri-invest.ma/map/my-cri/3 ; CRI portal https://agadirinvest.com/ |
| MA-10 | Guelmim-Oued Noun | https://www.cri-invest.ma/map/my-cri/8 |
| MA-11 | Laayoune-Sakia El Hamra | https://www.cri-invest.ma/map/my-cri/9 |
| MA-12 | Dakhla-Oued Ed-Dahab | use https://www.cri-invest.ma/ map and regional CRI search |

Official administrative anchors:

- Direction Generale des Collectivites Territoriales states Morocco has 12 regions, 75 prefectures/provinces, and 1503 communes: https://www.collectivites-territoriales.gov.ma/fr/presentation (A).
- Decree No. 2-15-40 fixing the 12 regions is hosted by DGCT: https://www.collectivites-territoriales.gov.ma/fr/node/2677 and PDF https://www.collectivites-territoriales.gov.ma/sites/default/files/2021-05/d%C3%A9cret%20fixant%20le%20nombre%20des%20r%C3%A9gions.pdf (A).
- ISO OBP lists Morocco subdivisions as 12 regions, 13 prefectures, and 62 provinces: https://www.iso.org/obp/ui/#iso:code:3166:MA (A for ISO coding).

Language and vocabulary:

```text
French: centre de donnees, datacenter, data center, data centre, centre de calcul,
cloud souverain, cloud national, cloud de l'Etat, hebergement, hebergement de donnees,
colocation, housing, salle serveur, salle informatique, calcul haute performance,
supercalculateur, permis de construire, autorisation d'urbanisme, CRUI, CRI,
raccordement electrique, poste electrique, autoconsommation, cable sous-marin,
station d'atterrissement.

Arabic: مركز البيانات, مركز المعطيات, مركز الحوسبة, الاستضافة, السحابة السيادية,
رخصة البناء, الاستثمار, الاتصالات, المكتب الوطني للكهرباء.
```

Capacity discipline: record MW/MVA/kVA/racks/square metres only when the source ties the number to a named data-center site. Renewable plant MW, cable bandwidth, or national grid projects are context, not data-center IT load.

---

## 1. Official / Primary Source Routes

### 1.1 ANRT - telecom regulator

Primary route: https://www.anrt.ma/ and English entry https://www.anrt.ma/en (A when reachable). ANRT is useful for telecom operator status, market indicators, licensing, interconnection, spectrum, 5G, and fiber decisions. It does not license data centers as a separate facility class.

Use ANRT evidence as A for telecom/legal status, not automatic data-center evidence.

```text
site:anrt.ma "data center"
site:anrt.ma "datacenter"
site:anrt.ma "centre de donnees"
site:anrt.ma "hebergement"
site:anrt.ma "cloud"
site:anrt.ma "Maroc Telecom" licence
site:anrt.ma "Orange Maroc" licence
site:anrt.ma "Inwi" licence
site:anrt.ma "5G" decision
site:anrt.ma "fibre" decision
site:anrt.ma "indicateurs" "2026"
```

Extract: operator legal names, licence/authorization class, decision dates, wholesale/fiber obligations, 5G status, and demand context.

### 1.2 Ministry of Digital Transition / ADD / Maroc Digital 2030

Primary routes:

- Ministry: https://www.mmsp.gov.ma/fr (A).
- Digital Morocco 2030 official page: https://www.mmsp.gov.ma/fr/actualites/cliquez-ici-pour-d%C3%A9couvrir-la-strat%C3%A9gie-digital-morocco-2030 (A for strategy existence).
- Morocco government strategy page: https://maroc.ma/en/strategies-and-public-policies/digital-morocco-2030 (A).
- ADD: https://www.add.gov.ma/ (A when reachable); open-data portal route https://www.data.gov.ma/ (A).

Use these for policy and public-cloud demand. They are not facility evidence unless a page names a data-center project, locality, contracting party, or award.

```text
site:mmsp.gov.ma "data center"
site:mmsp.gov.ma "centre de donnees"
site:mmsp.gov.ma "cloud souverain"
site:add.gov.ma "data center"
site:add.gov.ma "cloud"
site:data.gov.ma "centre de donnees"
"Maroc Digital 2030" "data center"
"Maroc IA 2030" "cloud" "data center"
"Ministere de la Transition Numerique" "Vertiv" "50 MW"
```

### 1.3 CRI / CRUI investment and permit route

Primary national portal: https://www.cri-invest.ma/ (A for the national investment e-portal). Fes-Meknes describes CRI-Invest as a 100% online project-investment path for project launch, progress tracking, information, procedures, incentives, acts, and administrative authorizations: https://fesmeknesinvest.ma/cri-invest/ (A for platform purpose).

Method:

- For investment-scale DCs, search CRI and CRUI news/communiques, annual reports, board minutes, and PDF newsletters.
- For ordinary building permits, search the commune, prefecture/province, urban agency, or CRUI route. There is no reliable national open permit database.
- For free-zone projects, search the zone operator as a separate A-grade source: Tanger Med Zones, Atlantic Free Zone Kenitra, Midparc, CasaNearshore, Technopark, Haliopolis/Haliopark.

```text
site:cri-invest.ma "data center"
site:cri-invest.ma "centre de donnees"
site:cri-invest.ma "cloud"
site:{regional_cri_domain} "data center"
site:{regional_cri_domain} "centre de donnees"
site:{regional_cri_domain} "cloud"
"CRUI" "{region}" "data center"
"commission regionale unifiee d'investissement" "{region}" "data center"
"permis de construire" "data center" "{commune}"
"autorisation" "data center" "{province}"
```

### 1.4 AMDIE and investment incentives

Primary route: https://www.amdie.gov.ma/ (A). Use AMDIE for strategic investment announcements, investment charter context, and foreign-investor project promotion. Treat announcement capacity/status as A only if AMDIE itself states it; otherwise keep press-derived details at B.

```text
site:amdie.gov.ma "data center"
site:amdie.gov.ma "datacenter"
site:amdie.gov.ma "intelligence artificielle"
site:amdie.gov.ma "cloud"
"AMDIE" "data center" "Maroc"
"charte de l'investissement" "data center" "Maroc"
```

### 1.5 Energy, grid, and self-production

Primary routes:

- ONEE electricity branch: https://www.one.org.ma/ (A for grid/project/procurement context).
- ONEE distribution context: https://www.one.ma/fr/pages/interne.asp?esp=2&id1=5&id2=56&t2=1 (A for distribution scope when reachable).
- ANRE laws page: https://anre.ma/en/regulations/lois/ (A). ANRE lists Law No. 48-15 on electricity-sector regulation and creation of ANRE.
- Law 82-21 self-production PDF hosted by ANRE: https://anre.ma/wp-content/uploads/2023/08/Loi-82-21-BO_7400_Fr.pdf (A).
- MASEN: https://www.masen.ma/en and https://www.masen.ma/en/presentation (A for renewable-energy project context).

Use these for power feasibility, grid access, tariffs, self-production, renewable procurement, and high-voltage substations. Do not convert renewable MW into DC IT load.

```text
site:one.org.ma "data center"
site:one.org.ma "centre de donnees"
site:one.org.ma "poste" "Nouaceur"
site:one.org.ma "poste" "Settat"
site:anre.ma "autoproduction"
site:anre.ma "raccordement"
site:masen.ma "data center"
"ONEE" "data center" "raccordement"
"autoconsommation" "data center" "Maroc"
"TAQA" "data center" "Maroc"
```

### 1.6 CNDP - data protection

Primary route: https://www.cndp.ma/ (A for Moroccan personal-data regulatory material under Law 09-08). CNDP can reveal processors, hosting/security requirements, sanctions, or data-transfer context, but is usually C as facility evidence unless it names the facility/operator directly.

```text
site:cndp.ma "hebergement"
site:cndp.ma "cloud"
site:cndp.ma "data center"
site:cndp.ma "centre de donnees"
"CNDP" "{operator}" "hebergement"
```

### 1.7 Public procurement

Primary route: https://www.marchespublics.gov.ma/ (A for tenders/awards). Search buyer names as well as generic terms. A tender proves procurement, not facility commissioning.

```text
site:marchespublics.gov.ma "data center"
site:marchespublics.gov.ma "centre de donnees"
site:marchespublics.gov.ma "cloud"
site:marchespublics.gov.ma "hebergement"
site:marchespublics.gov.ma "salle informatique"
"appel d'offres" "data center" "Maroc"
"attribution" "centre de donnees" "Maroc"
```

### 1.8 Hyperscaler official pages

- Oracle OCI Morocco West / Casablanca is live: https://docs.oracle.com/iaas/releasenotes/oci/new-region-casablanca-1.htm. The page states release date 2026-02-20, region identifier `af-casablanca-1`, region key `LEJ`, and one availability domain (A).
- Oracle Morocco announcement: https://www.oracle.com/africa-fr/news/announcement/oracle-first-hyperscaler-open-public-cloud-2026-04-07/ states the public cloud region is in Casablanca and identifies N+ONE Datacenters as hosting partner (A for Oracle/N+ONE claim). Oracle's 2024 announcement of two planned Morocco regions was carried at https://www.prnewswire.com/news-releases/oracle-plans-to-open-two-public-cloud-regions-in-morocco-302158936.html (A/official-distribution for plan at time of publication).
- Oracle Agadir R&D hub: https://www.oracle.com/sa/news/announcement/oracle-establishes-second-morocco-rd-hub-to-power-the-future-of-ai-2026-06-30/ (A for R&D hub, not a DC).
- AWS official global infrastructure: https://aws.amazon.com/about-aws/global-infrastructure/ and regions page https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ (A for AWS region list; as checked in research, no Morocco public Region). AWS Wavelength with Orange was announced at https://aws.amazon.com/blogs/industries/aws-announces-new-wavelength-zones-in-morocco-and-senegal/ (A for Wavelength plan, not a full AWS Region).
- Azure official global infrastructure: https://azure.microsoft.com/en-us/explore/global-infrastructure and geographies route https://azure.microsoft.com/en-au/explore/global-infrastructure/geographies (A for Azure region/geography list; no Morocco public region found in research).
- Google Cloud locations: https://cloud.google.com/about/locations (A for Google Cloud location list; no Morocco cloud region found in research).

### 1.9 Operator / certification primary pages

| Operator / asset | Primary URL | Grade use |
|---|---|---|
| Uptime Institute Morocco awards | https://uptimeinstitute.com/uptime-institute-awards/country/id/MA | A for listed client, project name, location, and award type. Includes N+ONE Settat/Nouaceur, OCP Benguerir DC2, Orange Nouaceur, Wana/inwi Rabat-Sale, and other certified facilities. |
| N+ONE client story | https://uptimeinstitute.com/clients/nplusone | A for Uptime-listed N+ONE certified sites; A/B for general market statements by Uptime. |
| inwi Business Datacenter | https://inwi.ma/en/entreprise/datacenter | A for inwi's self-claimed datacenter service. Pair with Uptime and press for site names/specs. |
| Maroc DataCenter / MDC | https://www.mdc.ma/datacenter/ | A for MDC Temara site, Tier III-designed claim, 2000 m2, ownership/operator statements. |
| Orange Maroc press dossier | https://corporate.orange.ma/content/download/186730/3000921/version/1/file/DP_Orange_Conference_Novembre_VF.pdf | A for Orange Tech Nouaceur/Casablanca, 2025-11-19 inauguration, 1.5 MW initial capacity, 15000 m2, Uptime certification claim, 700 kWc solar. |
| Atlas Cloud Services | https://atlascloudservices.com/en/our-data-center/ | A for ACS Benguerir self-claimed data center and Uptime Tier III/Tier IV statements. |
| HostoWeb | https://www.hostoweb.com/en/ and https://www.hostoweb.com/en/about-us/contact | A for hosting/cloud services and office locations; C for exact DC locations unless corroborated. |
| Maroc Telecom/IAM | https://www.iam.ma/ | A for IAM pages if found; 2018 Casablanca DC details currently better supported by TelQuel and Minkels at B. |
| Public industry ministry Imtiaz page | https://www.mcinet.gov.ma/en/content/maroc-datacenter-1st-cloud-computing-platform-francophone-africa | A for public-program description of Maroc Datacenter as a 100% Moroccan Tier III-designed data centre project. |

---

## 2. Per-Region Official Enumeration Strategy

For every region, run the CRI/CRUI route first, then communes/urban agencies, then zone authorities, then utility/procurement, then operator/certification pages. Mark a region `no confirmed DC found` only after these surfaces are checked.

### 2.1 Tanger-Tetouan-Al Hoceima

Official routes: CRI-Invest https://www.cri-invest.ma/map/my-cri/5 and CRI TTA https://investangier.com/. Check Tanger Med Zones/TMSA, Tetouan commune/province, Tangier urban agency, Amendis/ONEE grid, and Tanger Med fiber/port announcements.

Known leads:

- Iozera / Eureka Park Tetouan 386 MW AI DC: company PR via PRNewswire and DCD are B/A-company-distribution for announcement, but no Moroccan official permit page found in this review. Status: planned/announced. Keep at B until CRI/CRUI or construction proof appears.
- Tanger/Tetouan connectivity and industrial zones are context unless a named facility appears.

```text
site:investangier.com "data center"
site:investangier.com "centre de donnees"
site:tmsa.ma "data center"
"Iozera" "Tetouan" "386MW"
"Eureka Park" "Tetouan" "data center"
"permis de construire" "datacenter" "Tetouan"
"Tanger Med" "data center"
```

### 2.2 L'Oriental

Official routes: CRI-Invest https://www.cri-invest.ma/map/my-cri/12 and CRI Oriental https://orientalinvest.ma/. Check Oujda, Nador, Nador West Med, Medusa cable landing, ONEE substations, and Oujda technopole/university.

Known leads:

- Nador Medusa cable landing is a connectivity asset, not a data center. Treat Orange/inwi landing-station pages or press as A/B for cable/CLS only.
- No confirmed colocation or hyperscale DC found in this review.

```text
site:orientalinvest.ma "data center"
site:orientalinvest.ma "centre de donnees"
"Nador" "data center"
"Nador" "station d'atterrissement"
"Medusa" "Nador" "Orange Maroc"
"Oujda" "centre de donnees"
```

### 2.3 Fes-Meknes

Official routes: CRI-Invest https://www.cri-invest.ma/map/my-cri/6 and CRI Fes-Meknes https://fesmeknesinvest.ma/. Check Fes Shore, Fes commune, Meknes commune, universities, and HostoWeb.

Known leads:

- HostoWeb has A-grade service/office evidence via https://www.hostoweb.com/en/ and contact locations in Fes/Casablanca, but exact Moroccan DC facility addresses remain C unless a network/datacenter page or third-party certificate corroborates them.
- No confirmed large colo/hyperscale site found in this review.

```text
site:fesmeknesinvest.ma "data center"
site:fesmeknesinvest.ma "centre de donnees"
"HostoWeb" "Fes" "data center"
"Fes Shore" "data center"
"Meknes" "centre de donnees"
```

### 2.4 Rabat-Sale-Kenitra

Official routes: CRI-Invest https://www.cri-invest.ma/map/my-cri/1 and CRI RSK https://www.rabatinvest.ma/. Check Rabat, Sale, Temara, Skhirate-Temara, Kenitra, Technopolis, Atlantic Free Zone, public procurement, CNDP, and state-hosting projects.

Confirmed/high-confidence assets:

- inwi / Wana Corporate, INWI Rabat Technopolis DC2, location Rabat-Sale: Uptime Institute country page and project page are A; inwi page is A for service; DCD/Le360/Medias24 are B for inauguration/specs.
- MDC / Maroc Datacenter, Temara near Rabat: https://www.mdc.ma/datacenter/ is A for owner/operator, Temara location, 2000 m2, Tier III-designed statements.
- Ministry/government 50 MW sovereign DC in Rabat with Vertiv support: press reports in July/August 2026 are B unless ministry or procurement page is found. Treat as planned/discussion, not operational.
- Ministry of Economy and Finance DC leads appear in Uptime lists/directories; verify from Uptime/certifier or procurement before inventorying.

```text
site:rabatinvest.ma "data center"
site:rabatinvest.ma "centre de donnees"
site:marchespublics.gov.ma "data center" "Rabat"
"INWI Rabat Technopolis DC2"
"MDC" "Temara" "datacenter"
"Maroc Datacenter" "Temara"
"Vertiv" "Rabat" "50 MW" "data center"
"Ministere de l'Economie et des Finances" "data center" "Rabat"
```

### 2.5 Beni Mellal-Khenifra

Official route: CRI-Invest https://www.cri-invest.ma/map/my-cri/7. Check Beni Mellal, Khouribga, OCP mining operations, universities, ONEE grid, and regional procurement.

Known leads:

- OCP internal IT/HPC references near Khouribga are C unless OCP/procurement/certification names a facility.
- No confirmed commercial data center found in this review.

```text
site:cri-invest.ma/map/my-cri/7 "data center"
"Beni Mellal" "data center"
"Khouribga" "data center" "OCP"
"Beni Mellal-Khenifra" "centre de donnees"
```

### 2.6 Casablanca-Settat

Official routes: CRI Casablanca-Settat https://www.casainvest.ma/ plus CRI-Invest national map. Check Casablanca, Nouaceur, Sapino, Settat, Mediouna, Bouskoura, Berrechid, Midparc, CasaNearshore, Technopark Casablanca, ONEE/Lydec grid, procurement, and Uptime.

Confirmed/high-confidence assets:

- Oracle OCI Morocco West / Casablanca `af-casablanca-1`: Oracle docs and announcement are A. Oracle identifies N+ONE Datacenters as hosting partner (A for Oracle statement).
- N+ONE Settat and Nouaceur certified sites: Uptime Institute country page and N+ONE client story are A for certification/location/project names. Tie to Oracle only where Oracle/DCD explicitly states hosting.
- Orange Maroc Casablanca Datacenter #1 / Orange Tech in Nouaceur: Orange corporate PDF and Uptime country page are A for facility/certification facts; press is B.
- inwi Sapino / Casablanca lead: inwi official datacenter page is A for service; Le360/DCD/directories are B/C for exact Sapino details unless Uptime/operator corroboration is found.
- Maroc Telecom downtown Casablanca DC: TelQuel and Minkels case page are B for 2018 inauguration, Avenue Hassan II/downtown, SME hosting; upgrade to A only if IAM page is found.
- Oracle second region in Settat remains planned until OCI docs show a region or Oracle issues opening announcement.
- Naver/Nexus/Lloyds 500 MW AI hub near Casablanca/free zone: NAVER and Lloyds pages are A for company announcements; exact Moroccan permits/site/status require CRI/CRUI or construction proof. Treat as planned.

```text
site:casainvest.ma "data center"
site:casainvest.ma "centre de donnees"
site:casainvest.ma "cloud"
site:marchespublics.gov.ma "data center" "Casablanca"
"af-casablanca-1" "LEJ"
"N+ONE" "Nouaceur" "Uptime"
"N+ONE" "Settat" "Uptime"
"Orange Tech" "Nouaceur" "1,5 MW"
"Maroc Telecom" "Avenue Hassan II" "data center"
"inwi" "Sapino" "data center"
"Naver" "Casablanca" "500MW" "data center"
"Nexus Core Systems" "Morocco" "500 MW"
```

### 2.7 Marrakech-Safi

Official routes: CRI-Invest https://www.cri-invest.ma/map/my-cri/10 and CRI Marrakech-Safi https://www.marrakechinvest.ma/. Check Benguerir/Rehamna, UM6P, OCP, Atlas Cloud Services, Marrakech procurement, GITEX Africa announcements, Safi industrial/port zones, and ONEE grid.

Confirmed/high-confidence assets:

- Atlas Cloud Services / Benguerir: https://atlascloudservices.com/en/our-data-center/ is A for operator self-claim; Uptime country page and Benguerir project pages are A for Uptime award facts.
- OCP Group Benguerir Data Center DC2: Uptime project page https://uptimeinstitute.com/component/tierachievement/datacenter/benguerir-data-center-dc2/1122 is A for project name, OCP client, Benguerir location, award. Capacity such as 2000 m2 / 5 MW needs an operator/press source and should be B unless official OCP/UM6P page is found.
- inwi Marrakech certified lead appears in secondary/certification searches; verify in Uptime/Wana list before inventorying.

```text
site:marrakechinvest.ma "data center"
site:marrakechinvest.ma "centre de donnees"
"Benguerir" "data center" "OCP"
"Atlas Cloud Services" "Benguerir"
"Benguerir Data Center DC2"
site:um6p.ma "supercomput"
site:ocpgroup.ma "data center" "Benguerir"
"GITEX Africa" "data center" "Marrakech"
```

### 2.8 Draa-Tafilalet

Official route: CRI-Invest national map plus regional CRI search. Check Errachidia, Ouarzazate, Midelt, Zagora, Noor Ouarzazate, MASEN, universities, and regional procurement.

Known leads:

- Noor Ouarzazate/MASEN is renewable-energy context only, not a data center.
- No confirmed DC found in this review.

```text
"Draa-Tafilalet" "data center"
"Ouarzazate" "data center"
"Ouarzazate" "centre de donnees"
"Midelt" "data center"
site:masen.ma "Ouarzazate" "data center"
site:marchespublics.gov.ma "centre de donnees" "Ouarzazate"
```

### 2.9 Souss-Massa

Official routes: CRI-Invest https://www.cri-invest.ma/map/my-cri/3 and CRI Souss-Massa https://agadirinvest.com/. Check Agadir, Ait Melloul, Haliopolis/Haliopark, Technopark Agadir, Oracle R&D, ONEE grid, and regional procurement.

Known leads:

- Oracle Agadir R&D hub is A for R&D, not data-center facility evidence.
- No confirmed commercial DC found in this review.

```text
site:agadirinvest.com "data center"
site:agadirinvest.com "centre de donnees"
"Agadir" "data center"
"Oracle" "Agadir" "R&D"
"Haliopark" "data center"
"Souss-Massa" "cloud souverain"
```

### 2.10 Guelmim-Oued Noun

Official route: CRI-Invest https://www.cri-invest.ma/map/my-cri/8. Check Guelmim, Tan-Tan, Sidi Ifni, regional renewables, ports, and southern-provinces investment incentives.

Known leads:

- No confirmed data-center facility found in this review.
- Energy/port narratives are context only.

```text
site:cri-invest.ma/map/my-cri/8 "data center"
"Guelmim" "data center"
"Guelmim-Oued Noun" "centre de donnees"
"Tan-Tan" "data center"
"provinces du Sud" "data center"
```

### 2.11 Laayoune-Sakia El Hamra

Official route: CRI-Invest https://www.cri-invest.ma/map/my-cri/9. Check Laayoune, Boujdour, Es-Semara, Tarfaya wind, southern-provinces investment pages, and procurement.

Known leads:

- No confirmed data-center facility found in this review.
- Tarfaya/Laayoune renewable projects are energy context only.

```text
site:cri-invest.ma/map/my-cri/9 "data center"
"Laayoune" "data center"
"Laayoune-Sakia El Hamra" "centre de donnees"
"Tarfaya" "data center"
site:marchespublics.gov.ma "centre de donnees" "Laayoune"
```

### 2.12 Dakhla-Oued Ed-Dahab

Official route: CRI-Invest national map plus Dakhla regional CRI search. Check Dakhla, Aousserd, Dakhla Atlantic Port, renewables, southern-provinces investment programs, and Ministry/ADD announcements.

Known leads:

- 500 MW renewable-powered Dakhla data-center plan: currently B via Reuters/DCD/Agence Ecofin-style coverage unless ministry/CRI/procurement record is found. Treat as planned; also note Western Sahara sensitivity in external reporting.

```text
"Dakhla" "data center" "500 MW"
"Dakhla" "centre de donnees" "500 MW"
"Dakhla" "cloud souverain"
"Dakhla-Oued Ed-Dahab" "data center"
"Igoudar Dakhla" "data center"
site:marchespublics.gov.ma "data center" "Dakhla"
```

---

## 3. Verification Rules

1. Every inventory record must include operator/owner, facility name if known, commune/locality, region, status, and evidence URL(s).
2. A live hyperscaler region requires official cloud-provider documentation or announcement. For Morocco, Oracle Casablanca is A; AWS/Azure/GCP Morocco public regions are not confirmed in official region lists as of this review.
3. A Tier claim requires Uptime Institute page or operator certificate page. Marketing language alone stays B/C.
4. A planned/MoU project stays `planned` until construction, permit, procurement, commissioning, or cloud-region evidence appears.
5. Cable landing stations, internet exchanges, R&D hubs, and tech parks are not data centers unless a source names a data-center facility there.
6. If a URL is search-indexed but direct HTTP access fails due to TLS, geoblocking, or site downtime, keep the URL but add a recheck note in the working inventory; do not fabricate alternate URLs.
