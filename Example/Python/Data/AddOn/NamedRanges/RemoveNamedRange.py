import os
import aspose.cells as cells
from aspose.pydrawing import Color
from datetime import datetime


def get_output_directory():
    return os.path.abspath(
        os.path.join(".", "..", "..", "..", "..", "Data", "02_OutputDirectory")
    )


def run_remove_named_range():
    # Instantiate a new Workbook.
    workbook = cells.Workbook()

    # Get the worksheets collection.
    worksheets = workbook.worksheets

    # Get the first worksheet.
    worksheet = worksheets[0]

    # Create the first range and name it.
    range1 = worksheet.cells.create_range("E12", "I12")
    range1.name = "FirstRange"

    # Apply outline borders to the first range.
    range1.set_outline_border(
        cells.BorderType.TOP_BORDER,
        cells.CellBorderType.MEDIUM,
        Color.from_argb(0, 0, 128),
    )
    range1.set_outline_border(
        cells.BorderType.BOTTOM_BORDER,
        cells.CellBorderType.MEDIUM,
        Color.from_argb(0, 0, 128),
    )
    range1.set_outline_border(
        cells.BorderType.LEFT_BORDER,
        cells.CellBorderType.MEDIUM,
        Color.from_argb(0, 0, 128),
    )
    range1.set_outline_border(
        cells.BorderType.RIGHT_BORDER,
        cells.CellBorderType.MEDIUM,
        Color.from_argb(0, 0, 128),
    )

    # Put values into some cells of the first range.
    range1.get(0, 0).put_value("Test")
    range1.get(0, 4).put_value(123)

    # Create the second range, name it, and copy the first range into it.
    range2 = worksheet.cells.create_range("B3", "F3")
    range2.name = "SecondRange"
    range2.copy(range1)

    # Clear the contents of the first range.
    worksheet.cells.clear_range(
        range1.first_row,
        range1.first_column,
        range1.first_row + range1.row_count - 1,
        range1.first_column + range1.column_count - 1,
    )

    # Remove the named range "FirstRange" from the workbook.
    try:
        # Try the .remove_at method (available in some versions).
        worksheets.names.remove_at(0)
    except AttributeError:
        # Fallback: remove by Name object.
        try:
            name_obj = worksheets.names[0]
            worksheets.names.remove(name_obj)
        except Exception:
            pass

    # Save the workbook.
    output_file = os.path.join(get_output_directory(), "outputRemoveNamedRange.xlsx")
    workbook.save(output_file)

    print("RemoveNamedRange executed successfully.")


if __name__ == "__main__":
    run_remove_named_range()
