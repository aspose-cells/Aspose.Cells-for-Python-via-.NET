import os
from pathlib import Path
import aspose.cells as cells
from aspose.pydrawing import Color

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "DrawingObjects" / "Controls" / "AddingTextBoxControl"

def run_adding_text_box_control():
    data_dir = get_data_dir()
    if not os.path.isdir(str(data_dir)):
        os.makedirs(str(data_dir))

    workbook = cells.Workbook()
    worksheet = workbook.worksheets[0]

    # First textbox
    textbox_index = worksheet.text_boxes.add(2, 1, 160, 200)
    textbox0 = worksheet.text_boxes[textbox_index]
    textbox0.text = "ASPOSE______The .NET & JAVA Component Publisher!"
    textbox0.placement = cells.drawing.PlacementType.FREE_FLOATING
    textbox0.font.color = Color.blue
    textbox0.font.is_bold = True
    textbox0.font.size = 14
    textbox0.font.is_italic = True
    textbox0.add_hyperlink("http://www.aspose.com/")

    lineformat = textbox0.line
    lineformat.weight = 6.0
    lineformat.dash_style = cells.drawing.MsoLineDashStyle.SQUARE_DOT

    # Second textbox
    textbox_index = worksheet.text_boxes.add(15, 4, 85, 120)
    textbox1 = worksheet.text_boxes[textbox_index]
    textbox1.text = "This is another simple text box"
    textbox1.placement = cells.drawing.PlacementType.MOVE_AND_SIZE

    output_path = os.path.join(str(data_dir), "book1.out.xls")
    workbook.save(output_path)

if __name__ == "__main__":
    run_adding_text_box_control()
