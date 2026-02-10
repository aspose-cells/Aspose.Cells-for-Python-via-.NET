import aspose.cells as cells
from datetime import datetime
from pathlib import Path
import os

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Files" / "Utility" / "SetPDFCreationTime"

def run():
    data_dir = get_data_dir()
    input_path = data_dir / "Book1.xlsx"
    workbook = cells.Workbook(str(input_path))

    options = cells.PdfSaveOptions()
    options.created_time = datetime.now()

    output_path = data_dir / "output.pdf"
    workbook.save(str(output_path), options)

if __name__ == "__main__":
    run()
