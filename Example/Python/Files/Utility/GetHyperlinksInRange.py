import os
from pathlib import Path
import aspose.cells as cells


def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Files" / "Utility" / "GetHyperlinksInRange"


def get_output_directory():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "02_OutputDirectory"


def run():
    # Input and output directories
    source_dir = get_data_dir()
    output_dir = get_output_directory()

    # Open the workbook
    workbook = cells.Workbook(str(source_dir / "HyperlinksSample.xlsx"))

    # Get the first worksheet
    worksheet = workbook.worksheets[0]

    # Create a range A2:B3
    range_obj = worksheet.cells.create_range("A2", "B3")

    # Get hyperlinks in the range
    hyperlinks = range_obj.hyperlinks

    for link in hyperlinks:
        print(f"{link.area} : {link.address}")
        # Delete the hyperlink
        link.delete()

    # Save the modified workbook
    workbook.save(str(output_dir / "HyperlinksSample_out.xlsx"))


if __name__ == "__main__":
    run()