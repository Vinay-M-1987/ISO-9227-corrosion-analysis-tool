import tkinter as tk
from tkinter import ttk
import pandas as pd

FILE_NAME = "corrosion_test_data.csv"

columns = [
    "Sample ID",
    "Material",
    "Coating",
    "Test Type",
    "Time (h)",
    "Corrosion (%)",
    "Mass Loss (mg)"
]

entries = []

# --- Decimal cleaning ---
def clean_value(value):
    value = value.replace(",", ".")
    try:
        return float(value)
    except:
        return None

# --- Add row ---
def add_row():
    row_entries = []
    row_index = len(entries) + 2

    for col_index in range(len(columns)):

        # Test Type dropdown
        if col_index == 3:
            combo = ttk.Combobox(root, values=["NSS", "AASS", "CASS"], width=12)
            combo.grid(row=row_index, column=col_index, padx=2, pady=2)
            row_entries.append(combo)

        else:
            entry = tk.Entry(root, width=15)
            entry.grid(row=row_index, column=col_index, padx=2, pady=2)
            row_entries.append(entry)

    entries.append(row_entries)

# --- Save data ---
def save_data():
    all_data = []

    for row_idx, row in enumerate(entries):
        row_data = {}
        valid = True

        for i, widget in enumerate(row):
            value = widget.get().strip()

            # Numeric columns → index-based check
            if i in [4, 5, 6]:  # Time, Corrosion, Mass Loss
                cleaned = clean_value(value)
                if cleaned is None:
                    print(f"❌ Invalid number in row {row_idx+1}, column '{columns[i]}'")
                    valid = False
                    break
                row_data[columns[i]] = cleaned
            else:
                row_data[columns[i]] = value

        if valid:
            all_data.append(row_data)

    if all_data:
        df = pd.DataFrame(all_data)
        try:
            df.to_csv(FILE_NAME, mode='a', header=False, index=False)
        except:
            df.to_csv(FILE_NAME, index=False)

        print("✅ Data saved successfully!")


# --- Sample Example ---
import pandas as pd

def load_sample_data():
    df = pd.read_csv("corrosion_test_data.csv")

    # Clear existing entries
    for row in entries:
        for widget in row:
            widget.delete(0, tk.END)

    # Fill table
    for i, (_, data_row) in enumerate(df.iterrows()):
        if i >= len(entries):
            add_row()

        for j, col in enumerate(df.columns):
            entries[i][j].insert(0, str(data_row[col]))

    print("✅ Example Data used!")


# --- Submit ---
def submit_data():
    print("📤 Data submitted for analysis!")
    import analysis_report

# --- GUI ---
root = tk.Tk()
root.title("Corrosion Test Table Input")

# --- Buttons ---
tk.Button(root, text="💾 Save", command=save_data).grid(row=0, column=0, pady=5)
tk.Button(root, text="▶ Submit", command=submit_data).grid(row=0, column=len(columns)-1, pady=5)
tk.Button(root, text="📄 Sample Table", command=load_sample_data)\
    .grid(row=100, column=len(columns)-1, pady=10)

# --- Header Row ---
for col_index, col_name in enumerate(columns):
    label = tk.Label(root, text=col_name, font=("Arial", 10, "bold"))
    label.grid(row=1, column=col_index, padx=5, pady=5)

# --- Initial rows ---
for _ in range(3):
    add_row()

# --- Add Row Button ---
tk.Button(root, text="➕ Add Row", command=add_row).grid(row=100, column=0, pady=10)

root.mainloop()