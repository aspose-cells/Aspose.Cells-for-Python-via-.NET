import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..","..", "..", "Data", "01_SourceDirectory"))

def run_accessing_maximum_display_range_of_worksheet():
    source_dir = get_source_directory()
    workbook = cells.Workbook(os.path.join(source_dir, "sampleAccessingMaximumDisplayRangeofWorksheet.xlsx"))
    worksheet = workbook.worksheets[0]
    max_range = worksheet.cells.max_display_range
    print("Maximum Display Range: " + max_range.refers_to)
    print("AccessingMaximumDisplayRangeofWorksheet executed successfully.")

if __name__ == "__main__":
    run_accessing_maximum_display_range_of_worksheet()