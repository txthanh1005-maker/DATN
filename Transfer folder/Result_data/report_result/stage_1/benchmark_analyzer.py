import json
import csv
import os
import matplotlib.pyplot as plt
import numpy as np
import re

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def extract_metrics(data):
    total_economic = 0.0
    total_pure = 0.0
    total_shed = 0.0
    for mg_data in data.values():
        pure_cost = 0.0
        if "Costs" in mg_data:
            pure_cost = mg_data["Costs"].get("Pure_Cost", 0.0)
            total_pure += pure_cost
            total_shed += mg_data["Costs"].get("Shedding_kWh", 0.0)
        
        # Calculate True Economic Cost: Pure Cost + Penalty Shedding
        # Note: 1 pu = 1 MW. C_shed_normal = 100000, C_shed_critical = 5000000
        shed_normal_sum = 0.0
        if "P_shed_normal" in mg_data:
            for val in mg_data["P_shed_normal"].values():
                if val: shed_normal_sum += val
                
        shed_crit_sum = 0.0
        if "P_shed_critical" in mg_data:
            for val in mg_data["P_shed_critical"].values():
                if val: shed_crit_sum += val
                
        true_economic = pure_cost + 100000 * shed_normal_sum + 5000000 * shed_crit_sum
        total_economic += true_economic
        
    return {
        "Economic_Cost": total_economic,
        "Pure_Cost": total_pure,
        "Shedding_kWh": total_shed
    }

def get_series(variables, possible_names, positive_only=False, negative_only=False):
    for name in possible_names:
        if name in variables:
            var_data = variables[name]
            series = [0.0] * 24
            
            if isinstance(var_data, list):
                for t, v in enumerate(var_data):
                    if v is None: continue
                    val = float(v)
                    if positive_only and val <= 0: continue
                    if negative_only and val >= 0: continue
                    if negative_only: val = abs(val)
                    if 0 <= t < 24:
                        series[t] += val
                if any(v > 0 for v in series):
                    return series
                
            elif isinstance(var_data, dict):
                for k, v in var_data.items():
                    if v is None: continue
                    val = float(v)
                    if positive_only and val <= 0: continue
                    if negative_only and val >= 0: continue
                    if negative_only: val = abs(val)
                    
                    t = -1
                    if isinstance(k, str):
                        if k.startswith("("):
                            parts = k.strip("()").split(",")
                            if len(parts) >= 2:
                                t = int(parts[-1].strip())
                        else:
                            try:
                                t = int(k)
                            except ValueError:
                                m = re.findall(r'\d+', k)
                                if m: t = int(m[-1])
                    if 0 <= t < 24:
                        series[t] += val
                if any(v > 0 for v in series) or not positive_only:
                    return series
    return [0.0] * 24

def get_series_avg(variables, possible_names):
    for name in possible_names:
        if name in variables:
            var_data = variables[name]
            series = [0.0] * 24
            counts = [0] * 24
            
            if isinstance(var_data, list):
                for t, v in enumerate(var_data):
                    if v is None: continue
                    val = float(v)
                    if 0 <= t < 24:
                        series[t] += val
                        counts[t] += 1
                if sum(counts) > 0:
                    return [s/c if c > 0 else 0.0 for s, c in zip(series, counts)]

            elif isinstance(var_data, dict):
                for k, v in var_data.items():
                    if v is None: continue
                    val = float(v)
                    t = -1
                    if isinstance(k, str):
                        if k.startswith("("):
                            parts = k.strip("()").split(",")
                            if len(parts) >= 2:
                                t = int(parts[-1].strip())
                        else:
                            try:
                                t = int(k)
                            except ValueError:
                                m = re.findall(r'\d+', k)
                                if m: t = int(m[-1])
                    if 0 <= t < 24:
                        series[t] += val
                        counts[t] += 1
                if sum(counts) > 0:
                    return [s/c if c > 0 else 0.0 for s, c in zip(series, counts)]
    return [0.0] * 24

