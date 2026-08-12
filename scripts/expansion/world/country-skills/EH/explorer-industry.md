# EH Explorer Industry — 西撒哈拉数据中心枚举（行业/贸易媒体/厂商面）

Date: 2026-08-12. 国家/地区: **EH 西撒哈拉（Western Sahara）**. Manifest division model: **single division only** — `["Western Sahara"]`. Scope: industry media, trade media, operator/vendor pages, certification pages, cable maps, directories, and regional media used to discover data-center leads, then cross-check with `EH/explorer-official.md`.

> **政治敏感性说明（事实中立 / neutral factual note）**：西撒哈拉最终地位存在争议；摩洛哥实际管理西部主要地区并在其材料中称为“南部省份”，波利萨里奥阵线/SADR 主张主权，联合国通过 MINURSO 维持任务存在。行业材料经常采用单一政治口径。记录时只标注来源归属和地理事实，不把媒体口径转换为主权判断。

Verified baseline（复核基线）:

- Manifest EH has exactly one division: `Western Sahara`. Any Laayoune/Dakhla/regional labels are locality fields or internal coverage buckets, not division values.
- No confirmed operating commercial colo, hyperscale, or public cloud region in EH was found in this review.
- The strongest current data-center lead is **Igoudar Dakhla / Igoudar Numérique**, now supported by Moroccan ministry pages. It remains `planned / studies launched`, not operating.
- The earlier “WACS Dakhla landing” claim is not supported. WACS official and common cable references list WACS as a Europe-West Africa-South Africa system but not a Dakhla landing. Dakhla connectivity should instead be investigated under **Maroc Telecom West Africa**; current public support found here is secondary cable-map/trade evidence, not IAM primary evidence.

Reliability grades（A/B/C 分级）:

- **A** = primary source for the specific fact: operator/facility page, company press release, official ministry/regulator/procurement/utility page, Uptime Institute award page, official cloud-provider page, official cable-system/operator page.
- **B** = strong secondary: Reuters, Data Center Dynamics, Ecofin Agency, MAP reposts, Medias24, Le360, TelQuel, Yabiladi, credible trade media with named parties and dates.
- **C** = weak lead: DataCenterMap, Datacenters.com, Baxtel, Cloudscene, datacentercatalog.com, datacenterplatform.com, LinkedIn/social posts, unattributed market reports, scrape-only summaries, inaccessible report snippets.

Directories are discovery only. Without A/B support, do not assert status, capacity, certification, or exact address from directory entries.

---

## 0. Market Frame / 市场框架

Western Sahara is a very small and politically sensitive data-center market. The practical search space is split into Morocco-administered coastal cities, UN/MINURSO procurement, and low-confidence SADR/Polisario-side claims.

Current asset posture:

- **Operating commercial colo / hyperscale DC**: none confirmed inside EH.
- **Announced/planned DC**: Igoudar Dakhla / Igoudar Numérique green data-center campus in Dakhla. Moroccan ministry pages support project existence, location, public parties, and target capacity of 500 MW. They do not confirm construction or operation.
- **Connectivity-adjacent**: Dakhla landing for Maroc Telecom West Africa cable is a plausible lead from TeleGeography/Submarine Cable Map and trade coverage; seek IAM/operator confirmation. Cable landing station is not a data center.
- **Nearby Morocco proper**: Casablanca, Rabat, Settat, Benguerir, Nador, Tangier, and Tarfaya are outside EH. Mention only as reference market/context; do not ingest into EH.
- **UN/MINURSO**: IT and telecom procurement can show on-territory technology spend but normally not a data-center facility.
- **SADR/Polisario side**: no verifiable operating data-center source found; use only attributed leads.

Core query set:

```text
"Western Sahara" "data center"
"Sahara occidental" "data center" OR "centre de données"
"Dakhla" "Igoudar" "data center"
"Igoudar Dakhla" "datacenter"
"Igoudar numérique" "Dakhla"
"Dakhla" "500 MW" "data center"
"Dakhla" "centre de données" "500 mégawatts"
"Laayoune" OR "Laâyoune" OR "El Aaiún" "data center"
"Maroc Telecom West Africa" "Dakhla" "landing"
"Dakhla" "submarine cable" "Maroc Telecom"
"MINURSO" "server room" OR "data centre"
```

Arabic and Spanish variants:

