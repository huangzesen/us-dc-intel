# LT · Country Anatomy

Datacenter-country knowledge layer for Lithuania (LT).

## Files

| Layer | File | Status |
|---|---|---|
| 国家层方法论 skill | `SKILL.md` | present（由两份 explorer 合并生成） |
| 官方/监管管线探索（Infostatyba、市政规划/PAV、Litgrid/ESO/VERT、RRT、AAA、Registru centras、Invest Lithuania） | `explorer-official.md` | present |
| 行业/厂商探索（Telia/Telecentras/Delska/Bite/Baltneta/Bacloud/Kaunas 群/Vilnius 中小运营、DCD/LRT/VZ/施工媒体） | `explorer-industry.md` | present |
| 分区层（10 county + 60 municipality） | `divisions/` — 待建 | to be added later |

## Division layer (future)

- 枚举顺序：Vilnius County（Tier 1）→ Kaunas County（含 Kruonis siting）→ Siauliai County（Bacloud）→ Klaipeda/Panevezys（Tier 2）→ Alytus/Marijampole/Taurage/Telsiai/Utena（Tier 3 紧凑扫描）。
- 每区记录需带 municipality、地址/地块与 Infostatyba/市政/电力证据；低产区写 defensible negative，排除 ZUDC/Valstybes duomenu agentura 等误报。
