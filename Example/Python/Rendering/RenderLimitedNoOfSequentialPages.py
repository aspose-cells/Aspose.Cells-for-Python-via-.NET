import os
from pathlib import Path
import aspose.cells as cells
from aspose.cells.rendering import ImageOrPrintOptions, SheetRender
from aspose.cells.drawing import ImageType

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    source_dir = str(get_source_directory())
    output_dir = str(get_output_directory())
    
    wb = cells.Workbook(os.path.join(source_dir, "sampleImageOrPrintOptions_PageIndexPageCount.xlsx"))
    ws = wb.worksheets[0]
    
    opts = ImageOrPrintOptions()
    opts.page_index = 3
    opts.page_count = 4
    opts.image_type = ImageType.PNG
    
    sr = SheetRender(ws, opts)
    
    for i in range(opts.page_index, sr.page_count):
        sr.to_image(i, os.path.join(output_dir, f"outputImage-{i + 1}.png"))

if __name__ == "__main__":
    run()