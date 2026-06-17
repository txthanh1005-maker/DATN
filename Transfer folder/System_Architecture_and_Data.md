# System Architecture and Input Parameters Summary

This document serves as a consolidated reference of the P2P Multi-Microgrid system architecture and input parameters, derived from the `Source_data`, `Line_data`, `Node_PQ_data` folders and `main.py`. This summary provides the necessary physical and topological groundwork for writing **Chapter 2: System Architecture and Parameters** of the graduation thesis.

## 1. Network Topology (Cấu trúc mạng)
The system consists of **1 Main Grid (MG0)** and **4 interconnected Microgrids (MG1, MG2, MG3, MG4)**.
These Microgrids form a Peer-to-Peer (P2P) trading network, allowing power exchange to maintain resilience, especially when isolated from the Main Grid.

* **MG1**: Heavy load MG. Connects to MG3 and MG4.
* **MG2**: Solar-only MG. Connects to MG3 and MG4.
* **MG3**: Light load / Excess generation MG (acts as the primary savior). Connects to MG1, MG2, MG4.
* **MG4**: Heavy load and high PV capacity MG. Connects to MG1, MG2, MG3.

## 2. Microgrid Configurations (Cấu hình nút của từng MG)
The precise component locations within each MG are defined as follows:

### Microgrid 1 (MG1)
- **Total Nodes**: 36
- **Photovoltaic (PV) Nodes**: 3, 10, 12, 14, 26, 36
- **Wind Turbine (WT) Node**: 32
- **Battery Energy Storage System (BESS) Node**: 19
- **Dispatchable Generator (DG) Node**: 5
- **Grid Trading Limits**: $\pm 1.5$ MW (1500 kW / 1.5 pu)

### Microgrid 2 (MG2)
- **Total Nodes**: 30
- **Photovoltaic (PV) Nodes**: 14, 19, 28, 30
- **Wind Turbine (WT) Node**: None
- **Battery Energy Storage System (BESS) Node**: 20
- **Dispatchable Generator (DG) Node**: 10
- **Grid Trading Limits**: $\pm 1.5$ MW (1500 kW / 1.5 pu)

### Microgrid 3 (MG3)
- **Total Nodes**: 21
- **Photovoltaic (PV) Nodes**: 2, 8, 11, 15
- **Wind Turbine (WT) Node**: 1
- **Battery Energy Storage System (BESS) Node**: 12
- **Dispatchable Generator (DG) Node**: 9
- **Grid Trading Limits**: $\pm 1.5$ MW (1500 kW / 1.5 pu)

### Microgrid 4 (MG4) - Heavy Load & High PV
MG4 acts as a dense industrial/residential complex with massive consumption (25 active load nodes) but also heavily relies on distributed solar generation. Its power balance fluctuates aggressively between day and night.
- **Total Nodes**: 35 (25 load nodes defined in `Node_PQ_data`)
- **Photovoltaic (PV) Nodes**: 18, 20, 27, 29 (High PV distribution)
- **Wind Turbine (WT) Node**: None
- **Battery Energy Storage System (BESS) Node**: 8
- **Dispatchable Generator (DG) Node**: 22 (For critical local backup)
- **Grid Trading Limits**: $\pm 1.5$ MW (1500 kW / 1.5 pu)

## 3. Input Data Sources (Nguồn cấp dữ liệu)

The system loads its parameters from physical Excel (`.xlsx`) files. When presenting the tables in Chapter 2, these are the sources of truth:

- **`Source_data/` (Dữ liệu Nguồn phát)**: 
  - Contains generation profiles (24-hour capacity factors) for PV and Wind Turbines.
  - Contains upper/lower generation limits for the Dispatchable Generators (DG) and Grid import/export limits.
  - *Files*: `MG0.xlsx`, `MG1.xlsx`, `MG2.xlsx`, `MG3.xlsx`, `MG4.xlsx`.

- **`Line_data/` (Dữ liệu Đường dây)**: 
  - Contains the resistance ($R$) and reactance ($X$) parameters for all internal distribution lines within each MG.
  - Defines the internal topology (From Node - To Node) of the radial network of each MG.
  - *Files*: `MG1_Line_data.xlsx`, `MG2_Line_data.xlsx`, etc.

- **`Node_PQ_data/` (Dữ liệu Phụ tải)**: 
  - Contains the 24-hour profiles for Active Power Demand ($P_{load}$) and Reactive Power Demand ($Q_{load}$) at every node in the system.
  - *Files*: Separated into subdirectories for `MG1`, `MG2`, `MG3`, `MG4`, containing files like `MG1_Load_data.xlsx`.

- **`Trading_data/` (Dữ liệu Đường liên kết P2P)**: 
  - Contains the capacity limits and impedance of the tie-lines connecting the microgrids together.

## 4. Key Global Parameters
- **Base Power ($S_{base}$)**: 1 MVA (Used for Per-Unit standardization).
- **Time Horizon ($H$)**: 24 hours (Day-ahead) / 5 hours (MPC Rolling Horizon).
- **Export Limit (Lưới chính)**: 5000 kW (Default maximum power drawn from MG0).
- **Fault Configurations (Kịch bản sự cố)**: 
  - Grid Loss (Mất kết nối lưới chính MG0) từ giờ thứ 9 đến 15.
  - PV Loss (Mất công suất điện mặt trời) từ giờ thứ 11 đến 15.
