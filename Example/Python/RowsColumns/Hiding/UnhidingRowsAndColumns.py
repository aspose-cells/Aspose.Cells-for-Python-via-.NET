import os
from datetime import datetime
from pathlib import Path
from aspose.cells import Workbook
from aspose.pydrawing import Color

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "RowsColumns/Hiding/UnhidingRowsAndColumns"

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    data_dir = get_data_dir()
    
    workbook = Workbook(os.path.join(data_dir, "book1.xls"))
    
    worksheet = workbook.worksheets[0]
    
    worksheet.cells.unhide_row(2, 13.5)
    worksheet.cells.unhide_column(1, 8.5)
    
    workbook.save(os.path.join(data_dir, "output.xls"))

if __name__ == "__main__":
    run()