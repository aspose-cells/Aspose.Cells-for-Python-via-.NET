import os
from aspose.cells import Workbook, WorkbookDesigner

def get_data_dir():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Data", "SmartMarkers/UsingHTMLProperty")

def get_output_directory():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "Data", "02_OutputDirectory")

def run():
    data_dir = get_data_dir()
    workbook = Workbook()
    designer = WorkbookDesigner()
    designer.workbook = workbook
    worksheet = workbook.worksheets[0]
    worksheet.cells.get("A1").put_value("=$VariableArray(HTML)")
    designer.set_data_source("VariableArray", ["Hello <b>World</b>", "Arabic", "Hindi", "Urdu", "French"])
    designer.process()
    output_path = os.path.join(get_output_directory(), "output.xls")
    workbook.save(output_path)

if __name__ == "__main__":
    run()