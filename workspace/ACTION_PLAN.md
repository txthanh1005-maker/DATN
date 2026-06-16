# Implementation Plan: Upgrade DATN Report to ATC & MPC Framework

## Overview
Update the LaTeX graduation thesis report (`DATN.tex`) to replace the obsolete ADMM/SOCP algorithm with the new ATC and MPC architecture, utilizing a 4-MG P2P topology. This plan strictly follows the 3-Layer structure defined in `workspace/Model & Algorithmlogic.md`.

## Architecture Decisions
- **4-Layer Compilation:** Compile LaTeX using `pdflatex` -> `bibtex` -> `pdflatex` -> `pdflatex`.
- **Equation numbering:** Use standard `equation` and `subequations` for math.
- **Validation:** Every equation must match the logic in `main.py` and `build_model.py`. All data for Chapter 5 must be extracted from `Result_data` folders.

## Task List

### Phase 1: Foundation (Chapter 2 - System Architecture)
#### [>] Task 1.2.1: Write Section 2.1 - Cấu trúc liên kết P2P
**Description:** Write the Network Topology describing the 4 Microgrids + MG0 topology.
**Acceptance criteria:**
- [ ] Explicitly describe MG1 (heavy load), MG2 (solar only), MG3 (savior), and MG4 (heavy load + high PV).
**Verification:**
- [ ] 4-layer compile succeeds.
- [ ] Peer Agent Review: `@domain_reviewer` cross-checks with `System_Architecture_and_Data.md`.
**Dependencies:** None
**Files likely touched:** `chapter2.tex`

#### [ ] Task 1.2.2: Write Section 2.2 - Các phần tử năng lượng
**Description:** Write the governing equations for Nguồn tái tạo (PV/WT), Tải, Hệ thống lưu trữ (BESS), và Nguồn dự phòng (DG).
**Acceptance criteria:**
- [ ] Equations for components are numbered.
**Verification:**
- [ ] 4-layer compile succeeds.
**Dependencies:** Task 1.2.1
**Files likely touched:** `chapter2.tex`

#### [ ] Task 1.2.3: Write Section 2.3 - Tham số hệ thống
**Description:** Specify the input data parameters (Excel sources, Base Power 1MVA, VOLL, capacities, limits).
**Acceptance criteria:**
- [ ] Parameters exactly match `System_Architecture_and_Data.md`.
**Verification:**
- [ ] 4-layer compile succeeds.
**Dependencies:** Task 1.2.2
**Files likely touched:** `chapter2.tex`

### Checkpoint: Chapter 2 Complete
- [ ] PDF compiles without errors and Chapter 2 is complete.

### Phase 2: Core Model (Chapter 3 - AC-OPF & ATC)
#### Task 2.3.1: Write Section 3.1 - Bài toán AC-OPF gốc
**Description:** Write the foundational non-linear power flow equations.
**Acceptance criteria:**
- [ ] AC-OPF equations use `equation`/`subequations`.
**Verification:**
- [ ] `@domain_reviewer` validates math accuracy against Python code.
**Dependencies:** Phase 1
**Files likely touched:** `chapter3.tex`

#### Task 2.3.2: Write Section 3.2 - SOCP Relaxation
**Description:** Write the mathematical proof of SOCP relaxation transforming AC-OPF into a convex problem.
**Acceptance criteria:**
- [ ] Equations map strictly to `build_model.py`.
**Verification:**
- [ ] `@domain_reviewer` validates math accuracy.
**Dependencies:** Task 2.3.1
**Files likely touched:** `chapter3.tex`

#### Task 2.3.3: Write Section 3.3 - Thuật toán ATC (Analytical Target Cascading)
**Description:** Document the decentralized optimization mechanism (Coordinator problem, Local problems, Exchange variables P, Q, \lambda, Convergence criteria).
**Acceptance criteria:**
- [ ] Clearly define target and response variables ($P, Q, \lambda$).
- [ ] Provide convergence threshold logic.
**Verification:**
- [ ] `@test-engineer` validates against `main.py`.
- [ ] 4-layer compile succeeds.
**Dependencies:** Task 2.3.2
**Files likely touched:** `chapter3.tex`

