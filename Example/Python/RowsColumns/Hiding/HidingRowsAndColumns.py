import os
from pathlib import Path
from datetime import datetime
import aspose.cells as cells

def get_source_directory(): 
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory(): 
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "RowsColumns/Hiding/HidingRowsAndColumns"

def run():
    data_dir = get_data_dir()
    
    fstream = open(os.path.join(data_dir, "book1.xls"), "rb")
    
    workbook = cells.Workbook(fstream)
    
    worksheet = workbook.worksheets[0]
    
    worksheet.cells.hide_row(2)
    
    worksheet.cells.hide_column(1)
    
    workbook.save(os.path.join(data_dir, "output.out.xls"))
    
    fstream.close()

if __name__ == "__main__":
    run()