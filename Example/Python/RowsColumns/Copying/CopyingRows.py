import os
from datetime import datetime
from pathlib import Path
from aspose.cells import Workbook
from aspose.pydrawing import Color

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "RowsColumns/Copying/CopyingRows"

def main():
    data_dir = get_data_dir()
    
    # ExStart:1
    # Open the existing excel file.
    excel_workbook1 = Workbook(str(data_dir / "book1.xls"))
    
    # Get the first worksheet in the workbook.
    ws_template = excel_workbook1.worksheets[0]
    
    # Copy the second row with data, formattings, images and drawing objects
    # To the 16th row in the worksheet.
    ws_template.cells.copy_row(ws_template.cells, 1, 15)
    
    # Save the excel file.
    excel_workbook1.save(str(data_dir / "output.xls"))
    # ExEnd:1

if __name__ == "__main__":
    main()