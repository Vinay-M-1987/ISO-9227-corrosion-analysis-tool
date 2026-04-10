import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

FILE_NAME = "corrosion_test_data.csv"

# --- Decision logic ---
def evaluate(row):
    if row["Corrosion (%)"] > 3:
        return "FAIL"
    elif row["Mass Loss (mg)"] > 8:
        return "CRITICAL"
    else:
        return "PASS"

# --- Load data ---
df = pd.read_csv(FILE_NAME)

# --- Apply evaluation ---
df["Status"] = df.apply(evaluate, axis=1)

# --- Ranking (best = lowest corrosion + mass loss)
df["Score"] = df["Corrosion (%)"] + df["Mass Loss (mg)"]
df = df.sort_values(by="Score")

# --- Save result table
df.to_csv("evaluated_results.csv", index=False)

# ================= GRAPH =================
plt.figure()

for sample in df["Sample ID"].unique():
    sample_data = df[df["Sample ID"] == sample]
    plt.scatter(
        sample_data["Corrosion (%)"],
        sample_data["Mass Loss (mg)"],
        label=sample
    )

plt.xlabel("Corrosion (%)")
plt.ylabel("Mass Loss (mg)")
plt.title("Corrosion vs Mass Loss (Sample Comparison)")
plt.legend()
plt.grid()

plt.savefig("corrosion_plot.png")
plt.close()

# ================= REPORT =================

report = f"""
===========================================
        CORROSION TEST REPORT
===========================================

Standard: ISO 9227 - Salt Spray Test
Date: {datetime.now().strftime("%Y-%m-%d")}

-------------------------------------------
Test Types:
NSS  - Neutral Salt Spray
AASS - Acetic Acid Salt Spray
CASS - Copper Accelerated Salt Spray
-------------------------------------------

Test Procedure:
Samples were exposed to salt spray environment
for defined duration. Corrosion area and mass
loss were measured and evaluated.

-------------------------------------------
FAIL / PASS CRITERIA:
- Corrosion > 3% → FAIL
- Mass Loss > 8 mg → CRITICAL
-------------------------------------------

TEST RESULTS:
"""

# Add table-like results
for _, row in df.iterrows():
    report += f"""
Sample: {row['Sample ID']}
Material: {row['Material']}
Coating: {row['Coating']}
Test: {row['Test Type']}
Time: {row['Time (h)']} h
Corrosion: {row['Corrosion (%)']} %
Mass Loss: {row['Mass Loss (mg)']} mg
Status: {row['Status']}
-------------------------------------------
"""

# Best sample
best = df.iloc[0]

report += f"""
BEST SAMPLE:
{best['Material']} + {best['Coating']} ({best['Test Type']})

-------------------------------------------
Remarks:
- Lower corrosion and mass loss indicate better performance
- CASS test shows highest severity
-------------------------------------------

Signatures:

Test Engineer: ______________________

Quality Engineer: ___________________

"""

# Save report
with open("corrosion_report.txt", "w", encoding="utf-8") as f:
    f.write(report)

print("✅ Analysis complete. Report & graph generated.")


# CONNECT ANALYSIS
import pdf_report