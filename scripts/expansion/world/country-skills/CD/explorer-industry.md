# CD Explorer Industry - DRC Datacenter Enumeration via Operators, Cloud, Trade Press, and Province Queries

Date: 2026-08-12. Scope: Democratic Republic of the Congo (DRC / RDC) methodology for discovering datacenter projects from industry/vendor sources, cloud-region evidence, telecom associations, trade press, and province-specific query patterns. Reliability grades: **A** = official/primary source, **B** = strong secondary/trade press or association source, **C** = weak directory/aggregator/social signal needing confirmation.

---

## 0. Market structure to assume

- DRC is a very small but active commercial datacenter market. The practical enumeration universe is concentrated in **Kinshasa**, with verified secondary signals in **Lubumbashi** and strategic-plan targets in **Goma, Moanda, Kisangani, Kinshasa, and Lubumbashi**.
- The strongest public evidence comes from operator pages and regulatory/network lists, not from planning portals. Start with **carrier-neutral colocations**, **licensed ISPs/MNOs**, and **IXP member lists**, then pivot each company name into French and English searches.
- The national digital plan is useful as a target-city map, not proof of build. The Presidency page describes the PNN Horizon 2025 as an infrastructure-focused digital strategy, and the published plan text calls for at least five neutral Tier-3/Tier-4 data centers in **Goma, Moanda, Kisangani, Kinshasa, and Lubumbashi**.
- No official AWS/Azure/GCP/OCI public cloud region is in DRC as of the checked official region lists. Cloud-region checks should be used to avoid false positives: nearest major public regions are South Africa regions such as AWS Africa (Cape Town), Azure South Africa North/West, Google Cloud `africa-south1` Johannesburg, and OCI South Africa Central (Johannesburg).

---

## 1. Vendor/operator seed list

### 1.1 Carrier-neutral and colo providers

| Operator / facility | Province | Evidence to use | Grade | Notes |
|---|---:|---|---|---|
| **Raxio DRC1 / Raxio Kinshasa** | Kinshasa | Official page: https://www.raxiogroup.com/data-centres/dr-congo/ ; datasheet: https://www.raxiogroup.com/wp-content/uploads/2025/04/RAX016-4-Data-Sheet-SITE-DRC1-v2.pdf ; launch release: https://www.raxiogroup.com/drc-inaugurates-30-million-raxio-data-centre-to-catalyse-digital-economy/ | A | Official source states Kinshasa location, 2024 launch, carrier-neutral Tier III positioning, 400 racks, 1.5 MW IT power. Datasheet gives Limete Industriel 12ieme rue no. 9/11 and rack power range. |
| **OADC Texaf - Kinshasa** | Kinshasa | Official page: https://www.openaccessdc.net/fr/kinshasa ; trade coverage: https://www.datacenterdynamics.com/en/news/oadc-launches-data-center-in-dr-congo/ ; https://www.connectingafrica.com/data-centers/drc-s-first-tier-3-data-center-is-live | A/B | OADC page confirms open-access carrier-neutral Kinshasa ecosystem; trade sources give launch timing, 2 MW-capable site, 550+ racks, Silikin Village/TEXAF context. |
| **Fastnet Lubumbashi Data Center** | Upper Katanga | Operator page: https://fastnet.cd/2017/09/27/hello-world/ ; trade coverage: https://www.datacenterdynamics.com/en/news/first-data-center-in-the-democratic-republic-of-the-congo-opens/ | B | Fastnet article says the Lubumbashi datacenter is at the ESNAP teleport with 50 racks and international fiber connectivity. Small facility; verify whether still operational before counting current supply. |
| **Orange Business RDC datacenter hosting** | Kinshasa likely; exact site not public | Official service page: https://business.orange.cd/fr/ict/hbergement-datacenter.html | B | Orange RDC offers rack/hosting space in its datacenter, backbone fiber, 24/7/365 support and SLA language. Treat as operator/datacenter-hosting evidence, not as public MW evidence. |
| **Global Broadband Solution / GBS** | Kinshasa; possible Lubumbashi directory signal | Official site: https://www.gbs.cd/ ; ARPTC ISP listing; directories: DataCenterMap / Datacenters.com / Inflect | C until operator page confirms facility | ARPTC confirms GBS as a licensed ISP; directories list Kinshasa and sometimes Lubumbashi datacenter entries. Use directories only as leads, then confirm via GBS, customer pages, PeeringDB/KINIX, or street/address evidence. |
| **United S.A. / UNITED Kinshasa** | Kinshasa | Official site/contact: https://united.cd/?lang=en ; ARPTC ISP listing; DataCenterMap/DatacenterPlatform directory entries | C/B | United official site confirms Kinshasa fiber/hosting business and address at 165 Batetela Avenue; facility-level claims mostly come from directories. |
| **Orioncom / Microcom / Afrinet / Liquid Telecom DRC / CSquared / GVA / Airtel / Vodacom / Africell** | Mostly Kinshasa, with city POPs | ARPTC ISP/MNO lists; KINIX/PeeringDB; company pages | B as operator leads | These are network operators whose POPs, hubs, or switch rooms may be mislabelled as datacenters. Count only if there is explicit colocation/datacenter/white-space evidence. |

