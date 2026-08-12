# FJ Explorer Official - Fiji Datacenter Enumeration via Official and Regulatory Sources

Date: 2026-08-12. Scope: Fiji (FJ), all 5 divisions/dependency from `world-manifest.jsonl`: Central, Eastern, Northern, Rotuma, Western. Angle: government, regulator, official operator, cable, registry, energy, and official cloud-region checks for datacenter and datacenter-adjacent infrastructure.

Reliability grades used by this explorer: **A** = primary government, regulator, state-owned/public operator, utility, company registry, official provider page, official filing, official tender, or official multilateral document; **B** = reputable local/regional/trade press with named parties and dates; **C** = directory, marketplace, social repost, SEO hosting page, cable map/database, or unattributed aggregate. Grade C may start a lead or support a negative-control note, but it must not establish a facility.

## 0. Verified Baseline

- Fiji has exactly 5 manifest divisions/dependency for this workflow: **Central**, **Eastern**, **Northern**, **Rotuma**, and **Western**.
- Fiji is a small but real Pacific datacenter market. The recordable official signals are: Telecom Fiji Limited (TFL) data-centre/colocation services; Vodafone Fiji's Fiji-based hosted cloud service; FINTEL's Vatuwaqa Communications Centre (VCC) cable landing and LEO/satellite colocation environment; Google's Natadola ICT facility and second Viti Levu cable landing station; and TFL's proposed NextGen Data Centre.
- Do not treat every telecom exchange, cable landing station, office, retail shop, ISP POP, `.fj` host, CDN edge, VPN endpoint, or offshore VPS landing page as a datacenter. Classify each candidate before recording it.
- Cable landing stations are `cable_landing_station` assets unless the source explicitly supports colocation, hosting, cloud, or datacenter-like equipment housing. FINTEL's VCC is datacenter-adjacent because FINTEL says it offers LEO Earth Station / Satellite Access Point colocation with power, cooling, and backhaul.
- Google's Natadola facility is a hyperscaler ICT/cable facility, not a Fiji Google Cloud public region. The Fijian Government release supports groundbreaking and scope, but not operational commissioning. Keep it `under_construction` or `near_completion_unverified` unless Google, the Fijian Government, FINTEL, or another primary source confirms service.
- No AWS, Microsoft Azure, Google Cloud, or Oracle Cloud public cloud region/local zone in Fiji was found on official region pages checked on 2026-08-12.
- English is sufficient for Fiji official-source discovery. Use Fijian/Hindi terms only for place-name normalization when a local source uses them.

## 1. Official Sources To Check First

### 1.1 Fiji Government, PM Office, Digital Government, and Statistics

Primary sources:

- Fiji Government portal: https://www.fiji.gov.fj/
- Fiji Government Google ICT facility release: https://www.fiji.gov.fj/google-ict-facility-to-usher-in-a-new-era-of-digital-connectivity/
- Prime Minister's Office: https://www.pmoffice.gov.fj/
- PM Office Google release mirror: https://www.pmoffice.gov.fj/google-ict-facility-to-usher-in-new-era-of-digital-connectivity/
- PM Office South Pacific Connect announcement: https://www.pmoffice.gov.fj/27-10-23/
- Fiji Bureau of Statistics: https://www.statsfiji.gov.fj/
- Fiji electricity statistics: https://www.statsfiji.gov.fj/electricity-2024/
- Fiji energy accounts: https://www.statsfiji.gov.fj/fijis-experimental-environmental-account-for-energy-2024/

Verified use:

- The Fiji Government release dated 30 Nov 2024 is Grade A for the Google Natadola facility's scope: a new cable landing station, data transmission servers/racks, and power generating equipment for Google's international fibre optic cables; it also places the project at Natadola in the Western Division and says it is Viti Levu's second cable landing station, complementing the Central Division landing.
- PM Office material is Grade A for the national Google subsea-cable partnership and planned physically diverse Fiji landing stations. It does not by itself prove an operating public cloud region.
- Fiji Bureau of Statistics and energy accounts are Grade A for national power/electricity context, not for facility existence.
- Government server rooms in Suva are plausible, but do not record a government datacenter without procurement, budget, project, or facility evidence.

Government query templates:

```text
site:fiji.gov.fj ("data centre" OR "data center" OR datacenter OR colocation)
site:fiji.gov.fj Google Natadola ("ICT facility" OR "cable landing station")
site:fiji.gov.fj ("submarine cable" OR Tabua OR Bulikula OR Honomoana)
site:fiji.gov.fj ("DigitalFIJI" OR "Digital Fiji" OR "digital transformation")
site:fiji.gov.fj ("server room" OR "data storage" OR "government cloud")
site:pmoffice.gov.fj Google Fiji ("subsea cable" OR "cable landing")
site:statsfiji.gov.fj (electricity OR energy OR EFL)
```

