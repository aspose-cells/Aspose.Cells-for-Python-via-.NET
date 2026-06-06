import os
from aspose.cells import Workbook
from aspose.cells.rendering import SheetRender, ImageOrPrintOptions

def get_source_directory():
    return os.path.join(os.path.dirname(__file__), "..", "..", "Data", "01_SourceDirectory")

def run():
    source_dir = get_source_directory()
    workbook = Workbook(os.path.join(source_dir, "SheetRenderSample.xlsx"))
    img_opt = ImageOrPrintOptions()
    worksheet = workbook.worksheets[1]
    sheet_render = SheetRender(worksheet, img_opt)
    printer_settings = None
    sheet_render.to_printer(printer_settings)

if __name__ == "__main__":
    run()