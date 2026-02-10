import os
from pathlib import Path
import aspose.cells as cells


def get_data_dir() -> Path:
    return (
        Path(__file__).parent
        / ".."
        / ".."
        / ".."
        / "Data"
        / "Files"
        / "Utility"
        / "AdvancedConversiontoPdf"
    ).resolve()


def main() -> None:
    data_dir = get_data_dir()
    os.makedirs(str(data_dir), exist_ok=True)

    workbook = cells.Workbook()
    workbook.worksheets[0].cells.get(0, 0).put_value("Testing PDF/A")

    pdf_save_options = cells.PdfSaveOptions()
    pdf_save_options.compliance = cells.rendering.PdfCompliance.PDF_A1B

    output_path = os.path.join(str(data_dir), "output.pdf")
    workbook.save(output_path, pdf_save_options)


if __name__ == "__main__":
    main()