### 1.2 Telecommunications Authority of Fiji (TAF)

Primary sources:

- TAF home: https://taf.org.fj/
- TAF history / role: https://taf.org.fj/history-of-telecommunications-authority-of-fiji/
- Licensing and regulatory page: https://taf.org.fj/licensing-regulatory/
- Types of licences: https://taf.org.fj/licensing-regulatory/types-of-licenses/
- Equipment type approval: https://taf.org.fj/equipment-type-approval/
- Import permit procedure: https://taf.org.fj/import-permit/
- Fees and charges: https://taf.org.fj/fees-charges-schedule/

Verified use:

- TAF is Grade A for telecom licensing, import permits, equipment type approval, spectrum and network-regulatory context.
- TAF is not a public datacenter registry. A telecom licence or equipment approval supports operator/equipment authorization, not a datacenter facility.
- Use TAF to validate operators behind hosting/cloud/cable leads and to identify telecom license classes; then require facility-specific evidence from the operator, registry, utility, tender, or government source.

TAF query templates:

```text
site:taf.org.fj ("data centre" OR "data center" OR datacenter OR hosting OR colocation)
site:taf.org.fj (licensee OR "telecommunications license" OR "network license")
site:taf.org.fj (Google OR Natadola OR "cable landing")
"Telecommunications Authority of Fiji" ("data centre" OR "data center" OR hosting)
"Telecommunications Act 2008" Fiji ("data centre" OR cloud OR hosting)
```

### 1.3 Official Telecom and ICT Operators

Primary sources:

- Telecom Fiji Limited (TFL): https://www.telecom.com.fj/
- TFL ICT Solutions: https://www.telecom.com.fj/business/ict-solutions/
- TFL-Google Vatuwaqa-to-Natadola terrestrial fibre release: https://www.telecom.com.fj/telecom-fiji-knowledge/telecom-fiji-and-google-announce-strategic-agreement-to-deliver-terrestrial-fiber-link-in-fiji/
- TFL TenderLink portal: https://www.tenderlink.com/tfl and https://portal.tenderlink.com/tfl/alltenders/
- Vodafone Fiji IaaS / Vodafone Hosted Cloud: https://www.vodafone.com.fj/business/products-services/ict-cloud-solutions/infrustructure-as-a-service
- Digicel Fiji: verify current official Fiji business pages before using as a datacenter lead.

Verified use:

- TFL's ICT Solutions page is Grade A that TFL offers cloud services, co-location services for disaster recovery, data centres, and hosted PABX. It does not disclose address, racks, MW, tier, or exact operational site. Directory claims that place the TFL data centre in Suva remain Grade C unless corroborated by TFL or another primary source.
- TFL's 9 Jun 2025 release is Grade A for the Vatuwaqa-to-Natadola terrestrial fibre route and confirms the two anchor endpoints: FINTEL's Vatuwaqa international cable landing station and Google's Natadola ICT facility. This is fibre/cable infrastructure evidence, not proof that Natadola is operational.
- TFL's NextGen Data Centre EOI appears in official TFL social/TenderLink references and is Grade A for EOI existence when the post or tender page is preserved; Fiji Times reporting is Grade B for the plan that construction would take about 24 months beginning in 2026. If the tender portal no longer lists the closed EOI, note it as closed/unavailable rather than dead.
- Vodafone Fiji's IaaS page is Grade A for a Fiji-based hosted cloud service connected to Vodafone IPVPN. It supports an operator-hosted cloud lead, but it does not disclose the physical data-centre site, capacity, or whether the facility is Central or Western.
- No primary Digicel Fiji datacenter page was verified in this pass; keep Digicel as telecom/network POP lead only.

Operator query templates:

```text
site:telecom.com.fj ("data centre" OR "data center" OR datacenter OR colocation OR "co-location")
site:telecom.com.fj ("NextGen" OR "Next Gen" OR "data centre" OR tender OR EOI)
site:telecom.com.fj Google Natadola Vatuwaqa (fibre OR fiber)
site:vodafone.com.fj ("data centre" OR "data center" OR "Vodafone Cloud" OR IaaS OR "Fiji based")
"Vodafone Fiji" ("data centre" OR "hosted cloud" OR "secure data")
"Digicel Fiji" ("data centre" OR "data center" OR hosting OR "server room")
"Amalgamated Telecom Holdings" Fiji ("data centre" OR "data center")
```

