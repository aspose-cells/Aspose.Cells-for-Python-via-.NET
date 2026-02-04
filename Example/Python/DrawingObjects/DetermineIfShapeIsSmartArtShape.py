import os
from pathlib import Path
import aspose.cells as cells

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def run_determine_if_shape_is_smart_art_shape():
    source_dir = get_source_directory()
    input_file = os.path.join(source_dir, "sampleSmartArtShape.xlsx")
    workbook = cells.Workbook(input_file)
    worksheet = workbook.worksheets[0]
    shape = worksheet.shapes[0]
    print("Is Smart Art Shape:", shape.is_smart_art)
    print("DetermineIfShapeIsSmartArtShape executed successfully.\r\n")

if __name__ == "__main__":
    run_determine_if_shape_is_smart_art_shape()