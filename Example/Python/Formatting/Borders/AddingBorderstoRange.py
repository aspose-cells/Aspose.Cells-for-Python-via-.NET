import os
from datetime import datetime
from aspose.cells import Workbook, Worksheet, BorderType, CellBorderType
from aspose.pydrawing import Color

def get_data_dir():
    return os.path.join(os.path.dirname(__file__), "..", "..", "..", "Data", "Formatting/Borders/AddingBorderstoRange")

def run():
    data_dir = get_data_dir()
    
    # Create directory if it is not already present.
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)
    
    # Instantiating a Workbook object
    workbook = Workbook()
    
    # Obtaining the reference of the first (default) worksheet by passing its sheet index
    worksheet = workbook.worksheets[0]
    
    # Accessing the "A1" cell from the worksheet
    cell = worksheet.cells.get("A1")
    
    # Adding some value to the "A1" cell
    cell.put_value("Hello World From Aspose")
    
    # Creating a range of cells starting from "A1" cell to 3rd column in a row
    range_obj = worksheet.cells.create_range(0, 0, 1, 3)
    
    # Adding a thick top border with blue line
    range_obj.set_outline_border(BorderType.TOP_BORDER, CellBorderType.THICK, Color.blue)
    
    # Adding a thick bottom border with blue line
    range_obj.set_outline_border(BorderType.BOTTOM_BORDER, CellBorderType.THICK, Color.blue)
    
    # Adding a thick left border with blue line
    range_obj.set_outline_border(BorderType.LEFT_BORDER, CellBorderType.THICK, Color.blue)
    
    # Adding a thick right border with blue line
    range_obj.set_outline_border(BorderType.RIGHT_BORDER, CellBorderType.THICK, Color.blue)
    
    # Saving the Excel file
    workbook.save(os.path.join(data_dir, "book1.out.xls"))

if __name__ == "__main__":
    run()