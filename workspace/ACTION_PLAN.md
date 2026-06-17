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
**Description:** Write the Network Topology describing the 4 Microgrids + Utility Grid topology.
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

### Phase 2: Local Microgrid Optimization (Chapter 3 - AC-OPF)
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

### Checkpoint: Chapter 3 Complete
- [ ] PDF compiles without errors. Mathematical core (SOCP) is robust.

### Phase 3: Spatial Coordination (Chapter 4 - Analytical Target Cascading)
#### [x] Task 3.4.1: Write Section 4.1 & 4.2 - ATC Overview & Coordinator Problem
**Description:** Trình bày tổng quan về Analytical Target Cascading (ATC) trong bài toán P2P (chia làm 2 cấp: Coordinator và Local). Viết phương trình tối ưu của Coordinator (Utility Grid), bao gồm hàm mục tiêu và các ràng buộc cập nhật tín hiệu giá (penalty multipliers $\lambda, c$).
**Acceptance criteria:**
- [ ] Giải thích rõ kiến trúc 2 cấp và biến mục tiêu $P_{tie}^*$.
- [ ] Phương trình hàm mục tiêu và cập nhật $\lambda, c$ của Coordinator.
**Verification:**
- [ ] `@domain_reviewer` kiểm tra tính chính xác của toán học.
**Dependencies:** Task 2.3.2
**Files likely touched:** `chapter4.tex`

#### [x] Task 3.4.2: Write Section 4.3 - Local Microgrid Problem with ATC
**Description:** Tích hợp hàm phạt (penalty function) của ATC vào bài toán Local SOCP đã xây dựng ở Section 3.4. Trình bày sự thay đổi trong hàm mục tiêu của các Local MG khi tham gia thị trường P2P.
**Acceptance criteria:**
- [ ] Hàm mục tiêu mới của Local MGs có chứa thành phần Augmented Lagrangian (bám theo $P_{tie}^*$ từ Coordinator).
**Verification:**
- [ ] `@domain_reviewer` kiểm tra chéo với hàm mục tiêu trong `main.py`.
**Dependencies:** Task 3.4.1
**Files likely touched:** `chapter4.tex`

#### [x] Task 3.4.3: Write Section 4.4 - ATC Iterative Algorithm & Convergence
**Description:** Viết quy trình lặp (Iterative Algorithm) của ATC và các điều kiện hội tụ (Convergence Criteria).
**Acceptance criteria:**
- [ ] Trình bày rõ các bước lặp $k$.
- [ ] Định nghĩa sai số nguyên thủy (primal residual) và đối ngẫu (dual residual) và điều kiện dừng $\epsilon$.
**Verification:**
- [ ] `@test-engineer` đối chiếu logic vòng lặp trong `main.py`.
**Dependencies:** Task 3.4.2
**Files likely touched:** `chapter4.tex`

### Checkpoint: Chapter 4 Complete
- [ ] PDF compiles without errors. ATC loop is robust.

### Phase 4: Temporal Coordination (Chapter 5 - MPC)

#### [>] Task 4.1: Khởi tạo Chapter 5 & Viết Section 5.1 (Khung thời gian MPC)
**Description:** Tạo mới file `chapters/chapter5.tex`, nhúng vào `DATN.tex`. Sau đó viết nội dung Section 5.1 trình bày logic cuộn thời gian (Rolling Horizon) của thuật toán điều khiển dự báo mô hình (MPC) qua các giai đoạn.
**Acceptance criteria:**
- [ ] File `chapter5.tex` được tạo và đưa vào `DATN.tex` bằng lệnh `\input`.
- [ ] Trình bày nguyên lý cơ bản của Rolling Horizon và khung thời gian dịch chuyển.
- [ ] Sử dụng đúng Nomenclature đã định nghĩa.
**Verification:**
- [ ] 4-layer compile succeeds.
- [ ] Peer Agent Review: `@english_teacher` kiểm tra văn phong học thuật.
**Dependencies:** Phase 3
**Files likely touched:**
- `DATN.tex`
- `chapters/chapter5.tex`
**Estimated scope:** Small (2 files)

