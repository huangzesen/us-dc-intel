# Final report build handoff

- Artifact: `us_data_center_construction_panorama.html`
- Frozen cutoff: `2026-07-16`
- Generation: deterministic local rendering from accepted frozen artifacts; no new web research and no external communication.

## Counts and decisions

- 208 unique project masters = 185 detailed Phase3/region physical records + 23 retained Phase2 seed-only evidence-gap records.
- 186 accepted Gantt candidates = 185 physical rows rendered by default + 1 DAF solicitation without a selected physical project; the DAF is excluded from physical project counts.
- The unique exclusion set is one DAF solicitation plus four aggregate/undisclosed seed records; six ledger mappings preserve the DAF in both Phase2 and Phase3.
- 1,072 Gantt events; 131 projected spans; 38 construction anchors; 513 county/city/state/utility actions.
- 51 jurisdictions; zero-result CT, DC, DE, FL, NE, VT. 8 live-only baselines and 53 announced/evidence-gap appendix rows are appendix-only.
- Status labels remain separate: announced, local process, approved-permitted, site work-construction, energized, partial live, full buildout. Actual evidence is solid; projection/model tails are dashed.
- Master IDs are unique. Unresolved Tulsa Anthem/Meta, Cheyenne Related/CoreWeave vs Project Jade, and Eagle Mountain Tripletail vs Pole Canyon/Pony remain separate and are not summed.
- Corrections applied in the accepted inputs are disclosed: ND inspection 2025-03-19; Frontier Odessa/Abilene separate; EdgeCore Mesa $1.9B is not 1,900 MW; Muskogee 100 MW + 82.5 MW follow-on; Utah phase vs ultimate scope; Boardman four data buildings plus support structures; SC-004 QTS York approved/permitted with no construction anchor.

## Source/provenance coverage

- Phase3 is authoritative; Phase2 regional records are enrichment; seed-only rows remain labeled as evidence gaps.
- 667/667 unique project URLs retained in master or exclusion ledger; 513/513 action URLs valid; 452/186 present project-source URL metric is the accepted source-conflict audit metric (452 URLs across 186 project rows). 38 rows lack a project-level `source_urls` field and are linked from their action URLs in the final HTML.
- Phase2-only source tier mix: T1 121, T2 94, T3 78, T4 60, T5 3 across 356 Phase2 source records / 212 domains. This is not presented as Phase3 tier statistics.

## Exact source files

