# Phase 4 Gantt and county-decision synthesis methodology

Frozen cutoff: **2026-07-16**. The artifacts are limited to the four regional Phase 2 JSONs and the 12 accepted Phase 3 county JSONs named below, with the Phase 1 construction-cycle model as the schedule basis. No new web research was performed.

## Outputs

- `gantt_rows.json`: one timeline candidate for each Phase 2/Phase 3 stable ID (186 candidates). Each candidate retains project/company/location/status, raw Phase 2 milestones, every Phase 3 county action as an event, source provenance, and 2024–2030 Gantt spans.
- `county_decision_register.json`: all 513 Phase 3 actions, one record per source action, categorized into `vote, zoning, incentive, permit, environment, water, power, utility, other`.

## Evidence and normalization rules

A source event is `actual` only when it records an action or milestone that occurred on or before the frozen cutoff. Future dates, scheduled-after-cutoff items, and explicitly forecast/target/expected dates are `projection`. Raw dates, date precision, result text, vote tally, body, caveat, case/permit number, stable ID, original action, and URL are preserved.

The normalized stage vocabulary is exactly: `announced, local_process, approved_or_permitted, site_work_or_construction, energized, live_partial, full_buildout`. An announcement is not approval. A zoning referral, moratorium, incentive/bond authorization, utility docket, or land purchase cannot create a construction anchor. Permit and utility actions remain their own evidence gates. The machine validator requires construction tails to originate only from explicit construction/site-work, energization, or live-service evidence.

Candidate-level `normalized_status` is the strongest non-projected actual event stage for that stable ID, including the source-backed cutoff `status_snapshot`. Projection events and modeled spans never advance the candidate status.

For county actions, `normalized_category` is a single primary subject category. Water/environmental terms are separated before power/utility, then incentives, permits, zoning, and general votes; unclassifiable records remain `other`. The original action object is retained in `original_action`.

## Schedule and Gantt conventions

Actual event markers use `evidence_state=actual`, `projection=false`, and solid rendering. Explicit target/forecast markers use `evidence_state=projection`, retain their stated date and basis, and use dashed rendering. Modeled spans are uncertainty ranges, not completion claims; they carry `duration_min_months`, `duration_max_months`, `uncertainty_start`, `uncertainty_finish`, basis, confidence, and source URLs. All modeled spans are dashed so uncertainty cannot be mistaken for observed completion; low-confidence projections are therefore visibly dashed.

When a project has an explicit construction/site-work anchor but no verified end or first usable capacity, the selected Phase 1 archetype is applied conservatively from the first observed construction evidence. The full-buildout range begins only after the modeled or actual first usable phase. If energized but not live, the Phase 1 S13 0–3 month first-usable allowance is used. If a live/ready-for-service milestone is actual, it supersedes the first-usable projection, while the remaining full-buildout tail stays projected unless full campus buildout is explicitly evidenced. No construction bar is inferred for announcement-only, land-only, zoning-only, incentive-only, or utility-only records.

Bounded QA repair: five candidates whose cutoff `status_snapshot` was stronger than the candidate-level status were promoted to the strongest actual stage. `SC-004` was separately reviewed. Its commercial source records project advancement and York County site-preparation support, but the available Phase 2/3 text does not explicitly verify site preparation itself, building approval, completion, energization, or service. The prior SC-004 construction anchor was therefore removed, its site-preparation-support events were normalized to `approved_or_permitted`, and the construction-derived modeled tails were removed. Raw source objects were not altered.

The four archetypes and ranges are copied from `phase1/construction_cycle.json`: fast-track powered corridor (18–30 months to first usable; 12–24 months to full buildout), base-case greenfield (24–42; 18–36), constrained greenfield (36–60; 24–60), and powered-shell expansion (9–18; 6–24). These are planning ranges, intentionally overlapping, and not additive forecasts.

The 2024–2030 window is a display window. Events outside it remain in the candidate event history and the decision register; window clipping is recorded in each span's `gantt_start`, `gantt_finish`, and `in_gantt_window` fields.

## Mechanical validation performed

- Timeline candidates: 186; expected 186; Phase 2 and Phase 3 stable-ID sets are exact matches.
- County actions: 513; expected 513; action occurrence keys and URLs are retained; category counts are `{"environment": 85, "incentive": 67, "other": 50, "permit": 111, "power": 15, "utility": 31, "vote": 56, "water": 38, "zoning": 60}`.
- Candidate status counts after bounded QA repair: `{"announced": 27, "local_process": 45, "approved_or_permitted": 69, "site_work_or_construction": 39, "energized": 1, "live_partial": 4, "full_buildout": 1}`.
- Allowed normalized stages/statuses: checked against the seven-value vocabulary above.
- Event ordering: dated events sort by effective date, with undated records retained last; modeled spans have ordered starts/finishes and window clipping checks.
- Projection labeling: every projection is explicitly labeled, has a non-empty basis and confidence, and uses dashed rendering; actual markers are not projections.
- Provenance: every Phase 2 milestone and Phase 3 action has source URL provenance; the top-level URL manifest is a recursive union of all HTTP(S) URLs in the selected Phase 2/3 JSON inputs. No stable IDs, action occurrences, or input URLs are dropped.
- Construction safety: modeled construction tails are emitted only when an explicit construction/site-work, energization, or live-service anchor exists; no announcement, zoning referral, moratorium, incentive/bond authorization, utility docket, or land purchase alone is accepted as a construction anchor.
- Parent QA receipt: `phase4/parent_gantt_validation.json` was preserved unchanged at SHA-256 `c07c761c0f7f386b2eb057911db4a5a818b88d9f6a8a5dd52067b6bf7e1b3b47`.

