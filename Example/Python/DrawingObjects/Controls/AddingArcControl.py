import os
from pathlib import Path
import aspose.cells as cells
from aspose.pydrawing import Color


def get_data_dir():
    return (
        Path(__file__).parent
        / ".."
        / ".."
        / "Data"
        / "DrawingObjects"
        / "Controls"
        / "AddingArcControl"
    ).resolve()


def run_adding_arc_control():
    data_dir = get_data_dir()
    os.makedirs(data_dir, exist_ok=True)

    workbook = cells.Workbook()
    worksheet = workbook.worksheets[0]

    # Add first arc shape
    arc1 = worksheet.shapes.add_arc(2, 0, 2, 0, 130, 130)
    arc1.fill.fill_type = cells.drawing.FillType.SOLID
    arc1.fill.solid_fill.color = Color.blue
    arc1.placement = cells.drawing.PlacementType.FREE_FLOATING
    arc1.line.weight = 1.0
    arc1.line.dash_style = cells.drawing.MsoLineDashStyle.SOLID

    # Add second arc shape
    arc2 = worksheet.shapes.add_arc(9, 0, 2, 0, 130, 130)
    arc2.line.fill_type = cells.drawing.FillType.SOLID
    arc2.line.solid_fill.color = Color.blue
    arc2.placement = cells.drawing.PlacementType.FREE_FLOATING
    arc2.line.weight = 1.0
    arc2.line.dash_style = cells.drawing.MsoLineDashStyle.SOLID

    output_path = data_dir / "book1.out.xls"
    workbook.save(str(output_path))


if __name__ == "__main__":
    run_adding_arc_control()
