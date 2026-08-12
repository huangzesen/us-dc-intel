# RS Explorer Industry - Serbia Datacenter Enumeration via Colo Operators, Cloud Regions, Trade Press, Associations, and District Query Patterns

Date: 2026-08-12. Country: **RS Serbia**. Scope: **industry / vendor / trade-press methodology** for enumerating datacenters, colocation, cloud-region infrastructure, telecom facilities, government/sovereign cloud campuses, and secondary regional data-center leads across Serbia's manifest divisions. Reliability grades: **A** = official/operator/regulator/cloud-provider/primary source; **B** = strong trade press, vendor case study, or maintained interconnection database; **C** = directory, marketplace, weak aggregator, SEO article, or unconfirmed local press lead.

---

## 0. Serbia-specific market frame

- Serbia is a **three-cluster market** for enumeration:
  - **Belgrade**: commercial colo, interconnection, telecom, managed hosting, and private cloud. Core seeds: CETIN, Telekom Srbija/MTS, Orion Telekom, SBB Telepark/Yettel, phoenixNAP, NetCast, BeotelNet, BeeNet RS-1, Absolut Solutions, and SOX/PeeringDB facilities.
  - **Kragujevac / Sumadija**: national state data-center campus, Government Cloud, Oracle Cloud Jovanovac region, IBM/Huawei/CERN hosting, national AI/supercomputer infrastructure, and planned hyperscale-ready expansion with e& enterprise.
  - **Vojvodina and southern Serbia**: Vrsac green/DC disaster-recovery facilities, Novi Sad cloud/hosting, Niš NiNet colo and a planned state-backed digital hub/data-center lead.
- Serbian-language search is mandatory. Operators and local press use `data centar`, `data-centar`, `kolokacija`, `telehousing`, `server housing`, `hosting`, `virtuelni privatni data centar`, `državni data centar`, `računarski centar`, `serverska sala`, and `centar za obradu podataka`. Cyrillic forms matter for local government and older press: `дата центар`, `дата-центар`, `државни дата центар`, `сервер сала`, `рачунарски центар`, `центар за обраду података`.
- Do not count every cloud or VPN product as a physical datacenter. Promote only when the source names a facility, address/locality, campus, data-center service, facility record, or official cloud region. `Virtual Data Center`, `VPS`, `cloud hosting`, `AWS/GCP/Azure connectivity`, and CDN/IX presence are leads until tied to a named facility.
- Kosovo-Metohija is present in the manifest. Treat the source territory carefully: many sources identify facilities as Kosovo/Pristina/Fushe Kosove rather than Serbia. Preserve source wording and flag jurisdictional ambiguity in notes.

---

## 1. Industry, operator, and directory source surfaces

### 1.1 Primary / high-confidence operator and regulator sources

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| RATEL data-center notification/list | https://www.ratel.rs/en/obavestenje-o-obavljanju-delatnosti-elektronskix-komunikacija | Serbia's regulator explicitly invites legal entities owning a DATA center to submit data and publishes a `List of Data Centers`. Use as the first national registry-style cross-check. | A |
| RATEL electronic communications operators database | https://ratel.itcentar.rs/en/page/operators-of-electronic-communications | Verify telecom/operator legal names and service registrations before promoting small ISP/datacenter claims. | A |
| Office for IT and eGovernment | https://www.ite.gov.rs/tekst/en/34/government-data-centre-in-kragujevac.php and https://www.ite.gov.rs/tekst/en/24/government-data-center.php | Primary source for Belgrade state DC, Kragujevac Government Data Centre, Government Cloud, Oracle/IBM/Huawei/CERN references, capacity and expansion claims. | A |
| CETIN Serbia | https://www.cetin.rs/services/data-center | Official Belgrade carrier-neutral datacenter/service page; use for existence and services. Address corroboration: https://www.cetin.rs/services and https://www.cetin.rs/about-us/our-office. | A |
| Telekom Srbija / MTS | https://mts.rs/Poslovni/Digital/Data-centar | Official data-center services page; combine with directories/PeeringDB for address/capacity. | A/B |
| Orion Telekom | https://oriontelekom.rs/telehousing/ and https://oriontelekom.rs/orion-telekom-launches-a-sovereign-ai-factory/ | Official Belgrade data-center / telehousing / high-density AI Factory source. Use Serbian pages for latest product language. | A |
| NetCast | https://netcast.rs/data-centar/ and https://netcast.rs/cloud/ | Official Belgrade data-center/cloud source; confirms own professional data center and service classes. | A |
| BeeNet | https://www.beenet.rs/en/data-center | Official operator source for RS-1 Belgrade, RS-2 Vrsac, and MNE-1 Podgorica. Extract only Serbia sites under RS. | A |
| ZELEN DATA CENTAR / HiTeam / E-Smart Systems | https://www.zelendata.rs/eng/zelendata-centar , https://www.hiteam.co.rs/eng/vest/18/hiteam-opened-the-first-green-data-center-in-serbia , https://e-smartsys.com/en/zelendata-centar/ | Official/partner sources for Vrsac green datacenter in Technology Park. | A/B |
| NiNet | https://ninet.rs/ipa-bulgaria-serbia/ | Official Niš operator/project source for Interreg Bulgaria-Serbia development/expansion of regional data-center capacity; useful for current pipeline. | A/B |
| IPKO | https://www.ipko.com/en/private/data-center/ and https://www.ipko.com/en/business/server-colocation/ | Official Kosovo/Fushe Kosove / Pristina colocation lead, if enumerating manifest Kosovo-Metohija. | A with jurisdiction note |

