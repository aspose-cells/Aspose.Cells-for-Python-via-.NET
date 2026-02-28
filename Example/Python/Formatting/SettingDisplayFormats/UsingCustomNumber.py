import os
import datetime
from aspose.cells import Workbook, SaveFormat
from aspose.pydrawing import Color

def get_data_dir():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "Data", "Formatting/SettingDisplayFormats/UsingCustomNumber")

def Run():
    data_dir = get_data_dir()

    # Create directory if it is not already present.
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)

    # Instantiating a Workbook object
    workbook = Workbook()

    # Adding a new worksheet to the Excel object
    i = workbook.worksheets.add()

    # Obtaining the reference of the newly added worksheet by passing its sheet index
    worksheet = workbook.worksheets[i]

    # Adding the current system date to "A1" cell
    worksheet.cells.get("A1").put_value(datetime.datetime.now())

    # Getting the style of A1 cell
    style = worksheet.cells.get("A1").get_style()

    # Setting the custom display format to show date as "d-mmm-yy"
    style.custom = "d-mmm-yy"

    # Applying the style to A1 cell
    worksheet.cells.get("A1").set_style(style)

    # Adding a numeric value to "A2" cell
    worksheet.cells.get("A2").put_value(20)

    # Getting the style of A2 cell
    style = worksheet.cells.get("A2").get_style()

    # Setting the custom display format to show value as percentage
    style.custom = "0.0%"

    # Applying the style to A2 cell
    worksheet.cells.get("A2").set_style(style)

    # Adding a numeric value to "A3" cell
    worksheet.cells.get("A3").put_value(2546)

    # Getting the style of A3 cell
    style = worksheet.cells.get("A3").get_style()

    # Setting the custom display format to show value as currency
    style.custom = "£#,##0;[Red]$-#,##0"

    # Applying the style to A3 cell
    worksheet.cells.get("A3").set_style(style)

    # Saving the Excel file
    workbook.save(os.path.join(data_dir, "book1.out.xls"), SaveFormat.EXCEL_97_TO_2003)