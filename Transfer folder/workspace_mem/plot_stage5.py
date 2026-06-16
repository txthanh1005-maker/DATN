import json
import os
import matplotlib.pyplot as plt
import numpy as np

def get_total_l(vars_dict):
    """Sum of all l (squared current) across all branches at each time step."""
    series = [0.0] * 24
    l_key = None
    for k in vars_dict.keys():
        if k.lower() in ['l', 'l_ij', 'l_line', 'i_line']:
            l_key = k
            break
    if not l_key:
        return np.array(series)
    
    l_data = vars_dict[l_key]
    if isinstance(l_data, dict):
        for k, v in l_data.items():
            if v is None: continue
            val = float(v)
            t = -1
            if isinstance(k, str) and k.startswith("("):
                parts = k.strip("()").split(",")
                if len(parts) >= 2:
                    try:
                        t = int(parts[-1].strip())
                    except ValueError:
                        pass
            if 0 <= t < 24:
                series[t] += val
    return np.array(series)

def get_series(var_data):
    series = [0.0] * 24
    if isinstance(var_data, dict):
        for k, v in var_data.items():
            if v is None: continue
            val = float(v)
            t = -1
            if isinstance(k, str) and k.startswith("("):
                parts = k.strip("()").split(",")
                if len(parts) >= 2:
                    try:
                        t = int(parts[-1].strip())
                    except ValueError:
                        pass
            if 0 <= t < 24:
                series[t] = val
    return np.array(series)
    
def plot_loss():
    base_path = r"D:\Code\P2P_trading_withQV_MG1234\P2P_trading_withQV_MG1234\Result_data\base_fault\base_fault.json"
    mpc_path = r"D:\Code\P2P_trading_withQV_MG1234\P2P_trading_withQV_MG1234\Result_data\current_method\current_method.json"
    
    base_l = np.zeros(24)
    mpc_l = np.zeros(24)
    
    try:
        with open(base_path, 'r', encoding='utf-8', errors='ignore') as f:
            base_data = json.load(f)
        for mg in ["MG1", "MG2", "MG3", "MG4"]:
            if mg in base_data:
                base_l += get_total_l(base_data[mg].get("Variables", base_data[mg]))
                
        with open(mpc_path, 'r', encoding='utf-8', errors='ignore') as f:
            mpc_data = json.load(f)
        for mg in ["MG1", "MG2", "MG3", "MG4"]:
            if mg in mpc_data:
                mpc_l += get_total_l(mpc_data[mg].get("Variables", mpc_data[mg]))
    except Exception as e:
        print("Error reading json for loss:", e)
        return

    time_steps = list(range(1, 25))
    plt.style.use('seaborn-v0_8-paper')
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
    
    plt.figure(figsize=(10, 6))
    plt.plot(time_steps, base_l, 'k--', linewidth=2, label='Base Fault (Isolated)')
    plt.plot(time_steps, mpc_l, 'r-', linewidth=2.5, marker='o', label='MPC (P2P Enabled)')
    
    plt.axvspan(9, 15, color='gray', alpha=0.3, label='Fault Window (9-15h)')
    plt.xlabel('Time (Hour)', fontsize=14)
    plt.ylabel('Total Squared Current $\sum l_{ij}$ (Proxy for Active Loss)', fontsize=14)
    plt.title('Stage 5: Network Active Power Loss Proxy ($l$) Comparison', fontsize=16, pad=15)
    plt.xticks(time_steps, fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(fontsize=12)
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.tight_layout()
    
    out_dir = r"D:\Code\P2P_trading_withQV_MG1234\P2P_trading_withQV_MG1234\Result_data\report_result\stage_5"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "Stage5_Power_Loss_Comparison.png")
    plt.savefig(out_path, dpi=300)
    plt.close()
    print(f"Saved {out_path}")

