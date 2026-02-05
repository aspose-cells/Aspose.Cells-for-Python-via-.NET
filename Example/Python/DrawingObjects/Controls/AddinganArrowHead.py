import os
from pathlib import Path
import aspose.cells as cells
from aspose.pydrawing import Color

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "DrawingObjects" / "Controls" / "AddinganArrowHead"

def run_adding_an_arrow_head():
    data_dir = get_data_dir()
    if not data_dir.is_dir():
        data_dir.mkdir(parents=True, exist_ok=True)

    workbook = cells.Workbook()
    worksheet = workbook.worksheets[0]

    # Add a line shape: (upperLeftRow, upperLeftColumn, upperLeftPixelX, upperLeftPixelY, lowerRightRow, lowerRightPixelX)
    line2 = worksheet.shapes.add_line(7, 0, 1, 0, 85, 250)

    line2.line.fill_type = cells.drawing.FillType.SOLID
    line2.line.solid_fill.color = Color.blue
    line2.line.weight = 3.0
    line2.placement = cells.drawing.PlacementType.FREE_FLOATING

    line2.line.end_arrowhead_width = cells.drawing.MsoArrowheadWidth.MEDIUM
    line2.line.end_arrowhead_style = cells.drawing.MsoArrowheadStyle.ARROW
    line2.line.end_arrowhead_length = cells.drawing.MsoArrowheadLength.MEDIUM
    line2.line.begin_arrowhead_style = cells.drawing.MsoArrowheadStyle.ARROW_DIAMOND
    line2.line.begin_arrowhead_length = cells.drawing.MsoArrowheadLength.MEDIUM

    worksheet.is_gridlines_visible = False

    output_path = data_dir / "book1.out.xlsx"
    workbook.save(str(output_path))

if __name__ == "__main__":
    run_adding_an_arrow_head()