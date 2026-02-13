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
        / "OpeningFilesThroughPath"
    )

def run():
    data_dir = get_data_dir()
    workbook = cells.Workbook(str(data_dir / "Book1.xlsx"))
    print("Workbook opened using path successfully!")

if __name__ == "__main__":
    run()