### 1.2 Official operator registries and network signal

- **ARPTC ISP list**: https://www.arptc-solution.cd/license_list/operatorinternetgrp . This is the best local operator census. It lists Airtel, Orange, Vodacom, GVA, Liquid Telecom DRC, Microcom, United, CSquared, Orioncom, Global Broadband Solution, Fast Net, Africell and others as Internet providers. **Grade A for licensed operator existence; not facility proof.**
- **ARPTC mobile operator list**: https://www.arptc-solution.cd/license_list/newoperatorsgrp . Lists Airtel Congo RDC, Orange RDC, Vodacom Congo RDC, Africell RDC. **Grade A operator source.**
- **KINIX / PeeringDB via ISOC Pulse**: https://pulse.internetsociety.org/en/ixp-tracker/ixp/293/ . Shows KINIX in Kinshasa, July 2026 data, 23 ASNs, 1,407 Gbps cumulative member port speeds, including Orange RDC, Airtel DRC, Africell, GBS, Microcom, Orioncom and United. **Grade B+ for interconnection ecosystem; not facility proof.**
- **Africa Data Centres Association members**: https://africadca.org/en/members . Use for pan-African operator names such as Raxio and other possible entrants. **Grade B.**

---

## 2. Cloud regions and cloud-on-ramp checks

Use cloud-region pages only as **negative/positive controls** for hyperscale self-builds. Do not infer a DRC physical facility from "DRC cloud service" marketing unless the provider names a local datacenter.

| Provider | Official region source | DRC finding |
|---|---|---|
| AWS | https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | No DRC region. Africa listed as `af-south-1` Africa (Cape Town), South Africa. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list | No DRC region. South Africa North/West are the relevant Africa regions. |
| Google Cloud | https://docs.cloud.google.com/compute/docs/regions-zones | No DRC region. `africa-south1-a/b/c` are Johannesburg, South Africa. |
| Oracle Cloud Infrastructure | https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm | No DRC region. `af-johannesburg-1` is South Africa Central. |

Query cloud/on-ramp leads:
```
"Kinshasa" ("cloud on-ramp" OR "Direct Connect" OR "ExpressRoute" OR "Cloud Interconnect" OR "FastConnect")
"RDC" ("AWS" OR "Azure" OR "Google Cloud" OR "Oracle Cloud") ("data center" OR datacenter OR "centre de données")
"OADC Texaf" ("cloud" OR "on-ramp" OR "plateformes cloud")
"Raxio DRC1" ("cloud" OR CDN OR "content" OR "interconnect")
```

---

## 3. Trade press, associations, and directories

### 3.1 High-value recurring sources

- **Data Center Dynamics (DCD)** country tag and article search: https://www.datacenterdynamics.com/en/news/?tag=democratic-republic-of-the-congo . **Grade B**; strong for launch dates and capacity claims, usually based on operator statements.
- **Connecting Africa**: search for DRC, OADC, Raxio, Kinshasa. **Grade B**; good telecom/datacenter launch coverage.
- **Developing Telecoms**: search for DRC + Raxio/OADC/Fastnet. **Grade B**.
- **Ecofin Agency / Agence Ecofin**: good Francophone telecom infrastructure coverage. **Grade B**.
- **Actualite.cd, Radio Okapi, Zoom Eco, DeskEco, MediaCongo, CIO Mag**: useful local French-language signals for official ceremonies, procurement, and government digital policy. **B/C depending on whether they cite a named operator, ministry, tender, or only quote political claims.**
- **Console Connect Africa Interconnection Report 2025**: https://info.consoleconnect.com/africa-interconnection-report-2025 . **Grade B**. It flags Kinshasa's two recent data centers, about 20 carriers, KINIX, and local IXPs in Goma and Lubumbashi. Use as a lead source, not final facility proof.
- **D4D Hub / Xalam DRC Data Center Market Briefing**: https://cms.d4dhub.eu/assets/Initiatives/Data-Governance-in-Africa/Digital-Investment-Facility/2507_Country-Market-Briefs/Data-Center-Market-Brief-Democratic-Republic-of-Congo.pdf . **Grade B** market context; use sparingly for market size and risk framing, not individual facility attribution unless corroborated.

### 3.2 Directory sources: use as leads only

- DataCenterMap: https://www.datacentermap.com/dr-congo/kinshasa/
- Datacenters.com DRC/Kinshasa/Lubumbashi pages.
- Inflect Kinshasa pages.
- Baxtel facility pages.
- DC Hub facility pages.

