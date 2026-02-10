import os
from pathlib import Path
import aspose.cells as cells


def get_data_dir() -> Path:
    return (
        Path(__file__).parents[3]
        / "Data"
        / "Files"
        / "Utility"
        / "SettingImagePrefrencesforHTML"
    )


def run() -> None:
    data_dir = get_data_dir()
    os.makedirs(data_dir, exist_ok=True)

    file_path = data_dir / "Book1.xlsx"
    if not file_path.is_file():
        wb = cells.Workbook()
        ws = wb.worksheets[0]
        ws.cells.get("A1").put_value("Sample")
        wb.save(str(file_path))

    workbook = cells.Workbook(str(file_path))

    save_options = cells.HtmlSaveOptions(cells.SaveFormat.HTML)
    save_options.image_options.image_type = cells.drawing.ImageType.PNG

    output_path = data_dir / "output.html"
    workbook.save(str(output_path), save_options)


if __name__ == "__main__":
    run()
