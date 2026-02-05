import os
from pathlib import Path
import aspose.cells as cells

def get_data_dir():
    return (Path(__file__).parent
            / ".." / ".." / ".."
            / "Data" / "DrawingObjects" / "Controls" / "ManipulatingTextBoxControls").resolve()

def run_manipulating_text_box_controls():
    data_dir = get_data_dir()

    # Open the existing Excel file.
    input_file = os.path.join(data_dir, "book1.xls")
    workbook = cells.Workbook(input_file)

    # Get the first worksheet.
    worksheet = workbook.worksheets[0]

    # Get the first textbox object and its text.
    textbox0 = worksheet.text_boxes[0]
    text0 = textbox0.text

    # Get the second textbox object and its text.
    textbox1 = worksheet.text_boxes[1]
    text1 = textbox1.text

    # Change the text of the second textbox.
    textbox1.text = "This is an alternative text"

    # Save the Excel file.
    output_file = os.path.join(data_dir, "output.out.xls")
    workbook.save(output_file)

if __name__ == "__main__":
    run_manipulating_text_box_controls()