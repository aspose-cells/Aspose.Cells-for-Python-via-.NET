import aspose.cells as cells
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Files/Handling/OpeningCSVFiles"

def run():
    data_dir = get_data_dir()
    load_options = cells.LoadOptions(cells.LoadFormat.CSV)
    workbook = cells.Workbook(str(data_dir / "Book_CSV.csv"), load_options)
    print("CSV file opened successfully!")

run()