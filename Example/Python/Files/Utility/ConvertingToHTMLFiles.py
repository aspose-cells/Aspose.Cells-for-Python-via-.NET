from pathlib import Path
import os
import aspose.cells as cells


def get_data_dir() -> Path:
    # Adjust the relative path to match the location of the example data
    data_dir = Path(__file__).resolve().parents[2] / "Data" / "Files" / "Utility" / "ConvertingToHTMLFiles"
    if not os.path.isdir(data_dir):
        os.makedirs(data_dir, exist_ok=True)
    return data_dir


def run() -> None:
    data_dir = get_data_dir()
    file_path = data_dir / "sample.xlsx"

    # If the sample workbook does not exist, create a minimal one
    if not file_path.is_file():
        wb = cells.Workbook()
        ws = wb.worksheets[0]
        ws.cells.get("A1").put_value("Hello Aspose!")
        wb.save(str(file_path), cells.SaveFormat.XLSX)

    workbook = cells.Workbook(str(file_path))
    output_path = data_dir / "ConvertingToHTMLFiles_out.html"
    workbook.save(str(output_path), cells.SaveFormat.HTML)


if __name__ == "__main__":
    run()