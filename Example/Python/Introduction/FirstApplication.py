import os
from datetime import datetime
from aspose.cells import Workbook, SaveFormat
from pathlib import Path

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    output_dir = get_output_directory()
    
    wb = Workbook()
    
    sheet = wb.worksheets[0]
    
    cell = sheet.cells.get("A1")
    
    cell.put_value("Hello World!")
    
    output_path = os.path.join(output_dir, "outputFirstApplication.xlsx")
    wb.save(output_path, SaveFormat.XLSX)