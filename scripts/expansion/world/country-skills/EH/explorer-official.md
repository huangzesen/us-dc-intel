# EH Explorer Official — 西撒哈拉数据中心枚举方法论（官方/政府面）

Date: 2026-08-12. 国家/地区: **EH 西撒哈拉（Western Sahara）**. Manifest division model: **single division only** — `["Western Sahara"]`. Scope: official, regulator, procurement, utility, international-organization, and operator-primary routes for finding data center assets in Western Sahara. Internal geographic work buckets below are enumeration zones, not manifest divisions.

> **政治敏感性说明（事实中立 / neutral factual note）**：西撒哈拉列于联合国非自治领土（Non-Self-Governing Territories）议题中，最终地位存在争议。摩洛哥实际管理西部主要城市和大西洋沿岸地区，并将其纳入摩方“南部省份”行政体系；波利萨里奥阵线/SADR 主张该领土主权并在防御墙以东有存在；MINURSO 是联合国西撒哈拉任务机构。本文仅按来源归属记录事实：摩洛哥机构材料标注“摩方/ Moroccan-administered source”，SADR/波利萨里奥材料标注“萨德拉/波利萨里奥来源”，联合国材料标注“UN/MINURSO”。不使用本文档判断主权。

Verified baseline（复核基线）:

- Manifest: `/scripts/expansion/world/world-manifest.jsonl` entry is `{"country_code":"EH","country_name":"Western Sahara","subnational_type":"country","divisions":["Western Sahara"]}`.
- UN status route: `https://www.un.org/dppa/decolonization/en/nsgt/western-sahara` may require browser verification; UN press and MINURSO/UN Peacekeeping pages are usable fallback official routes.
- IANA .EH: `https://www.iana.org/domains/root/db/eh.html` shows `.EH` has no assigned ccTLD manager and is not in the root zone.
- Direct URL checks from this environment: `mmsp.gov.ma`, `data.gov.ma`, `cri-invest.ma`, `masen.ma`, `cndp.ma`, `ungm.org`, `wacscable.com`, and `anp.org.ma` resolved; `anrt.ma`, `add.gov.ma`, `one.org.ma`, and `equipement.gov.ma` timed out; `amdie.gov.ma`, `marchespublics.gov.ma`, `iam.ma`, and `minurso.unmissions.org` returned access-control responses. Treat timeouts/403s as recheck notes, not as evidence that the source is invalid.

Reliability grades（A/B/C 分级）:

- **A** = 官方或一手证据 for the exact fact claimed: ministry/regulator/CRI/procurement/utility pages, UN/MINURSO pages, operator-owned facility pages, Uptime Institute awards, official cable-system/operator pages.
- **B** = strong secondary: Reuters, Data Center Dynamics, Ecofin Agency, MAP reposts, Medias24, Le360, TelQuel, Yabiladi, trade media with named parties and dates.
- **C** = lead only: directories, market reports, social posts, screenshots, unattributed claims, or sources that only imply a facility.

Capacity discipline（容量纪律）: record MW/MVA/kVA/racks/sqm only when tied by the source to a named data center site. Renewable-energy plant MW, cable capacity, telecom backbone capacity, or port/zone power plans are context, not data center IT load.

---

## 0. Operating Facts / 关键结构

Western Sahara has no separate national data-center registry, planning-permit search portal, telecom regulator, or power regulator. Official enumeration depends on Morocco-administered institutional sources for the west/coastal area, UN/MINURSO sources for the mission footprint, and SADR/Polisario sources only for attributed claims.

Internal coverage buckets（全部映射回 manifest 的单一 division: `Western Sahara`）:

| Bucket | Coverage | Primary route |
|---|---|---|
| A. Laayoune-Sakia El Hamra / 拉尤恩-萨基亚阿姆拉 | Laayoune, Smara, Boujdour, Tarfaya-adjacent checks. Tarfaya is north of the EH boundary in Morocco, so only use it as regional energy/context unless the source places the facility inside EH. | CRI-Invest, Moroccan procurement, municipal/wilaya notices, ONEE/MASEN, MINURSO for Laayoune |
| B. Dakhla-Oued Ed-Dahab / 达赫拉-黄金谷地 | Dakhla, Oued Ed-Dahab, Aousserd. Main known official data-center lead is Igoudar Dakhla. | MTNRA/MMSP ministry pages, regional council/wilaya, CRI-Invest, ANP, ONEE/MASEN, cable/operator sources |
| C. East of the berm / 防御墙以东 | Sparse population and no verifiable public data-center infrastructure route found. | SADR/Polisario sources and UN reporting; treat as C for infrastructure facts unless corroborated |
| D. International organization layer / 国际机构面 | MINURSO and UN procurement, mainly Laayoune. | UNGM and MINURSO/UN Peacekeeping |

