import os
import aspose.cells as cells

def get_data_directory():
    return os.path.abspath(
        os.path.join(".", "..", "..", "..", "..", "Data", "03_DataDirectory")
    )

def run_importing_from_dataview():
    # Create a new workbook and get the first worksheet
    workbook = cells.Workbook()
    worksheet = workbook.worksheets[0]

    # Data including column headers (mimics DataView import with field names shown)
    data = [
        ["Product ID", "Product Name", "Units In Stock"],
        [1, "Aniseed Syrup", 15],
        [2, "Boston Crab Meat", 123],
    ]

    # Populate the worksheet starting at cell A1 (row 0, column 0)
    for row_idx, row in enumerate(data):
        for col_idx, value in enumerate(row):
            worksheet.cells.get(row_idx, col_idx).put_value(value)

    # Save the workbook
    output_path = os.path.join(get_data_directory(), "output.xls")
    workbook.save(output_path)

if __name__ == "__main__":
    run_importing_from_dataview()