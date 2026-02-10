import os
from pathlib import Path
import aspose.cells as cells


def get_data_dir() -> Path:
    return (
        Path(__file__).parent.parent.parent
        / "Data"
        / "Files"
        / "Utility"
        / "WorksheetToImage"
    )


def _ensure_source_workbook(data_dir: Path) -> Path:
    src = data_dir / "MyTestBook1.xls"
    if not src.is_file():
        wb = cells.Workbook()
        ws = wb.worksheets[0]
        ws.name = "Sheet1"
        ws.cells.get("A1").put_value("Sample")
        wb.save(str(src))
    return src


def run() -> None:
    data_dir = get_data_dir()
    os.makedirs(data_dir, exist_ok=True)

    source_file = _ensure_source_workbook(data_dir)

    # Open the workbook.
    book = cells.Workbook(str(source_file))
    sheet = book.worksheets[0]

    # Define image/print options.
    img_options = cells.rendering.ImageOrPrintOptions()
    img_options.image_type = cells.drawing.ImageType.JPEG
    img_options.one_page_per_sheet = True

    # Render the sheet to an image.
    sheet_render = cells.rendering.SheetRender(sheet, img_options)
    # bitmap = sheet_render.to_image(0)

    # Save the image.
    output_path = data_dir / "SheetImage.out.jpg"
    sheet_render.to_image(0,str(output_path))

    print("Conversion to Image(s) completed.")


if __name__ == "__main__":
    run()
