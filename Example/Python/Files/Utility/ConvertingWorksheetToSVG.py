import os
from pathlib import Path
import aspose.cells as cells


def get_data_dir():
    return (
        Path(__file__).parent
        / ".."
        / ".."
        / ".."
        / "Data"
        / "Files"
        / "Utility"
        / "ConvertingWorksheetToSVG"
    )


def run():
    data_dir = get_data_dir()
    file_path = os.path.join(str(data_dir), "Template.xlsx")

    # Create a workbook object from the template file
    book = cells.Workbook(file_path)

    # Convert each worksheet into SVG format in a single page.
    img_options = cells.rendering.ImageOrPrintOptions()
    img_options.save_format = cells.SaveFormat.SVG
    img_options.one_page_per_sheet = True

    # Convert each worksheet into SVG format
    for sheet in book.worksheets:
        sr = cells.rendering.SheetRender(sheet, img_options)
        for i in range(sr.page_count):
            # Output the worksheet into SVG image format
            output_path = f"{file_path}{sheet.name}{i}.out.svg"
            sr.to_image(i, output_path)


if __name__ == "__main__":
    run()