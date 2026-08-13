#!/usr/bin/env python3
"""Export static GRIDWATCH data for the Astro site."""

from __future__ import annotations

import json
import re
import sqlite3
import unicodedata
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "datacenters.db"
OUT_PATH = ROOT / "astro" / "src" / "data" / "datacenters.json"
AMERICAS_MANIFEST = ROOT / "scripts" / "expansion" / "americas" / "americas-manifest.jsonl"
COUNTY_COORDS_PATH = ROOT / "scripts" / "expansion" / "us-county-coords.json"
COORD_RESULTS_DIR = ROOT / "scripts" / "expansion" / "world" / "coord-results"
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

# Approximate geographic centroids used for the interactive Leaflet map.
# US, Brazil, and Mexico were checked against common published country-center
# coordinates; the remaining Americas entries are approximate visual anchors.
COUNTRY_COORDS = {
    "AI": [18.2206, -63.0686],
    "AG": [17.0608, -61.7964],
    "AR": [-38.4161, -63.6167],
    "AS": [-14.275, -170.702],
    "AW": [12.5211, -69.9683],
    "BB": [13.1939, -59.5432],
    "BL": [17.9, -62.8333],
    "BM": [32.3078, -64.7505],
    "BO": [-16.2902, -63.5887],
    "BQ": [12.1784, -68.2385],
    "BR": [-14.235, -51.9253],
    "BS": [25.0343, -77.3963],
    "BZ": [17.1899, -88.4976],
    "CA": [56.1304, -106.3468],
    "CL": [-35.6751, -71.543],
    "CO": [4.5709, -74.2973],
    "CR": [9.7489, -83.7534],
    "CU": [21.5218, -77.7812],
    "CW": [12.1696, -68.99],
    "DM": [15.415, -61.371],
    "DO": [18.7357, -70.1627],
    "EC": [-1.8312, -78.1834],
    "FK": [-51.7963, -59.5236],
    "GD": [12.1165, -61.679],
    "GF": [3.9339, -53.1258],
    "GL": [71.7069, -42.6043],
    "GP": [16.265, -61.551],
    "GS": [-54.4296, -36.5879],
    "GT": [15.7835, -90.2308],
    "GU": [13.475, 144.75],
    "GY": [4.8604, -58.9302],
    "HN": [15.2, -86.2419],
    "HT": [18.9712, -72.2852],
    "JM": [18.1096, -77.2975],
    "KN": [17.3578, -62.783],
    "KY": [19.3133, -81.2546],
    "LC": [13.9094, -60.9789],
    "MF": [18.0708, -63.0501],
    "MQ": [14.6415, -61.0242],
    "MP": [15.213, 145.755],
    "MS": [16.7425, -62.1874],
    "MX": [23.6345, -102.5528],
    "NI": [12.8654, -85.2072],
    "PA": [8.538, -80.7821],
    "PE": [-9.19, -75.0152],
    "PM": [46.8852, -56.3159],
    "PR": [18.2208, -66.5901],
    "PY": [-23.4425, -58.4438],
    "SR": [3.9193, -56.0278],
    "SV": [13.7942, -88.8965],
    "SX": [18.0425, -63.0548],
    "TC": [21.694, -71.7979],
    "TT": [10.6918, -61.2225],
    "US": [39.8283, -98.5795],
    "UY": [-32.5228, -55.7658],
    "VC": [12.9843, -61.2872],
    "VE": [6.4238, -66.5897],
    "VG": [18.4207, -64.64],
    "VI": [18.3358, -64.8963],
}

