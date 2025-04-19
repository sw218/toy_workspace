from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

text = input("PDF로 저장할 텍스트를 입력하세요: ")
pdf.multi_cell(0, 10, text)

pdf.output("document.pdf")
print("PDF 파일이 'document.pdf'로 저장되었습니다.")
