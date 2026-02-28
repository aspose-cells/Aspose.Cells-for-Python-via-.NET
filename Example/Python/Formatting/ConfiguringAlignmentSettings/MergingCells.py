import os
from datetime import datetime
from pathlib import Path
import aspose.cells as cells
from aspose.pydrawing import Color

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Formatting/ConfiguringAlignmentSettings/MergingCells"

def run():
    # ExStart:1
    # The path to the documents directory.
    data_dir = get_data_dir()

    # Create directory if it is not already present.
    is_exists = os.path.isdir(data_dir)
    if not is_exists:
        os.makedirs(data_dir)

    # Instantiating a Workbook object
    workbook = cells.Workbook()

    # Obtaining the reference of the worksheet
    worksheet = workbook.worksheets[0]

    # Accessing the "A1" cell from the worksheet
    cell = worksheet.cells.get("A1")

    # Adding some value to the "A1" cell
    cell.put_value("Visit Aspose!")

    # Merging the first three columns in the first row to create a single cell
    worksheet.cells.merge(0, 0, 1, 3)

    # Saving the Excel file
    output_path = os.path.join(data_dir, "book1.out.xls")
    workbook.save(output_path, cells.SaveFormat.EXCEL_97_TO_2003)
    # ExEnd:1

if __name__ == "__main__":
    run()