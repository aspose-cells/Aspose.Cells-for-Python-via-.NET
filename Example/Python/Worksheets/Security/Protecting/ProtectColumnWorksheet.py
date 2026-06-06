import os
from aspose.cells import Workbook, Style, StyleFlag, ProtectionType, SaveFormat
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / ".." / "Data" / "Worksheets/Security/Protecting/ProtectColumnWorksheet"

def main():
    data_dir = get_data_dir()
    
    # Create directory if it is not already present.
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)
    
    # Create a new workbook (this automatically creates one worksheet by default)
    wb = Workbook()
    
    # Get the first worksheet
    sheet = wb.worksheets[0]
    
    # Loop through all the columns in the worksheet and unlock them
    for i in range(256):
        col = sheet.cells.columns.get(i)
        style = col.style
        style.is_locked = False
        flag = StyleFlag()
        flag.locked = True
        col.apply_style(style, flag)
    
    # Get the first column style
    col = sheet.cells.columns.get(0)
    style = col.style
    
    # Lock it
    style.is_locked = True
    
    # Instantiate the flag
    flag = StyleFlag()
    
    # Set the lock setting
    flag.locked = True
    
    # Apply the style to the first column
    col.apply_style(style, flag)
    
    # Protect the sheet
    sheet.protect(ProtectionType.ALL)
    
    # Save the excel file
    output_path = os.path.join(data_dir, "output.out.xls")
    wb.save(output_path, SaveFormat.EXCEL_97_TO_2003)

if __name__ == "__main__":
    main()