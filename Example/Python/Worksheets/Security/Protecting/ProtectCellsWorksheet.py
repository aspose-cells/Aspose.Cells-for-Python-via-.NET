import os
from aspose.cells import Workbook, SaveFormat, ProtectionType, StyleFlag

def get_data_dir():
    return os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "Data", "Worksheets", "Security", "Protecting", "ProtectCellsWorksheet")

def run():
    data_dir = get_data_dir()
    
    # Create directory if it is not already present.
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)
    
    # Create a new workbook.
    wb = Workbook()
    
    # Create a worksheet object and obtain the first sheet.
    sheet = wb.worksheets[0]
    
    # Unlock all cells first
    style = wb.create_style()
    style.is_locked = False
    style_flag = StyleFlag()
    style_flag.locked = True
    
    # Apply unlocked style to all cells in the sheet
    sheet.cells.apply_style(style, style_flag)
    
    # Lock cells A1, B1, C1
    for cell_name in ["A1", "B1", "C1"]:
        cell = sheet.cells.get(cell_name)
        style = cell.get_style()
        style.is_locked = True
        cell.set_style(style)
    
    # Protect the sheet
    sheet.protect(ProtectionType.ALL)
    
    # Save the excel file.
    output_path = os.path.join(data_dir, "output.xls")
    wb.save(output_path, SaveFormat.EXCEL_97_TO_2003)

if __name__ == "__main__":
    run()