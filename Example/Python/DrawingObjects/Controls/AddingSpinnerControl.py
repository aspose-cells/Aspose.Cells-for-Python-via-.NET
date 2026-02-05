import os
from pathlib import Path
import aspose.cells as cells
from aspose.pydrawing import Color


def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "DrawingObjects" / "Controls" / "AddingSpinnerControl"


def run_adding_spinner_control():
    data_dir = str(get_data_dir())
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)

    workbook = cells.Workbook()
    worksheet = workbook.worksheets[0]
    sheet_cells = worksheet.cells

    cell_a1 = sheet_cells.get("A1")
    cell_a1.put_value("Select Value:")
    style_a1 = cell_a1.get_style()
    style_a1.font.color = Color.red
    style_a1.font.is_bold = True
    cell_a1.set_style(style_a1)

    cell_a2 = sheet_cells.get("A2")
    cell_a2.put_value(0)
    style_a2 = cell_a2.get_style()
    style_a2.foreground_color = Color.black
    style_a2.pattern = cells.BackgroundType.SOLID
    style_a2.font.color = Color.white
    style_a2.font.is_bold = True
    cell_a2.set_style(style_a2)

    spinner = worksheet.shapes.add_spinner(1, 0, 1, 0, 20, 18)
    spinner.placement = cells.drawing.PlacementType.FREE_FLOATING
    spinner.linked_cell = "A2"
    spinner.max = 10
    spinner.min = 0
    spinner.incremental_change = 2
    spinner.shadow = True

    output_path = os.path.join(data_dir, "book1.out.xls")
    workbook.save(output_path)


if __name__ == "__main__":
    run_adding_spinner_control()