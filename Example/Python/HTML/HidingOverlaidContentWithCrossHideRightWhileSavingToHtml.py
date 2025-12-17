import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_hiding_overlaid_content_with_cross_hide_right_while_saving_to_html():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    workbook_path = os.path.join(source_dir, "sampleHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.xlsx")
    workbook = cells.Workbook(workbook_path)

    opts = cells.HtmlSaveOptions()
    opts.html_cross_string_type = cells.HtmlCrossType.CROSS_HIDE_RIGHT

    output_path = os.path.join(output_dir, "outputHidingOverlaidContentWithCrossHideRightWhileSavingToHtml.html")
    workbook.save(output_path, opts)

    print("HidingOverlaidContentWithCrossHideRightWhileSavingToHtml executed successfully.")

if __name__ == "__main__":
    run_hiding_overlaid_content_with_cross_hide_right_while_saving_to_html()
