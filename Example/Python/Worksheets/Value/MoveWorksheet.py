import os
from pathlib import Path
from datetime import datetime
from aspose.cells import Workbook

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets/Value/MoveWorksheet"

def run():
    data_dir = get_data_dir()
    
    input_path = os.path.join(data_dir, "book1.xls")
    
    wb = Workbook(input_path)
    
    sheets = wb.worksheets
    worksheet = sheets[0]
    
    worksheet.move_to(2)
    
    output_path = os.path.join(data_dir, "MoveWorksheet_out.xls")
    wb.save(output_path)

if __name__ == "__main__":
    run()