# Slice 13 Treemap Notes

- Replaced the section 03 compute horizon card with a square SVG treemap in `astro/src/pages/index.astro`.
- Country tile area uses `DATA.countries[].capacity_mw`, so it reflects tracked plus estimated capacity.
- Country tile color uses the dominant funnel status by `capacity_mw`. The gray bucket covers unknown, rejected, and coverage statuses.
- Country clicks drill into the selected country's `subnationals[]`; the current aggregate export does not include subnational status funnels, so subnational tiles inherit the parent country's dominant status color.
- The treemap is rendered with a small local squarify implementation and no new dependency.
