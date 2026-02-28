import os
from datetime import datetime
from aspose import pydrawing as draw
from aspose.cells import Workbook, Cell, BorderType
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "Formatting/FormattingSelectedCharacters"

def run():
    data_dir = get_data_dir()
    
    # Create directory if it is not already present
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)
    
    # Instantiating a Workbook object
    workbook = Workbook()
    
    # Obtaining the reference of the first(default) worksheet by passing its sheet index
    worksheet = workbook.worksheets[0]
    
    # Accessing the "A1" cell from the worksheet
    cell = worksheet.cells.get("A1")
    
    # Adding some value to the "A1" cell
    cell.put_value("Visit Aspose!")
    
    # Setting the font of selected characters to bold
    cell.characters(6, 7).font.is_bold = True
    
    # Setting the font color of selected characters to blue
    cell.characters(6, 7).font.color = draw.Color.blue
    
    # Saving the Excel file
    workbook.save(str(data_dir / "book1.out.xls"))

if __name__ == "__main__":
    run()