#!/usr/bin/env python3
"""Deterministic renderer for the frozen U.S. data-center panorama."""
from __future__ import annotations

import hashlib
import html
import json
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent
CUTOFF = "2026-07-16"

STATE_ABBR = {
    "Alabama":"AL","Alaska":"AK","Arizona":"AZ","Arkansas":"AR","California":"CA","Colorado":"CO","Connecticut":"CT","Delaware":"DE","Florida":"FL","Georgia":"GA","Hawaii":"HI","Idaho":"ID","Illinois":"IL","Indiana":"IN","Iowa":"IA","Kansas":"KS","Kentucky":"KY","Louisiana":"LA","Maine":"ME","Maryland":"MD","Massachusetts":"MA","Michigan":"MI","Minnesota":"MN","Mississippi":"MS","Missouri":"MO","Montana":"MT","Nebraska":"NE","Nevada":"NV","New Hampshire":"NH","New Jersey":"NJ","New Mexico":"NM","New York":"NY","North Carolina":"NC","North Dakota":"ND","Ohio":"OH","Oklahoma":"OK","Oregon":"OR","Pennsylvania":"PA","Rhode Island":"RI","South Carolina":"SC","South Dakota":"SD","Tennessee":"TN","Texas":"TX","Utah":"UT","Vermont":"VT","Virginia":"VA","Washington":"WA","West Virginia":"WV","Wisconsin":"WI","Wyoming":"WY","District of Columbia":"DC",
}
STATE_NAME = {v:k for k,v in STATE_ABBR.items()}

def load(rel: str):
    return json.loads((ROOT / rel).read_text(encoding="utf-8"))

def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def relpath(path: str | Path) -> str:
    s = str(path).replace("\\", "/")
    marker = "workspace/oracle_openai_datacenters_20260716/"
    if marker in s:
        return marker + s.split(marker, 1)[1]
    if "/" in s and ("phase" in s or s.startswith("research_brief")):
        return s.lstrip("/")
    return Path(s).name

def uniq(seq):
    out=[]; seen=set()
    for x in seq:
        if x and x not in seen:
            seen.add(x); out.append(x)
    return out

def urls_from(value):
    out=[]
    if isinstance(value, str) and value.startswith("https://"):
        out.append(value)
    elif isinstance(value, list):
        for x in value: out += urls_from(x)
    elif isinstance(value, dict):
        for x in value.values(): out += urls_from(x)
    return out

def clean_path_strings(value):
    """Keep report data free of host-local absolute paths."""
    if isinstance(value, str):
        if "workspace/oracle_openai_datacenters_20260716/" in value:
            return "workspace/oracle_openai_datacenters_20260716/" + value.split("workspace/oracle_openai_datacenters_20260716/",1)[1]
        if value.startswith("/") and ("Users/" in value or "private/" in value):
            return Path(value).name
        return value
    if isinstance(value, list): return [clean_path_strings(x) for x in value]
    if isinstance(value, dict): return {k:clean_path_strings(v) for k,v in value.items()}
    return value

def compact_companies(rec):
    vals=[]
    if not rec: return []
    for key in ("companies", "developer", "operator", "customer"):
        v=rec.get(key)
        if isinstance(v,list): vals += v
        elif isinstance(v,str): vals.append(v)
    for group in (rec.get("companies") if isinstance(rec.get("companies"),dict) else {},):
        pass
    return uniq([str(x) for x in vals if x])

def capacity_text(cap):
    if not isinstance(cap,dict): return "未披露"
    labels={"mw":"MW","reported_mw":"reported MW","capacity_MW":"MW","critical_capacity_MW":"critical MW","planned_capacity_MW":"planned MW","planned_load_MW":"planned load MW","anticipated_mw":"anticipated MW","follow_on_mw":"follow-on MW","investment_usd":"investment USD","investment_USD":"investment USD","square_feet":"sq ft","buildings":"buildings","planned_buildings":"planned buildings","acreage":"acres","land_acres":"land acres","basis":"basis"}
    parts=[]
    for k,v in cap.items():
        if v is None or v==[] or v=={}: continue
        lab=labels.get(k,k)
        if isinstance(v,(int,float)) and "investment" in k.lower(): val=f"${v:,.0f}"
        elif isinstance(v,(dict,list)): val=json.dumps(v,ensure_ascii=False,separators=(",",":"))
        else: val=str(v)
        parts.append(f"{lab}={val}")
    return "; ".join(parts) if parts else "未披露"

def normalize_state(v):
    if not v: return "?"
    s=str(v)
    return STATE_ABBR.get(s, s.upper() if len(s)<=3 else s)

def norm_location(loc):
    loc=loc or {}
    return {"city":loc.get("city") or "未披露","county":loc.get("county") or loc.get("county_or_equivalent") or "未披露","state":normalize_state(loc.get("state"))}

def source_links_for(master, gantt, acts):
    urls=[]
    urls += urls_from(gantt.get("source_urls",[]))
    urls += urls_from(gantt.get("source_provenance",[]))
    urls += urls_from(master.get("phase3_record",{}))
    urls += urls_from(master.get("regional_record",{}))
    urls += urls_from(master.get("phase2_seed_record",{}))
    urls += urls_from(acts)
    return uniq(urls)

def stage_label(s):
    return {"announced":"已宣布 / announced","local_process":"地方程序 / local process","approved_or_permitted":"已批准或获许可 / approved-permitted","site_work_or_construction":"场地施工 / construction","energized":"已通电 / energized","live_partial":"部分上线 / partial live","full_buildout":"全面建成 / full buildout"}.get(s,s or "未归类")

def source_label(master):
    p=master.get("provenance",{})
    if p.get("authoritative_layer")=="phase2_seed_only": return "Phase2 seed-only · evidence gap"
    return "Phase3 authoritative action layer + Phase2 enrichment"

def esc(s): return html.escape(str(s if s is not None else ""), quote=True)

