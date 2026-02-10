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
        / "ConfigureLinktoContentDocumentProperty"
    )


def run():
    data_dir = get_data_dir()
    workbook = cells.Workbook(str(data_dir / "sample-document-properties.xlsx"))

    # Access the custom document properties collection from the workbook
    custom_properties = workbook.custom_document_properties
    custom_properties.add_link_to_content("Owner", "MyRange")

    # Retrieve the property by name
    custom_property1 = custom_properties.get("Owner")
    is_linked_to_content = custom_property1.is_linked_to_content
    source = custom_property1.source

    workbook.save(str(data_dir / "out_sample-document-properties.xlsx"))


if __name__ == "__main__":
    run()