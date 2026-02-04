import os
from pathlib import Path
import aspose.cells as cells

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def run_rotate_text_with_shape_inside_worksheet():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    workbook = cells.Workbook(os.path.join(source_dir, "sampleRotateTextWithShapeInsideWorksheet.xlsx"))
    worksheet = workbook.worksheets[0]

    cell_b4 = worksheet.cells.get("B4")
    cell_b4.put_value("Text is not rotating with shape because RotateTextWithShape is false.")

    shape = worksheet.shapes[0]
    shape_text_alignment = shape.text_body.text_alignment
    shape_text_alignment.rotate_text_with_shape = False

    workbook.save(os.path.join(output_dir, "outputRotateTextWithShapeInsideWorksheet.xlsx"))

if __name__ == "__main__":
    run_rotate_text_with_shape_inside_worksheet()
