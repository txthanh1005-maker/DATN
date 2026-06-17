# MASTER PLAN: Upgrade DATN Report to ATC & MPC Framework

## 1. Objective & Success Criteria
- **Objective:** Update the existing LaTeX report (`DATN.tex`) from the outdated ADMM/SOCP algorithm to the new **Analytical Target Cascading (ATC)** and **Model Predictive Control (MPC)** rolling horizon architecture.
- **Success Criteria:**
  1. Old tables and obsolete ADMM mathematical models (Chapters 3 & 4) are completely replaced with a 3-layer architecture (Chapter 2: System Architecture, Chapter 3: AC-OPF/ATC, Chapter 4: MPC).
  2. Literature review (Chapter 1) is carefully filtered: retain core papers, remove ADMM-specific papers, and incorporate new ATC/MPC literature.
  3. Results (Chapter 5) strictly follow the 5-stage architecture found in `Transfer folder/Result_data/report_result` (Stage 1 to 5: Macro Economics, Resilience, Algorithmic Scalability, Scarcity Pricing, etc.).
  4. The document compiles successfully without errors (`DATN.pdf` generated).

## 2. Assumptions
- The core Python code in the `Transfer folder` is considered the absolute "Source of Truth" for any algorithm or scenario parameter.
- The physical grid limits (e.g., bounds for PV, Wind, BESS, DG, Voltage, Trading Limits) described in `System_Architecture_and_Data.md` remain valid.
- The system comprises a Utility Grid and 4 MGs (MG1: heavy load, MG2: solar only, MG3: light load/savior, MG4: heavy load and high PV).
- The SOCP relaxation constraints still apply to the AC power flow model in the local microgrid operations.
- **Physics & Grid Modeling Approximations:** Reactive power ($Q$) is assumed NOT to be exported across tie-lines ($Q_{tie} = 0$). Global active power balancing ($P_{tie}$) is handled explicitly at the coordinator (ATC) level, not in the local SOCP equations. BESS end-of-day targets and main grid limits are managed via objective penalty relaxations in ATC during fault scenarios, so strict edge boundaries are not hit or required in local hard constraints.
- The user has already backed up the old ADMM LaTeX version.

## 3. Tech Stack & Structure
- **Core Technology:** LaTeX (using `thesis_1side.cls`).
- **Mathematical Framework:** Analytical Target Cascading (ATC), Model Predictive Control (MPC), Second-Order Cone Programming (SOCP).
- **Report Structure (Bottom-Up Approach):**
  - **Chapter 3: Local Microgrid Optimization**
    - **Base Level (SOCP):** Basic AC-OPF equations, SOCP relaxation. Phân tích rõ 2 trạng thái: Normal (Exact) và Emergency (Inexact do cắt tải/nghẽn mạch).
  - **Chapter 4: Spatial Coordination - Analytical Target Cascading (ATC)**
    - **Mid Level (ATC):** Thuật toán phân rã ATC chạy vòng lặp phối hợp P2P trên một khung thời gian $h$ bất kỳ ($h=24$ cho Day-Ahead hoặc $h=5$ cho Intraday/Emergency).
  - **Chapter 5: Temporal Coordination - Model Predictive Control (MPC)**
    - **Top Level (MPC):** Logic cuộn thời gian (Rolling Horizon).
    - **Tích hợp:** Cách MPC gọi thuật toán ATC(h) để đối phó với Emergency (đứt gãy lưới chính, sụt giảm PV/WT).
- **Template Reference:** The structure and formatting must follow `ĐỒ_ÁN_TỐT_NGHIỆP___TUẤN_ANH.md` as the gold standard.

## 4. Work Breakdown (The Plan Filter)
*As explicitly requested, the order of execution has been swapped to prioritize the Model/Algorithm and Results before adjusting the Literature.*
1. **Phase 1 (System Architecture - Chapter 2):** Draft Chapter 2 defining the 4-MG topology, system limits, and data sources (from `System_Architecture_and_Data.md`).
2. **Phase 2 (Model & Algorithm - Chapters 3, 4, 5):** Rebuild Chapters 3, 4, and 5 using the 3-layer logic, variables, and constraints from `main.py` and `workspace/Model & Algorithmlogic.md`.
3. **Phase 3 (Results - Chapter 6):** Draft Chapter 6 structured exactly according to the 5-Stage Architecture stored in `Transfer folder/Result_data/report_result/` (e.g., Stage 1: Macro Economics, Stage 4: Algorithmic Scalability, Stage 5: Scarcity Pricing \lambda).
 4. **Phase 4 (Literature Filter & Chapter 1):** Audit `chapter1.tex` to separate relevant fundamental papers from outdated ones (ADMM specific), and add theoretical background for ATC and MPC.

## 5. Boundaries
- **ALWAYS DO:** Reference `Transfer folder` files before making any mathematical claims in LaTeX. Check `agy-memory/SESSION_STATE.md` for project context. **CRITICAL:** Every mathematical formula written in LaTeX MUST strictly follow the symbols defined in `workspace/Nomenclature.md`. Do not invent new mathematical symbols.
- **ASK FIRST:** Before permanently deleting any cited paper from `references.bib`, present a list of proposed removals to the User (Tư lệnh) for final approval.
- **FORBIDDEN:** Do not modify any Python files in `Transfer folder` or execute them. The focus is strictly on drafting the LaTeX report. Do not fabricate results; all results must be derived from `Result_data` or `SESSION_STATE.md`.

## 6. Commands & Tools
- **Compiler:** Use local `pdflatex` on the user's machine.
- **Compilation Sequence:** Must strictly follow the user's defined 4-layer compilation sequence (`pdflatex` $\rightarrow$ `bibtex` $\rightarrow$ `pdflatex` $\rightarrow$ `pdflatex`) to ensure cross-references and citations are accurately updated.

## 7. Code Style
- **Equations:** Every equation must be numbered using the standard `equation` environment.
- **Grouped Equations:** Use `subequations` (e.g., 1a, 1b) for equations that share similar properties or belong to a specific block.
- **Bibliography:** All references must be strictly organized within a `.bib` file (e.g., `references.bib`).
- **Abbreviations:** All abbreviations must be organized in `workspace/Abbreviations.md` for agents to read prior to writing, and implemented properly in LaTeX (e.g., via a list of abbreviations). **Strict Rule:** Once an abbreviation is defined (e.g., Wind Turbines (WT)), do not repeat the full phrase in subsequent texts; use only the abbreviation.

## 8. Testing Strategy
- **Success Condition:** The document must pass the 4-layer compilation sequence without any Fatal Errors.
- **Auditing:** Output math and formulas must be cross-checked by `test-engineer` or `domain_reviewer` against `main.py` before any task is marked as `[x] DONE`.
