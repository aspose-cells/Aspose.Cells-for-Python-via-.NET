from aspose.cells import Workbook
from aspose.pydrawing import Color
import os
from pathlib import Path

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def main():
    # ExStart:1
    #Source directory
    source_dir = get_source_directory()
    
    #Load source Excel file
    workbook = Workbook(str(source_dir / "BookWithSomeData.xlsx"))
    
    #Access first worksheet
    worksheet = workbook.worksheets[0]
    
    #Print number of cells in the Worksheet
    print("Number of Cells: " + str(worksheet.cells.count))
    
    # If the number of cells is greater than 2147483647, use CountLarge
    print("Number of Cells (CountLarge): " + str(worksheet.cells.count_large))
    # ExEnd:1

if __name__ == "__main__":
    main()