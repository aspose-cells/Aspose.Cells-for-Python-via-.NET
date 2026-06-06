import os
from datetime import datetime
from aspose.cells import Workbook
from aspose.pydrawing import Color
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets/Value/CopyWorksheetsBetweenWorkbooks"

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    data_dir = get_data_dir()
    
    input_path = os.path.join(str(data_dir), "book1.xls")
    
    # Create a Workbook.
    # Open a file into the first book.
    excel_workbook0 = Workbook(input_path)
    
    # Create another Workbook.
    excel_workbook1 = Workbook()
    
    # Copy the first sheet of the first book into second book.
    excel_workbook1.worksheets[0].copy(excel_workbook0.worksheets[0])
    
    # Save the file.
    output_path = os.path.join(str(data_dir), "CopyWorksheetsBetweenWorkbooks_out.xls")
    excel_workbook1.save(output_path)

if __name__ == "__main__":
    run()