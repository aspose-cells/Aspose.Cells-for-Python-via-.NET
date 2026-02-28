import os
from aspose import pydrawing as drawing
from aspose.cells import Workbook, Worksheet, BorderType, BackgroundType, FormatConditionType, OperatorType, CellArea
from datetime import datetime
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "Formatting/SetPattern"

def main():
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
    fc.style.pattern = BackgroundType.REVERSE_DIAGONAL_STRIPE
    fc.style.foreground_color = drawing.Color.from_argb(255, 255, 0)
    fc.style.background_color = drawing.Color.from_argb(0, 255, 255)
    
    workbook.save(os.path.join(str(data_dir), "output.xlsx"))

if __name__ == "__main__":
    main()