### 1.2 Cloud-region and global-vendor sources

| Provider/vendor | Official/current signal | Use | Grade |
|---|---|---|---|
| Oracle Cloud Infrastructure | Oracle release notes: https://docs.oracle.com/iaas/releasenotes/changes/dda8f9c9-90a8-4214-8fdb-5bd169be0eed/index.htm ; Serbia realm docs: https://docs.oracle.com/en/solutions/oci-serbia-realm/index.html ; regions list: https://www.oracle.com/cloud/public-cloud-regions/ | Oracle Cloud **Serbia Central (Jovanovac)** / `eu-jovanovac-1`, region key `BEG`, realm `OC20`; located in Kragujevac. Use as a physical-cloud-region anchor. | A |
| Oracle / Serbia government | https://www.ite.gov.rs/vest/en/771/oracle-corporation-opens-a-regional-hub-in-the-government-data-center-in-kragujevac.php | Primary local confirmation that Oracle regional hub/services are in the Government Data Center in Kragujevac. | A |
| AWS | https://aws.amazon.com/about-aws/global-infrastructure/regions_az/ and https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html | No Serbia AWS Region found in official region list during this run. Treat `AWS connectivity`, `AWS partner`, or `AWS Direct Connect` claims as network/service leads only. | A for negative check |
| Microsoft Azure | https://learn.microsoft.com/en-us/azure/reliability/regions-list and https://azure.microsoft.com/en-us/explore/global-infrastructure/geographies | No Serbia public Azure region found in official region/geography pages during this run. Azure Stack Hub in Kragujevac is a sovereign/government platform lead, not a public Azure region. | A for negative check |
| Google Cloud | https://cloud.google.com/about/locations | No Serbia Google Cloud region found in official locations during this run. `GCP connectivity` is not datacenter evidence unless a physical on-ramp/facility is named. | A for negative check |
| Huawei / IBM / NVIDIA / Eviden | Use Office for IT and eGovernment, ITA Serbia Digital Economy, DCD, and vendor releases/case studies | These vendors identify hosted workloads, cloud infrastructure, AI platforms, supercomputer equipment, or GPU services at Kragujevac/Orion. They validate compute/HPC leads but may not identify new standalone facilities. | A/B |
| e& enterprise | https://www.eandenterprise.com/en/press-release/eandenterprise-inks-landmark-deal-to-triple-serbias-data-center-capacity.html | Official 2025 MoU to add up to 40 MW to Serbia's existing 14 MW Tier-4 Kragujevac campus. Pair with government/permit checks before counting constructed capacity. | A |

### 1.3 Trade press, directories, network databases, and associations

| Source | URL / query surface | Use | Grade |
|---|---|---|---|
| Data Center Dynamics (DCD) | `site:datacenterdynamics.com Serbia data center`, tags `Serbia`, `Kragujevac`, `Telekom Srbija` | Best English trade source for Kragujevac construction/opening, Oracle region, Eviden supercomputer, e& expansion, Belgrade state DC. | B |
| SeeNews | `site:seenews.com Serbia data centre Orion e& Kragujevac` | Regional business press for Orion AI/data-center investment and e&/Kragujevac deals. | B |
| Telecompaper | `site:telecompaper.com Serbia data centre Orion Telekom CETIN SBB` | Telecom press; high-yield for operator launches such as Orion's Belgrade data center. | B |
| International Trade Administration Serbia Digital Economy guide | https://www.trade.gov/country-commercial-guides/serbia-digital-economy | Good market context for Kragujevac state DC, Huawei, AI platform, supercomputer, and broader ICT vendor environment. | B |
| Serbian Open eXchange / SOX via PeeringDB | https://www.peeringdb.com/ix/424 and https://www.peeringdb.com/net/3382 | Interconnection-driven facility discovery: CETIN, BeotelNet, Data Cloud Technology DC Kragujevac, Državni Data Centar DDC, NiNet DC Nis, Orion, SBB, Telekom Srbija. | B/C |
| PeeringDB facilities | https://www.peeringdb.com/ ; example CETIN facility https://www.peeringdb.com/fac/6734 | Facility address, on-net networks, IX participation. Maintained but self-reported; use as confirmation of interconnection, not construction/capacity. | B/C |
| DatacenterMap Serbia | https://www.datacentermap.com/serbia/ and https://www.datacentermap.com/serbia/belgrade/ | Lists Serbia markets and facilities. Useful for Belgrade/Nis/Vrsac/Kragujevac seeds, provider aliases, and approximate counts. | C+ |
| Baxtel Serbia | https://baxtel.com/data-center/serbia | Directory/market map; useful for capacity hints and nearby-facility leads. Verify all capacity/operator/status claims. | C+ |
| Datacenters.com Serbia | https://www.datacenters.com/locations/serbia | Marketplace seed list for commercial colo/bare metal/IaaS; not enough alone. | C |
| DataCenterPlatform Serbia | https://datacenterplatform.com/countries/serbia/ | Seed list including Absolut Solutions, BeotelNet, CETIN, Data Cloud Technology, Orion, etc. | C |
| datacenters.rs | https://datacenters.rs/ | New Serbia-focused directory. Useful as a starting index only; it says data compiled from public sources. | C |
| European Data Centre Association (EUDCA) | https://www.eudca.org/ | Regional association context; no Serbia-specific registry found during this run. Use for market framing only. | C |
| RNIDS / RSNOG / local network community | Query `site:rnids.rs data centar`, `RSNOG PeeringDB SOX data center Serbia` | Useful for network-operator context and SOX/PeeringDB adoption, not a facility registry. | B/C |

