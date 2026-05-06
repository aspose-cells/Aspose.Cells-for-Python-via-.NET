import os
from datetime import datetime
from aspose.cells import Workbook
from aspose.cells.tables import TableToRangeOptions
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "Tables/ConvertTableToRangeWithOptions"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    data_dir = get_data_dir()
    
    workbook = Workbook(str(data_dir / "book1.xlsx"))
    
    options = TableToRangeOptions()
    options.last_row = 5
    
    workbook.worksheets[0].list_objects[0].convert_to_range(options)
    
    output_dir = get_output_directory()
    os.makedirs(str(output_dir), exist_ok=True)
    
    workbook.save(str(output_dir / "output.xlsx"))

if __name__ == "__main__":
    run()