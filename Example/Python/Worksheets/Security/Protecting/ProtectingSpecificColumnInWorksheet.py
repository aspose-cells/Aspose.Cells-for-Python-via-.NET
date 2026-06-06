import os
from aspose.cells import Workbook, SaveFormat, ProtectionType, Style, StyleFlag
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / ".." / "Data" / "Worksheets/Security/Protecting/ProtectingSpecificColumnInWorksheet"

def main():
    data_dir = get_data_dir()

    # Create directory if it is not already present.
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)

    # Create a new workbook.
    wb = Workbook()
    
    # Get the first worksheet.
    sheet = wb.worksheets[0]

    # Unlock all columns first (0 to 255)
    for i in range(256):
        style = wb.create_style()
        style.is_locked = False
        flag = StyleFlag()
        flag.locked = True
        sheet.cells.columns.get(i).apply_style(style, flag)

    # Lock the first column (index 0)
    style = wb.create_style()
    style.is_locked = True
    flag = StyleFlag()
    flag.locked = True
    sheet.cells.columns.get(0).apply_style(style, flag)

    # Protect the sheet.
    sheet.protect(ProtectionType.ALL)

    # Save the excel file.
    wb.save(os.path.join(data_dir, "output.out.xls"), SaveFormat.EXCEL_97_TO_2003)

if __name__ == "__main__":
    main()