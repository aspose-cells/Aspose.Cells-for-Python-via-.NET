import os
import aspose.cells as cells
from aspose.pydrawing import Color


def get_output_directory():
    return os.path.abspath(
        os.path.join(".", "..", "..", "..", "..", "Data", "02_OutputDirectory")
    )


def run_format_ranges1():
    output_dir = get_output_directory()

    # Instantiate a new Workbook.
    workbook = cells.Workbook()

    # Get the first worksheet in the book.
    ws = workbook.worksheets[0]

    # Create a range of cells.
    rng = ws.cells.create_range(1, 1, 5, 5)

    # Name the range.
    rng.name = "MyRange"

    # Declare and create a style object.
    stl = workbook.create_style()

    # Specify some Font settings.
    stl.font.name = "Arial"
    stl.font.is_bold = True
    stl.font.color = Color.red

    # Set the fill color of the range.
    stl.foreground_color = Color.yellow
    stl.pattern = cells.BackgroundType.SOLID

    # Create a StyleFlag object and set required attributes.
    flg = cells.StyleFlag()
    flg.font = True
    flg.cell_shading = True

    # Apply the style to the range.
    rng.apply_style(stl, flg)

    # Save the Excel file.
    output_path = os.path.join(output_dir, "outputFormatRanges1.xlsx")
    workbook.save(output_path)

    print("FormatRanges1 executed successfully.")


if __name__ == "__main__":
    run_format_ranges1()