import os
from aspose.cells.utility import JsonLayoutOptions,JsonUtility
from pathlib import Path

def get_source_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "01_SourceDirectory"

def get_output_directory():
    return Path(__file__).parent / ".." / ".." / "Data" / "02_OutputDirectory"

def convert_json_to_csv():
    source_dir = get_source_directory()
    output_dir = get_output_directory()
    
    # Read JSON file
    json_file_path = source_dir / "SampleJson.json"
    str_json = json_file_path.read_text()
    
    # Create empty workbook
    workbook = Workbook()
    
    # Get Cells
    cells = workbook.worksheets[0].cells

    importOptions = JsonLayoutOptions()
    importOptions.convert_numeric_or_date = True
    importOptions.array_as_table  = True
    importOptions.ignore_array_title = True
    importOptions.ignore_object_title  = True
    JsonUtility.import_data(str_json, cells, 0, 0, importOptions)
    
    # Save Workbook
    output_file_path = output_dir / "SampleJson_out.csv"
    workbook.save(str(output_file_path))

if __name__ == "__main__":
    from aspose.cells import Workbook
    convert_json_to_csv()