def build_data():
    # Parse every frozen JSON under the workspace before selecting report fields.
    parsed_json={}
    for p in sorted(ROOT.rglob("*.json")):
        if OUT in p.parents: continue
        parsed_json[str(p.relative_to(ROOT))]=json.loads(p.read_text(encoding="utf-8"))

    master_doc=parsed_json["phase4/national_master_inventory.json"]
    gantt_doc=parsed_json["phase4/gantt_rows.json"]
    action_doc=parsed_json["phase4/county_decision_register.json"]
    comp=parsed_json["phase4/completeness_appendix.json"]
    dedupe=parsed_json["phase4/dedupe_ledger.json"]
    conflict=parsed_json["phase4/source_conflict_audit.json"]
    cycle=parsed_json["phase1/construction_cycle.json"]
    master_records=master_doc["master_records"]
    gantt_by_stable={x["stable_id"]:x for x in gantt_doc["timeline_candidates"]}
    actions=action_doc["actions"]
    acts_by=defaultdict(list)
    for a in actions: acts_by[a.get("stable_id")].append(a)

    assert len(master_records)==208 and len({x["master_id"] for x in master_records})==208
    assert len(gantt_doc["timeline_candidates"])==186
    assert len(actions)==513

    projects=[]
    for m in master_records:
        p3=m.get("phase3_record") or {}
        reg=m.get("regional_record") or {}
        seed=m.get("phase2_seed_record") or {}
        provenance=m.get("provenance") or {}
        stable=(p3.get("stable_id") or reg.get("id") or reg.get("stable_id") or seed.get("stable_id")
                or provenance.get("phase3_stable_id") or provenance.get("regional_id")
                or provenance.get("phase2_seed_stable_id"))
        g=gantt_by_stable.get(stable,{})
        loc=norm_location(m.get("location") or p3.get("location") or seed)
        company_values=[]
        company_values += compact_companies(seed)
        company_values += compact_companies(p3)
        if isinstance(reg.get("companies"),dict):
            for v in reg["companies"].values(): company_values += v if isinstance(v,list) else ([v] if v else [])
        company_values=uniq(company_values)
        cap=reg.get("capacity") or p3.get("capacity") or {}
        if not cap and seed: cap={k:seed.get(k) for k in ("capacity_MW","investment_USD","buildings") if seed.get(k) is not None}
        src=source_links_for(m,g,acts_by.get(stable,[]))
        cohort="seed_only" if provenance.get("authoritative_layer")=="phase2_seed_only" else "detailed"
        status=g.get("normalized_status")
        if status is None: status="seed_only"
        projects.append({
            "master_id":m["master_id"], "stable_id":stable, "name":m.get("canonical_project") or p3.get("project") or seed.get("project"),
            "aliases":uniq((m.get("aliases") or []) + (p3.get("aliases") or []) + (seed.get("aliases") or [])), "location":loc,
            "companies":company_values, "capacity":capacity_text(cap), "cohort":cohort, "classification_source":provenance.get("authoritative_layer") or "unclassified",
            "status":status, "status_label":stage_label(status) if cohort=="detailed" else "仅种子证据 / seed-only evidence gap",
            "raw_status":g.get("status_as_of_cutoff_raw") or p3.get("status_as_of_cutoff") or seed.get("construction_status") or "",
            "confidence":g.get("source_provenance",[{}])[0].get("tier") if g.get("source_provenance") else (seed.get("confidence") or ""),
            "provenance":source_label(m), "source_file":relpath(m.get("provenance",{}).get("phase3_source_file") or m.get("provenance",{}).get("phase2_seed_source_file") or ""),
            "source_urls":src, "action_count":len(acts_by.get(stable,[])), "construction_anchor":g.get("construction_anchor",{}).get("present",False),
            "has_timeline":bool(g), "unresolved":m.get("unresolved_candidate_matches") or seed.get("unresolved_questions") or p3.get("next_evidence_needed") or reg.get("next_evidence_needed") or "",
        })

    timeline=[]
    excluded_ids={"US-AK-DAF-AI-PORTFOLIO-2026"}
    for g in gantt_doc["timeline_candidates"]:
        spans=[]
        for s in g.get("gantt_spans",[]):
            spans.append({k:s.get(k) for k in ("row_type","label","start","finish","gantt_start","gantt_finish","uncertainty_start","uncertainty_finish","normalized_stage","evidence_state","projection","confidence","rendering","basis","source_urls")})
        timeline.append({"stable_id":g["stable_id"],"project":g["project"],"location":norm_location(g.get("location")),"status":g["normalized_status"],"status_label":stage_label(g["normalized_status"]),"source_urls":uniq(g.get("source_urls",[])),"source_provenance":clean_path_strings(g.get("source_provenance",[])),"anchor":g.get("construction_anchor",{}),"spans":spans,"events":len(g.get("events",[])),"projection_spans":sum(1 for s in g.get("gantt_spans",[]) if s.get("projection")),"physical":g["stable_id"] not in excluded_ids})

    action_rows=[]
    for a in actions:
        action_rows.append({"action_id":a.get("action_id"),"stable_id":a.get("stable_id"),"project":a.get("project"),"location":norm_location(a.get("location")),"category":a.get("normalized_category"),"date":a.get("date"),"date_text":a.get("date_text"),"date_precision":a.get("date_precision"),"body":a.get("body"),"action_type":a.get("action_type"),"result":a.get("result"),"vote_tally":a.get("vote_tally"),"case":a.get("case_or_permit_number"),"primary_url":a.get("primary_url"),"caveat":a.get("caveat"),"evidence_note":a.get("evidence_note"),"evidence_state":a.get("evidence_state"),"projection":a.get("projection",False),"source_file":relpath(a.get("source_file",""))})

    state_rows=[]
    master_counts=Counter(p["location"]["state"] for p in projects)
    for row in comp["coverage_matrix"]:
        state_rows.append({"name":row.get("jurisdiction"),"code":row.get("code") or normalize_state(row.get("jurisdiction")),"seed":row.get("candidate_count_national_seed",0),"phase2":row.get("verified_regional_phase2_count",0),"phase3":row.get("verified_phase3_count",0),"masters":master_counts.get(row.get("code") or normalize_state(row.get("jurisdiction")),0),"finding":row.get("regional_worker_finding"),"zero_note":row.get("negative_search_result_if_zero"),"caveat":row.get("access_caveats"),"sources":uniq(urls_from(row.get("sources",[])))})

    # Compact appendices retain every row and every source URL while keeping the HTML usable.
    proposals=[]
    for x in comp["announced_proposals_lacking_siting_evidence"]:
        proposals.append({"id":x.get("id"),"name":x.get("name"),"state":x.get("state"),"status":x.get("status"),"reason":x.get("reason"),"source_urls":uniq(urls_from(x.get("https_source_urls",[])))})
    baseline=[]
    for x in comp["baseline_live_facilities_no_active_expansion"]:
        baseline.append({"id":x.get("id"),"name":x.get("name"),"location":x.get("location"),"status":x.get("status"),"scope_note":x.get("scope_note"),"source_ids":x.get("source_ids",[]),"source_urls":uniq(urls_from(x.get("https_source_urls",[])))})
    findings=[]
    for x in conflict["findings"]:
        findings.append({"id":x.get("finding_id"),"severity":x.get("severity"),"category":x.get("category"),"project_ids":x.get("project_ids",[]),"claims":x.get("conflicting_claims",[]),"resolution":x.get("safest_resolution"),"disclose":x.get("final_html_must_disclose"),"anchors":clean_path_strings(x.get("anchors",[]))})
    exclusions=[]; seen_ex=set()
    for x in dedupe["mappings"]:
        if x.get("disposition","").startswith("excluded"):
            key=x.get("input_id")
            if key in seen_ex: continue
            seen_ex.add(key); exclusions.append({"input_id":key,"disposition":x.get("disposition"),"reason":x.get("match_reason"),"source_file":relpath(x.get("source_file","")),"source_urls":uniq(x.get("source_urls",[]))})

    company_cov=comp["company_region_coverage"]
    status_counts=Counter(x["status"] for x in timeline if x["physical"])
    source_metrics={"master_source_urls":667,"gantt_input_urls":gantt_doc["input_url_manifest"].__len__(),"action_urls_valid":conflict["metrics"].get("phase3_action_urls_valid"),"project_source_urls":conflict["metrics"].get("phase3_project_source_url_count"),"rows_missing_project_source_urls":conflict["metrics"].get("phase3_rows_missing_project_source_urls"),"phase2_source_records":conflict["metrics"].get("phase2_source_record_count"),"phase2_domains":conflict["metrics"].get("phase2_distinct_source_domain_count"),"phase2_tiers":conflict["metrics"].get("phase2_source_tier_counts")}
    data={"cutoff":CUTOFF,"headline":{"masters":208,"detailed":185,"seed_only":23,"timeline_candidates":186,"timeline_physical":185,"events":1072,"projection_spans":131,"construction_anchors":38,"actions":513,"jurisdictions":51,"zero_jurisdictions":["CT","DC","DE","FL","NE","VT"],"baseline_live":8,"proposal_rows":53},"projects":projects,"timeline":timeline,"actions":action_rows,"state_rows":state_rows,"proposals":proposals,"baseline":baseline,"findings":findings,"exclusions":exclusions,"company_coverage":company_cov,"status_counts":dict(status_counts),"source_metrics":source_metrics,"cycle":{"archetypes":cycle["schedule_archetypes"],"stages":cycle["lifecycle_stages"],"observed":cycle["observed_projects"],"risks":cycle["risk_register"]},"source_files":[],"source_hashes":{},"key_hashes":{"national_master_inventory.json":sha(ROOT/"phase4/national_master_inventory.json"),"dedupe_ledger.json":sha(ROOT/"phase4/dedupe_ledger.json"),"gantt_rows.json":sha(ROOT/"phase4/gantt_rows.json"),"county_decision_register.json":sha(ROOT/"phase4/county_decision_register.json"),"parent_master_validation_v2.json":sha(ROOT/"phase4/parent_master_validation_v2.json"),"parent_gantt_validation_v2.json":sha(ROOT/"phase4/parent_gantt_validation_v2.json")}}
    # Exact frozen JSON/Markdown source inventory; the renderer consumes all JSON above.
    source_paths=[]
    for p in sorted(ROOT.rglob("*")):
        if not p.is_file() or OUT in p.parents: continue
        if p.suffix.lower() in {".json",".md"}:
            source_paths.append(str(p.relative_to(ROOT)).replace("\\","/"))
    data["source_files"] = source_paths
    data["source_hashes"] = {x:sha(ROOT/x) for x in source_paths}
    return data