```text
"الصحراء الغربية" "مركز البيانات"
"الأقاليم الجنوبية" "مركز البيانات"
"الداخلة" "مركز البيانات" "Igoudar"
"العيون" "مركز البيانات"
"الكابل البحري" "الداخلة" "Maroc Telecom"
"Sáhara Occidental" "centro de datos"
"El Aaiún" "centro de datos"
"Dajla" "centro de datos" OR "centro de procesamiento de datos"
```

---

## 1. High-Signal Source List

| Source | Path | Default grade | Use |
|---|---|---|---|
| Moroccan Digital Transition Ministry / MTNRA-MMSP | `https://www.mmsp.gov.ma/fr` | A | Primary route for Igoudar Dakhla / Igoudar Numérique. |
| Igoudar Dakhla agreement page | `https://www.mmsp.gov.ma/fr/actualites/signature-de-deux-accords-strat%C3%A9giques-%C3%A0-dakhla-dans-les-domaines-de-l%E2%80%99intelligence-artificielle-et-de-la-transition-%C3%A9nerg%C3%A9tique` | A | 14 Nov 2025 official launch agreement for green data centers project. |
| Igoudar Numérique convention page | `https://www.mmsp.gov.ma/fr/actualites/signature-d%E2%80%99une-convention-pour-l%E2%80%99op%C3%A9rationnalisation-du-campus-datacenter-vert-%C2%AB-igoudar-num%C3%A9rique-%C2%BB-%C3%A0-dakhla` | A | 14 Apr 2026 official partnership convention; 500 MW target and study phase. |
| Data Center Dynamics | `https://www.datacenterdynamics.com/en/news/` | B | Dakhla 500 MW reporting, Reuters-derived context, industry framing. Upgrade only when linking to official pages. |
| Reuters | `https://www.reuters.com/` | B | Minister interviews and official/semiofficial announcements. Not facility-primary unless quoting documents directly. |
| Ecofin Agency / Agence Ecofin | `https://www.ecofinagency.com/` / `https://www.agenceecofin.com/` | B | Dakhla project and telecom cable coverage; some pages may 403. |
| Uptime Institute Morocco list | `https://uptimeinstitute.com/uptime-institute-awards/country/id/MA` | A | Certification search. EH has no separate Uptime country route found. |
| Maroc Telecom / IAM | `https://www.iam.ma/` | A when accessible | Operator-owned telecom/data-center facts. Direct access returned 403 in this review. |
| Maroc Telecom West Africa cable | seek IAM/operator page; public secondary: TeleGeography/Submarine Cable Map | B/C until primary found | Dakhla cable landing lead; not data-center proof. |
| WACS official | `https://wacscable.com/` | A for WACS only | Regional cable context. Do not use for Dakhla. |
| UNGM / MINURSO | `https://www.ungm.org/`, `https://minurso.unmissions.org/`, `https://peacekeeping.un.org/en/factsheet/minurso` | A for UN/procurement facts | MINURSO IT/telecom procurement; usually C as facility evidence. |
| Moroccan public procurement | `https://www.marchespublics.gov.ma/` | A route | Tender/award evidence; direct access returned 403 in this review. |
| Regional media: Medias24, Le360, TelQuel, Yabiladi, MAP | respective sites | B | Moroccan-side local reporting. Keep source attribution explicit. |
| WSRW / Sahara Press Service | `https://wsrw.org/`, `spsrasd.info` | B/C depending fact | Political/advocacy or SADR/Polisario-side claims; not facility-primary. |
| Directories | DataCenterMap, Datacenters.com, Baxtel, Cloudscene, SemanticNet/FiberAtlantic, datacentercatalog.com | C | Lead generation and cable/facility hints only. |

Trade-media queries:

```text
site:datacenterdynamics.com/en/news/ "Dakhla" "data center"
site:reuters.com "Dakhla" "data center" "Morocco"
site:ecofinagency.com "Dakhla" "data center"
site:agenceecofin.com "Dakhla" "centre de données"
site:medias24.com "Igoudar" OR "Dakhla" "datacenter"
site:le360.ma "Igoudar" OR "Dakhla" "data center"
site:telquel.ma "Dakhla" "datacenter"
site:yabiladi.com "Dakhla" "data center"
site:map.ma "Igoudar Dakhla"
site:wsrw.org "Dakhla" "data center"
site:spsrasd.info "data center" OR "centro de datos"
```

---

## 2. Facility and Project Leads

### 2.1 Confirmed / primary-supported leads