## Input files and SHA-256

- `workspace/oracle_openai_datacenters_20260716/research_brief.md` — `1e5770c3a072026eef7ad9ed03fb2a8d96228c68c105d74f99b9ef56b88bdac3`
- `workspace/oracle_openai_datacenters_20260716/phase1/construction_cycle.json` — `299bbdba0b5827c52a4bd29c751a2d426ce8a9a5d0afa05da101ab0726f6fd07`
- `workspace/oracle_openai_datacenters_20260716/phase1/construction_cycle.md` — `9ccdbd84c200a1ffaa994bf886c2c677689efb1ddaf3d9000741346a7adb8e07`
- `workspace/oracle_openai_datacenters_20260716/phase2/region_midatlantic_southeast.json` — `860d7f0767153f5cf8db10959615a73694ba0c07bea3084e3255f66646be10d5`
- `workspace/oracle_openai_datacenters_20260716/phase2/region_midwest_greatlakes.json` — `2dfb0467930a8c9cfdb1b79a70577cc1b429ac6935b72d2a62da7b719ee53213`
- `workspace/oracle_openai_datacenters_20260716/phase2/region_southwest_mountain.json` — `dc542cc2f57000c502c45ecf22d77d687e0e710823f552a3239aad3b6ef3e760`
- `workspace/oracle_openai_datacenters_20260716/phase2/region_west_northeast_remaining.json` — `d30fb209cd2b94629ab558779a225bbe79fa5ea60e8e687a7dfea8ae4c8cf761`
- `workspace/oracle_openai_datacenters_20260716/phase3/county_ak_hi_me_ma_nh_ri.json` — `6176a047977262d2757d81ff2f1b19e4a487621809bd625a5c9affe8f52b8252`
- `workspace/oracle_openai_datacenters_20260716/phase3/county_ca_or.json` — `fe2871511350314fc6def703a4dcfb0781525253e99993206673f60edd1b1257`
- `workspace/oracle_openai_datacenters_20260716/phase3/county_co_id_mt_nv_nm_wy.json` — `80e8fe8fe4a263e4f039d18e89fcb2b43ad692026fff14294df99b90edee3062`
- `workspace/oracle_openai_datacenters_20260716/phase3/county_ga_nc_sc.json` — `a3ec5aa7247580c397759f16b740ce81841350d3b640e81feef503625741aac9`
- `workspace/oracle_openai_datacenters_20260716/phase3/county_ia_il_mi_wi.json` — `717bc9940df202f270e9c0fa0c32f448d962b772d39f348360a741ddcc84fe0d`
- `workspace/oracle_openai_datacenters_20260716/phase3/county_ks_mn_mo_nd_sd.json` — `82d517cf404f8afec1a3a5d9f3e41720b8b9bd6bc8d264ef1a4ba8f7376480bf`
- `workspace/oracle_openai_datacenters_20260716/phase3/county_ms_al_la_ar_tn_ky.json` — `0bd7d74de0673dc5b5af0e64821bdee1ad5ae8d97dbe876582107b6c6d6b8962`
- `workspace/oracle_openai_datacenters_20260716/phase3/county_oh_in.json` — `408cb9aef20a0fc637bec7c4b5f25badc1c171e36d818b164af2f93b85e03256`
- `workspace/oracle_openai_datacenters_20260716/phase3/county_ok_az_ut.json` — `86dacb6b374387c6efa95a02f295163300c5298a50d2dd0ee0947d1b840f2329`
- `workspace/oracle_openai_datacenters_20260716/phase3/county_pa_nj_ny_wa.json` — `4ed724673394fb9b66cfdb913449c8b64a3e2dac3a61029214a8c1d1fbdf42d0`
- `workspace/oracle_openai_datacenters_20260716/phase3/county_tx.json` — `1752d2751d0777649002dcb98a24b153de1ea826afc6a469bd9cdc3ce1d018fe`
- `workspace/oracle_openai_datacenters_20260716/phase3/county_va_md_wv.json` — `d0411dcdb39a06773cccceca146bc311700ed6cde2d00bc20c05ea51969186bd`

## Output hashes

- `phase4/gantt_rows.json` — `dfc9173a74c81824f9df11dcd4c441bb8199637553d33be5cafc361d796903eb`
- `phase4/county_decision_register.json` — `f62d202e51bb02f82c8ecf684dd3f0fa87af26efcbc24d15f01cfa553b4180c7`

The SHA-256 of this methodology file is reported in the completion handoff after final validation; it is not embedded here to avoid a self-referential hash.
