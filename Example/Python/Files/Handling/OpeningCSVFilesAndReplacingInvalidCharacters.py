import os
from pathlib import Path
import aspose.cells as cells


def get_source_directory():
    return Path(__file__).parent.parent.parent / "Data" / "01_SourceDirectory"


def run():
    source_dir = get_source_directory()
    filename = source_dir / "[20180220142533][ASPOSE_CELLS_TEST].csv"

    if not filename.is_file():
        print(f"CSV file not found: {filename}")
        return

    load_options = cells.TxtLoadOptions()
    load_options.separator = ';'
    load_options.load_filter = cells.LoadFilter(cells.LoadDataFilterOptions.CELL_DATA)
    load_options.check_excel_restriction = False
    load_options.convert_numeric_data = False
    load_options.convert_date_time_data = False

    workbook = cells.Workbook(str(filename), load_options)

    print(workbook.worksheets[0].name)
    print(len(workbook.worksheets[0].name))
    print("CSV file opened successfully!")


if __name__ == "__main__":
    run()