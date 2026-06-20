import os

filepath = r'D:\Latex\DATN\chapters\chapter4.tex'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    (r'\State DAY-AHEAD SCHEDULING PHASE', r'\State \textbf{DAY-AHEAD SCHEDULING PHASE}'),
    (r'\State REAL-TIME EMERGENCY MPC PHASE', r'\State \textbf{REAL-TIME EMERGENCY MPC PHASE}'),
    (r'\State STEP 1: STATE UPDATE', r'\State \textbf{STEP 1: STATE UPDATE}'),
    (r'\State STEP 2: MODE BRANCHING \& EVENT DETECTION', r'\State \textbf{STEP 2: MODE BRANCHING \& EVENT DETECTION}'),
    (r'\State Mode 1 (Normal Operation):', r'\State \textbf{Mode 1 (Normal Operation):}'),
    (r'\State Mode 2 (Emergency Mode):', r'\State \textbf{Mode 2 (Emergency Mode):}'),
    (r'\State Activate Emergency Mode Constraints', r'\State \textbf{Activate Emergency Mode Constraints}'),
    (r'\State Update Objective Function:', r'\State \textbf{Update Objective Function:}'),
    (r'\Statex Algorithm 1 (Continued) -- MODE 2 (Emergency Mode) Continued', r'\Statex \textbf{Algorithm 1 (Continued) -- MODE 2 (Emergency Mode) Continued}'),
    (r'\State STEP 3: ROLLING HORIZON OPTIMIZATION LOOP', r'\State \textbf{STEP 3: ROLLING HORIZON OPTIMIZATION LOOP}'),
    (r'\State Call', r'\State \textbf{Call}'),
    (r'\State STEP 4: CONTROL IMPLEMENTATION', r'\State \textbf{STEP 4: CONTROL IMPLEMENTATION}'),
    (r'\State Apply only', r'\State \textbf{Apply only}'),
    (r'\State Mode 3 (Recovery Mode):', r'\State \textbf{Mode 3 (Recovery Mode):}')
]

for old, new in replacements:
    content = content.replace(old, new)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Restored chapter 4")
