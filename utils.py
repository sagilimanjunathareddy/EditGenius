from fpdf import FPDF
import os
from datetime import datetime

def clean_text(text):
    
    return ''.join(c if ord(c) < 128 else '-' for c in text)

def save_as_pdf(original, rewritten, output_dir="output"):
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        pdf_path = os.path.join(output_dir, f"output_{timestamp}.pdf")

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Helvetica", size=12)

        # Clean and write content
        pdf.multi_cell(0, 10, "Original Content:\n" + clean_text(original))
        pdf.ln()
        pdf.multi_cell(0, 10, "Rewritten Content:\n" + clean_text(rewritten))

        pdf.output(pdf_path)
        print(f"[✅] PDF saved to {pdf_path}")
        return pdf_path

    except Exception as e:
        print(f"[❌] PDF generation failed: {e}")
        return None

def save_feedback(original, rewritten, output_dir="output"):
    try:
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_path = os.path.join(output_dir, f"feedback_{timestamp}.txt")

        with open(file_path, "w", encoding="utf-8") as f:
            f.write("Original Content:\n")
            f.write(original + "\n\n")
            f.write("Rewritten Content:\n")
            f.write(rewritten)

        print(f"[✅] Feedback saved to {file_path}")
        return file_path
    except Exception as e:
        print(f"[❌] Feedback saving failed: {e}")
        return None
