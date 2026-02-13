import os
from pathlib import Path
import aspose.cells as cells

def get_data_dir():
    return (
        Path(__file__).parent
        / ".."
        / ".."
        / ".."
        / "Data"
        / "Files"
        / "Handling"
        / "SaveInExcel2007xlsxFormat"
    )

def run():
    workbook = cells.Workbook()
    output_path = get_data_dir() / "output.xlsx"
    os.makedirs(output_path.parent, exist_ok=True)
    workbook.save(str(output_path), cells.SaveFormat.XLSX)

if __name__ == "__main__":
    run()