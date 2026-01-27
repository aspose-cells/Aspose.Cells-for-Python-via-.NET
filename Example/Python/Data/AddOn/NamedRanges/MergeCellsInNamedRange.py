import os
import aspose.cells as cells
from aspose.pydrawing import Color


def get_output_directory():
    return os.path.abspath(
        os.path.join(".", "..", "..", "..", "..", "Data", "02_OutputDirectory")
    )


def run_merge_cells_in_named_range():
    output_dir = get_output_directory()

    # Instantiate a new Workbook.
    wb1 = cells.Workbook()
    # Get the first worksheet in the workbook.
    worksheet1 = wb1.worksheets[0]

    # Create a range.
    mrange = worksheet1.cells.create_range("D6", "I12")
    # Name the range.
    mrange.name = "TestRange"
    # Merge the cells of the range.
    mrange.merge()

    # Get the range by name.
    range1 = wb1.worksheets.get_range_by_name("TestRange")

    # Define a style object.
    style = wb1.create_style()
    style.horizontal_alignment = cells.TextAlignmentType.CENTER
    style.vertical_alignment = cells.TextAlignmentType.CENTER
    style.pattern = cells.BackgroundType.SOLID
    style.foreground_color = Color.aqua

    # Create a StyleFlag object.
    flag = cells.StyleFlag()
    flag.horizontal_alignment = True
    flag.vertical_alignment = True
    flag.cell_shading = True

    # Apply the style to the range.
    range1.apply_style(style, flag)

    # Input data into the first cell of the range.
    top_cell = worksheet1.cells.get(range1.first_row, range1.first_column)
    top_cell.put_value("Welcome to Aspose APIs.")

    # Save the Excel file.
    wb1.save(os.path.join(output_dir, "outputMergeCellsInNamedRange.xlsx"))
    print("MergeCellsInNamedRange executed successfully.")


if __name__ == "__main__":
    run_merge_cells_in_named_range()
