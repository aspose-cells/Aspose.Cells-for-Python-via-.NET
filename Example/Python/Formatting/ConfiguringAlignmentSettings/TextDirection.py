import os
from aspose import pydrawing as drawing
from aspose.cells import Workbook, SaveFormat, TextDirectionType
from datetime import datetime
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Formatting/ConfiguringAlignmentSettings/TextDirection"

def run():
    # ExStart:1
    # The path to the documents directory.
    data_dir = get_data_dir()

    # Create directory if it is not already present.
    is_exists = os.path.isdir(data_dir)
    if not is_exists:
        os.makedirs(data_dir)

    # Instantiating a Workbook object
    workbook = Workbook()

    # Obtaining the reference of the worksheet
    worksheet = workbook.worksheets[0]

    # Accessing the "A1" cell from the worksheet
    cell = worksheet.cells.get("A1")

    # Adding some value to the "A1" cell
    cell.put_value("Visit Aspose!")

    # Setting the horizontal alignment of the text in the "A1" cell
    style = cell.get_style()

    # Setting the text direction from right to left
    style.text_direction = TextDirectionType.RIGHT_TO_LEFT

    cell.set_style(style)

    # Saving the Excel file
    workbook.save(os.path.join(data_dir, "book1.out.xls"), SaveFormat.EXCEL_97_TO_2003)
    # ExEnd:1

if __name__ == "__main__":
    run()