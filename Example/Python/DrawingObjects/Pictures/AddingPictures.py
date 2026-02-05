import os
from pathlib import Path
import aspose.cells as cells

def get_data_dir():
    return (
        Path(__file__).parent
        / ".."
        / ".."
        / "Data"
        / "DrawingObjects"
        / "Pictures"
        / "AddingPictures"
    )

def _ensure_placeholder_image(path: Path):
    if not path.is_file():
        # Minimal 1x1 JPEG binary data
        jpeg_bytes = (
            b"\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00\x48\x00\x48\x00\x00"
            b"\xff\xdb\x00C\x00" + b"\x00" * 64 +
            b"\xff\xc0\x00\x11\x08\x00\x01\x00\x01\x03\x01\x22\x00\x02\x11\x01\x03\x11\x01"
            b"\xff\xda\x00\x0c\x03\x01\x00\x02\x11\x03\x11\x00?"
            b"\xd9"
        )
        path.write_bytes(jpeg_bytes)

def run_adding_pictures():
    data_dir = get_data_dir()
    data_dir.mkdir(parents=True, exist_ok=True)

    picture_path = data_dir / "logo.jpg"
    _ensure_placeholder_image(picture_path)

    workbook = cells.Workbook()
    sheet_index = workbook.worksheets.add()
    worksheet = workbook.worksheets[sheet_index]

    # Add picture to cell F6 (row index 5, column index 5)
    worksheet.pictures.add(5, 5, str(picture_path))

    output_path = data_dir / "output.xls"
    workbook.save(str(output_path))

if __name__ == "__main__":
    run_adding_pictures()