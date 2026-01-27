import os
import aspose.cells as cells

def get_source_directory():
    # Adjust the relative path as needed for your project layout
    return os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "..",
            "..",
            "Data",
            "01_SourceDirectory",
        )
    )

def run_access_cell_using_cell_index_in_cells_collection():
    source_dir = get_source_directory()
    file_name = "sampleAccessCellUsingCellIndexInCellsCollection.xlsx"
    input_path = os.path.join(source_dir, file_name)

    # Fallback to the script's directory if the file is not found in the source directory
    if not os.path.isfile(input_path):
        input_path = os.path.join(os.path.dirname(__file__), file_name)

    workbook = cells.Workbook(input_path)
    worksheet = workbook.worksheets[0]

    # Access a cell using its row and column indices (zero‑based)
    cell = worksheet.cells.get(5, 2)

    print(f"Cell Name: {cell.name} Value: {cell.string_value}")
    print("AccessCellUsingCellIndexInCellsCollection executed successfully.")

if __name__ == "__main__":
    run_access_cell_using_cell_index_in_cells_collection()