- `phase1/construction_cycle.json` — `299bbdba0b5827c52a4bd29c751a2d426ce8a9a5d0afa05da101ab0726f6fd07`
- `phase1/construction_cycle.md` — `9ccdbd84c200a1ffaa994bf886c2c677689efb1ddaf3d9000741346a7adb8e07`
- `phase1/global_site_inventory.json` — `5ec71ec88265e62c3b235ecad7efcd6af462ecf6b2ad030775cefe46ce47557b`
- `phase1/global_site_inventory.md` — `2c30d1ba8f6d03bf2277b408e7f06754ff063e900f25e9ed49e06cc0a250dbd2`
- `phase1/international_and_nonstargate.json` — `bab0bad98ff23aea240a6be733f01249566f89f6d57c0226dd15319808ce28a3`
- `phase1/international_and_nonstargate.md` — `672fc7185db5222366dae5cda0ded443cedf3edae8566f7dd21849e535fdc82b`
- `phase1/us_county_vote_map.md` — `a30d5e9613c6c00f84f864fd9bc61c6892d2ee739e46ef67f6fd3a3f4b642a2a`
- `phase2/national_all_company_seed.json` — `30d34a113377ff80bfb5a55d1299420b9e6dd74f7b782c808c6c028fdf37a699`
- `phase2/national_all_company_seed.md` — `bcd7c2a38092da547a02d9540409ac506a8f723d1f564942e2c44c7738a6bf38`
- `phase2/region_midatlantic_southeast.json` — `860d7f0767153f5cf8db10959615a73694ba0c07bea3084e3255f66646be10d5`
- `phase2/region_midatlantic_southeast.md` — `27ee266672fee3ded01e9525be732fe748e9c9801670025a666abdf1c63a4739`
- `phase2/region_midwest_greatlakes.json` — `2dfb0467930a8c9cfdb1b79a70577cc1b429ac6935b72d2a62da7b719ee53213`
- `phase2/region_midwest_greatlakes.md` — `fe814152f9c9e581d5be7b31869501f53aa87cd5c8fd186b157b86a6b406e309`
- `phase2/region_southwest_mountain.json` — `dc542cc2f57000c502c45ecf22d77d687e0e710823f552a3239aad3b6ef3e760`
- `phase2/region_southwest_mountain.md` — `b40610e44f0b382d18344e08cacb5a8fbd34e8a660be16523d2a223f64d5369c`
- `phase2/region_west_northeast_remaining.json` — `d30fb209cd2b94629ab558779a225bbe79fa5ea60e8e687a7dfea8ae4c8cf761`
- `phase2/region_west_northeast_remaining.md` — `75baf65cfc5e5fc6f2977f977094dd311fb81231148e42bdfd065c3544ce58b3`
- `phase3/county_ak_hi_me_ma_nh_ri.json` — `6176a047977262d2757d81ff2f1b19e4a487621809bd625a5c9affe8f52b8252`
- `phase3/county_ak_hi_me_ma_nh_ri.md` — `358c58382c8f00ed6ee820d3895f3c8ec3b228f26beb0b48c918c0d69fff3178`
- `phase3/county_ca_or.json` — `fe2871511350314fc6def703a4dcfb0781525253e99993206673f60edd1b1257`
- `phase3/county_ca_or.md` — `63d93dd102bdaa7519828d287df4b35079fbfb9fc4ecd5848ddbaf3d49df697e`
- `phase3/county_co_id_mt_nv_nm_wy.json` — `80e8fe8fe4a263e4f039d18e89fcb2b43ad692026fff14294df99b90edee3062`
- `phase3/county_co_id_mt_nv_nm_wy.md` — `3699086fe1925d491215e4c92cdc8a2d4c493d14e8614ba3306a572bf4afc9cd`
- `phase3/county_ga_nc_sc.json` — `a3ec5aa7247580c397759f16b740ce81841350d3b640e81feef503625741aac9`
- `phase3/county_ga_nc_sc.md` — `ac4c1277f3f2fba7129382d44a63dde293736ba11fe2012b5e950553c5e20619`
- `phase3/county_ia_il_mi_wi.json` — `717bc9940df202f270e9c0fa0c32f448d962b772d39f348360a741ddcc84fe0d`
- `phase3/county_ia_il_mi_wi.md` — `51f53c508e210aa1b9f505ba525cea93f326fe5cb58952c0dfc44eabe601e1b9`
- `phase3/county_ks_mn_mo_nd_sd.json` — `82d517cf404f8afec1a3a5d9f3e41720b8b9bd6bc8d264ef1a4ba8f7376480bf`
- `phase3/county_ks_mn_mo_nd_sd.md` — `d9300ab4887a9705020901c7a08d7f8f666fb09feb31deec5c96293e7ee76c50`
- `phase3/county_ms_al_la_ar_tn_ky.json` — `0bd7d74de0673dc5b5af0e64821bdee1ad5ae8d97dbe876582107b6c6d6b8962`
- `phase3/county_ms_al_la_ar_tn_ky.md` — `702a67ac87571455e1f2419c8619f118fdc5c14810f9911ea8893e97427ea2f1`
- `phase3/county_oh_in.json` — `408cb9aef20a0fc637bec7c4b5f25badc1c171e36d818b164af2f93b85e03256`
- `phase3/county_oh_in.md` — `4e3712fb7c34c436a0df858d578200907f0f5aff5a1f0e651df561e8b4399178`
- `phase3/county_ok_az_ut.json` — `86dacb6b374387c6efa95a02f295163300c5298a50d2dd0ee0947d1b840f2329`
- `phase3/county_ok_az_ut.md` — `5076d2c23ddc4c9bb95d0186c1d34d9a46231ba6a6b4de86cb4b58962379e759`
- `phase3/county_pa_nj_ny_wa.json` — `4ed724673394fb9b66cfdb913449c8b64a3e2dac3a61029214a8c1d1fbdf42d0`
- `phase3/county_pa_nj_ny_wa.md` — `af076e3aa2a8ba7aae81221f0be7e95b4364a064ec157beb33c0c44d63598e15`
- `phase3/county_tx.json` — `1752d2751d0777649002dcb98a24b153de1ea826afc6a469bd9cdc3ce1d018fe`
- `phase3/county_tx.md` — `8f318ee95764a7a11941d378684d069c3bbc7439a188ecfe4f745255a066160f`
- `phase3/county_va_md_wv.json` — `d0411dcdb39a06773cccceca146bc311700ed6cde2d00bc20c05ea51969186bd`
- `phase3/county_va_md_wv.md` — `5501346bf28eeaf972d730704079b3f322b252141d06d460354cb79c053af873`
- `phase4/completeness_appendix.json` — `f7627af08d1f79772d289d6ca90e5ee0ceec4b6ddfd26125e757425ab7f0cd64`
- `phase4/completeness_appendix.md` — `43899cdf43c199ce5534282456a428005f4e31a84ebe0bc80e1cb04378a24d2c`
- `phase4/county_decision_register.json` — `f62d202e51bb02f82c8ecf684dd3f0fa87af26efcbc24d15f01cfa553b4180c7`
- `phase4/dedupe_ledger.json` — `9484ab2dc20d8b02ecd48ce9919919ee22be9e91fef2da5cd33927a8c5d7f95c`
- `phase4/gantt_methodology.md` — `cacbcbbcec390d4cd5027c5d1b4f0cb02ede6a5025e40121f412506ba7ff5015`
- `phase4/gantt_rows.json` — `dfc9173a74c81824f9df11dcd4c441bb8199637553d33be5cafc361d796903eb`
- `phase4/national_master_inventory.json` — `2113de4b0a3455288dc010fcf731fca2aa127d7faa02cfd7418950716b1d1b9a`
- `phase4/national_master_inventory.md` — `43d8017019f40a29f1d5f17ab39ee666317d69fccb47f26c6fde00e184b7a0b9`
- `phase4/parent_gantt_validation.json` — `c07c761c0f7f386b2eb057911db4a5a818b88d9f6a8a5dd52067b6bf7e1b3b47`
- `phase4/parent_gantt_validation_v2.json` — `9f608e1900b5a9949062bddece0166ff60eb226e7ee0df65f277575d47036aa4`
- `phase4/parent_master_validation.json` — `0312d3c51ee0c96c32b3d3256ab57254f8569818cd6f705cf26f23a3125c5032`
- `phase4/parent_master_validation_v2.json` — `8a3e2f73cd343071c319f971a5202524f0704fc7933f61f44944f6988780e5e6`
- `phase4/source_conflict_audit.json` — `52f00fd4fbf1626dd8e95987e3cd966f0a7379f3cc5ed2364283379c3aabd07f`
- `phase4/source_conflict_audit.md` — `8c06be42bb99ee80cb6c446bc6d2c2d79803f0d31538e8e9b5ff427c877d048c`
- `research_brief.md` — `1e5770c3a072026eef7ad9ed03fb2a8d96228c68c105d74f99b9ef56b88bdac3`
- `us_county_vote_map.json` — `ae1dfd57114af450e11cc0dd87db75b4e1abd2100ef4362ed7cb10f9eceef77f`
- `watch_state.json` — `b863f842569429737f72167466ec57886aabb70974e8bbe1d3a716073dd303f6`

