
"""
[Semantic Metadata]
- Implements: Module chịu trách nhiệm xây dựng mô hình bài toán, khai báo các biến quyết định và liên kết các ràng buộc.
- Related_to_Paper: Emergency_Sharing_Plan, Literature reivew knowleadge
"""

#! Khai báo thư viện 
from xml.parsers.expat import model

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import sys
import time

import pyomo.environ as pe
import pyomo.opt as po
from pyomo.environ import *
from pyomo.environ import value as py_value, Constraint
from pyomo.core.expr.visitor import identify_variables
from pyomo.environ import Constraint, value as py_value
from pyomo.environ import SolverStatus, TerminationCondition

import Function
from Function import Create_Model_basedata, active_power_Wind_constraints
from Function import Create_Configuration
from Function import Create_Z_line
from Function import Create_Load_data
from Function import create_price_from_grid
from Function import create_PV_para
from Function import create_Wind_para
from Function import create_BESS_DG_para
from Function import create_location_source
from Function import Create_variable
from Function import Build_tree_form
from Function import object_function
from Function import (
    #* System
    hard_constraint_shed_critical,
    limit_shed_to_load,
    active_power_balance_constraints,
    reactive_power_balance_constraints,
    limit_sell_to_grid,
    voltage_balance_contraints,
    slack_bus_constraints,
    voltage_limit_constraints,
    socp_relaxation_constraints,
    lb_limit_current,
    #* RE
    active_power_PV_constraints,
    active_power_Wind_constraints,
    #* DG
    active_power_DG_constraints,
    active_ramp_limit_constraints,
    binary_DG_constraints,
    Cost_on_constraints,
    up_time_constraint,
    down_time_constraint,
    Spinning_reserve_constraints,
    #* BESS
    SOC_limit_constraints,
    maximum_charging_power_constraints,
    maximum_discharging_power_constraints,
    SOC_limit_constraints,
    SOC_temporal_variation_constraints,
    SOC_equal_constraints,
    BESS_I_limit_constraints,
    #* Trading
    create_trading_para,
    create_phat_ADMM,
    Trading_limit_constraints,
    initialize_admm_params
)
from Function_maingrid import (
    Create_Z_line_maingrid,
    Create_Load_data_maingrid,
    object_function_maingrid,
    active_power_balance_constraints_maingrid,
    Create_variable_maingrid,)

#! BUILD MAIN GRID MODEL0
def build_coordinator_model(config,trading_limit,export_limits, stage='Normal'):
    model = pe.ConcreteModel()
    number_of_node = config['number_of_node']
    Create_Model_basedata(model, number_of_node, 0)
    file_path_line = f"./Line_data/MG0_Line_data.xlsx"
    Create_Z_line_maingrid(model, file_path_line)
    Create_Load_data_maingrid(model, number_of_node, 0)
    file_path_source = f"./Source_data/MG0.xlsx"
    create_price_from_grid(model,file_path_source)
    Build_tree_form(number_of_node,model)
    create_location_source(model, config['list_PV'], config['list_Wind'], config['list_BESS'],config['list_DG'])
    
    #* Trading
    file_path_trading = f"./Trading_data/MG0.xlsx"
    create_trading_para(model, file_path_trading)
    create_phat_ADMM(model)
    #! KHAI BÁO BIẾN DÙNG TRONG MODEL
    Create_variable_maingrid(model)
    
    #! OBJECTIVE FUNCTION 
    object_function_maingrid(model,export_limits)
    
    #! CONSTRAINTS
    active_power_balance_constraints_maingrid(model)
    reactive_power_balance_constraints(model)
    voltage_balance_contraints(model)
    # slack_bus_constraints(model)
    voltage_limit_constraints(model, stage)
    socp_relaxation_constraints(model)
    lb_limit_current(model,999)
    
    #* Trading
    Trading_limit_constraints(model,trading_limit,-trading_limit)
    
    if stage == 'Emergency':
        Function.apply_fault(model, time_fault=17, export_limit=export_limits)
            
    return model

