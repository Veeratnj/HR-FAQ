import os
import shutil
from pdf2image import convert_from_path
 
def pdf_split(path, key):
    output_dir = f'img_{key}'
 
    if os.path.exists(output_dir):
        for filename in os.listdir(output_dir):
            file_path = os.path.join(output_dir, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
        shutil.rmtree(output_dir)  
    
    os.makedirs(output_dir)  
    
    pages = convert_from_path(path, 300)
    for i, page in enumerate(pages):
        img_path = f'{output_dir}/page_{i + 1}.png'
        page.save(img_path, 'PNG')
    
    if os.path.exists(path):
        os.remove(path)
 
    print("PDF split complete and original PDF file removed.")
    
    return [os.path.join(output_dir, f) for f in os.listdir(output_dir) if f.endswith('.png')]
 
 
if '__main__'==__name__:
    pdf_split(path='',key='')