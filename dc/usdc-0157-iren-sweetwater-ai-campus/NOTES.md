# USDC-0157 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: IREN reports Sweetwater 1 and 2 under construction with executed grid-connection agreements; no county building/land-use approval record was found
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：从“Sweetwater 1/2 under construction with executed grid-connection agreements”提升为 `partial live`。IREN 在 2026-05-01 公告 Sweetwater 1 1.4GW 站点高压变电站已接入 ERCOT 电网；该证据只证明 Sweetwater 1 变电站/电网侧 energization，IREN 同时说明电力交付会随数据中心分期建设和投运逐步爬坡，不等于 full buildout。来源：https://iren.gcs-web.com/news-releases/news-release-details/iren-announces-successful-energization-sweetwater-1
- capacity/owner 补全：IREN 当前 Sweetwater 页面列示该 West Texas campus 为 2,000 MW、2,200 acres，分为 Sweetwater 1（1,400 MW、1,700 acres、2026 Substation Energization、UNDER CONSTRUCTION）与 Sweetwater 2（600 MW、500 acres、2027 Substation Energization、UNDER CONSTRUCTION）；owner/operator 记为 IREN Limited。来源：https://iren.com/data-centers/sweetwater
- 行业/媒体交叉验证：DCD 于 2026-05-06 报道 IREN 已 energized 1.4GW Sweetwater 1，两个 Sweetwater sites 位于 Sweetwater 外的 Fisher County，总计 2GW/2,200 acres；DCD 称 Sweetwater 2 energization expected in 2028，与 IREN 当前页面的 2027 Substation Energization 存在时间差。来源：https://www.datacenterdynamics.com/en/news/iren-energizes-first-phase-of-2gw-sweetwater-data-center-campus-in-texas/
- local media 验证：KTXS 于 2026-05-28 报道 Sweetwater campus 在 Fisher County，并称 IREN recently energized its 1.4GW Sweetwater 1 site；报道还给出约 300 名施工人员现场、未来六个月施工人力增至三到四倍、完工后 200+ 本地运营岗位等公司口径。来源：https://ktxs.com/news/local/iren-partners-with-nvidia-to-develop-ai-ready-architecture-for-west-texas-data-center-campus
- 冲突/不足：未找到当前可公开索引的 Fisher/Nolan county permit、site-plan 或 commissioners-court order 原始记录。Cleanview 仍列 Sweetwater 1 为 Nolan County/planned/1,400 MW/1,300 acres；Interconnection.fyi 仍列 Nolan County/proposed/250+ MW。data.json 已将 county/status 冲突写入 `contradictions`。来源：https://cleanview.co/data-centers/texas/722/iren-sweetwater-1 ; https://www.interconnection.fyi/data-center/project/iren-sweetwater-1-8d9cdcbd
- 修订（fix pass 2026-08-11）：`history` 已同步本次 refresh——新增 2026-08-11 历史条目记录 status_as_of_cutoff（partial live）、capacity_mw（2,000）、owner（IREN Limited）与 location county（Fisher，Nolan 作为 contradiction 保留），使 history[-1].status_as_of_cutoff 与顶层字段一致。