Trade/local press query templates:

```text
site:datacenterdynamics.com Serbia "data center"
site:datacenterdynamics.com Serbia "data centre"
site:datacenterdynamics.com Kragujevac "data center"
site:seenews.com Serbia "data centre" Orion OR Kragujevac
site:telecompaper.com Serbia "data centre" "Orion Telekom"
site:ekapija.com "data centar" Srbija
site:ekapija.com "državni data centar" Kragujevac
site:bizlife.rs "data centar" Srbija
site:benchmark.rs "data centar" Srbija
site:pcpress.rs "data centar" Srbija
site:netokracija.rs "data centar" Srbija
site:gradjevinarstvo.rs "data centar" Kragujevac OR Beograd OR Niš
site:serbia-business.eu "data centre" Serbia
site:trade.gov Serbia "Data Center" Kragujevac
```

Local lifecycle terms:

```text
"otvoren data centar"        # opened
"pušten u rad" "data centar" # commissioned / in operation
"izgradnja data centra"      # construction
"gradi se data centar"       # being built
"planira data centar"        # planned
"memorandum" "data centar"   # MoU/intent; do not count as built
"kapacitet" "MW" "data centar"
"rek ormar" OR "rack kabinet"
"Tier 3" OR "Tier III" OR "Tier 4" OR "Class 4"
"dozvola" "data centar"      # permit
"urbanistički projekat" "data centar"
"trafostanica" "data centar" # substation/power clue
```

---

## 2. Operator and project seed list

### 2.1 Belgrade commercial / telecom / interconnection cluster

| Operator/project | Search anchor | Notes | Seed grade |
|---|---|---|---|
| CETIN Serbia Belgrade Data Center | `CETIN Serbia data center Omladinskih brigada 90`, `CETIN carrier neutral data centar Belgrade`, `PeeringDB fac 6734` | CETIN official page describes telehousing and largest interconnection hub in Serbia/CEE; PeeringDB gives address and SOX/NetIX/GNM-IX ecosystem. | A |
| Telekom Srbija / MTS Belgrade Data Center | `mts data centar Beograd Katićeva`, `Telekom Srbija data centar PeeringDB 8085`, `datacenters.rs Telekom Srbija` | Official MTS page verifies service; PeeringDB/directories can provide facility/address/capacity leads such as Katićeva 14-18. Promote capacity only if primary corroboration is found. | A/B |
| SBB Telepark / Yettel Belgrade | `SBB Telepark data centar Nehruova`, `Serbia Broadband Telepark data center`, `PeeringDB Serbia BroadBand 866` | Directory/PeeringDB seed; SBB/Yettel pages show Telepark/company address but public data-center details often come from directories. Verify with official business service pages or RATEL list. | B/C |
| Orion Telekom Belgrade Data Center / AI Factory | `Orion telekom telehousing data centar Beograd`, `Orion sovereign AI Factory data center campus Belgrade`, `Mala pruga 8 data centar` | Official pages state Tier-3 Belgrade data center, racks 8 kW+, green energy, ISO certifications, and GPU infrastructure physically located in its Belgrade data center. Telecompaper/SeeNews are strong launch/investment corroboration. | A/B |
| phoenixNAP Belgrade | `phoenixNAP Belgrade data center Omladinskih brigada 92`, `phoenixNAP expands global presence Europe Serbia` | Operator press release plus directories; confirm exact location and whether facility is owned/leased inside another carrier-neutral site. | B |
| NetCast Data Center | `NetCast data centar Omladinskih brigada 21`, `NetCast sopstveni profesionalni data centar` | Official Serbian pages confirm own Belgrade data center and cloud/data-center services. | A |
| BeotelNet Data Center | `BeotelNet Data Center Belgrade PeeringDB`, `BeotelNet kolokacija data centar` | SOX/PeeringDB facility lead; look for official BeotelNet/MTS records before counting as separate active colo. | B/C |
| BeeNet RS-1 Belgrade | `BeeNet RS-1 Belgrade data center`, `BeeNet operates three data centers Belgrade Vršac Podgorica` | Official BeeNet data-center page lists RS-1 Belgrade. Extract details from operator page; keep separate from BeeNet RS-2 Vrsac. | A |
| Absolut Solutions / Beograd | `Absolut Solutions DC Belgrade data center`, `Absolut Solutions kolokacija Srbija` | Directory seed from DataCenterPlatform/Baxtel; requires operator/RATEL confirmation. | C |

