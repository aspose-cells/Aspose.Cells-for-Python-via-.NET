import os
from datetime import datetime
from pathlib import Path
from aspose.cells import Workbook
from aspose.pydrawing import Color

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "RowsColumns/InsertingAndDeleting/DeletingMultipleRows"

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    data_dir = get_data_dir()
    
    workbook = Workbook(os.path.join(data_dir, "Book1.xlsx"))
    
    worksheet = workbook.worksheets[0]
    
    worksheet.cells.delete_rows(2, 10)
    
    workbook.save(os.path.join(data_dir, "output.xlsx"))

if __name__ == "__main__":
    run()