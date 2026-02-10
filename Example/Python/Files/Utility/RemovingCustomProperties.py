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
        / "RemovingCustomProperties"
    )


def run():
    data_dir = get_data_dir()
    workbook = cells.Workbook(str(data_dir / "sample-document-properties.xlsx"))

    custom_properties = workbook.custom_document_properties
    prop = custom_properties.get("Publisher")
    if prop is not None:
        custom_properties.remove(prop)

    workbook.save(str(data_dir / "out_sample-document-properties.xlsx"))


if __name__ == "__main__":
    run()
