import subprocess
import json
import urllib.parse

dois = [
    # SOCP, ADMM, ATC
    "10.1109/access.2024.3382940",
    "10.1016/j.ijepes.2021.107126",
    "10.1016/j.ijepes.2022.108572",
    "10.1016/j.apenergy.2020.115336",
    "10.1109/tii.2024.3478274",
    "10.1007/s10589-022-00433-4",
    "10.1109/epee59859.2023.10351909",
    "10.3389/fenrg.2024.1438961",
    
    # Robust Optimization, Resilient, MPC, DRO
    "10.1155/2020/4215906",
    "10.1109/TSG.2019.2947935",
    "10.1016/j.ijepes.2019.105483",
    "10.1109/cac59555.2023.10451685",
    "10.1109/TPWRS.2021.3060595",
    "10.1109/TSG.2019.2933458",
    "10.1109/tsg.2020.3010570",
    "10.1109/access.2020.2968586",
    
    # Further Robust/DRO
    "10.1109/tcst.2022.3208456",
    "10.1109/tase.2024.3485922",
    "10.1016/j.est.2025.118148",
]

def fetch_json(url):
    res = subprocess.run(["curl.exe", "-s", url], capture_output=True, text=True)
    if res.returncode == 0:
        return json.loads(res.stdout)
    return None

for doi in dois:
    url = f"https://api.openalex.org/works/https://doi.org/{doi}"
    try:
        data = fetch_json(url)
        if data and 'title' in data:
            print(f"VALID: {doi} -> {data.get('title')} ({data.get('publication_year')})")
        else:
            print(f"NOT FOUND/ERROR: {doi}")
    except Exception as e:
        print(f"ERROR: {doi} -> {e}")

titles = [
    "Data-driven distributionally robust optimization for microgrid energy management",
    "Resilience-oriented optimal operation of networked microgrids under extreme weather events",
    "Adaptive robust energy management of microgrids considering uncertainties in renewable energy and load demand",
    "Tractable two-stage robust optimal operation of microgrids with high renewable penetration",
    "Distributionally robust scheduling of microgrids with flexible loads"
]

for title in titles:
    query = urllib.parse.quote(title)
    url = f"https://api.openalex.org/works?search={query}"
    try:
        data = fetch_json(url)
        if data and data.get("results"):
            top = data["results"][0]
            print(f"VALID TITLE: {title} -> Found: {top.get('title')} ({top.get('publication_year')})")
        else:
            print(f"ERROR TITLE: {title} -> Not found")
    except Exception as e:
        print(f"ERROR TITLE: {title} -> {e}")