Core multilingual terms:

```text
French: centre de données, datacenter, data center, centre de calcul, hébergement,
hébergement de données, colocation, salle serveur, cloud souverain, cloud de l'Etat,
permis de construire, autorisation d'urbanisme, CRUI, CRI, raccordement électrique,
poste électrique, autoproduction, câble sous-marin, station d'atterrissement,
provinces du Sud, Sahara marocain, Sahara occidental, port Atlantique de Dakhla,
Igoudar Dakhla, Igoudar numérique.

Arabic: مركز البيانات, مركز المعطيات, مركز الحوسبة, الاستضافة, الحوسبة السحابية,
السحابة السيادية, رخصة البناء, الاتصالات, الكابل البحري, محطة الإنزال,
الأقاليم الجنوبية, الصحراء المغربية, الصحراء الغربية, الداخلة, العيون.

Spanish: centro de datos, centro de procesamiento de datos, centro de cálculo,
alojamiento, fibra óptica, cable submarino, estación de aterrizaje,
Sáhara Occidental, El Aaiún, Dajla.
```

---

## 1. Official / Primary Routes

### 1.1 Digital Transition Ministry / MTNRA-MMSP

Main URL: `https://www.mmsp.gov.ma/fr` (A). This is currently the strongest official source for the Dakhla data-center pipeline.

Verified project pages:

- `https://www.mmsp.gov.ma/fr/actualites/signature-de-deux-accords-strat%C3%A9giques-%C3%A0-dakhla-dans-les-domaines-de-l%E2%80%99intelligence-artificielle-et-de-la-transition-%C3%A9nerg%C3%A9tique` — 14 Nov 2025. Officially says two agreements were signed in Dakhla and that the first launches the green data centers project **Igoudar Dakhla**.
- `https://www.mmsp.gov.ma/fr/actualites/signature-d%E2%80%99une-convention-pour-l%E2%80%99op%C3%A9rationnalisation-du-campus-datacenter-vert-%C2%AB-igoudar-num%C3%A9rique-%C2%BB-%C3%A0-dakhla` — 14 Apr 2026. Officially says a partnership convention was signed for the green datacenter campus **Igoudar Numérique** in Dakhla, with **target capacity 500 MW**, and that it launches strategic studies covering governance, economic model, deployment phases, structuring, and financing.

Grading: A for official existence of the announced program, location (Dakhla), named project/campus, named public parties, and 500 MW target. Do **not** mark operational or under construction from these pages; current status is `planned / studies launched`.

```text
site:mmsp.gov.ma "Igoudar Dakhla"
site:mmsp.gov.ma "Igoudar numérique" "Dakhla"
site:mmsp.gov.ma "datacenter vert" "Dakhla"
site:mmsp.gov.ma "centre de données" "Dakhla"
site:mmsp.gov.ma "500 mégawatts" "Dakhla"
site:mmsp.gov.ma "cloud souverain" "Dakhla"
```

### 1.2 ANRT — Telecom Regulator

Main URL: `https://www.anrt.ma/` and `https://www.anrt.ma/en` (A when reachable; direct check timed out from this environment). ANRT covers telecom licensing, spectrum, interconnection, 5G/fiber background under Morocco-administered administration. It does not license data centers as a standalone facility class.

```text
site:anrt.ma "data center"
site:anrt.ma "centre de données"
site:anrt.ma "hébergement"
site:anrt.ma "cloud"
site:anrt.ma "Laayoune" OR "Laâyoune" OR "Dakhla"
site:anrt.ma "provinces du Sud"
"ANRT" "Dakhla" "fibre"
"ANRT" "Laayoune" "5G"
```

Use for: operator legal names, license category, spectrum/fiber context, and telecom availability. Not facility proof unless ANRT names a specific data center.

### 1.3 CRI / CRUI Investment and Permits

Main URL: `https://www.cri-invest.ma/` (A). Laayoune-Sakia El Hamra map route: `https://www.cri-invest.ma/map/my-cri/9` (A path; verified reachable). Dakhla-Oued Ed-Dahab should be reached through the CRI-Invest map/search, plus regional CRI pages when stable.

```text
site:cri-invest.ma "Igoudar" "Dakhla"
site:cri-invest.ma "data center" "Dakhla"
site:cri-invest.ma "centre de données" "Laayoune"
site:cri-invest.ma "cloud" "provinces du Sud"
"CRUI" "Dakhla" "datacenter"
"commission régionale unifiée d'investissement" "Dakhla" "centre de données"
"permis de construire" "Dakhla" "data center"
"permis de construire" "Laayoune" "centre de données"
```

Use for: investment approval, land, permitting, regional announcements. A permit or investment approval supports project status only to the stage stated by the document.

### 1.4 AMDIE Investment Promotion

