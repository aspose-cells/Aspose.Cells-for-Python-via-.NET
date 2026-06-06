import os
from aspose.cells import Workbook, SaveFormat, ProtectionType, StyleFlag
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / ".." / "Data" / "Worksheets/Security/Protecting/ProtectRowWorksheet"

def protect_row_worksheet():
    data_dir = get_data_dir()
    
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)
    
    wb = Workbook()
    sheet = wb.worksheets[0]
    
    # Unlock all columns (0 to 255)
    for i in range(256):
        style = wb.create_style()
        style.is_locked = False
        flag = StyleFlag()
        flag.locked = True
        sheet.cells.apply_column_style(i, style, flag)
    
    # Lock the first row
    style = wb.create_style()
    style.is_locked = True
    flag = StyleFlag()
    flag.locked = True
    sheet.cells.apply_row_style(0, style, flag)
    
    # Protect the sheet
    sheet.protect(ProtectionType.ALL)
    
    output_path = data_dir / "output.out.xls"
    wb.save(str(output_path), SaveFormat.EXCEL_97_TO_2003)

if __name__ == "__main__":
    protect_row_worksheet()