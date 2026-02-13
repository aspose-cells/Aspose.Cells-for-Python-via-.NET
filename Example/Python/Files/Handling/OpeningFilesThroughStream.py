import aspose.cells as cells
from io import BytesIO
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Files" / "Handling" / "OpeningFilesThroughStream"

def run():
    data_dir = get_data_dir()
    file_path = data_dir / "Book2.xls"
    with open(file_path, "rb") as f:
        stream = BytesIO(f.read())
    workbook = cells.Workbook(stream)
    print("Workbook opened using stream successfully!")

if __name__ == "__main__":
    run()