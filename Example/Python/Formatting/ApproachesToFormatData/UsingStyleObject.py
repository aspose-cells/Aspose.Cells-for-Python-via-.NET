import os
from datetime import datetime
from aspose import pydrawing as drawing
import aspose.cells as cells
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Formatting" / "ApproachesToFormatData" / "UsingStyleObject"

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

    # Adding a new worksheet to the Excel object
    i = workbook.worksheets.add()

    # Obtaining the reference of the first worksheet by passing its sheet index
    worksheet = workbook.worksheets[i]

    # Accessing the "A1" cell from the worksheet
    cell = worksheet.cells.get("A1")

    # Adding some value to the "A1" cell
    cell.put_value("Hello Aspose!")
    
    # Adding a new Style
    style = workbook.create_style()

    # Setting the vertical alignment of the text in the "A1" cell
    style.vertical_alignment = cells.TextAlignmentType.CENTER

    # Setting the horizontal alignment of the text in the "A1" cell
    style.horizontal_alignment = cells.TextAlignmentType.CENTER

    # Setting the font color of the text in the "A1" cell
    style.font.color = drawing.Color.green

    # Shrinking the text to fit in the cell
    style.shrink_to_fit = True

    # Setting the bottom border color of the cell to red
    style.borders.get(cells.BorderType.BOTTOM_BORDER).color = drawing.Color.red

    # Setting the bottom border type of the cell to medium
    style.borders.get(cells.BorderType.BOTTOM_BORDER).line_style = cells.CellBorderType.MEDIUM

    # Assigning the Style object to the "A1" cell
    cell.set_style(style)


    # Apply the same style to some other cells
    worksheet.cells.get("B1").set_style(style)
    worksheet.cells.get("C1").set_style(style)
    worksheet.cells.get("D1").set_style(style)


    # Saving the Excel file
    workbook.save(os.path.join(data_dir, "book1.out.xls"))
    # ExEnd:1

if __name__ == "__main__":
    run()