STATE_COORDS = {
    "AL": [32.8067, -86.7911],
    "AK": [61.3707, -152.4044],
    "AZ": [33.7298, -111.4312],
    "AR": [34.9697, -92.3731],
    "CA": [36.1162, -119.6816],
    "CO": [39.0598, -105.3111],
    "CT": [41.5978, -72.7554],
    "DE": [39.3185, -75.5071],
    "DC": [38.9072, -77.0369],
    "FL": [27.7663, -81.6868],
    "GA": [33.0406, -83.6431],
    "HI": [21.0943, -157.4983],
    "ID": [44.2405, -114.4788],
    "IL": [40.3495, -88.9861],
    "IN": [39.8494, -86.2583],
    "IA": [42.0115, -93.2105],
    "KS": [38.5266, -96.7265],
    "KY": [37.6681, -84.6701],
    "LA": [31.1695, -91.8678],
    "ME": [44.6939, -69.3819],
    "MD": [39.0639, -76.8021],
    "MA": [42.2302, -71.5301],
    "MI": [43.3266, -84.5361],
    "MN": [45.6945, -93.9002],
    "MS": [32.7416, -89.6787],
    "MO": [38.4561, -92.2884],
    "MT": [46.9219, -110.4544],
    "NE": [41.1254, -98.2681],
    "NV": [38.3135, -117.0554],
    "NH": [43.4525, -71.5639],
    "NJ": [40.2989, -74.521],
    "NM": [34.8405, -106.2485],
    "NY": [42.1657, -74.9481],
    "NC": [35.6301, -79.8064],
    "ND": [47.5289, -99.784],
    "OH": [40.3888, -82.7649],
    "OK": [35.5653, -96.9289],
    "OR": [44.572, -122.0709],
    "PA": [40.5908, -77.2098],
    "PR": [18.2208, -66.5901],
    "RI": [41.6809, -71.5118],
    "SC": [33.8569, -80.945],
    "SD": [44.2998, -99.4388],
    "TN": [35.7478, -86.6923],
    "TX": [31.0545, -97.5635],
    "UT": [40.15, -111.8624],
    "VT": [44.0459, -72.7107],
    "VA": [37.7693, -78.17],
    "WA": [47.4009, -121.4905],
    "WV": [38.4912, -80.9545],
    "WI": [44.2685, -89.6165],
    "WY": [42.756, -107.3025],
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


_SUBNATIONAL_COORDS: dict[tuple[str, str], list[float]] | None = None
_COUNTRY_COORDS_DERIVED: dict[str, list[float]] | None = None


def country_coord(code: str) -> list[float | None]:
    code = (code or "").strip().upper()
    if code in COUNTRY_COORDS:
        return COUNTRY_COORDS[code]
    # Derive missing country markers from the mean of their coord-results entries.
    # This keeps the fallback data-driven instead of hardcoding every country.
    return load_subnational_coords().get((code, "__country_centroid__"), [None, None])


def load_subnational_coords() -> dict[tuple[str, str], list[float]]:
    """Load world subnational coords from coord-results/*.jsonl (daemon-generated)."""
    global _SUBNATIONAL_COORDS, _COUNTRY_COORDS_DERIVED
    if _SUBNATIONAL_COORDS is not None:
        return _SUBNATIONAL_COORDS
    coords: dict[tuple[str, str], list[float]] = {}
    country_totals: dict[str, list[float]] = {}
    if COORD_RESULTS_DIR.exists():
        for path in sorted(COORD_RESULTS_DIR.glob("batch-*.jsonl")):
            try:
                with path.open(encoding="utf-8") as handle:
                    for line in handle:
                        line = line.strip()
                        if not line:
                            continue
                        item = json.loads(line)
                        lat = item.get("lat")
                        lng = item.get("lng")
                        if lat is None or lng is None:
                            continue
                        try:
                            lat_float = float(lat)
                            lng_float = float(lng)
                        except (TypeError, ValueError):
                            continue
                        code = (item.get("country_code") or "").strip().upper()
                        division = (item.get("division") or "").strip()
                        coord = [lat_float, lng_float]
                        coords[(code, division)] = coord
                        # A province-only DB label (e.g. Xinjiang) can use the
                        # first matching "Province - City" coordinate.
                        prefix = division.split(" - ", 1)[0].strip()
                        if prefix and prefix != division:
                            coords.setdefault((code, prefix), coord)
                        if code:
                            total = country_totals.setdefault(code, [0.0, 0.0, 0.0])
                            total[0] += lat_float
                            total[1] += lng_float
                            total[2] += 1
            except Exception:
                continue
    _COUNTRY_COORDS_DERIVED = {
        code: [total[0] / total[2], total[1] / total[2]]
        for code, total in country_totals.items()
        if total[2]
    }
    # Keep derived centroids in the same lookup cache, without affecting the
    # exact/secondary subnational keys or counting a centroid as a data record.
    for code, coord in _COUNTRY_COORDS_DERIVED.items():
        coords[(code, "__country_centroid__")] = coord
    _SUBNATIONAL_COORDS = coords
    return coords


DC_META_DIR = ROOT / "astro" / "public" / "dc"
CENTERS_OUT_PATH = ROOT / "astro" / "public" / "data" / "centers.json"
_DC_METADATA: dict[str, dict] | None = None


def load_dc_metadata() -> dict[str, dict]:
    """Load slug -> metadata map from dc/<slug>/data.json (DC detail pages)."""
    global _DC_METADATA
    if _DC_METADATA is not None:
        return _DC_METADATA
    meta: dict[str, dict] = {}
    dc_root = ROOT / "dc"
    if dc_root.exists():
        for d in sorted(dc_root.iterdir()):
            p = d / "data.json"
            if p.exists():
                try:
                    j = json.loads(p.read_text(encoding="utf-8"))
                    slug = j.get("slug") or d.name
                    meta[slug] = j
                except Exception:
                    continue
    _DC_METADATA = meta
    return meta


def write_dc_metadata(meta: dict[str, dict]) -> int:
    """Emit per-slug files fetched lazily by the DC detail modal (plan §6.1)."""
    DC_META_DIR.mkdir(parents=True, exist_ok=True)
    written = 0
    for slug, item in meta.items():
        if not re.fullmatch(r"[A-Za-z0-9._-]+", slug):
            continue
        (DC_META_DIR / f"{slug}.json").write_text(
            json.dumps(item, ensure_ascii=False, separators=(",", ":")), encoding="utf-8"
        )
        written += 1
    return written


def slugify(name: str) -> str:
    s = unicodedata.normalize("NFKD", name or "").encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return re.sub(r"-{2,}", "-", s)[:80] or "unnamed"


def subnational_coord(country: str, name: str) -> list[float | None]:
    code = (country or "").strip().upper()
    normalized_name = (name or "").strip()
    if code == "US":
        abbr = state_abbr(normalized_name)
        if abbr and abbr in STATE_COORDS:
            return STATE_COORDS[abbr]
    coord = load_subnational_coords().get((code, normalized_name))
    if coord:
        return coord
    return country_coord(code)


COUNTY_SUFFIXES = (
    " city and borough",
    " census area",
    " municipality",
    " borough",
    " county",
    " parish",
    " municipio",
)


def normalize_county_name(value: str | None) -> str:
    text = unicodedata.normalize("NFKD", value or "").encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^a-zA-Z0-9]+", " ", text).strip().lower()
    for suffix in COUNTY_SUFFIXES:
        if text.endswith(suffix):
            text = text[: -len(suffix)].strip()
            break
    return text


