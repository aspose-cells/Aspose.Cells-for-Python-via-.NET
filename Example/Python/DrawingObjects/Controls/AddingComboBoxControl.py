import os
from pathlib import Path
import aspose.cells as cells

def get_data_dir():
    return (Path(__file__).parent /
            ".." / ".." /
            ".." / "Data" /
            "DrawingObjects" / "Controls" / "AddingComboBoxControl")

def run_adding_combo_box_control():
    data_dir = get_data_dir()
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)

    workbook = cells.Workbook()
    sheet = workbook.worksheets[0]
    worksheet_cells = sheet.cells

    # Input a value.
    cell_b3 = worksheet_cells.get("B3")
    cell_b3.put_value("Employee:")
    style_b3 = cell_b3.get_style()
    style_b3.font.is_bold = True
    cell_b3.set_style(style_b3)

    # Input some values that denote the input range for the combo box.
    for row, value in enumerate(
        ["Emp001", "Emp002", "Emp003", "Emp004", "Emp005", "Emp006"], start=2):
        worksheet_cells.get(row, 0).put_value(value)  # Column A is index 0

    # Add a new combo box.
    combo_box = sheet.shapes.add_combo_box(2, 0, 2, 0, 22, 100)

    # Set properties.
    combo_box.linked_cell = "A1"
    combo_box.input_range = "A2:A7"
    combo_box.drop_down_lines = 5
    combo_box.shadow = True

    # AutoFit columns.
    sheet.auto_fit_columns()

    # Save the file.
    output_path = os.path.join(data_dir, "book1.out.xls")
    workbook.save(output_path)

if __name__ == "__main__":
    run_adding_combo_box_control()