### 1.4 FINTEL, Google, and Cable Landing Infrastructure

Primary sources:

- FINTEL facilities: https://fintel.com.fj/our-facilities/
- FINTEL about: https://fintel.com.fj/about-us/
- Google South Pacific Connect / Honomoana and Tabua blog: https://cloud.google.com/blog/products/infrastructure/honomoana-and-tabua-subsea-cables-connect-south-pacific
- Google Central Pacific Connect / Bulikula and Halaihai blog: https://cloud.google.com/blog/products/infrastructure/introducing-bulikula-and-halaihai-subsea-cables-to-connect-the-central-pacific
- Samoa Submarine Cable Company (Tui-Samoa): https://www.ssccsamoa.com/
- Southern Cross Cable Network: https://www.southerncrosscables.com/

Verified use:

- FINTEL states its engineering facilities are at Vatuwaqa Communications Centre (VCC) and that it is Fiji's international gateway and cable landing station operator. This is Grade A for VCC and its cable/telecom role.
- FINTEL lists major cable systems including Southern Cross Cable Network, Tonga Cable, Interchange Cable Network, Southern Cross NEXT, Tui-Samoa, Gondwana 2, and Google Tabua/Bulikula. Use FINTEL for Fiji landing evidence; use cable owners for RFS/technical dates where available.
- FINTEL explicitly offers colocation services for LEO Earth Stations and Satellite Access Point farms at VCC, with secure facilities, uninterrupted power, cooling, and high-capacity backhaul. Record this as `leo_ground_station_colocation` or `colo_adjacent_telecom`, not general commercial colocation unless FINTEL publishes a broader colocation product.
- Google official blogs are Grade A for the South Pacific/Central Pacific cable initiatives and partner names. They do not prove a Fiji public cloud region or a commissioned datacenter.
- SSCC is Grade A for Tui-Samoa landing points including Suva and Savusavu; if FINTEL and cable databases disagree on RFS year, cite the exact source and date rather than resolving by assumption.

Cable query templates:

```text
site:fintel.com.fj ("Vatuwaqa" OR "cable landing" OR colocation OR LEO OR Starlink OR OneWeb)
site:fintel.com.fj (Tabua OR Bulikula OR "Southern Cross" OR "Tui Samoa" OR Gondwana)
site:cloud.google.com/blog/products/infrastructure Fiji (Tabua OR Bulikula OR Honomoana OR Halaihai)
site:ssccsamoa.com (Suva OR Savusavu OR "Tui-Samoa" OR "Tui Samoa")
site:southerncrosscables.com (Fiji OR Suva OR Savusavu)
FINTEL ("data centre" OR "data center" OR colocation OR "ground station")
```

### 1.5 Registry, Investment, Land, and Business Checks

Primary sources:

- Registrar of Companies ROC Public: https://roc.digital.gov.fj/
- ROC public entity search: https://roc.digital.gov.fj/BuyInformation/Search
- businessNOW: https://www.businessnow.gov.fj/
- Investment Fiji: https://www.investmentfiji.org.fj/

Verified use:

- ROC Public is Grade A for Fiji entity existence, registration details, and foreign-company/business-name records when the entity result is directly retrieved. It may require form search or a valid email to purchase detailed information.
- Investment Fiji and businessNOW are Grade A for investment and registration process context, but not facility evidence unless they name a project/entity.
- Press reports about Staghorn Services Pte Ltd, Natadola Bay Resort Ltd, FNPF, or iTaukei Land Trust Board lease assignments remain Grade B until confirmed through ROC, land registry, iTLTB, or project filings.

Registry query templates:

```text
site:investmentfiji.org.fj ("data centre" OR "data center" OR ICT OR digital OR telecommunications)
site:businessnow.gov.fj ("data centre" OR "data center" OR telecommunications OR ICT)
"Staghorn Services" Fiji (ROC OR "Registrar of Companies" OR Natadola)
"Natadola Bay Resort" (Google OR "data centre" OR "data center")
"iTaukei Land Trust Board" Natadola Google ("data centre" OR "data center")
```

### 1.6 Energy, Water, and Major Load Checks

Primary sources:

- Energy Fiji Limited (EFL): https://efl.com.fj/
- EFL annual reports and outage/network pages under https://efl.com.fj/
- Fiji Bureau of Statistics electricity/energy pages listed above
- Water Authority of Fiji: verify current official URL before citing project-specific water evidence.

Verified use:

