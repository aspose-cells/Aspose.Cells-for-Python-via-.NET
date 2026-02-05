import os
from pathlib import Path
import aspose.cells as cells
from aspose.cells.drawing import PlacementType, MsoLineDashStyle

def get_data_dir():
    return (
        Path(__file__).parent
        / ".." / ".." / ".."
        / "Data" / "DrawingObjects" / "Controls" / "AddingRectangleControl"
    )

def run_adding_rectangle_control():
    data_dir = get_data_dir()
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)

    workbook = cells.Workbook()
    rectangle = workbook.worksheets[0].shapes.add_rectangle(3, 0, 2, 0, 70, 130)
    rectangle.placement = PlacementType.FREE_FLOATING
    rectangle.line.weight = 4.0
    rectangle.line.dash_style = MsoLineDashStyle.SOLID

    output_path = os.path.join(str(data_dir), "book1.out.xls")
    workbook.save(output_path)

if __name__ == "__main__":
    run_adding_rectangle_control()