Belgrade focused templates:

```text
"Belgrade" "data center" Serbia CETIN Telekom SBB Orion NetCast BeotelNet
"Beograd" "data centar" CETIN Telekom SBB Orion NetCast BeotelNet
"Београд" "дата центар" Orion Telekom CETIN
"Novi Beograd" "data centar" "Omladinskih brigada"
"Zemun" "data centar" "Mala pruga"
"Katićeva" "Telekom Srbija" "data centar"
"Nehruova" SBB Telepark "data centar"
"Omladinskih brigada 90" "data center" OR "data centar"
"Omladinskih brigada 92" phoenixNAP OR "data center"
"Omladinskih brigada 21" NetCast
site:ratel.rs "Beograd" "data centar"
site:peeringdb.com "Belgrade" "Serbia" "Data Center"
site:oriontelekom.rs "data centar" "Beograd"
site:cetin.rs "Data Center" "Belgrade"
site:mts.rs "Data-centar"
```

### 2.2 Kragujevac / Sumadija government, sovereign cloud, and hyperscale expansion

| Operator/project | Search anchor | Notes | Seed grade |
|---|---|---|---|
| State / Government Data Centre in Kragujevac | `Government Data Centre in Kragujevac Office for IT eGovernment`, `Državni data centar Kragujevac`, `Jovanovac data center Kragujevac` | Official Office page states two facilities, about 14,000 m2, 4 ha plot, class 4/Tier 4-style standard, state and commercial users, Oracle/IBM/Huawei/CERN. | A |
| Data Cloud Technology d.o.o. / DCT Kragujevac | `Data Cloud Technology DC Kragujevac`, `DCT Kragujevac data center`, `PeeringDB 11606` | Commercial/operator entity tied to the state campus; use PeeringDB/SOX and government references to resolve legal/operator role. | A/B |
| Oracle Cloud Jovanovac / Serbia Central | `Oracle Cloud Jovanovac eu-jovanovac-1`, `OCI Serbia Central Jovanovac`, `Oracle Government Data Center Kragujevac` | Official Oracle region docs and local government announcement validate public cloud-region presence in Kragujevac. | A |
| Government Cloud / Azure Stack Hub / Smart Serbia | `Smart Serbia Azure Stack Hub Kragujevac`, `Government Cloud State Data Center Serbia` | Government platform in Kragujevac. Count as sovereign/government cloud infrastructure, not Azure public region. | A |
| CERN/IBM/Huawei hosted capacity | `CERN stores data Kragujevac`, `IBM Huawei Government Data Centre Kragujevac`, `Huawei AI platform Kragujevac data center` | Good for workload/vendor validation; do not count each vendor as separate facility unless source says they opened their own datacenter. | A/B |
| Eviden / national supercomputer | `Eviden Serbia supercomputer Kragujevac data center`, `Nvidia supercomputer Government Data Centre Kragujevac` | HPC/supercomputer deployment inside state DC; classify as HPC infrastructure within existing campus. | B |
| e& enterprise Kragujevac expansion | `e& enterprise triple Serbia data center capacity Kragujevac 40 MW`, `Kragujevac Block 2 data centre 56 MW` | Official e& says up to 40 MW added to existing 14 MW campus; Office page says plan for Block 2/new modules with about 56 MW. Treat as planned/pipeline until permits or construction records confirm stage. | A |
| City Data Center Kragujevac | `City Data Center Kragujevac Huawei donation`, `gradski data centar Kragujevac` | Municipal city-cloud facility. Keep separate from national campus only if location/operator/source demonstrates separate physical facility. | A/B |

Kragujevac templates:

```text
"Kragujevac" "Government Data Centre"
"Kragujevac" "data center" Oracle IBM Huawei CERN
"Kragujevac" "Jovanovac" "Oracle Cloud"
"Kragujevac" "državni data centar"
"Крагујевац" "државни дата центар"
"Kragujevac" "Data Cloud Technology" "data center"
"Kragujevac" "e& enterprise" "40 MW"
"Kragujevac" "Block 2" "data center" OR "data centre"
"Kragujevac" "supercomputer" "data center"
site:ite.gov.rs Kragujevac "data centre"
site:datacenterdynamics.com Kragujevac "data center"
site:eandenterprise.com Serbia Kragujevac "data center"
site:docs.oracle.com "eu-jovanovac-1"
site:peeringdb.com "Data Cloud Technology DC Kragujevac"
```

### 2.3 Vojvodina: Vrsac, Novi Sad, and regional DR/cloud

