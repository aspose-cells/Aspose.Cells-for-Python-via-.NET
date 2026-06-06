import os
from pathlib import Path
from aspose.cells import Workbook
from datetime import datetime

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets/Display/RemovePanes"

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    data_dir = get_data_dir()
    
    # Instantiate a new workbook and Open a template file
    book = Workbook(os.path.join(data_dir, "Book1.xls"))
    
    # Set the active cell
    book.worksheets[0].active_cell = "A20"
    
    # Split the worksheet window
    book.worksheets[0].remove_split()
    
    # Save the excel file
    book.save(os.path.join(data_dir, "output.xls"))

if __name__ == "__main__":
    run()