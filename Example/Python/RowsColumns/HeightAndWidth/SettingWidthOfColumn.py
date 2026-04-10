import os
import sys
from pathlib import Path
from datetime import datetime
import aspose.cells as cells

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "01_SourceDirectory"

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "RowsColumns/HeightAndWidth/SettingWidthOfColumn"

def run():
    data_dir = str(get_data_dir())
    
    fstream = open(os.path.join(data_dir, "book1.xls"), "rb")
    
    workbook = cells.Workbook(fstream)
    
    worksheet = workbook.worksheets[0]
    
    worksheet.cells.set_column_width(1, 17.5)
    
    workbook.save(os.path.join(data_dir, "output.out.xls"))
    
    fstream.close()

if __name__ == "__main__":
    run()