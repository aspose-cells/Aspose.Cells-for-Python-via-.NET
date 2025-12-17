import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_export_similar_border_style():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    input_file = os.path.join(source_dir, "sampleExportSimilarBorderStyle.xlsx")
    workbook = cells.Workbook(input_file)

    opts = cells.HtmlSaveOptions()
    opts.export_similar_border_style = True

    output_file = os.path.join(output_dir, "outputExportSimilarBorderStyle.html")
    workbook.save(output_file, opts)

    print("ExportSimilarBorderStyle executed successfully.")

if __name__ == "__main__":
    run_export_similar_border_style()