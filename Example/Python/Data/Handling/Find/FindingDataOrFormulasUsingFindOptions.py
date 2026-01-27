import os
import aspose.cells as cells

def get_source_directory():
    # Primary expected location based on the original example structure
    primary = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "Data", "01_SourceDirectory")
    )
    if os.path.isdir(primary):
        return primary

    # Fallback to a local Data folder next to this script
    fallback = os.path.abspath(os.path.join(os.path.dirname(__file__), "Data", "01_SourceDirectory"))
    if os.path.isdir(fallback):
        return fallback

    # Last resort: current working directory's Data folder
    return os.path.abspath(os.path.join(".", "Data", "01_SourceDirectory"))

def run_finding_data_or_formulas_using_find_options():
    source_dir = get_source_directory()
    workbook_path = os.path.join(source_dir, "sampleFindingDataOrFormulasUsingFindOptions.xlsx")

    if not os.path.isfile(workbook_path):
        raise FileNotFoundError(f"Input file not found: {workbook_path}")

    # Instantiate the workbook object
    workbook = cells.Workbook(workbook_path)
    workbook.calculate_formula()

    # Get Cells collection
    worksheet = workbook.worksheets[0]
    cells_collection = worksheet.cells

    # Instantiate FindOptions object
    find_options = cells.FindOptions()

    # Define the search area
    ca = cells.CellArea()
    ca.start_row = 8
    ca.start_column = 2
    ca.end_row = 17
    ca.end_column = 13
    find_options.set_range(ca)

    # Set searching properties
    find_options.search_backward = False
    find_options.search_order_by_rows = True
    find_options.look_in_type = cells.LookInType.VALUES
    find_options.look_at_type = cells.LookAtType.ENTIRE_CONTENT

    # Find the cell with the specified value
    cell = cells_collection.find(341, None, find_options)

    if cell is not None:
        print("Name of the cell containing the value:", cell.name)
    else:
        print("Record not found")

    print("FindingDataOrFormulasUsingFindOptions executed successfully.")

if __name__ == "__main__":
    run_finding_data_or_formulas_using_find_options()