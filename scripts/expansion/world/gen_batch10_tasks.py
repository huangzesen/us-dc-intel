import json

tasks = json.load(open('batch10_tasks.json'))

TPL = """WRITE the draft datacenter methodology for {name} ({code}) at /Users/huangzesen/work/projects/us-dc-intel/scripts/expansion/world/country-skills/{code}/explorer-official.md and explorer-industry.md. This is the DRAFT layer (deepseek flash) of a two-layer pipeline: fable/gpt5.6 will later review and finalize these files, so write thorough, sourced, grade-honest drafts now. Scope: official/regulatory methodology (explorer-official.md) + industry/vendor discovery methodology (explorer-industry.md) for finding datacenter projects in {name}. Division model: {subnational_type}; divisions to cover: {divisions}. Include: (0) structure facts — administrative divisions, national registries or their absence, legal/regulatory basis, data protection laws; (1) search vocabulary in local language(s) and English (data center, data centre, server farm, colocation, hosting, cloud, digital infrastructure, IXP, submarine cable); (2) official/regulatory pipeline — telecom/ICT regulator, energy/grid operator, investment promotion agency, planning/permits, government IT agency, e-procurement portals, cloud-region official pages (AWS/Azure/GCP/OCI region check); (3) industry pipeline — trade press, industry associations, colocation/cloud operators, hyperscaler presence, PeeringDB/DCD/DatacenterMap, Uptime entries, subsea cable landing stations, IXPs; (4) query templates per pipeline; (5) per-division enumeration approach with realistic expectations (major hub vs no-activity); (6) reliability grades A (official/primary/operator-owned), B (reliable trade press/regulator-adjacent), C (aggregator/weak), U (unverified) with the rule that an entry's grade covers only the fact actually supported; (7) known facilities/projects and their evidence status as of 2026-08; (8) update/re-check cadence. Ground every claimed source with real URLs; mark anything you could not verify live as 'verify' so the review layer re-checks it. HARD CONSTRAINTS: NO-DELETION (never delete/rm any file; do not touch files outside your two target paths); do NOT create SKILL.md or ANATOMY.md (the merge layer owns those); no git writes; do not fabricate URLs or evidence; mark confidence honestly. COMPLETION: report the two file paths, division coverage count, and any sections left as 'verify'."""

out = []
for t in tasks:
    divs = '; '.join(t['divisions'][:24])
    if len(t['divisions']) > 24:
        divs += '; ...' + str(len(t['divisions'])) + ' total'
    task = TPL.format(name=t['name'], code=t['code'], subnational_type=t['subnational_type'], divisions=divs)
    out.append({'task': task, 'tools': ['file', 'shell', 'web']})

with open('batch10_daemon_tasks.json', 'w') as f:
    json.dump(out, f, ensure_ascii=False, indent=1)
print('generated', len(out), 'tasks')
for t in out:
    print(t['task'][:100].replace('\n', ' '))
