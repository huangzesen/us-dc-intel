# TK Explorer Industry（行业管道）— Tokelau Datacenter Enumeration

Date: 2026-08-12. Status: final source-verification pass. Scope: Tokelau (TK). Repo divisions per manifest: **`["Tokelau"]`**. Sub-location tags: **Atafu / Nukunonu / Fakaofo / Unknown TK**. Angle: industry / operator / connectivity methodology for proving whether any commercial data center, colocation provider, cloud region, IXP, cable-landing facility, telecom exchange, satellite gateway, government server room, or other datacenter-like infrastructure exists in Tokelau. Official/regulatory workflow is in `explorer-official.md`.

Reliability grades: **A** = primary/operator/official source (Teletok/Tokelau Government, IANA, Southern Cross/Ciena, cloud-provider official region list, NZ MFAT); **B** = strong secondary/trade press, cable-system databases, network metadata, named vendor/project releases; **C** = directory, market report, SEO page, social media, geolocation/IP inference, or unattributed lead only.

---

## 0. Market Reality（行业现实）

- **Commercial DC/colo/cloud market: verified-negative baseline.** Public operator, official, cloud-provider, and industry searches found no verified Tokelau commercial colocation provider, cloud region, carrier-neutral facility, IXP, CDN edge facility, AI/HPC site, or enterprise DC market. Expected commercial count is zero.
- **Connectivity improved materially, but this is not DC evidence.** The prior “satellite-only” baseline was stale. Southern Cross NEXT now provides Tokelau’s first international submarine fibre connection, with Tokelau listed by Southern Cross and Ciena/Southern Cross releases. Sources: https://www.ciena.com/about/newsroom/press-releases/southern-cross-next-launches%21 and https://www.southerncrosscables.com/
- **Operator set is tiny.** Teletok / Telecommunication Tokelau Corporation is the key telecom entity. Tokelau Government legacy material says each atoll had its own satellite link and that management was by the government-owned company Teletok: https://www.tokelau.org.nz/Tokelau%2BGovernment/Government%2BDepartments/Energy%2Band%2BTelecommunications.html. IANA lists Telecommunication Tokelau Corporation (Teletok), Fenuafala, Fakaofo, as `.tk` ccTLD manager: https://www.iana.org/domains/root/db/tk.html
- **Demand and power are micro-scale.** Tokelau’s official 2016 population was 1,499, split across the three atolls. Source: https://www.tokelau.org.nz/. Tokelau Government describes the renewable-energy system as local solar arrays, batteries, and generators for island demand: https://www.tokelau.org.nz/Solar%2BProject.html. This supports telecom/government IT rooms, not MW-scale commercial IT load.
- **Division handling:** manifest division = `Tokelau`. Atolls are only sub-location fields. Never split TK into invented provinces/districts, and never count offshore New Zealand/Samoa facilities as TK.

## 1. Operator and Infrastructure Sources（运营商与基础设施来源）

| Source | URL | Use | Grade |
|---|---|---|---|
| Teletok / Telecommunication Tokelau Corporation | Tokelau Government telecom page above; IANA .tk record https://www.iana.org/domains/root/db/tk.html | Identity of the government-owned telecom entity; telecom facilities, `.tk`, legacy satellite links. | A |
| Tokelau Government portal | https://www.tokelau.org.nz/ | National notices, departments, statistics, Energy/Telecommunications responsibilities. | A |
| Southern Cross Cable Network | https://www.southerncrosscables.com/ | Confirms Southern Cross NEXT connections to Fiji, Tokelau, and Kiribati. | A/B |
| Ciena/Southern Cross NEXT launch release | https://www.ciena.com/about/newsroom/press-releases/southern-cross-next-launches%21 | Confirms NEXT launch and first international submarine fibre connections to Tokelau and Kiribati. | A/B |
| Ciena/Southern Cross 400GbE release | https://www.ciena.com/about/newsroom/press-releases/southern-cross-400gbe-services-now-available%21 | Confirms 400GbE commercial service context on NEXT and repeats Tokelau/Kiribati first-fibre connection. | A/B |
| BGP / ASN tools | bgp.tools / APNIC / RIPE / PeeringDB searches for Teletok, AS57382, AS198147, AS55523 | Network footprint only; not facility proof. | B/C |
| Cloud-provider official location lists | AWS, Azure, Google Cloud, Oracle OCI official lists | A-grade absence/presence for cloud regions. | A |
| Data center directories / market pages | DataCenterMap, datacenters.com, generic colocation market pages | Weak negative/lead checks only. Absence is useful context; presence requires primary confirmation. | C |

