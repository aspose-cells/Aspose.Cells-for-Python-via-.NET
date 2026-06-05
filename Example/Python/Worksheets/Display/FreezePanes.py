import os
from datetime import datetime
from pathlib import Path
from aspose.pydrawing import Color
import aspose.cells as cells


def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets/Display/FreezePanes"


def main():
    data_dir = get_data_dir()
    
    # Creating a file stream containing the Excel file to be opened
    # Note: In Python, we use Workbook(file_path) directly instead ofFileStream
    workbook = cells.Workbook(str(data_dir / "book1.xls"))
    
    # Accessing the first worksheet in the Excel file
    worksheet = workbook.worksheets[0]
    
    # Applying freeze panes settings
    worksheet.freeze_panes(3, 2, 3, 2)
    
    # Saving the modified Excel file
    workbook.save(str(data_dir / "output.xls"))


if __name__ == "__main__":
    main()