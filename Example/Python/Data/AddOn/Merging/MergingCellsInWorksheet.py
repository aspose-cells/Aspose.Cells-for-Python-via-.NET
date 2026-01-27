import os
import aspose.cells as cells
from aspose.pydrawing import Color


def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "..", "..", "Data", "02_OutputDirectory"))


def run_merging_cells_in_worksheet():
    workbook = cells.Workbook()
    worksheet = workbook.worksheets[0]
    ws_cells = worksheet.cells

    # Merge cells C6:E7 into C6
    ws_cells.merge(5, 2, 2, 3)

    # Set value for merged cell
    ws_cells.get(5, 2).put_value("This is my value")

    # Get and modify style
    style = ws_cells.get(5, 2).get_style()
    font = style.font
    font.name = "Times New Roman"
    font.size = 18
    font.color = Color.blue
    font.is_bold = True
    font.is_italic = True

    style.foreground_color = Color.red
    style.pattern = cells.BackgroundType.SOLID

    # Apply style
    ws_cells.get(5, 2).set_style(style)

    # Save workbook
    output_path = os.path.join(get_output_directory(), "outputMergingCellsInWorksheet.xlsx")
    workbook.save(output_path)

    print("MergingCellsInWorksheet executed successfully.")


if __name__ == "__main__":
    run_merging_cells_in_worksheet()
