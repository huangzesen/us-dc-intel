# Phase 4 source/conflict audit

Cutoff: 2026-07-16. This is an independent read-only QA pass over the research brief and all 42 Phase 1–3 JSON/Markdown artifacts. The machine-readable companion is [source_conflict_audit.json](/Users/huangzesen/work/projects/find_a_job/.lingtai/codex/workspace/oracle_openai_datacenters_20260716/phase4/source_conflict_audit.json).

## Outcome

The 186 accepted Phase 3 stable IDs reconcile exactly, one-to-one, with the four regional Phase 2 sets. There are no duplicate stable IDs or exact normalized aliases. All 513 action URLs and 452 present project source URLs are syntactically valid, and all 186 IDs plus all 513 action URLs are covered by the corresponding Phase 3 Markdown.

There is one blocker: the requested 2024–2030 Gantt is not represented as a comprehensive schedule for the 186 accepted projects. Phase 1 contains seven observed benchmark projects and 20 milestones only. The final HTML must not present that schedule as an all-project Gantt without adding a stable-ID crosswalk and project bars, or explicitly disclosing the limited seven-project scope.

There are 13 material findings. They concern date precision, schema normalization, source-tier reproducibility, missing project-level source lists, one confirmed date error, unresolved phase crosswalks, capacity scope/unit conflicts, building-count scope, and possible double-counting identities. The artifacts themselves already caveat withdrawals, moratoria, referrals, utility proceedings, tax incentives, and company announcements in the reviewed examples; no demonstrated company/reporting action was found mislabeled as a government action.

## Mechanical checks

| Check | Result |
|---|---|
| Phase 3 projects / unique IDs | 186 / 186 |
| Four regional Phase 2 projects / unique IDs | 186 / 186 |
| Phase 3 ↔ regional Phase 2 ID differences | 0 / 0 |
| Duplicate IDs / exact normalized alias groups | 0 / 0 |
| Exact city/county/state collision groups | 6; not demonstrated duplicates |
| Phase 3 actions / valid action URLs | 513 / 513 |
| Present project source URLs / valid | 452 / 452 |
| Actual URL fields across all input JSON / invalid | 1,640 / 0 |
| Phase 3 IDs and action URLs in Markdown | 186 / 186; 513 / 513 |
| Phase 3 files with exact action-count markers | 7 of 12 |
| Rows without project-level `source_urls` | 38, all in Ohio/Indiana and PA/NJ/NY/WA files |
| Phase 2 source records / distinct domains | 356 / 212 |
| Phase 2 tier mix | T1 121, T2 94, T3 78, T4 60, T5 3 |

The six location collisions are Abilene/Taylor TX, Delta/Millard UT, Eagle Mountain/Utah UT, Mesa/Maricopa AZ, Niagara Falls/Niagara NY, and Tulsa/Tulsa OK. They are retained as QA notes, not duplicate findings, because the supplied records identify different names or owners and do not demonstrate identity duplication.

## Findings

### F4-001 — blocker: Gantt coverage

The brief requests an evidence-backed 2024–2030 Gantt ([research_brief.md:4](/Users/huangzesen/work/projects/find_a_job/.lingtai/codex/workspace/oracle_openai_datacenters_20260716/research_brief.md:4)). The Phase 1 construction-cycle JSON has only seven `observed_projects` and 20 milestones ([construction_cycle.json:80](/Users/huangzesen/work/projects/find_a_job/.lingtai/codex/workspace/oracle_openai_datacenters_20260716/phase1/construction_cycle.json:80)); it supplies no bar/crosswalk for the 186 Phase 3 projects. Final HTML must disclose this limitation or add the missing evidence-backed schedule. Do not call the seven-project schedule comprehensive.

### F4-002 — material: action date precision

154 of 513 actions lack a declared accepted precision: 150 omit `date_precision` and four use custom values (`undated_web_page`, `undated_register_entry`, `snapshot`). Eleven actions are null or explicitly undated. Exact examples include the null/`undated_web_page` action at [county_ia_il_mi_wi.json:324](/Users/huangzesen/work/projects/find_a_job/.lingtai/codex/workspace/oracle_openai_datacenters_20260716/phase3/county_ia_il_mi_wi.json:324), two null/`undated_register_entry` actions at [county_oh_in.json:23](/Users/huangzesen/work/projects/find_a_job/.lingtai/codex/workspace/oracle_openai_datacenters_20260716/phase3/county_oh_in.json:23) and :72, and month-only/undated `action_date` records at [county_pa_nj_ny_wa.json:45](/Users/huangzesen/work/projects/find_a_job/.lingtai/codex/workspace/oracle_openai_datacenters_20260716/phase3/county_pa_nj_ny_wa.json:45) and :103. Texas actions have dates but no precision field. Normalize to day/month/year/undated or unknown, retain `date_text`, and never invent a day. Final HTML must disclose if these values drive the Gantt.

### F4-003 — material: construction-cycle schema

