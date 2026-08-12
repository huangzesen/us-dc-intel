# MA Explorer Industry - Morocco Datacenter Enumeration

Date: 2026-08-12. Country: **MA Morocco**. Scope: industry, trade press, operator pages, certification pages, directories, and regional-press discovery for Moroccan data centers. Use this with `MA/explorer-official.md` for official verification.

Reliability grades:

- **A** = primary source for the specific fact: operator/facility page, company press release, Oracle/OCI page, Uptime Institute award page, government/CRI/procurement/utility page, official zone-authority page.
- **B** = strong secondary source: Data Center Dynamics, Reuters-carried reporting, Agence Ecofin, Medias24, Le360, TelQuel, LesEco, L'Economiste, Le Matin, La Vie Eco, Moroccan World News, Le Desk, h24info, aujourdhui.ma, challenge.ma, 2M.ma, MAP reposts, vendor/integrator article with named details.
- **C** = weak lead: DataCenterMap, Datacenters.com, Baxtel, Cloudscene, datacentercatalog.com, datacenterplatform.com, Telecontact, LinkedIn/social posts, snippets, inaccessible reports, generic market studies.

Directory entries are lead generation only. Do not use C-grade sources to assert status, capacity, certifications, or exact facility address without A/B corroboration.

---

## 0. Market Frame

Morocco is a small but accelerating data-center market. The historic base is telco-led and public/captive: Maroc Telecom, Orange Maroc, inwi/Wana, banks, ministries, OCP/UM6P, and a specialist colocation layer including MDC/Maroc Datacenter, N+ONE, Atlas Cloud Services, and smaller hosting providers.

Confirmed/high-confidence market structure:

- Casablanca-Settat and Rabat-Sale-Kenitra are the two strongest clusters.
- Oracle OCI Morocco West / Casablanca is live and is the only verified public hyperscaler cloud region in Morocco found in this review. OCI docs list `af-casablanca-1`, region key `LEJ`, one availability domain, release date 2026-02-20: https://docs.oracle.com/iaas/releasenotes/oci/new-region-casablanca-1.htm (A). Oracle's 2026 Morocco announcement says N+ONE Datacenters hosts the region: https://www.oracle.com/africa-fr/news/announcement/oracle-first-hyperscaler-open-public-cloud-2026-04-07/ (A).
- AWS/Azure/Google Cloud do not show a Morocco public cloud region in their official global-region pages checked for this rewrite. AWS has a Wavelength-with-Orange announcement, which is edge/network infrastructure, not an AWS Region.
- Uptime Institute country list is the best certification backbone for Morocco: https://uptimeinstitute.com/uptime-institute-awards/country/id/MA (A). It lists certified projects including N+ONE Settat/Nouaceur, Orange Maroc Nouaceur, Wana/inwi Rabat-Sale, OCP/Atlas Benguerir, and others. Always use the project-specific Uptime page when possible.

Core query set:

```text
Morocco "data center" 2026
Maroc "data center" inauguration
Maroc "centre de donnees"
Maroc datacenter MW
"cloud souverain" Maroc "data center"
"Oracle" "af-casablanca-1"
"N+ONE" Maroc Uptime
"Orange Tech" Nouaceur "1,5 MW"
"inwi" "Rabat Technopolis" datacenter
"Maroc Telecom" "Avenue Hassan II" "data center"
"Maroc Datacenter" Temara
"MDC" Temara datacenter
"Atlas Cloud Services" Benguerir
"Benguerir Data Center DC2"
"Naver" Morocco "500MW" "data center"
"Iozera" Tetouan "386MW"
"Dakhla" "500 MW" "data center"
"Vertiv" Morocco "50 MW" "data center"
```

Arabic secondary checks:

```text
"المغرب" "مركز البيانات"
"الدار البيضاء" "مركز البيانات"
"الرباط" "مركز البيانات"
"طنجة" "مركز البيانات"
"الداخلة" "مركز البيانات" "500"
"الناضور" "الكابل البحري"
"الاستضافة" "المغرب"
```

---

## 1. High-Signal Source List

