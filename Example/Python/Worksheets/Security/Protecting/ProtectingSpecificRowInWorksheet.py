import os
from pathlib import Path
import aspose.cells as cells

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / ".." / "Data" / "Worksheets/Security/Protecting/ProtectingSpecificRowInWorksheet"

def protect_specific_row():
    data_dir = get_data_dir()
    
    # Create directory if it is not already present
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)
    
    # Create a new workbook
    wb = cells.Workbook()
    
    # Get the first worksheet
    sheet = wb.worksheets[0]
    
    # Unlock all cells first
    for row in range(sheet.cells.max_row + 1):
        for col in range(sheet.cells.max_column + 1):
            cell = sheet.cells.get(row, col)
            style = cell.get_style()
            style.is_locked = False
            cell.set_style(style)
    
    # Lock the first row (row index 0)
    for col in range(sheet.cells.max_column + 1):
        cell = sheet.cells.get(0, col)
        style = cell.get_style()
        style.is_locked = True
        cell.set_style(style)
    
    # Protect the sheet with all protection types
    sheet.protect(cells.ProtectionType.ALL)
    
    # Save the excel file
    output_path = os.path.join(data_dir, "output.out.xls")
    wb.save(output_path, cells.SaveFormat.EXCEL_97_TO_2003)

if __name__ == "__main__":
    protect_specific_row()