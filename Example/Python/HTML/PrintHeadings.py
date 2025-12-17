import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_print_headings():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    input_path = os.path.join(source_dir, "Book1.xlsx")
    workbook = cells.Workbook(input_path)

    options = cells.HtmlSaveOptions()
    options.export_headings = True

    output_path = os.path.join(output_dir, "PrintHeadings_out.html")
    workbook.save(output_path, options)

    print("PrintHeadings executed successfully.")

if __name__ == "__main__":
    run_print_headings()