#! BUILD MGs MODEL1234
def build_microgrid_model(mg_id, config,trading_limit, export_limit, grid_interaction, fault_config=None, stage='Normal'):
    model = pe.ConcreteModel()
    number_of_node = config['number_of_node']
    number_of_config = 12
    
    #! KHAI BÁO BASEDATA CỦA MODEL
    #* System
    Create_Model_basedata(model, number_of_node, number_of_config)
    file_path_imp = "./Line_data/1pharse_Line Impedence.xlsx"
    Line_config = Create_Configuration(model, file_path_imp)
    file_path_line = f"./Line_data/MG{mg_id}_Line_data.xlsx"
    Create_Z_line(model, file_path_line, Line_config)
    Create_Load_data(model, number_of_node, mg_id)
    Build_tree_form(number_of_node,model)
    file_path_source = f"./Source_data/MG{mg_id}.xlsx"
    create_location_source(model, config['list_PV'], config['list_Wind'], config['list_BESS'],config['list_DG'])
    create_price_from_grid(model, file_path_source)
    
    #* SOURCE
    create_PV_para(model, file_path_source)
    create_Wind_para(model, file_path_source)
    create_BESS_DG_para(model, file_path_source)
    
    #* Trading
    file_path_trading = f"./Trading_data/MG{mg_id}.xlsx"
    create_trading_para(model, file_path_trading)
    create_phat_ADMM(model)
    #! KHAI BÁO BIẾN DÙNG TRONG MODEL
    Create_variable(model)
    
    #! OBJECTIVE FUNCTION 
    object_function(model, export_limit, stage=stage)
    
    #! CONSTRAINTS
    # hard_constraint_shed_critical(model)
    limit_shed_to_load(model)
    active_power_balance_constraints(model)
    reactive_power_balance_constraints(model)
    limit_sell_to_grid(model,5*export_limit* scale_power / S_base*grid_interaction, -export_limit* scale_power / S_base*grid_interaction)
    voltage_balance_contraints(model)
    # slack_bus_constraints(model)
    voltage_limit_constraints(model, stage)
    socp_relaxation_constraints(model)
    lb_limit_current(model, 999)
    
    #* RE
    active_power_PV_constraints(model)
    active_power_Wind_constraints(model)
    
    #* DG 
    active_power_DG_constraints(model)
    binary_DG_constraints(model)
    Cost_on_constraints(model)
    active_ramp_limit_constraints(model)
    Spinning_reserve_constraints(model)
    up_time_constraint(model)
    down_time_constraint(model)
    
    #* BESS
    maximum_charging_power_constraints(model)
    maximum_discharging_power_constraints(model)
    SOC_limit_constraints(model)
    SOC_temporal_variation_constraints(model)
    SOC_equal_constraints(model)
    BESS_I_limit_constraints(model)
    
    #* Trading
    Trading_limit_constraints(model,trading_limit,-trading_limit)
    
    if fault_config is not None:
        Function.apply_custom_fault(model, export_limit=export_limit, config=fault_config)
        
    return model

#! BUILD MGs MODEL1234 FOR MPC
def build_microgrid_model_mpc(mg_id, config, trading_limit, export_limit, grid_interaction, H, SOC_init, SOC_DA_ref, t_start, fault_config=None, stage='Emergency'):
    model = pe.ConcreteModel()
    
    # MPC parameters
    model.H = H
    model.t_start = t_start
    model.SOC_init = SOC_init
    model.SOC_DA_ref = SOC_DA_ref
    
    number_of_node = config['number_of_node']
    number_of_config = 12
    
    #! KHAI BÁO BASEDATA CỦA MODEL
    #* System
    Create_Model_basedata(model, number_of_node, number_of_config)
    file_path_imp = "./Line_data/1pharse_Line Impedence.xlsx"
    Line_config = Create_Configuration(model, file_path_imp)
    file_path_line = f"./Line_data/MG{mg_id}_Line_data.xlsx"
    Create_Z_line(model, file_path_line, Line_config)
    Create_Load_data(model, number_of_node, mg_id)
    Build_tree_form(number_of_node,model)
    file_path_source = f"./Source_data/MG{mg_id}.xlsx"
    create_location_source(model, config['list_PV'], config['list_Wind'], config['list_BESS'],config['list_DG'])
    create_price_from_grid(model, file_path_source)
    
    #* SOURCE
    create_PV_para(model, file_path_source)
    create_Wind_para(model, file_path_source)
    create_BESS_DG_para(model, file_path_source)
    
    #* Trading
    file_path_trading = f"./Trading_data/MG{mg_id}.xlsx"
    create_trading_para(model, file_path_trading)
    create_phat_ADMM(model)
    #! KHAI BÁO BIẾN DÙNG TRONG MODEL
    Create_variable(model)
    
    #! OBJECTIVE FUNCTION 
    object_function(model, export_limit, stage=stage)
    
    #! CONSTRAINTS
    # hard_constraint_shed_critical(model)
    limit_shed_to_load(model)
    active_power_balance_constraints(model)
    reactive_power_balance_constraints(model)
    limit_sell_to_grid(model,5*export_limit* scale_power / S_base*grid_interaction, -export_limit* scale_power / S_base*grid_interaction)
    voltage_balance_contraints(model)
    # slack_bus_constraints(model)
    voltage_limit_constraints(model, stage)
    socp_relaxation_constraints(model)
    lb_limit_current(model, 999)
    
    #* RE
    active_power_PV_constraints(model)
    active_power_Wind_constraints(model)
    
    #* DG 
    active_power_DG_constraints(model)
    binary_DG_constraints(model)
    Cost_on_constraints(model)
    active_ramp_limit_constraints(model)
    Spinning_reserve_constraints(model)
    up_time_constraint(model)
    down_time_constraint(model)
    
    #* BESS
    maximum_charging_power_constraints(model)
    maximum_discharging_power_constraints(model)
    SOC_limit_constraints(model)
    SOC_temporal_variation_constraints(model)
    SOC_equal_constraints(model)
    BESS_I_limit_constraints(model)
    
    #* Trading
    Trading_limit_constraints(model,trading_limit,-trading_limit)
    
    if fault_config is not None:
        Function.apply_custom_fault(model, export_limit=export_limit, config=fault_config)
        
    return model

