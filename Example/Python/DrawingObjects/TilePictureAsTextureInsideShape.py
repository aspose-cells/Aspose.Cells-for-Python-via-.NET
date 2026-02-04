import os
from pathlib import Path
import aspose.cells as cells

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def run_tile_picture_as_texture_inside_shape():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    input_file = os.path.join(source_dir, "sampleTextureFill_IsTiling.xlsx")
    workbook = cells.Workbook(input_file)

    worksheet = workbook.worksheets[0]
    shape = worksheet.shapes[0]

    shape.fill.texture_fill.is_tiling = True

    output_file = os.path.join(output_dir, "outputTextureFill_IsTiling.xlsx")
    workbook.save(output_file)

    print("TilePictureAsTextureInsideShape executed successfully.")

if __name__ == "__main__":
    run_tile_picture_as_texture_inside_shape()