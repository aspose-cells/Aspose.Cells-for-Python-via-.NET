import os
from datetime import datetime
import aspose.cells as cells

def get_output_directory():
    return os.path.abspath(os.path.join(".", "..", "..", "Data", "02_OutputDirectory"))

def run_working_with_content_type_properties():
    output_dir = get_output_directory()
    os.makedirs(output_dir, exist_ok=True)

    workbook = cells.Workbook(cells.FileFormatType.XLSX)

    index = workbook.content_type_properties.add("MK31", "Simple Data")
    workbook.content_type_properties[index].is_nillable = False

    index = workbook.content_type_properties.add(
        "MK32", datetime.now().strftime("%Y-%m-%dT%H:%M:%S"), "DateTime"
    )
    workbook.content_type_properties[index].is_nillable = True

    output_path = os.path.join(output_dir, "WorkingWithContentTypeProperties_out.xlsx")
    workbook.save(output_path)

if __name__ == "__main__":
    run_working_with_content_type_properties()
