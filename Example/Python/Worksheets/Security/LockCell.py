import os
from datetime import datetime
from pathlib import Path
from aspose.cells import Workbook, ProtectionType
from aspose.pydrawing import Color

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Worksheets/Security/LockCell"

def main():
    data_dir = get_data_dir()
    workbook = Workbook(str(data_dir / "Book1.xlsx"))
    
    worksheet = workbook.worksheets[0]
    
    worksheet.cells.get("A1").get_style().is_locked = True
    worksheet.protect(ProtectionType.ALL)
    workbook.save(str(data_dir / "output.xlsx"))

if __name__ == "__main__":
    main()