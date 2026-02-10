import os
from pathlib import Path
import aspose.cells as cells


def get_data_dir() -> Path:
    """
    Locate the directory that contains the sample Excel file.
    Checks several common relative locations and returns the first one that exists.
    """
    base = Path(__file__).resolve()
    candidates = [
        base.parent.parent.parent / "Data" / "Files" / "Utility" / "AddingDocumentProperties",
        base.parent.parent / "Data" / "Files" / "Utility" / "AddingDocumentProperties",
        base.parent / "Data" / "Files" / "Utility" / "AddingDocumentProperties",
        Path("Data") / "Files" / "Utility" / "AddingDocumentProperties",
    ]
    for p in candidates:
        if p.is_dir():
            return p
    # Fallback: use the directory of this script
    return base.parent


def run() -> None:
    data_dir = get_data_dir()
    input_path = data_dir / "sample-document-properties.xlsx"
    output_path = data_dir / "out_sample-document-properties.xlsx"

    # Ensure the output directory exists
    os.makedirs(output_path.parent, exist_ok=True)

    if input_path.is_file():
        workbook = cells.Workbook(str(input_path))
    else:
        # If the sample file is missing, start with a new workbook
        workbook = cells.Workbook()

    # Access the custom document properties collection and add a new property
    custom_props = workbook.custom_document_properties
    custom_props.add("Publisher", "Aspose")

    workbook.save(str(output_path))


if __name__ == "__main__":
    run()