def county_lookup_keys(county: str, abbr: str) -> list[tuple[str, str]]:
    normalized = normalize_county_name(county)
    keys = [(abbr, normalized)]
    for part in re.split(r"[/;,&]+", county):
        part_key = normalize_county_name(part)
        if part_key and (abbr, part_key) not in keys:
            keys.append((abbr, part_key))
    return keys


def load_county_coords() -> dict[tuple[str, str], dict[str, float | str]]:
    if not COUNTY_COORDS_PATH.exists():
        return {}
    coords = {}
    for item in json.loads(COUNTY_COORDS_PATH.read_text(encoding="utf-8")):
        abbr = state_abbr(item.get("state"))
        county = clean_text(item.get("county"), "")
        if not abbr or not county:
            continue
        coords[(abbr, normalize_county_name(county))] = {
            "county": county,
            "state": abbr,
            "lat": float(item["lat"]),
            "lng": float(item["lng"]),
        }
    return coords


def county_coord(county_coords: dict[tuple[str, str], dict[str, float | str]], county: str, abbr: str) -> list[float | None]:
    for key in county_lookup_keys(county, abbr):
        item = county_coords.get(key)
        if item:
            return [float(item["lat"]), float(item["lng"])]
    return STATE_COORDS.get(abbr, [None, None])


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


def empty_years() -> dict[int, dict[str, int | float]]:
    return {
        year: {
            "pipeline": 0,
            "construction": 0,
            "operational": 0,
            "pipeline_mw": 0.0,
            "construction_mw": 0.0,
            "operational_mw": 0.0,
        }
        for year in range(2018, 2031)
    }


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


