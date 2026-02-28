import os
from datetime import datetime
from aspose.cells import Workbook, SaveFormat
from aspose.pydrawing import Color

def get_data_dir():
    return os.path.join(os.path.dirname(__file__), "..", "..", "..", "Data", "Formatting/DealingWithFontSettings/SettingFontName")

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

    # Adding a new worksheet to the Excel object
    i = workbook.worksheets.add()

    # Obtaining the reference of the newly added worksheet by passing its sheet index
    worksheet = workbook.worksheets[i]

    # Accessing the "A1" cell from the worksheet
    cell = worksheet.cells.get("A1")

    # Adding some value to the "A1" cell
    cell.put_value("Hello Aspose!")

    # Obtaining the style of the cell
    style = cell.get_style()

    # Setting the font name to "Times New Roman"
    style.font.name = "Times New Roman"

    # Applying the style to the cell
    cell.set_style(style)

    # Saving the Excel file
    workbook.save(os.path.join(data_dir, "book1.out.xls"), SaveFormat.EXCEL_97_TO_2003)
    # ExEnd:1

run()