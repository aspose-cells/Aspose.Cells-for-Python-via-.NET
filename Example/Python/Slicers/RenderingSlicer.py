import os
from pathlib import Path
from aspose.cells import Workbook
from aspose.cells.drawing import ImageType
from aspose.cells.rendering import SheetRender, ImageOrPrintOptions

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def main():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    wb = Workbook(str(source_dir / "sampleRenderingSlicer.xlsx"))

    ws = wb.worksheets[0]

    ws.page_setup.print_area = "B15:E25"

    img_opts = ImageOrPrintOptions()
    img_opts.horizontal_resolution = 200
    img_opts.vertical_resolution = 200
    img_opts.image_type = ImageType.PNG
    img_opts.one_page_per_sheet = True
    img_opts.only_area = True

    sr = SheetRender(ws, img_opts)
    sr.to_image(0, str(output_dir / "outputRenderingSlicer.png"))

if __name__ == "__main__":
    main()