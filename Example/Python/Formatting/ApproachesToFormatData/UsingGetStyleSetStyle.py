import os
from datetime import datetime
from aspose.cells import Workbook, Worksheet, Cell, TextAlignmentType, BorderType, CellBorderType
from aspose.pydrawing import Color

def get_data_dir():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "Data", "Formatting/ApproachesToFormatData/UsingGetStyleSetStyle")

def run():
    data_dir = get_data_dir()
    
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)
    
    workbook = Workbook()
    worksheet = workbook.worksheets[0]
    cell = worksheet.cells.get("A1")
    cell.put_value("Hello Aspose!")
    
    style = cell.get_style()
    style.vertical_alignment = TextAlignmentType.CENTER
    style.horizontal_alignment = TextAlignmentType.CENTER
    style.font.color = Color.green
    style.shrink_to_fit = True
    bottom_border = style.borders.get(BorderType.BOTTOM_BORDER)
    bottom_border.color = Color.red
    bottom_border.line_style = CellBorderType.MEDIUM
    
    cell.set_style(style)
    
    workbook.save(os.path.join(data_dir, "book1.out.xls"))