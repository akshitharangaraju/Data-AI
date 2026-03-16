from fpdf import FPDF
import datetime
import os

def generate_medical_document(analysis_text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 18)
    pdf.cell(0, 15, "CARDIOLOGY SPECIALIST - CLINICAL SUMMARY", ln=True, align="C")
    pdf.set_font("Helvetica", "I", 10)
    pdf.cell(0, 10, f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}", ln=True, align="R")
    pdf.line(10, 32, 200, 32)
    pdf.ln(10)
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 10, "Specialist Assessment:", ln=True)
    pdf.set_font("Helvetica", "", 11)
    pdf.multi_cell(0, 8, analysis_text)
    
    if not os.path.exists("reports"): os.makedirs("reports")
    path = f"reports/Cardio_Report_{datetime.date.today()}.pdf"
    pdf.output(path)
    return path