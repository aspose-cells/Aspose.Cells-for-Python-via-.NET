import os
from datetime import datetime
from pathlib import Path

import aspose.cells as cells
from aspose.pydrawing import Color

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets/Display/SplitPanes"

def run():
    data_dir = get_data_dir()
    
    book = cells.Workbook(str(data_dir / "Book1.xls"))
    
    book.worksheets[0].active_cell = "A20"
    
    book.worksheets[0].split()
    
    book.save(str(data_dir / "output.xls"))

if __name__ == "__main__":
    run()