Teletok query templates:

```text
"Teletok" Tokelau (hosting OR server OR colocation OR "data centre" OR "data center" OR cloud)
"Telecommunication Tokelau Corporation" (hosting OR server OR colocation OR cable OR satellite)
site:tokelau.org.nz Teletok (server OR data OR cloud OR telecommunications OR cable)
"Teletok" (Southern Cross NEXT OR fibre OR "submarine cable" OR bandwidth OR capacity)
```

## 2. Connectivity Pivots（互联线索）

### 2.1 Southern Cross NEXT

Use Southern Cross NEXT as the primary modern connectivity pivot. It is a **cable/connectivity lead**, not a data-center lead by itself.

- Southern Cross site describes NEXT as a low-latency, high-capacity cable linking datacentres in Sydney, Los Angeles, and Auckland, with connections to Fiji, Tokelau, and Kiribati. Source: https://www.southerncrosscables.com/
- Ciena/Southern Cross announced the NEXT launch on 2022-07-07 and stated that NEXT would provide the first international submarine fibre connections to Tokelau and Kiribati. Source: https://www.ciena.com/about/newsroom/press-releases/southern-cross-next-launches%21
- Ciena/Southern Cross announced commercial 400GbE services on NEXT in 2023 and again described Tokelau/Kiribati first-fibre connections. Source: https://www.ciena.com/about/newsroom/press-releases/southern-cross-400gbe-services-now-available%21

Query templates:

```text
"Southern Cross NEXT" Tokelau ("landing" OR "cable landing" OR "Nukunonu" OR Teletok)
"Tokelau" ("submarine cable" OR fibre OR "cable landing" OR "landing station") ("Southern Cross" OR NEXT)
"Tokelau" "400GbE" "Southern Cross"
```

### 2.2 Legacy satellite and local access

Tokelau Government legacy material says each of the three atolls had its own satellite link for international calls and internet, managed by Teletok. Keep satellite links as historical/current resilience leads until a current Teletok or government source clarifies the exact post-NEXT architecture. Do **not** count a satellite terminal, VSAT, Starlink terminal, or gateway as a DC unless a source explicitly names hosting/compute/colo function.

Query templates:

```text
"Tokelau" satellite (VSAT OR O3b OR SES OR Intelsat OR Kacific OR Starlink) bandwidth
"Tokelau" internet (satellite OR fibre OR "Southern Cross" OR Teletok)
"Atafu" OR "Nukunonu" OR "Fakaofo" Tokelau (satellite OR Teletok OR telecom)
```

## 3. Cloud / Colo / IXP Checks（云、托管、IXP 负检查）

Official cloud lists to check before recording any hyperscaler claim:

- AWS Regions: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html
- Azure regions: https://learn.microsoft.com/en-us/azure/reliability/regions-list
- Google Cloud locations: https://cloud.google.com/about/locations
- Oracle OCI regions: https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm

As of this pass, none lists Tokelau. Nearby or related regions such as AWS Asia Pacific (New Zealand), Azure New Zealand North, Australia regions, Fiji connectivity, or offshore Southern Cross endpoints must not be counted as TK.

Industry negative queries:

