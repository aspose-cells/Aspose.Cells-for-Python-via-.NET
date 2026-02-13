import os
from pathlib import Path
import aspose.cells as cells

def get_data_dir() -> Path:
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Files" / "Handling" / "OpeningHTMLFile"

def run():
    # ExStart:1
    data_dir = get_data_dir()
    file_path = data_dir / "Book1.html"

    # Instantiate LoadOptions specified by the LoadFormat.
    load_options = cells.HtmlLoadOptions(cells.LoadFormat.HTML)

    # Create a Workbook object and opening the file from its path
    wb = cells.Workbook(str(file_path), load_options)

    # Save the XLSX file
    output_path = str(file_path) + "output.xlsx"
    wb.save(output_path)
    # ExEnd:1

if __name__ == "__main__":
    run()