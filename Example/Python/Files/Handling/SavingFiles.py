import os
from pathlib import Path
import aspose.cells as cells

def get_data_dir():
    return (Path(__file__).parent.parent.parent
            / "Data"
            / "Files"
            / "Handling"
            / "SavingFiles")

data_dir = get_data_dir()
os.makedirs(data_dir, exist_ok=True)

# Create a new Workbook
workbook = cells.Workbook()

# Save in Excel 97‑2003 format
workbook.save(str(data_dir / "book1.out.xls"))
workbook.save(str(data_dir / "book1.out.xls"), cells.SaveFormat.EXCEL_97_TO_2003)

# Save in Excel2007 xlsx format
workbook.save(str(data_dir / "book1.out.xlsx"))

# Save in Excel2007 xlsb format
workbook.save(str(data_dir / "book1.out.xlsb"))

# Save in ODS format
workbook.save(str(data_dir / "book1.out.ods"))

# Save in PDF format
workbook.save(str(data_dir / "book1.out.pdf"))

# Save in HTML format
workbook.save(str(data_dir / "book1.out.html"))

# Save in SpreadsheetML format
workbook.save(str(data_dir / "book1.out.xml"))