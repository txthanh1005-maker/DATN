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
- The system comprises MG0 (Main Grid) and 4 MGs (MG1: heavy load, MG2: solar only, MG3: light load/savior, MG4: heavy load and high PV).
- The SOCP relaxation constraints still apply to the AC power flow model in the local microgrid operations.
- The user has already backed up the old ADMM LaTeX version.

## 3. Tech Stack & Structure
- **Core Technology:** LaTeX (using `thesis_1side.cls`).
- **Mathematical Framework:** Analytical Target Cascading (ATC), Model Predictive Control (MPC), Second-Order Cone Programming (SOCP).
- **Report Structure (3-Layer Core): read from workspace\Model & Algorithmlogic.md**
  - **Lớp 1 (Chapter 2): System Architecture & Parameters** (Network topology, energy components, input datasets from Excel).
  - **Lớp 2 (Chapter 3): Optimal Power Flow & ATC** (Non-linear AC-OPF, SOCP relaxation, ATC mechanism for P2P trading).
  - **Lớp 3 (Chapter 4): Model Predictive Control** (Rolling Horizon, integration of MPC and ATC, Emergency Mode).
- **Template Reference:** The structure and formatting must follow `ĐỒ_ÁN_TỐT_NGHIỆP___TUẤN_ANH.md` as the gold standard.

## 4. Work Breakdown (The Plan Filter)
*As explicitly requested, the order of execution has been swapped to prioritize the Model/Algorithm and Results before adjusting the Literature.*
1. **Phase 1 (System Architecture - Chapter 2):** Draft Chapter 2 defining the 4-MG topology, system limits, and data sources (from `System_Architecture_and_Data.md`).
2. **Phase 2 (Model & Algorithm - Chapters 3 & 4):** Rebuild Chapters 3 and 4 using the 3-layer logic, variables, and constraints from `main.py` and `workspace/Model & Algorithmlogic.md`.
3. **Phase 3 (Results - Chapter 5):** Draft Chapter 5 structured exactly according to the 5-Stage Architecture stored in `Transfer folder/Result_data/report_result/` (e.g., Stage 1: Macro Economics, Stage 4: Algorithmic Scalability, Stage 5: Scarcity Pricing \lambda).
 4. **Phase 4 (Literature Filter & Chapter 1):** Audit `chapter1.tex` to separate relevant fundamental papers from outdated ones (ADMM specific), and add theoretical background for ATC and MPC.

## 5. Boundaries
- **ALWAYS DO:** Reference `Transfer folder` files before making any mathematical claims in LaTeX. Check `agy-memory/SESSION_STATE.md` for project context.
- **ASK FIRST:** Before permanently deleting any cited paper from `references.bib`, present a list of proposed removals to the User (Tư lệnh) for final approval.
- **FORBIDDEN:** Do not modify any Python files in `Transfer folder` or execute them. The focus is strictly on drafting the LaTeX report. Do not fabricate results; all results must be derived from `Result_data` or `SESSION_STATE.md`.

## 6. Commands & Tools
- **Compiler:** Use local `pdflatex` on the user's machine.
- **Compilation Sequence:** Must strictly follow the user's defined 4-layer compilation sequence (`pdflatex` $\rightarrow$ `bibtex` $\rightarrow$ `pdflatex` $\rightarrow$ `pdflatex`) to ensure cross-references and citations are accurately updated.

## 7. Code Style
- **Equations:** Every equation must be numbered using the standard `equation` environment.
- **Grouped Equations:** Use `subequations` (e.g., 1a, 1b) for equations that share similar properties or belong to a specific block.
- **Bibliography:** All references must be strictly organized within a `.bib` file (e.g., `references.bib`).

## 8. Testing Strategy
- **Success Condition:** The document must pass the 4-layer compilation sequence without any Fatal Errors.
- **Auditing:** Output math and formulas must be cross-checked by `test-engineer` or `domain_reviewer` against `main.py` before any task is marked as `[x] DONE`.
