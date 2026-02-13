import os
from pathlib import Path
import aspose.cells as cells

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Files/Handling/SaveXLSFile"

def run():
    data_dir = get_data_dir()
    response = None
    workbook = cells.Workbook()
    if response is not None:
        workbook.save(
            response,
            os.path.join(data_dir, "output.xls"),
            cells.ContentDisposition.INLINE,
            cells.XlsSaveOptions()
        )