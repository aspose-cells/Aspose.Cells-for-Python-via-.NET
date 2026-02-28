import os
from aspose import pydrawing as draw
from aspose.cells import Workbook, FormatConditionType, OperatorType, FontUnderlineType, CellArea

def get_data_dir():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Data", "Formatting/SetFont")

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
    fc.style.font.is_italic = True
    fc.style.font.is_bold = True
    fc.style.font.is_strikeout = True
    fc.style.font.underline = FontUnderlineType.DOUBLE
    fc.style.font.color = draw.Color.black
    
    output_path = os.path.join(data_dir, "output.xlsx")
    workbook.save(output_path)