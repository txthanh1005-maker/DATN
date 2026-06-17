# Implementation Plan: Upgrade DATN Report to ATC & MPC Framework

## Overview
Update the LaTeX graduation thesis report (`DATN.tex`) to replace the obsolete ADMM/SOCP algorithm with the new ATC and MPC architecture, utilizing a 4-MG P2P topology. This plan strictly follows the 3-Layer structure defined in `workspace/Model & Algorithmlogic.md`.

## Architecture Decisions
- **4-Layer Compilation:** Compile LaTeX using `pdflatex` -> `bibtex` -> `pdflatex` -> `pdflatex`.
- **Equation numbering:** Use standard `equation` and `subequations` for math.
- **Validation:** Every equation must match the logic in `main.py` and `build_model.py`. All data for Chapter 5 must be extracted from `Result_data` folders.

## Task List

### Phase 0: Setup & Standardizations
#### [x] Task 0.1: Setup Abbreviations Dictionary
**Description:** Initialize `workspace/Abbreviations.md` and set up the corresponding Danh mục chữ viết tắt (List of Abbreviations) structure in LaTeX (`DATN.tex`).
**Acceptance criteria:**
- [ ] `Abbreviations.md` contains key domain terms (ATC, MPC, SOCP, MG, PV, WT, BESS, DG...).
- [ ] LaTeX document has a clear table/list for abbreviations.
**Verification:**
- [ ] LaTeX compiles successfully.
**Dependencies:** None
**Files likely touched:** `workspace/Abbreviations.md`, `DATN.tex`

### Phase 1: Foundation (Chapter 3 - System Architecture & Mathematical Formulation)
#### [x] Task 1.2.1: Write Section 3.1 - Cấu trúc liên kết P2P
**Description:** Write the Network Topology describing the 4 Microgrids + MG0 topology.
**Acceptance criteria:**
- [ ] Explicitly describe MG1 (heavy load), MG2 (solar only), MG3 (savior), and MG4 (heavy load + high PV).
**Verification:**
- [ ] 4-layer compile succeeds.
- [ ] Peer Agent Review: `@domain_reviewer` cross-checks with `System_Architecture_and_Data.md`.
**Dependencies:** None
**Files likely touched:** `chapter3.tex`

#### [x] Task 1.2.2: Write Section 3.2 - Mô hình hóa các phần tử năng lượng
**Description:** Write the governing equations for Nguồn tái tạo (PV/WT), Tải, Hệ thống lưu trữ (BESS), và Nguồn dự phòng (DG).
**Acceptance criteria:**
- [ ] Equations for components are numbered.
**Verification:**
- [ ] 4-layer compile succeeds.
**Dependencies:** Task 1.2.1
**Files likely touched:** `chapter3.tex`

#### [x] Task 1.2.3: Extract Nomenclature (Bảng ký hiệu)
**Description:** Review `main.py`, `build_model.py`, and `Function.py` to extract all mathematical Sets (hours, nodes, MGs), Parameters, and Variables into a Nomenclature table (`workspace/Nomenclature.md`).
**Acceptance criteria:**
- [ ] `Nomenclature.md` is created with clear tables mapping Pyomo variables/params to LaTeX symbols.
**Verification:**
- [ ] Output table is comprehensive and correct.
**Dependencies:** None
**Files likely touched:** `Nomenclature.md`

#### [x] Task 1.2.4: Write Section 3.3 - Tham số hệ thống
**Description:** Specify the input data parameters (Excel sources, Base Power 1MVA, VOLL, capacities, limits).
**Acceptance criteria:**
- [x] Parameters exactly match `System_Architecture_and_Data.md`.
**Verification:**
- [x] 4-layer compile succeeds.
**Dependencies:** Task 1.2.2
**Files likely touched:** `chapter3.tex`

### Checkpoint: Chapter 2 Complete
- [ ] PDF compiles without errors and Chapter 2 is complete.

