# 🧪 Automated Corrosion Test Analysis Tool (ISO 9227)

## 📖 Overview
This mini project demonstrates the application of Python in test report creation, by automating the analysis of corrosion test data based on ISO 9227 (Salt Spray Testing).

It replaces manual Excel-based evaluation with a structured, traceable, and automated workflow.

---

## 🚀 Features
- 📊 Table-based GUI for structured data input
- 🧼 Data validation (handles decimal formats like 1,5 → 1.5, German → English )
- ⚙️ Automated evaluation logic (PASS / FAIL / CRITICAL)
- 📈 Graph generation (Corrosion vs Mass Loss)
- 📄 Professional PDF report generation
- 📂 Sample dataset loading for quick demo

---

## 🧪 Test Standard
ISO 9227 – Corrosion tests in artificial atmospheres (Salt Spray Test)

### Test Types:
- NSS – Neutral Salt Spray
- AASS – Acetic Acid Salt Spray
- CASS – Copper Accelerated Salt Spray

---

## 📊 Output
The tool generates:
- Evaluated results table
- Correlation graph
- Structured PDF report including:
  - Test details
  - Results table
  - Graph
  - Evaluation criteria
  - Signature section

---

## Sample Graph

![This is an alt text.](/image/corrosion_plot.png "This is a sample Graph.")

---


## ⚙️ How to Run

### 1. Install dependencies
```bash
pip install pandas matplotlib reportlab



# Run this script:
python table_input_gui.py
