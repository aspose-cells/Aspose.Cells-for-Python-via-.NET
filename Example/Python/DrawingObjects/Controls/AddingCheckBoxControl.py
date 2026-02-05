import os
from pathlib import Path
import aspose.cells as cells

def get_data_dir():
    return (
        Path(__file__).parent
        / ".." / ".." / ".."
        / "Data" / "DrawingObjects" / "Controls" / "AddingCheckBoxControl"
    )

def run_adding_check_box_control():
    data_dir = get_data_dir()
    if not os.path.isdir(str(data_dir)):
        os.makedirs(str(data_dir))

    workbook = cells.Workbook()
    worksheet = workbook.worksheets[0]

    index = worksheet.check_boxes.add(5, 5, 100, 120)
    checkbox = worksheet.check_boxes[index]
    checkbox.text = "Click it!"

    cell = worksheet.cells.get("B1")
    cell.put_value("LnkCell")
    checkbox.linked_cell = "B1"
    checkbox.value = True

    output_path = os.path.join(str(data_dir), "book1.out.xls")
    workbook.save(output_path)

if __name__ == "__main__":
    run_adding_check_box_control()