import os
from datetime import datetime
from aspose import pydrawing as drawing
from aspose.cells import Workbook, SaveFormat, BorderType

def get_data_dir():
    return os.path.join(os.path.dirname(__file__), "..", "..", "..", "Data", "Formatting/SettingDisplayFormats/UsingBuiltInNumberFormats")

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

    # Obtaining the reference of first worksheet
    worksheet = workbook.worksheets[0]

    # Adding the current system date to "A1" cell
    worksheet.cells.get("A1").put_value(datetime.now())

    # Getting the Style of the A1 Cell
    style = worksheet.cells.get("A1").get_style()

    # Setting the display format to number 15 to show date as "d-mmm-yy"
    style.number = 15

    # Applying the style to the A1 cell
    worksheet.cells.get("A1").set_style(style)

    # Adding a numeric value to "A2" cell
    worksheet.cells.get("A2").put_value(20)

    # Getting the Style of the A2 Cell
    style = worksheet.cells.get("A2").get_style()

    # Setting the display format to number 9 to show value as percentage
    style.number = 9

    # Applying the style to the A2 cell
    worksheet.cells.get("A2").set_style(style)

    # Adding a numeric value to "A3" cell
    worksheet.cells.get("A3").put_value(2546)

    # Getting the Style of the A3 Cell
    style = worksheet.cells.get("A3").get_style()

    # Setting the display format to number 6 to show value as currency
    style.number = 6

    # Applying the style to the A3 cell
    worksheet.cells.get("A3").set_style(style)

    # Saving the Excel file
    workbook.save(os.path.join(data_dir, "book1.out.xls"), SaveFormat.EXCEL_97_TO_2003)
    # ExEnd:1

if __name__ == "__main__":
    run()