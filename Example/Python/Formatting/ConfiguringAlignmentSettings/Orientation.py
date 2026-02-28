import os
from datetime import datetime
from pathlib import Path
from aspose import cells
from aspose.cells import Workbook, SaveFormat
from aspose.pydrawing import Color

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Formatting/ConfiguringAlignmentSettings/Orientation"

def run():
    data_dir = get_data_dir()
    
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)
    
    workbook = Workbook()
    worksheet = workbook.worksheets[0]
    cell = worksheet.cells.get("A1")
    cell.put_value("Visit Aspose!")
    
    style = cell.get_style()
    style.rotation_angle = 25
    cell.set_style(style)
    
    workbook.save(os.path.join(data_dir, "book1.out.xls"), SaveFormat.EXCEL_97_TO_2003)

if __name__ == "__main__":
    run()