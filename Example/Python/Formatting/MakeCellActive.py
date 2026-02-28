import os
from aspose.cells import Workbook
from aspose.pydrawing import Color
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "Formatting/MakeCellActive"

def make_cell_active():
    data_dir = get_data_dir()
    os.makedirs(data_dir, exist_ok=True)
    
    workbook = Workbook()
    
    worksheet1 = workbook.worksheets[0]
    
    cells = worksheet1.cells
    
    cells.get(1, 1).put_value("Hello World!")
    
    workbook.worksheets.active_sheet_index = 0
    
    worksheet1.active_cell = "B2"
    
    worksheet1.first_visible_column = 1
    
    worksheet1.first_visible_row = 1
    
    workbook.save(str(data_dir / "output.xls"))

make_cell_active()