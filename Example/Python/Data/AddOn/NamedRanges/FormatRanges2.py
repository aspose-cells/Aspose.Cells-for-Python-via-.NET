import os
import aspose.cells as cells
from aspose.pydrawing import Color

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "..", "..", "Data", "02_OutputDirectory"))

def run_format_ranges2():
    output_dir = get_output_directory()
    workbook = cells.Workbook()
    worksheet = workbook.worksheets[0]

    cell = worksheet.cells.get("G8")
    cell.put_value("Hello World From Aspose")

    range_obj = worksheet.cells.create_range(5, 5, 5, 5)

    range_obj.set_outline_border(cells.BorderType.TOP_BORDER, cells.CellBorderType.THICK, Color.blue)
    range_obj.set_outline_border(cells.BorderType.BOTTOM_BORDER, cells.CellBorderType.THICK, Color.blue)
    range_obj.set_outline_border(cells.BorderType.LEFT_BORDER, cells.CellBorderType.THICK, Color.blue)
    range_obj.set_outline_border(cells.BorderType.RIGHT_BORDER, cells.CellBorderType.THICK, Color.blue)

    output_path = os.path.join(output_dir, "outputFormatRanges2.xlsx")
    workbook.save(output_path)

    print("FormatRanges2 executed successfully.")

if __name__ == "__main__":
    run_format_ranges2()