| Source | Route | Default grade | Use |
|---|---|---|---|
| Oracle OCI release notes | https://docs.oracle.com/iaas/releasenotes/oci/new-region-casablanca-1.htm | A | Live OCI Casablanca region facts. |
| Oracle Morocco announcement | https://www.oracle.com/africa-fr/news/announcement/oracle-first-hyperscaler-open-public-cloud-2026-04-07/ | A | Casablanca region announcement and N+ONE hosting partner. |
| Uptime Institute Morocco awards | https://uptimeinstitute.com/uptime-institute-awards/country/id/MA | A | Certification project names, clients, locations, award types. |
| Uptime N+ONE story | https://uptimeinstitute.com/clients/nplusone | A | N+ONE Settat/Nouaceur certified facilities. |
| inwi Business Datacenter | https://inwi.ma/en/entreprise/datacenter | A | inwi service offering; pair with Uptime/press for named sites. |
| Orange Maroc press dossier | https://corporate.orange.ma/content/download/186730/3000921/version/1/file/DP_Orange_Conference_Novembre_VF.pdf | A | Orange Tech Nouaceur/Casablanca: inauguration date, initial MW, m2, solar, Uptime claim. |
| MDC / Maroc Datacenter | https://www.mdc.ma/datacenter/ | A | Temara site, 2000 m2, Tier III-designed/self-claimed facts. |
| Atlas Cloud Services | https://atlascloudservices.com/en/our-data-center/ | A | Benguerir data-center self-claims and Uptime Tier III/IV statement. |
| HostoWeb | https://www.hostoweb.com/en/ ; https://www.hostoweb.com/en/about-us/contact | A/C | A for services/offices; C for exact DC facility locations unless corroborated. |
| Maroc Telecom/IAM | https://www.iam.ma/ | A if page found | Operator-primary route for IAM hosting/DC claims. |
| Ministry industry page for Maroc Datacenter | https://www.mcinet.gov.ma/en/content/maroc-datacenter-1st-cloud-computing-platform-francophone-africa | A | Public-program description of Maroc Datacenter / Tier III-designed project. |
| Data Center Dynamics | https://www.datacenterdynamics.com/en/news/ | B | Oracle, Naver, Iozera, Dakhla, inwi discovery. |
| Agence Ecofin | https://www.agenceecofin.com/ and https://www.ecofinagency.com/ | B | Dakhla, Orange, digital-infrastructure coverage. |
| Medias24 | https://medias24.com/ | B | inwi, Vertiv, policy and energy-market coverage. |
| Le360 | https://fr.le360.ma/ | B | inwi, Maroc market notes, regional business coverage. |
| TelQuel | https://telquel.ma/ | B | Maroc Telecom Casablanca 2018 DC. |
| Le Matin | https://lematin.ma/ | B | Certification/infrastructure/business announcements. |
| LesEco | https://leseco.ma/ | B | Certifications, CRI/sector coverage. |
| La Vie Eco / L'Economiste / Le Desk / Moroccan World News | source-specific search | B | Secondary project discovery and policy context. |
| NAVER Corp press | https://www.navercorp.com/media/pressReleasesDetail?seq=32606 | A for company announcement | 500 MW Morocco AI/data-center consortium; still planned unless official Moroccan permit/construction evidence appears. |
| Lloyds Capital data centers | https://www.lloydscapital.com/datacenters | A for company self-claim | 500 MW Morocco AI campus/free-zone claim; verify site and permits separately. |
| Iozera PRNewswire | https://www.prnewswire.com/news-releases/us-based-iozera-announces-mou-with-government-of-morocco-for-launch-of-eco-friendly-ai-data-center-in-morocco-302136157.html | A-company/B-project | Company-distributed MoU announcement for Tetouan 386 MW AI hub; not proof of construction. |
| Directories | DataCenterMap, Datacenters.com, Baxtel, Cloudscene, datacentercatalog.com | C | Discovery only. |

Trade-press query templates:

