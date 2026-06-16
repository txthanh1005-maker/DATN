import json
import os
import matplotlib.pyplot as plt
import numpy as np
import ast
import matplotlib.cm as cm

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def plot_load_shedding():
    filepath = r"D:\Code\P2P_trading_withQV_MG1234\P2P_trading_withQV_MG1234\Result_data\current_method.json"
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return

    data = load_json(filepath)
    out_dir = r"D:\Code\P2P_trading_withQV_MG1234\P2P_trading_withQV_MG1234\Result_data\report_result\stage_3"
    os.makedirs(out_dir, exist_ok=True)

    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
    
    for mg_key, mg_data in data.items():
        try:
            mg_index = int(mg_key)
        except ValueError:
            # Handle if key is "1" or "MG_1"
            mg_index = int(''.join(filter(str.isdigit, mg_key)))

        shed_normal_nodes = {}
        shed_critical_nodes = {}

        if "P_shed_normal" in mg_data:
            for k, v in mg_data["P_shed_normal"].items():
                if v and v > 1e-4:
                    node, t = ast.literal_eval(k)
                    if node not in shed_normal_nodes:
                        shed_normal_nodes[node] = np.zeros(24)
                    shed_normal_nodes[node][t] += v

        if "P_shed_critical" in mg_data:
            for k, v in mg_data["P_shed_critical"].items():
                if v and v > 1e-4:
                    node, t = ast.literal_eval(k)
                    if node not in shed_critical_nodes:
                        shed_critical_nodes[node] = np.zeros(24)
                    shed_critical_nodes[node][t] += v

        fig, ax = plt.subplots(figsize=(8, 4))
        x = np.arange(24)
        has_shedding = False
        bottom_normal = np.zeros(24)
        bottom_critical = np.zeros(24)

        for idx, node in enumerate(sorted(shed_normal_nodes.keys())):
            node_data = shed_normal_nodes[node]
            ax.bar(x, node_data, width=0.6, bottom=bottom_normal, label=f'Node {node} (Normal)', color=colors[idx % len(colors)])
            bottom_normal += node_data
            has_shedding = True

        for idx, node in enumerate(sorted(shed_critical_nodes.keys())):
            node_data = shed_critical_nodes[node]
            bottom_critical_plot = bottom_normal + bottom_critical
            ax.bar(x, node_data, width=0.6, bottom=bottom_critical_plot, label=f'Node {node} (Critical)', hatch='//', color=colors[(idx + 4) % len(colors)])
            bottom_critical += node_data
            has_shedding = True

        ax.axvspan(9, 15, color='red', alpha=0.1, label='Fault Window')

        ax.set_title(f'Load Shedding by Node - MG {mg_index} (MPC)', fontsize=12, fontweight='bold')
        ax.set_xlabel('Time (h)', fontsize=10)
        ax.set_ylabel('Power Shed (MW)', fontsize=10)
        ax.set_xticks(x)
        ax.grid(True, axis='y', linestyle='--', alpha=0.7)
        
        if has_shedding:
            ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=9)
        else:
            # Always show legend for fault window
            ax.legend(loc='upper right', fontsize=9)
            
        fig.tight_layout()
        out_path = os.path.join(out_dir, f"Load_Shedding_MG{mg_index}.png")
        fig.savefig(out_path, dpi=300, bbox_inches='tight')
        plt.close(fig)
        print(f"Saved {out_path}")

if __name__ == '__main__':
    plot_load_shedding()
