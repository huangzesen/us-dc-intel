#!/usr/bin/env python3
"""Export static GRIDWATCH data for the Astro site."""

from __future__ import annotations

import json
import sqlite3
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "datacenters.db"
OUT_PATH = ROOT / "astro" / "src" / "data" / "datacenters.json"
AMERICAS_MANIFEST = ROOT / "scripts" / "expansion" / "americas" / "americas-manifest.jsonl"
COUNTIES_EXPLORED = 3222

STATE_NAMES = {
    "AL": "Alabama",
    "AK": "Alaska",
    "AZ": "Arizona",
    "AR": "Arkansas",
    "CA": "California",
    "CO": "Colorado",
    "CT": "Connecticut",
    "DE": "Delaware",
    "DC": "District of Columbia",
    "FL": "Florida",
    "GA": "Georgia",
    "HI": "Hawaii",
    "ID": "Idaho",
    "IL": "Illinois",
    "IN": "Indiana",
    "IA": "Iowa",
    "KS": "Kansas",
    "KY": "Kentucky",
    "LA": "Louisiana",
    "ME": "Maine",
    "MD": "Maryland",
    "MA": "Massachusetts",
    "MI": "Michigan",
    "MN": "Minnesota",
    "MS": "Mississippi",
    "MO": "Missouri",
    "MT": "Montana",
    "NE": "Nebraska",
    "NV": "Nevada",
    "NH": "New Hampshire",
    "NJ": "New Jersey",
    "NM": "New Mexico",
    "NY": "New York",
    "NC": "North Carolina",
    "ND": "North Dakota",
    "OH": "Ohio",
    "OK": "Oklahoma",
    "OR": "Oregon",
    "PA": "Pennsylvania",
    "PR": "Puerto Rico",
    "RI": "Rhode Island",
    "SC": "South Carolina",
    "SD": "South Dakota",
    "TN": "Tennessee",
    "TX": "Texas",
    "UT": "Utah",
    "VT": "Vermont",
    "VA": "Virginia",
    "WA": "Washington",
    "WV": "West Virginia",
    "WI": "Wisconsin",
    "WY": "Wyoming",
}

NAME_TO_STATE = {name.upper(): abbr for abbr, name in STATE_NAMES.items()}
NAME_TO_STATE.update({"WASHINGTON DC": "DC", "DISTRICT OF COLUMBIA": "DC"})

STATE_LAYOUT = {
    "AK": [0, 0],
    "ME": [0, 10],
    "VT": [1, 9],
    "NH": [1, 10],
    "WA": [2, 0],
    "ID": [2, 1],
    "MT": [2, 2],
    "ND": [2, 3],
    "MN": [2, 4],
    "IL": [2, 5],
    "WI": [2, 6],
    "MI": [2, 7],
    "NY": [2, 8],
    "MA": [2, 9],
    "OR": [3, 0],
    "NV": [3, 1],
    "WY": [3, 2],
    "SD": [3, 3],
    "IA": [3, 4],
    "IN": [3, 5],
    "OH": [3, 6],
    "PA": [3, 7],
    "NJ": [3, 8],
    "CT": [3, 9],
    "RI": [3, 10],
    "CA": [4, 0],
    "UT": [4, 1],
    "CO": [4, 2],
    "NE": [4, 3],
    "MO": [4, 4],
    "KY": [4, 5],
    "WV": [4, 6],
    "VA": [4, 7],
    "MD": [4, 8],
    "DE": [4, 9],
    "AZ": [5, 1],
    "NM": [5, 2],
    "KS": [5, 3],
    "AR": [5, 4],
    "TN": [5, 5],
    "NC": [5, 6],
    "SC": [5, 7],
    "DC": [5, 8],
    "OK": [6, 3],
    "LA": [6, 4],
    "MS": [6, 5],
    "AL": [6, 6],
    "GA": [6, 7],
    "HI": [7, 0],
    "TX": [7, 3],
    "FL": [7, 8],
    "PR": [7, 10],
}

