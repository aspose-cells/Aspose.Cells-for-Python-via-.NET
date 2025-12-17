import os
import aspose.cells as cells

def get_output_directory():
    return os.path.abspath(
        os.path.join(".", "..", "..", "Data", "02_OutputDirectory")
    )

def run_exclude_unused_styles_in_excel_to_html():
    output_dir = get_output_directory()

    # Create workbook
    wb = cells.Workbook()

    # Create an unused named style
    wb.create_style().name = "UnusedStyle_XXXXXXXXXXXXXX"

    # Access first worksheet
    ws = wb.worksheets[0]

    # Put some value in cell C7
    ws.cells.get("C7").put_value("This is sample text.")

    # Specify HTML save options, exclude unused styles
    opts = cells.HtmlSaveOptions()
    opts.exclude_unused_styles = True

    # Save the workbook in HTML format
    output_file = os.path.join(output_dir, "outputExcludeUnusedStylesInExcelToHTML.html")
    wb.save(output_file, opts)

    print("ExcludeUnusedStylesInExcelToHTML executed successfully.")

if __name__ == "__main__":
    run_exclude_unused_styles_in_excel_to_html()