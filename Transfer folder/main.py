
"""
[Semantic Metadata]
- Implements: Tập lệnh chính thực thi chương trình, cấu hình dữ liệu và điều phối các hàm khởi tạo mô hình tối ưu cho lưới điện/P2P.
- Related_to_Paper: Emergency_Sharing_Plan
"""

# %% [Phần 0: Chạy cái này một lần duy nhất]
#! Khai báo thư viện 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import sys
import time
import json

import pyomo.environ as pe
import pyomo.opt as po
from pyomo.environ import *
from pyomo.environ import value as py_value, Constraint
from pyomo.core.expr.visitor import identify_variables

import logging
logging.getLogger('pyomo.core').setLevel(logging.ERROR)
from pyomo.environ import Constraint, value as py_value
from pyomo.environ import SolverStatus, TerminationCondition

print ("Start the program")
#! Khai báo hàm 
import build_model
from build_model import build_microgrid_model
from build_model import solve_microgrid_model
from build_model import ATC_Global_model
from build_model import Result_print
from build_model import build_coordinator_model
from Function import S_base, create_graph_separate_MG_trading, load_trading_network, print_line_data
from Function import scale_power

mg_configs = {
        1: {
            'number_of_node': 36,
            # 'list_PV': {3, 8, 10, 12, 14, 26, 36},
            'list_PV': {3, 10, 12, 14, 26, 36},
            'list_Wind': {32},
            'list_BESS': {19},
            'list_DG': {5},
            'grid_trading_limit_max':150,
            'grid_trading_limit_min':-150
        },
        2: {
            'number_of_node': 30,
            'list_PV': {14, 19, 28, 30},
            'list_Wind': {},
            'list_BESS': {20},
            'list_DG': {10},
            'grid_trading_limit_max':1500,
            'grid_trading_limit_min':-1500
        },
        3: {
            'number_of_node': 21,
            'list_PV': {2, 8, 11, 15},
            'list_Wind': {1},
            'list_BESS': {12},
            'list_DG': {9},
            'grid_trading_limit_max':150,
            'grid_trading_limit_min':-150
        },
        4: {
            # Dữ liệu trích xuất từ code MG4
            'number_of_node': 35,          # number_of_node4
            'list_PV': {18, 20, 27,29},       # list_PV
            'list_Wind': {},               # list_Wind (Rỗng)
            'list_BESS': {8},              # list_BESS
            'list_DG': {22},               #          
            'grid_trading_limit_max':150,
            'grid_trading_limit_min':-150 # limit_buy_sell_form_grid (tham số 2)
        }
    } 
trading_limit = {
    0:0* scale_power / S_base,
    1:0* scale_power / S_base,
    2:0* scale_power/ S_base,
    3:0* scale_power / S_base,
    4:0* scale_power / S_base
}

# %%
#! BASE FAULT MODEL
model_name = "base_fault"
export_limit = 5000
from build_model import accident_model
from data_exporter import expmodel
from Function import print_result, create_graph_separate_MG_trading, create_graph_separate_MG_Q, S_base, scale_power, plot_ieee_graphs

# Chạy mô hình độc lập khi có lỗi. Vẫn dùng export_limit=5000 nhưng ép trading_limit_p2p = 0
trading_limit_p2p_base = {
    0: 0 * scale_power / S_base,
    1: 0 * scale_power / S_base,
    2: 0 * scale_power / S_base,
    3: 0 * scale_power / S_base,
    4: 0 * scale_power / S_base
}

# 2. Các lỗi xảy ra tuần tự (Cascading)
fault_configs_cascading = {
    1: [],
    2: [
        {'start_time': 9, 'end_time': 15, 'type': 'grid_loss', 'severity': 0.0},
        {'start_time': 11, 'end_time': 15, 'type': 'pv_loss', 'severity': 0.0}  
    ],
    3: [],
    4: [        
        {'start_time': 9, 'end_time': 15, 'type': 'grid_loss', 'severity': 0.0},
        {'start_time': 11, 'end_time': 15, 'type': 'pv_loss', 'severity': 0.0}]
}
fault_configs = fault_configs_cascading 

print("\n" + "="*60)
print("🚀 [BƯỚC 1/3] BẮT ĐẦU CHẠY MÔ HÌNH: BASE FAULT (INDEPENDENT) 🚀")
print("="*60)
# Build and solve accident model without P2P trading
model_MG_base_fault, trading_line_base = accident_model(mg_configs, trading_limit_p2p_base, export_limit, fault_configs)

expmodel(model_name, "Result_data", model_MG_base_fault)

for MG in {1, 2, 3, 4}:
    print_result(model_MG_base_fault[MG], MG)
    create_graph_separate_MG_trading(model_MG_base_fault[MG], export_limit * scale_power / S_base, trading_line_base, MG, model_name=model_name)
    create_graph_separate_MG_Q(model_MG_base_fault[MG], export_limit * scale_power / S_base, trading_line_base, MG, model_name=model_name)

# %%
#! PERFECT FORESIGHT MODEL
model_name = "foresight_model"
from build_model import ATC_Global_model_mpc

