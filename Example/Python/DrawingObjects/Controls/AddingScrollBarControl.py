import os
from pathlib import Path
import aspose.cells as cells
from aspose.pydrawing import Color


def get_data_dir():
    return (
        Path(__file__).parent
        / ".." / ".." / ".."
        / "Data" / "DrawingObjects" / "Controls" / "AddingScrollBarControl"
    ).resolve()


def run_adding_scroll_bar_control():
    data_dir = get_data_dir()
    if not data_dir.is_dir():
        data_dir.mkdir(parents=True, exist_ok=True)

    workbook = cells.Workbook()
    worksheet = workbook.worksheets[0]
    worksheet.is_gridlines_visible = False
    cells_obj = worksheet.cells

    cell_a1 = cells_obj.get("A1")
    cell_a1.put_value(1)

    style = cell_a1.get_style()
    style.font.color = Color.maroon
    style.font.is_bold = True
    style.number = 1
    cell_a1.set_style(style)

    scrollbar = worksheet.shapes.add_scroll_bar(0, 0, 1, 0, 125, 20)
    scrollbar.placement = cells.drawing.PlacementType.FREE_FLOATING
    scrollbar.linked_cell = "A1"
    scrollbar.max = 20
    scrollbar.min = 1
    scrollbar.incremental_change = 1
    scrollbar.page_change = 5
    scrollbar.shadow = True

    output_path = data_dir / "book1.out.xls"
    workbook.save(str(output_path))


if __name__ == "__main__":
    run_adding_scroll_bar_control()