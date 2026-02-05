import os
from pathlib import Path
import aspose.cells as cells
from aspose.cells import Workbook

def get_data_dir() -> Path:
    # Adjust the relative path as needed to match the original data directory structure
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "DrawingObjects" / "Controls" / "AddingLabelControl"

def run_adding_label_control():
    data_dir = get_data_dir()
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)

    workbook = Workbook()
    sheet = workbook.worksheets[0]

    # Add a new label to the worksheet.
    label = sheet.shapes.add_label(2, 0, 2, 0, 60, 120)

    # Set the caption of the label.
    label.text = "This is a Label"

    # Set the placement type (free floating).
    label.placement = cells.drawing.PlacementType.FREE_FLOATING

    # Save the workbook.
    output_path = os.path.join(data_dir, "book1.out.xls")
    workbook.save(output_path)

if __name__ == "__main__":
    run_adding_label_control()