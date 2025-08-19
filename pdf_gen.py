from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors

# JSON-like data
data = {
    "leave_process": "Employees can apply for leave using the HR portal. "
                     "Approval from the manager is required. "
                     "Portal link is www.veeratech.com",

    "department_change": "Submit a department change request via the internal transfer form. "
                         "HR will review and schedule an interview if needed.",

    "salary_slip": "Salary slips are available in the employee self-service portal under the 'Pay' section."
}

# PDF file name
pdf_file = "HR_Guide.pdf"

# Create document
doc = SimpleDocTemplate(pdf_file, pagesize=A4)
styles = getSampleStyleSheet()

# Custom title style
title_style = ParagraphStyle(
    name="TitleStyle",
    fontSize=18,
    leading=22,
    alignment=1,  # center
    spaceAfter=20,
    textColor=colors.HexColor("#1a73e8")
)

# Section header style
header_style = ParagraphStyle(
    name="HeaderStyle",
    fontSize=14,
    leading=18,
    spaceAfter=10,
    textColor=colors.darkblue,
    underlineWidth=1
)

# Body text style
body_style = ParagraphStyle(
    name="BodyStyle",
    fontSize=11,
    leading=14,
    spaceAfter=15
)

# Story content
story = []

# Title
story.append(Paragraph("HR Policies & Processes", title_style))
story.append(Spacer(1, 12))

# Add each section
for key, value in data.items():
    header = key.replace("_", " ").title()  # e.g. leave_process → Leave Process
    story.append(Paragraph(header, header_style))
    story.append(Paragraph(value, body_style))
    story.append(Spacer(1, 12))

# Build PDF
doc.build(story)
print(f"✅ PDF generated successfully: {pdf_file}")
