import os
from aspose.cells import WorkbookDesigner
from pathlib import Path

def get_data_dir():
    return Path(__file__).parent / ".." / ".." / "Data" / "SmartMarkers/UsingVariableArray"

def run():
    # ExStart:1
    # The path to the documents directory.
    data_dir = get_data_dir()

    # Instantiate a new Workbook designer.
    report = WorkbookDesigner()

    # Get the first worksheet of the workbook.
    w = report.workbook.worksheets[0]

    # Set the Variable Array marker to a cell.
    # You may also place this Smart Marker into a template file manually in Ms Excel and then open this file via Workbook.
    w.cells.get("A1").put_value("&=$VariableArray")

    # Set the DataSource for the marker(s).
    report.set_data_source("VariableArray", ["English", "Arabic", "Hindi", "Urdu", "French"])

    # Process the markers.
    report.process(False)

    # Save the Excel file.
    output_path = os.path.join(data_dir, "output.xlsx")
    report.workbook.save(output_path)
    # ExEnd:1

if __name__ == "__main__":
    run()