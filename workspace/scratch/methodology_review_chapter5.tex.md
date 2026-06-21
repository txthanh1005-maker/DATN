## Methodology Review Report (Peer Reviewer 1)

### Reviewer Identity
Electrical Engineering & Power Systems Methodology Expert

### Overall Recommendation
Minor Revision

### Confidence Score
5

### Summary Assessment
Chapter 5 presents an outstanding, rigorously validated analysis of the proposed framework. The 3D Evaluation Framework (Horizontal, Vertical, Boundary) provides deep methodological scrutiny. The mathematical extraction of the Tie-line Congestion Paradox and the Voltage Paradox perfectly validates the necessity of the AC-OPF SOCP formulation. However, the simulation relies on a highly specific synthetic testbed, and reproducibility is hindered by the absence of open data access.

### Strengths (3-5 items)
1. **[Validation of the Voltage Paradox]**: Demonstrating that massive active power wheeling through MG4 induces extreme $I^2X$ reactive losses, forcing proactive active power shedding to prevent voltage collapse, is a phenomenal physical insight that validates the entire AC-OPF requirement.
2. **[Proof of Tie-line Congestion Paradox]**: The mathematical explanation utilizing KKT optimality conditions to show how transmission capacity constraints uncouple the ATC consensus price ($\lambda$) from localized VOLL spikes highlights a deep understanding of optimization theory.
3. **[3D Stress Matrix]**: Testing the framework not just against baseline models (PF, Base Fault) but against spatiotemporal extremes (3-MG Long fault) proves the robustness of the Graceful Degradation mechanism.

### Weaknesses (3-5 items)
1. **[Lack of Reproducible Datasets]**: The specific load profiles, PV/WT generation curves, and precise line impedance matrices for the 122 combined nodes are not provided in the chapter or an appendix. The author must consider providing a link to a GitHub repository or data appendix to allow other researchers to replicate these specific paradoxes.
2. **[Omission of Primary Control Dynamics]**: The simulation steps are 1-hour intervals. While valid for tertiary scheduling, this entirely masks the millisecond-level transient stability issues caused by massive tie-line power swings. The author could consider explicitly defining this as an out-of-scope assumption to prevent ecological fallacies regarding real-time stability.
3. **[Generalizability of Paradoxes]**: The observed paradoxes heavily depend on the specific $R/X$ ratio of the simulated networks. The author could consider adding a sensitivity analysis varying the line $R/X$ parameters to prove these phenomena are general to distribution grids and not testbed-specific artifacts.

### Detailed Comments

#### Research Questions & Hypotheses
- The results conclusively prove that the framework can securely manage extreme grid events.

#### Research Design
- The comparison against Perfect Foresight (PF) and isolated Base Fault provides perfect theoretical upper and lower bounds for evaluation.

#### Sampling Strategy
- The testbed (combining 36, 30, 21, and 35 node networks) provides sufficient topological complexity to test multi-path congestion.

#### Data Collection
- Source data for generation/load profiles is abstractly mentioned but not explicitly sourced.

#### Analysis Methods
- Step 4a: Effect sizes / statistical bounds do not apply directly to this deterministic optimization analysis, but the optimality gap (1.69%) is correctly reported.

#### Results Presentation
- Figures excellently capture the dynamic pricing, voltage envelopes, and CPU time convergence.

#### Reproducibility
- Critical gap: Without the explicit mathematical matrices of the testbed or source code, independent verification is impossible.

#### Methodological Fallacies Detected
- **Ecological Fallacy Risk**: Inferring that the system is completely "resilient" based on 1-hour macroscopic scheduling without proving it can survive the physical transient shocks of the $t=9$ blackout.

### Questions for Authors
1. Can you provide the exact line impedance configurations and the generation/load datasets to facilitate replication?
2. Have you verified whether the massive spatial power flows commanded by the MPC at the 1-hour level can be stably executed by the underlying droop/primary inverters without triggering frequency trips?

### Minor Issues
- None.
