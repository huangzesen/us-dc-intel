// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
// base: '/datacenters/' — deployed under https://xhelio.ai/datacenters/
// (GitHub Pages serves the repo at huangzesen/xhelio-datacenters under the
//  datacenters/ subdirectory; assets must resolve relative to that mount.)
//
// NOTE: Astro always emits hashed assets under dist/_astro/ (vite build.assetsDir
// is ignored by Astro). GitHub Pages does NOT serve underscore-prefixed
// directories even with .nojekyll, so the deploy step renames _astro -> assets
// and rewrites the reference in index.html. See astro/SKILL.md.
export default defineConfig({
  base: '/datacenters/',
});
