import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..","..", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "..","..", "Data", "02_OutputDirectory"))

def run_rename_named_range():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    # Open an existing Excel file
    workbook = cells.Workbook(os.path.join(source_dir, "sampleRenameNamedRange.xlsx"))

    # Get the first worksheet
    sheet = workbook.worksheets[0]

    # Get the named range "MyTestRange"
    name = workbook.worksheets.names.get("MyTestRange")

    # Rename it
    name.text = "MyNewRange"

    # Save the Excel file
    workbook.save(os.path.join(output_dir, "outputRenameNamedRange.xlsx"))

    print("RenameNamedRange executed successfully.")

if __name__ == "__main__":
    run_rename_named_range()