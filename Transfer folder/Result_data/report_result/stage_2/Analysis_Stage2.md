7# Stage 2 Analysis: Temporal Dynamics of SOC and Emergency P2P Trading

## 1. Introduction
This analysis evaluates the temporal dynamics of the State of Charge (SOC) and Peer-to-Peer (P2P) trading behaviors across four interconnected microgrids (MG1, MG2, MG3, MG4) during a 24-hour operation cycle. We specifically focus on the critical fault window from **t=9 to t=15**, comparing two operational strategies:
- **MPC (Current Method):** A rolling-horizon Model Predictive Control approach that reacts to conditions as they unfold.
- **Perfect Foresight Model:** An optimization approach with complete advance knowledge of the day's generation, load profiles, and the impending fault over a full 24-hour horizon.

*Note on Initial and Boundary Conditions:* To ensure strict analytical fairness, both models are constrained to start at the exact same physical baseline parameter (`ini_BESS`) at $t=0$ and are mathematically enforced to return to this exact value at the end of the dispatch cycle ($t=24$). This cyclic constraint ($SOC[24] = SOC[0]$) guarantees that no method artificially deflates its operational costs by permanently depleting the storage reserves.

## 2. SOC Dynamics: Proactive vs. Reactive

### 2.1 The Foresight Model (Proactive Pre-charging)
The SOC curves for the Foresight model demonstrate a clear anticipatory strategy while strictly adhering to the 24-hour cyclic boundary condition.
- **Pre-fault Phase (t=0 to 8):** Knowing that a severe fault will occur at t=9, the Foresight model actively charges the Energy Storage Systems (ESS) across the microgrids. The SOC ramps up to near maximum capacity right before the fault strikes.
- **Fault Phase (t=9 to 15):** During the outage, the pre-stored energy is smoothly and heavily discharged to support critical loads, ensuring minimal disruption. 
- **Post-fault Phase (t=16 to 24):** After surviving the fault, the algorithm optimally schedules energy replenishment from the grid or local renewables to strictly satisfy the end-of-day recovery constraint.

### 2.2 The MPC Method (Reactive Response)
In contrast, the current MPC method lacks long-term visibility regarding the unexpected fault.
- **Pre-fault Phase (t=0 to 8):** The SOC follows standard economic dispatch (from the Day-Ahead base model), maintaining normal operating levels without aggressive pre-charging. Both methods visibly originate from the exact same SOC at $t=0$, but the MPC maintains a much flatter profile.
- **Fault Phase (t=9 to 15):** When the fault suddenly isolates or limits the system at t=9, the MGs are caught off-guard with lower initial SOC levels. The batteries drain rapidly. To survive the crisis and prevent massive load shedding, the system is forced to rely heavily on dynamic P2P energy sharing.
- **Post-fault Phase (t=16 to 24):** The MPC must adaptively re-charge its depleted batteries in the final hours, absorbing energy to meet the cyclic boundary requirement.

## 3. P2P Energy Sharing: Victims and Rescuers

During the fault window, the disparate generation and load profiles of the four microgrids necessitate intense cooperation:

- **MG1 & MG2 (The "Victims"):** 
  These microgrids experience severe energy deficits due to the fault. Under the MPC method, their local BESS are insufficient to cover the prolonged outage because they were not pre-charged. They become heavy importers of power, drawing heavily from the P2P network to keep critical loads online.
  
- **MG3 & MG4 (The "Rescuers"):** 
  Equipped with either lower critical loads or higher renewable generation at the time, MG3 and MG4 act as lifelines. The P2P mechanism enables them to dynamically route their surplus power to MG1 and MG2. Under MPC, this emergency sharing is visually pronounced, characterized by massive spikes in exchange power and highly volatile internal pricing ($\lambda$) due to the scarcity of power.

## 4. Conclusion
The comparative charts illustrate the fundamental trade-off between the two methods within perfectly fair boundary conditions. The **Foresight model** smooths out the crisis by leveraging the BESS as a temporal buffer (pre-charging), minimizing the need for frantic P2P transfers. The **MPC method**, while caught without adequate SOC reserves at the fault onset, brilliantly showcases the resilience of the interconnected P2P framework—relying on the spatial diversity of the microgrids (rescuers MG3/MG4 supporting victims MG1/MG2) to dynamically manage the crisis and recover its SOC by the end of the day.
