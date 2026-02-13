import os
from pathlib import Path
import aspose.cells as cells

def get_data_dir() -> Path:
    return (
        Path(__file__).parent
        / ".." / ".." / ".." / "Data" / "Files" / "Handling" / "SaveFileInExcel972003format"
    )

def run() -> None:
    data_dir = get_data_dir()
    os.makedirs(data_dir, exist_ok=True)

    # Creating a Workbook object
    workbook = cells.Workbook()

    # Your code goes here for any workbook related operations

    # Save in Excel 97 – 2003 format
    output_path = os.path.join(data_dir, "output.xls")
    workbook.save(output_path)

    # OR
    workbook.save(output_path, cells.SaveFormat.EXCEL_97_TO_2003)