#! SOLVE MODEL EACH MG
from Function import S_base, solve,scale_power
from Function import print_result, print_active_shedding_nodes
from Function import create_graph_separate_MG_trading
def solve_microgrid_model(mg_id, model, trading_line, export_limit, model_da=None):
    limit = export_limit
    print(f"--- Start solving MG{mg_id} ---")
    solve(model)
    print_result(model, mg_id)
    create_graph_separate_MG_trading(model, limit, trading_line, mg_id, model_da=model_da)
    print_active_shedding_nodes(model, mg_id)
    print(f"--- End solving MG{mg_id} ---\n")
    return

#! BASE_MODEL
def Base_model(mg_configs, trading_limit, export_limit):
    number_of_MG = {1,2,3,4}
    export_limit = export_limit * scale_power / S_base
    trading_line, trading_node = load_trading_network(number_of_MG)
    model_MG = {}
    for MG in number_of_MG:
        model_MG[MG] = build_microgrid_model(MG, mg_configs[MG], trading_limit[MG], export_limit, 1)
        solve_microgrid_model(MG, model_MG[MG], trading_line, export_limit)
    return model_MG, trading_line

#! ACCIDENT_MODEL
def accident_model(mg_configs, trading_limit, export_limit, fault_configs):
    number_of_MG = {1,2,3,4}
    export_limit = export_limit * scale_power / S_base
    trading_line, trading_node = load_trading_network(number_of_MG)
    model_MG = {}
    for MG in number_of_MG:
        model_MG[MG] = build_microgrid_model(MG, mg_configs[MG], trading_limit[MG], export_limit, 1, fault_config=fault_configs.get(MG), stage='Emergency')
        solve_microgrid_model(MG, model_MG[MG], trading_line, export_limit)
    return model_MG, trading_line