These sources are **C** unless they quote an operator source. They are useful for addresses and alias discovery, but they can duplicate POPs, hosting offices, or stale facilities. Always pivot to operator pages, ARPTC, PeeringDB, launch coverage, or customer references.

---

## 4. Search language and query patterns

### 4.1 Core French/English vocabulary

Use both DRC/RDC, Congo-Kinshasa, province names, and city names.

```
("RDC" OR "République démocratique du Congo" OR "DR Congo" OR "Congo Kinshasa") ("data center" OR datacenter OR "centre de données" OR "centre informatique")
("RDC" OR "DRC") ("colocation" OR "hébergement datacenter" OR "hébergement serveur" OR "salle blanche" OR "white space")
("RDC" OR "DRC") ("Tier III" OR "Tier 3" OR "Tier-III" OR "Uptime Institute")
("RDC" OR "DRC") ("cloud souverain" OR "souveraineté numérique" OR "coffre-fort numérique")
("RDC" OR "DRC") ("point d'échange Internet" OR IXP OR KINIX OR "Goma IXP" OR "Lubumbashi IXP")
```

### 4.2 Vendor pivots

```
"Raxio DRC1" OR "Raxio Kinshasa" (MW OR racks OR Limete OR Tier)
"OADC Texaf" OR "OADC Kinshasa" (MW OR racks OR Silikin OR TEXAF OR Tier)
"Fastnet" "Lubumbashi" ("data center" OR datacenter OR "centre de données" OR racks)
"Orange RDC" ("datacenter" OR "centre de données" OR "hébergement")
"Global Broadband Solution" OR GBS ("datacenter" OR "data center" OR Kinshasa OR Lubumbashi)
"United" OR "UNITED S.A." ("datacenter" OR "data center" OR "hébergement" OR Kinshasa)
site:arptc-solution.cd (datacenter OR "centre de données" OR "fournisseur d'accès")
site:peeringdb.com Kinshasa KINIX datacenter
```

### 4.3 Government/procurement pivots

```
site:presidence.cd ("Plan National du Numérique" OR "centre de données" OR datacenter)
site:adn.cd ("datacenter" OR "centre de données" OR "cloud souverain" OR "appel d'offres")
site:numerique.gouv.cd ("centre de données" OR datacenter OR "cloud souverain")
site:arptc.gouv.cd OR site:arptc-solution.cd ("opérateurs" OR "fournisseurs d'accès" OR datacenter)
site:mediacongo.net ("centre des données" OR datacenter OR "cloud souverain") ("appel d'offres" OR attribution)
"RDC" "Fourniture d'équipements de centre des données" "Cloud souverain"
```

Procurement portals are fragmented. `armp-rdc.org` may be unreliable or compromised in search results; use it only after opening and validating the page. Practical procurement leads often surface through MediaCongo, dgMarket/AFD buyer pages, World Bank notices, and ministry/ADN postings.

---

## 5. Province-by-province enumeration pattern

For every province, search both the province name and the main city. Add local French names where they differ from the manifest English name. Default query:

```
("{province_fr}" OR "{province_en}" OR "{city}") ("datacenter" OR "data center" OR "centre de données" OR "centre informatique" OR "salle serveurs" OR "cloud souverain" OR colocation OR "hébergement serveur")
("{city}") ("fibre optique" OR backbone OR "ring urbain" OR IXP OR "point d'échange Internet") ("datacenter" OR "centre de données")
("{operator}") ("{city}" OR "{province_fr}") ("datacenter" OR colocation OR hébergement OR "point de présence" OR POP)
```

