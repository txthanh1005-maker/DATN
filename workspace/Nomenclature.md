# Nomenclature

## 1. Sets & Indices
| Mathematical Symbol | Code Variable | Description |
| :--- | :--- | :--- |
| $t \in \mathcal{T}$ | `model.time` | Set of time intervals (hours) in the scheduling horizon. |
| $i, j \in \mathcal{N}$ | `model.index_of_node` | Set of buses/nodes in the network. |
| $c \in \mathcal{C}$ | `model.index_of_Configuration`| Set of line configurations. |
| $(i,j) \in \mathcal{E}$ | `model.node_links` | Set of distribution lines (branches) connecting nodes $i$ and $j$. |
| $i \in \mathcal{N}^{PV}$ | `model.node_has_PV` | Set of nodes equipped with PV systems. |
| $i \in \mathcal{N}^{WT}$ | `model.node_has_Wind` | Set of nodes equipped with Wind Turbine (WT) systems. |
| $i \in \mathcal{N}^{DG}$ | `model.node_has_DG` | Set of nodes equipped with Diesel Generators (DG). |
| $i \in \mathcal{N}^{BESS}$| `model.node_has_BESS` | Set of nodes equipped with Battery Energy Storage Systems (BESS).|
| $i \in \mathcal{N}^{trade}$| `model.node_has_trade`| Set of nodes with tie-lines for P2P trading with other MGs. |
| $j \in \Omega(i)$ | `model.child_of` | Set of child nodes connected to node $i$. |
| $m \in \mathcal{M}$ | `MG` | Set of Microgrids. |

## 2. Parameters
| Mathematical Symbol | Code Variable | Description |
| :--- | :--- | :--- |
| $S_{base}$ | `S_base` | System base apparent power (VA). |
| $U_{base}$ | `U_base` | System base voltage (V). |
| $Z_{base}$ | `Z_base` | System base impedance ($\Omega$). |
| $I_{base}$ | `I_base` | System base current (A). |
| $R_{ij}$ | `model.R_line` | Resistance of line connected to node $j$. |
| $X_{ij}$ | `model.X_line` | Reactance of line connected to node $j$. |
| $C_{ij}$ | `model.C_line` | Capacitance of line connected to node $j$. |
| $P_{load,i,t}$ | `model.p_node` | Active power demand at node $i$, time $t$. |
| $Q_{load,i,t}$ | `model.q_node` | Reactive power demand at node $i$, time $t$. |
| $\pi_{buy,t}$ | `model.Price_buy` | Electricity price for purchasing from the main grid at time $t$. |
| $\pi_{sell,t}$ | `model.Price_sell` | Electricity price for selling to the main grid at time $t$. |
| $P_{PV,i,t}^{peak}$ | `model.P_PV_peak` | Maximum active power generation of PV at node $i$, time $t$. |
| $Q_{PV,i,t}$ | `model.Q_PV` | Reactive power output limit of PV at node $i$, time $t$. |
| $S_{PV,i,t}$ | `model.S_PV` | Apparent power capacity of PV at node $i$, time $t$. |
| $P_{WT,i,t}^{peak}$ | `model.P_Wind_peak` | Maximum active power generation of WT at node $i$, time $t$. |
| $Q_{WT,i,t}$ | `model.Q_Wind` | Reactive power output limit of WT at node $i$, time $t$. |
| $S_{WT,i,t}$ | `model.S_Wind` | Apparent power capacity of WT at node $i$, time $t$. |
| $\pi_{trade,t}$ | `model.trading_cost`| Trading cost/price between MGs at time $t$. |
| $\lambda_{i,t}$ | `model.lamda_ATC` | Lagrange multiplier for active power trading at node $i$, time $t$. |
| $\rho_{i,t}$ | `model.rho_ATC` | Penalty parameter (ADMM) for active power trading at node $i$, time $t$. |
| $P_{target,i,t}$ | `model.P_target` | Target active power trading amount provided by DSO at node $i$, time $t$. |
| $\alpha_{DG}$ | `model.alpha_DG` | Fixed cost coefficient of DG. |
| $\beta_{DG}$ | `model.beta_DG` | Linear cost coefficient of DG. |
| $\gamma_{DG}$ | `model.theta_DG` | Quadratic cost coefficient of DG. |
| $\kappa_{DG}$ | `model.keta_DG` | Linear Operation and Maintenance (O&M) cost coefficient of DG. |
| $C_{start,DG}$ | `model.Cold_start_cost_DG`| Cold start cost of DG. |
| $P_{DG}^{min}, P_{DG}^{max}$| `model.P_Qmin_DG`, `model.P_Qmax_DG` | Minimum and maximum active power output of DG. |
| $Q_{DG}^{min}, Q_{DG}^{max}$| `model.Q_min_DG`, `model.Q_max_DG` | Minimum and maximum reactive power output of DG. |
| $R_{DG}$ | `model.Ramp_rate_DG`| Ramp rate limit of DG. |
| $T_{up}^{DG}, T_{down}^{DG}$ | `model.Time_up_DG`, `model.Time_down_DG`| Minimum up and down time of DG. |
| $C_{BESS}$ | `model.Theta_BESS` | Degradation cost coefficient of BESS. |
| $\eta_{BESS}$ | `model.Eff_BESS` | Charging/discharging efficiency of BESS. |
| $P_{BESS}^{max}$ | `model.P_BESS_max_BESS` | Maximum charging/discharging power of BESS. |
| $SOC^{min}, SOC^{max}$ | `model.SOC_min_BESS`, `model.SOC_max_BESS` | Minimum and maximum State of Charge (SOC) limits of BESS. |
| $SOC^{ini}$ | `model.SOC_ini_BESS`| Initial State of Charge of BESS. |
| $E_{BESS}$ | `model.Capacity_BESS` | Energy capacity of BESS. |
| $\omega_{loss}$ | `model.omega_loss` | Penalty coefficient for distribution network power losses. |
| $C_{shed}^{normal}$ | `model.C_shed_normal` | Penalty cost (VOLL) for normal load shedding. |
| $C_{shed}^{critical}$ | `model.C_shed_critical` | Penalty cost (VOLL) for critical load shedding. |
| $\beta_{SOC}$ | `model.beta_SOC` | Penalty coefficient for SOC deviation in MPC. |

