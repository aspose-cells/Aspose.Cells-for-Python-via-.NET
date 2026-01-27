import os
import aspose.cells as cells

def get_source_directory():
    # Adjust the relative path based on the script location
    return os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "..",
            "..",
            "Data",
            "01_SourceDirectory"
        )
    )

def run_finding_cells_containing_formula():
    source_dir = get_source_directory()
    workbook_path = os.path.join(source_dir, "sampleFindingCellsContainingFormula.xlsx")
    workbook = cells.Workbook(workbook_path)

    worksheet = workbook.worksheets[0]

    find_options = cells.FindOptions()
    find_options.look_in_type = cells.LookInType.FORMULAS

    cell = worksheet.cells.find("=SUM(A5:A10)", None, find_options)

    print("Name of the cell containing formula: " + cell.name)
    print("FindingCellsContainingFormula executed successfully.")

if __name__ == "__main__":
    run_finding_cells_containing_formula()