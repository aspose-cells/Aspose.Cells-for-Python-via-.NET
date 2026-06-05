import os
from datetime import datetime
from pathlib import Path
from aspose.cells import Workbook, ShiftType
from aspose.pydrawing import Color

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    out_dir = get_output_directory()
    os.makedirs(out_dir, exist_ok=True)
    
    workbook = Workbook()
    worksheet = workbook.worksheets[0]
    
    worksheet.cells.get(0, 2).value = 1
    worksheet.cells.get(1, 2).value = 2
    worksheet.cells.get(2, 2).value = 3
    worksheet.cells.get(2, 3).value = 4
    worksheet.cells.create_range(0, 2, 3, 1).name = "NamedRange"
    
    cut = worksheet.cells.create_range("C:C")
    worksheet.cells.insert_cut_cells(cut, 0, 1, ShiftType.RIGHT)
    workbook.save(str(out_dir / "CutAndPasteCells.xlsx"))
    
    print("CutAndPasteCells executed successfully.")

if __name__ == "__main__":
    run()