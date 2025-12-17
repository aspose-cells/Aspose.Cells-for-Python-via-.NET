import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_set_scalable_column_width():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    workbook = cells.Workbook(os.path.join(source_dir, "sampleForScalableColumns.xlsx"))

    options = cells.HtmlSaveOptions()
    options.width_scalable = True
    options.export_images_as_base64 = True

    workbook.save(os.path.join(output_dir, "outsampleForScalableColumns.html"), options)

    print("SetScalableColumnWidth executed successfully.")

if __name__ == "__main__":
    run_set_scalable_column_width()