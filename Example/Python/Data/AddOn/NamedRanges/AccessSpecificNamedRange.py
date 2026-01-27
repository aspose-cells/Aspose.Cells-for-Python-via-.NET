import os
import aspose.cells as cells

def get_source_directory() -> str:
    """
    Returns the absolute path to the directory that contains the source Excel files.
    Adjusted to be relative to this script's location.
    """
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "Data", "01_SourceDirectory")
    )

def run_access_specific_named_range() -> None:
    source_dir = get_source_directory()
    workbook_path = os.path.join(source_dir, "sampleAccessSpecificNamedRange.xlsx")

    if not os.path.isfile(workbook_path):
        raise FileNotFoundError(f"Workbook not found: {workbook_path}")

    workbook = cells.Workbook(workbook_path)

    # Retrieve the named range "MyRangeTwo"
    named_range = workbook.worksheets.get_range_by_name("MyRangeTwo")
    if named_range is not None:
        print("Named Range : " + named_range.refers_to)

    print("AccessSpecificNamedRange executed successfully.")

if __name__ == "__main__":
    run_access_specific_named_range()