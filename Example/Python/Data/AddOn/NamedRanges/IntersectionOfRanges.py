import os
import aspose.cells as cells
from aspose.pydrawing import Color


def get_source_directory() -> str:
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "Data", "01_SourceDirectory")
    )


def get_output_directory() -> str:
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "Data", "02_OutputDirectory")
    )


def run_intersection_of_ranges() -> None:
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    # Ensure the output directory exists
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    # Load the workbook
    workbook_path = os.path.join(source_dir, "sampleIntersectionOfRanges.xlsx")
    workbook = cells.Workbook(workbook_path)

    # Retrieve named ranges
    ranges = workbook.worksheets.get_named_ranges()

    # Determine if the first range intersects the second range
    is_intersect = ranges[0].is_intersect(ranges[1])

    # Create a style with solid red shading
    style = workbook.create_style()
    style.foreground_color = Color.red
    style.pattern = cells.BackgroundType.SOLID

    # Prepare a StyleFlag to apply cell shading only
    flag = cells.StyleFlag()
    flag.cell_shading = True

    if is_intersect:
        # Obtain the intersecting range
        intersection = ranges[0].intersect(ranges[1])
        # Name the intersecting range
        intersection.name = "Intersection"
        # Apply the style to the intersecting range
        intersection.apply_style(style, flag)

    # Save the modified workbook
    output_path = os.path.join(output_dir, "outputIntersectionOfRanges.xlsx")
    workbook.save(output_path)


if __name__ == "__main__":
    run_intersection_of_ranges()