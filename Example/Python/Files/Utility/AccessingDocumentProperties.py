import aspose.cells as cells
from pathlib import Path

def get_data_dir():
    return (
        Path(__file__).parent
        / ".."
        / ".."
        / ".."
        / "Data"
        / "Files"
        / "Utility"
        / "AccessingDocumentProperties"
    ).resolve()

def run():
    data_dir = get_data_dir()
    workbook_path = data_dir / "sample-document-properties.xlsx"
    workbook = cells.Workbook(str(workbook_path))

    # Custom document properties collection
    custom_properties = workbook.custom_document_properties

    # Access by name
    custom_property1 = next(
        (prop for prop in custom_properties if prop.name == "ContentTypeId"), None
    )
    if custom_property1:
        print(f"{custom_property1.name} {custom_property1.value}")

    # Access by index
    if len(custom_properties) > 0:
        custom_property2 = custom_properties[0]
        print(f"{custom_property2.name} {custom_property2.value}")

if __name__ == "__main__":
    run()