| Operator/project | Search anchor | Notes | Seed grade |
|---|---|---|---|
| ZELEN DATA CENTAR, Vrsac | `ZELEN DATA CENTAR Vršac Technology Park`, `Zelendata Centar Beogradski put 2g`, `HiTeam first green data center Serbia` | Official page gives Technology Park / Beogradski put 2g, Vrsac; HiTeam/E-Smart corroborate first green data center. | A |
| BeeNet RS-2 Vrsac | `BeeNet RS-2 Vršac 2 MW`, `BeeNet Vrsac disaster recovery data center` | Official BeeNet page states RS-2 Vrsac and network details; directories add capacity. | A/B |
| NEOplanta / NEO Data Center, Novi Sad | `NEOplanta NEO Data Center Novi Sad`, `E-CAPS NEO data center Novi Sad`, `NEO Cloud Novi Sad first cloud data center` | E-CAPS/NEO pages are official leads for Novi Sad cloud data center; verify exact facility address and current services. | A/B |
| Sat-Trakt / Subotica/Bačka Topola regional ISP leads | `Sat-Trakt data center Subotica`, `Sat-Trakt kolokacija`, `PeeringDB Sat-Trakt Serbia` | Network/database lead only; many hits are ISP/network services. Promote with RATEL/operator page. | C/B |
| Novi Sad municipal/university/HPC server rooms | `Novi Sad data centar`, `Novi Sad serverska sala`, `FTN Novi Sad računarski centar` | Likely server-room/HPC/support leads; classify separately from commercial colo. | C/B |

Vojvodina templates:

```text
"Vojvodina" "data centar" OR "data center"
"Vršac" "data centar" OR "data center"
"Vrsac" "ZELEN DATA CENTAR"
"Вршац" "дата центар"
"Beogradski put 2g" "ZELEN DATA"
"BeeNet" "RS-2" "Vršac"
"Novi Sad" "data centar" "NEO"
"Novi Sad" "NEOplanta" "data center"
"Нови Сад" "дата центар"
"Subotica" "data centar" OR "kolokacija"
"Zrenjanin" "data centar" OR "serverska sala"
site:ratel.rs "Vršac" "data centar"
site:peeringdb.com "Vrsac" "Serbia"
site:datacentermap.com/serbia/vrsac
```

### 2.4 Niš / Nisava and southern Serbia

| Operator/project | Search anchor | Notes | Seed grade |
|---|---|---|---|
| NiNet Data Center, Niš | `NiNet data center Niš Bulevar Nemanjića 25`, `Ninet DC Nis colocation`, `NINET regional data centers Bulgaria Serbia` | Directories list an operational colo facility; NiNet/Interreg official project page and tender validate regional data-center capacity expansion in Niš. | A/B for project; C+ for directory-only capacity |
| Interreg IPA Bulgaria-Serbia DATACENTERSBGSR | `BGRS0500152 DATACENTERSBGSR Ninet Niš data-centre equipment`, `Interreg IPA Bulgaria Serbia data-centre equipment Ninet` | EU cross-border project/tender for supply, installation and commissioning of data-centre equipment. Useful for current expansion evidence. | A |
| Planned state-backed Niš / Tehnis data center | `Niš Tehnis data centre 20 MW`, `Niš planned data centre Tehnis`, `Niš Science and Technology Park data center` | Trade/local-business lead says planned facility in Tehnis district with up to 20 MW/€50m; must verify with official urban plan, land decision, grid or procurement before counting as planned A/B. | B/C |
| Jotel / local ISP/server room leads | `Jotel Niš data centar`, `Niš kolokacija hosting`, `Niš serverska sala` | May produce ISP hosting/server-room leads. Promote only with named facility/source. | C |

Niš / Nisava templates:

```text
"Niš" "data centar"
"Nis" "data center" Serbia
"Ниш" "дата центар"
"NiNet" "data center" "Niš"
"Bulevar Nemanjića 25" "NiNet"
"NINET" "DATACENTERSBGSR"
"BGRS0500152" "NINET" "data-centre equipment"
"Tehnis" "data centre" "Niš"
"Niš" "20 MW" "data centre"
"Niš" "trafostanica" "data centar"
site:ipa-bgrs.mrrb.bg Ninet "data-centre"
site:ninet.rs "data centar"
site:peeringdb.com "Ninet DC Nis"
```

### 2.5 Kosovo-Metohija manifest handling

| Operator/project | Search anchor | Notes | Seed grade |
|---|---|---|---|
| IPKO Data Center / server colocation | `IPKO data center Fushe Kosove Ulpiana Pristina`, `IPKO server colocation Kosovo` | IPKO official pages state its data center is in the industrial area of Fushe Kosove and backup in Ulpiana/Pristina. Record source jurisdiction as Kosovo; map to manifest division only because manifest includes Kosovo-Metohija. | A |
| Telecom of Kosovo Core Telecom / IT DC | `Telecom of Kosovo Core Telecom IT data center Pristina`, `Telecom of Kosovo data center colocation` | Datacenters.com/directory lead; needs operator confirmation. | C |
| Kujtesa / Artmotion / regional ISP leads | `Kujtesa data center Pristina`, `Artmotion data center Kosovo`, `Pristina colocation` | Likely ISP/cloud offerings; promote only with physical facility proof. | C |