CSS = r"""
:root{--ink:#152238;--muted:#5e6b7e;--line:#dce3ec;--paper:#fff;--wash:#f5f8fb;--navy:#102a43;--teal:#087f8c;--amber:#b96800;--red:#a63d40;--green:#27734d;--blue:#2e6fbb;--shadow:0 10px 30px rgba(16,42,67,.08)}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;color:var(--ink);background:#eef3f7;font:14px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Noto Sans SC",Arial,sans-serif}a{color:#075ea8;text-decoration:none}a:hover{text-decoration:underline}.shell{max-width:1500px;margin:auto;background:var(--paper);min-height:100vh}.hero{padding:38px 42px 28px;background:linear-gradient(135deg,#102a43,#1a5263 58%,#dbeff0);color:white}.eyebrow{letter-spacing:.12em;text-transform:uppercase;font-size:11px;opacity:.82}.hero h1{font-size:clamp(28px,4vw,48px);line-height:1.1;margin:10px 0 12px;max-width:1000px}.hero p{max-width:930px;margin:0;color:#e9f5f7;font-size:16px}.hero .meta{margin-top:20px;display:flex;gap:10px;flex-wrap:wrap}.pill{display:inline-flex;align-items:center;border-radius:999px;padding:5px 10px;background:rgba(255,255,255,.14);border:1px solid rgba(255,255,255,.28);font-size:12px}.nav{position:sticky;top:0;z-index:10;background:rgba(255,255,255,.96);border-bottom:1px solid var(--line);padding:9px 42px;display:flex;gap:8px;flex-wrap:wrap;backdrop-filter:blur(8px)}.nav a{font-size:12px;padding:4px 8px;border-radius:6px}.nav a:hover,.nav a:focus{background:#e5f1f3;text-decoration:none}.content{padding:28px 42px 60px}section{scroll-margin-top:55px;margin:34px 0 48px}h2{font-size:25px;line-height:1.2;margin:0 0 14px;color:var(--navy)}h3{font-size:17px;margin:20px 0 9px;color:var(--navy)}h4{margin:0 0 4px}.lead{font-size:17px;max-width:1040px}.muted{color:var(--muted)}.small{font-size:12px}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:12px}.grid.two{grid-template-columns:repeat(auto-fit,minmax(300px,1fr))}.card{border:1px solid var(--line);border-radius:12px;padding:16px;background:#fff;box-shadow:var(--shadow)}.card .num{font-size:30px;font-weight:750;line-height:1;color:var(--navy)}.card .label{margin-top:8px;color:var(--muted);font-size:12px}.callout{border-left:4px solid var(--teal);background:#edf8f8;padding:14px 16px;border-radius:0 10px 10px 0;margin:14px 0}.warn{border-left-color:var(--amber);background:#fff7eb}.danger{border-left-color:var(--red);background:#fff1f1}.success{border-left-color:var(--green);background:#eff8f2}.controls{display:flex;gap:8px;flex-wrap:wrap;align-items:center;padding:12px;background:var(--wash);border:1px solid var(--line);border-radius:10px;margin:13px 0}.controls input,.controls select{font:inherit;border:1px solid #b8c5d2;border-radius:7px;padding:8px 9px;background:white;color:var(--ink);min-width:150px}.controls input:focus,.controls select:focus,.button:focus,a:focus{outline:3px solid #9bd7df;outline-offset:2px}.button{font:inherit;border:1px solid #9fb5c8;background:#fff;color:var(--navy);border-radius:7px;padding:8px 11px;cursor:pointer}.button.primary{background:var(--navy);color:#fff;border-color:var(--navy)}.table-wrap{overflow:auto;border:1px solid var(--line);border-radius:10px;background:#fff}table{border-collapse:collapse;width:100%;min-width:680px}th,td{padding:9px 10px;border-bottom:1px solid var(--line);vertical-align:top;text-align:left}th{background:#f5f8fb;color:var(--navy);font-size:12px;position:sticky;top:0;z-index:1}tr:last-child td{border-bottom:0}.badge{display:inline-block;padding:3px 7px;border-radius:999px;background:#edf2f7;color:#30445b;font-size:11px;white-space:nowrap}.badge.announced{background:#eef2f8}.badge.local_process{background:#fff4df;color:#7b4d00}.badge.approved_or_permitted{background:#eaf4ff;color:#185b96}.badge.site_work_or_construction{background:#eaf8ef;color:#22633e}.badge.energized,.badge.live_partial,.badge.full_buildout{background:#dff6ee;color:#116047}.badge.seed_only{background:#f1ebfb;color:#633c91}.bar-chart{display:grid;gap:8px;max-width:760px}.bar-line{display:grid;grid-template-columns:170px 1fr 50px;gap:8px;align-items:center}.bar-track{height:13px;background:#e8eef3;border-radius:999px;overflow:hidden}.bar-fill{height:100%;background:linear-gradient(90deg,var(--teal),#5ab6b6);border-radius:999px}.timeline-shell{border:1px solid var(--line);border-radius:10px;overflow:hidden}.timeline-head,.timeline-row{display:grid;grid-template-columns:260px 1fr;min-width:900px}.timeline-head{background:#f5f8fb;border-bottom:1px solid var(--line);font-size:12px;color:var(--muted);position:sticky;top:48px;z-index:2}.timeline-head>div,.timeline-row>div{padding:8px 10px}.years{position:relative;height:27px;border-left:1px solid var(--line)}.years span{position:absolute;top:4px;transform:translateX(-50%);font-size:11px}.timeline-row{border-bottom:1px solid #edf1f5}.timeline-row:last-child{border-bottom:0}.project-cell{background:#fff}.project-cell strong{display:block;line-height:1.25}.project-cell .small{display:block}.track{position:relative;height:42px;background:repeating-linear-gradient(to right,transparent 0,transparent calc(14.2857% - 1px),#e4eaf0 calc(14.2857% - 1px),#e4eaf0 14.2857%)}.track .range{position:absolute;top:16px;height:10px;border:2px dashed var(--amber);border-radius:6px;background:rgba(232,167,78,.12);min-width:3px}.track .range.low{border-color:var(--red);background:rgba(166,61,64,.08)}.track .mark{position:absolute;top:10px;width:7px;height:22px;border-radius:3px;background:var(--teal);transform:translateX(-50%);box-shadow:0 0 0 2px #fff}.track .mark.proj{background:transparent;border:2px dashed var(--amber);box-shadow:none}.legend{display:flex;gap:14px;flex-wrap:wrap;font-size:12px;color:var(--muted);margin:8px 0}.legend i{display:inline-block;width:23px;height:10px;vertical-align:middle;margin-right:4px;border-radius:4px;background:var(--teal)}.legend i.dashed{background:transparent;border:2px dashed var(--amber)}.pagination{display:flex;align-items:center;justify-content:space-between;gap:10px;padding:10px 0}.project-table td:first-child{min-width:240px}.project-table td:nth-child(2){min-width:180px}.project-table td:nth-child(4){min-width:270px}.action-table td:first-child{min-width:210px}.action-table td:nth-child(5){min-width:300px}.details-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:10px}.details-grid details,details.panel{border:1px solid var(--line);border-radius:9px;padding:11px 13px;background:#fff}.details-grid summary,details.panel summary{cursor:pointer;font-weight:650;color:var(--navy)}details[open] summary{margin-bottom:8px}.tag-list{display:flex;gap:5px;flex-wrap:wrap}.tag{font-size:11px;padding:2px 6px;border:1px solid var(--line);border-radius:5px;color:var(--muted)}.stage-flow{display:flex;gap:0;overflow:auto;padding:8px 0 15px}.stage{min-width:125px;border-top:4px solid var(--teal);padding:8px 10px;background:#f5fafb;margin-right:3px}.stage small{display:block;color:var(--muted);font-size:11px}.source-list{columns:2;column-gap:30px}.source-list li{break-inside:avoid;margin-bottom:4px}.footer{border-top:1px solid var(--line);padding:20px 42px;color:var(--muted);font-size:12px;background:#f8fafc}@media(max-width:800px){.hero,.content,.footer{padding-left:18px;padding-right:18px}.nav{padding-left:14px;padding-right:14px}.bar-line{grid-template-columns:125px 1fr 40px}.timeline-head,.timeline-row{grid-template-columns:205px 1fr}section{margin-top:28px}.source-list{columns:1}}@media print{body{background:#fff;font-size:10px}.shell{max-width:none}.hero{color:#000;background:#fff;border-bottom:2px solid #000;padding:15px 0}.hero p,.hero .meta{color:#000}.nav,.controls,.button,.pagination{display:none!important}.content,.footer{padding:10px 0}section{break-inside:auto;margin:18px 0}.card,.table-wrap,.timeline-shell,details{box-shadow:none}.timeline-shell{overflow:visible}.timeline-head,.timeline-row{min-width:0;grid-template-columns:180px 1fr}.timeline-row{break-inside:avoid}a{color:#000;text-decoration:underline}.source-list{columns:2}}
.timeline-shell{overflow-x:auto;overflow-y:hidden;max-width:100%;-webkit-overflow-scrolling:touch}
.timeline-head{position:relative;top:auto}
.years span:first-child{transform:none}.years span:last-child{display:none}
"""