- EFL is Grade A for utility context and grid/outage/electricity information. It is not facility evidence unless a page, connection notice, tariff, substation project, annual report, or interconnection document names a datacenter or site.
- No Grade A EFL or WAF source was verified for Google Natadola power/water arrangements in this pass. Treat power and water as open verification items.
- For TFL NextGen and Google Natadola, do not infer MW from investment value, cable bandwidth, generation capacity, or Fiji grid statistics.

Energy query templates:

```text
site:efl.com.fj ("data centre" OR "data center" OR Google OR Natadola OR "large customer")
site:efl.com.fj substation (Natadola OR Vatuwaqa OR Nadi OR Lautoka)
"Energy Fiji Limited" Google Natadola (power OR electricity OR substation)
"Water Authority of Fiji" Google Natadola ("data centre" OR "data center" OR water)
site:statsfiji.gov.fj electricity EFL (industrial OR commercial)
```

### 1.7 Official Cloud Region Absence Checks

Use only official provider pages for cloud-region status. Absence of Fiji in these lists means do not create a Fiji public cloud region from reseller, local hosting, cable, CDN, or marketing claims.

| Provider | Official source | Fiji result checked 2026-08-12 |
|---|---|---|
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ and https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | No Fiji AWS Region or Local Zone found. |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list and https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies | No Fiji Azure public region found. |
| Google Cloud | https://cloud.google.com/about/locations and https://docs.cloud.google.com/compute/docs/regions-zones | No Fiji Google Cloud public region found; Natadola is cable/ICT infrastructure. |
| Oracle Cloud Infrastructure | https://docs.oracle.com/iaas/Content/General/Concepts/regions.htm and https://www.oracle.com/cloud/public-cloud-regions/ | No Fiji OCI public cloud region found. |

## 2. Division Coverage Matrix

Run the universal block for all five divisions/dependency. A negative result still counts as coverage when the search route and reason are recorded.

| Division | Coverage status | Expected official yield |
|---|---:|---|
| Central | Covered | Highest yield. Suva/Vatuwaqa: FINTEL VCC, TFL official ICT services, Vodafone cloud/service infrastructure, government ICT, TAF/ROC, banks and institutions. Validate all commercial-DC claims here first. |
| Eastern | Covered | Low yield. Ovalau/Levuka, Kadavu, Lau, Lomaiviti. Expect government connectivity, telecom access, satellite/maritime links, and public-service ICT, not named datacenters. |
| Northern | Covered | Low/medium yield. Vanua Levu: Savusavu cable spur evidence, Labasa telecom/fibre leads, EFL regional grid context. Cable infrastructure is not commercial DC. |
| Rotuma | Covered | Very low yield. Remote dependency; expect satellite/backhaul, telecom service, and government connectivity references only. Record negative coverage explicitly. |
| Western | Covered | High yield. Natadola/Nadroga for Google ICT facility; Nadi/Lautoka/Denarau/Sigatoka for telecom, airport/tourism, Vodafone/TFL network, and possible future TFL NextGen siting. |

Universal division query block:

```text
"{division}" Fiji ("data centre" OR "data center" OR datacenter)
"{division}" Fiji ("server room" OR server OR hosting OR colocation)
"{division}" Fiji ("cable landing" OR "submarine cable" OR fiber OR fibre OR "landing station")
"{division}" Fiji (telecom OR telecommunications OR internet OR ICT OR EFL OR power)
site:fiji.gov.fj "{division}" (ICT OR data OR communications OR cable)
```

High-yield locality variants:

```text
(Suva OR Vatuwaqa) Fiji FINTEL ("cable landing" OR "data centre" OR colocation)
Suva Fiji "Telecom Fiji" ("data centre" OR colocation OR hosting)
(Natadola OR Sigatoka OR Nadroga) Fiji Google ("ICT facility" OR "data centre" OR "landing station")
(Nadi OR Lautoka OR Denarau) Fiji ("data centre" OR server OR Vodafone OR 5G OR fibre)
(Savusavu OR Labasa OR "Vanua Levu") Fiji (cable OR landing OR fibre OR "Telecom Fiji")
Rotuma Fiji (satellite OR internet OR telecom OR backhaul)
(Levuka OR Ovalau OR Kadavu OR Lau) Fiji (internet OR satellite OR telecom)
```

## 3. Enumeration Workflow

