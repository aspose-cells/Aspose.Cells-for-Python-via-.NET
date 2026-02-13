import os
from pathlib import Path
import aspose.cells as cells


def get_data_dir() -> Path:
    return (
        Path(__file__).parent.parent.parent
        / "Data"
        / "Files"
        / "Handling"
        / "OpeningSpreadsheetMLFiles"
    )


def run() -> None:
    data_dir = get_data_dir()
    file_path = data_dir / "Book3.xml"

    # If the sample file does not exist, inform the user but do not raise an exception
    if not file_path.is_file():
        print(f"SpreadsheetML file not found at: {file_path}")
        return

    # LoadOptions specifying SpreadsheetML format
    load_options = cells.LoadOptions(cells.LoadFormat.SpreadsheetML)

    # Open the SpreadsheetML file
    workbook = cells.Workbook(str(file_path), load_options)

    print("SpreadSheetML file opened successfully!")


if __name__ == "__main__":
    run()