| Lead | Locality / bucket | Status | Best evidence | Grade guidance |
|---|---|---|---|---|
| Igoudar Dakhla / Igoudar Numérique green data-center campus | Dakhla, bucket B; manifest division `Western Sahara` | `planned / studies launched` | MTNRA/MMSP 14 Nov 2025 and 14 Apr 2026 pages | A for project announcement, Dakhla location, named parties, renewable-energy positioning, and 500 MW target. Not operational/construction evidence. |
| MINURSO Laayoune IT/server-room spend | Laayoune, buckets A/D | mission-internal IT only | UNGM/MINURSO | A for procurement/mission facts; C for data-center facility evidence unless a source names a DC. |

### 2.2 Connectivity and non-DC assets

| Lead | Locality | Status | Evidence | Grade guidance |
|---|---|---|---|---|
| Maroc Telecom West Africa cable landing at Dakhla | Dakhla | connectivity lead | TeleGeography/Submarine Cable Map, Ecofin/trade coverage; seek IAM page | B/C until operator-primary source found; not a data center. |
| WACS | not Dakhla | operating regional cable | WACS official site and cable references | A for WACS system; exclude as EH/Dakhla asset unless a future primary source says otherwise. |
| Dakhla Atlantic Port / economic zone | Dakhla | infrastructure context | ANP, CRI, regional sources | C data-center lead unless a named DC project appears. |
| Maroc Telecom local network sites | Laayoune/Dakhla | telecom infrastructure | IAM/ANRT if found | A for telecom service/site only; C for any data-center inference. |

### 2.3 Exclusions / out-of-scope

| Asset / market | Reason |
|---|---|
| Oracle/N+ONE/Maroc Telecom facilities in Casablanca/Rabat/Settat | Morocco proper, not EH. |
| Benguerir planned or existing data-center/AI assets | Morocco proper, not EH. |
| Nador Medusa cable landing station | Morocco proper, not EH. |
| Tarfaya wind project | Outside EH boundary; energy context only. |
| Xlinks Morocco-UK power project | Morocco proper north of EH; non-DC energy context. |

---

## 3. Enumeration Matrix

| Target type | Sources in order | Default grade | Rule |
|---|---|---|---|
| Operating commercial colo / wholesale | directories -> trade media -> operator pages -> Uptime list | C -> B -> A | Current baseline: none confirmed in EH. |
| Hyperscale / cloud region | cloud-provider official pages, operator announcements | A | No EH cloud region confirmed. |
| Planned green/hyperscale DC | MMSP/MTNRA -> procurement/CRI -> Reuters/DCD/Ecofin | A/B | Igoudar Dakhla is A for planned/project facts; status stays planned/studies. |
| Public-sector DC | procurement, ministry, ADD, CNDP, regional council | A/B | Procurement does not prove operation. |
| Telecom data center / exchange | IAM, ANRT, Uptime, trade media | A/C | Distinguish network office/exchange from DC. |
| Cable landing / connectivity | operator cable pages, cable-system pages, TeleGeography, trade media | A/B/C | Not a data center. Dakhla lead is Maroc Telecom West Africa, not WACS. |
| Power/grid | ONEE, MASEN, project owners | A | Context only unless connected to named DC. |
| UN/MINURSO | UNGM, MINURSO, UN Peacekeeping | A/C | Usually IT procurement or communications, not a DC. |
| SADR/Polisario side | SPS, WSRW, UN, independent reporting | C/B | Attribute source; do not assert infrastructure without corroboration. |

---

## 4. Grading and Ingestion Rules

1. Required fields: owner/operator, project/facility name, locality, manifest division `Western Sahara`, internal bucket, status, source URL, source attribution.
2. Do not ingest Laayoune-Sakia El Hamra or Dakhla-Oued Ed-Dahab as division values; they are internal/admin context only.
3. Igoudar Dakhla/Igoudar Numérique may be ingested as planned with A official evidence. Use `500 MW target capacity` wording, not live IT load.
4. Any claim that Igoudar is under construction, commissioned, Tier-certified, occupied by cloud tenants, or operating needs new primary evidence.
5. Treat Huawei, Reuters, DCD, Ecofin, and regional-media mentions as B unless Huawei or another operator publishes its own project/facility page.
6. Cable landing stations, ports, free zones, fiber routes, and training/research institutes are connectivity or economic context, not DCs.
7. WACS/Dakhla claims should be treated as an error unless backed by a new primary source. Search Maroc Telecom West Africa for the Dakhla cable lead instead.
8. Directory entries cannot establish a data center record by themselves.
9. For blocked or unstable URLs, preserve the original URL with `recheck` and record the access symptom (`403`, timeout, JS/captcha).
10. Political wording must be source-attributed and neutral; do not normalize one party’s territorial terminology into the canonical geography field.