The declared Gantt enums in `construction_cycle.json.gantt_schema.required_fields` do not match the observed values. There are 24 enum violations across 20 milestones, including `official_release`, `developer_release`, `forecast_at_source_date`, `actual_statement`, `announcement`, and approximation labels; all 20 milestones omit the schema’s `evidence_note`. Normalize to the declared enums while preserving the original label in evidence notes. This is a data-quality issue, not a reason to invent precision.

### F4-004 — material: source tiers are not reproducible across phases

The Phase 2 regional files mix string tiers (`"T1"`) and numeric tiers (`1`) at `projects[*].sources[*].tier`; see [region_midatlantic_southeast.json](/Users/huangzesen/work/projects/find_a_job/.lingtai/codex/workspace/oracle_openai_datacenters_20260716/phase2/region_midatlantic_southeast.json) versus [region_midwest_greatlakes.json](/Users/huangzesen/work/projects/find_a_job/.lingtai/codex/workspace/oracle_openai_datacenters_20260716/phase2/region_midwest_greatlakes.json). Phase 3 action and project URLs have no per-source tier linkage. Normalize the field and report the current tier mix as Phase 2-only unless provenance is carried into Phase 3. Final HTML must disclose that limitation if it presents tier statistics.

### F4-005 — material: missing project-level source lists

All 19 rows in `phase3/county_oh_in.json` and all 19 rows in `phase3/county_pa_nj_ny_wa.json` lack `projects[*].source_urls`. Their action-level primary URLs are present and valid, so this is not absence of evidence; it is non-uniform row-level traceability. Derive project lists from action URLs before claiming uniform project-source coverage, and disclose the derivation in final HTML.

### F4-006 — material: Applied Digital Ellendale date

Phase 2 records `ND-ELLENDALE-APPLIED-POLARIS-FORGE` government inspection as 2026-03-19 at [region_midwest_greatlakes.json:63](/Users/huangzesen/work/projects/find_a_job/.lingtai/codex/workspace/oracle_openai_datacenters_20260716/phase2/region_midwest_greatlakes.json:63). Phase 3’s important correction says the official release is 2025-03-19 and identifies 2026-03-19 as unsupported ([county_ks_mn_mo_nd_sd.json:22](/Users/huangzesen/work/projects/find_a_job/.lingtai/codex/workspace/oracle_openai_datacenters_20260716/phase3/county_ks_mn_mo_nd_sd.json:22)); its action is dated 2025-03-19 at :272. Use 2025-03-19 and remove the erroneous duplicate date. Final HTML must disclose the correction if the Phase 2 date was rendered.

### F4-007 — material: Frontier phase/date crosswalk

Phase 1 lists TDLR registration `TABS2026024088` with 2025-10-30 start and 2027-04-19 completion and separately notes Oracle’s 1H27 delivery statement ([global_site_inventory.json:83](/Users/huangzesen/work/projects/find_a_job/.lingtai/codex/workspace/oracle_openai_datacenters_20260716/phase1/global_site_inventory.json:83), :99). Phase 3 Texas lists TDLR registration `TABS2026024110` with 2026-09-04 start and 2028-04-18 completion and says it is not a local building permit ([county_tx.json:58](/Users/huangzesen/work/projects/find_a_job/.lingtai/codex/workspace/oracle_openai_datacenters_20260716/phase3/county_tx.json:58)). Keep them as separate candidate phases/buildings until an address/owner crosswalk exists; do not merge into one bar or equate registration completion with energization. Final HTML must disclose.

### F4-008 — material: EdgeCore Mesa unit/ID conflict

The national seed assigns 1,900 MW to `US-AZ-EDGECORE-MESA-EXPANSION-2024` ([national_all_company_seed.json:40](/Users/huangzesen/work/projects/find_a_job/.lingtai/codex/workspace/oracle_openai_datacenters_20260716/phase2/national_all_company_seed.json:40)). The regional accepted ID `US-AZ-EDGECORE-MESA-2024` has null MW and says the evidence supports $1.9B and 2.1M square feet, not 1.9 GW ([region_southwest_mountain.json:34](/Users/huangzesen/work/projects/find_a_job/.lingtai/codex/workspace/oracle_openai_datacenters_20260716/phase2/region_southwest_mountain.json:34)). Keep MW null, preserve investment, and resolve the ID crosswalk before aggregation. Final HTML must disclose any seed value shown.

### F4-009 — material: Core Scientific Muskogee capacity/status

The seed reports `US-OK-CORE-SCIENTIFIC-MUSKOGEE-2025` at 1,500 MW and “under construction” ([national_all_company_seed.json:898](/Users/huangzesen/work/projects/find_a_job/.lingtai/codex/workspace/oracle_openai_datacenters_20260716/phase2/national_all_company_seed.json:898), :903). Regional and county evidence under a different ID supports a 100 MW phase and 82.5 MW follow-on, with no energization/CO verified ([region_southwest_mountain.json:25](/Users/huangzesen/work/projects/find_a_job/.lingtai/codex/workspace/oracle_openai_datacenters_20260716/phase2/region_southwest_mountain.json:25)). Render only the evidenced staged capacities and do not label 1,500 MW live or committed. Final HTML must disclose.

