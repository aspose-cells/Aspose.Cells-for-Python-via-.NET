import os
from pathlib import Path
import aspose.cells as cells


def get_data_dir():
    return (
        Path(__file__).parent
        / ".." / ".." / "Data" / "DrawingObjects" / "Controls" / "AddingOvalControl"
    )


def run_adding_oval_control():
    data_dir = get_data_dir()
    if not os.path.isdir(str(data_dir)):
        os.makedirs(str(data_dir))

    workbook = cells.Workbook()

    # Add first oval
    oval1 = workbook.worksheets[0].shapes.add_oval(2, 0, 2, 0, 130, 160)
    oval1.placement = cells.drawing.PlacementType.FREE_FLOATING
    oval1.line.weight = 1.0
    oval1.line.dash_style = cells.drawing.MsoLineDashStyle.SOLID

    # Add second oval (circle)
    oval2 = workbook.worksheets[0].shapes.add_oval(9, 0, 2, 15, 130, 130)
    oval2.placement = cells.drawing.PlacementType.FREE_FLOATING
    oval2.line.weight = 1.0
    oval2.line.dash_style = cells.drawing.MsoLineDashStyle.SOLID

    output_path = os.path.join(str(data_dir), "book1.out.xls")
    workbook.save(output_path)


if __name__ == "__main__":
    run_adding_oval_control()