def plot_charts(filepath, output_dir):
    if not os.path.exists(filepath):
        print(f"Cannot plot: {filepath} not found.")
        return
        
    data = load_json(filepath)
    first_key = list(data.keys())[0]
    vars_dict = data[first_key]
    
    if "Variables" in vars_dict:
        vars_dict = vars_dict["Variables"]
        
    # --- Chart 1: P_trade (Bar, Left Y) + lamda (Line, Right Y) ---
    p_trade_pos = get_series(vars_dict, ["P_trade", "p_trade", "P_tr"], positive_only=True)
    if sum(p_trade_pos) == 0:
        p_trade_pos = get_series(vars_dict, ["P_trade_buy", "P_buy", "p_trade_buy"])
        
    lamda = get_series_avg(vars_dict, ["lamda", "lambda", "lamda_trade", "lambda_t", "Price", "price", "lamda_c"])
    
    time_steps = list(range(24))
    
    fig1, ax1 = plt.subplots(figsize=(10, 5))
    ax1.bar(time_steps, p_trade_pos, color='skyblue', label='P_trade')
    ax1.set_xlabel('Time (Hour)')
    ax1.set_ylabel('P_trade (kW)', color='blue')
    ax1.tick_params(axis='y', labelcolor='blue')
    ax1.set_xticks(time_steps)
    
    ax2 = ax1.twinx()
    ax2.plot(time_steps, lamda, color='red', marker='o', label='Internal Price (\u03bb)')
    ax2.set_ylabel('Price (\u03bb)', color='red')
    ax2.tick_params(axis='y', labelcolor='red')
    
    fig1.suptitle("P_trade and Internal Electricity Price (lamda)")
    fig1.legend(loc='upper right', bbox_to_anchor=(0.9, 0.9))
    fig1.tight_layout()
    chart1_path = os.path.join(output_dir, "Chart1_P_trade_lamda.png")
    fig1.savefig(chart1_path)
    plt.close(fig1)
    
    # --- Chart 2: EMS Dispatch (Stacked Area, Left Y) + SOC (Line, Right Y) ---
    p_dg = get_series(vars_dict, ["P_dg", "p_dg", "Pdg", "P_gen"])
    p_trade_buy = get_series(vars_dict, ["P_trade_buy", "P_trade", "P_tr", "P_buy"], positive_only=True)
    p_wind = get_series(vars_dict, ["P_wind", "P_w", "p_wind"])
    p_pv = get_series(vars_dict, ["P_pv", "P_s", "p_pv"])
    
    p_dis = get_series(vars_dict, ["P_dis", "P_bess_dis", "P_discharge", "p_dis"])
    if sum(p_dis) == 0:
        p_dis = get_series(vars_dict, ["P_bess", "P_ess", "p_bess"], positive_only=True)
        
    p_shed = get_series(vars_dict, ["P_shed", "P_curt", "Shedding", "p_shed", "P_load_shed", "P_ls"])
    soc = get_series_avg(vars_dict, ["SOC", "soc", "E_bess", "E_bat", "E"])
    
    stack_data = [p_pv, p_wind, p_dg, p_trade_buy, p_dis, p_shed]
    labels = ["PV", "Wind", "DG", "P_trade_buy", "BESS Disch", "Load Shedding"]
    colors = ['gold', 'lightblue', 'gray', 'purple', 'lightgreen', 'red']
    
    fig2, ax3 = plt.subplots(figsize=(10, 5))
    ax3.stackplot(time_steps, stack_data, labels=labels, colors=colors, alpha=0.8)
    ax3.set_xlabel('Time (Hour)')
    ax3.set_ylabel('Power Dispatch (kW)')
    ax3.set_xticks(time_steps)
    
    # Highlight Fault Window: t=9 to 15
    ax3.axvspan(9, 15, color='red', alpha=0.2, label='Fault Window')
    
    ax4 = ax3.twinx()
    ax4.plot(time_steps, soc, color='blue', linewidth=2, marker='s', label='SOC / E_bess')
    ax4.set_ylabel('SOC / E_bess', color='blue')
    ax4.tick_params(axis='y', labelcolor='blue')
    
    fig2.suptitle("EMS Dispatch and BESS SOC")
    fig2.legend(loc='upper right', bbox_to_anchor=(0.9, 0.9))
    fig2.tight_layout()
    chart2_path = os.path.join(output_dir, "Chart2_EMS_Dispatch.png")
    fig2.savefig(chart2_path)
    plt.close(fig2)
    
    # --- Chart 3: Voltage Profile (Line) ---
    fig3, ax5 = plt.subplots(figsize=(10, 5))
    v_data = vars_dict.get("V", vars_dict.get("v", vars_dict.get("Voltage", {})))
    if isinstance(v_data, dict):
        node_v = {}
        for k, val in v_data.items():
            if val is None: continue
            k_str = str(k).strip("()")
            parts = k_str.split(",")
            if len(parts) >= 2:
                node = parts[0].strip()
                t_str = parts[-1].strip()
                try:
                    t = int(t_str)
                    if node not in node_v:
                        node_v[node] = [1.0] * 24
                    if 0 <= t < 24:
                        node_v[node][t] = float(val)
                except ValueError:
                    pass
            elif len(parts) == 1:
                try:
                    t = int(parts[0].strip())
                    node = "MG"
                    if node not in node_v:
                        node_v[node] = [1.0] * 24
                    if 0 <= t < 24:
                        node_v[node][t] = float(val)
                except ValueError:
                    pass
        nodes_to_plot = list(node_v.keys())[:4]
        for node in nodes_to_plot:
            ax5.plot(time_steps, node_v[node], marker='o', label=f'Node {node}')
    elif isinstance(v_data, list):
        v_series = [float(v) if v is not None else 1.0 for v in v_data]
        ax5.plot(time_steps, v_series[:24], marker='o', label='V Profile')

    ax5.set_xlabel('Time (Hour)')
    ax5.set_ylabel('Voltage (p.u.)')
    ax5.set_xticks(time_steps)
    ax5.axvspan(9, 15, color='red', alpha=0.2, label='Fault Window')
    fig3.suptitle("Voltage Profile of MGs")
    fig3.legend(loc='upper right', bbox_to_anchor=(0.9, 0.9))
    fig3.tight_layout()
    chart3_path = os.path.join(output_dir, "Chart3_Voltage_Profile.png")
    fig3.savefig(chart3_path)
    plt.close(fig3)
    
    # --- Chart 4: Load Shedding Stacked Bar ---
    p_shed_crit = get_series(vars_dict, ["P_shed_critical", "P_shed_crit", "p_shed_critical", "P_crit_shed", "p_shed_c"])
    p_shed_norm = get_series(vars_dict, ["P_shed_normal", "P_shed_norm", "p_shed_normal", "P_norm_shed", "p_shed_n"])
    
    fig4, ax6 = plt.subplots(figsize=(10, 5))
    ax6.bar(time_steps, p_shed_crit, color='black', label='P_shed_critical')
    ax6.bar(time_steps, p_shed_norm, bottom=p_shed_crit, color='orange', label='P_shed_normal')
    ax6.set_xlabel('Time (Hour)')
    ax6.set_ylabel('Shedding Power (kW)')
    ax6.set_xticks(time_steps)
    ax6.axvspan(9, 15, color='red', alpha=0.1, label='Fault Window')
    
    fig4.suptitle("Load Shedding Details (Critical vs Normal)")
    fig4.legend(loc='upper right', bbox_to_anchor=(0.9, 0.9))
    fig4.tight_layout()
    chart4_path = os.path.join(output_dir, "Chart4_Load_Shedding.png")
    fig4.savefig(chart4_path)
    plt.close(fig4)
    
    # --- Chart 5: Performance (CPU Time and Iterations) ---
    cpu_time = None
    iterations = None
    
    for source in [vars_dict, data[first_key]]:
        if "CPU_Time" in source or "cpu_time" in source:
            cpu_time = source.get("CPU_Time", source.get("cpu_time"))
        if "Iterations" in source or "iterations" in source:
            iterations = source.get("Iterations", source.get("iterations"))
            
    if cpu_time is None and "Performance" in data[first_key]:
        perf = data[first_key]["Performance"]
        cpu_time = perf.get("CPU_Time", perf.get("cpu_time"))
        iterations = perf.get("Iterations", perf.get("iterations"))
        
    def to_series(val):
        if isinstance(val, (int, float)):
            return [float(val)] * 24
        elif isinstance(val, list):
            return [float(v) if v is not None else 0.0 for v in val]
        elif isinstance(val, dict):
            s = [0.0]*24
            for k, v in val.items():
                if v is None: continue
                try:
                    t = int(str(k).strip("()").split(",")[-1].strip())
                    if 0 <= t < 24: s[t] = float(v)
                except: pass
            return s
        return [0.0]*24

    if cpu_time is not None or iterations is not None:
        fig5, ax7 = plt.subplots(figsize=(10, 5))
        cpu_series = to_series(cpu_time) if cpu_time is not None else [0.0]*24
        iter_series = to_series(iterations) if iterations is not None else [0.0]*24
        
        if cpu_time is not None:
            ax7.bar(time_steps, cpu_series[:24], color='purple', alpha=0.6, label='CPU Time')
            ax7.set_ylabel('CPU Time (s)', color='purple')
            ax7.tick_params(axis='y', labelcolor='purple')
            
        ax7.set_xlabel('Time (Hour)')
        ax7.set_xticks(time_steps)
        
        if iterations is not None:
            ax8 = ax7.twinx() if cpu_time is not None else ax7
            ax8.plot(time_steps, iter_series[:24], color='green', marker='d', label='Iterations')
            ax8.set_ylabel('Iterations', color='green')
            ax8.tick_params(axis='y', labelcolor='green')
            if cpu_time is None:
                ax8.set_xlabel('Time (Hour)')
                ax8.set_xticks(time_steps)
                
        fig5.suptitle("Performance Metrics (CPU Time & Iterations)")
        lines_labels = [ax.get_legend_handles_labels() for ax in fig5.axes]
        lines, labels = [sum(lol, []) for lol in zip(*lines_labels)]
        fig5.legend(lines, labels, loc='upper right', bbox_to_anchor=(0.9, 0.9))
        fig5.tight_layout()
        chart5_path = os.path.join(output_dir, "Chart5_Performance.png")
        fig5.savefig(chart5_path)
        plt.close(fig5)
        print(f"Charts saved to {chart1_path}, {chart2_path}, {chart3_path}, {chart4_path}, and {chart5_path}")
    else:
        print(f"Charts saved to {chart1_path}, {chart2_path}, {chart3_path}, and {chart4_path}")

