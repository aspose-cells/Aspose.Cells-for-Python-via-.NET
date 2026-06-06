import os
from datetime import datetime
from aspose.cells import Workbook
from aspose.pydrawing import Color

def get_data_dir():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "Data", "Worksheets", "PageSetupFeatures", "InsertImageInHeaderFooter")

def run():
    data_dir = get_data_dir()
    
    workbook = Workbook()
    
    logo_url = os.path.join(data_dir, "aspose-logo.jpg")
    
    with open(logo_url, "rb") as file:
        binary_data = file.read()
    
    page_setup = workbook.worksheets[0].page_setup
    
    page_setup.set_header_picture(1, binary_data)
    
    page_setup.set_header(1, "&G")
    
    page_setup.set_header(2, "&A")
    
    output_path = os.path.join(data_dir, "InsertImageInHeaderFooter_out.xls")
    workbook.save(output_path)

if __name__ == "__main__":
    run()