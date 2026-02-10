import os
from pathlib import Path
import aspose.cells as cells

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / ".." / "Data" / "Files/Utility/AccessingValueOfDocumentProperties"

# Path to the Excel file
data_dir = get_data_dir()
excel_path = data_dir / "sample-document-properties.xlsx"

# Load the workbook
workbook = cells.Workbook(str(excel_path))

# Retrieve all custom document properties
custom_properties = workbook.worksheets.custom_document_properties

# Access the first custom property
custom_property1 = custom_properties[0]
object_value = custom_property1.value

# Access the second custom property and handle its type
custom_property2 = custom_properties[1]
if custom_property2.type == cells.properties.PropertyType.STRING:
    value = str(custom_property2.value)
    print(f"{custom_property2.name} : {value}")