ZH_NAMES = {
    "AL": "亚拉巴马",
    "AK": "阿拉斯加",
    "AZ": "亚利桑那",
    "AR": "阿肯色",
    "CA": "加利福尼亚",
    "CO": "科罗拉多",
    "CT": "康涅狄格",
    "DE": "特拉华",
    "DC": "华盛顿特区",
    "FL": "佛罗里达",
    "GA": "佐治亚",
    "HI": "夏威夷",
    "ID": "爱达荷",
    "IL": "伊利诺伊",
    "IN": "印第安纳",
    "IA": "艾奥瓦",
    "KS": "堪萨斯",
    "KY": "肯塔基",
    "LA": "路易斯安那",
    "ME": "缅因",
    "MD": "马里兰",
    "MA": "马萨诸塞",
    "MI": "密歇根",
    "MN": "明尼苏达",
    "MS": "密西西比",
    "MO": "密苏里",
    "MT": "蒙大拿",
    "NE": "内布拉斯加",
    "NV": "内华达",
    "NH": "新罕布什尔",
    "NJ": "新泽西",
    "NM": "新墨西哥",
    "NY": "纽约",
    "NC": "北卡罗来纳",
    "ND": "北达科他",
    "OH": "俄亥俄",
    "OK": "俄克拉何马",
    "OR": "俄勒冈",
    "PA": "宾夕法尼亚",
    "PR": "波多黎各",
    "RI": "罗得岛",
    "SC": "南卡罗来纳",
    "SD": "南达科他",
    "TN": "田纳西",
    "TX": "得克萨斯",
    "UT": "犹他",
    "VT": "佛蒙特",
    "VA": "弗吉尼亚",
    "WA": "华盛顿州",
    "WV": "西弗吉尼亚",
    "WI": "威斯康星",
    "WY": "怀俄明",
}

COUNTRY_ZH_NAMES = {
    "AI": "安圭拉",
    "AG": "安提瓜和巴布达",
    "AR": "阿根廷",
    "AW": "阿鲁巴",
    "BB": "巴巴多斯",
    "BL": "圣巴泰勒米",
    "BM": "百慕大",
    "BO": "玻利维亚",
    "BQ": "博内尔、圣尤斯特歇斯和萨巴",
    "BR": "巴西",
    "BS": "巴哈马",
    "BZ": "伯利兹",
    "CA": "加拿大",
    "CL": "智利",
    "CO": "哥伦比亚",
    "CR": "哥斯达黎加",
    "CU": "古巴",
    "CW": "库拉索",
    "DM": "多米尼克",
    "DO": "多米尼加共和国",
    "EC": "厄瓜多尔",
    "FK": "福克兰群岛",
    "GD": "格林纳达",
    "GF": "法属圭亚那",
    "GL": "格陵兰",
    "GP": "瓜德罗普",
    "GS": "南乔治亚和南桑威奇群岛",
    "GT": "危地马拉",
    "GY": "圭亚那",
    "HN": "洪都拉斯",
    "HT": "海地",
    "JM": "牙买加",
    "KN": "圣基茨和尼维斯",
    "KY": "开曼群岛",
    "LC": "圣卢西亚",
    "MF": "圣马丁",
    "MQ": "马提尼克",
    "MS": "蒙特塞拉特",
    "MX": "墨西哥",
    "NI": "尼加拉瓜",
    "PA": "巴拿马",
    "PE": "秘鲁",
    "PM": "圣皮埃尔和密克隆",
    "PR": "波多黎各",
    "PY": "巴拉圭",
    "SR": "苏里南",
    "SV": "萨尔瓦多",
    "SX": "荷属圣马丁",
    "TC": "特克斯和凯科斯群岛",
    "TT": "特立尼达和多巴哥",
    "US": "美国",
    "UY": "乌拉圭",
    "VC": "圣文森特和格林纳丁斯",
    "VE": "委内瑞拉",
    "VG": "英属维尔京群岛",
    "VI": "美属维尔京群岛",
}

STATUS_ORDER = ["ann", "pla", "app", "con", "op"]
STATUS_LABELS = {
    "ann": ["Announced", "已公告"],
    "pla": ["Planned", "规划中"],
    "app": ["Approved", "已批准"],
    "con": ["Construction", "在建"],
    "op": ["Operational", "运营中"],
    "rej": ["Rejected", "已否决"],
    "unk": ["Unknown", "未知"],
}


def state_abbr(value: str | None) -> str | None:
    if not value:
        return None
    raw = value.strip()
    upper = raw.upper()
    if upper in STATE_NAMES:
        return upper
    return NAME_TO_STATE.get(upper)


def status_key(value: str | None) -> str:
    s = (value or "").strip().lower()
    if "construct" in s or "under construction" in s:
        return "con"
    if "operational" in s or s in {"active", "online"}:
        return "op"
    if "approved" in s or "permitted" in s or "greenlit" in s or "agreement executed" in s:
        return "app"
    if "planned" in s or "planning" in s or "site acquired" in s or "zoned" in s:
        return "pla"
    if "announced" in s or "filed" in s:
        return "ann"
    if "rejected" in s or "denied" in s:
        return "rej"
    return "unk"


