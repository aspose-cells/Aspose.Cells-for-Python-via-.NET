import os
from datetime import datetime
from pathlib import Path
from aspose.pydrawing import Color
import aspose.cells as cells

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "RowsColumns/HeightAndWidth/SetWidthAllColumns"

def run():
    data_dir = get_data_dir()
    
    # Create directory if it is not already present.
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)
    
    # Opening the Excel file through the file path
    workbook = cells.Workbook(str(data_dir / "book1.xls"))
    
    # Accessing the first worksheet in the Excel file
    worksheet = workbook.worksheets[0]
    
    # Setting the width of all columns in the worksheet to 20.5
    worksheet.cells.standard_width = 20.5
    
    # Saving the modified Excel file
    workbook.save(str(data_dir / "output.out.xls"))

if __name__ == "__main__":
    run()