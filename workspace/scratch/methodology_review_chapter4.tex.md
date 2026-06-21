## Methodology Review Report (Peer Reviewer 1)

### Reviewer Identity
Electrical Engineering & Power Systems Methodology Expert

### Overall Recommendation
Minor Revision

### Confidence Score
5

### Summary Assessment
Chapter 4 establishes the temporal coordination layer via Model Predictive Control (MPC). The 3-Mode Spatiotemporal Coordination framework is highly innovative, effectively bridging Day-Ahead economics with Real-Time resilience. The formulation of Graceful Degradation using hierarchical VOLL penalties and a terminal SOC constraint is mathematically rigorous. The main limitation is the acknowledged "BESS Hoarding Syndrome" stemming from the deterministic formulation of the MPC.

### Strengths (3-5 items)
1. **[3-Mode State Machine]**: The explicit branching into Normal, Emergency, and Recovery modes prevents computational waste during stable periods and appropriately marshals resources during faults.
2. **[Graceful Degradation Formulation]**: Structuring the objective weights such that $C_{shed}^{critical} \gg \beta_{SOC} > C_{shed}^{normal}$ elegantly forces the mathematical solver to autonomously prioritize critical loads and battery preservation without requiring brittle heuristic rules.
3. **[SOC Inheritance Logic]**: The explicit formulation of SOC transition across the rolling horizon (Eq. 4.2) guarantees physical continuity between the successive optimization windows.

### Weaknesses (3-5 items)
1. **[Deterministic Overconfidence]**: The MPC relies on deterministic forecast vectors. Because it does not incorporate stochastic scenarios or probability bounds, it becomes overly conservative (hoarding) during emergencies since it assumes the worst-case continuous fault. The author could consider expanding on why a deterministic MPC was chosen over a Stochastic MPC, perhaps citing computational limits.
2. **[Terminal SOC Penalty Rigidity]**: The strict terminal SOC penalty ($J_{SOC}$) artificially distorts the BESS behavior near the end of the 5-hour horizon, forcing it to hold charge rather than deploying it to save normal loads. The author could consider discussing how an adaptive $\beta_{SOC}$ might mitigate this.
3. **[Horizon Length Justification]**: The prediction horizon is fixed at $h=5$ for emergency mode. The methodology lacks a rigorous justification for this specific length (e.g., why not $h=3$ or $h=8$). The author could consider presenting a brief trade-off analysis between computational time and predictive accuracy.

### Detailed Comments

#### Research Questions & Hypotheses
- The framework brilliantly answers the need for a dynamic, real-time adaptive response mechanism.

#### Research Design
- The coupling of ATC inside the MPC rolling loop is computationally heavy but mathematically exact.

#### Sampling Strategy
- N/A

#### Data Collection
- N/A

#### Analysis Methods
- The control implementation accurately reflects industry standards for MPC: optimizing over horizon $h$ but executing only step 1.

#### Results Presentation
- Flowcharts and timeline diagrams clearly explain the sliding window mechanism.

#### Reproducibility
- The state update rules and penalty assignments are explicitly documented.

#### Methodological Fallacies Detected
- **Confirmation Bias risk**: Using a perfect 5-hour forecast during the simulation might overstate the MPC's performance compared to reality where forecasts degrade rapidly over time.

### Questions for Authors
1. How was the prediction horizon $h=5$ selected? Does increasing it significantly increase the CPU time for the nested ATC loops beyond real-time feasibility?
2. In real-world implementation, forecast vectors ($\mathbf{P}_{PV}$) contain significant error. How sensitive is the Graceful Degradation logic to severe forecasting errors within the 5-hour window?

### Minor Issues
- None.