def evidence_bucket(value: str | None) -> str:
    s = (value or "").strip().lower()
    if s in {"official", "news", "tracker"}:
        return s
    if s == "social":
        return "other"
    return "other"


def clean_text(value: str | None, fallback: str) -> str:
    value = (value or "").strip()
    return value if value else fallback


def row_value(row: sqlite3.Row, columns: set[str], column: str, fallback=None):
    return row[column] if column in columns else fallback


def country_code(value: str | None) -> str:
    code = (value or "US").strip().upper()
    return code or "US"


def load_americas() -> dict[str, str]:
    if not AMERICAS_MANIFEST.exists():
        return {"US": "United States"}
    countries = {}
    with AMERICAS_MANIFEST.open(encoding="utf-8") as handle:
        for line in handle:
            item = json.loads(line)
            countries[item["country_code"].upper()] = item["country_name"]
    return countries


def empty_funnel() -> dict[str, dict[str, float | int]]:
    return defaultdict(lambda: {"count": 0, "capacity_mw": 0.0})


def empty_years() -> dict[int, dict[str, int]]:
    return {year: {"pipeline": 0, "construction": 0, "operational": 0} for year in range(2018, 2031)}


def funnel_rows(acc: dict[str, dict[str, float | int]]) -> list[dict]:
    return [
        {
            "key": key,
            "count": int(acc[key]["count"]),
            "capacity_mw": round(float(acc[key]["capacity_mw"]), 1),
            "label": STATUS_LABELS[key],
        }
        for key in STATUS_ORDER
    ]


def wave_rows(years: dict[int, dict[str, int]]) -> list[dict]:
    return [
        {"year": year, **parts}
        for year, parts in years.items()
    ]


def add_year_signal(years: dict[int, dict[str, int]], year: int | None, key: str) -> None:
    if year in years:
        if key == "op":
            years[year]["operational"] += 1
        elif key == "con":
            years[year]["construction"] += 1
        elif key in {"ann", "pla", "app"}:
            years[year]["pipeline"] += 1


