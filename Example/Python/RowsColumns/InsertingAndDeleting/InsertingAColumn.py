import os
from datetime import datetime
from pathlib import Path
import aspose.cells as cells
from aspose.pydrawing import Color

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "RowsColumns/InsertingAndDeleting/InsertingAColumn"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    # ExStart:1
    data_dir = get_data_dir()
    output_dir = get_output_directory()
    
    # Creating a file stream containing the Excel file to be opened
    # In Python, we can directly open the file using Workbook constructor with file path
    file_path = os.path.join(data_dir, "book1.xls")
    workbook = cells.Workbook(file_path)
    
    # Accessing the first worksheet in the Excel file
    worksheet = workbook.worksheets[0]
    
    # Inserting a column into the worksheet at 2nd position (index 1)
    worksheet.cells.insert_column(1)
    
    # Saving the modified Excel file
    output_path = os.path.join(output_dir, "output.out.xls")
    workbook.save(output_path)
    # ExEnd:1

if __name__ == "__main__":
    run()