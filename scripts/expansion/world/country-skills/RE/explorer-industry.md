# RE Explorer Industry - 留尼汪（La Reunion）行业/媒体/厂商源枚举方法

Date: 2026-08-12. Country: **RE Reunion / 留尼汪**. Manifest verified from `world-manifest.jsonl`: `{"country_code":"RE","country_name":"Reunion","subnational_type":"country","divisions":["Reunion"]}`. This is a **single-division model / 单分区模型**; every discovered facility belongs to division `Reunion`, with commune/locality stored separately.

Scope: operator, industry, vendor, local-media, directory, and bilingual search methodology for discovering operating, construction, planned, and lead-stage data-center facilities in Reunion. This file complements `explorer-official.md`; industry findings must be upgraded through operator, government, procurement, certification, or other first-party evidence whenever possible.

Reliability grades / 可信度分级：**A** = operator/official/first-party source proves the specific claim. **B** = reliable trade, local media, or vendor source with named party, date, and location. **C** = directory, marketplace, SEO page, social profile, or unsourced aggregator. Grade each field separately; never let a directory capacity or address inherit the grade of an operator existence claim.

---

## 0. Market Shape / 市场形态

- Reunion has a small but real data-hosting and colocation market. The key verified development is **Omega 1 / Omega One** in **Le Port**, in the Oceinde/Zeop ecosystem.
- The prior drafts underweighted Omega 1. It should now be the primary facility seed: TCO and the Omega 1 operator site verify the facility and commune; DCD, Imaz Press, Zinfos974, DataCenterMap, and Baxtel provide useful industry details to cross-check.
- **SFR Business Reunion** has a first-party hosting offer branded around secure datacenter hosting and `NETCENTER`. A directory page claims an SFR Le Port facility at 3 avenue Theodore Drouhet; keep that address C-grade until matched to SFR, planning, utility, or procurement evidence.
- **Zeop Entreprise** advertises Reunion-based business services and references `data-center`; because Zeop is part of the Oceinde group, treat Zeop data-center references as potential Omega 1 references until proven separate.
- **Orange Reunion / Orange Business** remains a high-priority telecom and enterprise-services pivot, but this pass did not verify a Reunion-specific Orange datacenter facility page. Keep as lead/operator context.
- **Cable and IXP evidence** is important for connectivity context, not facility creation. SAFE, METISS, LION/LION2, and REUNIX/IXP data can explain why Le Port/Saint-Denis/Saint-Paul are plausible, but do not prove a data center by themselves.
- **No hyperscaler region**: official AWS, Azure, Google Cloud, and OCI region pages list no Reunion region. Local cloud or hosting should be treated as local/operator services, not hyperscale cloud regions.

---

## 1. Priority Operator and Facility Sweep / 优先运营者与设施扫描

| Lead | Verified/usable source path | Commune | Grade and action |
|---|---|---|---|
| Omega 1 / Omega One | `https://www.omegaone.re/`; TCO article/PDF; DCD; Imaz Press; Zinfos974; DataCenterMap; Baxtel | Le Port | **A** for existence/operator web presence and Le Port locality from TCO/operator. **B** for launch narrative and technical values when from trade/local media. Verify ISO 27001/HDS and any Tier claim in registries before certification fields. |
| SFR Business Reunion hosting / NETCENTER | `https://www.sfrbusiness.re/entreprises-et-collectivites/hebergement/`; DataCenterMap SFR Le Port page | Le Port or unknown | **A** for first-party hosting service. Directory-only address/capacity stays **C**. Search SFR pages, permits, procurement, and ARCEP for facility confirmation. |
| Zeop Entreprise hosting/data-center services | `https://entreprise.zeop.re/`; `https://entreprise.zeop.re/services/hebergement/`; older Zinfos974 hosting article | Le Port / Saint-Denis TBD | **A** for current operator service pages if accessible. Resolve relationship to Omega 1 and avoid duplicate facility records. |
| Orange Reunion / Orange Business | `https://reunion.orange.fr/`, `https://www.orange-business.com/fr`, ARCEP | Saint-Denis or unknown | **A** for operator/regulatory context only; facility remains lead until first-party DC or permit evidence. |
| Local web/cloud hosters | DataCenterMap, Cloudscene, Datacenters.com, hosting searches | TBD | **C** seed only; upgrade through company site + address + facility evidence. |
| REUNIX / local IXP | PeeringDB, ISOC Pulse country tracker | Saint-Denis likely; verify | **B/A** for IXP after PeeringDB/IXP source; not DC. |
| SAFE/METISS/LION | Submarine Networks, TeleGeography/Submarine Cable Map, operator announcements | Saint-Paul / Reunion landing localities | **B** connectivity context; not DC. |

