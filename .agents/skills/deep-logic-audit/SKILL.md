---
name: deep-logic-audit
description: Thể thức kiểm tra sâu (3 bước) dành cho đánh giá logic vật lý, AC-OPF và tìm các "Missing Links" trong các chương Luận văn khoa học.
---

# Deep Logic Audit Workflow (Quy trình Review 3 Bước của Tư lệnh)

This skill provides a rigorous, 3-step auditing framework specifically designed to evaluate complex scientific writing (such as AC-OPF, Grid Stability, and P2P Trading chapters) for logical consistency, cross-linking, and academic depth.

## Trigger
Use this skill when the user asks to "audit", "review the logic", "tìm missing link", or "rà soát sâu" a specific chapter or document.

## Execution Steps

You must follow this exact 3-step process. Do NOT skip steps or merge them.

### Step 1: The Skim (Xác định Xương sống Logic)
- **Action:** Read through the entire text of the target document/chapter quickly.
- **Purpose:** Do not look for spelling or minor errors. Focus entirely on identifying the overarching logic, system configuration, and major physical phenomena being described (e.g., Load Shedding, Voltage Limits, P2P Pricing).
- **Output:** Establish a "Global Baseline" of the system's intended behavior.

### Step 2: The Deep Dive & Roll-up (Review Cuốn chiếu từng Section)
- **Action:** Go back to the beginning and review the document section-by-section. For each section, you MUST open and cross-reference the corresponding charts/data images.
- **Questions to Answer per Section:**
  1. **Missing Links (Đứt gãy liên kết):** Does the input/data in this section have implications for downstream sections that the author failed to analyze? (e.g., MG2 losing PV makes it a sink, which forces MG4 to act as a transit hub).
  2. **Isolated Islands (Đoạn văn Cô lập):** Are there any paragraphs or analyses that stand completely independent without linking to the sections above or below them? If an insight is isolated, trigger a WARNING and propose a method to weave it into the broader narrative or connect it to subsequent results.
  3. **Physical Logic Contradictions (Mâu thuẫn Vật lý):** Does the text contradict the actual plotted data or the fundamental laws of Power Systems (e.g., AC-OPF limits, $I^2X$ losses, Economic Dispatch principles)?
  4. **Mathematical Cross-Validation:** Which specific constraint or mathematical equation is driving this phenomenon? Explicitly link the observed behavior to the AC-OPF formulation.
  5. **Hostile Examiner (Red Teaming):** If you were a hostile committee member trying to reject this thesis based on this specific chart/paragraph, what weakness would you attack? Provide preemptive defenses.

### Step 3: The Audit Report
- **Action:** Output a structured report to the user.
- **Format:**
  - Break down the report by Section.
  - Clearly identify any [LOGIC BUGS] and [MISSING LINKS].
  - Provide actionable, deep AC-OPF academic recommendations to deepen the analysis.
  - Suggest footnotes or preemptive defenses for any vulnerabilities identified in the Red Teaming phase.
  - If a section is mathematically and logically perfect, explicitly state [PASS].
- **Constraint:** Do not auto-edit the user's code/LaTeX unless explicitly commanded. Just provide the specialized audit analysis.
