import os
import aspose.cells as cells
from aspose.pydrawing import Color


def get_source_directory():
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "Data", "01_SourceDirectory")
    )


def get_output_directory():
    return os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..", "..", "..", "..", "Data", "02_OutputDirectory")
    )


def run_union_of_ranges():
    source_dir = get_source_directory()
    output_dir = get_output_directory()

    # Ensure the output directory exists
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    input_path = os.path.join(source_dir, "sampleUnionOfRanges.xlsx")
    workbook = cells.Workbook(input_path)

    # Get the named ranges
    ranges = workbook.worksheets.get_named_ranges()

    # Create a style and set shading
    style = workbook.create_style()
    style.foreground_color = Color.red
    style.pattern = cells.BackgroundType.SOLID

    # Create a StyleFlag to apply cell shading
    flag = cells.StyleFlag()
    flag.cell_shading = True

    # Perform union operation on the first two named ranges
    union_ranges = ranges[0].union(ranges[1])

    # Apply the style to each range in the union result
    for rng in union_ranges:
        rng.apply_style(style, flag)

    # Save the modified workbook
    output_path = os.path.join(output_dir, "outputUnionOfRanges.xlsx")
    workbook.save(output_path)

    print("UnionOfRanges executed successfully.")


if __name__ == "__main__":
    run_union_of_ranges()
