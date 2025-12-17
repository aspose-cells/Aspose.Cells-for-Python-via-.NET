import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_set_single_sheet_tab_name_in_html():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    # Load the sample Excel file containing a single sheet only
    workbook = cells.Workbook(os.path.join(source_dir, "sampleSingleSheet.xlsx"))

    # Specify HTML save options
    options = cells.HtmlSaveOptions()
    options.encoding = "utf-8"
    options.export_images_as_base64 = True
    options.export_grid_lines = True
    options.export_similar_border_style = True
    options.export_bogus_row_data = True
    options.exclude_unused_styles = True
    options.export_hidden_worksheet = True

    # Save the workbook in HTML format with the specified options
    workbook.save(os.path.join(output_dir, "outputSampleSingleSheet.htm"), options)

    print("SetSingleSheetTabNameInHtml executed successfully.")

if __name__ == "__main__":
    run_set_single_sheet_tab_name_in_html()