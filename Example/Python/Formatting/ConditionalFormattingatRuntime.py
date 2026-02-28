import os
from datetime import datetime
from aspose import pydrawing as drawing
import aspose.cells as cells

def get_data_dir():
    return os.path.join(os.path.dirname(__file__), "..", "..", "Data", "Formatting/ConditionalFormattingatRuntime")

def Run():
    data_dir = get_data_dir()
    file_path = os.path.join(data_dir, "Book1.xlsx")
    
    workbook = cells.Workbook()
    sheet = workbook.worksheets[0]
    
    index = sheet.conditional_formattings.add()
    fcs = sheet.conditional_formattings[index]
    
    ca = cells.CellArea()
    ca.start_row = 0
    ca.end_row = 0
    ca.start_column = 0
    ca.end_column = 0
    fcs.add_area(ca)
    
    ca = cells.CellArea()
    ca.start_row = 1
    ca.end_row = 1
    ca.start_column = 1
    ca.end_column = 1
    fcs.add_area(ca)
    
    condition_index = fcs.add_condition(cells.FormatConditionType.CELL_VALUE, cells.OperatorType.BETWEEN, "=A2", "100")
    
    condition_index2 = fcs.add_condition(cells.FormatConditionType.CELL_VALUE, cells.OperatorType.BETWEEN, "50", "100")
    
    fc = fcs[condition_index]
    fc.style.background_color = drawing.Color.red
    
    output_path = os.path.join(data_dir, "output.xls")
    workbook.save(output_path)

Run()