def main():
    base_dir = r"D:\Code\P2P_trading_withQV_MG1234\P2P_trading_withQV_MG1234\Result_data"
    files = {
        "base_fault": "base_fault.json",
        "current_method": "current_method.json",
        "foresight_model": "foresight_model.json"
    }
    
    results = {}
    for name, filename in files.items():
        filepath = os.path.join(base_dir, filename)
        if os.path.exists(filepath):
            data = load_json(filepath)
            results[name] = extract_metrics(data)
        else:
            print(f"File not found: {filepath}")
            results[name] = {"Economic_Cost": 0.0, "Pure_Cost": 0.0, "Shedding_kWh": 0.0}
            
    csv_file = os.path.join(base_dir, "Benchmark_Summary.csv")
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Model", "Economic_Cost", "Pure_Cost", "Shedding_kWh"])
        for name, metrics in results.items():
            writer.writerow([name, metrics["Economic_Cost"], metrics["Pure_Cost"], metrics["Shedding_kWh"]])
            
    print(f"Data written to {csv_file}")
    print("\n--- MACRO COMPARISON ---")
    
    curr = results.get("current_method", {})
    fore = results.get("foresight_model", {})
    
    if fore.get("Economic_Cost", 0) > 0:
        gap_econ = (curr.get("Economic_Cost", 0) - fore.get("Economic_Cost", 0)) / fore.get("Economic_Cost", 1) * 100
        print(f"Economic Cost Optimality Gap: {gap_econ:.2f}%")
        
    if fore.get("Pure_Cost", 0) > 0:
        gap_pure = (curr.get("Pure_Cost", 0) - fore.get("Pure_Cost", 0)) / fore.get("Pure_Cost", 1) * 100
        print(f"Pure Cost Optimality Gap: {gap_pure:.2f}%")
        
    print("\nDetailed Metrics:")
    for name, m in results.items():
        print(f"{name}: Pure Cost = {m['Pure_Cost']:.2f}, Economic Cost = {m['Economic_Cost']:.2f}, Shedding = {m['Shedding_kWh']:.4f} kWh")
        
    # Tạo đồ thị cho current_method
    curr_filepath = os.path.join(base_dir, "current_method.json")
    if os.path.exists(curr_filepath):
        print(f"\nGenerating charts for current_method...")
        plot_charts(curr_filepath, base_dir)

if __name__ == "__main__":
    main()
