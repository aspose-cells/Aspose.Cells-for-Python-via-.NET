import os
from aspose import pydrawing as drawing
from aspose.cells import Workbook, SaveFormat
from datetime import datetime
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Formatting/ConfiguringAlignmentSettings/WrappingText"

def run():
    data_dir = get_data_dir()
    
    # Create directory if it is not already present
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
    
    # Enabling the text to be wrapped within the cell
    style.is_text_wrapped = True
    
    cell.set_style(style)
    
    # Saving the Excel file
    workbook.save(str(data_dir / "book1.out.xls"), SaveFormat.EXCEL_97_TO_2003)

if __name__ == "__main__":
    run()