# SB · Country Anatomy

Datacenter-country knowledge layer for Solomon Islands (SB).

## Files

| Layer | File | Status |
|---|---|---|
| 国家层方法论 skill | `SKILL.md` | present（由两份 explorer 合并生成） |
| 官方/监管管线探索（TCSI/MCA、Telecommunications Act 2009、Lands/Physical Planning、Solomon Power、SISCC/ACS-1、Noro DC、SINBIP、云缺省） | `explorer-official.md` | present |
| 行业/厂商探索（Our Telekom/bmobile/SATSOL/SISCC/Solomon Tower、云/主权云扫描、CS²/SIDN/ACS-1/IXP、本地媒体与目录） | `explorer-industry.md` | present |
| 分区层（9 省 + Honiara Capital Territory） | `divisions/` — 待建 | to be added later |

## Division layer (future)

- 枚举顺序：Capital Territory（Honiara，最高产）→ Western（Noro DC）→ Guadalcanal（Honiara 溢出风险，按法定/行政地点归区）→ Malaita/Choiseul（SIDN 登陆节点）→ Central/Isabel（低产）→ Makira-Ulawa/Temotu/Rennell-Bellona（负向）。
- 每区需记录状态动词（proposed/planned/under construction/handed over/opened/operational）与功能（colo/hosting/DR/CLS/core/edge/government DC）；海缆站与塔站不构成 DC 记录。
