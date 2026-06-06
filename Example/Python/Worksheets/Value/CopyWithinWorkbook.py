import os
from pathlib import Path
from datetime import datetime
from aspose.cells import Workbook
from aspose.pydrawing import Color

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets/Value/CopyWithinWorkbook"

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    data_dir = get_data_dir()
    input_path = str(data_dir / "book1.xls")
    
    # Open an existing Excel file.
    wb = Workbook(input_path)
    
    # Create a WorksheetCollection object with reference to
    # the sheets of the Workbook.
    sheets = wb.worksheets
    
    # Copy data to a new sheet from an existing
    # sheet within the Workbook.
    sheets.add_copy("Sheet1")
    
    # Save the Excel file.
    output_path = str(data_dir / "CopyWithinWorkbook_out.xls")
    wb.save(output_path)

if __name__ == "__main__":
    run()