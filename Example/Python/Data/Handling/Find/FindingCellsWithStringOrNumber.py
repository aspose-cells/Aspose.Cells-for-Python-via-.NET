import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "Data", "01_SourceDirectory")
    )

def run_finding_cells_with_string_or_number():
    source_dir = get_source_directory()
    workbook_path = os.path.join(source_dir, "sampleFindingCellsWithStringOrNumber.xlsx")
    workbook = cells.Workbook(workbook_path)

    workbook.calculate_formula()

    cells_collection = workbook.worksheets[0].cells

    opts = cells.FindOptions()
    opts.look_in_type = cells.LookInType.VALUES
    opts.look_at_type = cells.LookAtType.ENTIRE_CONTENT

    cell1 = cells_collection.find(224, None, opts)
    if cell1:
        print("Name of the cell containing the value:", cell1.name)
    else:
        print("Record not found")

    cell2 = cells_collection.find("Items E", None, opts)
    if cell2:
        print("Name of the cell containing the value:", cell2.name)
    else:
        print("Record not found")

    opts.look_at_type = cells.LookAtType.CONTAINS
    cell3 = cells_collection.find("Data", None, opts)
    if cell3:
        print("Name of the cell containing the value:", cell3.name)
    else:
        print("Record not found")

    print("FindingCellsWithStringOrNumber executed successfully.")

if __name__ == "__main__":
    run_finding_cells_with_string_or_number()
