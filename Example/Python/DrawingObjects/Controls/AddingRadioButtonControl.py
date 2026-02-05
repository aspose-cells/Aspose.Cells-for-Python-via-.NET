import os
from pathlib import Path
import aspose.cells as cells
from aspose.cells.drawing import MsoLineDashStyle


def get_data_dir() -> Path:
    return (
        Path(__file__).parent.parent.parent
        / "Data"
        / "DrawingObjects"
        / "Controls"
        / "AddingRadioButtonControl"
    )


def run_adding_radio_button_control() -> None:
    data_dir = get_data_dir()
    data_dir.mkdir(parents=True, exist_ok=True)

    workbook = cells.Workbook()
    worksheet = workbook.worksheets[0]

    # Insert header text and make it bold
    cell = worksheet.cells.get("C2")
    cell.put_value("Age Groups")
    style = cell.get_style()
    style.font.is_bold = True
    cell.set_style(style)

    # First radio button
    radio1 = worksheet.shapes.add_radio_button(3, 0, 2, 0, 30, 110)
    radio1.text = "20-29"
    radio1.linked_cell = "A1"
    radio1.shadow = True
    radio1.line.weight = 4.0
    radio1.line.dash_style = MsoLineDashStyle.SOLID

    # Second radio button
    radio2 = worksheet.shapes.add_radio_button(6, 0, 2, 0, 30, 110)
    radio2.text = "30-39"
    radio2.linked_cell = "A1"
    radio2.shadow = True
    radio2.line.weight = 4.0
    radio2.line.dash_style = MsoLineDashStyle.SOLID

    # Third radio button
    radio3 = worksheet.shapes.add_radio_button(9, 0, 2, 0, 30, 110)
    radio3.text = "40-49"
    radio3.linked_cell = "A1"
    radio3.shadow = True
    radio3.line.weight = 4.0
    radio3.line.dash_style = MsoLineDashStyle.SOLID

    # Save the workbook
    output_path = data_dir / "book1.out.xls"
    workbook.save(str(output_path))


if __name__ == "__main__":
    run_adding_radio_button_control()
