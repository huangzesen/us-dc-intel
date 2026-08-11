# USDC-0090 — 更新记录

## 2026-07-16（baseline 抽取）
- 初始数据自 legacy-baseline-20260716 冻结 baseline 抽取（national_master_inventory.json, SHA 2113de4b…）。
- status: County records show a pending project viewer entry for a special development permit and major design review, with the Zoning Administrator disposition recorded as Approved on 2026-02-05
- 待办：按 SKILL.md 数据源优先级做首次独立核实与补证。

## 2026-08-11（refresh）
- status 更新：从“county viewer pending + ZA disposition approved + Prime groundbreaking claim”细化为“official land-use/CEQA layer approved-permitted; construction only company-reported; no building permit/CO/utility energization/commissioning/live-service record located”。Sacramento County project viewer仍显示 PLNP2024-00238 为 Pending，但同页记录 Zoning Administrator disposition 为 Approved，日期 2026-02-05。来源：https://planningdocuments.saccounty.net/ViewProjectDetails.aspx?ControlNum=PLNP2024-00238
- 新增官方 CEQA 证据：CEQAnet 对 Prime Sacramento Datacenter Addition 记录 Notice of Determination，lead agency 为 Sacramento County，project approved/adopted 日期 2026-02-05，posted/received/filed 日期 2026-02-25；该证据只确认环境/审批层，不确认建筑许可、完工或并网。来源：https://ceqanet.lci.ca.gov/1996122010/10
- 保留并扩展 2026-05-07 Prime 公告：Prime 宣布 SMF02 groundbreaking，称新增 150,000 平方英尺、18 MW critical IT load，并使 Sacramento campus 达到 26 MW across two facilities；该事实按 developer/company evidence 处理。来源：https://primedatacenters.com/news/prime-data-centers-breaks-ground-on-second-sacramento-data-center-expanding-regional-campus-footprint/
- 新增当前公司页证据（2026-08-11 访问）：Prime Sacramento location page 将 SMF01 标为 2407 AK Street / 8 MW / live，将第二栋标为 2408 AK Street / 18 MW / under construction；据此将 `capacity_mw` 从 null 更新为 26，并添加 `capacity_mw_basis` 明确这是 company-reported critical IT load，非 utility/government verified。来源：https://primedatacenters.com/locations/sacramento/
- 新增项目团队佐证（2026-08-11 访问）：BKF SMF01-02 project page 描述 Prime Data Centers SMF01-02 为 Sacramento 150,000 SF / 18 MW data center，支持第二栋规模但不作为 permit/energization 证据。来源：https://www.bkf.com/projects/prime-data-center-smf01-02/
- owner 更新：`owner` 从 null 更新为 Prime Data Centers；依据 county application/applicant trail、CEQAnet 项目名、Prime 公司公告/地点页。
- 冲突/不一致：一是 county viewer 仍为 Pending，但同页 disposition 为 Approved，CEQAnet 又确认 NOD/approval date；处理为官方 land-use/CEQA approved-permitted，viewer pending 保留为 caveat。二是 Prime 公告称第二栋为 SMF02，当前地点页称 SMF01-02 / 2408 AK Street，而 county/agenda 使用 2407 AK St、2345 McClellan Park Drive、APNs 215-0330-069/-070；处理为保留 canonical SMF01/SMF02 campus，并在 contradictions 记录 source-specific naming/address。
- 未核实项：未找到 county building permit、final inspection、certificate of occupancy、utility interconnection/service、energization、commissioning 或 full-service record；因此不把公司 under construction 直接升级为官方 construction/energized/live 证据。
