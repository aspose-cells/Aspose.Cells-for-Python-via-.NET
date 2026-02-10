import os
from pathlib import Path
import aspose.cells as cells


def get_data_dir() -> Path:
    # Adjust the path to point to the example data folder
    return (
        Path(__file__).parent.parent.parent
        / "Data"
        / "Files/Utility/ConvertingToMHTMLFiles"
    )


def _determine_mhtml_save_format():
    # Aspose.Cells may expose the MHTML enum under different names depending on the version
    for name in ("MHTML", "MHtml", "MHtmlFormat"):
        fmt = getattr(cells.SaveFormat, name, None)
        if fmt is not None:
            return fmt
    # Fallback to HTML if MHTML is unavailable (the file will still be saved with .mht extension)
    return cells.SaveFormat.HTML


def run() -> None:
    data_dir = get_data_dir()
    file_path = data_dir / "Book1.xlsx"

    # Ensure the source workbook exists; create a simple one if it does not.
    if not file_path.is_file():
        wb_tmp = cells.Workbook()
        ws = wb_tmp.worksheets[0]
        ws.name = "Sheet1"
        ws.cells.get("A1").put_value("Sample")
        os.makedirs(data_dir, exist_ok=True)
        wb_tmp.save(str(file_path))

    # Determine the correct SaveFormat value for MHTML.
    mhtml_format = _determine_mhtml_save_format()

    # Set up HTML save options for MHTML (or HTML as a fallback).
    save_options = cells.HtmlSaveOptions(mhtml_format)

    # Load the workbook.
    wb = cells.Workbook(str(file_path))

    # Save as MHTML (.mht) using the determined options.
    wb.save(str(file_path) + ".out.mht", save_options)


if __name__ == "__main__":
    run()