1. Confirm the manifest divisions: Central, Eastern, Northern, Rotuma, Western.
2. Start with Grade A national sources: Fiji Government/PM Office, TAF, TFL, Vodafone Fiji, FINTEL, Google blogs, ROC/businessNOW/Investment Fiji, EFL, and Stats Fiji.
3. Classify every lead as `commercial_colocation`, `operator_hosted_cloud`, `operator_internal_datacentre`, `hyperscaler_ict_facility`, `cable_landing_station`, `leo_ground_station_colocation`, `government_server_room`, `telecom_pop`, `office_only`, or `seo_false_positive` before assigning datacenter status.
4. Require source-to-claim matching. A Grade A source for a project may only support the attributes it states: e.g., fiji.gov.fj proves Natadola scope/groundbreaking, not operational commissioning; TFL proves data-centre/colocation service existence, not capacity.
5. Use ROC, businessNOW, Investment Fiji, land/iTLTB records, EFL, and WAF to verify announced projects when press names entities, leases, utilities, or foreign investment.
6. Search all 5 divisions and record negative/low-yield coverage. Eastern and Rotuma should be marked searched, not skipped.
7. Check official cloud-region pages as a separate negative-control step.
8. Record capacity only from stated IT load, racks, floor area, tier certification, or named facility specs. Never convert cable bandwidth, project value, or grid generation into datacenter MW.

## 4. Current Facility and Project Seeds

Re-check each seed before inventory use.

| Seed | Division | Type | Conservative status as of 2026-08-12 | Best evidence | Reliability |
|---|---|---|---|---|---|
| Telecom Fiji data-centre / colocation services | Central likely; exact site not official | Commercial colocation / operator data centre service | Operational service; address/capacity undisclosed | TFL ICT Solutions | A for service; C for directory locality |
| Vodafone Fiji Hosted Cloud / IaaS | Not disclosed; Fiji-based | Operator hosted cloud / internal DC lead | Operational Fiji-based cloud service; physical site/capacity undisclosed | Vodafone IaaS page | A for service; location beyond Fiji unverified |
| FINTEL Vatuwaqa Communications Centre | Central (Suva/Vatuwaqa) | Cable landing station + LEO/SAP colocation | Operational cable hub and LEO/satellite colocation environment | FINTEL facilities | A |
| Southern Cross / Tui-Samoa / other Fiji cable landings | Central; Northern for Savusavu spur | Cable landing stations | Operational telecom infrastructure; not commercial DC | FINTEL, SSCC, cable owners/databases | A/B depending source |
| Google Natadola ICT facility | Western (Natadola, Nadroga) | Hyperscaler ICT facility + cable landing station | Under construction / commissioning unverified | Fiji Government release; PM Office; Google blogs; TFL fibre release | A for scope; no Grade A operational proof |
| Google Tabua / Bulikula / related cable systems | Central and Western landings | Subsea cable systems | Cable infrastructure; verify RFS/commissioning per system | Google blogs; FINTEL; cable sources | A/B |
| TFL NextGen Data Centre | Site not disclosed | Proposed commercial data centre | Proposed / EOI stage; site/capacity not public | TFL official social/TenderLink reference; Fiji Times | A for EOI if source preserved; B for schedule |
| Digicel Fiji | National | Telecom POP/server-room lead | No public DC evidence verified | Digicel/TAF searches | Lead only |
| Government / DigitalFIJI server rooms | Central likely | Government server-room lead | Plausible but not recordable without named project/procurement | Fiji Government/ICT searches | Lead only |

## 5. Reliability Pitfalls

- Do not upgrade Natadola to operational from "near completion" or cable-landing press. Wait for a Grade A commissioning or service source.
- Do not label Natadola a GCP region; official Google Cloud location pages do not list Fiji.
- Do not assign Suva to Vodafone or TFL physical sites unless the source says so. TFL's official page proves services; directory sites may only be C-grade locality leads.
- Do not turn FINTEL VCC into general-purpose colocation unless FINTEL publishes a broader service. Its explicit colocation evidence is for LEO Earth Stations and Satellite Access Point farms.
- Do not resolve conflicting cable RFS dates by preference. Record the exact source and date.
- Do not use investment values (FJ$200M, US$250M, etc.) as capacity. Keep conflicting figures source-specific.
- Watch locality: Suva/Vatuwaqa = Central; Savusavu/Labasa = Northern; Natadola/Nadi/Lautoka/Sigatoka/Denarau = Western; Rotuma is separate.

## 6. Expected Outcome

A final Fiji enumeration should be small and clearly tiered: TFL's official data-centre/colocation service, Vodafone Fiji's Fiji-based hosted cloud lead, FINTEL VCC and its LEO/SAP colocation environment, operational cable landing infrastructure at Vatuwaqa and Savusavu, Google's Natadola ICT/cable facility as under-construction unless commissioned by Grade A evidence, and TFL NextGen as proposed/EOI-stage. Eastern and Rotuma are expected to be negative or access-network-only, but both must be searched and recorded as covered.
