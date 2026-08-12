# -*- coding: utf-8 -*-
import json

rows = [
    {
        "name": "平潭两岸融合智算中心",
        "province": "福建",
        "city/subnational": "平潭综合实验区",
        "status": "在建（2024-09开工，2025-02省发改委现场调研，2026-03已建成2300P算力规模）",
        "capacity_mw": 115,
        "developer": "平潭城发集团旗下产投公司联合软通动力等企业共建",
        "source_urls": [
            "https://fgw.fujian.gov.cn/zwgk/xwdt/bwdt/202502/t20250218_6765496.htm",
            "https://fjrb.fjdaily.com/pc/con/202603/29/content_522261.html",
            "http://m.hxnews.com/news/fj/pingtan/202504/29/2199837.shtml"
        ],
        "evidence_date": "2026-03-29",
        "evidence_grade": "A",
        "notes": "2300 PFLOPS按0.05MW/PFLOPS折算约115MW（父级启发式）。省数字经济重点方向，定位全省算力网络重要支点；省发改委2025年一季度调研实地走访该项目。"
    },
    {
        "name": "嘉庚智算中心（嘉庚创新实验室智能计算中心）",
        "province": "福建",
        "city/subnational": "厦门市（临空经济片区九溪路与洞庭路交叉口东北侧）",
        "status": "运营中（2022年成立，AI4EC Lab运营）",
        "capacity_mw": None,
        "developer": "厦门大学、嘉庚创新实验室（福建能源材料科学与技术创新实验室）、北京科学智能研究院（AI4EC Lab）、火炬集团",
        "source_urls": [
            "https://www.stats.gov.cn/zs/tjwh/tjkw/tjqk/zgxxb/202606/P020260611325529440387.pdf",
            "https://fjrb.fjdaily.com/pc/con/202606/28/content_545568.html",
            "https://fj.sina.cn/news/2026-02-02/detail-inhkkzkk8122292.d.html"
        ],
        "evidence_date": "2026-06-28",
        "evidence_grade": "B",
        "notes": "科研型AI智算中心，采用冷板式液冷/风液协同散热，PUE显著改善；省市重点项目；规模未披露（科研平台）。"
    },
    {
        "name": "莆田异星智能智算中心项目",
        "province": "福建",
        "city/subnational": "莆田市",
        "status": "已列入2026年度省数字经济重点项目（闽数据〔2026〕9号）",
        "capacity_mw": None,
        "developer": "异星智能（公司主体待核实）",
        "source_urls": [
            "https://fgw.fujian.gov.cn/ztzl/szfjzt/tzgg/202603/t20260318_7113138.htm"
        ],
        "evidence_date": "2026-03-18",
        "evidence_grade": "A",
        "notes": "名单第62项（数字要素驱动业）；省数字经济重点项目133个/总投资1299亿元之一；容量数据未在公示中披露，需查莆田市发改委备案。"
    },
    {
        "name": "脉易智算人工智能先进计算中心项目",
        "province": "福建",
        "city/subnational": "福建（名单中紧随莆田异星项目，城市待核实）",
        "status": "已列入2026年度省数字经济重点项目（闽数据〔2026〕9号）",
        "capacity_mw": None,
        "developer": "脉易智算（公司主体待核实）",
        "source_urls": [
            "https://fgw.fujian.gov.cn/ztzl/szfjzt/tzgg/202603/t20260318_7113138.htm"
        ],
        "evidence_date": "2026-03-18",
        "evidence_grade": "A",
        "notes": "名单第63项（数字要素驱动业）；容量数据未披露。"
    },
    {
        "name": "宁德时代21C创新实验室超算中心",
        "province": "福建",
        "city/subnational": "宁德市",
        "status": "已列入2026年度省数字经济重点项目（闽数据〔2026〕9号）",
        "capacity_mw": None,
        "developer": "宁德时代（CATL）",
        "source_urls": [
            "https://fgw.fujian.gov.cn/ztzl/szfjzt/tzgg/202603/t20260318_7113138.htm"
        ],
        "evidence_date": "2026-03-18",
        "evidence_grade": "A",
        "notes": "名单第65项（数字要素驱动业）；企业级超算中心，容量未披露。"
    },
    {
        "name": "福建省海洋与渔业数据中心项目",
        "province": "福建",
        "city/subnational": "福州市（省级政务设施）",
        "status": "投资概算经省发改委批复（2023-11），按发改环资规〔2017〕1975号不单独进行节能审查",
        "capacity_mw": None,
        "developer": "福建省海洋与渔业局（省海洋与渔业数据中心）",
        "source_urls": [
            "https://fgw.fujian.gov.cn/zfxxgkzl/zfxxgkml/yzdgkdqtxx/202311/t20231120_6302675.htm"
        ],
        "evidence_date": "2023-11-20",
        "evidence_grade": "A",
        "notes": "省级部门数据中心，规模小（政务机房），非商业IDC。"
    },
    {
        "name": "思明智算中心",
        "province": "福建",
        "city/subnational": "厦门市思明区",
        "status": "运营中（2026-03省发改委数据管理局调研走访）",
        "capacity_mw": None,
        "developer": "厦门市思明区相关主体（待核实）",
        "source_urls": [
            "https://fgw.fujian.gov.cn/ztzl/szfjzt/hydt/202603/t20260309_7107355.htm"
        ],
        "evidence_date": "2026-03-09",
        "evidence_grade": "A",
        "notes": "省级行业动态提及（厦门城市大脑、可信数据空间、思明智算中心等调研点）；容量未披露。"
    },
    {
        "name": "紫华光算力赋能项目",
        "province": "福建",
        "city/subnational": "福建（城市待核实）",
        "status": "已列入2026年度省数字经济重点项目（闽数据〔2026〕9号）",
        "capacity_mw": None,
        "developer": "紫华光（公司主体待核实）",
        "source_urls": [
            "https://fgw.fujian.gov.cn/ztzl/szfjzt/tzgg/202603/t20260318_7113138.htm"
        ],
        "evidence_date": "2026-03-18",
        "evidence_grade": "A",
        "notes": "名单第39项（数字技术应用业）；名称指向算力赋能类项目，性质待核实。"
    },
    {
        "name": "数字福建云计算中心（东湖）",
        "province": "福建",
        "city/subnational": "福州市长乐区东湖数字小镇（滨海新城）",
        "status": "已建成运营（2016年前后投用，省经济信息中心运维）",
        "capacity_mw": None,
        "developer": "福建省经济信息中心（数字福建云计算中心）",
        "source_urls": [
            "https://www.vjshi.com/watch/6957918.html"
        ],
        "evidence_date": "2024-01-01",
        "evidence_grade": "C",
        "notes": "福建省政务云核心节点之一；公开检索仅见媒体素材页，未获发改委/环保管线一手文件，容量待核。"
    },
    {
        "coverage": True,
        "province": "福建",
        "searched_sources": [
            "fgw.fujian.gov.cn（节能审查意见/公示公告/省数字经济重点项目名单/行业动态）",
            "sthjt.fujian.gov.cn（环评公示）",
            "dpc.xm.gov.cn（厦门项目备案）",
            "通用web检索（福州/厦门/泉州/莆田数据中心·智算中心·算力中心 备案/环评/节能审查）"
        ],
        "found_projects": 9,
        "notes": "福建省发改委节能审查意见存放于zfxxgkzl/zfxxgkml/yzdgkdqtxx/目录，近一年列表未见大型数据中心节能审查意见；省生态环境厅环评公示中未检索到大型数据中心环评批复；福州/厦门大型运营商数据中心（中国移动/电信/联通）的节能审查与环评批复未能在开放web检索中直接定位，建议后续批次通过福建省投资项目在线审批监管平台及市发改委备案栏目逐项复核；2026年度省数字经济重点项目名单为本批主要来源。"
    }
]

path = "/Users/huangzesen/work/projects/us-dc-intel/scripts/expansion/cn-gov/fujian.jsonl"
with open(path, "w", encoding="utf-8") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
print("written", len(rows))
