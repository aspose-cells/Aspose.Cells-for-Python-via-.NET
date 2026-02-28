import os
from aspose.cells import Workbook, Worksheet, FormatConditionCollection, FormatCondition, BorderType, CellBorderType, CellArea, FormatConditionType, OperatorType
from aspose.pydrawing import Color
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "Formatting/SetBorder"

def run():
    data_dir = get_data_dir()
    
    workbook = Workbook()
    sheet = workbook.worksheets[0]
    
    index = sheet.conditional_formattings.add()
    fcs = sheet.conditional_formattings[index]
    
    ca = CellArea()
    ca.start_row = 0
    ca.end_row = 5
    ca.start_column = 0
    ca.end_column = 3
    fcs.add_area(ca)
    
    condition_index = fcs.add_condition(FormatConditionType.CELL_VALUE, OperatorType.BETWEEN, "50", "100")
    
    fc = fcs[condition_index]
    borders = fc.style.borders
    
    borders.get(BorderType.LEFT_BORDER).line_style = CellBorderType.DASHED
    borders.get(BorderType.RIGHT_BORDER).line_style = CellBorderType.DASHED
    borders.get(BorderType.TOP_BORDER).line_style = CellBorderType.DASHED
    borders.get(BorderType.BOTTOM_BORDER).line_style = CellBorderType.DASHED
    
    borders.get(BorderType.LEFT_BORDER).color = Color(0, 255, 255)
    borders.get(BorderType.RIGHT_BORDER).color = Color(0, 255, 255)
    borders.get(BorderType.TOP_BORDER).color = Color(0, 255, 255)
    borders.get(BorderType.BOTTOM_BORDER).color = Color(255, 255, 0)
    
    workbook.save(os.path.join(data_dir, "output.xlsx"))

if __name__ == "__main__":
    run()