trading_limit_p2p = {
    0: 150 * scale_power / S_base,
    1: 150 * scale_power / S_base,
    2: 150 * scale_power / S_base,
    3: 150 * scale_power / S_base,
    4: 150 * scale_power / S_base
}

print("\n" + "="*60)
print("🚀 [BƯỚC 2/3] BẮT ĐẦU CHẠY MÔ HÌNH: PERFECT FORESIGHT (ATC 24H) 🚀")
print("="*60)
import sys
import os

if not os.path.exists("Emergency_Sharing_Plan"):
    os.makedirs("Emergency_Sharing_Plan")

print("# Báo cáo quá trình hội tụ ATC Perfect Foresight\n")
SOC_init_pf = {MG: None for MG in {1,2,3,4}}
SOC_DA_ref_pf = {MG: None for MG in {1,2,3,4}}
t_start_pf = time.time()
model_MG_pf, trading_line_pf, history_r, history_s, history_rho, lamda = ATC_Global_model_mpc(mg_configs, export_limit, trading_limit_p2p, H=24, SOC_init=SOC_init_pf, SOC_DA_ref=SOC_DA_ref_pf, t_start=0, fault_configs=fault_configs)
t_end_pf = time.time()
total_time_pf = t_end_pf - t_start_pf
Result_print(model_MG_pf, export_limit, trading_line_pf)
print(">> ATC Perfect Foresight run completed.")

expmodel(model_name, "Result_data", model_MG_pf)

for MG in {1, 2, 3, 4}:
    print_result(model_MG_pf[MG], MG)
    create_graph_separate_MG_trading(model_MG_pf[MG], export_limit * scale_power / S_base, trading_line_pf, MG, model_name=model_name)
    create_graph_separate_MG_Q(model_MG_pf[MG], export_limit * scale_power / S_base, trading_line_pf, MG, model_name=model_name)

# %%
#! CURRENT METHOD (MPC)
model_name = "current_method"
from build_model import ATC_Global_model, run_MPC_simulation

print("\n" + "="*60)
print("🚀 [BƯỚC 3/3] BẮT ĐẦU CHẠY MÔ HÌNH: CURRENT METHOD (MPC ROLLING HORIZON) 🚀")
print("="*60)
print("# Báo cáo quá trình hội tụ ATC Day-Ahead\n")
t_start_da = time.time()
model_MG_atc, trading_line_atc, history_r, history_s, history_rho, lamda = ATC_Global_model(mg_configs, export_limit, trading_limit_p2p)
t_end_da = time.time()
total_time_da = t_end_da - t_start_da
Result_print(model_MG_atc, export_limit, trading_line_atc)
print(">> ATC run completed.")

H = 5
print(f"\n--- RUNNING FULL MPC SIMULATION (Rolling Horizon) WITH H={H} ---")

warm_start_data = {}
for MG in {1, 2, 3, 4}:
    for node in model_MG_atc[MG].node_has_trade:
        for t in range(24):
            warm_start_data[(MG, node, t)] = {
                'lamda': py_value(model_MG_atc[MG].lamda_ATC[node, t]),
                'P_target': py_value(model_MG_atc[MG].P_target[node, t]),
                'P_trade': py_value(model_MG_atc[MG].P_trade[node, t])
            }

model_MG_mpc, trading_line_mpc, cpu_time_history, convergence_all_hours = run_MPC_simulation(
    mg_configs=mg_configs, 
    export_limit=export_limit, 
    trading_limit_p2p=trading_limit_p2p, 
    H=H, 
    model_MG_atc=model_MG_atc, 
    fault_configs=fault_configs,
    perfect_foresight=False,
    warm_start_data=warm_start_data
)

expmodel(model_name, "Result_data", model_MG_mpc)

for MG in {1, 2, 3, 4}:
    print(f"--- RESULTS FOR MG{MG} IN MPC ---")
    print_result(model_MG_mpc[MG], MG)
    create_graph_separate_MG_trading(model_MG_mpc[MG], export_limit * scale_power / S_base, trading_line_mpc, MG, model_name=model_name, model_da=model_MG_atc[MG])
    create_graph_separate_MG_Q(model_MG_mpc[MG], export_limit * scale_power / S_base, trading_line_mpc, MG, model_name=model_name, model_da=model_MG_atc[MG])

print("--- FULL SIMULATION COMPLETED ---")

import os
if not os.path.exists("Result_data"):
    os.makedirs("Result_data")

conv_all_array = {}
if convergence_all_hours:
    for t_str, history_r in convergence_all_hours.items():
        conv_all_array[t_str] = []
        for key, val in history_r.items():
            conv_all_array[t_str].append({
                "MG": key[0],
                "partner": key[1],
                "time": key[2],
                "step": key[3],
                "r_value": val
            })

metrics = {
    "DayAhead_Total_Time": total_time_da,
    "PerfectForesight_Total_Time": total_time_pf,
    "MPC_Time_Per_Hour": cpu_time_history,
    "MPC_Total_Time": sum(cpu_time_history),
    "MPC_Convergence_All": conv_all_array
}

with open("Result_data/stage4_metrics.json", "w") as f:
    json.dump(metrics, f, indent=4)

# %%
