import os
from pathlib import Path
import aspose.cells as cells

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "DrawingObjects/OLE/RefreshOLEObjects"

def run_refresh_ole_objects():
    data_dir = get_data_dir()
    input_file = data_dir / "sample.xlsx"
    workbook = cells.Workbook(str(input_file))
    sheet = workbook.worksheets[0]
    sheet.ole_objects[0].auto_load = True
    output_file = data_dir / "RefreshOLEObjects_out.xlsx"
    workbook.save(str(output_file), cells.SaveFormat.XLSX)

if __name__ == "__main__":
    run_refresh_ole_objects()
