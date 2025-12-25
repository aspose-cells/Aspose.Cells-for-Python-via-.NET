import os
import aspose.cells as cells

def get_source_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "01_SourceDirectory"))

def run_print_preview():
    source_dir = get_source_directory()
    workbook_path = os.path.join(source_dir, "Book1.xlsx")
    workbook = cells.Workbook(workbook_path)

    img_options = cells.rendering.ImageOrPrintOptions()
    preview = cells.rendering.WorkbookPrintingPreview(workbook, img_options)
    print(f"Workbook page count: {preview.evaluated_page_count}")

    preview2 = cells.rendering.SheetPrintingPreview(workbook.worksheets[0], img_options)
    print(f"Worksheet page count: {preview2.evaluated_page_count}")

    print("PrintPreview executed successfully.")

if __name__ == "__main__":
    run_print_preview()