```text
"Tokelau" (colocation OR colo OR "rack space" OR "carrier hotel" OR IXP OR "internet exchange")
"Tokelau" ("data centre" OR "data center" OR datacenter) -tourism
"Tokelau" (AWS OR Azure OR "Google Cloud" OR Oracle OR OCI OR "cloud region" OR "local zone" OR "edge location")
"Tokelau" (GPU OR AI OR "artificial intelligence" OR supercomputer OR "high performance computing")
site:datacentermap.com Tokelau
site:cloudinfrastructuremap.com Tokelau
```

Classification:

- Cloud-provider sales pages, CDN country availability, Starlink availability, domain registration, and generic “serve customers in Tokelau” pages are **service availability**, not facilities.
- Data center directory entries are **C** unless matched to Teletok, Tokelau Government, Southern Cross, or another named primary operator record.
- Network metadata can identify ASNs/prefixes and likely offshore DNS anycast, but it cannot establish a physical Tokelau server room.

## 4. .tk Domain Noise（.tk 域名噪声）

`.tk` is the highest-risk false-positive source for Tokelau.

- IANA records `.tk` as a country-code TLD and lists Telecommunication Tokelau Corporation (Teletok) in Fakaofo as manager, but technical contact details point to BV Dot TK in Amsterdam and the name servers are not evidence of Tokelau-local datacenter capacity: https://www.iana.org/domains/root/db/tk.html
- Freenom / Dot TK / free-domain history is relevant for cyber/DNS market notes only. It does not prove local hosting, colocation, cloud, or data-center operations.

Noise queries:

```text
"Tokelau" ".tk" ("data center" OR hosting OR server OR DNS)
"Dot TK" OR Freenom Tokelau (registry OR registrar OR DNS OR hosting)
"tk domains" ("data center" OR "cloud" OR "server")
```

Rule: record `.tk` items as DNS/registry context only unless the source independently proves physical equipment in Tokelau.

## 5. Energy and Buildability（能源与可建性）

- Tokelau Government’s solar project page describes local solar panels, batteries, and generators serving the three atolls and meeting island demand: https://www.tokelau.org.nz/Solar%2BProject.html
- Energy and telecommunications material indicates Teletok is a significant electricity user in the local system, reinforcing that telecom loads are visible in a microgrid context. Source: https://www.tokelau.org.nz/Tokelau%2BGovernment/Government%2BDepartments/Energy%2Band%2BTelecommunications/Energy.html
- Any commercial DC claim must show its power source. A MW-scale IT load is implausible without a separately evidenced generation, fuel, cooling, land, and logistics plan.

Energy queries:

```text
"Tokelau" (solar OR battery OR diesel OR generator OR microgrid) (Teletok OR telecommunications OR "data centre" OR "server")
"Tokelau Renewable Energy Project" (kW OR MW OR panels OR battery OR diesel)
site:tokelau.org.nz ("power" OR "energy") (Teletok OR telecom OR server OR data)
```

## 6. Per-Atoll Industry Strategy（按环礁行业枚举）

| sub_location | Priority | Industry route | Expected yield |
|---|---:|---|---|
| Fakaofo | Medium | Teletok identity / `.tk` manager address via IANA; Tokelau Government village references; telecom and public-service searches. | Telecom or registry/admin leads only; commercial DC unlikely. |
| Nukunonu | Medium | Southern Cross NEXT / cable-location searches, telecom searches, Tokelau Government notices. | Cable/telecom lead possible; count as DC only with explicit hosting/colo/compute function. |
| Atafu | Low | Teletok/telecom/satellite and government project searches. | Very low; likely no DC. |
| Unknown TK | High | National operator, cable, cloud, ASN, and media hits with no atoll detail. | Default bucket for unlocated leads. |

Atoll templates:

```text
"Atafu" Tokelau (Teletok OR telecom OR satellite OR fibre OR "earth station" OR server OR hosting OR colocation)
"Nukunonu" Tokelau (Teletok OR telecom OR satellite OR fibre OR "landing station" OR server OR hosting OR colocation)
"Fakaofo" Tokelau (Teletok OR telecom OR satellite OR fibre OR "earth station" OR server OR hosting OR colocation)
"{atoll}" Tokelau ("data centre" OR "data center" OR datacenter)
```