```text
site:datacenterdynamics.com/en/news/ Morocco "data center"
site:datacenterdynamics.com/en/news/ "Oracle" "Casablanca"
site:datacenterdynamics.com/en/news/ "Naver" "Morocco"
site:agenceecofin.com Maroc "data center"
site:ecofinagency.com Morocco "data center"
site:medias24.com "data center" Maroc
site:le360.ma "datacenter" Maroc
site:telquel.ma "Maroc Telecom" "data center"
site:leseco.ma "data center" Maroc
site:lematin.ma "datacenter" "inwi"
site:moroccoworldnews.com "Orange Maroc" "data center"
site:ledesk.ma "Maroc IA 2030" "cloud"
site:lavieeco.com "Medusa" "Nador"
```

---

## 2. Facility and Project Leads

### 2.1 Operational / certified / high-confidence

| Asset | Region | Status | Best evidence | Grade guidance |
|---|---|---|---|---|
| Oracle OCI Morocco West / Casablanca, `af-casablanca-1`, key `LEJ` | Casablanca-Settat | Live public cloud region | OCI release notes; Oracle Morocco announcement | A for cloud region; A that Oracle names N+ONE hosting partner. |
| N+ONE Datacenter II Phase 1 | Casablanca-Settat, Settat | Certified facility | Uptime country list; https://uptimeinstitute.com/clients/nplusone | A for N+ONE project/location/certification. |
| N+ONE Datacenter I Phase 2 | Casablanca-Settat, Nouaceur | Certified facility | Uptime country list; N+ONE Uptime client story | A for N+ONE project/location/certification. |
| Orange Maroc Casablanca Datacenter #1 / Orange Tech | Casablanca-Settat, Nouaceur/Casablanca | Operational/inaugurated 2025-11-19 | Orange PDF; Uptime Morocco awards | A for Orange PDF facts and Uptime certification; B for press summaries. |
| inwi / Wana INWI Rabat Technopolis DC2 | Rabat-Sale-Kenitra, Rabat-Sale/Sale Technopolis | Operational/certified | Uptime country/project page; inwi page; DCD/Le360/Medias24 | A for Uptime/inwi service; B for 1000 m2/inauguration articles. |
| MDC / Maroc Datacenter Temara | Rabat-Sale-Kenitra, Temara | Operational/self-claimed | https://www.mdc.ma/datacenter/ | A for Temara, 2000 m2, owner/operator, Tier III-designed self-claim. |
| Atlas Cloud Services / Benguerir | Marrakech-Safi, Benguerir | Operational/self-claimed/certification lead | Atlas page; Uptime country/project pages | A for operator/Uptime facts; B for 5 MW / 2000 m2 if sourced to press only. |
| OCP Group Benguerir Data Center DC2 | Marrakech-Safi, Benguerir | Certified design award | Uptime project page | A for OCP client/project/location/award; capacity requires separate source. |
| Maroc Telecom downtown Casablanca DC | Casablanca-Settat, Casablanca | Operational per 2018 press/case study | TelQuel 2018; Minkels case page | B unless IAM page is found. |
| HostoWeb Moroccan DC network | Fes-Meknes / Casablanca-Settat leads | Hosting/cloud service provider | HostoWeb home/contact pages | A for service/offices; C for exact DC sites. |

Operator query templates:

```text
site:uptimeinstitute.com/uptime-institute-awards/country/id/MA Morocco
site:uptimeinstitute.com "N+ONE DATACENTER" Morocco
site:uptimeinstitute.com "INWI Rabat Technopolis DC2"
site:uptimeinstitute.com "Benguerir Data Center DC2"
site:inwi.ma "datacenter"
site:mdc.ma "Temara" "datacenter"
site:corporate.orange.ma "Orange Tech" "Data Center"
site:atlascloudservices.com "Benguerir" "data center"
site:iam.ma "data center" OR "hebergement" OR "cloud"
site:hostoweb.com "Data Center" Morocco
```

### 2.2 Planned / announced pipeline

