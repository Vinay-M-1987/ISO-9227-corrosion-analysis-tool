from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import pandas as pd
from datetime import datetime

# Load evaluated data
df = pd.read_csv("evaluated_results.csv")

# Create PDF
doc = SimpleDocTemplate("corrosion_report.pdf")
styles = getSampleStyleSheet()

elements = []

# ===== Title =====
elements.append(Paragraph("CORROSION TEST REPORT", styles["Title"]))
elements.append(Spacer(1, 12))

elements.append(Paragraph("Standard: ISO 9227 - Salt Spray Test", styles["Normal"]))
elements.append(Paragraph(f"Date: {datetime.now().strftime('%Y-%m-%d')}", styles["Normal"]))
elements.append(Spacer(1, 12))

# ===== Test Types =====
elements.append(Paragraph("Test Types:", styles["Heading3"]))
elements.append(Paragraph("NSS - Neutral Salt Spray", styles["Normal"]))
elements.append(Paragraph("AASS - Acetic Acid Salt Spray", styles["Normal"]))
elements.append(Paragraph("CASS - Copper Accelerated Salt Spray", styles["Normal"]))
elements.append(Spacer(1, 12))

# ===== Table =====
table_data = [df.columns.tolist()] + df.values.tolist()

table = Table(table_data)
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
]))

elements.append(Paragraph("Test Results:", styles["Heading3"]))
elements.append(table)
elements.append(Spacer(1, 20))

# ===== Graph =====
elements.append(Paragraph("Correlation: Corrosion vs Mass Loss", styles["Heading3"]))
elements.append(Image("corrosion_plot.png", width=400, height=300))
elements.append(Spacer(1, 20))

# ===== Criteria =====
elements.append(Paragraph("Evaluation Criteria:", styles["Heading3"]))
elements.append(Paragraph("Corrosion > 3% → FAIL", styles["Normal"]))
elements.append(Paragraph("Mass Loss > 8 mg → CRITICAL", styles["Normal"]))
elements.append(Spacer(1, 20))

# ===== Signatures =====
elements.append(Paragraph("Signatures:", styles["Heading3"]))
elements.append(Spacer(1, 20))
elements.append(Paragraph("Test Engineer: ____________________", styles["Normal"]))
elements.append(Paragraph("Quality Engineer: ____________________", styles["Normal"]))

doc.build(elements)

print("✅ PDF report generated!")