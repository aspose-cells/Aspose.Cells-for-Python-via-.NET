import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "..","..", "Data", "01_SourceDirectory"))

def run_access_cell_using_cell_name():
    source_dir = get_source_directory()
    workbook_path = os.path.join(source_dir, "sampleAccessCellUsingCellName.xlsx")
    workbook = cells.Workbook(workbook_path)

    worksheet = workbook.worksheets[0]

    cell = worksheet.cells.get("C6")
    print(f"Cell Name: {cell.name} Value: {cell.string_value}")

    print("AccessCellUsingCellName executed successfully.")

if __name__ == "__main__":
    run_access_cell_using_cell_name()