def add_year_signal(years: dict[int, dict[str, int | float]], year: int | None, key: str, mw: float = 0.0) -> None:
    if year in years:
        if key == "op":
            years[year]["operational"] += 1
            years[year]["operational_mw"] += mw
        elif key == "con":
            years[year]["construction"] += 1
            years[year]["construction_mw"] += mw
        elif key in {"ann", "pla", "app"}:
            years[year]["pipeline"] += 1
            years[year]["pipeline_mw"] += mw


def main() -> None:
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    rows = con.execute("select * from centers").fetchall()
    columns = set(rows[0].keys()) if rows else set()
    americas = load_americas()
    county_coords = load_county_coords()
    dc_meta = load_dc_metadata()

    total_mw = sum(float(r["capacity_mw"] or 0) for r in rows)
    source_count = con.execute("select count(url) from sources where url is not null and trim(url) != ''").fetchone()[0]
    state_acc: dict[str, dict[str, float | int]] = defaultdict(lambda: {"facilities": 0, "capacity_mw": 0.0})
    county_acc: dict[tuple[str, str], dict[str, float | int | str]] = defaultdict(
        lambda: {"county": "", "state_abbr": "", "facilities": 0, "capacity_mw": 0.0}
    )
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
        tracked_mw = mw
        est_mw = 0.0
        # Country-mean fill (Jason 3560-3566, 3622-3624): every country's missing
        # capacity is filled with that country's known-capacity mean, and the
        # tracked/est split is exposed in the UI.
        if mw <= 0 and columns.intersection({"capacity_mw_est_mean"}):
            mw = float(r["capacity_mw_est_mean"] or 0)
            tracked_mw = 0.0
            est_mw = mw
        key = status_key(r["status"])
        year = r["year"] if isinstance(r["year"], int) else None
        owner = clean_text(r["owner"], "Unknown operator")
        subnational_label = subnational or (STATE_NAMES.get(abbr) if abbr else clean_text(r["state"], "Unknown"))

        country_acc[code]["facilities"] += 1
        country_acc[code]["capacity_mw"] += mw
        country_acc[code]["tracked_mw"] = country_acc[code].get("tracked_mw", 0.0) + tracked_mw
        country_acc[code]["est_mw"] = country_acc[code].get("est_mw", 0.0) + est_mw
        country_acc[code]["funnel"][key]["count"] += 1
        country_acc[code]["funnel"][key]["capacity_mw"] += mw
        add_year_signal(country_acc[code]["years"], year, key, mw)
        if subnational_label != "Unknown":
            country_acc[code]["subnationals"][subnational_label]["facilities"] += 1
            country_acc[code]["subnationals"][subnational_label]["capacity_mw"] += mw

        if code == "US" and abbr in STATE_LAYOUT:
            state_acc[abbr]["facilities"] += 1
            state_acc[abbr]["capacity_mw"] += mw
        county = clean_text(r["county"], "Unknown")
        if code == "US" and abbr and county != "Unknown":
            county_keys.add((county.lower(), abbr))
            county_key = (abbr, county.strip().lower())
            county_acc[county_key]["county"] = county
            county_acc[county_key]["state_abbr"] = abbr
            county_acc[county_key]["facilities"] += 1
            county_acc[county_key]["capacity_mw"] += mw
        status_acc[key]["count"] += 1
        status_acc[key]["capacity_mw"] += mw
        dev_acc[owner]["facilities"] += 1
        dev_acc[owner]["capacity_mw"] += mw
        evidence_acc[evidence_bucket(r["evidence_grade"])] += 1

        add_year_signal(years, year, key, mw)

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
                    "slug": (r["existing_slug"] if isinstance(r["existing_slug"], str) and r["existing_slug"] else None),
                    "est": bool(mw > 0 and not (r["capacity_mw"] and r["capacity_mw"] > 0)),
                }
            )
            # Method rows have no existing_slug in DB; attach dc/<slug>/data.json
            # via the same slug convention merge_method.py uses (best effort).
            if centers[-1]["slug"] is None:
                cand = f"method-{code.lower()}-{slugify(centers[-1]['project'])}"
                if cand in dc_meta:
                    centers[-1]["slug"] = cand

    states = []
    for abbr, pos in STATE_LAYOUT.items():
        acc = state_acc[abbr]
        lat, lng = STATE_COORDS.get(abbr, [None, None])
        states.append(
            {
                "abbr": abbr,
                "row": pos[0],
                "col": pos[1],
                "facilities": int(acc["facilities"]),
                "capacity_mw": round(float(acc["capacity_mw"]), 1),
                "name_en": STATE_NAMES[abbr],
                "name_zh": ZH_NAMES[abbr],
                "lat": lat,
                "lng": lng,
            }
        )

    counties = []
    for (_abbr, _county_key), acc in county_acc.items():
        abbr = str(acc["state_abbr"])
        county = str(acc["county"])
        lat, lng = county_coord(county_coords, county, abbr)
        counties.append(
            {
                "county": county,
                "state": STATE_NAMES.get(abbr, abbr),
                "state_abbr": abbr,
                "facilities": int(acc["facilities"]),
                "capacity_mw": round(float(acc["capacity_mw"]), 1),
                "lat": lat,
                "lng": lng,
            }
        )
    counties.sort(key=lambda item: (item["capacity_mw"], item["facilities"], item["state_abbr"], item["county"]), reverse=True)

    countries = []
    for code, acc in country_acc.items():
        name_en = americas.get(code, code)
        subnationals = sorted(
            (
                {
                    "name": name,
                    "facilities": int(sub["facilities"]),
                    "capacity_mw": round(float(sub["capacity_mw"]), 1),
                    "lat": subnational_coord(code, name)[0],
                    "lng": subnational_coord(code, name)[1],
                }
                for name, sub in acc["subnationals"].items()
            ),
            key=lambda item: (item["capacity_mw"], item["facilities"]),
            reverse=True,
        )
        lat, lng = country_coord(code)
        countries.append(
            {
                "code": code,
                "name_en": name_en,
                "name_zh": COUNTRY_ZH_NAMES.get(code, name_en),
                "facilities": int(acc["facilities"]),
                "capacity_mw": round(float(acc["capacity_mw"]), 1),
                "capacity_gw": round(float(acc["capacity_mw"]) / 1000, 1),
                "tracked_mw": round(float(acc.get("tracked_mw", 0.0)), 1),
                "tracked_gw": round(float(acc.get("tracked_mw", 0.0)) / 1000, 1),
                "est_mw": round(float(acc.get("est_mw", 0.0)), 1),
                "est_gw": round(float(acc.get("est_mw", 0.0)) / 1000, 1),
                "lat": lat,
                "lng": lng,
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
            # Mechanical consistency (Jason 3672/3674): world totals are the
            # exact sum of the rounded per-country stats (tracked + est
            # mean-fill), never an independent DB-only number.
            "capacity_mw": round(sum(c["capacity_mw"] for c in countries), 1),
            "capacity_gw": round(sum(c["capacity_mw"] for c in countries) / 1000, 1),
            "tracked_mw": round(sum(c["tracked_mw"] for c in countries), 1),
            "est_mw": round(sum(c["est_mw"] for c in countries), 1),
            "tracked_gw": round(sum(c["tracked_mw"] for c in countries) / 1000, 1),
            "est_gw": round(sum(c["est_mw"] for c in countries) / 1000, 1),
            "facilities": len(rows),
            "sources": int(source_count),
            "counties_with_projects": len(counties),
            "counties_explored": COUNTIES_EXPLORED,
            "countries_with_projects": len(country_acc),
            "countries_explored": len(americas),
            "registry_rows": len(centers),
        },
        "countries": countries,
        "states": states,
        "funnel": funnel,
        "years": wave,
        "developers": developers,
        "evidence": evidence,
        "flagship": flagship,
        "status_labels": STATUS_LABELS,
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"wrote {OUT_PATH} ({OUT_PATH.stat().st_size:,} bytes)")

    # Payload split (plan §6.2): centers + counties are fetched after first
    # paint from public/data/centers.json instead of riding in the inline HTML.
    deferred = {"centers": centers, "counties": counties}
    CENTERS_OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    CENTERS_OUT_PATH.write_text(json.dumps(deferred, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"wrote {CENTERS_OUT_PATH} ({CENTERS_OUT_PATH.stat().st_size:,} bytes)")

    # DC detail metadata (Jason 3596): emit only slugs referenced by centers.
    used_slugs = {c.get("slug") for c in centers if c.get("slug")}
    dc_meta_out = {s: dc_meta[s] for s in used_slugs if s in dc_meta}
    n_files = write_dc_metadata(dc_meta_out)
    print(f"wrote {DC_META_DIR}/<slug>.json ({n_files} files)")


if __name__ == "__main__":
    main()
