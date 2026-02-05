import os
from pathlib import Path
import aspose.cells as cells

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "DrawingObjects" / "Controls" / "AddingGroupBoxControl"

def run_adding_group_box_control():
    data_dir = get_data_dir()
    if not data_dir.is_dir():
        data_dir.mkdir(parents=True, exist_ok=True)

    workbook = cells.Workbook()
    worksheet = workbook.worksheets[0]

    # Add a group box
    box = worksheet.shapes.add_group_box(1, 0, 1, 0, 300, 250)
    box.text = "Age Groups"
    box.placement = cells.drawing.PlacementType.FREE_FLOATING
    box.shadow = False

    # Add first radio button
    radio1 = worksheet.shapes.add_radio_button(3, 0, 2, 0, 30, 110)
    radio1.text = "20-29"
    radio1.linked_cell = "A1"
    radio1.shadow = True
    radio1.line.weight = 4.0
    radio1.line.dash_style = cells.drawing.MsoLineDashStyle.SOLID

    # Add second radio button
    radio2 = worksheet.shapes.add_radio_button(6, 0, 2, 0, 30, 110)
    radio2.text = "30-39"
    radio2.linked_cell = "A1"
    radio2.shadow = True
    radio2.line.weight = 4.0
    radio2.line.dash_style = cells.drawing.MsoLineDashStyle.SOLID

    # Add third radio button
    radio3 = worksheet.shapes.add_radio_button(9, 0, 2, 0, 30, 110)
    radio3.text = "40-49"
    radio3.linked_cell = "A1"
    radio3.shadow = True
    radio3.line.weight = 4.0
    radio3.line.dash_style = cells.drawing.MsoLineDashStyle.SOLID

    # Group the shapes
    shape_objects = [box, radio1, radio2, radio3]
    worksheet.shapes.group(shape_objects)

    # Save the workbook
    output_path = data_dir / "book1.out.xls"
    workbook.save(str(output_path))

if __name__ == "__main__":
    run_adding_group_box_control()
