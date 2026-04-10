import os
from pathlib import Path
from datetime import datetime
from aspose.cells import Workbook
from aspose.pydrawing import Color

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "RowsColumns/HeightAndWidth/SetColumnViewWidthInPixels"

def run():
    source_dir = get_source_directory()
    out_dir = get_output_directory()
    
    workbook = Workbook(str(source_dir / "Book1.xlsx"))
    
    worksheet = workbook.worksheets[0]
    
    worksheet.cells.set_view_column_width_pixel(7, 200)
    
    workbook.save(str(out_dir / "SetColumnViewWidthInPixels_Out.xlsx"))

if __name__ == "__main__":
    run()