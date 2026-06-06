import os
from datetime import datetime
from pathlib import Path
from aspose import pydrawing as drawing
from aspose.cells import Workbook

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets/Management/AccessingWorksheetsusingSheetName"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"

def main():
    data_dir = get_data_dir()
    input_path = str(data_dir / "book1.xlsx")
    
    # Instantiating a Workbook object
    # Opening the Excel file
    workbook = Workbook(input_path)
    
    # Accessing a worksheet using its sheet name
    worksheet = workbook.worksheets.get("Sheet1")
    cell = worksheet.cells.get("A1")
    print(cell.value)

if __name__ == "__main__":
    main()