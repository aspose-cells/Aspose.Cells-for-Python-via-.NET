import aspose.cells as cells
from pathlib import Path


def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Files" / "Handling" / "SavingFiletoStream"


def run():
    data_dir = get_data_dir()
    file_path = data_dir / "Book1.xlsx"

    output_path = data_dir / "output.xlsx"
    with open(output_path, "wb") as stream:
        workbook = cells.Workbook(str(file_path))
        workbook.save(stream, cells.SaveFormat.XLSX)


if __name__ == "__main__":
    run()