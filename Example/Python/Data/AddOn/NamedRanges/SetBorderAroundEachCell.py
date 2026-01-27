import os
import aspose.cells as cells
from aspose.pydrawing import Color

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "..", "..", "Data", "02_OutputDirectory"))

def run_set_border_around_each_cell():
    output_dir = get_output_directory()

    # Instantiate a new Workbook.
    workbook = cells.Workbook()

    # Access the cells in the first worksheet.
    sheet_cells = workbook.worksheets[0].cells

    # Create a range of cells.
    cell_range = sheet_cells.create_range("D6", "M16")

    # Create the style and add it to the style collection.
    style = workbook.create_style()

    # Specify the font settings.
    style.font.name = "Arial"
    style.font.is_bold = True
    style.font.color = Color.blue

    # Set the borders.
    top_border = style.borders.get(cells.BorderType.TOP_BORDER)
    top_border.line_style = cells.CellBorderType.THICK
    top_border.color = Color.blue

    left_border = style.borders.get(cells.BorderType.LEFT_BORDER)
    left_border.line_style = cells.CellBorderType.THICK
    left_border.color = Color.blue

    bottom_border = style.borders.get(cells.BorderType.BOTTOM_BORDER)
    bottom_border.line_style = cells.CellBorderType.THICK
    bottom_border.color = Color.blue

    right_border = style.borders.get(cells.BorderType.RIGHT_BORDER)
    right_border.line_style = cells.CellBorderType.THICK
    right_border.color = Color.blue

    # Create StyleFlag object and enable formatting attributes.
    flag = cells.StyleFlag()
    flag.font = True
    flag.borders = True

    # Apply the style with format settings to the range.
    cell_range.apply_style(style, flag)

    # Save the Excel file.
    output_path = os.path.join(output_dir, "outputSetBorderAroundEachCell.xlsx")
    workbook.save(output_path)

    print("SetBorderAroundEachCell executed successfully.")

if __name__ == "__main__":
    run_set_border_around_each_cell()
