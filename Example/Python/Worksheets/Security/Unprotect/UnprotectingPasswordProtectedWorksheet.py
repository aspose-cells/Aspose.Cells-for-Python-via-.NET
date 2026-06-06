import os
from datetime import datetime
from pathlib import Path
from aspose import pydrawing
from aspose.cells import Workbook
from aspose.pydrawing import Color

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / ".." / "Data" / "Worksheets/Security/Unprotect/UnprotectingPasswordProtectedWorksheet"

def run():
    # The path to the documents directory.
    data_dir = get_data_dir()
    
    # Instantiating a Workbook object
    workbook = Workbook(str(data_dir / "book1.xls"))
    
    # Accessing the first worksheet in the Excel file
    worksheet = workbook.worksheets[0]
    
    # Unprotecting the worksheet with a password
    worksheet.unprotect("")
    
    # Save Workbook
    workbook.save(str(data_dir / "output.out.xls"))

if __name__ == "__main__":
    run()