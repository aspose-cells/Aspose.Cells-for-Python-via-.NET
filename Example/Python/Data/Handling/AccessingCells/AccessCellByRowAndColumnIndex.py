import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..","..", "..", "Data", "01_SourceDirectory"))

def run_access_cell_by_row_and_column_index():
    source_dir = get_source_directory()
    workbook_path = os.path.join(source_dir, "sampleAccessCellByRowAndColumnIndex.xlsx")
    workbook = cells.Workbook(workbook_path)
    worksheet = workbook.worksheets[0]
    cell = worksheet.cells.get(5, 2)
    print(f"Cell Name: {cell.name} Value: {cell.string_value}")
    print("AccessCellByRowAndColumnIndex executed successfully.")

if __name__ == "__main__":
    run_access_cell_by_row_and_column_index()
