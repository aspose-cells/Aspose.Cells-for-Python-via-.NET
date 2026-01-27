import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "..",
            "..",
            "Data",
            "01_SourceDirectory",
        )
    )

def get_output_directory():
    return os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
            "..",
            "..",
            "..",
            "Data",
            "02_OutputDirectory",
        )
    )

def run_autofilter_begins_with():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    input_path = os.path.join(source_dir, "sourseSampleCountryNames.xlsx")
    if not os.path.isfile(input_path):
        raise FileNotFoundError(f"Source file not found: {input_path}")

    workbook = cells.Workbook(input_path)
    worksheet = workbook.worksheets[0]

    worksheet.auto_filter.range = "A1:A18"
    worksheet.auto_filter.custom(
        0, cells.FilterOperatorType.BEGINS_WITH, "Ba"
    )
    worksheet.auto_filter.refresh()

    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "outSourseSampleCountryNames.xlsx")
    workbook.save(output_path)

    print("AutofilterBeginsWith executed successfully.")

if __name__ == "__main__":
    run_autofilter_begins_with()