#### [ ] Task 4.2: Viết Section 5.2 (Cơ chế cập nhật trạng thái và Dự báo)
**Description:** Viết nội dung quy định cách các tham số trạng thái như State of Charge (SOC) của BESS và các số liệu dự báo (PV, WT, Tải) được cập nhật và chuyển giao giữa các bước lặp cuộn thời gian của MPC.
**Acceptance criteria:**
- [ ] Công thức hóa quá trình kế thừa SOC từ thời điểm trước ($t \rightarrow t+1$).
- [ ] Tuân thủ nghiêm ngặt các ký hiệu và quy ước toán học của dự án.
**Verification:**
- [ ] 4-layer compile succeeds.
- [ ] Peer Agent Review: `@domain_reviewer` kiểm tra logic cập nhật tham số với code lõi Python.
**Dependencies:** Task 4.1
**Files likely touched:**
- `chapters/chapter5.tex`
**Estimated scope:** Small (1 file)

#### [ ] Task 4.3: Viết Section 5.3 (Tích hợp MPC và ATC trong Vận hành Khẩn cấp)
**Description:** Trình bày cốt lõi của giải pháp: cách lớp quản lý thời gian (MPC) kết hợp chặt chẽ với thuật toán điều phối không gian (ATC SOCP - Chapter 4) để phản ứng linh hoạt với tình huống đứt gãy kết nối (Emergency Mode) như N-2 hoặc sập nguồn.
**Acceptance criteria:**
- [ ] Thể hiện rõ dòng chảy "Từ dưới lên" (Bottom-Up Integration).
- [ ] Làm nổi bật được quá trình kích hoạt biến phạt (penalty function) và cơ chế cắt tải (load shedding) trong luồng MPC.
**Verification:**
- [ ] 4-layer compile succeeds.
- [ ] Peer Agent Review: `@domain_reviewer` đối chiếu kiến trúc tích hợp.
**Dependencies:** Task 4.2
**Files likely touched:**
- `chapters/chapter5.tex`
**Estimated scope:** Medium (1 file)

### Checkpoint: Chapter 5 Complete
- [ ] PDF biên dịch thành công không có lỗi (0 errors).
- [ ] Luồng điều khiển MPC và ATC đã được liên kết một cách logic và khoa học.
- [ ] Đã Review với Human (Tư lệnh) trước khi tiến tới Phase 5 (Results).

### Phase 5: Results (Chapter 6)
#### [ ] Task 5.6.1: Stage 1 & 2 (Macro Economics & Resilience)
**Description:** Write results based on `Result_data/report_result/stage_1` and `stage_2`.
**Acceptance criteria:**
- [ ] Extract and format charts/tables correctly with `MW/MWh` units.
**Verification:**
- [ ] 4-layer compile succeeds.
**Dependencies:** Phase 4
**Files likely touched:** `chapter6.tex`

#### [ ] Task 5.6.2: Stage 3 (100% Critical Load Protected)
**Description:** Write Node-Level Load Shedding resolution analysis.
**Acceptance criteria:**
- [ ] Explain negative premium and protected loads using charts.
**Verification:**
- [ ] 4-layer compile succeeds.
**Dependencies:** Task 5.6.1
**Files likely touched:** `chapter6.tex`

#### [ ] Task 5.6.3: Stage 4 (Algorithmic Scalability)
**Description:** Write analysis on CPU metrics and ATC convergence.
**Acceptance criteria:**
- [ ] Incorporate CPU time ($\sim 91s$) and residual plots.
**Verification:**
- [ ] 4-layer compile succeeds.
**Dependencies:** Task 5.6.2
**Files likely touched:** `chapter6.tex`

#### [ ] Task 5.6.4: Stage 5 (ATC Scarcity Pricing \lambda)
**Description:** Analyze the 5 tie-line price signals.
**Acceptance criteria:**
- [ ] Include Scarcity Pricing $\lambda$ graphs and market signals logic.
**Verification:**
- [ ] `@test-engineer` visual review of PDF.
- [ ] 4-layer compile succeeds.
**Dependencies:** Task 5.6.3
**Files likely touched:** `chapter6.tex`

### Phase 6: Polish & Literature (Chapter 1)
#### [ ] Task 6.1.1: Audit Literature
**Description:** Propose ADMM paper removals from `references.bib`.
**Acceptance criteria:**
- [ ] Present list to user. Await approval.
**Verification:**
- [ ] Human (Tư lệnh) review.
**Dependencies:** None
**Files likely touched:** `references.bib`

#### [ ] Task 6.1.2: Rewrite Chapter 1
**Description:** Write Introduction and ATC/MPC literature background.
**Acceptance criteria:**
- [ ] Clean integration of new `.bib` citations without outdated logic.
**Verification:**
- [ ] Final 4-layer compile without any errors.
**Dependencies:** Task 6.1.1
**Files likely touched:** `chapter1.tex`
