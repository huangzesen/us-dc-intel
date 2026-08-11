# design/ · 设计规格 SKILL

> 职责：承载 GRIDWATCH 视觉设计的规范与已批准原型。

## 内容

- `design-proposal.md` —— 设计提案（艺术方向：国家电网调度室 × 彭博终端；配色/排版/组件/数据可视化/实施计划）
- `design-mockup.html` —— **已批准的设计规格**（Jason 3328「much much much better」）；自包含、真实数据、Dark/Light + 中英、零外部依赖

## 维护契约

- 修改设计：先改 `design-mockup.html`（或新增变体），再更新 `design-proposal.md` 对应章节，确保两者一致
- Astro 正式站（`astro/`）以 `design-mockup.html` 为视觉基准；实现偏差须记录
- 配色/字体/组件 token 变更时同步 Astro 与 mockup，避免漂移

## 边界

- mockup 是设计真源；正式实现以 `astro/` 为准；两者不一致时先修 mockup 再改实现
