import os
import aspose.cells as cells
from aspose.pydrawing import Color


def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "..", "..", "Data", "02_OutputDirectory"))


def run_copy_named_ranges():
    workbook = cells.Workbook()
    worksheet = workbook.worksheets[0]

    # Create the first range and name it
    range1 = worksheet.cells.create_range("E12", "I12")
    range1.name = "MyRange"

    # Set outline borders for the range
    border_color = Color.from_argb(0, 0, 128)
    range1.set_outline_border(cells.BorderType.TOP_BORDER, cells.CellBorderType.MEDIUM, border_color)
    range1.set_outline_border(cells.BorderType.BOTTOM_BORDER, cells.CellBorderType.MEDIUM, border_color)
    range1.set_outline_border(cells.BorderType.LEFT_BORDER, cells.CellBorderType.MEDIUM, border_color)
    range1.set_outline_border(cells.BorderType.RIGHT_BORDER, cells.CellBorderType.MEDIUM, border_color)

    # Put values into the first range using absolute cell coordinates
    start_row = range1.first_row
    start_col = range1.first_column
    worksheet.cells.get(start_row, start_col).put_value("Test")          # E12
    worksheet.cells.get(start_row, start_col + 4).put_value("123")      # I12

    # Create the second range, name it, and copy the first range into it
    range2 = worksheet.cells.create_range("B3", "F3")
    range2.name = "testrange"
    range2.copy(range1)

    # Save the workbook
    output_path = os.path.join(get_output_directory(), "outputCopyNamedRanges.xlsx")
    workbook.save(output_path)

    print("CopyNamedRanges executed successfully.")


if __name__ == "__main__":
    run_copy_named_ranges()
