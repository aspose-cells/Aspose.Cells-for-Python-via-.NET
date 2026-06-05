from aspose.cells import Workbook
from aspose.pydrawing import Color
import os
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets/Display/DisplayHideGridlines"

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    # ExStart:1
    data_dir = get_data_dir()
    
    # Creating a file stream containing the Excel file to be opened
    file_path = os.path.join(data_dir, "book1.xls")
    
    # Instantiating a Workbook object
    # Opening the Excel file
    workbook = Workbook(file_path)
    
    # Accessing the first worksheet in the Excel file
    worksheet = workbook.worksheets[0]
    
    # Hiding the grid lines of the first worksheet of the Excel file
    worksheet.is_gridlines_visible = False
    
    # Saving the modified Excel file
    output_path = os.path.join(data_dir, "output.xls")
    workbook.save(output_path)
    # ExEnd:1

if __name__ == "__main__":
    run()