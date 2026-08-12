# EE Explorer Official - Estonia Datacenter Enumeration

Date: 2026-08-12. Scope: Estonia (EE), all 15 counties: Harju, Hiiu, Ida-Viru, Jõgeva, Järva, Lääne, Lääne-Viru, Põlva, Pärnu, Rapla, Saare, Tartu, Valga, Viljandi, Võru. Angle: official, regulatory, planning, construction, environmental, electricity-grid, and other primary-source evidence for data-center facilities and projects.

Reliability grades in this official explorer:

- **A**: Estonian official register/portal, municipal planning or permit document, regulator decision, environmental decision, grid operator document, cadastral record, or official hyperscale cloud-region list.
- **B**: first-party operator/developer page or press release, established trade/local press, contractor case study, investment-agency article, industry association/IXP source.
- **C**: catalog/aggregator, search snippet, social media, forum, directory mirror, unsourced market list.

Use this file to decide whether a candidate can be counted. Operator pages and trade press can seed and support a record, but the strongest confirmation is EHR, municipal planning/permitting, environmental, grid, cadastral, or business-register evidence.

---

## 0. Estonia-Specific Ground Rules

- Estonia has **15 counties and 79 local government units** according to the state portal (https://www.eesti.ee/en/republic-of-estonia/republic-of-estonia/information-about-estonia/) and census methodology (https://rahvaloendus.ee/en/census-2021/methodology-and-quality/levels-of-administrative-units-and-spatial-data). Counties are enumeration buckets; local affairs are handled by municipalities. Note: the 2026 Ministry of Regional Affairs page says 78 units (https://www.agri.ee/en/objectives-and-activities/local-governments), so use EHAK/state spatial data if exact current municipality counts matter.
- The official spatial-administration reference is EHAK / Administrative and Settlement Division from Maa- ja Ruumiamet: https://geoportaal.maaamet.ee/eng/spatial-data/administrative-and-settlement-division-p312.html. Use it to map addresses, municipalities, and counties.
- The **Building Register (Ehitisregister, EHR)** is the main official facility evidence source. TTJA describes EHR as the register for planned, under-construction, and existing buildings and procedures, and says it is public and used by local governments for construction-document processing: https://ttja.ee/ariklient/ehitised-ehitamine/ehitisregister-ehr. Public app: https://ehr.ee. E-construction platform: https://livekluster.ehr.ee/ui/ehr/v1.
- EHR does not reliably expose a public purpose/category called `andmekeskus`. Data centers may appear as office, telecom, industrial, storage, technical, or other building purposes. Search by address, legal entity, parcel, municipality, and planning/permit IDs, not only by data-center keywords.
- Building permits (`ehitusluba`), building notices (`ehitusteatis`), use permits (`kasutusluba`), use notices (`kasutusteatis`), construction-start notices, detailed plans (`detailplaneering`), and design conditions (`projekteerimistingimused`) are normally municipal workflows surfaced through EHR and municipal pages.
- **Count as operating** only with a use permit/use notice, EHR `kasutusel` status, or first-party operator page clearly advertising a live facility. **Count as under construction** only with a building permit/start notice or official construction contract tied to a site. **Count as planned** with a detailed-plan initiation/adoption, EIA/KMH screening, grid-connection evidence, or developer application.
- The Business Register (Äriregister) at https://ariregister.rik.ee is Grade A for company identity, registry code, registered address, officers, and activity codes. EMTAK 6311/63101 (`andmetöötlus, veebimajutus jms`) and 6312/63120 are useful pivots, but they do not prove a physical data center.
- Official announcements are published at https://www.ametlikudteadaanded.ee. Search for planning, EIA/KMH, and permit notices by operator, parcel, municipality, and `andmekeskus`.
- Environment: Keskkonnaamet (https://keskkonnaamet.ee) and KOTKAS (https://kotkas.envir.ee) are Grade A for environmental permits, air permits for backup generators, waste/water permits, and EIA/KMH decisions. Keskkonnaamet states environmental permits are applied for in KOTKAS: https://keskkonnaamet.ee/en/environmental-use-radiation/environmental-protection-permit.
- Electricity: Elering (TSO, https://elering.ee/en/connecting-electricity-network, portal https://egle.ee) is Grade A for transmission connections; Elektrilevi (DSO, https://www.elektrilevi.ee) is Grade A for distribution connections; Konkurentsiamet (https://www.konkurentsiamet.ee) is Grade A regulator context. Grid evidence alone is not a data-center record unless tied to a specific developer/site.
- No public hyperscale cloud region is listed in Estonia by AWS, Azure, Google Cloud, or Oracle as of this review. Check official lists before claiming a provider region: AWS https://aws.amazon.com/about-aws/global-infrastructure/regions_az/; AWS Local Zones https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/; Azure https://azure.microsoft.com/en-us/explore/global-infrastructure/; Google Cloud https://cloud.google.com/about/locations; Google data-center locations https://datacenters.google/locations; Oracle https://www.oracle.com/cloud/public-cloud-regions/.

Estonian lifecycle vocabulary:

```
üldplaneering -> detailplaneering -> projekteerimistingimused / ehitusprojekt -> ehitusluba / ehitusteatis -> ehitamise alustamise teatis -> kasutusluba / kasutusteatis -> kasutusel
```

---

## 1. Official Source Backbone

### 1.1 Construction and Planning

- EHR public app: https://ehr.ee. Grade A.
- E-construction platform: https://livekluster.ehr.ee/ui/ehr/v1. Grade A.
- TTJA EHR description: https://ttja.ee/ariklient/ehitised-ehitamine/ehitisregister-ehr. Grade A.
- Maa- ja Ruumiamet e-construction/EHR page: https://maaruum.ee/ruumiloome-ehitus-ja-planeerimine/e-ehitus/e-ehitus. Grade A.
- EHR legal/regulatory basis: https://www.riigiteataja.ee/akt/129122024048. Grade A.
- Tallinn Planning Register: https://tpr.tallinn.ee and Tallinn's English service description https://www.tallinn.ee/en/tallinns-register-plans. Grade A for Tallinn plans, design conditions, and building-project proceedings.
- Ametlikud Teadaanded: https://www.ametlikudteadaanded.ee. Grade A.

EHR extraction fields:

```
EHR code
address
county / municipality / settlement
cadastral unit
building status
building purpose and gross area
permit/notice type and number
permit/notice date
authority
owner / applicant / representative
related structures: substation, generator, fuel tank, cooling, telecom ducts
```

### 1.2 Business, Land, and State ICT

- Äriregister: https://ariregister.rik.ee. Grade A for legal entities and EMTAK codes.
- Inforegister: https://www.inforegister.ee. Grade C/B mirror for quick discovery; confirm in Äriregister.
- Maa-amet / Land Board / cadastre: https://maaamet.ee and Geoportal EHAK page above. Grade A.
- RIA: https://www.ria.ee and state cloud `Riigipilv`: https://riigipilv.ee. Grade A context for state ICT, but public locations are not a commercial facility census.
- e-Estonia / Invest Estonia / Trade with Estonia pages are government promotion or investment-marketing context. Use as B unless they link to permits or official plans.

### 1.3 Environment and Grid

- Keskkonnaamet: https://keskkonnaamet.ee. Grade A.
- KOTKAS: https://kotkas.envir.ee. Grade A.
- KOTKAS legal/system reference: https://www.riha.ee/Infos%C3%BCsteemid/Vaata/kotkas and https://www.riigiteataja.ee/akt/130062020005. Grade A.
- Elering connection process: https://elering.ee/en/connecting-electricity-network. Grade A.
- Elering homepage/grid context: https://elering.ee/en. Grade A.
- Elektrilevi: https://www.elektrilevi.ee. Grade A.
- Konkurentsiamet: https://www.konkurentsiamet.ee. Grade A.
- Baltic synchronisation context: Konkurentsiamet annual-report page notes the Baltic States disconnected from the Russian system on 2025-02-08 and synchronised with continental Europe on 2025-02-09: https://aastaraamat.konkurentsiamet.ee/en/node. Grade A context.

Environmental/grid extraction fields:

```
permit or decision number
applicant / operator
site address / cadastral unit
backup generator count and MW/kW
fuel storage volume
UPS/battery storage
cooling and water demand
noise / air-emissions modelling
connection voltage and substation name
connection capacity MW/MVA
heat-reuse or district-heating link
status and decision date
```

---

## 2. Query Templates

Use Estonian first, then English. Replace `{maakond}`, `{vald}`, `{linn}`, `{operator}`, `{address}`, and `{parcel}`.

### 2.1 Estonian Core Terms

```
andmekeskus
andmekeskused
andmekeskuste
andmetöötluskeskus
serveriruum
serverikeskus
kolokatsioon
veebimajutus
andmetöötlus
pilveteenus
tehisintellekti taristu
andmekeskus ehitusluba
andmekeskus kasutusluba
andmekeskus detailplaneering
andmekeskus projekteerimistingimused
andmekeskus keskkonnamõju hindamine
andmekeskus KMH
andmekeskus keskkonnaluba
andmekeskus välisõhu saasteluba
andmekeskus varugeneraator
andmekeskus diiselgeneraator
andmekeskus alajaam
andmekeskus liitumine
andmekeskus 110 kV
andmekeskus 330 kV
andmekeskus kaugküte
andmekeskus jääksoojus
andmekeskus soojuse taaskasutus
```

### 2.2 Official Search Patterns

```
site:ehr.ee "andmekeskus"
site:livekluster.ehr.ee "andmekeskus"
site:ametlikudteadaanded.ee "andmekeskus"
site:kotkas.envir.ee "andmekeskus"
site:keskkonnaamet.ee "andmekeskus"
site:elering.ee "andmekeskus"
site:elektrilevi.ee "andmekeskus"
site:ariregister.rik.ee "andmekeskus"
site:tallinn.ee "andmekeskus"
site:tallinn.ee "planeeringute register" "andmekeskus"
"andmekeskus" "ehitusluba" "{vald}"
"andmekeskus" "kasutusluba" "{linn}"
"andmekeskus" "detailplaneering" "{vald}"
"{operator}" "ehitusluba" "{vald}"
"{operator}" "detailplaneering"
"{operator}" "keskkonnaluba"
"{operator}" "KOTKAS"
"{operator}" "Elering" "liitumine"
"{address}" "ehitisregister"
"{parcel}" "detailplaneering"
filetype:pdf "andmekeskus" "detailplaneering" "{vald}"
filetype:pdf "andmekeskus" "ehitusluba" "{maakond}"
```

### 2.3 Business-Register Pivots

```
site:ariregister.rik.ee "6311" "andmetöötlus"
site:ariregister.rik.ee "63101" "andmetöötlus"
site:inforegister.ee "63101" "andmetöötlus" "{maakond}"
"{operator} OÜ" "registrikood"
"{operator}" "EMTAK" "6311"
"{operator}" "EMTAK" "63101"
"{operator}" "andmekeskus" "registrikood"
```

### 2.4 English Official-Adjacent Searches

```
"Estonia" "data center" "building permit"
"Estonia" "data centre" "planning permission"
"Estonia" "data center" "environmental permit"
"Estonia" "data centre" "environmental impact assessment"
"Estonia" "data center" "grid connection"
"{operator}" "{municipality}" "data center" "MW"
"{county}" "data center" "planning"
```

---

## 3. Officially Actionable Facility Seeds

Do not treat this table as a final inventory. It is a prioritized queue for official verification.

| Candidate | County / municipality | Best current source trail | Current official-use status |
|---|---|---|---|
| Greenergy Data Centers / MCF Group Estonia, GRE DC1 | Harju / Saue vald, Hüüru, Alajaama tee 1 | Greenergy contact page gives office/data-center address and MCF legal entity: https://gdc.ee/est/kontaktid (B); Greenergy first-party facility claims: https://www.greenergydatacenters.com and https://gdc.ee (B); Invest Estonia repeats 14,500 m2 / 31.5 MW: https://investinestonia.com/estonia-has-the-most-advanced-data-center-in-the-region/ (B); DCD launch: https://www.datacenterdynamics.com/en/news/greenergy-launches-data-center-in-estonia/ (B); company/address mirror: https://www.inforegister.ee/en/14069314-MCF-GROUP-ESTONIA-OU/ (C until confirmed in Äriregister). | Operating facility is well supported by first-party/trade sources. For Grade A count, verify Alajaama tee 1 in EHR, Saue municipal permit records, Äriregister, and cadastral data. |
| Greenergy / MCF expansion | Harju / Saue vald | Caverion 2026 contractor release says expansion technical systems due autumn 2026: https://www.caverion.com/newsroom/releases/2026/mcf-group-estonia-chooses-caverion-as-main-contractor-for-a-eur-50-million-project-the-largest-high-security-data-centre-in-the-baltics-is-expanding/ (B); Delfi/Ärileht AI expansion article (B): https://arileht.delfi.ee/artikkel/120600543/baltikumi-esimene-ai-tehas-mcf-investeerib-huuru-andmekeskuse-laienemisse-ligi-100-miljonit-eurot. | Under-construction/planned only after EHR/Saue building permit or start notice is verified. |
| Sunly Risti Data Center Campus | Lääne / Lääne-Nigula vald, near Risti | Sunly first-party notice: https://sunly.ee/uudised/sunly-kavandab-eestisse-baltimaade-suurimat-andmekeskust (B); municipal notice says Sunly submitted a detailed-plan application, 36 ha, six data-processing buildings, Elering-grid connection via Risti solar-park substation: https://www.laanenigula.ee/uudised/sunly-kavandab-eestisse-baltimaade-suurimat-andmekeskust (A for municipal planning notice); project site: https://ristikampus.ai/ (B); ERR English: https://news.err.ee/1609962983/renewable-energy-company-wants-to-build-baltics-largest-data-center-in-estonia (B); DCD: https://www.datacenterdynamics.com/en/news/sunly-plans-to-build-baltic-regions-largest-data-center-in-estonia/ (B). | Planned project. Do not count as operating or under construction until detailed plan, EHR permit/start notice, and environmental/grid decisions advance. |
| Telia Eesti Tallinn data centers | Harju / Tallinn and Tallinn edge | Telia corporate DC/colo service page: https://www.teliacompany.com/en/solutions/global/data-centers-and-colocation (B for group service); ERR says Telia planned a 10m EUR data center next to Utilitas by H2 2021: https://www.err.ee/951199/telia-ehitab-utilitase-elektrijaama-korvale-10-miljoniga-andmekeskuse (B); Telia Digitark first-party mirror may exist, but use the ERR URL unless the current Telia page is found. | Candidate operating telco facilities. Verify each address in Tallinn Planning Register/EHR before counting as distinct physical sites. |
| Elisa Eesti Tallinn | Harju / Tallinn | Elisa first-party says data-center services in Finland and Estonia: https://elisa.com/carrierservices/Co-location_services_and_solutions/data-center-services/ (B); catalog address Adala 4: https://www.datacentermap.com/estonia/tallinn/elisa-tallinn/ (C). | Candidate operating colo. Verify Adala 4 and owner/use in EHR/Tallinn before counting. |
| WaveCom | Harju / Tallinn, Endla 16 | WaveCom first-party DC page: https://wavecom.ee/en/andmekeskus (B); WaveCom news/contact page gives Endla 16: https://wavecom.ee/en/news/wavecom-opened-innovative-data-center-tallinn (B). | Candidate operating facility. Confirm Endla 16 in EHR and legal entity in Äriregister. |
| INFONET DC | Harju / Tallinn, Laevastiku 3r | First-party facility page: https://infonetdc.com/en/data-center/ (B); first-party contacts page gives INFONET DC OÜ reg. no. 12501440 and datacenter address Laevastiku 3r: https://infonetdc.com/en/contacts/ (B). | Candidate operating facility. Verify EHR/Tallinn and Äriregister before Grade A count. |
| FairyHosting / Narva Datacenter | Ida-Viru / Narva | FairyHosting first-party colocation page says colocation in Estonia and lists Telia Sõpruse/Tallinn plus Narva company address: https://fairyhosting.com/colocation (B for service, not Narva facility); catalog Narva DC address Mihail/Ak. Maslovi 1: https://www.datacentermap.com/estonia/narva/narva-datacenter/ and https://colomap.com/facilities/narva-datacenter/ (C); FairyHosting 2014 address notice: https://my.fairyhosting.com/announcements/12 (B for company address only). | Do not count Narva DC from catalogs alone. Verify via EHR/Narva/Äriregister or a stronger FairyHosting facility page. |
| RIA / Riigipilv state infrastructure | Not public | https://www.ria.ee and https://riigipilv.ee (A context). | Context only; do not enumerate secret/non-public state facilities. |
| Nebius Estonia | No confirmed county | ERR speculation only: https://news.err.ee/1610099740/tech-firm-nebius-hiring-push-fuels-speculation-over-estonia-data-center-plans (B). | Watchlist only; no facility record without official/operator site. |

---

## 4. Division-by-Division Official Strategy

Each county workflow starts with: EHR county filter, county+municipality web search, municipal detailed-plan/permit pages, Ametlikud Teadaanded, Äriregister EMTAK 6311/63101 entities by registered address, KOTKAS/Keskkonnaamet, and Elering/Elektrilevi. County names below include ASCII aliases used in `world-manifest.jsonl`.

| County | Municipal coverage to include | Priority and official strategy |
|---|---|---|
| Harju | Tallinn, Saue, Rae, Harku, Viimsi, Maardu, Keila, Saku, Lääne-Harju, Jõelähtme, Kiili, Kose, Kuusalu, Raasiku, Anija, Loksa | Highest priority. Verify Greenergy at Alajaama tee 1/Hüüru via EHR, Saue planning/permits, Äriregister, cadastre. In Tallinn use TPR + EHR for Telia, Elisa, WaveCom, INFONET and catalog addresses: Sõpruse pst 193, Pärnu mnt 158, Sõle tn 14/25, Ädala/Adala 4, Endla 16, Laevastiku 3R. Sweep industrial municipalities Rae, Saue, Harku, Lääne-Harju, Maardu for new detailed plans and 110 kV/330 kV loads. |
| Hiiu | Hiiumaa vald | Low yield. Run EHR county sweep, Hiiumaa planning pages, Ametlikud Teadaanded, and `andmekeskus/serveriruum` searches. Avoid counting municipal IT rooms or island-services data portals. |
| Ida-Viru | Narva, Narva-Jõesuu, Sillamäe, Kohtla-Järve, Jõhvi, Alutaguse, Lüganuse, Toila | Medium priority because of Narva catalog seed and industrial/grid context. Verify FairyHosting/Narva via Narva EHR/planning and company records. Sweep IVIA https://ivia.ee, industrial parks, Enefit/power-zone planning, and Elering/Elektrilevi large-load notices. |
| Jõgeva | Jõgeva, Mustvee, Põltsamaa | Low yield. EHR county sweep, municipal detailed plans, EMTAK 6311 registered addresses, and terms `andmekeskus`, `serveriruum`, `veebimajutus`. |
| Järva | Paide, Türi, Järva vald | Low yield. Focus Paide/Türi industrial plots and EHR purpose-code anomalies. No confirmed DC lead in this review. |
| Lääne | Haapsalu, Lääne-Nigula, Vormsi | High priority for Sunly Risti. Track Lääne-Nigula detailed-plan initiation/adoption, EHR permit filings, KOTKAS/KMH screening, Elering connection/substation evidence, Risti campus site, and Ametlikud Teadaanded. Haapsalu/Vormsi otherwise low yield. |
| Lääne-Viru | Rakvere linn, Rakvere vald, Tapa, Kadrina, Vinni, Viru-Nigula, Haljala, Väike-Maarja | Low-medium. Sweep Rakvere/Tapa/Viru-Nigula industrial land and Elering substations. Distinguish data-center leads from logistics/industrial warehouses. |
| Põlva | Põlva, Räpina, Kanepi | Low yield. One-pass official sweep; likely only small hosting/server-room mentions. |
| Pärnu | Pärnu linn, Tori, Saarde, Häädemeeste, Põhja-Pärnumaa, Lääneranna, Kihnu | Low-medium. Keskkonnaamet HQ is in Pärnu but not a DC. Sweep Pärnu city industrial/port areas, KOTKAS for generator permits, and municipal plans. |
| Rapla | Rapla, Kohila, Märjamaa, Kehtna | Low-medium due proximity to Tallinn and industrial sites. Sweep Kohila/Märjamaa/Rapla detailed plans and EHR county filter; use low-yield template before recording no projects. |
| Saare | Saaremaa, Muhu, Ruhnu | Low yield. Grid/Elering island projects are context only unless a DC customer is named. Sweep Kuressaare/Saaremaa planning and EHR. |
| Tartu | Tartu linn, Tartu vald, Kambja, Luunja, Elva, Nõo, Kastre, Peipsiääre | Medium for research/HPC and enterprise IT, low for commercial colo. Check University of Tartu/HPC only as non-commercial unless colo is marketed; sweep Tartu Science Park/industrial areas and EHR. |
| Valga | Valga, Tõrva, Otepää | Low yield. Sweep Valga city and cross-border heat/power references; catalogs may list old telco sites but require EHR/operator proof. |
| Viljandi | Viljandi linn, Viljandi vald, Mulgi, Põhja-Sakala | Low yield. EHR and municipal one-pass; watch industrial land plans and EMTAK 6311 entities. |
| Võru | Võru linn, Võru vald, Antsla, Rõuge, Setomaa | Low yield. EHR, municipal planning, and Ametlikud Teadaanded. Avoid generic public-data-service false positives. |

Low-yield county template:

```
"{maakond}" "andmekeskus"
"{maakond}" "data center"
"{maakond}" "serveriruum"
"{main town}" "andmekeskus"
site:{municipality-domain} "andmekeskus"
site:{municipality-domain} "detailplaneering" "andmekeskus"
site:{municipality-domain} "ehitusluba" "andmekeskus"
site:ametlikudteadaanded.ee "{vald}" "andmekeskus"
site:kotkas.envir.ee "{vald}" "andmekeskus"
```

---

## 5. Record Rules

A record should not be promoted above its weakest unresolved dependency. Examples:

- Operator page says facility is live, but no official address/permit found: `evidence_grade=B`, `status=operating_by_operator`, `official_status=unverified`.
- Catalog lists a facility and address, but operator page only advertises generic hosting: `evidence_grade=C`, `status=candidate`, `do_not_count=true`.
- Municipal notice says detailed-plan application filed: `evidence_grade=A`, `status=planned`, `do_not_count_as_operating=true`.
- EHR use permit or active EHR building status tied to an operator/address: `evidence_grade=A`, countable.
- Grid connection or substation work names no data-center customer: context only, no facility record.

Recommended fields:

```
name
country
county
municipality
settlement
address
cadastral_or_parcel_id
operator_or_developer
legal_entity
registry_code
em_tak_code
status
status_basis
capacity_mw
white_space_m2
building_area_m2
racks
construction_evidence_url
planning_evidence_url
environment_evidence_url
energy_evidence_url
operator_evidence_url
trade_press_url
evidence_date
evidence_grade
do_not_count_reason
notes
```
