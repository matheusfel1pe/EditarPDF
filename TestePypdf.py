import os
from PyPDF2 import PdfReader, PdfWriter


def remove_page_range(input_pdf, output_pdf, start_page, end_page):
    pdf_reader = PdfReader(input_pdf)
    pdf_writer = PdfWriter()

    for page_number, page in enumerate(pdf_reader.pages, start=1):
        if not (start_page <= page_number <= end_page):
            pdf_writer.add_page(page)

    with open(output_pdf, 'wb') as output:
        pdf_writer.write(output)


input_pdf_name = 'Fundamentos Matemáticos.pdf'
folder_path = 'EditarMeusPDF/arquivos'
input_pdf_path = os.path.join(folder_path, input_pdf_name)
output_pdf_name = 'Fundamentos_Matematicos.pdf'
output_pdf_path = os.path.join(folder_path, output_pdf_name)
start_page = 2
end_page = 20

remove_page_range(input_pdf_path, output_pdf_path, start_page, end_page)
