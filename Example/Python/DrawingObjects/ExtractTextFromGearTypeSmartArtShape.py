import os
from pathlib import Path
import aspose.cells as cells

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def run_extract_text_from_gear_type_smart_art_shape():
    source_dir = get_source_directory()
    input_file = os.path.join(source_dir, "sampleExtractTextFromGearTypeSmartArtShape.xlsx")
    workbook = cells.Workbook(input_file)
    worksheet = workbook.worksheets[0]
    shape = worksheet.shapes[0]
    group_shape = shape.get_result_of_smart_art()
    grouped_shapes = group_shape.get_grouped_shapes()
    for shp in grouped_shapes:
        if shp.type == cells.drawing.AutoShapeType.GEAR9 or shp.type == cells.drawing.AutoShapeType.GEAR6:
            print("Gear Type Shape Text: " + shp.text)
    print("ExtractTextFromGearTypeSmartArtShape executed successfully.")

if __name__ == "__main__":
    run_extract_text_from_gear_type_smart_art_shape()