| Manifest division | French/local terms and city pivots | Enumeration priority |
|---|---|---|
| Central Kongo | Kongo Central, Bas-Congo, Matadi, Moanda, Boma | **High**: Moanda is a PNN datacenter target and subsea-cable landing area. Search WACS, 2Africa, SCPT, Orange, Airtel, landing station, "station d'atterrissement", "centre de données Moanda". |
| Lower Uele | Bas-Uele, Buta | Low: broad web/local press; expect no commercial DC unless government/NGO edge facility. |
| Equator | Equateur, Mbandaka | Low/medium: search provincial government and Mbandaka telecom POP/hosting. |
| Upper Katanga | Haut-Katanga, Lubumbashi | **High**: verified Fastnet facility; mining-economy demand; PNN target city; local IXP signal. Search Fastnet, GBS, Liquid, Vodacom, Orange, "ESNAP", "Lubumbashi IXP", universities/HPC. |
| Upper Lomami | Haut-Lomami, Kamina | Low: search Kamina plus telco POP/VSAT/backbone. |
| Upper Uele | Haut-Uele, Isiro | Low: search Isiro plus telco/government digital-service terms. |
| Ituri | Bunia, Ituri | Medium: conflict/humanitarian telecom may create edge rooms, but avoid counting NGO server rooms as colocation. Search Bunia + fibre/IXP/datacenter. |
| Central Kasai | Kasaï-Central, Kasai Central, Kananga | Low/medium: search Kananga + "centre de données" and government modernization. |
| Eastern Kasai | Kasaï-Oriental, Kasai Oriental, Mbuji-Mayi | Medium: mining/economic city; search Mbuji-Mayi + GBS/Orange/Vodacom/Fastnet. |
| Kwango | Kenge, Kwango | Low. |
| Kwilu | Kikwit, Bandundu, Kwilu | Low/medium: Kikwit and Bandundu city pivots. |
| Kinshasa | Kinshasa, Gombe, Limete, Silikin Village, TEXAF | **Very high**: enumerate Raxio, OADC, Orange, GBS, United, Orioncom/Microcom/Afrinet, KINIX, cloud/CDN nodes. Address-level dedupe is required. |
| Kasai | Kasaï, Tshikapa | Low/medium: search Tshikapa + mining/telecom/hosting. |
| Lomami | Kabinda, Lomami | Low. |
| Lualaba | Kolwezi, Lualaba | **Medium/high**: mining demand; search Kolwezi + operator names, fibre, private cloud, datacenter, "salle serveur". Do not confuse mine/company internal IT rooms with commercial DCs. |
| Maniema | Kindu, Maniema | Low. |
| Mai-Ndombe | Mai Ndombe, Inongo | Low. |
| Mongala | Lisala, Mongala | Low. |
| North Kivu | Nord-Kivu, Goma | **High for planned/edge**: PNN target city and local IXP signal. Search Goma + IXP, "ring urbain", Raxio/OADC expansion, government/ADN, humanitarian cloud rooms. Verify security/status carefully. |
| North Ubangi | Nord-Ubangi, Gbadolite | Low. |
| Sankuru | Lusambo, Sankuru | Low. |
| South Kivu | Sud-Kivu, Bukavu | Medium: search Bukavu + telco POP/cloud/IXP; check university/NGO institutional facilities but grade conservatively. |
| South Ubangi | Sud-Ubangi, Gemena | Low. |
| Tanganyika | Kalemie, Tanganyika | Medium: port/corridor city; search Kalemie plus backbone/fibre/hosting. |
| Tshopo | Kisangani, Tshopo | **High for planned**: PNN target city. Search Kisangani + "centre de données", "ring urbain", SCPT, Liquid, Orange, Vodacom. |
| Tshuapa | Boende, Tshuapa | Low. |

---

## 6. Verification rules and pitfalls

1. **Count facilities, not offices or POPs.** DRC directories often describe offices, POPs, hosting services, or telecom switch sites as datacenters. Require explicit facility language: racks, white space, IT load/MW, Tier certification, colocation, datacenter address, or launch/inauguration.
2. **Use ARPTC as an operator census only.** A company on the ARPTC ISP/MNO list is a valid lead, not a datacenter record.
3. **Use IXPs as adjacency evidence.** KINIX and any Goma/Lubumbashi IXP signal are excellent interconnection leads, but an IXP may be hosted inside a telco room, neutral colo, university, or association site.
4. **Separate PNN target from execution.** PNN target cities are a province-query map. Treat "planned national datacenter", "cloud souverain", and "coffre-fort numérique" as planned/announced until a tender, contract, site, build, or launch is found.
5. **Beware Congo ambiguity.** Search results for "Congo data center" often mix DRC (CD, Kinshasa/Lubumbashi/Goma/Moanda/Kisangani) with Republic of Congo (CG, Brazzaville/Pointe-Noire). Never assign Brazzaville or Pointe-Noire facilities to CD.
6. **Capacity hierarchy:** operator official MW/racks or certified datasheet = A; trade article quoting operator = B; directory MW/rack number = C until corroborated.
7. **Status hierarchy:** operational/launch/inauguration + operator page > under construction/groundbreaking > procurement/contract award > PNN strategy or political announcement.

---

## 7. Suggested workflow

1. Seed Kinshasa from Raxio, OADC, Orange, GBS, United, KINIX members, and datacenter directories; dedupe by address and operator.
2. Seed Lubumbashi from Fastnet and search every ARPTC/KINIX operator name against Lubumbashi and Haut-Katanga.
3. Sweep the PNN target cities: Goma, Moanda, Kisangani, Kinshasa, Lubumbashi.
4. Run the province table queries for all 26 provinces using French/local names first, then English names.
5. For each hit, assign evidence grade per source and record why a non-Kinshasa item is or is not a real datacenter.
6. Recheck official cloud region pages before recording any hyperscale claim; current public evidence supports no DRC hyperscale region.

