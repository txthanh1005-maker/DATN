import json
import os
import matplotlib.pyplot as plt
import numpy as np
import re

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def extract_energy_and_costs(data):
    total_pure = 0.0
    total_shed = 0.0
    shed_normal_sum = 0.0
    shed_crit_sum = 0.0
    
    # Energy components in kWh
    total_pv = 0.0
    total_wind = 0.0
    total_dg = 0.0
    total_grid = 0.0
    total_bess_dis = 0.0
    
    for mg, mg_data in data.items():
        if "Costs" in mg_data:
            total_pure += mg_data["Costs"].get("Pure_Cost", 0.0)
            total_shed += mg_data["Costs"].get("Shedding_kWh", 0.0)
            
        if "P_shed_normal" in mg_data:
            for val in mg_data["P_shed_normal"].values():
                if val: shed_normal_sum += val
        if "P_shed_critical" in mg_data:
            for val in mg_data["P_shed_critical"].values():
                if val: shed_crit_sum += val
                
        # Extract energy series
        vars_dict = mg_data.get("Variables", mg_data)
        
        def sum_var(names):
            s = 0.0
            for name in names:
                if name in vars_dict:
                    v_data = vars_dict[name]
                    if isinstance(v_data, list):
                        s += sum(v for v in v_data if v is not None and v > 0)
                        return s
                    elif isinstance(v_data, dict):
                        s += sum(v for v in v_data.values() if v is not None and v > 0)
                        return s
            return s

        total_pv += sum_var(["P_PV", "P_pv", "p_pv", "P_s"])
        total_wind += sum_var(["P_Wind", "P_wind", "p_wind", "P_w"])
        total_dg += sum_var(["P_DG", "P_dg", "p_dg", "Pdg"])
        total_grid += sum_var(["P_pos", "P_Grid", "P_grid", "p_grid"])
        total_bess_dis += sum_var(["PD_BESS", "P_dis", "P_bess_dis", "P_discharge"])
        if sum_var(["PD_BESS", "P_dis", "P_bess_dis", "P_discharge"]) == 0:
            total_bess_dis += sum_var(["P_BESS", "P_bess", "p_bess"]) # if P_bess is positive for discharge
            
    true_economic = total_pure + 100000 * shed_normal_sum + 5000000 * shed_crit_sum
    
    return {
        "True_Economic_Cost": true_economic,
        "Shedding_MWh": total_shed,
        "PV_MWh": total_pv,
        "Wind_MWh": total_wind,
        "DG_MWh": total_dg,
        "Grid_MWh": total_grid,
        "BESS_Dis_MWh": total_bess_dis
    }

def main():
    base_dir = r"D:\Code\P2P_trading_withQV_MG1234\P2P_trading_withQV_MG1234\Result_data"
    output_dir = os.path.join(base_dir, "report_result", "stage_1")
    os.makedirs(output_dir, exist_ok=True)
    
    files = {
        "Base Fault": "base_fault.json",
        "MPC (Current)": "current_method.json",
        "Foresight": "foresight_model.json"
    }
    
    results = {}
    for name, filename in files.items():
        filepath = os.path.join(base_dir, filename)
        if os.path.exists(filepath):
            data = load_json(filepath)
            results[name] = extract_energy_and_costs(data)
        else:
            print(f"File not found: {filepath}")
            return
            
    models = list(results.keys())
    
    # ---------------------------------------------------------
    # CHART 1: Grouped Bar Chart (True Economic Cost vs Shedding)
    # ---------------------------------------------------------
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    
    eco_costs = [results[m]["True_Economic_Cost"] for m in models]
    sheddings = [results[m]["Shedding_MWh"] for m in models]
    
    x = np.arange(len(models))
    width = 0.35
    
    bar1 = ax1.bar(x - width/2, eco_costs, width, label='True Economic Cost (cents)', color='royalblue')
    ax1.set_xlabel('Models', fontweight='bold')
    ax1.set_ylabel('True Economic Cost (cents)', color='royalblue', fontweight='bold')
    ax1.tick_params(axis='y', labelcolor='royalblue')
    ax1.set_xticks(x)
    ax1.set_xticklabels(models, fontweight='bold')
    
    # Use log scale for Economic Cost to make differences visible if there are extreme values
    ax1.set_yscale('log')
    
    ax2 = ax1.twinx()
    bar2 = ax2.bar(x + width/2, sheddings, width, label='Load Shedding (MWh)', color='crimson')
    ax2.set_ylabel('Load Shedding (MWh)', color='crimson', fontweight='bold')
    ax2.tick_params(axis='y', labelcolor='crimson')
    
    fig1.suptitle('Macro-Level Comparison: Total Cost vs Load Shedding', fontsize=14, fontweight='bold')
    
    # Add values on top of bars
    for i, rect in enumerate(bar1):
        height = rect.get_height()
        ax1.text(rect.get_x() + rect.get_width()/2., height,
                f'{eco_costs[i]:,.0f}', ha='center', va='bottom', rotation=0, fontsize=9)
    for i, rect in enumerate(bar2):
        height = rect.get_height()
        ax2.text(rect.get_x() + rect.get_width()/2., height,
                f'{sheddings[i]:.4f}', ha='center', va='bottom', rotation=0, fontsize=9)
                
    fig1.tight_layout()
    chart1_path = os.path.join(output_dir, "Stage1_Cost_vs_Shedding.png")
    fig1.savefig(chart1_path, dpi=300)
    plt.close(fig1)
    
    # ---------------------------------------------------------
    # CHART 2: Stacked Bar Chart (Energy Distribution -> Negative Premium)
    # ---------------------------------------------------------
    fig2, ax = plt.subplots(figsize=(10, 6))
    
    pv = np.array([results[m]["PV_MWh"] for m in models])
    wind = np.array([results[m]["Wind_MWh"] for m in models])
    dg = np.array([results[m]["DG_MWh"] for m in models])
    grid = np.array([results[m]["Grid_MWh"] for m in models])
    bess = np.array([results[m]["BESS_Dis_MWh"] for m in models])
    
    ax.bar(models, grid, label='Grid Import (MWh)', color='purple', edgecolor='black')
    ax.bar(models, pv, bottom=grid, label='PV (MWh)', color='gold', edgecolor='black')
    ax.bar(models, wind, bottom=grid+pv, label='Wind (MWh)', color='skyblue', edgecolor='black')
    ax.bar(models, dg, bottom=grid+pv+wind, label='DG (MWh)', color='gray', edgecolor='black')
    ax.bar(models, bess, bottom=grid+pv+wind+dg, label='BESS Discharge (MWh)', color='lightgreen', edgecolor='black')
    
    # Calculate total energy to put text on top
    totals = grid + pv + wind + dg + bess
    for i, total in enumerate(totals):
        ax.text(i, total + 0.5, f'Total: {total:.1f} MWh', ha='center', fontweight='bold')
        
    ax.set_ylabel('Total Energy Utilized (MWh)', fontweight='bold')
    ax.set_title('Energy Mix Distribution (Unblocking Stranded Renewables)', fontsize=14, fontweight='bold')
    ax.legend(loc='lower left', bbox_to_anchor=(1, 0.5))
    
    fig2.tight_layout()
    chart2_path = os.path.join(output_dir, "Stage1_Energy_Mix.png")
    fig2.savefig(chart2_path, dpi=300)
    plt.close(fig2)
    
    print(f"Successfully saved {chart1_path} and {chart2_path}")

if __name__ == "__main__":
    main()