#! BUILD GLOBAL TRADING N MGS
from Function import (
    load_trading_network,
    solve,
)
def ATC_Global_model(mg_configs, export_limit, trading_limit):
    number_of_MG = {1, 2, 3, 4}
    consecutive_converged_steps = 0
    export_limit = export_limit * scale_power / S_base
    trading_line, trading_node = load_trading_network(number_of_MG)

    # Khởi tạo mô hình
    model_MG = {}
    for MG in number_of_MG:
        model_MG[MG] = build_microgrid_model(MG, mg_configs[MG], trading_limit[MG], export_limit, 1)

    p_past = {}
    
    # Khởi tạo tham số ATC
    for MG in number_of_MG:
        for node in model_MG[MG].node_has_trade:
            for t in range(24):
                model_MG[MG].lamda_ATC[node, t] = py_value(model_MG[MG].Price_sell[t])
                model_MG[MG].rho_ATC[node, t] = 0.05
                model_MG[MG].P_target[node, t] = 0.0
                p_past[(MG, node, t)] = 0.0

    history_r = {}
    history_s = {}
    history_rho = {}

    fix_value = scale_power / S_base
    
    #! Vòng lặp ATC
    for step in range(200):
        print(f"🔄 [ATC DAY-AHEAD] Iteration {step} / 200")
        is_current_step_converged = True
        
        # 1. Giải từng MG (MG Level)
        p_trade_current = {}
        for MG in number_of_MG:
            results = solve(model_MG[MG])
            # Trích xuất P_trade thực tế (kW)
            for node in model_MG[MG].node_has_trade:
                for t in range(24):
                    p_val = py_value(model_MG[MG].P_trade[node, t])
                    p_trade_current[(MG, node, t)] = p_val if p_val is not None else 0.0
        
        # 2. DSO Level: Tính sai số, mục tiêu P_target, và cập nhật lambda, rho
        for MG in number_of_MG:
            for node in model_MG[MG].node_has_trade:
                if (MG, node) not in trading_line:
                    continue
                for index, j in enumerate(trading_line[MG, node]):
                    node_to = trading_node[MG, node][index]
                    
                    if MG > j: 
                        continue 
                        
                    for t in range(24):
                        # p_trade_current is already in pu
                        p_ij = p_trade_current[(MG, node, t)]
                        p_ji = p_trade_current[(j, node_to, t)]
                        
                        # DSO cấp mục tiêu P_target (vẫn giữ ở hệ pu)
                        p_target_ij = (p_ij - p_ji) / 2
                        p_target_ji = -p_target_ij
                        
                        model_MG[MG].P_target[node, t] = p_target_ij
                        model_MG[j].P_target[node_to, t] = p_target_ji
                        
                        # Mismatch
                        r_local_pu = p_ij + p_ji
                        
                        rho_current = py_value(model_MG[MG].rho_ATC[node, t])
                        lambda_current_ij = py_value(model_MG[MG].lamda_ATC[node, t])
                        lambda_current_ji = py_value(model_MG[j].lamda_ATC[node_to, t])
                        
                        # Cập nhật lambda
                        lambda_new_ij = lambda_current_ij + rho_current * (p_ij - p_target_ij)
                        lambda_new_ji = lambda_current_ji + rho_current * (p_ji - p_target_ji)
                        
                        model_MG[MG].lamda_ATC[node, t] = lambda_new_ij
                        model_MG[j].lamda_ATC[node_to, t] = lambda_new_ji
                        
                        # Tốc độ dao động
                        p_past_ij = p_past[(MG, node, t)]
                        speed_local_pu = rho_current * abs(p_ij - p_past_ij)
                        
                        # Cập nhật Rho
                        r_sq = r_local_pu ** 2
                        s_sq = speed_local_pu ** 2
                        mu = 10
                        tau = 1.5
                        epsilon_stop = 0.001
                        
                        rho_new = rho_current
                        if r_sq > epsilon_stop or s_sq > epsilon_stop:
                            is_current_step_converged = False
                            if r_sq > mu * s_sq:
                                rho_new = rho_current * tau
                            elif s_sq > mu * r_sq:
                                rho_new = rho_current / tau
                            model_MG[MG].rho_ATC[node, t] = rho_new
                            model_MG[j].rho_ATC[node_to, t] = rho_new
                            
                        history_r[(MG, j, t, step)] = r_local_pu
                        history_s[(MG, j, t, step)] = speed_local_pu
                        history_rho[(MG, j, t, step)] = rho_new
                        
                        print(f"Step {step}, trading:({MG},{j}), time {t}: r={r_local_pu:.9f}, s={speed_local_pu:.9f}, rho={rho_new:.4f}, lamda = {lambda_new_ij:.4f},pij = {p_ij:.4f}, pji = {p_ji:.4f}")
                        
        p_past = p_trade_current.copy()
        
        if is_current_step_converged:
            consecutive_converged_steps += 1
            print(f"Step {step}: CONVERGED (Consecutive: {consecutive_converged_steps}/3)")
        else:
            consecutive_converged_steps = 0
            print(f"Step {step}: Not fully converged yet.")

        if consecutive_converged_steps >= 3:
            print(f">>> COMPLETED: Stably converged in {step - 1} steps")
            break

    lamda = {}
    for MG in number_of_MG:
        for node in model_MG[MG].node_has_trade:
            if (MG, node) in trading_line:
                for index, j in enumerate(trading_line[MG, node]):
                    node_to = trading_node[MG, node][index]
                    for t in range(24):
                        lamda[(MG, j, t)] = py_value(model_MG[MG].lamda_ATC[node, t])

    return model_MG, trading_line, history_r, history_s, history_rho, lamda

