import os
from pathlib import Path
import aspose.cells as cells

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / ".." / "Data" / "DrawingObjects" / "Pictures" / "PositioningPictures" / "ProportionalPositioning"

def run_proportional_positioning():
    data_dir = get_data_dir()
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir)

    workbook = cells.Workbook()
    sheet_index = workbook.worksheets.add()
    worksheet = workbook.worksheets[sheet_index]

    picture_index = worksheet.pictures.add(5, 5, os.path.join(data_dir, "logo.jpg"))
    picture = worksheet.pictures[picture_index]
    picture.upper_delta_x = 200
    picture.upper_delta_y = 200

    workbook.save(os.path.join(data_dir, "book1.out.xls"))

if __name__ == "__main__":
    run_proportional_positioning()