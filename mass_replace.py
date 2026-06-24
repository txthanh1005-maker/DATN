import os
import re

files_to_edit = [
    "DATN.tex",
    "chapters/chapter1.tex",
    "chapters/chapter2.tex",
    "chapters/chapter3.tex",
    "chapters/chapter4.tex",
    "chapters/chapter5.tex"
]

replacements = {
    # Spatiotemporal first
    r"\bSpatiotemporal\b": "Distributed Dynamic",
    r"\bspatiotemporal\b": "distributed dynamic",
    
    # Specific Spatial
    r"\bSpatial coordination\b": "Distributed coordination",
    r"\bspatial coordination\b": "distributed coordination",
    r"\bSpatial Coordination\b": "Distributed Coordination",
    r"\bSpatial Coord\.\b": "Dist. Coord.",
    r"\bspatial scalability\b": "network scalability",
    r"\bspatial node\b": "network node",
    r"\bspatial deviation\b": "inter-node deviation",
    r"\bspatial discrepancy\b": "inter-node discrepancy",
    r"\bspatial mismatch\b": "inter-node mismatch",
    r"\bspatial coupling\b": "network coupling",
    r"\bSpatial ATC\b": "Distributed ATC",
    r"\bSpatial and Temporal Control\b": "Distributed and Dynamic Control",
    r"\bspatial or temporal coordination\b": "distributed or dynamic coordination",
    r"\bspatial power distribution\b": "network power distribution",
    r"\bspatial power flow\b": "network power flow",
    r"\bspatial penalty\b": "network penalty",
    r"\bspatially shifted\b": "topologically shifted",
    r"\bspatial P2P\b": "network-wide P2P",
    r"\bspatial advantage\b": "topological advantage",
    r"\bspatial analysis\b": "network analysis",
    r"\bSpatial Depth\b": "Network Depth",
    r"\bspatial depth\b": "network depth",
    r"\bspatial and temporal stress\b": "network and dynamic stress",
    r"\bspatial power transfers\b": "tie-line power transfers",
    r"\bspatially---transforming\b": "topologically---transforming",
    r"Spatial / Market": "Distributed / Market",
    
    # Specific Temporal
    r"\btemporal dynamic scheduling\b": "real-time dynamic scheduling",
    r"\bTemporal Dynamics\b": "Real-time Dynamics",
    r"\btemporal dynamics\b": "real-time dynamics",
    r"\bmulti-temporal\b": "multi-period",
    r"\bStatic Temporal Rigidity\b": "Static Operational Rigidity",
    r"\btemporal foresight\b": "multi-period foresight",
    r"\btemporal dimensions\b": "dynamic dimensions",
    r"\btemporal resilience\b": "dynamic resilience",
    r"\bTemporal Resil\.\b": "Dynamic Resil.",
    r"\binter-temporal\b": "multi-period",
    r"\bTemporal Coordination\b": "Dynamic Coordination",
    r"\btemporal Coordination\b": "dynamic coordination",
    r"\btemporal framework\b": "dynamic framework",
    r"\btemporal coordinator\b": "dynamic coordinator",
    r"\btemporal coupling\b": "multi-period coupling",
    r"\btemporal stage\b": "operational stage",
    r"\btemporal safeguard\b": "multi-period safeguard",
    r"\btemporal energy shifting\b": "multi-period energy shifting",
    r"\btemporal limitation\b": "myopic limitation",
    r"\btemporal correlation\b": "multi-period correlation",
    r"\btemporal stress\b": "duration-based stress",
    r"\bTemporal Depth\b": "Prolonged Depth",
    r"\btemporal depth\b": "prolonged depth",
    r"\btemporal divergence\b": "operational divergence",
    r"\bTemporal distribution\b": "Time-series distribution",
    
    # Fallbacks (Must be done LAST)
    r"\bSpatial\b": "Distributed",
    r"\bspatial\b": "distributed",
    r"\bSpatially\b": "Topologically",
    r"\bspatially\b": "topologically",
    r"\bTemporal\b": "Dynamic",
    r"\btemporal\b": "dynamic",
}

def replace_in_file(filepath):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for pattern, replacement in replacements.items():
        content = re.sub(pattern, replacement, content)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Processed {filepath}")

base_path = r"D:\Latex\DATN"
for filename in files_to_edit:
    filepath = os.path.join(base_path, filename)
    replace_in_file(filepath)

print("Mass replacement completed successfully.")
