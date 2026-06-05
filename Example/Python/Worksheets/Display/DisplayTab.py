import os
from aspose.cells import Workbook
from datetime import datetime
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets/Display/DisplayTab"

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    data_dir = get_data_dir()
    
    workbook = Workbook(str(data_dir / "book1.xls"))
    
    workbook.settings.show_tabs = True
    
    output_dir = get_output_directory()
    os.makedirs(output_dir, exist_ok=True)
    workbook.save(str(output_dir / "output.xls"))

if __name__ == "__main__":
    run()