Kosovo-Metohija templates:

```text
"Kosovo" "data center" IPKO Telekom Kujtesa Artmotion
"Pristina" "data center" "colocation"
"Prishtina" "data center" "colocation"
"Fushe Kosove" "data center" IPKO
"Fushë Kosovë" "data center" IPKO
"Ulpiana" "IPKO" "data center"
"Kosovo-Metohija" "data center"
"Косово и Метохија" "дата центар"
site:ipko.com "data center"
site:datacenters.com "Telecom of Kosovo" "data center"
```

---

## 3. Cloud and hyperscaler enumeration rules

1. Start with official region lists before accepting trade claims.
2. Serbia has one strong public-cloud region signal from this run: **Oracle Cloud Serbia Central (Jovanovac), `eu-jovanovac-1`, Kragujevac**.
3. AWS, Azure, and Google Cloud have no official Serbia public cloud regions found during this run. Record their Serbia mentions as:
   - local office/sales/partner = no facility;
   - Direct Connect/ExpressRoute/Interconnect/IX = network on-ramp lead only;
   - Azure Stack Hub / Government Cloud = sovereign/local government platform, not Azure public region;
   - CDN/edge/PoP = physical-host lead only if host facility is named.
4. Vendor workloads inside the Kragujevac Government Data Centre should not be double-counted as separate datacenters unless the source explicitly states a separate facility or dedicated region/campus module.

Cloud query templates:

```text
"Oracle Cloud" "Jovanovac" "Serbia"
"Oracle Cloud" "eu-jovanovac-1"
"Oracle Cloud" "Kragujevac" "Government Data Center"
"OCI Serbia Central" "Jovanovac"
"AWS Serbia" "Region" "Local Zone"
"AWS Belgrade" "Direct Connect"
"Azure Serbia" "region"
"Azure Stack Hub" "Kragujevac" "State Data Centre"
"Google Cloud Serbia" "region"
"Google Cloud Belgrade" "interconnect"
"Cloudflare" "Belgrade" "SOX" "data center"
"Akamai" "Belgrade" "SOX"
```

---

## 4. Per-division industry workflow

### 4.1 Tier 1 divisions - run full operator + cloud + interconnection + press sweep

| Manifest division | Primary localities / aliases | Enumeration approach |
|---|---|---|
| Belgrade | `Beograd`, `Београд`, `Novi Beograd`, `Zemun`, `Omladinskih brigada`, `Katićeva`, `Nehruova`, `Mala pruga` | Full commercial colo sweep: CETIN, Telekom/MTS, SBB/Yettel, Orion, phoenixNAP, NetCast, BeotelNet, BeeNet RS-1, Absolut. Cross-check RATEL list, PeeringDB/SOX, DatacenterMap, Baxtel, Datacenters.com. |
| Sumadija | `Šumadija`, `Sumadija`, `Kragujevac`, `Крагујевац`, `Jovanovac`, `DCT`, `Državni data centar` | Full government/cloud sweep: Office for IT and eGovernment, Oracle, e& enterprise, DCD, ITA, PeeringDB/SOX, local city pages. Capture national campus, Oracle region, supercomputer/HPC, expansion, and city data center separately if physically distinct. |
| Vojvodina | `Vojvodina`, `Војводина`, `Vršac/Vrsac`, `Novi Sad`, `Subotica`, `Zrenjanin`, `Pančevo/Pancevo` | Full non-Belgrade sweep: ZelenData, BeeNet RS-2, NEOplanta/NEO Data Center, Sat-Trakt/local ISP leads, technology parks, RATEL, PeeringDB. |
| Nisava | `Niš`, `Nis`, `Ниш`, `Nish`, `Bulevar Nemanjića`, `Tehnis` | Full secondary-market sweep: NiNet facility, Interreg DATACENTERSBGSR, planned Tehnis/state-backed facility, Jotel/local ISPs, PeeringDB/SOX. |
| Kosovo-Metohija | `Kosovo`, `Kosova`, `Kosovo-Metohija`, `Kosovo and Metohija`, `Pristina/Prishtina`, `Fushe Kosove/Fushë Kosovë`, `Ulpiana` | Source-sensitive sweep: IPKO official, Telecom of Kosovo directories, local ISP colo. Preserve source jurisdiction and do not normalize away Kosovo wording. |

### 4.2 Tier 2 divisions - local ISP, industrial, and public-sector sweep

These districts are plausible for municipal server rooms, industrial IT rooms, local ISP hosting, reconstruction programs, or edge nodes but have no strong public colo seed from this run. Use universal Serbian terms plus local city aliases and only promote with a named facility/operator/source.

