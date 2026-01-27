import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_autofilter_blank():
    source_dir = get_source_directory()
    output_dir = get_output_directory()
    os.makedirs(output_dir, exist_ok=True)

    input_path = os.path.join(source_dir, "sampleBlank.xlsx")
    workbook = cells.Workbook(input_path)

    worksheet = workbook.worksheets[0]
    worksheet.auto_filter.match_blanks(0)
    worksheet.auto_filter.refresh()

    output_path = os.path.join(output_dir, "outSampleBlank.xlsx")
    workbook.save(output_path)

    print("AutofilterBlank executed successfully.")

if __name__ == "__main__":
    run_autofilter_blank()
