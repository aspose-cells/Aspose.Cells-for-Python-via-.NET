import os
from pathlib import Path
import aspose.cells as cells

def get_data_dir():
    return (
        Path(__file__).parent
        / ".." / ".." / ".." / ".."
        / "Data" / "DrawingObjects" / "Pictures" / "PositioningPictures" / "AbsolutePositioning"
    )

def run_absolute_positioning():
    data_dir = get_data_dir()

    # Instantiating a Workbook object
    workbook = cells.Workbook()

    # Adding a new worksheet to the Workbook object
    sheet_index = workbook.worksheets.add()

    # Obtaining the reference of the newly added worksheet by passing its sheet index
    worksheet = workbook.worksheets[sheet_index]

    # Adding a picture at the location of cell F6 (row 5, column 5)
    picture_index = worksheet.pictures.add(5, 5, os.path.join(data_dir, "logo.jpg"))

    # Accessing the newly added picture
    picture = worksheet.pictures[picture_index]

    # Absolute positioning of the picture in unit of pixels
    picture.left = 60
    picture.top = 10

    # Saving the Excel file
    workbook.save(os.path.join(data_dir, "book1.out.xls"))

if __name__ == "__main__":
    run_absolute_positioning()