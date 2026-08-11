# kanban/ · 静态看板 SKILL

> 职责：把探索/合并结果渲染为自包含单文件看板 `index.html`（当前线上 https://xhelio.ai/datacenters/ 由它驱动）。

## 维护契约

1. **重渲染**：`python3 kanban/render_kanban.py` → 生成 `kanban/index.html`（读 `scripts/expansion/**`，统计批次/州/项目）
2. **部署**（需 Jason 授权）：
   - 构建产物复制到 pages repo **`datacenters/index.html`**（⚠️ 根 `index.html` 是 457B 重定向页，勿覆盖）
   - pages repo: `huangzesen/xhelio-datacenters` → GitHub Pages + CNAME xhelio.ai → push 后 CDN 1-2 分钟刷新
3. **验证**：`curl https://xhelio.ai/datacenters/` 应含预期标记（如 `btn-en`/`btn-light`）且 **leak-check 干净**（无 /Users/、scratch/、daemons/、logs/、.lingtai）

## 现有功能

metrics（county 批次进度）、buckets、状态列、表格、Dark/Light 主题切换、EN/中文切换（localStorage 记忆）。

## 边界

- 看板是展示层；数据真源在 `datacenters.db`/`merge-output/`；不直接改数据
- 新设计版（GRIDWATCH，`design/` + `astro/`）将逐步取代本看板，作为过渡保留

## 相关文件

- `kanban/render_kanban.py`（渲染脚本）→ `kanban/index.html`（产物）
- `scripts/expansion/**`（数据输入）· `datacenters.db`（主库）
- `design/SKILL.md`（新设计规格）· `astro/SKILL.md`（正式站）· 顶层 `SKILL.md`/`ANATOMY.md`
