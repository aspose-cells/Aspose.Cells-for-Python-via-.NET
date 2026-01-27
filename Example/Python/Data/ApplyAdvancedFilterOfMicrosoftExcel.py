import os
from aspose.cells import Workbook, SaveFormat


def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))


def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))


def run_apply_advanced_filter():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    # Load the source workbook
    input_file = os.path.join(source_dir, "sampleAdvancedFilter.xlsx")
    workbook = Workbook(input_file)

    # Access the first worksheet
    worksheet = workbook.worksheets[0]

    # Apply advanced filter on range A5:D19 with criteria A1:D2,
    # filter in place, and keep all filtered records (not unique only)
    worksheet.advanced_filter(True, "A5:D19", "A1:D2", "", False)

    # Save the workbook in XLSX format
    output_file = os.path.join(output_dir, "outputAdvancedFilter.xlsx")
    workbook.save(output_file, SaveFormat.XLSX)

    print("ApplyAdvancedFilterOfMicrosoftExcel executed successfully.")


if __name__ == "__main__":
    run_apply_advanced_filter()