### Phase 2: Local Microgrid Optimization & Spatial Coordination (Chapter 3 - AC-OPF & ATC)
#### [x] Task 2.3.1a: Write Section 3.4.1 - Hàm mục tiêu (Objective Function)
**Description:** Viết các phương trình hàm mục tiêu của bài toán AC-OPF, bao gồm chi phí lưới, DG, BESS, P2P, cắt tải.
**Acceptance criteria:**
- [x] Cấu trúc thành các phương trình tổng và con. Tuân thủ Nomenclature.
**Verification:** Passed by `@domain_reviewer`.
**Dependencies:** Phase 1
**Files likely touched:** `chapter3.tex`

#### [x] Task 2.3.1b: Write Section 3.4.2 - Ràng buộc trào lưu công suất (DistFlow Constraints)
**Description:** Viết hệ phương trình DistFlow phi tuyến gốc cho mạng hình tia: Cân bằng công suất P, Q và phương trình sụt áp.
**Acceptance criteria:**
- [x] Phương trình $P, Q$ tại nút và sụt áp trên nhánh.
**Verification:**
- [x] `@domain_reviewer` kiểm tra chéo với code.
**Dependencies:** Task 2.3.1a
**Files likely touched:** `chapter3.tex`

#### [x] Task 2.3.2: Write Section 3.5 - Khử phi tuyến SOCP (SOCP Relaxation & Exactness)
**Description:** Trình bày biến đổi DistFlow thành SOCP lồi. Phân tích rõ sự khác biệt giữa trạng thái Normal (SOCP Exact - Không lỗi) và Emergency do đứt gãy/cắt tải (SOCP Inexact - Lỗi) cùng cơ chế biến phạt.
**Acceptance criteria:**
- [x] Trình bày rõ ràng 2 trường hợp Exactness và Inexactness của SOCP.
**Verification:**
- [x] `@domain_reviewer` kiểm tra logic toán học.
**Dependencies:** Task 2.3.1b
**Files likely touched:** `chapter3.tex`

#### [ ] Task 2.3.3: Write Section 3.6 - Phối hợp Không gian với thuật toán ATC
**Description:** Xây dựng mô hình Analytical Target Cascading (ATC) để điều phối P2P giữa các MG. Thuật toán hoạt động trên khung thời gian tổng quát $h$ ($h=24$ hoặc $h=5$).
**Acceptance criteria:**
- [ ] Phương trình Coordinator và Local problem, biến $P, Q, \lambda$, và điều kiện hội tụ.
**Verification:**
- [ ] `@test-engineer` kiểm tra chéo với `main.py`.
**Dependencies:** Task 2.3.2
**Files likely touched:** `chapter3.tex`

### Checkpoint: Chapter 3 Complete
- [ ] PDF compiles without errors. Mathematical core (SOCP & ATC) is robust.

### Phase 3: Temporal Coordination (Chapter 4 - MPC)
#### [ ] Task 3.4.1: Write Section 4.1 - Khung thời gian Model Predictive Control (MPC)
**Description:** Trình bày logic cuộn thời gian (Rolling Horizon) của MPC qua 3 giai đoạn (Day-ahead, Intraday, Real-time) và cách cập nhật trạng thái (SOC, dự báo).
**Acceptance criteria:**
- [ ] Sơ đồ/Logic luồng thời gian dịch chuyển.
**Verification:**
- [ ] 4-layer compile succeeds.
**Dependencies:** Phase 2
**Files likely touched:** `chapter4.tex`

#### [ ] Task 3.4.2: Write Section 4.2 - Tích hợp MPC và ATC trong Vận hành Khẩn cấp (Emergency Mode)
**Description:** Trình bày cách lớp MPC gọi lớp ATC SOCP để ứng phó với tình huống khẩn cấp (N-2, đứt gãy kết nối, kích hoạt load shedding). Thể hiện rõ dòng chảy "Từ dưới lên" (Bottom-Up Integration).
**Acceptance criteria:**
- [ ] Liên kết rõ ràng thuật toán ở Chapter 3 với logic thời gian ở Chapter 4.
**Verification:**
- [ ] `@domain_reviewer` kiểm tra tính hợp lý của kiến trúc.
**Dependencies:** Task 3.4.1
**Files likely touched:** `chapter4.tex`

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
