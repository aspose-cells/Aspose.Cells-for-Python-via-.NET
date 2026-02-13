from pathlib import Path
import aspose.cells as cells

def get_data_dir():
    return (
        Path(__file__).parent
        / ".." / ".." / ".."
        / "Data" / "Files" / "Handling" / "OpeningFilewithDataOnly"
    )

def run():
    data_dir = get_data_dir()
    load_options = cells.LoadOptions(cells.LoadFormat.XLSX)
    load_options.load_filter = cells.LoadFilter(cells.LoadDataFilterOptions.CELL_DATA)
    book = cells.Workbook(str(data_dir / "Book1.xlsx"), load_options)
    print("File data imported successfully!")

if __name__ == "__main__":
    run()