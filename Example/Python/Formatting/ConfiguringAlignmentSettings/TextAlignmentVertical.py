import os
from aspose import pydrawing as drawing
from aspose.cells import Workbook, SaveFormat, TextAlignmentType
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Formatting/ConfiguringAlignmentSettings/TextAlignmentVertical"

def main():
    data_dir = get_data_dir()
    
    # Create directory if it is not already present
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)
    
    # Instantiating a Workbook object
    workbook = Workbook()
    
    # Clearing all the worksheets
    workbook.worksheets.clear()
    
    # Adding a new worksheet to the Excel object
    i = workbook.worksheets.add()
    
    # Obtaining the reference of the newly added worksheet by passing its sheet index
    worksheet = workbook.worksheets[i]
    
    # Accessing the "A1" cell from the worksheet
    cell = worksheet.cells.get("A1")
    
    # Adding some value to the "A1" cell
    cell.put_value("Visit Aspose!")
    
    # Setting the horizontal alignment of the text in the "A1" cell
    style = cell.get_style()
    
    # Setting the vertical alignment of the text in a cell
    style.vertical_alignment = TextAlignmentType.CENTER
    
    cell.set_style(style)
    
    # Saving the Excel file
    workbook.save(os.path.join(data_dir, "book1.out.xls"), SaveFormat.EXCEL_97_TO_2003)

if __name__ == "__main__":
    main()