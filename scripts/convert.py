import os
from fpdf import FPDF

def convert_images_to_pdf(images, pdf_dir, title):
    pdf = FPDF()
    for image in images:
        pdf.add_page()
        pdf.image(image, 0, 0, 210, 297)
    pdf.set_title(title)
    
    # ファイル名の重複を避けるための処理
    base_output_path = os.path.join(pdf_dir, f'{title}.pdf')
    output_path = base_output_path
    counter = 1
    while os.path.exists(output_path):
        output_path = os.path.join(pdf_dir, f'{title}_{counter}.pdf')
        counter += 1
    
    pdf.output(output_path, 'F')
    return output_path