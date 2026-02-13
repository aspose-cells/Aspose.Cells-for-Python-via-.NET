import os
from pathlib import Path
import aspose.cells as cells


def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Files/Handling/OpeningTabDelimitedFiles"


def run():
    load_options = cells.LoadOptions(cells.LoadFormat.TAB_DELIMITED)
    file_path = os.path.join(get_data_dir(), "Book1TabDelimited.txt")
    wb_tab_delimited = cells.Workbook(file_path, load_options)
    print("Tab delimited file opened successfully!")


if __name__ == "__main__":
    run()