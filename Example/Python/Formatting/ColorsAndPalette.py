import os
from datetime import datetime
from aspose.cells import Workbook, SaveFormat, BorderType
from aspose.pydrawing import Color

def get_data_dir():
    return os.path.join(os.path.dirname(__file__), "..", "..", "Data", "Formatting/ColorsAndPalette")

def run():
    data_dir = get_data_dir()

    # Create directory if it is not already present.
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)

    # Instantiating an Workbook object
    workbook = Workbook()

    # Adding Orchid color to the palette at 55th index
    workbook.change_palette(Color.orchid, 55)

    # Adding a new worksheet to the Excel object
    i = workbook.worksheets.add()

    # Obtaining the reference of the newly added worksheet by passing its sheet index
    worksheet = workbook.worksheets[i]

    # Accessing the "A1" cell from the worksheet
    cell = worksheet.cells.get("A1")

    # Adding some value to the "A1" cell
    cell.put_value("Hello Aspose!")

    # Defining new Style object
    style_object = workbook.create_style()
    # Setting the Orchid (custom) color to the font
    style_object.font.color = Color.orchid

    # Applying the style to the cell
    cell.set_style(style_object)

    # Saving the Excel file
    workbook.save(os.path.join(data_dir, "book1.out.xls"), SaveFormat.AUTO)

if __name__ == "__main__":
    run()