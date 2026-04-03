import os
from datetime import datetime
from pathlib import Path
from aspose import cells as cells
from aspose.pydrawing import Color
from aspose.cells.rendering import ImageOrPrintOptions
from aspose.cells.drawing import ImageType

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def run():
    source_dir = get_source_directory()
    output_dir = get_output_directory()
    
    wb = cells.Workbook()
    ws = wb.worksheets[0]
    
    opts = ImageOrPrintOptions()
    opts.image_type = ImageType.PNG
    opts.output_blank_page_when_nothing_to_print = True
    
    sr = cells.rendering.SheetRender(ws, opts)
    output_path = os.path.join(output_dir, "OutputBlankPageWhenNothingToPrint.png")
    sr.to_image(0, str(output_path))

if __name__ == "__main__":
    run()