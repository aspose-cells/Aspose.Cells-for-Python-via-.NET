import os
from pathlib import Path
from datetime import datetime
from aspose.pydrawing import Color
import aspose.cells as cells

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Formatting/ApproachesToFormatData/UsingExcelPredefinedStyles"

def Run():
    data_dir = get_data_dir()

    # Create directory if it is not already present.
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)

    # Instantiate a new Workbook.
    workbook = cells.Workbook()

    # Create a style object .
    style = workbook.create_style()

    # Input a value to A1 cell.
    workbook.worksheets[0].cells.get("A1").put_value("Test")

    # Apply the style to the cell.
    workbook.worksheets[0].cells.get("A1").set_style(style)

    # Save the Excel 2007 file.
    workbook.save(os.path.join(data_dir, "book1.out.xlsx"))