# USDC-0107 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: Canceled
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 保持 `Canceled`。2025-04-09 Bangor Daily News 报道称，former Great Northern Paper mill 的 $300 million Nautilus data center 已被取消，并引用 One Katahdin / mill site redevelopment 负责人称项目已停止、Nautilus 未公开宣布放弃。来源：https://www.bangordailynews.com/2025/04/09/mainefocus/mainefocus-business/300m-data-center-former-millinocket-paper-mill-canceled/
- 取消结论由 2025-04-16 Data Center Dynamics 独立复核：Nautilus canceled planned 60 MW Millinocket data center；DCD 同样说明 Nautilus 未回应置评请求。来源：https://www.datacenterdynamics.com/en/news/nautilus-cancels-flagship-maine-data-center/
- owner / developer 从 `null` 更新为 `Nautilus Data Technologies (proposed developer/operator); Our Katahdin / One North controlled the former mill site`。Nautilus 官方 2021-06-05 新闻稿称 Nautilus 将在 Millinocket former Great Northern Paper mill site 开发项目，Nautilus 与 site owner Our Katahdin 执行 99-year lease。来源：https://nautilusdt.com/press-release/nautilus-data-technologies-to-develop-the-first-sustainable-digital-infrastructure-in-a-qualified-opportunity-zone/；https://www.ourkatahdin.com/data-center-to-locate-at-former-mill-site-in-millinocket/
- capacity_mw 从 `null` 更新为 `60`，但仅作为 planned/canceled critical IT load。Nautilus 与 Our Katahdin 2021-06-05 公告均称 13-acre, 60 MW facility / plans to expand to 60 MW critical IT load；2025 取消报道也沿用 60 MW。未发现 utility interconnection、energized load、commissioning 或 operating-capacity 证据。来源：https://nautilusdt.com/press-release/nautilus-data-technologies-to-develop-the-first-sustainable-digital-infrastructure-in-a-qualified-opportunity-zone/；https://www.ourkatahdin.com/data-center-to-locate-at-former-mill-site-in-millinocket/；https://www.datacenterdynamics.com/en/news/nautilus-cancels-flagship-maine-data-center/
- local-government 补证：Millinocket Town Council 2021 packets 显示 2021 年仍有 Nautilus data center / mill site development 跟进，其中 2021-11-22 packet 记载 Our Katahdin 尚在等待/处理 Brookfield facility rights/easements。未在本次刷新中找到批准、施工、并网或 CO 记录。来源：https://millinocket.org/wp-content/uploads/2021/11/11-22-2021-TentAgenda-Regular-Meeting.pdf；https://millinocket.org/wp-content/uploads/2021/09/9-23-21-Tentative-Agenda-Reg-Council.pdf
- contradictions / caveats：60 MW 是 planned/canceled 口径，不代表 live capacity；取消证据来自地方和行业报道引用 site redevelopment manager，未找到 Nautilus 自己发布的取消公告或官方政府撤件/注销文件。
- verified: true for original announcement/lease/planned 13-acre/60 MW proposal and cancellation-by-reporting status; verified: false for owner-filed cancellation notice, current permits, construction start, energization, commissioning, and operating capacity because public evidence was not located.
