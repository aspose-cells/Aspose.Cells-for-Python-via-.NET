import os
from pathlib import Path
import aspose.cells as cells

def get_data_dir():
    return (
        Path(__file__).parent
        / ".." / ".." / ".."
        / "Data" / "DrawingObjects" / "Controls" / "AddingLineControl"
    ).resolve()

def run_adding_line_control():
    data_dir = get_data_dir()
    if not os.path.isdir(str(data_dir)):
        os.makedirs(str(data_dir))

    workbook = cells.Workbook()
    worksheet = workbook.worksheets[0]

    # Add first line
    line1 = worksheet.shapes.add_line(5, 0, 1, 0, 0, 250)
    line1.line.dash_style = cells.drawing.MsoLineDashStyle.SOLID
    line1.placement = cells.drawing.PlacementType.FREE_FLOATING

    # Add second line
    line2 = worksheet.shapes.add_line(7, 0, 1, 0, 85, 250)
    line2.line.dash_style = cells.drawing.MsoLineDashStyle.DASH_LONG_DASH
    line2.line.weight = 4.0
    line2.placement = cells.drawing.PlacementType.FREE_FLOATING

    # Add third line
    line3 = worksheet.shapes.add_line(13, 0, 1, 0, 0, 250)
    line3.line.dash_style = cells.drawing.MsoLineDashStyle.SOLID
    line3.placement = cells.drawing.PlacementType.FREE_FLOATING

    # Hide gridlines
    workbook.worksheets[0].is_gridlines_visible = False

    # Save the workbook
    output_path = os.path.join(str(data_dir), "book1.out.xls")
    workbook.save(output_path)

if __name__ == "__main__":
    run_adding_line_control()
