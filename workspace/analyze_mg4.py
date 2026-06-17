import pandas as pd
import glob
import os

source_file = r"D:\Latex\DATN\Transfer folder\Source_data\MG4.xlsx"
df_source = pd.read_excel(source_file)
print("--- MG4.xlsx ---")
print(df_source.head())

load_files = glob.glob(r"D:\Latex\DATN\Transfer folder\Node_PQ_data\MG4\*.xlsx")
total_load_kw = 0
for f in load_files:
    df_load = pd.read_excel(f)
    # Assuming standard format has something like P, Q or similar.
    # We will just print the first one's head and sum over all if possible.
    total_load_kw += df_load.iloc[:, 1].sum() # Guessing 2nd column is P

print(f"\nTotal load files: {len(load_files)}")
print(f"Total load (rough estimate): {total_load_kw}")
df_load_1 = pd.read_excel(load_files[0])
print("\n--- First load file head ---")
print(df_load_1.head())
