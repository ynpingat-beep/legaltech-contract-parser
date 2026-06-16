from contracts.utils import extract_text_from_pdf

pdf_path = r"media\contracts\ERP_BMD_REPORT_YASH.pdf"

text = extract_text_from_pdf(pdf_path)

print(text)