### F4-010 — material: Joule and Creekstone scope conflict

For Joule, Phase 2 distinguishes 455 MW Phase 1 under construction from a 4,000+ MW proposed full buildout ([region_southwest_mountain.json:49](/Users/huangzesen/work/projects/find_a_job/.lingtai/codex/workspace/oracle_openai_datacenters_20260716/phase2/region_southwest_mountain.json:49)). For Creekstone, it distinguishes 220 MW Phase 1 from a 2 GW tracker figure and 9,700+ MW proposed expansion ([region_southwest_mountain.json:50](/Users/huangzesen/work/projects/find_a_job/.lingtai/codex/workspace/oracle_openai_datacenters_20260716/phase2/region_southwest_mountain.json:50)); Phase 3 preserves those distinctions. Use separate phase and ultimate-buildout fields; never render full-campus values as current construction or sum them. Final HTML must disclose.

### F4-011 — material: AWS Boardman building count

Phase 2 says `US-OR-AWS-BOARDMAN-2024` is a five-building expansion ([region_west_northeast_remaining.json:58](/Users/huangzesen/work/projects/find_a_job/.lingtai/codex/workspace/oracle_openai_datacenters_20260716/phase2/region_west_northeast_remaining.json:58)). Phase 3 says that description is inconsistent with county findings and records four data-center buildings plus support buildings ([county_ca_or.json:473](/Users/huangzesen/work/projects/find_a_job/.lingtai/codex/workspace/oracle_openai_datacenters_20260716/phase3/county_ca_or.json:473), :504). Use the county-approved scope for government reporting; disclose the five-versus-four distinction.

### F4-012 — material: Anthem/Meta Tulsa possible duplicate

Meta Tulsa’s Phase 2 row aliases “Meta Project Anthem / east Tulsa” ([region_southwest_mountain.json:26](/Users/huangzesen/work/projects/find_a_job/.lingtai/codex/workspace/oracle_openai_datacenters_20260716/phase2/region_southwest_mountain.json:26)). The separate Anthem row carries an unverified 800 MW trade figure, no primary record, and explicitly warns it may be an alias/misattribution ([region_southwest_mountain.json:32](/Users/huangzesen/work/projects/find_a_job/.lingtai/codex/workspace/oracle_openai_datacenters_20260716/phase2/region_southwest_mountain.json:32)). Hold Anthem as an unresolved lead and do not add 800 MW to Meta or count a second campus. Final HTML must disclose.

### F4-013 — material: Related/CoreWeave versus Project Jade/Tembo

The Cheyenne records are 302 MW Related/CoreWeave and 2,700 MW Google/Jupiter Star Project Jade/Tembo, with Phase 2 explicitly requiring a parcel crosswalk ([region_southwest_mountain.json:70](/Users/huangzesen/work/projects/find_a_job/.lingtai/codex/workspace/oracle_openai_datacenters_20260716/phase2/region_southwest_mountain.json:70), :71). Phase 3 keeps them separate pending that crosswalk and says not to merge ([county_co_id_mt_nv_nm_wy.json:1066](/Users/huangzesen/work/projects/find_a_job/.lingtai/codex/workspace/oracle_openai_datacenters_20260716/phase3/county_co_id_mt_nv_nm_wy.json:1066), :1204). Do not sum 302 MW and 2,700 MW or infer Jade construction from Related. Final HTML must disclose.

### F4-014 — material: Tract Tripletail versus Pole Canyon/Pony

Tract Tripletail is reported at 7,000 MW ultimate scale, while Pole Canyon/Pony is 1,820 MW proposed; Phase 2 explicitly says possible overlap and prohibits summing without a parcel crosswalk ([region_southwest_mountain.json:47](/Users/huangzesen/work/projects/find_a_job/.lingtai/codex/workspace/oracle_openai_datacenters_20260716/phase2/region_southwest_mountain.json:47), :57). Phase 3 retains both as proposed leads without resolving the parcel identity. Do not aggregate or present them as independent campuses until cross-walked. Final HTML must disclose.

## Resolution rules for final rendering

Use facts and projections as separate fields. Government approval, company announcement, tax incentive, utility proceeding, referral, withdrawal, moratorium, registration, groundbreaking, construction, completion, and energization must remain distinct events. For unresolved identities, retain provenance but do not sum capacities. For month-only or undated evidence, preserve the textual date and use an explicit precision/unknown marker.

## Input hashes

SHA-256 group hashes are recorded in the JSON companion: Phase 1 `d786428fe4615d1432a62d97f34d461449968c31705c5c93ed0a9639f7a273e1`, Phase 2 `ffb6d77fd1369b5409ca751711bcd105bfa9b7538df4da8b876bfba7077f4039`, Phase 3 `7afb430039ecb1d984e3e19e1176069e70b72094b64f8d5d31b1bd78628ef08c`, brief `1e5770c3a072026eef7ad9ed03fb2a8d96228c68c105d74f99b9ef56b88bdac3`, and all-input manifest `f77dff721d80896509b98867cfc985ccaba25322539bf3330b4cc3d2361b4c51`.
