import os
import aspose.cells as cells
from aspose.pydrawing import Color

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "..", "..", "Data", "02_OutputDirectory"))

def run_create_named_range_of_cells():
    workbook = cells.Workbook()
    worksheet = workbook.worksheets[0]

    range_obj = worksheet.cells.create_range("B4", "G14")
    range_obj.name = "TestRange"

    style = workbook.create_style()
    style.pattern = cells.BackgroundType.SOLID
    style.foreground_color = Color.yellow
    range_obj.set_style(style)

    output_file = os.path.join(get_output_directory(), "outputCreateNamedRangeofCells.xlsx")
    workbook.save(output_file)

    print("CreateNamedRangeofCells executed successfully.")

if __name__ == "__main__":
    run_create_named_range_of_cells()