| Project | Region | Status | Evidence | Grade guidance |
|---|---|---|---|---|
| Naver / Nexus Core Systems / Lloyds Capital / Nvidia 500 MW AI campus | Near Casablanca / free-zone claim; verify exact commune | Planned/announced | NAVER press, Lloyds Capital page, DCD | A for company announcements; B for press detail; no operational claim until permit/construction/commissioning proof. |
| Iozera / Eureka Park 386 MW AI data center | Tanger-Tetouan-Al Hoceima, Tetouan | Planned/MoU | Iozera PRNewswire, DCD, Telecompaper | A-company/B-project; do not mark under construction without CRI/permit/site evidence. |
| Dakhla 500 MW renewable data center | Dakhla-Oued Ed-Dahab | Planned/government-announced in press | DCD / Reuters-carried, Ecofin | B unless ministry/CRI/procurement page appears. Note Western Sahara sensitivity. |
| Rabat sovereign DC with Vertiv support, 50 MW | Rabat-Sale-Kenitra, Rabat | Planned/discussion/MoU | Developing Telecoms, TechAfricaNews, WeAreTech, Medias24-style sources | B unless ministry or procurement page found. |
| Oracle second Morocco region in Settat | Casablanca-Settat, Settat | Planned | Oracle 2024 announcement / PRNewswire; future OCI docs needed | A for Oracle plan at announcement date; not live until OCI docs/opening announcement. |

Pipeline queries:

```text
"NAVER Cloud" "Morocco" "500MW"
"Nexus Core Systems" "Morocco" "AI factory"
"Lloyds Capital" "Morocco flagship" "500MW"
"Iozera" "Eureka Park" "Tetouan"
"Iozera" "Government of Morocco" "386MW"
"Dakhla" "500MW" "renewable" "data center"
"Vertiv" "Morocco" "50 MW" "sovereign data center"
"Oracle" "Settat" "cloud region" "Morocco"
```

---

## 3. Per-Region Industry Patterns

### 3.1 Tanger-Tetouan-Al Hoceima

Leads: Iozera/Eureka Park Tetouan 386 MW planned AI hub (B/A-company), Tanger Med connectivity and zones (A for zone context), possible Orange/Tanger network site leads (B/C). No operational colo facility confirmed in this review.

```text
"data center" Tanger
"centre de donnees" Tanger
"data center" Tetouan
"Iozera" Tetouan
"Eureka Park" Tetouan "data center"
"Tanger Med" "data center"
site:investangier.com "data center"
```

### 3.2 L'Oriental

Leads: Nador Medusa cable landing / Orange and inwi connectivity (B/A depending source), Nador West Med, Oujda technopole/university. Treat CLS as connectivity, not DC.

```text
"data center" Nador
"data center" Oujda
"Medusa" Nador "Orange Maroc"
"inwi" Nador "Medusa"
site:orientalinvest.ma "data center"
```

### 3.3 Fes-Meknes

Leads: HostoWeb Fes office/service lead (A for office/services, C for facility), Fes Shore, university/HPC. No confirmed commercial DC found.

```text
"data center" Fes
"HostoWeb" Fes "data center"
"Fes Shore" "data center"
site:fesmeknesinvest.ma "centre de donnees"
```

### 3.4 Rabat-Sale-Kenitra

Leads: inwi Rabat Technopolis DC2 (A/B), MDC Temara (A), public-sector DC/procurement leads, Vertiv/Rabat 50 MW sovereign DC plan (B), Atlantic Free Zone/Kenitra context.

```text
"INWI Rabat Technopolis DC2"
"inwi" "Rabat Technopolis" "Tier III"
"Maroc Datacenter" Temara
"MDC" Temara "2000m2"
"Vertiv" Rabat "50 MW"
"data center" Kenitra
site:rabatinvest.ma "data center"
```

### 3.5 Beni Mellal-Khenifra

Leads: OCP Khouribga internal IT only if sourced; otherwise low-confidence. No confirmed DC.

```text
"Beni Mellal" "data center"
"Khouribga" "data center" OCP
"Beni Mellal-Khenifra" "centre de donnees"
```

### 3.6 Casablanca-Settat

