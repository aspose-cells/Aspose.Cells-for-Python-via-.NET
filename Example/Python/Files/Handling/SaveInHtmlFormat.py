import os
import aspose.cells as cells
from pathlib import Path
from aspose.pydrawing import Color

def get_data_dir():
    return (
        Path(__file__).parent / ".." / ".." / ".." / "Data" / "Files" / "Handling" / "SaveInHtmlFormat"
    ).resolve()

def run():
    data_dir = get_data_dir()
    os.makedirs(data_dir, exist_ok=True)
    workbook = cells.Workbook()
    output_file = data_dir / "output.html"
    workbook.save(str(output_file), cells.SaveFormat.HTML)

if __name__ == "__main__":
    run()
