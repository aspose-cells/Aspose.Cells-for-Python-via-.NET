import os
import aspose.cells as cells
from datetime import datetime

def get_data_directory():
    return os.path.abspath(os.path.join(".", "Data"))

def run_importing_from_data_column():
    data_dir = get_data_directory()
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)

    # Prepare data equivalent to the .NET DataTable
    # First row = column headers (because IsFieldNameShown = True)
    data = [
        ["Product ID", "Product Name"],
        [1, "Aniseed Syrup"],
        [2, "Boston Crab Meat"]
    ]

    # Create a new workbook and get the first worksheet
    workbook = cells.Workbook()
    sheet = workbook.worksheets[0]

    # Set import options (kept for parity with the original example)
    import_options = cells.ImportTableOptions()
    import_options.is_field_name_shown = True
    import_options.is_html_string = True
    import_options.column_indexes = [0, 1]   # import only the first two columns

    # Import the data starting at row 1, column 1 (zero‑based indexing)
    start_row = 1
    start_column = 1
    for r, row_data in enumerate(data):
        for c, value in enumerate(row_data):
            sheet.cells.get(start_row + r, start_column + c).put_value(value)

    # Save the workbook
    output_path = os.path.join(data_dir, "DataImport.out.xls")
    workbook.save(output_path)

if __name__ == "__main__":
    run_importing_from_data_column()
