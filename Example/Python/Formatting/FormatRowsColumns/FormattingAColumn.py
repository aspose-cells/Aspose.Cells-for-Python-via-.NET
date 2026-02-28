import os
from aspose.cells import Workbook, Worksheet, Style, StyleFlag, TextAlignmentType, CellBorderType, BorderType
from aspose.pydrawing import Color
from datetime import datetime
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Formatting/FormatRowsColumns/FormattingAColumn"

def run():
    data_dir = get_data_dir()
    
    # Create directory if it is not already present.
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)
    
    # Instantiating a Workbook object
    workbook = Workbook()
    
    # Obtaining the reference of the first (default) worksheet by passing its sheet index
    worksheet = workbook.worksheets[0]
    
    # Adding a new Style to the styles
    style = workbook.create_style()
    
    # Setting the vertical alignment of the text in the "A1" cell
    style.vertical_alignment = TextAlignmentType.CENTER
    
    # Setting the horizontal alignment of the text in the "A1" cell
    style.horizontal_alignment = TextAlignmentType.CENTER
    
    # Setting the font color of the text in the "A1" cell
    style.font.color = Color.green
    
    # Shrinking the text to fit in the cell
    style.shrink_to_fit = True
    
    # Setting the bottom border color of the cell to red
    style.borders.get(BorderType.BOTTOM_BORDER).color = Color.red
    
    # Setting the bottom border type of the cell to medium
    style.borders.get(BorderType.BOTTOM_BORDER).line_style = CellBorderType.MEDIUM
    
    # Creating StyleFlag
    style_flag = StyleFlag()
    style_flag.horizontal_alignment = True
    style_flag.vertical_alignment = True
    style_flag.shrink_to_fit = True
    style_flag.borders = True
    style_flag.font_color = True
    
    # Accessing a column from the Columns collection
    column = worksheet.cells.columns[0]
    
    # Applying the style to the column
    column.apply_style(style, style_flag)
    
    # Saving the Excel file
    workbook.save(os.path.join(data_dir, "book1.out.xls"))