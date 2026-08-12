# TK Explorer Official（官方管道）— Tokelau Datacenter Enumeration

Date: 2026-08-12. Status: final source-verification pass. Scope: Tokelau (TK). Repo divisions per manifest: **`["Tokelau"]`**. Angle: official / regulatory / government methodology for proving whether any data center, cloud region, colocation facility, government server room, telecom exchange, cable landing station, or datacenter-like ICT facility exists in Tokelau. Industry/operator workflow is in `explorer-industry.md`.

Reliability grades: **A** = official/primary source (Tokelau Government, NZ MFAT, law, IANA, operator/cloud-provider official page, official project document); **B** = strong secondary source or named project/vendor/trade source; **C** = directory, SEO page, social post, map snippet, unattributed media, or weak lead only.

---

## 0. Official Ground Truth（官方地面真值）

- **Political / administrative status**: Tokelau is a non-self-governing territory within the Realm of New Zealand. NZ MFAT states that Tokelau has its own political institutions, judicial system, and public services, while New Zealand retains responsibility for international obligations, defence/security, and EEZ management. Source: https://www.mfat.govt.nz/en/countries-and-regions/australia-and-pacific/tokelau
- **Governance geography**: Tokelau consists of three atolls, **Atafu, Nukunonu, and Fakaofo**. MFAT confirms the Ulu o Tokelau role rotates annually among the three Faipule and that the General Fono includes elected representatives from each atoll. Source: MFAT Tokelau page above. The Tokelau Government site also lists national departments including Energy and Telecommunications, Office of the Administrator, Office of the Council, Transport & Support Services, Health, and Education: https://www.tokelau.org.nz/
- **Manifest division rule**: repo manifest has a single division, `Tokelau`; use atolls only as `sub_location` values (`Atafu`, `Nukunonu`, `Fakaofo`, `Unknown TK`). Do **not** invent provincial, district, or NZ-style subdivisions.
- **Population / demand base**: Tokelau Government/TNSO reports the 2016 de jure usually resident population as **1,499**: Atafu 541, Fakaofo 506, Nukunonu 452. Source: https://www.tokelau.org.nz/ and statistics page https://www.tokelau.org.nz/Stats.html. SPC/Pacific Data Hub carries the 2022 Population and Housing Census dataset and should be checked for newer household ICT data: https://pacificdata.org/data/dataset/spc_tkl_2022_phc_v01_m
- **Energy constraint**: Tokelau Government describes the Tokelau Renewable Energy Project as solar panels, storage batteries, and biofuel/diesel generators on the three atolls, funded by New Zealand, sized to meet local island demand rather than industrial loads. Source: https://www.tokelau.org.nz/Solar%2BProject.html. Treat all power systems as atoll microgrids unless an official utility/project document proves a larger grid.
- **Connectivity correction**: Tokelau is **not satellite-only anymore**. Legacy Tokelau Government material says each atoll had its own satellite link managed by government-owned Teletok (https://www.tokelau.org.nz/Tokelau%2BGovernment/Government%2BDepartments/Energy%2Band%2BTelecommunications.html), but Southern Cross NEXT now provides the first international submarine fibre connection to Tokelau and Kiribati. Sources: Ciena/Southern Cross launch release https://www.ciena.com/about/newsroom/press-releases/southern-cross-next-launches%21 and Southern Cross site https://www.southerncrosscables.com/
- **No commercial DC market baseline**: As of this pass, no official Tokelau Government, NZ MFAT, Teletok/IANA, or hyperscaler source identifies a Tokelau commercial data center, colocation facility, cloud region, IXP, AI/HPC site, or carrier-neutral facility. Expected count is zero for commercial DC/colo/cloud; count only official server-room, telecom, or cable/landing facilities if a primary source names them.

## 1. Official Source Register（官方来源登记表）

| Source | URL | Grade | Datacenter use |
|---|---|---:|---|
| NZ MFAT Tokelau page | https://www.mfat.govt.nz/en/countries-and-regions/australia-and-pacific/tokelau | A | Constitutional/governance baseline; development assistance and infrastructure programmes. |
| Tokelau Government portal | https://www.tokelau.org.nz/ | A | National departments, notices, statistics, General Fono and public-service references. |
| Tokelau Government - Energy and Telecommunications | https://www.tokelau.org.nz/Tokelau%2BGovernment/Government%2BDepartments/Energy%2Band%2BTelecommunications.html | A for historical official text; verify currency | Teletok/government-owned telecom and legacy satellite links; use with newer cable sources. |
| Tokelau Government - Solar Project | https://www.tokelau.org.nz/Solar%2BProject.html | A | Confirms atoll microgrid / renewable-energy context. |
| Tokelau Government - Statistics | https://www.tokelau.org.nz/Stats.html | A | Population and census pointers; confirms official census route. |
| SPC / Pacific Data Hub 2022 Census | https://pacificdata.org/data/dataset/spc_tkl_2022_phc_v01_m | A/B | Latest census dataset route; useful for ICT demand and household connectivity. |
| Tokelau Act 1948 | https://www.legislation.govt.nz/act/public/1948/0024/latest/whole.html | A | NZ legal basis; use only for constitutional/regulatory context. |
| IANA .tk root record | https://www.iana.org/domains/root/db/tk.html | A | Confirms ccTLD manager as Telecommunication Tokelau Corporation (Teletok), Fakaofo, with technical contact in the Netherlands. Not local DC proof. |
| Southern Cross NEXT / Ciena launch | https://www.ciena.com/about/newsroom/press-releases/southern-cross-next-launches%21 | A/B | Confirms first international submarine fibre connections to Tokelau and Kiribati. |
| Southern Cross Cable Network | https://www.southerncrosscables.com/ | A/B | Current operator-facing system overview; lists Southern Cross NEXT connections to Fiji, Tokelau, and Kiribati. |

## 2. Official Negative Evidence（官方负项）

Use official lists, not reseller marketing, for cloud-region checks:

- AWS Regions: https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html — no TK region; nearest official regional entries are New Zealand/Australia/Asia Pacific.
- Azure regions: https://learn.microsoft.com/en-us/azure/reliability/regions-list — no TK public region; New Zealand North/Australia regions are separate geographies.
- Google Cloud locations: https://cloud.google.com/about/locations — no TK region or zone.
- Oracle OCI regions: https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm — no TK public cloud region.

Government-domain checks to rerun each pass:

```text
site:tokelau.org.nz ("data centre" OR "data center" OR datacenter OR "server room" OR "server farm" OR colocation OR hosting OR cloud)
site:tokelau.org.nz (ICT OR digital OR telecommunications OR "Energy and Telecommunications") (project OR tender OR procurement OR contract OR strategy)
site:mfat.govt.nz Tokelau ("data centre" OR "data center" OR cloud OR ICT OR digital OR broadband OR cable OR infrastructure)
site:legislation.govt.nz Tokelau (telecommunications OR privacy OR "data protection" OR "electronic transactions")
site:pacificdata.org Tokelau (internet OR phone OR computer OR telecommunications)
```

Classification rule: if the only evidence is a generic cloud reseller, `.tk` domain-registration page, satellite-service availability page, SEO market report, or country-code dropdown, mark **C / false positive** and do not count it.

## 3. Per-Division Strategy（按 division 枚举）

Manifest division is **Tokelau** only. Atoll names are sub-location tags for evidence handling.

| sub_location | Priority | Official route | Count rule |
|---|---:|---|---|
| Fakaofo | Medium | Tokelau Government village/departments, IANA .tk record, Teletok/Fenuafala references, General Fono and public-service records. | Count only if a primary source names a physical server room, telecom facility, cable/landing equipment, or DC-like function in Fakaofo. |
| Nukunonu | Medium | Southern Cross NEXT route references, Teletok/government telecom material, Tokelau Government notices, atoll project records. | Treat cable/telecom nodes as telecom/cable facilities, not commercial DCs, unless hosting/colo service is explicitly evidenced. |
| Atafu | Low | Tokelau Government notices, atoll ICT/energy projects, public-service records. | Expect no DC; record only named primary-source facilities. |
| Unknown TK | High | Any national or unlocated source that cannot be assigned to an atoll. | Prefer Unknown TK over invented atoll assignment. |

Atoll query templates:

```text
"Atafu" Tokelau ("data centre" OR "data center" OR datacenter OR "server room" OR Teletok OR telecom OR cable OR "landing station")
"Nukunonu" Tokelau ("data centre" OR "data center" OR datacenter OR "server room" OR Teletok OR telecom OR cable OR "landing station")
"Fakaofo" Tokelau ("data centre" OR "data center" OR datacenter OR "server room" OR Teletok OR telecom OR cable OR "landing station")
site:tokelau.org.nz "{atoll}" (ICT OR telecommunications OR Teletok OR server OR cable OR solar OR power)
```

## 4. Candidate Schema（候选字段）

Minimum counting standard:

- A primary source names the facility/project and function; or
- an operator/government page plus one independent A/B source confirms the same physical site; and
- any atoll-level assignment has explicit atoll/address evidence.

Use this schema:

```text
country_code: TK
division: Tokelau
sub_location: Atafu | Nukunonu | Fakaofo | Unknown TK
facility_or_project_name:
operator_or_owner: Teletok | Tokelau Government / Tokelau Public Service | Southern Cross / Teletok cable node | donor project | other
consent_or_authorisation: Tokelau government record | NZ legislation | donor agreement | operator source | none found
site_address:
coordinates:
status: operational | planned | lead | verified-negative
facility_type: cable landing / subsea terminal | satellite earth station | telecom exchange | government server room | colocation | cloud-region | AI/HPC | other
it_load_mw:
power_connection: atoll microgrid (solar + batteries + generators) | dedicated generator | unknown
connectivity: Southern Cross NEXT submarine fibre | satellite | local access network | unknown
evidence_grade: A | B | C
primary_urls:
secondary_urls:
notes:
last_checked: 2026-08-12
```

Expected starting records:

- **Southern Cross NEXT / Tokelau connection**: cable/connectivity facility lead; likely Nukunonu per Southern Cross/Ciena later references, but assign atoll only when source explicitly supports it. Not a data center.
- **Teletok telecom facilities**: telecom exchange / legacy satellite-link / operator facility leads; official identity is strong via Tokelau Government and IANA. Not commercial colocation unless Teletok publishes hosting/colo services.
- **Government IT / server rooms**: likely small public-service rooms only; record as leads only with primary evidence.
- **Commercial colocation / cloud region / AI-HPC**: verified-negative baseline.

## 5. False Positives（常见误报）

- `.tk` domain registration, Dot TK, Freenom, or DNS name-server infrastructure. IANA confirms the ccTLD relationship, but `.tk` operations involve technical contacts/name servers outside Tokelau and do not prove local hosting.
- Southern Cross NEXT marketing that mentions “datacentres” in Sydney, Auckland, or Los Angeles. Those are offshore endpoints, not TK facilities.
- Cable landing station, satellite terminal, VSAT, Starlink/Kacific/O3b terminal, or telecom exchange counted as a commercial data center.
- Solar plants, batteries, generators, fish freezers, refrigeration loads, or other atoll microgrid equipment counted as IT load.
- NZ-hosted Tokelau Government websites, email, cloud services, or vendor support counted as Tokelau-local infrastructure.
- Generic “Tokelau data center market” SEO pages, country dropdowns, or cloud-sales landing pages.

## 6. Change Detection（变化检测）

Rerun these triggers before each production enumeration:

```text
"Tokelau" ("data centre" OR "data center" OR datacenter OR colocation OR hosting OR "server room")
"Tokelau" ("cloud region" OR "sovereign cloud" OR "government cloud" OR "national data centre")
"Tokelau" ("Southern Cross NEXT" OR "submarine cable" OR fibre OR "landing station" OR "cable landing")
"Teletok" (hosting OR server OR colocation OR cloud OR "data centre" OR "data center")
"Tokelau" (AWS OR Azure OR "Google Cloud" OR Oracle OR OCI OR Starlink OR Kacific OR O3b)
"托克劳" (数据中心 OR 云 OR 算力 OR 海底光缆 OR 卫星互联网)
```

Escalate to manual review if any A/B source reports: a new cable landing station building, Teletok hosting/colocation product, government data-centre procurement, sovereign-cloud programme with a physical TK site, hyperscaler edge/region/Local Zone, power-system expansion sized for sustained IT load, or any named facility with racks/cooling/security.

## 7. Checker Checklist（复核清单）

1. Confirm manifest still lists TK as `["Tokelau"]`.
2. Recheck NZ MFAT and Tokelau Government for ICT, cable, cloud, procurement, and public-service IT changes.
3. Recheck Southern Cross/Ciena or operator materials for Tokelau landing-node details and atoll location.
4. Recheck Teletok identity through Tokelau Government and IANA; look for current official service pages or notices.
5. Recheck AWS/Azure/GCP/OCI official region lists.
6. Recheck energy/project records for any industrial-scale generation or grid change.
7. Keep `.tk` / Freenom / DNS infrastructure separate from physical Tokelau facilities.
8. If no primary facility evidence appears, record TK as **commercial DC/colo/cloud verified-negative**, with only telecom/cable/government-room leads where source-backed.

---

Conclusion: **Tokelau has no verified commercial data-center, colocation, hyperscale cloud, IXP, or AI/HPC market as of 2026-08-12.** The methodology should still track tiny telecom/cable/government IT facilities, especially Southern Cross NEXT / Teletok changes, but these are not commercial DC market evidence without explicit primary-source support.
