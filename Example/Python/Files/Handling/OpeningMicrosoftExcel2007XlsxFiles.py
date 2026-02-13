import os
from pathlib import Path
import aspose.cells as cells


def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Files/Handling/OpeningMicrosoftExcel2007XlsxFiles"


data_dir = get_data_dir()

# Instantiate LoadOptions specified by the LoadFormat.
load_options = cells.LoadOptions(cells.LoadFormat.XLSX)

# Create a Workbook object and open the file from its path
wb_excel2007 = cells.Workbook(os.path.join(data_dir, "Book_Excel2007.xlsx"), load_options)
print("Microsoft Excel 2007 workbook opened successfully!")