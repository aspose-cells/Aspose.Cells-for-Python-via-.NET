import os
from pathlib import Path
from datetime import datetime
from aspose.pydrawing import Color
import aspose.cells as cells

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "PivotTableExamples" / "SettingFormatOptions"

def run():
    # ExStart:1
    # The path to the documents directory.
    data_dir = get_data_dir()

    # Load a template file
    workbook = cells.Workbook(str(data_dir / "Book1.xls"))

    # Get the first worksheet
    worksheet = workbook.worksheets[0]
    pivotindex = 0

    # Accessing the PivotTable
    pivot_table = worksheet.pivot_tables[pivotindex]

    # Setting the PivotTable report shows grand totals for rows.
    pivot_table.row_grand = True

    # Setting the PivotTable report shows grand totals for columns.
    pivot_table.column_grand = True

    # Setting the PivotTable report displays a custom string in cells that contain null values.
    pivot_table.display_null_string = True
    pivot_table.null_string = "null"

    # Setting the PivotTable report's layout
    pivot_table.page_field_order = cells.PrintOrderType.DOWN_THEN_OVER

    # Saving the Excel file
    workbook.save(str(data_dir / "output.xls"))

    # ExEnd:1

if __name__ == "__main__":
    run()