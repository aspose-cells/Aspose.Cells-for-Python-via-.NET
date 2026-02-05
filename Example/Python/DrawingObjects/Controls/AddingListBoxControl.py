import os
from pathlib import Path
import aspose.cells as cells


def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "DrawingObjects" / "Controls" / "AddingListBoxControl"


def run_adding_list_box_control():
    data_dir = get_data_dir()
    if not data_dir.is_dir():
        data_dir.mkdir(parents=True, exist_ok=True)

    workbook = cells.Workbook()
    sheet = workbook.worksheets[0]
    cells_coll = sheet.cells

    # Input a value.
    cells_coll.get("B3").put_value("Choose Dept:")
    # Set it bold.
    style = cells_coll.get("B3").get_style()
    style.font.is_bold = True
    cells_coll.get("B3").set_style(style)

    # Input list values.
    cells_coll.get("A2").put_value("Sales")
    cells_coll.get("A3").put_value("Finance")
    cells_coll.get("A4").put_value("MIS")
    cells_coll.get("A5").put_value("R&D")
    cells_coll.get("A6").put_value("Marketing")
    cells_coll.get("A7").put_value("HRA")

    # Add a new list box.
    list_box = sheet.shapes.add_list_box(2, 0, 3, 0, 122, 100)

    # Set properties.
    list_box.placement = cells.drawing.PlacementType.FREE_FLOATING
    list_box.linked_cell = "A1"
    list_box.input_range = "A2:A7"
    list_box.selection_type = cells.drawing.SelectionType.SINGLE
    list_box.shadow = True

    # Save the workbook.
    output_path = data_dir / "book1.out.xls"
    workbook.save(str(output_path))


if __name__ == "__main__":
    run_adding_list_box_control()