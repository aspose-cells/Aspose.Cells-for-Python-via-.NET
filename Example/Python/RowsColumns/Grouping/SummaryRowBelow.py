import os
from pathlib import Path
from datetime import datetime
from aspose import pydrawing as drawing
from aspose.cells import Workbook

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "RowsColumns/Grouping/SummaryRowBelow"

def main():
    data_dir = get_data_dir()
    workbook = Workbook(str(data_dir / "sample.xlsx"))
    worksheet = workbook.worksheets[0]

    # Grouping first six rows and first three columns
    worksheet.cells.group_rows(0, 5, True)
    worksheet.cells.group_columns(0, 2, True)

    # Setting SummaryRowBelow property to false
    worksheet.outline.summary_row_below = False

    # Saving the modified Excel file
    output_path = data_dir / "output.xls"
    workbook.save(str(output_path))

if __name__ == "__main__":
    main()