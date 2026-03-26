import os
from pathlib import Path
from datetime import datetime
from aspose import cells as cells
from aspose.pydrawing import Color

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "PivotTableExamples" / "RefreshAndCalculateItems"

def run():
    # ExStart:1
    # The path to the documents directory.
    data_dir = get_data_dir()

    # Load source excel file containing a pivot table having calculated items
    wb = cells.Workbook(str(data_dir / "sample.xlsx"))

    # Access first worksheet
    sheet = wb.worksheets[0]

    # Change the value of cell D2
    sheet.cells.get("D2").put_value(20)

    # Refresh and calculate all the pivot tables inside this sheet
    for pt in sheet.pivot_tables:
        pt.refresh_data()
        pt.calculate_data()

    # Save the workbook in output pdf
    wb.save(str(data_dir / "RefreshAndCalculateItems_out.pdf"), cells.SaveFormat.PDF)
    # ExEnd:1

if __name__ == "__main__":
    run()