Operator query templates:
```text
"Omega 1" OR "Omega One" "La Réunion" "data center" OR datacenter OR "centre de données"
"Omega 1" "Le Port" "ISO 27001" OR HDS OR "Tier 3" OR "120 racks" OR "1 MW"
"Groupe Océinde" "data center" OR "centre de données" OR "Omega 1"
"SFR Business Réunion" NETCENTER OR datacenter OR "hébergement" OR "PRA" OR "PCA"
"SFR Le Port" "3 avenue Théodore Drouhet" OR "Theodore Drouhet" datacenter
"Zeop entreprise" hébergement OR datacenter OR "data-center" OR "centre de données"
"Orange Réunion" "centre de données" OR datacenter OR hébergement OR cloud
```

---

## 2. Industry Source List / 行业来源表

| Source | URL | Use | Grade rule |
|---|---|---|---|
| Omega 1 operator site | `https://www.omegaone.re/` | Operator claims, services, certification badges, contact | A for operator claims; certification details need registry |
| TCO local authority | `https://www.tco.re/actualite-du-tco/lancement-de-la-construction-du-1er-data-center-de-lile-au-port-53046.html` | Official/local-government support for Omega 1 in Le Port | A for existence/locality and public article facts |
| DCD | `https://www.datacenterdynamics.com/en/news/oceinde-launches-omega-1-data-center-on-reunion-island/` and construction article | Trade confirmation of launch, investment, capacity, operator | B unless backed by operator/TCO PDF |
| Imaz Press Reunion | `https://imazpress.com/actus-reunion/le-port-omega-1-le-premier-data-center-de-la-reunion-est-ne` | Local launch reporting, capacity/PUE claims | B |
| Zinfos974 | `https://www.zinfos974.com/le-port-lancement-du-data-center-du-groupe-oceinde/`; older Zeop hosting article | Local launch and legacy hosting leads | B/C depending specificity |
| DataCenterMap | `https://www.datacentermap.com/reunion/le-port/oceinde-omega-1/`; `https://www.datacentermap.com/reunion/le-port/sfr-le-port/` | Directory seeds, addresses, capacity leads | C until matched to first-party source |
| Baxtel | `https://baxtel.com/data-center/oceinde-omega-1` | Directory/trade-style seed for Omega 1 | C/B depending attribution; verify |
| PeeringDB | `https://www.peeringdb.com/` | IXP/facility/network interconnection | A/B for listed IX/facility facts, not DC by itself |
| Internet Society Pulse | `https://pulse.internetsociety.org/en/ixp-tracker/country/RE/` | IXP count/context; may be Cloudflare-protected | B context |
| Submarine Networks | `https://www.submarinenetworks.com/en/systems/asia-europe-africa/safe`; `https://www.submarinenetworks.com/en/systems/asia-europe-africa/lion-2` | Cable landing/connectivity context | B; A only when citing owner/first-party source quoted by page |
| TeleGeography Submarine Cable Map | `https://www.submarinecablemap.com/` | Cable routes and landing points | B; bot-protection possible |
| Local media set | `clicanoo.re`, `linfo.re`, `zinfos974.com`, `ipreunion.com`, `freedom.re`, `lequotidien.re`, `la1ere.francetvinfo.fr/reunion/` | Local projects, permits, operator announcements | B if named/date/location; otherwise C |
| Certification registries | `uptimeinstitute.com`, `epi-certification.com`, `tiaonline.org` | Positive/negative certification checks | A for registry entries |
| Hyperscaler official pages | AWS/Azure/GCP/OCI official region pages | Negative control | A |

