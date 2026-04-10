import os
from datetime import datetime
from pathlib import Path
from aspose.cells import Workbook
from aspose.pydrawing import Color

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "RowsColumns/InsertingAndDeleting/InsertingMultipleRows"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    data_dir = get_data_dir()
    output_dir = get_output_directory()
    
    # Creating a file stream containing the Excel file to be opened
    fstream = open(data_dir / "book1.xls", "rb")
    
    # Instantiating a Workbook object
    # Opening the Excel file through the file stream
    workbook = Workbook(fstream)
    
    # Accessing the first worksheet in the Excel file
    worksheet = workbook.worksheets[0]
    
    # Inserting 10 rows into the worksheet starting from 3rd row
    worksheet.cells.insert_rows(2, 10)
    
    # Saving the modified Excel file
    workbook.save(os.path.join(output_dir, "output.out.xls"))
    
    # Closing the file stream to free all resources
    fstream.close()

if __name__ == "__main__":
    run()