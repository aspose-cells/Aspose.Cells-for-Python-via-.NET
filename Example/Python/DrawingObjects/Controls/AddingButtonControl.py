import os
from pathlib import Path
import aspose.cells as cells
from aspose.pydrawing import Color


def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "DrawingObjects" / "Controls" / "AddingButtonControl"


def run_adding_button_control():
    data_dir = get_data_dir()
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)

    workbook = cells.Workbook()
    sheet = workbook.worksheets[0]

    button = sheet.shapes.add_button(2, 0, 2, 0, 28, 80)
    button.text = "Aspose"
    button.placement = cells.drawing.PlacementType.FREE_FLOATING
    button.font.name = "Tahoma"
    button.font.is_bold = True
    button.font.color = Color.blue
    button.add_hyperlink("http://www.aspose.com/")

    output_path = os.path.join(data_dir, "book1.out.xls")
    workbook.save(output_path)


if __name__ == "__main__":
    run_adding_button_control()