## Key Phase4 receipt hashes

- `national_master_inventory.json` — `2113de4b0a3455288dc010fcf731fca2aa127d7faa02cfd7418950716b1d1b9a`
- `dedupe_ledger.json` — `9484ab2dc20d8b02ecd48ce9919919ee22be9e91fef2da5cd33927a8c5d7f95c`
- `gantt_rows.json` — `dfc9173a74c81824f9df11dcd4c441bb8199637553d33be5cafc361d796903eb`
- `county_decision_register.json` — `f62d202e51bb02f82c8ecf684dd3f0fa87af26efcbc24d15f01cfa553b4180c7`
- `parent_master_validation_v2.json` — `8a3e2f73cd343071c319f971a5202524f0704fc7933f61f44944f6988780e5e6`
- `parent_gantt_validation_v2.json` — `9f608e1900b5a9949062bddece0166ff60eb226e7ee0df65f277575d47036aa4`

## Output SHA-256

- `us_data_center_construction_panorama.html` — `adeb9eafe73dbaa190fa88c3aec490c8551b84845709b1860213ae5c45abcfb6`

## QA

- JSON parse: PASS for every frozen `*.json` under the workspace (excluding new `final/` output).
- HTML parser: PASS (`html.parser`).
- Inline data parse: PASS; 208 master IDs unique; 513 actions; 186 timeline candidates; required headline labels present.
- HTTPS-only source link audit: PASS for all embedded source URLs.
- Privacy/banned-string audit: PASS; no raw local absolute paths, credentials, email addresses, daemon IDs, or private identifiers in HTML.
- Structural controls: PASS by static inspection of client-side search/filter/pagination handlers and data-backed rendering paths.
- Artifact write scope: only new/owned files in `final/`; Phase1–4 inputs unchanged.