## 3. Decision Variables
| Mathematical Symbol | Code Variable | Description |
| :--- | :--- | :--- |
| $P_{line,ij,t}$ | `model.P_line` | Active power flow on line connected to node $j$ at time $t$. |
| $Q_{line,ij,t}$ | `model.Q_line` | Reactive power flow on line connected to node $j$ at time $t$. |
| $V_{i,t}^2$ | `model.U_node` | Squared voltage magnitude at node $i$, time $t$. |
| $I_{ij,t}^2$ | `model.I_line` | Squared current magnitude on line connected to node $j$ at time $t$. |
| $P_{PV,i,t}$ | `model.P_PV` | Actual active power generation of PV at node $i$, time $t$. |
| $Q_{PV,i,t}^{var}$ | `model.Q_PV_var` | Actual reactive power output of PV at node $i$, time $t$. |
| $P_{WT,i,t}$ | `model.P_Wind` | Actual active power generation of WT at node $i$, time $t$. |
| $Q_{WT,i,t}^{var}$ | `model.Q_Wind_var`| Actual reactive power output of WT at node $i$, time $t$. |
| $P_{DG,i,t}$ | `model.P_DG` | Active power generation of DG at node $i$, time $t$. |
| $Q_{DG,i,t}$ | `model.Q_DG` | Reactive power generation of DG at node $i$, time $t$. |
| $u_{DG,i,t}$ | `model.I_DG` | Binary status (1 if ON, 0 if OFF) of DG at node $i$, time $t$. |
| $v_{DG,i,t}$ | `model.On_cost_DG`| Startup binary variable of DG at node $i$, time $t$. |
| $R_{DG,t}$ | `model.R_DG` | Spinning reserve of DG at time $t$. |
| $P_{ch,i,t}$ | `model.PC_BESS` | Charging power of BESS at node $i$, time $t$. |
| $P_{dis,i,t}$ | `model.PD_BESS` | Discharging power of BESS at node $i$, time $t$. |
| $SOC_{i,t}$ | `model.SOC` | State of Charge of BESS at node $i$, time $t$. |
| $u_{ch,i,t}$ | `model.IC_BESS` | Binary status indicating charging mode of BESS at node $i$, time $t$. |
| $u_{dis,i,t}$ | `model.ID_BESS` | Binary status indicating discharging mode of BESS at node $i$, time $t$. |
| $P_{shed,i,t}$ | `model.P_shed` | Total active power load shedding at node $i$, time $t$. |
| $P_{shed,i,t}^{normal}$ | `model.P_shed_normal`| Normal load shedding at node $i$, time $t$. |
| $P_{shed,i,t}^{critical}$ | `model.P_shed_critical`| Critical load shedding at node $i$, time $t$. |
| $P_{tie,i,t}$ | `model.P_trade` | Active power traded via tie-lines with other MGs at node $i$, time $t$. |
| $P_{grid,t}^{buy}$ | `model.P_pos` | Active power purchased from the main grid at time $t$. |
| $P_{grid,t}^{sell}$ | `model.P_neg` | Active power sold to the main grid at time $t$ (non-positive value). |
| $P_{grid,t}^{paid}$ | `model.P_neg_paid`| Amount of active power sold to the grid that is compensated. |
| $P_{grid,t}^{free}$ | `model.P_neg_free`| Amount of active power sold to the grid beyond the limit (uncompensated). |
| $s_{SOC,i}$ | `model.SOC_slack`| Slack variable for the end-of-horizon SOC penalty in MPC. |