Main URL: `https://www.amdie.gov.ma/` (official domain; direct check returned 403). Use as an A route when accessible or cached through search. Only AMDIE-authored project details are A; media paraphrases remain B.

```text
site:amdie.gov.ma "Igoudar"
site:amdie.gov.ma "Dakhla" "data center"
site:amdie.gov.ma "centre de données"
site:amdie.gov.ma "provinces du Sud" "numérique"
"AMDIE" "Dakhla" "datacenter"
```

### 1.5 ONEE / MASEN — Power and Renewables

Main URLs: `https://www.one.org.ma/` (A when reachable; direct check timed out) and `https://www.masen.ma/en` (A; reachable). These sources are for grid and renewable-energy background, not automatic IT-load evidence.

Southern-area energy context to verify from ONEE/MASEN or project owners:

- Noor Laayoune / Foum El Oued and Noor Boujdour solar projects.
- Tarfaya wind project is outside the EH manifest geography; use only as nearby regional power context.
- Dakhla desalination, port, and regional energy projects may affect site feasibility but do not prove a data center.

```text
site:one.org.ma "Dakhla" "poste"
site:one.org.ma "Laayoune" "raccordement"
site:one.org.ma "centre de données"
site:masen.ma "Laayoune" OR "Boujdour" OR "Dakhla"
"Noor Laayoune" "Dakhla" "datacenter"
"autoproduction" "Dakhla" "centre de données"
"500 MW" "Dakhla" "énergies renouvelables" "datacenter"
```

### 1.6 CNDP — Data Protection

Main URL: `https://www.cndp.ma/` (A; reachable). Use CNDP for data-protection/legal context under Morocco-administered practice. CNDP notifications are not facility proof unless they name an operator/site.

```text
site:cndp.ma "hébergement" "Dakhla"
site:cndp.ma "cloud"
site:cndp.ma "centre de données"
"CNDP" "Igoudar" OR "Dakhla" "hébergement"
```

### 1.7 Public Procurement

Morocco procurement: `https://www.marchespublics.gov.ma/` (A route; direct check returned 403). UN procurement: `https://www.ungm.org/` (A; reachable). MINURSO route: `https://minurso.unmissions.org/` and UN Peacekeeping factsheet `https://peacekeeping.un.org/en/factsheet/minurso` (A routes; some access-control from this environment).

```text
site:marchespublics.gov.ma "Igoudar" OR "Dakhla" "datacenter"
site:marchespublics.gov.ma "centre de données"
site:marchespublics.gov.ma "salle informatique" "Laayoune"
site:marchespublics.gov.ma "cloud" "provinces du Sud"
"appel d'offres" "Igoudar Dakhla"
"attribution" "centre de données" "Dakhla"
site:ungm.org "MINURSO" "server"
site:ungm.org "MINURSO" "telecommunications"
site:minurso.unmissions.org "communications"
```

Procurement grading: tender/award = A for the procurement event; facility existence/status remains only what the tender states.

### 1.8 Operators, Certifications, and Cable Routes

| Source / asset | URL | Verified use |
|---|---|---|
| Uptime Institute Morocco list | `https://uptimeinstitute.com/uptime-institute-awards/country/id/MA` | A for awards in Morocco. Search it for Dakhla/Laayoune; absence is not proof of no facility, but no EH award should be inferred without a listed project. |
| Maroc Telecom / IAM | `https://www.iam.ma/` | A only for IAM-authored facts when accessible. Direct check returned 403. Its known data centers are in Morocco proper; any EH “data center” claim needs IAM or official project evidence. |
| Maroc Telecom West Africa submarine cable | IAM official page not found in this review; TeleGeography/Submarine Cable Map and trade coverage list Dakhla as a landing point. | Treat Dakhla landing as B/C connectivity lead unless IAM/operator official evidence is found. Cable landing station is not a data center. |
| WACS cable | `https://wacscable.com/` | A for WACS system existence. Do **not** use WACS as Dakhla evidence; available WACS references do not support a Dakhla landing. |
| ANP / Dakhla Atlantic Port | `https://www.anp.org.ma/` | A for port background when relevant. Port/economic-zone plans are C data-center leads until a named DC facility appears. |
| Equipment Ministry | `https://www.equipement.gov.ma/` | A route when reachable; direct check timed out. Use for roads/ports/building infrastructure context. |

---

## 2. Per-Zone Official Enumeration

### 2.1 Bucket A — Laayoune-Sakia El Hamra

Status baseline: no confirmed operating commercial colo, hyperscale, or public cloud region found in this review. MINURSO presence in Laayoune can generate IT/server-room procurement leads, but these are internal mission facilities unless a data center is explicitly named.

