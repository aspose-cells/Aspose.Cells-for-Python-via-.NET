import os
from pathlib import Path
from datetime import datetime
from aspose.cells import Workbook
from aspose.pydrawing import Color

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "Worksheets/GetCellValidationInODS"

def run():
    source_dir = str(get_source_directory())
    workbook = Workbook(os.path.join(source_dir, "SampleBook1.ods"))
    worksheet = workbook.worksheets[0]
    cell = worksheet.cells.get("A9")
    if cell.get_validation() is not None:
        print(cell.get_validation().type)
    print("GetCellValidationInODS executed successfully.")

if __name__ == "__main__":
    run()