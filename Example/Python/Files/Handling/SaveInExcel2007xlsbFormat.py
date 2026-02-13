import aspose.cells as cells
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Files/Handling/SaveInExcel2007xlsbFormat"

def run():
    data_dir = get_data_dir()
    data_dir.mkdir(parents=True, exist_ok=True)

    workbook = cells.Workbook()
    output_path = data_dir / "output.xlsb"
    workbook.save(str(output_path), cells.SaveFormat.XLSB)

if __name__ == "__main__":
    run()