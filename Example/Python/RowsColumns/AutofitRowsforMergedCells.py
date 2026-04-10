import os
from aspose.cells import Workbook, AutoFitterOptions, AutoFitMergedCellsType
from aspose.pydrawing import Color
from datetime import datetime
from pathlib import Path

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def Run():
    output_dir = str(get_output_directory())
    
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
    
    wb = Workbook()
    worksheet = wb.worksheets[0]
    
    range_obj = worksheet.cells.create_range(0, 0, 1, 2)
    range_obj.merge()
    
    worksheet.cells.get(0, 0).put_value("A quick brown fox jumps over the lazy dog. A quick brown fox jumps over the lazy dog....end")
    
    style = worksheet.cells.get(0, 0).get_style()
    style.is_text_wrapped = True
    worksheet.cells.get(0, 0).set_style(style)
    
    options = AutoFitterOptions()
    options.auto_fit_merged_cells_type = AutoFitMergedCellsType.EACH_LINE
    
    worksheet.auto_fit_rows(options)
    
    output_file = os.path.join(output_dir, "AutofitRowsforMergedCells.xlsx")
    wb.save(output_file)
    
    print("AutofitRowsforMergedCells executed successfully.\r\n")

if __name__ == "__main__":
    Run()