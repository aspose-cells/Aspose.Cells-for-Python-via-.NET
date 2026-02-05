import os
from pathlib import Path
import aspose.cells as cells

def get_data_dir() -> str:
    return str(
        Path(__file__).parent
        / ".." / ".." / ".."
        / "Data" / "DrawingObjects" / "OLE" / "InsertingOLEObjects"
    )

def run_inserting_ole_objects():
    data_dir = get_data_dir()
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)

    # Create a new workbook
    workbook = cells.Workbook()
    sheet = workbook.worksheets[0]

    # Load image bytes
    image_path = os.path.join(data_dir, "logo.jpg")
    with open(image_path, "rb") as f:
        image_data = f.read()

    # Load OLE object file bytes
    ole_path = os.path.join(data_dir, "book1.xls")
    with open(ole_path, "rb") as f:
        object_data = f.read()

    # Add OLE object with image placeholder
    sheet.ole_objects.add(14, 3, 200, 220, image_data)

    # Set embedded OLE object data
    sheet.ole_objects[0].object_data = object_data

    # Save the workbook
    output_path = os.path.join(data_dir, "output.out.xls")
    workbook.save(output_path)

if __name__ == "__main__":
    run_inserting_ole_objects()