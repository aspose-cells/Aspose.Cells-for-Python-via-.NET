import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..","..", "..", "Data", "01_SourceDirectory"))

def run_finding_cells_containing_string_value_or_number():
    source_dir = get_source_directory()
    input_file = os.path.join(source_dir, "sampleFindingCellsContainingStringValueOrNumber.xlsx")
    workbook = cells.Workbook(input_file)
    worksheet_cells = workbook.worksheets[0].cells

    opts = cells.FindOptions()
    opts.look_in_type = cells.LookInType.VALUES
    opts.look_at_type = cells.LookAtType.ENTIRE_CONTENT

    cell1 = worksheet_cells.find(205, None, opts)
    if cell1 is not None:
        print("Name of the cell containing the value: " + cell1.name)
    else:
        print("Record not found ")

    cell2 = worksheet_cells.find("Items A", None, opts)
    if cell2 is not None:
        print("Name of the cell containing the value: " + cell2.name)
    else:
        print("Record not found ")

    opts.look_at_type = cells.LookAtType.CONTAINS
    cell3 = worksheet_cells.find("Data", None, opts)
    if cell3 is not None:
        print("Name of the cell containing the value: " + cell3.name)
    else:
        print("Record not found ")

    print("FindingCellsContainingStringValueOrNumber executed successfully.")

if __name__ == "__main__":
    run_finding_cells_containing_string_value_or_number()