#! RESULTS
def Result_print(model_MG,export_limit,trading_line):
    for MG in model_MG:
        print_result(model_MG[MG], MG)
        create_graph_separate_MG_trading(model_MG[MG], export_limit * scale_power / S_base, trading_line, MG)
    return

#! MPC model 
def ATC_Global_model_mpc(mg_configs, export_limit, trading_limit, H, SOC_init, SOC_DA_ref, t_start, fault_configs, warm_start_data=None):
    number_of_MG = {1, 2, 3, 4}
    consecutive_converged_steps = 0
    export_limit = export_limit * scale_power / S_base
    trading_line, trading_node = load_trading_network(number_of_MG)

    # Khởi tạo mô hình
    model_MG = {}
    for MG in number_of_MG:
        global_stage = 'Emergency' if fault_configs and any(fault_configs.values()) else 'Normal'
        model_MG[MG] = build_microgrid_model_mpc(MG, mg_configs[MG], trading_limit[MG], export_limit, 1, H, SOC_init.get(MG), SOC_DA_ref.get(MG), t_start, fault_config=fault_configs.get(MG) if fault_configs else None, stage=global_stage)

    p_past = {}
    
    # Khởi tạo tham số ATC
    for MG in number_of_MG:
        for node in model_MG[MG].node_has_trade:
            for t in range(H):
                if warm_start_data and (MG, node, t) in warm_start_data:
                    model_MG[MG].lamda_ATC[node, t] = warm_start_data[(MG, node, t)]['lamda']
                    model_MG[MG].P_target[node, t] = warm_start_data[(MG, node, t)]['P_target']
                    p_past[(MG, node, t)] = warm_start_data[(MG, node, t)]['P_trade']
                    if 'rho' in warm_start_data[(MG, node, t)]:
                        model_MG[MG].rho_ATC[node, t] = warm_start_data[(MG, node, t)]['rho']
                    else:
                        model_MG[MG].rho_ATC[node, t] = 0.05
                else:
                    model_MG[MG].lamda_ATC[node, t] = py_value(model_MG[MG].Price_sell[t])
                    model_MG[MG].P_target[node, t] = 0.0
                    p_past[(MG, node, t)] = 0.0
                    model_MG[MG].rho_ATC[node, t] = 0.05

    history_r = {}
    history_s = {}
    history_rho = {}

    fix_value = scale_power / S_base
    
    #! Vòng lặp ATC
    for step in range(200):
        print(f"🔄 [ATC MPC] Iteration {step} / 200 (Hour {t_start})")
        is_current_step_converged = True
        
        # 1. Giải từng MG (MG Level)
        p_trade_current = {}
        for MG in number_of_MG:
            results = solve(model_MG[MG])
            if results.solver.termination_condition not in (TerminationCondition.optimal, TerminationCondition.feasible):
                from pyomo.util.infeasible import log_infeasible_constraints
                print(f"\n[🚨 CẢNH BÁO KHẨN CẤP] Phát hiện lỗi vô nghiệm (Infeasible) tại MG{MG}!")
                print(f"Trạng thái bộ giải: {results.solver.termination_condition}")
                print(f"Bước chạy ATC: {step}, Giờ bắt đầu MPC: {t_start}")
                print("--- Chi tiết các ràng buộc vi phạm (Infeasible Constraints): ---")
                try:
                    log_infeasible_constraints(model_MG[MG])
                except Exception as e:
                    print(f"Không thể xuất log ràng buộc: {e}")
                print("-----------------------------------------------------------------")
                raise RuntimeError(f"MG{MG} bi vo nghiem (Infeasible) tai buoc ATC {step}, gio MPC {t_start}. Dung mo phong MPC!")
            # Trích xuất P_trade thực tế (kW)
            for node in model_MG[MG].node_has_trade:
                for t in range(H):
                    p_val = py_value(model_MG[MG].P_trade[node, t])
                    p_trade_current[(MG, node, t)] = p_val if p_val is not None else 0.0
        
        # 2. DSO Level: Tính sai số, mục tiêu P_target, và cập nhật lambda, rho
        for MG in number_of_MG:
            for node in model_MG[MG].node_has_trade:
                if (MG, node) not in trading_line:
                    continue
                for index, j in enumerate(trading_line[MG, node]):
                    node_to = trading_node[MG, node][index]
                    
                    if MG > j: 
                        continue 
                        
                    for t in range(H):
                        # p_trade_current is already in pu
                        p_ij = p_trade_current[(MG, node, t)]
                        p_ji = p_trade_current[(j, node_to, t)]
                        
                        # DSO cấp mục tiêu P_target (vẫn giữ ở hệ pu)
                        p_target_ij = (p_ij - p_ji) / 2
                        p_target_ji = -p_target_ij
                        
                        model_MG[MG].P_target[node, t] = p_target_ij
                        model_MG[j].P_target[node_to, t] = p_target_ji
                        
                        # Mismatch
                        r_local_pu = p_ij + p_ji
                        
                        rho_current = py_value(model_MG[MG].rho_ATC[node, t])
                        lambda_current_ij = py_value(model_MG[MG].lamda_ATC[node, t])
                        lambda_current_ji = py_value(model_MG[j].lamda_ATC[node_to, t])
                        
                        # Cập nhật lambda
                        lambda_new_ij = lambda_current_ij + rho_current * (p_ij - p_target_ij)
                        lambda_new_ji = lambda_current_ji + rho_current * (p_ji - p_target_ji)
                        
                        model_MG[MG].lamda_ATC[node, t] = lambda_new_ij
                        model_MG[j].lamda_ATC[node_to, t] = lambda_new_ji
                        
                        # Tốc độ dao động
                        p_past_ij = p_past[(MG, node, t)]
                        speed_local_pu = rho_current * abs(p_ij - p_past_ij)
                        
                        # Cập nhật Rho
                        r_sq = r_local_pu ** 2
                        s_sq = speed_local_pu ** 2
                        mu = 10
                        tau = 1.5
                        epsilon_stop = 1e-4
                        
                        rho_new = rho_current
                        if r_sq > epsilon_stop or s_sq > epsilon_stop:
                            is_current_step_converged = False
                            if r_sq > mu * s_sq:
                                rho_new = rho_current * tau
                            elif s_sq > mu * r_sq:
                                rho_new = rho_current / tau
                            model_MG[MG].rho_ATC[node, t] = rho_new
                            model_MG[j].rho_ATC[node_to, t] = rho_new
                            
                        history_r[(MG, j, t, step)] = r_local_pu
                        history_s[(MG, j, t, step)] = speed_local_pu
                        history_rho[(MG, j, t, step)] = rho_new
                        
                        # print(f"Step {step}, trading:({MG},{j}), time {t}: r={r_local_pu:.9f}, s={speed_local_pu:.9f}, rho={rho_new:.4f}, lamda = {lambda_new_ij:.4f},pij = {p_ij:.4f}, pji = {p_ji:.4f}")
                        
        p_past = p_trade_current.copy()
        
        if is_current_step_converged:
            consecutive_converged_steps += 1
            print(f"Step {step}: CONVERGED (Consecutive: {consecutive_converged_steps}/3)")
        else:
            consecutive_converged_steps = 0
            print(f"Step {step}: Not fully converged yet.")

        if consecutive_converged_steps >= 3:
            print(f">>> COMPLETED: Stably converged in {step - 1} steps")
            break

    lamda = {}
    for MG in number_of_MG:
        for node in model_MG[MG].node_has_trade:
            if (MG, node) in trading_line:
                for index, j in enumerate(trading_line[MG, node]):
                    node_to = trading_node[MG, node][index]
                    for t in range(H):
                        lamda[(MG, j, t)] = py_value(model_MG[MG].lamda_ATC[node, t])

    return model_MG, trading_line, history_r, history_s, history_rho, lamda

