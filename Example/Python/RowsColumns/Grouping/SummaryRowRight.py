import os
from aspose import pydrawing as drawing
from aspose.cells import Workbook
from datetime import datetime
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "RowsColumns/Grouping/SummaryRowRight"

def main():
    data_dir = get_data_dir()
    workbook = Workbook(str(data_dir / "sample.xlsx"))
    worksheet = workbook.worksheets[0]

    # Grouping first six rows and first three columns
    worksheet.cells.group_rows(0, 5, True)
    worksheet.cells.group_columns(0, 2, True)

    worksheet.outline.summary_column_right = True

    # Saving the modified Excel file
    workbook.save(str(data_dir / "output.xls"))

if __name__ == "__main__":
    main()