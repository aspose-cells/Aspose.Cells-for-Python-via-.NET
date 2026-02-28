import os
from datetime import datetime
from aspose.cells import Workbook, SaveFormat
from aspose.pydrawing import Color

def get_data_dir():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "Data", "Formatting/ConfiguringAlignmentSettings/ShrinkingToFit")

def run():
    # ExStart:1
    # The path to the documents directory.
    data_dir = get_data_dir()

    # Create directory if it is not already present.
    if not os.path.isdir(data_dir):
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

    # Shrinking the text to fit according to the dimensions of the cell
    style.shrink_to_fit = True

    cell.set_style(style)

    # Saving the Excel file
    workbook.save(os.path.join(data_dir, "book1.out.xls"), SaveFormat.EXCEL_97_TO_2003)
    # ExEnd:1

if __name__ == "__main__":
    run()