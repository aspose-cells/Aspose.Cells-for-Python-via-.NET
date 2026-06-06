import os
from pathlib import Path
from aspose.cells import Workbook, SaveFormat, ProtectionType

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / ".." / "Data" / "Worksheets/Security/ProtectingSpecificCellsinaWorksheet"

if __name__ == "__main__":
    data_dir = get_data_dir()
    
    # Create directory if it is not already present.
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)
    
    # Create a new workbook.
    wb = Workbook()
    
    # Get the first worksheet.
    sheet = wb.worksheets[0]
    
    # Unlock all cells in the worksheet (default locked state is true when sheet is protected)
    style = wb.create_style()
    style.is_locked = False
    
    # Apply unlock style to all cells in columns 0-255 (A to IV in Excel 97-2003)
    for row in range(65536):
        for col in range(256):
            cell = sheet.cells.get(row, col)
            cell.set_style(style)
    
    # Lock specific cells A1, B1, C1
    lock_style = wb.create_style()
    lock_style.is_locked = True
    
    for cell_addr in ["A1", "B1", "C1"]:
        cell = sheet.cells.get(cell_addr)
        cell.set_style(lock_style)
    
    # Protect the sheet
    sheet.protect(ProtectionType.ALL)
    
    # Save the excel file.
    output_path = os.path.join(data_dir, "output.out.xls")
    wb.save(output_path, SaveFormat.EXCEL_97_TO_2003)