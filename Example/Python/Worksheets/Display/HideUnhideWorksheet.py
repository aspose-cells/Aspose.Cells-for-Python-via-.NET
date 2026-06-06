import os
from aspose.cells import Workbook
from aspose.pydrawing import Color
from datetime import datetime
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets/Display/HideUnhideWorksheet"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    data_dir = get_data_dir()
    output_dir = get_output_directory()
    
    # Creating a file stream containing the Excel file to be opened
    with open(os.path.join(data_dir, "book1.xls"), "rb") as fstream:
        # Instantiating a Workbook object with opening the Excel file through the file stream
        workbook = Workbook(fstream)
        
        # Accessing the first worksheet in the Excel file
        worksheet = workbook.worksheets[0]
        
        # Hiding the first worksheet of the Excel file
        worksheet.is_visible = False
        
        # Saving the modified Excel file in default (that is Excel 2003) format
        workbook.save(os.path.join(output_dir, "output.out.xls"))

if __name__ == "__main__":
    run()