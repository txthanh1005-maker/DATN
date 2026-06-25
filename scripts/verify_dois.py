import subprocess
import json

dois = [
    "10.1109/TIA.2025.3619008",
    "10.1016/j.epsr.2025.111629",
    "10.1016/j.ijepes.2025.110523",
    "10.1016/j.epsr.2025.112557"
]

def fetch_json(url):
    res = subprocess.run(["curl.exe", "-s", url], capture_output=True, text=True)
    if res.returncode == 0:
        try:
            return json.loads(res.stdout)
        except:
            return None
    return None

for doi in dois:
    url = f"https://api.openalex.org/works/https://doi.org/{doi}"
    try:
        data = fetch_json(url)
        if data and 'title' in data:
            print(f"VALID: {doi} -> {data.get('title')} ({data.get('publication_year')})")
        else:
            print(f"NOT FOUND: {doi}")
    except Exception as e:
        print(f"ERROR: {doi} -> {e}")