```text
site:cri-invest.ma "Laayoune" "data center"
site:marchespublics.gov.ma "Laayoune" "centre de données"
"Laayoune" OR "Laâyoune" "datacenter"
"Laayoune" "salle serveur" OR "salle informatique"
"العيون" "مركز البيانات"
site:ungm.org "MINURSO" "Laayoune" "server"
site:minurso.unmissions.org "Laayoune" "communications"
```

Checklist before “no confirmed DC”:

- CRI/CRUI and procurement queries run.
- City/province/wilaya pages searched.
- Uptime Morocco list searched for Laayoune/Laâyoune/El Aaiún.
- IAM/ANRT telecom references checked for whether a result is only a network office/technical center.
- UNGM/MINURSO checked for internal IT procurement.

### 2.2 Bucket B — Dakhla-Oued Ed-Dahab

Confirmed official project lead:

| Project | Status | Best evidence | Grade |
|---|---|---|---|
| Igoudar Dakhla / Igoudar Numérique green data-center campus | `planned / studies launched`; not confirmed operational or under construction | MTNRA/MMSP 14 Nov 2025 agreement page; MTNRA/MMSP 14 Apr 2026 partnership convention page | A for announced project, Dakhla location, public parties, and 500 MW target; not A for operation/construction |

Connectivity leads:

- Dakhla landing for **Maroc Telecom West Africa** appears in TeleGeography/Submarine Cable Map and trade coverage, but no IAM primary page was found in this review. Treat as B/C connectivity context until operator confirmation.
- WACS is not a Dakhla landing source; keep WACS only as a regional cable-system reference.

```text
site:mmsp.gov.ma "Igoudar Dakhla"
site:mmsp.gov.ma "Igoudar numérique" "500 mégawatts"
site:cri-invest.ma "Dakhla" "datacenter"
site:marchespublics.gov.ma "Dakhla" "Igoudar"
site:one.org.ma "Dakhla" "raccordement"
site:masen.ma "Dakhla" "énergies renouvelables"
"Dakhla" "Igoudar" "centre de données"
"Dakhla" "data center" "500 MW"
"Dakhla" "Maroc Telecom West Africa" "landing"
"الداخلة" "مركز البيانات" "Igoudar"
```

Checklist before status upgrade:

- Official contract, procurement award, building permit, environmental approval, construction notice, or operator commissioning page found.
- If using 500 MW, tie it to Igoudar/Igoudar Numérique and state it as target capacity.
- Separate campus/project status from any cloud-service availability claim.

### 2.3 Bucket C — East of the Berm / SADR-Polisario Area

No official data-center or telecom-grade infrastructure source was verified. Use SADR/Polisario sources only as attributed claims unless corroborated by UN, operator, or independent evidence.

```text
site:spsrasd.info "data center"
site:spsrasd.info "centre de données" OR "centro de datos"
"SADR" "ICT" "data center"
"Polisario" "telecom" "data center"
"المناطق المحررة" "مركز البيانات"
"Tindouf" "data center"    # Algeria-only background; do not map to EH
```

### 2.4 Bucket D — UN / MINURSO

MINURSO and UNGM are official for mission/procurement facts. They rarely prove a data center; most hits will be server, radio, satellite, IT equipment, or telecom-service procurement.

```text
site:ungm.org "MINURSO" "data centre"
site:ungm.org "MINURSO" "server room"
site:ungm.org "MINURSO" "information technology"
site:ungm.org "MINURSO" "telecommunications"
site:minurso.unmissions.org "IT" OR "communications"
```

---

## 3. Verification Rules

1. Every record must include owner/operator, facility/project name, locality, manifest division (`Western Sahara`), internal bucket, status, evidence URL, and source attribution.
2. Do not create subnational division values such as `Dakhla-Oued Ed-Dahab`; those are internal locality/bucket labels only.
3. Igoudar Dakhla/Igoudar Numérique can be entered as `planned` with A evidence for announcement and 500 MW target. Do not mark `under_construction`, `operational`, or exact campus size unless a later official source says so.
4. Cable landing stations, telecom exchanges, cloud services, training institutes, research centers, ports, and free zones are not data centers unless the source names a data-center facility.
5. Cloud region claims must come from AWS/Azure/GCP/OCI or the cloud provider’s official documentation. EH has no confirmed cloud region in this review.
6. Tier/certification claims require Uptime Institute or operator certificate evidence.
7. WACS must not be used as Dakhla evidence. For Dakhla connectivity, search Maroc Telecom West Africa and seek IAM/operator confirmation.
8. Treat procurement as evidence of procurement only; do not infer delivery, operation, capacity, or address beyond the tender/award.
9. If a URL is indexed but direct access fails due to timeout, TLS, bot block, or 403, keep the URL with `recheck` and do not invent substitutes.
10. Political language must stay attribution-based and neutral: “Moroccan-administered source states…”, “SADR/Polisario source states…”, “UN source states…”.
