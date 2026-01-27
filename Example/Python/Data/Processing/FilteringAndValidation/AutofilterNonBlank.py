import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_autofilter_non_blank():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    workbook = cells.Workbook(os.path.join(source_dir, "sampleNonBlank.xlsx"))
    worksheet = workbook.worksheets[0]

    worksheet.auto_filter.match_non_blanks(0)
    worksheet.auto_filter.refresh()

    workbook.save(os.path.join(output_dir, "outSampleNonBlank.xlsx"))
    print("AutofilterNonBlank executed successfully.")

if __name__ == "__main__":
    run_autofilter_non_blank()