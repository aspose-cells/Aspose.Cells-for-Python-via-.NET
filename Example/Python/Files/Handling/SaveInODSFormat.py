import os
import aspose.cells as cells
from pathlib import Path

def get_data_dir():
    return (Path(__file__).parent / ".." / ".." / ".." / "Data" / "Files"
            / "Handling" / "SaveInODSFormat").resolve()

def run():
    data_dir = get_data_dir()
    os.makedirs(data_dir, exist_ok=True)

    workbook = cells.Workbook()
    output_path = data_dir / "output.ods"
    workbook.save(str(output_path))

if __name__ == "__main__":
    run()