import os
import io
from pathlib import Path
import aspose.cells as cells


def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"


def run_access_and_modify_label_of_ole_object():
    source_dir = get_source_directory()
    input_file = os.path.join(source_dir, "sampleAccessAndModifyLabelOfOleObject.xlsx")

    # Load the sample Excel file
    wb = cells.Workbook(input_file)

    # Access first worksheet
    ws = wb.worksheets[0]

    # Access first Ole Object
    ole_object = ws.ole_objects[0]

    # Display the Label of the Ole Object
    print("Ole Object Label - Before: " + ole_object.label)

    # Modify the Label of the Ole Object
    ole_object.label = "Aspose APIs"

    # Save workbook to memory stream
    ms = io.BytesIO()
    wb.save(ms, cells.SaveFormat.XLSX)

    # Set the workbook reference to null
    wb = None

    # Load workbook from memory stream
    ms.seek(0)
    wb = cells.Workbook(ms)

    # Access first worksheet
    ws = wb.worksheets[0]

    # Access first Ole Object
    ole_object = ws.ole_objects[0]

    # Display the Label of the Ole Object that has been modified earlier
    print("Ole Object Label - After: " + ole_object.label)

    print("AccessAndModifyLabelOfOleObject executed successfully.")


if __name__ == "__main__":
    run_access_and_modify_label_of_ole_object()