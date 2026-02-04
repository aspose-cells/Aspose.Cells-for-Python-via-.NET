import os
from pathlib import Path
import aspose.cells as cells

def get_source_directory():
    return (Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory").resolve()

def get_output_directory():
    return (Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory").resolve()

def run_set_margins_of_comment_or_shape_inside_the_worksheet():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    input_path = os.path.join(str(source_dir), "sampleSetMarginsOfCommentOrShapeInsideTheWorksheet.xlsx")
    workbook = cells.Workbook(input_path)

    worksheet = workbook.worksheets[0]

    for shape in worksheet.shapes:
        txt_align = shape.text_body.text_alignment
        txt_align.is_auto_margin = False
        txt_align.top_margin_pt = 10.0
        txt_align.left_margin_pt = 10.0
        txt_align.bottom_margin_pt = 10.0
        txt_align.right_margin_pt = 10.0

    output_path = os.path.join(str(output_dir), "outputSetMarginsOfCommentOrShapeInsideTheWorksheet.xlsx")
    workbook.save(output_path)

    print("SetMarginsOfCommentOrShapeInsideTheWorksheet executed successfully.")

if __name__ == "__main__":
    run_set_margins_of_comment_or_shape_inside_the_worksheet()
