## Methodology Review Report (Peer Reviewer 1)

### Reviewer Identity
Electrical Engineering & Power Systems Methodology Expert

### Overall Recommendation
Minor Revision

### Confidence Score
5

### Summary Assessment
Chapter 2 rigorously details the local AC-OPF problem utilizing the SOCP relaxation. The mathematical modeling of components (BESS, DG, RES) is standard and correct. A major methodological strength is the explicit formulation of robustness against exactness failure during emergency modes via renewable curtailment. However, the reliance on a static binary emergency indicator $\Gamma_E(t)$ oversimplifies fault detection dynamics, and the constant BESS efficiency assumption may introduce estimation bias.

### Strengths (3-5 items)
1. **[Robustness Against Exactness Failure]**: The mechanism preventing the solver from artificially inflating branch currents $I_{ij}^2$ to burn surplus energy during islanding by utilizing zero-cost active power curtailment is a highly sophisticated mathematical safeguard.
2. **[Comprehensive DistFlow Formulation]**: The formulation properly retains all $I^2R$ and $I^2X$ loss components, ensuring extreme physical fidelity for the voltage constraints.
3. **[Emergency Mode Toggle]**: The isolation of fault logic via explicit component forcing ($P_k=0, Q_k=0$) rather than altering grid physical boundaries ensures the structural integrity of the mathematical optimization remains intact.

### Weaknesses (3-5 items)
1. **[Constant BESS Efficiency]**: The model assumes a fixed charging/discharging efficiency $\eta_{BESS}=0.90$. In reality, efficiency is a non-linear function of the charging power and SOC. The author could consider noting this as a modeling limitation to avoid over-simplification bias.
2. **[Deterministic Fault Indicator]**: The emergency indicator $\Gamma_E(t)$ implies perfect, instantaneous fault detection. The author could consider discussing the impact of detection latency on the mathematical formulation.
3. **[Radial Topology Enforcement]**: The DistFlow model and SOCP exactness strictly assume a radial grid ($\Omega(j)$ child nodes). The methodology does not specify what happens if the network is structurally meshed. The author could consider explicitly stating the topological requirement as a strict constraint.

### Detailed Comments

#### Research Questions & Hypotheses
- The mathematical formulation correctly operationalizes the objective of achieving physically accurate economic dispatch.

#### Research Design
- The two-formulation design (Normal vs Emergency) clearly differentiates the objective function shifts (profit vs resilience/VOLL).

#### Sampling Strategy
- N/A

#### Data Collection
- N/A

#### Analysis Methods
- The SOCP relaxation equation ($I_{ij}^2 V_i^2 \ge P_{line}^2 + Q_{line}^2$) is correctly implemented. The logic proving exactness via the loss penalty objective is theoretically sound.
- Step 4a: Effect sizes are not applicable to this deterministic mathematical modeling.

#### Results Presentation
- N/A

#### Reproducibility
- The equations are presented with sufficient clarity to reproduce the OPF model, provided the system parameters are fully disclosed.

#### Methodological Fallacies Detected
- Potential overfitting to radial networks: The SOCP relaxation exactness is only globally guaranteed for radial grids; applying this to a meshed topology without a spanning-tree extraction step would lead to inexact, non-physical solutions.

### Questions for Authors
1. How sensitive is the optimization outcome to the assumption of constant BESS round-trip efficiency?
2. If a fault creates a meshed loop in the microgrid, does the mathematical model fail, or is there a pre-processing step to maintain radiality?

### Minor Issues
- The spinning reserve constraint requires 20% of max capacity; an explanation of why 20% was chosen (empirical vs standard) would strengthen the methodology.