## 7. Candidate Fields（候选字段）

Minimum count standard: a primary operator/official source naming the physical facility and function, or an operator/government source plus a second A/B corroborating source. Atoll attribution requires explicit evidence.

```text
country_code: TK
division: Tokelau
sub_location: Atafu | Nukunonu | Fakaofo | Unknown TK
facility_or_project_name:
operator: Teletok | Tokelau Government | Southern Cross / Teletok cable node | satellite provider | donor project | other
facility_type: cable landing / subsea terminal | satellite earth station | telecom exchange | government server room | colocation | cloud region | IXP | AI/HPC | other
status: operational | planned | lead | verified-negative
capacity_or_scale: cable capacity | satellite capacity | racks | kW/MW | unknown
connectivity: Southern Cross NEXT submarine fibre | satellite | local access network | unknown
evidence_grade: A | B | C
primary_urls:
secondary_urls:
power: atoll microgrid | dedicated generator | unknown
site_address:
coordinates:
notes:
last_checked: 2026-08-12
```

Expected baseline:

- `commercial colocation`: verified-negative
- `cloud region / Local Zone`: verified-negative
- `IXP / carrier-neutral meet-me room`: verified-negative unless Teletok/Southern Cross/official source proves otherwise
- `Southern Cross NEXT cable node`: telecom/cable lead, not DC
- `Teletok telecom facilities`: telecom lead, not commercial DC
- `government IT rooms`: small server-room lead only when source-backed

## 8. False Positives and Escalation（误报与升级）

Common false positives:

- `.tk`, Dot TK, Freenom, registrar, DNS, or domain-abuse stories.
- Southern Cross NEXT endpoints in Sydney/Auckland/Los Angeles described as datacentres.
- Cable landing stations, satellite earth stations, VSAT/Starlink terminals, mobile towers, Wi-Fi access points, or telecom exchanges counted as colocation.
- Solar plants, batteries, diesel generators, refrigeration/freezer loads, or public buildings counted as IT facilities.
- IP geolocation that maps Teletok/Dot TK/DNS routes to New Zealand, Europe, or the US.
- NZ/Samoa-hosted Tokelau government services counted as TK-local hosting.

Escalate any of these:

- Teletok publishes hosting, rack, cloud, IXP, caching, or enterprise data-center service.
- Tokelau Government or NZ MFAT publishes a data-centre/cloud procurement or physical server-room project.
- Southern Cross/Teletok publishes detailed cable landing station or subsea terminal information with rack/power/hosting functions.
- A hyperscaler adds TK to an official region, Local Zone, edge, or cloud-location list.
- Energy project documents show generation/storage sized for sustained non-telecom IT loads.

## 9. Checker Checklist（行业侧复核清单）

1. Confirm manifest division remains `["Tokelau"]`.
2. Recheck Teletok/Tokelau Government/IANA for operator identity, current service pages, and facility references.
3. Recheck Southern Cross/Ciena for Tokelau cable node status and exact landing/atoll details.
4. Recheck official cloud-region lists for AWS, Azure, Google Cloud, and OCI.
5. Search industry/directories for `Tokelau data center/colo/cloud/IXP`, but hold all non-primary hits at C.
6. Keep `.tk` registry and DNS infrastructure separate from physical Tokelau facilities.
7. Record commercial DC/colo/cloud as **verified-negative** unless a primary source changes the baseline.

---

Conclusion: **Tokelau has no verified commercial data-center, colocation, hyperscale cloud, IXP, or AI/HPC market as of 2026-08-12.** The only credible infrastructure leads are micro-scale telecom, cable, and government IT facilities tied to Teletok, Tokelau Government, and Southern Cross NEXT; none should be counted as commercial DC capacity without explicit primary evidence.