| Division | Add local city / operator terms |
|---|---|
| Macva | `Šabac`, `Sabac`, `Loznica`, `data centar`, `kolokacija`, `SBB`, `Telekom`, local ISP names. |
| Kolubara | `Valjevo`, `Lajkovac`, `Ub`, `data centar`, `serverska sala`, industrial park leads. |
| Podunavlje | `Smederevo`, `Smederevska Palanka`, `Velika Plana`, `Železara`, `industrial park`, `data centar`. |
| Branicevo | `Požarevac`, `Pozarevac`, `Kostolac`, `data centar`, `serverska sala`, energy/utility IT. |
| Pomoravlje | `Jagodina`, `Ćuprija`, `Cuprija`, `Paraćin`, `Paracin`, `industrijska zona`, `data centar`. |
| Bor | `Bor`, `Majdanpek`, `ZiJin`, `rudnik`, `data centar`, `server sala`, industrial-control false positives. |
| Zajecar | `Zaječar`, `Zajecar`, `Knjaževac`, `Knjazevac`, `data centar`, local ISP/municipal IT. |
| Zlatibor | `Užice`, `Uzice`, `Priboj`, `Prijepolje`, `Zlatibor`, `data centar`, `regionalni inovacioni centar`. |
| Moravica | `Čačak`, `Cacak`, `Gornji Milanovac`, `Ivanjica`, `data centar`, tech park / local ISP. |
| Raska | `Raška`, `Raska`, `Kraljevo`, `Novi Pazar`, `Vrnjačka Banja`, `data centar`, `kolokacija`. |
| Rasina | `Kruševac`, `Krusevac`, `Trstenik`, `Aleksandrovac`, `data centar`, industrial/defense server rooms. |
| Toplica | `Prokuplje`, `Kuršumlija`, `Kursumlija`, `Blace`, `data centar`, likely negative-control. |
| Pirot | `Pirot`, `Dimitrovgrad`, `Babušnica`, `Babusnica`, `Slobodna zona Pirot`, `data centar`, cross-border telecom. |
| Jablanica | `Leskovac`, `Vlasotince`, `Lebane`, `data centar`, `serverska sala`, local ISP. |
| Pcinja | `Pčinja`, `Pcinja`, `Vranje`, `Bujanovac`, `Preševo`, `Presevo`, `data centar`, cross-border telecom. |

Universal district templates:

```text
"{division}" "data center" Serbia
"{division}" "data centre" Serbia
"{division}" "colocation" Serbia
"{division}" "telehousing"
"{locality}" "data centar"
"{locality}" "data-centar"
"{locality}" "kolokacija"
"{locality}" "server housing"
"{locality}" "serverska sala"
"{locality}" "računarski centar"
"{locality}" "centar za obradu podataka"
"{locality}" "дата центар"
"{locality_cyrillic}" "дата центар"
"{locality}" "Tier 3" OR "Tier III"
"{locality}" "trafostanica" "data centar"
"{locality}" "urbanistički projekat" "data centar"
site:ratel.rs "{locality}" "data centar"
site:peeringdb.com "{locality}" "Serbia"
site:datacentermap.com/serbia "{locality}"
site:baxtel.com/data-center/serbia "{locality}"
site:ekapija.com "{locality}" "data centar"
site:gradjevinarstvo.rs "{locality}" "data centar"
```

### 4.3 Negative-control handling for low-yield districts

For districts without a known seed, a no-project result is defensible only after checking:

```text
"{division}" "data center" Serbia
"{locality}" "data centar"
"{locality}" "дата центар"
"{locality}" "kolokacija"
"{locality}" "serverska sala"
site:ratel.rs "{locality}" "data centar"
site:peeringdb.com "{locality}" "Serbia"
site:ekapija.com "{locality}" "data centar"
site:datacenterdynamics.com "{locality}" Serbia
```

Common false positives:
- Municipal open-data portals and `pametni grad` dashboards without server facility evidence.
- Telecom exchanges, base stations, fiber route projects, 5G sites, and `kolokacija` in the tower/passive-infrastructure sense.
- Industrial automation/control rooms in mines, steel plants, factories, and power plants.
- `Virtual Private Data Center` or VPS products hosted outside the named district.
- Kosovo political/news pages that mention `data` but not a physical data center.

---

## 5. Serbian alias and language table

