import re
import urllib.parse
import subprocess
import json
import time

TEX_PATH = r"D:\Latex\DATN\chapters\chapter1.tex"
BIB_PATH = r"D:\Latex\DATN\references.bib"
REPORT_PATH = r"D:\Latex\DATN\workspace\Final_Citation_Audit_Report.md"

def fetch_openalex(doi, title):
    if doi:
        doi_clean = re.sub(r'^https?://(dx\.)?doi\.org/', '', doi)
        url = f"https://api.openalex.org/works/https://doi.org/{doi_clean}"
        res = subprocess.run(["curl.exe", "-s", url], capture_output=True, text=True)
        if res.returncode == 0:
            try:
                data = json.loads(res.stdout)
                if 'title' in data:
                    return data
            except:
                pass
    if title:
        enc_title = urllib.parse.quote(title)
        url = f"https://api.openalex.org/works?filter=title.search:{enc_title}"
        res = subprocess.run(["curl.exe", "-s", url], capture_output=True, text=True)
        if res.returncode == 0:
            try:
                data = json.loads(res.stdout)
                if data and data.get("results"):
                    return data["results"][0]
            except:
                pass
    return None

def parse_bib():
    with open(BIB_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    entries = {}
    current_key = None
    current_entry = {}
    
    for line in content.split('\n'):
        line = line.strip()
        if line.startswith('@'):
            if current_key:
                entries[current_key] = current_entry
            match = re.search(r'@\w+\{([^,]+),', line)
            if match:
                current_key = match.group(1).strip()
                current_entry = {}
        elif current_key and '=' in line:
            parts = line.split('=', 1)
            key = parts[0].strip().lower()
            val = parts[1].strip()
            val = re.sub(r'^[\{"]', '', val)
            val = re.sub(r'[\}",]+$', '', val)
            current_entry[key] = val
            
    if current_key:
        entries[current_key] = current_entry
        
    return entries

def extract_cites():
    with open(TEX_PATH, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # split into sentences roughly
    sentences = re.split(r'(?<=[.!?])\s+', content)
    
    cites = {}
    for sentence in sentences:
        matches = re.findall(r'\\cite\{([^}]+)\}', sentence)
        for match in matches:
            keys = [k.strip() for k in match.split(',')]
            for k in keys:
                if k not in cites:
                    cites[k] = []
                # Keep surrounding text
                clean_sent = re.sub(r'\s+', ' ', sentence).strip()
                cites[k].append(clean_sent)
    return cites

def get_stop_words():
    return {"and", "of", "the", "in", "for", "a", "to", "on", "with", "based", "is", "by", "an", "this", "that", "it"}

def check_linkage(context, title):
    if not title: return "No title to check"
    
    title_words = set(re.findall(r'\w+', title.lower())) - get_stop_words()
    context_words = set(re.findall(r'\w+', context.lower())) - get_stop_words()
    
    overlap = title_words.intersection(context_words)
    if len(overlap) >= 1:
        return "PASS"
    return f"WARNING (low overlap). Title: {title}"

def main():
    print("Extracting citations...")
    cites = extract_cites()
    print("Parsing bib...")
    bib_entries = parse_bib()
    
    results = []
    
    print(f"Found {len(cites)} unique citations.")
    
    for i, (key, contexts) in enumerate(cites.items()):
        print(f"[{i+1}/{len(cites)}] Checking {key}")
        entry = bib_entries.get(key, {})
        bib_title = entry.get('title', '')
        bib_doi = entry.get('doi', '')
        bib_year = entry.get('year', 'Unknown')
        
        oa_data = fetch_openalex(bib_doi, bib_title)
        
        status = "REAL"
        oa_year = bib_year
        oa_title = bib_title
        
        if not entry:
            status = "MISSING_IN_BIB"
        elif not oa_data:
            status = "HALLUCINATION / NOT_FOUND"
        else:
            oa_title = oa_data.get('title', bib_title)
            oa_year = oa_data.get('publication_year', bib_year)
            if str(bib_year) != str(oa_year) and bib_year != 'Unknown':
                status = f"YEAR_MISMATCH (Bib: {bib_year}, OA: {oa_year})"
                
        ctx = contexts[0] if contexts else "No context found"
        linkage = check_linkage(ctx, oa_title) if oa_data else "N/A"
        
        results.append({
            "key": key,
            "year": int(oa_year) if str(oa_year).isdigit() else 0,
            "display_year": oa_year,
            "title": oa_title or bib_title,
            "status": status,
            "linkage": linkage,
            "context": ctx
        })
        time.sleep(0.05)
        
    results.sort(key=lambda x: x['year'], reverse=True)
    
    from collections import defaultdict
    grouped = defaultdict(list)
    for r in results:
        year_cat = str(r['display_year'])
        if r['year'] < 2020 and r['year'] > 0:
            year_cat = "Before 2020"
        elif r['year'] == 0:
            year_cat = "Unknown/Missing"
        grouped[year_cat].append(r)
        
    print("Writing report...")
    with open(REPORT_PATH, 'w', encoding='utf-8') as f:
        f.write("# Báo Cáo Kiểm Toán Trích Dẫn Độc Lập (Chương 1)\n\n")
        f.write("Báo cáo này liệt kê và đối chiếu tất cả các trích dẫn có trong `chapter1.tex` so với `references.bib` và cơ sở dữ liệu học thuật OpenAlex. Báo cáo được sắp xếp theo trình tự thời gian.\n\n")
        
        passed = sum(1 for r in results if r['status'] == 'REAL' and r['linkage'] == 'PASS')
        errors = sum(1 for r in results if r['status'] != 'REAL' or r['linkage'] != 'PASS')
        
        f.write(f"**Tổng số trích dẫn:** {len(results)}\n")
        f.write(f"**PASS (Hợp lệ & Linkage tốt):** {passed}\n")
        f.write(f"**CÓ LỖI/CẢNH BÁO:** {errors}\n\n")
        
        def year_sort_key(y):
            if str(y).isdigit(): return int(y)
            if y == "Before 2020": return 2019
            return 0
            
        cats = sorted(grouped.keys(), key=year_sort_key, reverse=True)
        
        for cat in cats:
            f.write(f"## Năm: {cat}\n\n")
            for r in grouped[cat]:
                status_icon = "✅" if r['status'] == "REAL" else "❌"
                linkage_icon = "🔗" if r['linkage'] == "PASS" else "⚠️"
                
                f.write(f"### `[{r['key']}]` {r['title']}\n")
                f.write(f"- **Tình trạng tồn tại (OpenAlex):** {status_icon} {r['status']}\n")
                f.write(f"- **Kiểm tra Linkage:** {linkage_icon} {r['linkage']}\n")
                f.write(f"- **Câu văn chứa trích dẫn:** > {r['context']}\n\n")
                
if __name__ == '__main__':
    main()
