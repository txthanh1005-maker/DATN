# Stage 3 Analysis: AC Physics and System Resilience

## 1. Introduction
This stage validates the physical feasibility of the optimization strategies (Base Fault, Perfect Foresight, and MPC) through the lens of Alternating Current Optimal Power Flow (AC-OPF). Specifically, we analyze the Voltage Profiles, Load Shedding behaviors, and Reactive Power (Q) dynamics across the four microgrids (MG1, MG2, MG3, MG4). The results demonstrate that the theoretical economic dispatch strictly adheres to the physical constraints of the electrical network.

## 2. Voltage Stability (Voltage Profile)
The primary indicator of physical grid stability is the nodal voltage. The voltage constraints strictly require that all node voltages remain within the permissible bounds of **0.95 p.u.** and **1.05 p.u.** at all times.
- **Normal Operation:** During the pre-fault (t=0 to 8) and post-fault (t=16 to 24) phases, the voltage profiles for all nodes in every microgrid exhibit minimal deviation from the nominal 1.0 p.u. level.
- **Fault Window (t=9 to 15):** Even under severe active power deficits during the cascading fault (loss of grid and PV), the optimization algorithm correctly dispatches local Reactive Power (Q) resources to maintain voltage limits. The Voltage Swing envelopes for all nodes tightly remain within the safe region, never violating the 0.95 p.u. lower bound or 1.05 p.u. upper bound. This confirms that the P2P power sharing does not trigger localized voltage collapse.

## 3. Load Shedding Dynamics
A critical mandate of the Emergency Sharing Plan is the absolute protection of critical loads. 
- **100% Critical Load Protected:** Across all four microgrids, the $P_{shed\_critical}$ component (represented by the black bar in the Load Shedding charts) is identically **zero** at every hour. No critical load is ever sacrificed.
- **Normal Load Shedding:** During the fault window (t=9 to 15), MG1 and MG2 (the primary victims) are forced to shed a portion of their normal loads ($P_{shed\_normal}$, orange bars) due to capacity limits. The MPC method effectively minimizes this shedding compared to the Base Fault scenario by actively drawing on P2P trading support from the rescuer microgrids (MG3 and MG4). MG3 and MG4 exhibit zero or near-zero load shedding, proving they have sufficient local reserves to sustain themselves while exporting power.

## 4. Reactive Power (Q) Management
The AC-OPF formulation ensures that Active Power (P) transactions are supported by adequate Reactive Power (Q) injections.
- Reactive power is balanced locally within each microgrid to support nodal voltages.
- The dispatch of Diesel Generators (DG) and Grid import/export dynamically adjusts Q output to compensate for the line losses and voltage drops caused by heavy P2P power transfers during the fault.

## 5. Conclusion
The AC Physics analysis conclusively proves that the proposed P2P energy trading mechanism is not only economically optimal but also physically secure. The strict adherence to voltage limits and the successful protection of all critical loads validate the robustness of the underlying mathematical model in real-world, dynamic fault scenarios.