def run_MPC_simulation(mg_configs, export_limit, trading_limit_p2p, H, model_MG_atc, fault_configs, perfect_foresight=False, warm_start_data=None):
    number_of_MG = {1, 2, 3, 4}
    
    # 1. Khoi tao final_results clone tu DA
    final_results = {MG: model_MG_atc[MG].clone() for MG in number_of_MG}
    
    # 2. Tao ban sao reference de cap nhat sau Recovery ma khong lam hong DA goc
    current_DA_ref = {MG: model_MG_atc[MG].clone() for MG in number_of_MG}
    
    # Helper to update variables
    def update_model_results(MG, source_model, global_t, source_t=0, target_model=None):
        for var_src in source_model.component_objects(pe.Var, active=True):
            var_name = var_src.name
            if hasattr(target_model, var_name):
                var_target = getattr(target_model, var_name)
                for index in var_src:
                    if isinstance(index, tuple):
                        if index[-1] == source_t:
                            final_index = index[:-1] + (global_t,)
                            try:
                                if final_index in var_target:
                                    var_target[final_index].set_value(py_value(var_src[index]))
                            except Exception:
                                pass
                    else:
                        if index == source_t:
                            final_index = global_t
                            try:
                                if final_index in var_target:
                                    var_target[final_index].set_value(py_value(var_src[index]))
                            except Exception:
                                pass

    def has_fault(t_check):
        for MG, faults in fault_configs.items():
            for fault in faults:
                if fault['start_time'] <= t_check <= fault['end_time']:
                    return True
        return False

    trading_line_final = None

    SOC_init = {}
    for MG in number_of_MG:
        bess_list = list(mg_configs[MG]['list_BESS'])
        if len(bess_list) > 0:
            SOC_init[MG] = 0.5  # Khoi tao mac dinh cho BESS
        else:
            SOC_init[MG] = None

    was_faulty = False
    prev_model_MG_mpc = None
    cpu_time_history = []
    convergence_all_hours = {}

    for t in range(24):
        hour_cpu_time = 0.0
        is_faulty = has_fault(t)
        
        if is_faulty:
            print("\n" + "*"*60)
            print(f"🕒 [MPC HOUR] CHẠY TỐI ƯU CHO GIỜ t = {t} (CHẾ ĐỘ SỰ CỐ) 🕒")
            print("*"*60)
            SOC_DA_ref = {}
            for MG in number_of_MG:
                bess_list = list(mg_configs[MG]['list_BESS'])
                if len(bess_list) > 0:
                    bess_node = bess_list[0]
                    ref_t = min(t + H - 1, 23)
                    SOC_DA_ref[MG] = py_value(current_DA_ref[MG].SOC[bess_node, ref_t])
                else:
                    SOC_DA_ref[MG] = None
                    
            current_fault_configs = {}
            for MG, faults in fault_configs.items():
                current_fault_configs[MG] = []
                for fault in faults:
                    if perfect_foresight:
                        current_fault_configs[MG].append(fault)
                    else:
                        if t >= fault['start_time']:
                            current_fault_configs[MG].append(fault)
                            
            current_warm_start = {}
            for MG in number_of_MG:
                for node in model_MG_atc[MG].node_has_trade:
                    for t_mpc in range(min(H, 24 - t)):
                        global_t = t + t_mpc
                        if not was_faulty:
                            current_warm_start[(MG, node, t_mpc)] = {
                                'lamda': 0.0,
                                'P_target': 0.0,
                                'P_trade': 0.0
                            }
                        else:
                            prev_t_mpc = t_mpc + 1
                            H_prev = min(H, 24 - (t - 1))
                            if prev_model_MG_mpc and prev_t_mpc < H_prev:
                                current_warm_start[(MG, node, t_mpc)] = {
                                    'lamda': py_value(prev_model_MG_mpc[MG].lamda_ATC[node, prev_t_mpc]),
                                    'P_target': py_value(prev_model_MG_mpc[MG].P_target[node, prev_t_mpc]),
                                    'P_trade': py_value(prev_model_MG_mpc[MG].P_trade[node, prev_t_mpc]),
                                    'rho': py_value(prev_model_MG_mpc[MG].rho_ATC[node, prev_t_mpc])
                                }
                            else:
                                if warm_start_data and (MG, node, global_t) in warm_start_data:
                                    current_warm_start[(MG, node, t_mpc)] = warm_start_data[(MG, node, global_t)]
                                else:
                                    current_warm_start[(MG, node, t_mpc)] = {
                                        'lamda': py_value(model_MG_atc[MG].lamda_ATC[node, global_t]),
                                        'P_target': py_value(model_MG_atc[MG].P_target[node, global_t]),
                                        'P_trade': py_value(model_MG_atc[MG].P_trade[node, global_t]),
                                        'rho': py_value(model_MG_atc[MG].rho_ATC[node, global_t])
                                    }

            t_start_mpc = time.time()
            model_MG_mpc, trading_line_mpc, history_r, history_s, history_rho, lamda = ATC_Global_model_mpc(
                mg_configs=mg_configs,
                export_limit=export_limit,
                trading_limit=trading_limit_p2p,
                H=min(H, 24 - t),
                SOC_init=SOC_init,
                SOC_DA_ref=SOC_DA_ref,
                t_start=t,
                fault_configs=current_fault_configs,
                warm_start_data=current_warm_start
            )
            t_end_mpc = time.time()
            hour_cpu_time = t_end_mpc - t_start_mpc
            if history_r:
                convergence_all_hours[str(t)] = history_r
            
            prev_model_MG_mpc = model_MG_mpc

            if trading_line_final is None:
                trading_line_final = trading_line_mpc
            
            for MG in number_of_MG:
                update_model_results(MG, model_MG_mpc[MG], global_t=t, source_t=0, target_model=final_results[MG])
                
                bess_list = list(mg_configs[MG]['list_BESS'])
                if len(bess_list) > 0:
                    bess_node = bess_list[0]
                    SOC_init[MG] = py_value(model_MG_mpc[MG].SOC[bess_node, 0])
                    print(f"MG{MG} Handover SOC after t={t}: {SOC_init[MG]:.4f}")
            was_faulty = True
            
        else: # Normal
            if was_faulty: # Vua phuc hoi
                print("\n" + "*"*60)
                print(f"🕒 [MPC HOUR] CHẠY TỐI ƯU CHO GIỜ t = {t} (CHẾ ĐỘ PHỤC HỒI) 🕒")
                print("*"*60)
                H_rec = 24 - t
                SOC_DA_ref_rec = {}
                for MG in number_of_MG:
                    bess_list = list(mg_configs[MG]['list_BESS'])
                    if len(bess_list) > 0:
                        bess_node = bess_list[0]
                        SOC_DA_ref_rec[MG] = py_value(current_DA_ref[MG].SOC[bess_node, 23])
                    else:
                        SOC_DA_ref_rec[MG] = None
                        
                empty_fault_configs = {MG: [] for MG in number_of_MG}

                current_warm_start_rec = {}
                for MG in number_of_MG:
                    for node in model_MG_atc[MG].node_has_trade:
                        for t_mpc in range(H_rec):
                            global_t = t + t_mpc
                            if warm_start_data and (MG, node, global_t) in warm_start_data:
                                current_warm_start_rec[(MG, node, t_mpc)] = warm_start_data[(MG, node, global_t)]
                            else:
                                current_warm_start_rec[(MG, node, t_mpc)] = {
                                    'lamda': py_value(model_MG_atc[MG].lamda_ATC[node, global_t]),
                                    'P_target': py_value(model_MG_atc[MG].P_target[node, global_t]),
                                    'P_trade': py_value(model_MG_atc[MG].P_trade[node, global_t])
                                }

                t_start_mpc = time.time()
                model_MG_mpc_rec, trading_line_rec, history_r, history_s, history_rho, lamda = ATC_Global_model_mpc(
                    mg_configs=mg_configs,
                    export_limit=export_limit,
                    trading_limit=trading_limit_p2p,
                    H=H_rec,
                    SOC_init=SOC_init,
                    SOC_DA_ref=SOC_DA_ref_rec,
                    t_start=t,
                    fault_configs=empty_fault_configs,
                    warm_start_data=current_warm_start_rec
                )
                t_end_mpc = time.time()
                hour_cpu_time = t_end_mpc - t_start_mpc
                if history_r:
                    convergence_all_hours[str(t)] = history_r
                if trading_line_final is None:
                    trading_line_final = trading_line_rec
                    
                # Update current_DA_ref from t to 23 (lay SOC_DA_ref moi cho cac gio tiep theo)
                for MG in number_of_MG:
                    for t_mpc in range(H_rec):
                        global_t = t + t_mpc
                        update_model_results(MG, model_MG_mpc_rec[MG], global_t=global_t, source_t=t_mpc, target_model=current_DA_ref[MG])
                
                was_faulty = False
                
            # Binh thuong: lay ket qua tu current_DA_ref cho gio t roi ghi vao final_results
            print("\n" + "*"*60)
            print(f"🕒 [MPC HOUR] CHẠY TỐI ƯU CHO GIỜ t = {t} (CHẾ ĐỘ BÌNH THƯỜNG) 🕒")
            print("*"*60)
            for MG in number_of_MG:
                update_model_results(MG, current_DA_ref[MG], global_t=t, source_t=t, target_model=final_results[MG])
                
                bess_list = list(mg_configs[MG]['list_BESS'])
                if len(bess_list) > 0:
                    bess_node = bess_list[0]
                    SOC_init[MG] = py_value(current_DA_ref[MG].SOC[bess_node, t])
        cpu_time_history.append(hour_cpu_time)

    return final_results, trading_line_final, cpu_time_history, convergence_all_hours
