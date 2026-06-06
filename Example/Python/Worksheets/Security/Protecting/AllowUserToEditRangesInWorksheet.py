import os
from pathlib import Path
from datetime import datetime
from aspose.cells import Workbook, ProtectionType

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / ".." / "Data" / "Worksheets/Security/Protecting/AllowUserToEditRangesInWorksheet"

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    data_dir = get_data_dir()
    
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)
    
    book = Workbook()
    sheet = book.worksheets[0]
    allow_ranges = sheet.allow_edit_ranges
    
    idx = allow_ranges.add("r2", 1, 1, 3, 3)
    proteced_range = allow_ranges[idx]
    proteced_range.password = "123"
    
    sheet.protect(ProtectionType.ALL)
    
    output_path = data_dir / "protectedrange.out.xls"
    book.save(str(output_path))

if __name__ == "__main__":
    run()