import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_export_print_area_to_html():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    workbook_path = os.path.join(source_dir, "sampleInlineCharts.xlsx")
    workbook = cells.Workbook(workbook_path)

    worksheet = workbook.worksheets[0]
    worksheet.page_setup.print_area = "D2:M20"

    options = cells.HtmlSaveOptions()
    options.export_print_area_only = True

    output_path = os.path.join(output_dir, "outputInlineCharts.html")
    workbook.save(output_path, options)

    print("ExportPrintAreaToHtml executed successfully.")

if __name__ == "__main__":
    run_export_print_area_to_html()