Media and trade query templates:
```text
site:datacenterdynamics.com Reunion OR "La Réunion" "Omega 1" OR datacenter
site:imazpress.com "Omega 1" OR "data center" OR "centre de données"
site:zinfos974.com "Omega 1" OR datacenter OR "centre de données" OR "hébergement de données"
site:clicanoo.re OR site:linfo.re Réunion datacenter OR "centre de données" OR "cloud"
site:capacitymedia.com OR site:telecomreview.com Réunion "data center" OR "Indian Ocean"
"La Réunion" datacenter OR "centre de données" "colocation" OR hébergement OR "salle de serveurs"
"La Réunion" "cloud souverain" OR "cloud de confiance" OR "data center"
留尼汪 数据中心 OR 云计算 OR 托管 OR 海底光缆
```

---

## 3. Directory-to-Primary Workflow / 目录到一手源工作流

1. Use directories only when they provide a name/operator/address/capacity seed. For Reunion, the key directory leads are Omega 1 and SFR Le Port.
2. Match the lead to primary domains: `omegaone.re`, `oceinde.com`, `entreprise.zeop.re`, `sfrbusiness.re`, `reunion.orange.fr`, `arcep.fr`, `tco.re`, `reunion.gouv.fr`, `boamp.fr`, and `marches-publics.gouv.fr`.
3. Assign commune carefully: Omega 1 = **Le Port**; SFR directory address 3 avenue Theodore Drouhet = **Le Port** if verified; Sainte-Clotilde/Le Chaudron = **Saint-Denis**; SAFE landing St. Paul = **Saint-Paul**.
4. Upgrade C to A only when a first-party or official source proves the same facility/field. A directory's MW/rack count stays C unless the operator, press dossier, permit, or reliable named media confirms it.
5. If a Zeop/Oceinde/SFR/Orange service page proves hosting but not a named physical facility, create a service/lead note rather than a full facility record.

Negative-control queries:
```text
"La Réunion" "AWS region" OR "Azure region" OR "Google Cloud region" OR "OCI region"
"France South" Azure Marseille "La Réunion"
"La Réunion" VPS OR "dedicated server" OR "cloud hosting" -datacenter
"Réunion" Starlink "data center" OR gateway
"Saint-Denis" "data center" -Mauritius -"La Réunion"
"RE" "data center" -Réunion -Reunion
留尼汪 AWS OR Azure OR 谷歌云 区域
```

---

## 4. Enumeration Matrix / 枚举矩阵

### Matrix A: Source Category x Provable Fields

| Source category | Facility existence | Address/commune | Capacity/MW/racks | Status/date | Certification | Cable/IXP | Baseline grade |
|---|---|---|---|---|---|---|---|
| Operator first-party page | Yes | Sometimes | Claimed only | Yes | Claimed only unless cert shown | Sometimes | A for operator claim |
| Government/local authority | Yes | Yes | Sometimes | Yes | No | Sometimes | A |
| Certification registry | Yes | Yes | No | Yes | Yes | No | A |
| Procurement/planning/ICPE | Lead/permit | Yes if stated | Sometimes | Yes | No | No | A |
| Trade/local media | Usually | Usually | Sometimes | Yes | Usually no | Sometimes | B |
| Cable/IXP databases | No DC proof | Landing/IX locality | No DC capacity | Yes | No | Yes | B/A for connectivity only |
| Directory/marketplace/social | Hint | Hint | Hint | Weak | Weak | Hint | C |

### Matrix B: Commune Scan Priority

