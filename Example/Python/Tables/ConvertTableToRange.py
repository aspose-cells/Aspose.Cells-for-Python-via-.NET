import os
from pathlib import Path
from datetime import datetime

import aspose.cells as cells

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "Tables/ConvertTableToRange"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    data_dir = get_data_dir()
    
    wb = cells.Workbook(str(data_dir / "book1.xlsx"))
    
    wb.worksheets[0].list_objects[0].convert_to_range()
    
    output_dir = get_output_directory()
    os.makedirs(output_dir, exist_ok=True)
    
    wb.save(str(output_dir / "output.xlsx"))

if __name__ == "__main__":
    run()