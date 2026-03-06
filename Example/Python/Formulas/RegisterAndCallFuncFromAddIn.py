import os
from datetime import datetime
from aspose import pydrawing as drawing
from aspose.cells import Workbook, SaveFormat
from pathlib import Path

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def main():
    # Create empty workbook
    workbook = Workbook()

    # Register macro enabled add-in along with the function name
    id = workbook.worksheets.register_add_in_function(str(get_source_directory() / "TESTUDF.xlam"), "TEST_UDF", False)

    # Register more functions in the file (if any)
    workbook.worksheets.register_add_in_function(id, "TEST_UDF1")  # in this way you can add more functions that are in the same file

    # Access first worksheet
    worksheet = workbook.worksheets[0]

    # Access first cell
    cell = worksheet.cells.get("A1")

    # Set formula name present in the add-in
    cell.formula = "=TEST_UDF()"

    # Save workbook to output XLSX format.
    output_path = get_output_directory() / "test_udf.xlsx"
    workbook.save(str(output_path), SaveFormat.XLSX)

if __name__ == "__main__":
    main()