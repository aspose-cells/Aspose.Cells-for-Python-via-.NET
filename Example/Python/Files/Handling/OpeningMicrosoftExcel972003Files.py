import os
from pathlib import Path
import aspose.cells as cells

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Files" / "Handling" / "OpeningMicrosoftExcel972003Files"

def run():
    data_dir = get_data_dir()
    file_path = os.path.join(data_dir, "Book_Excel97_2003.xls")
    with open(file_path, "rb") as stream:
        load_options = cells.LoadOptions(cells.LoadFormat.EXCEL_97_TO_2003)
        wb_excel97 = cells.Workbook(stream, load_options)
    print("Microsoft Excel 97 - 2003 workbook opened successfully!")

if __name__ == "__main__":
    run()