import aspose.cells as cells
import os
from pathlib import Path
from datetime import datetime
from aspose.pydrawing import Color


def get_data_dir():
    return (
        Path(__file__).parent
        / ".."
        / ".."
        / ".."
        / "Data"
        / "Files"
        / "Handling"
        / "OpeningFiles"
    ).resolve()


data_dir = get_data_dir()

# 1. Opening through Path
workbook1 = cells.Workbook(str(data_dir / "Book1.xls"))
print("Workbook opened using path successfully!")

# 2. Opening through Stream
with open(data_dir / "Book2.xls", "rb") as fstream:
    workbook2 = cells.Workbook(fstream)
    print("Workbook opened using stream successfully!")

# 3. Opening Microsoft Excel 97 - 2003 Files
with open(data_dir / "Book_Excel97_2003.xls", "rb") as stream:
    load_options1 = cells.LoadOptions(cells.LoadFormat.EXCEL_97_TO_2003)
    wb_excel97 = cells.Workbook(stream, load_options1)
    print("Microsoft Excel 97 - 2003 workbook opened successfully!")

# 4. Opening Microsoft Excel 2007 Xlsx Files
load_options2 = cells.LoadOptions(cells.LoadFormat.XLSX)
wb_excel2007 = cells.Workbook(str(data_dir / "Book_Excel2007.xlsx"), load_options2)
print("Microsoft Excel 2007 workbook opened successfully!")

# 5. Opening SpreadsheetML Files
load_options3 = cells.LoadOptions(cells.LoadFormat.SPREADSHEET_ML)
wb_spreadsheetml = cells.Workbook(str(data_dir / "Book3.xml"), load_options3)
print("SpreadSheetML file opened successfully!")

# 6. Opening csv Files
load_options4 = cells.LoadOptions(cells.LoadFormat.CSV)
wb_csv = cells.Workbook(str(data_dir / "Book_CSV.csv"), load_options4)
print("CSV file opened successfully!")

# 7. Opening Tab Delimited Files
load_options5 = cells.LoadOptions(cells.LoadFormat.TAB_DELIMITED)
wb_tab_delimited = cells.Workbook(str(data_dir / "Book1TabDelimited.txt"), load_options5)
print("Tab delimited file opened successfully!")

# 8. Opening Encrypted Excel Files
load_options6 = cells.LoadOptions()
load_options6.password = "1234"
wb_encrypted = cells.Workbook(str(data_dir / "encryptedBook.xls"), load_options6)
print("Encrypted excel file opened successfully!")

# 9. Opening File with Data only
load_options7 = cells.LoadOptions(cells.LoadFormat.XLSX)
load_options7.load_filter = cells.LoadFilter(cells.LoadDataFilterOptions.CELL_DATA)
wb_partial = cells.Workbook(str(data_dir / "Book1.xlsx"), load_options7)

# 10. Opening Excel95/5.0 XLS Files
load_options_excel95 = cells.LoadOptions(cells.LoadFormat.AUTO)
wb_excel95 = cells.Workbook(str(data_dir / "Excel95_5.0.xls"), load_options_excel95)
print("Excel95/5.0 XLS opened successfully!")