from aspose.cells import Workbook
from aspose.pydrawing import Color
import os
from pathlib import Path

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def main():
    output_dir = get_output_directory()
    
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
    
    workbook = Workbook()
    
    worksheet = workbook.worksheets[0]
    
    worksheet.cells.get(0, 0).put_value(1)
    worksheet.cells.get(1, 0).put_value(2)
    worksheet.cells.get(2, 0).put_value(3)
    worksheet.cells.get(3, 0).put_value(4)
    worksheet.cells.get(4, 0).put_value(5)
    worksheet.cells.get(5, 0).put_value(6)
    worksheet.cells.get(0, 1).put_value(7)
    worksheet.cells.get(1, 1).put_value(8)
    worksheet.cells.get(2, 1).put_value(9)
    worksheet.cells.get(3, 1).put_value(10)
    worksheet.cells.get(4, 1).put_value(11)
    worksheet.cells.get(5, 1).put_value(12)
    
    background = worksheet.page_setup.ods_page_background
    
    background.color = Color.azure
    background.type = background.type.COLOR
    
    output_file = os.path.join(output_dir, "ColoredBackground.ods")
    workbook.save(output_file)
    
    print("SetODSColoredBackground executed successfully.")

if __name__ == "__main__":
    main()