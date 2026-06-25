# Thesis Information

**English Title:** RESILIENCE-ORIENTED PEER-TO-PEER ENERGY TRADING IN MULTI-MICROGRIDS VIA NETWORK-CONSTRAINED DISTRIBUTED PREDICTIVE CONTROL

**Vietnamese Title:** GIAO DỊCH NĂNG LƯỢNG NGANG HÀNG ĐỊNH HƯỚNG ĐỘ PHỤC HỒI TRONG ĐA LƯỚI ĐIỆN VI MÔ THÔNG QUA ĐIỀU KHIỂN DỰ BÁO PHÂN TÁN CÓ RÀNG BUỘC MẠNG

## General Description

This thesis proposes a Tri-layer Cooperative Resilience Architecture for Multi-Microgrid (MMG) networks, aiming to transform Peer-to-Peer (P2P) energy trading from a purely economic construct into a robust, self-healing grid resilience backbone. 

### Problem Statement
The integration of distributed energy resources (DERs) and the shift towards P2P trading in interconnected microgrids face severe limitations because existing approaches treat physical grid limits, distributed coordination, and real-time dynamics in isolation:
1. **Neglect of Exact Physics:** Simplified linear power flow models (e.g., DC-OPF, LinDistFlow) fail to capture the strong active-reactive power coupling (P-Q-V) in radial distribution networks with high R/X ratios. This leads to severe voltage drops and grid collapse during aggressive energy trading or emergency islanding.
2. **Privacy and Structural Vulnerabilities:** Centralized Energy Management Systems pose data privacy risks and act as a single point of failure during extreme weather events. Conversely, standard flat distributed algorithms (such as ADMM) suffer from structural gradient conflicts and diverge when applied to complex, non-linear hierarchical AC-OPF problems.
3. **Static Operational Rigidity:** Traditional Day-Ahead static scheduling operates as an open-loop system. It cannot dynamically adapt to sudden contingencies (such as unexpected outages or main grid disconnections), causing the system to breach dispatch bounds and trigger cascading failures. 

### Methodology
To address these challenges, the thesis develops a unified operational framework integrating three critical methodological layers:
1. **Physical Layer (AC-OPF via SOCP Relaxation):** The network's physical power flow is formulated using the exact non-linear Branch Flow Model (DistFlow) to capture voltage magnitude limits, branch losses, and reactive power. To ensure mathematical convexity and computational tractability without sacrificing physical fidelity, a Second-Order Cone Programming (SOCP) relaxation is applied. P2P markets are strictly limited to trading active power, while distributed generators autonomously provide local reactive power support to guarantee voltage stability.
2. **Distributed Coordination Layer (Analytical Target Cascading - ATC):** To preserve prosumer data privacy and eliminate centralized points of failure, a hierarchical distributed coordination mechanism is constructed using ATC. The Distribution System Operator (DSO) sets boundary target variables, and each microgrid autonomously solves its local SOCP problem using an Augmented Lagrangian penalty function. This target-response iterative process securely decouples the optimization, clearing P2P energy trades via limited boundary variable exchanges and dynamically scaled multipliers to ensure fast convergence.
3. **Dynamic Adaptation Layer (Model Predictive Control - MPC):** To protect the network from unforeseen real-time disturbances, the architecture incorporates a rolling-horizon MPC. Operating as a three-mode state machine (Normal, Emergency, Recovery), the MPC continuously updates system states (e.g., battery State of Charge) and forecasting data. During an emergency, the MPC integrates with the distributed ATC to execute multi-period predictive dispatch. By coupling a strictly weighted Value of Lost Load (VOLL) penalty with battery energy penalties, the system proactively executes "Graceful Degradation"—curtailing low-priority loads early to conserve battery reserves, thereby mathematically guaranteeing the uninterrupted survival of critical infrastructure through prolonged faults.