| Manifest division | Also query | Notes |
|---|---|---|
| Belgrade | `Beograd`, `Београд`, `Novi Beograd`, `Нови Београд`, `Zemun`, `Земун` | Main commercial and interconnection market. Address terms are high-yield. |
| Macva | `Mačva`, `Мачва`, `Šabac`, `Sabac`, `Шабац`, `Loznica` | Likely local ISP/municipal false positives. |
| Kolubara | `Колубара`, `Valjevo`, `Ваљево`, `Lajkovac`, `Ub` | Low-yield; use industrial/municipal terms. |
| Podunavlje | `Подунавље`, `Smederevo`, `Смедерево`, `Smederevska Palanka`, `Velika Plana` | Industrial leads may be non-datacenter control rooms. |
| Branicevo | `Braničevo`, `Браничево`, `Požarevac`, `Pozarevac`, `Пожаревац`, `Kostolac` | Energy/utility IT false positives likely. |
| Sumadija | `Šumadija`, `Шумадија`, `Kragujevac`, `Крагујевац`, `Jovanovac`, `Јовановац` | National data-center campus and Oracle region. |
| Pomoravlje | `Поморавље`, `Jagodina`, `Јагодина`, `Ćuprija/Cuprija`, `Paraćin/Paracin` | Negative-control unless local ISP/operator page appears. |
| Bor | `Бор`, `Majdanpek`, `Мајданпек`, `ZiJin` | Mining/industrial IT false positives likely. |
| Zajecar | `Zaječar`, `Зајечар`, `Knjaževac/Knjazevac` | Low-yield; local ISP/server-room searches. |
| Zlatibor | `Златибор`, `Užice/Uzice`, `Ужице`, `Priboj`, `Prijepolje` | Tech/tourism portal false positives. |
| Moravica | `Моравица`, `Čačak/Cacak`, `Чачак`, `Gornji Milanovac` | Local ISP and technology-park checks. |
| Raska | `Raška`, `Рашка`, `Kraljevo`, `Краљево`, `Novi Pazar`, `Нови Пазар` | Low-yield; split from Kosovo-adjacent news. |
| Rasina | `Расина`, `Kruševac/Krusevac`, `Крушевац`, `Trstenik` | Industrial/defense server-room false positives. |
| Nisava | `Nišava`, `Нишава`, `Niš/Nis/Nish`, `Ниш`, `Bulevar Nemanjića`, `Tehnis` | NiNet operational/expansion lead and planned state-backed/Tehnis lead. |
| Toplica | `Топлица`, `Prokuplje`, `Прокупље`, `Kuršumlija/Kursumlija` | Likely negative-control. |
| Pirot | `Пирот`, `Dimitrovgrad`, `Димитровград`, `Babušnica/Babusnica` | Check Interreg/cross-border infrastructure but avoid generic EU digital-project false positives. |
| Jablanica | `Јабланица`, `Leskovac`, `Лесковац`, `Vlasotince` | Low-yield; local ISP/municipal IT. |
| Pcinja | `Pčinja`, `Пчиња`, `Vranje`, `Врање`, `Bujanovac`, `Preševo/Presevo` | Low-yield; cross-border telecom false positives. |
| Kosovo-Metohija | `Kosovo`, `Kosova`, `Косово и Метохија`, `Pristina/Prishtina`, `Приштина`, `Fushe Kosove/Fushë Kosovë`, `Ulpiana` | Preserve source jurisdiction; IPKO is strong official lead. |
| Vojvodina | `Војводина`, `Vršac/Vrsac`, `Вршац`, `Novi Sad`, `Нови Сад`, `Subotica`, `Zrenjanin`, `Pančevo/Pancevo` | Strong Vrsac and Novi Sad leads; many local ISP/network leads. |

---

## 6. Extraction and grading rules

For every candidate, extract:

- Facility name exactly as source states it, including Serbian diacritics if present.
- Operator/legal entity and brand (`CETIN doo Beograd`, `Telekom Srbija/MTS`, `Data Cloud Technology`, etc.).
- Manifest division and source locality/address. Preserve cases like `Jovanovac near Kragujevac`, `Omladinskih brigada`, `Mala pruga`, `Beogradski put 2g`, `Bulevar Nemanjića 25`.
- Status: `operational`, `under construction`, `planned/MoU`, `expansion`, `design/tender only`, or `unknown`.
- Type: `commercial_colocation`, `telecom_datacenter`, `government_datacenter`, `sovereign_cloud_region`, `HPC/supercomputer`, `enterprise_private`, `edge/IX/PoP`, `server_room`.
- Capacity only when explicit: MW, kW/rack, racks, sqm, rack cabinets, or site area. Keep source-specific units and do not convert unless necessary.
- Source chain: regulator/operator/cloud provider first; then official government; then trade press; then directories/PeeringDB.

Promotion rules:

- **A**: RATEL list/operator registry, official operator page naming data-center service/facility, Office for IT and eGovernment page, Oracle/AWS/Azure/GCP official cloud-region list, e& official expansion release, EU/Interreg tender, or official municipal/state source.
- **B**: DCD, SeeNews, Telecompaper, ITA, vendor case study, PeeringDB/SOX when the record is maintained and facility-specific.
- **C**: DatacenterMap, Baxtel, Datacenters.com, DataCenterPlatform, datacenters.rs, connectbase/newby/colo.exchange/colomap, SEO pages, unsourced market reports.

False-positive rules:

- `kolokacija` can mean tower/site sharing under telecom regulations; require datacenter/server facility context.
- `cloud`, `VPDC`, `VPS`, `hosting`, `IaaS`, `backup`, or `disaster recovery` is not enough without facility location evidence.
- Vendor hosted workload in Kragujevac does not create a new facility unless a separate facility is named.
- A PeeringDB facility validates interconnection presence; it does not validate MW, construction date, ownership, or full commercial availability.
- For Kosovo-Metohija, keep legal/geographic caveats in notes and avoid implying Serbian operational control when sources present the facility as Kosovo.
