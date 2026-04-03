import os
import datetime
from aspose import pydrawing as drawing
from aspose.cells import Workbook
from aspose.cells.rendering import SheetRender, ImageOrPrintOptions
from aspose.cells.drawing import ImageType
from pathlib import Path

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def export_range_of_cells_in_worksheet_to_image():
    source_dir = str(get_source_directory())
    output_dir = str(get_output_directory())
    
    workbook = Workbook(os.path.join(source_dir, "sampleExportRangeOfCellsInWorksheetToImage.xlsx"))
    worksheet = workbook.worksheets[0]
    
    worksheet.page_setup.print_area = "D8:G16"
    worksheet.page_setup.left_margin = 0.0
    worksheet.page_setup.right_margin = 0.0
    worksheet.page_setup.top_margin = 0.0
    worksheet.page_setup.bottom_margin = 0.0
    
    options = ImageOrPrintOptions()
    options.one_page_per_sheet = True
    options.image_type = ImageType.JPEG
    options.horizontal_resolution = 200
    options.vertical_resolution = 200
    
    sr = SheetRender(worksheet, options)
    sr.to_image(0, os.path.join(output_dir, "outputExportRangeOfCellsInWorksheetToImage.jpg"))

if __name__ == "__main__":
    export_range_of_cells_in_worksheet_to_image()