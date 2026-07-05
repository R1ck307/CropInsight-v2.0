from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime

def generate_pdf_report(filename, crop, result):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    content = []

    # Title
    content.append(Paragraph("CropInsight AI Diagnosis Report", styles["Title"]))
    content.append(Spacer(1, 12))

    # Date
    content.append(Paragraph(f"Date: {datetime.now()}", styles["Normal"]))
    content.append(Spacer(1, 12))

    # Crop
    content.append(Paragraph(f"<b>Crop:</b> {crop}", styles["Normal"]))
    content.append(Spacer(1, 12))

    # Best match
    best = result["best_match"]

    content.append(Paragraph("Diagnosis Result", styles["Heading2"]))
    content.append(Paragraph(f"Disease: {best['disease']}", styles["Normal"]))
    content.append(Paragraph(f"Confidence: {best['confidence']}%", styles["Normal"]))
    content.append(Paragraph(f"Severity: {best['severity']}", styles["Normal"]))
    content.append(Spacer(1, 12))

    # Treatments
    content.append(Paragraph("Recommended Treatments", styles["Heading2"]))

    for t in result["treatments"]:
        content.append(Paragraph(
            f"- {t['treatment_type']}: {t['description']}",
            styles["Normal"]
        ))

    doc.build(content)

    return filename
