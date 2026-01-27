import os
import aspose.cells as cells

def get_source_directory():
    # Determine the project root by walking up directories until the "Data/01_SourceDirectory" folder is found
    current_dir = os.path.abspath(os.path.dirname(__file__))
    while True:
        candidate = os.path.abspath(os.path.join(current_dir, "Data", "01_SourceDirectory"))
        if os.path.isdir(candidate):
            return candidate
        parent = os.path.abspath(os.path.join(current_dir, ".."))
        if parent == current_dir:  # Reached filesystem root
            raise FileNotFoundError("Unable to locate 'Data/01_SourceDirectory' folder.")
        current_dir = parent

def run_identify_cells_in_named_range():
    source_dir = get_source_directory()
    workbook_path = os.path.join(source_dir, "sampleIdentifyCellsInNamedRange.xlsx")
    if not os.path.isfile(workbook_path):
        raise FileNotFoundError(f"Workbook not found at '{workbook_path}'.")
    
    workbook = cells.Workbook(workbook_path)
    rng = workbook.worksheets.get_range_by_name("MyRangeThree")
    
    print("First Row : " + str(rng.first_row))
    print("First Column : " + str(rng.first_column))
    print("Row Count : " + str(rng.row_count))
    print("Column Count : " + str(rng.column_count))
    print("IdentifyCellsInNamedRange executed successfully.")

if __name__ == "__main__":
    run_identify_cells_in_named_range()