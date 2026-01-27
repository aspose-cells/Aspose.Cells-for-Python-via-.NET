import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_autofilter_contains():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    input_file = os.path.join(source_dir, "sourseSampleCountryNames.xlsx")
    workbook = cells.Workbook(input_file)

    worksheet = workbook.worksheets[0]

    worksheet.auto_filter.range = "A1:A18"
    worksheet.auto_filter.custom(0, cells.FilterOperatorType.CONTAINS, "Ba")
    worksheet.auto_filter.refresh()

    output_file = os.path.join(output_dir, "outSourseSampleCountryNames.xlsx")
    workbook.save(output_file)

    print("AutofilterContains executed successfully.")

if __name__ == "__main__":
    run_autofilter_contains()