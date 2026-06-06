import os
from pathlib import Path
from datetime import datetime
import aspose.cells as cells
from aspose.pydrawing import Color

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets/Management/RemovingWorksheetsUsingSheetName"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    data_dir = get_data_dir()
    
    output_dir = get_output_directory()
    os.makedirs(output_dir, exist_ok=True)
    
    workbook = cells.Workbook(str(data_dir / "book1.xls"))
    
    workbook.worksheets.remove_at("Sheet1")
    
    workbook.save(str(output_dir / "output.out.xls"))

if __name__ == "__main__":
    run()