### Checkpoint: Chapter 3 Complete
- [ ] PDF compiles without errors. Mathematical core is robust.

### Phase 3: Control Strategy (Chapter 4 - MPC)
#### Task 3.4.1: Write Section 4.1 - Khái niệm Rolling Horizon trong MPC
**Description:** Detail the MPC time-shifting logic and state updates (SOC, forecasts).
**Acceptance criteria:**
- [ ] Explain time-step updates for 5-hour horizon.
**Verification:**
- [ ] 4-layer compile succeeds.
**Dependencies:** Phase 2
**Files likely touched:** `chapter4.tex`

#### Task 3.4.2: Write Section 4.2 - Tích hợp MPC và ATC
**Description:** Detail the outer (MPC) / inner (ATC) loop flow (flowchart/diagram logic).
**Acceptance criteria:**
- [ ] Clear structural relationship established.
**Verification:**
- [ ] `@test-engineer` logic check.
- [ ] 4-layer compile succeeds.
**Dependencies:** Task 3.4.1
**Files likely touched:** `chapter4.tex`

#### Task 3.4.3: Write Section 4.3 - Cơ chế kích hoạt khẩn cấp (Emergency Mode)
**Description:** Write the mathematical conditions for grid fault reconfigurations (N-2, Islanding).
**Acceptance criteria:**
- [ ] Detail N-2 or islanding structural shifts based on fault scenarios.
**Verification:**
- [ ] 4-layer compile succeeds.
**Dependencies:** Task 3.4.2
**Files likely touched:** `chapter4.tex`

### Checkpoint: Chapter 4 Complete
- [ ] Control strategy is fully documented.

### Phase 4: Results (Chapter 5)
#### Task 4.5.1: Stage 1 & 2 (Macro Economics & Resilience)
**Description:** Write results based on `Result_data/report_result/stage_1` and `stage_2`.
**Acceptance criteria:**
- [ ] Extract and format charts/tables correctly with `MW/MWh` units.
**Verification:**
- [ ] 4-layer compile succeeds.
**Dependencies:** Phase 3
**Files likely touched:** `chapter5.tex`

#### Task 4.5.2: Stage 3 (100% Critical Load Protected)
**Description:** Write Node-Level Load Shedding resolution analysis.
**Acceptance criteria:**
- [ ] Explain negative premium and protected loads using charts.
**Verification:**
- [ ] 4-layer compile succeeds.
**Dependencies:** Task 4.5.1
**Files likely touched:** `chapter5.tex`

#### Task 4.5.3: Stage 4 (Algorithmic Scalability)
**Description:** Write analysis on CPU metrics and ATC convergence.
**Acceptance criteria:**
- [ ] Incorporate CPU time ($\sim 91s$) and residual plots.
**Verification:**
- [ ] 4-layer compile succeeds.
**Dependencies:** Task 4.5.2
**Files likely touched:** `chapter5.tex`

#### Task 4.5.4: Stage 5 (ATC Scarcity Pricing \lambda)
**Description:** Analyze the 5 tie-line price signals.
**Acceptance criteria:**
- [ ] Include Scarcity Pricing $\lambda$ graphs and market signals logic.
**Verification:**
- [ ] `@test-engineer` visual review of PDF.
- [ ] 4-layer compile succeeds.
**Dependencies:** Task 4.5.3
**Files likely touched:** `chapter5.tex`

### Phase 5: Polish & Literature (Chapter 1)
#### Task 5.1.1: Audit Literature
**Description:** Propose ADMM paper removals from `references.bib`.
**Acceptance criteria:**
- [ ] Present list to user. Await approval.
**Verification:**
- [ ] Human (Tư lệnh) review.
**Dependencies:** None
**Files likely touched:** `references.bib`

#### Task 5.1.2: Rewrite Chapter 1
**Description:** Write Introduction and ATC/MPC literature background.
**Acceptance criteria:**
- [ ] Clean integration of new `.bib` citations without outdated logic.
**Verification:**
- [ ] Final 4-layer compile without any errors.
**Dependencies:** Task 5.1.1
**Files likely touched:** `chapter1.tex`