def main() -> None:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    rows = con.execute("select * from centers").fetchall()
    columns = set(rows[0].keys()) if rows else set()
    americas = load_americas()

    total_mw = sum(float(r["capacity_mw"] or 0) for r in rows)
    source_count = con.execute("select count(url) from sources where url is not null and trim(url) != ''").fetchone()[0]
    county_count = con.execute(
        "select count(distinct lower(county) || ',' || upper(state)) "
        "from centers where county is not null and trim(county) != ''"
    ).fetchone()[0]

    state_acc: dict[str, dict[str, float | int]] = defaultdict(lambda: {"facilities": 0, "capacity_mw": 0.0})
    country_acc: dict[str, dict] = defaultdict(
        lambda: {
            "facilities": 0,
            "capacity_mw": 0.0,
            "subnationals": defaultdict(lambda: {"facilities": 0, "capacity_mw": 0.0}),
            "funnel": empty_funnel(),
            "years": empty_years(),
        }
    )
    county_keys = set()
    status_acc = empty_funnel()
    years = empty_years()
    dev_acc: dict[str, dict[str, float | int]] = defaultdict(lambda: {"facilities": 0, "capacity_mw": 0.0})
    evidence_acc: dict[str, int] = defaultdict(int)
    centers = []

    for r in rows:
        code = country_code(row_value(r, columns, "country", "US"))
        subnational = clean_text(row_value(r, columns, "subnational", None), "")
        abbr = state_abbr(subnational or r["state"])
        mw = float(r["capacity_mw"] or 0)
        key = status_key(r["status"])
        year = r["year"] if isinstance(r["year"], int) else None
        owner = clean_text(r["owner"], "Unknown operator")
        subnational_label = subnational or (STATE_NAMES.get(abbr) if abbr else clean_text(r["state"], "Unknown"))

        country_acc[code]["facilities"] += 1
        country_acc[code]["capacity_mw"] += mw
        country_acc[code]["funnel"][key]["count"] += 1
        country_acc[code]["funnel"][key]["capacity_mw"] += mw
        add_year_signal(country_acc[code]["years"], year, key)
        if subnational_label != "Unknown":
            country_acc[code]["subnationals"][subnational_label]["facilities"] += 1
            country_acc[code]["subnationals"][subnational_label]["capacity_mw"] += mw

        if code == "US" and abbr in STATE_LAYOUT:
            state_acc[abbr]["facilities"] += 1
            state_acc[abbr]["capacity_mw"] += mw
        county = clean_text(r["county"], "Unknown")
        if code == "US" and abbr and county != "Unknown":
            county_keys.add((county.lower(), abbr))
        status_acc[key]["count"] += 1
        status_acc[key]["capacity_mw"] += mw
        dev_acc[owner]["facilities"] += 1
        dev_acc[owner]["capacity_mw"] += mw
        evidence_acc[evidence_bucket(r["evidence_grade"])] += 1

        add_year_signal(years, year, key)

        if key not in {"rej", "unk"} and mw > 0:
            centers.append(
                {
                    "project": clean_text(r["canonical_project"], "Unnamed project"),
                    "developer": owner,
                    "county": county,
                    "state": abbr,
                    "country": code,
                    "subnational": subnational_label,
                    "capacity_mw": round(mw, 1),
                    "status": key,
                    "year": year,
                    "evidence": evidence_bucket(r["evidence_grade"]),
                }
            )

    states = []
    for abbr, pos in STATE_LAYOUT.items():
        acc = state_acc[abbr]
        states.append(
            {
                "abbr": abbr,
                "row": pos[0],
                "col": pos[1],
                "facilities": int(acc["facilities"]),
                "capacity_mw": round(float(acc["capacity_mw"]), 1),
                "name_en": STATE_NAMES[abbr],
                "name_zh": ZH_NAMES[abbr],
            }
        )

    countries = []
    for code, acc in country_acc.items():
        name_en = americas.get(code, code)
        subnationals = sorted(
            (
                {
                    "name": name,
                    "facilities": int(sub["facilities"]),
                    "capacity_mw": round(float(sub["capacity_mw"]), 1),
                }
                for name, sub in acc["subnationals"].items()
            ),
            key=lambda item: (item["capacity_mw"], item["facilities"]),
            reverse=True,
        )
        countries.append(
            {
                "code": code,
                "name_en": name_en,
                "name_zh": COUNTRY_ZH_NAMES.get(code, name_en),
                "facilities": int(acc["facilities"]),
                "capacity_mw": round(float(acc["capacity_mw"]), 1),
                "capacity_gw": round(float(acc["capacity_mw"]) / 1000, 1),
                "subnationals": subnationals,
                "funnel": funnel_rows(acc["funnel"]),
                "years": wave_rows(acc["years"]),
            }
        )
    countries.sort(key=lambda item: (item["capacity_mw"], item["facilities"], item["code"]), reverse=True)

    funnel = funnel_rows(status_acc)
    wave = wave_rows(years)

    devs_by_mw = sorted(dev_acc.items(), key=lambda item: item[1]["capacity_mw"], reverse=True)[:10]
    devs_by_n = sorted(dev_acc.items(), key=lambda item: item[1]["facilities"], reverse=True)[:10]
    developers = {
        "mw": [
            {"name": name, "capacity_mw": round(float(acc["capacity_mw"]), 1), "facilities": int(acc["facilities"])}
            for name, acc in devs_by_mw
        ],
        "n": [
            {"name": name, "capacity_mw": round(float(acc["capacity_mw"]), 1), "facilities": int(acc["facilities"])}
            for name, acc in devs_by_n
        ],
    }

    evidence = [
        {"key": key, "count": int(evidence_acc[key])}
        for key in ["official", "news", "tracker", "other"]
    ]

    flagship = sorted(centers, key=lambda c: (c["capacity_mw"], c["year"] or 0), reverse=True)[:60]

    payload = {
        "generated_date": "2026-08-11",
        "totals": {
            "capacity_mw": round(total_mw, 1),
            "capacity_gw": round(total_mw / 1000, 1),
            "facilities": len(rows),
            "sources": int(source_count),
            "counties_with_projects": int(county_count),
            "counties_explored": COUNTIES_EXPLORED,
            "countries_with_projects": len(country_acc),
            "countries_explored": len(americas),
        },
        "countries": countries,
        "states": states,
        "funnel": funnel,
        "years": wave,
        "developers": developers,
        "evidence": evidence,
        "centers": flagship,
        "status_labels": STATUS_LABELS,
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"wrote {OUT_PATH} ({OUT_PATH.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