def plot_lambda():
    mpc_path = r"D:\Code\P2P_trading_withQV_MG1234\P2P_trading_withQV_MG1234\Result_data\current_method\current_method.json"
    try:
        with open(mpc_path, 'r', encoding='utf-8', errors='ignore') as f:
            data = json.load(f)
    except Exception as e:
        print("Error reading json for lambda:", e)
        return

    mgs = ["1", "2", "3", "4"]
    mg_nodes = {}
    for mg in mgs:
        mg_key = f"MG{mg}"
        if mg_key not in data and mg in data:
            mg_key = mg
        if mg_key in data:
            vars_dict = data[mg_key].get("Variables", data[mg_key])
            p_trade_dict = vars_dict.get("P_trade", vars_dict.get("p_trade", {}))
            lamda_dict = vars_dict.get("lamda_ATC", vars_dict.get("lamda", {}))
            
            mg_nodes[mg] = {}
            nodes = set()
            for k in p_trade_dict.keys():
                if isinstance(k, str) and k.startswith("("):
                    parts = k.strip("()").split(",")
                    if len(parts) >= 2:
                        nodes.add(parts[0].strip(" '\""))
            
            for node in nodes:
                node_p_trade = {k: v for k, v in p_trade_dict.items() if k.startswith(f"({node},") or k.startswith(f"('{node}',")}
                node_lamda = {k: v for k, v in lamda_dict.items() if k.startswith(f"({node},") or k.startswith(f"('{node}',")}
                mg_nodes[mg][node] = {
                    'p_trade': get_series(node_p_trade),
                    'lamda': get_series(node_lamda)
                }

    nodes_flat = []
    for mg, nodes in mg_nodes.items():
        for node, data_node in nodes.items():
            nodes_flat.append({
                'mg': mg, 'node': node,
                'p_trade': data_node['p_trade'], 'lamda': data_node['lamda'], 'paired': False
            })
            
    pairs = []
    for i in range(len(nodes_flat)):
        if nodes_flat[i]['paired']: continue
        best_match = -1
        best_score = float('inf')
        for j in range(i+1, len(nodes_flat)):
            if nodes_flat[j]['paired']: continue
            diff_p = np.sum(np.abs(nodes_flat[i]['p_trade'] + nodes_flat[j]['p_trade']))
            diff_lamda = np.sum(np.abs(nodes_flat[i]['lamda'] - nodes_flat[j]['lamda']))
            score = diff_p + diff_lamda * 10
            if score < best_score:
                best_score = score
                best_match = j
        if best_match != -1:
            nodes_flat[i]['paired'] = True
            nodes_flat[best_match]['paired'] = True
            pairs.append((nodes_flat[i], nodes_flat[best_match]))

    time_steps = list(range(1, 25))
    markers = ['o', 's', '^', 'D', 'v', '<', '>', 'p', '*']
    linestyles = ['-', '--', '-.', ':']
    
    plt.style.use('seaborn-v0_8-paper')
    plt.rcParams['font.family'] = 'serif'
    plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
    
    fig, ax = plt.subplots(figsize=(10, 6))
    for idx, (nodeA, nodeB) in enumerate(pairs):
        mgA = nodeA['mg']
        mgB = nodeB['mg']
        lamda_avg = (nodeA['lamda'] + nodeB['lamda']) / 2.0
        if np.max(np.abs(lamda_avg)) < 1e-6:
            continue
            
        marker = markers[idx % len(markers)]
        ls = linestyles[idx % len(linestyles)]
        label_str = f"MG{mgA} - MG{mgB} Tie-line"
        ax.plot(time_steps, lamda_avg, marker=marker, markersize=6, linestyle=ls, linewidth=1.5, label=label_str)

    ax.set_xlabel('Time (Hour)', fontsize=14)
    ax.set_ylabel('Internal Price ($\lambda_{ATC}$)', fontsize=14)
    ax.set_xticks(time_steps)
    ax.grid(True, linestyle=':', alpha=0.6)
    ax.axvspan(9, 15, color='gray', alpha=0.3, label='Fault Window (9-15h)')
    ax.legend(loc='upper left', bbox_to_anchor=(1.02, 1), frameon=True, fontsize=11)
    plt.title('Stage 5: ATC Scarcity Pricing Dynamics ($\lambda$) For All Connections', fontsize=16, pad=15)
    fig.tight_layout()

    out_dir = r"D:\Code\P2P_trading_withQV_MG1234\P2P_trading_withQV_MG1234\Result_data\report_result\stage_5"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "Stage5_ATC_Pricing_Lambda.png")
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close(fig)
    print(f"Saved {out_path}")

if __name__ == '__main__':
    plot_loss()
    plot_lambda()