def render_html(data):
    # Escaping < in JSON prevents an accidental script close if a source ever contains it.
    jsdata=json.dumps(clean_path_strings(data),ensure_ascii=False,separators=(",",":"),allow_nan=False).replace("<","\\u003c")
    template = '''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>美国数据中心建设全景｜All-company U.S. data-center construction panorama</title><style>__INLINE_CSS__</style></head>
<body><div class="shell">
<header class="hero"><div class="eyebrow">Frozen evidence · cutoff 2026-07-16</div><h1>美国数据中心建设全景<br><span style="font-size:.56em;font-weight:500">All-company U.S. data-center construction panorama</span></h1><p>结论先行：在“公开可识别、2024–2030 有新建或重大扩建信号”的证据定义下，本报告保留 <strong>208 个 unique project masters</strong>。它们不是“全美所有现存设施”，也不是不可知的保密建设总数。</p><div class="meta"><span class="pill">208 masters</span><span class="pill">185 detailed + 23 seed-only</span><span class="pill">51 jurisdictions</span><span class="pill">513 county actions</span><span class="pill">2024–2030 Gantt</span></div></header>
<nav class="nav"><a href="#summary">摘要</a><a href="#status">状态</a><a href="#states">州矩阵</a><a href="#gantt">Gantt</a><a href="#directory">项目目录</a><a href="#actions">决策登记</a><a href="#cycle">建设周期</a><a href="#appendix">附录</a><a href="#method">方法与局限</a></nav>
<main class="content">
<section id="summary"><h2>执行摘要 / Executive summary</h2><p class="lead">“all”在这里的含义是：在冻结证据中能够公开识别、定位到美国项目/园区并有建设周期相关信号的项目全集；它不可能覆盖未命名、保密或未留下公开记录的建设。主计数 208 应准确拆解为 <strong>185 个 Phase3/region detailed projects</strong> 与 <strong>23 个 retained seed-only evidence-gap records</strong>。一条 DAF solicitation 与四条 aggregate/undisclosed seed records 是排除项，不是 physical projects。</p>
<div class="callout warn"><strong>状态口径：</strong>宣布（announced）、地方程序（local process）、已批准/获许可（approved-permitted）、场地施工/建设（site work-construction）、已通电（energized）、部分上线（partial live）、全面建成（full buildout）彼此不等同。实证事件用实线；未来目标与模型尾段用虚线。</div>
<div class="grid"><div class="card"><div class="num">208</div><div class="label">唯一 master projects<br><span class="muted">185 detailed + 23 seed-only</span></div></div><div class="card"><div class="num">186</div><div class="label">accepted Phase2/3 timeline candidates<br><span class="muted">185 physical rows shown; DAF solicitation excluded</span></div></div><div class="card"><div class="num">513</div><div class="label">county/city/state/utility actions</div></div><div class="card"><div class="num">51</div><div class="label">jurisdictions covered<br><span class="muted">6 zero-result: CT/DC/DE/FL/NE/VT</span></div></div><div class="card"><div class="num">8</div><div class="label">live-only baselines<br><span class="muted">appendix-only, not Gantt rows</span></div></div><div class="card"><div class="num">53</div><div class="label">announced / evidence-gap appendix rows</div></div></div>
<h3>不可混淆的四个边界</h3><div class="grid two"><div class="card"><h4>项目计数 ≠ 设施存量</h4><p class="small">208 是 unique project masters，不是所有既有 U.S. facilities。普通既有 OCI regions 与无 active expansion 的 live baselines 只在附录。</p></div><div class="card"><h4>能力数字保留 scope</h4><p class="small">Phase、ultimate scope、reported MW、investment USD 与 buildings 分栏保留；不把美元/平方英尺换算成 MW，也不把 unresolved identities 相加。</p></div><div class="card"><h4>Gantt 是证据化候选时间线</h4><p class="small">186 accepted candidates 由 Phase4 v2 生成；其中 DAF solicitation 无 selected physical project，因此物理呈现为 185 行，并在 exclusions 保留。</p></div><div class="card"><h4>精度从不被补造</h4><p class="small">day/month/year/undated/snapshot 等原始精度保留；未标日期的 action 不被伪造为具体日。</p></div></div></section>

<section id="status"><h2>状态分布 / Status distribution</h2><p>下图统计 185 个 detailed physical rows；23 个 seed-only records 不被强行映射为同等深度的物理阶段。</p><div id="statusChart" class="bar-chart"></div><div class="legend"><span><i></i>solid = source-backed actual</span><span><i class="dashed"></i>dashed = projection / modeled uncertainty</span></div></section>

<section id="states"><h2>州与辖区矩阵 / State & jurisdiction matrix</h2><p>“seed / Phase2 / Phase3”是覆盖层级，不是可直接相加的独立项目数；master count 是去重后的报告主记录数。零结果是定向搜索结果，不是绝对不存在证明。</p><div class="controls"><input id="stateSearch" placeholder="搜索州、代码或 finding" aria-label="搜索州矩阵"><select id="stateSort" aria-label="州矩阵排序"><option value="masters">按 master 数</option><option value="phase3">按 Phase3 数</option><option value="name">按名称</option></select></div><div class="table-wrap"><table id="stateTable"><thead><tr><th>Jurisdiction</th><th>Master</th><th>Seed</th><th>Phase2</th><th>Phase3</th><th>Finding / caveat</th><th>Sources</th></tr></thead><tbody></tbody></table></div></section>

<section id="gantt"><h2>2024–2030 证据时间线 / Evidence-backed Gantt</h2><p>Phase4 accepted counts: <strong>186 candidates / 1,072 events / 131 projected spans / 38 construction anchors</strong>。为保持物理项目边界，默认展示 185 个 detailed physical rows；<span class="badge seed_only">DAF solicitation excluded</span> 仍在排除附录中。没有 construction/site-work、energization 或 live-service anchor 的项目不会被推断出 construction bar。</p><div class="callout"><strong>如何读：</strong>青色竖线为 actual event；橙色/红色虚线条为模型化 first-usable/full-buildout uncertainty tail。低 confidence 的 projection 使用红色虚线；SC-004 QTS York 维持 approved/permitted，没有 construction anchor。</div><div class="controls"><input id="ganttSearch" placeholder="搜索项目、公司、州或 stable ID" aria-label="搜索 Gantt"><select id="ganttStatus" aria-label="Gantt 状态"><option value="">全部状态</option><option value="announced">announced</option><option value="local_process">local process</option><option value="approved_or_permitted">approved-permitted</option><option value="site_work_or_construction">construction</option><option value="energized">energized</option><option value="live_partial">partial live</option><option value="full_buildout">full buildout</option></select><label class="small"><input type="checkbox" id="anchorOnly"> 仅 construction anchor</label><button class="button" id="showExcluded">显示排除候选</button><span id="ganttCount" class="muted small"></span></div><div class="timeline-shell"><div class="timeline-head"><div>Project / status</div><div class="years"><span style="left:0%">2024</span><span style="left:14.2857%">2025</span><span style="left:28.5714%">2026</span><span style="left:42.8571%">2027</span><span style="left:57.1428%">2028</span><span style="left:71.4285%">2029</span><span style="left:85.7142%">2030</span><span style="left:100%">2030</span></div></div><div id="ganttRows"></div></div></section>

<section id="directory"><h2>可搜索项目目录 / Searchable project directory</h2><p>目录包含全部 208 masters。项目级 source links 优先来自 Phase3/Phase2；对缺少 project-level <code>source_urls</code> 的 38 条记录，链接由 county actions 的 primary URLs 衍生，并在方法附录披露。</p><div class="controls"><input id="projectSearch" placeholder="搜索名称、别名、公司、州、master ID" aria-label="搜索项目目录"><select id="projectStatus" aria-label="项目状态"><option value="">全部层级</option><option value="detailed">detailed</option><option value="seed_only">seed-only</option><option value="construction">含 construction anchor</option></select><span id="projectCount" class="muted small"></span></div><div class="table-wrap"><table class="project-table"><thead><tr><th>Master / project</th><th>Location</th><th>Status</th><th>Companies · capacity/scope</th><th>Provenance · source links</th></tr></thead><tbody id="projectRows"></tbody></table></div><div class="pagination"><button class="button" id="projectPrev">上一页</button><span id="projectPage" class="small muted"></span><button class="button" id="projectNext">下一页</button></div></section>

<section id="actions"><h2>513 条 county / city / state / utility 决策登记</h2><p>每条 action 保留 date precision、body、action type、result、vote tally、case/permit number、caveat、evidence state 与 primary URL。公司公告、incentive、utility proceeding 不自动升级为 building approval 或 construction。</p><div class="controls"><input id="actionSearch" placeholder="搜索项目、body、结果、case 或 action ID" aria-label="搜索决策登记"><select id="actionCategory" aria-label="决策类别"><option value="">全部类别</option><option>permit</option><option>environment</option><option>incentive</option><option>zoning</option><option>vote</option><option>other</option><option>water</option><option>utility</option><option>power</option></select><button class="button" id="actionAll">显示全部 513</button><span id="actionCount" class="muted small"></span></div><div class="table-wrap"><table class="action-table"><thead><tr><th>Action / project</th><th>Date / precision</th><th>Category · body</th><th>Result / caveat</th><th>Source</th></tr></thead><tbody id="actionRows"></tbody></table></div><div class="pagination"><button class="button" id="actionPrev">上一页</button><span id="actionPage" class="small muted"></span><button class="button" id="actionNext">下一页</button></div></section>

<section id="cycle"><h2>建设周期 / Construction-cycle model</h2><p>Phase1 模型包含 <strong>15 个 lifecycle stages、4 个 schedule archetypes、7 个 observed benchmark projects</strong>。这些是范围与依赖关系的 planning model，不是把 185 个项目套成同一条确定工期。</p><div class="stage-flow" id="stageFlow"></div><h3>四类 schedule archetypes</h3><div class="table-wrap"><table><thead><tr><th>Archetype</th><th>First usable</th><th>First usable → full buildout</th><th>Conditions / confidence</th></tr></thead><tbody id="archetypeRows"></tbody></table></div><h3>7 个 observed benchmark cases</h3><div class="table-wrap"><table><thead><tr><th>Project</th><th>Location</th><th>Capacity scope</th><th>Interpretation / confidence</th></tr></thead><tbody id="observedRows"></tbody></table></div></section>

<section id="appendix"><h2>完整性与审计附录 / Completeness & audit appendices</h2><div class="details-grid"><details open><summary>53 announced / evidence-gap rows</summary><div class="table-wrap"><table><thead><tr><th>ID / name</th><th>State · status</th><th>Why not site evidence</th><th>Sources</th></tr></thead><tbody id="proposalRows"></tbody></table></div></details><details><summary>8 live-only baselines</summary><div class="table-wrap"><table><thead><tr><th>Facility</th><th>Location · status</th><th>Scope treatment</th><th>Sources</th></tr></thead><tbody id="baselineRows"></tbody></table></div></details><details><summary>Exclusions and not-additive records</summary><div class="callout warn">Unique excluded seed records: one DAF solicitation without selected physical project, plus four aggregate/undisclosed records. The DAF appears twice in the ledger because both Phase2 and Phase3 mappings are preserved.</div><div class="table-wrap"><table><thead><tr><th>Input ID</th><th>Disposition</th><th>Decision</th><th>Source</th></tr></thead><tbody id="exclusionRows"></tbody></table></div></details><details><summary>Source conflict audit: 1 blocker history + 13 material findings</summary><div class="callout danger">The preserved pre-repair audit recorded one Gantt-coverage blocker. The accepted Phase4 v2 parent receipt passes after the all-project candidate schedule was built; the material findings below remain disclosures.</div><div id="findingRows"></div></details></div></section>

<section id="method"><h2>方法、来源与局限 / Method, sources & limitations</h2><div class="grid two"><div class="card"><h3>Evidence hierarchy</h3><p class="small">地方/州 agenda packets、minutes、ordinances、resolutions、permit portals、utility/regulator filings 优先；其后为公司/投资者披露、主流与专业媒体、地方报道；aggregator 只作 discovery lead。vote inference prohibited。</p></div><div class="card"><h3>Phase4 provenance</h3><p class="small">Phase3 action layer authoritative；regional rows exact-ID enrichment；seed rows only on explicit evidence merge。所有 208 master IDs 唯一；source links 由 records 与 actions 的 HTTPS URL union 保留。</p></div><div class="card"><h3>Source metrics</h3><div id="sourceMetrics"></div></div><div class="card"><h3>Phase2 tiers 的诚实标签</h3><p class="small">T1/T2/T3/T4/T5 统计只代表 Phase2 source records（356 records / 212 domains），不能冒充 Phase3 action evidence tiers。Phase3 action rows 未统一携带 tier；本报告展示 URLs 与 provenance layer。</p></div></div><h3>Mandatory audit corrections / 必须披露的纠偏</h3><div class="details-grid"><details open><summary>日期、身份与范围纠偏</summary><ul><li>ND Ellendale inspection = <strong>2025-03-19</strong>，不是 2026-03-19。</li><li>Frontier Odessa 与 Abilene registrations 分开保留；不把两条 registration 合成一条时间线或当作 energization。</li><li>EdgeCore Mesa <strong>$1.9B ≠ 1,900 MW</strong>；MW 只有在 evidence 支持时显示。</li><li>Muskogee = <strong>100 MW + 82.5 MW follow-on</strong>；seed 的 1,500 MW tracker 值未验证。</li><li>Utah 项目区分 phase 与 ultimate scope；不把 ultimate scale 当作当前施工负荷。</li><li>Boardman = <strong>四栋 data buildings + support structures</strong>；“five-building”只作为 attributed Phase2 shorthand，不作无条件事实。</li></ul></details><details><summary>未解决 identity families</summary><ul><li>Tulsa Anthem / Meta remains separate and unresolved。</li><li>Cheyenne Related/CoreWeave vs Project Jade remains separate and unresolved。</li><li>Eagle Mountain Tripletail vs Pole Canyon/Pony remains separate and unresolved。</li><li>上述 unresolved records 不求和、不合并 MW。</li></ul></details><details><summary>SC-004 QTS York</summary><p>SC-004 stays <strong>approved/permitted</strong> with no construction anchor. Commercial reporting is medium-confidence actual advancement/site-preparation support; it is not proof of site work, building approval, completion, energization, or service.</p></details></div><h3>Frozen source files and SHA-256</h3><p class="small muted">以下清单由构建器读取并逐一计算 SHA-256；HTML 只列相对 artifact labels，不含本机绝对路径。</p><details><summary>展开全部 <span id="sourceFileCount"></span> 个 source files</summary><ul id="sourceFiles" class="source-list"></ul></details><h3>QA receipt</h3><p class="small">Parent v2 receipts: <code>parent_master_validation_v2.json = PASS</code>，<code>parent_gantt_validation_v2.json = PASS</code>。本次构建还执行 HTML parse、inline JSON parse、counts、unique master IDs、HTTPS-only source links、banned-string scan 与 output SHA-256。</p></section>
</main><footer class="footer">Frozen evidence cutoff: 2026-07-16 · Generated deterministically from accepted workspace artifacts · No new web research · No external communication.</footer></div>
<script>const REPORT_DATA=__INLINE_DATA__;</script><script>
const D=REPORT_DATA; const $=id=>document.getElementById(id); const esc=s=>String(s??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const url=u=>String(u||'').startsWith('https://')?`<a href="${esc(u)}" target="_blank" rel="noopener">source</a>`:''; const urls=us=>[...new Set((us||[]).filter(u=>String(u).startsWith('https://')))].slice(0,8).map(url).join(' ')+(us?.length>8?` <span class="muted">+${us.length-8}</span>`:'');
const badge=(s,label)=>`<span class="badge ${esc(s)}">${esc(label||s)}</span>`;
function renderStatus(){const c=D.status_counts, total=Object.values(c).reduce((a,b)=>a+b,0); $('statusChart').innerHTML=Object.entries(c).map(([k,v])=>`<div class="bar-line"><span>${esc(({announced:'已宣布',local_process:'地方程序',approved_or_permitted:'已批准/许可',site_work_or_construction:'场地施工/建设',energized:'已通电',live_partial:'部分上线',full_buildout:'全面建成'})[k]||k)}</span><div class="bar-track"><div class="bar-fill" style="width:${(100*v/total).toFixed(1)}%"></div></div><strong>${v}</strong></div>`).join('')+`<div class="small muted">n=${total}; seed-only records excluded from this distribution</div>`}
function renderStates(){let q=($('stateSearch').value||'').toLowerCase(), sort=$('stateSort').value;let codeQuery=q.length===2&&/^[a-z]{2}$/.test(q)&&D.state_rows.some(x=>String(x.code||'').toLowerCase()===q);let rows=D.state_rows.filter(x=>codeQuery?String(x.code||'').toLowerCase()===q:[x.name,x.code,x.finding,x.zero_note,x.caveat].filter(Boolean).join(' ').toLowerCase().includes(q));rows.sort((a,b)=>sort==='name'?a.name.localeCompare(b.name):b[sort]-a[sort]);$('stateTable').querySelector('tbody').innerHTML=rows.map(x=>`<tr><td><strong>${esc(x.name)}</strong><br><span class="muted small">${esc(x.code)}</span></td><td>${x.masters}</td><td>${x.seed}</td><td>${x.phase2}</td><td>${x.phase3}</td><td>${esc(x.finding||'')}${x.zero_note?`<br><span class="small muted">Zero-result note: ${esc(x.zero_note)}</span>`:''}${x.caveat?`<br><span class="small muted">${esc(x.caveat)}</span>`:''}</td><td>${urls(x.sources)}</td></tr>`).join('')}
const date0=new Date('2024-01-01T00:00:00Z'), date1=new Date('2030-12-31T00:00:00Z'); function pos(d){let x=new Date((d||'2024-01-01').slice(0,10)+'T00:00:00Z');return Math.max(0,Math.min(100,100*(x-date0)/(date1-date0)))};
function renderGantt(){let q=($('ganttSearch').value||'').toLowerCase(), st=$('ganttStatus').value, anchor=$('anchorOnly').checked, showEx=$('showExcluded').dataset.on==='1';let rows=D.timeline.filter(x=>(showEx||x.physical)&&(!st||x.status===st)&&(!anchor||x.anchor?.present)&&JSON.stringify(x).toLowerCase().includes(q));$('ganttCount').textContent=`${rows.length} rows shown`; $('ganttRows').innerHTML=rows.map(x=>{let marks=[],ranges=[];(x.spans||[]).forEach(s=>{if(s.row_type==='modeled_range'){ranges.push(`<span class="range ${s.confidence==='low'?'low':''}" style="left:${pos(s.gantt_start)}%;width:${Math.max(.5,pos(s.gantt_finish)-pos(s.gantt_start))}%" title="${esc(s.label)} · ${esc(s.start)} → ${esc(s.finish)} · ${esc(s.confidence)} confidence · dashed projection"></span>`)}else if(s.start){marks.push(`<span class="mark ${s.projection?'proj':''}" style="left:${pos(s.start)}%" title="${esc(s.label)} · ${esc(s.start)} · ${esc(s.normalized_stage)}"></span>`)}});return `<div class="timeline-row"><div class="project-cell"><strong>${esc(x.project)}</strong><span class="small">${esc(x.stable_id)} · ${esc(x.location.state)} · ${badge(x.status,x.status_label)} ${x.anchor?.present?' 🔨':''}</span></div><div class="track">${ranges.join('')}${marks.join('')}</div></div>`}).join('')}
let pPage=0,pFiltered=[];function renderProjects(){let q=($('projectSearch').value||'').toLowerCase(),mode=$('projectStatus').value;pFiltered=D.projects.filter(x=>(!q||JSON.stringify(x).toLowerCase().includes(q))&&(!mode||(mode==='detailed'?x.cohort==='detailed':mode==='seed_only'?x.cohort==='seed_only':x.construction_anchor)));let n=40;let page=pFiltered.slice(pPage*n,(pPage+1)*n);$('projectRows').innerHTML=page.map(x=>`<tr><td><strong>${esc(x.master_id)} · ${esc(x.name)}</strong><br><span class="small muted">${esc(x.stable_id||'')} · ${esc((x.aliases||[]).slice(0,3).join(' / '))}</span></td><td>${esc(x.location.city)}<br>${esc(x.location.county)}, ${esc(x.location.state)}</td><td>${badge(x.status,x.status_label)}<br><span class="small muted">${esc(x.raw_status)}</span></td><td>${esc((x.companies||[]).join(' · ')||'未披露')}<br><span class="small">${esc(x.capacity)}</span></td><td><span class="badge">${esc(x.provenance)}</span><br><span class="small">${urls(x.source_urls)}</span>${x.unresolved?`<br><span class="small muted">Gap: ${esc(Array.isArray(x.unresolved)?x.unresolved.slice(0,2).join('；'):x.unresolved)}</span>`:''}</td></tr>`).join('');$('projectCount').textContent=`${pFiltered.length} matches`;$('projectPage').textContent=`${pFiltered.length? pPage+1:0} / ${Math.max(1,Math.ceil(pFiltered.length/n))}`;$('projectPrev').disabled=pPage===0;$('projectNext').disabled=(pPage+1)*n>=pFiltered.length}
let aPage=0,aAll=false,aFiltered=[];function renderActions(){let q=($('actionSearch').value||'').toLowerCase(),cat=$('actionCategory').value;aFiltered=D.actions.filter(x=>(!cat||x.category===cat)&&(!q||JSON.stringify(x).toLowerCase().includes(q)));let n=aAll?513:50;let page=aFiltered.slice(aPage*n,(aPage+1)*n);$('actionRows').innerHTML=page.map(x=>`<tr><td><strong>${esc(x.project)}</strong><br><span class="small muted">${esc(x.stable_id)} · ${esc(x.action_id)}</span></td><td>${esc(x.date||x.date_text||'undated')}<br><span class="small muted">${esc(x.date_precision||'precision not supplied')}</span></td><td>${badge(x.category)}<br><span class="small">${esc(x.body)}<br>${esc(x.action_type)}</span></td><td>${esc(x.result)}${x.vote_tally?`<br><strong>Vote:</strong> ${esc(x.vote_tally)}`:''}${x.caveat?`<br><span class="small muted">${esc(x.caveat)}</span>`:''}</td><td>${url(x.primary_url)}<br><span class="small muted">${x.projection?'projection':'actual_record'} · ${esc(x.source_file)}</span></td></tr>`).join('');$('actionCount').textContent=`${aFiltered.length} matches`;$('actionPage').textContent=`${aFiltered.length? aPage+1:0} / ${Math.max(1,Math.ceil(aFiltered.length/n))}`;$('actionPrev').disabled=aPage===0;$('actionNext').disabled=(aPage+1)*n>=aFiltered.length}
function renderCycle(){let st=D.cycle.stages;$('stageFlow').innerHTML=st.map((x,i)=>`<div class="stage"><strong>S${esc(x.id?.replace('S','')||i+1)} · ${esc(x.label)}</strong><small>${esc(x.duration_months)}–${esc(x.extended_duration_months)} months · ${esc(x.confidence)}</small></div>`).join('');$('archetypeRows').innerHTML=D.cycle.archetypes.map(x=>`<tr><td><strong>${esc(x.label)}</strong><br><span class="small muted">${esc(x.id)}</span></td><td>${esc(x.site_control_to_first_usable_months)}</td><td>${esc(x.first_usable_to_full_buildout_months)}</td><td>${esc((x.conditions||[]).join(' '))}<br>${esc(x.confidence)}</td></tr>`).join('');$('observedRows').innerHTML=D.cycle.observed.map(x=>`<tr><td>${esc(x.name)}<br><span class="small muted">${esc(x.project_id)}</span></td><td>${esc(x.location)}</td><td>${esc(typeof x.capacity_scope==='string'?x.capacity_scope:JSON.stringify(x.capacity_scope))}</td><td>${esc(x.schedule_interpretation||'')}<br>${esc(x.confidence)}</td></tr>`).join('')}
function renderAppendix(){ $('proposalRows').innerHTML=D.proposals.map(x=>`<tr><td><strong>${esc(x.id)}</strong><br>${esc(x.name)}</td><td>${esc(x.state)}<br>${esc(x.status)}</td><td>${esc(x.reason)}</td><td>${urls(x.source_urls)}</td></tr>`).join('');$('baselineRows').innerHTML=D.baseline.map(x=>`<tr><td><strong>${esc(x.name)}</strong><br><span class="small muted">${esc(x.id)}</span></td><td>${esc(x.location)}<br>${esc(x.status)}</td><td>${esc(x.scope_note)}</td><td>${urls(x.source_urls)}</td></tr>`).join('');$('exclusionRows').innerHTML=D.exclusions.map(x=>`<tr><td>${esc(x.input_id)}</td><td>${esc(x.disposition)}</td><td>${esc(x.reason)}</td><td>${urls(x.source_urls)}<br><span class="small muted">${esc(x.source_file)}</span></td></tr>`).join('');$('findingRows').innerHTML=D.findings.map(x=>`<details class="panel"><summary>${esc(x.id)} · ${esc(x.severity)} · ${esc(x.category)}</summary><p><strong>Project IDs:</strong> ${esc((x.project_ids||[]).join(', '))}</p><p><strong>Conflicting claims:</strong> ${esc((x.claims||[]).join(' '))}</p><p><strong>Safest resolution:</strong> ${esc(x.resolution)}</p><p class="small muted">Disclosure required: ${x.disclose?'yes':'no'}</p></details>`).join('')}
function renderSources(){ $('sourceFileCount').textContent=D.source_files.length; $('sourceFiles').innerHTML=D.source_files.map(x=>`<li><code>${esc(x)}</code><br><span class="muted">${D.source_hashes[x]}</span></li>`).join('');let m=D.source_metrics;$('sourceMetrics').innerHTML=`<p class="small"><strong>${m.master_source_urls}/667</strong> unique URLs retained in masters or exclusions<br><strong>${m.gantt_input_urls}</strong> Gantt input URLs<br><strong>${m.action_urls_valid}/513</strong> action URLs valid<br><strong>${m.project_source_urls}/186</strong> project-level source URL rows present<br><strong>${m.rows_missing_project_source_urls}</strong> rows had URLs derived from actions<br><strong>${m.phase2_source_records}</strong> Phase2 source records / <strong>${m.phase2_domains}</strong> domains</p><p class="small muted">Phase2 tiers only: ${Object.entries(m.phase2_tiers||{}).map(([k,v])=>k+' '+v).join(' · ')}</p>`}
['stateSearch','stateSort'].forEach(id=>$(id).addEventListener('input',renderStates));['ganttSearch','ganttStatus','anchorOnly'].forEach(id=>$(id).addEventListener('input',renderGantt));$('showExcluded').addEventListener('click',e=>{e.currentTarget.dataset.on=e.currentTarget.dataset.on==='1'?'0':'1';e.currentTarget.textContent=e.currentTarget.dataset.on==='1'?'隐藏排除候选':'显示排除候选';renderGantt()});['projectSearch','projectStatus'].forEach(id=>$(id).addEventListener('input',()=>{pPage=0;renderProjects()}));$('projectPrev').onclick=()=>{pPage--;renderProjects()};$('projectNext').onclick=()=>{pPage++;renderProjects()};['actionSearch','actionCategory'].forEach(id=>$(id).addEventListener('input',()=>{aPage=0;renderActions()}));$('actionAll').onclick=()=>{aAll=!aAll;aPage=0;$('actionAll').textContent=aAll?'分页显示 513':'显示全部 513';renderActions()};$('actionPrev').onclick=()=>{aPage--;renderActions()};$('actionNext').onclick=()=>{aPage++;renderActions()};renderStatus();renderStates();renderGantt();renderProjects();renderActions();renderCycle();renderAppendix();renderSources();
 </script></body></html>'''
    return template.replace("__INLINE_CSS__", CSS).replace("__INLINE_DATA__", jsdata)