Leads: Oracle/N+ONE live region (A), N+ONE Nouaceur/Settat certifications (A), Orange Tech Nouaceur/Casablanca (A), Maroc Telecom downtown Casablanca (B), inwi Sapino (B/C unless operator/Uptime corroborated), Naver/Nexus/Lloyds planned 500 MW hub (A-company/B), Oracle Settat planned region (A-plan, not live).

```text
"af-casablanca-1" "LEJ"
"Oracle" "N+ONE Datacenters" Casablanca
"N+ONE" Nouaceur Settat Uptime
"Orange Tech" Nouaceur "1.5 MW"
"Maroc Telecom" "data center" Casablanca "2018"
"inwi" Sapino "data center"
"Naver" Casablanca "500MW"
site:casainvest.ma "data center"
```

### 3.7 Marrakech-Safi

Leads: Atlas Cloud Services / Benguerir (A), OCP Benguerir DC2 Uptime (A), UM6P/African SuperComputing Center (B/A if UM6P page found), GITEX Africa deal announcements in Marrakech (B discovery), possible inwi Marrakech certification lead (verify in Uptime).

```text
"Benguerir Data Center DC2"
"Atlas Cloud Services" "Benguerir"
"OCP" "Benguerir" "data center"
"UM6P" "supercomputing" "Benguerir"
"inwi" Marrakech "Uptime" "data center"
site:marrakechinvest.ma "data center"
```

### 3.8 Draa-Tafilalet

Leads: none confirmed. Noor Ouarzazate is energy context only.

```text
"Ouarzazate" "data center"
"Draa-Tafilalet" "centre de donnees"
"green data center" "Ouarzazate"
```

### 3.9 Souss-Massa

Leads: Oracle Agadir R&D hub (A for R&D only), Haliopark/Agadir tech/offshoring context. No confirmed DC.

```text
"Agadir" "data center"
"Oracle" "Agadir" "R&D hub"
"Haliopark" "data center"
site:agadirinvest.com "data center"
```

### 3.10 Guelmim-Oued Noun

Leads: none confirmed; renewables and southern-provinces investment context only.

```text
"Guelmim" "data center"
"Guelmim-Oued Noun" "centre de donnees"
"Tan-Tan" "data center"
```

### 3.11 Laayoune-Sakia El Hamra

Leads: none confirmed; Tarfaya/Laayoune renewable projects are context only.

```text
"Laayoune" "data center"
"Laayoune-Sakia El Hamra" "centre de donnees"
"Tarfaya" "data center"
```

### 3.12 Dakhla-Oued Ed-Dahab

Leads: Dakhla 500 MW renewable-powered data center plan (B, planned), possible Igoudar Dakhla naming in weaker sources (C unless official/strong press confirms), Dakhla Atlantic Port/connectivity context. Note Western Sahara dispute sensitivity in external datasets.

```text
"Dakhla" "data center" "500 MW"
"Dakhla" "centre de donnees" "500 MW"
"Igoudar Dakhla" "data center"
"Dakhla" "cloud souverain"
```

---

## 4. Status Language

Interpret French/English status language conservatively:

- `MoU`, `protocole d'accord`, `annonce`, `plan`, `will build`, `expected`, `aims`, `study`, `exploring` = planned.
- `appel d'offres`, `consultation`, `attribution`, `regulatory authorizations obtained`, `land acquired`, `CRUI approval` = procurement/permit stage.
- `construction started`, `chantier`, `lancement des travaux`, `groundbreaking` = under construction, but verify date and site.
- `inaugure`, `mis en service`, `operational`, `now available`, `certified constructed facility`, `region available` = operational or certified signal.

Verification rules:

1. Every facility lead needs owner/operator, locality, region, status, and evidence URL.
2. Separate `cloud region`, `data center`, `cable landing station`, `R&D hub`, and `tech park` asset types.
3. Keep planned hyperscale/AI projects out of operational counts until a commissioning/source page confirms service.
4. Deduplicate by operator + facility/locality + region. N+ONE Settat and N+ONE Nouaceur are separate Uptime-listed projects.
5. Recheck official hyperscaler region lists each run before saying Morocco has or lacks AWS/Azure/GCP regions.
