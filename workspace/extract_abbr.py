import re
import os

abbr_dict = {
    'ATC': 'Analytical Target Cascading',
    'MPC': 'Model Predictive Control',
    'OPF': 'Optimal Power Flow',
    'AC-OPF': 'Alternating Current Optimal Power Flow',
    'SOCP': 'Second-Order Cone Programming',
    'KKT': 'Karush-Kuhn-Tucker',
    'HILP': 'High-Impact Low-Probability',
    'MG': 'Microgrid',
    'P2P': 'Peer-to-Peer',
    'PV': 'Photovoltaic',
    'WT': 'Wind Turbine',
    'BESS': 'Battery Energy Storage System',
    'DG': 'Diesel Generator',
    'SOC': 'State of Charge',
    'ESS': 'Energy Storage System',
    'RES': 'Renewable Energy Sources',
    'VOLL': 'Value of Lost Load',
    'FIT': 'Feed-in Tariffs',
    'ADMM': 'Alternating Direction Method of Multipliers',
    'PCC': 'Point of Common Coupling',
    'MINLP': 'Mixed-Integer Non-Linear Programming',
    'MILP': 'Mixed-Integer Linear Programming',
    'NLP': 'Non-Linear Programming',
    'DER': 'Distributed Energy Resource',
    'LMP': 'Locational Marginal Pricing',
    'DLMP': 'Distribution Locational Marginal Pricing'
}

files_to_check = ['DATN.tex'] + [f'chapters/chapter{i}.tex' for i in range(1, 6)]
replacements = []
new_abbrs = {}

# Regex to find `Something Something (ABBR)` or `Something Something (ABBRs)`
pattern = re.compile(r'\b([A-Za-z][A-Za-z0-9\-\s]{3,})\s*\(([A-Z0-9\-]{2,}s?)\)')

for file in files_to_check:
    filepath = os.path.join(r'D:\Latex\DATN', file)
    if not os.path.exists(filepath):
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    def repl(match):
        full_word = match.group(1).strip()
        abbr = match.group(2).strip()
        base_abbr = abbr[:-1] if abbr.endswith('s') else abbr
        
        # Check if words form the acronym
        words = [w for w in full_word.replace('-', ' ').split() if len(w) > 0]
        letters = ''.join([w[0].upper() for w in words])
        
        is_match = False
        if base_abbr in abbr_dict:
            is_match = True
        elif base_abbr in letters or letters in base_abbr:
            is_match = True
        
        # Filter out common false positives like "Section (IV)" or "(Eq)"
        if is_match and len(base_abbr) >= 2 and base_abbr not in ['II', 'III', 'IV', 'VI', 'VII']:
            if base_abbr not in abbr_dict:
                new_abbrs[base_abbr] = full_word
            replacements.append((file, full_word, abbr))
            return abbr
        
        return match.group(0)

    new_content = pattern.sub(repl, content)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("--- SUMMARY ---")
print(f"Total replacements: {len(replacements)}")
for r in replacements:
    print(f"[{r[0]}] '{r[1]}' -> {r[2]}")
    
print("\n--- NEW ABBREVIATIONS ---")
for k, v in new_abbrs.items():
    print(f"{k}: {v}")
