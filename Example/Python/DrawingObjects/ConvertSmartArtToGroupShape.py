import os
from pathlib import Path
import aspose.cells as cells

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def run_convert_smart_art_to_group_shape():
    source_dir = get_source_directory()
    input_file = os.path.join(source_dir, "sampleSmartArtShape_GetResultOfSmartArt.xlsx")

    # Load the Excel file containing the SmartArt shape
    workbook = cells.Workbook(input_file)

    # Access the first worksheet
    worksheet = workbook.worksheets[0]

    # Access the first shape
    shape = worksheet.shapes[0]

    # Determine if shape is SmartArt
    print("Is Smart Art Shape:", shape.is_smart_art)

    # Determine if shape is a group shape
    print("Is Group Shape:", shape.is_group)

    # Convert SmartArt shape into a group shape and check the result
    result = shape.get_result_of_smart_art()
    print("Is Group Shape after conversion:", result.is_group)

    print("ConvertSmartArtToGroupShape executed successfully.\n")

if __name__ == "__main__":
    run_convert_smart_art_to_group_shape()