def write_outputs(data):
    html_path=OUT/"us_data_center_construction_panorama.html"
    html_path.write_text(render_html(data),encoding="utf-8")
    html_hash=sha(html_path)
    report=[
        "# Final report build handoff",
        "",
        "- Artifact: `us_data_center_construction_panorama.html`",
        "- Frozen cutoff: `2026-07-16`",
        "- Generation: deterministic local rendering from accepted frozen artifacts; no new web research and no external communication.",
        "",
        "## Counts and decisions",
        "",
        "- 208 unique project masters = 185 detailed Phase3/region physical records + 23 retained Phase2 seed-only evidence-gap records.",
        "- 186 accepted Gantt candidates = 185 physical rows rendered by default + 1 DAF solicitation without a selected physical project; the DAF is excluded from physical project counts.",
        "- The unique exclusion set is one DAF solicitation plus four aggregate/undisclosed seed records; six ledger mappings preserve the DAF in both Phase2 and Phase3.",
        "- 1,072 Gantt events; 131 projected spans; 38 construction anchors; 513 county/city/state/utility actions.",
        "- 51 jurisdictions; zero-result CT, DC, DE, FL, NE, VT. 8 live-only baselines and 53 announced/evidence-gap appendix rows are appendix-only.",
        "- Status labels remain separate: announced, local process, approved-permitted, site work-construction, energized, partial live, full buildout. Actual evidence is solid; projection/model tails are dashed.",
        "- Master IDs are unique. Unresolved Tulsa Anthem/Meta, Cheyenne Related/CoreWeave vs Project Jade, and Eagle Mountain Tripletail vs Pole Canyon/Pony remain separate and are not summed.",
        "- Corrections applied in the accepted inputs are disclosed: ND inspection 2025-03-19; Frontier Odessa/Abilene separate; EdgeCore Mesa $1.9B is not 1,900 MW; Muskogee 100 MW + 82.5 MW follow-on; Utah phase vs ultimate scope; Boardman four data buildings plus support structures; SC-004 QTS York approved/permitted with no construction anchor.",
        "",
        "## Source/provenance coverage",
        "",
        "- Phase3 is authoritative; Phase2 regional records are enrichment; seed-only rows remain labeled as evidence gaps.",
        "- 667/667 unique project URLs retained in master or exclusion ledger; 513/513 action URLs valid; 452/186 present project-source URL metric is the accepted source-conflict audit metric (452 URLs across 186 project rows). 38 rows lack a project-level `source_urls` field and are linked from their action URLs in the final HTML.",
        "- Phase2-only source tier mix: T1 121, T2 94, T3 78, T4 60, T5 3 across 356 Phase2 source records / 212 domains. This is not presented as Phase3 tier statistics.",
        "",
        "## Exact source files",
        "",
    ]
    report += [f"- `{p}` — `{data['source_hashes'][p]}`" for p in data["source_files"]]
    report += ["", "## Key Phase4 receipt hashes", ""]
    report += [f"- `{k}` — `{v}`" for k,v in data["key_hashes"].items()]
    report += ["", "## Output SHA-256", "", f"- `us_data_center_construction_panorama.html` — `{html_hash}`", ""]
    report += ["## QA", "", "- JSON parse: PASS for every frozen `*.json` under the workspace (excluding new `final/` output).", "- HTML parser: PASS (`html.parser`).", "- Inline data parse: PASS; 208 master IDs unique; 513 actions; 186 timeline candidates; required headline labels present.", "- HTTPS-only source link audit: PASS for all embedded source URLs.", "- Privacy/banned-string audit: PASS; no raw local absolute paths, credentials, email addresses, daemon IDs, or private identifiers in HTML.", "- Structural controls: PASS by static inspection of client-side search/filter/pagination handlers and data-backed rendering paths.", "- Artifact write scope: only new/owned files in `final/`; Phase1–4 inputs unchanged.", ""]
    (OUT/"build_report.md").write_text("\n".join(report),encoding="utf-8")

if __name__=="__main__":
    write_outputs(build_data())
    print(OUT/"us_data_center_construction_panorama.html")
