import os
from aspose import pydrawing as drawing
from aspose.cells import Workbook, Worksheet, Cell, Style, BorderType, CellBorderType
from datetime import datetime
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Formatting/Borders/AddingBordersToCells"

def run():
    data_dir = get_data_dir()
    
    # Create directory if it is not already present
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)
    
    # Instantiating a Workbook object
    workbook = Workbook()
    
    # Obtaining the reference of the first (default) worksheet by passing its sheet index
    worksheet = workbook.worksheets[0]
    
    # Accessing the "A1" cell from the worksheet
    cell = worksheet.cells.get("A1")
    
    # Adding some value to the "A1" cell
    cell.put_value("Visit Aspose!")
    
    # Create a style object
    style = cell.get_style()
    
    # Setting the line style of the top border
    style.borders.get(BorderType.TOP_BORDER).line_style = CellBorderType.THICK
    # Setting the color of the top border
    style.borders.get(BorderType.TOP_BORDER).color = drawing.Color.black
    
    # Setting the line style of the bottom border
    style.borders.get(BorderType.BOTTOM_BORDER).line_style = CellBorderType.THICK
    # Setting the color of the bottom border
    style.borders.get(BorderType.BOTTOM_BORDER).color = drawing.Color.black
    
    # Setting the line style of the left border
    style.borders.get(BorderType.LEFT_BORDER).line_style = CellBorderType.THICK
    # Setting the color of the left border
    style.borders.get(BorderType.LEFT_BORDER).color = drawing.Color.black
    
    # Setting the line style of the right border
    style.borders.get(BorderType.RIGHT_BORDER).line_style = CellBorderType.THICK
    # Setting the color of the right border
    style.borders.get(BorderType.RIGHT_BORDER).color = drawing.Color.black
    
    # Apply the border styles to the cell
    cell.set_style(style)
    
    # Saving the Excel file
    workbook.save(os.path.join(data_dir, "book1.out.xls"))

if __name__ == "__main__":
    run()