| Commune | Operators | Directories | Local media | Procurement/official | Cable/IXP | Expected output |
|---|---|---|---|---|---|---|
| Le Port | High | High | High | High | Medium | **High**: Omega 1 confirmed; SFR Le Port lead; Zeop/Oceinde ecosystem |
| Saint-Denis / Sainte-Clotilde / Le Chaudron | High | Medium | Medium | High | IXP likely | Medium-high: operator offices/services, possible REUNIX/facility leads |
| Saint-Paul | Low | Medium | Medium | Medium | High | Cable landing context; no DC without hosting evidence |
| La Possession | Low | Low | Low | Low | Low | Negative/permit scan |
| Saint-Pierre | Low | Low | Low | Medium | Low | Local government/server-room procurement scan |
| Le Tampon, Saint-Louis, Saint-André, Saint-Benoît, Sainte-Marie, Sainte-Suzanne | Low | Low | Low | Low | Low | Explicit negative scan |

Commune query template:
```text
"{commune}" Réunion "centre de données" OR datacenter OR "salle de serveurs" OR hébergement OR colocation
"{commune}" Réunion telecom OR "station d'atterrissement" OR "câble sous-marin"
"{commune}" Réunion "groupe électrogène" OR "poste source" OR onduleur OR climatisation
site:datacentermap.com "{commune}" Réunion
site:clicanoo.re OR site:linfo.re "{commune}" datacenter OR "centre de données" OR telecom
"{commune}" "data center" OR "server room" "permis de construire"
```

---

## 5. Seed Records to Validate / 待核验种子

| Seed | Status | Capacity | Operator | Grade | Source path |
|---|---|---|---|---|---|
| Omega 1 / Omega One | Operating / launched by Nov 2024 | 1 MW / 120 racks reported; verify against operator/TCO PDF before A | Oceinde/Omega 1; Zeop ecosystem | A existence/locality; B/C capacity; certification pending registry | `omegaone.re`, TCO, DCD, Imaz Press, Zinfos974, DataCenterMap, Baxtel |
| SFR Business Reunion NETCENTER / hosting | Operating service | null | SFR Business Reunion | A for service; C for directory-only facility details | `sfrbusiness.re`, DataCenterMap SFR Le Port |
| Zeop Entreprise data-center/hébergement service | Operating service / facility relationship TBD | null | Zeop / Groupe Oceinde | A for service page; facility TBD | `entreprise.zeop.re`, Zinfos974 legacy article, Omega 1 |
| Orange Reunion / Orange Business hosting lead | Lead | null | Orange | A operator context only; facility not verified | Orange/ARCEP/procurement |
| Local hosters/cloud resellers | Lead | null | TBD | C starting point | hosting directories and local searches |
| REUNIX / local IXP | Active IXP context | n/a | TBD | B/A after PeeringDB | ISOC Pulse, PeeringDB |
| SAFE landing | Connectivity | n/a | consortium | B | Submarine Networks, TeleGeography |
| METISS landing | Connectivity | n/a | consortium | B | TeleGeography/Submarine Cable Map, operator/media |
| LION/LION2 | Connectivity | n/a | Orange/consortium | B | Submarine Networks, operator/media |
| Uptime/TIA/EPI Reunion certifications | Negative in this pass | n/a | none found | A negative after registry search | Uptime, EPI/TIA |

---

## 6. Capacity and Reliability Rules / 容量与可信度规则

- **A-grade capacity** requires first-party/operator document, official permit, official press dossier, certification document, or procurement file that states the value.
- **B-grade capacity** can come from DCD, Imaz Press, Zinfos974, or another named reliable media/trade source. Store the exact source and date.
- **C-grade capacity** includes DataCenterMap/Baxtel/Cloudscene-only MW, racks, cabinet counts, coordinates, or inferred values.
- Never infer capacity from cable bandwidth, transformer size, "Tier 3 equivalent", "hub", "sovereign", "world-class", or island market forecasts.
- Store "equivalent Tier 3" separately from certified Tier III. Require registry evidence for Uptime/TIA/EPI certifications.
- Keep negative scans explicit: for low-output communes, write "no public DC evidence found on run date" rather than deleting the commune from coverage.
